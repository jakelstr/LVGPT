package main

import (
	"bufio"
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
	"os"
	"strings"
)

var exitBlockLines []int

var depthCounter int

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
		return fmt.Sprintf("<BinaryExpr><op>%s</op><left>%s</left><right>%s</right></BinaryExpr>", binaryExpr.Op, findBottomBinaryExpr(binaryExpr.X), findBottomBinaryExpr(binaryExpr.Y))
	}
	return fmt.Sprintf("%s", expr)
}

/* func processBinaryExpr(expr ast.BinaryExpr) string{
	var left string = findBottomBinaryExpr(expr.X)
	var right string = findBottomBinaryExpr(expr.Y)
	return fmt.Sprintf("<binary<op>%s</op>\n<left>%s</left>\n<right>%s</right>\n", x.Op, left, right)
} */

func processCallExpr(expr ast.Expr) string {
	if selectorExpr, ok := expr.(*ast.SelectorExpr); ok {
		return fmt.Sprintf("<SelectorExpr>%s</SelectorExpr>", selectorExpr.Sel.Name)
	}
	return fmt.Sprintf("%s", expr)
}

func main() {
	visited := make(map[ast.Node]bool)

	depthCounter := -1
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

	openTags := make([]string, 0)

	w := bufio.NewWriter(file)

	ast.Inspect(f, func(n ast.Node) bool {
		nodeType := fmt.Sprintf("%T", n)
		if nodeType != "<nil>" {
			nodeType = strings.TrimPrefix(nodeType, "*ast.")
			depthCounter++
			//fmt.Printf("<%s>\n", nodeType)
			w.WriteString(fmt.Sprintf("<%s>\n", nodeType))
			w.Flush()
			openTags = append(openTags, nodeType)
		} else {
			depthCounter--
			lastTag := openTags[len(openTags)-1]
			openTags = openTags[:len(openTags)-1]
			//fmt.Printf("</%s>\n", lastTag)
			w.WriteString(fmt.Sprintf("</%s>\n", lastTag))
			w.Flush()
		}
		if len(exitBlockLines) > 0 {
			if exitBlockLines[len(exitBlockLines)-1] > depthCounter {
				exitBlockLines[len(exitBlockLines)-1] = exitBlockLines[len(exitBlockLines)-1] // Copy lexitBlockLinesst element to index i.
				exitBlockLines[len(exitBlockLines)-1] = 0                                     // ErexitBlockLinesse lexitBlockLinesst element (write zero vexitBlockLineslue).
				exitBlockLines = exitBlockLines[:len(exitBlockLines)-1]                       // Truncate slice.
				//fmt.Printf("Exited block...\n\n")
			}
		}
		switch x := n.(type) {

		//case *ast.BlockStmt:
		//	fmt.Printf("Block Statement, list size: %d\n", len(x.List))
		/*for _, statement := range x.List {
			switch statement := statement.(type) {
			case *ast.DeclStmt:
				decl := statement.Decl.(*ast.GenDecl)
				//decl.Specs
			}
		}*/
		case *ast.IfStmt:
			fmt.Printf("If Statement\n")
		case *ast.File:
			fmt.Printf("File ends on block %d\n", int(n.End()))

		case *ast.BlockStmt:
			fmt.Printf("Entering Block... At depth %d\n", depthCounter)
			exitBlockLines = append(exitBlockLines, depthCounter)
		case *ast.Ident:
			w.WriteString(fmt.Sprintf("<name>%s</name>\n", x.Name))
			w.Flush()

		case *ast.FuncDecl:
			if x.Type.Results != nil {
				for _, result := range x.Type.Results.List {
					fmt.Println("Function:", x.Name.Name, "Return Type:", result.Type)
				}
			} else {
				fmt.Println("Function:", x.Name.Name, "has no return values")
			}
		case *ast.CallExpr:
			funcName := x.Fun.(*ast.SelectorExpr).Sel.Name
			fmt.Println("Function call:", funcName)
			w.WriteString(fmt.Sprintf("<args>"))
			for _, arg := range x.Args {
				if basicLit, ok := arg.(*ast.BasicLit); ok {
					w.WriteString(fmt.Sprintf("<arg><BasicLit>%s</BasicLit></arg>", processBasicLit(*basicLit)))
				}
				if ident, ok := arg.(*ast.Ident); ok {
					w.WriteString(fmt.Sprintf("<arg><Ident><name>%s</name></Ident></arg>\n", ident.Name))
					w.Flush()
				}
			}
			w.WriteString(fmt.Sprintf("</args>"))
		case *ast.AssignStmt:
			fmt.Printf("AssignStmt: ")

			w.WriteString("<LhsArray>\n")
			for i, lhs := range x.Lhs {
				w.WriteString(fmt.Sprintf("<Lhs id=\"%d\">%s</Lhs>\n", i, lhs))
			}
			w.WriteString("</LhsArray>\n")
			w.WriteString("<RhsArray>\n")
			for i, rhs := range x.Rhs {
				if _, ok := rhs.(*ast.BasicLit); ok {
					basicLit := rhs.(*ast.BasicLit)
					w.WriteString(fmt.Sprintf("<Rhs id=\"%d\">\n<BasicLit>%s</BasicLit></Rhs>\n", i, processBasicLit(*basicLit)))
					//fmt.Printf("RHS: %s\n", processBasicLit(*basicLit))
				}
				if _, ok := rhs.(*ast.BinaryExpr); ok {
					binaryExpr := rhs.(*ast.BinaryExpr)
					visited[binaryExpr] = true
					w.WriteString(fmt.Sprintf("<Rhs id=\"%d\">%s</Rhs>\n", i, findBottomBinaryExpr((binaryExpr))))
					//fmt.Printf("RHS: %s\n", processBasicLit(*basicLit))
				}
			}
			w.WriteString("</RhsArray>\n")
			w.Flush()

		case *ast.SelectorExpr:
			fmt.Printf("Selector Expr: %s, %s\n", x.X, x.Sel)

		case *ast.ExprStmt:
			/*if _, ok := x.X.(*ast.CallExpr); ok {
				callExpr := x.X.(*ast.CallExpr)
				w.WriteString(fmt.Sprintf("<ExprStmt><CallExpr>%s</CallExpr></ExprStmt>\n", callExpr.Fun))
				w.Flush()
			}*/

		case *ast.BasicLit:
			w.WriteString(processBasicLit(*x))
			w.Flush()

		case *ast.DeclStmt:
			fmt.Printf("Decl statement %s\n", x.Decl)
		case *ast.ValueSpec:
			//fmt.Printf("Value Spec %s\n", x.Values)
			w.WriteString(fmt.Sprintf("<type>%s</type>\n", x.Type))
			w.WriteString(fmt.Sprintf("<names>\n"))
			for _, name := range x.Names {
				//visited[name] = true
				w.WriteString(fmt.Sprintf("<name>%s</name>\n", name.Name))
			}
			w.WriteString(fmt.Sprintf("</names>\n"))
			w.WriteString(fmt.Sprintf("<values>\n"))
			for _, value := range x.Values {
				w.WriteString(fmt.Sprintf("<value>\n"))
				if _, ok := value.(*ast.BinaryExpr); ok {
					visited[value] = true
					w.WriteString(findBottomBinaryExpr(value))
					//fmt.Printf("RHS: %s\n", processBasicLit(*basicLit))
				}
				if basicLit, ok := value.(*ast.BasicLit); ok {
					visited[value] = true
					w.WriteString(fmt.Sprintf("<BasicLit>%s</BasicLit>", processBasicLit(*basicLit)))
					//fmt.Printf("RHS: %s\n", processBasicLit(*basicLit))
				}
				w.WriteString(fmt.Sprintf("</value>\n"))
			}
			w.WriteString(fmt.Sprintf("</values>\n"))
			w.Flush()

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
		case *ast.BinaryExpr:
			//var left string = findBottomBinaryExpr(x.X)
			//var right string = findBottomBinaryExpr(x.Y)

			//w.WriteString(fmt.Sprintf("<op>%s</op>\n<left>%s</left>\n<right>%s</right>\n", x.Op, left, right))
			if !visited[x] {
				w.WriteString(findBottomBinaryExpr(x))
				w.Flush()
			}

		default:
			nodeType := fmt.Sprintf("%T", n)
			if nodeType != "<nil>" {
				fmt.Printf("Node type: %s\n", nodeType)
			}

		}
		return true
	})

	//fmt.Printf("final depth: %d\n", depthCounter)

}
