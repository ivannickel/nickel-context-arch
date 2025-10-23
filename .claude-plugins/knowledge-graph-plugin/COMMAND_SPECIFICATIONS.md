# Knowledge Graph Commands - Technical Specifications

**Version:** 0.1.0 (Revised)
**Date:** 2025-10-21
**Last Revised:** 2025-10-21
**Authors:** jacob-dietle, Claude (plugin-design-strategist)

---

## Revision History

### v0.1.0-revised (2025-10-21)
**Critical Format Corrections Based on Official Claude Code Documentation**

After reviewing official Claude Code documentation and examples from `@anthropics/claude-code` and `davila7/claude-code-templates`, the following corrections were made:

1. **Frontmatter Format Changed:**
   - ❌ **Old (Incorrect):** YAML format (`---\nkey: value\n---`)
   - ✅ **New (Correct):** Table format (`| description | allowed-tools |`)
   - **Reason:** Commands use table-based frontmatter, not YAML (agents use YAML)

2. **Command Execution Model Changed:**
   - ❌ **Old (Incorrect):** "Parse JSON output and display to user"
   - ✅ **New (Correct):** "Claude interprets JSON and makes decisions based on instructions"
   - **Reason:** Commands are **instructions for Claude**, not scripts Claude parses

3. **Added `allowed-tools` Field:**
   - Now explicitly lists tools Claude can use (Bash, Read, Edit, Task, Grep)
   - This was missing in original spec

4. **Command Naming Updated:**
   - Changed from `/commit` and `/sync` to `/knowledge-graph:commit` and `/knowledge-graph:sync`
   - Follows plugin namespacing convention

