import xml.etree.ElementTree as ET
import uuid

blockTable = {}

class terminal:
    def __init__(self, name):
        self.uuid = str(uuid.uuid4())
        self.name = name
        self.edges = []
class wire:
    def __init__(self, fromUUID, toUUID):
        self.uuid = str(uuid.uuid4())
        self.fromUUID = fromUUID
        self.toUUID = toUUID

class LVNode:
    def __init__(self, name):
        self.uuid = str(uuid.uuid4())
        self.terminals = {}
        self.name = name
        self.attributes = {"name" : name}
        self.isIndicator = False

    def addTerminal(self, name):
        term = terminal(name)
        self.terminals[term.uuid] = term

    def getTerminalByName(self, name):
        for t in self.terminals:
            if self.terminals[t].name == name:
                return self.terminals[t]
        return None


class NumericControl(LVNode):
    def __init__(self, name, numType):
        LVNode.__init__(self, name)
        LVNode.addTerminal(self, name)
        self.attributes["type"] = "Numeric Control"
        self.attributes["numericType"] = numType
    def setValue(self, val):
        self.attributes["value"] = val
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)

class NumericIndicator(LVNode):
    def __init__(self, name, numType):
        LVNode.__init__(self, name)
        LVNode.addTerminal(self, name)
        self.attributes["type"] = "Numeric Indicator"
        self.attributes["numericType"] = numType
        self.isIndicator = True
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)
    
class StringControl(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        LVNode.addTerminal(self, name)
        self.attributes["type"] = "String Control"
    def setValue(self, val):
        self.attributes["value"] = val
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)
    
class StringConstant(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        LVNode.addTerminal(self, name)
        self.attributes["type"] = "String Constant"
    def setValue(self, val):
        self.attributes["value"] = val
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)

class StringIndicator(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        LVNode.addTerminal(self, name)
        self.attributes["type"] = "String Indicator"
        self.isIndicator = True
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)

class AddNode(LVNode):
    def  __init__(self):
        LVNode.__init__(self, "add")
        LVNode.addTerminal(self, "x")
        LVNode.addTerminal(self, "y")
        LVNode.addTerminal(self, "x+y")
        self.attributes["type"] = "Add"
    def getTerms(self):
        outputTerm = LVNode.getTerminalByName(self, "x+y")
        leftTerm = LVNode.getTerminalByName(self, "x")
        rightTerm = LVNode.getTerminalByName(self, "y")
        return (leftTerm, rightTerm, outputTerm)
    
class MultiplyNode(LVNode):
    def  __init__(self):
        LVNode.__init__(self, "mult")
        LVNode.addTerminal(self, "x")
        LVNode.addTerminal(self, "y")
        LVNode.addTerminal(self, "x*y")
        self.attributes["type"] = "Multiply"
    def getTerms(self):
        outputTerm = LVNode.getTerminalByName(self, "x*y")
        leftTerm = LVNode.getTerminalByName(self, "x")
        rightTerm = LVNode.getTerminalByName(self, "y")
        return (leftTerm, rightTerm, outputTerm)

class SubtractNode(LVNode):
    def  __init__(self):
        LVNode.__init__(self, "subtract")
        LVNode.addTerminal(self, "x")
        LVNode.addTerminal(self, "y")
        LVNode.addTerminal(self, "x-y")
        self.attributes["type"] = "Subtract"
    def getTerms(self):
        outputTerm = LVNode.getTerminalByName(self, "x-y")
        leftTerm = LVNode.getTerminalByName(self, "x")
        rightTerm = LVNode.getTerminalByName(self, "y")
        return (leftTerm, rightTerm, outputTerm)
    
class DivideNode(LVNode):
    def  __init__(self):
        LVNode.__init__(self, "divide")
        LVNode.addTerminal(self, "x")
        LVNode.addTerminal(self, "y")
        LVNode.addTerminal(self, "x/y")
        self.attributes["type"] = "Divide"
    def getTerms(self):
        outputTerm = LVNode.getTerminalByName(self, "x/y")
        leftTerm = LVNode.getTerminalByName(self, "x")
        rightTerm = LVNode.getTerminalByName(self, "y")
        return (leftTerm, rightTerm, outputTerm)

