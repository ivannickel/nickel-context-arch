# Agent Handoff Package: Nickel System Upgrade & Graph Buildout

**Handoff Date:** 2025-10-30
**From:** System Design Agent (Current Session)
**To:** Execution Orchestrator Agent (Cursor Window)
**Engagement:** Nickel GTM Context Architecture
**Pattern:** Layer-Based + Evidence Attribution (SOP 2 + SOP 4)

---

## Executive Summary

**Mission:** Execute dimensional system upgrade + process 160 remaining transcripts using multi-agent orchestration

**Current State:**
- ✅ Iteration 1 complete: 5/165 transcripts (3%), 31 nodes, 67 patterns, 88% quality
- ✅ System upgrade specs complete: Dimensional + Pixee methodology designed
- ✅ High-value Nickel context available: ICP, positioning, competitive intel
- ⏳ **Next:** Strategic lens creation → Sample batch validation → Full corpus processing

**Multi-Agent Architecture:**
- **Pattern Choice:** Layer-Based (3-6 month engagement, research → execution)
- **Agent Cascade:** 5-agent sequential + parallel execution
- **Evidence Standard:** VERIFIED/INFERRED/UNKNOWN throughout
- **Quality Gates:** 2 validation checkpoints (after sample batch, after full corpus)

**Timeline:** 45-55 hours total execution time across 10-15 work sessions

---

## Part 1: Multi-Agent Orchestration Architecture

### Pattern Selection [VERIFIED: agent_orchestration_patterns_sop.md:19-29]

**Engagement Characteristics:**
```
Duration:    3-6 months (ongoing GTM intelligence)
Team Size:   2-3 (Jacob + Ivan stakeholder)
Complexity:  High (165 transcripts, 6 dimensional analysis, strategic GTM context)
Type:        Research → Execution (discovery patterns → actionable GTM intelligence)
```

**Recommended Pattern:** **Layer-Based Structure** (SOP 2)

**Why Not Domain-Based?**
- Nickel already has domain-based knowledge_base/ from Iteration 1
- But processing workflow needs layer separation (research → execution)
- Hybrid: Keep domain structure for outputs, add layer structure for processing

**Adjusted Structure:**
```
nickel_gtm_context_architecture/
├── knowledge_base/                 # OUTPUTS (domain-based, from Iteration 1)
│   ├── 00_foundation/
│   ├── 01_customer/
│   ├── 02_product/
│   ├── 03_market/
│   ├── strategic_lens.yaml
│   └── taxonomy.yaml
│
├── _PROCESSING/                    # NEW: Layer-based workflow
│   ├── research/                   # Layer 1: Discovery & Analysis
│   │   ├── strategic_lens_creation/
│   │   ├── dimensional_extractions/
│   │   └── pattern_analysis/
│   │
│   ├── execution/                  # Layer 2: Node Creation & Validation
│   │   ├── node_synthesis/
│   │   ├── taxonomy_updates/
│   │   └── quality_validation/
│   │
│   └── data/                       # Layer 3: Data Pipeline
│       ├── raw/                    # Source transcripts (read-only)
│       ├── staging/                # Dimensional annotations
│       └── outputs/                # Finalized nodes → knowledge_base/
│
└── _AGENT_WORKSPACE/               # Agent specs, logs, reports
    ├── agents/                     # Agent specifications
    ├── execution_logs/             # Agent run logs
    └── validation_reports/         # Checkpoint reports
```

**Key Insight:** Outputs go to domain-based knowledge_base/ (for end-users), but processing happens in layer-based _PROCESSING/ (for agents)

---

### Agent Cascade Design

**5-Agent Architecture:**

