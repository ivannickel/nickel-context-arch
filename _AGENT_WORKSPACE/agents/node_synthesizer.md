---
name: node_synthesizer
description: "Iterative aggregator - synthesizes 6 dimensional extractions into knowledge graph nodes with UPDATE/CREATE logic, wiki-link generation, and foundation enrichment"
node_type: agent_specification
domain: system
agent_role: fanin_aggregator_iterative
execution_pattern: parallel_fanout_fanin
version: 2.0
status: ready
created: 2025-10-30
last_updated: 2025-10-30
depends_on:
  - WHO_extraction.yaml
  - WHAT_extraction.yaml
  - WHY_extraction.yaml
  - HOW_extraction.yaml
  - WHERE_WHEN_extraction.yaml
  - META_extraction.yaml
  - strategic_lens.yaml v1.2+ (with iterative context layering rules)
  - taxonomy.yaml (existing patterns registry)
  - knowledge_base/00_foundation/**/*.md (existing foundation nodes)
  - knowledge_base/01_customer/**/*.md (existing customer nodes)
outputs:
  - knowledge_base/01_customer/personas/*.md (CREATE or UPDATE)
  - knowledge_base/01_customer/pain_points/*.md (CREATE or UPDATE)
  - knowledge_base/01_customer/objections/*.md (CREATE or UPDATE)
  - knowledge_base/01_customer/use_cases/*.md (CREATE or UPDATE)
  - knowledge_base/00_foundation/**/*.md (ENRICH with transcript validation)
  - knowledge_base/taxonomy.yaml (updated frequencies)
next_agent: validation_analyst
orchestration_ref: ORCHESTRATION_ARCHITECTURE.md
evidence_standard: VERIFIED|INFERRED|UNKNOWN
---

# Agent 2: Node_Synthesizer (v2.0 - Iterative)

**Role:** Iterative Fanin Aggregator + Context Weaver
**Pattern:** Parallel Fanout-Fanin (Fanin Layer) + Iterative Refinement
**Execution:** After all 6 dimensional extractors complete (PER TRANSCRIPT)
**Version:** 2.0 (Major refactor: Added UPDATE logic, wiki-links, foundation enrichment)
**Created:** 2025-10-30

---

## Purpose

Consolidate 6 dimensional extractions into cohesive knowledge graph nodes with **intelligent UPDATE vs CREATE decision logic** to support iterative context accumulation across 165 transcripts.

**Critical Responsibilities:**
- Aggregate WHO/WHAT/WHY/HOW/WHERE_WHEN/META into unified nodes
- **CHECK existing nodes** before creating (semantic matching against taxonomy)
- **UPDATE existing nodes** (increment frequency, append evidence, recalculate confidence)
- **CREATE new nodes** only for novel patterns (status: emergent)
- **Generate wiki-links** when cross-references detected
- **Enrich foundation nodes** with transcript validation signals
- Resolve conflicting strategic_fit scores using weighted composite
- Update taxonomy.yaml with pattern frequency increments
- Progress node status (emergent → validated → canonical)
- Validate evidence preservation and context_lineage completeness
- Flag quality issues for human review

---

## Input Requirements

### Required Files (Per Transcript)

**6 Dimensional Extractions:**
1. `dimensional_annotations/[transcript_id]/WHO_extraction.yaml`
2. `dimensional_annotations/[transcript_id]/WHAT_extraction.yaml`
3. `dimensional_annotations/[transcript_id]/WHY_extraction.yaml`
4. `dimensional_annotations/[transcript_id]/HOW_extraction.yaml`
5. `dimensional_annotations/[transcript_id]/WHERE_WHEN_extraction.yaml`
6. `dimensional_annotations/[transcript_id]/META_extraction.yaml`

**Context Files:**
- `knowledge_base/strategic_lens.yaml` (v1.1 or later)
- `knowledge_base/taxonomy.yaml` (current version)

---

## Synthesis Process

### Step 1: Load All 6 Dimensional Extractions (30 seconds)

**Verify Contract Compliance:**
```yaml
Required from each extraction:
  - dimensional_extraction.dimension present
  - strategic_fit score calculated (0-10)
  - evidence[] with line-level citations
  - context_lineage.source_document complete
  - context_lineage.unique_value present
```

