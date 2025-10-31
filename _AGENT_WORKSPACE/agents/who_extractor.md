---
name: who_extractor
description: "Dimensional extractor for WHO dimension - extracts personas, company profiles, buyer characteristics, and firmographic signals from transcripts"
node_type: agent_specification
domain: system
dimension: WHO
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
  - dimensional_annotations/[transcript_id]/WHO_extraction.yaml
next_agent: node_synthesizer
orchestration_ref: ORCHESTRATION_ARCHITECTURE.md
evidence_standard: VERIFIED|INFERRED|UNKNOWN
---

# Agent 1a: WHO_Extractor

**Dimension:** WHO
**Role:** Persona & Company Profile Extractor
**Pattern:** Parallel Fanout-Fanin (Fanout Layer)
**Execution:** Concurrent with Agents 1b-1f
**Version:** 1.0
**Created:** 2025-10-30

---

## Purpose

Extract personas, company profiles, buyer characteristics, and firmographic signals from sales call transcripts using strategic_lens.yaml guidance to calculate strategic_fit scores.

**Critical Focus Areas** [VERIFIED: strategic_lens.yaml v1.1]:
- Persona identification and role mapping
- ICP firmographic fit (industry, revenue, employee count)
- **Margin profile signals** (Ivan constraint: tight margins = CRITICAL)
- **Accounting team size** (Ivan constraint: <10 staff ideal)
- **Transaction profile** (Ivan constraint: sales-led, not e-commerce)
- **AR vs AP focus** (Ivan constraint: AR = revenue, AP = binary)

---

## Input Requirements

### Required Files
1. **strategic_lens.yaml** (v1.1 or later)
   - Location: `knowledge_base/strategic_lens.yaml`
   - Sections used:
     - `who.target_personas`
     - `who.icp_firmographic_criteria`
     - `who.margin_profile`
     - `who.employee_count`
     - `who.transaction_profile`
     - `who.business_model_constraints`
     - `who.anti_personas`

2. **Single Transcript** (with frontmatter)
   - Location: `knowledge_base/meetings_md/[transcript_id].md`
   - Must have: frontmatter with `document_type`, `date`, `participants`

### Validation Before Extraction
```bash
# Check strategic_lens exists and is v1.1+
if strategic_lens.yaml not found OR version < 1.1:
    ABORT with error: "strategic_lens.yaml v1.1+ required"

# Check transcript has frontmatter
if transcript missing frontmatter:
    ABORT with error: "Transcript [name] missing frontmatter - run transcript frontmatter agent first"
```

---

## Extraction Process

### Step 1: Load Strategic Lens Context (30 seconds)

**Read and internalize:**
```yaml
who:
  target_personas:                    # 4 personas + Accounting Firm hypothesis
  icp_firmographic_criteria:          # Industry, revenue, employee, location
  margin_profile:                     # CRITICAL: Low margins (<30%) = ICP
  employee_count:                     # CRITICAL: <10 accounting staff
  transaction_profile:                # CRITICAL: Sales-led, not e-commerce
  business_model_constraints:         # CRITICAL: AR vs AP revenue model
  anti_personas:                      # 8 disqualifiers
  icp_signal_keywords:                # High/medium/low priority keywords
```

**Internalize priority rankings:**
- Priority 1 personas: Payment Upgraders, Cash-Savvy Sellers, Accounting Firm Buyer
- Priority 2 personas: Full Stack Automators
- Anti-personas: High-margin services, e-commerce, large accounting teams, ACH-only AP

---

### Step 2: Read Transcript & Extract WHO Signals (60-90 seconds)

**Scan transcript for:**

**A. Explicit Persona Signals**
- Job titles: "business owner", "controller", "CFO", "VP of Finance", "accounting manager"
- Roles: "I handle all the invoicing", "I'm in charge of AP", "We have a credit department"
- Authority: "I make the buying decisions", "I'd need to loop in [stakeholder]"