```
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 0: STRATEGIC LENS CREATION                                │
│                                                                   │
│ Agent 1: Strategic Lens Builder (STANDALONE)                     │
│ ├─ Input:  taxonomy.yaml v1.2.0 (67 patterns)                   │
│ │          Nickel context docs (ICP, positioning, competitive)   │
│ ├─ Output: strategic_lens.yaml v1.0                             │
│ └─ Time:   60-90 min                                             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 1: SAMPLE BATCH (10 transcripts)                          │
│                                                                   │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ Per-Transcript Loop (10 iterations)                      │    │
│ │                                                           │    │
│ │ Agent 2a-f: Dimensional Extractors (PARALLEL)            │    │
│ │ ├─ 2a: WHO Extractor     (personas, buyers)             │    │
│ │ ├─ 2b: WHAT Extractor    (pains, use cases)             │    │
│ │ ├─ 2c: WHY Extractor     (objections, competitive)      │    │
│ │ ├─ 2d: HOW Extractor     (product requirements)         │    │
│ │ ├─ 2e: WHERE_WHEN        (journey stage)                │    │
│ │ └─ 2f: META Extractor    (market context)               │    │
│ │                                                           │    │
│ │ Input:  Transcript + strategic_lens.yaml                 │    │
│ │ Output: 6 dimensional annotations (staging/)             │    │
│ │ Time:   10-15 min per transcript (parallel)              │    │
│ │                                                           │    │
│ │                        ↓                                  │    │
│ │                                                           │    │
│ │ Agent 3: Node Synthesizer (SEQUENTIAL, waits for 2a-f)   │    │
│ │ ├─ Input:  6 dimensional annotations                     │    │
│ │ ├─ Output: 5-10 knowledge graph nodes → outputs/         │    │
│ │ └─ Time:   3-5 min per transcript                        │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                   │
│ Total per transcript: 15-20 min                                  │
│ Total for 10 transcripts: 2.5-3.5 hours                         │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ CHECKPOINT 1: SAMPLE BATCH VALIDATION                            │
│                                                                   │
│ Agent 4: Validation Analyst (STANDALONE)                         │
│ ├─ Input:  50-100 nodes from sample batch                       │
│ │          taxonomy.yaml updates                                 │
│ │          Pattern frequency changes                             │
│ ├─ Output: Validation report (revalidation %, discovery %, quality) │
│ │          GO/NO-GO decision for scaling                         │
│ └─ Time:   30-60 min                                             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    [IF GO: Proceed to Phase 2]
                    [IF NO-GO: Update lens, retry sample batch]
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 2: FULL CORPUS (150 remaining transcripts)                │
│                                                                   │
│ Repeat Agent 2a-f → Agent 3 loop for 150 transcripts            │
│ Batch size: 10-20 per session                                   │
│ Total sessions: 8-15 sessions                                   │
│ Total time: 40-50 hours                                         │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ CHECKPOINT 2: FINAL VALIDATION                                   │
│                                                                   │
│ Agent 4: Validation Analyst (FINAL RUN)                         │
│ ├─ Input:  All 165 transcripts processed                        │
│ │          Final taxonomy                                        │
│ │          Complete knowledge graph                              │
│ ├─ Output: Final quality report                                 │
│ │          Pattern stability score                               │
│ │          Knowledge graph health metrics                        │
│ └─ Time:   2-3 hours                                             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 3: SYNTHESIS & HANDOFF                                     │
│                                                                   │
│ Agent 5: Synthesis Generator (STANDALONE)                        │
│ ├─ Input:  Complete knowledge graph                             │
│ ├─ Output: Domain synthesis roll-ups (_synthesis/ docs)         │
│ │          Inter-domain strategic bridges                        │
│ │          GTM playbooks and recommendations                     │
│ └─ Time:   6-8 hours                                             │
└─────────────────────────────────────────────────────────────────┘
```

**Total Timeline:** 50-60 hours across 10-15 sessions

---

### Agent Specifications

#### Agent 1: Strategic Lens Builder

**Role:** Convert taxonomy + Nickel context → strategic priorities data structure

**Input:**
- `knowledge_base/taxonomy.yaml` v1.2.0 (67 patterns)
- `knowledge_base/raw_context/ICP Summary & Use Cases.md`
- `knowledge_base/raw_context/Nickel core positioning statement.md`
- `knowledge_base/raw_context/Discovery call script.md`
- Any other Nickel strategy docs

**Process:**
1. Read all input files
2. Map 67 taxonomy patterns to dimensional categories (WHO/WHAT/WHY/HOW/WHERE_WHEN/META)
3. Integrate Nickel ICP → `who.target_personas`
4. Integrate pain points → `what.critical_pain_points`
5. Integrate competitive intel → `why.competitive_threats`
6. Assign priority rankings (1-3) based on:
   - Frequency from taxonomy (higher = priority 1)
   - Strategic importance from Nickel context (ICP persona = priority 1)
   - Validation status (needs_validation: true if freq=1)
7. Calculate strategic_fit scoring criteria (0-10 scale) for high-priority items

**Output:**
- `knowledge_base/strategic_lens.yaml` v1.0
- Structure per NICKEL_STRUCTURE_MAPPING.md section 2.2

**Evidence Attribution:**
- [VERIFIED: taxonomy.yaml] for frequency data
- [VERIFIED: ICP Summary.md] for persona criteria
- [INFERRED: from frequency + ICP] for priority assignments

**Success Criteria:**
- ✅ All 67 patterns mapped to dimensions
- ✅ Nickel context integrated (ICP, positioning, competitive)
- ✅ Priority rankings (1-3) assigned to all items
- ✅ Strategic_fit criteria defined for priority 1-2 items
- ✅ Validation flags set for freq=1 patterns

**Time:** 60-90 min

**Dependencies:** None (standalone)

**Prompt Template:**
```
Read taxonomy.yaml and Nickel context docs in raw_context/.

Create strategic_lens.yaml that:
1. Maps all 67 patterns from taxonomy to WHO/WHAT/WHY/HOW/WHERE_WHEN/META dimensions
2. Integrates Nickel's ICP definition, positioning, and strategic priorities
3. Assigns priority rankings (1-3) for each pattern based on:
   - Frequency from taxonomy (6+ = priority 1, 2-5 = priority 2, 1 = priority 3)
   - Strategic importance from Nickel context (ICP personas = priority 1)
   - Critical severity (severity: critical = priority 1 regardless of frequency)
4. Calculates strategic_fit scoring criteria (0-10) for high-priority items
5. Flags patterns needing validation (frequency = 1)

Use VERIFIED attribution for data from files.
Use INFERRED attribution for priority assignments.

Schema: See NICKEL_STRUCTURE_MAPPING.md section 2.2
```

---

#### Agents 2a-f: Dimensional Extractors (Parallel)

**Shared Configuration:**
- Run in parallel (all 6 simultaneously per transcript)
- Each agent is independent (no inter-agent dependencies)
- All read same inputs (transcript + strategic_lens.yaml)
- Each writes to separate output file in staging/

**Agent 2a: WHO Extractor**

**Role:** Extract personas, company profiles, buyer characteristics

