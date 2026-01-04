import uuid
import xml.etree.ElementTree as ET
from .terminals import terminal, wire
from .tunnel import tunnel, Tunnelable
from .node import LVNode, HasFrontPanelControl
# from utils import indent_xml

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
    loops = 0
    while changed and loops < 100:
        loops += 1
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