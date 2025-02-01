import xml.etree.ElementTree as ET
import uuid
from lvgptGraph import *

lvGraph = LVGraph()

def determineBinaryDictOpUniform(binaryDict):
    left = binaryDict["left"]
    right = binaryDict["right"]
    op = type(binaryDict["op"])
    uniform = True
    inputs = []
    if type(left) is dict:
        subUniform, subOp, subInputs = determineBinaryDictOpUniform(left)
        uniform = uniform and subUniform and subOp == op
        subInputs.extend(inputs)
        inputs = subInputs
    else:
        inputs.append(left)
    if type(right) is dict:
        subUniform, subOp, subInputs = determineBinaryDictOpUniform(right)
        uniform = uniform and subUniform and subOp == op
        subInputs.extend(inputs)
        inputs = subInputs
    else:
        inputs.append(right)
    return (uniform, op, inputs)

def convertBinaryDictToConcatStrings(binaryDict, blockLevel):
    uniform, op, binVars = determineBinaryDictOpUniform(binaryDict)
    if uniform and op is AddNode:
        lvGraph.deleteNode(binaryDict['op'].uuid)
        concatNode = ConcatenateStringsNode()
        lvGraph.addNode(concatNode)
        if len(binVars) > 2:
            for x in range(len(binVars) - 2):
                concatNode.addTerminal()
        binaryDict["op"] = concatNode
        stringTerms = concatNode.getStringTerms()
        for x in range(len(binVars)):
            varNode = lvGraph.getNodeByUUID(binVars[x])
            lvGraph.addTerminalEdge(varNode.getTerminal().uuid, stringTerms[x].uuid)
    
    return (binaryDict, "STRING")

def processBinaryExpr(node):
    returnDict = {}
    op = node.find("op").text
    if op == "+":
        returnDict["op"] = AddNode()
    elif op == "-":
        returnDict["op"] = SubtractNode()
    elif op == "*":
        returnDict["op"] = MultiplyNode()
    elif op == "/":
        returnDict["op"] = DivideNode()
    elif op == ">=":
        returnDict["op"] = GreaterOrEqualNode()
    left = node.find("left")
    right = node.find("right")
    if len(left) > 0:
        if left[0].tag == "BinaryExpr":
            returnDict["left"] = processBinaryExpr(left[0])
        if left[0].tag == "Ident":
            returnDict["left"] = left[0].find("name").text
    else:
        returnDict["left"] = left.text
    if len(right) > 0:
        if right[0].tag == "BinaryExpr":
            returnDict["right"] = processBinaryExpr(right[0])
        elif right[0].tag == "Ident":
            returnDict["right"] = right[0].find("name").text
        elif right[0].tag == "BasicLit":
            varType = right[0].find("kind").text
            val = right[0].find("value").text
            nodeName = "const"
            node = getConstantNodeByVarType(nodeName, varType)
            node.setValue(val)
            lvGraph.addNode(node)
            returnDict["right"] = nodeName
    else:
        returnDict["right"] = right.text
    return returnDict

def processBinaryDict(binaryDict):
    left = binaryDict["left"]
    right = binaryDict["right"]
    op = binaryDict["op"]
    opNodeName = op.name
    op.name = opNodeName
    lvGraph.addNode(op)
    outType = "int"
    leftOutType = "int"
    rightOutType = "int"
    opLeftTerm, opRightTerm, opOutputTerm = op.getTerms()
    if type(left) is dict:
        left, leftOutType = processBinaryDict(left)
        _, _, subOutput = left["op"].getTerms()
        lvGraph.addTerminalEdge(subOutput.uuid, opLeftTerm.uuid)
    else:
        left = lvGraph.getNodeByName(left)
        leftNode = lvGraph.getNodeByUUID(left)
        lvGraph.addTerminalEdge(leftNode.getTerminal().uuid, opLeftTerm.uuid)
        leftOutType = leftNode.varType
    if type(right) is dict:
        right, rightOutType = processBinaryDict(right)
        _, _, subOutput = right["op"].getTerms()
        lvGraph.addTerminalEdge(subOutput.uuid, opRightTerm.uuid)
    else:
        right = lvGraph.getNodeByName(right)
        rightNode = lvGraph.getNodeByUUID(right)
        lvGraph.addTerminalEdge(rightNode.getTerminal().uuid, opRightTerm.uuid)
        rightOutType = rightNode.varType
    if leftOutType.upper() == rightOutType.upper():
        outType = leftOutType.upper()
    else:
        #panic I guess idk
        pass
    binaryDict["left"] = left
    binaryDict["right"] = right
    return (binaryDict, outType)

