from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, List, Tuple

import numpy as np
from sentence_transformers import SentenceTransformer


ActionFunc = Callable[[str, Dict[str, str], Dict[str, object]], str]


@dataclass
class PatternRule:
    cluster_id: int
    pattern: str
    regex: str
    parameters: List[str]
    action_name: str
    compiled: re.Pattern[str]


@dataclass
class MatchResult:
    rule: PatternRule | None
    params: Dict[str, str]
    method: str
    score: float | None


@dataclass
class ActionSchemaResult:
    action: str
    params: Dict[str, object]
    method: str
    score: float | None


SUPPORTED_ACTIONS = [
    "dial_call",
    "answer_call",
    "hangup_call",
    "hold_call",
    "resume_call",
    "transfer_call",
    "conference_start",
    "conference_join",
    "mute_call",
    "unmute_call",
    "generic_action",
]


ORDINAL_TO_INDEX = {
    "first": 1,
    "second": 2,
    "third": 3,
    "fourth": 4,
}


def infer_action_name(pattern_text: str, examples: List[str]) -> str:
    text = (pattern_text + " " + " ".join(examples)).lower()

    if "progkeys" in text and "navigate" in text:
        return "open_progkeys"
    if "select a key programming page" in text:
        return "select_programming_page"
    if "choose your emplacement" in text and "validate" in text:
        return "choose_slot_and_validate"
    if 'select "number"' in text or "select number" in text:
        return "select_number_type"
    if "set up your programmable key" in text:
        return "configure_progkey"
    if "start the call" in text and "prog" in text:
        return "start_call_with_progkey"
    if "calls" in text or "dials" in text or "outgoing call" in text:
        return "dial_call"
    if "switches the active call" in text or "switch active call" in text or "switch the active call" in text:
        return "switch_active_call"
    if "on hold" in text or "puts" in text and "hold" in text:
        return "put_on_hold"
    if "retrieves the call" in text or "retrieve call" in text:
        return "retrieve_call"
    if "takes the call" in text or "answers the call" in text:
        return "answer_call"
    if "hang up" in text or "end the communication" in text or "release the communication" in text:
        return "end_call"
    if "mute" in text and "press" in text:
        return "toggle_mute"
    return "generic_action"


def compile_rule_regex(pattern_text: str, regex_text: str) -> re.Pattern[str]:
    # Prefer the extracted regex. Fall back to exact pattern matching when regex is invalid.
    try:
        return re.compile(regex_text, flags=re.IGNORECASE)
    except re.error:
        escaped = re.escape(pattern_text)
        return re.compile(rf"^{escaped}$", flags=re.IGNORECASE)


def pattern_text_for_embedding(pattern_text: str) -> str:
    # Replace placeholders like {param_1} with a neutral token for stable embeddings.
    return re.sub(r"\{[^{}]+\}", "VALUE", pattern_text).strip()


def load_rules(patterns_path: Path) -> List[PatternRule]:
    raw = json.loads(patterns_path.read_text(encoding="utf-8"))
    rules: List[PatternRule] = []

    for item in raw:
        pattern_obj = item.get("pattern", {})
        pattern_text = str(pattern_obj.get("pattern", "")).strip()
        regex_text = str(pattern_obj.get("regex", "")).strip()
        params = [str(p) for p in pattern_obj.get("parameters", [])]
        examples = item.get("examples", []) if isinstance(item.get("examples", []), list) else []

        if not pattern_text and not regex_text:
            continue

        action_name = infer_action_name(pattern_text, examples)
        compiled = compile_rule_regex(pattern_text, regex_text if regex_text else re.escape(pattern_text))

        rules.append(
            PatternRule(
                cluster_id=int(item.get("cluster_id", -1)),
                pattern=pattern_text,
                regex=regex_text,
                parameters=params,
                action_name=action_name,
                compiled=compiled,
            )
        )

    return rules


def _resolve_rule_regex(step_text: str, rules: List[PatternRule]) -> MatchResult:
    # High-precision rule matcher: exact full regex match first.
    for rule in rules:
        match = rule.compiled.fullmatch(step_text)
        if not match:
            continue
        return MatchResult(rule=rule, params=map_params(rule, match), method="regex_fullmatch", score=None)

    # Secondary regex path: search match.
    for rule in rules:
        match = rule.compiled.search(step_text)
        if not match:
            continue
        return MatchResult(rule=rule, params=map_params(rule, match), method="regex_search", score=None)

    return MatchResult(rule=None, params={}, method="regex_miss", score=None)


