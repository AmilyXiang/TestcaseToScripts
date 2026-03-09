import re
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd


def normalize_columns(columns: List[Any]) -> List[str]:
    normalized = []
    for col in columns:
        if col is None:
            normalized.append("")
        else:
            normalized.append(str(col).strip())
    return normalized


def find_column_name(columns: List[str], candidates: List[str]) -> str | None:
    lowered = {c.lower(): c for c in columns}
    for name in candidates:
        key = name.lower()
        if key in lowered:
            return lowered[key]
    return None


def normalize_cell(value: Any) -> str | None:
    if pd.isna(value):
        return None
    text = str(value).strip()
    return text or None


def split_numbered_items(text: str | None) -> List[str]:
    """Split a text blob by top-level numbered bullets: 1. ... 2. ... 3. ..."""
    if not text:
        return []

    normalized = text.replace("\r\n", "\n").replace("\r", "\n").strip()
    if not normalized:
        return []

    marker = re.compile(r"(?m)^\s*(\d+)\.\s*")
    matches = list(marker.finditer(normalized))
    if len(matches) < 2:
        return [normalized]

    parts: List[str] = []
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(normalized)
        segment = normalized[start:end].strip()
        if segment:
            parts.append(segment)

    return parts if parts else [normalized]


def align_substeps(action_text: str | None, expected_text: str | None) -> List[Dict[str, str | None]]:
    """Align numbered action/expected blocks into per-substep pairs."""
    actions = split_numbered_items(action_text)
    expecteds = split_numbered_items(expected_text)

    # Default single-step pair when no split is possible.
    if len(actions) <= 1 and len(expecteds) <= 1:
        return [{"action": action_text, "expected_result": expected_text}]

    total = max(len(actions), len(expecteds))
    pairs: List[Dict[str, str | None]] = []

    for idx in range(total):
        # Broadcast single-side text when only one side is unsplit.
        action_item = actions[idx] if idx < len(actions) else (actions[0] if len(actions) == 1 else None)
        expected_item = expecteds[idx] if idx < len(expecteds) else (expecteds[0] if len(expecteds) == 1 else None)
        pairs.append({"action": action_item, "expected_result": expected_item})

    return pairs


def extract_case_id(
    row: Dict[str, Any],
    case_id_col: str | None,
    title_col: str | None,
    fallback_index: int,
) -> str:
    if case_id_col:
        case_id = normalize_cell(row.get(case_id_col))
        if case_id:
            return case_id

    title = normalize_cell(row.get(title_col)) if title_col else None
    if title:
        # Example title: RQPLEIAD_180_01_Create_Emergency_Program_Key
        match = re.match(r"^([A-Za-z0-9]+[_-]\d+[_-]\d+)", title)
        if match:
            return match.group(1)
    return f"CASE_{fallback_index:03d}"


def parse_sheet(df: pd.DataFrame) -> List[Dict[str, Any]]:
    # Remove fully empty rows and columns to keep meaningful testcase records only.
    cleaned = df.dropna(how="all").dropna(axis=1, how="all")
    if cleaned.empty:
        return []

    cleaned.columns = normalize_columns(list(cleaned.columns))

    columns = list(cleaned.columns)

    # Ignore helper columns that are not part of structured testcase content.
    ignored = {"steps", "is_converted"}
    effective_columns = [col for col in columns if col.lower() not in ignored]

    case_id_col = find_column_name(effective_columns, ["id", "case-id", "case id", "caseid"])
    title_col = find_column_name(columns, ["title", "test case", "testcase"])
    description_col = find_column_name(columns, ["description", "desc"])
    preconditions_col = find_column_name(columns, ["preconditions", "precondition"])
    # Prefer the unified TestRail columns.
    step_col = find_column_name(columns, ["steps (step)"])
    expected_col = find_column_name(
        columns,
        ["steps (expected result)"],
    )

    # Backward-compatible fallback for older templates.
    if not step_col:
        step_col = find_column_name(effective_columns, ["step"])
    if not expected_col:
        expected_col = find_column_name(effective_columns, ["expected result", "expected", "result"])

    cases: List[Dict[str, Any]] = []
    current_case: Dict[str, Any] | None = None

    for _, raw_row in cleaned.iterrows():
        row = {col: normalize_cell(value) for col, value in raw_row.items()}

        title_value = row.get(title_col) if title_col else None
        description_value = row.get(description_col) if description_col else None
        preconditions_value = row.get(preconditions_col) if preconditions_col else None
        step_value = row.get(step_col) if step_col else None
        expected_value = row.get(expected_col) if expected_col else None

        if title_value:
            case_id = extract_case_id(row, case_id_col, title_col, len(cases) + 1)
            current_case = {
                "case_id": case_id,
                "title": title_value,
                "description": description_value,
                "preconditions": preconditions_value,
                "steps": [],
            }
            cases.append(current_case)

        if current_case and (step_value or expected_value):
            aligned_steps = align_substeps(step_value, expected_value)
            for item in aligned_steps:
                current_case["steps"].append(
                    {
                        "step_no": len(current_case["steps"]) + 1,
                        "action": item.get("action"),
                        "expected_result": item.get("expected_result"),
                    }
                )

    return cases


def parse_testrail_excel(
    file_path: Path,
    sheet: str | None = None,
) -> Dict[str, List[Dict[str, Any]]]:
    if not file_path.exists():
        raise FileNotFoundError(f"Excel file not found: {file_path}")

    # Read all sheets by default, or a specific sheet when requested.
    if sheet:
        workbook = {sheet: pd.read_excel(file_path, sheet_name=sheet)}
    else:
        workbook = pd.read_excel(file_path, sheet_name=None)

    parsed: Dict[str, List[Dict[str, Any]]] = {}
    for sheet_name, df in workbook.items():
        parsed[sheet_name] = parse_sheet(df)
    return parsed
