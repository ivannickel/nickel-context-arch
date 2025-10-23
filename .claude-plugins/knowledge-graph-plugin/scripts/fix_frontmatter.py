#!/usr/bin/env python3
"""
Apply automatic fixes to frontmatter issues.
"""

import os
import sys
import json
import yaml
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Any

def read_file_content(file_path: str) -> str:
    """Read file content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file_content(file_path: str, content: str):
    """Write file content."""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_frontmatter_and_body(content: str) -> tuple:
    """Extract frontmatter and body separately."""
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if match:
        frontmatter_str = match.group(1)
        body = match.group(2)
        frontmatter = yaml.safe_load(frontmatter_str) or {}
        return frontmatter, body
    return {}, content

def apply_fix(frontmatter: Dict[str, Any], fix: Dict[str, Any]) -> Dict[str, Any]:
    """Apply a single fix to frontmatter."""
    fix_type = fix["type"]

    if fix_type == "add_field":
        frontmatter[fix["field"]] = fix["suggested_value"]

    elif fix_type == "add_to_array":
        field = fix["field"]
        if field not in frontmatter:
            frontmatter[field] = []
        if not isinstance(frontmatter[field], list):
            frontmatter[field] = [frontmatter[field]]

        position = fix.get("position", 0)
        value = fix["value"]

        # Don't add if already present
        if value not in frontmatter[field]:
            if position == 0:
                frontmatter[field].insert(0, value)
            else:
                frontmatter[field].append(value)

    elif fix_type == "convert_to_array":
        field = fix["field"]
        if field in frontmatter and not isinstance(frontmatter[field], list):
            frontmatter[field] = [frontmatter[field]]

    elif fix_type == "suggest_related_docs":
        # Add suggested docs
        if "related_docs" not in frontmatter:
            frontmatter["related_docs"] = []
        for suggestion in fix["suggestions"]:
            if suggestion not in frontmatter["related_docs"]:
                frontmatter["related_docs"].append(suggestion)

    elif fix_type == "suggest_hub_links":
        # Add first suggested hub link
        if "related_docs" not in frontmatter:
            frontmatter["related_docs"] = []
        if fix["suggestions"] and len(fix["suggestions"]) > 0:
            hub = f"[[{fix['suggestions'][0]}]]"
            if hub not in frontmatter["related_docs"]:
                frontmatter["related_docs"].append(hub)

    elif fix_type == "fix_wiki_link":
        # Fix wiki-link format
        field = "related_docs"
        if field in frontmatter and isinstance(frontmatter[field], list):
            frontmatter[field] = [
                fix["suggested"] if doc == fix["current"] else doc
                for doc in frontmatter[field]
            ]

    return frontmatter

def fix_file(file_path: str, issues: List[Dict[str, Any]]) -> bool:
    """Fix all issues in a file."""
    try:
        content = read_file_content(file_path)
        frontmatter, body = extract_frontmatter_and_body(content)

        # Apply all fixes
        for issue in issues:
            if "fix" in issue and issue["fix"]["type"] not in ["manual", "generate_frontmatter"]:
                frontmatter = apply_fix(frontmatter, issue["fix"])

        # Reconstruct file
        frontmatter_str = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False, allow_unicode=True)
        new_content = f"---\n{frontmatter_str}---\n{body}"

        write_file_content(file_path, new_content)
        return True
    except Exception as e:
        print(f"Error fixing {file_path}: {e}", file=sys.stderr)
        return False

def get_validation_report() -> Dict[str, Any]:
    """Get validation report from previous run."""
    try:
        result = subprocess.run(
            ["python", ".claude-plugins/knowledge-graph-plugin/scripts/validate_commit.py"],
            capture_output=True,
            text=True,
            check=False
        )
        return json.loads(result.stdout)
    except Exception as e:
        print(f"Error getting validation report: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Apply frontmatter fixes")
    parser.add_argument("--apply", action="store_true", help="Actually apply fixes (default: dry-run)")
    args = parser.parse_args()

    # Get validation report
    report = get_validation_report()

    if not report.get("can_auto_fix"):
        print("Cannot auto-fix: Some issues require manual intervention", file=sys.stderr)
        sys.exit(1)

    # Apply fixes
    fixed_count = 0
    for file_result in report["files"]:
        if file_result["status"] in ["error", "warning"] and file_result["issues"]:
            # Filter to only auto-fixable issues
            fixable_issues = [
                issue for issue in file_result["issues"]
                if issue.get("fix", {}).get("type") not in ["manual", "generate_frontmatter"]
            ]

            if fixable_issues:
                if args.apply:
                    if fix_file(file_result["path"], fixable_issues):
                        fixed_count += 1
                        print(f"✓ Fixed {file_result['path']} ({len(fixable_issues)} issues)")
                else:
                    print(f"Would fix {file_result['path']} ({len(fixable_issues)} issues)")

    if args.apply:
        print(f"\n✅ Fixed {fixed_count} file(s)")
    else:
        print(f"\nDry-run complete. Use --apply to actually fix files.")

    sys.exit(0)

if __name__ == "__main__":
    main()
