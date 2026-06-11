"""
One-shot migration: inject action_actor / expected_actor / precondition_actor
into an existing Copilot-refined action JSON without touching any intent fields.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from build_testcase_actions_local import _extract_actor

FIELD_ORDER = [
    "case_id", "title", "step_no", "sub_step_no",
    "action_actor", "action_text", "action_intent",
    "expected_actor", "expected_text", "expected_intent",
    "precondition_actor", "precondition_text", "precondition_intent", "precondition_required",
]


def patch(src: Path, dst: Path) -> None:
    data = json.loads(src.read_text(encoding="utf-8"))
    rows = data.get("rows", [])

    for row in rows:
        row["action_actor"] = _extract_actor(row.get("action_text", ""))
        row["expected_actor"] = _extract_actor(row.get("expected_text", ""))
        pre = row.get("precondition_text", "")
        row["precondition_actor"] = _extract_actor(pre) if pre else "A"

        # reorder for readability
        ordered = {k: row[k] for k in FIELD_ORDER if k in row}
        for k in row:
            if k not in ordered:
                ordered[k] = row[k]
        row.clear()
        row.update(ordered)

    dst.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    nr = sum(1 for r in rows if r.get("action_intent") == "needs_review")
    ag = sum(1 for r in rows if r.get("expected_intent") == "assert_generic")
    print(f"Patched {len(rows)} rows -> {dst}")
    print(f"  needs_review: {nr}  assert_generic: {ag}")
    # show a multi-actor sample
    for r in rows:
        if r.get("action_actor") != r.get("expected_actor"):
            print(f"  Sample multi-actor row [{r['case_id']} {r['step_no']}_{r['sub_step_no']}]: "
                  f"action={r['action_actor']} expected={r['expected_actor']} pre={r['precondition_actor']}")
            break


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    patch(args.input, args.output)


if __name__ == "__main__":
    main()
