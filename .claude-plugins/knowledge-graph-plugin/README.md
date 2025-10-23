# Knowledge Graph Plugin
**Taxonomy Navigator for FOAM-based Knowledge Graphs**

Version: 0.1.0 (Observation Phase)
Status: Production Ready
Philosophy: Garden, Don't Architect

---

## Table of Contents

1. [Overview](#overview)
2. [Philosophy](#philosophy)
3. [Installation](#installation)
4. [Quick Start](#quick-start)
5. [Commands Reference](#commands-reference)
6. [Agents Reference](#agents-reference)
7. [Architecture](#architecture)
8. [Roadmap](#roadmap)
9. [Troubleshooting](#troubleshooting)

---

## Overview

### What is This?

The Knowledge Graph Plugin helps you manage an **emergent taxonomy** in FOAM-based knowledge graphs. Unlike traditional taxonomy systems that enforce rigid structures upfront, this plugin:

- **Observes** actual tag usage patterns
- **Identifies** vestigial tags and consolidation opportunities
- **Suggests** tags based on existing patterns
- **Maintains** taxonomy health through periodic gardening

### Problem It Solves

**Before:**
- Tags applied incrementally during file cleanup
- No visibility into tag sprawl (100 tags, 70 used once)
- Manual grep/search to find patterns
- No consolidation path for duplicate tags

**After:**
- Weekly taxonomy snapshots show health at a glance
- Auto-detect vestigial tags for pruning
- Data-driven consolidation recommendations
- Living registry tracks blessed/deprecated tags

### Not For You If...

- You want rigid taxonomy enforcement (this is permissive)
- You prefer upfront taxonomy design (this is emergent)
- You work solo with <20 files (overhead not worth it)

### Perfect For You If...

- Multiple contributors working async
- Tags applied incrementally, not systematically
- Need visibility without blocking contributors
- Want data-driven consolidation decisions

---

## Philosophy

### Design Principles

**1. Garden, Don't Architect**
```
Taxonomy is a living system. New growth is normal.
Prune periodically. Don't enforce rigid structure.
```

**2. Observe, Then Act**
```
Watch actual usage patterns emerge.
Make decisions based on data, not assumptions.
```

**3. Permissive by Default**
```
New tags are fine. Contributors aren't blocked.
Clean up weekly, not daily.
```

**4. Reversible Everything**
```
All changes logged in changelog.
Can roll back any consolidation.
```

**5. Progressive Disclosure**
```
v0.1: Just observation (safe, read-only)
v0.2: Add governance (prune, merge)
v0.3: Add real-time guidance (suggestions)
```

### The Weekly Ritual

**"Taxonomy Garden Hour" - 15 minutes every Monday**

```bash
# 1. Health check
/taxonomy-snapshot

# 2. Review vestigial tags (v0.2+)
/taxonomy-prune --dry-run

# 3. Consolidate duplicates (v0.2+)
/taxonomy-merge old-tag new-tag

# 4. Commit changes
git add taxonomy-registry.yml taxonomy-changelog.md
git commit -m "Weekly taxonomy maintenance"
```

**Time:** 15 min/week
**Impact:** Prevents runaway sprawl, maintains health

---

## Installation

### Prerequisites

- Claude Code CLI installed
- FOAM-based knowledge graph (markdown files with YAML frontmatter)
- Python 3.9+ (for analysis scripts)
- Git (for tracking changes)

### Current Status (v0.1)

The plugin is already in your repo at:
```
05_apps/knowledge-graph-plugin/
```

**To use:**
```bash
# Ensure scripts are executable
chmod +x 05_apps/knowledge-graph-plugin/scripts/*.py

# Run commands directly
python 05_apps/knowledge-graph-plugin/scripts/scan_taxonomy.py
```

---

## Quick Start

### Step 1: Establish Baseline

Generate your first taxonomy snapshot:

```bash
cd /path/to/knowledge-graph
python 05_apps/knowledge-graph-plugin/scripts/scan_taxonomy.py
```

**Output:**
- `CURRENT_TAXONOMY_SNAPSHOT.md` - Full analysis
- `taxonomy-registry.yml` - Auto-generated registry
- Console summary

### Step 2: Review Snapshot

Open `CURRENT_TAXONOMY_SNAPSHOT.md` and review:

- **Tag frequency distribution** - Which tags are actually used?
- **Tag co-occurrence patterns** - Which tags appear together?
- **Vestigial candidates** - Single-use tags >30 days old
- **Domain coverage** - % compliance with domain tags

### Step 3: Weekly Maintenance (Manual for v0.1)

**Every Monday:**

1. Run scan again to see changes:
   ```bash
   python scripts/scan_taxonomy.py --compare=previous
   ```

2. Review growth/shrinkage:
   - New tags added this week?
   - Any tags becoming vestigial?
   - Consolidation opportunities?

3. Manually edit `taxonomy-registry.yml` to bless/deprecate tags

4. Commit changes:
   ```bash
   git add taxonomy-registry.yml CURRENT_TAXONOMY_SNAPSHOT.md
   git commit -m "Weekly taxonomy maintenance"
   ```

---

## Commands Reference

### v0.1 (Current - Manual Execution)

#### `scan_taxonomy.py`

**Purpose:** Generate comprehensive taxonomy snapshot

**Usage:**
```bash
python scripts/scan_taxonomy.py [options]

Options:
  --output=snapshot    # Generate CURRENT_TAXONOMY_SNAPSHOT.md
  --output=registry    # Generate taxonomy-registry.yml
  --output=both        # Generate both (default)
  --domains=<list>     # Comma-separated domains to scan
  --format=md|json     # Output format (default: md)
```

**Examples:**
```bash
# Full scan with snapshot + registry
python scripts/scan_taxonomy.py

# Scan only customer domain
python scripts/scan_taxonomy.py --domains=customer

# Output as JSON for scripting
python scripts/scan_taxonomy.py --format=json > snapshot.json
```

**Output Files:**
- `CURRENT_TAXONOMY_SNAPSHOT.md` - Human-readable analysis
- `taxonomy-registry.yml` - Machine-readable registry
- Console: Summary stats

---

## Agents Reference

### Taxonomy Observer Agent

**File:** `agents/taxonomy_observer.md`

**Purpose:** Read-only analysis of taxonomy patterns

**Capabilities:**
- Extract tag usage from frontmatter
- Calculate frequency distributions
- Detect co-occurrence patterns
- Identify vestigial candidates
- Generate health reports

**Invocation:**
```
User: "Analyze the taxonomy health of customer domain"
Agent: Uses taxonomy_observer to scan and report
```

**Tools:** Read, Grep, Glob (read-only)

---

## Architecture

### Directory Structure

```
05_apps/knowledge-graph-plugin/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
│
├── agents/
│   ├── taxonomy_observer.md     # Read-only analysis agent
│   ├── navigation_agent.md      # Graph navigation
│   ├── taxonomy_enforcement_agent.md
│   ├── plugin_marketplace_expert.md
│   ├── plugin_design_strategist.md
│   └── PLUGIN_DESIGN_FRAMEWORK.md
│
├── commands/
│   └── [v0.2+ commands]
│
├── scripts/
│   ├── scan_taxonomy.py         # ← v0.1: Main analysis script
│   └── check_domain_tags.py     # Legacy domain tag checker
│
├── data/
│   ├── taxonomy-registry.yml    # Blessed/deprecated tags
│   └── taxonomy-changelog.md    # Evolution tracking
│
├── README.md                    # ← This file
├── CURRENT_TAXONOMY_SNAPSHOT.md # Latest baseline
└── CHANGELOG.md                 # Plugin version history
```

### Data Flow (v0.1)

```
┌─────────────────────────────────────────────────────────────┐
│ 1. SCAN                                                      │
│    python scripts/scan_taxonomy.py                          │
│    → Reads all .md files in 00-03 domains                  │
│    → Extracts YAML frontmatter                             │
│    → Parses tags: arrays                                    │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. ANALYZE                                                   │
│    → Count tag frequency                                     │
│    → Calculate co-occurrence (which tags appear together)   │
│    → Detect vestigial tags (single-use, old)               │
│    → Identify domain tag compliance                         │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. OUTPUT                                                    │
│    → CURRENT_TAXONOMY_SNAPSHOT.md (human-readable)         │
│    → taxonomy-registry.yml (machine-readable)              │
│    → Console summary                                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Roadmap

### v0.1: OBSERVATION ✅ (Current)

**Ship Date:** 2025-10-12

**Features:**
- ✅ `scan_taxonomy.py` - Comprehensive analysis script
- ✅ `CURRENT_TAXONOMY_SNAPSHOT.md` - Baseline report
- ✅ `taxonomy-registry.yml` - Auto-generated registry
- ✅ Tag frequency analysis
- ✅ Co-occurrence detection
- ✅ Vestigial tag identification

**Success Metric:**
"Run scan weekly, identify 3+ consolidation opportunities in first month"

---

### v0.2: GOVERNANCE (Target: 2025-10-26)

**Features:**
- `/taxonomy-snapshot` - CLI command
- `/tag-history <tag>` - Usage over time
- `/taxonomy-prune` - Remove vestigial tags
- `/taxonomy-merge <old> <new>` - Consolidate duplicates
- `/taxonomy-bless <tag>` - Mark as standard

**Success Metric:**
"Reduce tag variants by 40% (100 → 60)"

---

### v0.3: GUIDANCE (Target: 2025-11-09)

**Features:**
- `/suggest-tags` - Analyze file, recommend tags
- PreToolUse[Write] hook - Suggest tags on file creation
- Auto-detect tag drift

**Success Metric:**
"95% of new files use standard tags"

---

## Troubleshooting

### Script fails with "No module named..."

**Solution:** Install Python dependencies (create requirements.txt first)

---

### "No .md files found"

**Solution:** Run from repo root:
```bash
cd /path/to/Pixee
python 05_apps/knowledge-graph-plugin/scripts/scan_taxonomy.py
```

---

### Tags not detected in files

**Debug:** Check YAML frontmatter format:
```yaml
# Correct format
tags:
  - tag1
  - tag2

# Wrong format (won't parse)
tags: tag1, tag2
```

---

## FAQ

### Will this enforce taxonomy on contributors?

**A:** No. v0.1 is read-only observation. v0.3 will suggest tags but never block file creation.

### How often should I run the scan?

**A:** Weekly is ideal. Daily is overkill unless you have 50+ contributors.

### Can I roll back a merge?

**A:** Yes. All changes logged in `taxonomy-changelog.md`. Use git history to revert.

---

## License

Internal use only (for now). Will be open-sourced upon public distribution.

---

## Credits

**Design Framework:** Jeff Dean + John Carmack principles
**Maintainer:** Pixee GTM Team

---

**Last Updated:** 2025-10-12
**Plugin Version:** 0.1.0
**Status:** Production Ready (Observation Phase)
