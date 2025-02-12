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
)

var exitBlockLines []int

var depthCounter int = -1

var openTags = make([]string, 0)

var visited = make(map[ast.Node]bool)

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
	visited[&node] = true
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
	ast.Inspect(f, func(n ast.Node) bool {
		retString += processNode(n)
		return true
	})
	fmt.Println(retString)
	return retString
}

func processNode(n ast.Node) string {
	retString := ""
	nodeType := fmt.Sprintf("%T", n)
	if nodeType != "<nil>" {

		nodeType = strings.TrimPrefix(nodeType, "*ast.")
		depthCounter++
		//fmt.Printf("<%s>\n", nodeType)
		if visited[n] {
			openTags = append(openTags, "SKIP")
			return ""
		} else {
			retString += fmt.Sprintf("<%s>\n", nodeType)
			openTags = append(openTags, nodeType)
		}
		visited[n] = true

	} else {
		if depthCounter > -1 {
			depthCounter--
			lastTag := openTags[len(openTags)-1]
			openTags = openTags[:len(openTags)-1]
			//fmt.Printf("</%s>\n", lastTag)
			if lastTag != "SKIP" {
				retString += fmt.Sprintf("</%s>\n", lastTag)
			}
		}

	}
	switch x := n.(type) {

	case *ast.IfStmt:
		retString += fmt.Sprintf("%s\n", processIfStmt(x))

	case *ast.File:
		fmt.Printf("File ends on block %d\n", int(n.End()))

	case *ast.BlockStmt:
		fmt.Printf("Entering Block... At depth %d\n", depthCounter)
		//exitBlockLines = append(exitBlockLines, depthCounter)
		for _, stmt := range x.List {
			retString += walkNode(stmt)
		}
	case *ast.Ident:
		retString += fmt.Sprintf("<name>%s</name>\n", x.Name)

	case *ast.FuncDecl:
		if x.Type.Results != nil {
			for _, result := range x.Type.Results.List {
				fmt.Println("Function:", x.Name.Name, "Return Type:", result.Type)
			}
		} else {
			fmt.Println("Function:", x.Name.Name, "has no return values")
		}
	case *ast.CallExpr:
		//funcName := x.Fun.(*ast.SelectorExpr).Sel.Name
		//fmt.Println("Function call:", funcName)
		retString += fmt.Sprintf("<args>")
		for _, arg := range x.Args {
			retString += fmt.Sprintf("<arg>%s</arg>", walkNode(arg))
		}
		retString += fmt.Sprintf("</args>")
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
			/* 			if _, ok := rhs.(*ast.BasicLit); ok {
			   				basicLit := rhs.(*ast.BasicLit)
			   				retString += fmt.Sprintf("<Rhs id=\"%d\">\n%s</Rhs>\n", i, walkNode(basicLit))
			   				//fmt.Printf("RHS: %s\n", processBasicLit(*basicLit))
			   			}
			   			if _, ok := rhs.(*ast.BinaryExpr); ok {
			   				binaryExpr := rhs.(*ast.BinaryExpr)
			   				visited[binaryExpr] = true
			   				retString += fmt.Sprintf("<Rhs id=\"%d\">%s</Rhs>\n", i, findBottomBinaryExpr((binaryExpr)))
			   				//fmt.Printf("RHS: %s\n", processBasicLit(*basicLit))
			   			} */
			retString += fmt.Sprintf("<Rhs id=\"%d\">%s</Rhs>\n", i, walkNode(rhs))
		}
		retString += "</RhsArray>\n"

	case *ast.SelectorExpr:
		retString += fmt.Sprintf("<x>%s</x><sel>%s</sel>", x.X, x.Sel)
		visited[x.X] = true
		visited[x.Sel] = true
		fmt.Printf("Selector Expr: %s, %s\n", x.X, x.Sel)

	case *ast.ExprStmt:
		/*if _, ok := x.X.(*ast.CallExpr); ok {
			callExpr := x.X.(*ast.CallExpr)
			w.WriteString(fmt.Sprintf("<ExprStmt><CallExpr>%s</CallExpr></ExprStmt>\n", callExpr.Fun))

		}*/

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
		fmt.Printf("Decl statement %s\n", x.Decl)
	case *ast.ArrayType:
		if x.Len != nil {
			retString += fmt.Sprintf("<len>%s</len>", walkNode(x.Len))
		}
		if x.Elt != nil {
			retString += fmt.Sprintf("<type>%s</type>", walkNode(x.Elt))
		}

	case *ast.ValueSpec:
		//fmt.Printf("Value Spec %s\n", x.Values)
		retString += fmt.Sprintf("<type>%s</type>\n", walkNode(x.Type))
		retString += fmt.Sprintf("<names>\n")
		for _, name := range x.Names {
			//visited[name] = true
			retString += fmt.Sprintf("<name>%s</name>\n", name.Name)
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

	default:
		nodeType := fmt.Sprintf("%T", n)
		if nodeType != "<nil>" {
			//retString += fmt.Sprintf("Node type: %s\n", nodeType)
		}

	}
	return retString
}

func main() {

	fset := token.NewFileSet()
	f, err := parser.ParseFile(fset, "../python/codexout.go", nil, parser.AllErrors)
	if err != nil {
		panic(err)
	}

	file, err := os.Create("goast1.txt")
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
