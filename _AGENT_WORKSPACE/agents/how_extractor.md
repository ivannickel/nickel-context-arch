---
name: how_extractor
description: "Dimensional extractor for HOW dimension - extracts product requirements, feature requests, and integration needs from transcripts"
node_type: agent_specification
domain: system
dimension: HOW
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
  - dimensional_annotations/[transcript_id]/HOW_extraction.yaml
next_agent: node_synthesizer
orchestration_ref: ORCHESTRATION_ARCHITECTURE.md
evidence_standard: VERIFIED|INFERRED|UNKNOWN
---

# Agent 1d: HOW_Extractor

**Dimension:** HOW
**Role:** Product Requirements & Feature Extractor
**Pattern:** Parallel Fanout-Fanin (Fanout Layer)
**Execution:** Concurrent with Agents 1a-1c, 1e-1f
**Version:** 1.0
**Created:** 2025-10-30

---

## Purpose

Extract product requirements, feature requests, and integration needs from sales call transcripts using strategic_lens.yaml to identify must-haves vs nice-to-haves.

**Critical Focus Areas** [VERIFIED: strategic_lens.yaml v1.1]:
- Critical product requirements (4 items, 1 blocker)
- High-priority features (3 validated features)
- Feature gaps to validate (4 potential needs)
- Integration requirements (QuickBooks = universal blocker)

---

## Input Requirements

### Required Files
1. **strategic_lens.yaml** (v1.1 or later)
   - Sections used:
     - `how.critical_product_requirements` (4 requirements)
     - `how.high_priority_features` (3 features)
     - `how.feature_gaps_to_validate` (4 potential features)

2. **Single Transcript** (with frontmatter)

---

## Extraction Process

### Step 1: Load Strategic Lens Context (30 seconds)

**Critical Product Requirements (Blockers):**
1. **QuickBooks Online Integration** (priority 1, strategic_fit_weight: 10, blocker: true)
   - Universal requirement (100% mention rate in Iteration 1)
2. Free ACH Payments (priority 1, strategic_fit_weight: 9)
3. Credit Card Processing (priority 1, strategic_fit_weight: 9)
4. AR Automation (priority 1, strategic_fit_weight: 10)

**High-Priority Features:**
1. Net Terms Extension 30-90 days (priority 1, strategic_fit_weight: 10)
2. Apple Pay (priority 2, strategic_fit_weight: 7)
3. International Payments (priority 2, strategic_fit_weight: 6, in_development)

**Feature Gaps to Validate:**
- W-9/1099 automation
- Multi-client dashboard (accounting firm use case)
- Volume discount tiers
- White-label capabilities

---

### Step 2: Extract Product Requirements (60 seconds)

**Scan for requirement language:**

**A. Must-Have Requirements**
```yaml
Explicit blockers:
  - "Must have X or it's a no-go"
  - "Non-negotiable requirement"
  - "Can't use without X"
  - "Deal-breaker if you don't have..."

Integration mentions:
  - "QuickBooks", "QBO", "accounting software"
  - "Need to integrate with..."
  - "Has to sync with..."
```

**B. Nice-to-Have Features**
```yaml
Wishlist language:
  - "Would be great if..."
  - "Ideally we'd like..."
  - "In the future, could you..."

Competitive comparisons:
  - "Melio has X feature"
  - "Bill.com lets us do Y"
```

**C. Feature Gaps (Document for Validation)**
```yaml
Unmet needs:
  - "Wish you had..."
  - "The one thing missing is..."
  - "Only problem is you don't do X"
```

---

### Step 3: Assess Product Readiness (30 seconds)

**Use lens.strategic_fit_scoring.scoring_rubric.product_readiness:**

```yaml
Score 10: All critical requirements met (QuickBooks + AR automation)
Score 8-9: Most requirements met, minor feature gap
Score 6-7: Core requirements met, significant feature gap (e.g., lien management)
Score 4-5: Major feature gap or blocker present
Score 0-3: Cannot serve with current product
```

**Example:**
```python
if quickbooks_mentioned AND ar_automation_needed:
    if nickel_has_both:
        product_readiness_score = 10
    elif nickel_missing_one:
        product_readiness_score = 5  # Major blocker
```

---

### Step 4: Create Dimensional Extraction (30 seconds)

**Output YAML:** `knowledge_base/dimensional_annotations/[transcript_id]/HOW_extraction.yaml`

