# LVGPT

LVGPT explores generating LabVIEW block diagrams from LLM-produced code. The early pipeline transpiled Go, but the repository now focuses on a Python-only graph builder that turns AST XML into LabVIEW VI XML. The Go AST tooling has been removed to keep the project focused on a single implementation.

## Repository layout
- `python/lvgpt`: package entry points for AST-to-graph conversion
- `python/lvgpt/lvgraph`: LabVIEW graph data structures and nodes
- `LabVIEW/`: example assets, XML fixtures, and helper data

## Quick start
1. Install the package from the repo root:
   - `pip install -e .`
2. Run the CLI on an AST XML file:
   - `lvgpt-build path/to/ast.xml -o output.vi.xml`

## Examples
- `examples/simple_ast.xml` includes a tiny AST that prints `a + b`.
- `examples/simple_ast.vi.xml` is the expected LabVIEW XML output for that AST.

## Graph IR (LLM output)
The preferred LLM interface is a small JSON/YAML graph IR that maps directly to nodes and wires.

Example:
```json
{
  "nodes": [
    {"id": "a", "kind": "NumericConstant", "params": {"name": "a", "numType": "Long", "value": "1"}},
    {"id": "b", "kind": "NumericConstant", "params": {"name": "b", "numType": "Long", "value": "2"}},
    {"id": "add", "kind": "Add"},
    {"id": "out", "kind": "NumericIndicator", "params": {"name": "output", "numType": "Long"}}
  ],
  "edges": [
    {"from": "a.a", "to": "add.x"},
    {"from": "b.b", "to": "add.y"},
    {"from": "add.x+y", "to": "out.output"}
  ]
}
```

You can build a graph from the IR with:
- `from lvgpt.graph_ir import parse_graph_ir, build_graph_from_spec`
Edges can also be written with explicit fields:
```json
{"from_node": "add", "from_terminal": "x+y", "to_node": "out", "to_terminal": "output"}
```

YAML support requires `PyYAML` to be installed, and schema validation uses `jsonschema` when available.

CLI:
- `lvgpt-build-ir path/to/graph_ir.json -o output.vi.xml`

## Node catalog
The node catalog is generated at runtime from available `LVNode` subclasses:
- `from lvgpt.catalog import build_node_catalog`

## Testing
1. Install test dependencies:
   - `pip install -e .[dev]`
2. Run pytest (with the repo Python package on the path):
   - `PYTHONPATH=python pytest`

## Status
This is an experimental toolchain. Expect the AST coverage and node vocabulary to evolve as more test cases are added.
