import xml.etree.ElementTree as ET
from lvgptGraph import *
import logging
lvGraph = LVGraph()

# Configure logging for better debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
            caseSelector = CaseStructure(lvGraph.getAvailableNodeName("case"))
            trueCaseUUID = caseSelector.addFrame("True")
            falseCaseUUID = caseSelector.addFrame("False")
            lvGraph.addNode(caseSelector)
            lvGraph.addSubSymbolTable(trueCaseUUID)

            blockStmtTag = node.find("body/BlockStmt")
            for child in blockStmtTag:
                processBlockStmtChild(child, trueCaseUUID)

    elif node.tag == "ForStmt":
        logger.info("Processing ForStmt")
        processForStmt(node)
    elif node.tag == "RangeStmt":
        logger.info("Processing RangeStmt")
        processRangeStmt(node)

    elif node.tag == "SwitchStmt":
        caseSelector = CaseStructure(lvGraph.getAvailableNodeName("case"))
        processSwitchBody(node.find("body"), caseSelector)
        lvGraph.setDiagram(blockUUID)
        lvGraph.addNode(caseSelector)
        tagNode = node.find("tag")
        if tagNode[0].tag == "Ident":
            varName = tagNode.find("Ident/name").text
            caseTerminalUUID = lvGraph.getTerminalFromSymbolTable(varName)
            lvGraph.addTerminalEdge(caseTerminalUUID, caseSelector.getCaseSelectorExternal().uuid)
        processCaseSelectorPrintTerminals(caseSelector)

    else:
        logger.warning(f"Unhandled block statement type: {node.tag}")
        
                                    



def process():
    tree = ET.parse('goast/goast1.txt')
    with open("python/goast2.xml", "wb") as writeBack:
        ET.indent(tree, space="\t", level=0)
        tree.write(writeBack)
    root = tree.getroot()
    propNode = PropertyNode()
    propNode.addProperty("prop1")
    propNode.addProperty("prop2")
    lvGraph.addNode(propNode)
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

def test_property_node_wiring():

    visNode = ET.Element("vis")
    viNode = ET.Element("vi")
    bdNode = ET.Element("bd")
    bdNode.attrib["name"] = "test"
    outputNodesElem = ET.Element("nodes")
    outputWiresElem = ET.Element("wires")
    # Create the Class Specifier Constant node.
    # (Here, the id_string is set to "NumericConstant" as specified.)

    whileLoop = WhileLoop("whileLoop")
    lvGraph.addNode(whileLoop)

    tc = BoolConstant("tc")
    tc.setValue(True)
    lvGraph.addNode(tc, whileLoop.getSubdiagram())

    whileLoopCondTerm = whileLoop.getConditionalTerminal()
    lvGraph.addTerminalEdge(tc.getTerminal().uuid, whileLoopCondTerm.uuid)
    
    # Create a Property Node.
    # propNode = PropertyNode()
    # propNode.setLinkUUID(stringControl.uuid)
    # classPropTerminalUUID = propNode.addProperty("Value")
    # lvGraph.addNode(propNode)
    


    for i, n in enumerate(lvGraph.graph["nodes"]):
        outputNodesElem.append(lvGraph.graph["nodes"][n].writeNodeToXML(i))
    for w in lvGraph.getWires():
        outputWiresElem.append(writeWireToXML(w))
    bdNode.append(outputNodesElem)
    bdNode.append(outputWiresElem)
    viNode.append(bdNode)
    visNode.append(viNode)
    tree = ET.ElementTree(visNode)
    with open("python/ai-test.xml", "wb") as files:
        ET.indent(tree, space="\t", level=0)
        tree.write(files)