def addBinaryNodeToLVGraph(binaryXMLNode, nodeName, createOutputNode=True):
    binExpDict = processBinaryExpr(binaryXMLNode)
    binExpDict, outType = processBinaryDict(binExpDict)
    if outType.upper() == "STRING":
        binExpDict, outType = convertBinaryDictToConcatStrings(binExpDict, 0)
    _, _, finalOutputTerm = binExpDict["op"].getTerms()
    retVal = finalOutputTerm.uuid
    if createOutputNode:
        retVal = nodeName
        varNode = getIndicatorNodeByVarType(nodeName, outType)
        lvGraph.addNode(varNode)
        lvGraph.addTerminalEdge(finalOutputTerm.uuid, varNode.getTerminal().uuid)
    return retVal

def getPrintExprFunction(callExprNode):
    selectorExpr = callExprNode.find("SelectorExpr")
    if selectorExpr is not None:
        xVal = selectorExpr.find("x").text
        selVal = selectorExpr.find("sel").text
        if xVal is not None and selVal is not None and xVal == "fmt":
            return selVal
    return None

def findPrintExpression(parentNode, x, sel):
    found = False
    exprNode = None
    exprStmt = parentNode.find("ExprStmt/CallExpr")
    if exprStmt is not None:
        selectorExpr = exprStmt.find("SelectorExpr")
        if selectorExpr is not None:
            xVal = selectorExpr.find("x").text
            selVal = selectorExpr.find("sel").text
            if x == xVal and sel == selVal:
                found = True
                exprNode = exprStmt
    return (found, exprNode)

def unaryPrintStmt(blockStmt):
    retVal = False
    retNode = None
    if len(blockStmt) == 1:
        found, node = findPrintExpression(blockStmt, "fmt", "Println")
        retVal = found
        retNode = node
    return retVal, retNode

def determineIfStatementRep(ifNode):
    ifUnaryPrint = False
    ifUnaryPrintNode = None
    elseUnaryPrint = False
    elseUnaryPrintNode = None
    bodyNode = ifNode.find("body")
    if bodyNode is not None:
        if bodyNode[0].tag == "BlockStmt":
            ifUnaryPrint, ifUnaryPrintNode = unaryPrintStmt(bodyNode[0])

    elseNode = ifNode.find("else")
    if elseNode is not None:
        if elseNode[0].tag == "BlockStmt":
            elseUnaryPrint, elseUnaryPrintNode = unaryPrintStmt(elseNode[0])

    return (ifUnaryPrint, elseUnaryPrint, ifUnaryPrintNode, elseUnaryPrintNode)

def printNodeToLVRep(printNode):
    outputTermUUID = None
    printFunction = getPrintExprFunction(printNode)
    if printFunction == "Println":
        arg = printNode.find("args/arg")
        if arg[0].tag == "BasicLit":
            kind = arg[0].find("kind").text.upper()
            val = arg[0].find("value").text
            if kind == "STRING":
                nodeName = "strcon"
                node = StringConstant(nodeName)
                node.setValue(val)
                lvGraph.addNode(node)
                outputTermUUID = node.getTerminal().uuid
        elif arg[0].tag == "Ident":
            identName = arg[0].find("name").text
            nodeUUID = lvGraph.getNodeByName(identName)
            node = lvGraph.getNodeByUUID(nodeUUID)
            if node.varType != "STRING":
                formatNode = FormatIntoStringsNode()
                formatString = "%d"
                formatStringNode = StringConstant("format string")
                formatStringNode.setValue(formatString)
                lvGraph.addNode(formatNode)
                lvGraph.addNode(formatStringNode)
                lvGraph.addTerminalEdge(formatStringNode.getTerminal().uuid, formatNode.getTerminalByName("format string").uuid)
                inputTerminal = lvGraph.getNodeByUUID(formatNode.uuid).getInputTerms()[0] #these are probably in order idk
                lvGraph.addTerminalEdge(node.getTerminal().uuid, inputTerminal.uuid)
                outputTermUUID = formatNode.getTerminalByName("resulting string").uuid
            else:
                outputTermUUID = node.getTerminal().uuid
    return outputTermUUID

