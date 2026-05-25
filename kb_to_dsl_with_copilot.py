import json
import os
import shutil
import subprocess
from pathlib import Path


def _resolve_copilot_command(copilot_cmd: str) -> list[str]:
    """Resolve a runnable Copilot CLI command on Windows."""
    found = shutil.which(copilot_cmd)
    if found:
        return [found]

    appdata = os.environ.get("APPDATA", "")
    bootstrapper = Path(appdata) / "Code" / "User" / "globalStorage" / "github.copilot-chat" / "copilotCli" / "copilot.ps1"
    if bootstrapper.exists():
        return ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(bootstrapper)]

    return []


def _resolve_gh_command() -> list[str]:
    """Resolve GitHub CLI command path if available."""
    found = shutil.which("gh")
    if found:
        return [found]

    program_files = os.environ.get("ProgramFiles", r"C:\Program Files")
    gh_exe = Path(program_files) / "GitHub CLI" / "gh.exe"
    if gh_exe.exists():
        return [str(gh_exe)]

    return []


def _load_gh_auth_token() -> str | None:
    """Read token from gh auth if available so Copilot subprocess inherits auth."""
    gh_command = _resolve_gh_command()
    if not gh_command:
        return None

    try:
        proc = subprocess.run(
            gh_command + ["auth", "token"],
            capture_output=True,
            text=True,
            cwd=None,
        )
    except Exception:
        return None

    token = (proc.stdout or "").strip()
    if proc.returncode != 0 or not token:
        return None
    return token


def _extract_json_object(text: str) -> dict:
    """Extract the first JSON object from Copilot output."""
    candidate = text.strip()
    if not candidate:
        raise ValueError("empty Copilot output")

    try:
        return json.loads(candidate)
    except Exception:
        pass

    start = candidate.find("{")
    end = candidate.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("Copilot output does not contain JSON")

    return json.loads(candidate[start : end + 1])


