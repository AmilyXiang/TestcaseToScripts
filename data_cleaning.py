import html
import re
from typing import Any, List


LEADING_INDEX_RE = re.compile(r"^\s*(?:\d+|[A-Za-z])[\.)]\s+")
LEADING_ESCAPED_INDEX_RE = re.compile(r"^\s*(?:\d+|[A-Za-z])\\\.\s+")


def cleanup_markup_text(text: Any) -> Any:
    """Remove HTML/markdown artifacts while preserving meaningful sentence content."""
    if not isinstance(text, str):
        return text

    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = normalized.replace("\u3000", " ").replace("\xa0", " ")
    normalized = html.unescape(normalized)

    # Restore over-escaped double quotes often seen in exported Excel/JSON text.
    while '""' in normalized:
        normalized = normalized.replace('""', '"')

    # Remove markdown image tokens.
    normalized = re.sub(r"!\[[^\]]*\]\([^\)]*\)", "", normalized)

    # Repair soft-wrap HTML breaks injected inside words, e.g. "an<br />other" -> "another".
    normalized = re.sub(r"(?<=\w)\s*<\s*br\s*/?\s*>\s*(?=\w)", "", normalized, flags=re.IGNORECASE)

    # Convert remaining line-break tags to line boundaries.
    normalized = re.sub(r"<\s*br\s*/?\s*>", "\n", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"<\s*/\s*p\s*>\s*<\s*p\s*>", "\n", normalized, flags=re.IGNORECASE)

    # Remove non-semantic HTML tags but keep content.
    normalized = re.sub(r"<\s*img[^>]*>", "", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"<[^>]+>", "", normalized)

    # Normalize whitespace and blank lines.
    normalized = re.sub(r"[ \t]+", " ", normalized)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    normalized = "\n".join(line.strip() for line in normalized.split("\n")).strip()

    return normalized


def has_oxo(text: str) -> bool:
    return "oxo" in text.lower()


def should_merge_wrapped(prev: str, curr: str) -> bool:
    if not prev or not curr:
        return False

    prev_tail = prev.rstrip()
    curr_head = curr.lstrip()
    if not prev_tail or not curr_head:
        return False

    # Keep explicit sentence boundaries as hard splits.
    if prev_tail.endswith((".", "!", "?", ":", ";")):
        return False

    first = curr_head[0]

    # Typical soft-wrap continuation: starts with lowercase, digit, or closing punctuation.
    if first.islower() or first.isdigit() or first in (")", "]", "}", ",", "."):
        return True

    # Hard-wrap continuation for single-letter tokens, e.g. "phone" + "B, ...".
    if re.match(r"^[A-Z](?:\b|[\),\.:;])", curr_head):
        return True

    # If previous line ends with connectors, current line likely continues the same thought.
    if prev_tail.endswith(("(", "[", "{", "=", "/", "-")):
        return True

    return False


def collapse_soft_wrapped_lines(text: str) -> str:
    parts = [line.strip() for line in text.splitlines() if line.strip()]
    if not parts:
        return ""

    merged: List[str] = [parts[0]]
    for part in parts[1:]:
        if should_merge_wrapped(merged[-1], part):
            merged[-1] = f"{merged[-1].rstrip()} {part.lstrip()}"
        else:
            merged.append(part)
    return "\n".join(merged)


def remove_oxo_lines(text: str) -> str:
    kept_lines = [line for line in text.splitlines() if not has_oxo(line)]
    return "\n".join(line for line in kept_lines if line.strip()).strip()


def _normalize_leading_index(line: str) -> str:
    cleaned = line
    # Handle escaped markdown numbering such as "1\. text".
    cleaned = LEADING_ESCAPED_INDEX_RE.sub("", cleaned)
    # Handle standard numbering such as "1. text" / "1) text" / "A. text".
    cleaned = LEADING_INDEX_RE.sub("", cleaned)
    return cleaned.strip()


def clean_step_text(text: Any) -> Any:
    """Clean step/action-like text and remove leading list numbering markers per line."""
    if not isinstance(text, str):
        return text

    normalized = cleanup_markup_text(text)
    normalized = remove_oxo_lines(normalized)
    if not normalized:
        return ""

    normalized = collapse_soft_wrapped_lines(normalized)
    normalized = re.sub(r"(?<=\d)\\\.", ".", normalized)

    lines = [line for line in normalized.split("\n")]
    lines = [_normalize_leading_index(line) for line in lines]
    lines = [line for line in lines if line]

    return "\n".join(lines).strip()


def split_numbered_points(text: Any) -> List[str]:
    """Split a cleaned multi-point text into sub points when possible."""
    if not isinstance(text, str) or not text.strip():
        return []

    normalized = clean_step_text(text)
    # When multiple numbered points are packed in one line, insert line breaks before each index.
    normalized = re.sub(r"\s+(?=(?:\d+|[A-Za-z])[\.)]\s+)", "\n", normalized)
    normalized = re.sub(r"\s+(?=(?:\d+|[A-Za-z])\\\.\s+)", "\n", normalized)

    points = [_normalize_leading_index(line) for line in normalized.split("\n")]
    points = [point.strip() for point in points if point and point.strip()]
    return points