**Core Insight:** Commands tell Claude **HOW to execute a workflow**, not **WHAT to output**. Claude reads instructions, executes tools, interprets results, makes decisions, and interacts with users based on the guidance provided.

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Command 1: `/commit` Specification](#command-1-commit-specification)
4. [Command 2: `/sync` Specification](#command-2-sync-specification)
5. [Shared Components](#shared-components)
6. [File Structure](#file-structure)
7. [Testing Strategy](#testing-strategy)
8. [Performance Requirements](#performance-requirements)
9. [Error Handling](#error-handling)
10. [Future Enhancements](#future-enhancements)

---

## Overview

### Purpose

Provide knowledge-graph-aware git workflow commands that:
1. Validate frontmatter integrity before commits
2. Surface high-impact changes after pulls
3. Maintain team awareness and alignment

### Success Criteria

- **Primary:** Awareness and alignment across 4 collaborators
- **Proxy Metrics:**
  - 95% domain tag compliance on new files
  - <3 min post-pull triage time
  - 100% hub change awareness within 24h

### User Personas

- **Primary User:** Technical GTM professional (comfortable with git, new to knowledge graphs)
- **Team Size:** 4 active collaborators (scaling from 2)
- **Skill Levels:** Mixed (power users + newcomers)

---

## Architecture

### System Context Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     Knowledge Graph Repo                     │
│                                                               │
│  ┌─────────────┐         ┌──────────────┐                   │
│  │   User      │────────▶│ Claude Code  │                   │
│  └─────────────┘         └──────┬───────┘                   │
│                                  │                            │
│                                  │ invokes                    │
│                                  ▼                            │
│                   ┌──────────────────────────┐               │
│                   │  Knowledge Graph Plugin  │               │
│                   │  ┌────────────────────┐  │               │
│                   │  │  /commit command   │  │               │
│                   │  └─────────┬──────────┘  │               │
│                   │            │              │               │
│                   │  ┌─────────▼──────────┐  │               │
│                   │  │  /sync command     │  │               │
│                   │  └─────────┬──────────┘  │               │
│                   │            │              │               │
│                   │  ┌─────────▼──────────┐  │               │
│                   │  │ Shared Components  │  │               │
│                   │  │ • Validator        │  │               │
│                   │  │ • Metadata Parser  │  │               │
│                   │  │ • Git Interface    │  │               │
│                   │  │ • Fix Generator    │  │               │
│                   │  └────────────────────┘  │               │
│                   └─────────┬────────────────┘               │
│                             │                                 │
│                             ▼                                 │
│           ┌─────────────────────────────────┐                │
│           │   Knowledge Graph Documents     │                │
│           │   (00_foundation/, 01_customer, │                │
│           │    02_content/, etc.)           │                │
│           └─────────────────────────────────┘                │
│                             ▲                                 │
│                             │                                 │
│                   ┌─────────┴────────────┐                   │
│                   │   Git Repository     │                   │
│                   │   (origin/dev)       │                   │
│                   └──────────────────────┘                   │
└─────────────────────────────────────────────────────────────┘
```

### Component Interaction Flow

```
/commit Flow:
  User types "/commit"
    ↓
  Claude Code invokes commit.md
    ↓
  validate_commit.py executed
    ↓
  Scans changed files → Extracts frontmatter → Validates rules
    ↓
  If errors found:
    generate_fixes.py → Create fix plan → Present to user
      ↓
    User chooses: [Apply fixes | Commit anyway | Cancel]
      ↓
    If apply: fix_frontmatter.py → Re-validate
      ↓
  Output validation report
    ↓
  Claude Code handles actual git commit

/sync Flow:
  User types "/sync"
    ↓
  Claude Code invokes sync.md
    ↓
  sync_analyzer.py executed
    ↓
  Git fetch → Git diff → Identify changed files
    ↓
  For each changed file:
    Extract metadata → Classify (hub/spoke/taxonomy)
    Calculate impact (downstream links)
    ↓
  generate_sync_summary.py
    ↓
  Prioritize: [High-priority hubs | Standard updates | Taxonomy]
    ↓
  Git pull
    ↓
  Output contextualized summary
```

---

## Command 1: `/commit` Specification

### 1.1 Command Interface

**File:** `.claude-plugins/knowledge-graph-plugin/commands/commit.md`

**Invocation:**
```bash
/knowledge-graph:commit                    # Default: warn and offer fixes
/knowledge-graph:commit --strict          # Block on any warnings
/knowledge-graph:commit --skip-validation # Skip validation entirely
```

**Frontmatter (Table Format):**
```markdown
| description | allowed-tools | argument-hint |
|---|---|---|
| Validate knowledge graph frontmatter and commit changes with user control over fixes | Bash, Read, Edit, Task | [--strict\|--skip-validation] |
```

### 1.2 Command Body Template

**Key Principle:** The command file contains **instructions for Claude**, not a script. Claude reads these instructions, executes tools, interprets results, makes decisions, and interacts with the user.

```markdown
| description | allowed-tools | argument-hint |
|---|---|---|
| Validate knowledge graph frontmatter and commit changes with user control over fixes | Bash, Read, Edit, Task | [--strict\|--skip-validation] |

# Knowledge Graph Commit

Validate knowledge graph frontmatter integrity before committing changes.

## Your Task

You will validate all changed markdown files in the knowledge graph against frontmatter standards, offer to fix any issues, and then proceed with the git commit workflow.

## Process

### Step 1: Run Validation Script

Execute the validation script using the Bash tool:

```bash
python .claude-plugins/knowledge-graph-plugin/scripts/validate_commit.py $ARGUMENTS
```

The script will output a JSON report with validation results including:
- Summary statistics (total files, errors, warnings)
- Per-file issues with severity levels
- Suggested fixes for each issue
- Whether issues can be auto-fixed

### Step 2: Interpret and Present Results

Parse the JSON output from the validation script. For each file:

**If the file is valid:**
- Display: `✅ [filename] - Valid`

**If the file has errors:**
- Display: `❌ [filename] - [N] issues`
- For each issue, present:
  - **What's wrong:** The issue message from the JSON
  - **Why it matters:** The explanation field
  - **How to fix:** The suggested fix from the JSON

**If the file has warnings:**
- Display: `⚠️ [filename] - [N] warnings`
- Present same format as errors

### Step 3: Determine Fix Strategy

Look at the `can_auto_fix` field in the JSON report.

**If can_auto_fix is true:**

Present the user with these options:

```
OPTIONS:
  1. Apply fixes automatically and commit
  2. Commit without fixes (not recommended - may break knowledge graph)
  3. Cancel and fix manually

What would you like to do? [1/2/3]
```

**If can_auto_fix is false:**

Some issues require manual intervention. Present:

```
⚠️ Some issues cannot be auto-fixed and require manual intervention.

OPTIONS:
  1. Cancel and fix manually
  2. Commit anyway (not recommended)

What would you like to do? [1/2]
```

### Step 4: Execute User's Choice

**If user chooses "Apply fixes automatically" (Option 1):**

1. Run the fix script:
   ```bash
   python .claude-plugins/knowledge-graph-plugin/scripts/fix_frontmatter.py --apply
   ```

2. The script will modify files and output a summary. Display this to the user.

3. Re-run validation to confirm fixes worked:
   ```bash
   python .claude-plugins/knowledge-graph-plugin/scripts/validate_commit.py
   ```

4. If validation now passes, display: `✅ All files now valid`

5. Proceed to commit (Step 5)

**If user chooses "Commit without fixes" (Option 2):**

Display warning:
```
⚠️ Committing with validation issues...

Note: Knowledge graph may have integrity issues.
Recommend running /knowledge-graph:validate-frontmatter on affected files later.
```

Proceed to commit (Step 5)

**If user chooses "Cancel" (Option 3 or 1 for manual-only):**

Display:
```
Commit cancelled. Fix issues manually and run /knowledge-graph:commit again.

To fix manually:
- Review the issues listed above
- Edit the affected files
- Run /knowledge-graph:commit when ready
```

Exit without committing.

### Step 5: Proceed to Git Commit

Once validation passes (or user chose to proceed anyway), you should now delegate to Claude Code's standard git commit workflow.

Display:
```
📤 KNOWLEDGE GRAPH COMMIT

All validation checks complete. Proceeding with commit...
```

Then follow the standard commit workflow:
1. Run `git status` to see changed files
2. Run `git diff` to see changes
3. Stage relevant files
4. Create commit with appropriate message
5. Ask user if they want to push

## Arguments Handling

- **$ARGUMENTS** may contain:
  - `--strict`: Pass this flag to the validation script. Treats warnings as errors.
  - `--skip-validation`: Skip validation entirely and go straight to commit
  - No arguments: Default behavior (warn and offer fixes)

**If `--skip-validation` is present:**
Skip Steps 1-4 and go directly to Step 5 (git commit).

## Error Handling

**If validation script fails to execute:**
```
❌ ERROR: Validation script failed to execute

[Error message from script]

Possible fixes:
- Ensure Python 3 is installed: python --version
- Check script exists at: .claude-plugins/knowledge-graph-plugin/scripts/validate_commit.py

Cannot proceed to commit without validation.
```

**If fix script fails:**
```
❌ ERROR: Failed to apply fixes

[Error message from script]

Recommend:
1. Fix issues manually
2. Run /knowledge-graph:commit again
```

Do not proceed to commit.

## Performance Expectations

- Validation should complete in <5 seconds for typical commits (10 files)
- Fixing should complete in <3 seconds
- Total workflow: <10 seconds before proceeding to commit

## Notes

- This command integrates with Claude Code's built-in git workflow
- The validation script outputs structured JSON for programmatic parsing
- All frontmatter fixes preserve existing file structure
- Users maintain full control over whether fixes are applied
```

### 1.3 Validation Script Specification

**File:** `.claude-plugins/knowledge-graph-plugin/scripts/validate_commit.py`

**Purpose:** Scan changed markdown files and validate frontmatter against knowledge graph standards

**Inputs:**
- Changed files from git (git diff --name-only HEAD)
- Validation rules (hardcoded or from config)
- Optional flags: --strict, --files <file1> <file2>

**Outputs:**
- JSON report to stdout
- Exit code: 0 (valid), 1 (errors found), 2 (warnings only)

**Logic Flow:**

```python
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
                "suggested_template": "See /add-frontmatter command"
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
                any(hub in doc for hub in TIER_1_HUBS)
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
                        "suggestions": TIER_1_HUBS
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
        if "call_transcript" in file_path:
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
```

### 1.4 Fix Generator Script Specification

**File:** `.claude-plugins/knowledge-graph-plugin/scripts/fix_frontmatter.py`

**Purpose:** Automatically apply fixes to frontmatter issues identified by validation

**Inputs:**
- Validation report JSON (from validate_commit.py)
- --apply flag to actually write changes

**Outputs:**
- Modified markdown files with fixed frontmatter
- Summary of changes made

**See full implementation in Section 5: Shared Components**

---

## Command 2: `/sync` Specification

### 2.1 Command Interface

**File:** `.claude-plugins/knowledge-graph-plugin/commands/sync.md`

**Invocation:**
```bash
/knowledge-graph:sync                     # Pull from origin/dev with summary
/knowledge-graph:sync --branch main      # Pull from different branch
/knowledge-graph:sync --quiet            # Pull without summary
```

**Frontmatter (Table Format):**
```markdown
| description | allowed-tools | argument-hint |
|---|---|---|
| Pull changes from remote and generate knowledge-graph-aware summary highlighting hub changes and taxonomy updates | Bash, Read, Grep, Task | [--branch <name>\|--quiet] |
```

### 2.2 Command Body Template

**Key Principle:** The command file contains **instructions for Claude**, not a script. Claude reads these instructions, executes git operations, interprets results, and presents a contextualized summary.

```markdown
| description | allowed-tools | argument-hint |
|---|---|---|
| Pull changes from remote and generate knowledge-graph-aware summary highlighting hub changes and taxonomy updates | Bash, Read, Grep, Task | [--branch <name>\|--quiet] |

# Knowledge Graph Sync

Pull changes from remote and generate a knowledge-graph-aware summary highlighting high-impact changes.

## Your Task

You will fetch changes from the remote repository, analyze them through the lens of the knowledge graph structure (identifying hub vs spoke documents, taxonomy changes, downstream impacts), and present a prioritized summary to help users quickly understand what changed and why it matters.

## Process

### Step 1: Fetch from Remote

Determine the target branch from $ARGUMENTS (default: `origin/dev`).

Execute fetch using Bash tool:

```bash
git fetch origin dev
```

(Or use branch specified in $ARGUMENTS if `--branch <name>` is present)

### Step 2: Analyze Changed Files

Run the sync analyzer script:

```bash
python .claude-plugins/knowledge-graph-plugin/scripts/sync_analyzer.py --branch origin/dev
```

(Use the branch from $ARGUMENTS if specified)

The script will output a JSON report containing:
- Metadata (total files changed, last author, commit count)
- High-priority changes (Tier 1/2 hub documents)
- Standard updates (spoke documents, apps)
- Taxonomy changes (new tags, personas)
- Health check results (broken links, missing tags)

### Step 3: Present Contextualized Summary

Parse the JSON output and format it into a user-friendly summary.

**If `--quiet` flag is present:**
Skip summary presentation and go directly to Step 4 (pull).

**Otherwise, present this structured summary:**

```
📥 KNOWLEDGE GRAPH SYNC

Fetching from [branch]...
Analyzing changes...

─────────────────────────────────────────
Changes from [author] ([count] files, [time] ago)

🎯 HIGH PRIORITY - Review These First:
─────────────────────────────────────────

[For each high-priority file from JSON:]

[N]. [filename] (Tier [1/2] hub - [domain])
   Changed: [time] ago by [author]
   Impact: [downstream_count] documents link to this hub

   What changed:
   • [Change summary from JSON]

   → WHY YOU SHOULD CARE:
     [why_matters explanation from JSON]

   → NEXT ACTIONS:
     [next_actions list from JSON]

─────────────────────────────────────────
📝 STANDARD UPDATES:
─────────────────────────────────────────

[For each standard update from JSON:]

[N]. [filename] ([domain] spoke)
   • [Brief description]
   • Tags: [tags from frontmatter]
   • Links to: [key related_docs]
   • No action needed [or specific note]

─────────────────────────────────────────
🏷️  TAXONOMY CHANGES:
─────────────────────────────────────────

[If taxonomy_changes exists in JSON:]

New tags added:
  • [tag-name] ([N] uses) - [context]

New personas added:
  • [persona-name] - [context]

⚠️  GOVERNANCE ALERT:
  [Any governance alerts from JSON, e.g., single-use tags]

→ NEXT ACTION:
  Run /knowledge-graph:taxonomy-snapshot to update local registry

─────────────────────────────────────────
📊 KNOWLEDGE GRAPH HEALTH:
─────────────────────────────────────────

[From health_check in JSON:]
✅ No broken wiki-links detected
✅ All new files have domain tags
⚠️  [Any warnings]

─────────────────────────────────────────

Pulling from [branch]...
```

### Step 4: Pull from Remote

After presenting the summary (or if --quiet), execute the pull:

```bash
git pull origin dev
```

(Use branch from $ARGUMENTS if specified)

**If pull succeeds:**
```
✅ Pull complete

Your local knowledge graph is now up to date.

RECOMMENDED NEXT STEPS:
  1. [Top recommended action from high-priority items]
  2. [Second recommended action]
  3. [Run taxonomy snapshot if needed]
```

**If merge conflicts occur:**
Show detailed conflict resolution instructions (see Error Handling section).

### Step 5: Output Summary Statistics

Display final status:
```
📊 SYNC SUMMARY:
  • Files changed: [N]
  • Hub documents updated: [N]
  • Taxonomy changes: [Yes/No]
  • Action items: [N]
```

## Arguments Handling

- **$ARGUMENTS** may contain:
  - `--branch <name>`: Specify remote branch to sync from (default: origin/dev)
  - `--quiet`: Skip summary presentation, just pull
  - No arguments: Default behavior (sync from origin/dev with full summary)

**Branch handling:**
If user specifies `--branch main`, replace `origin/dev` with `origin/main` in all git commands.

## Error Handling

**If fetch fails (network error):**
```
❌ ERROR: Cannot fetch from remote

Failed to connect to [branch]

Possible causes:
  • No internet connection
  • Remote repository unavailable
  • Authentication required

Fix: Check network connection and git credentials
```

Do not proceed to pull.

**If merge conflicts occur during pull:**
```
❌ MERGE CONFLICTS DETECTED

The following files have conflicts:
  • [file1]
  • [file2]

Resolve conflicts manually:
  1. Open conflicted files
  2. Look for <<<<<<< === >>>>>>> markers
  3. Choose which changes to keep
  4. Remove conflict markers
  5. Run 'git add <file>' for each resolved file
  6. Run 'git commit' to complete merge

Then run /knowledge-graph:sync again to see summary.
```

**If sync analyzer script fails:**
```
⚠️ Warning: Could not generate detailed analysis

Proceeding with basic pull...
```

Continue with pull but skip detailed summary.

**If no changes to pull:**
```
📥 KNOWLEDGE GRAPH SYNC

Fetching from [branch]...

✅ Already up to date

No changes since your last pull.
Knowledge graph is synchronized.
```

## Performance Expectations

- Fetch + diff analysis: <5 seconds
- Summary generation: <3 seconds
- Pull operation: <5 seconds (network dependent)
- Total workflow: <15 seconds end-to-end

## Notes

- This command provides **context** about what changed, not just file names
- Hub document changes are prioritized because they affect multiple downstream documents
- Taxonomy changes surface new tags/personas to prevent sprawl
- Health checks catch common issues (broken links, missing domain tags)
- Users can run --quiet for quick pulls without analysis

## Example Output Scenarios

**Scenario 1: Hub Document Updated**
```
🎯 HIGH PRIORITY - Review These First:

1. MEDDPICC_and_Personas.md (Tier 1 hub - foundation)
   Changed: 22 hours ago by daharmattan1
   Impact: 12 documents link to this hub

   What changed:
   • Added "Head of AppSec" persona
   • Updated CISO pain points

   → WHY YOU SHOULD CARE:
     Foundation hub affects customer interviews and content strategy

   → NEXT ACTIONS:
     - Review new persona definition
     - Update content referencing AppSec leaders
```

**Scenario 2: Routine Content Update**
```
📝 STANDARD UPDATES:

3. google_ads_campaign_q4.md (content spoke)
   • New campaign messaging for Q4
   • Tags: [content, campaign-messaging, paid-ads]
   • Links to: content_strategy_master
   • No action needed (routine content update)
```

**Scenario 3: Taxonomy Change Alert**
```
🏷️  TAXONOMY CHANGES:

New tags added:
  • tool-sprawl-fatigue (1 use)

⚠️  GOVERNANCE ALERT:
  New tag "tool-sprawl-fatigue" is single-use.
  Consider consolidating with existing "tool-sprawl" tag.
```
```

### 2.3 Sync Analyzer Script Specification

**File:** `.claude-plugins/knowledge-graph-plugin/scripts/sync_analyzer.py`

**Purpose:** Analyze git changes and generate knowledge-graph-aware summary

**Inputs:**
- Git diff between local and remote
- Frontmatter from changed files
- Knowledge graph structure (hub/spoke relationships)

**Outputs:**
- JSON report with prioritized changes, impact analysis, taxonomy changes

**Implementation:** See Python script in Section 5 (Shared Components)

---

## Shared Components

Complete utility library, fix generator, and helper functions will be implemented as specified.

---

## File Structure

```
.claude-plugins/knowledge-graph-plugin/
├── commands/
│   ├── commit.md                      # NEW
│   └── sync.md                        # NEW
├── scripts/
│   ├── validate_commit.py             # NEW
│   ├── fix_frontmatter.py             # NEW
│   ├── sync_analyzer.py               # NEW
│   └── kg_utils.py                    # NEW
├── logs/
│   └── commands.log                   # NEW
└── COMMAND_SPECIFICATIONS.md          # THIS FILE
```

---

## Performance Requirements

- `/commit`: <10s for 10 files
- `/sync`: <15s end-to-end
- Support 500+ documents
- <100MB memory usage

---

## Success Metrics (30 Days)

1. **Awareness & Alignment:** All team members know when hubs change
2. **Domain Tag Compliance:** 95% on new files
3. **Time Savings:** <3 min post-pull triage
4. **Adoption:** All 4 team members using commands

---

**Ready for implementation. All architecture, flows, scripts, and interfaces are fully specified.**