class ConcatenateStringsNode(LVNode):
    def  __init__(self):
        LVNode.__init__(self, "concat")
        LVNode.addTerminal(self, "string")
        LVNode.addTerminal(self, "string")
        LVNode.addTerminal(self, "concatenated string")
        self.attributes["type"] = "Concatenate Strings"
        self.attributes["nodes"] = "2"
    def getTerms(self):
        outputTerm = LVNode.getTerminalByName(self, "concatenated string")
        return (None, None, outputTerm)
    def addTerminal(self):
        LVNode.addTerminal(self, "string")
        self.attributes["nodes"] = str(int(self.attributes["nodes"]) + 1)
    def getStringTerms(self):
        return [item for item in self.terminals.values() if item.name == "string"]
    
class FormatIntoStringsNode(LVNode):
    def  __init__(self):
        LVNode.__init__(self, "fstr")
        LVNode.addTerminal(self, "input 1")
        LVNode.addTerminal(self, "format string")
        LVNode.addTerminal(self, "resulting string")
        self.attributes["type"] = "Format Into String"
        self.attributes["nodes"] = "1"
    def getTerms(self):
        outputTerm = LVNode.getTerminalByName(self, "concatenated string")
        return (None, None, outputTerm)
    def addTerminal(self):
        self.attributes["nodes"] = str(int(self.attributes["nodes"]) + 1)
        LVNode.addTerminal(self, "input " + str(int(self.attributes["nodes"])))
    def getInputTerms(self):
        return [item for item in self.terminals.values() if "input" in item.name]

class var:
    def __init__(self, name, value, varType):
        self.value = value
        self.varType = varType
        self.name = name

def getControlNodeByVarType(varName, varType):
    match varType.upper():
        case "INT":
            return NumericControl(varName, "Quad")
        case "INT8":
            return NumericControl(varName, "Byte")
        case "INT16":
            return NumericControl(varName, "Word")
        case "INT32":
            return NumericControl(varName, "Long")
        case "INT64":
            return NumericControl(varName, "Quad")
        case "UINT":
            return NumericControl(varName, "Unsigned Quad")
        case "UINT8":
            return NumericControl(varName, "Unsigned Byte")
        case "UINT16":
            return NumericControl(varName, "Unsigned Word")
        case "UINT32":
            return NumericControl(varName, "Unsigned Long")
        case "UINT64":
            return NumericControl(varName, "Unsigned Quad")
        case "FLOAT32":
            return NumericControl(varName, "Single Precision")
        case "FLOAT64":
            return NumericControl(varName, "Double Precision")
        case "STRING":
            return StringControl(varName)
    return LVNode(varName)

def getIndicatorNodeByVarType(varName, varType):
    match varType.upper():
        case "INT":
            return NumericIndicator(varName, "Quad")
        case "INT8":
            return NumericIndicator(varName, "Byte")
        case "INT16":
            return NumericIndicator(varName, "Word")
        case "INT32":
            return NumericIndicator(varName, "Long")
        case "INT64":
            return NumericIndicator(varName, "Quad")
        case "UINT":
            return NumericIndicator(varName, "Unsigned Quad")
        case "UINT8":
            return NumericIndicator(varName, "Unsigned Byte")
        case "UINT16":
            return NumericIndicator(varName, "Unsigned Word")
        case "UINT32":
            return NumericIndicator(varName, "Unsigned Long")
        case "UINT64":
            return NumericIndicator(varName, "Unsigned Quad")
        case "FLOAT32":
            return NumericIndicator(varName, "Single Precision")
        case "FLOAT64":
            return NumericIndicator(varName, "Double Precision")
        case "STRING":
            return StringIndicator(varName)
    return LVNode(varName)

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
    wires = []
    nodes = []
    uniform, op, binVars = determineBinaryDictOpUniform(binaryDict)
    if uniform and op is AddNode:
        concatNode = ConcatenateStringsNode()
        if len(binVars) > 2:
            for x in range(len(binVars) - 2):
                concatNode.addTerminal()
        binaryDict["op"] = concatNode
        stringTerms = concatNode.getStringTerms()
        for x in range(len(binVars)):
            varNode = blockTable[blockLevel]["nodes"][binVars[x].nodeUUID]
            w = wire(varNode.getTerminal().uuid, stringTerms[x].uuid)
            wires.append(w)
    nodes.append(concatNode)
    return (binaryDict, wires, nodes, "STRING")

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
        returnDict["left"] = processBinaryExpr(left[0])
    else:
        returnDict["left"] = left.text
    if len(right) > 0:
        returnDict["right"] = processBinaryExpr(right[0])
    else:
        returnDict["right"] = right.text
    return returnDict

