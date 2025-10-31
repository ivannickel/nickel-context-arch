# Nickel GTM Context Architecture - Multi-Agent Orchestration

**Version:** 1.0
**Created:** 2025-10-30
**Pattern Framework:** Sequential Cascade + Parallel Fanout-Fanin + Iterative Refinement
**Evidence Attribution:** [VERIFIED: agent_orchestration_patterns research kit]

---

## Architecture Overview

### Pattern Selection Rationale

**Primary Pattern: Pattern 4 - Parallel Fanout-Fanin** [VERIFIED: undiscovered_orchestration_patterns.md:27]
- **Why:** 6 dimensional extractors analyze SAME transcript from orthogonal perspectives
- **Benefit:** Reduces per-transcript time from 90 min (sequential) → 15 min (parallel)
- **Implementation:** WHO/WHAT/WHY/HOW/WHERE_WHEN/META agents run concurrently

**Secondary Pattern: Pattern 1 - Sequential Cascade** [VERIFIED: discovered_patterns.md:7]
- **Why:** Phase progression requires predecessor completion (lens → sample → validation → corpus)
- **Benefit:** Clear validation gates, progressive context deepening
- **Implementation:** Phase 0 → Phase 1 → Checkpoint 1 → Phase 2 → Checkpoint 2

**Tertiary Pattern: Pattern 5 - Iterative Refinement Loop** [VERIFIED: undiscovered_orchestration_patterns.md:78]
- **Why:** Sample batch validation may require lens refinement
- **Benefit:** Quality-gated iteration prevents scaling with bad lens
- **Implementation:** If checkpoint fails (quality < 85%), refine lens + retry sample batch

---

