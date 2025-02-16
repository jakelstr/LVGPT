import uuid
import xml.etree.ElementTree as ET
from enum import Enum


def generate_xy_position(index, base_x=50, base_y=50, spacing_x=150, spacing_y=50, columns=4):
    """
    Generate an (x, y) position for a node given its index.
    
    Args:
        index (int): The zero-based index of the node.
        base_x (int): Starting x position.
        base_y (int): Starting y position.
        spacing_x (int): Horizontal spacing between nodes.
        spacing_y (int): Vertical spacing between nodes.
        columns (int): Number of columns in the grid layout.
        
    Returns:
        tuple: (x, y) coordinates for the node.
    """
    col = index % columns
    row = index // columns
    x = base_x + col * spacing_x
    y = base_y + row * spacing_y
    return x, y


def assign_node_levels_for_subset(nodes, lvGraph):
    """
    Compute a level (integer) for each node in a subset (all sharing the same diagram)
    based on connectivity. Only considers edges between nodes in the given list.
    """
    levels = {node.uuid: 0 for node in nodes}
    node_ids = {node.uuid for node in nodes}
    changed = True
    while changed:
        changed = False
        for node in nodes:
            max_source_level = -1
            # For each input terminal, check its connected source node (if it’s in this diagram)
            for term in node.terminals.values():
                if term.isInput:
                    if term.is_tunnel:
                        direction = determine_tunnel_direction(term, lvGraph)
                        if direction == "out":
                            # If the tunnel terminal is sending data out, skip it.
                            continue
                    for edge in term.edges:
                        source_uuid = lvGraph.getTerminalOwner(edge)
                        if source_uuid in node_ids:
                            max_source_level = max(max_source_level, levels.get(source_uuid, 0))
            new_level = max_source_level + 1 if max_source_level >= 0 else 0
            if new_level != levels[node.uuid]:
                levels[node.uuid] = new_level
                changed = True
    return levels


def layout_diagram_relative(lvGraph, diagram_id, spacing_x=150, spacing_y=50, padding = 20):
    """
    Layout nodes that belong to a given diagram (nodes with parentDiagram == diagram_id)
    in a coordinate system where (0,0) is the upper left corner.
    Positions are computed left-to-right based on connectivity (levels) and top-to-bottom
    based on the ordering within each level.
    """
    # Filter nodes belonging to this diagram.
    nodes = [node for node in lvGraph.graph["nodes"].values()
             if node.attributes.get("parentDiagram") == diagram_id]
    if not nodes:
        return

    # Compute levels (only among these nodes).
    levels = assign_node_levels_for_subset(nodes, lvGraph)

    # Group nodes by level.
    level_groups = {}
    for node in nodes:
        lvl = levels[node.uuid]
        level_groups.setdefault(lvl, []).append(node)

    # For each level, sort nodes (here by name) and assign positions relative to (0,0).
    for lvl, node_list in level_groups.items():
        node_list.sort(key=lambda n: n.name)
        for i, node in enumerate(node_list):
            x = lvl * spacing_x + padding
            y = i * spacing_y + padding
            node.attributes["xPos"] = str(x)
            node.attributes["yPos"] = str(y)


def determine_tunnel_direction(term, lvGraph):
    """
    Given a tunnel terminal (term.is_tunnel True), look at its connected edges
    to decide if it is acting as an 'in' or 'out' terminal.
    
    For each edge, we retrieve the connected terminal (the one not equal to term).
    If that connected terminal is an input, then term is functioning as an output,
    and vice versa.
    
    Returns:
        "in" if the tunnel terminal appears to be receiving data,
        "out" if it appears to be sending data.
        In the case of a tie or no connections, defaults to:
            "in" if term.isInput is True, else "out".
    """
    in_count = 0
    out_count = 0
    # Each edge is stored as the UUID of the connected terminal.
    for edge in term.edges:
        # Get the connected terminal object.
        owner_node_uuid = lvGraph.getTerminalOwner(edge)
        owner_node = lvGraph.graph["nodes"].get(owner_node_uuid)
        if owner_node is None:
            continue
        other_terminal = owner_node.terminals.get(edge)
        if other_terminal is None:
            continue
        # If the connected terminal is an input, then this tunnel terminal must be output.
        if other_terminal.isInput:
            out_count += 1
        else:
            in_count += 1
    if in_count > out_count:
        return "in"
    elif out_count > in_count:
        return "out"
    else:
        # Default to the terminal's own isInput meaning.
        return "in" if term.isInput else "out"


