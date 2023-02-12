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
        LVNode.addTerminal(self, "x")
        LVNode.addTerminal(self, "y")
        LVNode.addTerminal(self, "x/y")
        self.attributes["type"] = "Divide"
    def getTerms(self):
        outputTerm = LVNode.getTerminalByName(self, "x/y")
        leftTerm = LVNode.getTerminalByName(self, "x")
        rightTerm = LVNode.getTerminalByName(self, "y")
        return (leftTerm, rightTerm, outputTerm)

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
            name = valSpec.find("Ident/name").text
            value = None
            basicLit = valSpec.find("BasicLit/value")
            if basicLit is not None:
                value = basicLit.text
            varItem = var(name, value, varType)
            varNode = getControlNodeByVarType(name, varType)
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
                         
                else:
                    if rhsNode.text == "BinaryExpr":
                        binExpNode = node.find("BinaryExpr")
                        if binExpNode is not None:
                            binExpDict = processBinaryExpr(binExpNode)
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
            