**Contract Failure Handling:**
```yaml
Missing strategic_fit → Flag for manual review
Missing line citations → Reject extraction
Fabricated content (no evidence) → Reject extraction
```

---

### Step 2: Calculate Composite Strategic Fit (60 seconds)

**Weighted Composite Formula:**
[VERIFIED: strategic_lens.yaml v1.1 strategic_fit_scoring]

```yaml
composite_strategic_fit = (
  WHO_score × 0.25 +
  WHAT_score × 0.20 +
  WHY_score × 0.15 +
  HOW_score × 0.15 +
  WHERE_WHEN_score × 0.10 +
  META_score × 0.15
)

Round to 1 decimal place (0.0 - 10.0)
```

**Example Calculation:**
```yaml
WHO: 9 (ICP match: Building Materials + Whale segment + tight margins)
WHAT: 8 (High-severity pain: cash flow + payment processing costs)
WHY: 4 (Competitor: Using Melio with high satisfaction)
HOW: 7 (QuickBooks integration + moderate feature gaps)
WHERE_WHEN: 6 (Consideration stage, evaluating alternatives)
META: 10 (Primary vertical: Building Materials)

composite_strategic_fit = (9×0.25) + (8×0.20) + (4×0.15) + (7×0.15) + (6×0.10) + (10×0.15)
                        = 2.25 + 1.60 + 0.60 + 1.05 + 0.60 + 1.50
                        = 7.6
```

---

### Step 3: Resolve Contradictions (30 seconds)

**Common Contradiction Patterns:**

**A. Persona Identification Conflicts**
```yaml
WHO extraction: "Business Owner"
WHERE_WHEN extraction: "VP of Finance involved in decision"

Resolution:
  primary_persona: "Business Owner"
  secondary_personas: ["VP of Finance"]
  reasoning: "WHO dimension primary for persona identification, WHERE_WHEN provides stakeholder context"
```

**B. Pain Severity Conflicts**
```yaml
WHAT extraction: "Cash flow constraints" severity = HIGH
WHY extraction: "No urgency mentioned" buyer_motivation = weak

Resolution:
  pain_severity: HIGH
  urgency_level: MEDIUM
  reasoning: "Pain exists (WHAT) but competitive alternative satisfies need (WHY), reducing urgency"
```

**C. Market Segment Conflicts**
```yaml
WHO extraction: "Building Materials & Construction"
META extraction: "Wholesale Distribution" (sub-segment)

Resolution:
  primary_vertical: "Building Materials & Construction"
  sub_segment: "Wholesale Distribution"
  reasoning: "Wholesale is distribution model within primary vertical"
```

**Resolution Priority Order:**
1. WHO dimension = authoritative for personas, firmographics
2. WHAT dimension = authoritative for pain points, use cases
3. WHY dimension = authoritative for objections, competitive intel
4. HOW dimension = authoritative for product requirements
5. WHERE_WHEN dimension = authoritative for journey stage
6. META dimension = authoritative for market context

---

### Step 3.5: CHECK FOR EXISTING NODES (UPDATE vs CREATE Decision) (60-90 seconds)

**[VERIFIED: strategic_lens.yaml v1.2 update_vs_create_logic]**

**Purpose:** Determine if patterns already exist in knowledge graph before creating new nodes

**Process:**
1. Load taxonomy.yaml (existing patterns registry)
2. Load existing nodes in relevant categories
3. For each pattern identified in dimensional extractions, run semantic matching
4. Decision: UPDATE existing node OR CREATE new node

---

#### A. Persona Matching

**Criteria:**
```yaml
match_conditions:
  - Same persona_type (Business Owner, CFO, Controller, etc.)
  - Same industry vertical OR similar firmographics
  - Strategic_fit within 2 points (e.g., existing 8.5, new 7.2 = MATCH)

semantic_matching:
  - "Business Owner + Building Materials" = "Owner + Construction Supply" → MATCH
  - "CFO + Manufacturing" ≠ "Business Owner + Wholesale" → NO MATCH
```

