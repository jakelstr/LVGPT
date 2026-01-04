"""Command-line entry point for building LabVIEW VIs from Graph IR."""

import argparse
import pathlib

from .graph_ir import build_graph_from_spec, load_graph_ir


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        type=pathlib.Path,
        help="Path to a Graph IR JSON/YAML file to convert into LabVIEW VI XML.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=pathlib.Path,
        required=False,
        help="Optional destination path for the generated VI XML.",
    )
    parser.add_argument(
        "--no-layout",
        action="store_true",
        help="Skip auto-layout for the generated VI XML.",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    output_path = args.output or args.input.with_suffix(".vi.xml")
    spec = load_graph_ir(args.input)
    graph = build_graph_from_spec(spec, layout=not args.no_layout)
    graph.writeXML(args.input.stem, output_path)

    print(f"Wrote LabVIEW VI XML to {output_path}")


if __name__ == "__main__":
    main()
