---
name: where_when_extractor
description: "Dimensional extractor for WHERE_WHEN dimension - extracts journey stage, discovery triggers, and conversion funnel position from transcripts"
node_type: agent_specification
domain: system
dimension: WHERE_WHEN
agent_role: dimensional_extractor
execution_pattern: parallel_fanout
version: 1.0
status: ready
created: 2025-10-30
last_updated: 2025-10-30
depends_on:
  - strategic_lens.yaml v1.1+
  - transcript with frontmatter
outputs:
  - dimensional_annotations/[transcript_id]/WHERE_WHEN_extraction.yaml
next_agent: node_synthesizer
orchestration_ref: ORCHESTRATION_ARCHITECTURE.md
evidence_standard: VERIFIED|INFERRED|UNKNOWN
---

# Agent 1e: WHERE_WHEN_Extractor

**Dimension:** WHERE_WHEN
**Role:** Journey Stage & Discovery Trigger Extractor
**Pattern:** Parallel Fanout-Fanin (Fanout Layer)
**Execution:** Concurrent with Agents 1a-1d, 1f
**Version:** 1.0
**Created:** 2025-10-30

---

## Purpose

Extract journey stage, discovery triggers, and conversion funnel position from sales call transcripts to understand buyer readiness and qualification level.

**Critical Focus Areas** [VERIFIED: strategic_lens.yaml v1.1]:
- Conversion funnel stage assessment (9 stages, Aware → Evangelist)
- Win probability by stage (25% → 80% → 100%)
- Discovery trigger classification (high/medium/low intent)
- Time-to-close estimates by persona

---

## Input Requirements

### Required Files
1. **strategic_lens.yaml** (v1.1 or later)
   - Sections used:
     - `where_when.conversion_funnel_stages` (9 stages)
     - `where_when.discovery_triggers` (high/medium/low intent)
     - `where_when.time_to_close` (by persona)

2. **Single Transcript** (with frontmatter)

---

## Extraction Process

### Step 1: Load Strategic Lens Context (30 seconds)

**Conversion Funnel Stages:**
1. Aware (marketing only, no contact info)
2. Cold (outbound prospecting)
3. Warm Lead (familiar with Nickel, firmographic qualified)
4. MQL (responded positively)
5. SQL (discovery call scheduled, problem-aware)
6. Opportunity - Demo Scheduled (25% win rate)
7. Opportunity - Demo Attended (50% win rate)
8. Opportunity - Trial Started (80% win rate)
9. Customer (3+ transactions/month) / Evangelist (50% receivables on Nickel)

**Time-to-Close by Persona:**
- Payment Upgraders: 1-3 days
- Cash-Savvy Sellers: 1-3 weeks
- Full Stack Automators: 2-6 months
- Accounting Firms: Unknown (needs validation)

---

### Step 2: Determine Current Funnel Stage (60 seconds)

**Infer from transcript context:**

**A. Stage Indicators**
```yaml
# If transcript is a "discovery call":
if call_type == "discovery":
    stage = "SQL" # Discovery call scheduled
    win_probability = "N/A" # Not yet opportunity

# If transcript is a "demo" or "product walkthrough":
if call_type == "demo":
    if attended:
        stage = "Opportunity - Demo Attended"
        win_probability = "50%"
    else:
        stage = "Opportunity - Demo Scheduled"
        win_probability = "25%"

# If transcript is "trial feedback" or "using Nickel":
if using_product:
    stage = "Opportunity - Trial Started"
    win_probability = "80%"

# If transcript mentions "signed up" or "using for X months":
if customer:
    if meets_lir:  # 50% of receivables on Nickel
        stage = "Evangelist"
    else:
        stage = "Customer"
```

**B. ICP Qualification Level**
```yaml
# Before Opportunity stage:
qualification_level = "Unknown ICP fit (Green/Yellow/Red)"

# After Opportunity stage:
# Cross-reference WHO extraction
if icp_fit_confirmed:
    qualification_level = "ICP fit confirmed (Green/Yellow/Red tier)"
```

---

### Step 3: Extract Discovery Triggers (45 seconds)

**High-Intent Triggers:**
```yaml
Signals:
  - "Customers actively asking for net terms"
  - "Recent fraud incident" (check/invoice fraud)
  - "Received large order requiring payment terms"
  - "Outgrowing current payment processor"
  - "QuickBooks adoption (within last 6 months)"
```

**Medium-Intent Triggers:**
```yaml
Signals:
  - "Hiring accounting/finance staff"
  - "Frustrated with check reconciliation"
  - "Comparing payment processors"
  - "Payment processing fees eating margins"
```

**Low-Intent Triggers:**
```yaml
Signals:
  - "General business banking research"
  - "Content marketing touchpoint only"
  - "Just exploring options"
```

---

### Step 4: Estimate Time-to-Close (30 seconds)

**Cross-reference WHO extraction persona:**