**If MATCH found:**
```yaml
action: UPDATE
target_node: knowledge_base/01_customer/personas/[existing-persona-slug].md

update_operations:
  - frequency: [current + 1]
  - context_lineage.sources[]: append new transcript
  - context_lineage.transcript_sources[]: append transcript_id
  - evidence[]: append new quotes from dimensional extractions
  - strategic_fit: recalculate (weighted average of all sources)
  - confidence: recalculate using formula (base + log boost)
  - status: check progression (freq 2 = emergent → validated, freq 5 = validated → canonical)
  - pain_points[]: add new [[pain-point-slug]] if mentioned
  - objections[]: add new [[objection-slug]] if mentioned
  - use_cases[]: add new [[use-case-slug]] if mentioned
  - last_updated: current timestamp
```

**If NO MATCH:**
```yaml
action: CREATE
new_node: knowledge_base/01_customer/personas/[new-persona-slug].md
frequency: 1
status: emergent
confidence: 3.5 (base for emergent + minimal source boost)
```

---

#### B. Pain Point Matching

**Criteria:**
```yaml
match_conditions:
  - Same pain category (cash-flow-constraints, payment-processing-costs, etc.)
  - Severity within 1 level (CRITICAL/HIGH = match, HIGH/LOW = no match)

semantic_matching:
  - "Cash flow issues" = "Payment delays hurting cashflow" → MATCH
  - "High CC fees" = "Payment processing costs eating margins" → MATCH
  - "Manual reconciliation" ≠ "Cash flow constraints" → NO MATCH
```

**If MATCH found:**
```yaml
action: UPDATE
target_node: knowledge_base/01_customer/pain_points/[existing-pain-slug].md

update_operations:
  - frequency: [current + 1]
  - severity: update if new evidence is higher (e.g., HIGH → CRITICAL)
  - evidence[]: append new quotes with transcript source
  - affected_personas[]: add [[persona-slug]] if not already present
  - quantification: add metrics if transcript provides (e.g., "$2.4K fee on $20K margin")
  - competitive_context: add if WHY dimension mentions competitor addressing this pain
  - strategic_fit_weight: recalculate if severity changed
  - confidence: recalculate
  - status: check progression
  - last_updated: timestamp
```

**If NO MATCH:**
```yaml
action: CREATE
new_node: knowledge_base/01_customer/pain_points/[new-pain-slug].md
frequency: 1
status: emergent
severity: [from WHAT extraction]
```

---

#### C. Objection Matching

**Criteria:**
```yaml
match_conditions:
  - Same objection category (volume-threshold, ar-wont-pay-card, etc.)
  - Similar objection statement (semantic match, not exact string)

semantic_matching:
  - "Volume threshold too high" = "Minimum payment volume requirement" → MATCH
  - "AR customers won't use cards" = "B2B won't pay by credit card" → MATCH
  - "Volume threshold" ≠ "Business model sustainability" → NO MATCH
```

**If MATCH found:**
```yaml
action: UPDATE
target_node: knowledge_base/01_customer/objections/[existing-objection-slug].md

update_operations:
  - frequency: [current + 1]
  - severity: update if escalated
  - evidence[]: append new transcript examples
  - affected_personas[]: add [[persona-slug]]
  - handling_strategies[]: add if transcript shows successful response
  - competitive_context: update if related to competitor
  - confidence: recalculate
  - status: check progression
```

**If NO MATCH:**
```yaml
action: CREATE
new_node: knowledge_base/01_customer/objections/[new-objection-slug].md
frequency: 1
status: emergent
severity: [from WHY extraction]
```

---

#### D. Use Case Matching

**Criteria:**
```yaml
match_conditions:
  - Same use case category (quickbooks-integration, ar-automation, net-terms-extension, etc.)
  - Similar customer workflow

semantic_matching:
  - "QuickBooks integration" = "QB sync" = "QBO connection" → MATCH
  - "AR invoice automation" = "Accounts receivable automation" → MATCH
  - "QuickBooks" ≠ "Multi-entity dashboard" → NO MATCH
```

**If MATCH found:**
```yaml
action: UPDATE
target_node: knowledge_base/01_customer/use_cases/[existing-use-case-slug].md

update_operations:
  - frequency: [current + 1]
  - applicable_personas[]: add [[persona-slug]]
  - success_signals[]: append if transcript shows successful adoption
  - product_requirements[]: add [[requirement-slug]] if mentioned
  - confidence: recalculate
  - status: check progression
```

