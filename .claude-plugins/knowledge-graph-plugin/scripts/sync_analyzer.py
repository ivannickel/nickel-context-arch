#!/usr/bin/env python3
"""
Analyze sync changes through knowledge graph lens.
"""

import os
import sys
import json
import subprocess
import yaml
import re
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

# Configuration
TIER_1_HUBS = [
    "comprehensive_market_and_customer_intelligence_context.md",
    "MEDDPICC_and_Personas.md",
    "condensed_positioning.md",
    "CLAUDE.md"
]

TIER_2_HUBS = [
    "All Call Summaries.md",
    "content_strategy_master.md",
    "Campaign_Messaging_and_Value_Propositions.md"
]

DOMAIN_MAP = {
    "00_foundation": "foundation",
    "01_customer": "customer",
    "02_content": "content",
    "03_market_intelligence": "market-intelligence",
    "05_apps": "apps"
}

def get_remote_diff(branch: str = "origin/dev") -> List[str]:
    """Get list of changed files between local and remote."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", f"HEAD..{branch}"],
            capture_output=True,
            text=True,
            check=True
        )
        files = [f for f in result.stdout.strip().split('\n') if f]
        return files
    except subprocess.CalledProcessError as e:
        print(f"Error getting diff: {e}", file=sys.stderr)
        sys.exit(1)

def get_commit_metadata(branch: str = "origin/dev") -> Dict[str, Any]:
    """Get metadata about commits since last pull."""
    try:
        # Count commits
        count_result = subprocess.run(
            ["git", "rev-list", "--count", f"HEAD..{branch}"],
            capture_output=True,
            text=True,
            check=True
        )
        commit_count = int(count_result.stdout.strip() or 0)

        # Get last commit info
        log_result = subprocess.run(
            ["git", "log", f"HEAD..{branch}", "--format=%an|||%ar|||%s", "-1"],
            capture_output=True,
            text=True,
            check=True
        )

        if log_result.stdout.strip():
            author, time_ago, message = log_result.stdout.strip().split('|||', 2)
        else:
            author = time_ago = message = "N/A"

        return {
            "commits_since_last_pull": commit_count,
            "last_author": author,
            "last_commit_time": time_ago,
            "last_commit_message": message
        }
    except Exception as e:
        return {
            "commits_since_last_pull": 0,
            "last_author": "unknown",
            "last_commit_time": "unknown",
            "last_commit_message": ""
        }

def extract_frontmatter(file_path: str, branch: str = "origin/dev") -> Dict[str, Any]:
    """Extract frontmatter from file (from remote version)."""
    try:
        # Get file content from remote
        result = subprocess.run(
            ["git", "show", f"{branch}:{file_path}"],
            capture_output=True,
            text=True,
            check=True
        )
        content = result.stdout

        match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if match:
            return yaml.safe_load(match.group(1)) or {}
        return {}
    except:
        return {}

def get_diff_summary(file_path: str, branch: str = "origin/dev") -> str:
    """Get summary of what changed in file."""
    try:
        result = subprocess.run(
            ["git", "diff", f"HEAD..{branch}", "--", file_path],
            capture_output=True,
            text=True,
            check=True
        )
        diff = result.stdout

        # Extract changed lines (simplified)
        added_lines = [line for line in diff.split('\n') if line.startswith('+') and not line.startswith('+++')]
        removed_lines = [line for line in diff.split('\n') if line.startswith('-') and not line.startswith('---')]

        # Try to summarize meaningfully
        if len(added_lines) > len(removed_lines):
            return f"Added {len(added_lines)} lines"
        elif len(removed_lines) > len(added_lines):
            return f"Removed {len(removed_lines)} lines"
        else:
            return f"Modified {len(added_lines)} lines"
    except:
        return "Modified"

def count_downstream_links(file_path: str) -> int:
    """Count how many other documents link to this file."""
    file_name = Path(file_path).stem
    count = 0

    try:
        # Search for wiki-links to this file
        result = subprocess.run(
            ["git", "grep", "-l", f"\\[\\[{file_name}"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            links = result.stdout.strip().split('\n')
            # Filter out self-references
            count = len([link for link in links if link and link != file_path])
    except:
        pass

    return count

def classify_file(file_path: str) -> Dict[str, Any]:
    """Classify file as hub/spoke/taxonomy and determine priority."""
    file_name = Path(file_path).name

    classification = {
        "file": file_path,
        "priority": "standard",
        "tier": None,
        "domain": "unknown",
        "type": "spoke"
    }

    # Check if hub document
    if file_name in TIER_1_HUBS:
        classification["priority"] = "high"
        classification["tier"] = 1
        classification["type"] = "hub"
    elif file_name in TIER_2_HUBS:
        classification["priority"] = "high"
        classification["tier"] = 2
        classification["type"] = "hub"

    # Determine domain
    for domain_path, domain_name in DOMAIN_MAP.items():
        if file_path.startswith(domain_path):
            classification["domain"] = domain_name
            break

    # Special cases
    if "taxonomy" in file_path.lower():
        classification["type"] = "taxonomy"
        classification["priority"] = "high"
    elif file_path.startswith("05_apps") or file_path.startswith(".claude"):
        classification["type"] = "app"
        classification["priority"] = "low"

    return classification

def analyze_file(file_path: str, branch: str) -> Dict[str, Any]:
    """Analyze a single changed file."""
    classification = classify_file(file_path)
    frontmatter = extract_frontmatter(file_path, branch)

    analysis = {
        **classification,
        "frontmatter": frontmatter,
        "changes_summary": get_diff_summary(file_path, branch),
        "downstream_count": 0,
        "why_matters": "",
        "next_actions": []
    }

    # For hub documents, get downstream count
    if classification["type"] == "hub":
        analysis["downstream_count"] = count_downstream_links(file_path)
        analysis["why_matters"] = generate_why_matters(classification, analysis["downstream_count"])
        analysis["next_actions"] = generate_next_actions(classification, frontmatter)

    return analysis

def generate_why_matters(classification: Dict[str, Any], downstream_count: int) -> str:
    """Generate explanation of why this change matters."""
    if classification["tier"] == 1:
        return f"Foundation hub with {downstream_count} dependent documents. Changes affect multiple domains."
    elif classification["tier"] == 2:
        domain = classification["domain"]
        return f"Domain hub for {domain}. Changes affect {downstream_count} documents in this domain."
    elif classification["type"] == "taxonomy":
        return "Taxonomy changes affect tag standards and graph structure across all documents."
    return ""

def generate_next_actions(classification: Dict[str, Any], frontmatter: Dict[str, Any]) -> List[str]:
    """Generate suggested next actions."""
    actions = []

    if classification["tier"] in [1, 2]:
        actions.append("Review changes to hub document")
        actions.append("Check if any of your documents reference this hub")
        actions.append("Update related content if messaging changed")

    if classification["type"] == "taxonomy":
        actions.append("Run /knowledge-graph:taxonomy-snapshot to update local registry")
        actions.append("Review new tags for consolidation opportunities")

    return actions

def check_taxonomy_changes(changed_files: List[str]) -> Dict[str, Any]:
    """Detect taxonomy-related changes."""
    taxonomy_changes = {
        "new_tags": [],
        "new_personas": [],
        "registry_updated": False,
        "governance_alerts": []
    }

    # Check if taxonomy-registry.yml changed
    if any("taxonomy-registry.yml" in f or "taxonomy" in f for f in changed_files):
        taxonomy_changes["registry_updated"] = True

    return taxonomy_changes

def run_health_check(changed_files: List[str]) -> Dict[str, Any]:
    """Run quick health check on changed files."""
    health = {
        "broken_links": [],
        "missing_domain_tags": [],
        "validation_warnings": []
    }

    # Quick validation could be added here
    return health

def generate_report(changed_files: List[str], branch: str) -> Dict[str, Any]:
    """Generate complete sync analysis report."""
    metadata = get_commit_metadata(branch)
    metadata["branch"] = branch
    metadata["total_files_changed"] = len(changed_files)

    # Analyze each file
    high_priority = []
    standard_updates = []

    for file in changed_files:
        # Skip non-markdown files
        if not file.endswith('.md'):
            continue

        analysis = analyze_file(file, branch)

        if analysis["priority"] == "high":
            high_priority.append(analysis)
        else:
            standard_updates.append(analysis)

    # Sort high priority by tier
    high_priority.sort(key=lambda x: (x["tier"] or 99, -x["downstream_count"]))

    # Taxonomy changes
    taxonomy_changes = check_taxonomy_changes(changed_files)

    # Health check
    health_check = run_health_check(changed_files)

    return {
        "metadata": metadata,
        "high_priority": high_priority,
        "standard_updates": standard_updates,
        "taxonomy_changes": taxonomy_changes,
        "health_check": health_check
    }

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Analyze knowledge graph sync changes")
    parser.add_argument("--branch", default="origin/dev", help="Remote branch to compare")
    parser.add_argument("--quiet", action="store_true", help="Minimal output")
    args = parser.parse_args()

    # Get changed files
    changed_files = get_remote_diff(args.branch)

    if not changed_files:
        print(json.dumps({
            "metadata": {
                "branch": args.branch,
                "total_files_changed": 0,
                "commits_since_last_pull": 0
            },
            "high_priority": [],
            "standard_updates": [],
            "taxonomy_changes": {},
            "health_check": {}
        }))
        sys.exit(0)

    # Generate report
    report = generate_report(changed_files, args.branch)

    # Output JSON
    print(json.dumps(report, indent=2))
    sys.exit(0)

if __name__ == "__main__":
    main()