## 8-Agent Suite Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 0: STRATEGIC LENS (Sequential - COMPLETE)                 │
│                                                                   │
│ Agent 0: Strategic Lens Builder                                  │
│ ├─ Input:  68 raw_context GTM docs + Ivan transcript            │
│ ├─ Output: strategic_lens.yaml v1.1                             │
│ └─ Status: ✅ COMPLETE                                           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 1: DIMENSIONAL EXTRACTION (Parallel Fanout-Fanin)         │
│                                                                   │
│ Per-Transcript Loop (10-20 transcripts for sample batch):       │
│                                                                   │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │ Fanout: 6 Parallel Dimensional Extractors                │  │
│   │                                                           │  │
│   │  Agent 1a: WHO_Extractor      (personas, buyers)        │  │
│   │  Agent 1b: WHAT_Extractor     (pains, use cases)        │  │
│   │  Agent 1c: WHY_Extractor      (objections, competitive) │  │
│   │  Agent 1d: HOW_Extractor      (product requirements)    │  │
│   │  Agent 1e: WHERE_WHEN_Extract (journey stage)           │  │
│   │  Agent 1f: META_Extractor     (market context)          │  │
│   │                                                           │  │
│   │  All read: strategic_lens.yaml + single transcript       │  │
│   │  Time per agent: 2-3 min (parallel execution)            │  │
│   └──────────────────────────────────────────────────────────┘  │
│                              ↓                                    │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │ Fanin: Node Synthesizer                                  │  │
│   │                                                           │  │
│   │  Agent 2: Node_Synthesizer                               │  │
│   │  ├─ Input:  6 dimensional extractions                    │  │
│   │  ├─ Output: 5-10 knowledge graph nodes → knowledge_base/ │  │
│   │  └─ Time:   3-5 min per transcript                       │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                   │
│ Total per transcript: 15-20 min (vs 90 min sequential)          │
│ Total for 10 transcripts: 2.5-3.5 hours                         │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ CHECKPOINT 1: VALIDATION GATE (Iterative Refinement)            │
│                                                                   │
│ Agent 3: Validation_Analyst                                      │
│ ├─ Input:  50-100 nodes from sample batch                       │
│ │          taxonomy.yaml updates                                 │
│ │          Pattern frequency changes                             │
│ ├─ Output: Validation report (GO/NO-GO decision)                │
│ │          - Pattern revalidation rate ≥60%                     │
│ │          - New discovery rate ≥20%                            │
│ │          - Quality maintained ≥85%                            │
│ └─ Time:   30-60 min                                             │
│                                                                   │
│ Decision:                                                         │
│   ✅ GO: Proceed to Phase 2 (full corpus)                        │
│   🔄 REFINE: Update strategic_lens.yaml, retry sample batch     │
│   ❌ NO-GO: Fix quality/attribution issues                       │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    [IF GO: Proceed to Phase 2]
                    [IF REFINE: Iteration loop back to Phase 1]
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 2: FULL CORPUS (Repeat Phase 1 pattern for 140-150)      │
│                                                                   │
│ Repeat Agents 1a-1f → Agent 2 loop for remaining transcripts    │
│ Time: 35-45 hours (10-15 sessions)                              │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ CHECKPOINT 2: FINAL VALIDATION                                   │
│                                                                   │
│ Agent 3: Validation_Analyst (rerun on full corpus)              │
│ └─ Output: Final quality report, synthesis readiness            │
└─────────────────────────────────────────────────────────────────┘
```

---

## Agent Role Taxonomy

### Agent 0: Strategic Lens Builder (Foundation Layer)
**Pattern:** Sequential Cascade - Layer 0 (Foundation)
**Role:** Context Consolidator
**Status:** ✅ COMPLETE
**Output:** [strategic_lens.yaml](../../knowledge_base/strategic_lens.yaml) v1.1

---

### Agents 1a-1f: Dimensional Extractors (Parallel Layer)
**Pattern:** Parallel Fanout-Fanin - Fanout
**Role:** Specialized Extractors (orthogonal dimensions)

**Shared Characteristics:**
- **Input:** strategic_lens.yaml + single transcript
- **Execution:** Concurrent (true parallelism, no inter-agent dependencies)
- **Output:** Dimensional annotation YAML + direct node creation
- **Time:** 2-3 min per agent (parallel)
- **Attribution:** VERIFIED (direct quotes), INFERRED (calculated scores), UNKNOWN (needs validation)

**Individual Roles:**

| Agent | Dimension | Focus | Output |
|-------|-----------|-------|--------|
| **1a: WHO_Extractor** | WHO | Personas, company profiles, buyer characteristics, firmographics | Persona nodes, company context |
| **1b: WHAT_Extractor** | WHAT | Pain points, use cases, product fit signals | Pain point nodes, use case nodes |
| **1c: WHY_Extractor** | WHY | Objections, competitive mentions, buyer motivations | Objection nodes, competitive intel |
| **1d: HOW_Extractor** | HOW | Product requirements, feature requests, integration needs | Product requirement nodes |
| **1e: WHERE_WHEN_Extractor** | WHERE_WHEN | Journey stage, discovery triggers, conversion funnel position | Journey stage nodes |
| **1f: META_Extractor** | META | Market context, segment insights, trends | Market intelligence nodes |

---

### Agent 2: Node_Synthesizer (Fanin Layer)
**Pattern:** Parallel Fanout-Fanin - Fanin
**Role:** Aggregator + Quality Validator

**Function:**
- Consolidates 6 dimensional extractions
- Resolves contradictions (e.g., conflicting strategic_fit scores)
- Creates/updates knowledge graph nodes
- Updates taxonomy.yaml with pattern frequencies
- Validates context_lineage completeness

**Input:** 6 dimensional annotation YAMLs (from Agents 1a-1f)
**Output:** 5-10 knowledge graph nodes in domain directories
**Time:** 3-5 min per transcript

---

### Agent 3: Validation_Analyst (Quality Gate)
**Pattern:** Iterative Refinement Loop - Validation Gate
**Role:** Quality Assessor + Decision Gate

**Function:**
- Measures pattern revalidation rate (did Iteration 1 patterns reappear?)
- Measures new discovery rate (novel patterns emerged?)
- Assesses quality (attribution complete? strategic_fit calculated?)
- Generates GO/NO-GO decision for scaling
- If NO-GO: Identifies lens refinements needed

**Input:** Batch of 50-100 nodes + taxonomy.yaml updates
**Output:** Validation report + scaling decision
**Time:** 30-60 min per checkpoint

---

## Contract Specifications

### Agent 1a → Agent 2 Contract (WHO Dimension)

**MUST_PROVIDE:**
```yaml
dimensional_extraction:
  dimension: "WHO"
  personas_extracted:
    - name: "<persona name>"
      priority: <1-3 from lens>
      strategic_fit: <0-10 calculated score>
      evidence: [line-level quotes with VERIFIED tag]

  context_lineage:
    source_document:
      file: "<transcript>.md"
      lines_extracted: "<line ranges>"
      unique_value: "<why this source matters>"