def processBinaryDict(binaryDict, blockLevel):
    wires = []
    nodes = []
    left = binaryDict["left"]
    right = binaryDict["right"]
    op = binaryDict["op"]
    outType = "int"
    leftOutType = "int"
    rightOutType = "int"
    opLeftTerm, opRightTerm, opOutputTerm = op.getTerms()
    if type(left) is dict:
        left, subWires, subNodes, leftOutType = processBinaryDict(left, blockLevel)
        wires.extend(subWires)
        nodes.extend(subNodes)
        _, _, subOutput = left["op"].getTerms()
        wires.append(wire(subOutput.uuid, opLeftTerm.uuid))
    else:
        if left in blockTable[blockLevel]["vars"]:
            left = blockTable[blockLevel]["vars"][left]
            leftNode = blockTable[blockLevel]["nodes"][left.nodeUUID]
            leftWire = wire(leftNode.getTerminal().uuid, opLeftTerm.uuid)
            leftOutType = left.varType
            wires.append(leftWire)
    if type(right) is dict:
        right, subWires, subNodes, rightOutType = processBinaryDict(right, blockLevel)
        _, _, subOutput = right["op"].getTerms()
        wires.append(wire(subOutput.uuid, opRightTerm.uuid))
        wires.extend(subWires)
        nodes.extend(subNodes)
    else:
        if right in blockTable[blockLevel]["vars"]:
            right = blockTable[blockLevel]["vars"][right]
            rightNode = blockTable[blockLevel]["nodes"][right.nodeUUID]
            rightWire = wire(rightNode.getTerminal().uuid, opRightTerm.uuid)
            rightOutType = right.varType
            wires.append(rightWire)
    nodes.append(op)
    if leftOutType.upper() == rightOutType.upper():
        outType = leftOutType.upper()
    else:
        #panic I guess idk
        pass
    binaryDict["left"] = left
    binaryDict["right"] = right
    return (binaryDict, wires, nodes, outType)


