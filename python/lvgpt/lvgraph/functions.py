from .node import LVNode
class AbsoluteValue(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Absolute Value")
        LVNode.addTerminal(self, "abs(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Absolute Value"
        self.attributes["genclass"] = "Function"


class AcceptTls(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Accept TLS")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "client certificate chain", varType="Array", isInput=False)
        LVNode.addTerminal(self, "TLS connection", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "timeout ms (300000)", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "immutable TLS configuration", varType="Refnum")
        LVNode.addTerminal(self, "TCP connection", varType="Refnum")
        self.attributes["type"] = "Accept TLS"
        self.attributes["genclass"] = "Function"


class AccessRights(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Access Rights")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "permissions", varType="I16", isInput=False)
        LVNode.addTerminal(self, "group", varType="String", isInput=False)
        LVNode.addTerminal(self, "owner", varType="String", isInput=False)
        LVNode.addTerminal(self, "dup path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "path", varType="Path")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "new permissions", varType="I16")
        LVNode.addTerminal(self, "new group", varType="String")
        LVNode.addTerminal(self, "new owner", varType="String")
        self.attributes["type"] = "Access Rights"
        self.attributes["genclass"] = "Function"


class Add(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Add")
        LVNode.addTerminal(self, "x+y", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Add"
        self.attributes["genclass"] = "Function"


class AddWithErrorTerminals(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Add (with error terminals)")
        LVNode.addTerminal(self, "x+y", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        self.attributes["type"] = "Add (with error terminals)"
        self.attributes["genclass"] = "Function"


class AddArrayElements(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Add Array Elements")
        LVNode.addTerminal(self, "sum", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "numeric array", varType="Array")
        self.attributes["type"] = "Add Array Elements"
        self.attributes["genclass"] = "Function"


class AddEntropy(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Add Entropy")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "entropy", varType="Array")
        self.attributes["type"] = "Add Entropy"
        self.attributes["genclass"] = "Function"


class AddPrivateKeyToTlsConfiguration(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Add Private Key To TLS Configuration")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "TLS configuration out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "certificate chain", varType="Array")
        LVNode.addTerminal(self, "private key", varType="Array")
        LVNode.addTerminal(self, "TLS configuration", varType="Refnum")
        self.attributes["type"] = "Add Private Key To TLS Configuration"
        self.attributes["genclass"] = "Function"


class AddTrustedCertificateToTlsConfiguration(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Add Trusted Certificate To TLS Configuration")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "TLS configuration out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "certificate", varType="Array")
        LVNode.addTerminal(self, "TLS configuration", varType="Refnum")
        self.attributes["type"] = "Add Trusted Certificate To TLS Configuration"
        self.attributes["genclass"] = "Function"


class Allspoll(LVNode):
    def __init__(self):
        LVNode.__init__(self, "AllSpoll")
        LVNode.addTerminal(self, "bus", varType="I32")
        LVNode.addTerminal(self, "address list", varType="Array")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "serial poll byte list", varType="Array", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "byte count", varType="I32", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "AllSpoll"
        self.attributes["genclass"] = "Function"


class AlwaysCopy(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Always Copy")
        LVNode.addTerminal(self, "Output", varType="I32", isInput=False)
        LVNode.addTerminal(self, "Input", varType="I32")
        self.attributes["type"] = "Always Copy"
        self.attributes["genclass"] = "Function"


class And(LVNode):
    def __init__(self):
        LVNode.__init__(self, "And")
        LVNode.addTerminal(self, "x .and. y?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "y", varType="Boolean")
        LVNode.addTerminal(self, "x", varType="Boolean")
        self.attributes["type"] = "And"
        self.attributes["genclass"] = "Function"


class AndArrayElements(LVNode):
    def __init__(self):
        LVNode.__init__(self, "And Array Elements")
        LVNode.addTerminal(self, "logical AND", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "Boolean array", varType="Array")
        self.attributes["type"] = "And Array Elements"
        self.attributes["genclass"] = "Function"


class AppendTrueFalseString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Append True/False String")
        LVNode.addTerminal(self, "output string", varType="String", isInput=False)
        LVNode.addTerminal(self, "selector", varType="Boolean")
        LVNode.addTerminal(self, "false string", varType="String")
        LVNode.addTerminal(self, "true string", varType="String")
        LVNode.addTerminal(self, "string ("")", varType="String")
        self.attributes["type"] = "Append True/False String"
        self.attributes["genclass"] = "Function"


class ArrayMaxMin(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Array Max & Min")
        LVNode.addTerminal(self, "array", varType="Array")
        LVNode.addTerminal(self, "max value", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "max index (indices)", varType="I32", isInput=False)
        LVNode.addTerminal(self, "min value", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "min index (indices)", varType="I32", isInput=False)
        self.attributes["type"] = "Array Max & Min"
        self.attributes["genclass"] = "Function"


class ArrayOfStringsToPath(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Array of Strings to Path")
        LVNode.addTerminal(self, "array of strings", varType="Array")
        LVNode.addTerminal(self, "relative", varType="Boolean")
        LVNode.addTerminal(self, "path", varType="Path", isInput=False)
        self.attributes["type"] = "Array of Strings to Path"
        self.attributes["genclass"] = "Function"


class ArraySize(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Array Size")
        LVNode.addTerminal(self, "size(s)", varType="I32", isInput=False)
        LVNode.addTerminal(self, "array", varType="Array")
        self.attributes["type"] = "Array Size"
        self.attributes["genclass"] = "Function"


class ArrayToCluster(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Array To Cluster")
        LVNode.addTerminal(self, "cluster", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "array", varType="Array")
        self.attributes["type"] = "Array To Cluster"
        self.attributes["genclass"] = "Function"


class ArrayToSpreadsheetString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Array To Spreadsheet String")
        LVNode.addTerminal(self, "spreadsheet string", varType="String", isInput=False)
        LVNode.addTerminal(self, "delimiter (Tab)", varType="String")
        LVNode.addTerminal(self, "array", varType="Array")
        LVNode.addTerminal(self, "format string", varType="String")
        self.attributes["type"] = "Array To Spreadsheet String"
        self.attributes["genclass"] = "Function"


class Arraymeminfo(LVNode):
    def __init__(self):
        LVNode.__init__(self, "ArrayMemInfo")
        LVNode.addTerminal(self, "mem info out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "array out", varType="Array", isInput=False)
        LVNode.addTerminal(self, "array in", varType="Array")
        self.attributes["type"] = "ArrayMemInfo"
        self.attributes["genclass"] = "Function"


class AssertStructuralTypeMatch(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Assert Structural Type Match")
        LVNode.addTerminal(self, "reference", varType="LV Variant")
        LVNode.addTerminal(self, "anything", varType="LV Variant")
        self.attributes["type"] = "Assert Structural Type Match"
        self.attributes["genclass"] = "Function"


class AutomationClose(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Automation Close")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error in(no error)", varType="Cluster")
        LVNode.addTerminal(self, "Automation Refnum", varType="Refnum")
        self.attributes["type"] = "Automation Close"
        self.attributes["genclass"] = "Function"


class AutomationOpen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Automation Open")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "Automation Refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "", varType="Boolean")
        LVNode.addTerminal(self, "machine name", varType="String")
        LVNode.addTerminal(self, "Automation Refnum", varType="Refnum")
        self.attributes["type"] = "Automation Open"
        self.attributes["genclass"] = "Function"


class BitpackToArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Bitpack to Array")
        LVNode.addTerminal(self, "bparray", varType="Array", isInput=False)
        LVNode.addTerminal(self, "data", varType="Cluster")
        self.attributes["type"] = "Bitpack to Array"
        self.attributes["genclass"] = "Function"


class BluetoothCloseConnection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Bluetooth Close Connection")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "connection ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "abort (F)", varType="Boolean")
        LVNode.addTerminal(self, "connection ID", varType="Refnum")
        self.attributes["type"] = "Bluetooth Close Connection"
        self.attributes["genclass"] = "Function"


class BluetoothCreateListener(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Bluetooth Create Listener")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "channel", varType="U16", isInput=False)
        LVNode.addTerminal(self, "listener ID", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "service description", varType="Cluster")
        LVNode.addTerminal(self, "address", varType="String")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "uuid", varType="String")
        self.attributes["type"] = "Bluetooth Create Listener"
        self.attributes["genclass"] = "Function"


class BluetoothDiscover(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Bluetooth Discover")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "device list", varType="Array", isInput=False)
        LVNode.addTerminal(self, "number of devices", varType="U16", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "time limit ms (10000)", varType="I32")
        self.attributes["type"] = "Bluetooth Discover"
        self.attributes["genclass"] = "Function"


class BluetoothOpenConnection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Bluetooth Open Connection")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "connection ID", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "uuid", varType="String")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (60000)", varType="I32")
        LVNode.addTerminal(self, "channel (0)", varType="U16")
        LVNode.addTerminal(self, "address", varType="String")
        self.attributes["type"] = "Bluetooth Open Connection"
        self.attributes["genclass"] = "Function"


class BluetoothRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Bluetooth Read")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "data out", varType="String", isInput=False)
        LVNode.addTerminal(self, "connection ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "mode (standard)", varType="Enum U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (25000)", varType="I32")
        LVNode.addTerminal(self, "bytes to read", varType="I32")
        LVNode.addTerminal(self, "connection ID", varType="Refnum")
        self.attributes["type"] = "Bluetooth Read"
        self.attributes["genclass"] = "Function"


class BluetoothWaitOnListener(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Bluetooth Wait On Listener")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "remote channel", varType="U16", isInput=False)
        LVNode.addTerminal(self, "remote address", varType="String", isInput=False)
        LVNode.addTerminal(self, "listener ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "connection ID", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (wait forever: -1)", varType="I32")
        LVNode.addTerminal(self, "resolve remote address (T)", varType="Boolean")
        LVNode.addTerminal(self, "listener ID in", varType="Refnum")
        self.attributes["type"] = "Bluetooth Wait On Listener"
        self.attributes["genclass"] = "Function"


class BluetoothWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Bluetooth Write")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "bytes written", varType="I32", isInput=False)
        LVNode.addTerminal(self, "connection ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (25000)", varType="I32")
        LVNode.addTerminal(self, "data in", varType="String")
        LVNode.addTerminal(self, "connection ID", varType="Refnum")
        self.attributes["type"] = "Bluetooth Write"
        self.attributes["genclass"] = "Function"


class BooleanArrayToNumber(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Boolean Array To Number")
        LVNode.addTerminal(self, "number", varType="U32", isInput=False)
        LVNode.addTerminal(self, "Boolean array", varType="Array")
        self.attributes["type"] = "Boolean Array To Number"
        self.attributes["genclass"] = "Function"


class BooleanTo01(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Boolean To (0,1)")
        LVNode.addTerminal(self, "0, 1", varType="I16", isInput=False)
        LVNode.addTerminal(self, "Boolean", varType="Boolean")
        self.attributes["type"] = "Boolean To (0,1)"
        self.attributes["genclass"] = "Function"


class BuildPath(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Build Path")
        LVNode.addTerminal(self, "appended path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "name or relative path", varType="Path")
        LVNode.addTerminal(self, "base path", varType="Path")
        self.attributes["type"] = "Build Path"
        self.attributes["genclass"] = "Function"


class ByteArrayToString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Byte Array To String")
        LVNode.addTerminal(self, "string", varType="String", isInput=False)
        LVNode.addTerminal(self, "unsigned byte array", varType="Array")
        self.attributes["type"] = "Byte Array To String"
        self.attributes["genclass"] = "Function"


class CallChain(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Call Chain")
        LVNode.addTerminal(self, "call chain", varType="Array", isInput=False)
        self.attributes["type"] = "Call Chain"
        self.attributes["genclass"] = "Function"


class CancelNotification(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Cancel Notification")
        LVNode.addTerminal(self, "notifier", varType="Refnum")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "notifier out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "canceled notifcation", varType="String", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Cancel Notification"
        self.attributes["genclass"] = "Function"


class CastUnitBases(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Cast Unit Bases")
        LVNode.addTerminal(self, "x", varType="Double Float")
        LVNode.addTerminal(self, "unit (none)", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float", isInput=False)
        self.attributes["type"] = "Cast Unit Bases"
        self.attributes["genclass"] = "Function"


class ClearFixedPointOverflowStatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Clear Fixed-Point Overflow Status")
        LVNode.addTerminal(self, "overflow?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "FXP with overflow cleared", varType="Fixed Point", isInput=False)
        LVNode.addTerminal(self, "FXP", varType="Fixed Point")
        self.attributes["type"] = "Clear Fixed-Point Overflow Status"
        self.attributes["genclass"] = "Function"


class CloseFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Close File")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Close File"
        self.attributes["genclass"] = "Function"


class CloseFileDeprecated(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Close File (deprecated)")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Close File (deprecated)"
        self.attributes["genclass"] = "Function"


class CloseMatlabSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Close MATLAB Session")
        LVNode.addTerminal(self, "session in", varType="Refnum")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Close MATLAB Session"
        self.attributes["genclass"] = "Function"


class ClosePythonSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Close Python Session")
        LVNode.addTerminal(self, "session in", varType="Refnum")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Close Python Session"
        self.attributes["genclass"] = "Function"


class CloseReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Close Reference")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "reference", varType="Refnum")
        self.attributes["type"] = "Close Reference"
        self.attributes["genclass"] = "Function"


class CloseTlsConfiguration(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Close TLS Configuration")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "TLS configuration", varType="Refnum")
        self.attributes["type"] = "Close TLS Configuration"
        self.attributes["genclass"] = "Function"


class CloseVariableConnection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Close Variable Connection")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "shared variable refnum in", varType="Refnum")
        self.attributes["type"] = "Close Variable Connection"
        self.attributes["genclass"] = "Function"


class ClusterToArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Cluster To Array")
        LVNode.addTerminal(self, "array", varType="Array", isInput=False)
        LVNode.addTerminal(self, "cluster", varType="Cluster")
        self.attributes["type"] = "Cluster To Array"
        self.attributes["genclass"] = "Function"


class CoerceToType(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Coerce To Type")
        LVNode.addTerminal(self, "x", varType="Extended Float")
        LVNode.addTerminal(self, "type", varType="Extended Float")
        LVNode.addTerminal(self, "coerced x", varType="Extended Float", isInput=False)
        self.attributes["type"] = "Coerce To Type"
        self.attributes["genclass"] = "Function"


class CollectionSize(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Collection Size")
        LVNode.addTerminal(self, "size", varType="I32", isInput=False)
        LVNode.addTerminal(self, "collection", varType="Set Collection")
        self.attributes["type"] = "Collection Size"
        self.attributes["genclass"] = "Function"


class ComplexConjugate(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Complex Conjugate")
        LVNode.addTerminal(self, "x - iy", varType="Double Complex", isInput=False)
        LVNode.addTerminal(self, "x + iy", varType="Double Complex")
        self.attributes["type"] = "Complex Conjugate"
        self.attributes["genclass"] = "Function"


class ComplexToPolar(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Complex To Polar")
        LVNode.addTerminal(self, "r * e^(i*theta)", varType="Double Complex")
        LVNode.addTerminal(self, "r", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "theta", varType="Double Float", isInput=False)
        self.attributes["type"] = "Complex To Polar"
        self.attributes["genclass"] = "Function"


class ComplexToReIm(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Complex To Re/Im")
        LVNode.addTerminal(self, "x + iy", varType="Double Complex")
        LVNode.addTerminal(self, "x", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float", isInput=False)
        self.attributes["type"] = "Complex To Re/Im"
        self.attributes["genclass"] = "Function"


class ControlHelpWindow(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Control Help Window")
        LVNode.addTerminal(self, "Top Left Corner", varType="Cluster")
        LVNode.addTerminal(self, "Show", varType="Boolean")
        self.attributes["type"] = "Control Help Window"
        self.attributes["genclass"] = "Function"


class ControlOnlineHelp(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Control Online Help")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "Path to the help file", varType="Path")
        LVNode.addTerminal(self, "String to search for", varType="String")
        LVNode.addTerminal(self, "Operation", varType="Enum U16")
        self.attributes["type"] = "Control Online Help"
        self.attributes["genclass"] = "Function"


class Copy(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Copy")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "cancelled", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "new path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "prompt (Choose or enter target path for copy)", varType="String")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "overwrite (F)", varType="Boolean")
        LVNode.addTerminal(self, "target path (use dialog)", varType="Path")
        LVNode.addTerminal(self, "source path", varType="Path")
        self.attributes["type"] = "Copy"
        self.attributes["genclass"] = "Function"


class CopyDeprecated(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Copy (deprecated)")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "new path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "target path", varType="Path")
        LVNode.addTerminal(self, "source path", varType="Path")
        self.attributes["type"] = "Copy (deprecated)"
        self.attributes["genclass"] = "Function"


class Cosecant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Cosecant")
        LVNode.addTerminal(self, "1/sin(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Cosecant"
        self.attributes["genclass"] = "Function"


class Cosine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Cosine")
        LVNode.addTerminal(self, "cos(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Cosine"
        self.attributes["genclass"] = "Function"


class Cotangent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Cotangent")
        LVNode.addTerminal(self, "1/tan(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Cotangent"
        self.attributes["genclass"] = "Function"


class CpuInformation(LVNode):
    def __init__(self):
        LVNode.__init__(self, "CPU Information")
        LVNode.addTerminal(self, "# of logical processors", varType="I32", isInput=False)
        LVNode.addTerminal(self, "# of packages", varType="I32", isInput=False)
        LVNode.addTerminal(self, "# of cores per package", varType="I32", isInput=False)
        LVNode.addTerminal(self, "# of logical processors per core", varType="I32", isInput=False)
        self.attributes["type"] = "CPU Information"
        self.attributes["genclass"] = "Function"


class CreateFolder(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Create Folder")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "cancelled", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "created path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "prompt (Create Folder)", varType="String")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "path (use dialog)", varType="Path")
        self.attributes["type"] = "Create Folder"
        self.attributes["genclass"] = "Function"


class CreateNetworkStreamEndpoint(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Create Network Stream Endpoint")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "endpoint", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "timeout in ms (-1)", varType="I32")
        LVNode.addTerminal(self, "element allocation mode", varType="U32")
        LVNode.addTerminal(self, "buffer sizes", varType="Cluster")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "data type", varType="Void")
        LVNode.addTerminal(self, "remote endpoint url", varType="String")
        LVNode.addTerminal(self, "endpoint name", varType="String")
        self.attributes["type"] = "Create Network Stream Endpoint"
        self.attributes["genclass"] = "Function"


class CreateNetworkStreamReaderEndpoint(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Create Network Stream Reader Endpoint")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "reader endpoint", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "timeout in ms (-1)", varType="I32")
        LVNode.addTerminal(self, "element allocation mode", varType="U32")
        LVNode.addTerminal(self, "reader buffer size", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "data type", varType="Void")
        LVNode.addTerminal(self, "writer url", varType="String")
        LVNode.addTerminal(self, "reader name", varType="String")
        self.attributes["type"] = "Create Network Stream Reader Endpoint"
        self.attributes["genclass"] = "Function"


class CreateNetworkStreamWriterEndpoint(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Create Network Stream Writer Endpoint")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "writer endpoint", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "timeout in ms (-1)", varType="I32")
        LVNode.addTerminal(self, "element allocation mode", varType="U32")
        LVNode.addTerminal(self, "writer buffer size", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "data type", varType="Void")
        LVNode.addTerminal(self, "reader url", varType="String")
        LVNode.addTerminal(self, "writer name", varType="String")
        self.attributes["type"] = "Create Network Stream Writer Endpoint"
        self.attributes["genclass"] = "Function"


class CreateUniqueNetworkStreamEndpoint(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Create Unique Network Stream Endpoint")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "endpoint", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "max connections (-1)", varType="I32")
        LVNode.addTerminal(self, "timeout in ms (-1)", varType="I32")
        LVNode.addTerminal(self, "element allocation mode", varType="U32")
        LVNode.addTerminal(self, "buffer sizes", varType="Cluster")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "data type", varType="Void")
        LVNode.addTerminal(self, "base endpoint name", varType="String")
        self.attributes["type"] = "Create Unique Network Stream Endpoint"
        self.attributes["genclass"] = "Function"


class CreateUniqueNetworkStreamReaderEndpoint(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Create Unique Network Stream Reader Endpoint")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "reader endpoint", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "max connections (-1)", varType="I32")
        LVNode.addTerminal(self, "timeout in ms (-1)", varType="I32")
        LVNode.addTerminal(self, "element allocation mode", varType="U32")
        LVNode.addTerminal(self, "reader buffer size", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "data type", varType="Void")
        LVNode.addTerminal(self, "base reader name", varType="String")
        self.attributes["type"] = "Create Unique Network Stream Reader Endpoint"
        self.attributes["genclass"] = "Function"


class CreateUniqueNetworkStreamWriterEndpoint(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Create Unique Network Stream Writer Endpoint")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "writer endpoint", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "max connections (-1)", varType="I32")
        LVNode.addTerminal(self, "timeout in ms (-1)", varType="I32")
        LVNode.addTerminal(self, "element allocation mode", varType="U32")
        LVNode.addTerminal(self, "writer buffer size", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "data type", varType="Void")
        LVNode.addTerminal(self, "base writer name", varType="String")
        self.attributes["type"] = "Create Unique Network Stream Writer Endpoint"
        self.attributes["genclass"] = "Function"


class CreateUserEvent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Create User Event")
        LVNode.addTerminal(self, "user event datatype", varType="Cluster")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "user event", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Create User Event"
        self.attributes["genclass"] = "Function"


class CurrentProcessorId(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Current Processor ID")
        LVNode.addTerminal(self, "current processor ID", varType="I32", isInput=False)
        self.attributes["type"] = "Current Processor ID"
        self.attributes["genclass"] = "Function"


class CurrentViSMenubar(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Current VI's Menubar")
        LVNode.addTerminal(self, "menu reference", varType="Refnum", isInput=False)
        self.attributes["type"] = "Current VI's Menubar"
        self.attributes["genclass"] = "Function"


class CurrentViSPath(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Current VI's Path")
        LVNode.addTerminal(self, "path", varType="Path", isInput=False)
        self.attributes["type"] = "Current VI's Path"
        self.attributes["genclass"] = "Function"


class DataCacheSize(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Data Cache Size")
        LVNode.addTerminal(self, "cache level (2)", varType="I32")
        LVNode.addTerminal(self, "total cache size (in bytes)", varType="I32", isInput=False)
        LVNode.addTerminal(self, "cache entry size (in bytes)", varType="I32", isInput=False)
        self.attributes["type"] = "Data Cache Size"
        self.attributes["genclass"] = "Function"


class DatasocketClose(LVNode):
    def __init__(self):
        LVNode.__init__(self, "DataSocket Close")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "timed out", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "ms timeout (0)", varType="I32")
        LVNode.addTerminal(self, "connection id", varType="Refnum")
        self.attributes["type"] = "DataSocket Close"
        self.attributes["genclass"] = "Function"


class DatasocketOpen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "DataSocket Open")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "connection id", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "ms timeout (10000)", varType="I32")
        LVNode.addTerminal(self, "mode", varType="Enum U16")
        LVNode.addTerminal(self, "URL", varType="String")
        self.attributes["type"] = "DataSocket Open"
        self.attributes["genclass"] = "Function"


class DatasocketRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "DataSocket Read")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "timed out", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "data", varType="LV Variant", isInput=False)
        LVNode.addTerminal(self, "connection out", varType="String", isInput=False)
        LVNode.addTerminal(self, "timestamp", varType="Timestamp", isInput=False)
        LVNode.addTerminal(self, "quality", varType="U64", isInput=False)
        LVNode.addTerminal(self, "wait for updated value (T)", varType="Boolean")
        LVNode.addTerminal(self, "status", varType="U32", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "ms timeout (10000)", varType="I32")
        LVNode.addTerminal(self, "type (Variant)", varType="LV Variant")
        LVNode.addTerminal(self, "connection in", varType="String")
        self.attributes["type"] = "DataSocket Read"
        self.attributes["genclass"] = "Function"


class DatasocketWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "DataSocket Write")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "timed out", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "connection out", varType="String", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "ms timeout (0)", varType="I32")
        LVNode.addTerminal(self, "data", varType="Cluster")
        LVNode.addTerminal(self, "connection in", varType="String")
        self.attributes["type"] = "DataSocket Write"
        self.attributes["genclass"] = "Function"


class DateTimeToSeconds(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Date/Time To Seconds")
        LVNode.addTerminal(self, "time stamp", varType="Timestamp", isInput=False)
        LVNode.addTerminal(self, "is UTC (F)", varType="Boolean")
        LVNode.addTerminal(self, "date time rec", varType="Cluster")
        self.attributes["type"] = "Date/Time To Seconds"
        self.attributes["genclass"] = "Function"


class DecimalDigit(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Decimal Digit?")
        LVNode.addTerminal(self, "digit?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "char", varType="String")
        self.attributes["type"] = "Decimal Digit?"
        self.attributes["genclass"] = "Function"


class DecimalStringToNumber(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Decimal String To Number")
        LVNode.addTerminal(self, "number", varType="I32", isInput=False)
        LVNode.addTerminal(self, "offset past number", varType="I32", isInput=False)
        LVNode.addTerminal(self, "default (0L)", varType="I32")
        LVNode.addTerminal(self, "offset", varType="I32")
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "Decimal String To Number"
        self.attributes["genclass"] = "Function"


class Decrement(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Decrement")
        LVNode.addTerminal(self, "x-1", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Decrement"
        self.attributes["genclass"] = "Function"


class DefaultDirectory(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Default Directory")
        LVNode.addTerminal(self, "path", varType="Path", isInput=False)
        self.attributes["type"] = "Default Directory"
        self.attributes["genclass"] = "Function"


class Delete(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Delete")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "cancelled", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "deleted path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "prompt (Delete)", varType="String")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "confirm (F)", varType="Boolean")
        LVNode.addTerminal(self, "entire hierarchy (F)", varType="Boolean")
        LVNode.addTerminal(self, "path (use dialog)", varType="Path")
        self.attributes["type"] = "Delete"
        self.attributes["genclass"] = "Function"


class DeleteDeprecated(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Delete (deprecated)")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "dup path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "path", varType="Path")
        self.attributes["type"] = "Delete (deprecated)"
        self.attributes["genclass"] = "Function"


class DeleteDataValueReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Delete Data Value Reference")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "data value", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "data value reference", varType="Refnum")
        self.attributes["type"] = "Delete Data Value Reference"
        self.attributes["genclass"] = "Function"


class DeleteMenuItems(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Delete Menu Items")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "menu reference out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "items", varType="String")
        LVNode.addTerminal(self, "menu tag", varType="String")
        LVNode.addTerminal(self, "menu reference", varType="Refnum")
        self.attributes["type"] = "Delete Menu Items"
        self.attributes["genclass"] = "Function"


class DeleteVariantAttribute(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Delete Variant Attribute")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "found", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "Variant out", varType="LV Variant", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "name (all attributes)", varType="String")
        LVNode.addTerminal(self, "Variant", varType="LV Variant")
        self.attributes["type"] = "Delete Variant Attribute"
        self.attributes["genclass"] = "Function"


class DeleteWaveformAttribute(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Delete Waveform Attribute")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "no found", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "waveform out", varType="Waveform", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "name (all attributes)", varType="String")
        LVNode.addTerminal(self, "waveform", varType="Waveform")
        self.attributes["type"] = "Delete Waveform Attribute"
        self.attributes["genclass"] = "Function"


class DenyAccess(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Deny Access")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "deny mode (0:deny read/write)", varType="Enum U16")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Deny Access"
        self.attributes["genclass"] = "Function"


class DequeueElement(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Dequeue Element")
        LVNode.addTerminal(self, "queue", varType="Refnum")
        LVNode.addTerminal(self, "timeout in ms (-1)", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "queue out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "element", varType="String", isInput=False)
        LVNode.addTerminal(self, "timed out?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Dequeue Element"
        self.attributes["genclass"] = "Function"


class DestroyStreamEndpoint(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Destroy Stream Endpoint")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "endpoint in", varType="Refnum")
        self.attributes["type"] = "Destroy Stream Endpoint"
        self.attributes["genclass"] = "Function"


class DestroyUserEvent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Destroy User Event")
        LVNode.addTerminal(self, "user event", varType="Refnum")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Destroy User Event"
        self.attributes["genclass"] = "Function"


class Devclear(LVNode):
    def __init__(self):
        LVNode.__init__(self, "DevClear")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "address", varType="I16")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "DevClear"
        self.attributes["genclass"] = "Function"


class Devclearlist(LVNode):
    def __init__(self):
        LVNode.__init__(self, "DevClearList")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "address list", varType="Array")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "DevClearList"
        self.attributes["genclass"] = "Function"


class DeviceControlStatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Device Control/Status")
        LVNode.addTerminal(self, "new param", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "err", varType="I32", isInput=False)
        LVNode.addTerminal(self, "spc reset (F)", varType="Boolean")
        LVNode.addTerminal(self, "async (T)", varType="Boolean")
        LVNode.addTerminal(self, "param (-)", varType="Cluster")
        LVNode.addTerminal(self, "code (-)", varType="I32")
        LVNode.addTerminal(self, "ctrl/stat (T:ctrl)", varType="Boolean")
        LVNode.addTerminal(self, "device refnum", varType="Refnum")
        self.attributes["type"] = "Device Control/Status"
        self.attributes["genclass"] = "Function"


class Divide(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Divide")
        LVNode.addTerminal(self, "x/y", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Divide"
        self.attributes["genclass"] = "Function"


class DivideWithErrorTerminals(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Divide (with error terminals)")
        LVNode.addTerminal(self, "x/y", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        self.attributes["type"] = "Divide (with error terminals)"
        self.attributes["genclass"] = "Function"


class DynamicFpgaInterfaceCast(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Dynamic FPGA Interface Cast")
        LVNode.addTerminal(self, "Type", varType="Refnum")
        LVNode.addTerminal(self, "Session In", varType="Refnum")
        LVNode.addTerminal(self, "Session Out", varType="Refnum", isInput=False)
        self.attributes["type"] = "Dynamic FPGA Interface Cast"
        self.attributes["genclass"] = "Function"


class ElementOfSet(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Element of Set?")
        LVNode.addTerminal(self, "found?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "element", varType="String")
        LVNode.addTerminal(self, "set", varType="Set Collection")
        self.attributes["type"] = "Element of Set?"
        self.attributes["genclass"] = "Function"


class EmptyArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Empty Array?")
        LVNode.addTerminal(self, "empty?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "array", varType="Array")
        self.attributes["type"] = "Empty Array?"
        self.attributes["genclass"] = "Function"


class EmptyCollection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Empty Collection?")
        LVNode.addTerminal(self, "empty?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "collection", varType="Set Collection")
        self.attributes["type"] = "Empty Collection?"
        self.attributes["genclass"] = "Function"


class EmptyStringPath(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Empty String/Path?")
        LVNode.addTerminal(self, "empty?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "string/path", varType="String")
        self.attributes["type"] = "Empty String/Path?"
        self.attributes["genclass"] = "Function"


class EnableMenuTracking(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Enable Menu Tracking")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "menu reference out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "enable (T)", varType="Boolean")
        LVNode.addTerminal(self, "menu reference", varType="Refnum")
        self.attributes["type"] = "Enable Menu Tracking"
        self.attributes["genclass"] = "Function"


class Enablelocal(LVNode):
    def __init__(self):
        LVNode.__init__(self, "EnableLocal")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "address list", varType="Array")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "EnableLocal"
        self.attributes["genclass"] = "Function"


class Enableremote(LVNode):
    def __init__(self):
        LVNode.__init__(self, "EnableRemote")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "address list", varType="Array")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "EnableRemote"
        self.attributes["genclass"] = "Function"


class EnqueueElement(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Enqueue Element")
        LVNode.addTerminal(self, "queue", varType="Refnum")
        LVNode.addTerminal(self, "element", varType="String")
        LVNode.addTerminal(self, "timeout in ms (-1)", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "queue out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "timed out?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Enqueue Element"
        self.attributes["genclass"] = "Function"


class EnqueueElementAtOppositeEnd(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Enqueue Element At Opposite End")
        LVNode.addTerminal(self, "queue", varType="Refnum")
        LVNode.addTerminal(self, "element", varType="String")
        LVNode.addTerminal(self, "timeout in ms (-1)", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "queue out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "timed out?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Enqueue Element At Opposite End"
        self.attributes["genclass"] = "Function"


class Eof(LVNode):
    def __init__(self):
        LVNode.__init__(self, "EOF")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "offset", varType="I32", isInput=False)
        LVNode.addTerminal(self, "dup refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "pos offset (0)", varType="I32")
        LVNode.addTerminal(self, "pos mode (0:1)", varType="Enum U16")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "EOF"
        self.attributes["genclass"] = "Function"


class EqualTo0(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Equal To 0?")
        LVNode.addTerminal(self, "x = 0?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Equal To 0?"
        self.attributes["genclass"] = "Function"


class Equal(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Equal?")
        LVNode.addTerminal(self, "x = y?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Equal?"
        self.attributes["genclass"] = "Function"


class ExclusiveOr(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Exclusive Or")
        LVNode.addTerminal(self, "x .xor. y?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "y", varType="Boolean")
        LVNode.addTerminal(self, "x", varType="Boolean")
        self.attributes["type"] = "Exclusive Or"
        self.attributes["genclass"] = "Function"


class Exponential(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Exponential")
        LVNode.addTerminal(self, "exp(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Exponential"
        self.attributes["genclass"] = "Function"


class ExponentialArg1(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Exponential (Arg) -1")
        LVNode.addTerminal(self, "exp(x) -1", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Exponential (Arg) -1"
        self.attributes["genclass"] = "Function"


class FileDialog(LVNode):
    def __init__(self):
        LVNode.__init__(self, "File Dialog")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "cancelled", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "exists", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "selected path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "pattern label", varType="String")
        LVNode.addTerminal(self, "button label", varType="String")
        LVNode.addTerminal(self, "pattern (all files)", varType="String")
        LVNode.addTerminal(self, "prompt", varType="String")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "default name", varType="String")
        LVNode.addTerminal(self, "start path", varType="Path")
        self.attributes["type"] = "File Dialog"
        self.attributes["genclass"] = "Function"


class FileDialogDeprecated(LVNode):
    def __init__(self):
        LVNode.__init__(self, "File Dialog (deprecated)")
        LVNode.addTerminal(self, "cancelled", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "exists", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "pattern label", varType="String")
        LVNode.addTerminal(self, "button label", varType="String")
        LVNode.addTerminal(self, "datalog type", varType="I32")
        LVNode.addTerminal(self, "prompt", varType="String")
        LVNode.addTerminal(self, "pattern", varType="String")
        LVNode.addTerminal(self, "default name", varType="String")
        LVNode.addTerminal(self, "select mode (2)", varType="Enum U32")
        LVNode.addTerminal(self, "start path", varType="Path")
        self.attributes["type"] = "File Dialog (deprecated)"
        self.attributes["genclass"] = "Function"


class FileDirectoryInfo(LVNode):
    def __init__(self):
        LVNode.__init__(self, "File/Directory Info")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "last mod", varType="Timestamp", isInput=False)
        LVNode.addTerminal(self, "size", varType="I64", isInput=False)
        LVNode.addTerminal(self, "path out", varType="Path", isInput=False)
        LVNode.addTerminal(self, "resolved path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "directory", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "shortcut", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "path", varType="Path")
        self.attributes["type"] = "File/Directory Info"
        self.attributes["genclass"] = "Function"


class FileDirectoryInfoDeprecated(LVNode):
    def __init__(self):
        LVNode.__init__(self, "File/Directory Info (deprecated)")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "last mod", varType="Timestamp", isInput=False)
        LVNode.addTerminal(self, "size", varType="I32", isInput=False)
        LVNode.addTerminal(self, "dup path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "directory", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "path", varType="Path")
        self.attributes["type"] = "File/Directory Info (deprecated)"
        self.attributes["genclass"] = "Function"


class Findlstn(LVNode):
    def __init__(self):
        LVNode.__init__(self, "FindLstn")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "number of listeners", varType="I32", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "listener address list", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "limit", varType="I16")
        LVNode.addTerminal(self, "address list", varType="Array")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "FindLstn"
        self.attributes["genclass"] = "Function"


class Findrqs(LVNode):
    def __init__(self):
        LVNode.__init__(self, "FindRQS")
        LVNode.addTerminal(self, "bus", varType="I32")
        LVNode.addTerminal(self, "address list", varType="Array")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "requester status byte", varType="I16", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "requester index", varType="I32", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "FindRQS"
        self.attributes["genclass"] = "Function"


class FirstCall(LVNode):
    def __init__(self):
        LVNode.__init__(self, "First Call?")
        LVNode.addTerminal(self, "First Call?: T/F", varType="Boolean", isInput=False)
        self.attributes["type"] = "First Call?"
        self.attributes["genclass"] = "Function"


class FixedPointOverflow(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Fixed-Point Overflow?")
        LVNode.addTerminal(self, "overflow?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "FXP", varType="Fixed Point")
        self.attributes["type"] = "Fixed-Point Overflow?"
        self.attributes["genclass"] = "Function"


class FixedPointToIntegerCast(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Fixed-Point to Integer Cast")
        LVNode.addTerminal(self, "integer", varType="I32", isInput=False)
        LVNode.addTerminal(self, "fixed-point", varType="Fixed Point")
        self.attributes["type"] = "Fixed-Point to Integer Cast"
        self.attributes["genclass"] = "Function"


class FlattenToJson(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flatten To JSON")
        LVNode.addTerminal(self, "anything", varType="Cluster")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "enable LabVIEW extensions? (T)", varType="Boolean")
        LVNode.addTerminal(self, "JSON string", varType="String", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Flatten To JSON"
        self.attributes["genclass"] = "Function"


class FlattenToString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flatten To String")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "type string", varType="Array", isInput=False)
        LVNode.addTerminal(self, "data string", varType="String", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "byte order (0:big-endian, network order)", varType="Enum U16")
        LVNode.addTerminal(self, "prepend array or string size? (T)", varType="Boolean")
        LVNode.addTerminal(self, "anything", varType="Cluster")
        self.attributes["type"] = "Flatten To String"
        self.attributes["genclass"] = "Function"


class FlattenToXml(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flatten To XML")
        LVNode.addTerminal(self, "xml string", varType="String", isInput=False)
        LVNode.addTerminal(self, "anything", varType="Cluster")
        self.attributes["type"] = "Flatten To XML"
        self.attributes["genclass"] = "Function"


class FlattenedStringToVariant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flattened String To Variant")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "Variant", varType="LV Variant", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "data string", varType="String")
        LVNode.addTerminal(self, "type string", varType="Array")
        self.attributes["type"] = "Flattened String To Variant"
        self.attributes["genclass"] = "Function"


class FloatingPointEqual(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Floating Point Equal?")
        LVNode.addTerminal(self, "x ~ y?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "tolerance", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Floating Point Equal?"
        self.attributes["genclass"] = "Function"


class FlushEventQueue(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flush Event Queue")
        LVNode.addTerminal(self, "event registration refnum", varType="Refnum")
        LVNode.addTerminal(self, "include static events? (T)", varType="Boolean")
        LVNode.addTerminal(self, "event type or object", varType="Enum U32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "oldest event time", varType="U32")
        LVNode.addTerminal(self, "keep most recent", varType="I32")
        LVNode.addTerminal(self, "event reg refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "number of events discarded", varType="U32", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Flush Event Queue"
        self.attributes["genclass"] = "Function"


class FlushFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flush File")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Flush File"
        self.attributes["genclass"] = "Function"


class FlushFileDeprecated(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flush File (deprecated)")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "dup refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Flush File (deprecated)"
        self.attributes["genclass"] = "Function"


class FlushQueue(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flush Queue")
        LVNode.addTerminal(self, "queue", varType="Refnum")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "queue out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "remaining elements", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Flush Queue"
        self.attributes["genclass"] = "Function"


class FlushStream(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flush Stream")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "timed out?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "endpoint out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout in ms (-1)", varType="I32")
        LVNode.addTerminal(self, "wait condition", varType="U8")
        LVNode.addTerminal(self, "endpoint in", varType="Refnum")
        self.attributes["type"] = "Flush Stream"
        self.attributes["genclass"] = "Function"


class FormatDateTimeString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Format Date/Time String")
        LVNode.addTerminal(self, "date/time string", varType="String", isInput=False)
        LVNode.addTerminal(self, "UTC format", varType="Boolean")
        LVNode.addTerminal(self, "seconds (now)", varType="Timestamp")
        LVNode.addTerminal(self, "time format string (%c)", varType="String")
        self.attributes["type"] = "Format Date/Time String"
        self.attributes["genclass"] = "Function"


class FormatValue(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Format Value")
        LVNode.addTerminal(self, "output string", varType="String", isInput=False)
        LVNode.addTerminal(self, "value (0)", varType="Double Float")
        LVNode.addTerminal(self, "format string", varType="String")
        LVNode.addTerminal(self, "string ("")", varType="String")
        self.attributes["type"] = "Format Value"
        self.attributes["genclass"] = "Function"


class FpgaRefnumToSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "FPGA Refnum to Session")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "Session", varType="U64", isInput=False)
        LVNode.addTerminal(self, "error in(no error)", varType="Cluster")
        LVNode.addTerminal(self, "Refnum", varType="Refnum")
        self.attributes["type"] = "FPGA Refnum to Session"
        self.attributes["genclass"] = "Function"


class FractExpStringToNumber(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Fract/Exp String To Number")
        LVNode.addTerminal(self, "number", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "offset past number", varType="I32", isInput=False)
        LVNode.addTerminal(self, "use system decimal point (T)", varType="Boolean")
        LVNode.addTerminal(self, "default (0 dbl)", varType="Double Float")
        LVNode.addTerminal(self, "offset", varType="I32")
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "Fract/Exp String To Number"
        self.attributes["genclass"] = "Function"


class GenerateFrontPanelActivity(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Generate Front Panel Activity")
        LVNode.addTerminal(self, "front panel (this VI's panel)", varType="Refnum")
        self.attributes["type"] = "Generate Front Panel Activity"
        self.attributes["genclass"] = "Function"


class GenerateOccurrence(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Generate Occurrence")
        LVNode.addTerminal(self, "occurrence", varType="Refnum", isInput=False)
        self.attributes["type"] = "Generate Occurrence"
        self.attributes["genclass"] = "Function"


class GenerateUserEvent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Generate User Event")
        LVNode.addTerminal(self, "user event", varType="Refnum")
        LVNode.addTerminal(self, "event data cluster", varType="Cluster")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "priority (normal)", varType="Enum U32")
        LVNode.addTerminal(self, "user event out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Generate User Event"
        self.attributes["genclass"] = "Function"


class GenerateUserDefinedTraceEvent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Generate User-Defined Trace Event")
        LVNode.addTerminal(self, "trace integer", varType="I32")
        LVNode.addTerminal(self, "trace string", varType="String")
        self.attributes["type"] = "Generate User-Defined Trace Event"
        self.attributes["genclass"] = "Function"


class GetControlValuesByIndex(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Control Values by Index")
        LVNode.addTerminal(self, "VI Refnum", varType="Refnum")
        LVNode.addTerminal(self, "control indexes", varType="Array")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "data values", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Get Control Values by Index"
        self.attributes["genclass"] = "Function"


class GetDatalogPosition(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Datalog Position")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "offset (in records)", varType="I64", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Get Datalog Position"
        self.attributes["genclass"] = "Function"


class GetDateTimeInSeconds(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Date/Time In Seconds")
        LVNode.addTerminal(self, "seconds since 1Jan1904", varType="Timestamp", isInput=False)
        self.attributes["type"] = "Get Date/Time In Seconds"
        self.attributes["genclass"] = "Function"


class GetDateTimeString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Date/Time String")
        LVNode.addTerminal(self, "time string", varType="String", isInput=False)
        LVNode.addTerminal(self, "date string", varType="String", isInput=False)
        LVNode.addTerminal(self, "want seconds? (F)", varType="Boolean")
        LVNode.addTerminal(self, "seconds (now)", varType="Timestamp")
        LVNode.addTerminal(self, "date format (0)", varType="Enum U16")
        self.attributes["type"] = "Get Date/Time String"
        self.attributes["genclass"] = "Function"


class GetDragDropData(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Drag Drop Data")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "data", varType="String", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "type", varType="String")
        LVNode.addTerminal(self, "data name", varType="String")
        self.attributes["type"] = "Get Drag Drop Data"
        self.attributes["genclass"] = "Function"


class GetFilePosition(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get File Position")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "offset (in bytes)", varType="I64", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Get File Position"
        self.attributes["genclass"] = "Function"


class GetFileSize(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get File Size")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "size (in bytes)", varType="I64", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "file", varType="Path")
        self.attributes["type"] = "Get File Size"
        self.attributes["genclass"] = "Function"


class GetHelpWindowStatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Help Window Status")
        LVNode.addTerminal(self, "Top Left Corner", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "Show", varType="Boolean", isInput=False)
        self.attributes["type"] = "Get Help Window Status"
        self.attributes["genclass"] = "Function"


class GetMenuItemInfo(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Menu Item Info")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "enabled", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "item name", varType="String", isInput=False)
        LVNode.addTerminal(self, "menu reference out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "checked", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "submenu tags", varType="Array", isInput=False)
        LVNode.addTerminal(self, "short cut", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "item tag", varType="String")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "menu reference", varType="Refnum")
        self.attributes["type"] = "Get Menu Item Info"
        self.attributes["genclass"] = "Function"


class GetMenuSelection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Menu Selection")
        LVNode.addTerminal(self, "menu reference", varType="Refnum")
        LVNode.addTerminal(self, "ms timeout (200)", varType="I32")
        LVNode.addTerminal(self, "block menu (F)", varType="Boolean")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timed out", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "menu reference out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "item tag", varType="String", isInput=False)
        LVNode.addTerminal(self, "item path", varType="String", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Get Menu Selection"
        self.attributes["genclass"] = "Function"


class GetMenuShortCutInfo(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Menu Short Cut Info")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "item path", varType="String", isInput=False)
        LVNode.addTerminal(self, "item tag", varType="String", isInput=False)
        LVNode.addTerminal(self, "menu reference out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "short cut", varType="Cluster")
        LVNode.addTerminal(self, "menu reference", varType="Refnum")
        self.attributes["type"] = "Get Menu Short Cut Info"
        self.attributes["genclass"] = "Function"


class GetNotifierStatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Notifier Status")
        LVNode.addTerminal(self, "notifier", varType="Refnum")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "notifier name", varType="String", isInput=False)
        LVNode.addTerminal(self, "notifier out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "current notification", varType="String", isInput=False)
        LVNode.addTerminal(self, "# waiting", varType="I32", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Get Notifier Status"
        self.attributes["genclass"] = "Function"


class GetNumberOfRecords(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Number of Records")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "# of records", varType="I64", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Get Number of Records"
        self.attributes["genclass"] = "Function"


class GetPermissions(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Permissions")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "group", varType="String", isInput=False)
        LVNode.addTerminal(self, "owner", varType="String", isInput=False)
        LVNode.addTerminal(self, "path out", varType="Path", isInput=False)
        LVNode.addTerminal(self, "permissions", varType="I16", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "path", varType="Path")
        self.attributes["type"] = "Get Permissions"
        self.attributes["genclass"] = "Function"


class GetQueueStatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Queue Status")
        LVNode.addTerminal(self, "queue", varType="Refnum")
        LVNode.addTerminal(self, "return elements? (F)", varType="Boolean")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "max queue size", varType="I32", isInput=False)
        LVNode.addTerminal(self, "elements", varType="Array", isInput=False)
        LVNode.addTerminal(self, "queue name", varType="String", isInput=False)
        LVNode.addTerminal(self, "# elements in queue", varType="I32", isInput=False)
        LVNode.addTerminal(self, "queue out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "# pending remove", varType="I32", isInput=False)
        LVNode.addTerminal(self, "# pending insert", varType="I32", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Get Queue Status"
        self.attributes["genclass"] = "Function"


class GetTypeAndCreator(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Type and Creator")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "creator", varType="String", isInput=False)
        LVNode.addTerminal(self, "type", varType="String", isInput=False)
        LVNode.addTerminal(self, "path out", varType="Path", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "path", varType="Path")
        self.attributes["type"] = "Get Type and Creator"
        self.attributes["genclass"] = "Function"


class GetVariantAttribute(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Variant Attribute")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "values", varType="Array", isInput=False)
        LVNode.addTerminal(self, "names", varType="Array", isInput=False)
        LVNode.addTerminal(self, "duplicate Variant", varType="LV Variant", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "default value (empty Variant)", varType="LV Variant")
        LVNode.addTerminal(self, "name", varType="String")
        LVNode.addTerminal(self, "Variant", varType="LV Variant")
        self.attributes["type"] = "Get Variant Attribute"
        self.attributes["genclass"] = "Function"


class GetVolumeInfo(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Volume Info")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "free (bytes)", varType="I64", isInput=False)
        LVNode.addTerminal(self, "size (bytes)", varType="I64", isInput=False)
        LVNode.addTerminal(self, "path out", varType="Path", isInput=False)
        LVNode.addTerminal(self, "", varType="U32", isInput=False)
        LVNode.addTerminal(self, "volume path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "path", varType="Path")
        self.attributes["type"] = "Get Volume Info"
        self.attributes["genclass"] = "Function"


class GetWaveformAttribute(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Waveform Attribute")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "values", varType="Array", isInput=False)
        LVNode.addTerminal(self, "names", varType="Array", isInput=False)
        LVNode.addTerminal(self, "duplicate waveform", varType="Waveform", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "default value (empty Variant)", varType="LV Variant")
        LVNode.addTerminal(self, "name", varType="String")
        LVNode.addTerminal(self, "waveform", varType="Waveform")
        self.attributes["type"] = "Get Waveform Attribute"
        self.attributes["genclass"] = "Function"


class GpibClear(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Clear")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "address string", varType="String")
        self.attributes["type"] = "GPIB Clear"
        self.attributes["genclass"] = "Function"


class GpibInitialization(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Initialization")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "require re-addressing (T)", varType="Boolean")
        LVNode.addTerminal(self, "disallow DMA (F)", varType="Boolean")
        LVNode.addTerminal(self, "assert REN with IFC (T)", varType="Boolean")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "IST bit sense (T)", varType="Boolean")
        LVNode.addTerminal(self, "address string", varType="String")
        LVNode.addTerminal(self, "system controller (T)", varType="Boolean")
        self.attributes["type"] = "GPIB Initialization"
        self.attributes["genclass"] = "Function"


class GpibMisc(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Misc")
        LVNode.addTerminal(self, "command string", varType="String")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "output string", varType="String", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "GPIB Misc"
        self.attributes["genclass"] = "Function"


class GpibRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Read")
        LVNode.addTerminal(self, "address string", varType="String")
        LVNode.addTerminal(self, "byte count", varType="I32")
        LVNode.addTerminal(self, "mode (0)", varType="I16")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (488.2 global)", varType="I32")
        LVNode.addTerminal(self, "data", varType="String", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "GPIB Read"
        self.attributes["genclass"] = "Function"


class GpibSerialPoll(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Serial Poll")
        LVNode.addTerminal(self, "address string", varType="String")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "serial poll byte", varType="I16", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "GPIB Serial Poll"
        self.attributes["genclass"] = "Function"


class GpibStatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Status")
        LVNode.addTerminal(self, "address string", varType="String")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "GPIB error", varType="I16", isInput=False)
        LVNode.addTerminal(self, "byte count", varType="I32", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "GPIB Status"
        self.attributes["genclass"] = "Function"


class GpibTrigger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Trigger")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "address string", varType="String")
        self.attributes["type"] = "GPIB Trigger"
        self.attributes["genclass"] = "Function"


class GpibWait(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Wait")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "timeout ms (488.2 global)", varType="I32")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "wait state vector", varType="Array")
        LVNode.addTerminal(self, "address string", varType="String")
        self.attributes["type"] = "GPIB Wait"
        self.attributes["genclass"] = "Function"


class GpibWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Write")
        LVNode.addTerminal(self, "address string", varType="String")
        LVNode.addTerminal(self, "data", varType="String")
        LVNode.addTerminal(self, "mode (0)", varType="I16")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (488.2 global)", varType="I32")
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "GPIB Write"
        self.attributes["genclass"] = "Function"


class GreaterOrEqualTo0(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Greater Or Equal To 0?")
        LVNode.addTerminal(self, "x >= 0?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Greater Or Equal To 0?"
        self.attributes["genclass"] = "Function"


class GreaterOrEqual(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Greater Or Equal?")
        LVNode.addTerminal(self, "x >= y?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Greater Or Equal?"
        self.attributes["genclass"] = "Function"


class GreaterThan0(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Greater Than 0?")
        LVNode.addTerminal(self, "x > 0?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Greater Than 0?"
        self.attributes["genclass"] = "Function"


class Greater(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Greater?")
        LVNode.addTerminal(self, "x > y?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Greater?"
        self.attributes["genclass"] = "Function"


class HandlePeek(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Handle Peek")
        LVNode.addTerminal(self, "value", varType="I32", isInput=False)
        LVNode.addTerminal(self, "error", varType="I32", isInput=False)
        LVNode.addTerminal(self, "num type (long)", varType="I32")
        LVNode.addTerminal(self, "offset", varType="I32")
        LVNode.addTerminal(self, "handle", varType="Void")
        self.attributes["type"] = "Handle Peek"
        self.attributes["genclass"] = "Function"


class HandlePoke(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Handle Poke")
        LVNode.addTerminal(self, "old value", varType="I32", isInput=False)
        LVNode.addTerminal(self, "handle", varType="Void", isInput=False)
        LVNode.addTerminal(self, "error", varType="I32", isInput=False)
        LVNode.addTerminal(self, "new value", varType="I32")
        LVNode.addTerminal(self, "offset", varType="I32")
        LVNode.addTerminal(self, "handle", varType="Void")
        self.attributes["type"] = "Handle Poke"
        self.attributes["genclass"] = "Function"


class HexDigit(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Hex Digit?")
        LVNode.addTerminal(self, "hex?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "char", varType="String")
        self.attributes["type"] = "Hex Digit?"
        self.attributes["genclass"] = "Function"


class HexadecimalStringToNumber(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Hexadecimal String To Number")
        LVNode.addTerminal(self, "number", varType="U32", isInput=False)
        LVNode.addTerminal(self, "offset past number", varType="I32", isInput=False)
        LVNode.addTerminal(self, "default (0uL)", varType="U32")
        LVNode.addTerminal(self, "offset", varType="I32")
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "Hexadecimal String To Number"
        self.attributes["genclass"] = "Function"


class HyperbolicCosecant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Hyperbolic Cosecant")
        LVNode.addTerminal(self, "csch(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Hyperbolic Cosecant"
        self.attributes["genclass"] = "Function"


class HyperbolicCosine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Hyperbolic Cosine")
        LVNode.addTerminal(self, "cosh(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Hyperbolic Cosine"
        self.attributes["genclass"] = "Function"


class HyperbolicCotangent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Hyperbolic Cotangent")
        LVNode.addTerminal(self, "coth(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Hyperbolic Cotangent"
        self.attributes["genclass"] = "Function"


class HyperbolicSecant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Hyperbolic Secant")
        LVNode.addTerminal(self, "sech(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Hyperbolic Secant"
        self.attributes["genclass"] = "Function"


class HyperbolicSine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Hyperbolic Sine")
        LVNode.addTerminal(self, "sinh(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Hyperbolic Sine"
        self.attributes["genclass"] = "Function"


class HyperbolicTangent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Hyperbolic Tangent")
        LVNode.addTerminal(self, "tanh(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Hyperbolic Tangent"
        self.attributes["genclass"] = "Function"


class Implies(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Implies")
        LVNode.addTerminal(self, "x .implies. y?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "y", varType="Boolean")
        LVNode.addTerminal(self, "x", varType="Boolean")
        self.attributes["type"] = "Implies"
        self.attributes["genclass"] = "Function"


class InRangeAndCoerce(LVNode):
    def __init__(self):
        LVNode.__init__(self, "In Range and Coerce")
        LVNode.addTerminal(self, "In Range?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "coerced(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "lower limit", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        LVNode.addTerminal(self, "upper limit", varType="Double Float")
        self.attributes["type"] = "In Range and Coerce"
        self.attributes["genclass"] = "Function"


class IncludeFixedPointOverflowStatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Include Fixed-Point Overflow Status")
        LVNode.addTerminal(self, "FXP with overflow included", varType="Fixed Point", isInput=False)
        LVNode.addTerminal(self, "overflow", varType="Boolean")
        LVNode.addTerminal(self, "FXP", varType="Fixed Point")
        self.attributes["type"] = "Include Fixed-Point Overflow Status"
        self.attributes["genclass"] = "Function"


class Increment(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Increment")
        LVNode.addTerminal(self, "x+1", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Increment"
        self.attributes["genclass"] = "Function"


class IndexStringArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Index String Array")
        LVNode.addTerminal(self, "output string", varType="String", isInput=False)
        LVNode.addTerminal(self, "index", varType="I32")
        LVNode.addTerminal(self, "string array", varType="Array")
        LVNode.addTerminal(self, "string ("")", varType="String")
        self.attributes["type"] = "Index String Array"
        self.attributes["genclass"] = "Function"


class InsertIntoMap(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Insert Into Map")
        LVNode.addTerminal(self, "value unchanged?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "key already included?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "map out", varType="Map Collection", isInput=False)
        LVNode.addTerminal(self, "value", varType="I32")
        LVNode.addTerminal(self, "key", varType="String")
        LVNode.addTerminal(self, "map in", varType="Map Collection")
        self.attributes["type"] = "Insert Into Map"
        self.attributes["genclass"] = "Function"


class InsertIntoSet(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Insert Into Set")
        LVNode.addTerminal(self, "already included?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "set out", varType="Set Collection", isInput=False)
        LVNode.addTerminal(self, "element", varType="String")
        LVNode.addTerminal(self, "set in", varType="Set Collection")
        self.attributes["type"] = "Insert Into Set"
        self.attributes["genclass"] = "Function"


class InsertMenuItems(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Insert Menu Items")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "item tags out", varType="Array", isInput=False)
        LVNode.addTerminal(self, "menu reference out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "after item", varType="String")
        LVNode.addTerminal(self, "menu tag", varType="String")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "item tags", varType="Array")
        LVNode.addTerminal(self, "item names", varType="Array")
        LVNode.addTerminal(self, "menu reference", varType="Refnum")
        self.attributes["type"] = "Insert Menu Items"
        self.attributes["genclass"] = "Function"


class IntegerToFixedPointCast(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Integer to Fixed-Point Cast")
        LVNode.addTerminal(self, "integer", varType="I32")
        LVNode.addTerminal(self, "fixed-point type", varType="Fixed Point")
        LVNode.addTerminal(self, "fixed-point", varType="Fixed Point", isInput=False)
        self.attributes["type"] = "Integer to Fixed-Point Cast"
        self.attributes["genclass"] = "Function"


class Interpolate1dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Interpolate 1D Array")
        LVNode.addTerminal(self, "y value", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "fractional index or x", varType="Double Float")
        LVNode.addTerminal(self, "array of numbers or points", varType="Array")
        self.attributes["type"] = "Interpolate 1D Array"
        self.attributes["genclass"] = "Function"


class InverseCosecant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Cosecant")
        LVNode.addTerminal(self, "arccsc(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Inverse Cosecant"
        self.attributes["genclass"] = "Function"


class InverseCosine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Cosine")
        LVNode.addTerminal(self, "arccos(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Inverse Cosine"
        self.attributes["genclass"] = "Function"


class InverseCotangent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Cotangent")
        LVNode.addTerminal(self, "arccot(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Inverse Cotangent"
        self.attributes["genclass"] = "Function"


class InverseHyperbolicCosecant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Hyperbolic Cosecant")
        LVNode.addTerminal(self, "arccsch(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Inverse Hyperbolic Cosecant"
        self.attributes["genclass"] = "Function"


class InverseHyperbolicCosine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Hyperbolic Cosine")
        LVNode.addTerminal(self, "argcosh(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Inverse Hyperbolic Cosine"
        self.attributes["genclass"] = "Function"


class InverseHyperbolicCotangent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Hyperbolic Cotangent")
        LVNode.addTerminal(self, "arccoth(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Inverse Hyperbolic Cotangent"
        self.attributes["genclass"] = "Function"


class InverseHyperbolicSecant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Hyperbolic Secant")
        LVNode.addTerminal(self, "arcsech(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Inverse Hyperbolic Secant"
        self.attributes["genclass"] = "Function"


class InverseHyperbolicSine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Hyperbolic Sine")
        LVNode.addTerminal(self, "argsinh(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Inverse Hyperbolic Sine"
        self.attributes["genclass"] = "Function"


class InverseHyperbolicTangent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Hyperbolic Tangent")
        LVNode.addTerminal(self, "argtanh(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Inverse Hyperbolic Tangent"
        self.attributes["genclass"] = "Function"


class InverseSecant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Secant")
        LVNode.addTerminal(self, "arcsec(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Inverse Secant"
        self.attributes["genclass"] = "Function"


class InverseSine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Sine")
        LVNode.addTerminal(self, "arcsin(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Inverse Sine"
        self.attributes["genclass"] = "Function"


class InverseTangent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Tangent")
        LVNode.addTerminal(self, "arctan(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Inverse Tangent"
        self.attributes["genclass"] = "Function"


class InverseTangent2Input(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Tangent (2 Input)")
        LVNode.addTerminal(self, "atan2(y,x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        LVNode.addTerminal(self, "y", varType="Double Float")
        self.attributes["type"] = "Inverse Tangent (2 Input)"
        self.attributes["genclass"] = "Function"


class IpToString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IP To String")
        LVNode.addTerminal(self, "name", varType="String", isInput=False)
        LVNode.addTerminal(self, "dot notation? (F)", varType="Boolean")
        LVNode.addTerminal(self, "net address", varType="U32")
        self.attributes["type"] = "IP To String"
        self.attributes["genclass"] = "Function"


class IrdaCloseConnection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IrDA Close Connection")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "connection ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "abort (F)", varType="Boolean")
        LVNode.addTerminal(self, "connection ID", varType="Refnum")
        self.attributes["type"] = "IrDA Close Connection"
        self.attributes["genclass"] = "Function"


class IrdaCreateListener(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IrDA Create Listener")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "listener ID", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "service name", varType="String")
        self.attributes["type"] = "IrDA Create Listener"
        self.attributes["genclass"] = "Function"


class IrdaDiscover(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IrDA Discover")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "device list", varType="Array", isInput=False)
        LVNode.addTerminal(self, "number of devices", varType="U16", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        self.attributes["type"] = "IrDA Discover"
        self.attributes["genclass"] = "Function"


class IrdaOpenConnection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IrDA Open Connection")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "connection ID", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (60000)", varType="I32")
        LVNode.addTerminal(self, "remote device id", varType="U32")
        LVNode.addTerminal(self, "service name", varType="String")
        self.attributes["type"] = "IrDA Open Connection"
        self.attributes["genclass"] = "Function"


class IrdaRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IrDA Read")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "data out", varType="String", isInput=False)
        LVNode.addTerminal(self, "connection ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "mode (standard)", varType="Enum U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (25000)", varType="I32")
        LVNode.addTerminal(self, "bytes to read", varType="I32")
        LVNode.addTerminal(self, "connection ID", varType="Refnum")
        self.attributes["type"] = "IrDA Read"
        self.attributes["genclass"] = "Function"


class IrdaWaitOnListener(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IrDA Wait On Listener")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "remote device ID", varType="U32", isInput=False)
        LVNode.addTerminal(self, "remote LSAP-SEL", varType="String", isInput=False)
        LVNode.addTerminal(self, "listener ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "connection ID", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (wait forever: -1)", varType="I32")
        LVNode.addTerminal(self, "resolve remote address (T)", varType="Boolean")
        LVNode.addTerminal(self, "listener ID in", varType="Refnum")
        self.attributes["type"] = "IrDA Wait On Listener"
        self.attributes["genclass"] = "Function"


class IrdaWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IrDA Write")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "bytes written", varType="I32", isInput=False)
        LVNode.addTerminal(self, "connection ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (25000)", varType="I32")
        LVNode.addTerminal(self, "data in", varType="String")
        LVNode.addTerminal(self, "connection ID", varType="Refnum")
        self.attributes["type"] = "IrDA Write"
        self.attributes["genclass"] = "Function"


class Isdebuggingactive(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IsDebuggingActive")
        LVNode.addTerminal(self, "debugging?", varType="Boolean", isInput=False)
        self.attributes["type"] = "IsDebuggingActive"
        self.attributes["genclass"] = "Function"


class IviDeleteSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IVI Delete Session")
        LVNode.addTerminal(self, "IVI session", varType="Refnum")
        self.attributes["type"] = "IVI Delete Session"
        self.attributes["genclass"] = "Function"


class IviNewSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IVI New Session")
        LVNode.addTerminal(self, "IVI session", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "IVI session handle", varType="U32")
        LVNode.addTerminal(self, "resource name ("")", varType="String")
        LVNode.addTerminal(self, "IVI session (for class)", varType="Refnum")
        self.attributes["type"] = "IVI New Session"
        self.attributes["genclass"] = "Function"


class JoinNumbers(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Join Numbers")
        LVNode.addTerminal(self, "(hi.lo)", varType="U32", isInput=False)
        LVNode.addTerminal(self, "lo", varType="U16")
        LVNode.addTerminal(self, "hi", varType="U16")
        self.attributes["type"] = "Join Numbers"
        self.attributes["genclass"] = "Function"


class LeakVariantValueReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Leak Variant Value Reference")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "variant value ref out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "variant value ref in", varType="Refnum")
        self.attributes["type"] = "Leak Variant Value Reference"
        self.attributes["genclass"] = "Function"


class LessOrEqualTo0(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Less Or Equal To 0?")
        LVNode.addTerminal(self, "x <= 0?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Less Or Equal To 0?"
        self.attributes["genclass"] = "Function"


class LessOrEqual(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Less Or Equal?")
        LVNode.addTerminal(self, "x <= y?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Less Or Equal?"
        self.attributes["genclass"] = "Function"


class LessThan0(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Less Than 0?")
        LVNode.addTerminal(self, "x < 0?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Less Than 0?"
        self.attributes["genclass"] = "Function"


class Less(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Less?")
        LVNode.addTerminal(self, "x < y?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Less?"
        self.attributes["genclass"] = "Function"


class LexicalClass(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Lexical Class")
        LVNode.addTerminal(self, "class number", varType="I16", isInput=False)
        LVNode.addTerminal(self, "char", varType="String")
        self.attributes["type"] = "Lexical Class"
        self.attributes["genclass"] = "Function"


class ListDirectory(LVNode):
    def __init__(self):
        LVNode.__init__(self, "List Directory")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "folder names", varType="Array", isInput=False)
        LVNode.addTerminal(self, "file names", varType="Array", isInput=False)
        LVNode.addTerminal(self, "dup folder path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "datalog type", varType="I32")
        LVNode.addTerminal(self, "pattern", varType="String")
        LVNode.addTerminal(self, "folder path", varType="Path")
        self.attributes["type"] = "List Directory"
        self.attributes["genclass"] = "Function"


class ListFolder(LVNode):
    def __init__(self):
        LVNode.__init__(self, "List Folder")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "folder names", varType="Array", isInput=False)
        LVNode.addTerminal(self, "filenames", varType="Array", isInput=False)
        LVNode.addTerminal(self, "path out", varType="Path", isInput=False)
        LVNode.addTerminal(self, "datalog type", varType="I32")
        LVNode.addTerminal(self, "pattern", varType="String")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "path", varType="Path")
        self.attributes["type"] = "List Folder"
        self.attributes["genclass"] = "Function"


class LoadCertificatesIntoMemory(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Load Certificates Into Memory")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "certificates", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "format", varType="Enum U32")
        LVNode.addTerminal(self, "path to certificates", varType="Path")
        self.attributes["type"] = "Load Certificates Into Memory"
        self.attributes["genclass"] = "Function"


class LoadPrivateKeyIntoMemory(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Load Private Key Into Memory")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "private key", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "password", varType="String")
        LVNode.addTerminal(self, "format", varType="Enum U32")
        LVNode.addTerminal(self, "path to private key", varType="Path")
        self.attributes["type"] = "Load Private Key Into Memory"
        self.attributes["genclass"] = "Function"


class LockRange(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Lock Range")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "dup refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "count", varType="I32")
        LVNode.addTerminal(self, "set lock (F)", varType="Boolean")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "pos offset (0)", varType="I32")
        LVNode.addTerminal(self, "pos mode (0:2)", varType="Enum U16")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Lock Range"
        self.attributes["genclass"] = "Function"


class LogarithmBase10(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Logarithm Base 10")
        LVNode.addTerminal(self, "log(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Logarithm Base 10"
        self.attributes["genclass"] = "Function"


class LogarithmBase2(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Logarithm Base 2")
        LVNode.addTerminal(self, "log2(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Logarithm Base 2"
        self.attributes["genclass"] = "Function"


class LogarithmBaseX(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Logarithm Base X")
        LVNode.addTerminal(self, "logx(y)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        LVNode.addTerminal(self, "y", varType="Double Float")
        self.attributes["type"] = "Logarithm Base X"
        self.attributes["genclass"] = "Function"


class LogicalShift(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Logical Shift")
        LVNode.addTerminal(self, "x << y", varType="U32", isInput=False)
        LVNode.addTerminal(self, "x", varType="U32")
        LVNode.addTerminal(self, "y", varType="I16")
        self.attributes["type"] = "Logical Shift"
        self.attributes["genclass"] = "Function"


class LookInMap(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Look In Map")
        LVNode.addTerminal(self, "value", varType="I32", isInput=False)
        LVNode.addTerminal(self, "key not found?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "default value", varType="I32")
        LVNode.addTerminal(self, "key", varType="String")
        LVNode.addTerminal(self, "map", varType="Map Collection")
        self.attributes["type"] = "Look In Map"
        self.attributes["genclass"] = "Function"


class LookupChannelProbe(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Lookup Channel Probe")
        LVNode.addTerminal(self, "refnum to monitor", varType="Refnum")
        LVNode.addTerminal(self, "probe type specifier", varType="Refnum")
        LVNode.addTerminal(self, "force create?", varType="Boolean")
        LVNode.addTerminal(self, "probe VI refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "type mismatched?", varType="Boolean", isInput=False)
        self.attributes["type"] = "Lookup Channel Probe"
        self.attributes["genclass"] = "Function"


class LossyEnqueueElement(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Lossy Enqueue Element")
        LVNode.addTerminal(self, "queue", varType="Refnum")
        LVNode.addTerminal(self, "element", varType="String")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "queue out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "overflow element", varType="String", isInput=False)
        LVNode.addTerminal(self, "overflow?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Lossy Enqueue Element"
        self.attributes["genclass"] = "Function"


class MakeTlsConfigurationImmutable(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Make TLS Configuration Immutable")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "immutable TLS configuration", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "TLS configuration", varType="Refnum")
        self.attributes["type"] = "Make TLS Configuration Immutable"
        self.attributes["genclass"] = "Function"


class Makeaddr(LVNode):
    def __init__(self):
        LVNode.__init__(self, "MakeAddr")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "packed address", varType="I16", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "secondary address", varType="I16")
        LVNode.addTerminal(self, "primary address", varType="I16")
        self.attributes["type"] = "MakeAddr"
        self.attributes["genclass"] = "Function"


class MantissaExponent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Mantissa & Exponent")
        LVNode.addTerminal(self, "number", varType="Double Float")
        LVNode.addTerminal(self, "mantissa", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "exponent", varType="Double Float", isInput=False)
        self.attributes["type"] = "Mantissa & Exponent"
        self.attributes["genclass"] = "Function"


class MatchFirstString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Match First String")
        LVNode.addTerminal(self, "index", varType="I32", isInput=False)
        LVNode.addTerminal(self, "output string", varType="String", isInput=False)
        LVNode.addTerminal(self, "string array", varType="Array")
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "Match First String"
        self.attributes["genclass"] = "Function"


class MatchPattern(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Match Pattern")
        LVNode.addTerminal(self, "string", varType="String")
        LVNode.addTerminal(self, "regular expression", varType="String")
        LVNode.addTerminal(self, "offset (0)", varType="I32")
        LVNode.addTerminal(self, "before substring", varType="String", isInput=False)
        LVNode.addTerminal(self, "match substring", varType="String", isInput=False)
        LVNode.addTerminal(self, "after substring", varType="String", isInput=False)
        LVNode.addTerminal(self, "offset past match", varType="I32", isInput=False)
        self.attributes["type"] = "Match Pattern"
        self.attributes["genclass"] = "Function"


class MatchTrueFalseString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Match True/False String")
        LVNode.addTerminal(self, "selection", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "output string", varType="String", isInput=False)
        LVNode.addTerminal(self, "false string", varType="String")
        LVNode.addTerminal(self, "true string", varType="String")
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "Match True/False String"
        self.attributes["genclass"] = "Function"


class MatrixSize(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Matrix Size")
        LVNode.addTerminal(self, "number of rows", varType="Array")
        LVNode.addTerminal(self, "number of columns", varType="I32", isInput=False)
        LVNode.addTerminal(self, "matrix", varType="I32", isInput=False)
        self.attributes["type"] = "Matrix Size"
        self.attributes["genclass"] = "Function"


class MaxMin(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Max & Min")
        LVNode.addTerminal(self, "min(x,y)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "max(x,y)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Max & Min"
        self.attributes["genclass"] = "Function"


class Move(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Move")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "cancelled", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "new path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "prompt (Choose or enter target path for move)", varType="String")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "overwrite (F)", varType="Boolean")
        LVNode.addTerminal(self, "target path (use dialog)", varType="Path")
        LVNode.addTerminal(self, "source path", varType="Path")
        self.attributes["type"] = "Move"
        self.attributes["genclass"] = "Function"


class MoveDeprecated(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Move (deprecated)")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "new path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "target path", varType="Path")
        LVNode.addTerminal(self, "source path", varType="Path")
        self.attributes["type"] = "Move (deprecated)"
        self.attributes["genclass"] = "Function"


class Multiply(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Multiply")
        LVNode.addTerminal(self, "x*y", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Multiply"
        self.attributes["genclass"] = "Function"


class MultiplyWithErrorTerminals(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Multiply (with error terminals)")
        LVNode.addTerminal(self, "x*y", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        self.attributes["type"] = "Multiply (with error terminals)"
        self.attributes["genclass"] = "Function"


class MultiplyArrayElements(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Multiply Array Elements")
        LVNode.addTerminal(self, "product", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "numeric array", varType="Array")
        self.attributes["type"] = "Multiply Array Elements"
        self.attributes["genclass"] = "Function"


class NaturalLogarithm(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Natural Logarithm")
        LVNode.addTerminal(self, "ln(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Natural Logarithm"
        self.attributes["genclass"] = "Function"


class NaturalLogarithmArg1(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Natural Logarithm (Arg +1)")
        LVNode.addTerminal(self, "ln(x+1)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Natural Logarithm (Arg +1)"
        self.attributes["genclass"] = "Function"


class Negate(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Negate")
        LVNode.addTerminal(self, "-x", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Negate"
        self.attributes["genclass"] = "Function"


class NewDataValueReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "New Data Value Reference")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "data value reference", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "data value", varType="Double Float")
        self.attributes["type"] = "New Data Value Reference"
        self.attributes["genclass"] = "Function"


class NewDirectory(LVNode):
    def __init__(self):
        LVNode.__init__(self, "New Directory")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "dup directory path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "permissions", varType="I16")
        LVNode.addTerminal(self, "group", varType="String")
        LVNode.addTerminal(self, "directory path", varType="Path")
        self.attributes["type"] = "New Directory"
        self.attributes["genclass"] = "Function"


class NewFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "New File")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "datalog type", varType="I32")
        LVNode.addTerminal(self, "overwrite (F)", varType="Boolean")
        LVNode.addTerminal(self, "permissions", varType="I16")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "deny mode (2)", varType="Enum U16")
        LVNode.addTerminal(self, "group", varType="String")
        LVNode.addTerminal(self, "file path", varType="Path")
        self.attributes["type"] = "New File"
        self.attributes["genclass"] = "Function"


class NewTlsConfiguration(LVNode):
    def __init__(self):
        LVNode.__init__(self, "New TLS Configuration")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "TLS configuration out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "load OS trusted CAs?", varType="Boolean")
        self.attributes["type"] = "New TLS Configuration"
        self.attributes["genclass"] = "Function"


class NewVi(LVNode):
    def __init__(self):
        LVNode.__init__(self, "New VI")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "vi refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "type specifier VI Refnum (for type only)", varType="Refnum")
        LVNode.addTerminal(self, "password", varType="String")
        LVNode.addTerminal(self, "not connected", varType="U32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "vi type (standard vi)", varType="Enum U32")
        LVNode.addTerminal(self, "template", varType="Path")
        LVNode.addTerminal(self, "application refnum", varType="Refnum")
        self.attributes["type"] = "New VI"
        self.attributes["genclass"] = "Function"


class NewViObject(LVNode):
    def __init__(self):
        LVNode.__init__(self, "New VI Object")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "object refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "bounds", varType="Cluster")
        LVNode.addTerminal(self, "auto wire? (F)", varType="Boolean")
        LVNode.addTerminal(self, "path", varType="Path")
        LVNode.addTerminal(self, "vi object class", varType="Refnum")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "position/next to", varType="Cluster")
        LVNode.addTerminal(self, "style", varType="U32")
        LVNode.addTerminal(self, "owner refnum", varType="Refnum")
        self.attributes["type"] = "New VI Object"
        self.attributes["genclass"] = "Function"


class Not(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Not")
        LVNode.addTerminal(self, ".not. x?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "x", varType="Boolean")
        self.attributes["type"] = "Not"
        self.attributes["genclass"] = "Function"


class NotANumberPathRefnum(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Not A Number/Path/Refnum?")
        LVNode.addTerminal(self, "NaN/Path/Refnum?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "number/path/refnum", varType="Double Float")
        self.attributes["type"] = "Not A Number/Path/Refnum?"
        self.attributes["genclass"] = "Function"


class NotAnd(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Not And")
        LVNode.addTerminal(self, ".not. (x .and. y)?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "y", varType="Boolean")
        LVNode.addTerminal(self, "x", varType="Boolean")
        self.attributes["type"] = "Not And"
        self.attributes["genclass"] = "Function"


class NotEqualTo0(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Not Equal To 0?")
        LVNode.addTerminal(self, "x != 0?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Not Equal To 0?"
        self.attributes["genclass"] = "Function"


class NotEqual(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Not Equal?")
        LVNode.addTerminal(self, "x != y?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Not Equal?"
        self.attributes["genclass"] = "Function"


class NotExclusiveOr(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Not Exclusive Or")
        LVNode.addTerminal(self, ".not. (x .xor. y)?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "y", varType="Boolean")
        LVNode.addTerminal(self, "x", varType="Boolean")
        self.attributes["type"] = "Not Exclusive Or"
        self.attributes["genclass"] = "Function"


class NotOr(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Not Or")
        LVNode.addTerminal(self, ".not. (x .or. y)?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "y", varType="Boolean")
        LVNode.addTerminal(self, "x", varType="Boolean")
        self.attributes["type"] = "Not Or"
        self.attributes["genclass"] = "Function"


class NumberOfCacheLevels(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Number of Cache Levels")
        LVNode.addTerminal(self, "# of cache levels", varType="I32", isInput=False)
        self.attributes["type"] = "Number of Cache Levels"
        self.attributes["genclass"] = "Function"


class NumberToBooleanArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Number To Boolean Array")
        LVNode.addTerminal(self, "Boolean array", varType="Array", isInput=False)
        LVNode.addTerminal(self, "number", varType="U32")
        self.attributes["type"] = "Number To Boolean Array"
        self.attributes["genclass"] = "Function"


class NumberToDecimalString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Number To Decimal String")
        LVNode.addTerminal(self, "decimal integer string", varType="String", isInput=False)
        LVNode.addTerminal(self, "width (-)", varType="I16")
        LVNode.addTerminal(self, "number", varType="I32")
        self.attributes["type"] = "Number To Decimal String"
        self.attributes["genclass"] = "Function"


class NumberToEngineeringString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Number To Engineering String")
        LVNode.addTerminal(self, "Engineering string", varType="String", isInput=False)
        LVNode.addTerminal(self, "use system decimal point (T)", varType="Boolean")
        LVNode.addTerminal(self, "precision (6)", varType="I16")
        LVNode.addTerminal(self, "width (-)", varType="I16")
        LVNode.addTerminal(self, "number", varType="Double Float")
        self.attributes["type"] = "Number To Engineering String"
        self.attributes["genclass"] = "Function"


class NumberToExponentialString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Number To Exponential String")
        LVNode.addTerminal(self, "E-format string", varType="String", isInput=False)
        LVNode.addTerminal(self, "use system decimal point (T)", varType="Boolean")
        LVNode.addTerminal(self, "precision (6)", varType="I16")
        LVNode.addTerminal(self, "width (-)", varType="I16")
        LVNode.addTerminal(self, "number", varType="Double Float")
        self.attributes["type"] = "Number To Exponential String"
        self.attributes["genclass"] = "Function"


class NumberToFractionalString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Number To Fractional String")
        LVNode.addTerminal(self, "F-format string", varType="String", isInput=False)
        LVNode.addTerminal(self, "use system decimal point (T)", varType="Boolean")
        LVNode.addTerminal(self, "precision (6)", varType="I16")
        LVNode.addTerminal(self, "width (-)", varType="I16")
        LVNode.addTerminal(self, "number", varType="Double Float")
        self.attributes["type"] = "Number To Fractional String"
        self.attributes["genclass"] = "Function"


class NumberToHexadecimalString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Number To Hexadecimal String")
        LVNode.addTerminal(self, "hex integer string", varType="String", isInput=False)
        LVNode.addTerminal(self, "width (-)", varType="I16")
        LVNode.addTerminal(self, "number", varType="I32")
        self.attributes["type"] = "Number To Hexadecimal String"
        self.attributes["genclass"] = "Function"


class NumberToOctalString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Number To Octal String")
        LVNode.addTerminal(self, "octal integer string", varType="String", isInput=False)
        LVNode.addTerminal(self, "width (-)", varType="I16")
        LVNode.addTerminal(self, "number", varType="I32")
        self.attributes["type"] = "Number To Octal String"
        self.attributes["genclass"] = "Function"


class ObtainNotifier(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Obtain Notifier")
        LVNode.addTerminal(self, "name (unnamed)", varType="String")
        LVNode.addTerminal(self, "notification data type", varType="LV Variant")
        LVNode.addTerminal(self, "create if not found? (T)", varType="Boolean")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "notifier out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "created new?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Obtain Notifier"
        self.attributes["genclass"] = "Function"


class ObtainQueue(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Obtain Queue")
        LVNode.addTerminal(self, "name (unnamed)", varType="String")
        LVNode.addTerminal(self, "element data type", varType="LV Variant")
        LVNode.addTerminal(self, "create if not found? (T)", varType="Boolean")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "max queue size (-1, unlimited)", varType="I32")
        LVNode.addTerminal(self, "queue out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "created new?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Obtain Queue"
        self.attributes["genclass"] = "Function"


class OctalDigit(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Octal Digit?")
        LVNode.addTerminal(self, "octal?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "char", varType="String")
        self.attributes["type"] = "Octal Digit?"
        self.attributes["genclass"] = "Function"


class OctalStringToNumber(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Octal String To Number")
        LVNode.addTerminal(self, "number", varType="U32", isInput=False)
        LVNode.addTerminal(self, "offset past number", varType="I32", isInput=False)
        LVNode.addTerminal(self, "default (0uL)", varType="U32")
        LVNode.addTerminal(self, "offset", varType="I32")
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "Octal String To Number"
        self.attributes["genclass"] = "Function"


class OldVisaOpen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Old VISA Open")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "timeout (0)", varType="U32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "access mode", varType="U32")
        LVNode.addTerminal(self, "resource name ("")", varType="String")
        LVNode.addTerminal(self, "VISA resource name (for class)", varType="Refnum")
        self.attributes["type"] = "Old VISA Open"
        self.attributes["genclass"] = "Function"


class OneButtonDialog(LVNode):
    def __init__(self):
        LVNode.__init__(self, "One Button Dialog")
        LVNode.addTerminal(self, "true", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "button name (\"OK\")", varType="String")
        LVNode.addTerminal(self, "message", varType="String")
        self.attributes["type"] = "One Button Dialog"
        self.attributes["genclass"] = "Function"


class OpenApplicationReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open Application Reference")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "application reference", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "", varType="I32")
        LVNode.addTerminal(self, "port number or service name (3363)", varType="U16")
        LVNode.addTerminal(self, "machine name ("":  open local reference)", varType="String")
        self.attributes["type"] = "Open Application Reference"
        self.attributes["genclass"] = "Function"


class OpenDevice(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open Device")
        LVNode.addTerminal(self, "err", varType="I32", isInput=False)
        LVNode.addTerminal(self, "device refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "unit(0)", varType="I32")
        LVNode.addTerminal(self, "device name", varType="String")
        self.attributes["type"] = "Open Device"
        self.attributes["genclass"] = "Function"


class OpenDynamicBitfileReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open Dynamic Bitfile Reference")
        LVNode.addTerminal(self, "Device address", varType="String")
        LVNode.addTerminal(self, "Bitfile path", varType="Path")
        LVNode.addTerminal(self, "Run When Loaded", varType="Boolean")
        LVNode.addTerminal(self, "Error In", varType="Cluster")
        LVNode.addTerminal(self, "Type", varType="Refnum")
        LVNode.addTerminal(self, "Refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "Error Out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Open Dynamic Bitfile Reference"
        self.attributes["genclass"] = "Function"


class OpenFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open File")
        LVNode.addTerminal(self, "file path", varType="Path")
        LVNode.addTerminal(self, "open mode (0)", varType="Enum U16")
        LVNode.addTerminal(self, "deny mode (2)", varType="Enum U16")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "datalog type", varType="I32")
        LVNode.addTerminal(self, "refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Open File"
        self.attributes["genclass"] = "Function"


class OpenMatlabSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open MATLAB Session")
        LVNode.addTerminal(self, "release name", varType="String")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "session out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Open MATLAB Session"
        self.attributes["genclass"] = "Function"


class OpenPythonSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open Python Session")
        LVNode.addTerminal(self, "python version", varType="String")
        LVNode.addTerminal(self, "python path", varType="Path")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "session out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Open Python Session"
        self.attributes["genclass"] = "Function"


class OpenViObjectReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open VI Object Reference")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "object refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "vi object class", varType="Refnum")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "name/order", varType="String")
        LVNode.addTerminal(self, "owner refnum", varType="Refnum")
        self.attributes["type"] = "Open VI Object Reference"
        self.attributes["genclass"] = "Function"


class OpenViReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open VI Reference")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "vi reference", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "password ("")", varType="String")
        LVNode.addTerminal(self, "type specifier VI Refnum (for type only)", varType="Refnum")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "options", varType="I32")
        LVNode.addTerminal(self, "vi path", varType="Path")
        LVNode.addTerminal(self, "application reference (local)", varType="Refnum")
        self.attributes["type"] = "Open VI Reference"
        self.attributes["genclass"] = "Function"


class OpenCreateReplaceDatalog(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open/Create/Replace Datalog")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "cancelled", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "record type", varType="Cluster")
        LVNode.addTerminal(self, "prompt", varType="String")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "access (0:read/write)", varType="Enum U16")
        LVNode.addTerminal(self, "operation (0:open)", varType="Enum U16")
        LVNode.addTerminal(self, "datalog path (use dialog)", varType="Path")
        self.attributes["type"] = "Open/Create/Replace Datalog"
        self.attributes["genclass"] = "Function"


class OpenCreateReplaceFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open/Create/Replace File")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "cancelled", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "disable buffering (F)", varType="Boolean")
        LVNode.addTerminal(self, "prompt", varType="String")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "access (0:read/write)", varType="Enum U16")
        LVNode.addTerminal(self, "operation (0:open)", varType="Enum U16")
        LVNode.addTerminal(self, "file path (use dialog)", varType="Path")
        self.attributes["type"] = "Open/Create/Replace File"
        self.attributes["genclass"] = "Function"


class Or(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Or")
        LVNode.addTerminal(self, "x .or. y?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "y", varType="Boolean")
        LVNode.addTerminal(self, "x", varType="Boolean")
        self.attributes["type"] = "Or"
        self.attributes["genclass"] = "Function"


class OrArrayElements(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Or Array Elements")
        LVNode.addTerminal(self, "logical OR", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "Boolean array", varType="Array")
        self.attributes["type"] = "Or Array Elements"
        self.attributes["genclass"] = "Function"


class PackageMatrix(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Package Matrix")
        LVNode.addTerminal(self, "matrix", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "array", varType="Array")
        LVNode.addTerminal(self, "matrix", varType="Cluster")
        self.attributes["type"] = "Package Matrix"
        self.attributes["genclass"] = "Function"


class Passcontrol(LVNode):
    def __init__(self):
        LVNode.__init__(self, "PassControl")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "address", varType="I16")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "PassControl"
        self.attributes["genclass"] = "Function"


class PathToArrayOfStrings(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Path to Array of Strings")
        LVNode.addTerminal(self, "path", varType="Path")
        LVNode.addTerminal(self, "relative", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "array of strings", varType="Array", isInput=False)
        self.attributes["type"] = "Path to Array of Strings"
        self.attributes["genclass"] = "Function"


class PathToString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Path To String")
        LVNode.addTerminal(self, "string", varType="String", isInput=False)
        LVNode.addTerminal(self, "path", varType="Path")
        self.attributes["type"] = "Path To String"
        self.attributes["genclass"] = "Function"


class PathType(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Path Type")
        LVNode.addTerminal(self, "type", varType="I16", isInput=False)
        LVNode.addTerminal(self, "path", varType="Path")
        self.attributes["type"] = "Path Type"
        self.attributes["genclass"] = "Function"


class PickLine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Pick Line")
        LVNode.addTerminal(self, "output string", varType="String", isInput=False)
        LVNode.addTerminal(self, "line index", varType="I32")
        LVNode.addTerminal(self, "multi-line string", varType="String")
        LVNode.addTerminal(self, "string ("")", varType="String")
        self.attributes["type"] = "Pick Line"
        self.attributes["genclass"] = "Function"


class PolarToComplex(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Polar To Complex")
        LVNode.addTerminal(self, "r * e^(i*theta)", varType="Double Complex", isInput=False)
        LVNode.addTerminal(self, "theta", varType="Double Float")
        LVNode.addTerminal(self, "r", varType="Double Float")
        self.attributes["type"] = "Polar To Complex"
        self.attributes["genclass"] = "Function"


class PolarToReIm(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Polar To Re/Im")
        LVNode.addTerminal(self, "y", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "theta", varType="Double Float")
        LVNode.addTerminal(self, "r", varType="Double Float")
        self.attributes["type"] = "Polar To Re/Im"
        self.attributes["genclass"] = "Function"


class PowerOf10(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Power Of 10")
        LVNode.addTerminal(self, "10^x", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Power Of 10"
        self.attributes["genclass"] = "Function"


class PowerOf2(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Power Of 2")
        LVNode.addTerminal(self, "2^x", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Power Of 2"
        self.attributes["genclass"] = "Function"


class PowerOfX(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Power Of X")
        LVNode.addTerminal(self, "x^y", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        LVNode.addTerminal(self, "y", varType="Double Float")
        self.attributes["type"] = "Power Of X"
        self.attributes["genclass"] = "Function"


class Ppoll(LVNode):
    def __init__(self):
        LVNode.__init__(self, "PPoll")
        LVNode.addTerminal(self, "bus", varType="I32")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "parallel poll byte", varType="I16", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "PPoll"
        self.attributes["genclass"] = "Function"


class Ppollconfig(LVNode):
    def __init__(self):
        LVNode.__init__(self, "PPollConfig")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "sense", varType="Boolean")
        LVNode.addTerminal(self, "dataline", varType="I16")
        LVNode.addTerminal(self, "address", varType="I16")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "PPollConfig"
        self.attributes["genclass"] = "Function"


class Ppollunconfig(LVNode):
    def __init__(self):
        LVNode.__init__(self, "PPollUnconfig")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "address list", varType="Array")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "PPollUnconfig"
        self.attributes["genclass"] = "Function"


class PreallocatedReadFromBinaryFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Preallocated Read from Binary File")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "num elements read", varType="I32", isInput=False)
        LVNode.addTerminal(self, "data out", varType="Array", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "byte order (0:big-endian, network order)", varType="Enum U16")
        LVNode.addTerminal(self, "data in", varType="Array")
        LVNode.addTerminal(self, "refnum in", varType="Refnum")
        self.attributes["type"] = "Preallocated Read from Binary File"
        self.attributes["genclass"] = "Function"


class PreserveRunTimeClass(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Preserve Run-Time Class")
        LVNode.addTerminal(self, "object out", varType="LabVIEW Class Instance", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "target object", varType="LabVIEW Class Instance")
        LVNode.addTerminal(self, "object in", varType="LabVIEW Class Instance")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        self.attributes["type"] = "Preserve Run-Time Class"
        self.attributes["genclass"] = "Function"


class PreviewQueueElement(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Preview Queue Element")
        LVNode.addTerminal(self, "queue", varType="Refnum")
        LVNode.addTerminal(self, "timeout in ms (-1)", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "queue out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "element", varType="String", isInput=False)
        LVNode.addTerminal(self, "timed out?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Preview Queue Element"
        self.attributes["genclass"] = "Function"


class Printable(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Printable?")
        LVNode.addTerminal(self, "printable ASCII?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "char", varType="String")
        self.attributes["type"] = "Printable?"
        self.attributes["genclass"] = "Function"


class QuitLabview(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Quit LabVIEW")
        LVNode.addTerminal(self, "quit? (T)", varType="Boolean")
        self.attributes["type"] = "Quit LabVIEW"
        self.attributes["genclass"] = "Function"


class QuotientRemainder(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Quotient & Remainder")
        LVNode.addTerminal(self, "floor(x/y)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x-y*floor(x/y)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Quotient & Remainder"
        self.attributes["genclass"] = "Function"


class RandomNumber01(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Random Number (0-1)")
        LVNode.addTerminal(self, "number: 0 to 1", varType="Double Float", isInput=False)
        self.attributes["type"] = "Random Number (0-1)"
        self.attributes["genclass"] = "Function"


class Rcvrespmsg(LVNode):
    def __init__(self):
        LVNode.__init__(self, "RcvRespMsg")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "byte count", varType="I32", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "data string", varType="String", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "count", varType="I32")
        LVNode.addTerminal(self, "mode", varType="I16")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "RcvRespMsg"
        self.attributes["genclass"] = "Function"


class ReAcceptTls(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Re-accept TLS")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "client certificate chain", varType="Array", isInput=False)
        LVNode.addTerminal(self, "TLS connection out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "timeout ms", varType="I32")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "", varType="Array")
        LVNode.addTerminal(self, "CA certificates", varType="Refnum")
        LVNode.addTerminal(self, "TLS connection", varType="Refnum")
        self.attributes["type"] = "Re-accept TLS"
        self.attributes["genclass"] = "Function"


class ReImToComplex(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Re/Im To Complex")
        LVNode.addTerminal(self, "x + iy", varType="Double Complex", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Re/Im To Complex"
        self.attributes["genclass"] = "Function"


class ReImToPolar(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Re/Im To Polar")
        LVNode.addTerminal(self, "theta", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "r", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Re/Im To Polar"
        self.attributes["genclass"] = "Function"


class ReadDatalog(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Read Datalog")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "record(s)", varType="Void", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "count (1)", varType="I32")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Read Datalog"
        self.attributes["genclass"] = "Function"


class ReadDevice(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Read Device")
        LVNode.addTerminal(self, "new offset", varType="I32", isInput=False)
        LVNode.addTerminal(self, "string", varType="String", isInput=False)
        LVNode.addTerminal(self, "err", varType="I16", isInput=False)
        LVNode.addTerminal(self, "spc reset (F)", varType="Boolean")
        LVNode.addTerminal(self, "misc (-)", varType="Array")
        LVNode.addTerminal(self, "async (T)", varType="Boolean")
        LVNode.addTerminal(self, "pos offset (-)", varType="I32")
        LVNode.addTerminal(self, "pos mode (-)", varType="I16")
        LVNode.addTerminal(self, "count", varType="I32")
        LVNode.addTerminal(self, "device refnum", varType="Refnum")
        self.attributes["type"] = "Read Device"
        self.attributes["genclass"] = "Function"


class ReadFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Read File")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "offset", varType="I32", isInput=False)
        LVNode.addTerminal(self, "data", varType="String", isInput=False)
        LVNode.addTerminal(self, "dup refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "byte stream type", varType="I32")
        LVNode.addTerminal(self, "convert eol (F)", varType="Boolean")
        LVNode.addTerminal(self, "count", varType="I32")
        LVNode.addTerminal(self, "line mode (F)", varType="Boolean")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "pos offset (0)", varType="I32")
        LVNode.addTerminal(self, "pos mode (0:2)", varType="Enum U16")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Read File"
        self.attributes["genclass"] = "Function"


class ReadFromBinaryFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Read from Binary File")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "cancelled", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "data", varType="String", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "data type", varType="String")
        LVNode.addTerminal(self, "prompt (Open existing file)", varType="String")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "byte order (0:big-endian, network order)", varType="Enum U16")
        LVNode.addTerminal(self, "count", varType="I32")
        LVNode.addTerminal(self, "file (use dialog)", varType="Path")
        self.attributes["type"] = "Read from Binary File"
        self.attributes["genclass"] = "Function"


class ReadFromTextFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Read from Text File")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "cancelled", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "text", varType="String", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "prompt (Open existing file)", varType="String")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "count", varType="I32")
        LVNode.addTerminal(self, "file (use dialog)", varType="Path")
        self.attributes["type"] = "Read from Text File"
        self.attributes["genclass"] = "Function"


class ReadMapMaxMinKeys(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Read Map Max & Min Keys")
        LVNode.addTerminal(self, "minimum", varType="String", isInput=False)
        LVNode.addTerminal(self, "maximum", varType="String", isInput=False)
        LVNode.addTerminal(self, "map", varType="Map Collection")
        self.attributes["type"] = "Read Map Max & Min Keys"
        self.attributes["genclass"] = "Function"


class ReadSetMaxMin(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Read Set Max & Min")
        LVNode.addTerminal(self, "minimum", varType="String", isInput=False)
        LVNode.addTerminal(self, "maximum", varType="String", isInput=False)
        LVNode.addTerminal(self, "set", varType="Set Collection")
        self.attributes["type"] = "Read Set Max & Min"
        self.attributes["genclass"] = "Function"


class Readstatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "ReadStatus")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "serial poll response", varType="I16", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "address", varType="I16")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "ReadStatus"
        self.attributes["genclass"] = "Function"


class Receive(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Receive")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "byte count", varType="I32", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "data string", varType="String", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "count", varType="I32")
        LVNode.addTerminal(self, "mode", varType="I16")
        LVNode.addTerminal(self, "address", varType="I16")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "Receive"
        self.attributes["genclass"] = "Function"


class Receivesetup(LVNode):
    def __init__(self):
        LVNode.__init__(self, "ReceiveSetup")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "address", varType="I16")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "ReceiveSetup"
        self.attributes["genclass"] = "Function"


class Reciprocal(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Reciprocal")
        LVNode.addTerminal(self, "1/x", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Reciprocal"
        self.attributes["genclass"] = "Function"


class RefnumToPath(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Refnum to Path")
        LVNode.addTerminal(self, "path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Refnum to Path"
        self.attributes["genclass"] = "Function"


class RefnumToSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Refnum to Session")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "Session", varType="U64", isInput=False)
        LVNode.addTerminal(self, "error in(no error)", varType="Cluster")
        LVNode.addTerminal(self, "Refnum", varType="Refnum")
        self.attributes["type"] = "Refnum to Session"
        self.attributes["genclass"] = "Function"


class RegisterSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Register Session")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "duplicate refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "cleanup mode (default to class = 0)", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "session", varType="U64")
        LVNode.addTerminal(self, "resource name", varType="String")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Register Session"
        self.attributes["genclass"] = "Function"


class ReleaseNotifier(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Release Notifier")
        LVNode.addTerminal(self, "notifier", varType="Refnum")
        LVNode.addTerminal(self, "force destroy? (F)", varType="Boolean")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "notifier name", varType="String", isInput=False)
        LVNode.addTerminal(self, "last notification", varType="String", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Release Notifier"
        self.attributes["genclass"] = "Function"


class ReleaseQueue(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Release Queue")
        LVNode.addTerminal(self, "queue", varType="Refnum")
        LVNode.addTerminal(self, "force destroy? (F)", varType="Boolean")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "queue name", varType="String", isInput=False)
        LVNode.addTerminal(self, "remaining elements", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Release Queue"
        self.attributes["genclass"] = "Function"


class RemoveFixedPointOverflowStatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Remove Fixed-Point Overflow Status")
        LVNode.addTerminal(self, "overflow?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "FXP with overflow removed", varType="Fixed Point", isInput=False)
        LVNode.addTerminal(self, "FXP", varType="Fixed Point")
        self.attributes["type"] = "Remove Fixed-Point Overflow Status"
        self.attributes["genclass"] = "Function"


class RemoveFromMap(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Remove From Map")
        LVNode.addTerminal(self, "value", varType="I32", isInput=False)
        LVNode.addTerminal(self, "key not found?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "map out", varType="Map Collection", isInput=False)
        LVNode.addTerminal(self, "key", varType="String")
        LVNode.addTerminal(self, "map in", varType="Map Collection")
        self.attributes["type"] = "Remove From Map"
        self.attributes["genclass"] = "Function"


class RemoveFromSet(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Remove From Set")
        LVNode.addTerminal(self, "not included?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "set out", varType="Set Collection", isInput=False)
        LVNode.addTerminal(self, "element", varType="String")
        LVNode.addTerminal(self, "set in", varType="Set Collection")
        self.attributes["type"] = "Remove From Set"
        self.attributes["genclass"] = "Function"


class ReplaceSubstring(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Replace Substring")
        LVNode.addTerminal(self, "replaced substring", varType="String", isInput=False)
        LVNode.addTerminal(self, "result string", varType="String", isInput=False)
        LVNode.addTerminal(self, "length", varType="I32")
        LVNode.addTerminal(self, "offset", varType="I32")
        LVNode.addTerminal(self, "substring", varType="String")
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "Replace Substring"
        self.attributes["genclass"] = "Function"


class RequestDeallocation(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Request Deallocation")
        LVNode.addTerminal(self, "flag", varType="Boolean")
        self.attributes["type"] = "Request Deallocation"
        self.attributes["genclass"] = "Function"


class Resetsys(LVNode):
    def __init__(self):
        LVNode.__init__(self, "ResetSys")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "address list", varType="Array")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "ResetSys"
        self.attributes["genclass"] = "Function"


class ResizeMatrix(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Resize Matrix")
        LVNode.addTerminal(self, "resized matrix", varType="Array", isInput=False)
        LVNode.addTerminal(self, "number of columns", varType="I32")
        LVNode.addTerminal(self, "number of rows", varType="I32")
        LVNode.addTerminal(self, "matrix", varType="Array")
        self.attributes["type"] = "Resize Matrix"
        self.attributes["genclass"] = "Function"


class ResourceIndex(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Resource Index")
        LVNode.addTerminal(self, "Index", varType="I32", isInput=False)
        LVNode.addTerminal(self, "Resource", varType="String")
        self.attributes["type"] = "Resource Index"
        self.attributes["genclass"] = "Function"


class Reverse1dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Reverse 1D Array")
        LVNode.addTerminal(self, "reversed array", varType="Array", isInput=False)
        LVNode.addTerminal(self, "array", varType="Array")
        self.attributes["type"] = "Reverse 1D Array"
        self.attributes["genclass"] = "Function"


class ReverseString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Reverse String")
        LVNode.addTerminal(self, "reversed", varType="String", isInput=False)
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "Reverse String"
        self.attributes["genclass"] = "Function"


class Rotate(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Rotate")
        LVNode.addTerminal(self, "x rotated left by y", varType="U32", isInput=False)
        LVNode.addTerminal(self, "x", varType="U32")
        LVNode.addTerminal(self, "y", varType="I16")
        self.attributes["type"] = "Rotate"
        self.attributes["genclass"] = "Function"


class Rotate1dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Rotate 1D Array")
        LVNode.addTerminal(self, "array (last n elements first)", varType="Array", isInput=False)
        LVNode.addTerminal(self, "array", varType="Array")
        LVNode.addTerminal(self, "n", varType="I32")
        self.attributes["type"] = "Rotate 1D Array"
        self.attributes["genclass"] = "Function"


class RotateLeftWithCarry(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Rotate Left With Carry")
        LVNode.addTerminal(self, "value", varType="I32", isInput=False)
        LVNode.addTerminal(self, "msb carry out", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "value", varType="I32")
        LVNode.addTerminal(self, "carry", varType="Boolean")
        self.attributes["type"] = "Rotate Left With Carry"
        self.attributes["genclass"] = "Function"


class RotateRightWithCarry(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Rotate Right With Carry")
        LVNode.addTerminal(self, "value", varType="I32", isInput=False)
        LVNode.addTerminal(self, "lsb carry out", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "value", varType="I32")
        LVNode.addTerminal(self, "carry", varType="Boolean")
        self.attributes["type"] = "Rotate Right With Carry"
        self.attributes["genclass"] = "Function"


class RotateString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Rotate String")
        LVNode.addTerminal(self, "first char last", varType="String", isInput=False)
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "Rotate String"
        self.attributes["genclass"] = "Function"


class RoundToNearest(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Round To Nearest")
        LVNode.addTerminal(self, "nearest integer value", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "number", varType="Double Float")
        self.attributes["type"] = "Round To Nearest"
        self.attributes["genclass"] = "Function"


class RoundTowardInfinity(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Round Toward +Infinity")
        LVNode.addTerminal(self, "ceil(x): smallest int >= x", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Round Toward +Infinity"
        self.attributes["genclass"] = "Function"


class RoundTowardInfinity(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Round Toward -Infinity")
        LVNode.addTerminal(self, "floor(x): largest int <= x", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Round Toward -Infinity"
        self.attributes["genclass"] = "Function"


class RtFifoCreate(LVNode):
    def __init__(self):
        LVNode.__init__(self, "RT FIFO Create")
        LVNode.addTerminal(self, "name (unnamed)", varType="String")
        LVNode.addTerminal(self, "type", varType="LV Variant")
        LVNode.addTerminal(self, "create if not found? (T)", varType="Boolean")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "size (10)", varType="U32")
        LVNode.addTerminal(self, "datapoints in waveform (1)", varType="U32")
        LVNode.addTerminal(self, "elements in array (1)", varType="U32")
        LVNode.addTerminal(self, "r/w modes (polling,polling)", varType="Cluster")
        LVNode.addTerminal(self, "rt fifo", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "created new?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "RT FIFO Create"
        self.attributes["genclass"] = "Function"


class RtFifoDelete(LVNode):
    def __init__(self):
        LVNode.__init__(self, "RT FIFO Delete")
        LVNode.addTerminal(self, "rt fifo", varType="Refnum")
        LVNode.addTerminal(self, "force destroy? (F)", varType="Boolean")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "RT FIFO Delete"
        self.attributes["genclass"] = "Function"


class RtFifoRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "RT FIFO Read")
        LVNode.addTerminal(self, "rt fifo", varType="Refnum")
        LVNode.addTerminal(self, "element", varType="String")
        LVNode.addTerminal(self, "timeout in ms (0)", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "# elements", varType="U32", isInput=False)
        LVNode.addTerminal(self, "rt fifo out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "element out", varType="String", isInput=False)
        LVNode.addTerminal(self, "empty?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "RT FIFO Read"
        self.attributes["genclass"] = "Function"


class RtFifoWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "RT FIFO Write")
        LVNode.addTerminal(self, "rt fifo", varType="Refnum")
        LVNode.addTerminal(self, "element", varType="String")
        LVNode.addTerminal(self, "timeout in ms (0)", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "overwrite on timeout (T)", varType="Boolean")
        LVNode.addTerminal(self, "# elements", varType="U32", isInput=False)
        LVNode.addTerminal(self, "rt fifo out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "timed out?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "RT FIFO Write"
        self.attributes["genclass"] = "Function"


class ScaleByPowerOf2(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Scale By Power Of 2")
        LVNode.addTerminal(self, "x*2^n", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        LVNode.addTerminal(self, "n", varType="I16")
        self.attributes["type"] = "Scale By Power Of 2"
        self.attributes["genclass"] = "Function"


class ScanStringForTokens(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Scan String For Tokens")
        LVNode.addTerminal(self, "token index", varType="I32", isInput=False)
        LVNode.addTerminal(self, "token string", varType="String", isInput=False)
        LVNode.addTerminal(self, "offset past token", varType="I32", isInput=False)
        LVNode.addTerminal(self, "string out", varType="String", isInput=False)
        LVNode.addTerminal(self, "use cached delim/oper data? (F)", varType="Boolean")
        LVNode.addTerminal(self, "allow empty tokens? (F)", varType="Boolean")
        LVNode.addTerminal(self, "delimiters (\s,\t,\r,\n)", varType="Array")
        LVNode.addTerminal(self, "operators (none)", varType="Array")
        LVNode.addTerminal(self, "offset", varType="I32")
        LVNode.addTerminal(self, "input string", varType="String")
        self.attributes["type"] = "Scan String For Tokens"
        self.attributes["genclass"] = "Function"


class ScanValue(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Scan Value")
        LVNode.addTerminal(self, "value", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "output string", varType="String", isInput=False)
        LVNode.addTerminal(self, "default (0 dbl)", varType="Double Float")
        LVNode.addTerminal(self, "format string", varType="String")
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "Scan Value"
        self.attributes["genclass"] = "Function"


class Search1dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Search 1D Array")
        LVNode.addTerminal(self, "index of element", varType="I32", isInput=False)
        LVNode.addTerminal(self, "start index (0)", varType="I32")
        LVNode.addTerminal(self, "element", varType="Double Float")
        LVNode.addTerminal(self, "1D array", varType="Array")
        self.attributes["type"] = "Search 1D Array"
        self.attributes["genclass"] = "Function"


class SearchAndReplaceString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Search and Replace String")
        LVNode.addTerminal(self, "input string", varType="String")
        LVNode.addTerminal(self, "replace all?", varType="Boolean")
        LVNode.addTerminal(self, "case sensitive?", varType="Boolean")
        LVNode.addTerminal(self, "multiline?", varType="Boolean")
        LVNode.addTerminal(self, "result string", varType="String", isInput=False)
        LVNode.addTerminal(self, "search string", varType="String")
        LVNode.addTerminal(self, "replace string", varType="String")
        LVNode.addTerminal(self, "number of replacements", varType="I32", isInput=False)
        LVNode.addTerminal(self, "offset", varType="I32")
        LVNode.addTerminal(self, "offset past replacement", varType="I32", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Search and Replace String"
        self.attributes["genclass"] = "Function"


class SearchVariableContainer(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Search Variable Container")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "refnum array out", varType="Array", isInput=False)
        LVNode.addTerminal(self, "container refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "access type", varType="Cluster")
        LVNode.addTerminal(self, "class", varType="Refnum")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "data type", varType="LV Variant")
        LVNode.addTerminal(self, "regular expression", varType="String")
        LVNode.addTerminal(self, "container refnum in", varType="Refnum")
        self.attributes["type"] = "Search Variable Container"
        self.attributes["genclass"] = "Function"


class SearchSplitString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Search/Split String")
        LVNode.addTerminal(self, "offset of match", varType="I32", isInput=False)
        LVNode.addTerminal(self, "match + rest of string", varType="String", isInput=False)
        LVNode.addTerminal(self, "substring before match", varType="String", isInput=False)
        LVNode.addTerminal(self, "offset (0)", varType="I32")
        LVNode.addTerminal(self, "search string/char (-)", varType="String")
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "Search/Split String"
        self.attributes["genclass"] = "Function"


class Secant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Secant")
        LVNode.addTerminal(self, "1/cos(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Secant"
        self.attributes["genclass"] = "Function"


class SecondsToDateTime(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Seconds To Date/Time")
        LVNode.addTerminal(self, "date time rec", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "to UTC (F)", varType="Boolean")
        LVNode.addTerminal(self, "time stamp (now)", varType="Timestamp")
        self.attributes["type"] = "Seconds To Date/Time"
        self.attributes["genclass"] = "Function"


class Seek(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Seek")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "offset", varType="I32", isInput=False)
        LVNode.addTerminal(self, "dup refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "pos offset (0)", varType="I32")
        LVNode.addTerminal(self, "pos mode (0:2)", varType="Enum U16")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Seek"
        self.attributes["genclass"] = "Function"


class Select(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Select")
        LVNode.addTerminal(self, "s? t:f", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "f", varType="Double Float")
        LVNode.addTerminal(self, "s", varType="Boolean")
        LVNode.addTerminal(self, "t", varType="Double Float")
        self.attributes["type"] = "Select"
        self.attributes["genclass"] = "Function"


class Send(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Send")
        LVNode.addTerminal(self, "bus", varType="I32")
        LVNode.addTerminal(self, "address", varType="I16")
        LVNode.addTerminal(self, "mode", varType="I16")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "data string", varType="String")
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "byte count", varType="I32", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Send"
        self.attributes["genclass"] = "Function"


class SendNotification(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Send Notification")
        LVNode.addTerminal(self, "notifier", varType="Refnum")
        LVNode.addTerminal(self, "notification", varType="String")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "notifier out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Send Notification"
        self.attributes["genclass"] = "Function"


class Sendcmds(LVNode):
    def __init__(self):
        LVNode.__init__(self, "SendCmds")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "byte count", varType="I32", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "command string", varType="String")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "SendCmds"
        self.attributes["genclass"] = "Function"


class Senddatabytes(LVNode):
    def __init__(self):
        LVNode.__init__(self, "SendDataBytes")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "byte count", varType="I32", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "data string", varType="String")
        LVNode.addTerminal(self, "mode", varType="I16")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "SendDataBytes"
        self.attributes["genclass"] = "Function"


class Sendifc(LVNode):
    def __init__(self):
        LVNode.__init__(self, "SendIFC")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "SendIFC"
        self.attributes["genclass"] = "Function"


class Sendlist(LVNode):
    def __init__(self):
        LVNode.__init__(self, "SendList")
        LVNode.addTerminal(self, "bus", varType="I32")
        LVNode.addTerminal(self, "address list", varType="Array")
        LVNode.addTerminal(self, "mode", varType="I16")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "data string", varType="String")
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "byte count", varType="I32", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "SendList"
        self.attributes["genclass"] = "Function"


class Sendllo(LVNode):
    def __init__(self):
        LVNode.__init__(self, "SendLLO")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "SendLLO"
        self.attributes["genclass"] = "Function"


class Sendsetup(LVNode):
    def __init__(self):
        LVNode.__init__(self, "SendSetup")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "address list", varType="Array")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "SendSetup"
        self.attributes["genclass"] = "Function"


class SessionToRefnum(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Session to Refnum")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "Refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in(no error)", varType="Cluster")
        LVNode.addTerminal(self, "Session", varType="U64")
        LVNode.addTerminal(self, "Class Type", varType="Refnum")
        self.attributes["type"] = "Session to Refnum"
        self.attributes["genclass"] = "Function"


class SetControlValuesByIndex(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Control Values by Index")
        LVNode.addTerminal(self, "VI Refnum", varType="Refnum")
        LVNode.addTerminal(self, "control indexes", varType="Array")
        LVNode.addTerminal(self, "data values", varType="Array")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Set Control Values by Index"
        self.attributes["genclass"] = "Function"


class SetDatalogPosition(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Datalog Position")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "from (0:start)", varType="Enum U16")
        LVNode.addTerminal(self, "offset (in records) (0)", varType="I64")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Set Datalog Position"
        self.attributes["genclass"] = "Function"


class SetFilePosition(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set File Position")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "from (0:start)", varType="Enum U16")
        LVNode.addTerminal(self, "offset (in bytes) (0)", varType="I64")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Set File Position"
        self.attributes["genclass"] = "Function"


class SetFileSize(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set File Size")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "size (in bytes)", varType="I64")
        LVNode.addTerminal(self, "file", varType="Path")
        self.attributes["type"] = "Set File Size"
        self.attributes["genclass"] = "Function"


class SetMenuItemInfo(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Menu Item Info")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "menu reference out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "short cut", varType="Cluster")
        LVNode.addTerminal(self, "checked", varType="Boolean")
        LVNode.addTerminal(self, "item tag", varType="String")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "enabled", varType="Boolean")
        LVNode.addTerminal(self, "item name", varType="String")
        LVNode.addTerminal(self, "menu reference", varType="Refnum")
        self.attributes["type"] = "Set Menu Item Info"
        self.attributes["genclass"] = "Function"


class SetNumberOfRecords(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Number of Records")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "# of records", varType="I64")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Set Number of Records"
        self.attributes["genclass"] = "Function"


class SetOccurrence(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Occurrence")
        LVNode.addTerminal(self, "occurrence", varType="Refnum")
        self.attributes["type"] = "Set Occurrence"
        self.attributes["genclass"] = "Function"


class SetPermissions(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Permissions")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "path out", varType="Path", isInput=False)
        LVNode.addTerminal(self, "permissions", varType="I16")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "new group", varType="String")
        LVNode.addTerminal(self, "new owner", varType="String")
        LVNode.addTerminal(self, "path", varType="Path")
        self.attributes["type"] = "Set Permissions"
        self.attributes["genclass"] = "Function"


class SetTypeAndCreator(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Type and Creator")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "path out", varType="Path", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "creator (no change)", varType="String")
        LVNode.addTerminal(self, "type (no change)", varType="String")
        LVNode.addTerminal(self, "path", varType="Path")
        self.attributes["type"] = "Set Type and Creator"
        self.attributes["genclass"] = "Function"


class SetVariantAttribute(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Variant Attribute")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "replaced", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "Variant out", varType="LV Variant", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "value", varType="Cluster")
        LVNode.addTerminal(self, "name", varType="String")
        LVNode.addTerminal(self, "Variant", varType="LV Variant")
        self.attributes["type"] = "Set Variant Attribute"
        self.attributes["genclass"] = "Function"


class SetWaveformAttribute(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Waveform Attribute")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "replaced", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "waveform out", varType="Waveform", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "value", varType="Cluster")
        LVNode.addTerminal(self, "name", varType="String")
        LVNode.addTerminal(self, "waveform", varType="Waveform")
        self.attributes["type"] = "Set Waveform Attribute"
        self.attributes["genclass"] = "Function"


class Setrwls(LVNode):
    def __init__(self):
        LVNode.__init__(self, "SetRWLS")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "address list", varType="Array")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "SetRWLS"
        self.attributes["genclass"] = "Function"


class Settimeout(LVNode):
    def __init__(self):
        LVNode.__init__(self, "SetTimeOut")
        LVNode.addTerminal(self, "previous timeout", varType="I32", isInput=False)
        LVNode.addTerminal(self, "new timeout (10000)", varType="I32")
        self.attributes["type"] = "SetTimeOut"
        self.attributes["genclass"] = "Function"


class SharedVariableToString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Shared Variable to String")
        LVNode.addTerminal(self, "string", varType="String", isInput=False)
        LVNode.addTerminal(self, "Shared Variable", varType="Refnum")
        self.attributes["type"] = "Shared Variable to String"
        self.attributes["genclass"] = "Function"


class Sign(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Sign")
        LVNode.addTerminal(self, "-1, 0, 1", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "number", varType="Double Float")
        self.attributes["type"] = "Sign"
        self.attributes["genclass"] = "Function"


class Sinc(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Sinc")
        LVNode.addTerminal(self, "sin(x)/x", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Sinc"
        self.attributes["genclass"] = "Function"


class Sine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Sine")
        LVNode.addTerminal(self, "sin(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Sine"
        self.attributes["genclass"] = "Function"


class SineCosine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Sine & Cosine")
        LVNode.addTerminal(self, "x", varType="Double Float")
        LVNode.addTerminal(self, "sin(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "cos(x)", varType="Double Float", isInput=False)
        self.attributes["type"] = "Sine & Cosine"
        self.attributes["genclass"] = "Function"


class SizeHandle(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Size Handle")
        LVNode.addTerminal(self, "handle", varType="Void", isInput=False)
        LVNode.addTerminal(self, "error", varType="I32", isInput=False)
        LVNode.addTerminal(self, "handle (-)", varType="Void")
        LVNode.addTerminal(self, "size", varType="I32")
        self.attributes["type"] = "Size Handle"
        self.attributes["genclass"] = "Function"


class Sort1dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Sort 1D Array")
        LVNode.addTerminal(self, "sorted array", varType="Array", isInput=False)
        LVNode.addTerminal(self, "array", varType="Array")
        self.attributes["type"] = "Sort 1D Array"
        self.attributes["genclass"] = "Function"


class SortArrayOfString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Sort Array of String")
        LVNode.addTerminal(self, "sorted array", varType="Array", isInput=False)
        LVNode.addTerminal(self, "array", varType="Array")
        self.attributes["type"] = "Sort Array of String"
        self.attributes["genclass"] = "Function"


class Split1dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Split 1D Array")
        LVNode.addTerminal(self, "second subarray", varType="Array", isInput=False)
        LVNode.addTerminal(self, "first subarray", varType="Array", isInput=False)
        LVNode.addTerminal(self, "index", varType="I32")
        LVNode.addTerminal(self, "array", varType="Array")
        self.attributes["type"] = "Split 1D Array"
        self.attributes["genclass"] = "Function"


class SplitNumber(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Split Number")
        LVNode.addTerminal(self, "x", varType="U32")
        LVNode.addTerminal(self, "hi(x)", varType="U16", isInput=False)
        LVNode.addTerminal(self, "lo(x)", varType="U16", isInput=False)
        self.attributes["type"] = "Split Number"
        self.attributes["genclass"] = "Function"


class SpreadsheetStringToArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Spreadsheet String To Array")
        LVNode.addTerminal(self, "array", varType="Array", isInput=False)
        LVNode.addTerminal(self, "delimiter (Tab)", varType="String")
        LVNode.addTerminal(self, "array type (2D Dbl)", varType="Array")
        LVNode.addTerminal(self, "spreadsheet string", varType="String")
        LVNode.addTerminal(self, "format string", varType="String")
        self.attributes["type"] = "Spreadsheet String To Array"
        self.attributes["genclass"] = "Function"


class Square(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Square")
        LVNode.addTerminal(self, "x^2", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Square"
        self.attributes["genclass"] = "Function"


class SquareRoot(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Square Root")
        LVNode.addTerminal(self, "sqrt(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Square Root"
        self.attributes["genclass"] = "Function"


class StartTls(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Start TLS")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "server certificate chain", varType="Array", isInput=False)
        LVNode.addTerminal(self, "TLS connection", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "server certificate validation", varType="Enum U32")
        LVNode.addTerminal(self, "timeout ms", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "server hostname", varType="String")
        LVNode.addTerminal(self, "immutable TLS configuration", varType="Refnum")
        LVNode.addTerminal(self, "TCP connection", varType="Refnum")
        self.attributes["type"] = "Start TLS"
        self.attributes["genclass"] = "Function"


class Stop(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Stop")
        LVNode.addTerminal(self, "stop? (T)", varType="Boolean")
        self.attributes["type"] = "Stop"
        self.attributes["genclass"] = "Function"


class StringLength(LVNode):
    def __init__(self):
        LVNode.__init__(self, "String Length")
        LVNode.addTerminal(self, "length", varType="I32", isInput=False)
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "String Length"
        self.attributes["genclass"] = "Function"


class StringSubset(LVNode):
    def __init__(self):
        LVNode.__init__(self, "String Subset")
        LVNode.addTerminal(self, "substring", varType="String", isInput=False)
        LVNode.addTerminal(self, "length (rest)", varType="I32")
        LVNode.addTerminal(self, "offset (0)", varType="I32")
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "String Subset"
        self.attributes["genclass"] = "Function"


class StringToByteArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "String To Byte Array")
        LVNode.addTerminal(self, "unsigned byte array", varType="Array", isInput=False)
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "String To Byte Array"
        self.attributes["genclass"] = "Function"


class StringToIp(LVNode):
    def __init__(self):
        LVNode.__init__(self, "String To IP")
        LVNode.addTerminal(self, "net address", varType="U32", isInput=False)
        LVNode.addTerminal(self, "name", varType="String")
        self.attributes["type"] = "String To IP"
        self.attributes["genclass"] = "Function"


class StringToPath(LVNode):
    def __init__(self):
        LVNode.__init__(self, "String To Path")
        LVNode.addTerminal(self, "path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "String To Path"
        self.attributes["genclass"] = "Function"


class StringToSharedVariable(LVNode):
    def __init__(self):
        LVNode.__init__(self, "String to Shared Variable")
        LVNode.addTerminal(self, "string", varType="String")
        LVNode.addTerminal(self, "valid Shared Variable?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "Shared Variable", varType="Refnum", isInput=False)
        self.attributes["type"] = "String to Shared Variable"
        self.attributes["genclass"] = "Function"


class StripPath(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Strip Path")
        LVNode.addTerminal(self, "path", varType="Path")
        LVNode.addTerminal(self, "stripped path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "name", varType="String", isInput=False)
        self.attributes["type"] = "Strip Path"
        self.attributes["genclass"] = "Function"


class Subtract(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Subtract")
        LVNode.addTerminal(self, "x-y", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Subtract"
        self.attributes["genclass"] = "Function"


class SubtractWithErrorTerminals(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Subtract (with error terminals)")
        LVNode.addTerminal(self, "x-y", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "y", varType="Double Float")
        LVNode.addTerminal(self, "x", varType="Double Float")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        self.attributes["type"] = "Subtract (with error terminals)"
        self.attributes["genclass"] = "Function"


class SwapBytes(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Swap Bytes")
        LVNode.addTerminal(self, "byte swapped", varType="U16", isInput=False)
        LVNode.addTerminal(self, "anything", varType="U16")
        self.attributes["type"] = "Swap Bytes"
        self.attributes["genclass"] = "Function"


class SwapValues(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Swap Values")
        LVNode.addTerminal(self, " y'", varType="I32", isInput=False)
        LVNode.addTerminal(self, " x'  ", varType="I32", isInput=False)
        LVNode.addTerminal(self, "y", varType="I32")
        LVNode.addTerminal(self, "?(T)", varType="Boolean")
        LVNode.addTerminal(self, "x", varType="I32")
        self.attributes["type"] = "Swap Values"
        self.attributes["genclass"] = "Function"


class SwapVectorElement(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Swap Vector Element")
        LVNode.addTerminal(self, "swapped element value", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "returned index", varType="I32", isInput=False)
        LVNode.addTerminal(self, "changed vector", varType="Array", isInput=False)
        LVNode.addTerminal(self, "element value", varType="Double Float")
        LVNode.addTerminal(self, "index", varType="I32")
        LVNode.addTerminal(self, "vector", varType="Array")
        self.attributes["type"] = "Swap Vector Element"
        self.attributes["genclass"] = "Function"


class SwapWords(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Swap Words")
        LVNode.addTerminal(self, "word swapped", varType="U32", isInput=False)
        LVNode.addTerminal(self, "anything", varType="U32")
        self.attributes["type"] = "Swap Words"
        self.attributes["genclass"] = "Function"


class Tangent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Tangent")
        LVNode.addTerminal(self, "tan(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        self.attributes["type"] = "Tangent"
        self.attributes["genclass"] = "Function"


class TcpCloseConnection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Close Connection")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "connection ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "abort (F)", varType="Boolean")
        LVNode.addTerminal(self, "connection ID", varType="Refnum")
        self.attributes["type"] = "TCP Close Connection"
        self.attributes["genclass"] = "Function"


class TcpCreateListener(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Create Listener")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "port", varType="U16", isInput=False)
        LVNode.addTerminal(self, "listener ID", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "net address", varType="U32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (25000)", varType="I32")
        LVNode.addTerminal(self, "port", varType="U16")
        LVNode.addTerminal(self, "service name", varType="String")
        self.attributes["type"] = "TCP Create Listener"
        self.attributes["genclass"] = "Function"


class TcpFlattenedRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Flattened Read")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "data out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "connection ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "type", varType="Cluster")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (25000)", varType="I32")
        LVNode.addTerminal(self, "connection ID", varType="Refnum")
        self.attributes["type"] = "TCP Flattened Read"
        self.attributes["genclass"] = "Function"


class TcpFlattenedWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Flattened Write")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "connection ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (25000)", varType="I32")
        LVNode.addTerminal(self, "data in", varType="Cluster")
        LVNode.addTerminal(self, "connection ID", varType="Refnum")
        self.attributes["type"] = "TCP Flattened Write"
        self.attributes["genclass"] = "Function"


class TcpFlexRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Flex Read")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "coerced?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "data out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "connection ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "type", varType="Cluster")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (25000)", varType="I32")
        LVNode.addTerminal(self, "connection ID", varType="Refnum")
        self.attributes["type"] = "TCP Flex Read"
        self.attributes["genclass"] = "Function"


class TcpFlexWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Flex Write")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "connection ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (25000)", varType="I32")
        LVNode.addTerminal(self, "data in", varType="Cluster")
        LVNode.addTerminal(self, "connection ID", varType="Refnum")
        self.attributes["type"] = "TCP Flex Write"
        self.attributes["genclass"] = "Function"


class TcpOpenConnection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Open Connection")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "connection ID", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "local port", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (60000)", varType="I32")
        LVNode.addTerminal(self, "remote port or service name", varType="U16")
        LVNode.addTerminal(self, "address", varType="String")
        self.attributes["type"] = "TCP Open Connection"
        self.attributes["genclass"] = "Function"


class TcpRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Read")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "data out", varType="String", isInput=False)
        LVNode.addTerminal(self, "connection ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "mode (standard)", varType="Enum U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (25000)", varType="I32")
        LVNode.addTerminal(self, "bytes to read", varType="I32")
        LVNode.addTerminal(self, "connection ID", varType="Refnum")
        self.attributes["type"] = "TCP Read"
        self.attributes["genclass"] = "Function"


class TcpWaitOnListener(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Wait On Listener")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "remote port", varType="U16", isInput=False)
        LVNode.addTerminal(self, "remote address", varType="String", isInput=False)
        LVNode.addTerminal(self, "listener ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "connection ID", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (wait forever: -1)", varType="I32")
        LVNode.addTerminal(self, "resolve remote address (T)", varType="Boolean")
        LVNode.addTerminal(self, "listener ID in", varType="Refnum")
        self.attributes["type"] = "TCP Wait On Listener"
        self.attributes["genclass"] = "Function"


class TcpWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Write")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "bytes written", varType="I32", isInput=False)
        LVNode.addTerminal(self, "connection ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (25000)", varType="I32")
        LVNode.addTerminal(self, "data in", varType="String")
        LVNode.addTerminal(self, "connection ID", varType="Refnum")
        self.attributes["type"] = "TCP Write"
        self.attributes["genclass"] = "Function"


class TdmsAdvancedAsynchronousReadDataRef(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Advanced Asynchronous Read (Data Ref)")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "tdms file out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "read process finished?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "auto delete reference? (T)", varType="Boolean")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "data reference", varType="Refnum")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        self.attributes["type"] = "TDMS Advanced Asynchronous Read (Data Ref)"
        self.attributes["genclass"] = "Function"


class TdmsAdvancedAsynchronousWriteDataRef(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Advanced Asynchronous Write (Data Ref)")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "tdms file out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "auto delete reference? (T)", varType="Boolean")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "data reference", varType="Refnum")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        self.attributes["type"] = "TDMS Advanced Asynchronous Write (Data Ref)"
        self.attributes["genclass"] = "Function"


class TdmsClose(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Close")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "file path out", varType="Path", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        self.attributes["type"] = "TDMS Close"
        self.attributes["genclass"] = "Function"


class TdmsConfigureAsynchronousReadsDataRef(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Configure Asynchronous Reads (Data Ref)")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "tdms file out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "timeout (5 s)", varType="Double Float")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "total size (in bytes) (-1)", varType="I64")
        LVNode.addTerminal(self, "max asynchronous reads (4)", varType="U32")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        self.attributes["type"] = "TDMS Configure Asynchronous Reads (Data Ref)"
        self.attributes["genclass"] = "Function"


class TdmsConfigureAsynchronousWritesDataRef(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Configure Asynchronous Writes (Data Ref)")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "tdms file out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "timeout (5 s)", varType="Double Float")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "max asynchronous writes (4)", varType="U32")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        self.attributes["type"] = "TDMS Configure Asynchronous Writes (Data Ref)"
        self.attributes["genclass"] = "Function"


class TdmsDefragment(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Defragment")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "object id", varType="U64", isInput=False)
        LVNode.addTerminal(self, "tdms file id", varType="U64", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "channel name", varType="String")
        LVNode.addTerminal(self, "group name", varType="String")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        self.attributes["type"] = "TDMS Defragment"
        self.attributes["genclass"] = "Function"


class TdmsDeleteData(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Delete Data")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "file path out", varType="Path", isInput=False)
        LVNode.addTerminal(self, "count (-1: all)", varType="I64")
        LVNode.addTerminal(self, "keep empty group/channel? (T)", varType="Boolean")
        LVNode.addTerminal(self, "from (0: start)", varType="Enum U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "channel name(s) in", varType="Array")
        LVNode.addTerminal(self, "group name in", varType="String")
        LVNode.addTerminal(self, "file path", varType="Path")
        self.attributes["type"] = "TDMS Delete Data"
        self.attributes["genclass"] = "Function"


class TdmsFlush(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Flush")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "tdms file out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        self.attributes["type"] = "TDMS Flush"
        self.attributes["genclass"] = "Function"


class TdmsGetAsynchronousReadStatusDataRef(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Get Asynchronous Read Status (Data Ref)")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "number of pending reads", varType="U32", isInput=False)
        LVNode.addTerminal(self, "tdms file out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        self.attributes["type"] = "TDMS Get Asynchronous Read Status (Data Ref)"
        self.attributes["genclass"] = "Function"


class TdmsGetAsynchronousWriteStatusDataRef(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Get Asynchronous Write Status (Data Ref)")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "number of pending writes", varType="U32", isInput=False)
        LVNode.addTerminal(self, "tdms file out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        self.attributes["type"] = "TDMS Get Asynchronous Write Status (Data Ref)"
        self.attributes["genclass"] = "Function"


class TdmsGetProperties(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Get Properties")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "channel name out", varType="String", isInput=False)
        LVNode.addTerminal(self, "group name out", varType="String", isInput=False)
        LVNode.addTerminal(self, "tdms file out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "property values", varType="Array", isInput=False)
        LVNode.addTerminal(self, "data type", varType="String")
        LVNode.addTerminal(self, "property names", varType="Array", isInput=False)
        LVNode.addTerminal(self, "property name", varType="String")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "channel name", varType="String")
        LVNode.addTerminal(self, "group name", varType="String")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        self.attributes["type"] = "TDMS Get Properties"
        self.attributes["genclass"] = "Function"


class TdmsInMemoryClose(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS In Memory Close")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "overwrite (F)", varType="Boolean")
        LVNode.addTerminal(self, "file path", varType="Path")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        self.attributes["type"] = "TDMS In Memory Close"
        self.attributes["genclass"] = "Function"


class TdmsInMemoryOpen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS In Memory Open")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "tdms file out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "byte array or file path", varType="Array")
        self.attributes["type"] = "TDMS In Memory Open"
        self.attributes["genclass"] = "Function"


class TdmsInMemoryReadBytes(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS In Memory Read Bytes")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "data", varType="Array", isInput=False)
        LVNode.addTerminal(self, "tdms file out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "byte count (-1: all)", varType="I64")
        LVNode.addTerminal(self, "offset (0)", varType="I64")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        self.attributes["type"] = "TDMS In Memory Read Bytes"
        self.attributes["genclass"] = "Function"


class TdmsListContents(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS List Contents")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "group/channel names", varType="Array", isInput=False)
        LVNode.addTerminal(self, "group names", varType="Array", isInput=False)
        LVNode.addTerminal(self, "tdms file out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "group name", varType="String")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        self.attributes["type"] = "TDMS List Contents"
        self.attributes["genclass"] = "Function"


class TdmsOpen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Open")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "tdms file out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "create index file? (T)", varType="Boolean")
        LVNode.addTerminal(self, "disable buffering (T)", varType="Boolean")
        LVNode.addTerminal(self, "file format version (2.0)", varType="Enum U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "byte order (2:little-endian)", varType="Enum U16")
        LVNode.addTerminal(self, "operation (0:open)", varType="Enum U16")
        LVNode.addTerminal(self, "file path", varType="Path")
        self.attributes["type"] = "TDMS Open"
        self.attributes["genclass"] = "Function"


class TdmsRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Read")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        LVNode.addTerminal(self, "offset (0)", varType="I64")
        LVNode.addTerminal(self, "count (-1: all)", varType="I64")
        LVNode.addTerminal(self, "tdms file out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "group name in", varType="String")
        LVNode.addTerminal(self, "group name out", varType="String", isInput=False)
        LVNode.addTerminal(self, "channel name(s) in", varType="Array")
        LVNode.addTerminal(self, "channel name(s) out", varType="Array", isInput=False)
        LVNode.addTerminal(self, "data", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "data type", varType="Array")
        LVNode.addTerminal(self, "return channels in file order? (F)", varType="Boolean")
        LVNode.addTerminal(self, "end of file?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "TDMS Read"
        self.attributes["genclass"] = "Function"


class TdmsRefnumToFileId(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Refnum To File ID")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "object id", varType="U64", isInput=False)
        LVNode.addTerminal(self, "tdms file id", varType="U64", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "channel name", varType="String")
        LVNode.addTerminal(self, "group name", varType="String")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        self.attributes["type"] = "TDMS Refnum To File ID"
        self.attributes["genclass"] = "Function"


class TdmsSetProperties(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Set Properties")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "channel name out", varType="String", isInput=False)
        LVNode.addTerminal(self, "group name out", varType="String", isInput=False)
        LVNode.addTerminal(self, "tdms file out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "property values", varType="Array")
        LVNode.addTerminal(self, "property names", varType="Array")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "channel name", varType="String")
        LVNode.addTerminal(self, "group name", varType="String")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        self.attributes["type"] = "TDMS Set Properties"
        self.attributes["genclass"] = "Function"


class TdmsWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Write")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        LVNode.addTerminal(self, "data layout (0:decimated)", varType="Enum U16")
        LVNode.addTerminal(self, "tdms file out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "group name in (Untitled)", varType="String")
        LVNode.addTerminal(self, "group name out", varType="String", isInput=False)
        LVNode.addTerminal(self, "channel name(s) in (Untitled)", varType="Array")
        LVNode.addTerminal(self, "channel name(s) out", varType="Array", isInput=False)
        LVNode.addTerminal(self, "data", varType="Array")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "TDMS Write"
        self.attributes["genclass"] = "Function"


class TdmsWriteIp(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Write IP")
        LVNode.addTerminal(self, "tdms file", varType="Refnum")
        LVNode.addTerminal(self, "tdms file out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "group name in", varType="String")
        LVNode.addTerminal(self, "group name out", varType="String", isInput=False)
        LVNode.addTerminal(self, "channel names in", varType="Array")
        LVNode.addTerminal(self, "channel names out", varType="Array", isInput=False)
        LVNode.addTerminal(self, "data", varType="Array")
        LVNode.addTerminal(self, "data out", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "TDMS Write IP"
        self.attributes["genclass"] = "Function"


class TemporaryDirectory(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Temporary Directory")
        LVNode.addTerminal(self, "path", varType="Path", isInput=False)
        self.attributes["type"] = "Temporary Directory"
        self.attributes["genclass"] = "Function"


class Testsrq(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TestSRQ")
        LVNode.addTerminal(self, "bus", varType="I32")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "SRQ", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "TestSRQ"
        self.attributes["genclass"] = "Function"


class Testsys(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TestSys")
        LVNode.addTerminal(self, "bus", varType="I32")
        LVNode.addTerminal(self, "address list", varType="Array")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "result list", varType="Array", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "failed devices", varType="I32", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "TestSys"
        self.attributes["genclass"] = "Function"


class TextToUtf8(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Text to UTF-8")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "utf-8 text", varType="String", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "encoding", varType="I32")
        LVNode.addTerminal(self, "text", varType="String")
        self.attributes["type"] = "Text to UTF-8"
        self.attributes["genclass"] = "Function"


class Threshold1dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Threshold 1D Array")
        LVNode.addTerminal(self, "fractional index or x", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "start index (0)", varType="I32")
        LVNode.addTerminal(self, "threshold y", varType="Double Float")
        LVNode.addTerminal(self, "array of numbers or points", varType="Array")
        self.attributes["type"] = "Threshold 1D Array"
        self.attributes["genclass"] = "Function"


class TickCountMs(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Tick Count (ms)")
        LVNode.addTerminal(self, "millisecond timer value", varType="U32", isInput=False)
        self.attributes["type"] = "Tick Count (ms)"
        self.attributes["genclass"] = "Function"


class TlsConnection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TLS Connection?")
        LVNode.addTerminal(self, "TLS?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "TCP connection", varType="Refnum")
        self.attributes["type"] = "TLS Connection?"
        self.attributes["genclass"] = "Function"


class ToByteInteger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Byte Integer")
        LVNode.addTerminal(self, "8bit integer", varType="I8", isInput=False)
        LVNode.addTerminal(self, "number", varType="I8")
        self.attributes["type"] = "To Byte Integer"
        self.attributes["genclass"] = "Function"


class ToDoublePrecisionComplex(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Double Precision Complex")
        LVNode.addTerminal(self, "double precision complex", varType="Double Complex", isInput=False)
        LVNode.addTerminal(self, "number", varType="Double Complex")
        self.attributes["type"] = "To Double Precision Complex"
        self.attributes["genclass"] = "Function"


class ToDoublePrecisionFloat(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Double Precision Float")
        LVNode.addTerminal(self, "double precision float", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "number", varType="Double Float")
        self.attributes["type"] = "To Double Precision Float"
        self.attributes["genclass"] = "Function"


class ToExtendedPrecisionComplex(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Extended Precision Complex")
        LVNode.addTerminal(self, "extended precision complex", varType="Extended Complex", isInput=False)
        LVNode.addTerminal(self, "number", varType="Double Complex")
        self.attributes["type"] = "To Extended Precision Complex"
        self.attributes["genclass"] = "Function"


class ToExtendedPrecisionFloat(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Extended Precision Float")
        LVNode.addTerminal(self, "extended precision float", varType="Extended Float", isInput=False)
        LVNode.addTerminal(self, "number", varType="Double Float")
        self.attributes["type"] = "To Extended Precision Float"
        self.attributes["genclass"] = "Function"


class ToFixedPoint(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Fixed-Point")
        LVNode.addTerminal(self, "number", varType="Fixed Point")
        LVNode.addTerminal(self, "fixed-point type", varType="Fixed Point")
        LVNode.addTerminal(self, "fixed-point", varType="Fixed Point", isInput=False)
        self.attributes["type"] = "To Fixed-Point"
        self.attributes["genclass"] = "Function"


class ToLongInteger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Long Integer")
        LVNode.addTerminal(self, "32bit integer", varType="I32", isInput=False)
        LVNode.addTerminal(self, "number", varType="I32")
        self.attributes["type"] = "To Long Integer"
        self.attributes["genclass"] = "Function"


class ToLowerCase(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Lower Case")
        LVNode.addTerminal(self, "all lower case string", varType="String", isInput=False)
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "To Lower Case"
        self.attributes["genclass"] = "Function"


class ToMoreGenericClass(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To More Generic Class")
        LVNode.addTerminal(self, "reference", varType="Refnum")
        LVNode.addTerminal(self, "target class", varType="Refnum")
        LVNode.addTerminal(self, "generic class reference", varType="Refnum", isInput=False)
        self.attributes["type"] = "To More Generic Class"
        self.attributes["genclass"] = "Function"


class ToMoreSpecificClass(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To More Specific Class")
        LVNode.addTerminal(self, "specific class reference", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "target class", varType="Refnum")
        LVNode.addTerminal(self, "reference", varType="Refnum")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        self.attributes["type"] = "To More Specific Class"
        self.attributes["genclass"] = "Function"


class ToOleVariant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To OLE Variant")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "x", varType="LV Variant")
        LVNode.addTerminal(self, "vt VARTYPE", varType="I32")
        LVNode.addTerminal(self, "OLE Variant", varType="LV Variant", isInput=False)
        self.attributes["type"] = "To OLE Variant"
        self.attributes["genclass"] = "Function"


class ToProbeString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Probe String")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "probe string", varType="String", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "maximum string length", varType="U32")
        LVNode.addTerminal(self, "data value", varType="LV Variant")
        self.attributes["type"] = "To Probe String"
        self.attributes["genclass"] = "Function"


class ToQuadInteger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Quad Integer")
        LVNode.addTerminal(self, "64bit integer", varType="I64", isInput=False)
        LVNode.addTerminal(self, "number", varType="I64")
        self.attributes["type"] = "To Quad Integer"
        self.attributes["genclass"] = "Function"


class ToSinglePrecisionComplex(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Single Precision Complex")
        LVNode.addTerminal(self, "single precision complex", varType="Single Complex", isInput=False)
        LVNode.addTerminal(self, "number", varType="Single Complex")
        self.attributes["type"] = "To Single Precision Complex"
        self.attributes["genclass"] = "Function"


class ToSinglePrecisionFloat(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Single Precision Float")
        LVNode.addTerminal(self, "single precision float", varType="Single Float", isInput=False)
        LVNode.addTerminal(self, "number", varType="Single Float")
        self.attributes["type"] = "To Single Precision Float"
        self.attributes["genclass"] = "Function"


class ToTimeStamp(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Time Stamp")
        LVNode.addTerminal(self, "Time Stamp", varType="Timestamp", isInput=False)
        LVNode.addTerminal(self, "number", varType="Double Float")
        self.attributes["type"] = "To Time Stamp"
        self.attributes["genclass"] = "Function"


class ToUnsignedByteInteger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Unsigned Byte Integer")
        LVNode.addTerminal(self, "unsigned 8bit integer", varType="U8", isInput=False)
        LVNode.addTerminal(self, "number", varType="U8")
        self.attributes["type"] = "To Unsigned Byte Integer"
        self.attributes["genclass"] = "Function"


class ToUnsignedLongInteger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Unsigned Long Integer")
        LVNode.addTerminal(self, "unsigned 32bit integer", varType="U32", isInput=False)
        LVNode.addTerminal(self, "number", varType="U32")
        self.attributes["type"] = "To Unsigned Long Integer"
        self.attributes["genclass"] = "Function"


class ToUnsignedQuadInteger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Unsigned Quad Integer")
        LVNode.addTerminal(self, "unsigned 64bit integer", varType="U64", isInput=False)
        LVNode.addTerminal(self, "number", varType="U64")
        self.attributes["type"] = "To Unsigned Quad Integer"
        self.attributes["genclass"] = "Function"


class ToUnsignedWordInteger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Unsigned Word Integer")
        LVNode.addTerminal(self, "unsigned 16bit integer", varType="U16", isInput=False)
        LVNode.addTerminal(self, "number", varType="U16")
        self.attributes["type"] = "To Unsigned Word Integer"
        self.attributes["genclass"] = "Function"


class ToUpperCase(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Upper Case")
        LVNode.addTerminal(self, "all upper case string", varType="String", isInput=False)
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "To Upper Case"
        self.attributes["genclass"] = "Function"


class ToVariant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Variant")
        LVNode.addTerminal(self, "Variant", varType="LV Variant", isInput=False)
        LVNode.addTerminal(self, "anything", varType="Cluster")
        self.attributes["type"] = "To Variant"
        self.attributes["genclass"] = "Function"


class ToWordInteger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Word Integer")
        LVNode.addTerminal(self, "16bit integer", varType="I16", isInput=False)
        LVNode.addTerminal(self, "number", varType="I16")
        self.attributes["type"] = "To Word Integer"
        self.attributes["genclass"] = "Function"


class Transpose1dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Transpose 1D Array")
        LVNode.addTerminal(self, "transposed array", varType="Array", isInput=False)
        LVNode.addTerminal(self, "1D array", varType="Array")
        self.attributes["type"] = "Transpose 1D Array"
        self.attributes["genclass"] = "Function"


class Transpose2dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Transpose 2D Array")
        LVNode.addTerminal(self, "transposed array", varType="Array", isInput=False)
        LVNode.addTerminal(self, "2D array", varType="Array")
        self.attributes["type"] = "Transpose 2D Array"
        self.attributes["genclass"] = "Function"


class TransposeMatrix(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Transpose Matrix")
        LVNode.addTerminal(self, "transposed matrix", varType="Array", isInput=False)
        LVNode.addTerminal(self, "matrix", varType="Array")
        self.attributes["type"] = "Transpose Matrix"
        self.attributes["genclass"] = "Function"


class Trigger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Trigger")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "address", varType="I16")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "Trigger"
        self.attributes["genclass"] = "Function"


class Triggerlist(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TriggerList")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "address list", varType="Array")
        LVNode.addTerminal(self, "bus", varType="I32")
        self.attributes["type"] = "TriggerList"
        self.attributes["genclass"] = "Function"


class TwoButtonDialog(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Two Button Dialog")
        LVNode.addTerminal(self, "T button?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "F button name (\"Cancel\")", varType="String")
        LVNode.addTerminal(self, "T button name (\"OK\")", varType="String")
        LVNode.addTerminal(self, "message", varType="String")
        self.attributes["type"] = "Two Button Dialog"
        self.attributes["genclass"] = "Function"


class TypeAndCreator(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Type and Creator")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "creator", varType="String", isInput=False)
        LVNode.addTerminal(self, "type", varType="String", isInput=False)
        LVNode.addTerminal(self, "dup path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "new creator", varType="String")
        LVNode.addTerminal(self, "new type", varType="String")
        LVNode.addTerminal(self, "path", varType="Path")
        self.attributes["type"] = "Type and Creator"
        self.attributes["genclass"] = "Function"


class TypeCast(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Type Cast")
        LVNode.addTerminal(self, "x", varType="Extended Float")
        LVNode.addTerminal(self, "type", varType="String")
        LVNode.addTerminal(self, "*(type *) &x", varType="String", isInput=False)
        self.attributes["type"] = "Type Cast"
        self.attributes["genclass"] = "Function"


class TypeError(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Type Error")
        LVNode.addTerminal(self, "bool const", varType="Boolean")
        self.attributes["type"] = "Type Error"
        self.attributes["genclass"] = "Function"


class TypeMustBeArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Type Must Be Array")
        LVNode.addTerminal(self, "any", varType="LV Variant")
        self.attributes["type"] = "Type Must Be Array"
        self.attributes["genclass"] = "Function"


class TypeMustBeCluster(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Type Must Be Cluster")
        LVNode.addTerminal(self, "any", varType="LV Variant")
        self.attributes["type"] = "Type Must Be Cluster"
        self.attributes["genclass"] = "Function"


class TypeOf(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Type Of")
        LVNode.addTerminal(self, "type", varType="LV Variant", isInput=False)
        LVNode.addTerminal(self, "any", varType="LV Variant")
        self.attributes["type"] = "Type Of"
        self.attributes["genclass"] = "Function"


class UdpClose(LVNode):
    def __init__(self):
        LVNode.__init__(self, "UDP Close")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "connection ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "connection ID", varType="Refnum")
        self.attributes["type"] = "UDP Close"
        self.attributes["genclass"] = "Function"


class UdpMulticastOpen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "UDP Multicast Open")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "port", varType="U16", isInput=False)
        LVNode.addTerminal(self, "connection ID", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "net address", varType="U32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "time-to-live", varType="U16")
        LVNode.addTerminal(self, "multicast addr", varType="U32")
        LVNode.addTerminal(self, "port", varType="U16")
        self.attributes["type"] = "UDP Multicast Open"
        self.attributes["genclass"] = "Function"


class UdpOpen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "UDP Open")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "service name", varType="U16", isInput=False)
        LVNode.addTerminal(self, "port", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "", varType="U32")
        LVNode.addTerminal(self, "net address", varType="Cluster")
        LVNode.addTerminal(self, "error in (no error)", varType="I32")
        LVNode.addTerminal(self, "", varType="String")
        LVNode.addTerminal(self, "", varType="U16")
        self.attributes["type"] = "UDP Open"
        self.attributes["genclass"] = "Function"


class UdpRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "UDP Read")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "data out", varType="String", isInput=False)
        LVNode.addTerminal(self, "connection ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "port", varType="U16", isInput=False)
        LVNode.addTerminal(self, "address", varType="U32", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (25000)", varType="I32")
        LVNode.addTerminal(self, "max size (548)", varType="I32")
        LVNode.addTerminal(self, "connection ID", varType="Refnum")
        self.attributes["type"] = "UDP Read"
        self.attributes["genclass"] = "Function"


class UdpWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "UDP Write")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "connection ID out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "port or service name", varType="U16")
        LVNode.addTerminal(self, "address", varType="U32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (25000)", varType="I32")
        LVNode.addTerminal(self, "data in", varType="String")
        LVNode.addTerminal(self, "connection ID", varType="Refnum")
        self.attributes["type"] = "UDP Write"
        self.attributes["genclass"] = "Function"


class UnbitpackFromArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Unbitpack from Array")
        LVNode.addTerminal(self, "data", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "type", varType="Cluster")
        LVNode.addTerminal(self, "bparray", varType="Array")
        self.attributes["type"] = "Unbitpack from Array"
        self.attributes["genclass"] = "Function"


class UnflattenFromJson(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Unflatten From JSON")
        LVNode.addTerminal(self, "JSON string", varType="String")
        LVNode.addTerminal(self, "type and defaults", varType="Cluster")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "path", varType="Array")
        LVNode.addTerminal(self, "default null elements? (F)", varType="Boolean")
        LVNode.addTerminal(self, "enable LabVIEW extensions? (T)", varType="Boolean")
        LVNode.addTerminal(self, "strict validation? (F)", varType="Boolean")
        LVNode.addTerminal(self, "value", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Unflatten From JSON"
        self.attributes["genclass"] = "Function"


class UnflattenFromString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Unflatten From String")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "value", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "rest of the binary string", varType="String", isInput=False)
        LVNode.addTerminal(self, "type", varType="Cluster")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "byte order (0:big-endian, network order)", varType="Enum U16")
        LVNode.addTerminal(self, "data includes array or string size? (T)", varType="Boolean")
        LVNode.addTerminal(self, "binary string", varType="String")
        self.attributes["type"] = "Unflatten From String"
        self.attributes["genclass"] = "Function"


class UnflattenFromXml(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Unflatten From XML")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "value", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "type", varType="Cluster")
        LVNode.addTerminal(self, "xml string", varType="String")
        self.attributes["type"] = "Unflatten From XML"
        self.attributes["genclass"] = "Function"


class UnleakVariantValueReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Unleak Variant Value Reference")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "variant value reference out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "variant value reference in", varType="Refnum")
        self.attributes["type"] = "Unleak Variant Value Reference"
        self.attributes["genclass"] = "Function"


class UnpackageMatrix(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Unpackage Matrix")
        LVNode.addTerminal(self, "matrix", varType="Cluster")
        LVNode.addTerminal(self, "matrix", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "array", varType="Array", isInput=False)
        self.attributes["type"] = "Unpackage Matrix"
        self.attributes["genclass"] = "Function"


class UnregisterForEvents(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Unregister For Events")
        LVNode.addTerminal(self, "event registration refnum", varType="Refnum")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Unregister For Events"
        self.attributes["genclass"] = "Function"


class UnregisterSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Unregister Session")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Unregister Session"
        self.attributes["genclass"] = "Function"


class Utf8ToText(LVNode):
    def __init__(self):
        LVNode.__init__(self, "UTF-8 to Text")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "text", varType="String", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "encoding", varType="I32")
        LVNode.addTerminal(self, "utf-8 text", varType="String")
        self.attributes["type"] = "UTF-8 to Text"
        self.attributes["genclass"] = "Function"


class VariantToData(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Variant To Data")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "Variant", varType="LV Variant")
        LVNode.addTerminal(self, "type", varType="LV Variant")
        LVNode.addTerminal(self, "data", varType="LV Variant", isInput=False)
        self.attributes["type"] = "Variant To Data"
        self.attributes["genclass"] = "Function"


class VariantToFlattenedString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Variant To Flattened String")
        LVNode.addTerminal(self, "Variant", varType="LV Variant")
        LVNode.addTerminal(self, "type string", varType="Array", isInput=False)
        LVNode.addTerminal(self, "data string", varType="String", isInput=False)
        self.attributes["type"] = "Variant To Flattened String"
        self.attributes["genclass"] = "Function"


class ViLibrary(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VI Library")
        LVNode.addTerminal(self, "path", varType="Path", isInput=False)
        self.attributes["type"] = "VI Library"
        self.attributes["genclass"] = "Function"


class VisaAssertInterruptSignal(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Assert Interrupt Signal")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "status ID", varType="U32")
        LVNode.addTerminal(self, "mode", varType="I16")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Assert Interrupt Signal"
        self.attributes["genclass"] = "Function"


class VisaAssertTrigger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Assert Trigger")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "protocol (default:  0)", varType="U16")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Assert Trigger"
        self.attributes["genclass"] = "Function"


class VisaAssertUtilitySignal(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Assert Utility Signal")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "bus signal", varType="U16")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Assert Utility Signal"
        self.attributes["genclass"] = "Function"


class VisaClear(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Clear")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Clear"
        self.attributes["genclass"] = "Function"


class VisaClose(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Close")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Close"
        self.attributes["genclass"] = "Function"


class VisaDisableEvent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Disable Event")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "mechanism (1:  VI_QUEUE)", varType="U16")
        LVNode.addTerminal(self, "event type (all enabled)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Disable Event"
        self.attributes["genclass"] = "Function"


class VisaDiscardEvents(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Discard Events")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "mechanism  (1:  VI_QUEUE)", varType="U16")
        LVNode.addTerminal(self, "event type (all enabled)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Discard Events"
        self.attributes["genclass"] = "Function"


class VisaEnableEvent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Enable Event")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "mechanism (1:  VI_QUEUE)", varType="U16")
        LVNode.addTerminal(self, "event type", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Enable Event"
        self.attributes["genclass"] = "Function"


class VisaFindResource(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Find Resource")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "return count", varType="U32", isInput=False)
        LVNode.addTerminal(self, "find list", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "search mode (0)", varType="U32")
        LVNode.addTerminal(self, "expression ("")", varType="String")
        self.attributes["type"] = "VISA Find Resource"
        self.attributes["genclass"] = "Function"


class VisaFlushIOBuffer(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Flush I/O Buffer")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "mask (16)", varType="U16")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Flush I/O Buffer"
        self.attributes["genclass"] = "Function"


class VisaGpibCommand(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA GPIB Command")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "return count", varType="U32", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "command", varType="String")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA GPIB Command"
        self.attributes["genclass"] = "Function"


class VisaGpibControlAtn(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA GPIB Control ATN")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "mode", varType="U16")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA GPIB Control ATN"
        self.attributes["genclass"] = "Function"


class VisaGpibControlRen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA GPIB Control REN")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "mode", varType="U16")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA GPIB Control REN"
        self.attributes["genclass"] = "Function"


class VisaGpibPassControl(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA GPIB Pass Control")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "secondary address (none)", varType="U16")
        LVNode.addTerminal(self, "primary address", varType="U16")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA GPIB Pass Control"
        self.attributes["genclass"] = "Function"


class VisaGpibSendIfc(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA GPIB Send IFC")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA GPIB Send IFC"
        self.attributes["genclass"] = "Function"


class VisaIn16(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA In 16")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "value", varType="U16", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA In 16"
        self.attributes["genclass"] = "Function"


class VisaIn32(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA In 32")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "value", varType="U32", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA In 32"
        self.attributes["genclass"] = "Function"


class VisaIn64(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA In 64")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "value", varType="U64", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA In 64"
        self.attributes["genclass"] = "Function"


class VisaIn8(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA In 8")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "value", varType="U8", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA In 8"
        self.attributes["genclass"] = "Function"


class VisaLock(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Lock")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "access key", varType="String", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "lock type (exclusive:  1)", varType="U32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "requested key", varType="String")
        LVNode.addTerminal(self, "timeout (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Lock"
        self.attributes["genclass"] = "Function"


class VisaMapAddress(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Map Address")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "access (False)", varType="Boolean")
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "map size (0)", varType="U32")
        LVNode.addTerminal(self, "map base (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Map Address"
        self.attributes["genclass"] = "Function"


class VisaMapTrigger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Map Trigger")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "mode", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "trigger destination", varType="I16")
        LVNode.addTerminal(self, "trigger source", varType="I16")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Map Trigger"
        self.attributes["genclass"] = "Function"


class VisaMemoryAllocation(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Memory Allocation")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "offset", varType="U32", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "size", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Memory Allocation"
        self.attributes["genclass"] = "Function"


class VisaMemoryAllocationEx(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Memory Allocation Ex")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "offset", varType="U64", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "size", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Memory Allocation Ex"
        self.attributes["genclass"] = "Function"


class VisaMemoryFree(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Memory Free")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "offset", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Memory Free"
        self.attributes["genclass"] = "Function"


class VisaMove(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        LVNode.addTerminal(self, "source space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "source width (8)", varType="U16")
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "source offset (0)", varType="U32")
        LVNode.addTerminal(self, "length", varType="U32")
        LVNode.addTerminal(self, "dest offset (0)", varType="U32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "dest space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "dest width (same as source)", varType="U16")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "VISA Move"
        self.attributes["genclass"] = "Function"


class VisaMoveIn16(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move In 16")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "data", varType="Array", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "count", varType="U32")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Move In 16"
        self.attributes["genclass"] = "Function"


class VisaMoveIn32(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move In 32")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "data", varType="Array", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "count", varType="U32")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Move In 32"
        self.attributes["genclass"] = "Function"


class VisaMoveIn64(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move In 64")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "data", varType="Array", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "count", varType="U32")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Move In 64"
        self.attributes["genclass"] = "Function"


class VisaMoveIn8(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move In 8")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "data", varType="Array", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "count", varType="U32")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Move In 8"
        self.attributes["genclass"] = "Function"


class VisaMoveOut16(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move Out 16")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "data", varType="Array")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Move Out 16"
        self.attributes["genclass"] = "Function"


class VisaMoveOut32(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move Out 32")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "data", varType="Array")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Move Out 32"
        self.attributes["genclass"] = "Function"


class VisaMoveOut64(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move Out 64")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "data", varType="Array")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Move Out 64"
        self.attributes["genclass"] = "Function"


class VisaMoveOut8(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move Out 8")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "data", varType="Array")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Move Out 8"
        self.attributes["genclass"] = "Function"


class VisaOpen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Open")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "timeout (0)", varType="U32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "access mode", varType="U32")
        LVNode.addTerminal(self, "duplicate session (F)", varType="Boolean")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Open"
        self.attributes["genclass"] = "Function"


class VisaOut16(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Out 16")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "value (0)", varType="U16")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Out 16"
        self.attributes["genclass"] = "Function"


class VisaOut32(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Out 32")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "value (0)", varType="U32")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Out 32"
        self.attributes["genclass"] = "Function"


class VisaOut64(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Out 64")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "value (0)", varType="U64")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Out 64"
        self.attributes["genclass"] = "Function"


class VisaOut8(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Out 8")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "value (0)", varType="U8")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Out 8"
        self.attributes["genclass"] = "Function"


class VisaPeek16(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Peek 16")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "value", varType="U16", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Peek 16"
        self.attributes["genclass"] = "Function"


class VisaPeek32(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Peek 32")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "value", varType="U32", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Peek 32"
        self.attributes["genclass"] = "Function"


class VisaPeek64(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Peek 64")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "value", varType="U64", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Peek 64"
        self.attributes["genclass"] = "Function"


class VisaPeek8(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Peek 8")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "value", varType="U8", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Peek 8"
        self.attributes["genclass"] = "Function"


class VisaPoke16(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Poke 16")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "value (0)", varType="U16")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Poke 16"
        self.attributes["genclass"] = "Function"


class VisaPoke32(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Poke 32")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "value (0)", varType="U32")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Poke 32"
        self.attributes["genclass"] = "Function"


class VisaPoke64(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Poke 64")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "value (0)", varType="U64")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Poke 64"
        self.attributes["genclass"] = "Function"


class VisaPoke8(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Poke 8")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "value (0)", varType="U8")
        LVNode.addTerminal(self, "offset (0)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Poke 8"
        self.attributes["genclass"] = "Function"


class VisaRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Read")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "return count", varType="U32", isInput=False)
        LVNode.addTerminal(self, "read buffer", varType="String", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "byte count", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Read"
        self.attributes["genclass"] = "Function"


class VisaReadStb(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Read STB")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status byte", varType="U16", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Read STB"
        self.attributes["genclass"] = "Function"


class VisaReadToFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Read To File")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "return count", varType="U32", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "byte count", varType="U32")
        LVNode.addTerminal(self, "filename", varType="Path")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Read To File"
        self.attributes["genclass"] = "Function"


class VisaRefnumToSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Refnum to Session")
        LVNode.addTerminal(self, "session", varType="U32", isInput=False)
        LVNode.addTerminal(self, "Visa Refnum", varType="Refnum")
        self.attributes["type"] = "VISA Refnum to Session"
        self.attributes["genclass"] = "Function"


class VisaSetIOBufferSize(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Set I/O Buffer Size")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "size (4096)", varType="U32")
        LVNode.addTerminal(self, "mask (16)", varType="U16")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Set I/O Buffer Size"
        self.attributes["genclass"] = "Function"


class VisaStatusDescription(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Status Description")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "status description", varType="String", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Status Description"
        self.attributes["genclass"] = "Function"


class VisaUnlock(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Unlock")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Unlock"
        self.attributes["genclass"] = "Function"


class VisaUnmapAddress(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Unmap Address")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Unmap Address"
        self.attributes["genclass"] = "Function"


class VisaUnmapTrigger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Unmap Trigger")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "trigger destination (all)", varType="I16")
        LVNode.addTerminal(self, "trigger source", varType="I16")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Unmap Trigger"
        self.attributes["genclass"] = "Function"


class VisaUsbControlIn(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA USB Control In")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        LVNode.addTerminal(self, "value (0)", varType="U16")
        LVNode.addTerminal(self, "index (0)", varType="U16")
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "request type", varType="I16")
        LVNode.addTerminal(self, "read buffer", varType="Array", isInput=False)
        LVNode.addTerminal(self, "request", varType="I16")
        LVNode.addTerminal(self, "length (0)", varType="U16")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "VISA USB Control In"
        self.attributes["genclass"] = "Function"


class VisaUsbControlOut(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA USB Control Out")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        LVNode.addTerminal(self, "value (0)", varType="U16")
        LVNode.addTerminal(self, "index (0)", varType="U16")
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "request type", varType="I16")
        LVNode.addTerminal(self, "request", varType="I16")
        LVNode.addTerminal(self, "length (0)", varType="Array")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "VISA USB Control Out"
        self.attributes["genclass"] = "Function"


class VisaVxiCmdOrQuery(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA VXI Cmd or Query")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "response", varType="U32", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "command", varType="U32")
        LVNode.addTerminal(self, "mode (x200: 16-bit cmd)", varType="U16")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA VXI Cmd or Query"
        self.attributes["genclass"] = "Function"


class VisaWaitOnEvent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Wait on Event")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "event  resource name", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "event type", varType="U32", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "timeout (0)", varType="U32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "event  resource name (for class)", varType="Refnum")
        LVNode.addTerminal(self, "event type (all enabled)", varType="U32")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Wait on Event"
        self.attributes["genclass"] = "Function"


class VisaWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Write")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "return count", varType="U32", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "write buffer", varType="String")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Write"
        self.attributes["genclass"] = "Function"


class VisaWriteFromFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Write From File")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "return count", varType="U32", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "count (entire file)", varType="U32")
        LVNode.addTerminal(self, "filename", varType="Path")
        LVNode.addTerminal(self, "VISA resource name", varType="Refnum")
        self.attributes["type"] = "VISA Write From File"
        self.attributes["genclass"] = "Function"


class VolumeInfo(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Volume Info")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "free", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "used", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "size", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "volume path", varType="Path", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "path", varType="Path")
        self.attributes["type"] = "Volume Info"
        self.attributes["genclass"] = "Function"


class WaitMs(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait (ms)")
        LVNode.addTerminal(self, "millisecond timer value", varType="U32", isInput=False)
        LVNode.addTerminal(self, "milliseconds to wait", varType="U32")
        self.attributes["type"] = "Wait (ms)"
        self.attributes["genclass"] = "Function"


class WaitForActivity(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait For Activity")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "connection IDs active", varType="Array", isInput=False)
        LVNode.addTerminal(self, "listener IDs active", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "timeout", varType="I32")
        LVNode.addTerminal(self, "connection IDs", varType="Array")
        LVNode.addTerminal(self, "listener IDs", varType="Array")
        self.attributes["type"] = "Wait For Activity"
        self.attributes["genclass"] = "Function"


class WaitForFrontPanelActivity(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait For Front Panel Activity")
        LVNode.addTerminal(self, "millisecond timer value", varType="U32", isInput=False)
        LVNode.addTerminal(self, "timeout ms (-1 never timeout)", varType="I32")
        LVNode.addTerminal(self, "front panel (this VI's panel)", varType="Refnum")
        LVNode.addTerminal(self, "do not wait! (False)", varType="Boolean")
        self.attributes["type"] = "Wait For Front Panel Activity"
        self.attributes["genclass"] = "Function"


class WaitForGpibRqs(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait for GPIB RQS")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "poll response byte", varType="I16", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "timeout ms (488.2 global)", varType="I32")
        LVNode.addTerminal(self, "address string", varType="String")
        self.attributes["type"] = "Wait for GPIB RQS"
        self.attributes["genclass"] = "Function"


class WaitOnNotification(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait on Notification")
        LVNode.addTerminal(self, "notifier", varType="Refnum")
        LVNode.addTerminal(self, "ignore previous (F)", varType="Boolean")
        LVNode.addTerminal(self, "timeout in ms (-1)", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "notifier out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "notification", varType="String", isInput=False)
        LVNode.addTerminal(self, "timed out?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Wait on Notification"
        self.attributes["genclass"] = "Function"


class WaitOnNotificationFromMultiple(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait on Notification from Multiple")
        LVNode.addTerminal(self, "notifiers", varType="Array")
        LVNode.addTerminal(self, "ignore previous (F)", varType="Boolean")
        LVNode.addTerminal(self, "timeout in ms (-1)", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "notifier out", varType="Array", isInput=False)
        LVNode.addTerminal(self, "notifiers out", varType="Array", isInput=False)
        LVNode.addTerminal(self, "timed out?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Wait on Notification from Multiple"
        self.attributes["genclass"] = "Function"


class WaitOnNotificationFromMultipleWithNotifierHistory(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait on Notification from Multiple with Notifier History")
        LVNode.addTerminal(self, "notifiers", varType="Array")
        LVNode.addTerminal(self, "ignore previous (F)", varType="Boolean")
        LVNode.addTerminal(self, "timeout in ms (-1)", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "notifier out", varType="Array", isInput=False)
        LVNode.addTerminal(self, "notifiers out", varType="Array", isInput=False)
        LVNode.addTerminal(self, "timed out?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Wait on Notification from Multiple with Notifier History"
        self.attributes["genclass"] = "Function"


class WaitOnNotificationWithNotifierHistory(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait on Notification with Notifier History")
        LVNode.addTerminal(self, "notifier", varType="Refnum")
        LVNode.addTerminal(self, "ignore previous (F)", varType="Boolean")
        LVNode.addTerminal(self, "timeout in ms (-1)", varType="I32")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "notifier out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "notification", varType="String", isInput=False)
        LVNode.addTerminal(self, "timed out?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Wait on Notification with Notifier History"
        self.attributes["genclass"] = "Function"


class WaitOnOccurrence(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait on Occurrence")
        LVNode.addTerminal(self, "timed out", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "ignore previous (T)", varType="Boolean")
        LVNode.addTerminal(self, "occurrence", varType="Refnum")
        LVNode.addTerminal(self, "ms timeout (-1)", varType="I32")
        self.attributes["type"] = "Wait on Occurrence"
        self.attributes["genclass"] = "Function"


class WaitUntilNextMsMultiple(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait Until Next ms Multiple")
        LVNode.addTerminal(self, "millisecond timer value", varType="U32", isInput=False)
        LVNode.addTerminal(self, "millisecond multiple", varType="U32")
        self.attributes["type"] = "Wait Until Next ms Multiple"
        self.attributes["genclass"] = "Function"


class Waitsrq(LVNode):
    def __init__(self):
        LVNode.__init__(self, "WaitSRQ")
        LVNode.addTerminal(self, "bus", varType="I32")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "SRQ", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "status", varType="Array", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "WaitSRQ"
        self.attributes["genclass"] = "Function"


class WhiteSpace(LVNode):
    def __init__(self):
        LVNode.__init__(self, "White Space?")
        LVNode.addTerminal(self, "space, h/v tab, cr, lf, ff?", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "char", varType="String")
        self.attributes["type"] = "White Space?"
        self.attributes["genclass"] = "Function"


class WriteDatalog(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Write Datalog")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "record(s)", varType="Void")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Write Datalog"
        self.attributes["genclass"] = "Function"


class WriteDevice(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Write Device")
        LVNode.addTerminal(self, "new offset", varType="I32", isInput=False)
        LVNode.addTerminal(self, "count", varType="I32", isInput=False)
        LVNode.addTerminal(self, "err", varType="I16", isInput=False)
        LVNode.addTerminal(self, "spc reset (F)", varType="Boolean")
        LVNode.addTerminal(self, "misc (-)", varType="Array")
        LVNode.addTerminal(self, "async (T)", varType="Boolean")
        LVNode.addTerminal(self, "pos offset (-)", varType="I32")
        LVNode.addTerminal(self, "pos mode (-)", varType="I16")
        LVNode.addTerminal(self, "string", varType="String")
        LVNode.addTerminal(self, "device refnum", varType="Refnum")
        self.attributes["type"] = "Write Device"
        self.attributes["genclass"] = "Function"


class WriteFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Write File")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "offset", varType="I32", isInput=False)
        LVNode.addTerminal(self, "dup refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "convert eol (F)", varType="Boolean")
        LVNode.addTerminal(self, "data", varType="Cluster")
        LVNode.addTerminal(self, "header (F)", varType="Boolean")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "pos offset (0)", varType="I32")
        LVNode.addTerminal(self, "pos mode (0:2)", varType="Enum U16")
        LVNode.addTerminal(self, "refnum", varType="Refnum")
        self.attributes["type"] = "Write File"
        self.attributes["genclass"] = "Function"


class WriteToBinaryFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Write to Binary File")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "cancelled", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "prepend array or string size? (T)", varType="Boolean")
        LVNode.addTerminal(self, "prompt (Choose or enter file path)", varType="String")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "byte order (0:big-endian, network order)", varType="Enum U16")
        LVNode.addTerminal(self, "data", varType="Cluster")
        LVNode.addTerminal(self, "file (use dialog)", varType="Path")
        self.attributes["type"] = "Write to Binary File"
        self.attributes["genclass"] = "Function"


class WriteToTextFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Write to Text File")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "cancelled", varType="Boolean", isInput=False)
        LVNode.addTerminal(self, "refnum out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "prompt (Choose or enter file path)", varType="String")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "text", varType="String")
        LVNode.addTerminal(self, "file (use dialog)", varType="Path")
        self.attributes["type"] = "Write to Text File"
        self.attributes["genclass"] = "Function"


class YThRootOfX(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Y-th Root of X")
        LVNode.addTerminal(self, "y-th root(x)", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "x", varType="Double Float")
        LVNode.addTerminal(self, "y", varType="Double Float")
        self.attributes["type"] = "Y-th Root of X"
        self.attributes["genclass"] = "Function"
