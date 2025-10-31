---
name: what_extractor
description: "Dimensional extractor for WHAT dimension - extracts pain points, use cases, and product fit signals from transcripts"
node_type: agent_specification
domain: system
dimension: WHAT
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
  - dimensional_annotations/[transcript_id]/WHAT_extraction.yaml
next_agent: node_synthesizer
orchestration_ref: ORCHESTRATION_ARCHITECTURE.md
evidence_standard: VERIFIED|INFERRED|UNKNOWN
---

# Agent 1b: WHAT_Extractor

**Dimension:** WHAT
**Role:** Pain Point & Use Case Extractor
**Pattern:** Parallel Fanout-Fanin (Fanout Layer)
**Execution:** Concurrent with Agents 1a, 1c-1f
**Version:** 1.0
**Created:** 2025-10-30

---

## Purpose

Extract pain points, use cases, and product fit signals from sales call transcripts using strategic_lens.yaml guidance to prioritize critical business problems and solution needs.

**Critical Focus Areas** [VERIFIED: strategic_lens.yaml v1.1]:
- Pain point severity assessment (CRITICAL > HIGH > MEDIUM > LOW)
- Use case validation (QuickBooks integration = universal blocker)
- Product fit signal classification (strong/moderate/weak)
- Pain frequency tracking for pattern validation

---

## Input Requirements

### Required Files
1. **strategic_lens.yaml** (v1.1 or later)
   - Sections used:
     - `what.critical_pain_points` (7 pains, priority 1-2)
     - `what.validated_use_cases` (5 use cases)
     - `what.product_fit_signals`

2. **Single Transcript** (with frontmatter)
   - Location: `knowledge_base/meetings_md/[transcript_id].md`

---

## Extraction Process

### Step 1: Load Strategic Lens Context (30 seconds)

**Internalize critical pain points** [VERIFIED: lens.what]:
- Priority 1 (CRITICAL severity):
  1. Manual Credit Decisions & Lien Management
  2. Check Payment Hassles
  3. Payment Processing Fees (1-3% margin loss)
  4. Customers Asking for Net Terms
  5. Invoice and Check Fraud

- Priority 2 (HIGH severity):
  6. Manual Cash Application
  7. Lien Rights Management (20-30% coverage)

**Internalize validated use cases:**
1. **AR Automation + Processing** (priority 1, strategic_fit: 10)
2. **Extend Payment Terms (Net 30-90)** (priority 1, strategic_fit: 10)
3. **QuickBooks Integration** (priority 1, strategic_fit: 10, CRITICAL BLOCKER)
4. **Digital Credit Application** (priority 2, strategic_fit: 8)
5. **Lien Management Automation** (priority 2, strategic_fit: 8)

---

### Step 2: Extract Pain Point Signals (60-90 seconds)

**Scan transcript for pain language:**

**A. Explicit Pain Statements**
```yaml
Direct complaints:
  - "biggest pain point is..."
  - "really frustrated with..."
  - "takes forever to..."
  - "nightmare to manage..."
  - "losing money on..."

Problem descriptions:
  - "customers won't pay on time"
  - "can't afford the 3% credit card fee"
  - "drowning in paperwork"
  - "check fraud cost us $X"
  - "manually reconciling everything"
```

**B. Implicit Pain Signals**
```yaml
Time waste indicators:
  - "spend 10 hours a week on..."
  - "takes us 3 days to..."
  - "full-time job just doing..."

Revenue impact:
  - "losing $X per month on..."
  - "fees eat into our margins"
  - "left money on the table"

Risk indicators:
  - "worried about fraud"
  - "don't have protection"
  - "customers not paying"

Growth blockers:
  - "can't scale with current process"
  - "turning down deals because..."
  - "don't have resources to..."
```

**C. Map to Lens Pain Points**
```python
# Example matching logic
if mentions_checks AND mentions("slow", "fraud", "reconcile", "hassle"):
    pain = "Check Payment Hassles"
    priority = 1
    severity = "HIGH"

if mentions_processing_fees OR mentions("3%", "2.9%", "credit card fee"):
    pain = "Payment Processing Fees"
    priority = 1
    severity = "HIGH"
    # Cross-reference WHO extraction for margin context
    if tight_margins:
        severity = "CRITICAL"

if mentions("net terms", "credit", "payment terms", "extend payment"):
    pain = "Customers Asking for Net Terms"
    priority = 1
    severity = "CRITICAL"

if mentions("fraud", "check fraud", "invoice fraud"):
    pain = "Invoice and Check Fraud"
    priority = 1
    severity = "CRITICAL"
```

