import uuid
import xml.etree.ElementTree as ET
from .terminals import terminal
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

class GenericFrontPanelControl(LVNode, FrontPanelControl):
    def __init__(self, name, style):
        LVNode.__init__(self, name)
        FrontPanelControl.__init__(self)
        self.attributes["type"] = "Control"
        self.attributes["style"] = style
        LVNode.addTerminal(self, name, False)

class GrowableFunction(LVNode):
    def __init__(self, name, chunks=1):
        LVNode.__init__(self, name)
        self.attributes["genclass"] = "GrowableFunction"
        self.attributes["chunks"] = str(chunks)
        self.attributes["defaultChunks"] = str(chunks)
        self.chunkTerminals = []
    
    def addChunk(self, termName, input=True, varType=None):
        self.attributes["chunks"] = str(int(self.attributes["chunks"]) + 1)
        chunkTerm = LVNode.addTerminal(self, termName, isInput=input, varType=varType)
        self.chunkTerminals.append(chunkTerm)
        return chunkTerm
    
    def addChunkTerminal(self, termUUID):
        self.chunkTerminals.append(termUUID)

    def searchForTerms(self, searchTerm):
        import re
        return [item for item in self.terminals.values() if re.search(searchTerm, item.name)]

class ObjectFunction(GrowableFunction):
    def __init__(self, name, chunks=1):
        GrowableFunction.__init__(self, name, chunks)

    def setLinkUUID(self, linkUUID):
        self.attributes["linkUUID"] = linkUUID

