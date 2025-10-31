#!/usr/bin/env python3
"""
Cleanup script for files with raw YAML field duplicates (no comment header)
Specifically targeting files 098-099 and 111-120
"""

import re
from pathlib import Path

BASE_DIR = Path(r"c:\Users\dietl\VSCode Projects\taste_systems\gtm_operating_system\gtm_engagements\03_active_client\nickel_ivan\nickel_gtm_context_architecture\knowledge_base\meetings_md")

# Files that need this specific cleanup
TARGET_FILES = [
    "098_nickel-for-sb-rotary-check-in_2025-09-23.md",
    "099_nickel-vip-software_2025-08-27.md",
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

def clean_file(filepath):
    """Remove raw YAML duplicates, keep only the block with the comment header"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the meeting_number line (last Circleback field)
        meeting_match = re.search(r'^meeting_number: \d+$', content, re.MULTILINE)
        if not meeting_match:
            return 0, 'no_meeting_number_found'

        meeting_line_end = meeting_match.end()

        # Find the strategic classification comment header
        header_match = re.search(r'^# === STRATEGIC CLASSIFICATION \(Transcript Classifier Agent v1\.0\) ===$', content, re.MULTILINE)
        if not header_match:
            return 0, 'no_header_found'

        header_start = header_match.start()

        # Find the end of YAML frontmatter (---)
        yaml_end_match = re.search(r'^---$', content[header_start:], re.MULTILINE)
        if not yaml_end_match:
            return 0, 'no_yaml_end_found'

        # Extract content before, during, and after
        before = content[:meeting_line_end]  # Up to meeting_number
        strategic_block = content[header_start:header_start + yaml_end_match.end()]  # The good block
        after = content[header_start + yaml_end_match.end():]  # Rest of file

        # Reconstruct: before + newline + strategic block + after
        new_content = before + '\n' + strategic_block + after

        # Count removed duplicates (rough estimate)
        # Count how many sets of classification fields were in the removed section
        removed_section = content[meeting_line_end:header_start]
        duplicate_count = removed_section.count('deal_stage:')  # Each dup has this field

        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return duplicate_count, 'success'

    except Exception as e:
        return 0, f'error: {str(e)}'

def main():
    """Process target files"""
    total_removed = 0
    results = []

    for filename in TARGET_FILES:
        filepath = BASE_DIR / filename
        if filepath.exists():
            removed, status = clean_file(filepath)
            total_removed += removed
            results.append((filename, removed, status))
            print(f"{filename}: {removed} duplicates removed - {status}")
        else:
            results.append((filename, 0, 'not_found'))
            print(f"{filename}: FILE NOT FOUND")

    # Summary
    print(f"\n{'='*70}")
    print("CLEANUP SUMMARY - Raw YAML Duplicates")
    print(f"{'='*70}")
    print(f"Files targeted: {len(TARGET_FILES)}")
    print(f"Total duplicates removed: {total_removed}")
    print(f"Successfully cleaned: {sum(1 for _, _, s in results if s == 'success')}")
    print(f"Errors: {sum(1 for _, _, s in results if 'error' in s)}")

if __name__ == "__main__":
    main()
