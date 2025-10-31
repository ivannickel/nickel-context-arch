#!/usr/bin/env python3
"""
Merge Transcript Classifications into Original Transcript Files

This script reads batch classification results and merges the classifications
into the corresponding transcript files in knowledge_base/meetings_md/
"""

import os
import re
from pathlib import Path
from typing import Dict, List

class ClassificationMerger:
    def __init__(self, workspace_dir: str, kb_dir: str):
        self.workspace_dir = Path(workspace_dir)
        self.kb_dir = Path(kb_dir)
        self.results_dir = self.workspace_dir / "transcript_batches"
        self.transcript_dir = self.kb_dir / "meetings_md"
        self.merged_count = 0
        self.skip_count = 0
        self.error_count = 0

    def parse_classification_results(self, results_file: str) -> Dict[str, Dict]:
        """Parse markdown results file and extract classifications by filename"""
        classifications = {}

        with open(results_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find each transcript section (delimited by === TRANSCRIPT: or === TRANSCRIPT)
        pattern = r'=== TRANSCRIPT:?\s*\(?(\d+_[\w\-]+)\.md\)?.*?\n\n(.*?)(?===|$)'

        sections = re.finditer(pattern, content, re.DOTALL)

        for match in sections:
            filename_part = match.group(1).strip()
            section_text = match.group(2)

            # Extract classification fields
            classification = {}
            fields = [
                'call_type', 'deal_stage', 'customer_segment',
                'has_pain_points', 'has_objections', 'has_competitive_intel',
                'has_use_case', 'has_pricing_discussion', 'has_integration_needs',
                'primary_industry', 'transaction_volume', 'ar_vs_ap',
                'processed', 'dimensional_extracted', 'extraction_priority'
            ]

            for field in fields:
                # Match field: value pattern (handling boolean and string values)
                field_pattern = f"\\*\\*{field}:\\*\\*\\s*([^\\n]+)"
                field_match = re.search(field_pattern, section_text, re.IGNORECASE)
                if field_match:
                    value = field_match.group(1).strip()
                    # Convert string booleans to lowercase
                    if value.lower() in ('true', 'false'):
                        value = value.lower()
                    classification[field] = value

            # Find full filename - look for any matching file
            # Use simple suffix match instead of glob
            filename_found = False
            for transcript_file in self.transcript_dir.iterdir():
                if transcript_file.is_file() and transcript_file.name.startswith(filename_part):
                    classifications[transcript_file.name] = classification
                    filename_found = True
                    break

            if not filename_found and classification:
                print(f"    WARNING: Could not match file for {filename_part}")

        return classifications

    def build_classification_block(self, classification: Dict) -> str:
        """Build YAML frontmatter classification block"""
        lines = ["# === STRATEGIC CLASSIFICATION ===\n"]

        # Order fields logically
        field_order = [
            'call_type', 'deal_stage', 'customer_segment',
            'has_pain_points', 'has_objections', 'has_competitive_intel',
            'has_use_case', 'has_pricing_discussion', 'has_integration_needs',
            'primary_industry', 'transaction_volume', 'ar_vs_ap',
            'processed', 'dimensional_extracted', 'extraction_priority'
        ]

        for field in field_order:
            if field in classification:
                value = classification[field]
                lines.append(f"{field}: {value}\n")

        return "".join(lines)

    def merge_classification_into_transcript(self, transcript_path: Path, classification: Dict) -> bool:
        """Merge classification into a single transcript file"""
        try:
            with open(transcript_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if classification already exists (to avoid duplicates)
            if '# === STRATEGIC CLASSIFICATION ===' in content:
                # Remove old classification block
                pattern = r'\n# === STRATEGIC CLASSIFICATION ===\n.*?(?=\n\n|\n[a-zA-Z]|\Z)'
                content = re.sub(pattern, '', content, flags=re.DOTALL)

            # Find the end of the initial YAML frontmatter
            # Pattern: first '---' marks start, second '---' marks end
            lines = content.split('\n')
            frontmatter_end = None
            found_first = False

            for i, line in enumerate(lines):
                if line.strip() == '---':
                    if not found_first:
                        found_first = True
                    else:
                        frontmatter_end = i
                        break

            if frontmatter_end is None:
                print(f"  ERROR: Could not find frontmatter end in {transcript_path.name}")
                return False

            # Build new content with classification inserted after frontmatter
            classification_block = self.build_classification_block(classification)
            new_lines = lines[:frontmatter_end+1] + ["\n" + classification_block] + lines[frontmatter_end+1:]
            new_content = '\n'.join(new_lines)

            # Write back to file
            with open(transcript_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            return True

        except Exception as e:
            print(f"  ERROR merging {transcript_path.name}: {e}")
            return False

    def merge_batch(self, batch_name: str) -> tuple[int, int, int]:
        """Merge a single batch results file"""
        results_file = self.results_dir / f"{batch_name}_results.md"

        if not results_file.exists():
            print(f"Results file not found: {results_file}")
            return 0, 0, 1

        print(f"\nProcessing {batch_name}...")
        classifications = self.parse_classification_results(str(results_file))

        merged = 0
        skipped = 0
        errors = 0

        for filename, classification in classifications.items():
            transcript_path = self.transcript_dir / filename

            if not transcript_path.exists():
                print(f"  SKIP: Transcript not found: {filename}")
                skipped += 1
                continue

            # Check if already has current classification
            with open(transcript_path, 'r', encoding='utf-8') as f:
                existing = f.read()

            if 'call_type:' in existing and '# === STRATEGIC CLASSIFICATION ===' in existing:
                print(f"  SKIP: {filename} already classified")
                skipped += 1
                continue

            if self.merge_classification_into_transcript(transcript_path, classification):
                print(f"  OK: {filename}")
                merged += 1
            else:
                errors += 1

        return merged, skipped, errors

    def merge_all_batches(self) -> None:
        """Merge all batch result files"""
        batches = ['batch_missing_A', 'batch_missing_B', 'batch_missing_C', 'batch_missing_D']

        total_merged = 0
        total_skipped = 0
        total_errors = 0

        for batch_name in batches:
            merged, skipped, errors = self.merge_batch(batch_name)
            total_merged += merged
            total_skipped += skipped
            total_errors += errors

        print(f"\n{'='*60}")
        print(f"MERGE SUMMARY")
        print(f"{'='*60}")
        print(f"Total Merged:  {total_merged}")
        print(f"Total Skipped: {total_skipped}")
        print(f"Total Errors:  {total_errors}")
        print(f"{'='*60}\n")


def main():
    workspace_dir = r"C:\Users\dietl\VSCode Projects\taste_systems\gtm_operating_system\gtm_engagements\03_active_client\nickel_ivan\nickel_gtm_context_architecture\_AGENT_WORKSPACE"
    kb_dir = r"C:\Users\dietl\VSCode Projects\taste_systems\gtm_operating_system\gtm_engagements\03_active_client\nickel_ivan\nickel_gtm_context_architecture\knowledge_base"

    merger = ClassificationMerger(workspace_dir, kb_dir)
    merger.merge_all_batches()


if __name__ == "__main__":
    main()
