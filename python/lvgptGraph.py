import uuid
import xml.etree.ElementTree as ET

class LVGraph:
    def __init__(self):
        #nodes is nodeUUID->LVNode, terminals is terminalUUID->nodeUUID, nodeNames is nodeName->nodeUUID
        self.graph = {"nodes":{}, "terminals":{}, "nodeNames":{}, "symbolTable":{}}
        self.diagramUUID = ""

    def addNode(self, node):
        if node.name in self.graph["nodeNames"]:
            node.name = self.getAvailableNodeName(node.name)
        node.attributes["parentDiagram"] = self.diagramUUID
        self.graph["nodeNames"][node.name] = node.uuid
        self.graph["nodes"][node.uuid] = node
        for termUUID in node.terminals:
            self.graph["terminals"][termUUID] = node.uuid
        
    def getAvailableNodeName(self, desiredName):
        if desiredName not in self.graph["nodeNames"]:
            return desiredName
        else:
            counter = 2
            found = False
            while not found:
                testName = desiredName + str(counter)
                if testName not in self.graph["nodeNames"]:
                    return testName
                else:
                    counter = counter + 1
    def getTerminalOwner(self, terminalUUID):
        return self.graph["terminals"][terminalUUID]
    def getNodeByName(self, nodeName):
        return self.graph["nodeNames"][nodeName]
    def getNodeByUUID(self, nodeUUID):
        return self.graph["nodes"][nodeUUID]
    def addTerminalEdge(self, term1UUID, term2UUID):
        term1OwnerUUID = self.graph["terminals"][term1UUID]
        term2OwnerUUID = self.graph["terminals"][term2UUID]
        term1Owner = self.graph["nodes"][term1OwnerUUID]
        term2Owner = self.graph["nodes"][term2OwnerUUID]
        term1 = term1Owner.terminals[term1UUID]
        term2 = term2Owner.terminals[term2UUID]
        term1.edges.append(term2UUID)
        term2.edges.append(term1UUID)
    def setDiagram(self, diagramUUID):
        self.diagramUUID = diagramUUID

    def getWires(self):
        wires = []
        for nUUID in self.graph["nodes"]:
            n = self.graph["nodes"][nUUID]
            for tUUID, t in n.terminals.items():
                for e in t.edges:
                    foreignNodeUUID = self.getTerminalOwner(e)
                    foreignNode = self.graph["nodes"][foreignNodeUUID]
                    foreignNode.terminals[e].edges.remove(t.uuid)
                    edgeWire = wire(t.uuid, e)
                    wires.append(edgeWire)
        return wires
    
    def deleteNode(self, nodeUUID):
        node = self.graph["nodes"][nodeUUID]
        for i, t in node.terminals.items():
            for e in t.edges:
                foreignNodeUUID = self.getTerminalOwner(e)
                foreignNode = self.getNodeByUUID(foreignNodeUUID)
                foreignNode.terminals[e].edges.remove(t.uuid)
        del self.graph["nodes"][nodeUUID]

    def addTerminalToNode(self, nodeUUID):
        node = self.graph["nodes"][nodeUUID]
        termUUID = node.addTerminal()
        self.graph["terminals"][termUUID] = nodeUUID

    def addSymbolTableEntry(self, symbolName, terminalUUID):
        if self.diagramUUID not in self.graph["symbolTable"]:
            self.graph["symbolTable"][self.diagramUUID] = {}
        self.graph["symbolTable"][self.diagramUUID][symbolName] = terminalUUID
    
    def getTerminalFromSymbolTable(self, symbolName):
        return self.graph["symbolTable"][self.diagramUUID][symbolName]
    
    def setTerminalVarType(self, terminalUUID, varType):
        parentNode = self.getNodeByUUID(self.getTerminalOwner(terminalUUID))
        parentNode.terminals[terminalUUID].varType = varType

    def getTerminalVarType(self, terminalUUID):
        parentNode = self.getNodeByUUID(self.getTerminalOwner(terminalUUID))
        return parentNode.terminals[terminalUUID].varType


