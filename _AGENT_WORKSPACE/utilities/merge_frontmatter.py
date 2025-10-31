#!/usr/bin/env python3
"""
Merge strategic classification frontmatter into transcript files.

Reads batch result files, parses classifications, and appends new fields
to existing Circleback frontmatter in transcript files.
"""

import re
import yaml
from pathlib import Path
from typing import Dict, Optional

BATCHES_DIR = Path("_AGENT_WORKSPACE/transcript_batches")
TRANSCRIPTS_DIR = Path("knowledge_base/meetings_md")

def parse_classifications_from_batch(result_file: Path) -> Dict[str, Dict]:
    """Parse all classifications from a batch result file."""
    classifications = {}

    with result_file.open('r', encoding='utf-8') as f:
        content = f.read()

    # Try two parsing strategies

    # Strategy 1: === TRANSCRIPT: format
    blocks = re.split(r'===\s*TRANSCRIPT:\s*([^\n]+)', content)
    if len(blocks) > 1:
        for i in range(1, len(blocks), 2):
            if i+1 >= len(blocks):
                break
            filename = blocks[i].strip()
            fields_text = blocks[i+1]
            classification = extract_fields(fields_text)
            if classification:
                classifications[filename] = classification

    # Strategy 2: TRANSCRIPT NNN: format (alternative format)
    if not classifications:
        # Match patterns like "### TRANSCRIPT 002:" or "### TRANSCRIPT 002: Erik Meza"
        pattern = r'###\s*TRANSCRIPT\s+(\d{3}):[^\n]*?\n.*?```\s*\n(.*?)\n```'
        matches = re.finditer(pattern, content, re.DOTALL)

        # Get transcript filenames from manifest
        batch_num = int(re.search(r'batch_(\d+)_results', result_file.name).group(1))
        manifest_file = BATCHES_DIR / f"batch_{batch_num:02d}.txt"

        transcript_files = []
        if manifest_file.exists():
            with manifest_file.open('r') as f:
                for line in f:
                    path = Path(line.strip())
                    transcript_files.append(path.name)

        # Map transcript numbers to filenames
        for match in matches:
            transcript_num = int(match.group(1))
            fields_text = match.group(2)

            # Get filename from manifest (transcript numbers are 1-indexed)
            if 0 < transcript_num <= len(transcript_files):
                filename = transcript_files[transcript_num - 1]
                classification = extract_fields(fields_text)
                if classification:
                    classifications[filename] = classification

    # Strategy 3: Numbered TRANSCRIPT: format (### N. TRANSCRIPT:)
    if not classifications:
        # Match patterns like "### 2. TRANSCRIPT: filename.md"
        pattern = r'###\s*\d+\.\s*TRANSCRIPT:\s*([^\n]+\.md)\n.*?```yaml\s*\n(.*?)\n```'
        matches = re.finditer(pattern, content, re.DOTALL)

        for match in matches:
            filename = match.group(1).strip()
            fields_text = match.group(2)
            classification = extract_fields(fields_text)
            if classification:
                classifications[filename] = classification

    # Strategy 4: ## TRANSCRIPT: format with bold fields
    if not classifications:
        # Match patterns like "## TRANSCRIPT: filename.md" followed by bold fields
        pattern = r'##\s*TRANSCRIPT:\s*([^\n]+\.md)\n(.*?)(?=##\s*TRANSCRIPT:|$)'
        matches = re.finditer(pattern, content, re.DOTALL)

        for match in matches:
            filename = match.group(1).strip()
            fields_text = match.group(2)
            classification = extract_fields(fields_text)
            if classification:
                classifications[filename] = classification

    # Strategy 5: ## TRANSCRIPT NNN: Name format with Filename: field
    if not classifications:
        # Match patterns like "## TRANSCRIPT 051: Name" with **Filename:** field
        pattern = r'##\s*TRANSCRIPT\s+\d+:.*?\n.*?\*\*Filename:\*\*\s*([^\n]+\.md).*?```\s*\n(.*?)\n```'
        matches = re.finditer(pattern, content, re.DOTALL)

        for match in matches:
            filename = match.group(1).strip()
            fields_text = match.group(2)
            classification = extract_fields(fields_text)
            if classification:
                classifications[filename] = classification

    # Strategy 6: ### Transcript N: filename.md format
    if not classifications:
        # Match patterns like "### Transcript 1: filename.md"
        pattern = r'###\s*Transcript\s+\d+:\s*([^\n]+\.md)\n.*?```\s*\n(.*?)\n```'
        matches = re.finditer(pattern, content, re.DOTALL)

        for match in matches:
            filename = match.group(1).strip()
            fields_text = match.group(2)
            classification = extract_fields(fields_text)
            if classification:
                classifications[filename] = classification

    return classifications

