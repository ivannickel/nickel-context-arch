# Transcript Frontmatter Schema (Extension)

**Version:** 1.0
**Created:** 2025-10-30
**Purpose:** Extend existing Circleback frontmatter with strategic classification for dimensional extraction

---

## Schema Definition

**IMPORTANT:** Transcripts already have Circleback-generated frontmatter. DO NOT duplicate these fields:
- `title`, `date`, `time`, `duration_sec`, `duration_min`, `participants`, `source`, `meeting_number`

**ADD these strategic classification fields BELOW existing frontmatter:**

```yaml
# === STRATEGIC CLASSIFICATION (ADD BELOW EXISTING) ===

# Call Classification
call_type: "discovery | demo | kickoff | review | follow_up | general"
deal_stage: "discovery | evaluation | activation | active | expansion | churned"
customer_segment: "shrimp | fish | whale | unknown"

# Strategic Signals (Boolean flags for extraction priority)
has_pain_points: true | false
has_objections: true | false
has_competitive_intel: true | false
has_use_case: true | false
has_pricing_discussion: true | false
has_integration_needs: true | false

# Customer Context
primary_industry: "construction | accounting | professional_services | manufacturing | hospitality | property_management | other"
transaction_volume: "sub_threshold | near_threshold | above_threshold | unknown"  # $2M AP spend threshold
ar_vs_ap: "ap_only | ar_only | both | unclear"

# Processing Status
processed: false
dimensional_extracted: false
extraction_priority: "high | medium | low"
---
```

---

## Field Definitions

### Call Classification

**call_type** (Primary call purpose):
- **discovery**: Initial exploratory call, qualification, needs assessment
- **demo**: Product demonstration, feature walkthrough
- **kickoff**: First activation/onboarding call after signup
- **review**: Follow-up/progress review for existing customers
- **follow_up**: Continuing conversation from previous call
- **general**: Unclear or mixed purpose

**deal_stage** (Pipeline position):
- **discovery**: First contact, qualification phase
- **evaluation**: Actively considering solution (demos, trials)
- **activation**: Signed up, onboarding in progress
- **active**: Live customer using product
- **expansion**: Discussing additional features/volume
- **churned**: Lost or inactive customer

**customer_segment** (ICP classification):
- **shrimp**: Low volume, simple needs (< $500K AP spend)
- **fish**: Mid-market, growing needs ($500K-$2M AP spend)
- **whale**: High volume, complex needs (> $2M AP spend)
- **unknown**: Insufficient information

### Strategic Signals

**has_pain_points**: Customer expresses problems, challenges, frustrations
- Keywords: "pain", "problem", "challenge", "struggling", "difficult", "frustrated", "issue"

**has_objections**: Customer raises concerns, blockers, hesitations
- Keywords: "concern", "worried", "expensive", "complicated", "not sure", "already using", "don't need"

**has_competitive_intel**: Mentions competitors or alternatives
- Keywords: "Relay", "Melio", "Bill.com", "PayPal", "Zelle", "Venmo", "competitor", "currently using", "switching from"

**has_use_case**: Describes specific workflows or use cases
- Keywords: "workflow", "process", "how we do", "currently we", "use case", "scenario"

**has_pricing_discussion**: Discusses costs, rates, discounts, ROI
- Keywords: "$", "cost", "price", "rate", "discount", "savings", "expensive", "2.9%", "fee"

**has_integration_needs**: Mentions integration requirements
- Keywords: "QuickBooks", "integration", "connect", "sync", "API", "Xero", "NetSuite"

### Customer Context

**primary_industry**: Customer's primary business vertical
- **construction**: General contracting, renovation, roofing, HVAC
- **accounting**: Accounting firms, bookkeeping services, CFO services
- **professional_services**: Consulting, agencies, B2B services
- **manufacturing**: Production, distribution, wholesale
- **hospitality**: Restaurants, entertainment, events
- **property_management**: HOAs, property management, real estate
- **other**: Doesn't fit above categories

**transaction_volume**: Relative to $2M AP spend threshold
- **sub_threshold**: Clear they are below $2M annual AP spend
- **near_threshold**: $800K-$2M range, could qualify for discounts
- **above_threshold**: $2M+ AP spend, discount-eligible
- **unknown**: Volume not discussed

**ar_vs_ap**: Payment flow direction
- **ap_only**: Only interested in paying vendors (accounts payable)
- **ar_only**: Only interested in collecting from customers (accounts receivable)
- **both**: Interested in both AP and AR
- **unclear**: Not explicitly discussed

### Processing Status

**processed**: Has basic extraction been completed?
**dimensional_extracted**: Has 6-dimensional extraction been performed?
**extraction_priority**: Strategic priority for dimensional extraction
- **high**: Discovery calls with competitive intel OR objections OR pricing discussion
- **medium**: Demos, kickoff calls, or calls with use cases
- **low**: General follow-ups, low-signal conversations

---

## Classification Logic (Agent Instructions)

### 1. Call Type (Filename + Content Analysis)

**Filename pattern matching:**
```
if "kickoff" in filename → call_type = "kickoff"
if "review" in filename → call_type = "review"
if "follow-up" in filename → call_type = "follow_up"
if "demo" in filename → call_type = "demo"
if "and-colton" or "and-jacob" in filename → call_type = "discovery"
else → call_type = "general"
```