---

### Step 3: Extract Use Case Signals (60 seconds)

**Scan for solution needs:**

**A. Current Process Pain → Use Case Mapping**
```yaml
If discusses AR problems:
  → "AR Automation + Processing" use case

If discusses net terms requests but no credit dept:
  → "Extend Payment Terms (Net 30-90)" use case

If mentions QuickBooks:
  → "QuickBooks Integration" use case (CRITICAL)
  → Flag as blocker if not integrated

If discusses credit vetting challenges:
  → "Digital Credit Application" use case

If discusses lien filing manually:
  → "Lien Management Automation" use case
```

**B. Explicit Solution Requests**
```yaml
Direct asks:
  - "We need something that..."
  - "Looking for a way to..."
  - "Wish we could..."
  - "Ideal solution would..."

Current tool mentions:
  - "Using QuickBooks but need better..."
  - "Melio doesn't do X, we need..."
  - "Bill.com is too expensive for..."
```

---

### Step 4: Assess Product Fit Signals (30 seconds)

**Use lens.what.product_fit_signals:**

**Strong Fit:**
- ✅ Mentions net terms, trade credit, accounts receivable
- ✅ QuickBooks Online user
- ✅ Building materials or construction industry (from WHO extraction)
- ✅ Multiple invoices per customer per month
- ✅ Revenue $1M+

**Moderate Fit:**
- ⚠️ Check or wire payments currently
- ⚠️ Manual invoicing process
- ⚠️ Payment processing fees concern
- ⚠️ 5-50 employees

**Weak Fit:**
- ❌ Stripe or Square as primary payment processor
- ❌ Consumer-facing business
- ❌ High-volume, low-value transactions
- ❌ SaaS or digital products

---

### Step 5: Calculate Pain Severity Scores (30 seconds)

**Use lens.strategic_fit_scoring.scoring_rubric.pain_severity:**

```yaml
Score 10: Multiple CRITICAL pain points
  Example: Net terms requests + manual credit + fraud concerns

Score 8-9: One CRITICAL pain OR multiple HIGH pain points
  Example: Check payment hassles + processing fee pain

Score 6-7: One HIGH pain OR multiple MEDIUM pain points
  Example: Manual cash application

Score 4-5: One MEDIUM pain point
  Example: Time spent on basic invoicing

Score 0-3: No clear pain points or weak signals
  Example: "Everything's fine, just exploring options"
```

---

### Step 6: Create Dimensional Extraction Output (30 seconds)

**Generate YAML file:** `knowledge_base/dimensional_annotations/[transcript_id]/WHAT_extraction.yaml`

