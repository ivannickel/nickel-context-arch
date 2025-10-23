#!/usr/bin/env python3
"""
Quick script to check domain tag presence in files
Part of knowledge-graph-plugin validation
"""

import os
import re
from pathlib import Path

def check_domain_tag(file_path):
    """Check if domain field matches a tag in tags array"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if file has frontmatter
        if not content.startswith('---'):
            return {'has_frontmatter': False}

        # Extract frontmatter
        frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not frontmatter_match:
            return {'has_frontmatter': False}

        frontmatter = frontmatter_match.group(1)

        # Extract domain field
        domain_match = re.search(r'^domain:\s*(\w+)', frontmatter, re.MULTILINE)
        domain = domain_match.group(1) if domain_match else None

        # Extract tags array
        tags_match = re.search(r'^tags:\s*\n((?:  - .+\n)+)', frontmatter, re.MULTILINE)
        if tags_match:
            tags_text = tags_match.group(1)
            tags = [line.strip('- ').strip() for line in tags_text.split('\n') if line.strip()]
        else:
            tags = []

        # Check if domain tag is present
        has_domain_tag = domain in tags if domain else False

        return {
            'has_frontmatter': True,
            'domain': domain,
            'tags': tags,
            'has_domain_tag': has_domain_tag,
            'compliant': has_domain_tag
        }

    except Exception as e:
        return {'error': str(e)}

def main():
    """Scan all markdown files in active domains"""

    base_path = Path(__file__).parent.parent.parent.parent
    domains = ['00_foundation', '01_customer', '02_content', '03_execute']

    results = {
        'total': 0,
        'compliant': 0,
        'non_compliant': [],
        'no_frontmatter': [],
        'no_tags': [],
        'errors': []
    }

    for domain_dir in domains:
        domain_path = base_path / domain_dir
        if not domain_path.exists():
            continue

        for md_file in domain_path.rglob('*.md'):
            results['total'] += 1
            check_result = check_domain_tag(md_file)

            if 'error' in check_result:
                results['errors'].append((str(md_file), check_result['error']))
            elif not check_result.get('has_frontmatter'):
                results['no_frontmatter'].append(str(md_file))
            elif check_result.get('compliant'):
                results['compliant'] += 1
            else:
                # Non-compliant
                relative_path = str(md_file.relative_to(base_path))
                results['non_compliant'].append({
                    'file': relative_path,
                    'domain': check_result.get('domain'),
                    'tags': check_result.get('tags', []),
                    'issue': 'Domain tag missing from tags array' if check_result.get('domain') else 'No domain field'
                })

    # Print report
    print("=" * 60)
    print("DOMAIN TAG COMPLIANCE REPORT")
    print("=" * 60)
    print(f"\nTotal files scanned: {results['total']}")
    print(f"Compliant files: {results['compliant']} ({results['compliant']/results['total']*100:.1f}%)")
    print(f"Non-compliant files: {len(results['non_compliant'])} ({len(results['non_compliant'])/results['total']*100:.1f}%)")

    if results['non_compliant']:
        print("\n" + "=" * 60)
        print("NON-COMPLIANT FILES (CRITICAL - Breaks Foam color-coding):")
        print("=" * 60)
        for item in results['non_compliant']:
            print(f"\n[X] {item['file']}")
            print(f"   Domain: {item['domain']}")
            print(f"   Tags: {item['tags']}")
            print(f"   Issue: {item['issue']}")
            print(f"   Fix: Add '{item['domain']}' to tags array")

    if results['no_frontmatter']:
        print("\n" + "=" * 60)
        print("NO FRONTMATTER:")
        print("=" * 60)
        for f in results['no_frontmatter']:
            print(f"[X] {f}")

    if results['errors']:
        print("\n" + "=" * 60)
        print("ERRORS:")
        print("=" * 60)
        for f, err in results['errors']:
            print(f"[!] {f}: {err}")

    print("\n" + "=" * 60)
    print(f"OVERALL COMPLIANCE: {results['compliant']}/{results['total']} ({results['compliant']/results['total']*100:.1f}%)")
    print("=" * 60)

    return 0 if not results['non_compliant'] else 1

if __name__ == '__main__':
    exit(main())
