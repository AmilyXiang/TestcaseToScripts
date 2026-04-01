#!/usr/bin/env python3
"""
DSL validator and auto-supplement mechanism.

Provides functions to:
1. Load DSL registry
2. Look up DSL entries for given action/assertion intent
3. Auto-create missing DSL entries for new actions/assertions
"""

import json
from pathlib import Path
from typing import Any, Dict, Optional


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class DSLValidator:
    """DSL registry validator with auto-supplement capability."""
    
    def __init__(self, dsl_registry_path: Path, capability_registry_path: Path):
        self.dsl_registry_path = dsl_registry_path
        self.capability_registry_path = capability_registry_path
        self.dsl_registry = load_json(dsl_registry_path) if dsl_registry_path.exists() else {"dsl_entries": {}, "meta": {}}
        self.capability_registry = load_json(capability_registry_path) if capability_registry_path.exists() else {}
        self.dsl_entries = self.dsl_registry.get("dsl_entries", {})
        self._build_lookup_index()
    
    def _build_lookup_index(self) -> None:
        """Build index: intent -> dsl_id for fast lookup."""
        self.intent_to_dsl_id = {}
        for dsl_id, entry in self.dsl_entries.items():
            intent = entry.get("intent", "")
            if intent:
                self.intent_to_dsl_id[intent] = dsl_id
    
    def lookup_dsl(self, intent: str, entry_type: str = "action") -> Optional[Dict[str, Any]]:
        """
        Look up DSL entry by intent.
        
        Args:
            intent: Action or assertion intent key
            entry_type: "action" or "assertion"
        
        Returns:
            DSL entry dict or None
        """
        # Try direct lookup
        if intent in self.intent_to_dsl_id:
            return self.dsl_entries.get(self.intent_to_dsl_id[intent])
        
        # Try to find by key
        for dsl_id, entry in self.dsl_entries.items():
            if entry.get("key") == intent and entry.get("type") == entry_type:
                return entry
        
        return None
    
    def get_or_create_dsl(self, intent: str, entry_type: str = "action", category: str = "Custom", description: str = "") -> Dict[str, Any]:
        """
        Get DSL entry, or create a new placeholder if not found.
        
        Args:
            intent: Action or assertion intent key
            entry_type: "action" or "assertion"
            category: Capability category (default "Custom")
            description: Human-readable description
        
        Returns:
            DSL entry dict
        """
        existing = self.lookup_dsl(intent, entry_type)
        if existing:
            return existing
        
        # Create new placeholder entry
        dsl_id = f"{entry_type}.{category}.{intent}"
        new_entry = {
            "type": entry_type,
            "category": category,
            "key": intent,
            "description": description,
            "intent": intent,
            "actor": "current_device" if entry_type == "action" else "",
            "target": "" if entry_type == "action" else "",
            "evidence_template": description,
            "status": "auto_created",
            "auto_created": True,
        }
        
        self.dsl_entries[dsl_id] = new_entry
        self.intent_to_dsl_id[intent] = dsl_id
        
        # Persist changes
        self._save_dsl_registry()
        
        return new_entry
    
    def _save_dsl_registry(self) -> None:
        """Save updated DSL registry to disk."""
        self.dsl_registry["dsl_entries"] = self.dsl_entries
        self.dsl_registry["meta"]["total_entries"] = len(self.dsl_entries)
        save_json(self.dsl_registry_path, self.dsl_registry)
    
    def validate_aao_entry(self, aao_entry: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate and supplement DSL entries for an AAO entry.
        
        If action/assertion intents are missing DSL entries, auto-create them.
        
        Args:
            aao_entry: Normalized AAO entry
        
        Returns:
            Updated AAO entry with DSL validation results
        """
        action_intent = aao_entry.get("action_intent", "")
        assertion_intent = aao_entry.get("assertion_intent", "")
        
        action_dsl = None
        assertion_dsl = None
        
        if action_intent:
            action_dsl = self.get_or_create_dsl(
                action_intent,
                entry_type="action",
                category="Custom",
                description=aao_entry.get("normalized_action", "")
            )
        
        if assertion_intent:
            assertion_dsl = self.get_or_create_dsl(
                assertion_intent,
                entry_type="assertion",
                category="Custom",
                description=aao_entry.get("normalized_expected_result", "")
            )
        
        return {
            **aao_entry,
            "dsl_validation": {
                "action_dsl_found": action_dsl is not None,
                "assertion_dsl_found": assertion_dsl is not None,
                "auto_created": False,
            }
        }
    
    def get_stats(self) -> Dict[str, Any]:
        """Get registry statistics."""
        action_count = sum(1 for e in self.dsl_entries.values() if e.get("type") == "action")
        assertion_count = sum(1 for e in self.dsl_entries.values() if e.get("type") == "assertion")
        placeholder_count = sum(1 for e in self.dsl_entries.values() if e.get("status") == "placeholder")
        auto_created_count = sum(1 for e in self.dsl_entries.values() if e.get("status") == "auto_created")
        
        return {
            "total_entries": len(self.dsl_entries),
            "action_entries": action_count,
            "assertion_entries": assertion_count,
            "placeholder_entries": placeholder_count,
            "auto_created_entries": auto_created_count,
        }


def main():
    """Demo: validate and auto-create DSL entries."""
    script_dir = Path(__file__).parent
    dsl_registry = script_dir / "resource" / "dsl_registry.json"
    capability_registry = script_dir / "resource" / "capability_registry.json"
    
    validator = DSLValidator(dsl_registry, capability_registry)
    
    print("DSL Validator initialized")
    print(f"Stats: {validator.get_stats()}")
    
    # Test: lookup existing entry
    existing = validator.lookup_dsl("take_call", "action")
    print(f"\nLookup 'take_call': {'Found' if existing else 'Not found'}")
    if existing:
        print(f"  → intent={existing.get('intent')}, category={existing.get('category')}")
    
    # Test: auto-create new entry
    new_entry = validator.get_or_create_dsl("custom_test_action", "action", "Testing", "Custom test action")
    print(f"\nAuto-create 'custom_test_action': Created")
    print(f"  → intent={new_entry.get('intent')}, status={new_entry.get('status')}")
    
    print(f"\nFinal stats: {validator.get_stats()}")


if __name__ == "__main__":
    main()