**Input:**
- Single transcript from `raw_context/`
- `strategic_lens.yaml` (for persona matching criteria)

**Process:**
1. Read transcript + strategic_lens.yaml
2. Identify personas mentioned:
   - Job titles, roles, responsibilities
   - Company size, industry, revenue
   - Buyer authority, decision-making process
3. For each persona found:
   - Match against `lens.who.target_personas` criteria
   - Calculate strategic_fit score (0-10) using lens priorities
   - Check against `lens.who.anti_personas` (disqualify if match)
4. Extract evidence:
   - Direct quotes with line numbers
   - Company context details
   - Strategic relevance explanation
5. Apply context_lineage:
   - Source document + line ranges
   - Unique_value (why this source matters)
   - Dimension: "WHO"

**Output:**
- `_PROCESSING/data/staging/[transcript_id]/WHO_extraction.yaml`

**Schema:**
```yaml
---
dimensional_extraction:
  dimension: "WHO"
  transcript:
    file: "[transcript_name].md"
    date: "YYYY-MM-DD"
  strategic_lens_version: "1.0"
  extraction_date: "YYYY-MM-DD"

personas_extracted:
  - name: "Accounting Firm Buyer"
    priority: 1
    strategic_fit: 9  # Calculation shown in evidence
    frequency: 1
    composite_score: 6.4  # (1 × 0.4) + (9 × 0.6)
    tier: "Tier 2"  # Composite < 8.0

    company_context:
      name: "[Company Name]"
      type: "CPA + Bookkeeping"
      client_count: 150
      employee_count: 15

    evidence:
      - quote: "We have 150 clients across our portfolio"
        location: "[transcript]:lines 342-345"
        type: "client_count"
        strategic_relevance: "Confirms 150x multiplier hypothesis from Iteration 1"
        confidence: "VERIFIED"

    needs_validation: true  # Only 1 example so far

context_lineage:
  source_document:
    file: "[transcript].md"
    lines_extracted: "342-345, 378-381, 412-445"
    unique_value: "First accounting firm mention in GTM Build Update context"
  extraction_agent: "WHO_Extractor"
  extraction_date: "YYYY-MM-DD"
  strategic_lens_version: "1.0"
---
```

**Evidence Attribution Rules:**
- [VERIFIED: transcript:line] for direct quotes
- [INFERRED: from quote + lens criteria] for strategic_fit scores
- [UNKNOWN: needs validation] for single-mention patterns

**Success Criteria:**
- ✅ All personas in transcript extracted
- ✅ Strategic_fit calculated per lens criteria
- ✅ Evidence includes line-level citations
- ✅ Context_lineage complete
- ✅ VERIFIED/INFERRED/UNKNOWN tagged appropriately

**Time:** 2-3 min per transcript (parallel with others)

**Dependencies:** Agent 1 (needs strategic_lens.yaml)

**Prompt Template:**
```
Read [transcript].md and strategic_lens.yaml.

Extract WHO dimension (personas, buyer profiles, company characteristics):
1. Identify all personas mentioned (job titles, roles, companies)
2. For each persona:
   - Match against lens.who.target_personas criteria
   - Calculate strategic_fit (0-10) using lens priorities
   - Check lens.who.anti_personas (disqualify if match)
   - Extract evidence with line numbers
   - Tag confidence: VERIFIED (direct quote), INFERRED (deduced), UNKNOWN (needs validation)
3. Create context_lineage with:
   - Lines extracted
   - Unique_value (why this source matters)
   - Dimension: "WHO"

Output: WHO_extraction.yaml per schema in AGENT_HANDOFF_PACKAGE.md

Spec reference: who_extractor.md (full specification)
```

---

**Agent 2b: WHAT Extractor**

**Role:** Extract pain points, use cases, product fit signals

**Input:** Same as Agent 2a

**Process:** Similar to 2a, but focused on:
- Pain points → match `lens.what.critical_pain_points`
- Use cases → match `lens.what.validated_use_cases`
- Product fit signals
- Strategic_fit scoring per lens priorities

**Output:** `_PROCESSING/data/staging/[transcript_id]/WHAT_extraction.yaml`

**Time:** 2-3 min per transcript (parallel)

---

**Agent 2c: WHY Extractor**

**Role:** Extract objections, motivations, competitive mentions

**Input:** Same as Agent 2a

**Process:** Similar to 2a, but focused on:
- Objections → match `lens.why.critical_objections`
- Competitive threats → match `lens.why.competitive_threats`
- Purchase motivations
- Strategic_fit scoring per lens priorities

**Output:** `_PROCESSING/data/staging/[transcript_id]/WHY_extraction.yaml`

**Time:** 2-3 min per transcript (parallel)

---

**Agent 2d: HOW Extractor**

**Role:** Extract product requirements, feature gaps, capabilities

**Input:** Same as Agent 2a

**Process:** Similar to 2a, but focused on:
- Feature requests
- Product capabilities mentioned
- Integration requirements
- Technical constraints

**Output:** `_PROCESSING/data/staging/[transcript_id]/HOW_extraction.yaml`

**Time:** 2-3 min per transcript (parallel)

---

**Agent 2e: WHERE_WHEN Extractor**

**Role:** Extract journey stage, discovery triggers, timing

**Input:** Same as Agent 2a

**Process:** Similar to 2a, but focused on:
- Buyer journey stage
- Discovery triggers (what led to Nickel)
- Timeline/urgency signals
- Implementation readiness

