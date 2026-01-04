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

func processIfStmt(expr *ast.IfStmt) AnalysisResult {
	mergedResult := AnalysisResult{
		AccessedVars: map[string]bool{},
		ModifiedVars: map[string]bool{},
		ChildResults: []*AnalysisResult{},
		XMLString:    "", // Initialize XMLString
	}
	condString := ""
	elseString := ""
	condResult := walkNode(expr.Cond)
	condString = condResult.XMLString
	if expr.Else != nil {
		elseResult := walkNode(expr.Else)
		mergedResult.AccessedVars = mergeMaps(mergedResult.AccessedVars, elseResult.AccessedVars)
		mergedResult.ModifiedVars = mergeMaps(mergedResult.ModifiedVars, elseResult.ModifiedVars)
		elseString = fmt.Sprintf("<else>%s</else>", elseResult.XMLString)

	}
	bodyResult := walkNode(expr.Body)
	bodyString := bodyResult.XMLString
	mergedResult.AccessedVars = mergeMaps(mergedResult.AccessedVars, bodyResult.AccessedVars)
	mergedResult.ModifiedVars = mergeMaps(mergedResult.ModifiedVars, bodyResult.ModifiedVars)
	mergedResult.XMLString += fmt.Sprintf("<cond>%s</cond>%s<body>%s</body>", condString, elseString, bodyString)
	return mergedResult
}

// AnalysisResult holds the XML string and variable information.
type AnalysisResult struct {
	XMLString    string
	AccessedVars map[string]bool
	ModifiedVars map[string]bool
	ChildResults []*AnalysisResult // For hierarchical structures like blocks
}

func mergeMaps(maps ...map[string]bool) map[string]bool {
	mergedMap := map[string]bool{}
	for _, m := range maps {
		for k, v := range m {
			mergedMap[k] = v
		}
	}
	return mergedMap
}

func mergeResults(results ...*AnalysisResult) *AnalysisResult {
	mergedResult := &AnalysisResult{
		AccessedVars: map[string]bool{},
		ModifiedVars: map[string]bool{},
		ChildResults: []*AnalysisResult{},
		XMLString:    "", // Initialize XMLString
	}

	for _, result := range results {
		if result == nil {
			continue // Skip nil results
		}
		mergedResult.XMLString += result.XMLString
		mergedResult.AccessedVars = mergeMaps(mergedResult.AccessedVars, result.AccessedVars)
		mergedResult.ModifiedVars = mergeMaps(mergedResult.ModifiedVars, result.ModifiedVars)
		mergedResult.ChildResults = append(mergedResult.ChildResults, result.ChildResults...) // Append child results
	}

	return mergedResult
}

func walkNode(f ast.Node) *AnalysisResult {
	return processNode(f)
}

