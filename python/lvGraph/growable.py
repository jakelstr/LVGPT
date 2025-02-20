from .node import LVNode, GrowableFunction, ObjectFunction
class ArraySubset(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Array Subset", chunks=1)
        LVNode.addTerminal(self, "array", varType="Array")
        LVNode.addTerminal(self, "subarray", varType="Array", isInput=False)
        LVNode.addTerminal(self, "index", varType="I32")
        LVNode.addTerminal(self, "length", varType="I32")
        self.attributes["type"] = "Array Subset"


class AssertStructuralTypeMismatch(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Assert Structural Type Mismatch", chunks=1)
        LVNode.addTerminal(self, "mismatch", varType="I32", isInput=False)
        LVNode.addTerminal(self, "type", varType="LV Variant")
        LVNode.addTerminal(self, "mismatch", varType="LV Variant")
        self.attributes["type"] = "Assert Structural Type Mismatch"


class BuildArray(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Build Array", chunks=1)
        LVNode.addTerminal(self, "appended array", varType="Array", isInput=False)
        LVNode.addTerminal(self, "element", varType="Double Float")
        self.attributes["type"] = "Build Array"


class BuildClusterArray(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Build Cluster Array", chunks=1)
        LVNode.addTerminal(self, "array of clusters", varType="Array", isInput=False)
        LVNode.addTerminal(self, "component element", varType="Void")
        self.attributes["type"] = "Build Cluster Array"


class BuildMap(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Build Map", chunks=1)
        LVNode.addTerminal(self, "map", varType="Map Collection", isInput=False)
        LVNode.addTerminal(self, "key", varType="String")
        LVNode.addTerminal(self, "value", varType="I32")
        self.attributes["type"] = "Build Map"


class BuildMatrix(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Build Matrix", chunks=1)
        LVNode.addTerminal(self, "appended array", varType="Array", isInput=False)
        LVNode.addTerminal(self, "element", varType="Array")
        self.attributes["type"] = "Build Matrix"


class BuildSet(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Build Set", chunks=1)
        LVNode.addTerminal(self, "set", varType="Set Collection", isInput=False)
        LVNode.addTerminal(self, "element", varType="String")
        self.attributes["type"] = "Build Set"


class BuildWaveform(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Build Waveform", chunks=1)
        LVNode.addTerminal(self, "output waveform", varType="Waveform", isInput=False)
        LVNode.addTerminal(self, "waveform", varType="Waveform")
        LVNode.addTerminal(self, "Y", varType="Array")
        self.attributes["type"] = "Build Waveform"


class Bundle(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Bundle", chunks=2)
        LVNode.addTerminal(self, "output cluster", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "cluster", varType="Cluster")
        LVNode.addTerminal(self, "term1", varType="Void")
        LVNode.addTerminal(self, "term2", varType="Void")
        self.attributes["type"] = "Bundle"


class BundleByName(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Bundle By Name", chunks=1)
        LVNode.addTerminal(self, "output cluster", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "input cluster", varType="Cluster")
        LVNode.addTerminal(self, "element", varType="Void")
        self.attributes["type"] = "Bundle By Name"


class CallLibraryFunctionNode(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Call Library Function Node", chunks=1)
        LVNode.addTerminal(self, "path in", varType="Path")
        LVNode.addTerminal(self, "path out", varType="Path", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        # LVNode.addTerminal(self, "", varType="Void")
        # LVNode.addTerminal(self, "", varType="Void", isInput=False)
        self.attributes["type"] = "Call Library Function Node"


class CallMatlabFunction(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Call MATLAB Function", chunks=1)
        LVNode.addTerminal(self, "session in", varType="Refnum")
        LVNode.addTerminal(self, "session out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "source file path", varType="Path")
        LVNode.addTerminal(self, "function name", varType="Path", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="String")
        LVNode.addTerminal(self, "error out", varType="String", isInput=False)
        LVNode.addTerminal(self, "function name", varType="Cluster")
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error out", varType="Void")
        LVNode.addTerminal(self, "return type", varType="Void", isInput=False)
        self.attributes["type"] = "Call MATLAB Function"


class CodeInterfaceNode(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Code Interface Node", chunks=1)
        LVNode.addTerminal(self, "input", varType="Void")
        LVNode.addTerminal(self, "output", varType="Void", isInput=False)
        self.attributes["type"] = "Code Interface Node"


class CompoundArithmetic(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Compound Arithmetic", chunks=2)
        LVNode.addTerminal(self, "result", varType="Double Float", isInput=False)
        LVNode.addTerminal(self, "value", varType="Double Float")
        LVNode.addTerminal(self, "value", varType="Double Float")
        self.attributes["type"] = "Compound Arithmetic"


class ConcatenateStrings(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Concatenate Strings", chunks=2)
        LVNode.addTerminal(self, "concatenated string", varType="String", isInput=False)
        LVNode.addTerminal(self, "string", varType="String")
        LVNode.addTerminal(self, "string", varType="String")
        self.attributes["type"] = "Concatenate Strings"


class ConstructorNode(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Constructor Node", chunks=1)
        LVNode.addTerminal(self, "new reference", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        self.attributes["type"] = "Constructor Node"


class Decimate1dArray(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Decimate 1D Array", chunks=2)
        LVNode.addTerminal(self, "array", varType="Array")
        LVNode.addTerminal(self, "decimated array", varType="Array", isInput=False)
        LVNode.addTerminal(self, "decimated array", varType="Array", isInput=False)
        self.attributes["type"] = "Decimate 1D Array"


class DeleteFromArray(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Delete From Array", chunks=1)
        LVNode.addTerminal(self, "deleted portion", varType="Void", isInput=False)
        LVNode.addTerminal(self, "array", varType="Array")
        LVNode.addTerminal(self, "length", varType="I32")
        LVNode.addTerminal(self, "array w/ subset deleted", varType="Void", isInput=False)
        LVNode.addTerminal(self, "index", varType="I32")
        self.attributes["type"] = "Delete From Array"


class FormatIntoFile(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Format Into File", chunks=1)
        LVNode.addTerminal(self, "format string", varType="String")
        LVNode.addTerminal(self, "input file", varType="Path")
        LVNode.addTerminal(self, "output file refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "input 1", varType="Double Float")
        self.attributes["type"] = "Format Into File"


class FormatIntoString(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Format Into String", chunks=1)
        LVNode.addTerminal(self, "format string", varType="String")
        LVNode.addTerminal(self, "initial string", varType="String")
        LVNode.addTerminal(self, "resulting string", varType="String", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "input 1", varType="Double Float")
        self.attributes["type"] = "Format Into String"


class GetFixedPointComponents(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Get Fixed-Point Components", chunks=1)
        LVNode.addTerminal(self, "input fixed-point number", varType="Fixed Point")
        LVNode.addTerminal(self, "Encoding", varType="Cluster", isInput=False)
        self.attributes["type"] = "Get Fixed-Point Components"


class GetMatrixDiagonal(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Get Matrix Diagonal", chunks=1)
        LVNode.addTerminal(self, "matrix", varType="Array")
        LVNode.addTerminal(self, "diagonal", varType="Array", isInput=False)
        LVNode.addTerminal(self, "index (row)", varType="I32")
        LVNode.addTerminal(self, "index (col)", varType="I32")
        self.attributes["type"] = "Get Matrix Diagonal"


class GetMatrixElements(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Get Matrix Elements", chunks=1)
        LVNode.addTerminal(self, "matrix", varType="Array")
        LVNode.addTerminal(self, "output matrix", varType="Array", isInput=False)
        LVNode.addTerminal(self, "index (row)", varType="I32")
        LVNode.addTerminal(self, "index (col)", varType="I32")
        self.attributes["type"] = "Get Matrix Elements"


class GetSubmatrix(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Get Submatrix", chunks=1)
        LVNode.addTerminal(self, "matrix", varType="Array")
        LVNode.addTerminal(self, "submatrix", varType="Array", isInput=False)
        LVNode.addTerminal(self, "row 1", varType="I32")
        LVNode.addTerminal(self, "row N", varType="I32")
        LVNode.addTerminal(self, "column 1", varType="I32")
        LVNode.addTerminal(self, "column N", varType="I32")
        self.attributes["type"] = "Get Submatrix"


class GetWaveformComponents(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Get Waveform Components", chunks=1)
        LVNode.addTerminal(self, "waveform", varType="Waveform")
        LVNode.addTerminal(self, "Y", varType="Array", isInput=False)
        self.attributes["type"] = "Get Waveform Components"


class IndexBundleClusterArray(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Index & Bundle Cluster Array", chunks=1)
        LVNode.addTerminal(self, "array of clusters", varType="Array", isInput=False)
        LVNode.addTerminal(self, "component array", varType="Void")
        self.attributes["type"] = "Index & Bundle Cluster Array"


class IndexArray(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Index Array", chunks=1)
        LVNode.addTerminal(self, "array", varType="Array")
        LVNode.addTerminal(self, "element", varType="Void", isInput=False)
        LVNode.addTerminal(self, "index", varType="I32")
        self.attributes["type"] = "Index Array"


class InitializeArray(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Initialize Array", chunks=1)
        LVNode.addTerminal(self, "element", varType="Double Float")
        LVNode.addTerminal(self, "initialized array", varType="Array", isInput=False)
        LVNode.addTerminal(self, "dimension size", varType="I32")
        self.attributes["type"] = "Initialize Array"


class InsertIntoArray(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Insert Into Array", chunks=2)
        LVNode.addTerminal(self, "array", varType="Array")
        LVNode.addTerminal(self, "output array", varType="Void", isInput=False)
        LVNode.addTerminal(self, "index", varType="I32")
        LVNode.addTerminal(self, "new element/subarray", varType="Double Float")
        self.attributes["type"] = "Insert Into Array"


class Interleave1dArrays(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Interleave 1D Arrays", chunks=2)
        LVNode.addTerminal(self, "interleaved array", varType="Array", isInput=False)
        LVNode.addTerminal(self, "array", varType="Array")
        LVNode.addTerminal(self, "array", varType="Array")
        self.attributes["type"] = "Interleave 1D Arrays"


class InvokeNode(ObjectFunction):
    def __init__(self):
        ObjectFunction.__init__(self, "Invoke Node", chunks=1)
        LVNode.addTerminal(self, "reference", varType="Refnum")
        LVNode.addTerminal(self, "reference out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "Method", varType="Void")
        LVNode.addTerminal(self, "Method", varType="Void", isInput=False)
        self.attributes["type"] = "Invoke Node"


class MergeErrors(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Merge Errors", chunks=2)
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "error in", varType="Cluster")
        self.attributes["type"] = "Merge Errors"


class MergeSignals(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Merge Signals", chunks=2)
        LVNode.addTerminal(self, "combined signal", varType="ExpressData", isInput=False)
        LVNode.addTerminal(self, "input signal", varType="ExpressData")
        LVNode.addTerminal(self, "input signal", varType="ExpressData")
        self.attributes["type"] = "Merge Signals"


class PropertyNode(ObjectFunction):
    def __init__(self):
        ObjectFunction.__init__(self, "Property Node", chunks=1)
        LVNode.addTerminal(self, "reference", varType="Refnum")
        LVNode.addTerminal(self, "reference out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "Property", varType="Void", isInput=False)
        self.attributes["type"] = "Property Node"


class PythonNode(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Python Node", chunks=1)
        LVNode.addTerminal(self, "session in", varType="Refnum")
        LVNode.addTerminal(self, "session out", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "module in", varType="Path")
        LVNode.addTerminal(self, "module out", varType="Path", isInput=False)
        # LVNode.addTerminal(self, "module out", varType="String")
        LVNode.addTerminal(self, "function name in", varType="String", isInput=True)
        # LVNode.addTerminal(self, "function name in", varType="Cluster")
        LVNode.addTerminal(self, "function name out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Void")
        LVNode.addTerminal(self, "error out", varType="Void", isInput=False)
        self.attributes["type"] = "Python Node"


class RegisterEventCallback(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Register Event Callback", chunks=1)
        LVNode.addTerminal(self, "event callback refnum", varType="Refnum")
        LVNode.addTerminal(self, "event callback refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "event source", varType="Void")
        LVNode.addTerminal(self, "VI Ref", varType="Void")
        LVNode.addTerminal(self, "User Parameter", varType="LV Variant")
        self.attributes["type"] = "Register Event Callback"


class RegisterForEvents(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Register For Events", chunks=1)
        LVNode.addTerminal(self, "event registration refnum", varType="Refnum")
        LVNode.addTerminal(self, "event registration refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in (no error)", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "event source", varType="Void")
        self.attributes["type"] = "Register For Events"


class ReplaceArraySubset(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Replace Array Subset", chunks=1)
        LVNode.addTerminal(self, "array", varType="Array")
        LVNode.addTerminal(self, "output array", varType="Array", isInput=False)
        LVNode.addTerminal(self, "new element/subarray", varType="Double Float")
        LVNode.addTerminal(self, "index", varType="I32")
        self.attributes["type"] = "Replace Array Subset"


class ReshapeArray(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Reshape Array", chunks=1)
        LVNode.addTerminal(self, "array", varType="Array")
        LVNode.addTerminal(self, "output array", varType="Array", isInput=False)
        LVNode.addTerminal(self, "dimension size", varType="I32")
        self.attributes["type"] = "Reshape Array"


class ScanFromFile(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Scan From File", chunks=1)
        LVNode.addTerminal(self, "format string", varType="String")
        LVNode.addTerminal(self, "input file", varType="Refnum")
        LVNode.addTerminal(self, "output file refnum", varType="Refnum", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "default value 1", varType="Double Float")
        LVNode.addTerminal(self, "output 1", varType="Double Float", isInput=False)
        self.attributes["type"] = "Scan From File"


class ScanFromString(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Scan From String", chunks=1)
        LVNode.addTerminal(self, "format string", varType="String")
        LVNode.addTerminal(self, "input string", varType="String")
        LVNode.addTerminal(self, "remaining string", varType="String", isInput=False)
        LVNode.addTerminal(self, "initial scan location", varType="U32")
        LVNode.addTerminal(self, "offset past scan", varType="U32", isInput=False)
        LVNode.addTerminal(self, "error in", varType="Cluster")
        LVNode.addTerminal(self, "error out", varType="Cluster", isInput=False)
        LVNode.addTerminal(self, "default value 1", varType="Double Float")
        LVNode.addTerminal(self, "output 1", varType="Double Float", isInput=False)
        self.attributes["type"] = "Scan From String"


class SetMatrixDiagonal(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Set Matrix Diagonal", chunks=1)
        LVNode.addTerminal(self, "matrix", varType="Array")
        LVNode.addTerminal(self, "output matrix", varType="Array", isInput=False)
        LVNode.addTerminal(self, "new diagonal/fill element", varType="Double Float")
        LVNode.addTerminal(self, "disabled index (row)", varType="I32")
        LVNode.addTerminal(self, "index (col)", varType="I32")
        self.attributes["type"] = "Set Matrix Diagonal"


class SetMatrixElements(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Set Matrix Elements", chunks=1)
        LVNode.addTerminal(self, "matrix", varType="Array")
        LVNode.addTerminal(self, "output matrix", varType="Array", isInput=False)
        LVNode.addTerminal(self, "new element/submatrix", varType="Double Float")
        LVNode.addTerminal(self, "disabled index (row)", varType="I32")
        LVNode.addTerminal(self, "index (col)", varType="I32")
        self.attributes["type"] = "Set Matrix Elements"


class SetSubmatrix(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Set Submatrix", chunks=1)
        LVNode.addTerminal(self, "matrix", varType="Array")
        LVNode.addTerminal(self, "output matrix", varType="Array", isInput=False)
        LVNode.addTerminal(self, "new submatrix/fill element", varType="Double Float")
        LVNode.addTerminal(self, "row 1", varType="I32")
        LVNode.addTerminal(self, "row N", varType="I32")
        LVNode.addTerminal(self, "column 1", varType="I32")
        LVNode.addTerminal(self, "column N", varType="I32")
        self.attributes["type"] = "Set Submatrix"


class SplitSignals(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Split Signals", chunks=2)
        LVNode.addTerminal(self, "combined signal", varType="ExpressData")
        LVNode.addTerminal(self, "output signal", varType="ExpressData", isInput=False)
        LVNode.addTerminal(self, "combined signal", varType="ExpressData")
        self.attributes["type"] = "Split Signals"


class Unbundle(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Unbundle", chunks=2)
        LVNode.addTerminal(self, "cluster", varType="Cluster")
        LVNode.addTerminal(self, "term1", varType="Void", isInput=False)
        LVNode.addTerminal(self, "term2", varType="Void", isInput=False)
        self.attributes["type"] = "Unbundle"


class UnbundleByName(GrowableFunction):
    def __init__(self):
        GrowableFunction.__init__(self, "Unbundle By Name", chunks=1)
        LVNode.addTerminal(self, "input cluster", varType="Cluster")
        LVNode.addTerminal(self, "element", varType="Void", isInput=False)
        self.attributes["type"] = "Unbundle By Name"