class LVGraph:
    def __init__(self):
        #nodes is nodeUUID->LVNode, terminals is terminalUUID->nodeUUID, nodeNames is nodeName->nodeUUID
        self.graph = {"nodes":{}, "terminals":{}, "nodeNames":{}, "symbolTable":{}}
        self.diagramUUID = str(uuid.uuid4())
        self.baseDiagram = self.diagramUUID
        self.symbolTable = SymbolTable()
            

    def addNode(self, node, diagramUUID=None):
        if node.name in self.graph["nodeNames"]:
            node.name = self.getAvailableNodeName(node.name)
        if not diagramUUID:
            diagramUUID = self.diagramUUID
        node.attributes["parentDiagram"] = diagramUUID
        self.graph["nodeNames"][node.name] = node.uuid
        self.graph["nodes"][node.uuid] = node
        for termUUID in node.terminals:
            self.graph["terminals"][termUUID] = node.uuid

        node.graph = self

    def finalize_layout(self, spacing_x=150, spacing_y=50):
        """
        Layout all diagrams (main and subdiagrams) independently.
        For each diagram, the upper left corner is (0,0).
        """
        # Layout the main diagram.
        layout_diagram_relative(self, self.diagramUUID, spacing_x, spacing_y)
        
        # Then layout each subdiagram.
        # We assume that subdiagrams are tracked in the 'frames' attribute of structures.
        node_count = 0
        for node in self.graph["nodes"].values():
            if hasattr(node, "frames") and node.frames:
                for subDiagram_id in node.frames.keys():
                    layout_diagram_relative(self, subDiagram_id, spacing_x, spacing_y)

            if isinstance(node, HasFrontPanelControl):
                x, y = generate_xy_position(node_count)
                node.attributes["FPxPos"] = str(x)
                node.attributes["FPyPos"] = str(y)
                node_count = node_count + 1


        
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
    
    def getTunnelCreateWires(self, tunnel):
        
        outside = tunnel.external_terminal
        inside = tunnel.terminals_internal[0]
        if len(outside.edges) > 0 and len(inside.edges) > 0:
            outsideForeignNodeUUID = self.getTerminalOwner(outside.edges[0])
            outsideForeignNode = self.graph["nodes"][outsideForeignNodeUUID]
            outsideForeignNode.terminals[outside.edges[0]].edges.remove(outside.uuid)
            insideForeignNodeUUID = self.getTerminalOwner(inside.edges[0])
            insideForeignNode = self.graph["nodes"][insideForeignNodeUUID]
            insideForeignNode.terminals[inside.edges[0]].edges.remove(inside.uuid)
            edgeWire = wire(outside.edges[0], inside.edges[0])
            del outside.edges[0]
            del inside.edges[0]
            tunnel.create_wire = edgeWire
    
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
    
    def registerTerminal(self, terminal_uuid, node_uuid):
        """Called by nodes when they add a terminal after being added to the graph."""
        self.graph["terminals"][terminal_uuid] = node_uuid

    def writeXML(self, vi_name, file_path):
        visNode = ET.Element("vis")
        viNode = ET.Element("vi")
        bdNode = ET.Element("bd")
        bdNode.attrib["name"] = vi_name
        bdNode.attrib["diagramUUID"] = self.diagramUUID
        outputNodesElem = ET.Element("nodes")
        outputWiresElem = ET.Element("wires")
        for i, n in enumerate(self.graph["nodes"]):
            if isinstance(self.graph["nodes"][n], Tunnelable):
                for t in self.graph["nodes"][n].tunnels.values():
                    self.getTunnelCreateWires(t)
            outputNodesElem.append(self.graph["nodes"][n].writeNodeToXML(i))
        for w in self.getWires():
            outputWiresElem.append(w.writeWireToXML())
        bdNode.append(outputNodesElem)
        bdNode.append(outputWiresElem)
        viNode.append(bdNode)
        visNode.append(viNode)
        tree = ET.ElementTree(visNode)
        with open(file_path, "wb") as files:
            ET.indent(tree, space="\t", level=0)
            tree.write(files)
    

