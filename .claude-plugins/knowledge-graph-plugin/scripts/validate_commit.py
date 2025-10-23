#!/usr/bin/env python3
"""
Validate frontmatter in changed markdown files for knowledge graph compliance.
"""

import os
import sys
import json
import yaml
import subprocess
import re
from pathlib import Path
from typing import Dict, List, Any

# Configuration
KNOWLEDGE_GRAPH_DOMAINS = [
    "00_foundation",
    "01_customer",
    "02_content",
    "03_market_intelligence",
    "05_apps"
]

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

DOMAIN_TAG_MAP = {
    "00_foundation": "foundation",
    "01_customer": "customer",
    "02_content": "content",
    "03_market_intelligence": "market-intelligence",
    "05_apps": "apps"
}

REQUIRED_FIELDS = [
    "name",
    "description",
    "domain",
    "file_type",
    "last_updated",
    "tags",
    "topics",
    "related_docs"
]

def get_changed_files() -> List[str]:
    """Get list of changed markdown files from git."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD"],
            capture_output=True,
            text=True,
            check=True
        )

        # Also get untracked files
        untracked = subprocess.run(
            ["git", "ls-files", "--others", "--exclude-standard"],
            capture_output=True,
            text=True,
            check=True
        )

        all_files = result.stdout.strip().split('\n') + untracked.stdout.strip().split('\n')

        # Filter for markdown files in knowledge graph domains
        md_files = []
        for f in all_files:
            if f and f.endswith('.md'):
                for domain in KNOWLEDGE_GRAPH_DOMAINS:
                    if f.startswith(domain):
                        md_files.append(f)
                        break

        return md_files
    except subprocess.CalledProcessError as e:
        print(f"Error getting changed files: {e}", file=sys.stderr)
        sys.exit(2)

def extract_frontmatter(file_path: str) -> Dict[str, Any]:
    """Extract YAML frontmatter from markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Match frontmatter between --- delimiters
        match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if not match:
            return None

        frontmatter_str = match.group(1)
        return yaml.safe_load(frontmatter_str)
    except Exception as e:
        return None