```

**VALIDATION:**
- ✅ All personas have strategic_fit score (0-10)
- ✅ All evidence has line-level citations [VERIFIED: file:line]
- ✅ Context_lineage includes unique_value explanation
- ❌ If no personas found: Flag as "No WHO signals in transcript" (not fabricate)

**CONTRACT FAILURE HANDLING:**
- Missing strategic_fit → Agent 2 flags for manual review
- Missing line citations → Agent 2 rejects extraction
- Fabricated personas (no evidence) → Agent 2 rejects extraction

---

### Agent 2 → Agent 3 Contract (Synthesis → Validation)

**MUST_PROVIDE:**
```yaml
nodes_created:
  count: <5-10 per transcript>
  domains: [foundation, customer, product, market]
  attribution_complete: <true/false>

taxonomy_updates:
  patterns_revalidated: [list of freq++ patterns]
  patterns_new: [list of freq=1 patterns]

quality_metrics:
  evidence_preservation: <percentage with line citations>
  strategic_fit_calculated: <percentage with scores>
```

**VALIDATION:**
- ✅ All nodes in correct domain directories
- ✅ All nodes have complete frontmatter (per ontology.yaml)
- ✅ No orphan nodes (all linked to transcripts)
- ✅ Taxonomy.yaml updated with pattern frequencies

---

## Evidence Attribution Standard

**Framework:** [VERIFIED: agent_orchestration_patterns/00_framework/discovered_patterns.md:74]

### Attribution Levels

**VERIFIED:** Direct observation from source
```yaml
evidence:
  - quote: "We have 150 clients across our portfolio"
    location: "hardy-butler-transcript.md:342-345"
    type: "client_count"
    confidence: "VERIFIED"