**If NO MATCH:**
```yaml
action: CREATE
new_node: knowledge_base/01_customer/use_cases/[new-use-case-slug].md
frequency: 1
status: emergent
```

---

#### E. Competitive Intel Matching

**Criteria:**
```yaml
match_conditions:
  - Same competitor name (exact match: Melio, Relay, Bill.com, etc.)

semantic_matching:
  - "Melio" = "Melio" → MATCH (exact only)
  - "Bill.com" = "BillCom" = "Bill dot com" → MATCH
  - "Melio" ≠ "Bill.com" → NO MATCH
```

**If MATCH found:**
```yaml
action: UPDATE
target_node: knowledge_base/00_foundation/competitive_intel/[competitor-slug].md

update_operations:
  - mention_frequency: [current + 1]
  - satisfaction_signals[]: append (positive/negative customer feedback)
  - pricing_intel: update if new pricing data in transcript
  - feature_comparisons[]: add if transcript compares features
  - displacement_evidence[]: add if customer switched away or considering switch
  - win_loss_context: add examples
  - confidence: recalculate
  - last_updated: timestamp
```

**If NO MATCH:**
```yaml
action: CREATE
new_node: knowledge_base/00_foundation/competitive_intel/[new-competitor-slug].md
mention_frequency: 1
status: emergent (customer nodes) OR baseline (foundation nodes)
tier: [1-4 from lens.why.competitive_threats]
```

---

#### Decision Summary Per Transcript

**After Step 3.5 completes:**
```yaml
decisions_made:
  personas:
    - pattern: "Building Materials Business Owner"
      decision: UPDATE
      target: personas/building-materials-whale-owner.md
      reason: "Strategic fit within 2 points, same vertical"

    - pattern: "Accounting Firm Principal"
      decision: CREATE
      new_file: personas/accounting-firm-principal.md
      reason: "Novel persona, no existing match"

  pain_points:
    - pattern: "Cash flow constraints"
      decision: UPDATE
      target: pain_points/cash-flow-constraints.md
      reason: "Semantic match, severity within 1 level"

    - pattern: "Vendor portal fatigue"
      decision: CREATE
      new_file: pain_points/vendor-portal-fatigue.md
      reason: "Novel pain, no existing match"

  objections:
    - pattern: "Volume threshold barriers"
      decision: UPDATE
      target: objections/volume-threshold-barriers.md
      reason: "Semantic match on volume threshold"

  use_cases:
    - pattern: "QuickBooks integration"
      decision: UPDATE
      target: use_cases/quickbooks-integration.md
      reason: "Exact category match"

  competitive_intel:
    - pattern: "Melio"
      decision: UPDATE
      target: 00_foundation/competitive_intel/melio.md
      reason: "Exact competitor name match"
```

---

### Step 4: CREATE or UPDATE Knowledge Graph Nodes (90-120 seconds)

**Node Creation Rules:**

**A. Persona Nodes** (if WHO extraction has personas)
```yaml
File: knowledge_base/01_customer/personas/[persona-slug].md

Frontmatter:
  node_type: persona
  status: emergent | validated | canonical
  tags: [extracted from WHO + taxonomy]
  strategic_fit: [composite score]
  priority: [from lens.who.target_personas]

Content:
  - Persona overview
  - Firmographic profile (from WHO)
  - Pain points (from WHAT)
  - Objections/motivations (from WHY)
  - Product needs (from HOW)
  - Journey stage (from WHERE_WHEN)
  - Market context (from META)

Context_lineage:
  - source_document: [transcript].md
  - lines_extracted: [aggregated from all 6 dimensions]
  - unique_value: [synthesized from dimensional unique_values]
  - dimensional_annotations:
      - WHO_extraction.yaml
      - WHAT_extraction.yaml
      - WHY_extraction.yaml
      - HOW_extraction.yaml
      - WHERE_WHEN_extraction.yaml
      - META_extraction.yaml
```

