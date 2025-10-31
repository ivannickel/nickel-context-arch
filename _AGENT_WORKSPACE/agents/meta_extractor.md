---
name: meta_extractor
description: "Dimensional extractor for META dimension - extracts market context, segment insights, and trends from transcripts"
node_type: agent_specification
domain: system
dimension: META
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
  - dimensional_annotations/[transcript_id]/META_extraction.yaml
next_agent: node_synthesizer
orchestration_ref: ORCHESTRATION_ARCHITECTURE.md
evidence_standard: VERIFIED|INFERRED|UNKNOWN
---

# Agent 1f: META_Extractor

**Dimension:** META
**Role:** Market Context & Segment Insights Extractor
**Pattern:** Parallel Fanout-Fanin (Fanout Layer)
**Execution:** Concurrent with Agents 1a-1e
**Version:** 1.0
**Created:** 2025-10-30

---

## Purpose

Extract market context, segment insights, and industry trends from sales call transcripts to identify broader patterns beyond individual deals.

**Critical Focus Areas** [VERIFIED: strategic_lens.yaml v1.1]:
- Market segment identification (primary: Building Materials, secondary: 4 verticals)
- Market trend signals (ACH adoption, LLM citations, CC usage in B2B, AR growth)
- Leading indicator of retention validation (50% receivables on Nickel)
- Segment-specific insights (construction, wholesale, logistics patterns)

---

## Input Requirements

### Required Files
1. **strategic_lens.yaml** (v1.1 or later)
   - Sections used:
     - `meta.market_segments` (primary + 4 secondary)
     - `meta.market_trends` (4 validated trends)
     - `meta.key_metrics` (LIR + August 2025 benchmarks)

2. **Single Transcript** (with frontmatter)

---

## Extraction Process

### Step 1: Load Strategic Lens Context (30 seconds)

**Market Segments:**
- Primary: Building Materials & Construction
- Secondary: Wholesale & Distribution, Transportation & Logistics, Large-Ticket B2B Services

**Market Trends:**
1. ACH adoption increasing (positive impact)
2. LLM citation increasing (Nickel in ChatGPT/Perplexity answers)
3. Credit card usage in B2B (18.2% core customers, growing)
4. AR product growth (49.3% of TPV for core customers)

**Leading Indicator of Retention:**
- Customer receives 50% of monthly receivables on Nickel

---

### Step 2: Extract Market Context Signals (60 seconds)

**A. Industry-Level Insights**
```yaml
Industry commentary:
  - "Everyone in our industry is..."
  - "Most contractors I talk to..."
  - "Industry standard is..."
  - "All my suppliers..."

Trend observations:
  - "We're seeing more customers want..."
  - "Used to be checks, now it's..."
  - "Industry is moving toward..."
```

**B. Segment-Specific Patterns**
```yaml
Building Materials segment:
  - Net terms expectations
  - Lien rights management
  - Project-based payment cycles

Construction segment:
  - Cash flow challenges
  - Sub-contractor payment pressures
  - Seasonal volume fluctuations

Wholesale/Distribution:
  - Multiple invoice per customer
  - High transaction volumes
  - Thin margins on bulk sales
```

---

### Step 3: Validate Trend Signals (45 seconds)

**Cross-reference to lens.meta.market_trends:**

```python
if mentions_ach AND mentions("free", "no fee", "bank transfer"):
    trend = "ACH adoption increasing"
    impact = "Positive - aligns with Nickel's free ACH"
    evidence = [extract quotes]

if mentions_credit_card AND mentions("B2B", "commercial customers"):
    trend = "Credit card usage in B2B"
    impact = "Positive - B2B customers increasingly accepting CC"
    evidence = [extract quotes]

if mentions_accounts_receivable AND mentions("growing", "more volume"):
    trend = "AR product growth"
    impact = "Positive - AR is 49.3% of Nickel core TPV"
    evidence = [extract quotes]
```

---

### Step 4: Calculate Market Fit Score (30 seconds)

**Use lens.strategic_fit_scoring.scoring_rubric.market_fit:**

```yaml
Score 10: Building Materials + Construction, growing segment
Score 8-9: Wholesale/Distribution or Manufacturing, stable segment
Score 6-7: Transportation/Logistics or Large-Ticket Services
Score 4-5: Adjacent vertical with transferable pain points
Score 0-3: Non-target market (retail, SaaS, consumer)
```

---

### Step 5: Create Dimensional Extraction (30 seconds)

