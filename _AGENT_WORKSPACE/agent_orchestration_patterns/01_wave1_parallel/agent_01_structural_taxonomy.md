# Agent 01: Structural Taxonomy Extractor

**Parallel Extraction Agent - Wave 1**

---

## Objective

Extract directory structure patterns, naming conventions, domain boundaries, and file organization principles across three case studies to build a reusable structural taxonomy for context engineering projects.

---

## Input Corpus


### Case Study 2: Recur/Statii (GTM Pipeline)
- **Path**: `gtm_engagements/02_warm_lead/recur_software_role/`
- **Size**: 165MB, 43 markdown + 3,141 LOC Python
- **Pattern Hypothesis**: Research docs + apps/ code separation, data staging pipeline

### Case Study 3: Pixee AI (Context Graph)
- **Path**: `gtm_engagements/03_active_client/pixee_ai_gtm/`
- **Size**: 173MB, 213+ markdown files
- **Pattern Hypothesis**: Domain-based (00-06) + _system meta-layer

---

## Analysis Tasks

### Task 1: Directory Hierarchy Mapping

**Objective**: Document tree structure, depth, branching factor, naming patterns

**Method**:
1. Generate directory tree for each case (max depth 4)
2. Calculate hierarchy metrics:
   - Max depth (how many levels deep)
   - Branching factor (avg subdirectories per parent)
   - Leaf-to-branch ratio (files vs directories)
3. Identify naming patterns:
   - Numeric prefixes (00_, 01_, 02_)
   - Functional names (docs/, apps/, research/)
   - Phase names (foundation/, discovery/, synthesis/)

**Output Section**: `directory_hierarchy_patterns`

**Deliverable**:
```markdown
## [Tool] Directory Hierarchy
- Max depth: 3
- Branching factor: 4.2 avg
- Naming: Functional (agents/, research/, routing/, context/)
- Pattern: Separation by agent role

## Recur Directory Hierarchy
- Max depth: 4
- Branching factor: 3.1 avg
- Naming: Mixed (docs/, apps/, research/, scoping/)
- Pattern: Research vs execution layer separation

## Pixee Directory Hierarchy
- Max depth: 5
- Branching factor: 5.8 avg
- Naming: Numeric prefixes (00-06) + _system
- Pattern: Domain-based with meta-layer
```

---

### Task 2: Domain Boundary Analysis

**Objective**: Identify conceptual domain separations (foundation vs execution vs archive)

**Method**:
1. Map directories to conceptual domains:
   - **Foundation**: Strategic, rarely-changing context
   - **Research**: Investigation, discovery, analysis
   - **Synthesis**: Frameworks, consolidation
   - **Execution**: Implementation, code, apps
   - **Archive**: Historical, disposal candidates
2. Identify boundary markers:
   - Directory names (00_foundation/, 04_archive/)
   - README.md descriptions
   - File movement patterns (from active → archive)

**Output Section**: `domain_boundary_analysis`

**Deliverable**:
```markdown
## Domain Taxonomy


### Recur Domains
- Research: docs/01_research/ (7 agent reports)
- Execution: apps/src/ (Python ETL)
- Data Staging: apps/data/ (raw/, normalized/, enrichment_pilot/)
- Scoping: scoping/ (requirements, proposals)

### Pixee Domains
- Foundation: 00_foundation/ (strategic context)
- Discovery: 01_customer/, research/
- Synthesis: 02_synthesis/ (frameworks)
- Execution: 03_execute/, 05_apps/, 06_apps/
- Validation: 03_validation/ (testing results)
- Archive: 04_archive/ (disposal candidates)
- Meta-System: _system/ (graph maintenance agents)
```

---

### Task 3: File Organization Principles

**Objective**: Extract organizing principles (chronological, functional, domain-based)

**Method**:
1. Analyze file naming conventions:
   - Chronological: dates, version numbers, iteration markers
   - Functional: agent_01_, spec_, report_
   - Domain: product_, customer_, competitive_
2. Identify organization philosophy:
   - **Time-based**: Files organized by when created (meeting notes, iterations)
   - **Function-based**: Files organized by what they do (agents/, scripts/)
   - **Domain-based**: Files organized by subject matter (customer/, product/)
3. Document file lifecycle patterns:
   - Creation location (where new files start)
   - Migration paths (from draft → final → archive)

**Output Section**: `file_organization_principles`

**Deliverable**:
```markdown
## Organization Philosophy Comparison


### Recur: Layer-Based
- Primary axis: Research vs Execution (docs/ vs apps/)
- Secondary axis: Data stage (raw/ → normalized/ → enrichment/)
- Lifecycle: Research static, data flows through stages

### Pixee: Domain-Based with Temporal Overlay
- Primary axis: Information domain (00-06 directories)
- Secondary axis: Subdomain (within each 0X directory)
- Lifecycle: Active → consolidation → archive (via refactor agents)
```

---

### Task 4: Front Matter Schema Analysis

