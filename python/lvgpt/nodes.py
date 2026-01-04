import uuid
import xml.etree.ElementTree as ET

from .lvgraph import LVNode, FrontPanelControl, FrontPanelIndicator, MultiFrameTunnel, SelectorTunnel, ShiftRegister
from .lvgraph.tunnel import Tunnelable

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
    
class NumericConstant(LVNode):
    def __init__(self, name, numType):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Numeric Constant"
        self.attributes["numericType"] = numType
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
    

class StringIndicator(LVNode, FrontPanelIndicator):
    def __init__(self, name):
        LVNode.__init__(self, name)
        FrontPanelIndicator.__init__(self)
        self.attributes["type"] = "String Control"
        self.attributes["style"] = "String Indicator (modern)"
        self.isIndicator = True
        self.varType = "STRING"
        LVNode.addTerminal(self, name)
    
class SubVIFromPath(LVNode):
    def __init__(self, name, path):
        LVNode.__init__(self, name)
        self.attributes["type"] = "SubVIFromPath"
        self.attributes["path"] = path
    
class BoolConstant(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Boolean Constant"
        self.varType = "BOOL"
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = str(val)

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

    
class FormatIntoStringsNode(LVNode):
    def  __init__(self):
        LVNode.__init__(self, "fstr")
        LVNode.addTerminal(self, "input 1")
        LVNode.addTerminal(self, "format string")
        LVNode.addTerminal(self, "resulting string", False)
        self.attributes["type"] = "Format Into String"
        self.attributes["nodes"] = "1"
        self.attributes["defaultNodeCount"] = "1"
        self.attributes["genclass"] = "Growable Function"
    def getTerms(self):
        outputTerm = LVNode.getTerminalByName(self, "resulting string")
        return (None, None, outputTerm)
    def addTerminal(self):
        self.attributes["nodes"] = str(int(self.attributes["nodes"]) + 1)
        return LVNode.addTerminal(self, "input " + str(int(self.attributes["nodes"])))
    def getInputTerms(self):
        return [item for item in self.terminals.values() if "input" in item.name]
    
class PropertyNode(LVNode):
    def __init__(self):
        LVNode.__init__(self, "prop")
        # Add the standard terminals for a PropertyNode
        LVNode.addTerminal(self, "reference")
        LVNode.addTerminal(self, "error in (no error)")
        LVNode.addTerminal(self, "reference out", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Property Node"
        self.attributes["linkUUID"] = ""
        # Dictionary mapping property names to the corresponding property terminal's UUID.
        self.properties = {}  # e.g., {"prop1": "uuid1", "prop2": "uuid2"}

    def getTerms(self):
        # Return the standard terminals used for wiring the PropertyNode.
        ref = LVNode.getTerminalByName(self, "reference")
        error_in = LVNode.getTerminalByName(self, "error in (no error)")
        ref_out = LVNode.getTerminalByName(self, "reference out")
        error_out = LVNode.getTerminalByName(self, "error out")
        return (ref, error_in, ref_out, error_out)
    
    def setLinkUUID(self, linkUUID):
        self.attributes["linkUUID"] = linkUUID

    def addProperty(self, property_name, write_terminal=True, terminal_name=None):
        """
        Adds a new property to the node.
        
        Args:
            property_name (str): The name of the property.
            terminal_name (str, optional): The name of the terminal that will be created.
                                           If not provided, the property name is used.
        """
        if terminal_name is None:
            terminal_name = property_name

        # Only add the property if it isn't already present.
        if property_name not in self.properties:
            # Create a new terminal for this property.
            # Note: addTerminal() is inherited from LVNode. It creates a terminal,
            # adds it to self.terminals, and returns its UUID.
            terminal_uuid = self.addTerminal(terminal_name)
            termDir = "write" if write_terminal else "read"
            self.properties[property_name] = (terminal_uuid, termDir)
            return terminal_uuid

            # Update a node attribute that lists visible properties.
            # (Here we store a comma-separated list of property names.)
            # self.attributes["properties"] = ",".join(self.properties.keys())

    def setVisibleProperties(self, properties):
        """
        Sets which properties are visible on the node.
        
        Args:
            properties (list): A list of property definitions. Each entry can be either:
                - A string (in which case the property name and terminal name are the same), or
                - A tuple of (property_name, terminal_name) if they differ.
        """
        # Clear any existing properties.
        self.properties = {}
        for prop in properties:
            if isinstance(prop, tuple):
                self.addProperty(prop[0], prop[1])
            else:
                self.addProperty(prop)

    def writeNodeToXML(self, index):
        rootElem = ET.Element("node")
        rootElem.attrib["uuid"] = self.uuid
        
        # Create an XML element for properties.
        propertiesElem = ET.Element("properties")
        for property_name, attrs in self.properties.items():
            propertyElem = ET.Element("property")
            propertyElem.attrib["name"] = property_name
            # Include the terminal UUID so that downstream tools know which terminal represents this property.
            propertyElem.attrib["terminalUUID"] = attrs[0]
            propertyElem.attrib["direction"] = attrs[1]
            propertiesElem.append(propertyElem)
        rootElem.append(propertiesElem)
        
        # Append the node's attributes as XML attributes.
        for attrib in self.attributes:
            rootElem.attrib[attrib] = self.attributes[attrib]
        
        # Append terminals to the XML.
        terminalsElem = ET.Element("terminals")
        for term in self.terminals:
            termElem = ET.Element("terminal")
            termElem.attrib["id"] = self.terminals[term].uuid
            termElem.attrib["name"] = self.terminals[term].name
            terminalsElem.append(termElem)
        rootElem.append(terminalsElem)
        return rootElem
    
    
class InsertIntoArrayNode(LVNode):
    def __init__(self, nodeName):
        LVNode.__init__(self, nodeName)
        LVNode.addTerminal(self, "array", varType=None)
        LVNode.addTerminal(self, "index", varType="QUAD")
        LVNode.addTerminal(self, "new element/subarray", varType=None)
        LVNode.addTerminal(self, "output array", False)
        self.attributes["type"] = "Insert Into Array"
        self.attributes["genclass"] = "Growable Function"
        self.attributes["nodes"] = "1"
        self.attributes["defaultNodeCount"] = "1"
    def getTerms(self):
        inputTerm = LVNode.getTerminalByName(self, "array")
        positionTerm = LVNode.getTerminalByName(self, "index")
        newItemTerm = LVNode.getTerminalByName(self, "new element/subarray")
        outputTerm = LVNode.getTerminalByName(self, "output array")
        return (inputTerm, positionTerm, newItemTerm, outputTerm)
    
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
    
class Structure(LVNode, Tunnelable):
    def __init__(self, name):
        LVNode.__init__(self, name)
        Tunnelable.__init__(self)
        self.frames = {}
    def writeNodeToXML(self, index):
        rootElem = ET.Element("node")
        rootElem.attrib["uuid"] = self.uuid
        
        casesElem = ET.Element("frames")
        for subD in self.frames:
            caseElem = ET.Element("frame")
            caseElem.attrib["frameName"] = self.frames[subD]
            caseElem.attrib["frameUUID"] = subD
            casesElem.append(caseElem)
        rootElem.append(casesElem)
        tunnelsElem = ET.Element("tunnels")
        for tunnel in self.tunnels.values():
            tunnel.writeTunnelToXML(tunnelsElem)
        rootElem.append(tunnelsElem)
        for attrib in self.attributes:
            rootElem.attrib[attrib] = self.attributes[attrib]
        terminalsElem = ET.Element("terminals")
        for term in self.terminals.values():
            if not term.is_tunnel:
                term.writeTerminalToXML(terminalsElem)
        rootElem.append(terminalsElem)
        return rootElem

    
class MultipleDiagramStructure(Structure):
    def __init__(self, name):
        Structure.__init__(self, name)
    def addFrame(self, subDiagramCase):
        subDiagramUUID = str(uuid.uuid4())
        self.frames[subDiagramUUID] = subDiagramCase
        return subDiagramUUID
    def setDefaultFrame(self, subDiagramUUID):
        for x in range(0, len(self.frames)):
            if list(self.frames.keys())[x] == subDiagramUUID:
                self.attributes["default_case"] = str(x)

    def getFrameCount(self):
        return len(self.frames)
    
    def addTunnel(self):
        name = "tunnel" + str(len(self.tunnels))
        tunnel = MultiFrameTunnel(name, self)
        self.tunnels[name] = tunnel
        return tunnel
    
class CaseStructure(MultipleDiagramStructure):
    def __init__(self, name):
        MultipleDiagramStructure.__init__(self, name)
        self.attributes["type"] = "Case Structure"
        self.case_selector = SelectorTunnel(self)

    def addFrame(self, case_name):
        frame_uuid = MultipleDiagramStructure.addFrame(self, case_name)
        self.case_selector.addFrame(frame_uuid, self)
        return frame_uuid

    def getCaseSelectorExternal(self):
        return self.case_selector.external_terminal
    def getCaseSelectorInternal(self):
        return self.case_selector.terminals_internal
    
    def writeNodeToXML(self, index):
        nodeElem = super().writeNodeToXML(index)
        tunnelsElem = nodeElem.find("tunnels")
        self.case_selector.writeTunnelToXML(tunnelsElem)
        return nodeElem

class Loop(Structure, Tunnelable):
    def __init__(self, name):
        Structure.__init__(self, name)
        Tunnelable.__init__(self)
        self.shift_registers = {}

    def addShiftRegister(self, yPos):
        name = "sr" + str(len(self.shift_registers))
        shift_register = ShiftRegister(name, yPos, self)
        self.shift_registers[name] = shift_register
        return shift_register
    
    def writeNodeToXML(self, index):
        nodeElem = super().writeNodeToXML(index)
        if len(self.shift_registers) > 0:
            shiftRegElem = ET.Element("shift_registers")
            for sr in self.shift_registers:
                self.shift_registers[sr].writeTunnelToXML(shiftRegElem)
            nodeElem.append(shiftRegElem)
        return nodeElem
        
    
class ForLoop(Loop):
    def __init__(self, name):
        Loop.__init__(self, name)
        self.attributes["type"] = "For Loop"
        LVNode.addTerminal(self, "Next", varType="INT32")  # Iteration Count
        LVNode.addTerminal(self, "Nint", isInput=False, varType="INT32")  # Current Iteration
        LVNode.addTerminal(self, "i", isInput=False, varType="INT32")  # Current Iteration
        self.attributes["cond_term"] = "False"
        subDiagramUUID = str(uuid.uuid4())
        self.frames[subDiagramUUID] = "main"

    def enableConditionalTerminal(self):
        self.attributes["cond_term"] = "True"
        LVNode.addTerminal(self, "conditional terminal", varType="BOOL")

    def getNTerm(self):
        return LVNode.getTerminalByName(self, "N")
    def getITerm(self):
        return LVNode.getTerminalByName(self, "i")
    def getSubdiagram(self):
        return list(self.frames.keys())[0]
    

class WhileLoop(Loop):
    def __init__(self, name):
        Loop.__init__(self, name)
        self.attributes["type"] = "While Loop"
        self.attributes["style"] = "While Loop #1"
        LVNode.addTerminal(self, "conditional terminal", varType="BOOL")
        LVNode.addTerminal(self, "i", isInput=False, varType="INT32")  # Current Iteration
        subDiagramUUID = str(uuid.uuid4())
        self.frames[subDiagramUUID] = "main"
    def getConditionalTerminal(self):
        return LVNode.getTerminalByName(self, "conditional terminal")
    def getITerm(self):
        return LVNode.getTerminalByName(self, "i")
    def getSubdiagram(self):
        return list(self.frames.keys())[0]

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