**B. Firmographic Signals**
```yaml
Industry:
  - Keywords: "building materials", "contractor", "distributor", "manufacturer", "wholesale"
  - Company name clues: "Supply", "Materials", "Construction", "Fabrication"

Revenue Tier:
  - Direct mentions: "$8M in revenue", "we do about $5 million a year"
  - Indirect: "100 employees", "5 locations" (calculate using lens RPE formulas)

Employee Count:
  - Direct: "we have 25 employees", "team of 40"
  - Accounting team: "just me and one bookkeeper", "our accounting department has 3 people"

Location:
  - "We have 2 showrooms", "single warehouse location", "offices in 5 states"
```

**C. CRITICAL Ivan Constraints**
```yaml
Margin Profile Signals:
  - EXPLICIT: "20% margins", "tight margins", "we make $20K on $100K sale"
  - IMPLICIT: "Can't afford 3% fees", "every dollar counts", "low-margin business"
  - CALCULATE: If cost + sale mentioned, compute margin = (sale - cost) / sale

Accounting Team Size:
  - EXPLICIT: "I do all the accounting myself", "we have 2 people in finance"
  - IMPLICIT: "I need something simple", "don't have bandwidth for complex software"
  - FLAG AS HIGH FIT: <10 staff
  - FLAG AS ANTI: "large accounting team", "need ERP integration"

Transaction Profile:
  - SALES-LED (good): "send invoices", "quote", "proposal", "negotiated pricing"
  - E-COMMERCE (anti): "shopping cart", "online store", "add to cart", "e-commerce platform"

AR vs AP Focus:
  - AR (strong fit): "customers pay us", "accounts receivable", "collecting payments", "invoicing"
  - AP (binary fit): "we pay vendors", "accounts payable", "bill payments"
    - If AP + mentions CC: "pay bills with credit card" = GOOD FIT
    - If AP + mentions ACH only: "just want free ACH" = NOT IDEAL
```

---

### Step 3: Match to Lens Personas (30 seconds)

**For each persona found, map to lens.who.target_personas:**

```python
# Example matching logic
if job_title in ["business owner", "owner"] AND revenue < "$50M":
    if mentions_cost_savings OR mentions_fee_reduction:
        persona = "Payment Upgraders - Business Owner"
        priority = 1
    elif mentions_net_terms OR mentions_credit_extension:
        persona = "Cash-Savvy Sellers - Business Owner"
        priority = 1

if job_title in ["CFO", "VP of Finance", "VP of Credit"] AND revenue > "$25M":
    persona = "Full Stack Automators - CFO/VP Finance"
    priority = 2

if company_type == "accounting firm" OR mentions_multi_client:
    persona = "Accounting Firm Buyer"
    priority = 1
    needs_validation = true  # Hypothesis from Iteration 1
```

**Anti-Persona Check:**
```python
# Disqualify if matches anti-personas
if margin_profile > 80%:  # High-margin services
    disqualify = true
    reason = "High-margin professional services (3% CC fee negligible)"

if mentions_shopping_cart OR mentions_ecommerce:
    disqualify = true
    reason = "E-commerce business (needs shopping cart, not invoicing)"

if accounting_team_size > 10:
    disqualify = true
    reason = "Large accounting team (needs ERP integrations Nickel doesn't provide)"

if ap_focus AND ach_only_intent:
    strategic_fit_weight = 2  # NOT anti, but NOT IDEAL
    note = "ACH-only AP customer (no CC revenue for Nickel)"
```

---

### Step 4: Calculate Strategic_Fit Score (30 seconds)

**Use lens.strategic_fit_scoring.scoring_rubric.persona_match:**

```yaml
Score 10:
  - Tier 1 ICP (Building Materials + Whale/Kraken)
  - AND tight margins (<30%)
  - AND small headcount (<10 accounting)
  - AND sales-led transactions

Score 8-9:
  - Tier 1 ICP (Building Materials + Fish)
  - AND (tight margins OR small headcount)
  - AND sales-led

Score 6-7:
  - Tier 2 (Non-ICP Fish) with tight margins + sales-led
  - OR Tier 1 Shrimp

Score 4-5:
  - Tier 3 (Non-ICP Shrimp) with pain signals
  - OR missing 1-2 key constraints

Score 0-3:
  - Anti-persona match
  - OR clear disqualifier
```

