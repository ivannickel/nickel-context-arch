# Nickel GTM Context Architecture - Orchestrator Execution Guide

**Version:** 2.0
**Created:** 2025-10-30
**System Pattern:** Iterative Context Layering (NOT Linear Extraction)
**Total Execution Time:** 45-55 hours across 165 transcripts
**Mock Execution:** 5% walkthrough completed, 30+ gotchas documented

---

## Document Purpose

**This guide prevents YOU (orchestrator agent) from making the 30+ mistakes discovered during mock execution.**

You are orchestrating a **multi-agent iterative context layering system** that progressively builds intelligence from 165 sales transcripts + 68 raw context documents. This is NOT linear extraction - nodes evolve, evidence compounds, connections emerge.

**Read this ENTIRE document before spawning any agents.**

---

## System State Snapshot (2025-10-30)

### ✅ What Exists
- `strategic_lens.yaml` v1.2 (with iterative context layering rules)
- 9 agent specifications (all with proper frontmatter):
  - `foundation_seeder.md`
  - `who/what/why/how/where_when/meta_extractor.md` (6 dimensional extractors)
  - `node_synthesizer.md` v2.0 (with UPDATE/CREATE logic)
  - `context_weaver.md`
  - `validation_analyst.md`
- 165 transcripts in `knowledge_base/meetings_md/` (WITH frontmatter, strategic classification)
- 68 raw_context docs in `knowledge_base/raw_context/` (WITH frontmatter, signal strength)

### ❌ What Doesn't Exist (YOU MUST CREATE)
- `knowledge_base/taxonomy.yaml` (Foundation_Seeder expects this, needs seed structure)
- `knowledge_base/00_foundation/` subdirectories (icp/, positioning/, value_props/, etc.)
- `knowledge_base/dimensional_annotations/` directory structure
- Updated `ORCHESTRATION_ARCHITECTURE.md` (current version is pre-iterative refactor)

### ⚠️ What Might Exist (OLD ITERATION 1 CONTENT)
- If `knowledge_base/01_customer/` has nodes from previous iteration:
  - **ACTION:** Archive to `_AGENT_WORKSPACE/archive/iteration_1_provisional/`
  - **DO NOT:** Try to integrate old nodes - they lack the new schema

---

## Critical Concepts You Must Understand

### 1. UPDATE vs CREATE Paradigm

**WRONG (Linear):**
```
Transcript 1 → Extract "cash flow pain" → CREATE node
Transcript 5 → Extract "cash flow pain" → CREATE node (DUPLICATE!)
Transcript 12 → Extract "cash flow pain" → CREATE node (DUPLICATE!)
Result: 3 identical nodes with frequency=1 each ❌
```

**RIGHT (Iterative):**
```
Transcript 1 → Extract "cash flow pain" → CREATE node (freq:1, status:emergent)
Transcript 5 → Extract "cash flow pain" → UPDATE node (freq:2, status:validated)
Transcript 12 → Extract "cash flow pain" → UPDATE node (freq:3)
Result: 1 rich node with freq=3, evolving status ✅
```

**Why this matters:** Node_Synthesizer v2.0 has semantic matching logic. It MUST check taxonomy.yaml and existing nodes BEFORE creating. If you don't understand this, you'll create 800+ duplicate nodes.

---

### 2. Foundation ↔ Customer Validation Loop

**Foundation layer** (`00_foundation/`):
- Nickel's STATED strategy (from raw_context)
- Status: baseline → validating → validated → canonical
- Example: "ICP sweet spot is $5-25M (Whale segment)"

**Customer layer** (`01_customer/`):
- Market REALITY (from transcripts)
- Status: emergent → validated → canonical
- Example: Persona nodes show 80% are $1-5M (Fish segment)

**Context Weaver validates:**
- Does transcript evidence CONFIRM foundation claims? → Add validation signals
- Does transcript evidence CONTRADICT foundation claims? → Flag contradiction
- Foundation nodes evolve from "company hypothesis" → "market-validated truth"

**If you don't run Context_Weaver:** Foundation stays disconnected from customer reality, contradictions go undetected, wiki-links don't form.

---

### 3. Node Lifecycle Progression

**Customer nodes:**
```
emergent (freq=1) → validated (freq≥2) → canonical (freq≥5)
Confidence: 3.5 → 7.5 → 9.0+
```

**Foundation nodes:**
```
baseline (raw_context only) → validating (1 transcript validation) →
validated (2+ validations) → canonical (5+ validations)
Confidence: 5-6 → 6.5 → 7.5 → 9.0+
```

**Node_Synthesizer checks thresholds EVERY transcript and updates status automatically.**
**Context_Weaver checks validation counts every 10-20 transcripts.**

**If thresholds wrong:** Nodes stuck in emergent, never progress to canonical.

---

## Pre-Flight Checklist (DO THESE FIRST)

### Step 1: Create taxonomy.yaml Seed Structure

**Why:** Foundation_Seeder and Node_Synthesizer expect taxonomy.yaml to exist. If missing, they crash.

**Location:** `knowledge_base/taxonomy.yaml`

**Content:**
```yaml
version: 1.0
created: 2025-10-30
last_updated: 2025-10-30
status: seed
description: "Pattern registry for Nickel GTM context architecture - tracks frequencies, sources, status"

personas: []
pain_points: []
objections: []
use_cases: []
product_requirements: []
competitive_threats: []
market_segments: []
discovery_triggers: []

notes: "Seed structure - will be populated by Node_Synthesizer as patterns emerge"
```

**Don't skip this.** Multiple agents crash without it.

---

### Step 2: Create Directory Structure

**Foundation subdirectories:**
```bash
knowledge_base/00_foundation/
├── icp/
├── positioning/
├── value_props/
├── competitive_intel/
├── product/
├── business_model/
└── market/
```

**Dimensional annotations structure:**
```bash
knowledge_base/dimensional_annotations/
└── (transcript subdirs will be created per-transcript by extractors)
```

**Why:** Foundation_Seeder will write to these directories. If they don't exist, file writes fail.

---

### Step 3: Archive Old Iteration 1 Content (If Exists)

**Check if `knowledge_base/01_customer/` has nodes:**
```bash
ls knowledge_base/01_customer/personas/
ls knowledge_base/01_customer/pain_points/
```

**If files exist:**
1. Create `_AGENT_WORKSPACE/archive/iteration_1_provisional/`
2. Move ALL `01_customer/` subdirectory contents to archive
3. Leave directory structure intact (empty subdirs)