def _decode_output(raw: bytes | None) -> str:
    if not raw:
        return ""
    for encoding in ("utf-8", "gbk"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def _run_copilot_prompt(prompt_text, copilot_cmd="copilot.cmd", cwd=None):
    """Run Copilot CLI and require a successful response."""
    command = _resolve_copilot_command(copilot_cmd)
    if not command:
        raise RuntimeError("Copilot CLI not found. Install or expose copilot.cmd / copilot.ps1 first.")

    env = os.environ.copy()
    token = env.get("COPILOT_GITHUB_TOKEN") or env.get("GH_TOKEN") or env.get("GITHUB_TOKEN") or _load_gh_auth_token()
    if token:
        env.setdefault("COPILOT_GITHUB_TOKEN", token)
        env.setdefault("GH_TOKEN", token)
        env.setdefault("GITHUB_TOKEN", token)

    proc = subprocess.run(
        command + ["-p", prompt_text, "--allow-all"],
        capture_output=True,
        text=False,
        cwd=cwd,
        env=env,
    )
    if proc.returncode != 0:
        raise RuntimeError((_decode_output(proc.stderr) or _decode_output(proc.stdout) or "Copilot CLI failed").strip())

    return {
        "return_code": proc.returncode,
        "stdout": _decode_output(proc.stdout),
        "stderr": _decode_output(proc.stderr),
    }

def kb_to_dsl_with_copilot(kb_path, dsl_output_path, copilot_cmd="copilot.cmd", prompt_folder="prompt"):
    """
    将normalized_kb文件批量转换为DSL中间文件，遇到intent为pending_llm时自动调用copilot-cli补全。
    """
    with open(kb_path, "r", encoding="utf-8") as f:
        kb_data = json.load(f)
    entries = kb_data.get("entries", [])

    project_root = Path(__file__).resolve().parent
    _ = prompt_folder  # retained for CLI compatibility.

    dsl_rows = []
    for entry in entries:
        action_text = str(entry.get("normalized_action", "") or "")
        expected_text = str(entry.get("normalized_expected_result", "") or "")
        actor = "current_device"
        target = ""
        action_intent = "no_action" if not action_text.strip() else "pending_llm"
        expected_intent = "no_expected" if not expected_text.strip() else "pending_llm"

        # 强制通过Copilot补全所有 pending_llm 占位。
        if action_intent == "pending_llm" or expected_intent == "pending_llm":
            prompt = (
                "你是一个测试步骤DSL补全器。\n"
                "请把输入步骤解析成严格JSON，禁止输出解释文字。\n"
                "返回格式必须是：\n"
                "{\n"
                '  "action": {"intent": "...", "actor": "...", "target": "..."},\n'
                '  "expected": {"intent": "..."}\n'
                "}\n\n"
                f"action_text: {action_text}\n"
                f"expected_text: {expected_text}\n"
                f"current_action_intent: {action_intent}\n"
                f"current_expected_intent: {expected_intent}\n"
            )
            result = _run_copilot_prompt(prompt, copilot_cmd=copilot_cmd, cwd=project_root)
            try:
                copilot_json = _extract_json_object(result["stdout"])
            except Exception as exc:
                debug_dir = project_root / "tmp"
                debug_dir.mkdir(parents=True, exist_ok=True)
                debug_file = debug_dir / f"copilot_debug_case_{entry.get('case_id')}_step_{entry.get('step_no')}_sub_{entry.get('sub_step_no')}.txt"
                debug_file.write_text(
                    "PROMPT:\n" + prompt + "\n\nSTDOUT:\n" + result["stdout"] + "\n\nSTDERR:\n" + result["stderr"],
                    encoding="utf-8",
                )
                raise RuntimeError(f"Copilot output is not valid JSON: {debug_file}") from exc

            action_block = copilot_json.get("action", {}) if isinstance(copilot_json, dict) else {}
            expected_block = copilot_json.get("expected", {}) if isinstance(copilot_json, dict) else {}

            if action_intent == "pending_llm":
                action_intent = str(action_block.get("intent", action_intent) or action_intent)
                actor = str(action_block.get("actor", actor) or actor)
                target = str(action_block.get("target", target) or target)
            if expected_intent == "pending_llm":
                expected_intent = str(expected_block.get("intent", expected_intent) or expected_intent)

            if action_intent == "pending_llm" or expected_intent == "pending_llm":
                raise RuntimeError(f"Copilot did not resolve pending_llm for case={entry.get('case_id')} step={entry.get('step_no')} sub_step={entry.get('sub_step_no')}")
        dsl_rows.append({
            "case_id": entry.get("case_id"),
            "step_no": entry.get("step_no"),
            "sub_step_no": entry.get("sub_step_no"),
            "dsl": {
                "action": {
                    "intent": action_intent,
                    "actor": actor,
                    "target": target,
                    "text": action_text,
                },
                "expected": {
                    "intent": expected_intent,
                    "text": expected_text,
                },
                "trace": {
                    "title": entry.get("title"),
                    "keywords": entry.get("keywords", []),
                },
            },
        })
    dsl_payload = {
        "meta": {
            "source": str(kb_path),
            "description": "AAO to DSL intermediate representation (with copilot-cli)",
            "row_count": len(dsl_rows),
        },
        "rows": dsl_rows,
    }
    with open(dsl_output_path, "w", encoding="utf-8") as f:
        json.dump(dsl_payload, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="kb->dsl（集成copilot-cli兜底）")
    parser.add_argument("--input", type=str, required=True, help="输入normalized_kb.json")
    parser.add_argument("--output", type=str, required=True, help="输出dsl.json")
    parser.add_argument("--copilot-cmd", type=str, default="copilot.cmd", help="copilot命令路径")
    parser.add_argument("--prompt-folder", type=str, default="prompt", help="prompt模板文件夹")
    args = parser.parse_args()
    kb_to_dsl_with_copilot(args.input, args.output, args.copilot_cmd, args.prompt_folder)
