import argparse
import json
from pathlib import Path
from testrail_parser import parse_testrail_excel


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Parse TestRail Excel file into JSON records.")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("RQPLEIAD 180 -Alarm button improvemen 12_29.xlsx"),
        help="Path to the TestRail Excel file.",
    )
    parser.add_argument(
        "--sheet",
        type=str,
        default=None,
        help="Optional sheet name to parse. If omitted, all sheets are parsed.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("parsed_testrail.json"),
        help="Path to save parsed JSON result.",
    )
    return parser


def main() -> None:
    args = build_arg_parser().parse_args()

    parsed = parse_testrail_excel(args.input, args.sheet)

    args.output.write_text(
        json.dumps(parsed, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    total_cases = sum(len(cases) for cases in parsed.values())
    total_steps = sum(len(case["steps"]) for cases in parsed.values() for case in cases)
    print(f"Parsed file: {args.input}")
    print(f"Sheets parsed: {len(parsed)}")
    print(f"Total cases: {total_cases}")
    print(f"Total steps: {total_steps}")
    print(f"Output JSON: {args.output}")


if __name__ == "__main__":
    main()
