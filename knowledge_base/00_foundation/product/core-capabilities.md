---
node_type: product_capability
status: baseline
confidence: 6.2
created: 2025-10-30
last_updated: 2025-10-30
sources:
  - ICP Summary & Use Cases 7085d388732a44caaa41db763f531999.md
  - strategic_lens.yaml v1.2
tags: [foundation, product, capabilities, ar-automation, payment-processing, credit-extension]
validation_status: awaiting_transcript_validation
transcript_validations: 0
---

# Core Product Capabilities

**Status:** Baseline (from raw_context, awaiting transcript validation)
**Confidence:** 6.2/10
**Sources:** 2 raw_context documents

## Product Capability Stack

[VERIFIED: strategic_lens.yaml:319-327]

### 1. AR Automation

**Priority:** 1
**Strategic Fit Weight:** 10/10

**Capabilities:**
- Automated invoice sending
- Payment reminders
- Reconciliation
- Applicable to all 3 ICP tiers

[VERIFIED: strategic_lens.yaml:977-983]

---

### 2. Payment Processing (ACH + Credit Card)

**Priority:** 1
**Strategic Fit Weight:** 9/10

**Payment Methods:**
[VERIFIED: strategic_lens.yaml:297-305]
- **Free ACH payments** (zero-fee bank transfers)
- **Credit card processing** (18.2% of core customers use)
- **Apple Pay** (live to top customers as of Aug 2025)
- **International payments** (coming soon)

[VERIFIED: 08 29 25 GTM Build Update.md:39] Apple Pay launched to top customers

---

### 3. Credit Application & Underwriting

**Priority:** 2
**Strategic Fit Weight:** 8/10
**ICP Fit:** Full Stack Automators primarily

**Capabilities:**
- Digital credit application
- Automated underwriting
- Scalable credit decisioning
- No manual credit department needed

[VERIFIED: ICP Summary.md:77-78, strategic_lens.yaml:730-736]

---

### 4. Net Terms Extension (30-90 days)

**Priority:** 1
**Strategic Fit Weight:** 10/10
**ICP Fit:** Cash-Savvy Sellers, Full Stack Automators

[VERIFIED: strategic_lens.yaml:307-315, 986-991]

**Mechanism:**
- Supplier extends 30-90 day terms to customers
- Supplier gets paid immediately (Nickel fronts capital)
- Nickel underwrites credit risk
- Customer pays Nickel on net terms schedule

---

### 5. Lien Management Automation

**Priority:** 2
**Strategic Fit Weight:** 8/10
**ICP Fit:** Full Stack Automators

[VERIFIED: ICP Summary.md:79, strategic_lens.yaml:738-744]

**Capabilities:**
- Automate lien filing
- Track lien deadlines
- Maintain compliance
- Protect payment rights on construction projects

**Context:**
[VERIFIED: ICP Summary.md:70] Current state: Most companies only maintain lien rights on 20-30% of projects (manual bottleneck)

---

### 6. Collections Automation

**Priority:** 2
**Strategic Fit Weight:** 8/10

[VERIFIED: strategic_lens.yaml:325]

**Capabilities:**
- Automated payment reminders
- Dunning workflows
- Late payment follow-up
- Reduce manual collections effort

---

## Product Roadmap Signals

[VERIFIED: 08 29 25 GTM Build Update.md:39]

**Recently Launched:**
- **Apple Pay:** Live to top customers (Aug 2025)

**Coming Soon:**
- **International Payments:** Roadmap item for Kraken tier customers

**Needs Validation from Transcripts:**
- W-9/1099 automation (Iteration 1 mention)
- Multi-client dashboard (accounting firm use case)
- Volume discount tiers
- White-label capabilities

---

## Capability Gaps (Hypothesis)

[INFERRED: anti-ICP + strategic constraints]

**Current Limitations:**
- No ERP integrations beyond QuickBooks Online (SAP, NetSuite, Oracle not supported)
- No shopping cart integrations (e-commerce use cases not supported)
- No consumer payment flows (B2B only)

---

## Context Lineage

**Source Documents:**
- `knowledge_base/raw_context/ICP Summary & Use Cases.md` (lines 72-79)
  - Unique value: Solutions needed per ICP tier, current state pain points

- `knowledge_base/raw_context/strategic_lens.yaml` (lines 297-327, 730-744, 977-991)
  - Unique value: Capability definitions, strategic fit weights, ICP fit mapping

---

## Transcript Validation

**Validation signals:**
- [ ] Feature frequency: Which capabilities are mentioned most in transcripts?
- [ ] Feature priorities: Do customers care more about AR automation, net terms, or lien management?
- [ ] Capability gaps: What features are customers asking for that don't exist?
- [ ] Competitive parity: Do Melio/Bill.com have similar capabilities (table stakes)?
- [ ] Persona variation: Do Payment Upgraders care about different features than Full Stack Automators?

**Expected evolution:**
- Capability priorities may shift based on customer demand patterns
- New capabilities may emerge from transcript feature requests
- Product gaps may be identified and prioritized
- Roadmap may be informed by validated customer needs