**Output YAML:** `knowledge_base/dimensional_annotations/[transcript_id]/META_extraction.yaml`

```yaml
---
dimensional_extraction:
  dimension: "META"
  transcript:
    file: "[transcript_name].md"
    date: "YYYY-MM-DD"
  strategic_lens_version: "1.1"
  extraction_date: "YYYY-MM-DD"
  extractor_agent: "META_Extractor v1.0"

market_segment:
  primary_vertical: "Building Materials & Construction"
  priority: 1
  strategic_fit_weight: 10

  evidence:
    - quote: "We're a building materials distributor serving contractors"
      location: "[transcript]:lines 45-46"
      confidence: "VERIFIED"

  segment_characteristics:
    - "Net terms common (net 30, net 60)"
    - "Project-based payment cycles"
    - "Tight margins (20-30%)"
    - "Multiple invoices per customer per project"

market_trends_observed:
  - trend: "ACH adoption increasing"
    impact: "Positive"
    evidence:
      - quote: "Most of our customers are moving away from checks to ACH"
        location: "[transcript]:lines 178-179"
        confidence: "VERIFIED"
    alignment_with_nickel: "Strong - Nickel's free ACH is competitive advantage"

  - trend: "Credit card usage in B2B"
    impact: "Positive"
    evidence:
      - quote: "More contractors are asking if they can pay with card"
        location: "[transcript]:lines 234-236"
        confidence: "VERIFIED"
    alignment_with_nickel: "Strong - Nickel processes CC at competitive rates"

segment_insights:
  industry_pain_points:
    - "Seasonal cash flow fluctuations (construction projects)"
    - "Sub-contractor payment pressures (pay subs before getting paid)"
    - "Lien rights management complexity"

  industry_opportunities:
    - "Net terms becoming standard expectation"
    - "Digital payment adoption accelerating"
    - "Automation appetite growing (labor shortage)"

  competitive_landscape_insights:
    - "Traditional banks not serving this segment well"
    - "Melio/Bill.com seen as 'too generic' for construction needs"

lir_validation:
  leading_indicator_mentioned: false
  customer_volume_signals: "200 invoices/month (from WHAT extraction)"
  receivables_concentration: "UNKNOWN - no mention of % on platform"
  notes: "Cannot validate LIR (50% receivables on Nickel) from this transcript"

market_fit_score: 10
reasoning: "Building Materials & Construction (primary vertical) + growing segment (ACH/CC adoption trends) = score 10 per lens rubric"

context_lineage:
  source_document:
    file: "[transcript].md"
    lines_extracted: "45-46, 178-179, 234-236"
    unique_value: "Market trend validation (ACH + CC adoption in construction) + segment-specific insights"
  extraction_agent: "META_Extractor"
  extraction_date: "YYYY-MM-DD"
  strategic_lens_version: "1.1"

quality_validation:
  market_segment_identified: true
  trends_cross_referenced_to_lens: true
  market_fit_scored: true
  segment_insights_captured: true
  evidence_complete: true
---
```

---

## Evidence Attribution Rules

**VERIFIED:** Direct industry observations, trend mentions
**INFERRED:** Segment patterns deduced from company profile
**UNKNOWN:** No market-level insights in transcript (deal-specific only)

---

## Contract Compliance Validation

✅ **MUST HAVE:**
- [ ] Market segment identified (primary/secondary)
- [ ] Market fit score calculated (0-10)
- [ ] Trends cross-referenced to lens (4 validated trends)
- [ ] Segment insights captured (pain points, opportunities)
- [ ] LIR validation attempted (50% receivables signal)

❌ **MUST NOT:**
- [ ] Fabricate market trends not mentioned
- [ ] Provide market fit score without reasoning
- [ ] Skip segment identification

---

## Output Location

`knowledge_base/dimensional_annotations/[transcript_id]/META_extraction.yaml`

---

## Execution Time

**Target:** 2-3 minutes per transcript

---

## Quality Checklist

- [ ] Market segment mapped to lens (primary + 4 secondary)
- [ ] Market fit score calculated (0-10)
- [ ] Trends validated against 4 lens trends
- [ ] Segment insights captured
- [ ] LIR validation attempted
- [ ] Evidence has line citations
- [ ] Contract compliance validated

---

**Version:** 1.0
**Status:** READY FOR EXECUTION
**Pattern:** Parallel Fanout-Fanin (Fanout Layer)
**Next Agent:** META_extraction.yaml → Node_Synthesizer (Agent 2)
