#!/usr/bin/env python3
"""
Frontmatter Cleanup Agent 5 - Batch Processor
Removes duplicate strategic classification blocks from transcript files
"""

import re
import os
from pathlib import Path
from typing import List, Tuple, Dict

BASE_DIR = Path(r"c:\Users\dietl\VSCode Projects\taste_systems\gtm_operating_system\gtm_engagements\03_active_client\nickel_ivan\nickel_gtm_context_architecture\knowledge_base\meetings_md")

# Files assigned to Agent 5
BATCH_FILES = [
    "121_nickel-platform-demo-jared-williams_2025-10-10.md",
    "122_christian-taylor-and-jacob-greenberg_2025-08-01.md",
    "123_nickel-review_2025-08-21.md",
    "124_luke-x-jacob_2025-09-15.md",
    "125_felipe-and-jacob-greenberg_2025-08-21.md",
    "126_natalie-x-nickel_2025-08-20.md",
    "127_nickel-demo-saad-rangoonwala_2025-08-27.md",
    "128_maria-x-nickel_2025-10-03.md",
    "129_nickel-true-course-xero-integration_2025-10-07.md",
    "130_nickel-demo-darah-smith_2025-09-05.md",
    "131_dipping-dots-x-nickel_2025-09-18.md",
    "132_sierra-club-x-nickel_2025-10-07.md",
    "133_alaska-wholesale-llc-matthew-fischer_2025-09-03.md",
    "134_nickel-platform-demo-mitesh-bhagat_2025-10-08.md",
    "135_ellen-moser-and-jacob-greenberg_2025-07-30.md",
    "136_nickel-mark-hull-jacob_2025-09-23.md",
    "137_nickel-demo-didier-garcia_2025-09-02.md",
    "138_nickel-x-dual-temp-review_2025-08-26.md",
    "139_nickel-demo-request-robert-stern_2025-09-11.md",
    "140_nickel-demo-request-kayla-rakes_2025-09-09.md",
    "141_nickel-arachdeck-utah_2025-09-29.md",
    "142_laura-golnabi-and-jacob-greenberg_2025-08-25.md",
    "143_nickel-demo-request-margarita-iruela_2025-09-12.md",
    "144_nickel-demo-request-lyle-brand_2025-10-03.md",
    "145_nickel-demo-request-nathaniel-seekins_2025-09-23.md",
    "146_nickel-demo-request-tasvir-mirza_2025-09-30.md",
    "147_nickel-demo-request-andy-haines_2025-09-17.md",
    "148_nickel-demo-request-jacob-sung_2025-10-01.md",
    "149_nickel-demo-request-roby-fitzhenry_2025-10-06.md",
    "150_nickel-weaver_2025-09-18.md",
]

def extract_frontmatter(content: str) -> Tuple[str, str, str]:
    """
    Extract frontmatter and content from markdown file.
    Returns: (frontmatter_content, transcript_content, original_content)
    """
    # Match frontmatter between --- markers
    frontmatter_pattern = r'^---\n(.*?)\n---\n(.*)$'
    match = re.match(frontmatter_pattern, content, re.DOTALL)

    if not match:
        return "", content, content

    frontmatter = match.group(1)
    transcript_content = match.group(2)

    return frontmatter, transcript_content, content


def parse_strategic_blocks(frontmatter: str) -> List[Dict[str, str]]:
    """
    Parse strategic classification blocks from frontmatter.
    Returns list of blocks with their content.
    """
    blocks = []

    # Split by strategic classification header
    parts = re.split(r'# === STRATEGIC CLASSIFICATION \(Transcript Classifier Agent v1\.0\) ===', frontmatter)

    # First part is Circleback metadata
    circleback_metadata = parts[0].strip()

    # Remaining parts are strategic classification blocks
    for i, part in enumerate(parts[1:], 1):
        # Extract until next # === or end
        next_header = re.search(r'\n# ===', part)
        if next_header:
            block_content = part[:next_header.start()].strip()
        else:
            block_content = part.strip()

        if block_content:
            blocks.append({
                'index': i,
                'content': block_content
            })

    return circleback_metadata, blocks


