#!/usr/bin/env python3
"""
Taxonomy Scanner for FOAM Knowledge Graphs
Generates comprehensive analysis of tag usage, patterns, and health.

Part of Knowledge Graph Plugin v0.1 (Observation Phase)
Philosophy: Garden, Don't Architect
"""

import os
import re
import yaml
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from typing import Dict, List, Set, Tuple


class TaxonomyScanner:
    """Analyzes taxonomy patterns across FOAM knowledge graph."""

    def __init__(self, repo_root: Path, domains: List[str] = None):
        self.repo_root = repo_root
        self.domains = domains or ['00_foundation', '01_customer', '02_content', '03_execute']

        # Data structures
        self.tag_frequency = Counter()
        self.tag_cooccurrence = defaultdict(Counter)
        self.file_tags = {}
        self.file_metadata = {}
        self.vestigial_candidates = []

    def scan_files(self):
        """Scan all markdown files in specified domains."""
        print(f"Scanning domains: {', '.join(self.domains)}")

        for domain in self.domains:
            domain_path = self.repo_root / domain
            if not domain_path.exists():
                print(f"Warning: Domain path not found: {domain_path}")
                continue

            md_files = list(domain_path.rglob("*.md"))
            print(f"  {domain}: {len(md_files)} files")

            for md_file in md_files:
                self._process_file(md_file)

    def _process_file(self, file_path: Path):
        """Extract and process frontmatter from a markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract YAML frontmatter
            match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            if not match:
                return

            frontmatter = yaml.safe_load(match.group(1))
            if not frontmatter:
                return

            # Extract tags
            tags = frontmatter.get('tags', [])
            if not isinstance(tags, list):
                return

            # Store file metadata
            rel_path = file_path.relative_to(self.repo_root)
            self.file_tags[str(rel_path)] = tags
            self.file_metadata[str(rel_path)] = {
                'name': frontmatter.get('name', file_path.stem),
                'domain': frontmatter.get('domain', 'unknown'),
                'file_type': frontmatter.get('file_type', 'unknown'),
                'last_updated': frontmatter.get('last_updated', 'unknown'),
                'tags': tags
            }

            # Update frequency counts
            for tag in tags:
                self.tag_frequency[tag] += 1

            # Update co-occurrence matrix
            for i, tag1 in enumerate(tags):
                for tag2 in tags[i+1:]:
                    self.tag_cooccurrence[tag1][tag2] += 1
                    self.tag_cooccurrence[tag2][tag1] += 1

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    def identify_vestigial_tags(self, min_age_days: int = 30):
        """Identify single-use tags that are old enough to be considered vestigial."""
        cutoff_date = datetime.now() - timedelta(days=min_age_days)

        for tag, count in self.tag_frequency.items():
            if count == 1:
                # Find the file using this tag
                for file_path, tags in self.file_tags.items():
                    if tag in tags:
                        metadata = self.file_metadata[file_path]
                        last_updated = metadata.get('last_updated', 'unknown')

                        # Try to parse date
                        is_old = False
                        if last_updated != 'unknown':
                            try:
                                file_date = datetime.strptime(last_updated, '%Y-%m-%d')
                                is_old = file_date < cutoff_date
                            except:
                                pass

                        self.vestigial_candidates.append({
                            'tag': tag,
                            'file': file_path,
                            'last_updated': last_updated,
                            'is_old': is_old
                        })
                        break

    def get_top_cooccurrences(self, tag: str, limit: int = 5) -> List[Tuple[str, int]]:
        """Get tags that most frequently co-occur with given tag."""
        if tag not in self.tag_cooccurrence:
            return []
        return self.tag_cooccurrence[tag].most_common(limit)

    def calculate_domain_coverage(self) -> Dict[str, Dict]:
        """Calculate tag usage statistics by domain."""
        domain_stats = defaultdict(lambda: {'file_count': 0, 'tagged_count': 0, 'tag_diversity': set()})

        for file_path, metadata in self.file_metadata.items():
            domain = metadata['domain']
            tags = metadata['tags']

            domain_stats[domain]['file_count'] += 1
            if tags:
                domain_stats[domain]['tagged_count'] += 1
                domain_stats[domain]['tag_diversity'].update(tags)

        # Convert sets to counts
        for domain in domain_stats:
            domain_stats[domain]['unique_tags'] = len(domain_stats[domain]['tag_diversity'])
            del domain_stats[domain]['tag_diversity']

        return dict(domain_stats)

    def generate_snapshot_markdown(self) -> str:
        """Generate human-readable snapshot report."""
        lines = [
            "# TAXONOMY SNAPSHOT",
            f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Plugin Version:** 0.1.0",
            "",
            "---",
            "",
            "## Executive Summary",
            "",
            f"- **Total unique tags:** {len(self.tag_frequency)}",
            f"- **Total tag instances:** {sum(self.tag_frequency.values())} (across {len(self.file_tags)} files)",
            f"- **Files with tags:** {len(self.file_tags)}",
            "",
        ]

        # Tag distribution
        single_use = sum(1 for count in self.tag_frequency.values() if count == 1)
        lines.extend([
            "### Tag Distribution",
            "",
            f"- **Single-use tags:** {single_use} ({single_use/len(self.tag_frequency)*100:.1f}%)",
            f"- **Tags used 2-5 times:** {sum(1 for c in self.tag_frequency.values() if 2 <= c <= 5)}",
            f"- **Tags used 6+ times:** {sum(1 for c in self.tag_frequency.values() if c > 5)}",
            "",
        ])

        # Top tags
        lines.extend([
            "## Top Tags by Frequency",
            "",
            "| Rank | Tag | Count | % of Files |",
            "|------|-----|-------|------------|"
        ])

        total_files = len(self.file_tags)
        for i, (tag, count) in enumerate(self.tag_frequency.most_common(20), 1):
            pct = (count / total_files * 100) if total_files > 0 else 0
            lines.append(f"| {i} | `{tag}` | {count} | {pct:.1f}% |")

        lines.extend(["", ""])

        # Co-occurrence patterns
        lines.extend([
            "## Tag Co-Occurrence Patterns",
            "",
            "**Top 10 Most Frequent Tags and Their Common Companions:**",
            ""
        ])

        for tag, count in self.tag_frequency.most_common(10):
            cooccur = self.get_top_cooccurrences(tag, limit=5)
            if cooccur:
                companions = ", ".join(f"`{t}` ({c})" for t, c in cooccur)
                lines.append(f"- **{tag}** ({count} uses) → Often paired with: {companions}")

        lines.extend(["", ""])

        # Vestigial candidates
        lines.extend([
            "## Vestigial Tag Candidates",
            "",
            f"**Definition:** Tags used only once, 30+ days old",
            f"**Count:** {len([v for v in self.vestigial_candidates if v['is_old']])}",
            "",
        ])

        old_vestigial = [v for v in self.vestigial_candidates if v['is_old']]
        if old_vestigial:
            lines.append("| Tag | File | Last Updated |")
            lines.append("|-----|------|--------------|")
            for v in old_vestigial[:20]:  # Limit to 20
                lines.append(f"| `{v['tag']}` | {v['file']} | {v['last_updated']} |")
        else:
            lines.append("*No vestigial tags detected (all single-use tags are recent)*")

        lines.extend(["", ""])

        # Domain coverage
        domain_stats = self.calculate_domain_coverage()
        lines.extend([
            "## Domain Coverage",
            "",
            "| Domain | Files | Tagged | Unique Tags |",
            "|--------|-------|--------|-------------|"
        ])

        for domain, stats in sorted(domain_stats.items()):
            lines.append(f"| {domain} | {stats['file_count']} | {stats['tagged_count']} | {stats['unique_tags']} |")

        lines.extend(["", ""])

        # Recommendations
        lines.extend([
            "## Recommendations",
            "",
            "### High Priority",
            ""
        ])

        if single_use > len(self.tag_frequency) * 0.6:
            lines.append(f"- **High tag sprawl detected** ({single_use} single-use tags). Consider consolidation during next garden session.")

        # Look for obvious variants
        tag_groups = defaultdict(list)
        for tag in self.tag_frequency.keys():
            prefix = tag.split('-')[0] if '-' in tag else tag
            tag_groups[prefix].append(tag)

        variant_candidates = [(prefix, tags) for prefix, tags in tag_groups.items() if len(tags) > 3]
        if variant_candidates:
            lines.append("- **Potential tag variant families detected:**")
            for prefix, tags in variant_candidates[:5]:
                lines.append(f"  - `{prefix}-*`: {', '.join(f'`{t}`' for t in sorted(tags)[:5])}")

        lines.extend(["", ""])

        # Footer
        lines.extend([
            "---",
            "",
            "**Next Steps:**",
            "1. Review vestigial candidates for removal",
            "2. Identify tag variant families for consolidation",
            "3. Run `/taxonomy-snapshot` again next week to track changes",
            ""
        ])

        return "\n".join(lines)

    def generate_registry_yaml(self) -> str:
        """Generate machine-readable taxonomy registry."""
        registry = {
            'version': '0.1.0',
            'generated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'statistics': {
                'unique_tags': len(self.tag_frequency),
                'total_instances': sum(self.tag_frequency.values()),
                'files_analyzed': len(self.file_tags)
            },
            'tags': {}
        }

        # Add all tags with metadata
        for tag, count in self.tag_frequency.items():
            registry['tags'][tag] = {
                'frequency': count,
                'status': 'active',  # All start as active in v0.1
                'notes': 'Auto-discovered during baseline scan'
            }

        return yaml.dump(registry, sort_keys=False, default_flow_style=False)


def main():
    parser = argparse.ArgumentParser(
        description='Scan FOAM knowledge graph for taxonomy patterns'
    )
    parser.add_argument(
        '--output',
        choices=['snapshot', 'registry', 'both'],
        default='both',
        help='What to generate (default: both)'
    )
    parser.add_argument(
        '--domains',
        type=str,
        help='Comma-separated list of domains to scan (default: all)'
    )
    parser.add_argument(
        '--format',
        choices=['md', 'json'],
        default='md',
        help='Output format (default: md)'
    )

    args = parser.parse_args()

    # Find repo root
    repo_root = Path.cwd()
    while not (repo_root / '.git').exists() and repo_root != repo_root.parent:
        repo_root = repo_root.parent

    if not (repo_root / '.git').exists():
        print("Error: Not in a git repository")
        return 1

    print(f"Repo root: {repo_root}")
    print()

    # Parse domains
    domains = None
    if args.domains:
        domains = [f"{d.strip()}_domain" if not d.startswith('0') else d.strip()
                   for d in args.domains.split(',')]

    # Initialize scanner
    scanner = TaxonomyScanner(repo_root, domains)

    # Run analysis
    print("=" * 60)
    print("TAXONOMY SCAN STARTING")
    print("=" * 60)
    print()

    scanner.scan_files()
    print()

    print("Analyzing patterns...")
    scanner.identify_vestigial_tags()

    # Generate outputs
    print()
    print("=" * 60)
    print("GENERATING OUTPUTS")
    print("=" * 60)
    print()

    if args.output in ['snapshot', 'both']:
        snapshot = scanner.generate_snapshot_markdown()
        output_path = repo_root / 'CURRENT_TAXONOMY_SNAPSHOT.md'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(snapshot)
        print(f"[OK] Generated: {output_path}")

    if args.output in ['registry', 'both']:
        registry = scanner.generate_registry_yaml()
        output_path = repo_root / '.claude-plugins' / 'knowledge-graph-plugin' / 'data' / 'taxonomy-registry.yml'
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(registry)
        print(f"[OK] Generated: {output_path}")

    # Console summary
    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print()
    print(f"Files analyzed:    {len(scanner.file_tags)}")
    print(f"Unique tags:       {len(scanner.tag_frequency)}")
    print(f"Total instances:   {sum(scanner.tag_frequency.values())}")
    print(f"Single-use tags:   {sum(1 for c in scanner.tag_frequency.values() if c == 1)}")
    print(f"Vestigial (old):   {len([v for v in scanner.vestigial_candidates if v['is_old']])}")
    print()

    print("Top 5 tags:")
    for i, (tag, count) in enumerate(scanner.tag_frequency.most_common(5), 1):
        print(f"  {i}. {tag:<30} ({count} files)")

    print()
    print("=" * 60)
    print("SCAN COMPLETE")
    print("=" * 60)

    return 0


if __name__ == '__main__':
    exit(main())