**Output:** `_PROCESSING/data/staging/[transcript_id]/WHERE_WHEN_extraction.yaml`

**Time:** 2-3 min per transcript (parallel)

---

**Agent 2f: META Extractor**

**Role:** Extract market context, industry patterns, segment insights

**Input:** Same as Agent 2a

**Process:** Similar to 2a, but focused on:
- Market segment classification
- Industry-specific patterns
- Macro trends mentioned
- Competitive landscape context

**Output:** `_PROCESSING/data/staging/[transcript_id]/META_extraction.yaml`

**Time:** 2-3 min per transcript (parallel)

---

#### Agent 3: Node Synthesizer

**Role:** Synthesize 6 dimensional extractions → knowledge graph nodes

**Input:**
- 6 dimensional extraction files from `_PROCESSING/data/staging/[transcript_id]/`
- `taxonomy.yaml` (to check if pattern exists)
- `strategic_lens.yaml` (for cross-dimensional validation)

**Process:**
1. **Read all 6 dimensional extractions** for single transcript
2. **Identify nodes to create/update:**
   - WHO extractions → `personas/` nodes
   - WHAT pains → `pain_points/` nodes
   - WHAT use cases → `use_cases/` nodes
   - WHY objections → `objections/` nodes
   - WHY competitive → `competitors/` nodes
   - HOW features → `product_requirements/` nodes (if new category needed)
   - WHERE_WHEN → `journey_stages/` nodes (if new category needed)
   - META → Market segment tags in frontmatter

3. **For each node:**
   - Check if exists in taxonomy.yaml (update frequency) or new (create)
   - Composite frontmatter from dimensional extractions:
     ```yaml
     ---
     context_type: pain_point
     name: "volume-threshold-barriers"
     frequency: 7  # Updated from 6 → 7 (revalidation!)
     severity: high
     iteration_discovered: 1

     # NEW: Context Lineage (from WHAT extraction)
     context_lineage:
       source_transcripts:
         - file: "[transcript].md"
           lines_extracted: "234-267"
           unique_value: "First mention in GTM Build Update context"
           strategic_fit: 9
           confidence: "VERIFIED"
       extraction_type: "dimensional_analysis"
       dimension: "WHAT"
       strategic_lens_version: "1.0"

     # NEW: Dimensional Annotations (cross-reference)
     dimensional_annotations:
       - dimension: "WHAT"
         extraction_type: "pain_point"
         strategic_fit: 9
       - dimension: "WHY"
         extraction_type: "objection"
         strategic_fit: 8
         notes: "Also manifests as pricing objection"

     evidence:
       - quote: "[quote from transcript]"
         location: "[transcript]:234-236"
         type: "pain_point"
         strategic_relevance: "[from WHAT extraction]"
         confidence: "VERIFIED"

     related_concepts:
       - "[[objections/volume-threshold-too-high]]"  # WHY dimension
       - "[[personas/fortune-500-vendor]]"  # WHO dimension
       - "[[use_cases/high-volume-ap]]"  # WHAT dimension
     ---
     ```

4. **Create inter-dimensional links:**
   - WHO persona mentions WHAT pain → Link persona ↔ pain
   - WHAT pain triggers WHY objection → Link pain ↔ objection
   - WHY objection blocks HOW feature → Link objection ↔ feature
   - Tier links: Tier 1 (must-link), Tier 2 (should-link), Tier 3 (could-link)

5. **Update taxonomy.yaml:**
   - Existing patterns: Increment frequency
   - New patterns: Add with frequency: 1, status: validated
   - Track iteration_discovered (current = iteration 2+)

6. **Move to outputs:**
   - Write finalized nodes to `_PROCESSING/data/outputs/[category]/`
   - These will be reviewed then moved to `knowledge_base/` in final step

**Output:**
- 5-10 nodes in `_PROCESSING/data/outputs/`
- Updated `taxonomy.yaml` (frequency changes)
- Inter-dimensional link map (for validation)

**Evidence Attribution:**
- Inherits VERIFIED/INFERRED/UNKNOWN from dimensional extractions
- Never upgrades confidence (INFERRED stays INFERRED)
- Can downgrade (VERIFIED → INFERRED if synthesizing multiple sources)

**Success Criteria:**
- ✅ All dimensional extractions represented in nodes
- ✅ Context_lineage present in all nodes
- ✅ Dimensional_annotations cross-referenced
- ✅ Inter-dimensional links created (3+ per node)
- ✅ Taxonomy updated (frequencies)
- ✅ Evidence attribution preserved (no confidence inflation)

**Time:** 3-5 min per transcript

**Dependencies:** Agents 2a-f (waits for all 6 dimensional extractions)

**Prompt Template:**
```
Read 6 dimensional extraction files from staging/[transcript_id]/.

Synthesize into knowledge graph nodes:
1. Identify nodes to create/update:
   - WHO → personas/
   - WHAT pains → pain_points/
   - WHAT use cases → use_cases/
   - WHY objections → objections/
   - WHY competitive → competitors/

2. For each node:
   - Check taxonomy.yaml (exists? update frequency : create new)
   - Composite frontmatter from dimensional extractions
   - Include context_lineage from source dimension
   - Add dimensional_annotations (cross-reference other dimensions)
   - Extract evidence with VERIFIED/INFERRED/UNKNOWN tags
   - Create inter-dimensional links (3+ per node)

3. Update taxonomy.yaml:
   - Existing patterns: frequency++
   - New patterns: add with frequency: 1, status: validated

4. Output nodes to _PROCESSING/data/outputs/[category]/

Evidence Attribution Rules:
- Inherit tags from dimensional extractions
- Never upgrade confidence (INFERRED stays INFERRED)
- Can downgrade if synthesizing multiple sources
- CRITICAL: No confidence inflation in agent cascade

Schema reference: NICKEL_STRUCTURE_MAPPING.md section 2.3
```

