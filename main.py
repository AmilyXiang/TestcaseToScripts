import argparse
import json
import subprocess
import sys
from pathlib import Path

from testrail_parser import parse_testrail_excel


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Testcase processing entrypoint.")
    subparsers = parser.add_subparsers(dest="command")

    parse_parser = subparsers.add_parser("parse", help="Parse TestRail Excel into structured JSON.")
    parse_parser.add_argument(
        "--input",
        type=Path,
        default=Path("RQPLEIAD 180 -Alarm button improvemen 12_29.xlsx"),
        help="Path to the TestRail Excel file.",
    )
    parse_parser.add_argument(
        "--sheet",
        type=str,
        default=None,
        help="Optional sheet name to parse. If omitted, all sheets are parsed.",
    )
    parse_parser.add_argument(
        "--output",
        type=Path,
        default=Path("parsed_testrail.json"),
        help="Path to save parsed JSON result.",
    )

    kb_parser = subparsers.add_parser("build-kb", help="Build normalized KB from parsed JSON using DeepSeek.")
    kb_parser.add_argument("--input", type=Path, default=Path("parsed_testrail.json"))
    kb_parser.add_argument("--skill", type=Path, default=Path("skills/step_result_unify_skill.md"))
    kb_parser.add_argument("--output", type=Path, default=Path("normalized_kb.json"))
    kb_parser.add_argument("--model", type=str, default="deepseek-chat")
    kb_parser.add_argument("--api-key", type=str, default=None)

    return parser


def run_parse(input_path: Path, output_path: Path, sheet: str | None) -> None:
    parsed = parse_testrail_excel(input_path, sheet)

    output_path.write_text(
        json.dumps(parsed, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    total_cases = sum(len(cases) for cases in parsed.values())
    total_steps = sum(len(case["steps"]) for cases in parsed.values() for case in cases)
    print(f"Parsed file: {input_path}")
    print(f"Sheets parsed: {len(parsed)}")
    print(f"Total cases: {total_cases}")
    print(f"Total steps: {total_steps}")
    print(f"Output JSON: {output_path}")


def run_build_kb(input_path: Path, skill_path: Path, output_path: Path, model: str, api_key: str | None) -> None:
    command = [
        sys.executable,
        "build_step_result_kb.py",
        "--input",
        str(input_path),
        "--skill",
        str(skill_path),
        "--output",
        str(output_path),
        "--model",
        model,
    ]
    if api_key:
        command.extend(["--api-key", api_key])
    subprocess.run(command, check=True)


def main() -> None:
    args = build_arg_parser().parse_args()

    if args.command in (None, "parse"):
        run_parse(args.input, args.output, args.sheet)
        return

    if args.command == "build-kb":
        run_build_kb(args.input, args.skill, args.output, args.model, args.api_key)
        return

    raise ValueError(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    main()
