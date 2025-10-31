#!/usr/bin/env python3
"""
Frontmatter Cleanup Script v2 - Agent 04 Batch
Handles both types of duplicate patterns:
1. Full blocks with # === STRATEGIC CLASSIFICATION header
2. Raw YAML fields without header
"""

import re
from pathlib import Path

BASE_DIR = Path(r"c:\Users\dietl\VSCode Projects\taste_systems\gtm_operating_system\gtm_engagements\03_active_client\nickel_ivan\nickel_gtm_context_architecture\knowledge_base\meetings_md")

# All files 091-120
ALL_FILES = [
    "091_nickel-demo-rachel-and-damian-foster_2025-09-03.md",
    "092_nickel-demo-request-shannon-rayman_2025-09-23.md",
    "093_nickel-demo-aurelie-nguyen_2025-08-27.md",
    "094_nickel-for-surgenex-reconnectfinalize_2025-10-10.md",
    "095_nickel-for-1800-water-damage-reconnect-check-in_2025-10-21.md",
    "096_nickel-for-gra-services-reconnect-ryanjosh-christi_2025-09-26.md",
    "097_nickel-demo-request-bobbie-smith_2025-10-15.md",
    "098_nickel-for-sb-rotary-check-in_2025-09-23.md",
    "099_nickel-vip-software_2025-08-27.md",
    "100_christian-ashley-nickel-str-management-check-in_2025-10-02.md",
    "101_nickel-demo-request-deborah-enriquez_2025-09-10.md",
    "102_nickel-demo-request-jason-molaison_2025-09-10.md",
    "103_nickel-platform-demo-charles-stafford_2025-10-16.md",
    "104_nickel-demo-sterling-chipman_2025-08-29.md",
    "105_nickel-for-blue-hills-at-round-top_2025-09-24.md",
    "106_nickel-demo-request-thanmay-kumar_2025-09-30.md",
    "107_nickel-demo-request-lyle-applbaum_2025-09-26.md",
    "108_nickel-demo-request-amanda-pettay_2025-10-16.md",
    "109_nickel-demo-request-byron-floyd_2025-09-29.md",
    "110_nickel-demo-request-ryan-jacob_2025-09-22.md",
    "111_nickel-demo-request-daniel-power_2025-10-01.md",
    "112_nickel-demo-request-john-macari_2025-10-14.md",
    "113_nickel-demo-request-tiffany-smith_2025-09-10.md",
    "114_nickel-for-sikama-international-christian-jeffrey_2025-09-29.md",
    "115_nickel-demo-request-winston-punla_2025-09-29.md",
    "116_nickel-demo-tom-leenheer_2025-09-05.md",
    "117_megan-jacoby-and-jacob-greenberg_2025-07-31.md",
    "118_herchel-biddy-and-jacob-greenberg_2025-08-05.md",
    "119_nickel-platform-demo-andrew-_2025-10-08.md",
    "120_jason-lilly-and-jacob-greenberg_2025-07-30.md",
]

# Pattern of classification fields
CLASSIFICATION_FIELDS = [
    'call_type', 'deal_stage', 'customer_segment', 'has_pain_points',
    'has_objections', 'has_competitive_intel', 'has_use_case',
    'has_pricing_discussion', 'has_integration_needs', 'primary_industry',
    'transaction_volume', 'ar_vs_ap', 'processed', 'dimensional_extracted',
    'extraction_priority'
]

def clean_frontmatter(content):
    """Remove all duplicate frontmatter and reconstruct with single block"""

    lines = content.split('\n')
    result_lines = []

    # Find frontmatter boundaries
    frontmatter_start = -1
    frontmatter_end = -1
    yaml_delim_count = 0

    for i, line in enumerate(lines):
        if line.strip() == '---':
            yaml_delim_count += 1
            if yaml_delim_count == 1:
                frontmatter_start = i
            elif yaml_delim_count == 2:
                frontmatter_end = i
                break

    if frontmatter_start == -1 or frontmatter_end == -1:
        return content, 0  # No valid frontmatter found

    # Extract frontmatter
    frontmatter_lines = lines[frontmatter_start+1:frontmatter_end]

    # Separate Circleback fields from classification fields
    circleback_fields = []
    classification_blocks = []
    current_block = []
    in_classification = False

    for line in frontmatter_lines:
        if '# === STRATEGIC CLASSIFICATION' in line:
            if current_block:
                # Save previous non-classification content
                if not in_classification:
                    circleback_fields.extend(current_block)
                current_block = []
            in_classification = True
            continue

        # Check if line is a classification field
        field_name = line.split(':')[0].strip() if ':' in line else ''
        if field_name in CLASSIFICATION_FIELDS:
            current_block.append(line)
        elif in_classification and not line.strip():
            # Empty line might be end of classification block
            if current_block:
                classification_blocks.append(current_block)
                current_block = []
                in_classification = False
        elif not in_classification:
            circleback_fields.append(line)
        else:
            # Part of classification block
            current_block.append(line)

    # Don't forget last block
    if current_block:
        if in_classification:
            classification_blocks.append(current_block)
        else:
            circleback_fields.extend(current_block)

    # Use last classification block
    final_classification = classification_blocks[-1] if classification_blocks else []

    # Reconstruct frontmatter
    result_lines.append(lines[frontmatter_start])  # First ---
    result_lines.extend(circleback_fields)
    if final_classification:
        result_lines.append('# === STRATEGIC CLASSIFICATION (Transcript Classifier Agent v1.0) ===')
        result_lines.extend(final_classification)
    result_lines.append(lines[frontmatter_end])  # Second ---

    # Add rest of content
    result_lines.extend(lines[frontmatter_end+1:])

    duplicates_removed = len(classification_blocks) - 1 if len(classification_blocks) > 1 else 0

    return '\n'.join(result_lines), duplicates_removed

def process_file(filepath):
    """Process a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, removed_count = clean_frontmatter(content)

        if removed_count > 0 or new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return removed_count, 'success'

        return 0, 'no_changes'

    except Exception as e:
        return 0, f'error: {str(e)}'

def main():
    """Process all files"""
    results = {}
    total_duplicates = 0

    for filename in ALL_FILES:
        filepath = BASE_DIR / filename
        if filepath.exists():
            removed, status = process_file(filepath)
            results[filename] = (removed, status)
            total_duplicates += removed
            print(f"{filename}: {removed} duplicates removed - {status}")
        else:
            results[filename] = (0, 'not_found')
            print(f"{filename}: FILE NOT FOUND")

    # Summary
    print(f"\n{'='*70}")
    print("BATCH 04 CLEANUP SUMMARY")
    print(f"{'='*70}")
    print(f"Total files: {len(ALL_FILES)}")
    print(f"Total duplicates removed: {total_duplicates}")
    print(f"Files with errors: {sum(1 for _, (_, s) in results.items() if 'error' in s)}")
    print(f"Files not found: {sum(1 for _, (_, s) in results.items() if s == 'not_found')}")
    print(f"Files successfully cleaned: {sum(1 for _, (_, s) in results.items() if s == 'success')}")

if __name__ == "__main__":
    main()
