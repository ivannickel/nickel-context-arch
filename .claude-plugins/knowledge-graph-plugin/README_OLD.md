# Pixee Knowledge Graph Plugin

**Claude Code plugin for governance, navigation, and automation of FOAM-based knowledge graph architecture**

Version: 0.1.0

---

## Overview

This plugin transforms Pixee's knowledge graph from a manual maintenance burden into an actively governed, self-correcting intelligence system. It provides specialized agents, slash commands, and hooks that enforce taxonomy standards, automate linking, validate frontmatter, and enable intelligent navigation.

### Key Features

✅ **Automated Compliance** - Hooks enforce taxonomy standards on every file operation
✅ **Intelligent Navigation** - Agents understand hub-and-spoke architecture for quick discovery
✅ **Smart Validation** - Real-time frontmatter checking against YAML standards
✅ **Graph Health Monitoring** - Continuous quality assessment and reporting
✅ **Cross-Domain Intelligence** - Navigate seamlessly across foundation, customer, content, execute domains

---

## Installation

### Local Development (Current Setup)

The plugin is already scaffolded in your repo at:
```
05_apps/knowledge-graph-plugin/
```

To activate it in Claude Code, you'll need to configure it as a local plugin (instructions coming in Phase 2).

### Future: Distribution via Marketplace

Once stable, this plugin will be published to a separate repo and installable via:
```bash
/plugin install github.com/yourusername/pixee-knowledge-graph-plugin
```

---

## Components

### Agents (`agents/`)

#### **Navigation Agent** (`navigation_agent.md`)
Specialized agent for finding documents across the knowledge graph using hub-and-spoke architecture.

**Capabilities:**
- Query by domain, persona, topic, or pain point
- Navigate via Tier 1 & 2 hub documents
- Suggest related documents based on context
- Identify orphaned or weakly-linked content

**Example Usage:**
- "Find all content about CISO pain points"
- "What strategy docs should inform this campaign?"
- "Show me customer calls about financial services"

#### **Taxonomy Enforcement Agent** (`taxonomy_enforcement_agent.md`)
Validates and enforces YAML frontmatter standards, metadata compliance, and linking requirements.

**Capabilities:**
- Validate YAML frontmatter completeness
- Enforce required fields (name, domain, tags, topics)
- Check minimum linking requirements (3+ related_docs, 1+ Tier 1 hub)
- Verify field formatting (lowercase-with-hyphens, ALL_CAPS)

**Example Usage:**
- Automatic validation on file creation/edit via hooks
- Manual validation via `/validate-frontmatter` command

---

### Commands (`commands/`)

#### `/validate-frontmatter`
Check current file's YAML frontmatter against taxonomy standards.

**Checks:**
- Required fields presence
- Domain tag inclusion (CRITICAL for Foam color-coding)
- Linking requirements (3+ docs, 1+ Tier 1 hub)
- Topic/persona counts
- Field value formatting

**Output:** Specific corrections with examples

---

#### `/navigate-to-hub`
Quick navigation menu to jump to Tier 1 & 2 hub documents.

**Tier 1 Hubs (Foundation):**
1. comprehensive_market_and_customer_intelligence_context.md
2. MEDDPICC_and_Personas.md
3. condensed_positioning.md
4. CLAUDE.md

**Tier 2 Hubs (Domain-Specific):**
5. All Call Summaries.md
6. content_strategy_master.md
7. Campaign_Messaging_and_Value_Propositions.md

---

#### `/graph-health`
Run comprehensive health check on knowledge graph structure.

**Health Checks:**
- Orphaned documents (no incoming links)
- Frontmatter completeness (% with valid YAML)
- Hub connectivity (all domains → Tier 1 hubs)
- Broken wiki-links
- Archive exclusion (.foamignore compliance)

**Output:** Health score (0-100) + critical issues + recommendations

---

#### `/add-frontmatter`
Generate and add compliant YAML frontmatter to current document.

**Process:**
1. Infer domain from file path
2. Suggest file_type based on content
3. Extract probable personas and topics
4. Recommend related_docs (always includes 1+ Tier 1 hub)
5. Generate complete YAML block per template

**Output:** YAML-ready frontmatter for user approval

---

### Hooks (`hooks/hooks.json`)