def validate_file(file_path: str, strict: bool = False) -> Dict[str, Any]:
    """Validate a single file's frontmatter."""
    result = {
        "path": file_path,
        "status": "valid",
        "issues": []
    }

    # Extract frontmatter
    frontmatter = extract_frontmatter(file_path)

    if frontmatter is None:
        result["status"] = "error"
        result["issues"].append({
            "severity": "error",
            "rule": "frontmatter_required",
            "message": "Missing or invalid YAML frontmatter",
            "explanation": "All knowledge graph documents require frontmatter between --- delimiters",
            "fix": {
                "type": "generate_frontmatter",
                "suggested_template": "See /knowledge-graph:add-frontmatter command"
            }
        })
        return result

    # Rule 1: Required fields present
    for field in REQUIRED_FIELDS:
        if field not in frontmatter:
            result["status"] = "error"
            result["issues"].append({
                "severity": "error",
                "rule": f"required_field_{field}",
                "message": f"Missing required field: {field}",
                "explanation": f"Field '{field}' is required for all knowledge graph documents",
                "fix": {
                    "type": "add_field",
                    "field": field,
                    "suggested_value": get_suggested_value(field, file_path, frontmatter)
                }
            })

    # Rule 2: Domain tag must be first in tags array
    if "tags" in frontmatter:
        tags = frontmatter["tags"]
        if not isinstance(tags, list):
            result["status"] = "error"
            result["issues"].append({
                "severity": "error",
                "rule": "tags_must_be_array",
                "message": "Tags field must be an array",
                "fix": {
                    "type": "convert_to_array",
                    "field": "tags"
                }
            })
        else:
            # Determine expected domain tag from file path
            expected_domain_tag = None
            for domain_path, domain_tag in DOMAIN_TAG_MAP.items():
                if file_path.startswith(domain_path):
                    expected_domain_tag = domain_tag
                    break

            if expected_domain_tag:
                if len(tags) == 0 or tags[0] != expected_domain_tag:
                    result["status"] = "error"
                    result["issues"].append({
                        "severity": "error",
                        "rule": "domain_tag_required",
                        "message": f"Missing or incorrect domain tag (expected '{expected_domain_tag}' as first tag)",
                        "explanation": "Foam uses domain tag for node color-coding in knowledge graph",
                        "fix": {
                            "type": "add_to_array",
                            "field": "tags",
                            "value": expected_domain_tag,
                            "position": 0
                        }
                    })

    # Rule 3: Minimum 3 related_docs
    if "related_docs" in frontmatter:
        related_docs = frontmatter["related_docs"]
        if not isinstance(related_docs, list):
            result["status"] = "error"
            result["issues"].append({
                "severity": "error",
                "rule": "related_docs_must_be_array",
                "message": "related_docs field must be an array",
                "fix": {
                    "type": "convert_to_array",
                    "field": "related_docs"
                }
            })
        elif len(related_docs) < 3:
            result["status"] = "error"
            result["issues"].append({
                "severity": "error",
                "rule": "minimum_related_docs",
                "message": f"Insufficient related_docs ({len(related_docs)} found, need 3+)",
                "explanation": "Minimum 3 related_docs required for knowledge graph connectivity",
                "fix": {
                    "type": "suggest_related_docs",
                    "current_count": len(related_docs),
                    "suggestions": suggest_related_docs(file_path, frontmatter)
                }
            })
        else:
            # Rule 4: At least one Tier 1 hub link
            has_tier1_hub = any(
                any(hub.replace('.md', '') in doc for hub in TIER_1_HUBS)
                for doc in related_docs
            )
            if not has_tier1_hub:
                severity = "warning" if not strict else "error"
                result["status"] = severity if result["status"] == "valid" else result["status"]
                result["issues"].append({
                    "severity": severity,
                    "rule": "tier1_hub_link_recommended",
                    "message": "No Tier 1 hub document linked",
                    "explanation": "Best practice: Link to at least one foundation hub (MEDDPICC, comprehensive_market, etc.)",
                    "fix": {
                        "type": "suggest_hub_links",
                        "suggestions": [hub.replace('.md', '') for hub in TIER_1_HUBS]
                    }
                })

    # Rule 5: Topic count (3-7 recommended)
    if "topics" in frontmatter:
        topics = frontmatter["topics"]
        if isinstance(topics, list):
            if len(topics) < 3 or len(topics) > 7:
                severity = "warning" if not strict else "error"
                result["status"] = severity if result["status"] == "valid" else result["status"]
                result["issues"].append({
                    "severity": severity,
                    "rule": "topic_count_recommendation",
                    "message": f"Topic count outside recommended range ({len(topics)} topics, recommend 3-7)",
                    "explanation": "3-7 topics provide optimal searchability without over-tagging",
                    "fix": {
                        "type": "manual",
                        "suggestion": "Review topics for relevance and consolidation"
                    }
                })

    # Rule 6: Validate wiki-link format in related_docs
    if "related_docs" in frontmatter:
        for doc in frontmatter["related_docs"]:
            if not re.match(r'\[\[[\w\s\-_#]+\]\]', doc):
                result["status"] = "error"
                result["issues"].append({
                    "severity": "error",
                    "rule": "wiki_link_format",
                    "message": f"Invalid wiki-link format: {doc}",
                    "explanation": "Use [[document_name]] or [[document_name#section]] format",
                    "fix": {
                        "type": "fix_wiki_link",
                        "current": doc,
                        "suggested": f"[[{doc.strip('[]')}]]"
                    }
                })

    return result

