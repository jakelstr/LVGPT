"""Graph IR parsing and LVGraph construction."""

from __future__ import annotations

import json
import inspect
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from .catalog import build_node_catalog
from .lvgraph import LVGraph, LVNode


@dataclass
class NodeSpec:
    node_id: str
    kind: str
    name: Optional[str] = None
    args: Optional[List[Any]] = None
    params: Optional[Dict[str, Any]] = None
    extra_terminals: int = 0


@dataclass
class EdgeSpec:
    from_node: str
    from_terminal: str
    to_node: str
    to_terminal: str


@dataclass
class GraphSpec:
    nodes: List[NodeSpec]
    edges: List[EdgeSpec]


GRAPH_IR_SCHEMA = {
    "type": "object",
    "required": ["nodes", "edges"],
    "properties": {
        "nodes": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "kind"],
                "properties": {
                    "id": {"type": "string"},
                    "kind": {"type": "string"},
                    "name": {"type": "string"},
                    "args": {"type": "array"},
                    "params": {"type": "object"},
                    "extra_terminals": {"type": "integer", "minimum": 0},
                },
            },
        },
        "edges": {
            "type": "array",
            "items": {
                "type": "object",
                "oneOf": [
                    {
                        "required": ["from", "to"],
                        "properties": {
                            "from": {"type": "string"},
                            "to": {"type": "string"},
                        },
                    },
                    {
                        "required": ["from_node", "from_terminal", "to_node", "to_terminal"],
                        "properties": {
                            "from_node": {"type": "string"},
                            "from_terminal": {"type": "string"},
                            "to_node": {"type": "string"},
                            "to_terminal": {"type": "string"},
                        },
                    },
                ],
            },
        },
    },
}


def parse_graph_ir(text: str) -> GraphSpec:
    """Parse JSON or YAML Graph IR into a GraphSpec."""

    data = _load_json_or_yaml(text)
    validate_graph_ir(data)
    return _graph_spec_from_dict(data)


def load_graph_ir(path: Path) -> GraphSpec:
    """Load Graph IR from disk."""

    text = Path(path).read_text()
    return parse_graph_ir(text)


def build_graph_from_spec(spec: GraphSpec, layout: bool = True) -> LVGraph:
    """Build an LVGraph from a GraphSpec."""

    catalog = build_node_catalog()
    class_map = _class_map_from_catalog(catalog)

    graph = LVGraph()
    nodes_by_id: Dict[str, LVNode] = {}

    for node_spec in spec.nodes:
        node_cls = class_map.get(node_spec.kind)
        if node_cls is None:
            raise ValueError(f"Unknown node kind: {node_spec.kind}")
        node = _instantiate_node(node_cls, node_spec)
        graph.addNode(node)
        nodes_by_id[node_spec.node_id] = node

        extra = node_spec.extra_terminals or 0
        for _ in range(extra):
            if _can_auto_add_terminal(node):
                node.addTerminal()
            else:
                raise ValueError(
                    f"Node {node_spec.node_id} does not support automatic extra terminals"
                )

    for edge in spec.edges:
        from_node = nodes_by_id[edge.from_node]
        to_node = nodes_by_id[edge.to_node]
        from_term = _resolve_terminal(from_node, edge.from_terminal, "out", edge.from_node)
        to_term = _resolve_terminal(to_node, edge.to_terminal, "in", edge.to_node)
        graph.addTerminalEdge(from_term.uuid, to_term.uuid)

    if layout:
        graph.finalize_layout()

    return graph


def _instantiate_node(node_cls: type, node_spec: NodeSpec) -> LVNode:
    params = dict(node_spec.params or {})
    args = list(node_spec.args or [])
    signature = inspect.signature(node_cls)
    param_names = [p.name for p in signature.parameters.values() if p.name != "self"]

    if "name" in param_names and "name" not in params and not args:
        params["name"] = node_spec.name or node_spec.node_id

    if args:
        node = node_cls(*args)
    else:
        node = node_cls(**params)

    if "name" in node.__dict__ and node_spec.name:
        node.name = node_spec.name
        node.attributes["name"] = node_spec.name

    value = params.get("value")
    if value is not None and hasattr(node, "setValue"):
        node.setValue(value)

    return node


