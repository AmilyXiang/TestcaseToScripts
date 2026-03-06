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
    case_id_col = find_column_name(columns, ["case-id", "case id", "caseid", "id"])
    title_col = find_column_name(columns, ["title", "test case", "testcase"])
    preconditions_col = find_column_name(columns, ["preconditions", "precondition"])
    step_col = find_column_name(columns, ["steps (step)", "step", "steps"])
    expected_col = find_column_name(
        columns,
        ["steps (expected result)", "expected result", "expected", "result"],
    )

    if not step_col and "Steps (Step)" in columns:
        step_col = "Steps (Step)"
    if not expected_col and "Steps (Expected Result)" in columns:
        expected_col = "Steps (Expected Result)"

    cases: List[Dict[str, Any]] = []
    current_case: Dict[str, Any] | None = None

    for _, raw_row in cleaned.iterrows():
        row = {col: normalize_cell(value) for col, value in raw_row.items()}

        title_value = row.get(title_col) if title_col else None
        preconditions_value = row.get(preconditions_col) if preconditions_col else None
        step_value = row.get(step_col) if step_col else None
        expected_value = row.get(expected_col) if expected_col else None

        if title_value:
            case_id = extract_case_id(row, case_id_col, title_col, len(cases) + 1)
            current_case = {
                "case_id": case_id,
                "title": title_value,
                "preconditions": preconditions_value,
                "steps": [],
            }
            cases.append(current_case)

        if current_case and (step_value or expected_value):
            current_case["steps"].append(
                {
                    "step_no": len(current_case["steps"]) + 1,
                    "action": step_value,
                    "expected_result": expected_value,
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