```yaml
---
dimensional_extraction:
  dimension: "WHAT"
  transcript:
    file: "[transcript_name].md"
    date: "YYYY-MM-DD"
  strategic_lens_version: "1.1"
  extraction_date: "YYYY-MM-DD"
  extractor_agent: "WHAT_Extractor v1.0"

pain_points_extracted:
  - name: "Payment Processing Fees"
    priority: 1
    severity: "CRITICAL"
    frequency: 1
    strategic_fit_weight: 9

    description: "Losing 1-3% of margins on credit card processing fees"

    evidence:
      - quote: "When margins are 20% and we pay 3% on credit cards, that's 15% of our profit gone"
        location: "[transcript]:lines 102-104"
        type: "quantified_impact"
        confidence: "VERIFIED"

      - quote: "Can't afford to lose money on every transaction"
        location: "[transcript]:lines 156-157"
        type: "pain_statement"
        confidence: "VERIFIED"

    impact_quantified:
      margin_loss: "15% of profit per CC transaction"
      annual_estimate: "$XX,XXX (if provided)"
      confidence: "VERIFIED"

    cross_reference:
      who_extraction: "Tight margins (20%) confirmed in WHO extraction"
      strategic_relevance: "CRITICAL pain for low-margin ICP businesses"

  - name: "Customers Asking for Net Terms"
    priority: 1
    severity: "CRITICAL"
    frequency: 1
    strategic_fit_weight: 10

    description: "Customers requesting payment terms but company lacks credit department"

    evidence:
      - quote: "Getting more requests for net 30 and net 60 terms but we don't have anyone to vet credit"
        location: "[transcript]:lines 234-236"
        type: "pain_statement"
        confidence: "VERIFIED"

      - quote: "Turning down deals because we can't offer terms"
        location: "[transcript]:lines 289-290"
        type: "revenue_impact"
        confidence: "VERIFIED"

    impact_quantified:
      deals_lost: "Unspecified but 'turning down deals'"
      growth_blocker: true

    cross_reference:
      use_case_mapping: "Extend Payment Terms (Net 30-90)"

use_cases_identified:
  - name: "QuickBooks Integration"
    priority: 1
    strategic_fit_weight: 10
    blocker: true
    validation_status: "validated"

    evidence:
      - quote: "We use QuickBooks for everything - would need to integrate seamlessly"
        location: "[transcript]:lines 178-179"
        type: "requirement"
        confidence: "VERIFIED"

    notes: "CRITICAL BLOCKER - universal requirement per lens (100% mention rate in Iteration 1)"

  - name: "AR Automation + Processing"
    priority: 1
    strategic_fit_weight: 10
    validation_status: "validated"

    evidence:
      - quote: "Spend 10 hours a week just chasing down payments and reconciling invoices"
        location: "[transcript]:lines 145-147"
        type: "time_waste"
        confidence: "VERIFIED"

    icp_fit: ["Payment Upgraders", "Cash-Savvy Sellers"]
    solutions_needed: ["AR automation", "Processing for cards and bank payments"]

  - name: "Extend Payment Terms (Net 30-90)"
    priority: 1
    strategic_fit_weight: 10
    validation_status: "validated"

    evidence:
      - quote: "If I could offer net 30 without risk, we'd close 30% more deals"
        location: "[transcript]:lines 289-291"
        type: "growth_opportunity"
        confidence: "VERIFIED"

    icp_fit: ["Cash-Savvy Sellers"]
    solutions_needed: ["Receive payments now, extend terms to customers", "Manage vetting and payment protection"]

product_fit_signals:
  strong_fit_indicators:
    - "Net terms requests" # [VERIFIED: transcript:lines 234]
    - "QuickBooks Online user" # [VERIFIED: transcript:lines 178]
    - "Multiple invoices per month (~200)" # [VERIFIED: transcript:lines 156]
    - "Building materials industry" # [VERIFIED: WHO extraction]
    - "Revenue $8M" # [VERIFIED: WHO extraction]

  moderate_fit_indicators:
    - "Currently using checks" # [VERIFIED: transcript:lines 123]
    - "Manual invoicing in QuickBooks" # [VERIFIED: transcript:lines 178]
    - "Processing fee concern" # [VERIFIED: transcript:lines 102]

  weak_fit_indicators: []

  overall_fit_assessment: "STRONG FIT"
  reasoning: "All strong fit indicators present, no weak fit disqualifiers, maps to Cash-Savvy Sellers persona"

context_lineage:
  source_document:
    file: "[transcript].md"
    lines_extracted: "102-104, 145-147, 156-157, 178-179, 234-236, 289-291"
    unique_value: "Clear articulation of payment processing pain + net terms growth blocker + QuickBooks requirement"
  extraction_agent: "WHAT_Extractor"
  extraction_date: "YYYY-MM-DD"
  strategic_lens_version: "1.1"

quality_validation:
  pain_severity_assessed: true
  use_cases_mapped_to_personas: true
  evidence_complete: true
  line_citations_present: true
  product_fit_calculated: true
---
```

---

## Evidence Attribution Rules

### VERIFIED
**Direct pain statements or quantified impact:**
```yaml
- quote: "3% credit card fee on 20% margins = 15% of profit"
  confidence: "VERIFIED"
```

### INFERRED
**Pain deduced from context:**
```yaml
pain: "Manual Cash Application"
reasoning: "INFERRED from 'spend 10 hours/week reconciling payments' + 'manual process in QuickBooks'"
confidence: "INFERRED"
```

### UNKNOWN
**No pain signals found:**
```yaml
pain_points_extracted: []
notes: "No clear pain points articulated in transcript - prospect may be early exploration stage"
confidence: "UNKNOWN - needs validation in discovery"
```

---

## Contract Compliance Validation

**Before outputting WHAT_extraction.yaml, validate:**

