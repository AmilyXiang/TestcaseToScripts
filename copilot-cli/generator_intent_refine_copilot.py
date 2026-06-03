#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from generator_copilot import GeneratorCopilot
from log_manager import get_logger
from prompt_manager import PromptManager


logger = get_logger("intent_refine_generator_copilot")


class GeneratorIntentRefineCopilot(GeneratorCopilot):
    """
    Run intent refine (action + precondition + expected) in one Copilot CLI pass.

    The Copilot CLI only accepts a plain-text prompt string; it cannot receive
    markdown files as attachments.  This generator therefore builds a fully
    self-contained prompt by inlining:
      - docs/intent_refine_mapping_template.md
      - docs/expected_intent_mapping_template.md
      - docs/precondition_intent_mapping_template.md
      - the full input testcase_actions JSON

    The resulting temp prompt instructs Copilot to output the refined JSON to
    the specified output file.
    """

    prompt_name = "prompt.intent_refine.copilot"

    # Marker strings in the base prompt that reference external docs files.
    # They are replaced with the actual file content when building the inline prompt.
    _DOC_MARKERS: List[tuple[str, str]] = [
        (
            "docs/intent_refine_mapping_template.md as the authoritative action_intent mapping source.",
            "docs/intent_refine_mapping_template.md (full content inlined below) as the authoritative action_intent mapping source.",
        ),
        (
            "docs/expected_intent_mapping_template.md as the authoritative expected_intent mapping source.",
            "docs/expected_intent_mapping_template.md (full content inlined below) as the authoritative expected_intent mapping source.",
        ),
        (
            "docs/precondition_intent_mapping_template.md as the authoritative precondition_intent mapping source.",
            "docs/precondition_intent_mapping_template.md (full content inlined below) as the authoritative precondition_intent mapping source.",
        ),
    ]

    def __init__(
        self,
        prompt_manager: PromptManager | None = None,
        temp_dir: str = "tmp",
        output_dir: str = "output_copilot",
        copilot_cmd: str = "copilot.cmd",
        skip_case_ids: List[str] | None = None,
        project_root: str = "",
    ):
        super().__init__(
            prompt_manager=prompt_manager,
            temp_dir=temp_dir,
            output_dir=output_dir,
            copilot_cmd=copilot_cmd,
            target_name="intent_refine",
        )
        self.skip_case_ids: List[str] = skip_case_ids or []
        self.project_root = project_root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def _read_doc(self, relative_path: str) -> str:
        """Read a docs/ file relative to project_root. Return empty string on failure."""
        full_path = os.path.join(self.project_root, relative_path)
        try:
            with open(full_path, encoding="utf-8") as f:
                return f.read().strip()
        except FileNotFoundError:
            logger.warning("[GeneratorIntentRefineCopilot] doc not found: %s", full_path)
            return f"(file not found: {relative_path})"

    def build_generate_prompt(
        self,
        input_action_file: str,
        output_action_file: str,
        skip_case_ids: List[str] | None = None,
    ) -> str:
        """Build a fully self-contained prompt with all docs and input JSON inlined.

        Copilot CLI cannot attach external files, so everything needed must be
        embedded in the prompt text itself.
        """
        use_skip = skip_case_ids if skip_case_ids is not None else self.skip_case_ids
        skip_json = json.dumps(use_skip, ensure_ascii=False)

        # 1. Fill base prompt placeholders.
        base_prompt = self.prompt_manager.get_prompt(
            self.prompt_name,
            input_action_file=self.normalize_prompt_path(input_action_file),
            output_action_file=self.normalize_prompt_path(output_action_file),
            skip_case_ids=skip_json,
        )

        # 2. Apply marker replacements so readers know content follows inline.
        for old, new in self._DOC_MARKERS:
            base_prompt = base_prompt.replace(old, new)

        # 3. Read all three mapping template docs.
        action_mapping_content = self._read_doc("docs/intent_refine_mapping_template.md")
        expected_mapping_content = self._read_doc("docs/expected_intent_mapping_template.md")
        precondition_mapping_content = self._read_doc("docs/precondition_intent_mapping_template.md")

        # 4. Read input JSON content.
        input_abs = (
            input_action_file
            if os.path.isabs(input_action_file)
            else os.path.join(self.project_root, input_action_file)
        )
        try:
            with open(input_abs, encoding="utf-8") as f:
                input_json_content = f.read().strip()
        except FileNotFoundError:
            raise FileNotFoundError(f"Input action file not found: {input_abs}")

        # 5. Assemble self-contained prompt: base rules + inlined docs + inlined JSON.
        inline_sections = (
            f"\n\n"
            f"{'=' * 72}\n"
            f"## INLINED: docs/intent_refine_mapping_template.md\n"
            f"{'=' * 72}\n"
            f"{action_mapping_content}\n\n"
            f"{'=' * 72}\n"
            f"## INLINED: docs/expected_intent_mapping_template.md\n"
            f"{'=' * 72}\n"
            f"{expected_mapping_content}\n\n"
            f"{'=' * 72}\n"
            f"## INLINED: docs/precondition_intent_mapping_template.md\n"
            f"{'=' * 72}\n"
            f"{precondition_mapping_content}\n\n"
            f"{'=' * 72}\n"
            f"## INPUT JSON: {self.normalize_prompt_path(input_action_file)}\n"
            f"{'=' * 72}\n"
            f"{input_json_content}\n"
        )

        return base_prompt + inline_sections

    def run_copilot_cli(self, prompt_file_path: str) -> Dict[str, Any]:
        """Override to set cwd to project_root so docs/ paths resolve correctly.

        NOTE: stdout/stderr are NOT captured (passed through to the parent
        terminal) so that Copilot CLI detects a real TTY and runs correctly.
        Capturing with PIPE (capture_output=True) removes the TTY, causing
        the CLI to hang silently.
        """
        cmd = self.build_copilot_cli_cmd(prompt_file_path)
        import subprocess
        # All streams are inherited from the parent process so that Copilot CLI
        # detects a real TTY on both stdin and stdout, which is required for
        # write/shell tool permissions to be granted.  Do NOT pass
        # capture_output=True or stdin=DEVNULL here.
        proc = subprocess.run(
            cmd,
            cwd=self.project_root,
        )
        return {
            "command": " ".join(cmd),
            "return_code": proc.returncode,
            "stdout": "",
            "stderr": "",
        }

    def prepare_prompt_file(
        self,
        input_action_file: str,
        output_action_file: str,
        skip_case_ids: List[str] | None = None,
        timestamp: str | None = None,
    ) -> str:
        """Build the prompt text and save it to a temp file.

        Returns the absolute path to the temp prompt file.
        This method does NOT call Copilot CLI — use it when you want to
        prepare prompt files in bulk and then run copilot.cmd directly in a
        real PowerShell terminal (which avoids subprocess TTY issues).
        """
        from datetime import datetime as _dt
        ts = timestamp or _dt.now().strftime("%Y%m%d_%H%M%S")
        generate_prompt = self.build_generate_prompt(
            input_action_file=input_action_file,
            output_action_file=output_action_file,
            skip_case_ids=skip_case_ids,
        )
        return self.build_temp_prompt_file(ts, generate_prompt)

    def generate(
        self,
        input_action_file: str,
        output_action_file: str,
        skip_case_ids: List[str] | None = None,
    ) -> Dict[str, Any]:
        """
        1) Fill prompt template with input/output file paths and skip list.
        2) Save filled prompt to a temp file.
        3) Build Copilot CLI command pointing at the temp prompt file.
        4) Invoke Copilot CLI (cwd = project_root so relative paths work).
        5) Return result dict.
        """
        logger.info("[GeneratorIntentRefineCopilot] generate start")
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            logger.info("[GeneratorIntentRefineCopilot] step1 build generation prompt")
            generate_prompt = self.build_generate_prompt(
                input_action_file=input_action_file,
                output_action_file=output_action_file,
                skip_case_ids=skip_case_ids,
            )

            logger.info("[GeneratorIntentRefineCopilot] step2 save temp prompt file")
            temp_prompt_file = self.build_temp_prompt_file(timestamp, generate_prompt)

            logger.info("[GeneratorIntentRefineCopilot] step3 run copilot command")
            copilot_result = self.run_copilot_cli(temp_prompt_file)
            logger.info("[GeneratorIntentRefineCopilot] command=%s", copilot_result["command"])
            logger.info("[GeneratorIntentRefineCopilot] return_code=%s", copilot_result["return_code"])

            output_exists = os.path.exists(output_action_file)
            output_status = "OK" if output_exists else "NOK"

            result = {
                "prompt_file": temp_prompt_file,
                "input_action_file": input_action_file,
                "output_action_file": output_action_file,
                "command": copilot_result["command"],
                "return_code": copilot_result["return_code"],
                "stdout": copilot_result["stdout"],
                "stderr": copilot_result["stderr"],
                "output_exists": output_exists,
                "output_status": output_status,
            }
            logger.info(
                "[GeneratorIntentRefineCopilot] done output_exists=%s output_status=%s",
                output_exists,
                output_status,
            )
            return result
        except Exception:
            logger.exception("[GeneratorIntentRefineCopilot] generate failed")
            raise


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Run intent refine (action+precondition+expected) via Copilot CLI."
    )
    parser.add_argument("--input", required=True, help="Input testcase_actions JSON path")
    parser.add_argument("--output", required=True, help="Output refined testcase_actions JSON path")
    parser.add_argument(
        "--skip-case-ids",
        default="[]",
        help='JSON list of case_ids to skip, e.g. \'["10172154","10172156"]\'',
    )
    parser.add_argument("--copilot-cmd", default="copilot.cmd", help="Copilot CLI command name")
    parser.add_argument("--temp-dir", default="tmp", help="Temp directory for prompt files")
    parser.add_argument(
        "--project-root",
        default="",
        help="Project root directory (defaults to parent of this script's directory)",
    )
    args = parser.parse_args()

    skip_ids: List[str] = json.loads(args.skip_case_ids)

    # PromptManager must point to the project-level prompt/ folder.
    project_root = args.project_root or str(Path(__file__).parent.parent)
    prompt_folder = os.path.join(project_root, "prompt")
    pm = PromptManager(prompt_folder=prompt_folder)

    generator = GeneratorIntentRefineCopilot(
        prompt_manager=pm,
        temp_dir=args.temp_dir,
        copilot_cmd=args.copilot_cmd,
        skip_case_ids=skip_ids,
        project_root=project_root,
    )

    result = generator.generate(
        input_action_file=args.input,
        output_action_file=args.output,
        skip_case_ids=skip_ids,
    )

    print(f"[{'OK' if result['output_exists'] else 'FAIL'}] output: {result['output_action_file']}")
    print(f"[INFO] return_code: {result['return_code']}")
    if result["stdout"]:
        print("[STDOUT]", result["stdout"][:500])
    if result["stderr"]:
        print("[STDERR]", result["stderr"][:500])

    if not result["output_exists"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
