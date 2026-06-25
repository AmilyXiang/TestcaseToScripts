#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from generator_copilot import GeneratorCopilot
from log_manager import get_logger
from prompt_manager import PromptManager


logger = get_logger("testrail_auto_cases_generator_copilot")


class GeneratorTestRailAutoCasesCopilot(GeneratorCopilot):
    """Generate TestRail auto cases via Copilot CLI using prompt-driven MCP workflow."""

    prompt_name = "prompt.testrail_auto_cases_fetcher"

    def __init__(
        self,
        prompt_manager: PromptManager | None = None,
        temp_dir: str = "tmp",
        output_dir: str = "output_copilot",
        copilot_cmd: str = "copilot.cmd",
        scope: str = "",
        run_id: int | None = None,
        project_id: int | None = None,
        auto_values: List[str] | None = None,
        max_retry: int = 2,
        output_prefix: str = "",
    ):
        super().__init__(
            prompt_manager=prompt_manager,
            temp_dir=temp_dir,
            output_dir=output_dir,
            copilot_cmd=copilot_cmd,
            target_name="testrail_auto_cases",
        )
        self.scope = scope.strip().lower()
        self.run_id = run_id
        self.project_id = project_id
        self.auto_values = auto_values or ["Auto"]
        self.max_retry = max_retry
        self.output_prefix = output_prefix.strip()

        self.resolved_scope = ""
        self.summary_file = ""
        self.details_file = ""

    def _resolve_scope(self) -> None:
        if self.run_id is None and self.project_id is None:
            raise ValueError("run_id and project_id cannot both be empty")

        if self.scope in ("run", "project"):
            self.resolved_scope = self.scope
        elif self.run_id is not None:
            self.resolved_scope = "run"
        else:
            self.resolved_scope = "project"

        if self.resolved_scope == "run" and self.run_id is None:
            raise ValueError("scope=run requires run_id")
        if self.resolved_scope == "project" and self.project_id is None:
            raise ValueError("scope=project requires project_id")

    def _resolve_output_paths(self) -> None:
        if self.output_prefix:
            prefix = self.output_prefix
        elif self.resolved_scope == "run":
            prefix = f"testrail_run_{self.run_id}_auto_cases"
        else:
            prefix = f"testrail_project_{self.project_id}_auto_cases"

        self.output_prefix = prefix
        self.summary_file = self.normalize_prompt_path(os.path.join(self.output_dir, f"{prefix}.summary.json"))
        self.details_file = self.normalize_prompt_path(os.path.join(self.output_dir, f"{prefix}.details.json"))

    @staticmethod
    def _render_auto_values(values: List[str]) -> str:
        return ", ".join([json.dumps(v, ensure_ascii=False) for v in values])

    def build_generate_prompt(self) -> str:
        base_prompt = self.prompt_manager.get_prompt(self.prompt_name)

        replaced = base_prompt
        replaced = replaced.replace("{{SCOPE}}", self.resolved_scope)
        replaced = replaced.replace("{{RUN_ID_OR_EMPTY}}", "" if self.run_id is None else str(self.run_id))
        replaced = replaced.replace("{{PROJECT_ID_OR_EMPTY}}", "" if self.project_id is None else str(self.project_id))
        replaced = replaced.replace("{{AUTO_VALUES}}", self._render_auto_values(self.auto_values))
        replaced = replaced.replace("{{MAX_RETRY}}", str(self.max_retry))
        replaced = replaced.replace("{{OUTPUT_DIR}}", self.output_dir)
        replaced = replaced.replace("{{OUTPUT_PREFIX_OR_EMPTY}}", self.output_prefix)

        # Add explicit output paths to reduce ambiguity for Copilot CLI execution.
        replaced += (
            "\n\n## Runtime Constraints (CLI)\n"
            f"- Must write summary JSON to: {self.summary_file}\n"
            f"- Must write details JSON to: {self.details_file}\n"
            "- Return strict JSON only.\n"
        )
        return replaced

    def generate(self) -> Dict[str, Any]:
        logger.info("[GeneratorTestRailAutoCasesCopilot] generate start")

        self._resolve_scope()
        self._resolve_output_paths()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        generate_prompt = self.build_generate_prompt()
        temp_prompt_file = self.build_temp_prompt_file(timestamp, generate_prompt)

        logger.info("[GeneratorTestRailAutoCasesCopilot] run copilot cli")
        copilot_result = self.run_copilot_cli(temp_prompt_file)

        summary_exists = os.path.exists(self.summary_file)
        details_exists = os.path.exists(self.details_file)

        result = {
            "prompt_file": temp_prompt_file,
            "scope": self.resolved_scope,
            "run_id": self.run_id,
            "project_id": self.project_id,
            "output_dir": self.output_dir,
            "output_prefix": self.output_prefix,
            "summary_file": self.summary_file,
            "details_file": self.details_file,
            "summary_exists": summary_exists,
            "details_exists": details_exists,
            "return_code": copilot_result["return_code"],
            "command": copilot_result["command"],
            "stdout": copilot_result["stdout"],
            "stderr": copilot_result["stderr"],
            "output_status": "OK" if (summary_exists and details_exists) else "NOK",
        }

        logger.info(
            "[GeneratorTestRailAutoCasesCopilot] done summary_exists=%s details_exists=%s",
            summary_exists,
            details_exists,
        )
        return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run TestRail auto cases fetch via Copilot CLI.")
    parser.add_argument("--scope", choices=["run", "project"], default="", help="Fetch scope.")
    parser.add_argument("--run-id", type=int, default=None, help="TestRail run_id.")
    parser.add_argument("--project-id", type=int, default=None, help="TestRail project_id.")
    parser.add_argument(
        "--auto-values",
        type=str,
        default='["Auto"]',
        help='JSON array for auto category labels, e.g. ["Auto"].',
    )
    parser.add_argument("--max-retry", type=int, default=2, help="Max retry per tool call.")
    parser.add_argument("--output-dir", default="output_copilot", help="Output directory.")
    parser.add_argument("--output-prefix", default="", help="Output file prefix.")
    parser.add_argument("--temp-dir", default="tmp", help="Temporary prompt directory.")
    parser.add_argument("--copilot-cmd", default="copilot.cmd", help="Copilot CLI command.")
    parser.add_argument(
        "--project-root",
        default="",
        help="Project root for locating prompt folder; defaults to parent of copilot-cli.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()

    project_root = args.project_root or str(Path(__file__).parent.parent)
    prompt_folder = os.path.join(project_root, "prompt")
    pm = PromptManager(prompt_folder=prompt_folder)

    auto_values = json.loads(args.auto_values)
    if not isinstance(auto_values, list) or not all(isinstance(x, str) for x in auto_values):
        raise ValueError("--auto-values must be a JSON string array")

    generator = GeneratorTestRailAutoCasesCopilot(
        prompt_manager=pm,
        temp_dir=args.temp_dir,
        output_dir=args.output_dir,
        copilot_cmd=args.copilot_cmd,
        scope=args.scope,
        run_id=args.run_id,
        project_id=args.project_id,
        auto_values=auto_values,
        max_retry=args.max_retry,
        output_prefix=args.output_prefix,
    )

    result = generator.generate()
    print(json.dumps(result, ensure_ascii=False, indent=2))

    if not (result["summary_exists"] and result["details_exists"]):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
