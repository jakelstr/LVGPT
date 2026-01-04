from .node import LVNode
import xml.etree.ElementTree as ET

class NumericConstant(LVNode):
    def __init__(self, name, numType):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Numeric Constant"
        self.attributes["numericType"] = numType
        self.varType = numType
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = str(val)

class StringConstant(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "String Constant"
        self.varType = "STRING"
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = val

class ClassSpecifierConstant(LVNode):
    def __init__(self, name, id_string):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Class Specifier Constant"
        self.attributes["id_string"] = id_string
        LVNode.addTerminal(self, name, False)
    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)
    
class BoolConstant(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Boolean Constant"
        self.varType = "BOOL"
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = str(val)

class ArrayConstant(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Array Constant"
        self.attributes["style"] = "Array (block diagram constant)"
        LVNode.addTerminal(self, name, True)
        self.value = []
        self.childNode = None

    def setChildNode(self, childNode):
        childNode.terminals = {}
        childNode.terminals_by_name = {}
        self.childNode = childNode

    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)
    
    def setValue(self, index, val):
        if index >= 0:
            if index == len(self.value):
                #this is a new element at the end, so append
                self.value.append(val)
            elif index < len(self.value):
                self.value[index] = val

    def setValue(self, array):
        array_len = len(array)
        for x in range(array_len):
            self.setValue(x, array[x])
    
    def writeNodeToXML(self, index):
        rootElem = ET.Element("node")
        rootElem.attrib["uuid"] = self.uuid
        
        valuesElem = ET.Element("values")
        for v in self.value:
            valueElem = ET.Element("value")
            valueElem.text = v
            valuesElem.append(valueElem)
        rootElem.append(valuesElem)
        childElem = ET.Element("child")
        if self.childNode is not None:
            childElem.append(self.childNode.writeNodeToXML(0))
        rootElem.append(childElem)
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