---

#### Agent 4: Validation Analyst

**Role:** Analyze sample batch (or full corpus) quality and provide GO/NO-GO decision

**Input:**
- All nodes from `_PROCESSING/data/outputs/`
- Updated `taxonomy.yaml`
- `strategic_lens.yaml` (for alignment check)
- Iteration 1 baseline (67 patterns, 88% quality, 72/100 stability)

**Process:**

1. **Pattern Revalidation Analysis**
   - Count how many Iteration 1 patterns (67 total) reappeared in new batch
   - Calculate revalidation rate: `(reappeared / 67) × 100%`
   - Target: ≥60% revalidation rate
   - [VERIFIED: taxonomy.yaml frequency changes]

2. **New Pattern Discovery Analysis**
   - Count new patterns added to taxonomy (frequency: 1, iteration_discovered: 2)
   - Calculate discovery rate: `(new patterns / total new extractions) × 100%`
   - Target: ≥20% discovery rate
   - [VERIFIED: taxonomy.yaml new entries]

3. **Quality Maintenance Analysis**
   - Spot-check 10% random sample of nodes (5-10 nodes)
   - Check for:
     - ✅ Context_lineage present (line-level attribution)
     - ✅ Evidence citations with VERIFIED/INFERRED/UNKNOWN
     - ✅ Strategic_fit scores calculated
     - ✅ Dimensional_annotations cross-referenced
     - ✅ Inter-dimensional links (3+ per node)
   - Calculate quality score: `(checks passed / checks total) × 100%`
   - Target: ≥85% quality
   - [VERIFIED: node spot-check results]

4. **Strategic Alignment Analysis**
   - WHO: Do extracted personas match lens.who.target_personas?
   - WHAT: Do pain points match lens.what.critical_pain_points?
   - WHY: Do objections match lens.why.critical_objections?
   - Calculate alignment rate: `(matches / lens priorities) × 100%`
   - Target: ≥70% alignment
   - [INFERRED: from pattern matches to lens priorities]

5. **Evidence Attribution Audit**
   - Check for confidence inflation (did INFERRED become VERIFIED without new evidence?)
   - Check for missing attributions (quantitative claims without tags)
   - Calculate attribution compliance: `(tagged claims / total claims) × 100%`
   - Target: 100% for quantitative claims
   - [VERIFIED: evidence attribution scan]

6. **Decision Logic**
   ```python
   if revalidation >= 60 and discovery >= 20 and quality >= 85 and alignment >= 70:
       decision = "GO - Proceed to scaling"
   elif quality < 80 or attribution < 90:
       decision = "NO-GO - Quality issues, fix before scaling"
   elif alignment < 60:
       decision = "NO-GO - Strategic misalignment, update lens"
   else:
       decision = "ADJUST - Update lens, retry sample batch"
   ```

**Output:**
- `_AGENT_WORKSPACE/validation_reports/Report_[N]_[Date].md`

**Report Structure:**
```markdown
# Validation Report [N]: [Sample Batch / Final Corpus]

**Date:** YYYY-MM-DD
**Batch Size:** [N transcripts processed]
**Total Nodes:** [N created/updated]

---

## Metrics Summary

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Pattern Revalidation | ≥60% | XX% | ✅ / ❌ |
| New Pattern Discovery | ≥20% | XX% | ✅ / ❌ |
| Quality Maintenance | ≥85% | XX% | ✅ / ❌ |
| Strategic Alignment | ≥70% | XX% | ✅ / ❌ |
| Attribution Compliance | 100% | XX% | ✅ / ❌ |

---

## Pattern Revalidation Analysis

**Iteration 1 Patterns (67 total):**
- Reappeared: XX patterns
- Frequency increased: XX patterns
- Not found: XX patterns (list)

**High-Priority Pattern Status:**
- accounting-firm-buyer (freq 1 → X): [Status]
- relay-financial (freq 1 → X): [Status]
- volume-threshold-barriers (freq 6 → X): [Status]

[VERIFIED: taxonomy.yaml frequency changes]

---

## New Pattern Discovery

**New Patterns Discovered:**
1. [pattern-name] (frequency: 1, dimension: WHO)
2. [pattern-name] (frequency: 1, dimension: WHAT)
[...]

[VERIFIED: taxonomy.yaml new entries]

---

## Quality Spot-Check (10% sample)

**Nodes Reviewed:** [List of 5-10 nodes]

**Quality Checklist:**
- Context_lineage: X/X ✅
- Evidence citations: X/X ✅
- Strategic_fit scores: X/X ✅
- Dimensional_annotations: X/X ✅
- Inter-dimensional links (3+): X/X ✅

**Overall Quality:** XX% [VERIFIED: spot-check results]

---

## Strategic Alignment

**WHO Dimension:**
- Target personas in lens: X
- Extracted personas matching: X (XX% alignment)

**WHAT Dimension:**
- Critical pains in lens: X
- Extracted pains matching: X (XX% alignment)

**WHY Dimension:**
- Critical objections in lens: X
- Extracted objections matching: X (XX% alignment)

**Overall Alignment:** XX% [INFERRED: from matches to lens]

---

## Evidence Attribution Audit

**Confidence Inflation Check:**
- ✅ No INFERRED → VERIFIED upgrades without evidence
- ❌ Found [N] instances of confidence inflation (list)

**Missing Attribution Check:**
- Quantitative claims: X total
- Tagged with VERIFIED/INFERRED/UNKNOWN: X (XX%)
- Missing attribution: X claims (list)

[VERIFIED: attribution scan results]

---

## Decision

**GO / NO-GO / ADJUST**

**Rationale:**
[Based on decision logic above]

**If NO-GO:**
- Issues identified: [List]
- Recommended actions: [List]

**If ADJUST:**
- Lens updates needed: [List]
- Sample batch retry plan: [Steps]

**If GO:**
- Approved for scaling to remaining transcripts
- Lock strategic_lens.yaml as v[X.X]
- Proceed with batch size: [N]

---

**Analyst:** Agent 4 (Validation Analyst)
**Evidence Standard:** VERIFIED/INFERRED per SOP 4
**Next Action:** [Based on decision]
```

