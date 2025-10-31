#!/usr/bin/env python3
"""
Frontmatter Cleanup Script - Agent 04 Batch
Removes duplicate strategic classification blocks from transcripts
"""

import re
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(r"c:\Users\dietl\VSCode Projects\taste_systems\gtm_operating_system\gtm_engagements\03_active_client\nickel_ivan\nickel_gtm_context_architecture\knowledge_base\meetings_md")

# Files to process (096-120)
FILES = [
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

def remove_duplicate_frontmatter(content):
    """Remove duplicate strategic classification blocks, keep only the last one"""

    # Pattern to match strategic classification block
    pattern = r'# === STRATEGIC CLASSIFICATION \(Transcript Classifier Agent v1\.0\) ===\n(?:^[a-z_]+: [^\n]+\n)+?'

    # Find all matches
    matches = list(re.finditer(pattern, content, re.MULTILINE))

    if len(matches) <= 1:
        return content, 0

    # Remove all but the last match
    duplicates_to_remove = matches[:-1]

    # Remove duplicates in reverse order to maintain string positions
    for match in reversed(duplicates_to_remove):
        content = content[:match.start()] + content[match.end():]

    return content, len(duplicates_to_remove)

def process_file(filepath):
    """Process a single file"""
    try:
        # Read file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove duplicates
        new_content, removed_count = remove_duplicate_frontmatter(content)

        # Write back if changes were made
        if removed_count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

        return {
            'filename': filepath.name,
            'duplicates_removed': removed_count,
            'status': 'success'
        }

    except Exception as e:
        return {
            'filename': filepath.name,
            'duplicates_removed': 0,
            'status': 'error',
            'error': str(e)
        }

def main():
    """Main processing function"""
    results = []

    for filename in FILES:
        filepath = BASE_DIR / filename
        if filepath.exists():
            result = process_file(filepath)
            results.append(result)
            print(f"[OK] {filename}: Removed {result['duplicates_removed']} duplicates")
        else:
            results.append({
                'filename': filename,
                'duplicates_removed': 0,
                'status': 'not_found'
            })
            print(f"[MISSING] {filename}: File not found")

    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    total_processed = sum(1 for r in results if r['status'] == 'success')
    total_duplicates = sum(r['duplicates_removed'] for r in results)
    print(f"Files processed: {total_processed}")
    print(f"Total duplicates removed: {total_duplicates}")
    print(f"Files not found: {sum(1 for r in results if r['status'] == 'not_found')}")
    print(f"Errors: {sum(1 for r in results if r['status'] == 'error')}")

if __name__ == "__main__":
    main()