Automated quality gates that trigger on file operations:

#### **PreToolUse Hooks**
- `Write` → Validate new markdown files have frontmatter
- `Edit` → Check for broken wiki-links before editing

#### **PostToolUse Hooks**
- `Write` → Update graph index after file creation

#### **SessionStart Hooks**
- Quick graph health check on session start

---

## Architecture

### Knowledge Graph Structure

```
00_foundation/     # Strategic intelligence (WHAT & WHO)
├── Tier 1 Hubs    # Most connected strategic documents
└── Brand standards, positioning, buyer intelligence

01_customer/       # Customer intelligence & validation
├── Tier 2 Hub     # All Call Summaries
└── Call transcripts, pain analysis, vertical insights

02_content/        # Content strategy & campaigns
├── Tier 2 Hubs    # content_strategy_master, Campaign_Messaging
└── SEO strategy, product launches, influencer partnerships

03_execute/        # Active campaigns & sales enablement
└── SDR playbooks, ad copy, battlecards, execution artifacts

05_apps/           # Agent prompts, workflows, automation
└── Self-contained tools and scripts

07_archive/        # Historical research (excluded from active graph)
```

### Hub-and-Spoke Model

**Tier 1 Hubs** (Foundation) → Most connected, strategic intelligence
**Tier 2 Hubs** (Domain) → Roll-up documents within each domain
**Spokes** → Individual documents that link to hubs

**Navigation Rule:** All documents must link to at least 1 Tier 1 hub

---

## YAML Frontmatter Standards

Every markdown file must start with YAML frontmatter:

```yaml
---
name: DOCUMENT_NAME_IN_CAPS
description: Brief one-sentence description
domain: foundation|customer|content|execute|apps
file_type: # From standard file types list
canonical_source: true|false
last_updated: YYYY-MM-DD

tags:
  - foundation|customer|content|execute|apps  # REQUIRED domain tag
  - function-tag-1
  - function-tag-2

personas:
  - ciso
  - vp-engineering

topics:
  - vulnerability-remediation
  - backlog-management
  - merge-rate

related_docs:
  - "[[tier-1-hub-document]]"
  - "[[related-doc-1]]"
  - "[[related-doc-2]]"
---
```

### Critical Requirements

1. **Domain tag in `tags:` array** - Required for Foam color-coding
2. **Minimum 3 `related_docs`** - With at least 1 Tier 1 hub
3. **3-7 topics** - From universal topics library
4. **2+ personas** - For customer/content domains

---

## Development Roadmap

### ✅ Phase 1: Foundation (Current)
- [x] Plugin structure scaffolded
- [x] Navigation agent created
- [x] Taxonomy enforcement agent created
- [x] Basic commands implemented
- [x] Hooks configuration defined

### 🔄 Phase 2: Python Scripts (Next)
- [ ] `validate_new_file.py` - Frontmatter validation
- [ ] `check_broken_links.py` - Wiki-link verification
- [ ] `update_graph_index.py` - Graph index maintenance
- [ ] `graph_health_check.py` - Comprehensive health assessment

### 📋 Phase 3: Integration
- [ ] Test plugin activation in Claude Code
- [ ] Configure local plugin loading
- [ ] Test hooks with actual file operations
- [ ] Refine agent prompts based on usage

### 🚀 Phase 4: Distribution
- [ ] Create separate distribution repo
- [ ] Add comprehensive README for public use
- [ ] Publish to Claude Code marketplace
- [ ] Setup versioning and release process

---

## Reference Documents

- **Knowledge Graph Management Guide**: `00_foundation/internal knowledge management guide/KNOWLEDGE_GRAPH_MANAGEMENT_GUIDE.md`
  - Part 1: Content Taxonomy & Topic Categories
  - Part 2: Linking Strategies & Patterns
  - Part 3: Graph Visualization & Configuration
  - Part 7: YAML Metadata Structure & Standards

---

## Contributing

This plugin is currently in active development for Pixee's internal use. Contributions should follow the taxonomy standards defined in the Knowledge Graph Management Guide.

---

## License

Internal use only (for now). Will be open-sourced upon public distribution.

---

**Maintainer:** Pixee GTM Team
**Last Updated:** 2025-10-11
