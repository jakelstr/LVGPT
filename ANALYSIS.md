# Project Review: LVGPT

## Overview
LVGPT translates LLM-generated code into a LabVIEW block diagram representation by mapping parsed program structures to custom node classes. The repository now centers on the Python graph builder and LabVIEW assets after removing the experimental Go AST traversal. The following assessment highlights notable issues and proposes improvements.

## Strengths
- Demonstrates end-to-end experimentation from prompt creation through Python-based graph modeling.
- Custom LabVIEW node abstractions (e.g., `NumericControl`, `PropertyNode`, `FormatIntoStringsNode`) provide a starting vocabulary for automated VI construction.

## Key Issues Identified
1. **Prompting workflow is undefined**: The previous OpenAI completions script has been removed, leaving no maintained entry point for generating or capturing model outputs alongside metadata.
2. **Monolithic AST processing**: The Python graph builder (`python/readAST.py`) mixes AST parsing helpers with manual graph-construction routines and uses global state, making the pipeline hard to reuse, extend, or reason about.
3. **Lack of cohesive architecture and tooling**: There is no shared package/CLI layout, no configuration management, and no automated validation of generated LabVIEW graphs. Mixed concerns (prompting, AST parsing, graph building) live in separate ad-hoc scripts.
4. **Missing automated tests and documentation**: No unit or integration tests exist to verify graph generation, and the README offers minimal guidance for setup, prompting workflows, or execution steps.

## Recommendations
### Incremental improvements
- Add a small, testable client module that uses the current Chat Completions API, injects model/temperature/prompts via configuration, and captures responses alongside metadata (e.g., prompt, seed, version) for reproducibility.
- Introduce a Python package layout (e.g., `python/src/lvgpt/`) with clear entry points for prompt generation, AST ingestion, and LabVIEW graph assembly. Add minimal CLI scripts or notebooks demonstrating the end-to-end flow.
- Add automated formatting/linting (e.g., `gofmt`, `ruff`), dependency management (requirements/go.mod tidy), and logging instead of `fmt.Println`/bare prints.
- Favor the existing Python AST-to-LVGraph path (`python/readAST.py` + node classes) as the single implementation. The Go prototype has been removed to avoid split ownership.

### Larger refactor
- Define a pipeline abstraction that spans prompt creation → code generation → AST normalization → LabVIEW graph synthesis. Consider gRPC/JSON interfaces between stages so Go and Python components can be swapped independently.
- Model LabVIEW nodes and wiring with typed data structures plus schema validation to catch type mismatches before export. Provide snapshot-based tests that assert generated graphs for sample prompts.
- Expand documentation: architecture diagram, supported constructs, how to run the pipeline locally (including required environment variables like `OPENAI_API_KEY`), and troubleshooting steps.

These changes would make the project more maintainable, reproducible, and ready for iterative experimentation with LLM-driven LabVIEW generation.
