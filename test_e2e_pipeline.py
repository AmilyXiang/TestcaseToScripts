#!/usr/bin/env python3
"""
End-to-end test: KB -> AAO -> DSL -> Action Schema pipeline.

Tests with a small sample from normalized_basic_call_no_oxo_new.json
"""

import json
from pathlib import Path
from aao_to_dsl_pipeline import run


def main():
    script_dir = Path(__file__).parent
    
    # Input
    input_file = script_dir / "normalized_basic_call_no_oxo_new.json"
    
    # Outputs
    dsl_output = script_dir / "test_output_dsl.json"
    action_output = script_dir / "test_output_schema.json"
    
    # Registry paths
    synonym_map = script_dir / "resource" / "synonym_map.json"
    capability_registry = script_dir / "resource" / "capability_registry.json"
    
    print("=" * 60)
    print("E2E Test: KB -> AAO -> DSL -> Action Schema")
    print("=" * 60)
    print(f"Input: {input_file}")
    print(f"DSL output: {dsl_output}")
    print(f"Action output: {action_output}")
    print()
    
    # Run pipeline (no API calls, use local name matching)
    try:
        run(
            input_path=input_file,
            dsl_output_path=dsl_output,
            action_output_path=action_output,
            synonym_map_path=synonym_map,
            capability_registry_path=capability_registry,
            model="deepseek-chat",
            api_key=None,  # No API calls in test
            base_url="https://api.deepseek.com",
        )
        
        print()
        print("=" * 60)
        print("Verification")
        print("=" * 60)
        
        # Verify DSL output
        if dsl_output.exists():
            dsl_data = json.loads(dsl_output.read_text())
            print(f"✓ DSL file created: {len(dsl_data.get('rows', []))} rows")
            if dsl_data.get('meta', {}).get('dsl_registry_stats'):
                stats = dsl_data['meta']['dsl_registry_stats']
                print(f"  DSL Registry: {stats['total_entries']} entries ({stats['action_entries']} action, {stats['assertion_entries']} assertion)")
        
        # Verify Action Schema output
        if action_output.exists():
            schema_data = json.loads(action_output.read_text())
            print(f"✓ Action Schema file created: {len(schema_data.get('rows', []))} rows")
        
        print()
        print("✓ E2E Test PASSED")
        
    except Exception as e:
        print(f"✗ E2E Test FAILED: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