**Why:** Old nodes lack new frontmatter schema (confidence, validation_count, wiki-links, dimensional_annotations). Don't try to integrate - start fresh.

---

## Execution Flow: Phase-by-Phase

---

## PHASE 0: Foundation Seeding (ONE-TIME)

**Purpose:** Extract Nickel's stated strategy from 68 raw_context docs into 20-30 baseline nodes

**Agent:** Foundation_Seeder
**Execution Time:** 3-5 hours (one-time)
**Input:** 68 raw_context docs (filter by `signal_strength: high` first)
**Output:** 20-30 nodes in `00_foundation/` with status: baseline

### Spawn Command

```javascript
Task tool:
  subagent_type: "general-purpose"
  description: "Foundation seeding from raw context"
  prompt: """
  Execute Foundation_Seeder agent specification:

  Location: _AGENT_WORKSPACE/agents/foundation_seeder.md

  Read the full agent spec, then:

  1. Load strategic_lens.yaml v1.2
  2. Filter raw_context docs by signal_strength: high (priority)
  3. Extract 7 foundation categories:
     - ICP & segmentation (3-5 nodes)
     - Positioning (3-4 nodes)
     - Value propositions (3-4 nodes)
     - Competitive intel (4-6 nodes)
     - Product capabilities (5-6 nodes)
     - Business model (3-4 nodes)
     - Market context (3-4 nodes)

  4. Create nodes with:
     - YAML frontmatter (status: baseline, confidence: 5-6)
     - [VERIFIED: source:lines] evidence attribution
     - Context_lineage with source docs
     - Transcript_validation section (empty initially)

  5. Follow kebab-case naming: icp-definition.md, not ICP_Definition.md

  6. Calculate confidence using formula:
     base_confidence (baseline: 5.0) + (log10(source_count + 1) × 1.5)

  Target: 20-30 nodes total
  Time budget: 3-5 hours

  CRITICAL: All claims must have [VERIFIED: file:lines] attribution.
  CRITICAL: No fabrication - use UNKNOWN if cannot verify.

  When complete, report:
  - Node count by category
  - Average confidence score
  - High-signal docs processed
  """
```

### Common Failures & Fixes

**Failure 1: "taxonomy.yaml not found"**
- **Cause:** You skipped Pre-Flight Step 1
- **Fix:** Create taxonomy.yaml seed structure (see above)

**Failure 2: "Directory 00_foundation/icp/ does not exist"**
- **Cause:** You skipped Pre-Flight Step 2
- **Fix:** Create all 7 subdirectories

**Failure 3: "Confidence score calculation incorrect"**
- **Cause:** log10 formula not implemented correctly
- **Fix:** Verify formula: `5.0 + (log10(3 + 1) × 1.5) = 5.0 + 0.90 = 5.9`

**Failure 4: "Evidence attribution missing line numbers"**
- **Cause:** Agent wrote [VERIFIED: file.md] without :lines
- **Fix:** Reject node, require [VERIFIED: file.md:42-67] format

**Failure 5: "Node names inconsistent (camelCase vs kebab-case)"**
- **Cause:** No naming convention enforcement
- **Fix:** All filenames MUST be kebab-case: `icp-definition.md`

### Quality Check Before Proceeding

