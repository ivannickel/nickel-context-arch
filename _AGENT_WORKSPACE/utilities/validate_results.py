#!/usr/bin/env python3
"""
Validate transcript classification results.
Checks coverage, distribution, and quality metrics.
"""

import re
from pathlib import Path
from collections import Counter

BATCHES_DIR = Path("_AGENT_WORKSPACE/transcript_batches")

def parse_classification(content: str) -> list:
    """Extract all classifications from a batch result file."""
    classifications = []

    # Find all transcript blocks
    blocks = re.split(r'===\s*TRANSCRIPT:\s*([^\n]+)', content)[1:]

    for i in range(0, len(blocks), 2):
        if i+1 >= len(blocks):
            break

        filename = blocks[i].strip()
        fields_text = blocks[i+1]

        # Extract fields
        classification = {'filename': filename}

        field_patterns = {
            'call_type': r'call_type:\s*(\w+)',
            'deal_stage': r'deal_stage:\s*(\w+)',
            'customer_segment': r'customer_segment:\s*(\w+)',
            'has_pain_points': r'has_pain_points:\s*(true|false)',
            'has_objections': r'has_objections:\s*(true|false)',
            'has_competitive_intel': r'has_competitive_intel:\s*(true|false)',
            'has_use_case': r'has_use_case:\s*(true|false)',
            'has_pricing_discussion': r'has_pricing_discussion:\s*(true|false)',
            'has_integration_needs': r'has_integration_needs:\s*(true|false)',
            'primary_industry': r'primary_industry:\s*(\w+)',
            'transaction_volume': r'transaction_volume:\s*(\w+)',
            'ar_vs_ap': r'ar_vs_ap:\s*(\w+)',
            'extraction_priority': r'extraction_priority:\s*(\w+)',
        }

        for field, pattern in field_patterns.items():
            match = re.search(pattern, fields_text)
            if match:
                value = match.group(1)
                if value in ('true', 'false'):
                    value = value == 'true'
                classification[field] = value
            else:
                classification[field] = None

        classifications.append(classification)

    return classifications

def main():
    print("\n=== TRANSCRIPT CLASSIFICATION VALIDATION ===\n")

    # Load all results
    all_classifications = []
    result_files = sorted(BATCHES_DIR.glob("batch_*_results.md"))

    print(f"Found {len(result_files)} batch result files\n")

    for result_file in result_files:
        with result_file.open('r', encoding='utf-8') as f:
            content = f.read()
            classifications = parse_classification(content)
            all_classifications.extend(classifications)
            print(f"[OK] {result_file.name}: {len(classifications)} transcripts")

    print(f"\n[OK] Total transcripts classified: {len(all_classifications)}")

    # Validation checks
    print("\n=== QUALITY CHECKS ===\n")

    # Check 1: Coverage
    expected_count = 165
    actual_count = len(all_classifications)
    coverage_pct = (actual_count / expected_count) * 100
    print(f"Coverage: {actual_count}/{expected_count} ({coverage_pct:.1f}%)")

    if actual_count == expected_count:
        print("  [PASS] All transcripts classified")
    else:
        print(f"  [FAIL] Missing {expected_count - actual_count} transcripts")

    # Check 2: Field completeness
    incomplete = [c for c in all_classifications if None in c.values()]
    if not incomplete:
        print("\n[PASS] All transcripts have complete fields")
    else:
        print(f"\n[FAIL] {len(incomplete)} transcripts missing fields")
        for c in incomplete[:5]:
            missing = [k for k, v in c.items() if v is None]
            print(f"  - {c['filename']}: missing {missing}")

    # Check 3: Priority distribution
    priority_counts = Counter(c['extraction_priority'] for c in all_classifications if c.get('extraction_priority'))
    total = sum(priority_counts.values())

    print(f"\n=== PRIORITY DISTRIBUTION ===")
    print(f"High:   {priority_counts['high']:3d} ({priority_counts['high']/total*100:5.1f}%) [Target: 15-25%]")
    print(f"Medium: {priority_counts['medium']:3d} ({priority_counts['medium']/total*100:5.1f}%) [Target: 45-55%]")
    print(f"Low:    {priority_counts['low']:3d} ({priority_counts['low']/total*100:5.1f}%) [Target: 20-40%]")

    # Check if within ranges
    high_pct = priority_counts['high']/total*100
    medium_pct = priority_counts['medium']/total*100

    if 15 <= high_pct <= 25 and 45 <= medium_pct <= 55:
        print("\n[PASS] Priority distribution within target ranges")
    else:
        print("\n[WARN] Priority distribution outside target ranges")

    # Check 4: Strategic signal coverage
    signal_fields = ['has_pain_points', 'has_objections', 'has_competitive_intel',
                     'has_use_case', 'has_pricing_discussion', 'has_integration_needs']

    with_signals = 0
    for c in all_classifications:
        if any(c.get(field) for field in signal_fields):
            with_signals += 1

    signal_pct = (with_signals / actual_count) * 100
    print(f"\n=== STRATEGIC SIGNAL COVERAGE ===")
    print(f"Transcripts with ≥1 signal: {with_signals}/{actual_count} ({signal_pct:.1f}%)")

    if signal_pct >= 70:
        print("[PASS] Signal coverage meets 70% target")
    else:
        print("[FAIL] Signal coverage below 70% target")

    # Summary statistics
    print(f"\n=== SUMMARY STATISTICS ===")

    print(f"\nCall Types:")
    for call_type, count in Counter(c['call_type'] for c in all_classifications).most_common():
        print(f"  {call_type:12s}: {count:3d} ({count/actual_count*100:5.1f}%)")

    print(f"\nCustomer Segments:")
    for segment, count in Counter(c['customer_segment'] for c in all_classifications).most_common():
        print(f"  {segment:12s}: {count:3d} ({count/actual_count*100:5.1f}%)")

    print(f"\nIndustries:")
    for industry, count in Counter(c['primary_industry'] for c in all_classifications).most_common():
        print(f"  {industry:20s}: {count:3d} ({count/actual_count*100:5.1f}%)")

    print(f"\nStrategic Signals:")
    for field in signal_fields:
        true_count = sum(1 for c in all_classifications if c.get(field))
        print(f"  {field:25s}: {true_count:3d} ({true_count/actual_count*100:5.1f}%)")

    print("\n[OK] Validation complete!\n")

if __name__ == "__main__":
    main()