def processBlockStmtChild(node, blockLevel):
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
                    varNode = getControlNodeByVarType(name, varType)
                    value = valueTag.find("BasicLit/value").text
                case "BinaryExpr":
                    varNode = getIndicatorNodeByVarType(name, varType)
                    binExpNode = valueTag.find("BinaryExpr")
                    if binExpNode is not None:
                        binExpDict = processBinaryExpr(binExpNode)
                        binExpDict, wires, nodes, outType = processBinaryDict(binExpDict, blockLevel)
                        if outType.upper() == "STRING":
                            binExpDict, wires, nodes, outType = convertBinaryDictToConcatStrings(binExpDict, blockLevel)
                        _, _, finalOutputTerm = binExpDict["op"].getTerms()
                        varType  = outType
                        finalWire = wire(finalOutputTerm.uuid, varNode.getTerminal().uuid)
                        blockTable[blockLevel]["wires"].append(finalWire)
                        blockTable[blockLevel]["wires"].extend(wires)
                        for b in nodes:
                            blockTable[blockLevel]["nodes"][b.uuid] = b
            varItem = var(name, value, varType)
            if value is not None:
                varNode.setValue(value)
            varItem.nodeUUID = varNode.uuid
            blockTable[blockLevel]["nodes"][varNode.uuid] = varNode
            blockTable[blockLevel]["vars"][name] = varItem
    elif node.tag == "AssignStmt":
        lhsDict = {}
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
                        varType = rhsNode.find("kind").text.lower()
                        varItem = var(lhsDict[lhs], value, varType)
                        if varItem.name in blockTable[blockLevel]["vars"]:
                            if blockTable[blockLevel]["vars"][varItem.name].value == None:
                                blockTable[blockLevel]["vars"][varItem.name].value = varItem.value
                                nodeUUID = blockTable[blockLevel]["vars"][varItem.name].nodeUUID
                                blockTable[blockLevel]["nodes"][nodeUUID].setValue(value)
                                #if it had a value already then I'm not sure what to do yet
                                #my best guess is it would have to end up as a property node value setting
                        else:
                            varNode = getControlNodeByVarType(varItem.name, varItem.varType)
                            varNode.setValue(value)
                            varItem.nodeUUID = varNode.uuid
                            blockTable[blockLevel]["nodes"][varNode.uuid] = varNode
                            blockTable[blockLevel]["vars"][varItem.name] = varItem
                         
                    elif rhsNode[0].tag == "BinaryExpr":
                        binExpDict = processBinaryExpr(rhsNode[0])
                        binExpDict, wires, nodes, outType = processBinaryDict(binExpDict, blockLevel)
                        _, _, finalOutputTerm = binExpDict["op"].getTerms()
                        varItem = var(lhsDict[lhs], 0, outType)
                        varNode = getIndicatorNodeByVarType(varItem.name, varItem.varType)
                        varItem.nodeUUID = varNode.uuid
                        blockTable[blockLevel]["nodes"][varNode.uuid] = varNode
                        blockTable[blockLevel]["vars"][varItem.name] = varItem
                        finalWire = wire(finalOutputTerm.uuid, varNode.getTerminal().uuid)
                        blockTable[blockLevel]["wires"].append(finalWire)
                        blockTable[blockLevel]["wires"].extend(wires)
                        for b in nodes:
                            blockTable[blockLevel]["nodes"][b.uuid] = b
    elif node.tag == "ExprStmt":
        wires = []
        nodes = []
        callExpr = node.find("CallExpr")
        if callExpr is not None:
            selectorExpr = callExpr.find("SelectorExpr")
            if selectorExpr is not None:
                names = selectorExpr.findall("Ident/name")
                if len(names) == 2 and names[0].text == "fmt" and names[1].text == "Printf":
                    args = callExpr.find("args")
                    if args is not None:
                        argNodes = args.findall("arg")
                        if argNodes[0].find("BasicLit") is not None:
                            formatNode = FormatIntoStringsNode()
                            formatString = argNodes[0].find("BasicLit/value").text
                            formatStringNode = StringConstant("format string")
                            formatStringNode.setValue(formatString)
                            nodes.append(formatNode)
                            nodes.append(formatStringNode)
                            formatWire = wire(formatStringNode.getTerminal().uuid, formatNode.getTerminalByName("format string").uuid)
                            wires.append(formatWire)
                            remaining_args = argNodes[1:]
                            for i in range(len(remaining_args)):
                                if i > 0:
                                    formatNode.addTerminal()
                                arg = remaining_args[i]
                                if arg.find("Ident") is not None:
                                    varName = arg.find("Ident/name").text
                                    if varName in blockTable[blockLevel]["vars"]:
                                        varItem = blockTable[blockLevel]["vars"][varName]
                                        if varItem.nodeUUID in blockTable[blockLevel]["nodes"]:
                                            varNode = blockTable[blockLevel]["nodes"][varItem.nodeUUID]
                                            inputTerminal = formatNode.getInputTerms()[i] #these are probably in order idk
                                            inputWire = wire(varNode.getTerminal().uuid, inputTerminal.uuid)
                                            wires.append(inputWire)
                            outputNode = StringIndicator("output")
                            nodes.append(outputNode)
                            outputWire = wire(formatNode.getTerminalByName("resulting string").uuid, outputNode.getTerminal().uuid)
                            wires.append(outputWire)
                            for n in nodes:
                                blockTable[blockLevel]["nodes"][n.uuid] = n
                            for w in wires:
                                blockTable[blockLevel]["wires"].append(w)



                                    

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
            blockTable[0] = {"vars":{}, "nodes":{}, "wires":[]}
            mainBlockStmt = funcDecl.find("BlockStmt")
            for node in mainBlockStmt:
                processBlockStmtChild(node, 0)
            for i, n in enumerate(blockTable[0]["nodes"]):
                outputNodesElem.append(writeNodeToXML(blockTable[0]["nodes"][n], i))
            for w in blockTable[0]["wires"]:
                outputWiresElem.append(writeWireToXML(w))
bdNode.append(outputNodesElem)
bdNode.append(outputWiresElem)
viNode.append(bdNode)
visNode.append(viNode)
tree = ET.ElementTree(visNode)
with open("python/ai.xml", "wb") as files:
    ET.indent(tree, space="\t", level=0)
    tree.write(files)
            
