This project originated as an idea to have LLMs generate LabVIEW VIs by way of transpiling Go code. At the time, LLMs could only really generate code from existing languages. As LLMs have become more powerful, the repository now relies solely on the Python graph builder in `python/lvgpt/build.py` and the accompanying node classes to synthesize LabVIEW diagrams. The previous Go AST tooling has been removed to simplify the pipeline.

## Getting started (Python package)

Install the package in editable mode and invoke the CLI to convert an AST XML document into LabVIEW VI XML:

```
pip install -e .
lvgpt-build path/to/ast.xml -o path/to/output.vi.xml
```

The CLI expects the AST to contain `<BlockStmt>` elements; the helper functions in `lvgpt.build` can also be imported directly for programmatic usage.

If you cannot install dependencies in your environment, set `PYTHONPATH=python` and invoke `python -m lvgpt.cli --help` from the repository root.

See `NEXT_STEPS.md` for the prioritized work to keep improving the Python-only workflow.