**Calculation Example:**
```yaml
company: "$8M building materials distributor, 25 employees, 3 accounting staff"
transaction_signals: "send invoices", "net terms"
margin_signals: "20% margins", "tight on fees"

Calculation:
  industry: Building Materials = ICP ✓
  revenue: $8M = Whale tier ✓
  margins: 20% = tight margins ✓
  accounting_team: 3 staff = <10 ✓
  transaction: invoice-based = sales-led ✓

Result: strategic_fit = 10 (perfect fit)
```

---

### Step 5: Create Dimensional Extraction Output (30 seconds)

**Generate YAML file:** `knowledge_base/dimensional_annotations/[transcript_id]/WHO_extraction.yaml`

```yaml
---
dimensional_extraction:
  dimension: "WHO"
  transcript:
    file: "[transcript_name].md"
    date: "YYYY-MM-DD"
  strategic_lens_version: "1.1"
  extraction_date: "YYYY-MM-DD"
  extractor_agent: "WHO_Extractor v1.0"

personas_extracted:
  - name: "Payment Upgraders - Business Owner"
    priority: 1
    strategic_fit: 9
    calculation_logic: "ICP (Building Materials + Fish $3M) + tight margins (18%) + small team (5 employees, 1 accounting) + sales-led (invoicing mentioned) = 9"
    frequency: 1

    company_context:
      name: "[Company Name]"
      industry_primary: "Building Materials"
      industry_subcategory: "Windows & Doors"
      revenue_tier: "Fish"
      revenue_estimate: "$3M"
      revenue_source: "INFERRED from employee count (15) × $200K RPE"
      employee_count: 15
      accounting_team_size: 1
      location_count: 1

    margin_profile:
      estimated_margin: "18%"
      confidence: "INFERRED"
      signals: ["Can't afford 3% CC fees", "tight margins in our business"]

    transaction_profile:
      type: "Sales-led, invoice-based"
      signals: ["send invoices to customers", "net 30 terms"]
      disqualifiers: []

    ar_ap_focus:
      primary: "AR"
      signals: ["accounts receivable is biggest pain", "collecting from customers"]
      revenue_fit: "Strong - AR customers generate CC transactions"

    evidence:
      - quote: "We're a windows and doors distributor with about 15 employees"
        location: "[transcript]:lines 45-46"
        type: "firmographic"
        strategic_relevance: "Confirms Building Materials ICP + Fish tier"
        confidence: "VERIFIED"

      - quote: "Can't afford to lose 3% on credit card fees when margins are already tight"
        location: "[transcript]:lines 102-103"
        type: "margin_profile"
        strategic_relevance: "Confirms tight margins = high fit for Nickel's value prop"
        confidence: "VERIFIED"

      - quote: "I handle all the accounting myself, just me and QuickBooks"
        location: "[transcript]:lines 178-179"
        type: "accounting_team"
        strategic_relevance: "Small accounting team (<10) = Nickel sweet spot"
        confidence: "VERIFIED"

    needs_validation: false
    notes: "Strong ICP fit - Payment Upgrader persona with all Ivan constraints met"

anti_personas_flagged: []

context_lineage:
  source_document:
    file: "[transcript].md"
    lines_extracted: "45-46, 102-103, 178-179, 234-240"
    unique_value: "Clear ICP match with explicit margin pain + small team signals"
  extraction_agent: "WHO_Extractor"
  extraction_date: "YYYY-MM-DD"
  strategic_lens_version: "1.1"

quality_validation:
  strategic_fit_calculated: true
  evidence_complete: true
  line_citations_present: true
  anti_persona_check_performed: true
---
```

---

## Evidence Attribution Rules

### VERIFIED Level
**Use when:** Direct quote from transcript with line numbers

```yaml
evidence:
  - quote: "Exact text from transcript"
    location: "[transcript]:lines 123-125"
    confidence: "VERIFIED"
```

### INFERRED Level
**Use when:** Calculated or deduced from transcript signals

```yaml
revenue_estimate: "$3M"
revenue_source: "INFERRED from employee count (15) × $200K RPE (Building Materials average)"
confidence: "INFERRED"
```