class terminal:
    def __init__(self, name):
        self.uuid = str(uuid.uuid4())
        self.name = name
        self.isInput = True
        self.edges = []
        self.varType = None
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
        self.varType = None

    def addTerminal(self, name, isInput=True, varType=None):
        term = terminal(name)
        term.isInput = isInput
        if varType is None:
            term.varType = self.varType
        else:
            term.varType = varType
        self.terminals[term.uuid] = term
        return term.uuid

    def getTerminalByName(self, name):
        for t in self.terminals:
            if self.terminals[t].name == name:
                return self.terminals[t]
        return None
    
    def writeNodeToXML(self, index):
        rootElem = ET.Element("node")
        rootElem.attrib["xPos"] = "0"
        rootElem.attrib["yPos"] = str(index * 50)
        if hasattr(self, "value") and self.value is not None:
            rootElem.attrib["value"] = self.value
        for attrib in self.attributes:
            rootElem.attrib[attrib] = self.attributes[attrib]
        terminalsElem = ET.Element("terminals")
        for term in self.terminals:
            termElem = ET.Element("terminal")
            termElem.attrib["id"] = self.terminals[term].uuid
            termElem.attrib["name"] = self.terminals[term].name
            terminalsElem.append(termElem)
        rootElem.append(terminalsElem)
        return rootElem


class NumericControl(LVNode):
    def __init__(self, name, numType):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Numeric Control"
        self.attributes["numericType"] = numType
        self.varType = numType
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = val
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)
    
class NumericConstant(LVNode):
    def __init__(self, name, numType):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Numeric Constant"
        self.attributes["numericType"] = numType
        self.varType = numType
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = val
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)

class NumericIndicator(LVNode):
    def __init__(self, name, numType):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Numeric Indicator"
        self.attributes["numericType"] = numType
        self.varType = numType
        self.isIndicator = True
        LVNode.addTerminal(self, name)
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)
    
class StringControl(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "String Control"
        self.varType = "STRING"
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = val
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)
    
class StringConstant(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "String Constant"
        self.varType = "STRING"
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = val
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)

class StringIndicator(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "String Indicator"
        self.isIndicator = True
        self.varType = "STRING"
        LVNode.addTerminal(self, name)
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)
    
class BoolConstant(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Bool Constant"
        self.varType = "BOOL"
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = val
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)

class BoolControl(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Bool Control"
        self.varType = "BOOL"
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = val
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)
    
class BoolIndicator(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Bool Indicator"
        self.isIndicator = True
        self.varType = "BOOL"
        LVNode.addTerminal(self, name)
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)

class AddNode(LVNode):
    def  __init__(self):
        LVNode.__init__(self, "add")
        LVNode.addTerminal(self, "x")
        LVNode.addTerminal(self, "y")
        LVNode.addTerminal(self, "x+y", False)
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
        LVNode.addTerminal(self, "x*y", False)
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
        LVNode.addTerminal(self, "x-y", False)
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
        LVNode.addTerminal(self, "x/y", False)
        self.attributes["type"] = "Divide"
    def getTerms(self):
        outputTerm = LVNode.getTerminalByName(self, "x/y")
        leftTerm = LVNode.getTerminalByName(self, "x")
        rightTerm = LVNode.getTerminalByName(self, "y")
        return (leftTerm, rightTerm, outputTerm)
    
class GreaterOrEqualNode(LVNode):
    def  __init__(self):
        LVNode.__init__(self, "divide")
        LVNode.addTerminal(self, "x")
        LVNode.addTerminal(self, "y")
        LVNode.addTerminal(self, "x >= y?", False, "BOOL")
        self.attributes["type"] = "Greater Or Equal"
    def getTerms(self):
        outputTerm = LVNode.getTerminalByName(self, "x >= y?")
        leftTerm = LVNode.getTerminalByName(self, "x")
        rightTerm = LVNode.getTerminalByName(self, "y")
        return (leftTerm, rightTerm, outputTerm)