def readArrayType(arrayTypeNode):
    arrayType = arrayTypeNode.find("type/Ident/name").text.upper()
    return arrayType

def getConstantNodeFromBasicLit(basicLit):
    value = basicLit.find("value").text
    varType = basicLit.find("kind").text.upper()
    node = getConstantNodeByVarType(lvGraph.getAvailableNodeName("const"), varType)
    node.setValue(value)
    return node

def processSwitchBody(bodyTag, caseNode):
    caseClauses = bodyTag.findall("BlockStmt/CaseClause")
    for c in caseClauses:
        case = c.find("cases/case")
        caseUUID = None
        if case[0].tag == "BasicLit":
            val = case.find("BasicLit/value").text
            caseUUID = caseNode.addSubdiagram(val)
            lvGraph.setDiagram(caseUUID)
        body = c.find("body")
        found, node = unaryPrintStmt(body)
        if found:
            arg = node.find("args/arg")
            if arg[0].tag == "BasicLit":
                constNode = getConstantNodeFromBasicLit(arg[0])
                lvGraph.addNode(constNode)
                caseNode.addPrintTunnel(constNode.getTerminal().uuid, caseUUID)
    return caseNode

def processCaseSelectorPrintTerminals(caseNode):
    innerTerms = {}
    for n, x in enumerate(caseNode.printTunnels):
        tunnels = caseNode.printTunnels[x]
        while len(tunnels) > len(innerTerms):
            innerTermList = []
            newNode = getIndicatorNodeByVarType(lvGraph.getAvailableNodeName("output"), "STRING")
            lvGraph.addNode(newNode)
            tunnelName = "tunnel" + str(len(innerTerms))
            for it in range(len(caseNode.printTunnels)):
                innerTermUUID = lvGraph.addTerminalToNode(caseNode.uuid, tunnelName + "InnerTerminal" + str(it))
                innerTermList.append(innerTermUUID)
            outerTermUUID = lvGraph.addTerminalToNode(caseNode.uuid, tunnelName + "OuterTerminal")
            lvGraph.addTerminalEdge(outerTermUUID, newNode.getTerminal().uuid)
            innerTerms[len(innerTerms)] = innerTermList
        for i, t in enumerate(tunnels):
            lvGraph.addTerminalEdge(t, innerTerms[i][n])

