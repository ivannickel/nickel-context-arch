"""
Frontmatter Cleanup Script - Agent 02 Batch
Removes duplicate strategic classification blocks from transcripts
"""

import re
import os
from pathlib import Path

# Batch assignment for Agent 02
BATCH_FILES = [
    "031_shaneque-downie-and-colton-ofarrell_2025-09-04.md",
    "032_homes-by-triple-m-nickel-kickoff-call_2025-09-16.md",
    "033_michael-mann-and-colton-ofarrell_2025-07-30.md",
    "034_ashley-melton-and-colton-ofarrell_2025-07-29.md",
    "035_belmont-custom-remodeling-llc-nickel-kickoff-call_2025-09-18.md",
    "036_mark-hull-and-colton-ofarrell_2025-08-18.md",
    "037_kumon-of-draper-nickel-kickoff-call_2025-09-24.md",
    "038_marc-colton-nickel-follow-up_2025-07-28.md",
    "039_capris-keller-and-colton-ofarrell_2025-07-14.md",
    "040_ecogate-nickel_2025-08-28.md",
    "041_jeff-colton-nickel-follow-up_2025-07-31.md",
    "042_marc-stelzer-and-colton-ofarrell_2025-08-20.md",
    "043_dan-sizelove-and-colton-ofarrell_2025-07-24.md",
    "044_kevin-redmon-and-colton-ofarrell_2025-08-06.md",
    "045_mateo-vosganian-and-colton-ofarrell_2025-08-13.md",
    "046_archadeck-of-austin-nickel-review-call_2025-09-24.md",
    "047_billy-siegler-and-colton-ofarrell_2025-08-18.md",
    "048_american-home-renewal-nickel_2025-07-22.md",
    "049_peter-trang-and-colton-ofarrell_2025-08-04.md",
    "050_nickel-kick-off-call_2025-09-04.md",
    "051_debbie-bechtel-and-colton-ofarrell_2025-08-01.md",
    "052_oscar-ob-garden-and-tina-boundless-data-colton-nic_2025-07-24.md",
    "053_vinay-shah-and-colton-ofarrell_2025-07-22.md",
    "054_mike-lovelady-and-colton-ofarrell_2025-07-30.md",
    "055_vijaya-kumar-and-colton-ofarrell_2025-07-23.md",
    "056_jordan-stealey-and-christian-sheerer_2025-07-18.md",
    "057_chris-sneed-and-christian-sheerer_2025-08-27.md",
    "058_nickel-for-abelrichard-jimmy-jacob-re-pos_2025-10-16.md",
    "059_patricia-zavala-and-christian-sheerer_2025-07-10.md",
    "060_jagadish-sudarsanam-and-christian-sheerer_2025-08-11.md",
]

BASE_DIR = Path(r"c:\Users\dietl\VSCode Projects\taste_systems\gtm_operating_system\gtm_engagements\03_active_client\nickel_ivan\nickel_gtm_context_architecture\knowledge_base\meetings_md")

def extract_frontmatter(content):
    """Extract YAML frontmatter and body from markdown content"""
    # Match frontmatter between --- markers
    pattern = r'^---\n(.*?)\n---\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)

    if not match:
        return None, content

    return match.group(1), match.group(2)

def remove_duplicate_strategic_blocks(frontmatter):
    """Remove duplicate strategic classification blocks, keeping only the last one"""

    # Pattern to match strategic classification block
    strategic_pattern = r'# === STRATEGIC CLASSIFICATION \(Transcript Classifier Agent v1\.0\) ===\n(?:.*?\n){14}'

    # Find all strategic blocks
    blocks = list(re.finditer(strategic_pattern, frontmatter, re.DOTALL))

    if len(blocks) <= 1:
        return frontmatter, 0  # No duplicates

    # Remove all but the last block
    duplicates_count = len(blocks) - 1

    # Remove blocks from first to second-to-last (keep last)
    for block in blocks[:-1]:
        frontmatter = frontmatter[:block.start()] + frontmatter[block.end():]
        # Adjust for removed text
        removed_len = block.end() - block.start()
        blocks = [re.match(strategic_pattern, frontmatter[max(0, b.start() - removed_len):], re.DOTALL)
                  for b in blocks[blocks.index(block)+1:]]
        blocks = [b for b in blocks if b]

    return frontmatter, duplicates_count

