#!/usr/bin/env python3
"""
Frontmatter Cleanup Agent 01
Processes batch of 30 transcripts to remove duplicate strategic classification blocks
"""

import re
import os
from pathlib import Path
from typing import List, Dict, Tuple

# Base directory
BASE_DIR = Path(r"c:\Users\dietl\VSCode Projects\taste_systems\gtm_operating_system\gtm_engagements\03_active_client\nickel_ivan\nickel_gtm_context_architecture")
MEETINGS_DIR = BASE_DIR / "knowledge_base" / "meetings_md"
REPORT_DIR = BASE_DIR / "_AGENT_WORKSPACE" / "cleanup_reports"

# Batch assignment
BATCH_FILES = [
    "001_abbas-rezaei-and-colton-ofarrell_2025-07-15.md",
    "002_erik-meza-and-colton-ofarrell_2025-07-15.md",
    "003_prime-renovations-ny-nickel_2025-07-23.md",
    "004_carson-crawford-and-colton-ofarrell_2025-08-14.md",
    "005_prime-renovations-ny-nickel_2025-07-23.md",
    "006_erik-meza-and-colton-ofarrell_2025-07-15.md",
    "007_frank-delbrouck-and-colton-ofarrell_2025-08-19.md",
    "008_hardy-butler-and-colton-ofarrell_2025-07-23.md",
    "009_ashland-roofing-nickel-2nd-review-call_2025-09-25.md",
    "010_amps-facility-solutions-nickel-kickoff-call_2025-09-29.md",
    "011_american-home-renewal-inc-nickel_2025-07-18.md",
    "012_matthew-and-colton-ofarrell_2025-08-20.md",
    "013_jay-omanson-and-colton-ofarrell_2025-08-12.md",
    "014_brandon-rogers-and-colton-ofarrell_2025-07-14.md",
    "015_hassan-colton-nickel_2025-07-31.md",
    "016_conner-rusch-and-colton-ofarrell_2025-07-18.md",
    "017_sharika-and-colton-ofarrell_2025-08-13.md",
    "018_ramon-j-otero-and-colton-ofarrell_2025-07-31.md",
    "019_peter-trang-and-colton-ofarrell_2025-08-01.md",
    "020_david-berry-and-colton-ofarrell_2025-07-22.md",
    "021_ashland-roofing-nickel-kickoff-call_2025-09-18.md",
    "022_steve-goldstein-and-colton-ofarrell_2025-07-30.md",
    "023_joan-schafer-and-colton-ofarrell_2025-08-25.md",
    "024_emma-benson-and-colton-ofarrell_2025-07-23.md",
    "025_david-kruyswijk-and-colton-ofarrell_2025-07-15.md",
    "026_kab-consulting-inc-nickel-kick-off-call_2025-09-10.md",
    "027_brent-rose-and-colton-ofarrell_2025-07-21.md",
    "028_abbas-rezaei-and-colton-ofarrell_2025-07-15.md",
    "029_deshyra-hubbard-and-colton-ofarrell_2025-07-24.md",
    "030_brandon-kopp-and-colton-ofarrell_2025-08-05.md",
]