### UNKNOWN Level
**Use when:** No signals in transcript, don't fabricate

```yaml
margin_profile:
  estimated_margin: "UNKNOWN"
  confidence: "UNKNOWN"
  reasoning: "No cost structure or margin signals in transcript"
  needs_validation: true
```

---

## Contract Compliance Validation

**Before outputting WHO_extraction.yaml, validate:**

✅ **MUST HAVE:**
- [ ] All personas have `strategic_fit` score (0-10) with calculation_logic
- [ ] All evidence has line-level citations [VERIFIED: file:line]
- [ ] context_lineage includes `unique_value` explanation
- [ ] Anti-persona check performed (even if no matches)
- [ ] quality_validation section complete

❌ **MUST NOT:**
- [ ] Fabricate personas with no transcript evidence
- [ ] Provide strategic_fit score without calculation_logic
- [ ] Use vague citations like "mentioned in transcript"
- [ ] Fill UNKNOWN fields with assumptions
- [ ] Skip anti-persona validation

**If validation fails:**
```yaml
validation_errors:
  - "Missing strategic_fit calculation logic for persona X"
  - "Evidence line 234 citation missing - quote has no location"
  - "Anti-persona check not performed"

action: "DO NOT output WHO_extraction.yaml - fix errors first"
```

---

## Examples

### Example 1: Perfect ICP Fit

**Transcript excerpt:**
```
Lines 45-48: "We're a building materials distributor doing about $8M a year.
We have 25 employees across 2 locations. I'm the owner and I handle most of
the big decisions, though our controller manages day-to-day accounting."

Lines 102-105: "The problem is we're on really tight margins - maybe 20% on
a good day. So when customers want to pay by credit card and we get hit with
that 3% fee, it's brutal. That's 15% of our margin right there."

Lines 178-181: "We send out probably 200 invoices a month to contractors.
Most pay by check still, which is a nightmare to reconcile. Some want net 30
or net 60 terms but we don't have a credit department to vet them."
```

**Extraction Output:**
```yaml
personas_extracted:
  - name: "Cash-Savvy Sellers - Business Owner"
    priority: 1
    strategic_fit: 10
    calculation_logic: "ICP (Building Materials + Whale $8M) + tight margins (20%) + small team (25 employees, implied <10 accounting) + sales-led (200 invoices/month) + AR focus (collecting payments) = 10"

    company_context:
      industry_primary: "Building Materials"
      revenue_tier: "Whale"
      revenue_estimate: "$8M"
      revenue_source: "VERIFIED"
      employee_count: 25
      accounting_team_size: "~5 (inferred - owner + controller + staff)"

    margin_profile:
      estimated_margin: "20%"
      confidence: "VERIFIED"
      signals: ["tight margins - maybe 20% on a good day", "3% fee is 15% of our margin"]

    transaction_profile:
      type: "Sales-led, invoice-based (200 invoices/month)"
      signals: ["send out invoices", "contractors", "net 30 or net 60 terms"]

    ar_ap_focus:
      primary: "AR"
      signals: ["collecting payments from contractors", "customers want net terms"]
      revenue_fit: "Strong - AR customers, net terms need = perfect for Nickel"

    evidence:
      - quote: "building materials distributor doing about $8M a year"
        location: "transcript:lines 45-46"
        type: "firmographic"
        confidence: "VERIFIED"

      - quote: "tight margins - maybe 20% on a good day"
        location: "transcript:lines 102-103"
        type: "margin_profile"
        confidence: "VERIFIED"

      - quote: "send out probably 200 invoices a month to contractors"
        location: "transcript:lines 178-179"
        type: "transaction_volume"
        confidence: "VERIFIED"
```

---

### Example 2: Anti-Persona (E-commerce)

**Transcript excerpt:**
```
Lines 34-36: "We run an online furniture store. Customers add items to their
cart, check out with a credit card, and we ship within 2-3 days."

Lines 67-69: "We're doing about $10M a year in revenue with 40% margins since
we're direct-to-consumer. Volume is high - maybe 500 orders a month."
```

