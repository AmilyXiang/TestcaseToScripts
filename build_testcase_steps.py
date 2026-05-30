from __future__ import annotations

import argparse
import json
from collections import OrderedDict
from pathlib import Path
from typing import Dict, List


def _uniq_keep_order(items: List[str]) -> List[str]:
    seen = set()
    out: List[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        out.append(item)
    return out


def build_simple_stepflow(input_action_file: Path, output_step_file: Path) -> Dict:
    payload = json.loads(input_action_file.read_text(encoding="utf-8"))
    rows = payload.get("rows", [])

    cases: "OrderedDict[str, List[Dict]]" = OrderedDict()
    for index, row in enumerate(rows):
        case_id = str(row.get("case_id", "")).strip()
        if not case_id:
            continue

        if case_id not in cases:
            cases[case_id] = []

        cases[case_id].append(
            {
                "step_number": f"{int(row.get('step_no', 0) or 0)}_{int(row.get('sub_step_no', 0) or 0)}",
                "action_intent": (row.get("action_intent") or "").strip() or "custom_action",
                "expected_intent": (row.get("expected_intent") or "").strip() or "assert_generic",
                "precondition_intent": (row.get("precondition_intent") or "").strip(),
                "_index": index,
            }
        )

    testcase_blocks: List[Dict] = []

    for case_id, steps in cases.items():
        n = len(steps)
        execute_action = [True] * n
        execute_expected = [True] * n

        # Rule A: consecutive different actions with same expected -> expected only on last row.
        i = 0
        while i < n:
            j = i
            expected = steps[i]["expected_intent"]
            while j + 1 < n and steps[j + 1]["expected_intent"] == expected:
                j += 1

            if j > i:
                action_chain = _uniq_keep_order([steps[k]["action_intent"] for k in range(i, j + 1)])
                if len(action_chain) > 1:
                    for k in range(i, j):
                        execute_expected[k] = False
                    execute_expected[j] = True

            i = j + 1

        # Rule B: consecutive same action with different expected -> action only on first row.
        i = 0
        while i < n:
            j = i
            action = steps[i]["action_intent"]
            while j + 1 < n and steps[j + 1]["action_intent"] == action:
                j += 1

            if j > i:
                expected_chain = _uniq_keep_order([steps[k]["expected_intent"] for k in range(i, j + 1)])
                if len(expected_chain) > 1:
                    execute_action[i] = True
                    for k in range(i + 1, j + 1):
                        execute_action[k] = False

            i = j + 1

        preconditions = _uniq_keep_order([s["precondition_intent"] for s in steps if s["precondition_intent"]])
        precondition_line = " ; ".join(preconditions) if preconditions else "None"

        out_steps: List[Dict] = []
        for i, step in enumerate(steps):
            out_row: Dict[str, str] = {"step_number": step["step_number"]}
            if execute_action[i]:
                out_row["action_intent"] = step["action_intent"]
            if execute_expected[i]:
                out_row["expected_intent"] = step["expected_intent"]

            if len(out_row) > 1:
                out_steps.append(out_row)

        testcase_blocks.append(
            {
                "case_id": case_id,
                "precondition_intent": precondition_line,
                "steps": out_steps,
            }
        )

    result = {
        "status": "ok",
        "input_action_file": str(input_action_file).replace("\\", "/"),
        "output_step_file": str(output_step_file).replace("\\", "/"),
        "style": "simple_stepflow_intent_first_clean",
        "rules_applied": [
            "rule_a_multi_action_to_one_expected_hide_deferred",
            "rule_b_one_action_to_multi_expected_hide_reused",
        ],
        "testcases": testcase_blocks,
    }

    output_step_file.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Build simple testcase stepflow JSON from testcase_actions JSON.")
    parser.add_argument("--input", type=Path, required=True, help="Input testcase_actions JSON file.")
    parser.add_argument("--output", type=Path, required=True, help="Output testcase_steps JSON file.")
    args = parser.parse_args()

    result = build_simple_stepflow(args.input, args.output)
    total_steps = sum(len(case.get("steps", [])) for case in result.get("testcases", []))
    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    print(f"Cases: {len(result.get('testcases', []))}")
    print(f"Output steps: {total_steps}")


if __name__ == "__main__":
    main()
