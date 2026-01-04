from enum import Enum
from .node import LVNode
import xml.etree.ElementTree as ET

class Tunnelable:
    def __init__(self, *args, **kwargs):
        self.tunnels = {}
        super().__init__(*args, **kwargs)

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
    