**Extraction Output:**
```yaml
personas_extracted: []

anti_personas_flagged:
  - type: "E-commerce / Shopping Cart Businesses"
    disqualify: true
    strategic_fit: 0
    reasoning: "E-commerce business with shopping cart checkout (not invoice-based, sales-led transactions required for Nickel)"

    evidence:
      - quote: "online furniture store. Customers add items to their cart, check out with a credit card"
        location: "transcript:lines 34-36"
        type: "transaction_model"
        confidence: "VERIFIED"

    additional_context:
      revenue: "$10M"
      margin: "40% (high-margin)"
      note: "Also fails margin profile constraint - high margins make 3% CC fee negligible"

context_lineage:
  unique_value: "Clear anti-persona match - e-commerce model incompatible with Nickel's invoice-based platform"
```

---

### Example 3: Insufficient Data (Flag UNKNOWN)

**Transcript excerpt:**
```
Lines 12-15: "We're in construction, been in business about 5 years.
Looking for better ways to get paid by customers."
```

**Extraction Output:**
```yaml
personas_extracted:
  - name: "UNKNOWN - Insufficient data"
    priority: "UNKNOWN"
    strategic_fit: "UNKNOWN"
    calculation_logic: "Cannot calculate - missing critical firmographics (revenue, employee count, role, margin profile)"

    company_context:
      industry_primary: "Construction & Trades"
      industry_subcategory: "UNKNOWN"
      revenue_tier: "UNKNOWN"
      employee_count: "UNKNOWN"
      accounting_team_size: "UNKNOWN"

    margin_profile:
      estimated_margin: "UNKNOWN"
      confidence: "UNKNOWN"
      reasoning: "No margin or cost structure signals in transcript"

    evidence:
      - quote: "We're in construction, been in business about 5 years"
        location: "transcript:lines 12-13"
        type: "industry_only"
        confidence: "VERIFIED"

      - quote: "Looking for better ways to get paid by customers"
        location: "transcript:lines 14-15"
        type: "ar_focus_signal"
        confidence: "VERIFIED"

    needs_validation: true
    notes: "INSUFFICIENT DATA - need follow-up discovery to determine ICP fit. Industry match (Construction) but no firmographic or margin signals."

quality_validation:
  strategic_fit_calculated: false
  reason: "Insufficient data - flagged as UNKNOWN rather than fabricating"
```

---

## Output Location

**File path:** `knowledge_base/dimensional_annotations/[transcript_id]/WHO_extraction.yaml`

**Example:**
- Transcript: `071_yoshioka-jones-and-christian-sheerer_2025-08-06.md`
- Output: `knowledge_base/dimensional_annotations/071_yoshioka-jones-and-christian-sheerer_2025-08-06/WHO_extraction.yaml`

---

## Execution Time

**Target:** 2-3 minutes per transcript
**Breakdown:**
- Load strategic lens: 30 sec
- Read transcript & extract signals: 60-90 sec
- Match personas & calculate fit: 30 sec
- Generate YAML output: 30 sec

**Total:** 2.5-3 min average

---

## Quality Checklist

Before marking WHO extraction complete, verify:

- [ ] strategic_lens.yaml v1.1 loaded successfully
- [ ] Transcript has frontmatter (document_type, date, participants)
- [ ] All personas matched to lens.who.target_personas
- [ ] Strategic_fit scores calculated with logic shown
- [ ] Ivan constraints checked (margins, accounting team, transaction type, AR/AP)
- [ ] Anti-personas validated (8 types checked)
- [ ] All evidence has line-level citations
- [ ] UNKNOWN fields flagged (not fabricated)
- [ ] context_lineage.unique_value explains why this source matters
- [ ] quality_validation section completed
- [ ] Contract compliance validated (no fabrication, no vague citations)

---

**Version:** 1.0
**Status:** READY FOR EXECUTION
**Pattern:** Parallel Fanout-Fanin (Fanout Layer)
**Next Agent:** WHO_extraction.yaml → Node_Synthesizer (Agent 2)
**Contract:** [ORCHESTRATION_ARCHITECTURE.md:Agent 1a → Agent 2 Contract]