def gen_unit_test_file():
    # Boolean Control and Indicator Test
    boolControl = BoolControl("boolean control")
    boolControl.setValue(True) # Set a value for testing
    lvGraph.addNode(boolControl)

    boolInd = BoolIndicator("boolean indicator")
    lvGraph.addNode(boolInd)

    lvGraph.addTerminalEdge(boolControl.getTerminal().uuid, boolInd.getTerminal().uuid)

    # String Control, Constant, Concatenation, and Indicator Test
    strControl = StringControl("string control")
    strControl.setValue("test")
    lvGraph.addNode(strControl)

    strInd = StringIndicator("string indicator")
    lvGraph.addNode(strInd)

    stringConst = StringConstant("string constant")
    stringConst.setValue("Const")
    lvGraph.addNode(stringConst)

    concatString = ConcatenateStringsNode()
    lvGraph.addNode(concatString)
    stringTerms = concatString.getStringTerms()
    
    lvGraph.addTerminalEdge(strControl.getTerminal().uuid, stringTerms[0].uuid)
    lvGraph.addTerminalEdge(stringConst.getTerminal().uuid, stringTerms[1].uuid)
    lvGraph.addTerminalEdge(concatString.getTerminal().uuid, strInd.getTerminal().uuid)

    # Numeric Control and Indicator Test
    numControl = NumericControl("numeric control", "Long")
    numControl.setValue("33")
    lvGraph.addNode(numControl)

    numInd = NumericIndicator("numeric indicator", "Long")
    lvGraph.addNode(numInd)

    lvGraph.addTerminalEdge(numControl.getTerminal().uuid, numInd.getTerminal().uuid)

    # Select Node Test (Boolean Based)
    selectNode = SelectNode()
    lvGraph.addNode(selectNode)
    true_val = NumericConstant("true_val", "Long")
    true_val.setValue("100")
    lvGraph.addNode(true_val)
    false_val = NumericConstant("false_val", "Long")
    false_val.setValue("200")
    lvGraph.addNode(false_val)
    select_ind = NumericIndicator("select_ind", "Long")
    lvGraph.addNode(select_ind)

    lvGraph.addTerminalEdge(true_val.getTerminal().uuid, selectNode.getTerms()[0].uuid) # True value
    lvGraph.addTerminalEdge(boolControl.getTerminal().uuid, selectNode.getTerms()[1].uuid) # Selector
    lvGraph.addTerminalEdge(false_val.getTerminal().uuid, selectNode.getTerms()[2].uuid) # False value
    lvGraph.addTerminalEdge(selectNode.getTerms()[3].uuid, select_ind.getTerminal().uuid)

    # Addition Node Test
    addNode = AddNode()
    lvGraph.addNode(addNode)
    add_input1 = NumericConstant("add_input1", "Long")
    add_input1.setValue("10")
    lvGraph.addNode(add_input1)
    add_input2 = NumericConstant("add_input2", "Long")
    add_input2.setValue("20")
    lvGraph.addNode(add_input2)
    add_indicator = NumericIndicator("add_indicator", "Long")
    lvGraph.addNode(add_indicator)
    lvGraph.addTerminalEdge(add_input1.getTerminal().uuid, addNode.getTerms()[0].uuid)
    lvGraph.addTerminalEdge(add_input2.getTerminal().uuid, addNode.getTerms()[1].uuid)
    lvGraph.addTerminalEdge(addNode.getTerms()[2].uuid, add_indicator.getTerminal().uuid)

    # Subtraction Node Test
    subtractNode = SubtractNode()
    lvGraph.addNode(subtractNode)
    sub_input1 = NumericConstant("sub_input1", "Long")
    sub_input1.setValue("30")
    lvGraph.addNode(sub_input1)
    sub_input2 = NumericConstant("sub_input2", "Long")
    sub_input2.setValue("5")
    lvGraph.addNode(sub_input2)
    sub_indicator = NumericIndicator("sub_indicator", "Long")
    lvGraph.addNode(sub_indicator)
    lvGraph.addTerminalEdge(sub_input1.getTerminal().uuid, subtractNode.getTerms()[0].uuid)
    lvGraph.addTerminalEdge(sub_input2.getTerminal().uuid, subtractNode.getTerms()[1].uuid)
    lvGraph.addTerminalEdge(subtractNode.getTerms()[2].uuid, sub_indicator.getTerminal().uuid)

     # Multiplication Node Test
    multiplyNode = MultiplyNode()
    lvGraph.addNode(multiplyNode)
    mult_input1 = NumericConstant("mult_input1", "Long")
    mult_input1.setValue("7")
    lvGraph.addNode(mult_input1)
    mult_input2 = NumericConstant("mult_input2", "Long")
    mult_input2.setValue("6")
    lvGraph.addNode(mult_input2)
    mult_indicator = NumericIndicator("mult_indicator", "Long")
    lvGraph.addNode(mult_indicator)
    lvGraph.addTerminalEdge(mult_input1.getTerminal().uuid, multiplyNode.getTerms()[0].uuid)
    lvGraph.addTerminalEdge(mult_input2.getTerminal().uuid, multiplyNode.getTerms()[1].uuid)
    lvGraph.addTerminalEdge(multiplyNode.getTerms()[2].uuid, mult_indicator.getTerminal().uuid)

    # Division Node Test
    divideNode = DivideNode()
    lvGraph.addNode(divideNode)
    div_input1 = NumericConstant("div_input1", "Double Precision")
    div_input1.setValue("100")
    lvGraph.addNode(div_input1)
    div_input2 = NumericConstant("div_input2", "Double Precision")
    div_input2.setValue("4")
    lvGraph.addNode(div_input2)
    div_indicator = NumericIndicator("div_indicator", "Double Precision")
    lvGraph.addNode(div_indicator)
    lvGraph.addTerminalEdge(div_input1.getTerminal().uuid, divideNode.getTerms()[0].uuid)
    lvGraph.addTerminalEdge(div_input2.getTerminal().uuid, divideNode.getTerms()[1].uuid)
    lvGraph.addTerminalEdge(divideNode.getTerms()[2].uuid, div_indicator.getTerminal().uuid)
    
    # Comparison Node Tests (Greater Or Equal)
    greaterOrEqualNode = GreaterOrEqualNode()
    lvGraph.addNode(greaterOrEqualNode)
    ge_input1 = NumericConstant("ge_input1", "Long")
    ge_input1.setValue("50")
    lvGraph.addNode(ge_input1)
    ge_input2 = NumericConstant("ge_input2", "Long")
    ge_input2.setValue("40")
    lvGraph.addNode(ge_input2)
    ge_indicator = BoolIndicator("ge_indicator")
    lvGraph.addNode(ge_indicator)
    lvGraph.addTerminalEdge(ge_input1.getTerminal().uuid, greaterOrEqualNode.getTerms()[0].uuid)
    lvGraph.addTerminalEdge(ge_input2.getTerminal().uuid, greaterOrEqualNode.getTerms()[1].uuid)
    lvGraph.addTerminalEdge(greaterOrEqualNode.getTerms()[2].uuid, ge_indicator.getTerminal().uuid)

    # Comparison Node Tests (Equal)
    equalNode = EqualNode()
    lvGraph.addNode(equalNode)
    eq_input1 = NumericConstant("eq_input1", "Long")
    eq_input1.setValue("50")
    lvGraph.addNode(eq_input1)
    eq_input2 = NumericConstant("eq_input2", "Long")
    eq_input2.setValue("50")
    lvGraph.addNode(eq_input2)
    eq_indicator = BoolIndicator("eq_indicator")
    lvGraph.addNode(eq_indicator)
    lvGraph.addTerminalEdge(eq_input1.getTerminal().uuid, equalNode.getTerms()[0].uuid)
    lvGraph.addTerminalEdge(eq_input2.getTerminal().uuid, equalNode.getTerms()[1].uuid)
    lvGraph.addTerminalEdge(equalNode.getTerms()[2].uuid, eq_indicator.getTerminal().uuid)

    # Comparison Node Tests (Not Equal)
    notEqualNode = NotEqualNode()
    lvGraph.addNode(notEqualNode)
    neq_input1 = NumericConstant("neq_input1", "Long")
    neq_input1.setValue("50")
    lvGraph.addNode(neq_input1)
    neq_input2 = NumericConstant("neq_input2", "Long")
    neq_input2.setValue("40")
    lvGraph.addNode(neq_input2)
    neq_indicator = BoolIndicator("neq_indicator")
    lvGraph.addNode(neq_indicator)
    lvGraph.addTerminalEdge(neq_input1.getTerminal().uuid, notEqualNode.getTerms()[0].uuid)
    lvGraph.addTerminalEdge(neq_input2.getTerminal().uuid, notEqualNode.getTerms()[1].uuid)
    lvGraph.addTerminalEdge(notEqualNode.getTerms()[2].uuid, neq_indicator.getTerminal().uuid)
    
    # Comparison Node Tests (Greater Than)
    greaterThanNode = GreaterThanNode()
    lvGraph.addNode(greaterThanNode)
    gt_input1 = NumericConstant("gt_input1", "Long")
    gt_input1.setValue("50")
    lvGraph.addNode(gt_input1)
    gt_input2 = NumericConstant("gt_input2", "Long")
    gt_input2.setValue("40")
    lvGraph.addNode(gt_input2)
    gt_indicator = BoolIndicator("gt_indicator")
    lvGraph.addNode(gt_indicator)
    lvGraph.addTerminalEdge(gt_input1.getTerminal().uuid, greaterThanNode.getTerms()[0].uuid)
    lvGraph.addTerminalEdge(gt_input2.getTerminal().uuid, greaterThanNode.getTerms()[1].uuid)
    lvGraph.addTerminalEdge(greaterThanNode.getTerms()[2].uuid, gt_indicator.getTerminal().uuid)

    # Comparison Node Tests (Less Than)
    lessThanNode = LessThanNode()
    lvGraph.addNode(lessThanNode)
    lt_input1 = NumericConstant("lt_input1", "Long")
    lt_input1.setValue("40")
    lvGraph.addNode(lt_input1)
    lt_input2 = NumericConstant("lt_input2", "Long")
    lt_input2.setValue("50")
    lvGraph.addNode(lt_input2)
    lt_indicator = BoolIndicator("lt_indicator")
    lvGraph.addNode(lt_indicator)
    lvGraph.addTerminalEdge(lt_input1.getTerminal().uuid, lessThanNode.getTerms()[0].uuid)
    lvGraph.addTerminalEdge(lt_input2.getTerminal().uuid, lessThanNode.getTerms()[1].uuid)
    lvGraph.addTerminalEdge(lessThanNode.getTerms()[2].uuid, lt_indicator.getTerminal().uuid)

    # Comparison Node Tests (Less or Equal)
    lessOrEqualNode = LessOrEqualNode()
    lvGraph.addNode(lessOrEqualNode)
    loe_input1 = NumericConstant("loe_input1", "Long")
    loe_input1.setValue("40")
    lvGraph.addNode(loe_input1)
    loe_input2 = NumericConstant("loe_input2", "Long")
    loe_input2.setValue("50")
    lvGraph.addNode(loe_input2)
    loe_indicator = BoolIndicator("loe_indicator")
    lvGraph.addNode(loe_indicator)
    lvGraph.addTerminalEdge(loe_input1.getTerminal().uuid, lessOrEqualNode.getTerms()[0].uuid)
    lvGraph.addTerminalEdge(loe_input2.getTerminal().uuid, lessOrEqualNode.getTerms()[1].uuid)
    lvGraph.addTerminalEdge(lessOrEqualNode.getTerms()[2].uuid, loe_indicator.getTerminal().uuid)
    
    # Insert Into Array Node Test
    insertIntoArrayNode = InsertIntoArrayNode("insert_into_array")
    lvGraph.addNode(insertIntoArrayNode)

    input_array = ArrayControl("input_array")
    input_array.setChildNode(StringControl("String"))
    input_array.setValue(0, "First")
    input_array.setValue(1, "Second")
    lvGraph.addNode(input_array)
    
    index_to_insert = NumericConstant("index_to_insert", "Long")
    index_to_insert.setValue("1")
    lvGraph.addNode(index_to_insert)
    
    new_item = StringConstant("new_item")
    new_item.setValue("Inserted")
    lvGraph.addNode(new_item)

    output_array_indicator = ArrayIndicator("output_array")
    lvGraph.addNode(output_array_indicator)
    childNode = StringIndicator("String")
    output_array_indicator.setChildNode(childNode)

    terms = insertIntoArrayNode.getTerms()
    lvGraph.addTerminalEdge(input_array.getTerminal().uuid, terms[0].uuid)
    lvGraph.addTerminalEdge(index_to_insert.getTerminal().uuid, terms[1].uuid)
    lvGraph.addTerminalEdge(new_item.getTerminal().uuid, terms[2].uuid)
    lvGraph.addTerminalEdge(terms[3].uuid, output_array_indicator.getTerminal().uuid)
    
    # Case Structure Test
    caseSelector = CaseStructure("case_structure")
    case_0_uuid = caseSelector.addFrame("0")
    case_1_uuid = caseSelector.addFrame("1")
    tunnel = caseSelector.addTunnel()
    lvGraph.addNode(caseSelector)
    caseSelector.setDefaultFrame(case_0_uuid)

    case_selector_control = NumericControl("case_selector", "Long")
    case_selector_control.setValue("1")
    lvGraph.addNode(case_selector_control)

    case_selector_external = caseSelector.getCaseSelectorExternal()
    lvGraph.addTerminalEdge(case_selector_control.getTerminal().uuid, case_selector_external.uuid)

    
    true_constant = BoolConstant("true_constant")
    true_constant.setValue(True)
    lvGraph.addNode(true_constant, case_0_uuid)

    case_0_indicator = BoolIndicator("case_indicator")
    lvGraph.addNode(case_0_indicator)


    false_constant = BoolConstant("false_constant")
    false_constant.setValue(False)
    lvGraph.addNode(false_constant, case_1_uuid)

    
    lvGraph.addTerminalEdge(tunnel.external_terminal.uuid, case_0_indicator.getTerminal().uuid)
    case_0_internal = next((term for term in tunnel.terminals_internal if case_0_uuid in term.name), None)
    case_1_internal = next((term for term in tunnel.terminals_internal if case_1_uuid in term.name), None)

    lvGraph.addTerminalEdge(true_constant.getTerminal().uuid, case_0_internal.uuid)
    lvGraph.addTerminalEdge(false_constant.getTerminal().uuid, case_1_internal.uuid)
    lvGraph.finalize_layout()

    lvGraph.writeXML("test", "LabVIEW/unit_tests/def.xml")