def clean_file(file_path):
    """Clean a single transcript file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter, body = extract_frontmatter(content)

        if frontmatter is None:
            return {
                'status': 'error',
                'message': 'No frontmatter found',
                'duplicates': 0
            }

        # Count strategic blocks before cleanup
        strategic_pattern = r'# === STRATEGIC CLASSIFICATION \(Transcript Classifier Agent v1\.0\) ===\n'
        blocks_before = len(re.findall(strategic_pattern, frontmatter))

        # Remove duplicates by keeping only last occurrence
        lines = frontmatter.split('\n')
        strategic_blocks = []
        current_block = []
        in_block = False
        block_start_idx = None

        for i, line in enumerate(lines):
            if line.startswith('# === STRATEGIC CLASSIFICATION'):
                if in_block and current_block:
                    # Save previous block
                    strategic_blocks.append((block_start_idx, current_block))
                # Start new block
                in_block = True
                block_start_idx = i
                current_block = [line]
            elif in_block:
                current_block.append(line)
                # Strategic block is exactly 15 lines (header + 14 fields)
                if len(current_block) == 15:
                    strategic_blocks.append((block_start_idx, current_block))
                    in_block = False
                    current_block = []

        duplicates_count = len(strategic_blocks) - 1 if strategic_blocks else 0

        if duplicates_count > 0:
            # Remove all but last strategic block
            # Build new frontmatter
            new_lines = []
            skip_until = -1

            for i, line in enumerate(lines):
                if i < skip_until:
                    continue

                # Check if this is start of a strategic block we want to remove
                is_block_to_remove = False
                for idx, (start_idx, block_lines) in enumerate(strategic_blocks[:-1]):  # All but last
                    if i == start_idx:
                        skip_until = start_idx + len(block_lines)
                        is_block_to_remove = True
                        break

                if not is_block_to_remove:
                    new_lines.append(line)

            frontmatter = '\n'.join(new_lines)

        # Reconstruct file
        new_content = f"---\n{frontmatter}\n---\n{body}"

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return {
            'status': 'success',
            'duplicates': duplicates_count,
            'blocks_before': blocks_before,
            'blocks_after': 1 if blocks_before > 0 else 0
        }

    except Exception as e:
        return {
            'status': 'error',
            'message': str(e),
            'duplicates': 0
        }

def main():
    results = []

    print("Starting frontmatter cleanup - Agent 02 batch")
    print(f"Processing {len(BATCH_FILES)} files...\n")

    for filename in BATCH_FILES:
        file_path = BASE_DIR / filename
        print(f"Processing: {filename}")

        if not file_path.exists():
            results.append({
                'file': filename,
                'status': 'error',
                'message': 'File not found',
                'duplicates': 0
            })
            print(f"  [ERROR] File not found")
            continue

        result = clean_file(file_path)
        result['file'] = filename
        results.append(result)

        if result['status'] == 'success':
            if result['duplicates'] > 0:
                print(f"  [OK] Removed {result['duplicates']} duplicate blocks")
            else:
                print(f"  [OK] No duplicates found")
        else:
            print(f"  [ERROR] Error: {result.get('message', 'Unknown error')}")

    # Summary
    print("\n" + "="*60)
    print("BATCH SUMMARY")
    print("="*60)

    successful = sum(1 for r in results if r['status'] == 'success')
    errors = sum(1 for r in results if r['status'] == 'error')
    total_duplicates = sum(r['duplicates'] for r in results)
    files_with_duplicates = sum(1 for r in results if r['duplicates'] > 0)

    print(f"Files processed: {len(results)}")
    print(f"Successful: {successful}")
    print(f"Errors: {errors}")
    print(f"Files with duplicates: {files_with_duplicates}")
    print(f"Total duplicates removed: {total_duplicates}")

    return results

if __name__ == "__main__":
    results = main()
