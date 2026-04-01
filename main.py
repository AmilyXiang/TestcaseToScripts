import argparse
import json
import subprocess
import sys
from pathlib import Path

from clean_testrail_json import process_file as run_clean_file
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
    kb_parser.add_argument("--max-workers", type=int, default=8)

    clean_parser = subparsers.add_parser("clean", help="Clean parsed TestRail JSON and auto-generate substeps/checkpoints.")
    clean_parser.add_argument("--input", type=Path, default=Path("parsed_testrail.json"))
    clean_parser.add_argument("--output", type=Path, default=Path("cleaned_testrail.json"))

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


def run_build_kb(
    input_path: Path,
    skill_path: Path,
    output_path: Path,
    model: str,
    api_key: str | None,
    max_workers: int,
) -> None:
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
        "--max-workers",
        str(max_workers),
    ]
    if api_key:
        command.extend(["--api-key", api_key])
    subprocess.run(command, check=True)


def run_clean(input_path: Path, output_path: Path) -> None:
    run_clean_file(input_path=input_path, output_path=output_path)


def main() -> None:
    args = build_arg_parser().parse_args()

    if args.command in (None, "parse"):
        run_parse(args.input, args.output, args.sheet)
        return

    if args.command == "build-kb":
        run_build_kb(args.input, args.skill, args.output, args.model, args.api_key, args.max_workers)
        return

    if args.command == "clean":
        run_clean(args.input, args.output)
        return

    raise ValueError(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    main()