def test_VI_From_File_wiring(path):    
    csc1 = ClassSpecifierConstant("csc1", "Control")
    csc1Term = csc1.getTerminal()
    lvGraph.addNode(csc1)
    csc2 = ClassSpecifierConstant("csc2", "Boolean")
    csc2Term = csc2.getTerminal()
    lvGraph.addNode(csc2)
    varToData = VariantToData("varToData")
    lvGraph.addNode(varToData)
    lvGraph.addTerminalEdge(csc1Term.uuid, varToData["type"].uuid)

    tsc = ToMoreSpecificClass("tsc")
    lvGraph.addNode(tsc)
    lvGraph.addTerminalEdge(csc2Term.uuid, tsc["target class"].uuid)
    lvGraph.addTerminalEdge(varToData["data"].uuid, tsc["reference"].uuid)
    lvGraph.addTerminalEdge(varToData["error out"].uuid, tsc["error in"].uuid)


    propNode = PropertyNode()
    classPropTerminalUUID = propNode.addProperty("Value")
    lvGraph.addNode(propNode)

    lvGraph.addTerminalEdge(tsc["error out"].uuid, propNode["error in (no error)"].uuid)
    lvGraph.addTerminalEdge(tsc["specific class reference"].uuid, propNode["reference"].uuid)

    lookInMap = LookInMap("lookInMap")
    lvGraph.addNode(lookInMap)
    valueConst = StringConstant("valueConst")
    valueConstTerm = valueConst.getTerminal()
    valueConst.setValue("value")
    lvGraph.addNode(valueConst)
    lvGraph.addTerminalEdge(valueConstTerm.uuid, lookInMap["key"].uuid)
    # lvGraph.addTerminalEdge(lookInMap["value"].uuid, classPropTerminalUUID)
    compareConst = StringConstant("compareConst")
    compareConstTerm = compareConst.getTerminal()
    compareConst.setValue("true")
    lvGraph.addNode(compareConst)

    eq = EqualNode()
    lvGraph.addNode(eq)
    lvGraph.addTerminalEdge(lookInMap["value"].uuid, eq["x"].uuid)
    lvGraph.addTerminalEdge(compareConstTerm.uuid, eq["y"].uuid)
    lvGraph.addTerminalEdge(eq["x = y?"].uuid, classPropTerminalUUID)

    lvGraph.writeXML("test", "LabVIEW/unit_tests/subVI.xml")