class TranscriptCleaner:
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.filename = filepath.name
        self.content = ""
        self.clean_content = ""
        self.duplicates_found = 0
        self.strategic_blocks = []
        self.validation_results = {}

    def read_file(self):
        """Read the transcript file"""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            self.content = f.read()

    def extract_strategic_blocks(self):
        """Extract all strategic classification blocks"""
        # Pattern to match strategic classification blocks
        pattern = r'# === STRATEGIC CLASSIFICATION \(Transcript Classifier Agent v1\.0\) ===\n(?:[\w_]+:.*\n)+'

        matches = list(re.finditer(pattern, self.content))
        self.strategic_blocks = [m.group(0) for m in matches]
        self.duplicates_found = len(self.strategic_blocks)

        return self.duplicates_found

    def remove_duplicates(self):
        """Remove duplicate blocks, keep only the last one"""
        if self.duplicates_found == 0:
            self.clean_content = self.content
            return

        if self.duplicates_found == 1:
            # No duplicates, just keep as is
            self.clean_content = self.content
            return

        # Find the frontmatter section
        parts = self.content.split('---')

        if len(parts) < 3:
            # Malformed frontmatter
            self.clean_content = self.content
            return

        # parts[0] is empty, parts[1] is frontmatter, parts[2:] is content
        frontmatter = parts[1]
        remaining_content = '---'.join(parts[2:])

        # Remove ALL strategic classification blocks from frontmatter
        pattern = r'# === STRATEGIC CLASSIFICATION \(Transcript Classifier Agent v1\.0\) ===\n(?:[\w_]+:.*\n)+'
        frontmatter_clean = re.sub(pattern, '', frontmatter)

        # Add back the LAST strategic block (keep only one)
        if self.strategic_blocks:
            last_block = self.strategic_blocks[-1]
            # Add it at the end of frontmatter
            frontmatter_clean = frontmatter_clean.rstrip() + '\n' + last_block

        # Reconstruct the file
        self.clean_content = '---' + frontmatter_clean + '---' + remaining_content

    def write_clean_file(self):
        """Write the cleaned content back to file"""
        with open(self.filepath, 'w', encoding='utf-8') as f:
            f.write(self.clean_content)

    def validate_classification(self):
        """Perform sanity checks on the classification"""
        if not self.strategic_blocks:
            self.validation_results = {
                'call_type_match': '❌ FAIL - No classification found',
                'boolean_flags': '❌ FAIL - No classification found',
                'priority_logic': '❌ FAIL - No classification found',
                'overall': '❌ FAILED'
            }
            return

        # Parse the last (kept) strategic block
        last_block = self.strategic_blocks[-1]
        classification = {}
        for line in last_block.split('\n'):
            if ':' in line and not line.startswith('#'):
                key, value = line.split(':', 1)
                classification[key.strip()] = value.strip()

        # Validation 1: call_type vs filename
        call_type = classification.get('call_type', 'unknown')
        filename_lower = self.filename.lower()

        call_type_match = '✅ PASS'
        if 'kickoff' in filename_lower or 'kick-off' in filename_lower:
            if call_type != 'kickoff':
                call_type_match = f'⚠️ WARN - Filename has "kickoff" but call_type is "{call_type}"'
        elif 'demo' in filename_lower:
            if call_type != 'demo':
                call_type_match = f'⚠️ WARN - Filename has "demo" but call_type is "{call_type}"'
        elif 'and-colton' in filename_lower or 'and-jacob' in filename_lower:
            if call_type not in ['discovery', 'general']:
                call_type_match = f'⚠️ WARN - Filename pattern suggests discovery but call_type is "{call_type}"'

        # Validation 2: Boolean flags (light check)
        # Read first 100 lines of transcript for quick validation
        content_lines = self.content.split('\n')
        transcript_start = 0
        for i, line in enumerate(content_lines):
            if line.strip() == '---' and i > 5:
                transcript_start = i + 1
                break

        transcript_sample = '\n'.join(content_lines[transcript_start:transcript_start+100]).lower()

        boolean_flags = '✅ PASS'
        warnings = []

        if classification.get('has_competitive_intel') == 'true':
            competitors = ['melio', 'bill.com', 'relay', 'brex', 'ramp', 'stripe', 'square']
            if not any(comp in transcript_sample for comp in competitors):
                warnings.append('has_competitive_intel=true but no competitors found in sample')

        if classification.get('has_pricing_discussion') == 'true':
            pricing_terms = ['$', 'price', 'cost', 'rate', 'fee', 'discount', 'percent']
            if not any(term in transcript_sample for term in pricing_terms):
                warnings.append('has_pricing_discussion=true but no pricing terms found')

        if classification.get('has_integration_needs') == 'true':
            integration_terms = ['quickbooks', 'integration', 'sync', 'connect', 'api']
            if not any(term in transcript_sample for term in integration_terms):
                warnings.append('has_integration_needs=true but no integration terms found')

        if warnings:
            boolean_flags = f'⚠️ WARN - {"; ".join(warnings)}'

        # Validation 3: Priority logic
        priority = classification.get('extraction_priority', 'unknown')
        has_competitive = classification.get('has_competitive_intel') == 'true'
        has_objections = classification.get('has_objections') == 'true'
        is_whale = classification.get('customer_segment') == 'whale'
        above_threshold = classification.get('transaction_volume') == 'above_threshold'

        priority_logic = '✅ PASS'
        if priority == 'high':
            if not (has_competitive or has_objections or is_whale or above_threshold):
                priority_logic = '⚠️ WARN - High priority but no obvious high-value signals'
        elif priority == 'low':
            if has_competitive or is_whale or above_threshold:
                priority_logic = '⚠️ WARN - Low priority but has high-value signals'

        # Overall status
        overall = '✅ CLEAN'
        if '❌' in call_type_match or '❌' in boolean_flags or '❌' in priority_logic:
            overall = '❌ FAILED'
        elif '⚠️' in call_type_match or '⚠️' in boolean_flags or '⚠️' in priority_logic:
            overall = '⚠️ WARNINGS'

        self.validation_results = {
            'call_type_match': call_type_match,
            'boolean_flags': boolean_flags,
            'priority_logic': priority_logic,
            'overall': overall
        }

    def process(self):
        """Complete processing workflow"""
        self.read_file()
        self.extract_strategic_blocks()
        self.remove_duplicates()
        self.validate_classification()
        if self.duplicates_found > 1:
            self.write_clean_file()

        return self.get_report()

    def get_report(self):
        """Generate report for this transcript"""
        action = "No action needed"
        if self.duplicates_found == 0:
            action = "❌ MISSING CLASSIFICATION - Needs re-processing"
        elif self.duplicates_found == 1:
            action = "No duplicates found"
        elif self.duplicates_found > 1:
            action = f"Removed {self.duplicates_found - 1} duplicates, kept last block"

        report = f"""=== TRANSCRIPT: {self.filename} ===

**Duplicates Found:** {self.duplicates_found} blocks
**Action Taken:** {action}

**Sanity Check:**
- call_type vs filename: {self.validation_results.get('call_type_match', 'N/A')}
- Boolean flags: {self.validation_results.get('boolean_flags', 'N/A')}
- Priority logic: {self.validation_results.get('priority_logic', 'N/A')}

**Overall:** {self.validation_results.get('overall', 'N/A')}

---
"""
        return report