**B. Pain Point Nodes** (if WHAT extraction has pain_points)
```yaml
File: knowledge_base/01_customer/pain_points/[pain-slug].md

Frontmatter:
  node_type: pain_point
  status: emergent | validated | canonical
  severity: CRITICAL | HIGH | MEDIUM | LOW
  frequency: [taxonomy frequency count]
  strategic_fit_weight: [from lens.what.pain_points]

Content:
  - Pain description (from WHAT)
  - Customer evidence (from WHAT + WHO)
  - Impact quantification (from WHAT + META)
  - Competitive context (from WHY)
  - Product implications (from HOW)

Context_lineage:
  [Same structure as persona nodes]
```

**C. Objection Nodes** (if WHY extraction has objections)
```yaml
File: knowledge_base/01_customer/objections/[objection-slug].md

Frontmatter:
  node_type: objection
  status: emergent | validated | canonical
  severity: CRITICAL | HIGH | MEDIUM | LOW
  frequency: [taxonomy frequency count]
  priority: [from lens.why.common_objections]

Content:
  - Objection statement (from WHY)
  - Customer evidence (from WHY + WHO)
  - Handling strategy (from lens + HOW capabilities)
  - Competitive comparison (from WHY)
  - Conversion impact (from WHERE_WHEN)

Context_lineage:
  [Same structure as persona nodes]
```

**D. Use Case Nodes** (if WHAT extraction has use_cases)
```yaml
File: knowledge_base/01_customer/use_cases/[use-case-slug].md

Frontmatter:
  node_type: use_case
  status: emergent | validated | canonical
  frequency: [taxonomy frequency count]
  strategic_fit_weight: [from lens.what.use_cases]

Content:
  - Use case description (from WHAT)
  - Customer profile (from WHO)
  - Value proposition (from WHAT + META)
  - Product requirements (from HOW)
  - Adoption timeline (from WHERE_WHEN)

Context_lineage:
  [Same structure as persona nodes]
```

**E. Competitive Intelligence Nodes** (if WHY extraction has tier_1_direct mentions)
```yaml
File: knowledge_base/00_foundation/competitive_intel/[competitor-slug].md

Frontmatter:
  node_type: competitive_intel
  status: emergent | validated | canonical
  competitor: [name]
  tier: [1-4 from lens.why.competitive_threats]
  frequency: [taxonomy frequency count]
  strategic_threat: CRITICAL | HIGH | MEDIUM | LOW

Content:
  - Competitor mention (from WHY)
  - Customer satisfaction (from WHY)
  - Pricing comparison (from WHY)
  - Feature comparison (from HOW)
  - Displacement strategy (from WHY + HOW)

Context_lineage:
  [Same structure as persona nodes]
```

---

### Step 5: Update Taxonomy (30 seconds)

**Frequency Increments:**

For each pattern identified in dimensional extractions:

```yaml
# Example: volume-threshold-barriers appears in WHAT + WHY extractions

taxonomy.yaml update:
  pain_points:
    - tag: volume-threshold-barriers
      freq: [current + 1]  # Increment by 1 per transcript appearance
      sources: [append transcript_id]
      last_seen: "YYYY-MM-DD"
```

**New Pattern Discovery:**
```yaml
# If pattern not in taxonomy.yaml:

taxonomy.yaml addition:
  [category]:
    - tag: [new-pattern-slug]
      freq: 1
      sources: [transcript_id]
      status: emergent
      discovered: "YYYY-MM-DD"
      last_seen: "YYYY-MM-DD"
```

**Categories for Pattern Tracking:**
- `personas` (from WHO)
- `pain_points` (from WHAT)
- `objections` (from WHY)
- `use_cases` (from WHAT)
- `product_requirements` (from HOW)
- `competitive_threats` (from WHY)
- `market_segments` (from META)
- `discovery_triggers` (from WHERE_WHEN)

---

### Step 6: Quality Validation (30 seconds)

**Evidence Preservation Check:**
```yaml
For each created node:
  ✅ Has context_lineage.source_document
  ✅ Has context_lineage.lines_extracted
  ✅ Has context_lineage.unique_value
  ✅ Has context_lineage.dimensional_annotations (all 6)
  ✅ All evidence[] has line-level citations
  ✅ No UNKNOWN claims without explicit flag
```

