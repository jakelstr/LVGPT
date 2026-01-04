"""Command-line entry point for building LabVIEW VIs from AST XML."""

import argparse
import pathlib
from .build import process


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        type=pathlib.Path,
        help="Path to an AST XML file to convert into a LabVIEW VI XML graph.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=pathlib.Path,
        required=False,
        help="Optional destination path for the generated VI XML.",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    output_path = args.output or args.input.with_suffix(".vi.xml")
    graph = process(args.input, output_path=output_path)

    print(f"Wrote LabVIEW VI XML to {output_path}")


if __name__ == "__main__":
    main()