**Time:** 30-60 min (sample batch), 2-3 hours (final corpus)

**Dependencies:** Agent 3 (needs synthesized nodes)

**Prompt Template:**
```
Analyze results from [sample batch / full corpus] processing.

Calculate metrics:
1. Pattern Revalidation: (Iteration 1 patterns reappeared / 67) × 100%
   [VERIFIED: taxonomy.yaml frequency changes]

2. New Pattern Discovery: (new patterns / total extractions) × 100%
   [VERIFIED: taxonomy.yaml new entries]

3. Quality Maintenance: Spot-check 10% nodes for:
   - Context_lineage, evidence, strategic_fit, dimensional_annotations, links
   [VERIFIED: spot-check results]

4. Strategic Alignment: (extracted patterns matching lens / lens priorities) × 100%
   [INFERRED: from pattern matches]

5. Attribution Compliance: (tagged claims / total claims) × 100%
   [VERIFIED: attribution scan]

Decision Logic:
- GO: revalidation ≥60%, discovery ≥20%, quality ≥85%, alignment ≥70%
- NO-GO: quality <80% or attribution <90%
- ADJUST: alignment <60% or other issues

Output: validation_reports/Report_[N].md

SOP Reference: agent_orchestration_patterns_sop.md SOP 4 (Evidence Attribution)
```

---

#### Agent 5: Synthesis Generator

**Role:** Create domain synthesis roll-ups, inter-domain bridges, GTM playbooks

**Input:**
- Complete knowledge graph (`knowledge_base/`)
- Final `taxonomy.yaml`
- All dimensional annotations (for cross-domain patterns)

**Process:**

1. **Domain Synthesis Roll-Ups**
   - Create `_synthesis/` documents per domain:
     - `00_foundation/_synthesis/nickel-strategic-context.md`
     - `01_customer/_synthesis/customer-intelligence-summary.md`
     - `02_product/_synthesis/product-requirements-summary.md`
     - `03_market/_synthesis/competitive-landscape-summary.md`
   - Aggregate patterns by frequency, strategic_fit, tier
   - [VERIFIED: from knowledge graph nodes]
   - [INFERRED: synthesis insights from patterns]

2. **Inter-Domain Strategic Bridges**
   - Identify Tier 1 links (must-have connections):
     - WHO (accounting firm) ↔ WHAT (low-volume clients pain) ↔ WHY (platform fees objection)
   - Create bridge documents:
     - `_synthesis/bridges/accounting-firm-segment-playbook.md`
     - `_synthesis/bridges/competitive-positioning-relay.md`
   - [INFERRED: from inter-dimensional link analysis]

3. **GTM Playbooks & Recommendations**
   - ICP refinement (validated personas)
   - Messaging framework (pain points → value props)
   - Competitive battle cards (Relay, Bill.com, etc.)
   - Objection handling scripts
   - [INFERRED: from strategic synthesis]

**Output:**
- 4-6 domain synthesis documents
- 3-5 inter-domain bridge documents
- 2-3 GTM playbook documents

**Time:** 6-8 hours

**Dependencies:** All 165 transcripts processed (Agent 3 complete)

---

## Part 2: Evidence Attribution Standard (SOP 4)

### VERIFIED / INFERRED / UNKNOWN Taxonomy

**Throughout the agent cascade, enforce:**

1. **Agent 1 (Strategic Lens Builder):**
   - Frequency data: [VERIFIED: taxonomy.yaml]
   - ICP criteria: [VERIFIED: ICP Summary.md]
   - Priority assignments: [INFERRED: from frequency + ICP]

2. **Agents 2a-f (Dimensional Extractors):**
   - Direct quotes: [VERIFIED: transcript:line]
   - Strategic_fit scores: [INFERRED: from quote + lens criteria]
   - Single-mention patterns: [UNKNOWN: needs validation]

3. **Agent 3 (Node Synthesizer):**
   - Inherits tags from extractions
   - **CRITICAL:** Never upgrades confidence (INFERRED stays INFERRED)
   - Can downgrade (VERIFIED → INFERRED if synthesizing multiple sources)