def clean_text_list(values: Any) -> List[Any]:
    """Clean list[str] values with OXO removal and soft-wrap merging."""
    if not isinstance(values, list):
        return []

    cleaned: List[Any] = []
    for item in values:
        if not isinstance(item, str):
            cleaned.append(item)
            continue

        normalized = clean_step_text(item)
        if isinstance(normalized, str) and normalized.strip():
            cleaned.append(normalized.strip())

    merged: List[Any] = []
    for item in cleaned:
        if not isinstance(item, str):
            merged.append(item)
            continue

        if merged and isinstance(merged[-1], str) and should_merge_wrapped(merged[-1], item):
            merged[-1] = f"{merged[-1].rstrip()} {item.lstrip()}"
        else:
            merged.append(item)

    return merged


def canonicalize_action_text(text: Any) -> Any:
    if not isinstance(text, str):
        return text

    normalized = cleanup_markup_text(text)
    normalized = re.sub(r"\s+", " ", normalized.strip())

    # Canonicalize equivalent incoming-call phrasings with explicit actor.
    normalized = re.sub(
        r"^(Receive a normal incoming call on the phone|Receive an incoming call on the phone|Phone receives a normal incoming call(?: on the phone)?)\.?$",
        "Phone receives an incoming call.",
        normalized,
        flags=re.IGNORECASE,
    )

    # Canonicalize remote-side answer/reject events.
    normalized = re.sub(
        r"^(Answer the call from the remote side|Have the remote side answer the call|Receive an answer from the remote side|Receive an answer to the call from the remote side|Receive an answer from the remote side for the call)\.?$",
        "Remote side answers the call.",
        normalized,
        flags=re.IGNORECASE,
    )
    normalized = re.sub(
        r"^(Have the remote side reject the call|Remote side reject the call|Receive a reject from the remote side)\.?$",
        "Remote side rejects the call.",
        normalized,
        flags=re.IGNORECASE,
    )

    # Repair common actor drift from model generations.
    if re.search(r"remote side", normalized, flags=re.IGNORECASE) and re.search(r"incoming call", normalized, flags=re.IGNORECASE):
        normalized = "Phone receives an incoming call."

    # Normalize capitalization variants for common button names.
    normalized = re.sub(r"\bPress the silence button\.?$", "Press the Silence button.", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bPress the switch button\.?$", "Press the Switch button.", normalized, flags=re.IGNORECASE)

    # Canonical casing for common domain terms and labels.
    normalized = re.sub(r"\boxe\b", "OXE", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*20h\b", "ALE-20h", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*30h\b", "ALE-30h", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*20\b", "ALE-20", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*30\b", "ALE-30", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*300\b", "ALE-300", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*400\b", "ALE-400", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*500\b", "ALE-500", normalized, flags=re.IGNORECASE)

    normalized = re.sub(r"\btransfer\b", "Transfer", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bsilence\b", "Silence", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bswitch\b", "Switch", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bhold\b", "Hold", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\brelease\b", "Release", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bconference\b", "Conference", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bemergency\b", "Emergency", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bguard\b", "Guard", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\boperator\b", "Operator", normalized, flags=re.IGNORECASE)

    normalized = re.sub(r"\bphone\b", "phone", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bremote side\b", "Remote side", normalized, flags=re.IGNORECASE)

    # Ensure final sentence punctuation.
    if normalized and not re.search(r"[.!?]$", normalized):
        normalized += "."

    return normalized


def canonicalize_expected_text(text: Any) -> Any:
    if not isinstance(text, str):
        return text
    normalized = cleanup_markup_text(text)
    normalized = re.sub(r"\s+", " ", normalized.strip())
    normalized = re.sub(r"\boxe\b", "OXE", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*20h\b", "ALE-20h", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*30h\b", "ALE-30h", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*20\b", "ALE-20", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*30\b", "ALE-30", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*300\b", "ALE-300", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*400\b", "ALE-400", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*500\b", "ALE-500", normalized, flags=re.IGNORECASE)
    return normalized


def canonicalize_precondition_text(text: Any) -> Any:
    if text is None:
        return None
    if not isinstance(text, str):
        return text

    normalized = cleanup_markup_text(text)
    normalized = re.sub(r"\s+", " ", normalized.strip())
    normalized = re.sub(r"\boxe\b", "OXE", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*20h\b", "ALE-20h", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*30h\b", "ALE-30h", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*20\b", "ALE-20", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*30\b", "ALE-30", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*300\b", "ALE-300", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*400\b", "ALE-400", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*500\b", "ALE-500", normalized, flags=re.IGNORECASE)
    return normalized or None


def canonicalize_keywords(values: Any) -> List[str]:
    if not isinstance(values, list):
        return []

    normalized: List[str] = []
    seen = set()
    for item in values:
        if not isinstance(item, str):
            continue
        token = item.strip().lower()
        token = re.sub(r"\s+", "-", token)
        token = re.sub(r"[^a-z0-9\-_/]", "", token)
        if not token or token in seen:
            continue
        seen.add(token)
        normalized.append(token)
    return normalized
