from .node import LVNode, FrontPanelControl, FrontPanelIndicator
import xml.etree.ElementTree as ET

class NumericControl(LVNode, FrontPanelControl):
    def __init__(self, name, numType):
        LVNode.__init__(self, name)
        FrontPanelControl.__init__(self)
        self.attributes["type"] = "Numeric Control"
        self.attributes["numericType"] = numType
        self.attributes["style"] = "Numeric Control (modern)"
        self.varType = numType
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = str(val)

class NumericIndicator(LVNode, FrontPanelIndicator):
    def __init__(self, name, numType):
        LVNode.__init__(self, name)
        FrontPanelIndicator.__init__(self)
        self.attributes["type"] = "Numeric Control"
        self.attributes["numericType"] = numType
        self.attributes["style"] = "Numeric Indicator (modern)"
        self.varType = numType
        self.isIndicator = True
        LVNode.addTerminal(self, name)
    
class StringControl(LVNode, FrontPanelControl):
    def __init__(self, name):
        LVNode.__init__(self, name)
        FrontPanelControl.__init__(self)
        self.attributes["type"] = "String Control"
        self.attributes["style"] = "String Control (modern)"
        self.varType = "STRING"
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = val

class StringIndicator(LVNode, FrontPanelIndicator):
    def __init__(self, name):
        LVNode.__init__(self, name)
        FrontPanelIndicator.__init__(self)
        self.attributes["type"] = "String Control"
        self.attributes["style"] = "String Indicator (modern)"
        self.isIndicator = True
        self.varType = "STRING"
        LVNode.addTerminal(self, name)

class BoolControl(LVNode, FrontPanelControl):
    def __init__(self, name):
        LVNode.__init__(self, name)
        FrontPanelControl.__init__(self)
        self.attributes["type"] = "Bool Control"
        self.attributes["style"] = "Push Button"
        self.varType = "BOOL"
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = str(val)
    
class BoolIndicator(LVNode, FrontPanelIndicator):
    def __init__(self, name):
        LVNode.__init__(self, name)
        FrontPanelIndicator.__init__(self)
        self.attributes["type"] = "Bool Control"
        self.attributes["style"] = "Round LED (modern)"
        self.isIndicator = True
        self.varType = "BOOL"
        LVNode.addTerminal(self, name)

class ArrayControl(LVNode, FrontPanelControl):
    def __init__(self, name):
        LVNode.__init__(self, name)
        FrontPanelControl.__init__(self)
        self.attributes["type"] = "Array Control"
        self.attributes["style"] = "Array (modern)"
        LVNode.addTerminal(self, name, False)
        self.value = []
        self.childNode = None

    def setChildNode(self, childNode):
        childNode.terminals = {}
        childNode.terminals_by_name = {}
        self.childNode = childNode

    def setValue(self, array):
        self.value = array

    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)
    
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
            self.childNode.attributes["xPos"] = self.attributes["xPos"]
            self.childNode.attributes["yPos"] = self.attributes["yPos"]
            self.childNode.attributes["FPxPos"] = self.attributes["FPxPos"]
            self.childNode.attributes["FPyPos"] = self.attributes["FPyPos"]
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
    
class ArrayIndicator(LVNode, FrontPanelIndicator):
    def __init__(self, name):
        LVNode.__init__(self, name)
        FrontPanelIndicator.__init__(self)
        self.attributes["type"] = "Array Control"
        self.attributes["style"] = "Array (modern)"
        LVNode.addTerminal(self, name, True)
        self.value = []
        self.childNode = None

    def setChildNode(self, childNode):
        childNode.terminals = {}
        childNode.terminals_by_name = {}
        self.childNode = childNode

    def getTerminal(self):
        return LVNode.getTerminalByName(self, self.name)
    
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
            self.childNode.attributes["xPos"] = self.attributes["xPos"]
            self.childNode.attributes["yPos"] = self.attributes["yPos"]
            self.childNode.attributes["FPxPos"] = self.attributes["FPxPos"]
            self.childNode.attributes["FPyPos"] = self.attributes["FPyPos"]
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
        # case "1DSTRINGARRAY":
        #     return StringArrayIndicator(varName)
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
        # case "STRING":
        #     return StringArrayControl(varName)
        case "BOOL":
            return BoolControl(varName)
    return LVNode(varName)