4. **Agent 4 (Validation Analyst):**
   - Metric calculations: [VERIFIED: from data scans]
   - Decision rationale: [INFERRED: from metrics]
   - Recommendations: [INFERRED: from analysis]

5. **Agent 5 (Synthesis Generator):**
   - Pattern aggregation: [VERIFIED: from nodes]
   - Synthesis insights: [INFERRED: from patterns]
   - GTM recommendations: [INFERRED: from strategic analysis]

**Quality Gate:** Agent 4 checks for confidence inflation at both validation checkpoints

---

## Part 3: Execution Instructions

### Session 1: Strategic Lens Creation (60-90 min)

**Location:** Cursor window, nickel_gtm_context_architecture directory

**Steps:**
1. Create `_PROCESSING/` directory structure (research/, execution/, data/)
2. Copy agent specifications to `_AGENT_WORKSPACE/agents/`
3. Execute Agent 1: Strategic Lens Builder
   - Input: taxonomy.yaml + Nickel context docs
   - Output: strategic_lens.yaml v1.0
   - Validation: All 67 patterns mapped, priorities assigned

**Deliverable:** `knowledge_base/strategic_lens.yaml`

**Evidence Attribution:** VERIFIED/INFERRED tags throughout

---

### Session 2-3: Sample Batch Processing (2.5-3.5 hours for 10 transcripts)

**Location:** Cursor window

**Transcript Selection Strategy:**
```
Pick 10 strategically:
1. Recent GTM Build Updates (10/24, 10/27, 10/31) - 3 transcripts
2. Customer feature requests - 2 transcripts
3. ICP/positioning docs - 2 transcripts
4. Competitive intelligence - 1 transcript
5. Onboarding/compliance - 1 transcript
6. Industry context - 1 transcript
```

**Per-Transcript Process:**
1. Execute Agents 2a-f in parallel:
   - WHO, WHAT, WHY, HOW, WHERE_WHEN, META extractions
   - Output: 6 files in `_PROCESSING/data/staging/[transcript_id]/`
   - Time: 10-15 min per transcript (parallel)

2. Execute Agent 3 (Node Synthesizer):
   - Input: 6 dimensional extractions
   - Output: 5-10 nodes in `_PROCESSING/data/outputs/`
   - Update: taxonomy.yaml (frequencies)
   - Time: 3-5 min per transcript

**Total per transcript:** 15-20 min
**Total for 10 transcripts:** 2.5-3.5 hours

**Deliverable:** 50-100 nodes, updated taxonomy, dimensional annotations

**Evidence Attribution:** Inherit tags from extractions, no confidence inflation

---

### Session 4: Sample Batch Validation (30-60 min)

**Location:** Cursor window

**Steps:**
1. Execute Agent 4: Validation Analyst
2. Calculate metrics (revalidation, discovery, quality, alignment, attribution)
3. Generate Report_1: Sample Batch Analysis
4. Decision: GO / NO-GO / ADJUST

**Deliverable:** `_AGENT_WORKSPACE/validation_reports/Report_1_Sample_Batch.md`

**Decision Point:**
- ✅ GO → Proceed to Sessions 5-15 (full corpus)
- ❌ NO-GO → Fix quality/attribution issues, retry sample batch
- 🔄 ADJUST → Update strategic_lens.yaml, retry sample batch

---

### Sessions 5-15: Full Corpus Processing (40-50 hours for 150 transcripts)

**If Sample Batch = GO:**

**Location:** Cursor window

**Batch Size:** 10-20 transcripts per session

**Process:** Repeat Sessions 2-3 process for remaining 150 transcripts

**Total Sessions:** 8-15 sessions (depending on batch size)

**Deliverable:** Complete knowledge graph (165 transcripts processed)

**Continuous Monitoring:** Quality checks every 2-3 sessions

---

### Session 16: Final Validation (2-3 hours)

**Location:** Cursor window

**Steps:**
1. Execute Agent 4: Validation Analyst (final run)
2. Calculate final metrics (pattern stability, quality, health)
3. Generate Report_2: Final Corpus Analysis

**Deliverable:** `_AGENT_WORKSPACE/validation_reports/Report_2_Final_Corpus.md`

---

### Session 17: Synthesis & Handoff (6-8 hours)

**Location:** Cursor window

**Steps:**
1. Execute Agent 5: Synthesis Generator
2. Create domain synthesis roll-ups
3. Create inter-domain strategic bridges
4. Generate GTM playbooks & recommendations

**Deliverable:**
- Domain synthesis documents in `_synthesis/`
- Inter-domain bridges
- GTM playbooks

---

## Part 4: Success Criteria

### Phase 0 Success (Strategic Lens):
- ✅ `strategic_lens.yaml` created
- ✅ All 67 taxonomy patterns mapped to dimensions
- ✅ Nickel context integrated (ICP, positioning, competitive)
- ✅ Priority rankings assigned (1-3)
- ✅ Strategic_fit criteria defined for high-priority items
- ✅ VERIFIED/INFERRED attribution throughout

### Checkpoint 1 Success (Sample Batch):
- ✅ 10 transcripts processed with dimensional approach
- ✅ 50-100 nodes created/updated
- ✅ Revalidation rate ≥60% (Iteration 1 patterns reappeared)
- ✅ New discovery rate ≥20% (novel patterns found)
- ✅ Quality maintained ≥85% (evidence, attribution, strategic_fit)
- ✅ Strategic alignment ≥70% (matches lens priorities)
- ✅ Attribution compliance 100% (no confidence inflation)
- ✅ Decision: GO (approved for scaling)

