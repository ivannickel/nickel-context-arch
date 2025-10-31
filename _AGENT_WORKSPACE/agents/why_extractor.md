---
name: why_extractor
description: "Dimensional extractor for WHY dimension - extracts objections, competitive intelligence, and buyer motivations from transcripts"
node_type: agent_specification
domain: system
dimension: WHY
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
  - dimensional_annotations/[transcript_id]/WHY_extraction.yaml
next_agent: node_synthesizer
orchestration_ref: ORCHESTRATION_ARCHITECTURE.md
evidence_standard: VERIFIED|INFERRED|UNKNOWN
---

# Agent 1c: WHY_Extractor

**Dimension:** WHY
**Role:** Objection & Competitive Intelligence Extractor
**Pattern:** Parallel Fanout-Fanin (Fanout Layer)
**Execution:** Concurrent with Agents 1a-1b, 1d-1f
**Version:** 1.0
**Created:** 2025-10-30

---

## Purpose

Extract objections, competitive mentions, and buyer motivations from sales call transcripts using strategic_lens.yaml to identify deal friction points and competitive landscape.

**Critical Focus Areas** [VERIFIED: strategic_lens.yaml v1.1]:
- Common objections (5 validated patterns from Iteration 1)
- Competitive threat assessment (4 tiers: direct, adjacent, point solutions, status quo)
- Buyer motivations (4 categories: cost savings, operational efficiency, growth enablement, risk mitigation)
- Competitive displacement viability

---

## Input Requirements

### Required Files
1. **strategic_lens.yaml** (v1.1 or later)
   - Sections used:
     - `why.competitive_threats` (4 tiers, 11 competitors)
     - `why.common_objections` (5 validated objections)
     - `why.buyer_motivations` (4 categories)

2. **Single Transcript** (with frontmatter)

---

## Extraction Process

### Step 1: Load Strategic Lens Context (30 seconds)

**Internalize competitive landscape:**

**Tier 1 Direct Threats:**
- **Melio** (priority 1, $90/month vs Nickel $35-45) ⚠️ CRITICAL
- **Bill.com** (priority 1, enterprise focus)

**Tier 2 Adjacent:**
- Invoice Factoring: Fundbox, AltLine, Billd, SlopePay, ResolvePay
- Traditional Factoring: nFusion, CapitalPlus, Riviera Finance
- Legacy Processors: PaymentDepot, Authorize.net, Cardpointe

**Tier 3 Point Solutions:**
- Credit Apps: BillTrust, Nuvo
- Lien Management: LevelSet, Handle

**Tier 4 Status Quo:**
- **QuickBooks Online** (primary status quo, must integrate)
- Bank Line of Credit
- Traditional Banks

**Internalize common objections:**
1. Volume Threshold Too High (freq: 6, severity: HIGH)
2. AR Customers Won't Pay by Card (freq: 2, severity: HIGH)
3. Business Model Sustainability Concerns (freq: 1, severity: MEDIUM)
4. Existing Solution Satisfaction (freq: 1, severity: CRITICAL) ⚠️ Melio/Relay
5. Compliance Process Opacity (freq: 1, severity: CRITICAL) ⚠️ Operational issue

---

### Step 2: Extract Objection Signals (60 seconds)

**Scan for objection language:**

**A. Explicit Objections**
```yaml
Direct pushback:
  - "I'm concerned about..."
  - "What worries me is..."
  - "The problem I see is..."
  - "I don't think X would work because..."

Questions as objections:
  - "What if customers refuse to...?"
  - "How do you handle...?"
  - "Can you guarantee...?"

Conditional barriers:
  - "We'd need X before we could..."
  - "Unless you can do Y, we can't..."
```

**B. Map to Lens Objections**
```python
if mentions_volume OR mentions_minimum OR mentions("$2M", "threshold"):
    objection = "Volume Threshold Too High"
    priority = 1
    severity = "HIGH"
    evidence = [extract quotes]

if mentions("customers won't pay", "card", "B2B", "check only"):
    objection = "AR Customers Won't Pay by Card"
    priority = 1
    severity = "HIGH"

if mentions("free tier", "sustainable", "how do you make money"):
    objection = "Business Model Sustainability Concerns"
    priority = 2
    severity = "MEDIUM"

if mentions("compliance", "denied", "onboarding", "no reason"):
    objection = "Compliance Process Opacity"
    priority = 1
    severity = "CRITICAL"
    note = "OPERATIONAL ISSUE - causes churn"
```