def main():
    """Main processing function"""
    print("Starting Frontmatter Cleanup Agent 01...")
    print(f"Processing {len(BATCH_FILES)} files...\n")

    reports = []
    stats = {
        'total': 0,
        'duplicates_removed': 0,
        'missing_classification': 0,
        'clean': 0,
        'warnings': 0,
        'failed': 0
    }

    for filename in BATCH_FILES:
        filepath = MEETINGS_DIR / filename

        if not filepath.exists():
            print(f"⚠️ File not found: {filename}")
            continue

        print(f"Processing: {filename}")
        cleaner = TranscriptCleaner(filepath)
        report = cleaner.process()
        reports.append(report)

        stats['total'] += 1
        if cleaner.duplicates_found == 0:
            stats['missing_classification'] += 1
        elif cleaner.duplicates_found > 1:
            stats['duplicates_removed'] += 1

        overall = cleaner.validation_results.get('overall', '')
        if '✅' in overall:
            stats['clean'] += 1
        elif '⚠️' in overall:
            stats['warnings'] += 1
        elif '❌' in overall:
            stats['failed'] += 1

    # Generate summary
    summary = f"""
=== BATCH SUMMARY ===

**Files Processed:** {stats['total']}
**Duplicates Removed:** {stats['duplicates_removed']} files had duplicates
**Missing Classification:** {stats['missing_classification']} files had no strategic classification

**Validation:**
- ✅ Clean: {stats['clean']} files
- ⚠️ Warnings: {stats['warnings']} files
- ❌ Failed: {stats['failed']} files

**Ready for Phase 2:** {'YES - All files processed successfully' if stats['failed'] == 0 else f'NO - {stats["failed"]} files need attention'}
"""

    # Write report
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_file = REPORT_DIR / "agent_01_report.md"

    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# Frontmatter Cleanup Report - Agent 01\n\n")
        f.write(f"**Generated:** 2025-10-30\n")
        f.write(f"**Batch Size:** {len(BATCH_FILES)} transcripts\n\n")
        f.write("---\n\n")

        for report in reports:
            f.write(report)
            f.write("\n")

        f.write(summary)

    print("\n" + "="*60)
    print(summary)
    print(f"\nReport written to: {report_file}")
    print("="*60)


if __name__ == "__main__":
    main()