class EmbeddingMatcher:
    def __init__(self, rules: List[PatternRule], model_name: str) -> None:
        self._rules = rules
        self._model = SentenceTransformer(model_name)

        # Use pattern text as canonical representation for semantic fallback.
        texts = [pattern_text_for_embedding(rule.pattern or rule.regex) for rule in rules]
        self._rule_embeddings = self._model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )

    def best_match(self, step_text: str) -> Tuple[int, float]:
        vec = self._model.encode([step_text], normalize_embeddings=True, convert_to_numpy=True)[0]
        sims = np.dot(self._rule_embeddings, vec)
        best_index = int(np.argmax(sims))
        best_score = float(sims[best_index])
        return best_index, best_score


class ActionEmbeddingResolver:
    def __init__(self, model_name: str) -> None:
        self._model = SentenceTransformer(model_name)
        self._action_texts = {
            "dial_call": "start or place an outgoing call by dialing a number or calling a target",
            "answer_call": "answer or take an incoming call",
            "hangup_call": "end, hang up, or release a call",
            "hold_call": "put a call on hold or park a call",
            "resume_call": "retrieve or resume a held call",
            "transfer_call": "transfer a call to another party",
            "conference_start": "merge calls to start a conference",
            "conference_join": "join an existing conference call",
            "mute_call": "mute call audio",
            "unmute_call": "unmute call audio",
        }
        self._actions = list(self._action_texts.keys())
        self._embeddings = self._model.encode(
            list(self._action_texts.values()),
            normalize_embeddings=True,
            convert_to_numpy=True,
        )

    def best_action(self, step_text: str) -> Tuple[str, float]:
        vec = self._model.encode([step_text], normalize_embeddings=True, convert_to_numpy=True)[0]
        sims = np.dot(self._embeddings, vec)
        best_index = int(np.argmax(sims))
        return self._actions[best_index], float(sims[best_index])


def extract_devices(step_text: str) -> List[str]:
    return re.findall(r"phone\s+[A-Za-z0-9_-]+", step_text, flags=re.IGNORECASE)


def extract_call_index(step_text: str) -> int | None:
    text = step_text.lower()
    for k, v in ORDINAL_TO_INDEX.items():
        if re.search(rf"\b{k}\b", text):
            return v

    m = re.search(r"\b(\d+)\s*(?:st|nd|rd|th)?\b", text)
    if m:
        return int(m.group(1))
    return None


def map_pattern_action_to_schema(pattern_action: str) -> str | None:
    mapping = {
        "dial_call": "dial_call",
        "answer_call": "answer_call",
        "end_call": "hangup_call",
        "put_on_hold": "hold_call",
        "retrieve_call": "resume_call",
        "toggle_mute": "mute_call",
    }
    return mapping.get(pattern_action)


def build_action_params(step_text: str, action: str) -> Dict[str, object]:
    params: Dict[str, object] = {}
    devices = extract_devices(step_text)

    if devices:
        params["device"] = devices[0]

    if action == "dial_call" and len(devices) >= 2:
        params["from_device"] = devices[0]
        params["to_device"] = devices[1]
    elif action in {"answer_call", "hangup_call", "hold_call", "resume_call", "mute_call", "unmute_call"}:
        if devices:
            params["device"] = devices[0]

    if action in {"conference_start", "conference_join"} and devices:
        params["participants"] = list(dict.fromkeys(devices))

    call_index = extract_call_index(step_text)
    if call_index is not None and "incoming call" in step_text.lower():
        params["call_index"] = call_index

    prefix_match = re.search(r"prefix\s*(\d+)", step_text, flags=re.IGNORECASE)
    if prefix_match:
        params["prefix"] = prefix_match.group(1)

    key_match = re.search(r"press(?:ing)?\s+(?:the\s+)?([A-Za-z0-9_\- ]+?)\s+key", step_text, flags=re.IGNORECASE)
    if key_match:
        params["key_name"] = key_match.group(1).strip()

    return params


