"""Generate an LLM prompt bundle for Graph IR generation."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PYTHON_ROOT = REPO_ROOT / "python"
if str(PYTHON_ROOT) not in sys.path:
    sys.path.insert(0, str(PYTHON_ROOT))

from lvgpt.catalog import build_llm_catalog
from lvgpt.graph_ir import GRAPH_IR_SCHEMA


DEFAULT_OUTPUT = Path("llm_graph_ir_prompt.txt")


def build_prompt(user_request: str) -> str:
    schema_text = json.dumps(GRAPH_IR_SCHEMA, indent=2, sort_keys=True)
    catalog_text = json.dumps(build_llm_catalog(), indent=2, sort_keys=True)

    return "\n".join(
        [
            "You generate ONLY JSON that matches this schema and uses ONLY node kinds from the catalog.",
            "No prose, no markdown, no code fences.",
            "",
            "Schema:",
            schema_text,
            "",
            "Reduced node catalog:",
            catalog_text,
            "",
            "Task:",
            user_request.strip(),
            "",
        ]
    )


def main() -> None:
    user_request = input("Describe the VI you want the LLM to generate: ").strip()
    if not user_request:
        raise SystemExit("No prompt provided.")

    output_path_text = input(
        f"Output file path [{DEFAULT_OUTPUT.as_posix()}]: "
    ).strip()
    output_path = Path(output_path_text) if output_path_text else DEFAULT_OUTPUT

    prompt_text = build_prompt(user_request)
    output_path.write_text(prompt_text)
    print(f"Wrote LLM prompt bundle to {output_path}")


if __name__ == "__main__":
    main()