def GeminiGenerate():

    # Create a While Loop
    while_loop = WhileLoop("While Loop")
    lvGraph.addNode(while_loop)

    # Conditional Terminal for While Loop
    stop_control = BoolControl("Stop Control")
    lvGraph.addNode(stop_control)
    
    conditional_terminal = while_loop.getConditionalTerminal()
    lvGraph.addTerminalEdge(stop_control.getTerminal().uuid, conditional_terminal.uuid)

    # Shift Register
    shift_register = while_loop.addShiftRegister(50)

    # Numeric Constant for Initial Value
    initial_value = NumericConstant("Initial Value", "Long")
    initial_value.setValue("0")
    lvGraph.addNode(initial_value)
    
    # Add Node inside the loop
    add_node = AddNode()
    lvGraph.addNode(add_node, while_loop.getSubdiagram())
    
    # Numeric Constant to Increment
    increment_value = NumericConstant("Increment", "Long")
    increment_value.setValue("1")
    lvGraph.addNode(increment_value, while_loop.getSubdiagram())
    
    #Numeric Indicator for output
    numeric_indicator = NumericIndicator("Output", "Long")
    lvGraph.addNode(numeric_indicator)

    # Connect Initial Value to Left Hand External of Shift Register
    lvGraph.addTerminalEdge(initial_value.getTerminal().uuid, shift_register.lhExternalTerminal.uuid)
    # Wire the output indicator to the right hand external
    lvGraph.addTerminalEdge(shift_register.rhExternalTerminal.uuid, numeric_indicator.getTerminal().uuid)

    # Connections within the loop
    diagram_id = while_loop.getSubdiagram()
    lvGraph.addTerminalEdge(shift_register.lhInternalTerminal.uuid, add_node.getTerms()[0].uuid)  # Shift Register Value to Add Node (x)
    lvGraph.addTerminalEdge(increment_value.getTerminal().uuid, add_node.getTerms()[1].uuid)  # Increment Value to Add Node (y)
    lvGraph.addTerminalEdge(add_node.getTerms()[2].uuid, shift_register.rhInternalTerminal.uuid) #Add Output to Shift Register
    

    lvGraph.finalize_layout()
    lvGraph.writeXML("while_loop_with_shift_register", "while_loop_with_shift_register.xml")


# Optionally, call the test function if this file is run directly.
if __name__ == "__main__":
    GeminiGenerate()