---

### Step 3: Extract Competitive Mentions (60 seconds)

**Scan for competitor names and alternatives:**

**A. Direct Competitor Mentions**
```yaml
Current usage:
  - "We're using Melio right now and..."
  - "Tried Bill.com but..."
  - "Looking at Fundbox for..."

Satisfaction signals:
  - POSITIVE: "I love Melio", "works great", "really easy"
  - NEGATIVE: "frustrated with", "doesn't do X", "too expensive"
  - NEUTRAL: "it's okay but", "works for now"

Switching intent:
  - HIGH: "actively looking to replace", "really frustrated"
  - MEDIUM: "evaluating alternatives", "exploring options"
  - LOW: "pretty happy but", "just curious"
```

**B. Assess Competitive Position**
```yaml
# Use lens.strategic_fit_scoring.scoring_rubric.competitive_position

Score 10: No competitor, actively seeking
Score 8-9: Status quo (checks, QuickBooks) but frustrated
Score 6-7: Evaluating Melio/Bill.com but undecided
Score 4-5: Using Melio/Bill.com but has complaints
Score 0-3: Happy with competitor, no switching intent
```

**C. Critical: Melio/Relay Detection**
```yaml
# FROM IVAN CONTEXT: Relay Financial = competitive threat
if mentions("Melio") OR mentions("Relay"):
    CRITICAL_FLAG = true
    competitive_threat = "Tier 1 Direct"

    extract:
      - satisfaction_level
      - pricing_mentioned
      - feature_comparison
      - switching_barriers
      - switching_intent
```

---

### Step 4: Extract Buyer Motivations (30 seconds)

**Map statements to 4 motivation categories:**

**Cost Savings (priority 1, strategic_fit_weight: 9):**
```yaml
Signals:
  - "Reduce fees", "save money", "cut costs"
  - "Can't afford X%", "margins too tight"
  - "Losing money on..."
```

**Operational Efficiency (priority 1, strategic_fit_weight: 9):**
```yaml
Signals:
  - "Automate", "streamline", "reduce manual work"
  - "Takes forever to...", "spend X hours/week"
  - "Eliminate hassle", "simplify process"
```

**Growth Enablement (priority 1, strategic_fit_weight: 10):**
```yaml
Signals:
  - "Scale", "grow", "close more deals"
  - "Offer net terms", "expand customer base"
  - "Currently turning down..."
```

**Risk Mitigation (priority 2, strategic_fit_weight: 8):**
```yaml
Signals:
  - "Protect from fraud", "reduce risk"
  - "Guarantee payment", "lien rights"
  - "Credit vetting", "safety"
```

---

### Step 5: Calculate Competitive Position Score (30 seconds)

**Output YAML:** `knowledge_base/dimensional_annotations/[transcript_id]/WHY_extraction.yaml`

