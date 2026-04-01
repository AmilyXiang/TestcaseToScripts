#!/usr/bin/env python3
"""
Generate baseline DSL registry from capability_registry.json annotations.

This creates a persistent DSL entry for each action/assertion capability,
enabling automatic DSL lookup and auto-creation for AAO entries.
"""

import json
from pathlib import Path
from typing import Any, Dict


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def generate_dsl_registry(capability_registry_path: Path, output_path: Path) -> None:
    """Generate baseline DSL entries from capability registry."""
    
    registry = load_json(capability_registry_path)
    annotations = registry.get("annotations", {})
    actions = annotations.get("action", {})
    assertions = annotations.get("assertion", {})
    
    dsl_entries = {}
    action_count = 0
    assertion_count = 0
    
    # Generate DSL entries for each action
    for category, capabilities in actions.items():
        if not isinstance(capabilities, dict):
            continue
        for action_key, description in capabilities.items():
            dsl_id = f"action.{category}.{action_key}"
            dsl_entries[dsl_id] = {
                "type": "action",
                "category": category,
                "key": action_key,
                "description": str(description or ""),
                "intent": action_key,  # Placeholder: use key as intent
                "actor": "current_device",  # Placeholder
                "target": "",  # Placeholder
                "evidence_template": description,  # Reuse description as evidence template
                "status": "placeholder",  # Mark as auto-generated placeholder
            }
            action_count += 1
    
    # Generate DSL entries for each assertion
    for category, capabilities in assertions.items():
        if not isinstance(capabilities, dict):
            continue
        for assertion_key, description in capabilities.items():
            dsl_id = f"assertion.{category}.{assertion_key}"
            dsl_entries[dsl_id] = {
                "type": "assertion",
                "category": category,
                "key": assertion_key,
                "description": str(description or ""),
                "intent": assertion_key,  # Placeholder: use key as intent
                "evidence_template": description,  # Reuse description as evidence template
                "status": "placeholder",  # Mark as auto-generated placeholder
            }
            assertion_count += 1
    
    output = {
        "meta": {
            "description": "Baseline DSL registry generated from capability_registry.json",
            "version": "1.0",
            "total_entries": len(dsl_entries),
            "action_entries": action_count,
            "assertion_entries": assertion_count,
        },
        "dsl_entries": dsl_entries,
    }
    
    save_json(output_path, output)
    print(f"✓ Generated DSL registry with {action_count} actions + {assertion_count} assertions = {len(dsl_entries)} total entries")
    print(f"  Saved to: {output_path}")


if __name__ == "__main__":
    script_dir = Path(__file__).parent
    capability_registry = script_dir / "resource" / "capability_registry.json"
    output_file = script_dir / "resource" / "dsl_registry.json"
    
    if not capability_registry.exists():
        print(f"Error: {capability_registry} not found")
        exit(1)
    
    generate_dsl_registry(capability_registry, output_file)