### Checkpoint 2 Success (Final Corpus):
- ✅ 165 transcripts fully processed
- ✅ Pattern stability ≥85/100 (target increase from 72/100)
- ✅ Quality maintained ≥85% throughout
- ✅ Complete dimensional coverage (WHO/WHAT/WHY/HOW/WHERE_WHEN/META)
- ✅ Inter-dimensional links created (3+ per node average)
- ✅ Evidence attribution 100% compliant (no inflation in cascade)

### Phase 3 Success (Synthesis):
- ✅ Domain synthesis roll-ups created
- ✅ Inter-domain strategic bridges documented
- ✅ GTM playbooks generated (ICP, messaging, competitive, objections)
- ✅ Handoff documentation complete

---

## Part 5: Risk Mitigation

### Risk 1: Agent Cascade Confidence Inflation

**Threat:** INFERRED becomes VERIFIED without new evidence as agents pass data

**Mitigation:**
- Agent 3 explicitly checks: Never upgrade confidence
- Agent 4 audits: Confidence inflation check at both checkpoints
- [VERIFIED: SOP 4 enforcement]

### Risk 2: Sample Batch Fails Validation

**Threat:** Revalidation <60% or alignment <70% at Checkpoint 1

**Mitigation:**
- Update strategic_lens.yaml based on misalignments
- Retry sample batch (10 more transcripts)
- Do not proceed to full corpus without pass
- [INFERRED: risk probability medium, impact high]

### Risk 3: Layer-Based Structure Not Followed

**Threat:** Agents write directly to knowledge_base/ instead of _PROCESSING/ layers

**Mitigation:**
- Clear instructions: staging → outputs → knowledge_base/ (3-step)
- Agent 3 only writes to outputs/, not knowledge_base/
- Final move: After validation, move outputs → knowledge_base/
- [INFERRED: process discipline required]

### Risk 4: Dimensional Annotation Overload

**Threat:** 165 × 6 = 990 annotation files becomes unmanageable

**Mitigation:**
- Annotations are intermediate working files (can be archived post-processing)
- Agent 3 can optionally skip writing annotations if embedding in nodes directly
- Decision: Create annotations for sample batch (auditability), optional for full corpus
- [INFERRED: flexibility in implementation]

---

## Part 6: Handoff Checklist

**Before starting execution, verify:**

- [ ] Cursor window open in nickel_gtm_context_architecture directory
- [ ] Git status clean (commit any in-progress work)
- [ ] taxonomy.yaml v1.2.0 present (67 patterns)
- [ ] Nickel context docs available in raw_context/
- [ ] 160 remaining transcripts confirmed in raw_context/
- [ ] Agent specifications copied to _AGENT_WORKSPACE/agents/
- [ ] This handoff package read and understood

**During execution, track:**

- [ ] Strategic_lens.yaml created (Phase 0)
- [ ] Sample batch (10 transcripts) processed (Phase 1)
- [ ] Validation Report 1 generated (Checkpoint 1)
- [ ] Decision: GO/NO-GO/ADJUST documented
- [ ] Full corpus (150 transcripts) processed (Phase 2)
- [ ] Validation Report 2 generated (Checkpoint 2)
- [ ] Synthesis documents created (Phase 3)

**After execution, deliverables:**

- [ ] knowledge_base/ updated with all nodes (165 transcripts)
- [ ] taxonomy.yaml final (stable patterns, 85+ stability score)
- [ ] strategic_lens.yaml locked as v2.0
- [ ] _synthesis/ documents created (domain + inter-domain + GTM playbooks)
- [ ] validation_reports/ complete (Report 1 + Report 2)
- [ ] _PROCESSING/ archived (intermediate artifacts preserved for audit)

---

## Part 7: Context References

**Primary Documentation:**
- `NICKEL_STRUCTURE_MAPPING.md` - System architecture and schemas
- `SYSTEM_UPGRADE_PLAN.md` - Detailed retrofit specifications
- `UPGRADE_EXECUTION_OUTLINE.md` - ADD/REFACTOR/KEEP checklist
- `PRACTICAL_EXECUTION_PLAN.md` - Simplified pragmatic guide
- `CLAUDE.md` - Project navigation and current status
- `FOUNDATION_STATUS.md` - Iteration 1 baseline metrics

**SOP References:**
- `_system/workflows/agent_orchestration_patterns_sop.md` - Layer-Based (SOP 2) + Evidence Attribution (SOP 4)

**Agent Specifications:**
- `knowledge_base/research/meta_analysis/knowledge_graph_nucleation/02_agent_library/who_extractor.md`
- [5 more dimension extractors with same structure]

**Evidence:**
- [VERIFIED: All file references above] - Documentation exists and current
- [INFERRED: Multi-agent orchestration patterns] - Applied from SOP 2 + SOP 4
- [UNKNOWN: Execution timeline variance] - 50-60 hours estimate, actual may vary based on transcript complexity

---

**Handoff Status:** READY FOR EXECUTION
**Next Agent:** Execution Orchestrator (Cursor Window)
**Next Action:** Session 1 - Strategic Lens Creation (60-90 min)
**Pattern:** Layer-Based + Evidence Attribution (SOP 2 + SOP 4)
**Success Metric:** Complete knowledge graph with 85+ stability, 85%+ quality, VERIFIED/INFERRED/UNKNOWN attribution compliance