def resolve_action_schema(
    step_text: str,
    pattern_action: str,
    use_embedding_fallback: bool,
    action_embedder: ActionEmbeddingResolver | None,
    embedding_threshold: float,
) -> ActionSchemaResult:
    text = step_text.lower()

    # Rule-based action typing (primary path).
    if "unmute" in text or "mute key again" in text:
        action = "unmute_call"
        return ActionSchemaResult(action=action, params=build_action_params(step_text, action), method="rule", score=None)
    if "mute" in text:
        action = "mute_call"
        return ActionSchemaResult(action=action, params=build_action_params(step_text, action), method="rule", score=None)
    if "transfer" in text:
        action = "transfer_call"
        return ActionSchemaResult(action=action, params=build_action_params(step_text, action), method="rule", score=None)
    if "conference" in text and ("merge" in text or "start" in text or "make" in text):
        action = "conference_start"
        return ActionSchemaResult(action=action, params=build_action_params(step_text, action), method="rule", score=None)
    if "conference" in text and "join" in text:
        action = "conference_join"
        return ActionSchemaResult(action=action, params=build_action_params(step_text, action), method="rule", score=None)
    if "on hold" in text or ("put" in text and "hold" in text) or "call park" in text:
        action = "hold_call"
        return ActionSchemaResult(action=action, params=build_action_params(step_text, action), method="rule", score=None)
    if "retrieve" in text or "resume" in text:
        action = "resume_call"
        return ActionSchemaResult(action=action, params=build_action_params(step_text, action), method="rule", score=None)
    if "hang up" in text or "hangs up" in text or "end the communication" in text or "release the communication" in text or "hook on" in text:
        action = "hangup_call"
        return ActionSchemaResult(action=action, params=build_action_params(step_text, action), method="rule", score=None)
    if "answer" in text or "takes the call" in text or "take call key" in text or "incoming call" in text and "takes" in text:
        action = "answer_call"
        return ActionSchemaResult(action=action, params=build_action_params(step_text, action), method="rule", score=None)
    if "dial" in text or "calls" in text or "outgoing call" in text:
        action = "dial_call"
        return ActionSchemaResult(action=action, params=build_action_params(step_text, action), method="rule", score=None)

    # Pattern-action mapping fallback.
    mapped = map_pattern_action_to_schema(pattern_action)
    if mapped:
        return ActionSchemaResult(action=mapped, params=build_action_params(step_text, mapped), method="pattern_mapping", score=None)

    # Embedding fallback.
    if use_embedding_fallback and action_embedder is not None:
        action, score = action_embedder.best_action(step_text)
        if score >= embedding_threshold:
            return ActionSchemaResult(action=action, params=build_action_params(step_text, action), method="embedding", score=score)

    # Generic fallback.
    return ActionSchemaResult(action="generic_action", params=build_action_params(step_text, "generic_action"), method="generic", score=None)


def resolve_rule(
    step_text: str,
    rules: List[PatternRule],
    embedding_matcher: EmbeddingMatcher | None,
    embedding_threshold: float,
) -> MatchResult:
    # Stage 1: regex rule matcher (high precision).
    regex_result = _resolve_rule_regex(step_text, rules)
    if regex_result.rule is not None:
        return regex_result

    # Stage 2: embedding similarity fallback.
    if embedding_matcher is not None and rules:
        idx, score = embedding_matcher.best_match(step_text)
        if score >= embedding_threshold:
            rule = rules[idx]
            return MatchResult(rule=rule, params={}, method="embedding", score=score)

    # Stage 3: generic action fallback.
    return MatchResult(rule=None, params={}, method="generic", score=None)


def map_params(rule: PatternRule, match: re.Match[str]) -> Dict[str, str]:
    groups = list(match.groups())
    if not groups:
        return {}

    mapped: Dict[str, str] = {}
    if rule.parameters:
        for idx, value in enumerate(groups):
            key = rule.parameters[idx] if idx < len(rule.parameters) else f"group_{idx + 1}"
            mapped[key] = value
    else:
        for idx, value in enumerate(groups):
            mapped[f"group_{idx + 1}"] = value
    return mapped


def action_open_progkeys(step: str, params: Dict[str, str], ctx: Dict[str, object]) -> str:
    ctx["ui_page"] = "ProgKeys"
    return f"UI -> Open ProgKeys page ({step})"


def action_select_programming_page(step: str, params: Dict[str, str], ctx: Dict[str, object]) -> str:
    ctx["programming_page_selected"] = True
    return f"UI -> Select key programming page ({step})"


def action_choose_slot_and_validate(step: str, params: Dict[str, str], ctx: Dict[str, object]) -> str:
    ctx["slot_selected"] = True
    return "UI -> Choose slot and validate"


def action_select_number_type(step: str, params: Dict[str, str], ctx: Dict[str, object]) -> str:
    ctx["progkey_type"] = "Number"
    return "Config -> Select progkey type: Number"


