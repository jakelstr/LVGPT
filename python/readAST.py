import xml.etree.ElementTree as ET
import uuid
from lvgptGraph import *

blockTable = {}
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
    left = node.find("left")
    right = node.find("right")
    if len(left) > 0:
        if left[0].tag == "BinaryExpr":
            returnDict["left"] = processBinaryExpr(left[0])
    else:
        returnDict["left"] = left.text
    if len(right) > 0:
        if left[0].tag == "BinaryExpr":
            returnDict["right"] = processBinaryExpr(right[0])
    else:
        returnDict["right"] = right.text
    return returnDict

def processBinaryDict(binaryDict):
    left = binaryDict["left"]
    right = binaryDict["right"]
    op = binaryDict["op"]
    opNodeName = lvGraph.getAvailableNodeName(op.name)
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

def addBinaryNodeToLVGraph(binaryXMLNode, nodeName):
    binExpDict = processBinaryExpr(binaryXMLNode)
    binExpDict, outType = processBinaryDict(binExpDict)
    if outType.upper() == "STRING":
        binExpDict, outType = convertBinaryDictToConcatStrings(binExpDict, 0)
    _, _, finalOutputTerm = binExpDict["op"].getTerms()
    nodeName = lvGraph.getAvailableNodeName(nodeName)
    varNode = getIndicatorNodeByVarType(nodeName, outType)
    lvGraph.addNode(varNode)
    lvGraph.addTerminalEdge(finalOutputTerm.uuid, varNode.getTerminal().uuid)
    return nodeName


def processBlockStmtChild(node, blockUUID):
    lvGraph.diagramUUID = blockUUID
    if node.tag == "DeclStmt":
        varType = ""
        valSpec = node.find("GenDecl/ValueSpec")
        if valSpec is not None:
            varType = valSpec.find("type").text
            name = valSpec.find("names/name").text
            value = None
            varNode = None
            valueTag = valSpec.find("values/value")

            match valueTag[0].tag:
                case "BasicLit":
                    nodeName = lvGraph.getAvailableNodeName(name)
                    varNode = getControlNodeByVarType(nodeName, varType)
                    value = valueTag.find("BasicLit/value").text
                    if value is not None:
                        varNode.setValue(value)
                    lvGraph.addNode(varNode)
                case "BinaryExpr":
                    varNode = getIndicatorNodeByVarType(name, varType)
                    binExpNode = valueTag.find("BinaryExpr")
                    if binExpNode is not None:
                        addBinaryNodeToLVGraph(binExpNode, name)
    elif node.tag == "AssignStmt":
        lhsDict = {}
        token = node.find("token").text
        lhsArrayNode = node.find("LhsArray")
        for lhs in lhsArrayNode:
            lhsDict[lhs.attrib["id"]] = lhs.text
        
        rhsDict = {}
        rhsArrayNode = node.find("RhsArray")
        for rhs in rhsArrayNode:
            rhsDict[rhs.attrib["id"]] = rhs

        for lhs in lhsDict:
            if lhs in rhsDict:
                rhsNode = rhsDict[lhs]
                if len(rhsNode) > 0:
                    if rhsNode[0].tag == "BasicLit":
                        rhsNode = rhsNode[0]
                        value = rhsNode.find("value").text
                        varType = rhsNode.find("kind").text.upper()
                        nodeName = lhsDict[lhs]
                        if token == "=":
                            nodeUUID = lvGraph.getNodeByName(nodeName) #need some way to keep track of name changes if vars are duplicated (idk how important)
                            node = lvGraph.getNodeByUUID(nodeUUID)
                            node.setValue(value)
                            #if it had a value already then I'm not sure what to do yet
                            #my best guess is it would have to end up as a property node value setting
                        else: #token will be := for new variables
                            nodeName = lvGraph.getAvailableNodeName(nodeName)
                            varNode = getControlNodeByVarType(nodeName, varType)
                            lvGraph.addNode(varNode)
                            varNode.setValue(value)
                         
                    elif rhsNode[0].tag == "BinaryExpr":
                        addBinaryNodeToLVGraph(rhsNode[0], lhsDict[lhs])
    elif node.tag == "ExprStmt":
        callExpr = node.find("CallExpr")
        if callExpr is not None:
            selectorExpr = callExpr.find("SelectorExpr")
            if selectorExpr is not None:
                names = selectorExpr.findall("Ident/name")
                if len(names) == 2 and names[0].text == "fmt":
                    match names[1].text:
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
                                    outputNode = StringIndicator(lvGraph.getAvailableNodeName("output"))
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

                                    

def writeNodeToXML(node, index):
    rootElem = ET.Element("node")
    rootElem.attrib["xPos"] = "0"
    rootElem.attrib["yPos"] = str(index * 50)
    for attrib in node.attributes:
        rootElem.attrib[attrib] = node.attributes[attrib]
    terminalsElem = ET.Element("terminals")
    for term in node.terminals:
        termElem = ET.Element("terminal")
        termElem.attrib["id"] = node.terminals[term].uuid
        termElem.attrib["name"] = node.terminals[term].name
        terminalsElem.append(termElem)
    rootElem.append(terminalsElem)
    return rootElem

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
            bdUUID = str(uuid.uuid4())
            blockTable[bdUUID] = {"vars":{}, "nodes":{}, "wires":[]}
            mainBlockStmt = funcDecl.find("BlockStmt")
            for node in mainBlockStmt:
                processBlockStmtChild(node, bdUUID)
            for i, n in enumerate(lvGraph.graph["nodes"]):
                outputNodesElem.append(writeNodeToXML(lvGraph.graph["nodes"][n], i))
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
