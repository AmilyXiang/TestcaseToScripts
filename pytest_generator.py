from __future__ import annotations

import re
import pprint
from dataclasses import asdict
from pathlib import Path
from typing import Any

import yaml

from testrail_xlsx_parser import TestCase


def sanitize_module_name(name: str) -> str:
    name = name.strip().lower()
    name = re.sub(r"[^a-z0-9_]+", "_", name)
    name = re.sub(r"_+", "_", name).strip("_")
    if not name:
        name = "generated"
    if name[0].isdigit():
        name = f"case_{name}"
    return name


def sanitize_test_name(title: str) -> str:
    base = sanitize_module_name(title)
    if not base.startswith("test_"):
        base = "test_" + base
    return base


def load_step_mapping(mapping_path: str | Path | None) -> list[dict[str, Any]]:
    if not mapping_path:
        return []
    mapping_path = Path(mapping_path)
    data = yaml.safe_load(mapping_path.read_text(encoding="utf-8"))
    if not data:
        return []
    rules = data.get("rules", [])
    if not isinstance(rules, list):
        raise ValueError("step mapping must contain 'rules' as a list")
    return rules


def map_step_to_ssh(step_text: str, rules: list[dict[str, Any]]) -> list[str]:
    """Return a list of SSH commands for a given natural-language step."""
    commands: list[str] = []
    for rule in rules:
        pattern = rule.get("pattern")
        if not pattern:
            continue
        if re.search(pattern, step_text, flags=re.IGNORECASE):
            cmds = rule.get("commands", [])
            if isinstance(cmds, str):
                cmds = [cmds]
            for cmd in cmds:
                if cmd:
                    commands.append(str(cmd))
    return commands


def render_pytest_module(
    *,
    module_name: str,
    cases: list[TestCase],
    mapping_rules: list[dict[str, Any]],
    cases_payload: list[dict[str, Any]] | None = None,
) -> str:
    lines: list[str] = []
    lines.append("from __future__ import annotations")
    lines.append("")
    lines.append("import pprint")
    lines.append("import pytest")
    lines.append("")
    lines.append("# Auto-generated from TestRail export.")
    lines.append("# Update step_mapping.yaml to map natural-language steps into SSH commands.")
    lines.append("")

    if cases_payload is None:
        case_payload = [asdict(c) for c in cases]
    else:
        case_payload = cases_payload
    # Embed as a Python literal to avoid escape-sequence interpretation issues.
    lines.append("CASES = " + pprint.pformat(case_payload, width=120, sort_dicts=False))
    lines.append("")

    lines.append("@pytest.mark.generated")
    lines.append("@pytest.mark.parametrize('case', CASES, ids=[c['title'] for c in CASES])")
    lines.append(f"def test_{sanitize_module_name(module_name)}(case, ssh_session, step_mapping_rules):")
    lines.append("    \"\"\"Execute a TestRail test case against DUT via SSH when mappings exist.\"\"\"")
    lines.append("    title = case['title']")
    lines.append("    pre = case.get('preconditions') or ''")
    lines.append("    steps = case.get('steps') or []")
    lines.append("")
    lines.append("    if pre:")
    lines.append("        # Preconditions are usually informational; you can map them into setup actions if needed.")
    lines.append("        pass")
    lines.append("")
    lines.append("    any_automated = False")
    lines.append("    for i, s in enumerate(steps, 1):")
    lines.append("        step_text = (s.get('step') or '').strip()")
    lines.append("        exp_text = (s.get('expected') or '').strip()")
    lines.append("        cmds = []")
    lines.append("        ai_cmds = s.get('suggested_commands') or []")
    lines.append("        if isinstance(ai_cmds, str):")
    lines.append("            ai_cmds = [ai_cmds]")
    lines.append("        cmds.extend([c for c in ai_cmds if c])")
    lines.append("")
    lines.append("        if not cmds:")
    lines.append("            for rule in step_mapping_rules:")
    lines.append("                pattern = rule.get('pattern')")
    lines.append("                if pattern and __import__('re').search(pattern, step_text, flags=__import__('re').IGNORECASE):")
    lines.append("                    rule_cmds = rule.get('commands', [])")
    lines.append("                    if isinstance(rule_cmds, str):")
    lines.append("                        rule_cmds = [rule_cmds]")
    lines.append("                    cmds.extend([c for c in rule_cmds if c])")
    lines.append("")
    lines.append("        if cmds:")
    lines.append("            any_automated = True")
    lines.append("            for cmd in cmds:")
    lines.append("                result = ssh_session.exec(cmd)")
    lines.append("                assert result.exit_code == 0, f'[{title}] step {i} failed: {cmd}\\n{result.stdout}\\n{result.stderr}'")
    lines.append("        else:")
    lines.append("            # No mapping: keep the step visible in output and mark as xfail (not silently passing).")
    lines.append("            pytest.xfail(f'No SSH mapping for step {i}: {step_text} | expected: {exp_text}')")
    lines.append("")
    lines.append("    if not any_automated:")
    lines.append("        pytest.xfail(f'No steps automated for case: {title}')")

    return "\n".join(lines) + "\n"