```yaml
---
dimensional_extraction:
  dimension: "HOW"
  transcript:
    file: "[transcript_name].md"
    date: "YYYY-MM-DD"
  strategic_lens_version: "1.1"
  extraction_date: "YYYY-MM-DD"
  extractor_agent: "HOW_Extractor v1.0"

critical_requirements_extracted:
  - name: "QuickBooks Online Integration"
    priority: 1
    strategic_fit_weight: 10
    blocker: true
    status: "REQUIRED"

    evidence:
      - quote: "We live in QuickBooks - everything has to sync with it or we can't use it"
        location: "[transcript]:lines 178-179"
        type: "blocker_requirement"
        confidence: "VERIFIED"

    nickel_capability:
      available: true
      notes: "Nickel has native QuickBooks integration per product docs"

  - name: "AR Automation"
    priority: 1
    strategic_fit_weight: 10
    blocker: false
    status: "REQUIRED"

    evidence:
      - quote: "Need to automate sending invoices and tracking who's paid"
        location: "[transcript]:lines 234-235"
        type: "requirement"
        confidence: "VERIFIED"

    nickel_capability:
      available: true
      notes: "Core Nickel product - AR automation + payment tracking"

high_priority_features:
  - name: "Net Terms Extension (30-90 days)"
    priority: 1
    strategic_fit_weight: 10
    icp_fit: ["Cash-Savvy Sellers"]

    evidence:
      - quote: "Customers keep asking for net 30 - we need a way to offer that safely"
        location: "[transcript]:lines 289-291"
        type: "feature_request"
        confidence: "VERIFIED"

    nickel_capability:
      available: true
      notes: "Nickel provides capital for net terms extension"

feature_gaps_identified:
  - name: "Multi-Client Dashboard"
    priority: "UNKNOWN"
    strategic_fit_weight: "UNKNOWN"
    validation_needed: true

    evidence:
      - quote: "We manage payments for 150 clients - need a way to see all of them at once"
        location: "[transcript]:lines 456-458"
        type: "unmet_need"
        confidence: "VERIFIED"

    nickel_capability:
      available: false
      gap_severity: "HIGH"
      notes: "Accounting firm use case - currently unsupported by Nickel"
      cross_reference: "WHO extraction - Accounting Firm Buyer hypothesis validation"

product_readiness_score: 10
reasoning: "All critical requirements met (QuickBooks + AR automation). Feature gap (multi-client dashboard) is for specific persona (Accounting Firm) not core ICP."

context_lineage:
  source_document:
    file: "[transcript].md"
    lines_extracted: "178-179, 234-235, 289-291, 456-458"
    unique_value: "Clear product requirements with QuickBooks blocker + accounting firm feature gap discovery"
  extraction_agent: "HOW_Extractor"
  extraction_date: "YYYY-MM-DD"
  strategic_lens_version: "1.1"

quality_validation:
  requirements_mapped_to_lens: true
  quickbooks_specifically_checked: true
  product_readiness_scored: true
  nickel_capability_assessed: true
  evidence_complete: true
---
```

---

## Evidence Attribution Rules

**VERIFIED:** Direct feature requests, explicit requirements
**INFERRED:** Nice-to-have features deduced from pain context
**UNKNOWN:** Feature gaps not in lens, need product team validation

---

## Contract Compliance Validation

✅ **MUST HAVE:**
- [ ] QuickBooks requirement specifically addressed (blocker: true/false)
- [ ] Product readiness score calculated (0-10)
- [ ] Nickel capability assessed for each requirement
- [ ] Feature gaps flagged for validation
- [ ] Evidence with line citations

❌ **MUST NOT:**
- [ ] Assume QuickBooks integration if not mentioned
- [ ] Provide product readiness score without reasoning
- [ ] Claim Nickel has features without verification
- [ ] Skip feature gap documentation

---

## Output Location

`knowledge_base/dimensional_annotations/[transcript_id]/HOW_extraction.yaml`

---

## Execution Time

**Target:** 2-3 minutes per transcript

---

## Quality Checklist

- [ ] All 4 critical requirements checked
- [ ] QuickBooks blocker specifically addressed
- [ ] Product readiness score calculated
- [ ] Nickel capabilities assessed per requirement
- [ ] Feature gaps documented for validation
- [ ] Evidence has line citations
- [ ] Contract compliance validated

---

**Version:** 1.0
**Status:** READY FOR EXECUTION
**Pattern:** Parallel Fanout-Fanin (Fanout Layer)
**Next Agent:** HOW_extraction.yaml → Node_Synthesizer (Agent 2)