def extract_fields(fields_text: str) -> Dict:
    """Extract classification fields from text using regex."""
    classification = {}

    field_patterns = {
        'call_type': [r'\*\*call_type:\*\*\s*(\w+)', r'call_type:\s*(\w+)'],
        'deal_stage': [r'\*\*deal_stage:\*\*\s*(\w+)', r'deal_stage:\s*(\w+)'],
        'customer_segment': [r'\*\*customer_segment:\*\*\s*(\w+)', r'customer_segment:\s*(\w+)'],
        'has_pain_points': [r'\*\*has_pain_points:\*\*\s*(true|false)', r'has_pain_points:\s*(true|false)'],
        'has_objections': [r'\*\*has_objections:\*\*\s*(true|false)', r'has_objections:\s*(true|false)'],
        'has_competitive_intel': [r'\*\*has_competitive_intel:\*\*\s*(true|false)', r'has_competitive_intel:\s*(true|false)'],
        'has_use_case': [r'\*\*has_use_case:\*\*\s*(true|false)', r'has_use_case:\s*(true|false)'],
        'has_pricing_discussion': [r'\*\*has_pricing_discussion:\*\*\s*(true|false)', r'has_pricing_discussion:\s*(true|false)'],
        'has_integration_needs': [r'\*\*has_integration_needs:\*\*\s*(true|false)', r'has_integration_needs:\s*(true|false)'],
        'primary_industry': [r'\*\*primary_industry:\*\*\s*(\w+)', r'primary_industry:\s*(\w+)'],
        'transaction_volume': [r'\*\*transaction_volume:\*\*\s*(\w+)', r'transaction_volume:\s*(\w+)'],
        'ar_vs_ap': [r'\*\*ar_vs_ap:\*\*\s*(\w+)', r'ar_vs_ap:\s*(\w+)'],
        'processed': [r'\*\*processed:\*\*\s*(true|false)', r'processed:\s*(true|false)'],
        'dimensional_extracted': [r'\*\*dimensional_extracted:\*\*\s*(true|false)', r'dimensional_extracted:\s*(true|false)'],
        'extraction_priority': [r'\*\*extraction_priority:\*\*\s*(\w+)', r'extraction_priority:\s*(\w+)'],
    }

    for field, patterns in field_patterns.items():
        # Try each pattern variant for this field
        for pattern in patterns:
            match = re.search(pattern, fields_text, re.IGNORECASE)
            if match:
                value = match.group(1).lower()
                if value in ('true', 'false'):
                    classification[field] = value == 'true'
                else:
                    classification[field] = value
                break  # Found a match, move to next field

    return classification

def extract_frontmatter(content: str) -> tuple[Optional[Dict], str, str]:
    """
    Extract existing frontmatter from file content.

    Returns: (frontmatter_dict, frontmatter_text, body_content)
    """
    # Check if file starts with ---
    if not content.startswith('---'):
        return None, '', content

    # Find the closing ---
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not match:
        return None, '', content

    frontmatter_text = match.group(1)
    body = match.group(2)

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        return frontmatter, frontmatter_text, body
    except yaml.YAMLError:
        return None, frontmatter_text, body

def merge_frontmatter(existing_fm: str, new_fields: Dict) -> str:
    """
    Merge new classification fields into existing frontmatter text.

    Returns complete frontmatter YAML string.
    """
    # Add strategic classification section
    strategic_section = "\n# === STRATEGIC CLASSIFICATION (Transcript Classifier Agent v1.0) ===\n"

    # Format fields
    for key, value in new_fields.items():
        if isinstance(value, bool):
            strategic_section += f"{key}: {str(value).lower()}\n"
        else:
            strategic_section += f"{key}: {value}\n"

    # Combine existing + new
    merged = existing_fm + strategic_section

    return merged

def merge_transcript(transcript_path: Path, classification: Dict) -> bool:
    """
    Merge classification into a single transcript file.

    Returns True if successful, False otherwise.
    """
    try:
        # Read original file
        with transcript_path.open('r', encoding='utf-8') as f:
            content = f.read()

        # Extract existing frontmatter
        fm_dict, fm_text, body = extract_frontmatter(content)

        if not fm_text:
            print(f"  [WARN] {transcript_path.name}: No frontmatter found")
            return False

        # Merge frontmatter
        merged_fm = merge_frontmatter(fm_text, classification)

        # Reconstruct file
        new_content = f"---\n{merged_fm}---\n{body}"

        # Write back
        with transcript_path.open('w', encoding='utf-8') as f:
            f.write(new_content)

        return True

    except Exception as e:
        print(f"  [ERROR] {transcript_path.name}: {e}")
        return False

def main():
    print("\n=== FRONTMATTER MERGE UTILITY ===\n")

    # Load all batch results
    result_files = sorted(BATCHES_DIR.glob("batch_*_results.md"))
    print(f"Found {len(result_files)} batch result files")

    all_classifications = {}
    for result_file in result_files:
        classifications = parse_classifications_from_batch(result_file)
        all_classifications.update(classifications)
        print(f"[OK] {result_file.name}: {len(classifications)} classifications")

    print(f"\n[OK] Total classifications loaded: {len(all_classifications)}")

    # Merge into transcript files
    print(f"\n=== MERGING FRONTMATTER ===\n")

    success_count = 0
    error_count = 0

    for filename, classification in sorted(all_classifications.items()):
        # Clean filename (remove extra characters)
        clean_filename = filename.strip().rstrip('=').strip()
        transcript_path = TRANSCRIPTS_DIR / clean_filename

        if not transcript_path.exists():
            print(f"  [SKIP] {clean_filename}: File not found")
            error_count += 1
            continue

        if merge_transcript(transcript_path, classification):
            success_count += 1
            if success_count % 10 == 0:
                print(f"[OK] Progress: {success_count} transcripts merged...")
        else:
            error_count += 1

    # Summary
    print(f"\n=== MERGE COMPLETE ===")
    print(f"Success: {success_count}/{len(all_classifications)}")
    print(f"Errors:  {error_count}/{len(all_classifications)}")

    if success_count == len(all_classifications):
        print("\n[OK] All transcripts successfully merged!")
    else:
        print(f"\n[WARN] {error_count} transcripts had issues")

    print()

if __name__ == "__main__":
    main()
