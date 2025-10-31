---
name: context_weaver
description: "Periodic agent that builds foundation ↔ customer connections, generates wiki-links, updates validation status, and flags contradictions every 10-20 transcripts"
node_type: agent_specification
domain: system
agent_role: connection_builder
execution_pattern: periodic_enrichment
version: 1.0
status: ready
created: 2025-10-30
last_updated: 2025-10-30
depends_on:
  - knowledge_base/00_foundation/**/*.md (baseline foundation nodes)
  - knowledge_base/01_customer/**/*.md (customer nodes from transcripts)
  - taxonomy.yaml (pattern frequencies)
  - strategic_lens.yaml v1.2+ (foundation_validation_rules, wiki_link_generation)
outputs:
  - knowledge_base/00_foundation/**/*.md (ENRICHED with validation signals)
  - knowledge_base/01_customer/**/*.md (ENRICHED with foundation context)
  - All nodes updated with wiki-links [[node-slug]]
  - Contradiction flags added where evidence conflicts
  - Node status progression (baseline → validating → validated → canonical)
next_agent: validation_analyst (at checkpoint) OR dimensional_extractors (continue processing)
orchestration_ref: ORCHESTRATION_ARCHITECTURE.md
evidence_standard: VERIFIED|INFERRED|UNKNOWN
execution_frequency: "Every 10-20 transcripts processed"
---

# Context_Weaver Agent

**Role:** Connection Builder + Validation Enrichment
**Pattern:** Periodic Enrichment (runs every 10-20 transcripts)
**Execution:** After Node_Synthesizer has processed batch of 10-20 transcripts
**Version:** 1.0
**Created:** 2025-10-30

---

## Purpose