```

**INFERRED:** Deduced from evidence using lens logic
```yaml
strategic_fit: 9
reasoning: "ICP match (Building Materials + Whale $8M) + tight margins (20%) + small accounting team (3 staff) = score 9"
confidence: "INFERRED from transcript evidence + lens.who.persona_match criteria"
```

**UNKNOWN:** Insufficient data to verify
```yaml
margin_profile: "UNKNOWN"
reasoning: "No cost structure signals in transcript"
needs_validation: true
```

### Anti-Patterns to Avoid

❌ **Silent Assumption**: "They probably have low margins because they're in construction" → Flag as UNKNOWN instead
❌ **Fabrication**: Creating personas with no transcript evidence
❌ **Vague Attribution**: "Mentioned in transcript" → Provide line numbers
❌ **Score Without Logic**: strategic_fit: 8 with no reasoning → Show calculation

---

## Quality Gates & Validation Rules

### Phase 1 → Checkpoint 1 Quality Criteria

**Pattern Revalidation Rate:** ≥60%
- Iteration 1 found 67 patterns
- Sample batch should see ≥40 patterns reappear (freq increase)
- **Pass:** 45 patterns revalidated
- **Fail:** Only 20 patterns revalidated → lens misaligned with corpus

**New Discovery Rate:** ≥20%
- Sample batch should discover ≥13 new patterns (20% of 67)
- **Pass:** 18 new patterns discovered
- **Fail:** Only 3 new patterns → sampling not diverse enough

**Quality Maintained:** ≥85%
- Evidence preservation: ≥90% nodes have line citations
- Strategic_fit calculated: ≥85% extractions have scores
- Attribution complete: ≥85% nodes have context_lineage
- **Pass:** 88% average quality
- **Fail:** 72% average quality → agents not following attribution standard

### Iteration Limits

**Maximum iterations:** 3
- Iteration 1: Initial sample batch
- Iteration 2: Refine lens, retry sample batch
- Iteration 3: Final attempt with refined lens
- If 3rd iteration fails → escalate to human (lens fundamentally misaligned)

---

## Execution Timeline

### Phase 0 (COMPLETE): 2 hours
- ✅ Strategic lens creation (v1.0 + v1.1 with Ivan refinements)

### Phase 1 (Sample Batch): 2.5-3.5 hours
- Select 10 transcripts strategically diverse
- Run 6 dimensional extractors (parallel) per transcript = 15-20 min each
- Total: 10 transcripts × 15-20 min = 2.5-3.5 hours

### Checkpoint 1: 30-60 min
- Validation analysis
- GO/NO-GO decision
- If REFINE: +2-3 hours iteration

### Phase 2 (Full Corpus): 35-45 hours
- 140-150 remaining transcripts
- 10-15 work sessions (3-4 hours each)

### Checkpoint 2: 30-60 min
- Final validation
- Synthesis readiness assessment

**Total Timeline:** 45-55 hours across 10-15 sessions

---

## File Structure

```
_AGENT_WORKSPACE/
├── agents/
│   ├── ORCHESTRATION_ARCHITECTURE.md       # ← This file
│   ├── who_extractor.md                     # Agent 1a spec
│   ├── what_extractor.md                    # Agent 1b spec
│   ├── why_extractor.md                     # Agent 1c spec
│   ├── how_extractor.md                     # Agent 1d spec
│   ├── where_when_extractor.md              # Agent 1e spec
│   ├── meta_extractor.md                    # Agent 1f spec
│   ├── node_synthesizer.md                  # Agent 2 spec
│   └── validation_analyst.md                # Agent 3 spec

knowledge_base/
├── strategic_lens.yaml                      # Agent 0 output (complete)
├── dimensional_annotations/                 # Agents 1a-1f outputs
│   ├── [transcript_id]/
│   │   ├── WHO_extraction.yaml
│   │   ├── WHAT_extraction.yaml
│   │   ├── WHY_extraction.yaml
│   │   ├── HOW_extraction.yaml
│   │   ├── WHERE_WHEN_extraction.yaml
│   │   └── META_extraction.yaml
│   └── ...
├── 00_foundation/                           # Agent 2 outputs (nodes)
├── 01_customer/                             # Agent 2 outputs (nodes)
├── 02_product/                              # Agent 2 outputs (nodes)
├── 03_market/                               # Agent 2 outputs (nodes)
└── taxonomy.yaml                            # Agent 2 updates (pattern frequencies)

_AGENT_WORKSPACE/
└── validation_reports/                      # Agent 3 outputs
    ├── checkpoint_1_sample_batch.md
    └── checkpoint_2_full_corpus.md
```

---

## Next Steps

**Immediate (can proceed in parallel with transcript frontmatter):**
1. Create 8 agent specifications (3-4 hours design work)
2. Set up dimensional_annotations/ directory structure
3. Create validation report templates

**When transcripts ready:**
4. Select 10 strategically diverse transcripts for sample batch
5. Execute Phase 1 (2.5-3.5 hours)
6. Run Checkpoint 1 validation
7. Scale to Phase 2 if passed

---

**Pattern Attribution:**
- [VERIFIED: agent_orchestration_patterns/04_novel_patterns/undiscovered_orchestration_patterns.md:27] Pattern 4: Parallel Fanout-Fanin
- [VERIFIED: agent_orchestration_patterns/00_framework/discovered_patterns.md:7] Pattern 1: Sequential Cascade
- [VERIFIED: agent_orchestration_patterns/04_novel_patterns/undiscovered_orchestration_patterns.md:78] Pattern 5: Iterative Refinement Loop

**Version:** 1.0
**Status:** DESIGN COMPLETE - Ready for agent spec creation
**Created:** 2025-10-30
