---
node_type: business_model
status: baseline
confidence: 6.4
created: 2025-10-30
last_updated: 2025-10-30
sources:
  - 08 29 25 - GTM Build Update 25e508663b7481b5b2c1d0667e859c1d.md
  - ICP Summary & Use Cases 7085d388732a44caaa41db763f531999.md
  - strategic_lens.yaml v1.2
tags: [foundation, business-model, metrics, lir, tpv, cc-adoption, ar-percentage]
validation_status: awaiting_transcript_validation
transcript_validations: 0
---

# Key Business Metrics

**Status:** Baseline (from raw_context, awaiting transcript validation)
**Confidence:** 6.4/10
**Sources:** 3 raw_context documents

## Leading Indicator of Retention (LIR)

[VERIFIED: ICP Summary.md:45-46, strategic_lens.yaml:1144-1148]

**Definition:** Customer receives **50% of monthly receivables** on Nickel's platform

**Significance:**
- North star metric for customer success
- Determines customer stickiness and long-term value
- Used to validate ICP fit (cohorts exceeding LIR = good ICP)
- Evangelist stage criteria (ready for upsell/referral)

**Strategic Implication:**
[VERIFIED: ICP Summary.md:45-47] "ICP is always a moving target... we will continue to update, change, add/remove ICPs based on customer cohorts that exceed our LIR"

**Priority:** 1 (Highest)
**Strategic Fit Weight:** 10/10

---

## August 2025 Performance Metrics

[VERIFIED: 08 29 25 GTM Build Update.md:49-62]

### Total Payment Volume (TPV)

**Overall TPV:** $35.2M (just short of July's $36M record)
**Core TPV (without CJ Brothers):** $26.2M (+4.98% MoM growth)

**Interpretation:**
- Overall TPV dip due to single large customer (CJ Brothers)
- Core business growing steadily (+4.98%)
- August acknowledged as slower month seasonally

### AR Product Performance

**AR as % of Total TPV:**
- Overall: 36.7%
- Core customers: 49.3% (nearly half)

**Strategic Significance:**
- AR customers have higher strategic fit (10/10 vs 5/10 for AP)
- Core customers nearly at 50% AR mix
- AR product leadership established

[VERIFIED: 08 29 25 GTM Build Update.md:56-57] "AR Leadership: Overall AR now represents 36.7% of total TPV, while core customers hit 49.3%"

### Credit Card Adoption

**CC as % of Total TPV:**
- Overall: 13.6%
- Core customers: 18.2% (growing)

**Strategic Significance:**
- Nickel's revenue depends on CC transaction fees
- Core customers adopt CC at higher rate (18.2% vs 13.6%)
- Growing trend validates revenue model

[VERIFIED: 08 29 25 GTM Build Update.md:58] "Credit Card Momentum: Overall adoption at 13.6%, but core customers usage keeps increasing at 18.2%"

### Transaction Growth

**AR Transactions:**
- Overall: +16.92% growth
- Core customers: +16.11% growth

**AP Transactions:**
- Overall: +0.64% growth (slowed)
- Core customers: +1.40% growth

**Interpretation:**
[VERIFIED: 08 29 25 GTM Build Update.md:60-61] AP transaction growth slowed, which is "in line with what we know about AP activation" - September focus needed on AP flow improvements

### Deals Closed

[VERIFIED: 08 29 25 GTM Build Update.md implied, strategic_lens.yaml:1165]

**August 2025:** 27 deals closed
**Company Revenue Represented:** $86M across 27 accounts

**Average Deal Size:** $3.18M per account (calculated: $86M / 27)

---

## Conversion Benchmarks (Needs Validation)

[VERIFIED: strategic_lens.yaml:1150-1158]

**Unknown Metrics (Awaiting Transcript Validation):**
- Demo Scheduled → Demo Attended conversion rate
- Demo Attended → Trial Started conversion rate
- Trial Started → Customer conversion rate

**Baseline Win Probability Estimates:**
[VERIFIED: Funnel Stages.md:52-59]
- Demo Scheduled: 25% win rate
- Demo Attended: 50% win rate
- Trial Invitation Sent: 75% win rate
- Trial Started: 80% win rate

---

## Context Lineage

**Source Documents:**
- `knowledge_base/raw_context/08 29 25 - GTM Build Update.md` (lines 49-62)
  - Unique value: August 2025 actual performance data (TPV, AR%, CC%, transaction growth, deals closed)

- `knowledge_base/raw_context/ICP Summary & Use Cases.md` (lines 45-47)
  - Unique value: LIR definition (50% receivables), ICP validation methodology

- `knowledge_base/raw_context/strategic_lens.yaml` (lines 1144-1166)
  - Unique value: Metric definitions, strategic significance, conversion funnel benchmarks

**Dimensional Mapping:**
- Meta dimension: Business performance metrics → [strategic_lens.yaml:1143-1166]
- WHO dimension: Core customers vs overall (segmentation impact on metrics)
- WHY dimension: Revenue model validation (CC adoption %, AR %)

---

## Transcript Validation

**Validation signals:**
- [ ] LIR achievement: What % of transcript customers hit 50% receivables threshold?
- [ ] TPV patterns: Average deal sizes by persona (Payment Upgraders vs Cash-Savvy vs Full Stack)
- [ ] AR vs AP distribution: Does 49.3% AR hold across transcript sample?
- [ ] CC adoption drivers: Why do some customers use CC while others don't?
- [ ] Conversion rate validation: Actual Demo→Trial→Customer rates from transcript journey stages

**Expected evolution:**
- Conversion benchmarks will be refined with actual pipeline data
- LIR thresholds may adjust based on cohort analysis
- Metrics may be segmented by persona or vertical for more granular insights
- New leading indicators may emerge from transcript pattern analysis
