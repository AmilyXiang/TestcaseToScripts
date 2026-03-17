from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

from data_cleaning import (
    clean_step_text,
    clean_text_list,
    cleanup_markup_text,
    split_numbered_points,
)


def _derive_list_field(text: Any) -> List[str]:
    """Build deterministic substep/checkpoint list from cleaned text."""
    if not isinstance(text, str) or not text.strip():
        return []

    points = split_numbered_points(text)
    # Only keep list field when it is truly decomposed into multiple atomic items.
    return points if len(points) > 1 else []


def clean_testrail_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    worksheet = payload.get("Worksheet", [])
    if not isinstance(worksheet, list):
        worksheet = []

    touched_steps = 0
    cleaned_fields = 0

    for case in worksheet:
        if not isinstance(case, dict):
            continue

        for field in ("title", "description", "preconditions"):
            value = case.get(field)
            if isinstance(value, str):
                cleaned = cleanup_markup_text(value)
                if cleaned != value:
                    cleaned_fields += 1
                case[field] = cleaned

        steps = case.get("steps", [])
        if not isinstance(steps, list):
            continue

        for step in steps:
            if not isinstance(step, dict):
                continue

            modified = False

            action = step.get("action")
            if isinstance(action, str):
                cleaned_action = clean_step_text(action)
                if cleaned_action != action:
                    cleaned_fields += 1
                    modified = True
                step["action"] = cleaned_action

            expected = step.get("expected_result")
            if isinstance(expected, str):
                cleaned_expected = clean_step_text(expected)
                if cleaned_expected != expected:
                    cleaned_fields += 1
                    modified = True
                step["expected_result"] = cleaned_expected

            if "action_substeps" in step and isinstance(step.get("action_substeps"), list):
                prev = step["action_substeps"]
                cleaned_list = clean_text_list(prev)
                if cleaned_list != prev:
                    cleaned_fields += 1
                    modified = True
                if cleaned_list:
                    step["action_substeps"] = cleaned_list
                else:
                    step.pop("action_substeps", None)

            if "expected_checkpoints" in step and isinstance(step.get("expected_checkpoints"), list):
                prev = step["expected_checkpoints"]
                cleaned_list = clean_text_list(prev)
                if cleaned_list != prev:
                    cleaned_fields += 1
                    modified = True
                if cleaned_list:
                    step["expected_checkpoints"] = cleaned_list
                else:
                    step.pop("expected_checkpoints", None)

            # Auto-generate template fields when absent.
            if "action_substeps" not in step:
                derived_actions = _derive_list_field(step.get("action"))
                if derived_actions:
                    step["action_substeps"] = derived_actions
                    cleaned_fields += 1
                    modified = True

            if "expected_checkpoints" not in step:
                derived_checks = _derive_list_field(step.get("expected_result"))
                if derived_checks:
                    step["expected_checkpoints"] = derived_checks
                    cleaned_fields += 1
                    modified = True

            if modified:
                touched_steps += 1

    payload["Worksheet"] = worksheet
    payload.setdefault("meta", {})
    payload["meta"]["cleaning"] = {
        "touched_steps": touched_steps,
        "cleaned_field_instances": cleaned_fields,
    }
    return payload


def process_file(input_path: Path, output_path: Path) -> None:
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    cleaned = clean_testrail_payload(payload)
    output_path.write_text(json.dumps(cleaned, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    worksheet = cleaned.get("Worksheet", [])
    total_steps = sum(
        1
        for case in worksheet
        if isinstance(case, dict)
        for step in case.get("steps", [])
        if isinstance(step, dict)
    )
    action_substeps_count = sum(
        1
        for case in worksheet
        if isinstance(case, dict)
        for step in case.get("steps", [])
        if isinstance(step, dict) and "action_substeps" in step
    )
    expected_checkpoints_count = sum(
        1
        for case in worksheet
        if isinstance(case, dict)
        for step in case.get("steps", [])
        if isinstance(step, dict) and "expected_checkpoints" in step
    )

    print(f"Input: {input_path}")
    print(f"Output: {output_path}")
    print(f"Cases: {len(worksheet)}")
    print(f"Steps: {total_steps}")
    print(f"Steps with action_substeps: {action_substeps_count}")
    print(f"Steps with expected_checkpoints: {expected_checkpoints_count}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Clean parsed TestRail JSON and auto-generate substep/checkpoint fields.")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    process_file(args.input, args.output)


if __name__ == "__main__":
    main()