def clean_frontmatter(frontmatter: str) -> Tuple[str, int]:
    """
    Remove duplicate strategic classification blocks, keep only the last one.
    Returns: (cleaned_frontmatter, num_duplicates_removed)
    """
    circleback_metadata, blocks = parse_strategic_blocks(frontmatter)

    if len(blocks) == 0:
        # No strategic classification found
        return frontmatter, 0

    if len(blocks) == 1:
        # Only one block, no duplicates
        return frontmatter, 0

    # Keep only the last block
    last_block = blocks[-1]
    num_removed = len(blocks) - 1

    # Reconstruct frontmatter
    cleaned = circleback_metadata + "\n"
    cleaned += "# === STRATEGIC CLASSIFICATION (Transcript Classifier Agent v1.0) ===\n"
    cleaned += last_block['content']

    return cleaned, num_removed


def validate_classification(filename: str, frontmatter: str, transcript_sample: str) -> Dict[str, any]:
    """
    Perform sanity checks on the classification.
    Returns validation results dict.
    """
    results = {
        'call_type_match': True,
        'call_type_message': '',
        'boolean_flags': True,
        'boolean_message': '',
        'priority_logic': True,
        'priority_message': '',
        'overall': 'CLEAN'
    }

    # Extract fields from frontmatter
    call_type_match = re.search(r'call_type:\s*(\w+)', frontmatter)
    call_type = call_type_match.group(1) if call_type_match else 'unknown'

    # Check 1: call_type vs filename
    filename_lower = filename.lower()
    if 'demo' in filename_lower and call_type != 'demo':
        results['call_type_match'] = False
        results['call_type_message'] = f"Filename has 'demo' but call_type={call_type}"
        results['overall'] = 'WARNINGS'
    elif 'kickoff' in filename_lower and call_type != 'kickoff':
        results['call_type_match'] = False
        results['call_type_message'] = f"Filename has 'kickoff' but call_type={call_type}"
        results['overall'] = 'WARNINGS'
    elif ('and-jacob' in filename_lower or 'and-colton' in filename_lower or 'x-jacob' in filename_lower) and call_type not in ['discovery', 'demo', 'general']:
        results['call_type_match'] = False
        results['call_type_message'] = f"Filename suggests discovery/demo but call_type={call_type}"
        results['overall'] = 'WARNINGS'
    else:
        results['call_type_message'] = f"call_type={call_type} matches filename pattern"

    # Check 2: Boolean flags sanity (light check on transcript sample)
    transcript_lower = transcript_sample.lower()

    has_competitive = 'has_competitive_intel: true' in frontmatter
    has_pricing = 'has_pricing_discussion: true' in frontmatter
    has_integration = 'has_integration_needs: true' in frontmatter

    warnings = []
    if has_competitive:
        competitors = ['melio', 'bill.com', 'relay', 'ramp', 'brex', 'divvy', 'quickbooks pay']
        if not any(comp in transcript_lower for comp in competitors):
            warnings.append("has_competitive_intel=true but no competitors found in sample")

    if has_pricing:
        pricing_terms = ['$', 'cost', 'price', 'rate', 'fee', 'pricing', 'payment']
        if not any(term in transcript_lower for term in pricing_terms):
            warnings.append("has_pricing_discussion=true but no pricing terms in sample")

    if has_integration:
        integration_terms = ['quickbooks', 'integration', 'integrate', 'sync', 'api', 'xero', 'fishbowl']
        if not any(term in transcript_lower for term in integration_terms):
            warnings.append("has_integration_needs=true but no integration terms in sample")

    if warnings:
        results['boolean_flags'] = False
        results['boolean_message'] = "; ".join(warnings)
        results['overall'] = 'WARNINGS'
    else:
        results['boolean_message'] = "Boolean flags have supporting evidence"

    # Check 3: Priority logic (basic sanity)
    priority_match = re.search(r'extraction_priority:\s*(\w+)', frontmatter)
    priority = priority_match.group(1) if priority_match else 'unknown'

    has_objections = 'has_objections: true' in frontmatter
    has_use_case = 'has_use_case: true' in frontmatter
    customer_segment = re.search(r'customer_segment:\s*(\w+)', frontmatter)
    segment = customer_segment.group(1) if customer_segment else 'unknown'

    # High priority should have competitive OR objections OR whale
    if priority == 'high':
        if not (has_competitive or has_objections or segment == 'whale'):
            results['priority_logic'] = False
            results['priority_message'] = "High priority but no competitive/objections/whale signals"
            results['overall'] = 'WARNINGS'
        else:
            results['priority_message'] = f"High priority justified (competitive={has_competitive}, objections={has_objections}, segment={segment})"
    elif priority == 'low':
        if has_competitive or has_objections or segment == 'whale':
            results['priority_logic'] = False
            results['priority_message'] = "Low priority but has high-value signals"
            results['overall'] = 'WARNINGS'
        else:
            results['priority_message'] = "Low priority seems reasonable"
    else:
        results['priority_message'] = f"Priority={priority} seems reasonable"

    return results