def action_configure_progkey(step: str, params: Dict[str, str], ctx: Dict[str, object]) -> str:
    ctx["progkey_configured"] = True
    return "Config -> Configure programmable key"


def action_start_call_with_progkey(step: str, params: Dict[str, str], ctx: Dict[str, object]) -> str:
    ctx["call_state"] = "dialing"
    return "Call -> Start call by programmable key"


def action_dial_call(step: str, params: Dict[str, str], ctx: Dict[str, object]) -> str:
    ctx["call_state"] = "dialing"
    return f"Call -> Dial action ({step})"


def action_answer_call(step: str, params: Dict[str, str], ctx: Dict[str, object]) -> str:
    ctx["call_state"] = "connected"
    return f"Call -> Answer call ({step})"


def action_switch_active_call(step: str, params: Dict[str, str], ctx: Dict[str, object]) -> str:
    ctx["call_switched"] = True
    return "Call -> Switch active call"


def action_end_call(step: str, params: Dict[str, str], ctx: Dict[str, object]) -> str:
    ctx["call_state"] = "idle"
    return "Call -> End communication"


def action_put_on_hold(step: str, params: Dict[str, str], ctx: Dict[str, object]) -> str:
    ctx["call_state"] = "hold"
    return "Call -> Put peer on hold"


def action_retrieve_call(step: str, params: Dict[str, str], ctx: Dict[str, object]) -> str:
    ctx["call_state"] = "connected"
    return "Call -> Retrieve held call"


def action_toggle_mute(step: str, params: Dict[str, str], ctx: Dict[str, object]) -> str:
    ctx["mute"] = not bool(ctx.get("mute", False))
    return f"Audio -> Toggle mute, current mute={ctx['mute']}"


def action_generic(step: str, params: Dict[str, str], ctx: Dict[str, object]) -> str:
    return f"Generic -> No specialized function mapped ({step})"


def build_action_registry() -> Dict[str, ActionFunc]:
    return {
        "open_progkeys": action_open_progkeys,
        "select_programming_page": action_select_programming_page,
        "choose_slot_and_validate": action_choose_slot_and_validate,
        "select_number_type": action_select_number_type,
        "configure_progkey": action_configure_progkey,
        "start_call_with_progkey": action_start_call_with_progkey,
        "dial_call": action_dial_call,
        "answer_call": action_answer_call,
        "hangup_call": action_end_call,
        "hold_call": action_put_on_hold,
        "resume_call": action_retrieve_call,
        "transfer_call": action_generic,
        "conference_start": action_generic,
        "conference_join": action_generic,
        "mute_call": action_toggle_mute,
        "unmute_call": action_toggle_mute,
        "switch_active_call": action_switch_active_call,
        "end_call": action_end_call,
        "put_on_hold": action_put_on_hold,
        "retrieve_call": action_retrieve_call,
        "toggle_mute": action_toggle_mute,
        "generic_action": action_generic,
    }


def load_demo_steps(normalized_path: Path, limit: int) -> List[str]:
    raw = json.loads(normalized_path.read_text(encoding="utf-8"))
    steps = [
        str(entry.get("normalized_action", "")).strip()
        for entry in raw.get("entries", [])
        if str(entry.get("normalized_action", "")).strip()
    ]
    return steps[:limit]


