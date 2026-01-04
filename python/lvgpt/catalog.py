"""Node catalog generation for LVGraph nodes."""

from __future__ import annotations

import inspect
from dataclasses import dataclass, asdict
from typing import Any, Dict, Iterable, List, Optional, Type

from .lvgraph import LVNode


@dataclass
class CatalogTerminal:
    name: str
    direction: str
    var_type: Optional[str] = None


@dataclass
class CatalogEntry:
    class_name: str
    type_name: Optional[str]
    constructor_params: List[str]
    terminals: List[CatalogTerminal]
    instantiation_error: Optional[str] = None


def _iter_node_classes(modules: Iterable[Any]) -> Iterable[Type[LVNode]]:
    for module in modules:
        for value in module.__dict__.values():
            if inspect.isclass(value) and issubclass(value, LVNode) and value is not LVNode:
                yield value


def _placeholder_args_for(signature: inspect.Signature, name: str) -> Dict[str, Any]:
    placeholders = {
        "name": name,
        "numType": "Long",
        "numericType": "Long",
        "id_string": "NumericConstant",
        "path": "path",
        "style": "style",
        "chunks": 1,
    }
    args = {}
    for param in signature.parameters.values():
        if param.name in placeholders:
            args[param.name] = placeholders[param.name]
    return args


def _instantiate_for_catalog(node_cls: Type[LVNode]) -> Optional[LVNode]:
    signature = inspect.signature(node_cls)
    required = [
        param
        for param in signature.parameters.values()
        if param.name != "self" and param.default is inspect._empty
    ]
    if not required:
        return node_cls()

    placeholder_args = _placeholder_args_for(signature, node_cls.__name__.lower())
    missing = [param.name for param in required if param.name not in placeholder_args]
    if missing:
        return None

    return node_cls(**placeholder_args)


def build_node_catalog() -> Dict[str, Any]:
    """Build a catalog of LVNode subclasses and their terminals."""

    from . import nodes  # Local import to avoid circular dependency
    from .lvgraph import functions

    entries: List[CatalogEntry] = []
    for node_cls in sorted(_iter_node_classes([nodes, functions]), key=lambda c: c.__name__):
        signature = inspect.signature(node_cls)
        constructor_params = [
            param.name
            for param in signature.parameters.values()
            if param.name != "self"
        ]
        instantiation_error = None
        terminals: List[CatalogTerminal] = []
        type_name = None
        try:
            instance = _instantiate_for_catalog(node_cls)
            if instance is None:
                raise RuntimeError("Missing placeholder args for constructor")
            type_name = instance.attributes.get("type")
            for term in instance.terminals.values():
                direction = "in" if term.isInput else "out"
                terminals.append(
                    CatalogTerminal(
                        name=term.name,
                        direction=direction,
                        var_type=term.varType,
                    )
                )
        except Exception as exc:
            instantiation_error = str(exc)

        entries.append(
            CatalogEntry(
                class_name=node_cls.__name__,
                type_name=type_name,
                constructor_params=constructor_params,
                terminals=terminals,
                instantiation_error=instantiation_error,
            )
        )

    return {
        "nodes": [asdict(entry) for entry in entries],
    }


def build_llm_catalog() -> Dict[str, Any]:
    """Build a reduced catalog suitable for LLM prompts."""

    full = build_node_catalog()
    reduced_nodes = []
    for node in full.get("nodes", []):
        if node.get("instantiation_error"):
            continue
        terminals = node.get("terminals") or []
        if not terminals:
            continue
        reduced_nodes.append(
            {
                "class_name": node.get("class_name"),
                "type_name": node.get("type_name"),
                "constructor_params": node.get("constructor_params"),
                "terminals": terminals,
            }
        )
    return {"nodes": reduced_nodes}