**Objective**: Extract YAML front matter patterns, metadata schemas

**Method**:
1. Scan all markdown files for front matter
2. Extract common fields across cases:
   - Pixee GTM agents: name, description, model, color
   - [Tool] agents: (check for front matter usage)
   - Recur: (check for front matter usage)
3. Identify metadata purposes:
   - Agent routing (which agent to invoke)
   - Display formatting (color, icons)
   - Lineage tracking (created_date, source, parent)
   - Classification (tags, categories, domain)

**Output Section**: `front_matter_schema_comparison`

**Deliverable**:
```markdown
## Front Matter Schemas

### Pixee GTM Agents (.claude/agents/)
```yaml
---
name: COMPANY FOUNDATION RESEARCH
description: Extract verifiable facts about a target company...
model: inherit
color: green
---
```
Fields: name, description, model, color
Purpose: Agent configuration for Claude Code


### Recur Agents
[Scan recur_software_role/docs/*.md for front matter]
Fields: [TBD based on scan]
Purpose: [TBD]

## Metadata Design Patterns
- **Agent Configuration**: name, description, model (for tool integration)
- **Lineage Tracking**: created_date, source, parent (for attribution)
- **Classification**: tags, domain, category (for navigation)
```

---

### Task 5: Wikilink & Reference Graph Topology

**Objective**: Map internal linking patterns, graph structure

**Method**:
1. Extract wikilinks: `[[file_name]]` or `[[folder/file]]`
2. Extract markdown links: `[text](path/to/file.md)`
3. Build graph:
   - Nodes = files
   - Edges = links/references
4. Calculate topology metrics:
   - Clustering coefficient (how interconnected)
   - Centrality (which files are most-referenced)
   - Isolated nodes (orphaned files)
5. Identify hub documents (high centrality)

**Output Section**: `wikilink_graph_topology`

**Deliverable**:
```markdown
## Linking Patterns


### Recur Case Study
- Wikilink usage: [Count] instances
- Hub documents: [Most-referenced files]
- Cross-layer links: Research → Code references
- Topology: [Pattern]

### Pixee Case Study
- Wikilink usage: [Count] instances (expected high due to graph architecture)
- Hub documents: 00_foundation/ files (hypothesis)
- Domain coupling: How often files link across domains (00 → 01 → 02)
- Topology: Domain graph with cross-links

## Graph Topology Insights
- **Recur**: [Topology type] - optimized for [purpose]
- **Pixee**: [Topology type] - optimized for [purpose]
```

---

## Output Contract

**File**: `meta_analysis/agent_orchestration_patterns/03_outputs/wave1/structural_taxonomy_report.md`

**Required Sections**:
1. `directory_hierarchy_patterns` (Task 1)
2. `domain_boundary_analysis` (Task 2)
3. `file_organization_principles` (Task 3)
4. `front_matter_schema_comparison` (Task 4)
5. `wikilink_graph_topology` (Task 5)
6. `reusable_structure_templates` (synthesis of patterns)
7. `decision_framework` (when to use each pattern)

**Deliverable**: Reusable directory structure templates for future projects

---

## Execution Protocol

### Step 1: Data Collection
- Generate directory trees (`find` commands, max depth 4)
- Extract all front matter (grep for `---` blocks)
- Extract all wikilinks and markdown references
- Calculate file/directory counts

### Step 2: Pattern Analysis
- Compare hierarchy metrics across cases
- Map domain boundaries via directory naming
- Classify organization philosophy (time/function/domain)
- Analyze front matter schemas
- Build reference graphs

### Step 3: Synthesis
- Identify common patterns across all 3 cases
- Document case-specific variations
- Create reusable templates for each pattern
- Build decision framework (when to use which structure)

### Step 4: Quality Validation
- [ ] All 5 analysis tasks completed
- [ ] Metrics calculated (depth, branching, centrality)
- [ ] Patterns compared across all 3 cases
- [ ] Templates are actionable (can implement in new project)
- [ ] Decision framework addresses key questions

---

## Success Criteria

**Completeness**:
- ✅ All 3 case studies analyzed
- ✅ All 5 tasks completed with concrete findings
- ✅ Quantitative metrics provided (not just qualitative)

**Actionability**:
- ✅ Reusable templates created for each structural pattern
- ✅ Decision framework helps choose pattern for new project
- ✅ Examples from real case studies illustrate each pattern

**Insight Quality**:
- ✅ Non-obvious patterns identified (not just surface-level observation)
- ✅ Patterns explain WHY structure chosen (not just WHAT structure is)
- ✅ Anti-patterns documented (what to avoid)

---

## Estimated Execution Time

- Data collection: 10 minutes
- Pattern analysis: 20 minutes
- Synthesis & documentation: 15 minutes
- **Total**: 30-45 minutes

---

## Next Agent Dependency

**Independence**: This agent has NO dependencies on other Wave 1 agents (true parallel execution)

**Downstream**: Agent 06 (Meta-Synthesis) will use this output to build unified pattern library