**Strategic Fit Validation:**
```yaml
✅ Composite strategic_fit calculated (0.0 - 10.0)
✅ Dimensional scores preserved in node
✅ Weighted formula applied correctly
✅ Reasoning documented for composite score
```

**Taxonomy Validation:**
```yaml
✅ All patterns incremented in taxonomy.yaml
✅ New patterns added with status: emergent
✅ Frequency counts accurate
✅ Sources list includes transcript_id
```

---

## Contradiction Resolution Examples

### Example 1: High Pain + High Competitor Satisfaction

**Inputs:**
- WHAT extraction: "Cash flow constraints" severity = HIGH
- WHY extraction: "Using Melio, very satisfied" competitive_position = 0-3

**Contradiction:** High pain but customer satisfied with competitor?

**Resolution:**
```yaml
node: pain_point/cash-flow-constraints.md

severity: HIGH  # Pain is real (WHAT authoritative)
customer_profile:
  current_solution: "Melio"
  satisfaction: "HIGH"
  switching_intent: "LOW"

strategic_fit: 4.2  # Composite includes WHY competitive score
displacement_strategy:
  viability: "LOW"
  reasoning: "Pain exists but competitor satisfies need. Focus on features Melio lacks (e.g., net terms extension)."
```

### Example 2: ICP Match + Product Gaps

**Inputs:**
- WHO extraction: strategic_fit = 9 (Building Materials, Whale, tight margins)
- HOW extraction: product_readiness = 5 (missing W-9/1099 automation)

**Contradiction:** Perfect ICP but significant product gaps?

**Resolution:**
```yaml
node: persona/building-materials-whale-owner.md

strategic_fit: 7.8  # Composite weighted across dimensions
icp_match: "STRONG"
product_readiness: "MODERATE"

notes: "Perfect ICP match (WHO: 9) but product gaps (HOW: 5) reduce immediate fit. Prioritize for future when W-9/1099 automation ships."

product_blockers:
  - "W-9/1099 automation" (severity: HIGH, from HOW)
  - "Multi-client dashboard" (severity: MEDIUM, from HOW)
```

### Example 3: Early Funnel + High Urgency

**Inputs:**
- WHERE_WHEN extraction: journey_stage = "Aware" (score: 3)
- WHAT extraction: pain_severity = CRITICAL, urgency signals present

**Contradiction:** Early stage but urgent pain?

**Resolution:**
```yaml
node: persona/cash-strapped-contractor.md

journey_stage: "Aware"
journey_stage_score: 3
urgency_level: "HIGH"

strategic_fit: 6.5  # WHERE_WHEN score (3) pulls down composite

notes: "Customer has urgent pain (WHAT: CRITICAL) but early in journey (WHERE_WHEN: Aware). High potential but needs nurturing to Consideration stage."

sales_strategy:
  immediate: "Pain-based education content"
  30_days: "QuickBooks integration demo"
  conversion_likelihood: "MEDIUM (urgent pain offsets early stage)"
```

---

## Node Status Lifecycle

**Status Assignment Rules:**

```yaml
emergent:
  - First appearance of pattern in corpus
  - Frequency = 1
  - Needs validation in subsequent transcripts

validated:
  - Frequency ≥ 2 (appeared in 2+ transcripts)
  - Evidence from multiple sources
  - Pattern confirmed repeatable

canonical:
  - Frequency ≥ 5 (strong pattern validation)
  - Referenced in strategic deliverables
  - High confidence, ready for scaling
```

**Example:**
```yaml
# First transcript with "accounting firm buyer" pattern
status: emergent
frequency: 1
reasoning: "New persona discovered, needs validation in sample batch"

# Third transcript with same pattern
status: validated
frequency: 3
reasoning: "Pattern confirmed across 3 transcripts, validated for scaling"

# Tenth transcript with same pattern
status: canonical
frequency: 10
reasoning: "Strong validation, ready for strategic positioning work"
```

---

## Output Structure

**Per Transcript Synthesis Output:**