class ConcatenateStringsNode(LVNode):
    def  __init__(self):
        LVNode.__init__(self, "concat")
        LVNode.addTerminal(self, "string")
        LVNode.addTerminal(self, "string")
        LVNode.addTerminal(self, "concatenated string", False)
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
        LVNode.addTerminal(self, "resulting string", False)
        self.attributes["type"] = "Format Into String"
        self.attributes["nodes"] = "1"
    def getTerms(self):
        outputTerm = LVNode.getTerminalByName(self, "resulting string")
        return (None, None, outputTerm)
    def addTerminal(self):
        self.attributes["nodes"] = str(int(self.attributes["nodes"]) + 1)
        return LVNode.addTerminal(self, "input " + str(int(self.attributes["nodes"])))
    def getInputTerms(self):
        return [item for item in self.terminals.values() if "input" in item.name]
    
class SelectNode(LVNode):
    def __init__(self):
        LVNode.__init__(self, "select")
        LVNode.addTerminal(self, "t")
        LVNode.addTerminal(self, "s", varType="BOOL")
        LVNode.addTerminal(self, "f")
        LVNode.addTerminal(self, "s? t:f", False)
        self.attributes["type"] = "Select"
    def getTerms(self):
        trueTerm = LVNode.getTerminalByName(self, "t")
        selectorTerm = LVNode.getTerminalByName(self, "s")
        falseTerm = LVNode.getTerminalByName(self, "f")
        outputTerm = LVNode.getTerminalByName(self, "s? t:f")
        return (trueTerm, selectorTerm, falseTerm, outputTerm)
    
class InsertIntoArrayNode(LVNode):
    def __init__(self, nodeName):
        LVNode.__init__(self, nodeName)
        LVNode.addTerminal(self, "n-dim array", varType=None)
        LVNode.addTerminal(self, "index 0", varType="QUAD")
        LVNode.addTerminal(self, "n or n-1 dim array", varType=None)
        LVNode.addTerminal(self, "output array", False)
        self.attributes["type"] = "Insert Into Array"
    def getTerms(self):
        inputTerm = LVNode.getTerminalByName(self, "n-dim array")
        positionTerm = LVNode.getTerminalByName(self, "index 0")
        newItemTerm = LVNode.getTerminalByName(self, "n or n-1 dim array")
        outputTerm = LVNode.getTerminalByName(self, "output array")
        return (inputTerm, positionTerm, newItemTerm, outputTerm)
    
class StringArrayControl(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "String Array Control"
        self.varType = "1DSTRINGARRAY"
        LVNode.addTerminal(self, name, False)
        self.value = []
    def setValue(self, index, val):
        if index >= 0:
            if index == len(self.value):
                #this is a new element at the end, so append
                self.value.append(val)
            elif index < len(self.value):
                self.value[index] = val

    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)
    
    def writeNodeToXML(self, index):
        rootElem = ET.Element("node")
        rootElem.attrib["xPos"] = "0"
        rootElem.attrib["yPos"] = str(index * 50)
        
        valuesElem = ET.Element("values")
        for v in self.value:
            valueElem = ET.Element("value")
            valueElem.text = v
            valuesElem.append(valueElem)
        rootElem.append(valuesElem)
        for attrib in self.attributes:
            rootElem.attrib[attrib] = self.attributes[attrib]
        terminalsElem = ET.Element("terminals")
        for term in self.terminals:
            termElem = ET.Element("terminal")
            termElem.attrib["id"] = self.terminals[term].uuid
            termElem.attrib["name"] = self.terminals[term].name
            terminalsElem.append(termElem)
        rootElem.append(terminalsElem)
        return rootElem
    