class SymbolTable:
    def __init__(self, parentTable=None):
        self.parentTable = parentTable
        self.children= {}

class tunnel:
    def __init__(self, name):
        self.name = name
        self.terminals = {}
        self.create_wire = None
    def addTerminal(self, terminalName, node):
        terminalUUID = LVNode.addTerminal(node, terminalName, is_tunnel=True)
        terminal = LVNode.getTerminalByName(node, terminalName)
        self.terminals[terminalName] = terminal
        return terminal
    
class Tunnelable:
    def __init__(self, *args, **kwargs):
        self.tunnels = {}
        super().__init__(*args, **kwargs)

class LoopTunnel(tunnel):
    class IndexType(Enum):
        last_value = 0
        indexing = 1
        concatenating = 2
    def __init__(self, name):
        tunnel.__init__(self, name)
        self.IndexType = LoopTunnel.IndexType.indexing

class ShiftRegister(tunnel):
    def __init__(self, name, yPos, loop):
        tunnel.__init__(self, name)
        self.lhExternalTerminal = self.addTerminal(f"{name} LH external", loop)
        self.lhInternalTerminal = self.addTerminal(f"{name} LH internal", loop)
        self.rhInternalTerminal = self.addTerminal(f"{name} RH internal", loop)
        self.rhExternalTerminal = self.addTerminal(f"{name} RH external", loop)
        self.yPos = yPos
    def writeTunnelToXML(self, rootElem):
        tunnelElem = ET.Element("tunnel")
        tunnelElem.attrib["name"] = self.name
        tunnelElem.attrib["yPos"] = str(self.yPos)
        lhElem = ET.Element("lh")
        lhExternalElem = ET.Element("external")
        self.lhExternalTerminal.writeTerminalToXML(lhExternalElem)
        lhElem.append(lhExternalElem)
        lhInternalElem = ET.Element("internal")
        self.lhInternalTerminal.writeTerminalToXML(lhInternalElem)
        lhElem.append(lhInternalElem)
        tunnelElem.append(lhElem)
        rhElem = ET.Element("rh")
        rhExternalElem = ET.Element("external")
        self.rhExternalTerminal.writeTerminalToXML(rhExternalElem)
        rhElem.append(rhExternalElem)
        rhInternalElem = ET.Element("internal")
        self.rhInternalTerminal.writeTerminalToXML(rhInternalElem)
        rhElem.append(rhInternalElem)
        tunnelElem.append(rhElem)
        
        if self.create_wire:
            createWireElem = ET.Element("create_wire")
            createWireElem.append(self.create_wire.writeWireToXML())
            tunnelElem.append(createWireElem)
        rootElem.append(tunnelElem)
        

class MultiFrameTunnel(tunnel):
    def __init__(self, name, multi_frame_structure):
        tunnel.__init__(self, name)
        self.external_terminal = self.addTerminal(f"{name} external {multi_frame_structure.uuid}", multi_frame_structure)
        self.terminals_internal = []
        for x in multi_frame_structure.frames.keys():
            self.terminals_internal.append(self.addTerminal(f"{name} internal {x}", multi_frame_structure))
    def addFrame(self, frame_uuid, multi_frame_structure):
        self.terminals_internal.append(self.addTerminal(f"{self.name} internal {frame_uuid}", multi_frame_structure))
    def writeTunnelToXML(self, rootElem):
        tunnelElem = ET.Element("tunnel")
        tunnelElem.attrib["name"] = self.name
        externalElem = ET.Element("external")
        self.external_terminal.writeTerminalToXML(externalElem)
        tunnelElem.append(externalElem)
        internalElem = ET.Element("internal")
        all_internal_terminals_unwired = all(not x.is_wired() for x in self.terminals_internal)
        if not all_internal_terminals_unwired:
            for x in self.terminals_internal:
                x.writeTerminalToXML(internalElem)
            tunnelElem.append(internalElem)
        if self.create_wire:
            createWireElem = ET.Element("create_wire")
            createWireElem.append(self.create_wire.writeWireToXML())
            tunnelElem.append(createWireElem)
        rootElem.append(tunnelElem)
        
