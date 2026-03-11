import argparse
import json
import re
from pathlib import Path
from typing import Any

TARGET_FIELDS = ("action_substeps", "expected_checkpoints", "expected_result")
MERGE_LIST_FIELDS = ("action_substeps", "expected_checkpoints")
SOFT_WRAP_ONLY_FIELDS = ("action",)


def has_oxo(text: str) -> bool:
    return "oxo" in text.lower()


def should_merge_wrapped(prev: str, curr: str) -> bool:
    if not prev or not curr:
        return False

    prev_tail = prev.rstrip()
    curr_head = curr.lstrip()
    if not prev_tail or not curr_head:
        return False

    # Keep explicit sentence boundaries as hard splits.
    if prev_tail.endswith((".", "!", "?", ":", ";")):
        return False

    first = curr_head[0]

    # Typical soft-wrap continuation: starts with lowercase, digit, or closing punctuation.
    if first.islower() or first.isdigit() or first in (")", "]", "}", ",", "."):
        return True

    # Hard-wrap continuation for single-letter tokens, e.g. "phone" + "B, ...".
    if re.match(r"^[A-Z](?:\b|[\),\.:;])", curr_head):
        return True

    # If previous line ends with connectors, current line likely continues the same thought.
    if prev_tail.endswith(("(", "[", "{", "=", "/", "-")):
        return True

    return False


def collapse_soft_wrapped_lines(text: str) -> str:
    parts = [line.strip() for line in text.splitlines() if line.strip()]
    if not parts:
        return ""

    merged: list[str] = [parts[0]]
    for part in parts[1:]:
        if should_merge_wrapped(merged[-1], part):
            merged[-1] = f"{merged[-1].rstrip()} {part.lstrip()}"
        else:
            merged.append(part)
    return "\n".join(merged)


def merge_wrapped_list(values: list[Any]) -> list[Any]:
    merged: list[Any] = []
    for item in values:
        if not isinstance(item, str):
            merged.append(item)
            continue

        text = item.strip()
        if not text:
            continue

        if merged and isinstance(merged[-1], str) and should_merge_wrapped(merged[-1], text):
            merged[-1] = f"{merged[-1].rstrip()} {text.lstrip()}"
        else:
            merged.append(text)

    return merged


def clean_string(value: str) -> str | None:
    # Drop full lines that contain OXO-related variants.
    kept_lines = [line for line in value.splitlines() if not has_oxo(line)]
    cleaned = "\n".join(line for line in kept_lines if line.strip()).strip()
    cleaned = collapse_soft_wrapped_lines(cleaned)
    return cleaned or None


def clean_list(values: list[Any]) -> list[Any]:
    cleaned: list[Any] = []
    for item in values:
        if isinstance(item, str):
            if has_oxo(item):
                continue
            stripped = item.strip()
            if stripped:
                cleaned.append(stripped)
        else:
            cleaned.append(item)
    return cleaned


def process_step(step: dict[str, Any]) -> tuple[dict[str, Any], int]:
    removed_count = 0
    for field in TARGET_FIELDS:
        if field not in step:
            continue

        value = step[field]
        if isinstance(value, str):
            before = value
            after = clean_string(value)
            if after != before:
                removed_count += 1
            if after is None:
                step.pop(field, None)
            else:
                step[field] = after
        elif isinstance(value, list):
            before_len = len(value)
            after_list = clean_list(value)
            if field in MERGE_LIST_FIELDS:
                after_list = merge_wrapped_list(after_list)
            if len(after_list) != before_len:
                removed_count += 1
            if after_list:
                step[field] = after_list
            else:
                step.pop(field, None)

    # Apply soft-wrap collapse to action text as well (no OXO filtering here).
    for field in SOFT_WRAP_ONLY_FIELDS:
        value = step.get(field)
        if not isinstance(value, str):
            continue
        collapsed = collapse_soft_wrapped_lines(value.strip())
        if collapsed != value:
            removed_count += 1
            step[field] = collapsed

    return step, removed_count


def process_file(input_path: Path, output_path: Path) -> None:
    data = json.loads(input_path.read_text(encoding="utf-8"))

    worksheet = data.get("Worksheet", [])
    if not isinstance(worksheet, list):
        worksheet = []
    touched_steps = 0
    modified_fields = 0
    removed_cases = 0
    kept_cases: list[dict[str, Any]] = []

    for case in worksheet:
        if not isinstance(case, dict):
            continue

        steps = case.get("steps", [])
        if not isinstance(steps, list):
            steps = []
            case["steps"] = steps

        for i, step in enumerate(steps):
            if not isinstance(step, dict):
                continue
            updated_step, removed = process_step(step)
            steps[i] = updated_step
            if removed > 0:
                touched_steps += 1
                modified_fields += removed

        if len(steps) == 0:
            removed_cases += 1
            continue

        kept_cases.append(case)

    data["Worksheet"] = kept_cases

    output_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Input: {input_path}")
    print(f"Output: {output_path}")
    print(f"Touched steps: {touched_steps}")
    print(f"Modified field instances: {modified_fields}")
    print(f"Removed empty-step cases: {removed_cases}")
    print(f"Remaining cases: {len(kept_cases)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Remove OXO-related content from selected step fields."
    )
    parser.add_argument("--input", required=True, help="Input cleaned JSON file")
    parser.add_argument("--output", required=True, help="Output JSON file")
    args = parser.parse_args()

    process_file(Path(args.input), Path(args.output))
