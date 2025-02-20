from node import LVNode

class GenericFunction(LVNode):
    def __init__(self, name, type):
        LVNode.__init__(self, name)
        self.attributes["type"] = type
        self.attributes["genclass"] = "Function"

class AbsoluteValue(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Absolute Value")
        LVNode.addTerminal(self, "abs(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Absolute Value"
        self.attributes["genclass"] = "Function"


class AcceptTls(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Accept TLS")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "client certificate chain", isInput=False)
        LVNode.addTerminal(self, "TLS connection", isInput=False)
        LVNode.addTerminal(self, "timeout ms (300000)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "immutable TLS configuration", isInput=True)
        LVNode.addTerminal(self, "TCP connection", isInput=True)
        self.attributes["type"] = "Accept TLS"
        self.attributes["genclass"] = "Function"


class AccessRights(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Access Rights")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "permissions", isInput=False)
        LVNode.addTerminal(self, "group", isInput=False)
        LVNode.addTerminal(self, "owner", isInput=False)
        LVNode.addTerminal(self, "dup path", isInput=False)
        LVNode.addTerminal(self, "path", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "new permissions", isInput=True)
        LVNode.addTerminal(self, "new group", isInput=True)
        LVNode.addTerminal(self, "new owner", isInput=True)
        self.attributes["type"] = "Access Rights"
        self.attributes["genclass"] = "Function"


class Add(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Add")
        LVNode.addTerminal(self, "x+y", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Add"
        self.attributes["genclass"] = "Function"


class AddWithErrorTerminals(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Add (with error terminals)")
        LVNode.addTerminal(self, "x+y", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        self.attributes["type"] = "Add (with error terminals)"
        self.attributes["genclass"] = "Function"


class AddArrayElements(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Add Array Elements")
        LVNode.addTerminal(self, "sum", isInput=False)
        LVNode.addTerminal(self, "numeric array", isInput=True)
        self.attributes["type"] = "Add Array Elements"
        self.attributes["genclass"] = "Function"


class AddEntropy(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Add Entropy")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "entropy", isInput=True)
        self.attributes["type"] = "Add Entropy"
        self.attributes["genclass"] = "Function"


class AddPrivateKeyToTlsConfiguration(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Add Private Key To TLS Configuration")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "TLS configuration out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "certificate chain", isInput=True)
        LVNode.addTerminal(self, "private key", isInput=True)
        LVNode.addTerminal(self, "TLS configuration", isInput=True)
        self.attributes["type"] = "Add Private Key To TLS Configuration"
        self.attributes["genclass"] = "Function"


class AddTrustedCertificateToTlsConfiguration(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Add Trusted Certificate To TLS Configuration")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "TLS configuration out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "certificate", isInput=True)
        LVNode.addTerminal(self, "TLS configuration", isInput=True)
        self.attributes["type"] = "Add Trusted Certificate To TLS Configuration"
        self.attributes["genclass"] = "Function"


class Allspoll(LVNode):
    def __init__(self):
        LVNode.__init__(self, "AllSpoll")
        LVNode.addTerminal(self, "bus", isInput=True)
        LVNode.addTerminal(self, "address list", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "serial poll byte list", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "byte count", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "AllSpoll"
        self.attributes["genclass"] = "Function"


class AlwaysCopy(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Always Copy")
        LVNode.addTerminal(self, "Output", isInput=False)
        LVNode.addTerminal(self, "Input", isInput=True)
        self.attributes["type"] = "Always Copy"
        self.attributes["genclass"] = "Function"


class And(LVNode):
    def __init__(self):
        LVNode.__init__(self, "And")
        LVNode.addTerminal(self, "x .and. y?", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "And"
        self.attributes["genclass"] = "Function"


class AndArrayElements(LVNode):
    def __init__(self):
        LVNode.__init__(self, "And Array Elements")
        LVNode.addTerminal(self, "logical AND", isInput=False)
        LVNode.addTerminal(self, "Boolean array", isInput=True)
        self.attributes["type"] = "And Array Elements"
        self.attributes["genclass"] = "Function"


class AppendTrueFalseString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Append True/False String")
        LVNode.addTerminal(self, "output string", isInput=False)
        LVNode.addTerminal(self, "selector", isInput=True)
        LVNode.addTerminal(self, "false string", isInput=True)
        LVNode.addTerminal(self, "true string", isInput=True)
        LVNode.addTerminal(self, "string ("")", isInput=True)
        self.attributes["type"] = "Append True/False String"
        self.attributes["genclass"] = "Function"


class ArrayMaxMin(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Array Max & Min")
        LVNode.addTerminal(self, "array", isInput=True)
        LVNode.addTerminal(self, "max value", isInput=False)
        LVNode.addTerminal(self, "max index (indices)", isInput=False)
        LVNode.addTerminal(self, "min value", isInput=False)
        LVNode.addTerminal(self, "min index (indices)", isInput=False)
        self.attributes["type"] = "Array Max & Min"
        self.attributes["genclass"] = "Function"


class ArrayOfStringsToPath(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Array of Strings to Path")
        LVNode.addTerminal(self, "array of strings", isInput=True)
        LVNode.addTerminal(self, "relative", isInput=True)
        LVNode.addTerminal(self, "path", isInput=False)
        self.attributes["type"] = "Array of Strings to Path"
        self.attributes["genclass"] = "Function"


class ArraySize(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Array Size")
        LVNode.addTerminal(self, "size(s)", isInput=False)
        LVNode.addTerminal(self, "array", isInput=True)
        self.attributes["type"] = "Array Size"
        self.attributes["genclass"] = "Function"


class ArrayToCluster(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Array To Cluster")
        LVNode.addTerminal(self, "cluster", isInput=False)
        LVNode.addTerminal(self, "array", isInput=True)
        self.attributes["type"] = "Array To Cluster"
        self.attributes["genclass"] = "Function"


class ArrayToSpreadsheetString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Array To Spreadsheet String")
        LVNode.addTerminal(self, "spreadsheet string", isInput=False)
        LVNode.addTerminal(self, "delimiter (Tab)", isInput=True)
        LVNode.addTerminal(self, "array", isInput=True)
        LVNode.addTerminal(self, "format string", isInput=True)
        self.attributes["type"] = "Array To Spreadsheet String"
        self.attributes["genclass"] = "Function"


class Arraymeminfo(LVNode):
    def __init__(self):
        LVNode.__init__(self, "ArrayMemInfo")
        LVNode.addTerminal(self, "mem info out", isInput=False)
        LVNode.addTerminal(self, "array out", isInput=False)
        LVNode.addTerminal(self, "array in", isInput=True)
        self.attributes["type"] = "ArrayMemInfo"
        self.attributes["genclass"] = "Function"


class AssertStructuralTypeMatch(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Assert Structural Type Match")
        LVNode.addTerminal(self, "reference", isInput=True)
        LVNode.addTerminal(self, "anything", isInput=True)
        self.attributes["type"] = "Assert Structural Type Match"
        self.attributes["genclass"] = "Function"


class AutomationClose(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Automation Close")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "error in(no error)", isInput=True)
        LVNode.addTerminal(self, "Automation Refnum", isInput=True)
        self.attributes["type"] = "Automation Close"
        self.attributes["genclass"] = "Function"


class AutomationOpen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Automation Open")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "Automation Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "", isInput=True)
        LVNode.addTerminal(self, "machine name", isInput=True)
        LVNode.addTerminal(self, "Automation Refnum", isInput=True)
        self.attributes["type"] = "Automation Open"
        self.attributes["genclass"] = "Function"


class BitpackToArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Bitpack to Array")
        LVNode.addTerminal(self, "bparray", isInput=False)
        LVNode.addTerminal(self, "data", isInput=True)
        self.attributes["type"] = "Bitpack to Array"
        self.attributes["genclass"] = "Function"


class BluetoothCloseConnection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Bluetooth Close Connection")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "connection ID out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "abort (F)", isInput=True)
        LVNode.addTerminal(self, "connection ID", isInput=True)
        self.attributes["type"] = "Bluetooth Close Connection"
        self.attributes["genclass"] = "Function"


class BluetoothCreateListener(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Bluetooth Create Listener")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "channel", isInput=False)
        LVNode.addTerminal(self, "listener ID", isInput=False)
        LVNode.addTerminal(self, "service description", isInput=True)
        LVNode.addTerminal(self, "address", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "uuid", isInput=True)
        self.attributes["type"] = "Bluetooth Create Listener"
        self.attributes["genclass"] = "Function"


class BluetoothDiscover(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Bluetooth Discover")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "device list", isInput=False)
        LVNode.addTerminal(self, "number of devices", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "time limit ms (10000)", isInput=True)
        self.attributes["type"] = "Bluetooth Discover"
        self.attributes["genclass"] = "Function"


class BluetoothOpenConnection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Bluetooth Open Connection")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "connection ID", isInput=False)
        LVNode.addTerminal(self, "uuid", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (60000)", isInput=True)
        LVNode.addTerminal(self, "channel (0)", isInput=True)
        LVNode.addTerminal(self, "address", isInput=True)
        self.attributes["type"] = "Bluetooth Open Connection"
        self.attributes["genclass"] = "Function"


class BluetoothRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Bluetooth Read")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "data out", isInput=False)
        LVNode.addTerminal(self, "connection ID out", isInput=False)
        LVNode.addTerminal(self, "mode (standard)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (25000)", isInput=True)
        LVNode.addTerminal(self, "bytes to read", isInput=True)
        LVNode.addTerminal(self, "connection ID", isInput=True)
        self.attributes["type"] = "Bluetooth Read"
        self.attributes["genclass"] = "Function"


class BluetoothWaitOnListener(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Bluetooth Wait On Listener")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "remote channel", isInput=False)
        LVNode.addTerminal(self, "remote address", isInput=False)
        LVNode.addTerminal(self, "listener ID out", isInput=False)
        LVNode.addTerminal(self, "connection ID", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (wait forever: -1)", isInput=True)
        LVNode.addTerminal(self, "resolve remote address (T)", isInput=True)
        LVNode.addTerminal(self, "listener ID in", isInput=True)
        self.attributes["type"] = "Bluetooth Wait On Listener"
        self.attributes["genclass"] = "Function"


class BluetoothWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Bluetooth Write")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "bytes written", isInput=False)
        LVNode.addTerminal(self, "connection ID out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (25000)", isInput=True)
        LVNode.addTerminal(self, "data in", isInput=True)
        LVNode.addTerminal(self, "connection ID", isInput=True)
        self.attributes["type"] = "Bluetooth Write"
        self.attributes["genclass"] = "Function"


class BooleanArrayToNumber(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Boolean Array To Number")
        LVNode.addTerminal(self, "number", isInput=False)
        LVNode.addTerminal(self, "Boolean array", isInput=True)
        self.attributes["type"] = "Boolean Array To Number"
        self.attributes["genclass"] = "Function"


class BooleanTo01(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Boolean To (0,1)")
        LVNode.addTerminal(self, "0, 1", isInput=False)
        LVNode.addTerminal(self, "Boolean", isInput=True)
        self.attributes["type"] = "Boolean To (0,1)"
        self.attributes["genclass"] = "Function"


class BuildPath(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Build Path")
        LVNode.addTerminal(self, "appended path", isInput=False)
        LVNode.addTerminal(self, "name or relative path", isInput=True)
        LVNode.addTerminal(self, "base path", isInput=True)
        self.attributes["type"] = "Build Path"
        self.attributes["genclass"] = "Function"


class ByteArrayToString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Byte Array To String")
        LVNode.addTerminal(self, "string", isInput=False)
        LVNode.addTerminal(self, "unsigned byte array", isInput=True)
        self.attributes["type"] = "Byte Array To String"
        self.attributes["genclass"] = "Function"


class CallChain(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Call Chain")
        LVNode.addTerminal(self, "call chain", isInput=False)
        self.attributes["type"] = "Call Chain"
        self.attributes["genclass"] = "Function"


class CancelNotification(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Cancel Notification")
        LVNode.addTerminal(self, "notifier", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "notifier out", isInput=False)
        LVNode.addTerminal(self, "canceled notifcation", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Cancel Notification"
        self.attributes["genclass"] = "Function"


class CastUnitBases(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Cast Unit Bases")
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "unit (none)", isInput=True)
        LVNode.addTerminal(self, "x", isInput=False)
        self.attributes["type"] = "Cast Unit Bases"
        self.attributes["genclass"] = "Function"


class ClearFixedPointOverflowStatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Clear Fixed-Point Overflow Status")
        LVNode.addTerminal(self, "overflow?", isInput=False)
        LVNode.addTerminal(self, "FXP with overflow cleared", isInput=False)
        LVNode.addTerminal(self, "FXP", isInput=True)
        self.attributes["type"] = "Clear Fixed-Point Overflow Status"
        self.attributes["genclass"] = "Function"


class CloseFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Close File")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "path", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Close File"
        self.attributes["genclass"] = "Function"


class CloseFileDeprecated(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Close File (deprecated)")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "path", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Close File (deprecated)"
        self.attributes["genclass"] = "Function"


class CloseMatlabSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Close MATLAB Session")
        LVNode.addTerminal(self, "session in", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Close MATLAB Session"
        self.attributes["genclass"] = "Function"


class ClosePythonSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Close Python Session")
        LVNode.addTerminal(self, "session in", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Close Python Session"
        self.attributes["genclass"] = "Function"


class CloseReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Close Reference")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "reference", isInput=True)
        self.attributes["type"] = "Close Reference"
        self.attributes["genclass"] = "Function"


class CloseTlsConfiguration(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Close TLS Configuration")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "TLS configuration", isInput=True)
        self.attributes["type"] = "Close TLS Configuration"
        self.attributes["genclass"] = "Function"


class CloseVariableConnection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Close Variable Connection")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "shared variable refnum in", isInput=True)
        self.attributes["type"] = "Close Variable Connection"
        self.attributes["genclass"] = "Function"


class ClusterToArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Cluster To Array")
        LVNode.addTerminal(self, "array", isInput=False)
        LVNode.addTerminal(self, "cluster", isInput=True)
        self.attributes["type"] = "Cluster To Array"
        self.attributes["genclass"] = "Function"


class CoerceToType(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Coerce To Type")
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "type", isInput=True)
        LVNode.addTerminal(self, "coerced x", isInput=False)
        self.attributes["type"] = "Coerce To Type"
        self.attributes["genclass"] = "Function"


class CollectionSize(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Collection Size")
        LVNode.addTerminal(self, "size", isInput=False)
        LVNode.addTerminal(self, "collection", isInput=True)
        self.attributes["type"] = "Collection Size"
        self.attributes["genclass"] = "Function"


class ComplexConjugate(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Complex Conjugate")
        LVNode.addTerminal(self, "x - iy", isInput=False)
        LVNode.addTerminal(self, "x + iy", isInput=True)
        self.attributes["type"] = "Complex Conjugate"
        self.attributes["genclass"] = "Function"


class ComplexToPolar(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Complex To Polar")
        LVNode.addTerminal(self, "r * e^(i*theta)", isInput=True)
        LVNode.addTerminal(self, "r", isInput=False)
        LVNode.addTerminal(self, "theta", isInput=False)
        self.attributes["type"] = "Complex To Polar"
        self.attributes["genclass"] = "Function"


class ComplexToReIm(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Complex To Re/Im")
        LVNode.addTerminal(self, "x + iy", isInput=True)
        LVNode.addTerminal(self, "x", isInput=False)
        LVNode.addTerminal(self, "y", isInput=False)
        self.attributes["type"] = "Complex To Re/Im"
        self.attributes["genclass"] = "Function"


class ControlHelpWindow(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Control Help Window")
        LVNode.addTerminal(self, "Top Left Corner", isInput=True)
        LVNode.addTerminal(self, "Show", isInput=True)
        self.attributes["type"] = "Control Help Window"
        self.attributes["genclass"] = "Function"


class ControlOnlineHelp(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Control Online Help")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "Path to the help file", isInput=True)
        LVNode.addTerminal(self, "String to search for", isInput=True)
        LVNode.addTerminal(self, "Operation", isInput=True)
        self.attributes["type"] = "Control Online Help"
        self.attributes["genclass"] = "Function"


class Copy(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Copy")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "cancelled", isInput=False)
        LVNode.addTerminal(self, "new path", isInput=False)
        LVNode.addTerminal(self, "prompt (Choose or enter target path for copy)", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "overwrite (F)", isInput=True)
        LVNode.addTerminal(self, "target path (use dialog)", isInput=True)
        LVNode.addTerminal(self, "source path", isInput=True)
        self.attributes["type"] = "Copy"
        self.attributes["genclass"] = "Function"


class CopyDeprecated(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Copy (deprecated)")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "new path", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "target path", isInput=True)
        LVNode.addTerminal(self, "source path", isInput=True)
        self.attributes["type"] = "Copy (deprecated)"
        self.attributes["genclass"] = "Function"


class Cosecant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Cosecant")
        LVNode.addTerminal(self, "1/sin(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Cosecant"
        self.attributes["genclass"] = "Function"


class Cosine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Cosine")
        LVNode.addTerminal(self, "cos(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Cosine"
        self.attributes["genclass"] = "Function"


class Cotangent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Cotangent")
        LVNode.addTerminal(self, "1/tan(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Cotangent"
        self.attributes["genclass"] = "Function"


class CpuInformation(LVNode):
    def __init__(self):
        LVNode.__init__(self, "CPU Information")
        LVNode.addTerminal(self, "# of logical processors", isInput=False)
        LVNode.addTerminal(self, "# of packages", isInput=False)
        LVNode.addTerminal(self, "# of cores per package", isInput=False)
        LVNode.addTerminal(self, "# of logical processors per core", isInput=False)
        self.attributes["type"] = "CPU Information"
        self.attributes["genclass"] = "Function"


class CreateFolder(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Create Folder")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "cancelled", isInput=False)
        LVNode.addTerminal(self, "created path", isInput=False)
        LVNode.addTerminal(self, "prompt (Create Folder)", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "path (use dialog)", isInput=True)
        self.attributes["type"] = "Create Folder"
        self.attributes["genclass"] = "Function"


class CreateNetworkStreamEndpoint(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Create Network Stream Endpoint")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "endpoint", isInput=False)
        LVNode.addTerminal(self, "timeout in ms (-1)", isInput=True)
        LVNode.addTerminal(self, "element allocation mode", isInput=True)
        LVNode.addTerminal(self, "buffer sizes", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "data type", isInput=True)
        LVNode.addTerminal(self, "remote endpoint url", isInput=True)
        LVNode.addTerminal(self, "endpoint name", isInput=True)
        self.attributes["type"] = "Create Network Stream Endpoint"
        self.attributes["genclass"] = "Function"


class CreateNetworkStreamReaderEndpoint(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Create Network Stream Reader Endpoint")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "reader endpoint", isInput=False)
        LVNode.addTerminal(self, "timeout in ms (-1)", isInput=True)
        LVNode.addTerminal(self, "element allocation mode", isInput=True)
        LVNode.addTerminal(self, "reader buffer size", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "data type", isInput=True)
        LVNode.addTerminal(self, "writer url", isInput=True)
        LVNode.addTerminal(self, "reader name", isInput=True)
        self.attributes["type"] = "Create Network Stream Reader Endpoint"
        self.attributes["genclass"] = "Function"


class CreateNetworkStreamWriterEndpoint(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Create Network Stream Writer Endpoint")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "writer endpoint", isInput=False)
        LVNode.addTerminal(self, "timeout in ms (-1)", isInput=True)
        LVNode.addTerminal(self, "element allocation mode", isInput=True)
        LVNode.addTerminal(self, "writer buffer size", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "data type", isInput=True)
        LVNode.addTerminal(self, "reader url", isInput=True)
        LVNode.addTerminal(self, "writer name", isInput=True)
        self.attributes["type"] = "Create Network Stream Writer Endpoint"
        self.attributes["genclass"] = "Function"


class CreateUniqueNetworkStreamEndpoint(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Create Unique Network Stream Endpoint")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "endpoint", isInput=False)
        LVNode.addTerminal(self, "max connections (-1)", isInput=True)
        LVNode.addTerminal(self, "timeout in ms (-1)", isInput=True)
        LVNode.addTerminal(self, "element allocation mode", isInput=True)
        LVNode.addTerminal(self, "buffer sizes", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "data type", isInput=True)
        LVNode.addTerminal(self, "base endpoint name", isInput=True)
        self.attributes["type"] = "Create Unique Network Stream Endpoint"
        self.attributes["genclass"] = "Function"


class CreateUniqueNetworkStreamReaderEndpoint(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Create Unique Network Stream Reader Endpoint")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "reader endpoint", isInput=False)
        LVNode.addTerminal(self, "max connections (-1)", isInput=True)
        LVNode.addTerminal(self, "timeout in ms (-1)", isInput=True)
        LVNode.addTerminal(self, "element allocation mode", isInput=True)
        LVNode.addTerminal(self, "reader buffer size", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "data type", isInput=True)
        LVNode.addTerminal(self, "base reader name", isInput=True)
        self.attributes["type"] = "Create Unique Network Stream Reader Endpoint"
        self.attributes["genclass"] = "Function"


class CreateUniqueNetworkStreamWriterEndpoint(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Create Unique Network Stream Writer Endpoint")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "writer endpoint", isInput=False)
        LVNode.addTerminal(self, "max connections (-1)", isInput=True)
        LVNode.addTerminal(self, "timeout in ms (-1)", isInput=True)
        LVNode.addTerminal(self, "element allocation mode", isInput=True)
        LVNode.addTerminal(self, "writer buffer size", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "data type", isInput=True)
        LVNode.addTerminal(self, "base writer name", isInput=True)
        self.attributes["type"] = "Create Unique Network Stream Writer Endpoint"
        self.attributes["genclass"] = "Function"


class CreateUserEvent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Create User Event")
        LVNode.addTerminal(self, "user event datatype", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "user event", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Create User Event"
        self.attributes["genclass"] = "Function"


class CurrentProcessorId(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Current Processor ID")
        LVNode.addTerminal(self, "current processor ID", isInput=False)
        self.attributes["type"] = "Current Processor ID"
        self.attributes["genclass"] = "Function"


class CurrentViSMenubar(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Current VI's Menubar")
        LVNode.addTerminal(self, "menu reference", isInput=False)
        self.attributes["type"] = "Current VI's Menubar"
        self.attributes["genclass"] = "Function"


class CurrentViSPath(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Current VI's Path")
        LVNode.addTerminal(self, "path", isInput=False)
        self.attributes["type"] = "Current VI's Path"
        self.attributes["genclass"] = "Function"


class DataCacheSize(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Data Cache Size")
        LVNode.addTerminal(self, "cache level (2)", isInput=True)
        LVNode.addTerminal(self, "total cache size (in bytes)", isInput=False)
        LVNode.addTerminal(self, "cache entry size (in bytes)", isInput=False)
        self.attributes["type"] = "Data Cache Size"
        self.attributes["genclass"] = "Function"


class DatasocketClose(LVNode):
    def __init__(self):
        LVNode.__init__(self, "DataSocket Close")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "timed out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "ms timeout (0)", isInput=True)
        LVNode.addTerminal(self, "connection id", isInput=True)
        self.attributes["type"] = "DataSocket Close"
        self.attributes["genclass"] = "Function"


class DatasocketOpen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "DataSocket Open")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "connection id", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "ms timeout (10000)", isInput=True)
        LVNode.addTerminal(self, "mode", isInput=True)
        LVNode.addTerminal(self, "URL", isInput=True)
        self.attributes["type"] = "DataSocket Open"
        self.attributes["genclass"] = "Function"


class DatasocketRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "DataSocket Read")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "timed out", isInput=False)
        LVNode.addTerminal(self, "data", isInput=False)
        LVNode.addTerminal(self, "connection out", isInput=False)
        LVNode.addTerminal(self, "timestamp", isInput=False)
        LVNode.addTerminal(self, "quality", isInput=False)
        LVNode.addTerminal(self, "wait for updated value (T)", isInput=True)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "ms timeout (10000)", isInput=True)
        LVNode.addTerminal(self, "type (Variant)", isInput=True)
        LVNode.addTerminal(self, "connection in", isInput=True)
        self.attributes["type"] = "DataSocket Read"
        self.attributes["genclass"] = "Function"


class DatasocketWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "DataSocket Write")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "timed out", isInput=False)
        LVNode.addTerminal(self, "connection out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "ms timeout (0)", isInput=True)
        LVNode.addTerminal(self, "data", isInput=True)
        LVNode.addTerminal(self, "connection in", isInput=True)
        self.attributes["type"] = "DataSocket Write"
        self.attributes["genclass"] = "Function"


class DateTimeToSeconds(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Date/Time To Seconds")
        LVNode.addTerminal(self, "time stamp", isInput=False)
        LVNode.addTerminal(self, "is UTC (F)", isInput=True)
        LVNode.addTerminal(self, "date time rec", isInput=True)
        self.attributes["type"] = "Date/Time To Seconds"
        self.attributes["genclass"] = "Function"


class DecimalDigit(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Decimal Digit?")
        LVNode.addTerminal(self, "digit?", isInput=False)
        LVNode.addTerminal(self, "char", isInput=True)
        self.attributes["type"] = "Decimal Digit?"
        self.attributes["genclass"] = "Function"


class DecimalStringToNumber(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Decimal String To Number")
        LVNode.addTerminal(self, "number", isInput=False)
        LVNode.addTerminal(self, "offset past number", isInput=False)
        LVNode.addTerminal(self, "default (0L)", isInput=True)
        LVNode.addTerminal(self, "offset", isInput=True)
        LVNode.addTerminal(self, "string", isInput=True)
        self.attributes["type"] = "Decimal String To Number"
        self.attributes["genclass"] = "Function"


class Decrement(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Decrement")
        LVNode.addTerminal(self, "x-1", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Decrement"
        self.attributes["genclass"] = "Function"


class DefaultDirectory(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Default Directory")
        LVNode.addTerminal(self, "path", isInput=False)
        self.attributes["type"] = "Default Directory"
        self.attributes["genclass"] = "Function"


class Delete(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Delete")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "cancelled", isInput=False)
        LVNode.addTerminal(self, "deleted path", isInput=False)
        LVNode.addTerminal(self, "prompt (Delete)", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "confirm (F)", isInput=True)
        LVNode.addTerminal(self, "entire hierarchy (F)", isInput=True)
        LVNode.addTerminal(self, "path (use dialog)", isInput=True)
        self.attributes["type"] = "Delete"
        self.attributes["genclass"] = "Function"


class DeleteDeprecated(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Delete (deprecated)")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "dup path", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "path", isInput=True)
        self.attributes["type"] = "Delete (deprecated)"
        self.attributes["genclass"] = "Function"


class DeleteDataValueReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Delete Data Value Reference")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "data value", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "data value reference", isInput=True)
        self.attributes["type"] = "Delete Data Value Reference"
        self.attributes["genclass"] = "Function"
class DeleteMenuItems(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Delete Menu Items")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "menu reference out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "items", isInput=True)
        LVNode.addTerminal(self, "menu tag", isInput=True)
        LVNode.addTerminal(self, "menu reference", isInput=True)
        self.attributes["type"] = "Delete Menu Items"
        self.attributes["genclass"] = "Function"


class DeleteVariantAttribute(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Delete Variant Attribute")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "found", isInput=False)
        LVNode.addTerminal(self, "Variant out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "name (all attributes)", isInput=True)
        LVNode.addTerminal(self, "Variant", isInput=True)
        self.attributes["type"] = "Delete Variant Attribute"
        self.attributes["genclass"] = "Function"


class DeleteWaveformAttribute(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Delete Waveform Attribute")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "no found", isInput=False)
        LVNode.addTerminal(self, "waveform out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "name (all attributes)", isInput=True)
        LVNode.addTerminal(self, "waveform", isInput=True)
        self.attributes["type"] = "Delete Waveform Attribute"
        self.attributes["genclass"] = "Function"


class DenyAccess(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Deny Access")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "deny mode (0:deny read/write)", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Deny Access"
        self.attributes["genclass"] = "Function"


class DequeueElement(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Dequeue Element")
        LVNode.addTerminal(self, "queue", isInput=True)
        LVNode.addTerminal(self, "timeout in ms (-1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "queue out", isInput=False)
        LVNode.addTerminal(self, "element", isInput=False)
        LVNode.addTerminal(self, "timed out?", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Dequeue Element"
        self.attributes["genclass"] = "Function"


class DestroyStreamEndpoint(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Destroy Stream Endpoint")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "endpoint in", isInput=True)
        self.attributes["type"] = "Destroy Stream Endpoint"
        self.attributes["genclass"] = "Function"


class DestroyUserEvent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Destroy User Event")
        LVNode.addTerminal(self, "user event", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Destroy User Event"
        self.attributes["genclass"] = "Function"


class Devclear(LVNode):
    def __init__(self):
        LVNode.__init__(self, "DevClear")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "address", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "DevClear"
        self.attributes["genclass"] = "Function"


class Devclearlist(LVNode):
    def __init__(self):
        LVNode.__init__(self, "DevClearList")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "address list", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "DevClearList"
        self.attributes["genclass"] = "Function"


class DeviceControlStatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Device Control/Status")
        LVNode.addTerminal(self, "new param", isInput=False)
        LVNode.addTerminal(self, "err", isInput=False)
        LVNode.addTerminal(self, "spc reset (F)", isInput=True)
        LVNode.addTerminal(self, "async (T)", isInput=True)
        LVNode.addTerminal(self, "param (-)", isInput=True)
        LVNode.addTerminal(self, "code (-)", isInput=True)
        LVNode.addTerminal(self, "ctrl/stat (T:ctrl)", isInput=True)
        LVNode.addTerminal(self, "device refnum", isInput=True)
        self.attributes["type"] = "Device Control/Status"
        self.attributes["genclass"] = "Function"


class Divide(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Divide")
        LVNode.addTerminal(self, "x/y", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Divide"
        self.attributes["genclass"] = "Function"


class DivideWithErrorTerminals(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Divide (with error terminals)")
        LVNode.addTerminal(self, "x/y", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        self.attributes["type"] = "Divide (with error terminals)"
        self.attributes["genclass"] = "Function"


class DynamicFpgaInterfaceCast(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Dynamic FPGA Interface Cast")
        LVNode.addTerminal(self, "Type", isInput=True)
        LVNode.addTerminal(self, "Session In", isInput=True)
        LVNode.addTerminal(self, "Session Out", isInput=False)
        self.attributes["type"] = "Dynamic FPGA Interface Cast"
        self.attributes["genclass"] = "Function"


class ElementOfSet(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Element of Set?")
        LVNode.addTerminal(self, "found?", isInput=False)
        LVNode.addTerminal(self, "element", isInput=True)
        LVNode.addTerminal(self, "set", isInput=True)
        self.attributes["type"] = "Element of Set?"
        self.attributes["genclass"] = "Function"


class EmptyArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Empty Array?")
        LVNode.addTerminal(self, "empty?", isInput=False)
        LVNode.addTerminal(self, "array", isInput=True)
        self.attributes["type"] = "Empty Array?"
        self.attributes["genclass"] = "Function"


class EmptyCollection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Empty Collection?")
        LVNode.addTerminal(self, "empty?", isInput=False)
        LVNode.addTerminal(self, "collection", isInput=True)
        self.attributes["type"] = "Empty Collection?"
        self.attributes["genclass"] = "Function"


class EmptyStringPath(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Empty String/Path?")
        LVNode.addTerminal(self, "empty?", isInput=False)
        LVNode.addTerminal(self, "string/path", isInput=True)
        self.attributes["type"] = "Empty String/Path?"
        self.attributes["genclass"] = "Function"


class EnableMenuTracking(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Enable Menu Tracking")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "menu reference out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "enable (T)", isInput=True)
        LVNode.addTerminal(self, "menu reference", isInput=True)
        self.attributes["type"] = "Enable Menu Tracking"
        self.attributes["genclass"] = "Function"


class Enablelocal(LVNode):
    def __init__(self):
        LVNode.__init__(self, "EnableLocal")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "address list", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "EnableLocal"
        self.attributes["genclass"] = "Function"


class Enableremote(LVNode):
    def __init__(self):
        LVNode.__init__(self, "EnableRemote")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "address list", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "EnableRemote"
        self.attributes["genclass"] = "Function"


class EnqueueElement(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Enqueue Element")
        LVNode.addTerminal(self, "queue", isInput=True)
        LVNode.addTerminal(self, "element", isInput=True)
        LVNode.addTerminal(self, "timeout in ms (-1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "queue out", isInput=False)
        LVNode.addTerminal(self, "timed out?", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Enqueue Element"
        self.attributes["genclass"] = "Function"


class EnqueueElementAtOppositeEnd(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Enqueue Element At Opposite End")
        LVNode.addTerminal(self, "queue", isInput=True)
        LVNode.addTerminal(self, "element", isInput=True)
        LVNode.addTerminal(self, "timeout in ms (-1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "queue out", isInput=False)
        LVNode.addTerminal(self, "timed out?", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Enqueue Element At Opposite End"
        self.attributes["genclass"] = "Function"


class Eof(LVNode):
    def __init__(self):
        LVNode.__init__(self, "EOF")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "offset", isInput=False)
        LVNode.addTerminal(self, "dup refnum", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "pos offset (0)", isInput=True)
        LVNode.addTerminal(self, "pos mode (0:1)", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "EOF"
        self.attributes["genclass"] = "Function"


class EqualTo0(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Equal To 0?")
        LVNode.addTerminal(self, "x = 0?", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Equal To 0?"
        self.attributes["genclass"] = "Function"


class Equal(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Equal?")
        LVNode.addTerminal(self, "x = y?", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Equal?"
        self.attributes["genclass"] = "Function"


class ExclusiveOr(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Exclusive Or")
        LVNode.addTerminal(self, "x .xor. y?", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Exclusive Or"
        self.attributes["genclass"] = "Function"


class Exponential(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Exponential")
        LVNode.addTerminal(self, "exp(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Exponential"
        self.attributes["genclass"] = "Function"


class ExponentialArg1(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Exponential (Arg) -1")
        LVNode.addTerminal(self, "exp(x) -1", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Exponential (Arg) -1"
        self.attributes["genclass"] = "Function"


class FileDialog(LVNode):
    def __init__(self):
        LVNode.__init__(self, "File Dialog")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "cancelled", isInput=False)
        LVNode.addTerminal(self, "exists", isInput=False)
        LVNode.addTerminal(self, "selected path", isInput=False)
        LVNode.addTerminal(self, "pattern label", isInput=True)
        LVNode.addTerminal(self, "button label", isInput=True)
        LVNode.addTerminal(self, "pattern (all files)", isInput=True)
        LVNode.addTerminal(self, "prompt", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "default name", isInput=True)
        LVNode.addTerminal(self, "start path", isInput=True)
        self.attributes["type"] = "File Dialog"
        self.attributes["genclass"] = "Function"


class FileDialogDeprecated(LVNode):
    def __init__(self):
        LVNode.__init__(self, "File Dialog (deprecated)")
        LVNode.addTerminal(self, "cancelled", isInput=False)
        LVNode.addTerminal(self, "exists", isInput=False)
        LVNode.addTerminal(self, "path", isInput=False)
        LVNode.addTerminal(self, "pattern label", isInput=True)
        LVNode.addTerminal(self, "button label", isInput=True)
        LVNode.addTerminal(self, "datalog type", isInput=True)
        LVNode.addTerminal(self, "prompt", isInput=True)
        LVNode.addTerminal(self, "pattern", isInput=True)
        LVNode.addTerminal(self, "default name", isInput=True)
        LVNode.addTerminal(self, "select mode (2)", isInput=True)
        LVNode.addTerminal(self, "start path", isInput=True)
        self.attributes["type"] = "File Dialog (deprecated)"
        self.attributes["genclass"] = "Function"


class FileDirectoryInfo(LVNode):
    def __init__(self):
        LVNode.__init__(self, "File/Directory Info")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "last mod", isInput=False)
        LVNode.addTerminal(self, "size", isInput=False)
        LVNode.addTerminal(self, "path out", isInput=False)
        LVNode.addTerminal(self, "resolved path", isInput=False)
        LVNode.addTerminal(self, "directory", isInput=False)
        LVNode.addTerminal(self, "shortcut", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "path", isInput=True)
        self.attributes["type"] = "File/Directory Info"
        self.attributes["genclass"] = "Function"


class FileDirectoryInfoDeprecated(LVNode):
    def __init__(self):
        LVNode.__init__(self, "File/Directory Info (deprecated)")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "last mod", isInput=False)
        LVNode.addTerminal(self, "size", isInput=False)
        LVNode.addTerminal(self, "dup path", isInput=False)
        LVNode.addTerminal(self, "directory", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "path", isInput=True)
        self.attributes["type"] = "File/Directory Info (deprecated)"
        self.attributes["genclass"] = "Function"


class Findlstn(LVNode):
    def __init__(self):
        LVNode.__init__(self, "FindLstn")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "number of listeners", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "listener address list", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "limit", isInput=True)
        LVNode.addTerminal(self, "address list", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "FindLstn"
        self.attributes["genclass"] = "Function"


class Findrqs(LVNode):
    def __init__(self):
        LVNode.__init__(self, "FindRQS")
        LVNode.addTerminal(self, "bus", isInput=True)
        LVNode.addTerminal(self, "address list", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "requester status byte", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "requester index", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "FindRQS"
        self.attributes["genclass"] = "Function"


class FirstCall(LVNode):
    def __init__(self):
        LVNode.__init__(self, "First Call?")
        LVNode.addTerminal(self, "First Call?: T/F", isInput=False)
        self.attributes["type"] = "First Call?"
        self.attributes["genclass"] = "Function"


class FixedPointOverflow(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Fixed-Point Overflow?")
        LVNode.addTerminal(self, "overflow?", isInput=False)
        LVNode.addTerminal(self, "FXP", isInput=True)
        self.attributes["type"] = "Fixed-Point Overflow?"
        self.attributes["genclass"] = "Function"


class FixedPointToIntegerCast(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Fixed-Point to Integer Cast")
        LVNode.addTerminal(self, "integer", isInput=False)
        LVNode.addTerminal(self, "fixed-point", isInput=True)
        self.attributes["type"] = "Fixed-Point to Integer Cast"
        self.attributes["genclass"] = "Function"


class FlattenToJson(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flatten To JSON")
        LVNode.addTerminal(self, "anything", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "enable LabVIEW extensions? (T)", isInput=True)
        LVNode.addTerminal(self, "JSON string", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Flatten To JSON"
        self.attributes["genclass"] = "Function"


class FlattenToString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flatten To String")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "type string", isInput=False)
        LVNode.addTerminal(self, "data string", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "byte order (0:big-endian, network order)", isInput=True)
        LVNode.addTerminal(self, "prepend array or string size? (T)", isInput=True)
        LVNode.addTerminal(self, "anything", isInput=True)
        self.attributes["type"] = "Flatten To String"
        self.attributes["genclass"] = "Function"


class FlattenToXml(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flatten To XML")
        LVNode.addTerminal(self, "xml string", isInput=False)
        LVNode.addTerminal(self, "anything", isInput=True)
        self.attributes["type"] = "Flatten To XML"
        self.attributes["genclass"] = "Function"


class FlattenedStringToVariant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flattened String To Variant")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "Variant", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "data string", isInput=True)
        LVNode.addTerminal(self, "type string", isInput=True)
        self.attributes["type"] = "Flattened String To Variant"
        self.attributes["genclass"] = "Function"


class FloatingPointEqual(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Floating Point Equal?")
        LVNode.addTerminal(self, "x ~ y?", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "tolerance", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Floating Point Equal?"
        self.attributes["genclass"] = "Function"


class FlushEventQueue(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flush Event Queue")
        LVNode.addTerminal(self, "event registration refnum", isInput=True)
        LVNode.addTerminal(self, "include static events? (T)", isInput=True)
        LVNode.addTerminal(self, "event type or object", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "oldest event time", isInput=True)
        LVNode.addTerminal(self, "keep most recent", isInput=True)
        LVNode.addTerminal(self, "event reg refnum out", isInput=False)
        LVNode.addTerminal(self, "number of events discarded", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Flush Event Queue"
        self.attributes["genclass"] = "Function"


class FlushFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flush File")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Flush File"
        self.attributes["genclass"] = "Function"


class FlushFileDeprecated(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flush File (deprecated)")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "dup refnum", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Flush File (deprecated)"
        self.attributes["genclass"] = "Function"


class FlushQueue(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flush Queue")
        LVNode.addTerminal(self, "queue", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "queue out", isInput=False)
        LVNode.addTerminal(self, "remaining elements", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Flush Queue"
        self.attributes["genclass"] = "Function"


class FlushStream(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Flush Stream")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "timed out?", isInput=False)
        LVNode.addTerminal(self, "endpoint out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout in ms (-1)", isInput=True)
        LVNode.addTerminal(self, "wait condition", isInput=True)
        LVNode.addTerminal(self, "endpoint in", isInput=True)
        self.attributes["type"] = "Flush Stream"
        self.attributes["genclass"] = "Function"


class FormatDateTimeString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Format Date/Time String")
        LVNode.addTerminal(self, "date/time string", isInput=False)
        LVNode.addTerminal(self, "UTC format", isInput=True)
        LVNode.addTerminal(self, "seconds (now)", isInput=True)
        LVNode.addTerminal(self, "time format string (%c)", isInput=True)
        self.attributes["type"] = "Format Date/Time String"
        self.attributes["genclass"] = "Function"


class FormatValue(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Format Value")
        LVNode.addTerminal(self, "output string", isInput=False)
        LVNode.addTerminal(self, "value (0)", isInput=True)
        LVNode.addTerminal(self, "format string", isInput=True)
        LVNode.addTerminal(self, "string ("")", isInput=True)
        self.attributes["type"] = "Format Value"
        self.attributes["genclass"] = "Function"


class FpgaRefnumToSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "FPGA Refnum to Session")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "Session", isInput=False)
        LVNode.addTerminal(self, "error in(no error)", isInput=True)
        LVNode.addTerminal(self, "Refnum", isInput=True)
        self.attributes["type"] = "FPGA Refnum to Session"
        self.attributes["genclass"] = "Function"


class FractExpStringToNumber(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Fract/Exp String To Number")
        LVNode.addTerminal(self, "number", isInput=False)
        LVNode.addTerminal(self, "offset past number", isInput=False)
        LVNode.addTerminal(self, "use system decimal point (T)", isInput=True)
        LVNode.addTerminal(self, "default (0 dbl)", isInput=True)
        LVNode.addTerminal(self, "offset", isInput=True)
        LVNode.addTerminal(self, "string", isInput=True)
        self.attributes["type"] = "Fract/Exp String To Number"
        self.attributes["genclass"] = "Function"


class GenerateFrontPanelActivity(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Generate Front Panel Activity")
        LVNode.addTerminal(self, "front panel (this VI's panel)", isInput=True)
        self.attributes["type"] = "Generate Front Panel Activity"
        self.attributes["genclass"] = "Function"


class GenerateOccurrence(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Generate Occurrence")
        LVNode.addTerminal(self, "occurrence", isInput=False)
        self.attributes["type"] = "Generate Occurrence"
        self.attributes["genclass"] = "Function"


class GenerateUserEvent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Generate User Event")
        LVNode.addTerminal(self, "user event", isInput=True)
        LVNode.addTerminal(self, "event data cluster", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "priority (normal)", isInput=True)
        LVNode.addTerminal(self, "user event out", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Generate User Event"
        self.attributes["genclass"] = "Function"


class GenerateUserDefinedTraceEvent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Generate User-Defined Trace Event")
        LVNode.addTerminal(self, "trace integer", isInput=True)
        LVNode.addTerminal(self, "trace string", isInput=True)
        self.attributes["type"] = "Generate User-Defined Trace Event"
        self.attributes["genclass"] = "Function"


class GetControlValuesByIndex(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Control Values by Index")
        LVNode.addTerminal(self, "VI Refnum", isInput=True)
        LVNode.addTerminal(self, "control indexes", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "data values", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Get Control Values by Index"
        self.attributes["genclass"] = "Function"


class GetDatalogPosition(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Datalog Position")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "offset (in records)", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Get Datalog Position"
        self.attributes["genclass"] = "Function"


class GetDateTimeInSeconds(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Date/Time In Seconds")
        LVNode.addTerminal(self, "seconds since 1Jan1904", isInput=False)
        self.attributes["type"] = "Get Date/Time In Seconds"
        self.attributes["genclass"] = "Function"


class GetDateTimeString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Date/Time String")
        LVNode.addTerminal(self, "time string", isInput=False)
        LVNode.addTerminal(self, "date string", isInput=False)
        LVNode.addTerminal(self, "want seconds? (F)", isInput=True)
        LVNode.addTerminal(self, "seconds (now)", isInput=True)
        LVNode.addTerminal(self, "date format (0)", isInput=True)
        self.attributes["type"] = "Get Date/Time String"
        self.attributes["genclass"] = "Function"


class GetDragDropData(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Drag Drop Data")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "data", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "type", isInput=True)
        LVNode.addTerminal(self, "data name", isInput=True)
        self.attributes["type"] = "Get Drag Drop Data"
        self.attributes["genclass"] = "Function"


class GetFilePosition(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get File Position")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "offset (in bytes)", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Get File Position"
        self.attributes["genclass"] = "Function"


class GetFileSize(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get File Size")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "size (in bytes)", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "file", isInput=True)
        self.attributes["type"] = "Get File Size"
        self.attributes["genclass"] = "Function"


class GetHelpWindowStatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Help Window Status")
        LVNode.addTerminal(self, "Top Left Corner", isInput=False)
        LVNode.addTerminal(self, "Show", isInput=False)
        self.attributes["type"] = "Get Help Window Status"
        self.attributes["genclass"] = "Function"


class GetMenuItemInfo(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Menu Item Info")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "enabled", isInput=False)
        LVNode.addTerminal(self, "item name", isInput=False)
        LVNode.addTerminal(self, "menu reference out", isInput=False)
        LVNode.addTerminal(self, "checked", isInput=False)
        LVNode.addTerminal(self, "submenu tags", isInput=False)
        LVNode.addTerminal(self, "short cut", isInput=False)
        LVNode.addTerminal(self, "item tag", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "menu reference", isInput=True)
        self.attributes["type"] = "Get Menu Item Info"
        self.attributes["genclass"] = "Function"


class GetMenuSelection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Menu Selection")
        LVNode.addTerminal(self, "menu reference", isInput=True)
        LVNode.addTerminal(self, "ms timeout (200)", isInput=True)
        LVNode.addTerminal(self, "block menu (F)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timed out", isInput=False)
        LVNode.addTerminal(self, "menu reference out", isInput=False)
        LVNode.addTerminal(self, "item tag", isInput=False)
        LVNode.addTerminal(self, "item path", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Get Menu Selection"
        self.attributes["genclass"] = "Function"


class GetMenuShortCutInfo(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Menu Short Cut Info")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "item path", isInput=False)
        LVNode.addTerminal(self, "item tag", isInput=False)
        LVNode.addTerminal(self, "menu reference out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "short cut", isInput=True)
        LVNode.addTerminal(self, "menu reference", isInput=True)
        self.attributes["type"] = "Get Menu Short Cut Info"
        self.attributes["genclass"] = "Function"


class GetNotifierStatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Notifier Status")
        LVNode.addTerminal(self, "notifier", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "notifier name", isInput=False)
        LVNode.addTerminal(self, "notifier out", isInput=False)
        LVNode.addTerminal(self, "current notification", isInput=False)
        LVNode.addTerminal(self, "# waiting", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Get Notifier Status"
        self.attributes["genclass"] = "Function"


class GetNumberOfRecords(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Number of Records")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "# of records", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Get Number of Records"
        self.attributes["genclass"] = "Function"


class GetPermissions(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Permissions")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "group", isInput=False)
        LVNode.addTerminal(self, "owner", isInput=False)
        LVNode.addTerminal(self, "path out", isInput=False)
        LVNode.addTerminal(self, "permissions", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "path", isInput=True)
        self.attributes["type"] = "Get Permissions"
        self.attributes["genclass"] = "Function"


class GetQueueStatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Queue Status")
        LVNode.addTerminal(self, "queue", isInput=True)
        LVNode.addTerminal(self, "return elements? (F)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "max queue size", isInput=False)
        LVNode.addTerminal(self, "elements", isInput=False)
        LVNode.addTerminal(self, "queue name", isInput=False)
        LVNode.addTerminal(self, "# elements in queue", isInput=False)
        LVNode.addTerminal(self, "queue out", isInput=False)
        LVNode.addTerminal(self, "# pending remove", isInput=False)
        LVNode.addTerminal(self, "# pending insert", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Get Queue Status"
        self.attributes["genclass"] = "Function"


class GetTypeAndCreator(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Type and Creator")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "creator", isInput=False)
        LVNode.addTerminal(self, "type", isInput=False)
        LVNode.addTerminal(self, "path out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "path", isInput=True)
        self.attributes["type"] = "Get Type and Creator"
        self.attributes["genclass"] = "Function"


class GetVariantAttribute(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Variant Attribute")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "values", isInput=False)
        LVNode.addTerminal(self, "names", isInput=False)
        LVNode.addTerminal(self, "duplicate Variant", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "default value (empty Variant)", isInput=True)
        LVNode.addTerminal(self, "name", isInput=True)
        LVNode.addTerminal(self, "Variant", isInput=True)
        self.attributes["type"] = "Get Variant Attribute"
        self.attributes["genclass"] = "Function"


class GetVolumeInfo(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Volume Info")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "free (bytes)", isInput=False)
        LVNode.addTerminal(self, "size (bytes)", isInput=False)
        LVNode.addTerminal(self, "path out", isInput=False)
        LVNode.addTerminal(self, "", isInput=False)
        LVNode.addTerminal(self, "volume path", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "path", isInput=True)
        self.attributes["type"] = "Get Volume Info"
        self.attributes["genclass"] = "Function"


class GetWaveformAttribute(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Get Waveform Attribute")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "values", isInput=False)
        LVNode.addTerminal(self, "names", isInput=False)
        LVNode.addTerminal(self, "duplicate waveform", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "default value (empty Variant)", isInput=True)
        LVNode.addTerminal(self, "name", isInput=True)
        LVNode.addTerminal(self, "waveform", isInput=True)
        self.attributes["type"] = "Get Waveform Attribute"
        self.attributes["genclass"] = "Function"


class GpibClear(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Clear")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "address string", isInput=True)
        self.attributes["type"] = "GPIB Clear"
        self.attributes["genclass"] = "Function"


class GpibInitialization(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Initialization")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "require re-addressing (T)", isInput=True)
        LVNode.addTerminal(self, "disallow DMA (F)", isInput=True)
        LVNode.addTerminal(self, "assert REN with IFC (T)", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "IST bit sense (T)", isInput=True)
        LVNode.addTerminal(self, "address string", isInput=True)
        LVNode.addTerminal(self, "system controller (T)", isInput=True)
        self.attributes["type"] = "GPIB Initialization"
        self.attributes["genclass"] = "Function"


class GpibMisc(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Misc")
        LVNode.addTerminal(self, "command string", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "output string", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "GPIB Misc"
        self.attributes["genclass"] = "Function"


class GpibRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Read")
        LVNode.addTerminal(self, "address string", isInput=True)
        LVNode.addTerminal(self, "byte count", isInput=True)
        LVNode.addTerminal(self, "mode (0)", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "timeout ms (488.2 global)", isInput=True)
        LVNode.addTerminal(self, "data", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "GPIB Read"
        self.attributes["genclass"] = "Function"


class GpibSerialPoll(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Serial Poll")
        LVNode.addTerminal(self, "address string", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "serial poll byte", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "GPIB Serial Poll"
        self.attributes["genclass"] = "Function"


class GpibStatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Status")
        LVNode.addTerminal(self, "address string", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "GPIB error", isInput=False)
        LVNode.addTerminal(self, "byte count", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "GPIB Status"
        self.attributes["genclass"] = "Function"


class GpibTrigger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Trigger")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "address string", isInput=True)
        self.attributes["type"] = "GPIB Trigger"
        self.attributes["genclass"] = "Function"


class GpibWait(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Wait")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "timeout ms (488.2 global)", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "wait state vector", isInput=True)
        LVNode.addTerminal(self, "address string", isInput=True)
        self.attributes["type"] = "GPIB Wait"
        self.attributes["genclass"] = "Function"


class GpibWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "GPIB Write")
        LVNode.addTerminal(self, "address string", isInput=True)
        LVNode.addTerminal(self, "data", isInput=True)
        LVNode.addTerminal(self, "mode (0)", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "timeout ms (488.2 global)", isInput=True)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "GPIB Write"
        self.attributes["genclass"] = "Function"


class GreaterOrEqualTo0(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Greater Or Equal To 0?")
        LVNode.addTerminal(self, "x >= 0?", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Greater Or Equal To 0?"
        self.attributes["genclass"] = "Function"


class GreaterOrEqual(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Greater Or Equal?")
        LVNode.addTerminal(self, "x >= y?", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Greater Or Equal?"
        self.attributes["genclass"] = "Function"


class GreaterThan0(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Greater Than 0?")
        LVNode.addTerminal(self, "x > 0?", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Greater Than 0?"
        self.attributes["genclass"] = "Function"


class Greater(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Greater?")
        LVNode.addTerminal(self, "x > y?", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Greater?"
        self.attributes["genclass"] = "Function"


class HandlePeek(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Handle Peek")
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "error", isInput=False)
        LVNode.addTerminal(self, "num type (long)", isInput=True)
        LVNode.addTerminal(self, "offset", isInput=True)
        LVNode.addTerminal(self, "handle", isInput=True)
        self.attributes["type"] = "Handle Peek"
        self.attributes["genclass"] = "Function"


class HandlePoke(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Handle Poke")
        LVNode.addTerminal(self, "old value", isInput=False)
        LVNode.addTerminal(self, "handle", isInput=False)
        LVNode.addTerminal(self, "error", isInput=False)
        LVNode.addTerminal(self, "new value", isInput=True)
        LVNode.addTerminal(self, "offset", isInput=True)
        LVNode.addTerminal(self, "handle", isInput=True)
        self.attributes["type"] = "Handle Poke"
        self.attributes["genclass"] = "Function"


class HexDigit(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Hex Digit?")
        LVNode.addTerminal(self, "hex?", isInput=False)
        LVNode.addTerminal(self, "char", isInput=True)
        self.attributes["type"] = "Hex Digit?"
        self.attributes["genclass"] = "Function"


class HexadecimalStringToNumber(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Hexadecimal String To Number")
        LVNode.addTerminal(self, "number", isInput=False)
        LVNode.addTerminal(self, "offset past number", isInput=False)
        LVNode.addTerminal(self, "default (0uL)", isInput=True)
        LVNode.addTerminal(self, "offset", isInput=True)
        LVNode.addTerminal(self, "string", isInput=True)
        self.attributes["type"] = "Hexadecimal String To Number"
        self.attributes["genclass"] = "Function"


class HyperbolicCosecant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Hyperbolic Cosecant")
        LVNode.addTerminal(self, "csch(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Hyperbolic Cosecant"
        self.attributes["genclass"] = "Function"


class HyperbolicCosine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Hyperbolic Cosine")
        LVNode.addTerminal(self, "cosh(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Hyperbolic Cosine"
        self.attributes["genclass"] = "Function"


class HyperbolicCotangent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Hyperbolic Cotangent")
        LVNode.addTerminal(self, "coth(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Hyperbolic Cotangent"
        self.attributes["genclass"] = "Function"


class HyperbolicSecant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Hyperbolic Secant")
        LVNode.addTerminal(self, "sech(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Hyperbolic Secant"
        self.attributes["genclass"] = "Function"


class HyperbolicSine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Hyperbolic Sine")
        LVNode.addTerminal(self, "sinh(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Hyperbolic Sine"
        self.attributes["genclass"] = "Function"


class HyperbolicTangent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Hyperbolic Tangent")
        LVNode.addTerminal(self, "tanh(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Hyperbolic Tangent"
        self.attributes["genclass"] = "Function"


class Implies(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Implies")
        LVNode.addTerminal(self, "x .implies. y?", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Implies"
        self.attributes["genclass"] = "Function"


class InRangeAndCoerce(LVNode):
    def __init__(self):
        LVNode.__init__(self, "In Range and Coerce")
        LVNode.addTerminal(self, "In Range?", isInput=False)
        LVNode.addTerminal(self, "coerced(x)", isInput=False)
        LVNode.addTerminal(self, "lower limit", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "upper limit", isInput=True)
        self.attributes["type"] = "In Range and Coerce"
        self.attributes["genclass"] = "Function"


class IncludeFixedPointOverflowStatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Include Fixed-Point Overflow Status")
        LVNode.addTerminal(self, "FXP with overflow included", isInput=False)
        LVNode.addTerminal(self, "overflow", isInput=True)
        LVNode.addTerminal(self, "FXP", isInput=True)
        self.attributes["type"] = "Include Fixed-Point Overflow Status"
        self.attributes["genclass"] = "Function"
class Increment(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Increment")
        LVNode.addTerminal(self, "x+1", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Increment"
        self.attributes["genclass"] = "Function"


class IndexStringArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Index String Array")
        LVNode.addTerminal(self, "output string", isInput=False)
        LVNode.addTerminal(self, "index", isInput=True)
        LVNode.addTerminal(self, "string array", isInput=True)
        LVNode.addTerminal(self, "string ("")", isInput=True)
        self.attributes["type"] = "Index String Array"
        self.attributes["genclass"] = "Function"


class InsertIntoMap(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Insert Into Map")
        LVNode.addTerminal(self, "value unchanged?", isInput=False)
        LVNode.addTerminal(self, "key already included?", isInput=False)
        LVNode.addTerminal(self, "map out", isInput=False)
        LVNode.addTerminal(self, "value", isInput=True)
        LVNode.addTerminal(self, "key", isInput=True)
        LVNode.addTerminal(self, "map in", isInput=True)
        self.attributes["type"] = "Insert Into Map"
        self.attributes["genclass"] = "Function"


class InsertIntoSet(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Insert Into Set")
        LVNode.addTerminal(self, "already included?", isInput=False)
        LVNode.addTerminal(self, "set out", isInput=False)
        LVNode.addTerminal(self, "element", isInput=True)
        LVNode.addTerminal(self, "set in", isInput=True)
        self.attributes["type"] = "Insert Into Set"
        self.attributes["genclass"] = "Function"


class InsertMenuItems(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Insert Menu Items")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "item tags out", isInput=False)
        LVNode.addTerminal(self, "menu reference out", isInput=False)
        LVNode.addTerminal(self, "after item", isInput=True)
        LVNode.addTerminal(self, "menu tag", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "item tags", isInput=True)
        LVNode.addTerminal(self, "item names", isInput=True)
        LVNode.addTerminal(self, "menu reference", isInput=True)
        self.attributes["type"] = "Insert Menu Items"
        self.attributes["genclass"] = "Function"


class IntegerToFixedPointCast(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Integer to Fixed-Point Cast")
        LVNode.addTerminal(self, "integer", isInput=True)
        LVNode.addTerminal(self, "fixed-point type", isInput=True)
        LVNode.addTerminal(self, "fixed-point", isInput=False)
        self.attributes["type"] = "Integer to Fixed-Point Cast"
        self.attributes["genclass"] = "Function"


class Interpolate1dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Interpolate 1D Array")
        LVNode.addTerminal(self, "y value", isInput=False)
        LVNode.addTerminal(self, "fractional index or x", isInput=True)
        LVNode.addTerminal(self, "array of numbers or points", isInput=True)
        self.attributes["type"] = "Interpolate 1D Array"
        self.attributes["genclass"] = "Function"


class InverseCosecant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Cosecant")
        LVNode.addTerminal(self, "arccsc(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Inverse Cosecant"
        self.attributes["genclass"] = "Function"


class InverseCosine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Cosine")
        LVNode.addTerminal(self, "arccos(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Inverse Cosine"
        self.attributes["genclass"] = "Function"


class InverseCotangent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Cotangent")
        LVNode.addTerminal(self, "arccot(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Inverse Cotangent"
        self.attributes["genclass"] = "Function"


class InverseHyperbolicCosecant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Hyperbolic Cosecant")
        LVNode.addTerminal(self, "arccsch(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Inverse Hyperbolic Cosecant"
        self.attributes["genclass"] = "Function"


class InverseHyperbolicCosine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Hyperbolic Cosine")
        LVNode.addTerminal(self, "argcosh(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Inverse Hyperbolic Cosine"
        self.attributes["genclass"] = "Function"


class InverseHyperbolicCotangent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Hyperbolic Cotangent")
        LVNode.addTerminal(self, "arccoth(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Inverse Hyperbolic Cotangent"
        self.attributes["genclass"] = "Function"


class InverseHyperbolicSecant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Hyperbolic Secant")
        LVNode.addTerminal(self, "arcsech(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Inverse Hyperbolic Secant"
        self.attributes["genclass"] = "Function"


class InverseHyperbolicSine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Hyperbolic Sine")
        LVNode.addTerminal(self, "argsinh(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Inverse Hyperbolic Sine"
        self.attributes["genclass"] = "Function"


class InverseHyperbolicTangent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Hyperbolic Tangent")
        LVNode.addTerminal(self, "argtanh(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Inverse Hyperbolic Tangent"
        self.attributes["genclass"] = "Function"


class InverseSecant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Secant")
        LVNode.addTerminal(self, "arcsec(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Inverse Secant"
        self.attributes["genclass"] = "Function"


class InverseSine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Sine")
        LVNode.addTerminal(self, "arcsin(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Inverse Sine"
        self.attributes["genclass"] = "Function"


class InverseTangent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Tangent")
        LVNode.addTerminal(self, "arctan(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Inverse Tangent"
        self.attributes["genclass"] = "Function"


class InverseTangent2Input(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Inverse Tangent (2 Input)")
        LVNode.addTerminal(self, "atan2(y,x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "y", isInput=True)
        self.attributes["type"] = "Inverse Tangent (2 Input)"
        self.attributes["genclass"] = "Function"


class IpToString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IP To String")
        LVNode.addTerminal(self, "name", isInput=False)
        LVNode.addTerminal(self, "dot notation? (F)", isInput=True)
        LVNode.addTerminal(self, "net address", isInput=True)
        self.attributes["type"] = "IP To String"
        self.attributes["genclass"] = "Function"


class IrdaCloseConnection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IrDA Close Connection")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "connection ID out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "abort (F)", isInput=True)
        LVNode.addTerminal(self, "connection ID", isInput=True)
        self.attributes["type"] = "IrDA Close Connection"
        self.attributes["genclass"] = "Function"


class IrdaCreateListener(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IrDA Create Listener")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "listener ID", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "service name", isInput=True)
        self.attributes["type"] = "IrDA Create Listener"
        self.attributes["genclass"] = "Function"


class IrdaDiscover(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IrDA Discover")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "device list", isInput=False)
        LVNode.addTerminal(self, "number of devices", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        self.attributes["type"] = "IrDA Discover"
        self.attributes["genclass"] = "Function"


class IrdaOpenConnection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IrDA Open Connection")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "connection ID", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (60000)", isInput=True)
        LVNode.addTerminal(self, "remote device id", isInput=True)
        LVNode.addTerminal(self, "service name", isInput=True)
        self.attributes["type"] = "IrDA Open Connection"
        self.attributes["genclass"] = "Function"


class IrdaRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IrDA Read")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "data out", isInput=False)
        LVNode.addTerminal(self, "connection ID out", isInput=False)
        LVNode.addTerminal(self, "mode (standard)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (25000)", isInput=True)
        LVNode.addTerminal(self, "bytes to read", isInput=True)
        LVNode.addTerminal(self, "connection ID", isInput=True)
        self.attributes["type"] = "IrDA Read"
        self.attributes["genclass"] = "Function"


class IrdaWaitOnListener(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IrDA Wait On Listener")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "remote device ID", isInput=False)
        LVNode.addTerminal(self, "remote LSAP-SEL", isInput=False)
        LVNode.addTerminal(self, "listener ID out", isInput=False)
        LVNode.addTerminal(self, "connection ID", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (wait forever: -1)", isInput=True)
        LVNode.addTerminal(self, "resolve remote address (T)", isInput=True)
        LVNode.addTerminal(self, "listener ID in", isInput=True)
        self.attributes["type"] = "IrDA Wait On Listener"
        self.attributes["genclass"] = "Function"


class IrdaWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IrDA Write")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "bytes written", isInput=False)
        LVNode.addTerminal(self, "connection ID out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (25000)", isInput=True)
        LVNode.addTerminal(self, "data in", isInput=True)
        LVNode.addTerminal(self, "connection ID", isInput=True)
        self.attributes["type"] = "IrDA Write"
        self.attributes["genclass"] = "Function"


class Isdebuggingactive(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IsDebuggingActive")
        LVNode.addTerminal(self, "debugging?", isInput=False)
        self.attributes["type"] = "IsDebuggingActive"
        self.attributes["genclass"] = "Function"


class IviDeleteSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IVI Delete Session")
        LVNode.addTerminal(self, "IVI session", isInput=True)
        self.attributes["type"] = "IVI Delete Session"
        self.attributes["genclass"] = "Function"


class IviNewSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "IVI New Session")
        LVNode.addTerminal(self, "IVI session", isInput=False)
        LVNode.addTerminal(self, "IVI session handle", isInput=True)
        LVNode.addTerminal(self, "resource name ("")", isInput=True)
        LVNode.addTerminal(self, "IVI session (for class)", isInput=True)
        self.attributes["type"] = "IVI New Session"
        self.attributes["genclass"] = "Function"


class JoinNumbers(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Join Numbers")
        LVNode.addTerminal(self, "(hi.lo)", isInput=False)
        LVNode.addTerminal(self, "lo", isInput=True)
        LVNode.addTerminal(self, "hi", isInput=True)
        self.attributes["type"] = "Join Numbers"
        self.attributes["genclass"] = "Function"


class LeakVariantValueReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Leak Variant Value Reference")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "variant value ref out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "variant value ref in", isInput=True)
        self.attributes["type"] = "Leak Variant Value Reference"
        self.attributes["genclass"] = "Function"


class LessOrEqualTo0(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Less Or Equal To 0?")
        LVNode.addTerminal(self, "x <= 0?", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Less Or Equal To 0?"
        self.attributes["genclass"] = "Function"


class LessOrEqual(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Less Or Equal?")
        LVNode.addTerminal(self, "x <= y?", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Less Or Equal?"
        self.attributes["genclass"] = "Function"


class LessThan0(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Less Than 0?")
        LVNode.addTerminal(self, "x < 0?", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Less Than 0?"
        self.attributes["genclass"] = "Function"


class Less(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Less?")
        LVNode.addTerminal(self, "x < y?", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Less?"
        self.attributes["genclass"] = "Function"


class LexicalClass(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Lexical Class")
        LVNode.addTerminal(self, "class number", isInput=False)
        LVNode.addTerminal(self, "char", isInput=True)
        self.attributes["type"] = "Lexical Class"
        self.attributes["genclass"] = "Function"


class ListDirectory(LVNode):
    def __init__(self):
        LVNode.__init__(self, "List Directory")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "folder names", isInput=False)
        LVNode.addTerminal(self, "file names", isInput=False)
        LVNode.addTerminal(self, "dup folder path", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "datalog type", isInput=True)
        LVNode.addTerminal(self, "pattern", isInput=True)
        LVNode.addTerminal(self, "folder path", isInput=True)
        self.attributes["type"] = "List Directory"
        self.attributes["genclass"] = "Function"


class ListFolder(LVNode):
    def __init__(self):
        LVNode.__init__(self, "List Folder")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "folder names", isInput=False)
        LVNode.addTerminal(self, "filenames", isInput=False)
        LVNode.addTerminal(self, "path out", isInput=False)
        LVNode.addTerminal(self, "datalog type", isInput=True)
        LVNode.addTerminal(self, "pattern", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "path", isInput=True)
        self.attributes["type"] = "List Folder"
        self.attributes["genclass"] = "Function"


class LoadCertificatesIntoMemory(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Load Certificates Into Memory")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "certificates", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "format", isInput=True)
        LVNode.addTerminal(self, "path to certificates", isInput=True)
        self.attributes["type"] = "Load Certificates Into Memory"
        self.attributes["genclass"] = "Function"


class LoadPrivateKeyIntoMemory(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Load Private Key Into Memory")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "private key", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "password", isInput=True)
        LVNode.addTerminal(self, "format", isInput=True)
        LVNode.addTerminal(self, "path to private key", isInput=True)
        self.attributes["type"] = "Load Private Key Into Memory"
        self.attributes["genclass"] = "Function"


class LockRange(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Lock Range")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "dup refnum", isInput=False)
        LVNode.addTerminal(self, "count", isInput=True)
        LVNode.addTerminal(self, "set lock (F)", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "pos offset (0)", isInput=True)
        LVNode.addTerminal(self, "pos mode (0:2)", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Lock Range"
        self.attributes["genclass"] = "Function"


class LogarithmBase10(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Logarithm Base 10")
        LVNode.addTerminal(self, "log(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Logarithm Base 10"
        self.attributes["genclass"] = "Function"


class LogarithmBase2(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Logarithm Base 2")
        LVNode.addTerminal(self, "log2(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Logarithm Base 2"
        self.attributes["genclass"] = "Function"


class LogarithmBaseX(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Logarithm Base X")
        LVNode.addTerminal(self, "logx(y)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "y", isInput=True)
        self.attributes["type"] = "Logarithm Base X"
        self.attributes["genclass"] = "Function"


class LogicalShift(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Logical Shift")
        LVNode.addTerminal(self, "x << y", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "y", isInput=True)
        self.attributes["type"] = "Logical Shift"
        self.attributes["genclass"] = "Function"


class LookInMap(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Look In Map")
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "key not found?", isInput=False)
        LVNode.addTerminal(self, "default value", isInput=True)
        LVNode.addTerminal(self, "key", isInput=True)
        LVNode.addTerminal(self, "map", isInput=True)
        self.attributes["type"] = "Look In Map"
        self.attributes["genclass"] = "Function"


class LookupChannelProbe(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Lookup Channel Probe")
        LVNode.addTerminal(self, "refnum to monitor", isInput=True)
        LVNode.addTerminal(self, "probe type specifier", isInput=True)
        LVNode.addTerminal(self, "force create?", isInput=True)
        LVNode.addTerminal(self, "probe VI refnum", isInput=False)
        LVNode.addTerminal(self, "type mismatched?", isInput=False)
        self.attributes["type"] = "Lookup Channel Probe"
        self.attributes["genclass"] = "Function"


class LossyEnqueueElement(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Lossy Enqueue Element")
        LVNode.addTerminal(self, "queue", isInput=True)
        LVNode.addTerminal(self, "element", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "queue out", isInput=False)
        LVNode.addTerminal(self, "overflow element", isInput=False)
        LVNode.addTerminal(self, "overflow?", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Lossy Enqueue Element"
        self.attributes["genclass"] = "Function"


class MakeTlsConfigurationImmutable(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Make TLS Configuration Immutable")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "immutable TLS configuration", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "TLS configuration", isInput=True)
        self.attributes["type"] = "Make TLS Configuration Immutable"
        self.attributes["genclass"] = "Function"


class Makeaddr(LVNode):
    def __init__(self):
        LVNode.__init__(self, "MakeAddr")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "packed address", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "secondary address", isInput=True)
        LVNode.addTerminal(self, "primary address", isInput=True)
        self.attributes["type"] = "MakeAddr"
        self.attributes["genclass"] = "Function"


class MantissaExponent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Mantissa & Exponent")
        LVNode.addTerminal(self, "number", isInput=True)
        LVNode.addTerminal(self, "mantissa", isInput=False)
        LVNode.addTerminal(self, "exponent", isInput=False)
        self.attributes["type"] = "Mantissa & Exponent"
        self.attributes["genclass"] = "Function"


class MatchFirstString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Match First String")
        LVNode.addTerminal(self, "index", isInput=False)
        LVNode.addTerminal(self, "output string", isInput=False)
        LVNode.addTerminal(self, "string array", isInput=True)
        LVNode.addTerminal(self, "string", isInput=True)
        self.attributes["type"] = "Match First String"
        self.attributes["genclass"] = "Function"


class MatchPattern(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Match Pattern")
        LVNode.addTerminal(self, "string", isInput=True)
        LVNode.addTerminal(self, "regular expression", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "before substring", isInput=False)
        LVNode.addTerminal(self, "match substring", isInput=False)
        LVNode.addTerminal(self, "after substring", isInput=False)
        LVNode.addTerminal(self, "offset past match", isInput=False)
        self.attributes["type"] = "Match Pattern"
        self.attributes["genclass"] = "Function"


class MatchTrueFalseString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Match True/False String")
        LVNode.addTerminal(self, "selection", isInput=False)
        LVNode.addTerminal(self, "output string", isInput=False)
        LVNode.addTerminal(self, "false string", isInput=True)
        LVNode.addTerminal(self, "true string", isInput=True)
        LVNode.addTerminal(self, "string", isInput=True)
        self.attributes["type"] = "Match True/False String"
        self.attributes["genclass"] = "Function"


class MatrixSize(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Matrix Size")
        LVNode.addTerminal(self, "number of rows", isInput=True)
        LVNode.addTerminal(self, "number of columns", isInput=False)
        LVNode.addTerminal(self, "matrix", isInput=False)
        self.attributes["type"] = "Matrix Size"
        self.attributes["genclass"] = "Function"


class MaxMin(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Max & Min")
        LVNode.addTerminal(self, "min(x,y)", isInput=False)
        LVNode.addTerminal(self, "max(x,y)", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Max & Min"
        self.attributes["genclass"] = "Function"


class Move(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Move")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "cancelled", isInput=False)
        LVNode.addTerminal(self, "new path", isInput=False)
        LVNode.addTerminal(self, "prompt (Choose or enter target path for move)", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "overwrite (F)", isInput=True)
        LVNode.addTerminal(self, "target path (use dialog)", isInput=True)
        LVNode.addTerminal(self, "source path", isInput=True)
        self.attributes["type"] = "Move"
        self.attributes["genclass"] = "Function"


class MoveDeprecated(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Move (deprecated)")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "new path", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "target path", isInput=True)
        LVNode.addTerminal(self, "source path", isInput=True)
        self.attributes["type"] = "Move (deprecated)"
        self.attributes["genclass"] = "Function"


class Multiply(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Multiply")
        LVNode.addTerminal(self, "x*y", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Multiply"
        self.attributes["genclass"] = "Function"


class MultiplyWithErrorTerminals(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Multiply (with error terminals)")
        LVNode.addTerminal(self, "x*y", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        self.attributes["type"] = "Multiply (with error terminals)"
        self.attributes["genclass"] = "Function"


class MultiplyArrayElements(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Multiply Array Elements")
        LVNode.addTerminal(self, "product", isInput=False)
        LVNode.addTerminal(self, "numeric array", isInput=True)
        self.attributes["type"] = "Multiply Array Elements"
        self.attributes["genclass"] = "Function"


class NaturalLogarithm(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Natural Logarithm")
        LVNode.addTerminal(self, "ln(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Natural Logarithm"
        self.attributes["genclass"] = "Function"


class NaturalLogarithmArg1(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Natural Logarithm (Arg +1)")
        LVNode.addTerminal(self, "ln(x+1)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Natural Logarithm (Arg +1)"
        self.attributes["genclass"] = "Function"


class Negate(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Negate")
        LVNode.addTerminal(self, "-x", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Negate"
        self.attributes["genclass"] = "Function"


class NewDataValueReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "New Data Value Reference")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "data value reference", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "data value", isInput=True)
        self.attributes["type"] = "New Data Value Reference"
        self.attributes["genclass"] = "Function"


class NewDirectory(LVNode):
    def __init__(self):
        LVNode.__init__(self, "New Directory")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "dup directory path", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "permissions", isInput=True)
        LVNode.addTerminal(self, "group", isInput=True)
        LVNode.addTerminal(self, "directory path", isInput=True)
        self.attributes["type"] = "New Directory"
        self.attributes["genclass"] = "Function"


class NewFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "New File")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "refnum", isInput=False)
        LVNode.addTerminal(self, "datalog type", isInput=True)
        LVNode.addTerminal(self, "overwrite (F)", isInput=True)
        LVNode.addTerminal(self, "permissions", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "deny mode (2)", isInput=True)
        LVNode.addTerminal(self, "group", isInput=True)
        LVNode.addTerminal(self, "file path", isInput=True)
        self.attributes["type"] = "New File"
        self.attributes["genclass"] = "Function"


class NewTlsConfiguration(LVNode):
    def __init__(self):
        LVNode.__init__(self, "New TLS Configuration")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "TLS configuration out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "load OS trusted CAs?", isInput=True)
        self.attributes["type"] = "New TLS Configuration"
        self.attributes["genclass"] = "Function"


class NewVi(LVNode):
    def __init__(self):
        LVNode.__init__(self, "New VI")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "vi refnum", isInput=False)
        LVNode.addTerminal(self, "type specifier VI Refnum (for type only)", isInput=True)
        LVNode.addTerminal(self, "password", isInput=True)
        LVNode.addTerminal(self, "not connected", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "vi type (standard vi)", isInput=True)
        LVNode.addTerminal(self, "template", isInput=True)
        LVNode.addTerminal(self, "application refnum", isInput=True)
        self.attributes["type"] = "New VI"
        self.attributes["genclass"] = "Function"


class NewViObject(LVNode):
    def __init__(self):
        LVNode.__init__(self, "New VI Object")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "object refnum", isInput=False)
        LVNode.addTerminal(self, "bounds", isInput=True)
        LVNode.addTerminal(self, "auto wire? (F)", isInput=True)
        LVNode.addTerminal(self, "path", isInput=True)
        LVNode.addTerminal(self, "vi object class", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "position/next to", isInput=True)
        LVNode.addTerminal(self, "style", isInput=True)
        LVNode.addTerminal(self, "owner refnum", isInput=True)
        self.attributes["type"] = "New VI Object"
        self.attributes["genclass"] = "Function"


class Not(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Not")
        LVNode.addTerminal(self, ".not. x?", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Not"
        self.attributes["genclass"] = "Function"


class NotANumberPathRefnum(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Not A Number/Path/Refnum?")
        LVNode.addTerminal(self, "NaN/Path/Refnum?", isInput=False)
        LVNode.addTerminal(self, "number/path/refnum", isInput=True)
        self.attributes["type"] = "Not A Number/Path/Refnum?"
        self.attributes["genclass"] = "Function"


class NotAnd(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Not And")
        LVNode.addTerminal(self, ".not. (x .and. y)?", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Not And"
        self.attributes["genclass"] = "Function"


class NotEqualTo0(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Not Equal To 0?")
        LVNode.addTerminal(self, "x != 0?", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Not Equal To 0?"
        self.attributes["genclass"] = "Function"


class NotEqual(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Not Equal?")
        LVNode.addTerminal(self, "x != y?", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Not Equal?"
        self.attributes["genclass"] = "Function"


class NotExclusiveOr(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Not Exclusive Or")
        LVNode.addTerminal(self, ".not. (x .xor. y)?", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Not Exclusive Or"
        self.attributes["genclass"] = "Function"


class NotOr(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Not Or")
        LVNode.addTerminal(self, ".not. (x .or. y)?", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Not Or"
        self.attributes["genclass"] = "Function"


class NumberOfCacheLevels(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Number of Cache Levels")
        LVNode.addTerminal(self, "# of cache levels", isInput=False)
        self.attributes["type"] = "Number of Cache Levels"
        self.attributes["genclass"] = "Function"


class NumberToBooleanArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Number To Boolean Array")
        LVNode.addTerminal(self, "Boolean array", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "Number To Boolean Array"
        self.attributes["genclass"] = "Function"


class NumberToDecimalString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Number To Decimal String")
        LVNode.addTerminal(self, "decimal integer string", isInput=False)
        LVNode.addTerminal(self, "width (-)", isInput=True)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "Number To Decimal String"
        self.attributes["genclass"] = "Function"


class NumberToEngineeringString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Number To Engineering String")
        LVNode.addTerminal(self, "Engineering string", isInput=False)
        LVNode.addTerminal(self, "use system decimal point (T)", isInput=True)
        LVNode.addTerminal(self, "precision (6)", isInput=True)
        LVNode.addTerminal(self, "width (-)", isInput=True)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "Number To Engineering String"
        self.attributes["genclass"] = "Function"


class NumberToExponentialString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Number To Exponential String")
        LVNode.addTerminal(self, "E-format string", isInput=False)
        LVNode.addTerminal(self, "use system decimal point (T)", isInput=True)
        LVNode.addTerminal(self, "precision (6)", isInput=True)
        LVNode.addTerminal(self, "width (-)", isInput=True)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "Number To Exponential String"
        self.attributes["genclass"] = "Function"


class NumberToFractionalString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Number To Fractional String")
        LVNode.addTerminal(self, "F-format string", isInput=False)
        LVNode.addTerminal(self, "use system decimal point (T)", isInput=True)
        LVNode.addTerminal(self, "precision (6)", isInput=True)
        LVNode.addTerminal(self, "width (-)", isInput=True)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "Number To Fractional String"
        self.attributes["genclass"] = "Function"


class NumberToHexadecimalString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Number To Hexadecimal String")
        LVNode.addTerminal(self, "hex integer string", isInput=False)
        LVNode.addTerminal(self, "width (-)", isInput=True)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "Number To Hexadecimal String"
        self.attributes["genclass"] = "Function"


class NumberToOctalString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Number To Octal String")
        LVNode.addTerminal(self, "octal integer string", isInput=False)
        LVNode.addTerminal(self, "width (-)", isInput=True)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "Number To Octal String"
        self.attributes["genclass"] = "Function"


class ObtainNotifier(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Obtain Notifier")
        LVNode.addTerminal(self, "name (unnamed)", isInput=True)
        LVNode.addTerminal(self, "notification data type", isInput=True)
        LVNode.addTerminal(self, "create if not found? (T)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "notifier out", isInput=False)
        LVNode.addTerminal(self, "created new?", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Obtain Notifier"
        self.attributes["genclass"] = "Function"


class ObtainQueue(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Obtain Queue")
        LVNode.addTerminal(self, "name (unnamed)", isInput=True)
        LVNode.addTerminal(self, "element data type", isInput=True)
        LVNode.addTerminal(self, "create if not found? (T)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "max queue size (-1, unlimited)", isInput=True)
        LVNode.addTerminal(self, "queue out", isInput=False)
        LVNode.addTerminal(self, "created new?", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Obtain Queue"
        self.attributes["genclass"] = "Function"


class OctalDigit(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Octal Digit?")
        LVNode.addTerminal(self, "octal?", isInput=False)
        LVNode.addTerminal(self, "char", isInput=True)
        self.attributes["type"] = "Octal Digit?"
        self.attributes["genclass"] = "Function"


class OctalStringToNumber(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Octal String To Number")
        LVNode.addTerminal(self, "number", isInput=False)
        LVNode.addTerminal(self, "offset past number", isInput=False)
        LVNode.addTerminal(self, "default (0uL)", isInput=True)
        LVNode.addTerminal(self, "offset", isInput=True)
        LVNode.addTerminal(self, "string", isInput=True)
        self.attributes["type"] = "Octal String To Number"
        self.attributes["genclass"] = "Function"


class OldVisaOpen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Old VISA Open")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name", isInput=False)
        LVNode.addTerminal(self, "timeout (0)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "access mode", isInput=True)
        LVNode.addTerminal(self, "resource name ("")", isInput=True)
        LVNode.addTerminal(self, "VISA resource name (for class)", isInput=True)
        self.attributes["type"] = "Old VISA Open"
        self.attributes["genclass"] = "Function"


class OneButtonDialog(LVNode):
    def __init__(self):
        LVNode.__init__(self, "One Button Dialog")
        LVNode.addTerminal(self, "true", isInput=False)
        LVNode.addTerminal(self, "button name (\"OK\")", isInput=True)
        LVNode.addTerminal(self, "message", isInput=True)
        self.attributes["type"] = "One Button Dialog"
        self.attributes["genclass"] = "Function"


class OpenApplicationReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open Application Reference")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "application reference", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "", isInput=True)
        LVNode.addTerminal(self, "port number or service name (3363)", isInput=True)
        LVNode.addTerminal(self, "machine name ("":  open local reference)", isInput=True)
        self.attributes["type"] = "Open Application Reference"
        self.attributes["genclass"] = "Function"


class OpenDevice(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open Device")
        LVNode.addTerminal(self, "err", isInput=False)
        LVNode.addTerminal(self, "device refnum", isInput=False)
        LVNode.addTerminal(self, "unit(0)", isInput=True)
        LVNode.addTerminal(self, "device name", isInput=True)
        self.attributes["type"] = "Open Device"
        self.attributes["genclass"] = "Function"


class OpenDynamicBitfileReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open Dynamic Bitfile Reference")
        LVNode.addTerminal(self, "Device address", isInput=True)
        LVNode.addTerminal(self, "Bitfile path", isInput=True)
        LVNode.addTerminal(self, "Run When Loaded", isInput=True)
        LVNode.addTerminal(self, "Error In", isInput=True)
        LVNode.addTerminal(self, "Type", isInput=True)
        LVNode.addTerminal(self, "Refnum", isInput=False)
        LVNode.addTerminal(self, "Error Out", isInput=False)
        self.attributes["type"] = "Open Dynamic Bitfile Reference"
        self.attributes["genclass"] = "Function"


class OpenFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open File")
        LVNode.addTerminal(self, "file path", isInput=True)
        LVNode.addTerminal(self, "open mode (0)", isInput=True)
        LVNode.addTerminal(self, "deny mode (2)", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "datalog type", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Open File"
        self.attributes["genclass"] = "Function"


class OpenMatlabSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open MATLAB Session")
        LVNode.addTerminal(self, "release name", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "session out", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Open MATLAB Session"
        self.attributes["genclass"] = "Function"


class OpenPythonSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open Python Session")
        LVNode.addTerminal(self, "python version", isInput=True)
        LVNode.addTerminal(self, "python path", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "session out", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Open Python Session"
        self.attributes["genclass"] = "Function"


class OpenViObjectReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open VI Object Reference")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "object refnum", isInput=False)
        LVNode.addTerminal(self, "vi object class", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "name/order", isInput=True)
        LVNode.addTerminal(self, "owner refnum", isInput=True)
        self.attributes["type"] = "Open VI Object Reference"
        self.attributes["genclass"] = "Function"
class OpenViReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open VI Reference")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "vi reference", isInput=False)
        LVNode.addTerminal(self, "password ("")", isInput=True)
        LVNode.addTerminal(self, "type specifier VI Refnum (for type only)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "options", isInput=True)
        LVNode.addTerminal(self, "vi path", isInput=True)
        LVNode.addTerminal(self, "application reference (local)", isInput=True)
        self.attributes["type"] = "Open VI Reference"
        self.attributes["genclass"] = "Function"


class OpenCreateReplaceDatalog(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open/Create/Replace Datalog")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "cancelled", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "record type", isInput=True)
        LVNode.addTerminal(self, "prompt", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "access (0:read/write)", isInput=True)
        LVNode.addTerminal(self, "operation (0:open)", isInput=True)
        LVNode.addTerminal(self, "datalog path (use dialog)", isInput=True)
        self.attributes["type"] = "Open/Create/Replace Datalog"
        self.attributes["genclass"] = "Function"


class OpenCreateReplaceFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Open/Create/Replace File")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "cancelled", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "disable buffering (F)", isInput=True)
        LVNode.addTerminal(self, "prompt", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "access (0:read/write)", isInput=True)
        LVNode.addTerminal(self, "operation (0:open)", isInput=True)
        LVNode.addTerminal(self, "file path (use dialog)", isInput=True)
        self.attributes["type"] = "Open/Create/Replace File"
        self.attributes["genclass"] = "Function"


class Or(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Or")
        LVNode.addTerminal(self, "x .or. y?", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Or"
        self.attributes["genclass"] = "Function"


class OrArrayElements(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Or Array Elements")
        LVNode.addTerminal(self, "logical OR", isInput=False)
        LVNode.addTerminal(self, "Boolean array", isInput=True)
        self.attributes["type"] = "Or Array Elements"
        self.attributes["genclass"] = "Function"


class PackageMatrix(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Package Matrix")
        LVNode.addTerminal(self, "matrix", isInput=False)
        LVNode.addTerminal(self, "array", isInput=True)
        LVNode.addTerminal(self, "matrix", isInput=True)
        self.attributes["type"] = "Package Matrix"
        self.attributes["genclass"] = "Function"


class Passcontrol(LVNode):
    def __init__(self):
        LVNode.__init__(self, "PassControl")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "address", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "PassControl"
        self.attributes["genclass"] = "Function"


class PathToArrayOfStrings(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Path to Array of Strings")
        LVNode.addTerminal(self, "path", isInput=True)
        LVNode.addTerminal(self, "relative", isInput=False)
        LVNode.addTerminal(self, "array of strings", isInput=False)
        self.attributes["type"] = "Path to Array of Strings"
        self.attributes["genclass"] = "Function"


class PathToString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Path To String")
        LVNode.addTerminal(self, "string", isInput=False)
        LVNode.addTerminal(self, "path", isInput=True)
        self.attributes["type"] = "Path To String"
        self.attributes["genclass"] = "Function"


class PathType(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Path Type")
        LVNode.addTerminal(self, "type", isInput=False)
        LVNode.addTerminal(self, "path", isInput=True)
        self.attributes["type"] = "Path Type"
        self.attributes["genclass"] = "Function"


class PickLine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Pick Line")
        LVNode.addTerminal(self, "output string", isInput=False)
        LVNode.addTerminal(self, "line index", isInput=True)
        LVNode.addTerminal(self, "multi-line string", isInput=True)
        LVNode.addTerminal(self, "string ("")", isInput=True)
        self.attributes["type"] = "Pick Line"
        self.attributes["genclass"] = "Function"


class PolarToComplex(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Polar To Complex")
        LVNode.addTerminal(self, "r * e^(i*theta)", isInput=False)
        LVNode.addTerminal(self, "theta", isInput=True)
        LVNode.addTerminal(self, "r", isInput=True)
        self.attributes["type"] = "Polar To Complex"
        self.attributes["genclass"] = "Function"


class PolarToReIm(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Polar To Re/Im")
        LVNode.addTerminal(self, "y", isInput=False)
        LVNode.addTerminal(self, "x", isInput=False)
        LVNode.addTerminal(self, "theta", isInput=True)
        LVNode.addTerminal(self, "r", isInput=True)
        self.attributes["type"] = "Polar To Re/Im"
        self.attributes["genclass"] = "Function"


class PowerOf10(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Power Of 10")
        LVNode.addTerminal(self, "10^x", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Power Of 10"
        self.attributes["genclass"] = "Function"


class PowerOf2(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Power Of 2")
        LVNode.addTerminal(self, "2^x", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Power Of 2"
        self.attributes["genclass"] = "Function"


class PowerOfX(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Power Of X")
        LVNode.addTerminal(self, "x^y", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "y", isInput=True)
        self.attributes["type"] = "Power Of X"
        self.attributes["genclass"] = "Function"


class Ppoll(LVNode):
    def __init__(self):
        LVNode.__init__(self, "PPoll")
        LVNode.addTerminal(self, "bus", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "parallel poll byte", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "PPoll"
        self.attributes["genclass"] = "Function"


class Ppollconfig(LVNode):
    def __init__(self):
        LVNode.__init__(self, "PPollConfig")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "sense", isInput=True)
        LVNode.addTerminal(self, "dataline", isInput=True)
        LVNode.addTerminal(self, "address", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "PPollConfig"
        self.attributes["genclass"] = "Function"


class Ppollunconfig(LVNode):
    def __init__(self):
        LVNode.__init__(self, "PPollUnconfig")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "address list", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "PPollUnconfig"
        self.attributes["genclass"] = "Function"


class PreallocatedReadFromBinaryFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Preallocated Read from Binary File")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "num elements read", isInput=False)
        LVNode.addTerminal(self, "data out", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "byte order (0:big-endian, network order)", isInput=True)
        LVNode.addTerminal(self, "data in", isInput=True)
        LVNode.addTerminal(self, "refnum in", isInput=True)
        self.attributes["type"] = "Preallocated Read from Binary File"
        self.attributes["genclass"] = "Function"


class PreserveRunTimeClass(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Preserve Run-Time Class")
        LVNode.addTerminal(self, "object out", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "target object", isInput=True)
        LVNode.addTerminal(self, "object in", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        self.attributes["type"] = "Preserve Run-Time Class"
        self.attributes["genclass"] = "Function"


class PreviewQueueElement(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Preview Queue Element")
        LVNode.addTerminal(self, "queue", isInput=True)
        LVNode.addTerminal(self, "timeout in ms (-1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "queue out", isInput=False)
        LVNode.addTerminal(self, "element", isInput=False)
        LVNode.addTerminal(self, "timed out?", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Preview Queue Element"
        self.attributes["genclass"] = "Function"


class Printable(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Printable?")
        LVNode.addTerminal(self, "printable ASCII?", isInput=False)
        LVNode.addTerminal(self, "char", isInput=True)
        self.attributes["type"] = "Printable?"
        self.attributes["genclass"] = "Function"


class QuitLabview(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Quit LabVIEW")
        LVNode.addTerminal(self, "quit? (T)", isInput=True)
        self.attributes["type"] = "Quit LabVIEW"
        self.attributes["genclass"] = "Function"


class QuotientRemainder(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Quotient & Remainder")
        LVNode.addTerminal(self, "floor(x/y)", isInput=False)
        LVNode.addTerminal(self, "x-y*floor(x/y)", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Quotient & Remainder"
        self.attributes["genclass"] = "Function"


class RandomNumber01(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Random Number (0-1)")
        LVNode.addTerminal(self, "number: 0 to 1", isInput=False)
        self.attributes["type"] = "Random Number (0-1)"
        self.attributes["genclass"] = "Function"


class Rcvrespmsg(LVNode):
    def __init__(self):
        LVNode.__init__(self, "RcvRespMsg")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "byte count", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "data string", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "count", isInput=True)
        LVNode.addTerminal(self, "mode", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "RcvRespMsg"
        self.attributes["genclass"] = "Function"


class ReAcceptTls(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Re-accept TLS")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "client certificate chain", isInput=False)
        LVNode.addTerminal(self, "TLS connection out", isInput=False)
        LVNode.addTerminal(self, "timeout ms", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "", isInput=True)
        LVNode.addTerminal(self, "CA certificates", isInput=True)
        LVNode.addTerminal(self, "TLS connection", isInput=True)
        self.attributes["type"] = "Re-accept TLS"
        self.attributes["genclass"] = "Function"


class ReImToComplex(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Re/Im To Complex")
        LVNode.addTerminal(self, "x + iy", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Re/Im To Complex"
        self.attributes["genclass"] = "Function"


class ReImToPolar(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Re/Im To Polar")
        LVNode.addTerminal(self, "theta", isInput=False)
        LVNode.addTerminal(self, "r", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Re/Im To Polar"
        self.attributes["genclass"] = "Function"


class ReadDatalog(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Read Datalog")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "record(s)", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "count (1)", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Read Datalog"
        self.attributes["genclass"] = "Function"


class ReadDevice(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Read Device")
        LVNode.addTerminal(self, "new offset", isInput=False)
        LVNode.addTerminal(self, "string", isInput=False)
        LVNode.addTerminal(self, "err", isInput=False)
        LVNode.addTerminal(self, "spc reset (F)", isInput=True)
        LVNode.addTerminal(self, "misc (-)", isInput=True)
        LVNode.addTerminal(self, "async (T)", isInput=True)
        LVNode.addTerminal(self, "pos offset (-)", isInput=True)
        LVNode.addTerminal(self, "pos mode (-)", isInput=True)
        LVNode.addTerminal(self, "count", isInput=True)
        LVNode.addTerminal(self, "device refnum", isInput=True)
        self.attributes["type"] = "Read Device"
        self.attributes["genclass"] = "Function"


class ReadFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Read File")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "offset", isInput=False)
        LVNode.addTerminal(self, "data", isInput=False)
        LVNode.addTerminal(self, "dup refnum", isInput=False)
        LVNode.addTerminal(self, "byte stream type", isInput=True)
        LVNode.addTerminal(self, "convert eol (F)", isInput=True)
        LVNode.addTerminal(self, "count", isInput=True)
        LVNode.addTerminal(self, "line mode (F)", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "pos offset (0)", isInput=True)
        LVNode.addTerminal(self, "pos mode (0:2)", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Read File"
        self.attributes["genclass"] = "Function"


class ReadFromBinaryFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Read from Binary File")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "cancelled", isInput=False)
        LVNode.addTerminal(self, "data", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "data type", isInput=True)
        LVNode.addTerminal(self, "prompt (Open existing file)", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "byte order (0:big-endian, network order)", isInput=True)
        LVNode.addTerminal(self, "count", isInput=True)
        LVNode.addTerminal(self, "file (use dialog)", isInput=True)
        self.attributes["type"] = "Read from Binary File"
        self.attributes["genclass"] = "Function"


class ReadFromTextFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Read from Text File")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "cancelled", isInput=False)
        LVNode.addTerminal(self, "text", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "prompt (Open existing file)", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "count", isInput=True)
        LVNode.addTerminal(self, "file (use dialog)", isInput=True)
        self.attributes["type"] = "Read from Text File"
        self.attributes["genclass"] = "Function"


class ReadMapMaxMinKeys(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Read Map Max & Min Keys")
        LVNode.addTerminal(self, "minimum", isInput=False)
        LVNode.addTerminal(self, "maximum", isInput=False)
        LVNode.addTerminal(self, "map", isInput=True)
        self.attributes["type"] = "Read Map Max & Min Keys"
        self.attributes["genclass"] = "Function"


class ReadSetMaxMin(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Read Set Max & Min")
        LVNode.addTerminal(self, "minimum", isInput=False)
        LVNode.addTerminal(self, "maximum", isInput=False)
        LVNode.addTerminal(self, "set", isInput=True)
        self.attributes["type"] = "Read Set Max & Min"
        self.attributes["genclass"] = "Function"


class Readstatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "ReadStatus")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "serial poll response", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "address", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "ReadStatus"
        self.attributes["genclass"] = "Function"


class Receive(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Receive")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "byte count", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "data string", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "count", isInput=True)
        LVNode.addTerminal(self, "mode", isInput=True)
        LVNode.addTerminal(self, "address", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "Receive"
        self.attributes["genclass"] = "Function"


class Receivesetup(LVNode):
    def __init__(self):
        LVNode.__init__(self, "ReceiveSetup")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "address", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "ReceiveSetup"
        self.attributes["genclass"] = "Function"


class Reciprocal(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Reciprocal")
        LVNode.addTerminal(self, "1/x", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Reciprocal"
        self.attributes["genclass"] = "Function"


class RefnumToPath(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Refnum to Path")
        LVNode.addTerminal(self, "path", isInput=False)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Refnum to Path"
        self.attributes["genclass"] = "Function"


class RefnumToSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Refnum to Session")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "Session", isInput=False)
        LVNode.addTerminal(self, "error in(no error)", isInput=True)
        LVNode.addTerminal(self, "Refnum", isInput=True)
        self.attributes["type"] = "Refnum to Session"
        self.attributes["genclass"] = "Function"


class RegisterSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Register Session")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "duplicate refnum", isInput=False)
        LVNode.addTerminal(self, "cleanup mode (default to class = 0)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "session", isInput=True)
        LVNode.addTerminal(self, "resource name", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Register Session"
        self.attributes["genclass"] = "Function"


class ReleaseNotifier(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Release Notifier")
        LVNode.addTerminal(self, "notifier", isInput=True)
        LVNode.addTerminal(self, "force destroy? (F)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "notifier name", isInput=False)
        LVNode.addTerminal(self, "last notification", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Release Notifier"
        self.attributes["genclass"] = "Function"


class ReleaseQueue(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Release Queue")
        LVNode.addTerminal(self, "queue", isInput=True)
        LVNode.addTerminal(self, "force destroy? (F)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "queue name", isInput=False)
        LVNode.addTerminal(self, "remaining elements", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Release Queue"
        self.attributes["genclass"] = "Function"


class RemoveFixedPointOverflowStatus(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Remove Fixed-Point Overflow Status")
        LVNode.addTerminal(self, "overflow?", isInput=False)
        LVNode.addTerminal(self, "FXP with overflow removed", isInput=False)
        LVNode.addTerminal(self, "FXP", isInput=True)
        self.attributes["type"] = "Remove Fixed-Point Overflow Status"
        self.attributes["genclass"] = "Function"


class RemoveFromMap(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Remove From Map")
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "key not found?", isInput=False)
        LVNode.addTerminal(self, "map out", isInput=False)
        LVNode.addTerminal(self, "key", isInput=True)
        LVNode.addTerminal(self, "map in", isInput=True)
        self.attributes["type"] = "Remove From Map"
        self.attributes["genclass"] = "Function"


class RemoveFromSet(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Remove From Set")
        LVNode.addTerminal(self, "not included?", isInput=False)
        LVNode.addTerminal(self, "set out", isInput=False)
        LVNode.addTerminal(self, "element", isInput=True)
        LVNode.addTerminal(self, "set in", isInput=True)
        self.attributes["type"] = "Remove From Set"
        self.attributes["genclass"] = "Function"


class ReplaceSubstring(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Replace Substring")
        LVNode.addTerminal(self, "replaced substring", isInput=False)
        LVNode.addTerminal(self, "result string", isInput=False)
        LVNode.addTerminal(self, "length", isInput=True)
        LVNode.addTerminal(self, "offset", isInput=True)
        LVNode.addTerminal(self, "substring", isInput=True)
        LVNode.addTerminal(self, "string", isInput=True)
        self.attributes["type"] = "Replace Substring"
        self.attributes["genclass"] = "Function"


class RequestDeallocation(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Request Deallocation")
        LVNode.addTerminal(self, "flag", isInput=True)
        self.attributes["type"] = "Request Deallocation"
        self.attributes["genclass"] = "Function"


class Resetsys(LVNode):
    def __init__(self):
        LVNode.__init__(self, "ResetSys")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "address list", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "ResetSys"
        self.attributes["genclass"] = "Function"


class ResizeMatrix(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Resize Matrix")
        LVNode.addTerminal(self, "resized matrix", isInput=False)
        LVNode.addTerminal(self, "number of columns", isInput=True)
        LVNode.addTerminal(self, "number of rows", isInput=True)
        LVNode.addTerminal(self, "matrix", isInput=True)
        self.attributes["type"] = "Resize Matrix"
        self.attributes["genclass"] = "Function"


class ResourceIndex(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Resource Index")
        LVNode.addTerminal(self, "Index", isInput=False)
        LVNode.addTerminal(self, "Resource", isInput=True)
        self.attributes["type"] = "Resource Index"
        self.attributes["genclass"] = "Function"


class Reverse1dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Reverse 1D Array")
        LVNode.addTerminal(self, "reversed array", isInput=False)
        LVNode.addTerminal(self, "array", isInput=True)
        self.attributes["type"] = "Reverse 1D Array"
        self.attributes["genclass"] = "Function"


class ReverseString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Reverse String")
        LVNode.addTerminal(self, "reversed", isInput=False)
        LVNode.addTerminal(self, "string", isInput=True)
        self.attributes["type"] = "Reverse String"
        self.attributes["genclass"] = "Function"


class Rotate(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Rotate")
        LVNode.addTerminal(self, "x rotated left by y", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "y", isInput=True)
        self.attributes["type"] = "Rotate"
        self.attributes["genclass"] = "Function"


class Rotate1dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Rotate 1D Array")
        LVNode.addTerminal(self, "array (last n elements first)", isInput=False)
        LVNode.addTerminal(self, "array", isInput=True)
        LVNode.addTerminal(self, "n", isInput=True)
        self.attributes["type"] = "Rotate 1D Array"
        self.attributes["genclass"] = "Function"


class RotateLeftWithCarry(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Rotate Left With Carry")
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "msb carry out", isInput=False)
        LVNode.addTerminal(self, "value", isInput=True)
        LVNode.addTerminal(self, "carry", isInput=True)
        self.attributes["type"] = "Rotate Left With Carry"
        self.attributes["genclass"] = "Function"


class RotateRightWithCarry(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Rotate Right With Carry")
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "lsb carry out", isInput=False)
        LVNode.addTerminal(self, "value", isInput=True)
        LVNode.addTerminal(self, "carry", isInput=True)
        self.attributes["type"] = "Rotate Right With Carry"
        self.attributes["genclass"] = "Function"


class RotateString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Rotate String")
        LVNode.addTerminal(self, "first char last", isInput=False)
        LVNode.addTerminal(self, "string", isInput=True)
        self.attributes["type"] = "Rotate String"
        self.attributes["genclass"] = "Function"


class RoundToNearest(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Round To Nearest")
        LVNode.addTerminal(self, "nearest integer value", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "Round To Nearest"
        self.attributes["genclass"] = "Function"


class RoundTowardInfinity(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Round Toward +Infinity")
        LVNode.addTerminal(self, "ceil(x): smallest int >= x", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Round Toward +Infinity"
        self.attributes["genclass"] = "Function"


class RoundTowardInfinity(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Round Toward -Infinity")
        LVNode.addTerminal(self, "floor(x): largest int <= x", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Round Toward -Infinity"
        self.attributes["genclass"] = "Function"


class RtFifoCreate(LVNode):
    def __init__(self):
        LVNode.__init__(self, "RT FIFO Create")
        LVNode.addTerminal(self, "name (unnamed)", isInput=True)
        LVNode.addTerminal(self, "type", isInput=True)
        LVNode.addTerminal(self, "create if not found? (T)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "size (10)", isInput=True)
        LVNode.addTerminal(self, "datapoints in waveform (1)", isInput=True)
        LVNode.addTerminal(self, "elements in array (1)", isInput=True)
        LVNode.addTerminal(self, "r/w modes (polling,polling)", isInput=True)
        LVNode.addTerminal(self, "rt fifo", isInput=False)
        LVNode.addTerminal(self, "created new?", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "RT FIFO Create"
        self.attributes["genclass"] = "Function"


class RtFifoDelete(LVNode):
    def __init__(self):
        LVNode.__init__(self, "RT FIFO Delete")
        LVNode.addTerminal(self, "rt fifo", isInput=True)
        LVNode.addTerminal(self, "force destroy? (F)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "RT FIFO Delete"
        self.attributes["genclass"] = "Function"


class RtFifoRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "RT FIFO Read")
        LVNode.addTerminal(self, "rt fifo", isInput=True)
        LVNode.addTerminal(self, "element", isInput=True)
        LVNode.addTerminal(self, "timeout in ms (0)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "# elements", isInput=False)
        LVNode.addTerminal(self, "rt fifo out", isInput=False)
        LVNode.addTerminal(self, "element out", isInput=False)
        LVNode.addTerminal(self, "empty?", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "RT FIFO Read"
        self.attributes["genclass"] = "Function"


class RtFifoWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "RT FIFO Write")
        LVNode.addTerminal(self, "rt fifo", isInput=True)
        LVNode.addTerminal(self, "element", isInput=True)
        LVNode.addTerminal(self, "timeout in ms (0)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "overwrite on timeout (T)", isInput=True)
        LVNode.addTerminal(self, "# elements", isInput=False)
        LVNode.addTerminal(self, "rt fifo out", isInput=False)
        LVNode.addTerminal(self, "timed out?", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "RT FIFO Write"
        self.attributes["genclass"] = "Function"


class ScaleByPowerOf2(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Scale By Power Of 2")
        LVNode.addTerminal(self, "x*2^n", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "n", isInput=True)
        self.attributes["type"] = "Scale By Power Of 2"
        self.attributes["genclass"] = "Function"


class ScanStringForTokens(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Scan String For Tokens")
        LVNode.addTerminal(self, "token index", isInput=False)
        LVNode.addTerminal(self, "token string", isInput=False)
        LVNode.addTerminal(self, "offset past token", isInput=False)
        LVNode.addTerminal(self, "string out", isInput=False)
        LVNode.addTerminal(self, "use cached delim/oper data? (F)", isInput=True)
        LVNode.addTerminal(self, "allow empty tokens? (F)", isInput=True)
        LVNode.addTerminal(self, "delimiters (\s,\t,\r,\n)", isInput=True)
        LVNode.addTerminal(self, "operators (none)", isInput=True)
        LVNode.addTerminal(self, "offset", isInput=True)
        LVNode.addTerminal(self, "input string", isInput=True)
        self.attributes["type"] = "Scan String For Tokens"
        self.attributes["genclass"] = "Function"


class ScanValue(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Scan Value")
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "output string", isInput=False)
        LVNode.addTerminal(self, "default (0 dbl)", isInput=True)
        LVNode.addTerminal(self, "format string", isInput=True)
        LVNode.addTerminal(self, "string", isInput=True)
        self.attributes["type"] = "Scan Value"
        self.attributes["genclass"] = "Function"


class Search1dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Search 1D Array")
        LVNode.addTerminal(self, "index of element", isInput=False)
        LVNode.addTerminal(self, "start index (0)", isInput=True)
        LVNode.addTerminal(self, "element", isInput=True)
        LVNode.addTerminal(self, "1D array", isInput=True)
        self.attributes["type"] = "Search 1D Array"
        self.attributes["genclass"] = "Function"


class SearchAndReplaceString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Search and Replace String")
        LVNode.addTerminal(self, "input string", isInput=True)
        LVNode.addTerminal(self, "replace all?", isInput=True)
        LVNode.addTerminal(self, "case sensitive?", isInput=True)
        LVNode.addTerminal(self, "multiline?", isInput=True)
        LVNode.addTerminal(self, "result string", isInput=False)
        LVNode.addTerminal(self, "search string", isInput=True)
        LVNode.addTerminal(self, "replace string", isInput=True)
        LVNode.addTerminal(self, "number of replacements", isInput=False)
        LVNode.addTerminal(self, "offset", isInput=True)
        LVNode.addTerminal(self, "offset past replacement", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Search and Replace String"
        self.attributes["genclass"] = "Function"


class SearchVariableContainer(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Search Variable Container")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "refnum array out", isInput=False)
        LVNode.addTerminal(self, "container refnum out", isInput=False)
        LVNode.addTerminal(self, "access type", isInput=True)
        LVNode.addTerminal(self, "class", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "data type", isInput=True)
        LVNode.addTerminal(self, "regular expression", isInput=True)
        LVNode.addTerminal(self, "container refnum in", isInput=True)
        self.attributes["type"] = "Search Variable Container"
        self.attributes["genclass"] = "Function"


class SearchSplitString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Search/Split String")
        LVNode.addTerminal(self, "offset of match", isInput=False)
        LVNode.addTerminal(self, "match + rest of string", isInput=False)
        LVNode.addTerminal(self, "substring before match", isInput=False)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "search string/char (-)", isInput=True)
        LVNode.addTerminal(self, "string", isInput=True)
        self.attributes["type"] = "Search/Split String"
        self.attributes["genclass"] = "Function"


class Secant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Secant")
        LVNode.addTerminal(self, "1/cos(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Secant"
        self.attributes["genclass"] = "Function"


class SecondsToDateTime(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Seconds To Date/Time")
        LVNode.addTerminal(self, "date time rec", isInput=False)
        LVNode.addTerminal(self, "to UTC (F)", isInput=True)
        LVNode.addTerminal(self, "time stamp (now)", isInput=True)
        self.attributes["type"] = "Seconds To Date/Time"
        self.attributes["genclass"] = "Function"


class Seek(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Seek")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "offset", isInput=False)
        LVNode.addTerminal(self, "dup refnum", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "pos offset (0)", isInput=True)
        LVNode.addTerminal(self, "pos mode (0:2)", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Seek"
        self.attributes["genclass"] = "Function"


class Select(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Select")
        LVNode.addTerminal(self, "s? t:f", isInput=False)
        LVNode.addTerminal(self, "f", isInput=True)
        LVNode.addTerminal(self, "s", isInput=True)
        LVNode.addTerminal(self, "t", isInput=True)
        self.attributes["type"] = "Select"
        self.attributes["genclass"] = "Function"


class Send(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Send")
        LVNode.addTerminal(self, "bus", isInput=True)
        LVNode.addTerminal(self, "address", isInput=True)
        LVNode.addTerminal(self, "mode", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "data string", isInput=True)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "byte count", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Send"
        self.attributes["genclass"] = "Function"


class SendNotification(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Send Notification")
        LVNode.addTerminal(self, "notifier", isInput=True)
        LVNode.addTerminal(self, "notification", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "notifier out", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Send Notification"
        self.attributes["genclass"] = "Function"


class Sendcmds(LVNode):
    def __init__(self):
        LVNode.__init__(self, "SendCmds")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "byte count", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "command string", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "SendCmds"
        self.attributes["genclass"] = "Function"


class Senddatabytes(LVNode):
    def __init__(self):
        LVNode.__init__(self, "SendDataBytes")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "byte count", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "data string", isInput=True)
        LVNode.addTerminal(self, "mode", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "SendDataBytes"
        self.attributes["genclass"] = "Function"


class Sendifc(LVNode):
    def __init__(self):
        LVNode.__init__(self, "SendIFC")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "SendIFC"
        self.attributes["genclass"] = "Function"


class Sendlist(LVNode):
    def __init__(self):
        LVNode.__init__(self, "SendList")
        LVNode.addTerminal(self, "bus", isInput=True)
        LVNode.addTerminal(self, "address list", isInput=True)
        LVNode.addTerminal(self, "mode", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "data string", isInput=True)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "byte count", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "SendList"
        self.attributes["genclass"] = "Function"


class Sendllo(LVNode):
    def __init__(self):
        LVNode.__init__(self, "SendLLO")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "SendLLO"
        self.attributes["genclass"] = "Function"


class Sendsetup(LVNode):
    def __init__(self):
        LVNode.__init__(self, "SendSetup")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "address list", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "SendSetup"
        self.attributes["genclass"] = "Function"


class SessionToRefnum(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Session to Refnum")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "Refnum", isInput=False)
        LVNode.addTerminal(self, "error in(no error)", isInput=True)
        LVNode.addTerminal(self, "Session", isInput=True)
        LVNode.addTerminal(self, "Class Type", isInput=True)
        self.attributes["type"] = "Session to Refnum"
        self.attributes["genclass"] = "Function"


class SetControlValuesByIndex(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Control Values by Index")
        LVNode.addTerminal(self, "VI Refnum", isInput=True)
        LVNode.addTerminal(self, "control indexes", isInput=True)
        LVNode.addTerminal(self, "data values", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Set Control Values by Index"
        self.attributes["genclass"] = "Function"


class SetDatalogPosition(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Datalog Position")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "from (0:start)", isInput=True)
        LVNode.addTerminal(self, "offset (in records) (0)", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Set Datalog Position"
        self.attributes["genclass"] = "Function"


class SetFilePosition(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set File Position")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "from (0:start)", isInput=True)
        LVNode.addTerminal(self, "offset (in bytes) (0)", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Set File Position"
        self.attributes["genclass"] = "Function"


class SetFileSize(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set File Size")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "size (in bytes)", isInput=True)
        LVNode.addTerminal(self, "file", isInput=True)
        self.attributes["type"] = "Set File Size"
        self.attributes["genclass"] = "Function"


class SetMenuItemInfo(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Menu Item Info")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "menu reference out", isInput=False)
        LVNode.addTerminal(self, "short cut", isInput=True)
        LVNode.addTerminal(self, "checked", isInput=True)
        LVNode.addTerminal(self, "item tag", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "enabled", isInput=True)
        LVNode.addTerminal(self, "item name", isInput=True)
        LVNode.addTerminal(self, "menu reference", isInput=True)
        self.attributes["type"] = "Set Menu Item Info"
        self.attributes["genclass"] = "Function"


class SetNumberOfRecords(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Number of Records")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "# of records", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Set Number of Records"
        self.attributes["genclass"] = "Function"


class SetOccurrence(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Occurrence")
        LVNode.addTerminal(self, "occurrence", isInput=True)
        self.attributes["type"] = "Set Occurrence"
        self.attributes["genclass"] = "Function"


class SetPermissions(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Permissions")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "path out", isInput=False)
        LVNode.addTerminal(self, "permissions", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "new group", isInput=True)
        LVNode.addTerminal(self, "new owner", isInput=True)
        LVNode.addTerminal(self, "path", isInput=True)
        self.attributes["type"] = "Set Permissions"
        self.attributes["genclass"] = "Function"


class SetTypeAndCreator(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Type and Creator")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "path out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "creator (no change)", isInput=True)
        LVNode.addTerminal(self, "type (no change)", isInput=True)
        LVNode.addTerminal(self, "path", isInput=True)
        self.attributes["type"] = "Set Type and Creator"
        self.attributes["genclass"] = "Function"


class SetVariantAttribute(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Variant Attribute")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "replaced", isInput=False)
        LVNode.addTerminal(self, "Variant out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "value", isInput=True)
        LVNode.addTerminal(self, "name", isInput=True)
        LVNode.addTerminal(self, "Variant", isInput=True)
        self.attributes["type"] = "Set Variant Attribute"
        self.attributes["genclass"] = "Function"


class SetWaveformAttribute(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Set Waveform Attribute")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "replaced", isInput=False)
        LVNode.addTerminal(self, "waveform out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "value", isInput=True)
        LVNode.addTerminal(self, "name", isInput=True)
        LVNode.addTerminal(self, "waveform", isInput=True)
        self.attributes["type"] = "Set Waveform Attribute"
        self.attributes["genclass"] = "Function"


class Setrwls(LVNode):
    def __init__(self):
        LVNode.__init__(self, "SetRWLS")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "address list", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "SetRWLS"
        self.attributes["genclass"] = "Function"
class Settimeout(LVNode):
    def __init__(self):
        LVNode.__init__(self, "SetTimeOut")
        LVNode.addTerminal(self, "previous timeout", isInput=False)
        LVNode.addTerminal(self, "new timeout (10000)", isInput=True)
        self.attributes["type"] = "SetTimeOut"
        self.attributes["genclass"] = "Function"


class SharedVariableToString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Shared Variable to String")
        LVNode.addTerminal(self, "string", isInput=False)
        LVNode.addTerminal(self, "Shared Variable", isInput=True)
        self.attributes["type"] = "Shared Variable to String"
        self.attributes["genclass"] = "Function"


class Sign(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Sign")
        LVNode.addTerminal(self, "-1, 0, 1", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "Sign"
        self.attributes["genclass"] = "Function"


class Sinc(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Sinc")
        LVNode.addTerminal(self, "sin(x)/x", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Sinc"
        self.attributes["genclass"] = "Function"


class Sine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Sine")
        LVNode.addTerminal(self, "sin(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Sine"
        self.attributes["genclass"] = "Function"


class SineCosine(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Sine & Cosine")
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "sin(x)", isInput=False)
        LVNode.addTerminal(self, "cos(x)", isInput=False)
        self.attributes["type"] = "Sine & Cosine"
        self.attributes["genclass"] = "Function"


class SizeHandle(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Size Handle")
        LVNode.addTerminal(self, "handle", isInput=False)
        LVNode.addTerminal(self, "error", isInput=False)
        LVNode.addTerminal(self, "handle (-)", isInput=True)
        LVNode.addTerminal(self, "size", isInput=True)
        self.attributes["type"] = "Size Handle"
        self.attributes["genclass"] = "Function"


class Sort1dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Sort 1D Array")
        LVNode.addTerminal(self, "sorted array", isInput=False)
        LVNode.addTerminal(self, "array", isInput=True)
        self.attributes["type"] = "Sort 1D Array"
        self.attributes["genclass"] = "Function"


class SortArrayOfString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Sort Array of String")
        LVNode.addTerminal(self, "sorted array", isInput=False)
        LVNode.addTerminal(self, "array", isInput=True)
        self.attributes["type"] = "Sort Array of String"
        self.attributes["genclass"] = "Function"


class Split1dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Split 1D Array")
        LVNode.addTerminal(self, "second subarray", isInput=False)
        LVNode.addTerminal(self, "first subarray", isInput=False)
        LVNode.addTerminal(self, "index", isInput=True)
        LVNode.addTerminal(self, "array", isInput=True)
        self.attributes["type"] = "Split 1D Array"
        self.attributes["genclass"] = "Function"


class SplitNumber(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Split Number")
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "hi(x)", isInput=False)
        LVNode.addTerminal(self, "lo(x)", isInput=False)
        self.attributes["type"] = "Split Number"
        self.attributes["genclass"] = "Function"


class SpreadsheetStringToArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Spreadsheet String To Array")
        LVNode.addTerminal(self, "array", isInput=False)
        LVNode.addTerminal(self, "delimiter (Tab)", isInput=True)
        LVNode.addTerminal(self, "array type (2D Dbl)", isInput=True)
        LVNode.addTerminal(self, "spreadsheet string", isInput=True)
        LVNode.addTerminal(self, "format string", isInput=True)
        self.attributes["type"] = "Spreadsheet String To Array"
        self.attributes["genclass"] = "Function"


class Square(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Square")
        LVNode.addTerminal(self, "x^2", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Square"
        self.attributes["genclass"] = "Function"


class SquareRoot(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Square Root")
        LVNode.addTerminal(self, "sqrt(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Square Root"
        self.attributes["genclass"] = "Function"


class StartTls(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Start TLS")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "server certificate chain", isInput=False)
        LVNode.addTerminal(self, "TLS connection", isInput=False)
        LVNode.addTerminal(self, "server certificate validation", isInput=True)
        LVNode.addTerminal(self, "timeout ms", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "server hostname", isInput=True)
        LVNode.addTerminal(self, "immutable TLS configuration", isInput=True)
        LVNode.addTerminal(self, "TCP connection", isInput=True)
        self.attributes["type"] = "Start TLS"
        self.attributes["genclass"] = "Function"


class Stop(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Stop")
        LVNode.addTerminal(self, "stop? (T)", isInput=True)
        self.attributes["type"] = "Stop"
        self.attributes["genclass"] = "Function"


class StringLength(LVNode):
    def __init__(self):
        LVNode.__init__(self, "String Length")
        LVNode.addTerminal(self, "length", isInput=False)
        LVNode.addTerminal(self, "string", isInput=True)
        self.attributes["type"] = "String Length"
        self.attributes["genclass"] = "Function"

class StringSubset(LVNode):
    def __init__(self):
        LVNode.__init__(self, "String Subset")
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "length (rest)", isInput=True)
        LVNode.addTerminal(self, "string", isInput=True)
        LVNode.addTerminal(self, "substring", isInput=False)
        self.attributes["type"] = "String Subset"
        self.attributes["genclass"] = "Function"


class StringToByteArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "String To Byte Array")
        LVNode.addTerminal(self, "unsigned byte array", isInput=False)
        LVNode.addTerminal(self, "string", isInput=True)
        self.attributes["type"] = "String To Byte Array"
        self.attributes["genclass"] = "Function"


class StringToIp(LVNode):
    def __init__(self):
        LVNode.__init__(self, "String To IP")
        LVNode.addTerminal(self, "net address", isInput=False)
        LVNode.addTerminal(self, "name", isInput=True)
        self.attributes["type"] = "String To IP"
        self.attributes["genclass"] = "Function"


class StringToPath(LVNode):
    def __init__(self):
        LVNode.__init__(self, "String To Path")
        LVNode.addTerminal(self, "path", isInput=False)
        LVNode.addTerminal(self, "string", isInput=True)
        self.attributes["type"] = "String To Path"
        self.attributes["genclass"] = "Function"


class StringToSharedVariable(LVNode):
    def __init__(self):
        LVNode.__init__(self, "String to Shared Variable")
        LVNode.addTerminal(self, "string", isInput=True)
        LVNode.addTerminal(self, "valid Shared Variable?", isInput=False)
        LVNode.addTerminal(self, "Shared Variable", isInput=False)
        self.attributes["type"] = "String to Shared Variable"
        self.attributes["genclass"] = "Function"


class StripPath(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Strip Path")
        LVNode.addTerminal(self, "path", isInput=True)
        LVNode.addTerminal(self, "stripped path", isInput=False)
        LVNode.addTerminal(self, "name", isInput=False)
        self.attributes["type"] = "Strip Path"
        self.attributes["genclass"] = "Function"


class Subtract(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Subtract")
        LVNode.addTerminal(self, "x-y", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Subtract"
        self.attributes["genclass"] = "Function"


class SubtractWithErrorTerminals(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Subtract (with error terminals)")
        LVNode.addTerminal(self, "x-y", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        self.attributes["type"] = "Subtract (with error terminals)"
        self.attributes["genclass"] = "Function"


class SwapBytes(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Swap Bytes")
        LVNode.addTerminal(self, "byte swapped", isInput=False)
        LVNode.addTerminal(self, "anything", isInput=True)
        self.attributes["type"] = "Swap Bytes"
        self.attributes["genclass"] = "Function"


class SwapValues(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Swap Values")
        LVNode.addTerminal(self, "y'", isInput=False)
        LVNode.addTerminal(self, "x'", isInput=False)
        LVNode.addTerminal(self, "y", isInput=True)
        LVNode.addTerminal(self, "?(T)", isInput=True)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Swap Values"
        self.attributes["genclass"] = "Function"


class SwapVectorElement(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Swap Vector Element")
        LVNode.addTerminal(self, "swapped element value", isInput=False)
        LVNode.addTerminal(self, "returned index", isInput=False)
        LVNode.addTerminal(self, "changed vector", isInput=False)
        LVNode.addTerminal(self, "element value", isInput=True)
        LVNode.addTerminal(self, "index", isInput=True)
        LVNode.addTerminal(self, "vector", isInput=True)
        self.attributes["type"] = "Swap Vector Element"
        self.attributes["genclass"] = "Function"


class SwapWords(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Swap Words")
        LVNode.addTerminal(self, "word swapped", isInput=False)
        LVNode.addTerminal(self, "anything", isInput=True)
        self.attributes["type"] = "Swap Words"
        self.attributes["genclass"] = "Function"


class Tangent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Tangent")
        LVNode.addTerminal(self, "tan(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        self.attributes["type"] = "Tangent"
        self.attributes["genclass"] = "Function"


class TcpCloseConnection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Close Connection")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "connection ID out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "abort (F)", isInput=True)
        LVNode.addTerminal(self, "connection ID", isInput=True)
        self.attributes["type"] = "TCP Close Connection"
        self.attributes["genclass"] = "Function"


class TcpCreateListener(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Create Listener")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "port", isInput=False)
        LVNode.addTerminal(self, "listener ID", isInput=False)
        LVNode.addTerminal(self, "net address", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (25000)", isInput=True)
        LVNode.addTerminal(self, "port", isInput=True)
        LVNode.addTerminal(self, "service name", isInput=True)
        self.attributes["type"] = "TCP Create Listener"
        self.attributes["genclass"] = "Function"


class TcpFlattenedRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Flattened Read")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "data out", isInput=False)
        LVNode.addTerminal(self, "connection ID out", isInput=False)
        LVNode.addTerminal(self, "type", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (25000)", isInput=True)
        LVNode.addTerminal(self, "connection ID", isInput=True)
        self.attributes["type"] = "TCP Flattened Read"
        self.attributes["genclass"] = "Function"


class TcpFlattenedWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Flattened Write")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "connection ID out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (25000)", isInput=True)
        LVNode.addTerminal(self, "data in", isInput=True)
        LVNode.addTerminal(self, "connection ID", isInput=True)
        self.attributes["type"] = "TCP Flattened Write"
        self.attributes["genclass"] = "Function"


class TcpFlexRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Flex Read")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "coerced?", isInput=False)
        LVNode.addTerminal(self, "data out", isInput=False)
        LVNode.addTerminal(self, "connection ID out", isInput=False)
        LVNode.addTerminal(self, "type", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (25000)", isInput=True)
        LVNode.addTerminal(self, "connection ID", isInput=True)
        self.attributes["type"] = "TCP Flex Read"
        self.attributes["genclass"] = "Function"


class TcpFlexWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Flex Write")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "connection ID out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (25000)", isInput=True)
        LVNode.addTerminal(self, "data in", isInput=True)
        LVNode.addTerminal(self, "connection ID", isInput=True)
        self.attributes["type"] = "TCP Flex Write"
        self.attributes["genclass"] = "Function"


class TcpOpenConnection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Open Connection")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "connection ID", isInput=False)
        LVNode.addTerminal(self, "local port", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (60000)", isInput=True)
        LVNode.addTerminal(self, "remote port or service name", isInput=True)
        LVNode.addTerminal(self, "address", isInput=True)
        self.attributes["type"] = "TCP Open Connection"
        self.attributes["genclass"] = "Function"


class TcpRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Read")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "data out", isInput=False)
        LVNode.addTerminal(self, "connection ID out", isInput=False)
        LVNode.addTerminal(self, "mode (standard)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (25000)", isInput=True)
        LVNode.addTerminal(self, "bytes to read", isInput=True)
        LVNode.addTerminal(self, "connection ID", isInput=True)
        self.attributes["type"] = "TCP Read"
        self.attributes["genclass"] = "Function"


class TcpWaitOnListener(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Wait On Listener")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "remote port", isInput=False)
        LVNode.addTerminal(self, "remote address", isInput=False)
        LVNode.addTerminal(self, "listener ID out", isInput=False)
        LVNode.addTerminal(self, "connection ID", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (wait forever: -1)", isInput=True)
        LVNode.addTerminal(self, "resolve remote address (T)", isInput=True)
        LVNode.addTerminal(self, "listener ID in", isInput=True)
        self.attributes["type"] = "TCP Wait On Listener"
        self.attributes["genclass"] = "Function"


class TcpWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TCP Write")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "bytes written", isInput=False)
        LVNode.addTerminal(self, "connection ID out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (25000)", isInput=True)
        LVNode.addTerminal(self, "data in", isInput=True)
        LVNode.addTerminal(self, "connection ID", isInput=True)
        self.attributes["type"] = "TCP Write"
        self.attributes["genclass"] = "Function"


class TdmsAdvancedAsynchronousReadDataRef(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Advanced Asynchronous Read (Data Ref)")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "tdms file out", isInput=False)
        LVNode.addTerminal(self, "read process finished?", isInput=False)
        LVNode.addTerminal(self, "auto delete reference? (T)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "data reference", isInput=True)
        LVNode.addTerminal(self, "tdms file", isInput=True)
        self.attributes["type"] = "TDMS Advanced Asynchronous Read (Data Ref)"
        self.attributes["genclass"] = "Function"


class TdmsAdvancedAsynchronousWriteDataRef(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Advanced Asynchronous Write (Data Ref)")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "tdms file out", isInput=False)
        LVNode.addTerminal(self, "auto delete reference? (T)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "data reference", isInput=True)
        LVNode.addTerminal(self, "tdms file", isInput=True)
        self.attributes["type"] = "TDMS Advanced Asynchronous Write (Data Ref)"
        self.attributes["genclass"] = "Function"


class TdmsClose(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Close")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "file path out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "tdms file", isInput=True)
        self.attributes["type"] = "TDMS Close"
        self.attributes["genclass"] = "Function"


class TdmsConfigureAsynchronousReadsDataRef(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Configure Asynchronous Reads (Data Ref)")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "tdms file out", isInput=False)
        LVNode.addTerminal(self, "timeout (5 s)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "total size (in bytes) (-1)", isInput=True)
        LVNode.addTerminal(self, "max asynchronous reads (4)", isInput=True)
        LVNode.addTerminal(self, "tdms file", isInput=True)
        self.attributes["type"] = "TDMS Configure Asynchronous Reads (Data Ref)"
        self.attributes["genclass"] = "Function"


class TdmsConfigureAsynchronousWritesDataRef(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Configure Asynchronous Writes (Data Ref)")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "tdms file out", isInput=False)
        LVNode.addTerminal(self, "timeout (5 s)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "max asynchronous writes (4)", isInput=True)
        LVNode.addTerminal(self, "tdms file", isInput=True)
        self.attributes["type"] = "TDMS Configure Asynchronous Writes (Data Ref)"
        self.attributes["genclass"] = "Function"


class TdmsDefragment(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Defragment")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "object id", isInput=False)
        LVNode.addTerminal(self, "tdms file id", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "channel name", isInput=True)
        LVNode.addTerminal(self, "group name", isInput=True)
        LVNode.addTerminal(self, "tdms file", isInput=True)
        self.attributes["type"] = "TDMS Defragment"
        self.attributes["genclass"] = "Function"


class TdmsDeleteData(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Delete Data")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "file path out", isInput=False)
        LVNode.addTerminal(self, "count (-1: all)", isInput=True)
        LVNode.addTerminal(self, "keep empty group/channel? (T)", isInput=True)
        LVNode.addTerminal(self, "from (0: start)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "channel name(s) in", isInput=True)
        LVNode.addTerminal(self, "group name in", isInput=True)
        LVNode.addTerminal(self, "file path", isInput=True)
        self.attributes["type"] = "TDMS Delete Data"
        self.attributes["genclass"] = "Function"


class TdmsFlush(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Flush")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "tdms file out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "tdms file", isInput=True)
        self.attributes["type"] = "TDMS Flush"
        self.attributes["genclass"] = "Function"


class TdmsGetAsynchronousReadStatusDataRef(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Get Asynchronous Read Status (Data Ref)")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "number of pending reads", isInput=False)
        LVNode.addTerminal(self, "tdms file out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "tdms file", isInput=True)
        self.attributes["type"] = "TDMS Get Asynchronous Read Status (Data Ref)"
        self.attributes["genclass"] = "Function"


class TdmsGetAsynchronousWriteStatusDataRef(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Get Asynchronous Write Status (Data Ref)")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "number of pending writes", isInput=False)
        LVNode.addTerminal(self, "tdms file out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "tdms file", isInput=True)
        self.attributes["type"] = "TDMS Get Asynchronous Write Status (Data Ref)"
        self.attributes["genclass"] = "Function"


class TdmsGetProperties(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Get Properties")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "channel name out", isInput=False)
        LVNode.addTerminal(self, "group name out", isInput=False)
        LVNode.addTerminal(self, "tdms file out", isInput=False)
        LVNode.addTerminal(self, "property values", isInput=False)
        LVNode.addTerminal(self, "data type", isInput=True)
        LVNode.addTerminal(self, "property names", isInput=False)
        LVNode.addTerminal(self, "property name", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "channel name", isInput=True)
        LVNode.addTerminal(self, "group name", isInput=True)
        LVNode.addTerminal(self, "tdms file", isInput=True)
        self.attributes["type"] = "TDMS Get Properties"
        self.attributes["genclass"] = "Function"


class TdmsInMemoryClose(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS In Memory Close")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "overwrite (F)", isInput=True)
        LVNode.addTerminal(self, "file path", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "tdms file", isInput=True)
        self.attributes["type"] = "TDMS In Memory Close"
        self.attributes["genclass"] = "Function"


class TdmsInMemoryOpen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS In Memory Open")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "tdms file out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "byte array or file path", isInput=True)
        self.attributes["type"] = "TDMS In Memory Open"
        self.attributes["genclass"] = "Function"


class TdmsInMemoryReadBytes(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS In Memory Read Bytes")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "data", isInput=False)
        LVNode.addTerminal(self, "tdms file out", isInput=False)
        LVNode.addTerminal(self, "byte count (-1: all)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "tdms file", isInput=True)
        self.attributes["type"] = "TDMS In Memory Read Bytes"
        self.attributes["genclass"] = "Function"


class TdmsListContents(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS List Contents")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "group/channel names", isInput=False)
        LVNode.addTerminal(self, "group names", isInput=False)
        LVNode.addTerminal(self, "tdms file out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "group name", isInput=True)
        LVNode.addTerminal(self, "tdms file", isInput=True)
        self.attributes["type"] = "TDMS List Contents"
        self.attributes["genclass"] = "Function"


class TdmsOpen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Open")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "tdms file out", isInput=False)
        LVNode.addTerminal(self, "create index file? (T)", isInput=True)
        LVNode.addTerminal(self, "disable buffering (T)", isInput=True)
        LVNode.addTerminal(self, "file format version (2.0)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "byte order (2:little-endian)", isInput=True)
        LVNode.addTerminal(self, "operation (0:open)", isInput=True)
        LVNode.addTerminal(self, "file path", isInput=True)
        self.attributes["type"] = "TDMS Open"
        self.attributes["genclass"] = "Function"


class TdmsRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Read")
        LVNode.addTerminal(self, "tdms file", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "count (-1: all)", isInput=True)
        LVNode.addTerminal(self, "tdms file out", isInput=False)
        LVNode.addTerminal(self, "group name in", isInput=True)
        LVNode.addTerminal(self, "group name out", isInput=False)
        LVNode.addTerminal(self, "channel name(s) in", isInput=True)
        LVNode.addTerminal(self, "channel name(s) out", isInput=False)
        LVNode.addTerminal(self, "data", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "data type", isInput=True)
        LVNode.addTerminal(self, "return channels in file order? (F)", isInput=True)
        LVNode.addTerminal(self, "end of file?", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "TDMS Read"
        self.attributes["genclass"] = "Function"


class TdmsRefnumToFileId(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Refnum To File ID")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "object id", isInput=False)
        LVNode.addTerminal(self, "tdms file id", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "channel name", isInput=True)
        LVNode.addTerminal(self, "group name", isInput=True)
        LVNode.addTerminal(self, "tdms file", isInput=True)
        self.attributes["type"] = "TDMS Refnum To File ID"
        self.attributes["genclass"] = "Function"


class TdmsSetProperties(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Set Properties")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "channel name out", isInput=False)
        LVNode.addTerminal(self, "group name out", isInput=False)
        LVNode.addTerminal(self, "tdms file out", isInput=False)
        LVNode.addTerminal(self, "property values", isInput=True)
        LVNode.addTerminal(self, "property names", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "channel name", isInput=True)
        LVNode.addTerminal(self, "group name", isInput=True)
        LVNode.addTerminal(self, "tdms file", isInput=True)
        self.attributes["type"] = "TDMS Set Properties"
        self.attributes["genclass"] = "Function"


class TdmsWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Write")
        LVNode.addTerminal(self, "tdms file", isInput=True)
        LVNode.addTerminal(self, "data layout (0:decimated)", isInput=True)
        LVNode.addTerminal(self, "tdms file out", isInput=False)
        LVNode.addTerminal(self, "group name in (Untitled)", isInput=True)
        LVNode.addTerminal(self, "group name out", isInput=False)
        LVNode.addTerminal(self, "channel name(s) in (Untitled)", isInput=True)
        LVNode.addTerminal(self, "channel name(s) out", isInput=False)
        LVNode.addTerminal(self, "data", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "TDMS Write"
        self.attributes["genclass"] = "Function"


class TdmsWriteIp(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TDMS Write IP")
        LVNode.addTerminal(self, "tdms file", isInput=True)
        LVNode.addTerminal(self, "tdms file out", isInput=False)
        LVNode.addTerminal(self, "group name in", isInput=True)
        LVNode.addTerminal(self, "group name out", isInput=False)
        LVNode.addTerminal(self, "channel names in", isInput=True)
        LVNode.addTerminal(self, "channel names out", isInput=False)
        LVNode.addTerminal(self, "data", isInput=True)
        LVNode.addTerminal(self, "data out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "TDMS Write IP"
        self.attributes["genclass"] = "Function"


class TemporaryDirectory(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Temporary Directory")
        LVNode.addTerminal(self, "path", isInput=False)
        self.attributes["type"] = "Temporary Directory"
        self.attributes["genclass"] = "Function"


class Testsrq(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TestSRQ")
        LVNode.addTerminal(self, "bus", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "SRQ", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "TestSRQ"
        self.attributes["genclass"] = "Function"


class Testsys(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TestSys")
        LVNode.addTerminal(self, "bus", isInput=True)
        LVNode.addTerminal(self, "address list", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "result list", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "failed devices", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "TestSys"
        self.attributes["genclass"] = "Function"


class TextToUtf8(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Text to UTF-8")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "utf-8 text", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "encoding", isInput=True)
        LVNode.addTerminal(self, "text", isInput=True)
        self.attributes["type"] = "Text to UTF-8"
        self.attributes["genclass"] = "Function"


class Threshold1dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Threshold 1D Array")
        LVNode.addTerminal(self, "fractional index or x", isInput=False)
        LVNode.addTerminal(self, "start index (0)", isInput=True)
        LVNode.addTerminal(self, "threshold y", isInput=True)
        LVNode.addTerminal(self, "array of numbers or points", isInput=True)
        self.attributes["type"] = "Threshold 1D Array"
        self.attributes["genclass"] = "Function"


class TickCountMs(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Tick Count (ms)")
        LVNode.addTerminal(self, "millisecond timer value", isInput=False)
        self.attributes["type"] = "Tick Count (ms)"
        self.attributes["genclass"] = "Function"


class TlsConnection(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TLS Connection?")
        LVNode.addTerminal(self, "TLS?", isInput=False)
        LVNode.addTerminal(self, "TCP connection", isInput=True)
        self.attributes["type"] = "TLS Connection?"
        self.attributes["genclass"] = "Function"


class ToByteInteger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Byte Integer")
        LVNode.addTerminal(self, "8bit integer", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "To Byte Integer"
        self.attributes["genclass"] = "Function"


class ToDoublePrecisionComplex(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Double Precision Complex")
        LVNode.addTerminal(self, "double precision complex", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "To Double Precision Complex"
        self.attributes["genclass"] = "Function"


class ToDoublePrecisionFloat(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Double Precision Float")
        LVNode.addTerminal(self, "double precision float", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "To Double Precision Float"
        self.attributes["genclass"] = "Function"


class ToExtendedPrecisionComplex(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Extended Precision Complex")
        LVNode.addTerminal(self, "extended precision complex", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "To Extended Precision Complex"
        self.attributes["genclass"] = "Function"


class ToExtendedPrecisionFloat(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Extended Precision Float")
        LVNode.addTerminal(self, "extended precision float", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "To Extended Precision Float"
        self.attributes["genclass"] = "Function"


class ToFixedPoint(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Fixed-Point")
        LVNode.addTerminal(self, "number", isInput=True)
        LVNode.addTerminal(self, "fixed-point type", isInput=True)
        LVNode.addTerminal(self, "fixed-point", isInput=False)
        self.attributes["type"] = "To Fixed-Point"
        self.attributes["genclass"] = "Function"


class ToLongInteger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Long Integer")
        LVNode.addTerminal(self, "32bit integer", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "To Long Integer"
        self.attributes["genclass"] = "Function"


class ToLowerCase(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Lower Case")
        LVNode.addTerminal(self, "all lower case string", isInput=False)
        LVNode.addTerminal(self, "string", isInput=True)
        self.attributes["type"] = "To Lower Case"
        self.attributes["genclass"] = "Function"


class ToMoreGenericClass(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To More Generic Class")
        LVNode.addTerminal(self, "reference", isInput=True)
        LVNode.addTerminal(self, "target class", isInput=True)
        LVNode.addTerminal(self, "generic class reference", isInput=False)
        self.attributes["type"] = "To More Generic Class"
        self.attributes["genclass"] = "Function"


class ToMoreSpecificClass(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To More Specific Class")
        LVNode.addTerminal(self, "specific class reference", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "target class", isInput=True)
        LVNode.addTerminal(self, "reference", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        self.attributes["type"] = "To More Specific Class"
        self.attributes["genclass"] = "Function"


class ToOleVariant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To OLE Variant")
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "vt VARTYPE", isInput=True)
        LVNode.addTerminal(self, "OLE Variant", isInput=False)
        self.attributes["type"] = "To OLE Variant"
        self.attributes["genclass"] = "Function"


class ToProbeString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Probe String")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "probe string", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "maximum string length", isInput=True)
        LVNode.addTerminal(self, "data value", isInput=True)
        self.attributes["type"] = "To Probe String"
        self.attributes["genclass"] = "Function"


class ToQuadInteger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Quad Integer")
        LVNode.addTerminal(self, "64bit integer", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "To Quad Integer"
        self.attributes["genclass"] = "Function"


class ToSinglePrecisionComplex(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Single Precision Complex")
        LVNode.addTerminal(self, "single precision complex", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "To Single Precision Complex"
        self.attributes["genclass"] = "Function"


class ToSinglePrecisionFloat(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Single Precision Float")
        LVNode.addTerminal(self, "single precision float", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "To Single Precision Float"
        self.attributes["genclass"] = "Function"


class ToTimeStamp(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Time Stamp")
        LVNode.addTerminal(self, "Time Stamp", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "To Time Stamp"
        self.attributes["genclass"] = "Function"


class ToUnsignedByteInteger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Unsigned Byte Integer")
        LVNode.addTerminal(self, "unsigned 8bit integer", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "To Unsigned Byte Integer"
        self.attributes["genclass"] = "Function"


class ToUnsignedLongInteger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Unsigned Long Integer")
        LVNode.addTerminal(self, "unsigned 32bit integer", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "To Unsigned Long Integer"
        self.attributes["genclass"] = "Function"


class ToUnsignedQuadInteger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Unsigned Quad Integer")
        LVNode.addTerminal(self, "unsigned 64bit integer", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "To Unsigned Quad Integer"
        self.attributes["genclass"] = "Function"


class ToUnsignedWordInteger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Unsigned Word Integer")
        LVNode.addTerminal(self, "unsigned 16bit integer", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "To Unsigned Word Integer"
        self.attributes["genclass"] = "Function"


class ToUpperCase(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Upper Case")
        LVNode.addTerminal(self, "all upper case string", isInput=False)
        LVNode.addTerminal(self, "string", isInput=True)
        self.attributes["type"] = "To Upper Case"
        self.attributes["genclass"] = "Function"


class ToVariant(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Variant")
        LVNode.addTerminal(self, "Variant", isInput=False)
        LVNode.addTerminal(self, "anything", isInput=True)
        self.attributes["type"] = "To Variant"
        self.attributes["genclass"] = "Function"


class ToWordInteger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "To Word Integer")
        LVNode.addTerminal(self, "16bit integer", isInput=False)
        LVNode.addTerminal(self, "number", isInput=True)
        self.attributes["type"] = "To Word Integer"
        self.attributes["genclass"] = "Function"


class Transpose1dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Transpose 1D Array")
        LVNode.addTerminal(self, "transposed array", isInput=False)
        LVNode.addTerminal(self, "1D array", isInput=True)
        self.attributes["type"] = "Transpose 1D Array"
        self.attributes["genclass"] = "Function"


class Transpose2dArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Transpose 2D Array")
        LVNode.addTerminal(self, "transposed array", isInput=False)
        LVNode.addTerminal(self, "2D array", isInput=True)
        self.attributes["type"] = "Transpose 2D Array"
        self.attributes["genclass"] = "Function"


class TransposeMatrix(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Transpose Matrix")
        LVNode.addTerminal(self, "transposed matrix", isInput=False)
        LVNode.addTerminal(self, "matrix", isInput=True)
        self.attributes["type"] = "Transpose Matrix"
        self.attributes["genclass"] = "Function"


class Trigger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Trigger")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "address", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "Trigger"
        self.attributes["genclass"] = "Function"


class Triggerlist(LVNode):
    def __init__(self):
        LVNode.__init__(self, "TriggerList")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "address list", isInput=True)
        LVNode.addTerminal(self, "bus", isInput=True)
        self.attributes["type"] = "TriggerList"
        self.attributes["genclass"] = "Function"


class TwoButtonDialog(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Two Button Dialog")
        LVNode.addTerminal(self, "T button?", isInput=False)
        LVNode.addTerminal(self, "F button name (\"Cancel\")", isInput=True)
        LVNode.addTerminal(self, "T button name (\"OK\")", isInput=True)
        LVNode.addTerminal(self, "message", isInput=True)
        self.attributes["type"] = "Two Button Dialog"
        self.attributes["genclass"] = "Function"


class TypeAndCreator(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Type and Creator")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "creator", isInput=False)
        LVNode.addTerminal(self, "type", isInput=False)
        LVNode.addTerminal(self, "dup path", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "new creator", isInput=True)
        LVNode.addTerminal(self, "new type", isInput=True)
        LVNode.addTerminal(self, "path", isInput=True)
        self.attributes["type"] = "Type and Creator"
        self.attributes["genclass"] = "Function"


class TypeCast(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Type Cast")
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "type", isInput=True)
        LVNode.addTerminal(self, "*(type *) &x", isInput=False)
        self.attributes["type"] = "Type Cast"
        self.attributes["genclass"] = "Function"


class TypeError(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Type Error")
        LVNode.addTerminal(self, "bool const", isInput=True)
        self.attributes["type"] = "Type Error"
        self.attributes["genclass"] = "Function"


class TypeMustBeArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Type Must Be Array")
        LVNode.addTerminal(self, "any", isInput=True)
        self.attributes["type"] = "Type Must Be Array"
        self.attributes["genclass"] = "Function"
class TypeMustBeCluster(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Type Must Be Cluster")
        LVNode.addTerminal(self, "any", isInput=True)
        self.attributes["type"] = "Type Must Be Cluster"
        self.attributes["genclass"] = "Function"


class TypeOf(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Type Of")
        LVNode.addTerminal(self, "type", isInput=False)
        LVNode.addTerminal(self, "any", isInput=True)
        self.attributes["type"] = "Type Of"
        self.attributes["genclass"] = "Function"


class UdpClose(LVNode):
    def __init__(self):
        LVNode.__init__(self, "UDP Close")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "connection ID out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "connection ID", isInput=True)
        self.attributes["type"] = "UDP Close"
        self.attributes["genclass"] = "Function"


class UdpMulticastOpen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "UDP Multicast Open")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "port", isInput=False)
        LVNode.addTerminal(self, "connection ID", isInput=False)
        LVNode.addTerminal(self, "net address", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "time-to-live", isInput=True)
        LVNode.addTerminal(self, "multicast addr", isInput=True)
        LVNode.addTerminal(self, "port", isInput=True)
        self.attributes["type"] = "UDP Multicast Open"
        self.attributes["genclass"] = "Function"


class UdpOpen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "UDP Open")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "service name", isInput=False)
        LVNode.addTerminal(self, "port", isInput=False)
        LVNode.addTerminal(self, "", isInput=True)
        LVNode.addTerminal(self, "net address", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "", isInput=True)
        LVNode.addTerminal(self, "", isInput=True)
        self.attributes["type"] = "UDP Open"
        self.attributes["genclass"] = "Function"


class UdpRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "UDP Read")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "data out", isInput=False)
        LVNode.addTerminal(self, "connection ID out", isInput=False)
        LVNode.addTerminal(self, "port", isInput=False)
        LVNode.addTerminal(self, "address", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (25000)", isInput=True)
        LVNode.addTerminal(self, "max size (548)", isInput=True)
        LVNode.addTerminal(self, "connection ID", isInput=True)
        self.attributes["type"] = "UDP Read"
        self.attributes["genclass"] = "Function"


class UdpWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "UDP Write")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "connection ID out", isInput=False)
        LVNode.addTerminal(self, "port or service name", isInput=True)
        LVNode.addTerminal(self, "address", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout ms (25000)", isInput=True)
        LVNode.addTerminal(self, "data in", isInput=True)
        LVNode.addTerminal(self, "connection ID", isInput=True)
        self.attributes["type"] = "UDP Write"
        self.attributes["genclass"] = "Function"


class UnbitpackFromArray(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Unbitpack from Array")
        LVNode.addTerminal(self, "data", isInput=False)
        LVNode.addTerminal(self, "type", isInput=True)
        LVNode.addTerminal(self, "bparray", isInput=True)
        self.attributes["type"] = "Unbitpack from Array"
        self.attributes["genclass"] = "Function"


class UnflattenFromJson(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Unflatten From JSON")
        LVNode.addTerminal(self, "JSON string", isInput=True)
        LVNode.addTerminal(self, "type and defaults", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "path", isInput=True)
        LVNode.addTerminal(self, "default null elements? (F)", isInput=True)
        LVNode.addTerminal(self, "enable LabVIEW extensions? (T)", isInput=True)
        LVNode.addTerminal(self, "strict validation? (F)", isInput=True)
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Unflatten From JSON"
        self.attributes["genclass"] = "Function"


class UnflattenFromString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Unflatten From String")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "rest of the binary string", isInput=False)
        LVNode.addTerminal(self, "type", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "byte order (0:big-endian, network order)", isInput=True)
        LVNode.addTerminal(self, "data includes array or string size? (T)", isInput=True)
        LVNode.addTerminal(self, "binary string", isInput=True)
        self.attributes["type"] = "Unflatten From String"
        self.attributes["genclass"] = "Function"


class UnflattenFromXml(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Unflatten From XML")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "type", isInput=True)
        LVNode.addTerminal(self, "xml string", isInput=True)
        self.attributes["type"] = "Unflatten From XML"
        self.attributes["genclass"] = "Function"


class UnleakVariantValueReference(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Unleak Variant Value Reference")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "variant value reference out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "variant value reference in", isInput=True)
        self.attributes["type"] = "Unleak Variant Value Reference"
        self.attributes["genclass"] = "Function"


class UnpackageMatrix(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Unpackage Matrix")
        LVNode.addTerminal(self, "matrix", isInput=True)
        LVNode.addTerminal(self, "matrix", isInput=False)
        LVNode.addTerminal(self, "array", isInput=False)
        self.attributes["type"] = "Unpackage Matrix"
        self.attributes["genclass"] = "Function"


class UnregisterForEvents(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Unregister For Events")
        LVNode.addTerminal(self, "event registration refnum", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Unregister For Events"
        self.attributes["genclass"] = "Function"


class UnregisterSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Unregister Session")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Unregister Session"
        self.attributes["genclass"] = "Function"


class Utf8ToText(LVNode):
    def __init__(self):
        LVNode.__init__(self, "UTF-8 to Text")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "text", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "encoding", isInput=True)
        LVNode.addTerminal(self, "utf-8 text", isInput=True)
        self.attributes["type"] = "UTF-8 to Text"
        self.attributes["genclass"] = "Function"


class VariantToData(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Variant To Data")
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "Variant", isInput=True)
        LVNode.addTerminal(self, "type", isInput=True)
        LVNode.addTerminal(self, "data", isInput=False)
        self.attributes["type"] = "Variant To Data"
        self.attributes["genclass"] = "Function"


class VariantToFlattenedString(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Variant To Flattened String")
        LVNode.addTerminal(self, "Variant", isInput=True)
        LVNode.addTerminal(self, "type string", isInput=False)
        LVNode.addTerminal(self, "data string", isInput=False)
        self.attributes["type"] = "Variant To Flattened String"
        self.attributes["genclass"] = "Function"


class ViLibrary(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VI Library")
        LVNode.addTerminal(self, "path", isInput=False)
        self.attributes["type"] = "VI Library"
        self.attributes["genclass"] = "Function"


class VisaAssertInterruptSignal(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Assert Interrupt Signal")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "status ID", isInput=True)
        LVNode.addTerminal(self, "mode", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Assert Interrupt Signal"
        self.attributes["genclass"] = "Function"


class VisaAssertTrigger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Assert Trigger")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "protocol (default:  0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Assert Trigger"
        self.attributes["genclass"] = "Function"


class VisaAssertUtilitySignal(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Assert Utility Signal")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "bus signal", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Assert Utility Signal"
        self.attributes["genclass"] = "Function"


class VisaClear(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Clear")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Clear"
        self.attributes["genclass"] = "Function"


class VisaClose(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Close")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Close"
        self.attributes["genclass"] = "Function"


class VisaDisableEvent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Disable Event")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "mechanism (1:  VI_QUEUE)", isInput=True)
        LVNode.addTerminal(self, "event type (all enabled)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Disable Event"
        self.attributes["genclass"] = "Function"


class VisaDiscardEvents(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Discard Events")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "mechanism  (1:  VI_QUEUE)", isInput=True)
        LVNode.addTerminal(self, "event type (all enabled)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Discard Events"
        self.attributes["genclass"] = "Function"


class VisaEnableEvent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Enable Event")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "mechanism (1:  VI_QUEUE)", isInput=True)
        LVNode.addTerminal(self, "event type", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Enable Event"
        self.attributes["genclass"] = "Function"


class VisaFindResource(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Find Resource")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "return count", isInput=False)
        LVNode.addTerminal(self, "find list", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "search mode (0)", isInput=True)
        LVNode.addTerminal(self, "expression ("")", isInput=True)
        self.attributes["type"] = "VISA Find Resource"
        self.attributes["genclass"] = "Function"


class VisaFlushIOBuffer(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Flush I/O Buffer")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "mask (16)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Flush I/O Buffer"
        self.attributes["genclass"] = "Function"


class VisaGpibCommand(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA GPIB Command")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "return count", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "command", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA GPIB Command"
        self.attributes["genclass"] = "Function"


class VisaGpibControlAtn(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA GPIB Control ATN")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "mode", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA GPIB Control ATN"
        self.attributes["genclass"] = "Function"


class VisaGpibControlRen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA GPIB Control REN")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "mode", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA GPIB Control REN"
        self.attributes["genclass"] = "Function"


class VisaGpibPassControl(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA GPIB Pass Control")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "secondary address (none)", isInput=True)
        LVNode.addTerminal(self, "primary address", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA GPIB Pass Control"
        self.attributes["genclass"] = "Function"


class VisaGpibSendIfc(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA GPIB Send IFC")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA GPIB Send IFC"
        self.attributes["genclass"] = "Function"


class VisaIn16(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA In 16")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA In 16"
        self.attributes["genclass"] = "Function"


class VisaIn32(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA In 32")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA In 32"
        self.attributes["genclass"] = "Function"


class VisaIn64(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA In 64")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA In 64"
        self.attributes["genclass"] = "Function"


class VisaIn8(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA In 8")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA In 8"
        self.attributes["genclass"] = "Function"


class VisaLock(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Lock")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "access key", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "lock type (exclusive:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "requested key", isInput=True)
        LVNode.addTerminal(self, "timeout (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Lock"
        self.attributes["genclass"] = "Function"


class VisaMapAddress(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Map Address")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "access (False)", isInput=True)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "map size (0)", isInput=True)
        LVNode.addTerminal(self, "map base (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Map Address"
        self.attributes["genclass"] = "Function"


class VisaMapTrigger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Map Trigger")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "mode", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "trigger destination", isInput=True)
        LVNode.addTerminal(self, "trigger source", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Map Trigger"
        self.attributes["genclass"] = "Function"


class VisaMemoryAllocation(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Memory Allocation")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "offset", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "size", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Memory Allocation"
        self.attributes["genclass"] = "Function"


class VisaMemoryAllocationEx(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Memory Allocation Ex")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "offset", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "size", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Memory Allocation Ex"
        self.attributes["genclass"] = "Function"


class VisaMemoryFree(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Memory Free")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "offset", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Memory Free"
        self.attributes["genclass"] = "Function"


class VisaMove(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move")
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        LVNode.addTerminal(self, "source space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "source width (8)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "source offset (0)", isInput=True)
        LVNode.addTerminal(self, "length", isInput=True)
        LVNode.addTerminal(self, "dest offset (0)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "dest space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "dest width (same as source)", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "VISA Move"
        self.attributes["genclass"] = "Function"


class VisaMoveIn16(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move In 16")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "data", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "count", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Move In 16"
        self.attributes["genclass"] = "Function"


class VisaMoveIn32(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move In 32")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "data", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "count", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Move In 32"
        self.attributes["genclass"] = "Function"


class VisaMoveIn64(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move In 64")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "data", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "count", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Move In 64"
        self.attributes["genclass"] = "Function"


class VisaMoveIn8(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move In 8")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "data", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "count", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Move In 8"
        self.attributes["genclass"] = "Function"


class VisaMoveOut16(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move Out 16")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "data", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Move Out 16"
        self.attributes["genclass"] = "Function"


class VisaMoveOut32(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move Out 32")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "data", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Move Out 32"
        self.attributes["genclass"] = "Function"


class VisaMoveOut64(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move Out 64")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "data", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Move Out 64"
        self.attributes["genclass"] = "Function"


class VisaMoveOut8(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Move Out 8")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "data", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Move Out 8"
        self.attributes["genclass"] = "Function"


class VisaOpen(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Open")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name", isInput=False)
        LVNode.addTerminal(self, "timeout (0)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "access mode", isInput=True)
        LVNode.addTerminal(self, "duplicate session (F)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Open"
        self.attributes["genclass"] = "Function"


class VisaOut16(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Out 16")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "value (0)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Out 16"
        self.attributes["genclass"] = "Function"


class VisaOut32(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Out 32")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "value (0)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Out 32"
        self.attributes["genclass"] = "Function"


class VisaOut64(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Out 64")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "value (0)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Out 64"
        self.attributes["genclass"] = "Function"


class VisaOut8(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Out 8")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "address space (A16:  1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "value (0)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Out 8"
        self.attributes["genclass"] = "Function"


class VisaPeek16(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Peek 16")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Peek 16"
        self.attributes["genclass"] = "Function"


class VisaPeek32(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Peek 32")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Peek 32"
        self.attributes["genclass"] = "Function"


class VisaPeek64(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Peek 64")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Peek 64"
        self.attributes["genclass"] = "Function"


class VisaPeek8(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Peek 8")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "value", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Peek 8"
        self.attributes["genclass"] = "Function"


class VisaPoke16(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Poke 16")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "value (0)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Poke 16"
        self.attributes["genclass"] = "Function"


class VisaPoke32(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Poke 32")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "value (0)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Poke 32"
        self.attributes["genclass"] = "Function"


class VisaPoke64(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Poke 64")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "value (0)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Poke 64"
        self.attributes["genclass"] = "Function"


class VisaPoke8(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Poke 8")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "value (0)", isInput=True)
        LVNode.addTerminal(self, "offset (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Poke 8"
        self.attributes["genclass"] = "Function"


class VisaRead(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Read")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "return count", isInput=False)
        LVNode.addTerminal(self, "read buffer", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "byte count", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Read"
        self.attributes["genclass"] = "Function"


class VisaReadStb(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Read STB")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status byte", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Read STB"
        self.attributes["genclass"] = "Function"


class VisaReadToFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Read To File")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "return count", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "byte count", isInput=True)
        LVNode.addTerminal(self, "filename", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Read To File"
        self.attributes["genclass"] = "Function"


class VisaRefnumToSession(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Refnum to Session")
        LVNode.addTerminal(self, "session", isInput=False)
        LVNode.addTerminal(self, "Visa Refnum", isInput=True)
        self.attributes["type"] = "VISA Refnum to Session"
        self.attributes["genclass"] = "Function"


class VisaSetIOBufferSize(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Set I/O Buffer Size")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "size (4096)", isInput=True)
        LVNode.addTerminal(self, "mask (16)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Set I/O Buffer Size"
        self.attributes["genclass"] = "Function"


class VisaStatusDescription(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Status Description")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "status description", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Status Description"
        self.attributes["genclass"] = "Function"


class VisaUnlock(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Unlock")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Unlock"
        self.attributes["genclass"] = "Function"


class VisaUnmapAddress(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Unmap Address")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Unmap Address"
        self.attributes["genclass"] = "Function"


class VisaUnmapTrigger(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Unmap Trigger")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "trigger destination (all)", isInput=True)
        LVNode.addTerminal(self, "trigger source", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Unmap Trigger"
        self.attributes["genclass"] = "Function"


class VisaUsbControlIn(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA USB Control In")
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        LVNode.addTerminal(self, "value (0)", isInput=True)
        LVNode.addTerminal(self, "index (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "request type", isInput=True)
        LVNode.addTerminal(self, "read buffer", isInput=False)
        LVNode.addTerminal(self, "request", isInput=True)
        LVNode.addTerminal(self, "length (0)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "VISA USB Control In"
        self.attributes["genclass"] = "Function"


class VisaUsbControlOut(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA USB Control Out")
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        LVNode.addTerminal(self, "value (0)", isInput=True)
        LVNode.addTerminal(self, "index (0)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "request type", isInput=True)
        LVNode.addTerminal(self, "request", isInput=True)
        LVNode.addTerminal(self, "length (0)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "VISA USB Control Out"
        self.attributes["genclass"] = "Function"


class VisaVxiCmdOrQuery(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA VXI Cmd or Query")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "response", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "command", isInput=True)
        LVNode.addTerminal(self, "mode (x200: 16-bit cmd)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA VXI Cmd or Query"
        self.attributes["genclass"] = "Function"


class VisaWaitOnEvent(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Wait on Event")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "event  resource name", isInput=False)
        LVNode.addTerminal(self, "event type", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "timeout (0)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "event  resource name (for class)", isInput=True)
        LVNode.addTerminal(self, "event type (all enabled)", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Wait on Event"
        self.attributes["genclass"] = "Function"


class VisaWrite(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Write")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "return count", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "write buffer", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Write"
        self.attributes["genclass"] = "Function"


class VisaWriteFromFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "VISA Write From File")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "return count", isInput=False)
        LVNode.addTerminal(self, "VISA resource name out", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "count (entire file)", isInput=True)
        LVNode.addTerminal(self, "filename", isInput=True)
        LVNode.addTerminal(self, "VISA resource name", isInput=True)
        self.attributes["type"] = "VISA Write From File"
        self.attributes["genclass"] = "Function"


class VolumeInfo(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Volume Info")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "free", isInput=False)
        LVNode.addTerminal(self, "used", isInput=False)
        LVNode.addTerminal(self, "size", isInput=False)
        LVNode.addTerminal(self, "volume path", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "path", isInput=True)
        self.attributes["type"] = "Volume Info"
        self.attributes["genclass"] = "Function"


class WaitMs(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait (ms)")
        LVNode.addTerminal(self, "millisecond timer value", isInput=False)
        LVNode.addTerminal(self, "milliseconds to wait", isInput=True)
        self.attributes["type"] = "Wait (ms)"
        self.attributes["genclass"] = "Function"


class WaitForActivity(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait For Activity")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "connection IDs active", isInput=False)
        LVNode.addTerminal(self, "listener IDs active", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "timeout", isInput=True)
        LVNode.addTerminal(self, "connection IDs", isInput=True)
        LVNode.addTerminal(self, "listener IDs", isInput=True)
        self.attributes["type"] = "Wait For Activity"
        self.attributes["genclass"] = "Function"


class WaitForFrontPanelActivity(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait For Front Panel Activity")
        LVNode.addTerminal(self, "millisecond timer value", isInput=False)
        LVNode.addTerminal(self, "timeout ms (-1 never timeout)", isInput=True)
        LVNode.addTerminal(self, "front panel (this VI's panel)", isInput=True)
        LVNode.addTerminal(self, "do not wait! (False)", isInput=True)
        self.attributes["type"] = "Wait For Front Panel Activity"
        self.attributes["genclass"] = "Function"


class WaitForGpibRqs(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait for GPIB RQS")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "poll response byte", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "timeout ms (488.2 global)", isInput=True)
        LVNode.addTerminal(self, "address string", isInput=True)
        self.attributes["type"] = "Wait for GPIB RQS"
        self.attributes["genclass"] = "Function"


class WaitOnNotification(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait on Notification")
        LVNode.addTerminal(self, "notifier", isInput=True)
        LVNode.addTerminal(self, "ignore previous (F)", isInput=True)
        LVNode.addTerminal(self, "timeout in ms (-1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "notifier out", isInput=False)
        LVNode.addTerminal(self, "notification", isInput=False)
        LVNode.addTerminal(self, "timed out?", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Wait on Notification"
        self.attributes["genclass"] = "Function"


class WaitOnNotificationFromMultiple(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait on Notification from Multiple")
        LVNode.addTerminal(self, "notifiers", isInput=True)
        LVNode.addTerminal(self, "ignore previous (F)", isInput=True)
        LVNode.addTerminal(self, "timeout in ms (-1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "notifier out", isInput=False)
        LVNode.addTerminal(self, "notifiers out", isInput=False)
        LVNode.addTerminal(self, "timed out?", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Wait on Notification from Multiple"
        self.attributes["genclass"] = "Function"


class WaitOnNotificationFromMultipleWithNotifierHistory(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait on Notification from Multiple with Notifier History")
        LVNode.addTerminal(self, "notifiers", isInput=True)
        LVNode.addTerminal(self, "ignore previous (F)", isInput=True)
        LVNode.addTerminal(self, "timeout in ms (-1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "notifier out", isInput=False)
        LVNode.addTerminal(self, "notifiers out", isInput=False)
        LVNode.addTerminal(self, "timed out?", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Wait on Notification from Multiple with Notifier History"
        self.attributes["genclass"] = "Function"


class WaitOnNotificationWithNotifierHistory(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait on Notification with Notifier History")
        LVNode.addTerminal(self, "notifier", isInput=True)
        LVNode.addTerminal(self, "ignore previous (F)", isInput=True)
        LVNode.addTerminal(self, "timeout in ms (-1)", isInput=True)
        LVNode.addTerminal(self, "error in (no error)", isInput=True)
        LVNode.addTerminal(self, "notifier out", isInput=False)
        LVNode.addTerminal(self, "notification", isInput=False)
        LVNode.addTerminal(self, "timed out?", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "Wait on Notification with Notifier History"
        self.attributes["genclass"] = "Function"


class WaitOnOccurrence(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait on Occurrence")
        LVNode.addTerminal(self, "timed out", isInput=False)
        LVNode.addTerminal(self, "ignore previous (T)", isInput=True)
        LVNode.addTerminal(self, "occurrence", isInput=True)
        LVNode.addTerminal(self, "ms timeout (-1)", isInput=True)
        self.attributes["type"] = "Wait on Occurrence"
        self.attributes["genclass"] = "Function"


class WaitUntilNextMsMultiple(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Wait Until Next ms Multiple")
        LVNode.addTerminal(self, "millisecond timer value", isInput=False)
        LVNode.addTerminal(self, "millisecond multiple", isInput=True)
        self.attributes["type"] = "Wait Until Next ms Multiple"
        self.attributes["genclass"] = "Function"


class Waitsrq(LVNode):
    def __init__(self):
        LVNode.__init__(self, "WaitSRQ")
        LVNode.addTerminal(self, "bus", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "SRQ", isInput=False)
        LVNode.addTerminal(self, "status", isInput=False)
        LVNode.addTerminal(self, "error out", isInput=False)
        self.attributes["type"] = "WaitSRQ"
        self.attributes["genclass"] = "Function"


class WhiteSpace(LVNode):
    def __init__(self):
        LVNode.__init__(self, "White Space?")
        LVNode.addTerminal(self, "space, h/v tab, cr, lf, ff?", isInput=False)
        LVNode.addTerminal(self, "char", isInput=True)
        self.attributes["type"] = "White Space?"
        self.attributes["genclass"] = "Function"


class WriteDatalog(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Write Datalog")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "record(s)", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Write Datalog"
        self.attributes["genclass"] = "Function"


class WriteDevice(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Write Device")
        LVNode.addTerminal(self, "new offset", isInput=False)
        LVNode.addTerminal(self, "count", isInput=False)
        LVNode.addTerminal(self, "err", isInput=False)
        LVNode.addTerminal(self, "spc reset (F)", isInput=True)
        LVNode.addTerminal(self, "misc (-)", isInput=True)
        LVNode.addTerminal(self, "async (T)", isInput=True)
        LVNode.addTerminal(self, "pos offset (-)", isInput=True)
        LVNode.addTerminal(self, "pos mode (-)", isInput=True)
        LVNode.addTerminal(self, "string", isInput=True)
        LVNode.addTerminal(self, "device refnum", isInput=True)
        self.attributes["type"] = "Write Device"
        self.attributes["genclass"] = "Function"


class WriteFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Write File")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "offset", isInput=False)
        LVNode.addTerminal(self, "dup refnum", isInput=False)
        LVNode.addTerminal(self, "convert eol (F)", isInput=True)
        LVNode.addTerminal(self, "data", isInput=True)
        LVNode.addTerminal(self, "header (F)", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "pos offset (0)", isInput=True)
        LVNode.addTerminal(self, "pos mode (0:2)", isInput=True)
        LVNode.addTerminal(self, "refnum", isInput=True)
        self.attributes["type"] = "Write File"
        self.attributes["genclass"] = "Function"


class WriteToBinaryFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Write to Binary File")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "cancelled", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "prepend array or string size? (T)", isInput=True)
        LVNode.addTerminal(self, "prompt (Choose or enter file path)", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "byte order (0:big-endian, network order)", isInput=True)
        LVNode.addTerminal(self, "data", isInput=True)
        LVNode.addTerminal(self, "file (use dialog)", isInput=True)
        self.attributes["type"] = "Write to Binary File"
        self.attributes["genclass"] = "Function"


class WriteToTextFile(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Write to Text File")
        LVNode.addTerminal(self, "error out", isInput=False)
        LVNode.addTerminal(self, "cancelled", isInput=False)
        LVNode.addTerminal(self, "refnum out", isInput=False)
        LVNode.addTerminal(self, "prompt (Choose or enter file path)", isInput=True)
        LVNode.addTerminal(self, "error in", isInput=True)
        LVNode.addTerminal(self, "text", isInput=True)
        LVNode.addTerminal(self, "file (use dialog)", isInput=True)
        self.attributes["type"] = "Write to Text File"
        self.attributes["genclass"] = "Function"


class YThRootOfX(LVNode):
    def __init__(self):
        LVNode.__init__(self, "Y-th Root of X")
        LVNode.addTerminal(self, "y-th root(x)", isInput=False)
        LVNode.addTerminal(self, "x", isInput=True)
        LVNode.addTerminal(self, "y", isInput=True)
        self.attributes["type"] = "Y-th Root of X"
        self.attributes["genclass"] = "Function"