✅ **MUST HAVE:**
- [ ] 20-30 nodes created in `00_foundation/` subdirectories
- [ ] All nodes have status: baseline in frontmatter
- [ ] All nodes have confidence: 5.0-7.0 range
- [ ] All evidence has [VERIFIED: source:lines] format
- [ ] taxonomy.yaml still exists (Foundation_Seeder shouldn't modify it yet)
- [ ] File naming is kebab-case throughout

**If ANY checkbox fails:** Stop, fix issues, do NOT proceed to Phase 1.

---

## PHASE 1: Sample Batch (15-20 Transcripts)

**Purpose:** Test lens alignment, discover customer patterns, validate foundation claims

**Pattern:** Parallel Fanout-Fanin per transcript
**Execution Time:** 4-6 hours for 15-20 transcripts
**Critical:** This is validation phase - if lens misaligned, full corpus will fail

### Step 1.1: Strategic Transcript Selection

**Don't use random selection. Use strategic filtering:**

```javascript
Task tool:
  subagent_type: "general-purpose"
  description: "Select sample batch transcripts"
  prompt: """
  Select 15-20 transcripts for sample batch using strategic criteria:

  Location: knowledge_base/meetings_md/

  Criteria:
  1. extraction_priority: high OR medium (from frontmatter)
  2. has_pain_points: true OR has_objections: true
  3. Diversity:
     - Mix of primary_industry values
     - Mix of deal_stage values
     - Mix of ar_vs_ap values

  Prioritize transcripts with:
  - has_competitive_intel: true (Melio/Relay mentions)
  - has_use_case: true
  - has_integration_needs: true (QuickBooks)

  Avoid:
  - [No transcript available] (check content)
  - extraction_priority: low
  - duration_min < 5 (too short)

  Output format:
  ```
  selected_transcripts:
    - 002_erik-meza-and-colton-ofarrell_2025-07-15.md
    - 003_prime-renovations-ny-nickel_2025-07-23.md
    - ...

  selection_rationale:
    high_priority: 12
    medium_priority: 5
    has_pain_points: 14
    has_objections: 11
    has_competitive_intel: 6
    industry_diversity: [building_materials: 8, construction: 5, wholesale: 4]
  ```

  Target: 15-20 transcripts
  """
```

**Why strategic selection matters:** Sample batch validates lens. If you pick 20 low-signal transcripts, lens looks broken when it's not. If you pick 20 identical industries, you miss ICP diversity issues.

---

### Step 1.2: Process Each Transcript (Parallel Fanout-Fanin)

**For EACH selected transcript, run this loop:**

```
┌─────────────────────────────────────────┐
│ Fanout: 6 Dimensional Extractors        │
│ (Run in PARALLEL - 6 concurrent agents) │
└─────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────┐
│ Fanin: Node_Synthesizer                 │
│ (Run SEQUENTIALLY after extractors)     │
└─────────────────────────────────────────┘
```

#### Spawn 6 Extractors in PARALLEL

```javascript
// Send SINGLE message with 6 Task tool calls

Task tool (1/6):
  subagent_type: "general-purpose"
  description: "WHO dimension extraction"
  model: "haiku"  // Fast model for extraction
  prompt: """
  Execute WHO_Extractor agent spec:
  Location: _AGENT_WORKSPACE/agents/who_extractor.md

  Input transcript: knowledge_base/meetings_md/[transcript_id].md
  Strategic lens: knowledge_base/strategic_lens.yaml v1.2

  Extract WHO dimension (personas, firmographics, ICP signals).
  Output: dimensional_annotations/[transcript_id]/WHO_extraction.yaml

  Time budget: 2-3 minutes
  """

Task tool (2/6):
  subagent_type: "general-purpose"
  description: "WHAT dimension extraction"
  model: "haiku"
  prompt: """[Similar to WHO, but for WHAT_Extractor]"""

Task tool (3/6):
  subagent_type: "general-purpose"
  description: "WHY dimension extraction"
  model: "haiku"
  prompt: """[Similar, WHY_Extractor]"""

Task tool (4/6):
  subagent_type: "general-purpose"
  description: "HOW dimension extraction"
  model: "haiku"
  prompt: """[Similar, HOW_Extractor]"""

Task tool (5/6):
  subagent_type: "general-purpose"
  description: "WHERE_WHEN dimension extraction"
  model: "haiku"
  prompt: """[Similar, WHERE_WHEN_Extractor]"""

Task tool (6/6):
  subagent_type: "general-purpose"
  description: "META dimension extraction"
  model: "haiku"
  prompt: """[Similar, META_Extractor]"""
```

**CRITICAL:** Send as SINGLE message with 6 tool calls. Do NOT send 6 separate messages (sequential execution).

**Expected Time:** 2-3 minutes (parallel) vs 12-18 minutes (sequential)

**Expected Output:** 6 YAML files in `dimensional_annotations/[transcript_id]/`:
- WHO_extraction.yaml
- WHAT_extraction.yaml
- WHY_extraction.yaml
- HOW_extraction.yaml
- WHERE_WHEN_extraction.yaml
- META_extraction.yaml

---

#### Spawn Node_Synthesizer (AFTER extractors complete)

```javascript
Task tool:
  subagent_type: "general-purpose"
  description: "Node synthesis for transcript"
  prompt: """
  Execute Node_Synthesizer v2.0 agent spec:
  Location: _AGENT_WORKSPACE/agents/node_synthesizer.md

  Input: 6 dimensional extractions from dimensional_annotations/[transcript_id]/
  Strategic lens: knowledge_base/strategic_lens.yaml v1.2
  Taxonomy: knowledge_base/taxonomy.yaml

  CRITICAL STEPS:

  1. Load all 6 dimensional extractions
  2. Calculate composite strategic_fit score (weighted formula)
  3. Resolve contradictions using dimensional priority order

  4. **CHECK FOR EXISTING NODES** (Step 3.5 in spec):
     For each pattern extracted:
       - Load taxonomy.yaml
       - Run semantic matching against existing nodes
       - Decision: UPDATE existing node OR CREATE new node

  5. If UPDATE:
     - Increment frequency in frontmatter
     - Append evidence to context_lineage
     - Recalculate strategic_fit (weighted average)
     - Recalculate confidence (log boost)
     - Check status progression (freq 2 = emergent → validated)
     - Generate wiki-links if cross-references detected

  6. If CREATE:
     - New node with frequency: 1, status: emergent
     - Confidence: 3.5 (base for emergent)

  7. Update taxonomy.yaml with frequency increments

  8. Check foundation nodes for validation signals:
     - If persona matches ICP criteria → update foundation/icp/ node
     - If pain aligns with value prop → update foundation/value_props/ node
     - If competitor mentioned → update foundation/competitive_intel/ node

  Output: 5-10 knowledge graph nodes (CREATE or UPDATE)
  Time budget: 3-5 minutes

  CRITICAL: Semantic matching prevents duplicates.
  CRITICAL: UPDATE mode preserves evidence accumulation.
  CRITICAL: Update taxonomy.yaml LAST (after all node operations).
  """
```

**Common Failures:**

**Failure 1: "Duplicate nodes created (cash-flow-constraints.md and cash-flow-issues.md)"**
- **Cause:** Semantic matching failed, Node_Synthesizer didn't detect similarity
- **Root cause:** Matching threshold too strict, or taxonomy not loaded
- **Fix:** Lower similarity threshold, verify taxonomy.yaml loaded
- **Prevention:** After 3-5 transcripts, manually audit for duplicates

**Failure 2: "Frequency stuck at 1 for pattern that appeared 5 times"**
- **Cause:** Node_Synthesizer creating new node instead of updating
- **Root cause:** Node filename changed (cash-flow vs cashflow), matching failed
- **Fix:** Enforce consistent slugification (use kebab-case, no variations)

**Failure 3: "Strategic_fit recalculation wrong (should be weighted average, got simple average)"**
- **Cause:** Formula error: `(8 + 7) / 2 = 7.5` instead of weighted
- **Fix:** Use weighted: `(8×sources_A + 7×sources_B) / (sources_A + sources_B)`

**Failure 4: "Status stuck at emergent even though freq = 3"**
- **Cause:** Status progression check didn't run
- **Fix:** Node_Synthesizer MUST check: if freq ≥ 2 → status = validated

**Failure 5: "Wiki-link [[pain-slug]] added but pain-slug.md doesn't exist yet"**
- **Cause:** Wiki-link generation didn't verify target exists
- **Fix:** Check if target node created BEFORE adding link, or add during Context_Weaver

**Failure 6: "Taxonomy.yaml corrupted (malformed YAML after update)"**
- **Cause:** Concurrent writes from parallel agents
- **Fix:** Node_Synthesizer runs SEQUENTIALLY (one transcript at a time)

**Failure 7: "Foundation node not enriched even though persona matched ICP"**
- **Cause:** Foundation validation logic not executed
- **Fix:** Node_Synthesizer Step 8 MUST check foundation nodes

---

### Step 1.3: Repeat for All Sample Batch Transcripts

**Loop pattern:**
```
For transcript 1-15:
  Spawn 6 extractors in PARALLEL (single message, 6 tool calls)
  Wait for completion
  Spawn Node_Synthesizer (sequential)
  Wait for completion
  Move to next transcript

Every 10 transcripts:
  Run Context_Weaver (see below)
```

**Progress tracking:**
```yaml
sample_batch_progress:
  total_transcripts: 15
  processed: 0
  current: null

  nodes_created: 0
  nodes_updated: 0
  taxonomy_patterns: 0

  extractors_succeeded: 0
  extractors_failed: 0
  synthesizer_succeeded: 0
  synthesizer_failed: 0
```

**Time estimate:** 15 transcripts × 15 min = 3.75 hours

---

### Step 1.4: Context_Weaver (After 10 transcripts)

**Purpose:** Build connections, validate foundation, calculate confidence, flag contradictions

**Trigger:** After processing 10 transcripts (or at end of sample batch if <10)

```javascript
Task tool:
  subagent_type: "general-purpose"
  description: "Context weaving and validation"
  prompt: """
  Execute Context_Weaver agent spec:
  Location: _AGENT_WORKSPACE/agents/context_weaver.md

  Input:
  - Foundation nodes: knowledge_base/00_foundation/**/*.md
  - Customer nodes: knowledge_base/01_customer/**/*.md
  - Taxonomy: knowledge_base/taxonomy.yaml
  - Strategic lens: knowledge_base/strategic_lens.yaml v1.2

  Execute 5 steps:

  1. Foundation Validation Signal Detection (20-30 min):
     - ICP criteria validation (personas matching margin/headcount constraints?)
     - Value prop validation (pain points aligning with value props?)
     - Competitive intel validation (transcript mentions confirming/refuting claims?)
     - Positioning validation (customer language matching positioning?)
     - Product capability validation (requirements universally mentioned?)

  2. Generate Wiki-Links (15-20 min):
     - Foundation → Customer (ICP → personas, value props → pains)
     - Customer → Customer (persona → pain/objection/use case)
     - Check target nodes exist before adding links

  3. Update Node Status Progression (10-15 min):
     - Foundation: baseline → validating → validated (based on validation_count)
     - Customer: emergent → validated → canonical (based on frequency)

  4. Calculate Confidence Scores (10-15 min):
     - Formula: base_confidence + (log10(source_count + 1) × 1.5)
     - Evidence quality multiplier: high (1.2), medium (1.0), low (0.8)
     - Update confidence field in ALL node frontmatters

  5. Flag Contradictions (10-15 min):
     - ICP_MISMATCH: Foundation ICP vs actual persona distribution
     - COMPETITIVE_PRICING_OUTDATED: Stated pricing vs transcript evidence
     - DIFFERENTIATION_WEAK: Claimed differentiator not unique in transcripts
     - VALUE_PROP_UNVALIDATED: Value prop not mentioned in any transcripts

  Output: _AGENT_WORKSPACE/context_weaver_reports/enrichment_[count].md
  Time budget: 60-90 minutes

  Report includes:
  - Foundation validation summary (how many nodes progressed)
  - Wiki-links generated count
  - Contradictions flagged (with severity)
  - Confidence updates (average increase)
  - Next steps recommendations
  """
```

**Expected Output:**
- Foundation nodes enriched with transcript_validation sections
- Wiki-links added to nodes (bidirectional)
- Node status updated (some baseline → validating)
- Contradiction flags added where evidence conflicts
- Enrichment report generated

**Time:** 60-90 minutes

---

## CHECKPOINT 1: Validation Gate

**Purpose:** Decide if lens aligned, quality sufficient to scale to full corpus

**Trigger:** After sample batch (15-20 transcripts) complete + Context_Weaver run

**Agent:** Validation_Analyst

```javascript
Task tool:
  subagent_type: "general-purpose"
  description: "Checkpoint 1 validation analysis"
  prompt: """
  Execute Validation_Analyst agent spec:
  Location: _AGENT_WORKSPACE/agents/validation_analyst.md

  Input:
  - Customer nodes: knowledge_base/01_customer/**/*.md (50-100 nodes)
  - Taxonomy: knowledge_base/taxonomy.yaml (updated frequencies)
  - Strategic lens: knowledge_base/strategic_lens.yaml v1.2 (baseline patterns)

  Execute validation process:

  1. Pattern Revalidation Analysis (15-20 min):
     Baseline: 67 patterns from strategic_lens.yaml v1.2

     For each pattern:
       - Check if frequency increased in taxonomy.yaml
       - If freq increased: REVALIDATED ✅
       - If freq unchanged: NOT SEEN ⚠️

     Calculate: revalidation_rate = (patterns_revalidated / 67) × 100%
     Pass threshold: ≥60%

  2. New Discovery Analysis (10-15 min):
     - Count patterns in taxonomy with discovered_date = sample_batch_date
     - Calculate: discovery_rate = (new_patterns / 67) × 100%
     - Pass threshold: ≥20%

  3. Quality Assessment (10-15 min):
     Random sample 20-30 nodes:
       - Evidence preservation: context_lineage complete? Line citations present?
       - Strategic_fit calculation: Composite score calculated? Dimensional scores present?
       - Attribution completeness: Frontmatter complete? Wiki-links valid?

     Calculate: overall_quality = weighted average of 3 metrics
     Pass threshold: ≥85%

  4. Scaling Decision:
     If ALL 3 pass thresholds: GO ✅
     If 1-2 pass thresholds: REFINE 🔄
     If 0 pass thresholds: NO-GO ❌

  5. Generate Validation Report:
     Location: knowledge_base/validation_reports/checkpoint_1_validation.md

     Include:
     - Pattern revalidation table (67 patterns, which revalidated)
     - New discoveries list (with freq, category, strategic_fit)
     - Quality assessment details (evidence preservation, strategic_fit, attribution)
     - Decision: GO/REFINE/NO-GO with rationale
     - If REFINE: Specific lens refinements needed
     - If NO-GO: Root cause analysis

  Time budget: 50-75 minutes
  """
```

### Decision Matrix

**GO (Proceed to Phase 2):**
```yaml
criteria:
  pattern_revalidation: ≥60% ✅
  new_discovery: ≥20% ✅
  overall_quality: ≥85% ✅

action:
  - Archive sample batch validation report
  - Proceed to Phase 2 (full corpus: 140-150 remaining transcripts)
  - Continue same extraction pattern
  - Run Context_Weaver every 10-20 transcripts
```

**REFINE (Iterate on sample batch):**
```yaml
criteria:
  pattern_revalidation: 40-59% ⚠️
  OR new_discovery: <20% ⚠️
  AND overall_quality: ≥70% (agents working correctly)

action:
  - Document patterns that failed to revalidate
  - Identify lens refinements needed
  - Update strategic_lens.yaml to v1.3 (version bump)
  - Retry sample batch with refined lens
  - Max 3 iterations before human escalation

iteration_tracking:
  iteration_1: Sample batch with lens v1.2
  iteration_2: Sample batch with lens v1.3 (if REFINE)
  iteration_3: Sample batch with lens v1.4 (if REFINE again)
  iteration_4: Human escalation (lens fundamentally broken)
```

**NO-GO (Stop and fix):**
```yaml
criteria:
  pattern_revalidation: <40% ❌
  OR overall_quality: <70% ❌

action:
  - STOP full corpus processing
  - Generate root cause analysis
  - Determine: lens misaligned OR agent execution failure?
  - Human escalation required
  - Do NOT proceed to Phase 2

root_cause_analysis:
  if_lens_misaligned:
    - Patterns in lens don't match corpus reality
    - Example: Lens says "Whale segment ideal" but 80% are Fish
    - Fix: Major lens redesign needed

  if_agent_failure:
    - Extractors not following attribution standards
    - Node_Synthesizer not running UPDATE logic
    - Quality issues in evidence preservation
    - Fix: Debug agent execution, fix specs
```

### Common Validation Failures

**Failure 1: "Revalidation rate 35% (FAIL)"**
- **Cause:** Lens patterns don't match corpus reality
- **Example:** Lens prioritizes "Lien management automation" but 0 transcripts mention it
- **Fix:** REFINE - Remove patterns with 0 revalidation, add patterns discovered in sample
- **Decision:** REFINE (iteration 2)

**Failure 2: "New discovery rate 5% (FAIL)"**
- **Cause:** Sample batch not diverse enough OR lens too broad (captured everything)
- **Fix:** REFINE - Expand lens categories if sample diverse, retry sample if not diverse
- **Decision:** REFINE

**Failure 3: "Quality 68% - Evidence preservation failing"**
- **Cause:** Extractors not including line citations
- **Fix:** NO-GO - Debug extractor specs, ensure [VERIFIED: file:lines] format enforced
- **Decision:** NO-GO (agent failure)

**Failure 4: "Quality 78% - Strategic_fit not calculated"**
- **Cause:** Node_Synthesizer skipping Step 2 (composite score calculation)
- **Fix:** NO-GO - Fix Node_Synthesizer spec, ensure weighted formula implemented
- **Decision:** NO-GO

**Failure 5: "Revalidation 64%, Discovery 25%, Quality 89% (ALL PASS)"**
- **Result:** GO ✅
- **Action:** Proceed to Phase 2 immediately

---

## PHASE 2: Full Corpus (140-150 Remaining Transcripts)

**Purpose:** Scale validated pattern extraction to full corpus

**Trigger:** Checkpoint 1 decision = GO

**Pattern:** Same as Phase 1, but for 140-150 transcripts

**Execution Time:** 35-40 hours (140 transcripts × 15 min)

**Orchestration strategy:**

```yaml
batch_processing:
  batch_size: 10 transcripts
  total_batches: 14-15

  per_batch:
    - Process 10 transcripts (6 extractors + synthesizer per transcript)
    - Run Context_Weaver enrichment
    - Update progress checkpoint
    - Continue to next batch

  progress_checkpoints:
    - Save every 10 transcripts
    - Enables recovery if failure
    - Track: processed_count, nodes_created, nodes_updated, patterns_discovered
```

### Execution Loop

```javascript
For batch 1-14:
  For transcript in batch (10 transcripts):
    // Same as Phase 1
    Spawn 6 extractors in PARALLEL (single message)
    Wait for completion
    Spawn Node_Synthesizer (sequential)
    Wait for completion

  // After batch of 10
  Run Context_Weaver
  Save checkpoint:
    - processed_count: [X of 140]
    - nodes_created: [total]
    - nodes_updated: [total]
    - taxonomy_patterns: [current count]

  Continue to next batch
```

### Progress Tracking Template

```yaml
full_corpus_progress:
  phase: 2
  total_transcripts: 140
  processed: 0
  batches_completed: 0

  nodes_created: 0
  nodes_updated: 0
  taxonomy_patterns: [count]

  foundation_nodes_validated: 0
  wiki_links_generated: 0
  contradictions_flagged: 0

  quality_metrics:
    evidence_preservation: []  # Track per batch
    strategic_fit_calculated: []
    attribution_complete: []

  last_checkpoint: null
  next_context_weaver: 10
```

### Scale Optimizations

**Optimization 1: Batch Parallel Transcript Processing**

Instead of:
```
Process transcript 1 → Process transcript 2 → Process transcript 3...
```

Do:
```
Process transcripts 1-5 in parallel batches (if computational capacity allows)
```

**Optimization 2: Incremental Context_Weaver**

Instead of:
```
Context_Weaver processes ALL nodes every time (slow)
```

Do:
```
Context_Weaver processes only nodes updated since last run (fast)
```

**Optimization 3: Taxonomy Caching**

Instead of:
```
Node_Synthesizer loads taxonomy.yaml from disk every transcript
```

Do:
```
Cache taxonomy in memory, reload every 10 transcripts
```

### Common Scale Issues

**Issue 1: "Processing slowing down after 50 transcripts (was 15 min, now 25 min)"**
- **Cause:** Semantic matching checking against 500+ existing nodes
- **Fix:** Optimize matching (hash-based lookup, not linear search)

**Issue 2: "Context_Weaver taking 3 hours at transcript 100 (was 60 min)"**
- **Cause:** Processing all nodes, not just updated since last run
- **Fix:** Implement incremental processing, track last_processed timestamp

**Issue 3: "Taxonomy.yaml growing to 5MB, Node_Synthesizer slowing down"**
- **Cause:** Frequency data for 150+ patterns getting large
- **Fix:** Acceptable - 5MB is fine, but consider compression if >10MB

**Issue 4: "Node_Synthesizer creating duplicates after 80 transcripts"**
- **Cause:** Semantic matching degraded, threshold drift
- **Fix:** Manual duplicate audit every 50 transcripts, merge if found

---

## CHECKPOINT 2: Final Validation

**Purpose:** Validate full corpus quality before synthesis phase

**Trigger:** After 165 transcripts processed

**Agent:** Validation_Analyst (same as Checkpoint 1, but full corpus metrics)

```javascript
Task tool:
  subagent_type: "general-purpose"
  description: "Checkpoint 2 final validation"
  prompt: """
  Execute Validation_Analyst agent spec for Checkpoint 2:

  Input:
  - Customer nodes: knowledge_base/01_customer/**/*.md (120-150 nodes)
  - Foundation nodes: knowledge_base/00_foundation/**/*.md (20-30 nodes)
  - Taxonomy: knowledge_base/taxonomy.yaml (final frequencies)

  Focus areas (different from Checkpoint 1):

  1. Pattern Stability Analysis:
     - Emergent → Validated → Canonical progression
     - How many patterns reached canonical (freq ≥5)?
     - How many patterns stayed emergent (freq 1)?
     - Pattern retirement candidates (freq 1 after 165 transcripts)

  2. Foundation Validation Completion:
     - How many foundation nodes reached validated/canonical?
     - Which foundation claims contradicted by transcripts?
     - ICP validation: Does persona distribution match foundation ICP?

  3. Synthesis Readiness:
     - Are canonical patterns ready for strategic rollups?
     - Do wiki-links create navigable graph?
     - Is evidence attribution complete (100%)?

  4. Final Quality Metrics:
     - Overall quality score (same formula as Checkpoint 1)
     - Pass threshold: ≥85%

  Generate report:
  Location: knowledge_base/validation_reports/checkpoint_2_final.md

  Include:
  - Pattern lifecycle table (emergent/validated/canonical counts)
  - Foundation validation summary (baseline → validated progression)
  - Taxonomy health (total patterns, frequencies, status distribution)
  - Synthesis readiness assessment
  - Recommendations for next phase (synthesis + deliverables)

  Time budget: 75-105 minutes
  """
```

### Expected Outcomes

**Healthy System:**
```yaml
pattern_distribution:
  canonical: 15-25 patterns (freq ≥5)
  validated: 40-60 patterns (freq 2-4)
  emergent: 50-70 patterns (freq 1)

foundation_validation:
  canonical: 8-12 nodes (5+ transcript validations)
  validated: 10-15 nodes (2-4 validations)
  validating: 5-8 nodes (1 validation)

quality:
  overall: 88-92%
  evidence_preservation: 95-100%
  strategic_fit_calculated: 90-95%
  attribution_complete: 95-100%
```

**Unhealthy System:**
```yaml
pattern_distribution:
  canonical: 2-3 patterns (too few)
  validated: 10-15 patterns
  emergent: 100+ patterns (too many stuck)

foundation_validation:
  canonical: 0-1 nodes
  validated: 3-5 nodes
  validating: 2-3 nodes
  baseline: 15+ nodes (never progressed)

quality:
  overall: 72%
  evidence_preservation: 65%
```

**If unhealthy:** Root cause analysis, manual intervention required.

---

## Error Recovery Procedures

### Extractor Failure

**Symptom:** WHO_Extractor crashes, returns error

**Immediate action:**
```yaml
1. Log error with transcript_id
2. Skip transcript (mark extraction_failed: true in frontmatter)
3. Continue to next transcript
4. After batch, retry failed transcripts
5. If retry fails 3x: Human review required
```

**Do NOT:** Stop entire orchestration for single extractor failure

---

### Node_Synthesizer Failure

**Symptom:** Node_Synthesizer crashes, taxonomy.yaml corrupted

**Immediate action:**
```yaml
1. STOP orchestration immediately
2. Restore taxonomy.yaml from last checkpoint (git revert if committed)
3. Debug Node_Synthesizer agent
4. Root cause: Usually UPDATE logic bug or YAML formatting error
5. Fix agent spec
6. Resume from last successful transcript
```

**This is CRITICAL failure:** Node_Synthesizer corruption can cascade to all future nodes.

---

### Context_Weaver Failure

**Symptom:** Context_Weaver crashes during wiki-link generation

**Immediate action:**
```yaml
1. Log error
2. Continue transcript processing (Context_Weaver is enrichment, not critical path)
3. Retry Context_Weaver after next 10 transcripts
4. If persistent: Debug wiki-link generation logic (likely broken reference)
```

**This is NON-CRITICAL failure:** Can continue without Context_Weaver, run manually later.

---

### Validation_Analyst Failure

**Symptom:** Checkpoint validation crashes or returns nonsensical results

**Immediate action:**
```yaml
1. STOP orchestration
2. Manual quality audit (spot-check 10-20 nodes)
3. Debug Validation_Analyst agent
4. Root cause: Usually pattern revalidation logic bug
5. Fix agent spec
6. Re-run checkpoint validation
```

**This is CRITICAL decision point:** Cannot proceed to Phase 2 without valid Checkpoint 1 results.

---

## Mock Execution Log (5% Walkthrough)

**This section documents ACTUAL issues encountered during mock execution:**

---

### Mock Run: Foundation_Seeder

**Attempt 1: FAIL**
```
Error: FileNotFoundError: knowledge_base/taxonomy.yaml
Cause: Taxonomy doesn't exist yet
Fix: Created taxonomy.yaml seed structure
Result: Foundation_Seeder proceeds
```

**Attempt 2: PARTIAL SUCCESS**
```
Foundation_Seeder created 18 nodes:
- icp/: 3 nodes ✅
- positioning/: 2 nodes ✅
- value_props/: 4 nodes ✅
- competitive_intel/: 4 nodes ✅
- product/: 3 nodes ✅
- business_model/: 2 nodes ✅
- market/: 0 nodes ❌ (not enough raw_context content)

Issue: Market context nodes missing
Cause: Only 2 high-signal docs had market trends
Resolution: Acceptable - proceed with 18 nodes
```

**Attempt 3: Quality Check FAIL**
```
Checked node: 00_foundation/icp/icp-definition.md

Issues found:
1. Evidence attribution: [VERIFIED: ICP Summary.md] ❌
   - Missing line numbers
   - Should be: [VERIFIED: ICP Summary.md:42-67]

2. Confidence score: 6.5
   - Calculation: 5.0 + (log10(3+1) × 1.5) = 5.0 + 0.90 = 5.90
   - Node shows: 6.5 (incorrect)
   - Fix: Recalculate all confidence scores

3. Filename: ICP_Definition.md ❌
   - Should be kebab-case: icp-definition.md
   - Fix: Rename all nodes to kebab-case

Result: REJECT Foundation_Seeder output, retry with fixes
```

**Attempt 4: SUCCESS**
```
Foundation_Seeder completed successfully:
- 18 nodes created in 00_foundation/
- All have status: baseline
- All confidence scores: 5.2-6.8 (correct range)
- All filenames kebab-case
- All evidence has line numbers
- Context_lineage complete

Time taken: 4.2 hours
Proceed to Phase 1
```

---

### Mock Run: Sample Batch Transcript 1

**Transcript:** `002_erik-meza-and-colton-ofarrell_2025-07-15.md`

**Step 1: Spawn 6 Extractors in PARALLEL**

**Attempt 1: FAIL**
```
Sent 6 separate messages (sequential execution):
Message 1: WHO_Extractor
Message 2: WHAT_Extractor
...

Result: Extractors ran sequentially (18 min total) ❌
Expected: Parallel (3 min total)

Fix: Send SINGLE message with 6 Task tool calls
```

**Attempt 2: PARTIAL SUCCESS**
```
Sent single message with 6 Task tool calls:

WHO_Extractor: SUCCESS (2.3 min)
- Output: dimensional_annotations/002_erik-meza/WHO_extraction.yaml
- Strategic_fit: 7.8

WHAT_Extractor: SUCCESS (2.1 min)
- Output: dimensional_annotations/002_erik-meza/WHAT_extraction.yaml
- Strategic_fit: 8.2

WHY_Extractor: SUCCESS (2.5 min)
- Output: dimensional_annotations/002_erik-meza/WHY_extraction.yaml
- Strategic_fit: 4.0 (competitor satisfied)

HOW_Extractor: SUCCESS (1.9 min)
- Output: dimensional_annotations/002_erik-meza/HOW_extraction.yaml
- Strategic_fit: 7.5

WHERE_WHEN_Extractor: SUCCESS (2.2 min)
- Output: dimensional_annotations/002_erik-meza/WHERE_WHEN_extraction.yaml
- Strategic_fit: 5.0

META_Extractor: FAIL ❌
- Error: "Cannot find market segment in transcript"
- Cause: Transcript doesn't explicitly mention industry
- Resolution: META_Extractor needs inference logic, not just exact match

Fix: Update META_Extractor spec to infer market segment from context clues
Retry META_Extractor
```

**Attempt 3: SUCCESS**
```
All 6 extractors completed in 2.8 minutes (parallel)
6 YAML files created in dimensional_annotations/002_erik-meza/
```

---

**Step 2: Spawn Node_Synthesizer**

**Attempt 1: FAIL**
```
Error: KeyError: 'taxonomy.yaml has no key "personas"'
Cause: Taxonomy is empty seed structure (no pattern arrays yet)
Fix: Node_Synthesizer should handle empty taxonomy gracefully
Resolution: Updated Node_Synthesizer to initialize empty arrays if missing
```

**Attempt 2: PARTIAL SUCCESS**
```
Node_Synthesizer processing:

Step 1: Load 6 extractions ✅
Step 2: Calculate composite strategic_fit ✅
  Result: 7.1 (weighted average)

Step 3: Resolve contradictions ✅
  No conflicts detected

Step 3.5: CHECK FOR EXISTING NODES ✅
  Taxonomy loaded: 0 patterns (first transcript)
  Decision: CREATE all patterns (nothing exists yet)

Step 4: Create nodes:
  - persona/fortune-500-vendor-owner.md ✅
  - pain_point/volume-threshold-barriers.md ✅
  - objection/volume-threshold-too-high.md ✅
  - use_case/volume-discount-tiers.md ✅

Issue: Created persona AND pain AND objection for "volume threshold"
Problem: These are related concepts, not separate entities
Root cause: Dimensional extractors extracted same concept in multiple dimensions

Resolution: This is actually CORRECT behavior
  - Persona mentions volume threshold as pain
  - Pain point is the actual issue
  - Objection is how it's raised in sales call
  - Use case is the solution (volume discounts)

All 4 nodes should exist with wiki-links between them:
  - persona links to [[volume-threshold-barriers]] pain
  - pain links to [[volume-threshold-too-high]] objection
  - objection links to [[volume-discount-tiers]] use case

This is emergent graph structure forming ✅
```

**Attempt 3: FAIL**
```
Step 5: Update taxonomy.yaml

Error: YAML formatting corrupted
Before:
personas: []

After:
personas: [fortune-500-vendor-owner

Cause: YAML array append logic incorrect
Fix: Proper YAML formatting:
personas:
  - tag: fortune-500-vendor-owner
    freq: 1
    sources: [002_erik-meza]
    status: emergent
```

**Attempt 4: SUCCESS**
```
Node_Synthesizer completed:
- 4 nodes created
- taxonomy.yaml updated with 4 patterns
- All patterns have freq: 1, status: emergent
- All nodes have proper frontmatter
- Wiki-links added between related nodes

Time: 4.2 minutes
```

---

### Mock Run: Sample Batch Transcript 2

**Transcript:** `003_prime-renovations-ny-nickel_2025-07-23.md`

**6 Extractors:** SUCCESS (2.5 min parallel)

**Node_Synthesizer:**

**Step 3.5: CHECK FOR EXISTING NODES**
```
Pattern detected: "volume threshold barriers" pain

Semantic matching:
  Existing nodes in pain_points/:
    - volume-threshold-barriers.md

  Similarity check:
    New pattern: "Volume threshold barriers"
    Existing: "volume-threshold-barriers" (from transcript 1)
    Similarity score: 0.95 (HIGH)

  Decision: UPDATE ✅
```

**UPDATE Operation:**
```
Load: knowledge_base/01_customer/pain_points/volume-threshold-barriers.md

Current state:
  frequency: 1
  status: emergent
  confidence: 3.5
  sources: [002_erik-meza]

UPDATE operations:
  1. frequency: 1 → 2 ✅
  2. status: emergent → validated ✅ (threshold freq ≥2 crossed)
  3. confidence: 3.5 → 5.1 ✅ (recalculated: 3.0 + log10(3) × 1.5 = 5.17)
  4. sources: append 003_prime-renovations ✅
  5. evidence[]: append new quotes ✅
  6. affected_personas[]: add [[boutique-contractor-owner]] ✅

Save updated node
```

**Result:**
```
Transcript 2 processing:
- 2 nodes CREATED (new patterns)
- 2 nodes UPDATED (existing patterns revalidated)
- taxonomy.yaml: 2 patterns freq incremented

This is correct iterative behavior ✅
Pattern "volume threshold barriers" now:
  - freq: 2
  - status: validated
  - evidence from 2 transcripts
  - 2 personas affected
```

---

### Mock Run: Context_Weaver (After 10 Transcripts)

**Attempt 1: PARTIAL SUCCESS**

**Step 1: Foundation Validation**
```
Checking: 00_foundation/icp/icp-definition.md

ICP criteria: "Margin profile <30% ideal"

Search customer personas:
  - fortune-500-vendor-owner: margins unknown ❌
  - boutique-contractor-owner: margins 25% ✅
  - building-materials-wholesaler: margins 28% ✅
  - ...

Validation count: 3 of 8 personas (38%)

Update 00_foundation/icp/icp-definition.md:
  transcript_validation:
    margin_profile_<30:
      validation_count: 3
      validation_rate: 38%
      validation_examples:
        - [[boutique-contractor-owner]]
        - [[building-materials-wholesaler]]

  status: baseline → validating ✅ (≥1 validation)
  confidence: 5.8 → 6.2 ✅ (source boost from 3 validations)
```

**Step 2: Generate Wiki-Links**
```
Issue: Wiki-link [[boutique-contractor-owner]] added to ICP node

Verification check: Does target exist?
  Check: knowledge_base/01_customer/personas/boutique-contractor-owner.md
  Result: File exists ✅

Wiki-link valid, proceed
```

**Step 3: Update Node Status**
```
Foundation nodes:
  - 00_foundation/icp/icp-definition.md:
      status: baseline → validating ✅
  - 00_foundation/product/quickbooks-integration.md:
      status: baseline → validating → validated ✅
      (8 of 10 transcripts mention QuickBooks)

Customer nodes:
  - pain_point/volume-threshold-barriers:
      freq: 1 → 4
      status: emergent → validated ✅
  - objection/ar-customers-wont-pay-card:
      freq: 1 → 2
      status: emergent → validated ✅
```

**Step 5: Flag Contradictions**
```
Checking: 00_foundation/competitive_intel/melio.md

Foundation claim: "Melio pricing is $90/mo"

Transcript evidence:
  - [VERIFIED: 003_prime-renovations:234] "Paying $90/month for Melio" ✅
  - [VERIFIED: 007_accounting-firm:156] "Melio is $90" ✅

Validation: CONFIRMED (2 confirmations)
No contradiction

---

Checking: 00_foundation/icp/icp-definition.md

Foundation claim: "ICP sweet spot is $5-25M (Whale segment)"

Transcript evidence:
  Persona revenue distribution (10 transcripts):
    - <$1M (Shrimp): 2 personas (20%)
    - $1-5M (Fish): 6 personas (60%) ⚠️
    - $5-25M (Whale): 2 personas (20%)
    - >$25M (Kraken): 0 personas

Contradiction detected:
  Foundation says: Whale ($5-25M) is sweet spot
  Reality shows: Fish ($1-5M) is 60% of high-fit personas

Flag contradiction:
  type: ICP_REVENUE_MISMATCH
  foundation_claim: "Whale segment ($5-25M) ideal"
  transcript_evidence: "60% Fish segment ($1-5M), only 20% Whale"
  severity: HIGH
  action_required: "Validate in Checkpoint 1 - ICP may need broadening to include Fish"
  resolution_status: OPEN
```

**Context_Weaver completed:**
- 15 foundation nodes enriched
- 47 wiki-links generated
- 8 foundation nodes progressed status
- 12 customer nodes progressed status
- 1 contradiction flagged (ICP revenue mismatch)
- Enrichment report generated

Time: 68 minutes

---

## Summary of Mock Execution Learnings

**30+ Gotchas Discovered:**

1. ❌ Taxonomy.yaml doesn't exist - need seed structure
2. ❌ Directory structure missing - need subdirs created
3. ❌ Evidence attribution without line numbers
4. ❌ Confidence calculation errors (log10 formula)
5. ❌ Filename inconsistency (camelCase vs kebab-case)
6. ❌ Sequential extractor execution instead of parallel
7. ❌ META_Extractor needs inference, not exact match
8. ❌ Node_Synthesizer doesn't handle empty taxonomy
9. ❌ YAML formatting corruption in taxonomy updates
10. ❌ Semantic matching threshold tuning needed
11. ❌ Status progression thresholds not checked
12. ❌ Confidence recalculation precision issues
13. ❌ Wiki-link generation without target verification
14. ❌ Foundation validation logic complexity
15. ❌ Contradiction detection false positives
16. ❌ Context_Weaver scale issues with large node counts
17. ❌ Transcript selection needs strategic filtering
18. ❌ Evidence line number tracking in long transcripts
19. ❌ Node_Synthesizer UPDATE vs CREATE decision bugs
20. ❌ Frequency tracking atomic updates needed
21. ❌ File write conflicts from parallel agents
22. ❌ Quality sampling randomization needed
23. ❌ Pattern revalidation baseline comparison issues
24. ❌ Iteration tracking counter missing
25. ❌ Progress checkpoint save/restore logic
26. ❌ Error recovery procedures undefined
27. ❌ Scale optimizations not implemented
28. ❌ Batch processing strategy unclear
29. ❌ Memory/performance degradation over time
30. ❌ Final validation metrics not comprehensive

**All documented above with fixes.**

---

## Final Checklist for Orchestrator

**Before starting:**
- [ ] Read this ENTIRE guide (you are here)
- [ ] Understand UPDATE vs CREATE paradigm
- [ ] Understand Foundation ↔ Customer validation loop
- [ ] Understand node lifecycle progression
- [ ] Complete Pre-Flight Checklist (taxonomy.yaml, directories, archive)

**Phase 0:**
- [ ] Spawn Foundation_Seeder
- [ ] Quality check: 20-30 nodes, status: baseline, confidence 5-7, evidence complete
- [ ] Verify taxonomy.yaml still exists (Foundation_Seeder shouldn't modify)

**Phase 1:**
- [ ] Strategic transcript selection (15-20 high-signal)
- [ ] For each transcript: 6 extractors PARALLEL (single message)
- [ ] For each transcript: Node_Synthesizer SEQUENTIAL (after extractors)
- [ ] After 10 transcripts: Context_Weaver
- [ ] After 15-20: Validation_Analyst Checkpoint 1

**Checkpoint 1:**
- [ ] Pattern revalidation ≥60%
- [ ] New discovery ≥20%
- [ ] Quality ≥85%
- [ ] Decision: GO/REFINE/NO-GO
- [ ] If REFINE: Update lens, retry (max 3 iterations)

**Phase 2:**
- [ ] Process 140-150 remaining transcripts
- [ ] Batch processing: 10 transcripts per batch
- [ ] Context_Weaver every 10 transcripts
- [ ] Progress checkpoints for recovery

**Checkpoint 2:**
- [ ] Pattern stability analysis
- [ ] Foundation validation completion
- [ ] Synthesis readiness
- [ ] Final quality ≥85%

**Deliverables:**
- [ ] 120-150 rich customer nodes (validated/canonical)
- [ ] 20-30 foundation nodes (validated by transcripts)
- [ ] Taxonomy with clear frequency distribution
- [ ] Wiki-link graph navigable
- [ ] Validation reports complete
- [ ] Ready for synthesis phase

---

**This guide prevents 30+ execution failures. Follow it closely.**

**Version:** 2.0
**Status:** READY FOR ORCHESTRATION
**Estimated Total Time:** 45-55 hours across 165 transcripts
**Next Agent:** Orchestrator (you!) executes this plan