def suggest_related_docs(file_path: str, frontmatter: Dict[str, Any]) -> List[str]:
    """Suggest related_docs based on file location and domain."""
    suggestions = []

    # Always suggest relevant Tier 1 hub
    if file_path.startswith("01_customer"):
        suggestions.extend([
            "[[All Call Summaries]]",
            "[[MEDDPICC_and_Personas]]",
            "[[comprehensive_market_and_customer_intelligence_context]]"
        ])
    elif file_path.startswith("02_content"):
        suggestions.extend([
            "[[content_strategy_master]]",
            "[[Campaign_Messaging_and_Value_Propositions]]",
            "[[comprehensive_market_and_customer_intelligence_context]]"
        ])
    elif file_path.startswith("00_foundation"):
        suggestions.extend([
            "[[MEDDPICC_and_Personas]]",
            "[[condensed_positioning]]",
            "[[CLAUDE]]"
        ])

    return suggestions[:5]  # Return top 5 suggestions

def get_suggested_value(field: str, file_path: str, frontmatter: Dict[str, Any]) -> Any:
    """Get suggested value for missing field."""
    if field == "name":
        return Path(file_path).stem.upper()
    elif field == "domain":
        for domain_path, domain_tag in DOMAIN_TAG_MAP.items():
            if file_path.startswith(domain_path):
                return domain_tag
        return "unknown"
    elif field == "last_updated":
        from datetime import date
        return date.today().isoformat()
    elif field == "tags":
        domain_tag = None
        for domain_path, tag in DOMAIN_TAG_MAP.items():
            if file_path.startswith(domain_path):
                domain_tag = tag
                break
        return [domain_tag] if domain_tag else []
    elif field == "topics":
        return []
    elif field == "related_docs":
        return suggest_related_docs(file_path, frontmatter)
    elif field == "file_type":
        # Infer from path
        if "call_transcript" in file_path or "call" in file_path.lower():
            return "call_transcript"
        elif "campaign" in file_path:
            return "campaign_messaging"
        return "document"
    else:
        return ""

def generate_report(validation_results: List[Dict[str, Any]], strict: bool) -> Dict[str, Any]:
    """Generate final validation report."""
    total_files = len(validation_results)
    files_with_errors = sum(1 for r in validation_results if r["status"] == "error")
    files_with_warnings = sum(1 for r in validation_results if r["status"] == "warning")
    valid_files = total_files - files_with_errors - files_with_warnings

    total_errors = sum(
        len([i for i in r["issues"] if i["severity"] == "error"])
        for r in validation_results
    )
    total_warnings = sum(
        len([i for i in r["issues"] if i["severity"] == "warning"])
        for r in validation_results
    )

    # Check if all issues are auto-fixable
    can_auto_fix = all(
        issue.get("fix", {}).get("type") != "manual"
        for result in validation_results
        for issue in result["issues"]
    )

    return {
        "summary": {
            "total_files": total_files,
            "valid_files": valid_files,
            "files_with_errors": files_with_errors,
            "files_with_warnings": files_with_warnings,
            "total_errors": total_errors,
            "total_warnings": total_warnings
        },
        "files": validation_results,
        "can_auto_fix": can_auto_fix,
        "strict_mode": strict
    }

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Validate knowledge graph frontmatter")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    parser.add_argument("--files", nargs="+", help="Specific files to validate")
    args = parser.parse_args()

    # Get files to validate
    if args.files:
        files = args.files
    else:
        files = get_changed_files()

    if not files:
        # No files to validate
        print(json.dumps({
            "summary": {
                "total_files": 0,
                "valid_files": 0,
                "files_with_errors": 0,
                "files_with_warnings": 0,
                "total_errors": 0,
                "total_warnings": 0
            },
            "files": [],
            "can_auto_fix": True,
            "strict_mode": args.strict
        }))
        sys.exit(0)

    # Validate each file
    results = []
    for file_path in files:
        result = validate_file(file_path, strict=args.strict)
        results.append(result)

    # Generate report
    report = generate_report(results, args.strict)

    # Output JSON
    print(json.dumps(report, indent=2))

    # Exit code
    if report["summary"]["files_with_errors"] > 0:
        sys.exit(1)
    elif report["summary"]["files_with_warnings"] > 0 and args.strict:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
