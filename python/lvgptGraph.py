import uuid
import xml.etree.ElementTree as ET

class LVGraph:
    def __init__(self):
        #nodes is nodeUUID->LVNode, terminals is terminalUUID->nodeUUID, nodeNames is nodeName->nodeUUID
        self.graph = {"nodes":{}, "terminals":{}, "nodeNames":{}, "symbolTable":{}}
        self.diagramUUID = str(uuid.uuid4())
        self.baseDiagram = self.diagramUUID
        self.symbolTable = SymbolTable()

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

    def addTerminalToNode(self, nodeUUID, terminalName=None):
        node = self.graph["nodes"][nodeUUID]
        termUUID = None
        if terminalName is not None:
            termUUID = node.addTerminal(terminalName)
        else:
            termUUID = node.addTerminal()
        self.graph["terminals"][termUUID] = nodeUUID
        return termUUID

    def addSymbolTableEntry(self, symbolName, terminalUUID):
        if self.diagramUUID == self.baseDiagram:
            self.symbolTable.children[symbolName] = terminalUUID
        else:
            if self.diagramUUID in self.symbolTable.children:
                subTable = self.symbolTable.children[self.diagramUUID]
                subTable.children[symbolName] = terminalUUID

    def addSubSymbolTable(self, subDiagramUUID, parentTable=None):
        if parentTable is None:
            parentTable = self.symbolTable
        self.symbolTable.children[subDiagramUUID] = SymbolTable(parentTable)
    
    def getTerminalFromSymbolTable(self, symbolName):
        symbolObj = None
        #is there a subtable for this diagramUUID?
        if self.diagramUUID in self.symbolTable.children:
            subTable = self.symbolTable.children[self.diagramUUID]
            if symbolName in subTable.children:
                symbolObj = subTable.children[symbolName]
            else:
                #if the symbol doesn't exist in the subtable, look upward
                parentTable = subTable.parentTable
                if symbolName in parentTable.children:
                    symbolObj = parentTable.children[symbolName]
        else:
            if symbolName in self.symbolTable.children:
                symbolObj = self.symbolTable.children[symbolName]
        return symbolObj
    
    def setTerminalVarType(self, terminalUUID, varType):
        parentNode = self.getNodeByUUID(self.getTerminalOwner(terminalUUID))
        parentNode.terminals[terminalUUID].varType = varType

    def getTerminalVarType(self, terminalUUID):
        parentNode = self.getNodeByUUID(self.getTerminalOwner(terminalUUID))
        return parentNode.terminals[terminalUUID].varType
    

class SymbolTable:
    def __init__(self, parentTable=None):
        self.parentTable = parentTable
        self.children= {}


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
        self.terminals_by_name = {}
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
        self.terminals_by_name[name] = term
        return term.uuid

    def getTerminalByName(self, name):
        term = self.terminals_by_name.get(name)
        return term
    
    def getTerminal(self):
        # If you designate a “primary” terminal, you might choose one here.
        # For example, return the first terminal added.
        if self.terminals:
            return list(self.terminals.values())[0]
        return None
    
    def __getitem__(self, key):
        # Allow simple lookup via node["terminalName"]
        return self.getTerminalByName(key)
    
    def writeNodeToXML(self, index):
        rootElem = ET.Element("node")
        rootElem.attrib["xPos"] = "0"
        rootElem.attrib["yPos"] = str(index * 50)
        rootElem.attrib["uuid"] = self.uuid
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

class LoopNode(LVNode):
    def __init__(self):
        LVNode.__init__(self, "loop")
        self.attributes["type"] = "While Loop"
        LVNode.addTerminal(self, "condition", varType="BOOL")
        LVNode.addTerminal(self, "loop body")
        LVNode.addTerminal(self, "output", False, "VOID")
    
    def getConditionTerminal(self):
        return self.terminals["condition"]
    
    def getBodyTerminal(self):
        return self.terminals["loop body"]

