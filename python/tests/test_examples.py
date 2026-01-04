import uuid
from pathlib import Path

from lvgpt.build import build_from_ast_file


def _deterministic_uuid_factory():
    counter = {"value": 0}

    def _uuid4():
        counter["value"] += 1
        return uuid.UUID(int=counter["value"])

    return _uuid4


def test_simple_ast_example(tmp_path, monkeypatch):
    monkeypatch.setattr(uuid, "uuid4", _deterministic_uuid_factory())

    repo_root = Path(__file__).resolve().parents[2]
    ast_path = repo_root / "examples" / "simple_ast.xml"
    golden_path = repo_root / "examples" / "simple_ast.vi.xml"
    output_path = tmp_path / "simple_ast.vi.xml"

    build_from_ast_file(ast_path, output_path=output_path)

    assert output_path.read_text() == golden_path.read_text()
