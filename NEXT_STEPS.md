# Next Steps for LVGPT (post-Go removal)

With the Go AST pipeline removed, the repository now hinges on the Python graph builders in `python/`. The new `lvgpt` package and `lvgpt-build` CLI wrap the existing AST-to-graph helpers. The tasks below are prioritized to make the Python-only workflow fully testable and contributor-friendly.

## 1) Examples and validation data
- Keep a dedicated `examples/` directory with sample AST inputs and generated LabVIEW XML for smoke testing.
- Add a minimal golden-file test case that exercises the current AST handling (BlockStmt traversal, binary expressions, and print statements).

## 2) Testing and validation
- Add unit tests for node wiring helpers (e.g., concatenation handling, case structures) and golden-file tests for full graph output.
- Introduce a lightweight CI workflow (GitHub Actions) to run the tests and lint the package with `ruff` or `flake8`.

## 3) Prompting workflow
- Reintroduce a minimal prompting client using the Chat Completions API, capturing prompts, parameters, and outputs for reproducibility.
- Store prompt/response artifacts alongside version metadata so test cases can be regenerated as models evolve.

## 4) Documentation
- Expand `README.md` with an architecture sketch showing how prompts → code → AST → LabVIEW graph flow.
- Add a short contributor guide covering dependency management, coding conventions, and how to run the tests/linters.

These steps will consolidate the Python pipeline, provide a runnable entry point, and establish guardrails for future iteration.