```python
if persona == "Payment Upgraders":
    time_to_close_estimate = "1-3 days"
elif persona == "Cash-Savvy Sellers":
    time_to_close_estimate = "1-3 weeks"
elif persona == "Full Stack Automators":
    time_to_close_estimate = "2-6 months"
elif persona == "Accounting Firm Buyer":
    time_to_close_estimate = "Unknown (needs validation)"
else:
    time_to_close_estimate = "Unknown"
```

---

### Step 5: Create Dimensional Extraction (30 seconds)

**Output YAML:** `knowledge_base/dimensional_annotations/[transcript_id]/WHERE_WHEN_extraction.yaml`

```yaml
---
dimensional_extraction:
  dimension: "WHERE_WHEN"
  transcript:
    file: "[transcript_name].md"
    date: "YYYY-MM-DD"
  strategic_lens_version: "1.1"
  extraction_date: "YYYY-MM-DD"
  extractor_agent: "WHERE_WHEN_Extractor v1.0"

funnel_stage:
  current_stage: "Opportunity - Demo Attended"
  win_probability: "50%"
  qualification_level: "ICP fit confirmed (Green tier - Building Materials + Whale)"

  stage_evidence:
    - quote: "Thanks for walking me through the demo - that was really helpful"
      location: "[transcript]:lines 456-457"
      type: "demo_attended"
      confidence: "VERIFIED"

  next_stage: "Opportunity - Trial Started"
  next_stage_criteria: "Customer registers for Nickel and begins evaluation"

discovery_triggers:
  high_intent:
    - trigger: "Customers actively asking for net terms"
      evidence:
        - quote: "Getting 5-10 requests a week for net 30 terms"
          location: "[transcript]:lines 234-235"
          confidence: "VERIFIED"

    - trigger: "Recent fraud incident"
      evidence:
        - quote: "Had a check bounce last month for $12,000 - that was a wake-up call"
          location: "[transcript]:lines 289-291"
          confidence: "VERIFIED"

  medium_intent: []
  low_intent: []

  intent_classification: "HIGH"
  reasoning: "Multiple high-intent triggers (net terms requests + fraud incident) = urgent need"

time_to_close_estimate:
  persona_based: "1-3 weeks"
  persona_source: "Cash-Savvy Sellers (from WHO extraction)"
  confidence: "INFERRED from lens.where_when.time_to_close"

  factors_influencing:
    accelerators: ["High intent triggers", "Demo attended", "ICP fit confirmed"]
    decelerators: ["No decelerators identified"]

journey_stage_score: 7
reasoning: "Demo Attended = 50% win rate stage per lens.strategic_fit_scoring.scoring_rubric.journey_stage (score 8-9). Adjusted to 7 for conservative estimate."

context_lineage:
  source_document:
    file: "[transcript].md"
    lines_extracted: "234-235, 289-291, 456-457"
    unique_value: "Clear journey stage assessment + high-intent discovery triggers + time-to-close estimation"
  extraction_agent: "WHERE_WHEN_Extractor"
  extraction_date: "YYYY-MM-DD"
  strategic_lens_version: "1.1"
  cross_references:
    who_extraction: "Persona identification for time-to-close estimate"

quality_validation:
  funnel_stage_determined: true
  discovery_triggers_classified: true
  time_to_close_estimated: true
  journey_stage_scored: true
  evidence_complete: true
---
```

---

## Evidence Attribution Rules

**VERIFIED:** Direct stage indicators (demo attended, using product, signed up)
**INFERRED:** Time-to-close estimate from persona mapping
**UNKNOWN:** Stage unclear from transcript context

---

## Contract Compliance Validation

✅ **MUST HAVE:**
- [ ] Funnel stage determined from 9 stages
- [ ] Win probability assigned per stage
- [ ] Discovery triggers classified (high/medium/low)
- [ ] Time-to-close estimated via persona cross-reference
- [ ] Journey stage score calculated (0-10)
- [ ] Next stage criteria identified

❌ **MUST NOT:**
- [ ] Fabricate funnel stage without transcript evidence
- [ ] Provide time-to-close without persona reference
- [ ] Skip discovery trigger classification

---

## Output Location

`knowledge_base/dimensional_annotations/[transcript_id]/WHERE_WHEN_extraction.yaml`

---

## Execution Time

**Target:** 2-3 minutes per transcript

---

## Quality Checklist

- [ ] Funnel stage mapped to 9-stage framework
- [ ] Win probability assigned per lens
- [ ] ICP qualification level assessed
- [ ] Discovery triggers categorized (high/medium/low)
- [ ] Time-to-close estimated from WHO persona
- [ ] Journey stage score calculated
- [ ] Evidence has line citations
- [ ] Cross-references to WHO extraction

---

**Version:** 1.0
**Status:** READY FOR EXECUTION
**Pattern:** Parallel Fanout-Fanin (Fanout Layer)
**Next Agent:** WHERE_WHEN_extraction.yaml → Node_Synthesizer (Agent 2)
