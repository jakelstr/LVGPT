package main

import (
	"bufio"
	"bytes"
	"encoding/xml"
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
	"os"
	"strings"

	"github.com/google/uuid"
)

var visited = make(map[uuid.UUID]ast.Node)

var variableLink = make(map[string][]string)

func xmlEscape(s string) string {
	var b bytes.Buffer
	xml.Escape(&b, []byte(s))
	return b.String()
}

func stripQuotes(s string) string {
	if len(s) >= 2 && s[0] == '"' && s[len(s)-1] == '"' {
		return s[1 : len(s)-1]
	}
	return s
}

func processBasicLit(node ast.BasicLit) string {
	kind := node.Kind
	value := node.Value
	return fmt.Sprintf("<kind>%s</kind>\n<value>%s</value>\n", kind, stripQuotes(value))
}

type CodeElement struct {
	Type string
	Name string
}

type CodePage struct {
	Elements []CodeElement
}

func findBottomBinaryExpr(expr ast.Expr) string {
	if binaryExpr, ok := expr.(*ast.BinaryExpr); ok {
		return fmt.Sprintf("<op>%s</op><left>%s</left><right>%s</right>", xmlEscape(fmt.Sprintf("%s", binaryExpr.Op)), walkNode(binaryExpr.X), walkNode(binaryExpr.Y))
	} else if basicLit, ok := expr.(*ast.BasicLit); ok {
		return fmt.Sprintf("<BasicLit>%s</BasicLit>", processBasicLit(*basicLit))
	}
	return fmt.Sprintf("%s", expr)
}

func processCallExpr(expr ast.Expr) string {
	if selectorExpr, ok := expr.(*ast.SelectorExpr); ok {
		return fmt.Sprintf("<SelectorExpr>%s</SelectorExpr>", selectorExpr.Sel.Name)
	}
	return fmt.Sprintf("%s", expr)
}

func processIfStmt(expr *ast.IfStmt) string {
	condString := ""
	elseString := ""
	condString = walkNode(expr.Cond)
	if expr.Else != nil {
		elseString = fmt.Sprintf("<else>%s</else>", walkNode(expr.Else))

	}
	bodyString := walkNode(expr.Body)
	return fmt.Sprintf("<cond>%s</cond>%s<body>%s</body>", condString, elseString, bodyString)
}

func walkNode(f ast.Node) string {
	retString := ""
	// ast.Inspect(f, func(n ast.Node) bool {
	// 	retString += processNode(n)
	// 	return true
	// })
	retString += processNode(f)
	// fmt.Println(retString)
	return retString
}

