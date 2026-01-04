import xml.etree.ElementTree as ET
import uuid

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
