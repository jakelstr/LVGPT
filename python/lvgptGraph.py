import uuid

class LVGraph:
    def __init__(self):
        #nodes is nodeUUID->LVNode, terminals is terminalUUID->nodeUUID, nodeNames is nodeName->nodeUUID
        self.graph = {"nodes":{}, "terminals":{}, "nodeNames":{}}
        self.diagramUUID = ""

    def addNode(self, node):
        if node.name in self.graph["nodeNames"]:
            return False
        else:
            node.attributes["parentDiagram"] = self.diagramUUID
            self.graph["nodeNames"][node.name] = node.uuid
            self.graph["nodes"][node.uuid] = node
            for termUUID in node.terminals:
                self.graph["terminals"][termUUID] = node.uuid
        return True
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


class terminal:
    def __init__(self, name):
        self.uuid = str(uuid.uuid4())
        self.name = name
        self.isInput = True
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
        self.varType = "NULL"

    def addTerminal(self, name, isInput=True):
        term = terminal(name)
        term.isInput = isInput
        self.terminals[term.uuid] = term
        return term.uuid

    def getTerminalByName(self, name):
        for t in self.terminals:
            if self.terminals[t].name == name:
                return self.terminals[t]
        return None


class NumericControl(LVNode):
    def __init__(self, name, numType):
        LVNode.__init__(self, name)
        LVNode.addTerminal(self, name, False)
        self.attributes["type"] = "Numeric Control"
        self.attributes["numericType"] = numType
        self.varType = numType
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
        self.varType = numType
        self.isIndicator = True
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)
    
class StringControl(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        LVNode.addTerminal(self, name, False)
        self.attributes["type"] = "String Control"
        self.varType = "STRING"
    def setValue(self, val):
        self.attributes["value"] = val
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)
    
class StringConstant(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        LVNode.addTerminal(self, name, False)
        self.attributes["type"] = "String Constant"
        self.varType = "STRING"
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
        self.varType = "STRING"
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
        outputTerm = LVNode.getTerminalByName(self, "concatenated string")
        return (None, None, outputTerm)
    def addTerminal(self):
        self.attributes["nodes"] = str(int(self.attributes["nodes"]) + 1)
        return LVNode.addTerminal(self, "input " + str(int(self.attributes["nodes"])))
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
    return LVNode(varName)