Build intelligent connections between foundation layer (company's stated strategy) and customer layer (transcript-validated reality), progressively enriching both layers as evidence accumulates.

**Critical Responsibilities:**
- **Validate foundation nodes** with transcript evidence (baseline → validating → validated)
- **Generate wiki-links** between related nodes (foundation ↔ customer)
- **Flag contradictions** when transcript evidence refutes foundation claims
- **Update confidence scores** based on accumulating sources
- **Progress node status** (emergent → validated → canonical)
- **Enrich foundation nodes** with transcript validation examples
- **Enrich customer nodes** with relevant foundation context

---

## Execution Trigger

**Frequency:** Every 10-20 transcripts processed

**Example:**
```yaml
Transcript count: 0 → Foundation_Seeder runs (one-time)
Transcript count: 1-10 → Dimensional Extractors + Node_Synthesizer only
Transcript count: 10 → Context_Weaver runs (1st enrichment pass)
Transcript count: 11-20 → Dimensional Extractors + Node_Synthesizer only
Transcript count: 20 → Context_Weaver runs (2nd enrichment pass)
Transcript count: 30, 40, 50... → Context_Weaver continues every 10-20 transcripts
```

**Why periodic, not per-transcript:**
- Efficient: Batch processing reduces redundant checks
- Pattern emergence: 10-20 transcripts gives patterns time to stabilize
- Computational cost: Connection-building across entire graph is expensive

---

## Input Requirements

### Foundation Layer
- Location: `knowledge_base/00_foundation/**/*.md`
- Expected: 20-30 baseline nodes
- Status: baseline, validating, validated, canonical
- Confidence: 5.0-7.0 initially, increases with transcript validation

### Customer Layer
- Location: `knowledge_base/01_customer/**/*.md`
- Expected: 30-150 nodes (grows with transcript processing)
- Status: emergent, validated, canonical
- Frequency: Tracked in taxonomy.yaml

### Strategic Lens
- `knowledge_base/strategic_lens.yaml` v1.2+
- Sections: foundation_validation_rules, wiki_link_generation

---

## Connection-Building Process

### Step 1: Foundation Validation Signal Detection (20-30 min)

**[VERIFIED: strategic_lens.yaml v1.2 foundation_validation_rules]**

**Purpose:** Find transcript evidence that validates or refutes foundation claims

---

#### A. ICP Criteria Validation

**Check:** Do customer personas match foundation ICP criteria?

```yaml
For each foundation/icp/*.md node:

  Load ICP criteria:
    - Firmographic requirements (revenue, headcount, vertical)
    - Ivan's constraints (margins <30%, headcount <10, sales-led, AR-focused)
    - Revenue tiers (Shrimp/Fish/Whale/Kraken)

  Search customer/personas/*.md:
    - Count personas matching margin_profile <30%
    - Count personas matching accounting_team <10
    - Count personas matching sales-led transaction_profile
    - Count personas matching AR-focused business_model

  Calculate validation_rate:
    matching_personas / total_personas_processed

  Update foundation/icp/icp-definition.md:
    transcript_validation:
      margin_profile_<30:
        validation_count: [X personas match]
        validation_rate: [X%]
        validation_examples:
          - [[building-materials-whale-owner]] (25% margins)
          - [[wholesale-distributor-owner]] (28% margins)

      accounting_team_<10:
        validation_count: [Y personas match]
        validation_rate: [Y%]
        validation_examples:
          - [[construction-contractor-cfo]] (6 staff)

      sales_led_transactions:
        validation_count: [Z personas match]
        validation_rate: [Z%]

    status: baseline → validating (if ≥1 validation) → validated (if ≥2 validations)
    confidence: recalculate with source boost
    last_enriched: [timestamp]
```

---

#### B. Value Prop Validation

**Check:** Do customer pain points align with foundation value props?

```yaml
For each foundation/value_props/*.md node:

  Load value prop claim:
    Example: "Eliminate payment delays"

  Search customer/pain_points/*.md:
    - Find pain points matching value prop theme
    - Example matches: cash-flow-constraints, payment-processing-delays

  Update foundation/value_props/supplier-finance-platform.md:
    transcript_validation:
      value_prop: "Eliminate payment delays"
      supporting_pains:
        - [[cash-flow-constraints]] (freq: 14, severity: CRITICAL)
        - [[check-payment-hassles]] (freq: 8, severity: HIGH)
      validation_strength: "STRONG" (multiple high-frequency pains align)

    status: baseline → validating → validated
    confidence: recalculate
    validation_count: [number of supporting pain points]
```

---

#### C. Competitive Intel Validation

**Check:** Do transcript mentions match foundation competitive claims?

```yaml
For each foundation/competitive_intel/*.md node:

  Load foundation claim:
    Example: "Melio pricing is $90/mo"

  Search transcript evidence (from customer nodes referencing Melio):
    - Find objections mentioning Melio
    - Find competitive_context in pain points

  Compare claim vs evidence:

    If MATCH:
      transcript_validation:
        claim: "Melio pricing is $90/mo"
        transcript_evidence:
          - [VERIFIED: transcript_42:156] "Paying $90/month for Melio"
          - [VERIFIED: transcript_67:203] "Melio costs $90"
        validation_status: "CONFIRMED"
        validation_count: 2

    If CONFLICT:
      contradiction_flag:
        claim: "Melio pricing is $90/mo"
        transcript_evidence:
          - [VERIFIED: transcript_89:178] "Melio is $49/month now"
        contradiction_type: "PRICING_OUTDATED"
        action_required: "Update foundation claim with current pricing"
        severity: "MEDIUM"

  Update node:
    status: baseline → validating → validated (if confirmed)
    OR add contradiction_flag (if conflict)
    confidence: adjust based on validation or contradiction
```

---

#### D. Positioning Statement Validation

**Check:** Does customer language match foundation positioning?

```yaml
For each foundation/positioning/*.md node:

  Load positioning claim:
    Example: "All-in-one Supplier Finance platform"

  Search transcript evidence:
    - Keywords: "all in one", "comprehensive solution", "single platform"
    - Pain points mentioning fragmentation, point solutions

  Update foundation/positioning/positioning-statement.md:
    transcript_validation:
      positioning: "All-in-one Supplier Finance platform"
      language_validation:
        customer_phrases:
          - [VERIFIED: transcript_23:145] "looking for all in one solution"
          - [VERIFIED: transcript_56:198] "tired of multiple tools"
        pain_point_support:
          - [[point-solution-fragmentation]] (freq: 5)
        validation_strength: "MODERATE"

    status: baseline → validating → validated
    confidence: recalculate
```

---

#### E. Product Capability Validation

**Check:** Do customer requirements match foundation stated capabilities?

```yaml
For each foundation/product/*.md node:

  Load capability claim:
    Example: "QuickBooks Online integration"

  Search customer/use_cases/*.md and product_requirements:
    - Count mentions of QuickBooks requirement
    - Check if blocker or nice-to-have

  Update foundation/product/quickbooks-integration.md:
    transcript_validation:
      capability: "QuickBooks Online integration"
      requirement_frequency: 47 of 50 transcripts (94%)
      blocker_status: "UNIVERSAL BLOCKER"
      validation_strength: "CRITICAL"
      customer_evidence:
        - [[quickbooks-integration]] use case (freq: 47, status: canonical)

    status: baseline → validating → validated → canonical
    confidence: 9.5 (very high with 94% frequency)
    notes: "Universal requirement validated - critical for all personas"
```

---

### Step 2: Generate Wiki-Links (15-20 min)

**[VERIFIED: strategic_lens.yaml v1.2 wiki_link_generation]**

**Purpose:** Create [[wiki-links]] between related nodes for graph navigation

---

#### A. Foundation → Customer Links

```yaml
For each foundation node:

  ICP nodes → Persona nodes:
    If persona matches ICP criteria:
      Add to foundation/icp/icp-definition.md:
        validation_examples:
          - [[building-materials-whale-owner]]
          - [[wholesale-distributor-owner]]

  Value prop nodes → Pain point nodes:
    If pain point aligns with value prop:
      Add to foundation/value_props/supplier-finance-platform.md:
        supporting_evidence:
          - [[cash-flow-constraints]]
          - [[payment-processing-costs]]

  Competitive intel nodes → Objection nodes:
    If objection mentions competitor:
      Add to foundation/competitive_intel/melio.md:
        customer_objections:
          - [[existing-solution-satisfaction]]
        win_loss_context:
          - [[competitive-displacement-challenge]]

  Product capability nodes → Use case nodes:
    If use case requires capability:
      Add to foundation/product/quickbooks-integration.md:
        use_cases:
          - [[ar-automation]]
          - [[invoice-reconciliation]]
```

---

#### B. Customer → Customer Links

```yaml
Persona → Pain/Objection/Use Case:
  For each persona node:
    - Add [[pain-point-slug]] to persona.pain_points[]
    - Add [[objection-slug]] to persona.objections[]
    - Add [[use-case-slug]] to persona.use_cases[]

  Reverse links:
    - Add [[persona-slug]] to pain_point.affected_personas[]
    - Add [[persona-slug]] to objection.affected_personas[]
    - Add [[persona-slug]] to use_case.applicable_personas[]

Pain → Objection:
  If causal relationship:
    - [[cash-flow-constraints]] pain → relates to → [[volume-threshold-barriers]] objection
    - Add [[objection-slug]] to pain.related_objections[]

Objection → Competitive Intel:
  If objection involves competitor:
    - [[existing-solution-satisfaction]] → links to → [[melio]] competitive intel
    - Add [[competitor-slug]] to objection.competitive_context[]

Use Case → Product Requirement:
  If use case has product dependency:
    - [[ar-automation]] → requires → [[quickbooks-integration]]
    - Add [[requirement-slug]] to use_case.requirements[]
```

---

### Step 3: Update Node Status Progression (10-15 min)

**Purpose:** Progress nodes through lifecycle as evidence accumulates

**[VERIFIED: strategic_lens.yaml v1.2 node_lifecycle]**

```yaml
Foundation nodes:
  baseline → validating:
    Trigger: ≥1 transcript validation signal
    Action: Update status, add validation_count: 1

  validating → validated:
    Trigger: ≥2 transcript validation signals
    Action: Update status, validation_count: 2+

  validated → canonical:
    Trigger: ≥5 transcript validation signals
    Action: Update status, validation_count: 5+, confidence: 9.0+

Customer nodes:
  emergent → validated:
    Trigger: frequency ≥2 (appeared in 2+ transcripts)
    Action: Update status in frontmatter

  validated → canonical:
    Trigger: frequency ≥5 (appeared in 5+ transcripts)
    Action: Update status, note as high-confidence pattern

For each node:
  Check current frequency or validation_count
  If threshold crossed:
    Update status field in frontmatter
    Update confidence score
    Update last_updated timestamp
    Add status_history entry
```

---

### Step 4: Calculate Confidence Scores (10-15 min)

**Purpose:** Recalculate confidence based on source accumulation

**[VERIFIED: strategic_lens.yaml v1.2 confidence_scoring]**

```yaml
Formula:
  base_confidence (by status):
    baseline: 5.0
    emergent: 3.0
    validating: 6.0
    validated: 7.5
    canonical: 9.0

  source_boost:
    base_confidence + (log10(source_count + 1) × 1.5)

  evidence_quality_multiplier:
    high_quality: 1.2 (direct quotes, quantified, multi-persona)
    medium_quality: 1.0 (indirect, qualitative)
    low_quality: 0.8 (vague, contradictory)

  cap: 10.0

For each node:
  Count sources (transcripts, raw_context docs)
  Assess evidence quality
  Calculate: (base + log_boost) × quality_multiplier
  Update confidence field in frontmatter
```

---

### Step 5: Flag Contradictions (10-15 min)

**Purpose:** Identify where transcript evidence conflicts with foundation claims

**[VERIFIED: strategic_lens.yaml v1.2 foundation_validation_rules.contradiction_flagging]**

```yaml
Contradiction types:

  ICP_MISMATCH:
    Foundation: "ICP sweet spot is $5-25M (Whale)"
    Transcripts: "80% high-fit customers are <$5M (Fish)"
    Flag: "ICP_REVENUE_MISMATCH"
    Severity: HIGH
    Action: "Validate in Checkpoint 1, consider ICP refinement"

  COMPETITIVE_PRICING_OUTDATED:
    Foundation: "Melio pricing is $90/mo"
    Transcripts: "Customer says Melio is $49/mo now"
    Flag: "PRICING_OUTDATED"
    Severity: MEDIUM
    Action: "Update foundation competitive intel"

  DIFFERENTIATION_WEAK:
    Foundation: "QuickBooks integration is advantage"
    Transcripts: "Competitors also have QB integration"
    Flag: "DIFFERENTIATION_NOT_UNIQUE"
    Severity: HIGH
    Action: "Positioning needs update, find different differentiator"

  VALUE_PROP_UNVALIDATED:
    Foundation: "Lien management automation"
    Transcripts: "0 mentions of lien management in 50 transcripts"
    Flag: "VALUE_PROP_NO_EVIDENCE"
    Severity: LOW
    Action: "Watch for mentions, may not be core value prop"

For each contradiction:
  Add contradiction_flag to foundation node:
    contradiction:
      type: [type]
      foundation_claim: [quote from foundation]
      transcript_evidence: [conflicting evidence with sources]
      severity: [CRITICAL/HIGH/MEDIUM/LOW]
      action_required: [what needs to happen]
      flagged_date: [timestamp]
      resolution_status: "OPEN"
```

---

### Step 6: Generate Enrichment Report (5-10 min)

**Output:** `_AGENT_WORKSPACE/context_weaver_reports/enrichment_[transcript_count].md`

```markdown
# Context Weaver Enrichment Report

**Transcript Count:** 1-20 (first batch)
**Enrichment Date:** YYYY-MM-DD
**Agent:** Context_Weaver v1.0

---

## Foundation Validation Summary

**Nodes Updated:** 15 of 20 foundation nodes

**Status Progression:**
- baseline → validating: 8 nodes
- validating → validated: 3 nodes
- No progression: 9 nodes (awaiting more evidence)

**Validation Highlights:**
1. **ICP margin_profile <30%:** 7 of 15 personas match (47%) ✅ VALIDATING
2. **QuickBooks integration:** 14 of 15 transcripts mention (93%) ✅ VALIDATED → CANONICAL
3. **Melio pricing ($90/mo):** 3 confirmations ✅ VALIDATED
4. **Lien management value prop:** 0 mentions ⚠️ NO EVIDENCE

---

## Wiki-Links Generated

**Total Links Added:** 47

**Foundation → Customer:**
- ICP nodes → Persona nodes: 12 links
- Value prop nodes → Pain point nodes: 8 links
- Competitive intel nodes → Objection nodes: 6 links
- Product capability nodes → Use case nodes: 9 links

**Customer → Customer:**
- Persona ↔ Pain/Objection/Use Case: 12 links

---

## Contradictions Flagged

**Total:** 2

1. **ICP_REVENUE_MISMATCH** (HIGH)
   - Foundation: ICP sweet spot is $5-25M (Whale)
   - Evidence: 60% of high-fit personas are $1-5M (Fish)
   - Action: Validate in Checkpoint 1, consider ICP broadening

2. **DIFFERENTIATION_WEAK** (MEDIUM)
   - Foundation: Free ACH is differentiator
   - Evidence: 3 transcripts mention competitors also have free ACH
   - Action: Position needs refinement, find unique angle

---

## Confidence Updates

**Average Confidence Increase:** +0.8 points

**Top Confidence Nodes:**
- quickbooks-integration: 9.5 (canonical, 93% frequency)
- icp-definition: 7.8 (validated, strong signals)
- cash-flow-constraints: 8.2 (validated, freq 14)

**Low Confidence Nodes:**
- lien-management value prop: 5.0 (baseline, no validation)
- kraken-tier ICP: 5.2 (baseline, 1 example only)

---

## Next Steps

**For Checkpoint 1 (after 50 transcripts):**
- Resolve ICP_REVENUE_MISMATCH contradiction
- Validate low-confidence foundation nodes
- Expect 5-10 more foundation nodes → validated status

**Pattern Watch:**
- Accounting firm buyer persona (freq 1 → watch for revalidation)
- Multi-entity dashboard requirement (freq 2 → emerging)
- Vendor portal fatigue pain (freq 1 → watch)

---

**Next Context Weaver Run:** After transcript 30-40