class RangeLoopNode(LVNode):
    def __init__(self):
        LVNode.__init__(self, "range_loop")
        self.attributes["type"] = "For Loop"
        LVNode.addTerminal(self, "iterable", varType="ARRAY")
        LVNode.addTerminal(self, "loop variable")
        LVNode.addTerminal(self, "loop body")
        self.varType = "ARRAY"
    
    def getIterableTerminal(self):
        return self.terminals["iterable"]
    
    def getLoopVariableTerminal(self):
        return self.terminals["loop variable"]
    
    def getBodyTerminal(self):
        return self.terminals["loop body"]

class NumericControl(LVNode):
    def __init__(self, name, numType):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Numeric Control"
        self.attributes["numericType"] = numType
        self.attributes["style"] = "Numeric Control (modern)"
        self.varType = numType
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = val
    
class NumericConstant(LVNode):
    def __init__(self, name, numType):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Numeric Constant"
        self.attributes["numericType"] = numType
        self.varType = numType
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = val

class NumericIndicator(LVNode):
    def __init__(self, name, numType):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Numeric Control"
        self.attributes["numericType"] = numType
        self.attributes["style"] = "Numeric Indicator (modern)"
        self.varType = numType
        self.isIndicator = True
        LVNode.addTerminal(self, name)
    
