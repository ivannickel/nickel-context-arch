---
node_type: business_model
status: baseline
confidence: 6.8
created: 2025-10-30
last_updated: 2025-10-30
sources:
  - strategic_lens.yaml v1.2
  - 08 29 25 - GTM Build Update 25e508663b7481b5b2c1d0667e859c1d.md
tags: [foundation, business-model, revenue-model, cc-transaction-fees, ar-vs-ap]
validation_status: awaiting_transcript_validation
transcript_validations: 0
---

# Revenue Model

**Status:** Baseline (from raw_context, awaiting transcript validation)
**Confidence:** 6.8/10
**Sources:** 2 raw_context documents

## Core Revenue Source

[VERIFIED: strategic_lens.yaml:538-540] **Primary Revenue:** Credit card transaction fees

**Revenue Model Implications:**
- Nickel must generate credit card transaction volume to be profitable
- Free tier economics depend on customers using credit cards for some payments
- Business model constraint drives ICP qualification logic

## AR vs. AP Customer Economics

[VERIFIED: strategic_lens.yaml:541-548]

### AR Customers (Accounts Receivable)

**Fit:** STRONG
**Revenue Potential:** High
**Strategic Fit Weight:** 10/10

**Why:**
- Customers (payers) **naturally choose their payment method**
- Payment method mix: some customers pay by credit card + some pay by ACH
- **High revenue probability:** Some customers will choose to pay by CC
- Supplier has less control over payment method, creating natural CC adoption

### AP Customers (Accounts Payable)

**Fit:** BINARY
**Revenue Potential:** High if CC, zero if ACH-only
**Strategic Fit Weight:** 5/10

**Why:**
- Supplier (payer) **chooses payment method** for all bills
- **Binary outcome:**
  - **All CC payments = Good** (generates transaction revenue)
  - **All ACH payments = No current revenue** (free ACH, $0 fees)
- Supplier incentivized to use free ACH (saves money, but Nickel earns nothing)

[VERIFIED: strategic_lens.yaml:549] **"CRITICAL business model constraint - must generate CC transaction revenue"**

## Business Model Validation Metrics

[VERIFIED: 08 29 25 GTM Build Update.md:57-58] **August 2025 Performance:**

**Credit Card Adoption Rates:**
- Overall: 13.6% of TPV via credit card
- Core customers: 18.2% of TPV via credit card (↑ growing)

**AR Leadership:**
- Overall: 36.7% of TPV is AR
- Core customers: 49.3% of TPV is AR (nearly half)

**Interpretation:**
[INFERRED: combining revenue model + metrics]
- AR product driving higher CC adoption (18.2% vs 13.6%)
- Core customers (higher LIR) have higher AR mix (49.3%)
- AR customers more valuable due to natural CC payment mix

## Strategic Constraints from Revenue Model

**ICP Qualification Impact:**
[VERIFIED: strategic_lens.yaml:538-549]

1. **AR customers prioritized** over AP customers (10/10 vs 5/10 fit)
2. **ACH-only AP customers = NOT IDEAL** (can onboard, but $0 current revenue)
3. **Payment method mix is critical qualification signal**

**Pricing Implications:**
- Free tier sustainable if customers adopt CC for some transactions
- High AR adoption = higher revenue per customer
- Low CC adoption = unprofitable customer (even if high TPV)

## Context Lineage

**Source Documents:**
- `knowledge_base/raw_context/strategic_lens.yaml` (lines 537-549)
  - Unique value: Ivan's explicit revenue model constraints, AR vs AP economics, strategic fit weights

- `knowledge_base/raw_context/08 29 25 - GTM Build Update.md` (lines 56-58)
  - Unique value: Actual CC adoption rates (13.6% overall, 18.2% core), AR percentage (36.7% overall, 49.3% core)

**Dimensional Mapping:**
- WHO dimension: ICP prioritization (AR > AP) based on revenue potential
- WHY dimension: Business model constraints drive customer fit logic
- Meta dimension: Key metrics track revenue model health (CC adoption %, AR %)

## Transcript Validation

**Validation signals:**
- [ ] AR vs AP customer split: What % of transcripts are AR-focused vs AP-focused?
- [ ] Payment method preferences: Do AR customers mention CC acceptance? Do AP customers prefer ACH?
- [ ] Free tier sustainability questions: Do customers ask "how is this free?"
- [ ] CC adoption barriers: What objections arise to credit card payments?
- [ ] Revenue realization: Can we correlate transcript patterns with actual CC adoption rates?

**Expected evolution:**
- Revenue model may expand beyond CC fees (e.g., net terms lending revenue)
- AR vs AP economics may shift if product launches AP revenue features
- CC adoption benchmarks may be refined based on customer segment patterns
- Free tier positioning may adjust based on customer understanding/skepticism