class StringArrayIndicator(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "String Array Indicator"
        self.varType = "1DSTRINGARRAY"
        LVNode.addTerminal(self, name, True)
        self.value = []

    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)
    
    def writeNodeToXML(self, index):
        rootElem = ET.Element("node")
        rootElem.attrib["xPos"] = "0"
        rootElem.attrib["yPos"] = str(index * 50)
        
        valuesElem = ET.Element("values")
        for v in self.value:
            valueElem = ET.Element("value")
            valueElem.text = v
            valuesElem.append(valueElem)
        rootElem.append(valuesElem)
        for attrib in self.attributes:
            rootElem.attrib[attrib] = self.attributes[attrib]
        terminalsElem = ET.Element("terminals")
        for term in self.terminals:
            termElem = ET.Element("terminal")
            termElem.attrib["id"] = self.terminals[term].uuid
            termElem.attrib["name"] = self.terminals[term].name
            terminalsElem.append(termElem)
        rootElem.append(terminalsElem)
        return rootElem
    
class CaseSelector(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Case Structure"
        LVNode.addTerminal(self, "case selector external")
        LVNode.addTerminal(self, "case selector internal")
        self.subdiagrams = {}
        self.printTunnels = {}

    def getCaseSelectorExternal(self):
        return LVNode.getTerminalByName(self, "case selector external")
    def getCaseSelectorInternal(self):
        return LVNode.getTerminalByName(self, "case selector internal")
    def addSubdiagram(self, subDiagramCase):
        subDiagramUUID = str(uuid.uuid4())
        self.subdiagrams[subDiagramUUID] = subDiagramCase
        return subDiagramUUID
    def addPrintTunnel(self, terminalUUID, caseUUID):
        if caseUUID in self.printTunnels:
            self.printTunnels[caseUUID].append(terminalUUID)
        else:
            self.printTunnels[caseUUID] = [terminalUUID]

    def writeNodeToXML(self, index):
        rootElem = ET.Element("node")
        rootElem.attrib["xPos"] = "0"
        rootElem.attrib["yPos"] = str(index * 50)
        
        casesElem = ET.Element("cases")
        for subD in self.subdiagrams:
            caseElem = ET.Element("case")
            caseElem.attrib["caseName"] = self.subdiagrams[subD]
            caseElem.attrib["caseUUID"] = subD
            casesElem.append(caseElem)
        rootElem.append(casesElem)
        for attrib in self.attributes:
            rootElem.attrib[attrib] = self.attributes[attrib]
        terminalsElem = ET.Element("terminals")
        for term in self.terminals:
            termElem = ET.Element("terminal")
            termElem.attrib["id"] = self.terminals[term].uuid
            termElem.attrib["name"] = self.terminals[term].name
            terminalsElem.append(termElem)
        rootElem.append(terminalsElem)
        return rootElem
    

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
        case "BOOL":
            return BoolControl(varName)
    return LVNode(varName)

def getConstantNodeByVarType(varName, varType):
    match varType.upper():
        case "INT":
            return NumericConstant(varName, "Quad")
        case "INT8":
            return NumericConstant(varName, "Byte")
        case "INT16":
            return NumericConstant(varName, "Word")
        case "INT32":
            return NumericConstant(varName, "Long")
        case "INT64":
            return NumericConstant(varName, "Quad")
        case "UINT":
            return NumericConstant(varName, "Unsigned Quad")
        case "UINT8":
            return NumericConstant(varName, "Unsigned Byte")
        case "UINT16":
            return NumericConstant(varName, "Unsigned Word")
        case "UINT32":
            return NumericConstant(varName, "Unsigned Long")
        case "UINT64":
            return NumericConstant(varName, "Unsigned Quad")
        case "FLOAT32":
            return NumericConstant(varName, "Single Precision")
        case "FLOAT64":
            return NumericConstant(varName, "Double Precision")
        case "STRING":
            return StringConstant(varName)
        case "BOOL":
            return BoolConstant(varName)
    return LVNode(varName)

def getIndicatorNodeByVarType(varName, varType):
    match varType.upper():
        case "INT" | "QUAD":
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
        case "1DSTRINGARRAY":
            return StringArrayIndicator(varName)
        case "BOOL":
            return BoolIndicator(varName)
    return LVNode(varName)

def getArrayControlNodeByVarType(varName, varType):
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
            return StringArrayControl(varName)
        case "BOOL":
            return BoolControl(varName)
    return LVNode(varName)