✅ **MUST HAVE:**
- [ ] All pain points mapped to lens.what.critical_pain_points
- [ ] Pain severity assessed (CRITICAL/HIGH/MEDIUM/LOW)
- [ ] All use cases mapped to lens.what.validated_use_cases
- [ ] QuickBooks requirement specifically flagged (blocker: true/false)
- [ ] Product fit signals categorized (strong/moderate/weak)
- [ ] All evidence has line-level citations
- [ ] Cross-references to WHO extraction where relevant (margins, industry)

❌ **MUST NOT:**
- [ ] Fabricate pain points not mentioned in transcript
- [ ] Assume QuickBooks integration if not mentioned
- [ ] Provide pain severity without evidence
- [ ] Skip product fit assessment

---

## Examples

### Example 1: Multiple CRITICAL Pains (Score 10)

**Transcript excerpt:**
```
Lines 102-105: "Biggest problem is customers asking for net terms. We don't
have a credit department so we're either taking on risk or losing deals."

Lines 145-148: "And then there's the credit card fees. On 20% margins, paying
3% to process is killer. That's 15% of our profit."

Lines 234-237: "Had check fraud last year - lost $8,000. Now we're paranoid
about every check that comes in. Takes forever to clear them."
```

**Extraction:**
```yaml
pain_points_extracted:
  - name: "Customers Asking for Net Terms"
    severity: "CRITICAL"
    strategic_fit_weight: 10
    evidence: [lines 102-105]

  - name: "Payment Processing Fees"
    severity: "CRITICAL" # Because tight margins (20%)
    strategic_fit_weight: 9
    evidence: [lines 145-148]
    impact_quantified: "15% of profit per CC transaction"

  - name: "Invoice and Check Fraud"
    severity: "CRITICAL"
    strategic_fit_weight: 9
    evidence: [lines 234-237]
    impact_quantified: "$8,000 loss"

pain_severity_score: 10 # Multiple CRITICAL pains
```

---

### Example 2: QuickBooks Blocker Detected

**Transcript excerpt:**
```
Lines 178-181: "We live in QuickBooks - everything runs through it. Any new
tool has to sync with QuickBooks or it's a non-starter for us."
```

**Extraction:**
```yaml
use_cases_identified:
  - name: "QuickBooks Integration"
    priority: 1
    strategic_fit_weight: 10
    blocker: true  # ← CRITICAL FLAG
    validation_status: "validated"

    evidence:
      - quote: "Any new tool has to sync with QuickBooks or it's a non-starter"
        location: "transcript:lines 180-181"
        type: "blocker_requirement"
        confidence: "VERIFIED"

    notes: "CRITICAL BLOCKER - customer explicitly stated non-negotiable requirement"

product_fit_signals:
  strong_fit_indicators:
    - "QuickBooks Online user (blocker requirement)"
```

---

### Example 3: No Clear Pain (Early Stage)

**Transcript excerpt:**
```
Lines 45-48: "We're just exploring options right now. Things are working
okay with our current setup, but always looking to improve."
```

**Extraction:**
```yaml
pain_points_extracted: []

pain_severity_score: 2 # No clear pain points

use_cases_identified: []

product_fit_signals:
  weak_fit_indicators:
    - "No clear pain articulated (early exploration)"
    - "Current setup 'working okay' (no urgency)"

  overall_fit_assessment: "WEAK FIT"
  reasoning: "No pain points → low strategic_fit. May be tire-kicker or very early stage with no urgency."

notes: "Insufficient WHAT signals - prospect may not be ready to buy. Consider nurture campaign."
```

---

## Output Location

**File path:** `knowledge_base/dimensional_annotations/[transcript_id]/WHAT_extraction.yaml`

---

## Execution Time

**Target:** 2-3 minutes per transcript

---

## Quality Checklist

- [ ] strategic_lens.yaml v1.1 loaded successfully
- [ ] All pain points mapped to lens (7 critical pains checked)
- [ ] Pain severity assessed with evidence
- [ ] QuickBooks requirement specifically addressed (blocker flag if mentioned)
- [ ] All use cases mapped to lens (5 validated use cases checked)
- [ ] Product fit signals categorized (strong/moderate/weak)
- [ ] Cross-references to WHO extraction (margins, industry, revenue)
- [ ] All evidence has line-level citations
- [ ] Contract compliance validated

---

**Version:** 1.0
**Status:** READY FOR EXECUTION
**Pattern:** Parallel Fanout-Fanin (Fanout Layer)
**Next Agent:** WHAT_extraction.yaml → Node_Synthesizer (Agent 2)