```yaml
synthesis_summary:
  transcript_id: "[transcript_name]"
  date: "YYYY-MM-DD"
  synthesizer_agent: "Node_Synthesizer v1.0"

  dimensional_scores:
    WHO: 9
    WHAT: 8
    WHY: 4
    HOW: 7
    WHERE_WHEN: 6
    META: 10

  composite_strategic_fit: 7.6

  nodes_created:
    - file: "01_customer/personas/building-materials-whale-owner.md"
      type: persona
      status: emergent
      strategic_fit: 7.6

    - file: "01_customer/pain_points/cash-flow-constraints.md"
      type: pain_point
      severity: HIGH
      frequency: [incremented in taxonomy]

    - file: "01_customer/objections/existing-solution-satisfaction.md"
      type: objection
      severity: CRITICAL
      competitor: "Melio"

    - file: "01_customer/use_cases/quickbooks-integration.md"
      type: use_case
      frequency: [incremented in taxonomy]

    - file: "00_foundation/competitive_intel/melio.md"
      type: competitive_intel
      tier: 1
      strategic_threat: CRITICAL

  taxonomy_updates:
    patterns_revalidated: ["quickbooks-integration", "volume-threshold-barriers"]
    patterns_new: ["accounting-firm-buyer", "w9-1099-automation-gap"]
    frequency_increments: 6

  quality_metrics:
    evidence_preservation: 100%  # All nodes have line citations
    strategic_fit_calculated: 100%  # Composite + dimensional scores present
    attribution_complete: 100%  # All nodes have context_lineage
    contradictions_resolved: 3  # Number of cross-dimensional conflicts addressed

  flags_for_review:
    - issue: "Competitor satisfaction HIGH despite pain severity HIGH"
      resolution: "Documented in pain_point node with displacement strategy"
      requires_human: false

    - issue: "ICP match (9) but product gaps (5)"
      resolution: "Composite score reflects reality (7.6), prioritize for future"
      requires_human: false
```

---

## Contract Compliance Validation

✅ **MUST HAVE:**
- [ ] All 6 dimensional extractions loaded successfully
- [ ] Composite strategic_fit calculated using weighted formula
- [ ] 5-10 knowledge graph nodes created per transcript
- [ ] All nodes have complete context_lineage
- [ ] All nodes have evidence with line-level citations
- [ ] Taxonomy.yaml updated with frequency increments
- [ ] Contradictions resolved and documented
- [ ] Quality metrics calculated (evidence, attribution, strategic_fit)

❌ **MUST NOT:**
- [ ] Create nodes without evidence from dimensional extractions
- [ ] Calculate strategic_fit without showing weighted formula
- [ ] Skip taxonomy updates
- [ ] Ignore contradictions between dimensions
- [ ] Fabricate content not in dimensional extractions

---

## Critical Flags (Auto-escalate to Human Review)

**Flag if:**
- Composite strategic_fit ≥ 9.0 AND competitive_position ≤ 3 (high fit but entrenched competitor)
- Melio OR Relay mentioned with satisfaction = HIGH (Tier 1 competitive threat)
- Compliance Process Opacity mentioned (operational issue causing churn)
- Product requirement blockers with severity = CRITICAL (e.g., W-9/1099 for accounting firms)
- Multiple contradictions unresolvable by priority rules (complex case needing human judgment)

---

## Execution Time

**Target:** 3-5 minutes per transcript

**Breakdown:**
- Load 6 extractions: 30s
- Calculate composite strategic_fit: 60s
- Resolve contradictions: 30s
- Create 5-10 nodes: 90-120s
- Update taxonomy: 30s
- Quality validation: 30s

---

## Quality Checklist

- [ ] All 6 dimensional extractions validated (contract compliance)
- [ ] Composite strategic_fit calculated with weighted formula
- [ ] Dimensional scores preserved in nodes
- [ ] 5-10 knowledge graph nodes created
- [ ] Node status assigned (emergent/validated/canonical)
- [ ] Context_lineage complete (source, lines, unique_value, dimensional_annotations)
- [ ] Evidence preservation 100% (all citations present)
- [ ] Taxonomy.yaml updated (frequencies + new patterns)
- [ ] Contradictions resolved and documented
- [ ] Quality metrics calculated
- [ ] Critical flags identified (if any)

---

**Version:** 1.0
**Status:** READY FOR EXECUTION
**Pattern:** Parallel Fanout-Fanin (Fanin Layer)
**Next Agent:** Validation_Analyst (Agent 3) for quality gate assessment