class StringControl(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
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
    
class ToMoreSpecificClass(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "To More Specific Class"
        self.attributes["genclass"] = "Function"
        LVNode.addTerminal(self, "specific class reference", varType="reference", isInput=False)
        LVNode.addTerminal(self, "reference", varType="reference")
        LVNode.addTerminal(self, "target class", varType="reference")
        LVNode.addTerminal(self, "error in", varType="error")
        LVNode.addTerminal(self, "error out", varType="error", isInput=False)
    def getTerms(self):
        targetClass = LVNode.getTerminalByName(self, "target class")
        reference = LVNode.getTerminalByName(self, "reference")
        specificClass = LVNode.getTerminalByName(self, "specific class reference")
        errorIn = LVNode.getTerminalByName(self, "error in")
        errorOut = LVNode.getTerminalByName(self, "error out")
        return (targetClass, reference, specificClass, errorIn, errorOut)
    
class VariantToData(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Variant To Data"
        self.attributes["genclass"] = "Function"
        LVNode.addTerminal(self, "variant", varType="variant")
        LVNode.addTerminal(self, "type", varType="reference")
        LVNode.addTerminal(self, "data", varType="reference", isInput=False)
        LVNode.addTerminal(self, "error in", varType="error")
        LVNode.addTerminal(self, "error out", varType="error", isInput=False)

class NewVIObject(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "New VI Object"
        self.attributes["genclass"] = "Function"
        LVNode.addTerminal(self, "owner refnum", varType="reference")
        LVNode.addTerminal(self, "style")
        LVNode.addTerminal(self, "location")
        LVNode.addTerminal(self, "vi object class")
        LVNode.addTerminal(self, "auto wire? (F)")
        LVNode.addTerminal(self, "path")
        LVNode.addTerminal(self, "bounds")
        LVNode.addTerminal(self, "object refnum", varType="reference", isInput=False)
        LVNode.addTerminal(self, "error in", varType="error")
        LVNode.addTerminal(self, "error out", varType="error", isInput=False)
    
class LookInMap(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Look In Map"
        self.attributes["genclass"] = "Function"
        LVNode.addTerminal(self, "map")
        LVNode.addTerminal(self, "key")
        LVNode.addTerminal(self, "default value")
        LVNode.addTerminal(self, "key not found?", isInput=False)
        LVNode.addTerminal(self, "value", isInput=False)


class StringIndicator(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
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
        self.attributes["type"] = "Bool Constant"
        self.varType = "BOOL"
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = val

class BoolControl(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Bool Control"
        self.attributes["style"] = "Push Button"
        self.varType = "BOOL"
        LVNode.addTerminal(self, name, False)
    def setValue(self, val):
        self.value = val
    
class BoolIndicator(LVNode):
    def __init__(self, name):
        LVNode.__init__(self, name)
        self.attributes["type"] = "Bool Control"
        self.attributes["style"] = "LED Button"
        self.isIndicator = True
        self.varType = "BOOL"
        LVNode.addTerminal(self, name)

class AddNode(LVNode):
    def  __init__(self):
        LVNode.__init__(self, "add")
        LVNode.addTerminal(self, "x")
        LVNode.addTerminal(self, "y")
        LVNode.addTerminal(self, "x+y", False)
        self.attributes["type"] = "Add"
        self.attributes["genclass"] = "Function"
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
        self.attributes["genclass"] = "Function"
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
        self.attributes["genclass"] = "Function"
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
        self.attributes["genclass"] = "Function"
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
        self.attributes["genclass"] = "Function"
    def getTerms(self):
        outputTerm = LVNode.getTerminalByName(self, "x >= y?")
        leftTerm = LVNode.getTerminalByName(self, "x")
        rightTerm = LVNode.getTerminalByName(self, "y")
        return (leftTerm, rightTerm, outputTerm)
class EqualNode(LVNode):
    def __init__(self):
        LVNode.__init__(self, "equal")
        LVNode.addTerminal(self, "x")
        LVNode.addTerminal(self, "y")
        LVNode.addTerminal(self, "x = y?", False, "BOOL")
        self.attributes["type"] = "Equal?"
        self.attributes["genclass"] = "Function"
    
    def getTerms(self):
        outputTerm = self.getTerminalByName("x == y?")
        leftTerm = self.getTerminalByName("x")
        rightTerm = self.getTerminalByName("y")
        return (leftTerm, rightTerm, outputTerm)

class NotEqualNode(LVNode):
    def __init__(self):
        LVNode.__init__(self, "not_equal")
        LVNode.addTerminal(self, "x")
        LVNode.addTerminal(self, "y")
        LVNode.addTerminal(self, "x != y?", False, "BOOL")
        self.attributes["type"] = "Not Equal?"
        self.attributes["genclass"] = "Function"
    
    def getTerms(self):
        outputTerm = self.getTerminalByName("x != y?")
        leftTerm = self.getTerminalByName("x")
        rightTerm = self.getTerminalByName("y")
        return (leftTerm, rightTerm, outputTerm)

class GreaterThanNode(LVNode):
    def __init__(self):
        LVNode.__init__(self, "greater_than")
        LVNode.addTerminal(self, "x")
        LVNode.addTerminal(self, "y")
        LVNode.addTerminal(self, "x > y?", False, "BOOL")
        self.attributes["type"] = "Greater Than?"
        self.attributes["genclass"] = "Function"
    
    def getTerms(self):
        outputTerm = self.getTerminalByName("x > y?")
        leftTerm = self.getTerminalByName("x")
        rightTerm = self.getTerminalByName("y")
        return (leftTerm, rightTerm, outputTerm)

class LessThanNode(LVNode):
    def __init__(self):
        LVNode.__init__(self, "less_than")
        LVNode.addTerminal(self, "x")
        LVNode.addTerminal(self, "y")
        LVNode.addTerminal(self, "x < y?", False, "BOOL")
        self.attributes["type"] = "Less Than?"
        self.attributes["genclass"] = "Function"
    
    def getTerms(self):
        outputTerm = self.getTerminalByName("x < y?")
        leftTerm = self.getTerminalByName("x")
        rightTerm = self.getTerminalByName("y")
        return (leftTerm, rightTerm, outputTerm)

class LessOrEqualNode(LVNode):
    def __init__(self):
        LVNode.__init__(self, "less_or_equal")
        LVNode.addTerminal(self, "x")
        LVNode.addTerminal(self, "y")
        LVNode.addTerminal(self, "x <= y?", False, "BOOL")
        self.attributes["type"] = "Less Or Equal?"
        self.attributes["genclass"] = "Function"
    
    def getTerms(self):
        outputTerm = self.getTerminalByName("x <= y?")
        leftTerm = self.getTerminalByName("x")
        rightTerm = self.getTerminalByName("y")
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
        rootElem.attrib["xPos"] = "0"
        rootElem.attrib["yPos"] = str(index * 50)
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
        rootElem.attrib["uuid"] = self.uuid
        
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
        self.attributes["type"] = "Array Control"
        self.attributes["style"] = "Array (modern)"
        self.varType = "1DSTRINGARRAY"
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
        rootElem.attrib["xPos"] = "0"
        rootElem.attrib["yPos"] = str(index * 50)
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
        rootElem.attrib["uuid"] = self.uuid
        
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