def run_demo(
    patterns_path: Path,
    normalized_path: Path,
    limit: int,
    use_embedding_fallback: bool,
    embedding_model: str,
    embedding_threshold: float,
) -> Dict[str, object]:
    rules = load_rules(patterns_path)
    actions = build_action_registry()
    steps = load_demo_steps(normalized_path, limit=limit)

    embedding_matcher: EmbeddingMatcher | None = None
    if use_embedding_fallback and rules:
        embedding_matcher = EmbeddingMatcher(rules, model_name=embedding_model)

    action_embedder: ActionEmbeddingResolver | None = None
    if use_embedding_fallback:
        action_embedder = ActionEmbeddingResolver(model_name=embedding_model)

    ctx: Dict[str, object] = {"call_state": "idle", "mute": False}

    runs: List[Dict[str, object]] = []

    for idx, step in enumerate(steps, start=1):
        match_result = resolve_rule(
            step_text=step,
            rules=rules,
            embedding_matcher=embedding_matcher,
            embedding_threshold=embedding_threshold,
        )

        if match_result.rule is None:
            pattern_action_name = "generic_action"
            cluster_id: int | str = "N/A"
        else:
            pattern_action_name = match_result.rule.action_name
            cluster_id = match_result.rule.cluster_id

        schema = resolve_action_schema(
            step_text=step,
            pattern_action=pattern_action_name,
            use_embedding_fallback=use_embedding_fallback,
            action_embedder=action_embedder,
            embedding_threshold=embedding_threshold,
        )

        action_fn = actions.get(schema.action, action_generic)
        result = action_fn(step, schema.params, ctx)

        runs.append(
            {
                "index": idx,
                "step": step,
                "cluster_id": cluster_id,
                "pattern_action": pattern_action_name,
                "pattern_params": match_result.params,
                "action": schema.action,
                "params": schema.params,
                "action_schema": {
                    "action": schema.action,
                    "params": schema.params,
                },
                "action_schema_method": schema.method,
                "resolution_method": match_result.method,
                "embedding_score": match_result.score,
                "action_embedding_score": schema.score,
                "execution_result": result,
            }
        )

    return {
        "meta": {
            "loaded_rules": len(rules),
            "demo_steps": len(steps),
            "patterns_path": str(patterns_path),
            "normalized_path": str(normalized_path),
            "pipeline": ["pattern", "regex_match", "embedding_similarity", "generic"],
            "action_schema_actions": SUPPORTED_ACTIONS,
            "embedding_fallback": use_embedding_fallback,
            "embedding_model": embedding_model if use_embedding_fallback else None,
            "embedding_threshold": embedding_threshold if use_embedding_fallback else None,
        },
        "runs": runs,
        "final_context": ctx,
    }


def print_text_report(report: Dict[str, object]) -> None:
    meta = report.get("meta", {})
    runs = report.get("runs", [])
    final_context = report.get("final_context", {})

    print(f"Loaded rules: {meta.get('loaded_rules', 0)}")
    print(f"Demo steps:   {meta.get('demo_steps', 0)}")
    print("-" * 88)

    for run in runs:
        idx = int(run.get("index", 0))
        step = str(run.get("step", ""))
        cluster_id = run.get("cluster_id", "N/A")
        action_name = str(run.get("action", "generic_action"))
        params = run.get("params", {})
        method = str(run.get("resolution_method", ""))
        score = run.get("embedding_score", None)
        result = str(run.get("execution_result", ""))

        print(f"[{idx:02d}] step: {step}")
        print(f"     cluster: {cluster_id} | action: {action_name}")
        print(f"     resolver: {method}")
        if score is not None:
            print(f"     similarity: {score:.4f}")
        if params:
            print(f"     params: {params}")
        print(f"     exec:   {result}")

    print("-" * 88)
    print(f"Final demo context: {final_context}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Demo: pattern -> test action function mapping")
    parser.add_argument(
        "--patterns",
        type=Path,
        default=Path("testrail/step_patterns_N_20_llm.json"),
        help="Path to pattern extraction JSON.",
    )
    parser.add_argument(
        "--normalized",
        type=Path,
        default=Path("testrail/normalized_N_20.json"),
        help="Path to normalized step JSON.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="How many normalized steps to run in demo mode.",
    )
    parser.add_argument(
        "--format",
        type=str,
        default="text",
        choices=["text", "json"],
        help="Output format.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional output file path. If omitted, prints to stdout.",
    )
    parser.add_argument(
        "--embedding-fallback",
        action="store_true",
        help="Enable embedding similarity fallback when regex does not match.",
    )
    parser.add_argument(
        "--embedding-model",
        type=str,
        default="sentence-transformers/all-MiniLM-L6-v2",
        help="Embedding model used in fallback stage.",
    )
    parser.add_argument(
        "--embedding-threshold",
        type=float,
        default=0.62,
        help="Minimum cosine similarity for embedding fallback to accept a match.",
    )
    args = parser.parse_args()

    report = run_demo(
        patterns_path=args.patterns,
        normalized_path=args.normalized,
        limit=args.limit,
        use_embedding_fallback=args.embedding_fallback,
        embedding_model=args.embedding_model,
        embedding_threshold=args.embedding_threshold,
    )

    if args.format == "json":
        payload = json.dumps(report, ensure_ascii=False, indent=2)
        if args.output:
            args.output.write_text(payload, encoding="utf-8")
            print(f"JSON report written: {args.output}")
        else:
            print(payload)
        return

    # Default text mode.
    print_text_report(report)


if __name__ == "__main__":
    main()