class SelectorTunnel(MultiFrameTunnel):
    def __init__(self, case_structure):
        MultiFrameTunnel.__init__(self, "case selector", case_structure)

    def writeTunnelToXML(self, rootElem):
        tunnelElem = ET.Element("SelectorTunnel")
        MultiFrameTunnel.writeTunnelToXML(self, tunnelElem)
        rootElem.append(tunnelElem)
    

class terminal:
    def __init__(self, name):
        self.uuid = str(uuid.uuid4())
        self.name = name
        self.isInput = True
        self.edges = []
        self.varType = None
    def is_wired(self):
        return len(self.edges) > 0
    
    def writeTerminalToXML(self, rootElem):
        termElem = ET.Element("terminal")
        termElem.attrib["id"] = self.uuid
        termElem.attrib["name"] = self.name
        rootElem.append(termElem)
        return rootElem
class wire:
    def __init__(self, fromUUID, toUUID):
        self.uuid = str(uuid.uuid4())
        self.fromUUID = fromUUID
        self.toUUID = toUUID
    def writeWireToXML(self):
        rootElem = ET.Element("wire")
        rootElem.attrib["id"] = self.uuid
        rootElem.attrib["from"] = self.fromUUID
        rootElem.attrib["to"] = self.toUUID
        return rootElem

class LVNode:
    def __init__(self, name):
        self.uuid = str(uuid.uuid4())
        self.terminals = {}
        self.terminals_by_name = {}
        self.name = name
        self.attributes = {"name" : name}
        self.isIndicator = False
        self.varType = None
        self.graph = None

    def addTerminal(self, name, isInput=True, varType=None, is_tunnel=False):
        term = terminal(name)
        term.isInput = isInput
        term.is_tunnel = is_tunnel
        if varType is None:
            term.varType = self.varType
        else:
            term.varType = varType
        self.terminals[term.uuid] = term
        self.terminals_by_name[name] = term
        if self.graph is not None:
            self.graph.registerTerminal(term.uuid, self.uuid)
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
        rootElem.attrib["uuid"] = self.uuid
        if hasattr(self, "value") and self.value is not None:
            rootElem.attrib["value"] = self.value
        for attrib in self.attributes:
            rootElem.attrib[attrib] = self.attributes[attrib]
        terminalsElem = ET.Element("terminals")
        for term in self.terminals.values():
            if not term.is_tunnel:
                term.writeTerminalToXML(terminalsElem)
        rootElem.append(terminalsElem)
        return rootElem

class HasFrontPanelControl:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class FrontPanelControl(HasFrontPanelControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class FrontPanelIndicator(HasFrontPanelControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
        self.attributes["type"] = "Greater Or Equal?"
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
        outputTerm = self.getTerminalByName("x = y?")
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
        self.attributes["type"] = "Greater?"
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
        self.attributes["type"] = "Less?"
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
        self.attributes["defaultNodeCount"] = "2"
        self.attributes["genclass"] = "Growable Function"
    def getTerms(self):
        outputTerm = LVNode.getTerminalByName(self, "concatenated string")
        return (None, None, outputTerm)
    def getTerminal(self):
        return LVNode.getTerminalByName(self, "concatenated string")
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
    
class SelectNode(LVNode):
    def __init__(self):
        LVNode.__init__(self, "select")
        LVNode.addTerminal(self, "t")
        LVNode.addTerminal(self, "s", varType="BOOL")
        LVNode.addTerminal(self, "f")
        LVNode.addTerminal(self, "s? t:f", False)
        self.attributes["type"] = "Select"
        self.attributes["genclass"] = "Function"
    def getTerms(self):
        trueTerm = LVNode.getTerminalByName(self, "t")
        selectorTerm = LVNode.getTerminalByName(self, "s")
        falseTerm = LVNode.getTerminalByName(self, "f")
        outputTerm = LVNode.getTerminalByName(self, "s? t:f")
        return (trueTerm, selectorTerm, falseTerm, outputTerm)
    
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