def processBlockStmtChild(node, blockUUID):
    lvGraph.diagramUUID = blockUUID
    if node.tag == "DeclStmt":
        varType = ""
        valSpec = node.find("GenDecl/ValueSpec")
        name = valSpec.find("names/name").text
        if valSpec is not None:
            varTypeNode = valSpec.find("type")
            if len(varTypeNode) == 0:
                varType = varTypeNode.text
            else:
                if varTypeNode[0].tag == "ArrayType":
                    arrayType = readArrayType(varTypeNode[0])
                    arrayNode = getArrayControlNodeByVarType(name, arrayType)
                    lvGraph.addNode(arrayNode)
                elif varTypeNode[0].tag == "Ident":
                    varType = varTypeNode.find("Ident/name").text
    
            value = None
            varNode = None
            valueTag = valSpec.find("values/value")
            if valueTag is not None:
                match valueTag[0].tag:
                    case "BasicLit":
                        varNode = getControlNodeByVarType(name, varType)
                        value = valueTag.find("BasicLit/value").text
                        if value is not None:
                            varNode.setValue(value)
                        lvGraph.addNode(varNode)
                    case "BinaryExpr":
                        varNode = getIndicatorNodeByVarType(name, varType)
                        binExpNode = valueTag.find("BinaryExpr")
                        if binExpNode is not None:
                            addBinaryNodeToLVGraph(binExpNode, name)
                    case "Ident":
                        varNode = getConstantNodeByVarType(name, varType)
                        value = valueTag.find("Ident/name").text
                        varNode.setValue(value)
                        lvGraph.addNode(varNode)
                        lvGraph.addSymbolTableEntry(name, varNode.getTerminal().uuid)
            else:
                varNode = getControlNodeByVarType(name, varType)
                lvGraph.addNode(varNode)
                lvGraph.addSymbolTableEntry(name, varNode.getTerminal().uuid)
    elif node.tag == "AssignStmt":
        lhsDict = {}
        token = node.find("token").text
        lhsArrayNode = node.find("LhsArray")
        varName = None
        varIndex = None #this is for array types
        for lhs in lhsArrayNode:
            if lhs[0].tag == "IndexExpr":
                varName = lhs[0].find("x/Ident/name").text
                varIndex = lhs[0].find("index/BasicLit/value").text
            else:
                varName = lhs.find("Ident/name").text
            lhsDict[lhs.attrib["id"]] = (varName, varIndex)
        
        rhsDict = {}
        rhsArrayNode = node.find("RhsArray")
        for rhs in rhsArrayNode:
            rhsDict[rhs.attrib["id"]] = rhs

        for lhs in lhsDict:
            if lhs in rhsDict:
                rhsNode = rhsDict[lhs]
                nodeName = lhsDict[lhs][0]
                varIndex = lhsDict[lhs][1]
                if len(rhsNode) > 0:
                    if rhsNode[0].tag == "BasicLit":
                        rhsNode = rhsNode[0]
                        value = rhsNode.find("value").text
                        varType = rhsNode.find("kind").text.upper()
                        if token == "=":
                            nodeUUID = lvGraph.getNodeByName(nodeName) #need some way to keep track of name changes if vars are duplicated (idk how important)
                            node = lvGraph.getNodeByUUID(nodeUUID)
                            if varIndex is not None:
                                node.setValue(int(varIndex), value)
                            else:
                                node.setValue(value)
                            #if it had a value already then I'm not sure what to do yet
                            #my best guess is it would have to end up as a property node value setting
                        else: #token will be := for new variables
                            varNode = getControlNodeByVarType(nodeName, varType)
                            lvGraph.addNode(varNode)
                            lvGraph.addSymbolTableEntry(nodeName, varNode.getTerminal().uuid)
                            varNode.setValue(value)

                    elif rhsNode[0].tag == "CompositeLit":
                        varType = None
                        typeNode = rhsNode[0].find("type")
                        if token == "=":
                            pass
                        else:
                            if typeNode[0].tag == "ArrayType":
                                varType = readArrayType(typeNode[0])
                                varNode = getArrayControlNodeByVarType(nodeName, varType)
                                eltNodes = rhsNode[0].findall("elts/elt")
                                for elt in eltNodes:
                                    valNode = elt.find("BasicLit/value")
                                    if valNode is not None:
                                        varNode.setValue(int(elt.attrib["id"]), valNode.text)
                                lvGraph.addNode(varNode)
                                lvGraph.addSymbolTableEntry(nodeName, varNode.getTerminal().uuid)

                    elif rhsNode[0].tag == "BinaryExpr":
                        addBinaryNodeToLVGraph(rhsNode[0], lhsDict[lhs])
                    elif rhsNode[0].tag == "Ident":
                        identName = rhsNode[0].find("name").text
                        if identName == "true" or identName == "false":
                            varNode = getControlNodeByVarType(nodeName, "BOOL")
                            lvGraph.addNode(varNode)
                            lvGraph.addSymbolTableEntry(nodeName, varNode.getTerminal().uuid)
                            varNode.setValue(identName)
                    elif rhsNode[0].tag == "CallExpr":
                        funcName = rhsNode[0].find("Ident/name")
                        args = rhsNode[0].findall("args/arg")
                        if funcName is not None:
                            funcName = funcName.text
                            match (funcName):
                                case "append":
                                    if len(args) == 2:
                                        incomingArray = args[0]
                                        incomingArray = incomingArray.find("Ident/name").text
                                        incomingArrayTerminalUUID = lvGraph.getTerminalFromSymbolTable(incomingArray) 
                                        newItem = args[1]
                                        newElemNode = None
                                        if newItem[0].tag == "BasicLit":
                                            newElemNode = getConstantNodeFromBasicLit(newItem[0])
                                        if newElemNode is not None:
                                            lvGraph.addNode(newElemNode)
                                            insertNode = InsertIntoArrayNode(lvGraph.getAvailableNodeName("insertintoarray"))
                                            lvGraph.addNode(insertNode)
                                            inputTerm, indexTerm, newElemTerm, outputTerm = insertNode.getTerms()
                                            lvGraph.addTerminalEdge(incomingArrayTerminalUUID, inputTerm.uuid)
                                            lvGraph.addSymbolTableEntry(incomingArray, outputTerm.uuid)
                                            lvGraph.addTerminalEdge(newElemNode.getTerminal().uuid, newElemTerm.uuid)
                                            lvGraph.setTerminalVarType(inputTerm.uuid, lvGraph.getTerminalVarType(incomingArrayTerminalUUID))
                                            lvGraph.setTerminalVarType(outputTerm.uuid, lvGraph.getTerminalVarType(inputTerm.uuid))

                            
    elif node.tag == "ExprStmt":
        callExpr = node.find("CallExpr")
        if callExpr is not None:
            selectorExpr = callExpr.find("SelectorExpr")
            if selectorExpr is not None:
                x = selectorExpr.find("x").text
                sel = selectorExpr.find("sel").text
                if x == "fmt":
                    match sel:
                        case "Printf":
                            args = callExpr.find("args")
                            if args is not None:
                                argNodes = args.findall("arg")
                                if argNodes[0].find("BasicLit") is not None:
                                    formatNode = FormatIntoStringsNode()
                                    formatString = argNodes[0].find("BasicLit/value").text
                                    formatStringNode = StringConstant("format string")
                                    formatStringNode.setValue(formatString)
                                    lvGraph.addNode(formatNode)
                                    lvGraph.addNode(formatStringNode)
                                    lvGraph.addTerminalEdge(formatStringNode.getTerminal().uuid, formatNode.getTerminalByName("format string").uuid)
                                    remaining_args = argNodes[1:]
                                    for i in range(len(remaining_args)):
                                        if i > 0:
                                            lvGraph.addTerminalToNode(formatNode.uuid)
                                        arg = remaining_args[i]
                                        if arg.find("Ident") is not None:
                                            varName = arg.find("Ident/name").text
                                            varNode = lvGraph.getNodeByUUID(lvGraph.getNodeByName(varName))
                                            inputTerminal = lvGraph.getNodeByUUID(formatNode.uuid).getInputTerms()[i] #these are probably in order idk
                                            lvGraph.addTerminalEdge(varNode.getTerminal().uuid, inputTerminal.uuid)
                                    outputNode = StringIndicator("output")
                                    lvGraph.addNode(outputNode)
                                    lvGraph.addTerminalEdge(formatNode.getTerminalByName("resulting string").uuid, outputNode.getTerminal().uuid)
                        case "Println":
                            args = callExpr.find("args")
                            if args is not None:
                                argNodes = args.findall("arg")
                                for arg in argNodes:
                                    match arg[0].tag:
                                        case "BinaryExpr":
                                            binExpNode = arg[0]
                                            if binExpNode is not None:
                                                addBinaryNodeToLVGraph(binExpNode, "output")
                                        case "Ident":
                                            varName = arg[0].find("name").text
                                            terminalUUID = lvGraph.getTerminalFromSymbolTable(varName)
                                            outputNode = getIndicatorNodeByVarType(lvGraph.getAvailableNodeName(varName + " Out"), lvGraph.getTerminalVarType(terminalUUID))
                                            lvGraph.addNode(outputNode)
                                            lvGraph.addTerminalEdge(terminalUUID, outputNode.getTerminal().uuid)

    elif node.tag == "IfStmt":
        condNode = node.find("cond")
        condUUID = None
        if condNode[0].tag == "BinaryExpr":
           condUUID = addBinaryNodeToLVGraph(condNode[0], None, False)
        elif condNode[0].tag == "Ident":
            identName = condNode[0].find("name").text
            condUUID = lvGraph.getNodeByUUID(lvGraph.getNodeByName(identName)).getTerminal().uuid
        ifUnary, elseUnary, ifPrintNode, elsePrintNode = determineIfStatementRep(node)
        if ifUnary and elseUnary:
            trueResultTerm = printNodeToLVRep(ifPrintNode)
            falseResultTerm = printNodeToLVRep(elsePrintNode)
            selectNode = SelectNode()
            selectNode.name = "select"
            lvGraph.addNode(selectNode)
            trueTerm, selectTerm, falseTerm, outTerm = selectNode.getTerms()
            lvGraph.addTerminalEdge(trueResultTerm, trueTerm.uuid)
            lvGraph.addTerminalEdge(falseResultTerm, falseTerm.uuid)
            lvGraph.addTerminalEdge(condUUID, selectTerm.uuid)
            outNode = getIndicatorNodeByVarType("output", "STRING")
            lvGraph.addNode(outNode)
            lvGraph.addTerminalEdge(outTerm.uuid, outNode.getTerminal().uuid)
        else:
            caseSelector = CaseSelector(lvGraph.getAvailableNodeName("case"))
            trueCaseUUID = caseSelector.addSubdiagram("True")
            falseCaseUUID = caseSelector.addSubdiagram("False")
            lvGraph.addNode(caseSelector)
            lvGraph.addSubSymbolTable(trueCaseUUID)

            blockStmtTag = node.find("body/BlockStmt")
            for child in blockStmtTag:
                processBlockStmtChild(child, trueCaseUUID)

    elif node.tag == "SwitchStmt":
        caseSelector = CaseSelector(lvGraph.getAvailableNodeName("case"))
        processSwitchBody(node.find("body"), caseSelector)
        lvGraph.setDiagram(blockUUID)
        lvGraph.addNode(caseSelector)
        tagNode = node.find("tag")
        if tagNode[0].tag == "Ident":
            varName = tagNode.find("Ident/name").text
            caseTerminalUUID = lvGraph.getTerminalFromSymbolTable(varName)
            lvGraph.addTerminalEdge(caseTerminalUUID, caseSelector.getCaseSelectorExternal().uuid)
        processCaseSelectorPrintTerminals(caseSelector)
        
                                    