def _graph_spec_from_dict(data: Dict[str, Any]) -> GraphSpec:
    nodes = []
    for node in data.get("nodes", []):
        nodes.append(
            NodeSpec(
                node_id=node["id"],
                kind=node["kind"],
                name=node.get("name"),
                args=node.get("args"),
                params=node.get("params"),
                extra_terminals=int(node.get("extra_terminals", 0)),
            )
        )

    edges = []
    for edge in data.get("edges", []):
        if "from_node" in edge:
            from_node = edge["from_node"]
            from_term = edge["from_terminal"]
            to_node = edge["to_node"]
            to_term = edge["to_terminal"]
        else:
            from_node, from_term = _split_endpoint(edge["from"])
            to_node, to_term = _split_endpoint(edge["to"])
        edges.append(
            EdgeSpec(
                from_node=from_node,
                from_terminal=from_term,
                to_node=to_node,
                to_terminal=to_term,
            )
        )

    return GraphSpec(nodes=nodes, edges=edges)


def _class_map_from_catalog(catalog: Dict[str, Any]) -> Dict[str, type]:
    from . import nodes
    from .lvgraph import functions

    class_map: Dict[str, type] = {}
    for module in (nodes, functions):
        for value in module.__dict__.values():
            if inspect.isclass(value) and issubclass(value, LVNode) and value is not LVNode:
                class_map[value.__name__] = value
    return class_map


def _split_endpoint(value: str) -> Tuple[str, Optional[str]]:
    if "." not in value:
        if ":" in value:
            raise ValueError(
                f"Invalid endpoint format: {value}. Use 'node_id.terminal_name'."
            )
        return value, None
    node_id, terminal = value.split(".", 1)
    return node_id, terminal


def _resolve_terminal(node: LVNode, terminal_name: Optional[str], direction: str, node_id: str):
    terminals = list(node.terminals.values())
    if terminal_name:
        term = node.getTerminalByName(terminal_name)
        if term is None:
            suggestions = _suggest_terminal(terminal_name, node)
            message = f"Missing terminal {terminal_name} on {node_id}."
            if suggestions:
                message += f" Did you mean: {', '.join(suggestions)}?"
            raise ValueError(message)
        return term

    if direction == "out":
        candidates = [term for term in terminals if not term.isInput]
    else:
        candidates = [term for term in terminals if term.isInput]

    if len(candidates) == 1:
        return candidates[0]

    if not candidates:
        raise ValueError(f"No {direction} terminals found on {node_id}.")

    names = ", ".join(sorted(term.name for term in candidates))
    raise ValueError(
        f"Ambiguous {direction} terminal on {node_id}. Choose one of: {names}."
    )


def _suggest_terminal(target: str, node: LVNode) -> List[str]:
    import difflib

    names = [term.name for term in node.terminals.values()]
    return difflib.get_close_matches(target, names, n=3, cutoff=0.6)


def validate_graph_ir(data: Dict[str, Any]) -> None:
    """Validate IR structure against the JSON schema."""

    try:
        import jsonschema  # type: ignore
    except Exception:
        _validate_graph_ir_basic(data)
        return

    jsonschema.validate(instance=data, schema=GRAPH_IR_SCHEMA)


def _validate_graph_ir_basic(data: Dict[str, Any]) -> None:
    if not isinstance(data, dict):
        raise ValueError("Graph IR must be a JSON/YAML object.")
    if "nodes" not in data or "edges" not in data:
        raise ValueError("Graph IR must include 'nodes' and 'edges'.")
    if not isinstance(data["nodes"], list) or not isinstance(data["edges"], list):
        raise ValueError("'nodes' and 'edges' must be arrays.")
    for node in data["nodes"]:
        if not isinstance(node, dict):
            raise ValueError("Each node must be an object.")
        if "id" not in node or "kind" not in node:
            raise ValueError("Each node must include 'id' and 'kind'.")
    for edge in data["edges"]:
        if not isinstance(edge, dict):
            raise ValueError("Each edge must be an object.")
        if "from" in edge and "to" in edge:
            continue
        if (
            "from_node" not in edge
            or "from_terminal" not in edge
            or "to_node" not in edge
            or "to_terminal" not in edge
        ):
            raise ValueError(
                "Each edge must include 'from'/'to' or "
                "'from_node'/'from_terminal'/'to_node'/'to_terminal'."
            )


def _can_auto_add_terminal(node: LVNode) -> bool:
    add_term = getattr(node, "addTerminal", None)
    if add_term is None:
        return False
    signature = inspect.signature(add_term)
    params = list(signature.parameters.values())
    return len(params) == 0 or (len(params) == 1 and params[0].name == "self")


def _load_json_or_yaml(text: str) -> Dict[str, Any]:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover - optional dependency
        raise RuntimeError("PyYAML not installed; unable to parse YAML.") from exc

    data = yaml.safe_load(text)
    if not isinstance(data, dict):
        raise ValueError("Graph IR must be a JSON/YAML object.")
    return data