func processNode(n ast.Node) string {
	retString := ""
	nodeType := fmt.Sprintf("%T", n)
	if nodeType != "<nil>" {

		nodeType = strings.TrimPrefix(nodeType, "*ast.")
		retString += fmt.Sprintf("<%s>\n", nodeType)
	} else {
		return ""
	}

	switch x := n.(type) {

	case *ast.IfStmt:
		retString += fmt.Sprintf("%s\n", processIfStmt(x))

	case *ast.File:
		fmt.Printf("File ends on block %d\n", int(n.End()))
		retString += walkNode(x.Name)
		for _, decl := range x.Decls {
			retString += walkNode(decl)
		}

	case *ast.BlockStmt:
		fmt.Printf("Entering Block... ")
		//exitBlockLines = append(exitBlockLines, depthCounter)
		for _, stmt := range x.List {
			retString += walkNode(stmt)
		}
	case *ast.Ident:
		retString += fmt.Sprintf("<name>%s</name>\n", x.Name)

	case *ast.FuncDecl:
		retString += walkNode(x.Name)
		if x.Body != nil {
			retString += walkNode(x.Body)
		}
		if x.Type.Results != nil {
			for _, result := range x.Type.Results.List {
				fmt.Println("Function:", x.Name.Name, "Return Type:", result.Type)
			}
		}
	case *ast.CallExpr:
		//funcName := x.Fun.(*ast.SelectorExpr).Sel.Name
		//fmt.Println("Function call:", funcName)
		retString += fmt.Sprintf("<args>")
		for _, arg := range x.Args {
			retString += fmt.Sprintf("<arg>%s</arg>", walkNode(arg))
		}
		retString += fmt.Sprintf("</args>")
		retString += fmt.Sprintf("<fun>%s</fun>", walkNode(x.Fun))
	case *ast.AssignStmt:
		fmt.Printf("AssignStmt: ")
		retString += fmt.Sprintf("<token>%s</token>\n", x.Tok)
		retString += "<LhsArray>\n"
		for i, lhs := range x.Lhs {
			retString += fmt.Sprintf("<Lhs id=\"%d\">%s</Lhs>\n", i, walkNode(lhs))
		}
		retString += "</LhsArray>\n"
		retString += "<RhsArray>\n"
		for i, rhs := range x.Rhs {
			retString += fmt.Sprintf("<Rhs id=\"%d\">%s</Rhs>\n", i, walkNode(rhs))
		}
		retString += "</RhsArray>\n"

	case *ast.SelectorExpr:
		retString += fmt.Sprintf("<x>%s</x><sel>%s</sel>", x.X, x.Sel)
		fmt.Printf("Selector Expr: %s, %s\n", x.X, x.Sel)

	case *ast.ExprStmt:
		/*if _, ok := x.X.(*ast.CallExpr); ok {
			callExpr := x.X.(*ast.CallExpr)
			w.WriteString(fmt.Sprintf("<ExprStmt><CallExpr>%s</CallExpr></ExprStmt>\n", callExpr.Fun))

		}*/
		retString += walkNode(x.X)

	case *ast.BasicLit:
		retString += processBasicLit(*x)

	case *ast.CompositeLit:
		retString += fmt.Sprintf("<type>%s</type><elts>", walkNode(x.Type))
		for i, elt := range x.Elts {
			retString += fmt.Sprintf("<elt id=\"%d\">%s</elt>", i, walkNode(elt))
		}
		retString += "</elts>"
	case *ast.IndexExpr:
		retString += fmt.Sprintf("<index>%s</index><x>%s</x>", walkNode(x.Index), walkNode(x.X))

	case *ast.DeclStmt:
		// fmt.Printf("Decl statement %s\n", x.Decl)
		retString += walkNode(x.Decl)
		// for _, spec := range x.Decl.(*ast.GenDecl).Specs {
		// 	retString += walkNode(spec)
		// }
	case *ast.ArrayType:
		if x.Len != nil {
			retString += fmt.Sprintf("<len>%s</len>", walkNode(x.Len))
		}
		if x.Elt != nil {
			retString += fmt.Sprintf("<type>%s</type>", walkNode(x.Elt))
		}

	case *ast.ValueSpec:
		if x.Type != nil {
			retString += fmt.Sprintf("<type>%s</type>\n", walkNode(x.Type))
		} else {
			retString += fmt.Sprintf("<type>nil</type>\n")
		}
		retString += fmt.Sprintf("<names>\n")
		for _, name := range x.Names {
			//visited[name] = true
			retString += fmt.Sprint(walkNode(name))
		}
		retString += fmt.Sprintf("</names>\n")
		retString += fmt.Sprintf("<values>\n")
		for _, value := range x.Values {
			retString += fmt.Sprintf("<value>\n")
			retString += walkNode(value)
			retString += fmt.Sprintf("</value>\n")
		}
		retString += fmt.Sprintf("</values>\n")

	case *ast.GenDecl:

		fmt.Printf("---- gen decl\n")
		for _, spec := range x.Specs {
			retString += walkNode(spec)
		}
		for _, spec := range x.Specs {
			switch spec := spec.(type) {
			case *ast.ImportSpec:
				fmt.Println("Import", spec.Path.Value)
			case *ast.TypeSpec:
				fmt.Println("Type", spec.Name.String())
			case *ast.ValueSpec:
				for _, id := range spec.Names {
					fmt.Printf("Var %s", id.Name)
					//fmt.Printf("Var %s: %v", id.Name, id.Obj.Decl.(*ast.ValueSpec).Values[0].(*ast.BasicLit).Value)
				}
			default:
				fmt.Printf("Unknown token type: %s\n", x.Tok)
			}
		}

	case *ast.CaseClause:
		retString += fmt.Sprint("<cases>")
		for _, c := range x.List {
			retString += fmt.Sprintf("<case>%s</case>", walkNode(c))
		}
		retString += fmt.Sprint("</cases>")
		retString += fmt.Sprint("<body>")
		for _, b := range x.Body {
			retString += fmt.Sprintf("%s", walkNode(b))
		}
		retString += fmt.Sprint("</body>")

	case *ast.BinaryExpr:
		retString += findBottomBinaryExpr(x)

	case *ast.SwitchStmt:
		retString += fmt.Sprintf("<tag>%s</tag><body>%s</body>", walkNode(x.Tag), walkNode(x.Body))

	case *ast.ImportSpec:
		retString += walkNode(x.Path)

	case *ast.ForStmt:
		initString := walkNode(x.Init)
		if initString != "" {
			retString += fmt.Sprintf("<init>%s</init>", initString)
		}
		condString := walkNode(x.Cond)
		if condString != "" {
			retString += fmt.Sprintf("<cond>%s</cond>", condString)
		}
		postString := walkNode(x.Post)
		if postString != "" {
			retString += fmt.Sprintf("<post>%s</post>", postString)
		}
		bodyString := walkNode(x.Body)
		if bodyString != "" {
			retString += fmt.Sprintf("<body>%s</body>", bodyString)
		}

	default:
		nodeType := fmt.Sprintf("%T", n)
		fmt.Println(nodeType)
		if nodeType != "<nil>" {
			//retString += fmt.Sprintf("Node type: %s\n", nodeType)
		}

	}
	retString += fmt.Sprintf("</%s>\n", nodeType)
	return retString
}

func main() {

	fset := token.NewFileSet()
	f, err := parser.ParseFile(fset, "../python/codexout.go", nil, parser.AllErrors)
	if err != nil {
		panic(err)
	}

	file, err := os.Create("goast1_new.txt")
	if err != nil {
		fmt.Println("Error creating file:", err)
		return
	}
	defer file.Close()

	w := bufio.NewWriter(file)

	w.WriteString(walkNode(f))
	w.Flush()

	//fmt.Printf("final depth: %d\n", depthCounter)

}