def process_file(filepath: Path) -> Dict[str, any]:
    """
    Process a single transcript file.
    Returns processing results.
    """
    filename = filepath.name

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            'filename': filename,
            'success': False,
            'error': str(e)
        }

    # Extract frontmatter
    frontmatter, transcript_content, original = extract_frontmatter(content)

    if not frontmatter:
        return {
            'filename': filename,
            'success': False,
            'error': 'No frontmatter found',
            'duplicates_found': 0,
            'missing_classification': True
        }

    # Clean duplicates
    cleaned_frontmatter, num_removed = clean_frontmatter(frontmatter)

    # Get transcript sample for validation (first 3000 chars)
    transcript_sample = transcript_content[:3000]

    # Validate
    validation = validate_classification(filename, cleaned_frontmatter, transcript_sample)

    # Write cleaned file if duplicates were removed
    if num_removed > 0:
        cleaned_content = f"---\n{cleaned_frontmatter}\n---\n{transcript_content}"
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
        except Exception as e:
            return {
                'filename': filename,
                'success': False,
                'error': f'Failed to write file: {str(e)}',
                'duplicates_found': num_removed + 1
            }

    return {
        'filename': filename,
        'success': True,
        'duplicates_found': num_removed + 1,
        'duplicates_removed': num_removed,
        'validation': validation
    }


