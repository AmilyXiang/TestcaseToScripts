from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pandas as pd


@dataclass(frozen=True)
class TestStep:
    step: str
    expected: str


@dataclass(frozen=True)
class TestCase:
    title: str
    preconditions: str
    steps: tuple[TestStep, ...]


def _clean_cell(value: object) -> str:
    if pd.isna(value):
        return ""
    text = str(value)
    # Excel sometimes stores CR as _x000D_
    text = text.replace("_x000D_", "")
    return text.strip()


def parse_testrail_xlsx(
    xlsx_path: str | Path,
    *,
    sheet: str | None = None,
    title_col: str = "Title",
    preconditions_col: str = "Preconditions",
    step_col: str = "Steps (Step)",
    expected_col: str = "Steps (Expected Result)",
) -> list[TestCase]:
    """Parse a TestRail XLSX export where steps are represented as multiple rows.

    Assumes a new test case starts when `title_col` is non-empty.
    Subsequent rows for the same case have empty Title/Preconditions but contain additional steps.
    """

    xlsx_path = Path(xlsx_path)
    xl = pd.ExcelFile(xlsx_path)

    sheet_names: Iterable[str]
    if sheet:
        sheet_names = [sheet]
    else:
        sheet_names = xl.sheet_names

    cases: list[TestCase] = []

    for sheet_name in sheet_names:
        df = xl.parse(sheet_name)
        missing = [c for c in (title_col, preconditions_col, step_col, expected_col) if c not in df.columns]
        if missing:
            raise ValueError(f"Sheet '{sheet_name}' missing columns: {missing}. Found: {list(df.columns)}")

        is_case_start = df[title_col].notna() & (df[title_col].astype(str).str.strip() != "")
        start_indices = df.index[is_case_start].tolist()
        if not start_indices:
            continue

        start_indices.append(df.index[-1] + 1)

        for idx, start in enumerate(start_indices[:-1]):
            end_exclusive = start_indices[idx + 1]
            block = df.loc[start : end_exclusive - 1]

            title = _clean_cell(block.iloc[0][title_col])
            preconditions = _clean_cell(block.iloc[0][preconditions_col])

            steps: list[TestStep] = []
            for _, row in block.iterrows():
                step_text = _clean_cell(row[step_col])
                exp_text = _clean_cell(row[expected_col])
                if not step_text and not exp_text:
                    continue
                steps.append(TestStep(step=step_text, expected=exp_text))

            cases.append(TestCase(title=title, preconditions=preconditions, steps=tuple(steps)))

    return cases