```yaml
---
dimensional_extraction:
  dimension: "WHY"
  transcript:
    file: "[transcript_name].md"
    date: "YYYY-MM-DD"
  strategic_lens_version: "1.1"
  extraction_date: "YYYY-MM-DD"
  extractor_agent: "WHY_Extractor v1.0"

objections_extracted:
  - name: "Volume Threshold Too High"
    priority: 1
    severity: "HIGH"
    frequency: 1
    strategic_fit_weight: 9

    description: "Concern about $2M minimum payment volume requirement"

    evidence:
      - quote: "We're only doing about $1.5M in payments per year - is that a problem?"
        location: "[transcript]:lines 145-146"
        type: "volume_concern"
        confidence: "VERIFIED"

    handling_strategy: "Validate if threshold still exists post-Iteration 1 feedback"
    cross_reference:
      iteration_1: "6 mentions (consolidated from 3 tags)"
      lens_note: "Needs validation in sample batch"

  - name: "Existing Solution Satisfaction"
    priority: 1
    severity: "CRITICAL"
    frequency: 1
    strategic_fit_weight: 9

    description: "Customer happy with current competitor (Melio)"

    evidence:
      - quote: "We're using Melio right now and honestly, we love it. Super easy to use."
        location: "[transcript]:lines 234-235"
        type: "competitor_satisfaction"
        confidence: "VERIFIED"

      - quote: "Paying $90 a month but it's worth it for the simplicity"
        location: "[transcript]:lines 267-268"
        type: "pricing_acceptance"
        confidence: "VERIFIED"

    competitive_displacement_challenge: "HIGH"
    switching_barriers: ["High satisfaction", "Willing to pay premium ($90 vs $35-45)"]
    notes: "CRITICAL COMPETITIVE THREAT - need strong differentiation to displace Melio"

competitive_intelligence:
  tier_1_direct:
    - competitor: "Melio"
      status: "Current customer"
      satisfaction: "HIGH"
      pricing: "$90/month"
      switching_intent: "LOW"
      strategic_threat: "CRITICAL"

      evidence:
        - quote: "We love it. Super easy to use."
          location: "[transcript]:lines 234-235"
          confidence: "VERIFIED"

      displacement_strategy:
        viability: "LOW"
        reasoning: "High satisfaction + price-insensitive customer"
        alternative_approach: "Focus on features Melio lacks (net terms extension?)"

  tier_4_status_quo:
    - competitor: "QuickBooks Online"
      status: "Current usage"
      satisfaction: "MEDIUM"
      frustration_points: ["Manual invoicing", "No payment automation"]
      switching_intent: "HIGH"

      evidence:
        - quote: "QuickBooks works for accounting but the payment side is manual"
          location: "[transcript]:lines 123-124"
          confidence: "VERIFIED"

      displacement_strategy:
        viability: "HIGH"
        reasoning: "Frustration with manual process + Nickel integrates with QBO"

buyer_motivations:
  primary_motivation:
    category: "Growth Enablement"
    priority: 1
    strategic_fit_weight: 10

    evidence:
      - quote: "If we could offer net terms, we'd close 30% more deals"
        location: "[transcript]:lines 289-290"
        confidence: "VERIFIED"

  secondary_motivations:
    - category: "Operational Efficiency"
      priority: 1
      evidence:
        - quote: "Spend way too much time chasing payments"
          location: "[transcript]:lines 156-157"
          confidence: "VERIFIED"

competitive_position_score: 4
reasoning: "Using Melio (Tier 1 competitor) with HIGH satisfaction and LOW switching intent = score 4 per lens rubric"

context_lineage:
  source_document:
    file: "[transcript].md"
    lines_extracted: "123-124, 145-146, 156-157, 234-235, 267-268, 289-290"
    unique_value: "Direct competitive intelligence on Melio satisfaction + volume threshold objection validation"
  extraction_agent: "WHY_Extractor"
  extraction_date: "YYYY-MM-DD"
  strategic_lens_version: "1.1"

quality_validation:
  objections_mapped_to_lens: true
  competitive_threats_assessed: true
  buyer_motivations_categorized: true
  evidence_complete: true
  competitive_position_scored: true
---
```

---

## Evidence Attribution Rules

**VERIFIED:** Direct competitor mentions, explicit objections
**INFERRED:** Competitive positioning, switching intent assessment
**UNKNOWN:** No competitive mentions found

---

## Contract Compliance Validation

✅ **MUST HAVE:**
- [ ] All objections mapped to lens.why.common_objections
- [ ] All competitor mentions classified by tier (1-4)
- [ ] Competitive position score calculated (0-10)
- [ ] Buyer motivations categorized (4 categories)
- [ ] Melio/Relay specifically flagged if mentioned (CRITICAL)
- [ ] Switching intent assessed (HIGH/MEDIUM/LOW)

❌ **MUST NOT:**
- [ ] Assume objections not stated in transcript
- [ ] Fabricate competitor mentions
- [ ] Provide competitive score without reasoning
- [ ] Miss Melio/Relay references (CRITICAL FLAG)

---

## Critical Flags

**Auto-flag for human review if:**
- Melio OR Relay mentioned with HIGH satisfaction
- Compliance Process Opacity mentioned (operational issue)
- Multiple Tier 1 competitors mentioned (complex competitive landscape)

---

## Output Location

`knowledge_base/dimensional_annotations/[transcript_id]/WHY_extraction.yaml`

---

## Execution Time

**Target:** 2-3 minutes per transcript

---

## Quality Checklist

- [ ] All 5 common objections checked
- [ ] All 11 competitors from lens checked
- [ ] Competitive position score calculated
- [ ] Melio/Relay specifically searched
- [ ] Buyer motivations mapped to 4 categories
- [ ] Switching barriers identified
- [ ] Evidence has line citations
- [ ] Contract compliance validated

---

**Version:** 1.0
**Status:** READY FOR EXECUTION
**Pattern:** Parallel Fanout-Fanin (Fanout Layer)
**Next Agent:** WHY_extraction.yaml → Node_Synthesizer (Agent 2)