def generate_report(results: List[Dict]) -> str:
    """
    Generate markdown report from processing results.
    """
    report = []
    report.append("# Frontmatter Cleanup Agent 5 - Batch Report\n")
    report.append(f"**Date:** 2025-10-30\n")
    report.append(f"**Files Assigned:** {len(BATCH_FILES)}\n\n")
    report.append("---\n\n")

    # Per-file results
    for result in results:
        report.append(f"## {result['filename']}\n\n")

        if not result['success']:
            report.append(f"**Status:** ❌ FAILED\n")
            report.append(f"**Error:** {result.get('error', 'Unknown error')}\n\n")
            if result.get('missing_classification'):
                report.append("**Issue:** Missing strategic classification block\n\n")
            report.append("---\n\n")
            continue

        # Duplicates
        dup_count = result.get('duplicates_found', 0)
        dup_removed = result.get('duplicates_removed', 0)

        if dup_count == 0:
            report.append(f"**Duplicates Found:** None (already clean)\n")
            report.append(f"**Action Taken:** No action needed\n\n")
        elif dup_count == 1:
            report.append(f"**Duplicates Found:** None (single classification block)\n")
            report.append(f"**Action Taken:** No action needed\n\n")
        else:
            report.append(f"**Duplicates Found:** {dup_count} identical blocks\n")
            report.append(f"**Action Taken:** Removed {dup_removed} duplicates, kept last block\n\n")

        # Validation
        val = result.get('validation', {})
        report.append("**Sanity Check:**\n")

        status_icon = "✅" if val.get('call_type_match') else "⚠️"
        report.append(f"- call_type vs filename: {status_icon} {val.get('call_type_message', 'N/A')}\n")

        status_icon = "✅" if val.get('boolean_flags') else "⚠️"
        report.append(f"- Boolean flags: {status_icon} {val.get('boolean_message', 'N/A')}\n")

        status_icon = "✅" if val.get('priority_logic') else "⚠️"
        report.append(f"- Priority logic: {status_icon} {val.get('priority_message', 'N/A')}\n\n")

        overall = val.get('overall', 'UNKNOWN')
        if overall == 'CLEAN':
            report.append(f"**Overall:** ✅ CLEAN\n\n")
        elif overall == 'WARNINGS':
            report.append(f"**Overall:** ⚠️ WARNINGS (not critical)\n\n")
        else:
            report.append(f"**Overall:** ❌ FAILED\n\n")

        report.append("---\n\n")

    # Summary
    report.append("# Batch Summary\n\n")

    total_files = len(results)
    successful = sum(1 for r in results if r['success'])
    failed = total_files - successful

    files_with_dups = sum(1 for r in results if r.get('success') and r.get('duplicates_removed', 0) > 0)
    missing_classification = sum(1 for r in results if r.get('missing_classification'))

    clean_files = sum(1 for r in results if r.get('success') and r.get('validation', {}).get('overall') == 'CLEAN')
    warning_files = sum(1 for r in results if r.get('success') and r.get('validation', {}).get('overall') == 'WARNINGS')
    failed_validation = sum(1 for r in results if r.get('success') and r.get('validation', {}).get('overall') == 'FAILED')

    report.append(f"**Files Processed:** {total_files}\n")
    report.append(f"**Successfully Processed:** {successful}\n")
    report.append(f"**Failed:** {failed}\n")
    report.append(f"**Duplicates Removed:** {files_with_dups} files had duplicates\n")
    report.append(f"**Missing Classification:** {missing_classification} files\n\n")

    report.append("**Validation:**\n")
    report.append(f"- ✅ Clean: {clean_files} files\n")
    report.append(f"- ⚠️ Warnings: {warning_files} files\n")
    report.append(f"- ❌ Failed: {failed_validation} files\n\n")

    if failed > 0 or missing_classification > 0:
        report.append("**Critical Issues:**\n")
        for r in results:
            if not r['success']:
                report.append(f"- {r['filename']}: {r.get('error', 'Unknown error')}\n")
            elif r.get('missing_classification'):
                report.append(f"- {r['filename']}: Missing strategic classification\n")
        report.append("\n")

    if warning_files > 0:
        report.append("**Files with Warnings (non-critical):**\n")
        for r in results:
            if r.get('success') and r.get('validation', {}).get('overall') == 'WARNINGS':
                report.append(f"- {r['filename']}\n")
        report.append("\n")

    # Ready for Phase 2?
    if failed == 0 and missing_classification == 0:
        report.append("**Ready for Phase 2:** ✅ YES\n\n")
        report.append("All files have been cleaned and validated. ")
        if warning_files > 0:
            report.append(f"{warning_files} files have minor warnings but are acceptable for Phase 2 dimensional extraction.\n")
        else:
            report.append("No warnings found.\n")
    else:
        report.append("**Ready for Phase 2:** ❌ NO\n\n")
        report.append(f"Issues found: {failed} failed files, {missing_classification} missing classifications. ")
        report.append("These files need re-classification before Phase 2.\n")

    return "".join(report)


def main():
    """Main processing function."""
    print("Starting Frontmatter Cleanup Agent 5...")
    print(f"Processing {len(BATCH_FILES)} files...")

    results = []

    for filename in BATCH_FILES:
        filepath = BASE_DIR / filename
        print(f"  Processing: {filename}...")
        result = process_file(filepath)
        results.append(result)

        if result['success']:
            dup_removed = result.get('duplicates_removed', 0)
            if dup_removed > 0:
                print(f"    [OK] Removed {dup_removed} duplicates")
            else:
                print(f"    [OK] Already clean")
        else:
            print(f"    [FAIL] Failed: {result.get('error', 'Unknown')}")

    print("\nGenerating report...")
    report = generate_report(results)

    # Write report
    report_path = Path(r"c:\Users\dietl\VSCode Projects\taste_systems\gtm_operating_system\gtm_engagements\03_active_client\nickel_ivan\nickel_gtm_context_architecture\_AGENT_WORKSPACE\cleanup_reports")
    report_path.mkdir(exist_ok=True)
    report_file = report_path / "agent_05_report.md"

    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\n[OK] Report written to: {report_file}")
    print("\nAgent 5 batch processing complete!")

    return results


if __name__ == "__main__":
    main()