def writeWireToXML(wire):
    rootElem = ET.Element("wire")
    rootElem.attrib["id"] = wire.uuid
    rootElem.attrib["from"] = wire.fromUUID
    rootElem.attrib["to"] = wire.toUUID
    return rootElem


tree = ET.parse('goast/goast1.txt')
with open("python/goast2.xml", "wb") as writeBack:
    ET.indent(tree, space="\t", level=0)
    tree.write(writeBack)
root = tree.getroot()

funcDecls = root.findall(".//FuncDecl")
visNode = ET.Element("vis")
viNode = ET.Element("vi")
bdNode = ET.Element("bd")
bdNode.attrib["name"] = "test"
outputNodesElem = ET.Element("nodes")
outputWiresElem = ET.Element("wires")
if len(funcDecls) > 0:
    for funcDecl in funcDecls:
        ident = funcDecl.find("Ident/name").text
        if ident == "main":
            bdUUID = lvGraph.diagramUUID
            bdNode.attrib["diagramUUID"] = bdUUID
            mainBlockStmt = funcDecl.find("BlockStmt")
            for node in mainBlockStmt:
                processBlockStmtChild(node, bdUUID)
            for i, n in enumerate(lvGraph.graph["nodes"]):
                outputNodesElem.append(lvGraph.graph["nodes"][n].writeNodeToXML(i))
            for w in lvGraph.getWires():
                outputWiresElem.append(writeWireToXML(w))
bdNode.append(outputNodesElem)
bdNode.append(outputWiresElem)
viNode.append(bdNode)
visNode.append(viNode)
tree = ET.ElementTree(visNode)
with open("python/ai.xml", "wb") as files:
    ET.indent(tree, space="\t", level=0)
    tree.write(files)