**Content validation:** Read first 100 lines to confirm

### 2. Deal Stage (Inferred from call_type + content)

**Heuristic mapping:**
```
call_type = "discovery" → deal_stage = "discovery"
call_type = "demo" → deal_stage = "evaluation"
call_type = "kickoff" → deal_stage = "activation"
call_type = "review" → deal_stage = "active"
```

**Override if content shows:** Customer says "we're already using", "we've been live for X weeks" → deal_stage = "active"

### 3. Strategic Signals (Keyword Scan)

Scan first 200 lines of transcript for keywords:

**has_pain_points:**
- Positive: "pain", "problem", "challenge", "struggling", "difficult", "frustrated", "issue", "headache", "manual"

**has_objections:**
- Positive: "concern", "worried", "expensive", "complicated", "not sure", "hesitant", "already using", "don't need", "skeptical"

**has_competitive_intel:**
- Positive: "Relay", "Melio", "Bill.com", "PayPal", "Zelle", "Venmo", "competitor", "currently using", "switching from", "compared to"

**has_use_case:**
- Positive: "workflow", "process", "how we do", "currently we", "use case", "scenario", "here's what", "we need to"

**has_pricing_discussion:**
- Positive: "$", "cost", "price", "rate", "discount", "savings", "expensive", "2.9", "fee", "cheaper", "volume discount"

**has_integration_needs:**
- Positive: "QuickBooks", "integration", "connect", "sync", "API", "Xero", "NetSuite", "integrate with", "connected to"

### 4. Customer Context (Content Analysis)

**primary_industry:** Scan for company type, business description, vertical mentions

**transaction_volume:** Look for dollar amounts, "we process $X", "annual spend", "volume"
- If mentions < $500K → sub_threshold
- If mentions $800K-$2M → near_threshold
- If mentions > $2M → above_threshold

**ar_vs_ap:** Look for "accounts payable", "paying vendors", "invoicing customers", "accounts receivable"

### 5. Extraction Priority (Calculated)

**High priority:**
- (call_type = "discovery") AND (has_competitive_intel OR has_objections OR has_pricing_discussion)
- (transaction_volume = "above_threshold")
- (customer_segment = "whale")

**Medium priority:**
- (call_type IN ["demo", "kickoff"]) AND has_use_case
- (has_pain_points = true)
- (customer_segment = "fish")

**Low priority:**
- (call_type = "follow_up" OR "general")
- (has_pain_points = false AND has_objections = false)
- (customer_segment = "shrimp" OR "unknown")

---

## Example: Fully Classified Transcript

**File:** `002_erik-meza-and-colton-ofarrell_2025-07-15.md`

```yaml
---
# === EXISTING CIRCLEBACK FRONTMATTER ===
title: Erik Meza and Colton O'Farrell
date: '2025-07-15'
time: '15:00:37'
duration_sec: 1562.87
duration_min: 26.0
participants:
- Colton O'Farrell <colton@getnickel.com>
- Erik Meza <erik@nlt-llc.com>
source: Circleback
meeting_number: 2

# === STRATEGIC CLASSIFICATION (NEW) ===
call_type: discovery
deal_stage: discovery
customer_segment: fish

has_pain_points: false
has_objections: true
has_competitive_intel: false
has_use_case: true
has_pricing_discussion: true
has_integration_needs: true

primary_industry: other
transaction_volume: sub_threshold
ar_vs_ap: both

processed: false
dimensional_extracted: false
extraction_priority: high
---
```

**Rationale:**
- `call_type: discovery` - Initial call with Colton, exploring fit
- `has_objections: true` - Customer mentions AR customers unlikely to pay by card
- `has_pricing_discussion: true` - Heavy focus on volume discount, 2.9% to 2.8%
- `has_integration_needs: true` - Discusses QuickBooks integration
- `has_use_case: true` - Describes AP workflow, Fortune 500 payment terms
- `transaction_volume: sub_threshold` - $800K annual AP spend (below $2M threshold)
- `ar_vs_ap: both` - Discusses both AP and potential AR usage
- `extraction_priority: high` - Discovery call with objections + pricing discussion

---

## Token Efficiency Notes

**For Agent Processing:**
- Read only **first 200 lines** of transcript for classification (saves 50-70% tokens)
- Use keyword matching, not semantic analysis (faster, cheaper)
- Batch process 5-10 transcripts per agent call (amortize instruction overhead)
- Skip reading if filename makes classification obvious (e.g., "kickoff-call")

**Expected Processing Time:**
- Per transcript: 10-15 seconds
- Per batch (10 transcripts): 90-120 seconds
- Full corpus (165 transcripts): ~20-25 minutes with 17 parallel agents

---

## Success Criteria

**Quality Gate:**
- `call_type` accuracy ≥ 95% (validated against filename)
- `extraction_priority` distribution: ~20% high, ~50% medium, ~30% low
- Strategic signal flags: At least 1 true flag for ≥70% of transcripts

**Validation Method:**
- Human spot-check 10 random transcripts (5 min)
- Automated check: Ensure no transcripts have all signals = false

---

**Last Updated:** 2025-10-30
**Status:** Ready for agent processing
**Next Step:** Create batch orchestration plan