func processNode(n ast.Node) *AnalysisResult {
	result := &AnalysisResult{
		AccessedVars: map[string]bool{},
		ModifiedVars: map[string]bool{},
		ChildResults: []*AnalysisResult{},
	}

	nodeType := fmt.Sprintf("%T", n)
	if nodeType != "<nil>" {
		nodeType = strings.TrimPrefix(nodeType, "*ast.")
		result.XMLString += fmt.Sprintf("<%s>\n", nodeType)
	} else {
		return result // Return empty result, not an empty string
	}

	switch x := n.(type) {

	case *ast.IfStmt:
		ifStmtResult := processIfStmt(x)
		result.XMLString += fmt.Sprintf("%s\n", ifStmtResult.XMLString)
		result.AccessedVars = mergeMaps(result.AccessedVars, ifStmtResult.AccessedVars)
		result.ModifiedVars = mergeMaps(result.ModifiedVars, ifStmtResult.ModifiedVars)

	case *ast.File:
		fmt.Printf("File ends on block %d\n", int(n.End()))
		nameResult := walkNode(x.Name)
		result = mergeResults(result, nameResult)

		for _, decl := range x.Decls {
			declResult := walkNode(decl)
			result = mergeResults(result, declResult)
		}

	case *ast.BlockStmt:
		fmt.Println("------Entering Block------")
		for _, stmt := range x.List {
			stmtResult := walkNode(stmt)
			result = mergeResults(result, stmtResult)
		}
		fmt.Println("------Exiting Block-------")
		for k, _ := range result.AccessedVars {
			fmt.Printf("Accessed: %s\n", k)
		}
		for k, _ := range result.ModifiedVars {
			fmt.Printf("Modified: %s\n", k)
		}

	case *ast.Ident:
		result.XMLString += fmt.Sprintf("<name>%s</name>\n", x.Name)
		result.AccessedVars[x.Name] = true

	case *ast.FuncDecl:
		nameResult := walkNode(x.Name)
		result = mergeResults(result, nameResult)
		result.AccessedVars[x.Name.Name] = true

		if x.Body != nil {
			bodyResult := walkNode(x.Body)
			result = mergeResults(result, bodyResult)
		}
		if x.Type.Results != nil {
			for _, res := range x.Type.Results.List {
				fmt.Println("Function:", x.Name.Name, "Return Type:", res.Type)
			}
		}

	case *ast.CallExpr:
		result.XMLString += "<args>"
		for _, arg := range x.Args {
			argResult := walkNode(arg)
			result.XMLString += fmt.Sprintf("<arg>%s</arg>", argResult.XMLString)
			result.AccessedVars = mergeMaps(result.AccessedVars, argResult.AccessedVars)
		}
		result.XMLString += "</args>"

		funResult := walkNode(x.Fun)
		result.XMLString += fmt.Sprintf("<fun>%s</fun>", funResult.XMLString)
		//result.AccessedVars = mergeMaps(result.AccessedVars, funResult.AccessedVars)

	case *ast.AssignStmt:
		result.XMLString += fmt.Sprintf("<token>%s</token>\n", x.Tok)
		result.XMLString += "<LhsArray>\n"
		for i, lhs := range x.Lhs {
			lhsResult := walkNode(lhs)
			result.XMLString += fmt.Sprintf("<Lhs id=\"%d\">%s</Lhs>\n", i, lhsResult.XMLString)
			result.ModifiedVars = mergeMaps(result.ModifiedVars, lhsResult.AccessedVars) // LHS is being modified
		}
		result.XMLString += "</LhsArray>\n"
		result.XMLString += "<RhsArray>\n"
		for i, rhs := range x.Rhs {
			rhsResult := walkNode(rhs)
			result.XMLString += fmt.Sprintf("<Rhs id=\"%d\">%s</Rhs>\n", i, rhsResult.XMLString)
			result.AccessedVars = mergeMaps(result.AccessedVars, rhsResult.AccessedVars) // RHS is being accessed
		}
		result.XMLString += "</RhsArray>\n"
		fmt.Println("AssignStmt")
		for k, _ := range result.AccessedVars {
			fmt.Printf("Accessed: %s\n", k)
		}
		for k, _ := range result.ModifiedVars {
			fmt.Printf("Modified: %s\n", k)
		}

	case *ast.SelectorExpr:
		fmt.Printf("Selector Expr: %s, %s\n", x.X, x.Sel)
		xResult := walkNode(x.X)
		result.XMLString += fmt.Sprintf("<x>%s</x>", xResult.XMLString)
		//result.AccessedVars = mergeMaps(result.AccessedVars, xResult.AccessedVars)
		result.XMLString += fmt.Sprintf("<sel>%s</sel>", x.Sel.Name)
		//result.AccessedVars[x.Sel.Name] = true

	case *ast.ExprStmt:
		exprResult := walkNode(x.X)
		result = mergeResults(result, exprResult)

	case *ast.BasicLit:
		result.XMLString += processBasicLit(*x)

	case *ast.CompositeLit:
		typeResult := walkNode(x.Type)
		result.XMLString += fmt.Sprintf("<type>%s</type>", typeResult.XMLString)
		result.AccessedVars = mergeMaps(result.AccessedVars, typeResult.AccessedVars)

		result.XMLString += "<elts>"
		for i, elt := range x.Elts {
			eltResult := walkNode(elt)
			result.XMLString += fmt.Sprintf("<elt id=\"%d\">%s</elt>", i, eltResult.XMLString)
			result.AccessedVars = mergeMaps(result.AccessedVars, eltResult.AccessedVars)
		}
		result.XMLString += "</elts>"

	case *ast.IndexExpr:
		indexResult := walkNode(x.Index)
		xResult := walkNode(x.X)
		result.XMLString += fmt.Sprintf("<index>%s</index><x>%s</x>", indexResult.XMLString, xResult.XMLString)
		result.AccessedVars = mergeMaps(result.AccessedVars, indexResult.AccessedVars)
		result.AccessedVars = mergeMaps(result.AccessedVars, xResult.AccessedVars)

	case *ast.DeclStmt:
		declResult := walkNode(x.Decl)
		result = mergeResults(result, declResult)

	case *ast.ArrayType:
		if x.Len != nil {
			lenResult := walkNode(x.Len)
			result.XMLString += fmt.Sprintf("<len>%s</len>", lenResult.XMLString)
			result.AccessedVars = mergeMaps(result.AccessedVars, lenResult.AccessedVars)
		}
		if x.Elt != nil {
			eltResult := walkNode(x.Elt)
			result.XMLString += fmt.Sprintf("<type>%s</type>", eltResult.XMLString)
			result.AccessedVars = mergeMaps(result.AccessedVars, eltResult.AccessedVars)
		}

	case *ast.ValueSpec:
		if x.Type != nil {
			typeResult := walkNode(x.Type)
			result.XMLString += fmt.Sprintf("<type>%s</type>\n", typeResult.XMLString)
			result.AccessedVars = mergeMaps(result.AccessedVars, typeResult.AccessedVars)
		} else {
			result.XMLString += "<type>nil</type>\n"
		}
		result.XMLString += "<names>\n"
		for _, name := range x.Names {
			nameResult := walkNode(name)
			result = mergeResults(result, nameResult)
		}
		result.XMLString += "</names>\n"
		result.XMLString += "<values>\n"
		for _, value := range x.Values {
			valueResult := walkNode(value)
			result.XMLString += "<value>\n"
			result.XMLString += valueResult.XMLString
			result.AccessedVars = mergeMaps(result.AccessedVars, valueResult.AccessedVars)
			result.XMLString += "</value>\n"
		}
		result.XMLString += "</values>\n"

	case *ast.GenDecl:
		fmt.Println("---- gen decl")
		for _, spec := range x.Specs {
			specResult := walkNode(spec)
			result = mergeResults(result, specResult)
		}
		for _, spec := range x.Specs {
			switch spec := spec.(type) {
			case *ast.ImportSpec:
				fmt.Println("Import", spec.Path.Value)
			case *ast.TypeSpec:
				fmt.Println("Type", spec.Name.String())
			case *ast.ValueSpec:
				for _, id := range spec.Names {
					fmt.Printf("CONST %s\n", id.Name)
				}
			default:
				fmt.Printf("Unknown token type: %s\n", x.Tok)
			}
		}

	case *ast.CaseClause:
		result.XMLString += "<cases>"
		for _, c := range x.List {
			cResult := walkNode(c)
			result.XMLString += fmt.Sprintf("<case>%s</case>", cResult.XMLString)
			result.AccessedVars = mergeMaps(result.AccessedVars, cResult.AccessedVars)
		}
		result.XMLString += "</cases>"
		result.XMLString += "<body>"
		for _, b := range x.Body {
			bResult := walkNode(b)
			result = mergeResults(result, bResult)
		}
		result.XMLString += "</body>"

	case *ast.BinaryExpr:
		xResult := walkNode(x.X)
		yResult := walkNode(x.Y)
		result.XMLString += fmt.Sprintf("<op>%s</op><x>%s</x><y>%s</y>", xmlEscape(x.Op.String()), xResult.XMLString, yResult.XMLString)
		result.AccessedVars = mergeMaps(result.AccessedVars, xResult.AccessedVars)
		result.AccessedVars = mergeMaps(result.AccessedVars, yResult.AccessedVars)

	case *ast.SwitchStmt:
		tagResult := walkNode(x.Tag)
		bodyResult := walkNode(x.Body)
		result.XMLString += fmt.Sprintf("<tag>%s</tag><body>%s</body>", tagResult.XMLString, bodyResult.XMLString)
		result.AccessedVars = mergeMaps(result.AccessedVars, tagResult.AccessedVars)
		result.ModifiedVars = mergeMaps(result.ModifiedVars, bodyResult.ModifiedVars)

	case *ast.ImportSpec:
		pathResult := walkNode(x.Path)
		result.XMLString += pathResult.XMLString
		result.AccessedVars = mergeMaps(result.AccessedVars, pathResult.AccessedVars)

	case *ast.ForStmt:
		initResult := walkNode(x.Init)
		if initResult.XMLString != "" {
			result.XMLString += fmt.Sprintf("<init>%s</init>", initResult.XMLString)
			result.AccessedVars = mergeMaps(result.AccessedVars, initResult.AccessedVars)
			result.ModifiedVars = mergeMaps(result.ModifiedVars, initResult.ModifiedVars)
		}
		condResult := walkNode(x.Cond)
		if condResult.XMLString != "" {
			result.XMLString += fmt.Sprintf("<cond>%s</cond>", condResult.XMLString)
			result.AccessedVars = mergeMaps(result.AccessedVars, condResult.AccessedVars)
		}
		postResult := walkNode(x.Post)
		if postResult.XMLString != "" {
			result.XMLString += fmt.Sprintf("<post>%s</post>", postResult.XMLString)
			result.AccessedVars = mergeMaps(result.AccessedVars, postResult.AccessedVars)
			result.ModifiedVars = mergeMaps(result.ModifiedVars, postResult.ModifiedVars)
		}
		bodyResult := walkNode(x.Body)
		if bodyResult.XMLString != "" {
			result.XMLString += fmt.Sprintf("<body>%s</body>", bodyResult.XMLString)
			result.AccessedVars = mergeMaps(result.AccessedVars, bodyResult.AccessedVars)
			result.ModifiedVars = mergeMaps(result.ModifiedVars, bodyResult.ModifiedVars)
			result.ChildResults = append(result.ChildResults, bodyResult)
			if len(bodyResult.ModifiedVars) > 0 {
				result.XMLString += "<shiftRegisters>"
				for k, _ := range bodyResult.ModifiedVars {
					result.XMLString += fmt.Sprintf("<shiftRegister>%s</shiftRegister>", k)
				}
				result.XMLString += "</shiftRegisters>"
			}
		}

	default:
		nodeType := fmt.Sprintf("%T", n)
		fmt.Println(nodeType)
		if nodeType != "<nil>" {
			//retString += fmt.Sprintf("Node type: %s\n", nodeType)
		}

	}
	result.XMLString += fmt.Sprintf("</%s>\n", nodeType)
	return result
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

	analysisResult := walkNode(f)

	w.WriteString(analysisResult.XMLString)
	w.Flush()

	for k, _ := range analysisResult.AccessedVars {
		fmt.Printf("Accessed: %s\n", k)
	}
	for k, _ := range analysisResult.ModifiedVars {
		fmt.Printf("Modified: %s\n", k)
	}

	//fmt.Printf("final depth: %d\n", depthCounter)

}
