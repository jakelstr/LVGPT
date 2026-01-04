from .node import LVNode
from .tunnel import Tunnelable, MultiFrameTunnel, SelectorTunnel, ShiftRegister, LoopTunnel
import uuid
import xml.etree.ElementTree as ET

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

    def getCaseSelector(self):
        return self.case_selector
    
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

    def addShiftRegister(self, yPos = None):
        name = "sr" + str(len(self.shift_registers))
        if not yPos:
            yPos = len(self.shift_registers) * 20
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
    
    def addTunnel(self):
        name = "tunnel" + str(len(self.tunnels))
        tunnel = LoopTunnel(name, self)
        self.tunnels[name] = tunnel
        return tunnel
        
    
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
        return LVNode.getTerminalByName(self, "Next")
    def getITerm(self):
        return LVNode.getTerminalByName(self, "i")
    def getSubdiagram(self):
        return list(self.frames.keys())[0]
    

class WhileLoop(Loop):
    def __init__(self, name):
        Loop.__init__(self, name)
        self.attributes["type"] = "While Loop"
        self.attributes["style"] = "While Loop #1"
        self.attributes["stop_if_true"] = "False"
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