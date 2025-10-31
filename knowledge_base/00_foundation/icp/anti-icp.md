---
node_type: icp_definition
status: baseline
confidence: 6.5
created: 2025-10-30
last_updated: 2025-10-30
sources:
  - strategic_lens.yaml v1.2
  - ICP Summary & Use Cases 7085d388732a44caaa41db763f531999.md
tags: [foundation, icp, anti-persona, disqualification-criteria]
validation_status: awaiting_transcript_validation
transcript_validations: 0
---

# Anti-ICP Profiles

**Status:** Baseline (from raw_context, awaiting transcript validation)
**Confidence:** 6.5/10
**Sources:** 2 raw_context documents

## Overview

Nickel's anti-ICP profiles identify business types that should be disqualified from sales pursuit, even if inbound. These are based on fundamental business model misalignments, product capability gaps, or economic incompatibility with Nickel's revenue model.

[VERIFIED: strategic_lens.yaml:578-627] Anti-personas were refined in Ivan's strategic lens v1.2 with explicit disqualification criteria and strategic fit weights.

## Critical Disqualifiers (Immediate Rejection)

### 1. High-Margin Professional Services

[VERIFIED: strategic_lens.yaml:579-585]

**Reason:** 100% margins on time - 3% CC fee is negligible, not a pain point

**Disqualify:** YES
**Strategic Fit Weight:** 0/10

**Examples:**
- Consulting firms
- Coaching services
- Freelance professionals with small transactions

**Why:** Nickel's value proposition centers on saving money for businesses with tight margins (<30%). High-margin service businesses don't experience payment processing fees as a significant pain point relative to their gross profit.

[VERIFIED: strategic_lens.yaml:583] Ivan explicitly stated: "CRITICAL: Tight margins are ICP requirement"

---

### 2. E-commerce / Shopping Cart Businesses

[VERIFIED: strategic_lens.yaml:587-592]

**Reason:** Need shopping cart experience, not sales-led invoicing

**Disqualify:** YES
**Strategic Fit Weight:** 0/10

**Why:** Nickel's product is designed for invoice-based, negotiated B2B transactions. E-commerce businesses require:
- Real-time payment flows integrated with checkout
- High-volume, low-value transactions
- Automated pricing (not negotiated quotes)
- Shopping cart integrations

Fundamental product-market mismatch.

---

### 3. Large Accounting Teams (ERP-Dependent)

[VERIFIED: strategic_lens.yaml:594-600]

**Reason:** Need ERP integrations that Nickel doesn't provide

**Disqualify:** YES
**Strategic Fit Weight:** 1/10

**Examples:**
- Companies with 10+ accounting staff
- Businesses with complex ERP systems (NetSuite, SAP, Oracle)

**Why:** These businesses have sophisticated accounting workflows and require deep ERP integrations beyond QuickBooks Online. Nickel's current product capabilities cannot support their complexity.

[VERIFIED: strategic_lens.yaml:518] Accounting team sweet spot is **<10 staff**. Companies with larger teams signal ERP dependency.

---

### 4. Retail Stores

[VERIFIED: strategic_lens.yaml:609-612]

**Reason:** Consumer-facing, not B2B

**Disqualify:** YES
**Strategic Fit Weight:** 0/10

**Why:** Nickel is a B2B payment platform. Retail stores serve end consumers, not businesses.

---

### 5. Software Companies

[VERIFIED: strategic_lens.yaml:614-617]

**Reason:** Not physical goods or project-based

**Disqualify:** YES
**Strategic Fit Weight:** 0/10

**Why:** Software/SaaS businesses typically have:
- Subscription revenue models
- Automated billing
- No net terms or trade credit needs
- Different payment infrastructure requirements (Stripe, recurring billing)

---

### 6. Healthcare Providers

[VERIFIED: strategic_lens.yaml:619-622]

**Reason:** Regulatory complexity, not ICP

**Disqualify:** YES
**Strategic Fit Weight:** 0/10

**Why:** Healthcare has unique regulatory requirements (HIPAA, insurance billing) and payment workflows that Nickel is not designed to handle.

---

### 7. Restaurants

[VERIFIED: strategic_lens.yaml:624-627]

**Reason:** Consumer-facing, low transaction value

**Disqualify:** YES
**Strategic Fit Weight:** 0/10

**Why:** Consumer-facing with low-value, high-volume POS transactions. Not B2B invoice-based.

---

## Partial Disqualifier (Not Ideal, But Not Anti-Persona)

### ACH-Only AP Customers

[VERIFIED: strategic_lens.yaml:602-607]

**Reason:** Want to pay all bills via free ACH - no CC transaction revenue for Nickel

**Disqualify:** NO (but deprioritize)
**Strategic Fit Weight:** 2/10

**Why:** Nickel's revenue model depends on credit card transaction fees. AP customers who pay all bills via ACH generate **zero current revenue**.

**Nuanced Position:**
- NOT a hard anti-persona (can still onboard)
- NOT IDEAL for current business model
- Future product upsell potential exists
- These vendors might become AR customers (two-sided marketplace hypothesis)

[VERIFIED: strategic_lens.yaml:607] "NOT anti-persona but NOT IDEAL - future product upsell potential, pay vendors who could be customers"

---

## Common Anti-ICP Patterns

**Consumer-Facing Businesses:**
- Disqualify if end customer is individual consumer, not business

**High-Volume, Low-Value Transactions:**
- Disqualify if average transaction <$500 and transactional (not project-based)

**Shopping Cart / E-commerce Model:**
- Disqualify if sales process is automated checkout, not negotiated quotes/invoices

**High-Margin Services (>50%):**
- Disqualify if gross margins are high enough that payment processing fees are negligible

**Complex Enterprise Systems:**
- Disqualify if current accounting setup requires ERP integrations beyond QuickBooks Online

---

## Context Lineage

**Source Documents:**
- `knowledge_base/raw_context/strategic_lens.yaml` (lines 578-627)
  - Unique value: Ivan's explicit anti-persona definitions with disqualification reasoning, strategic fit weights, and business model alignment

- `knowledge_base/raw_context/ICP Summary & Use Cases.md` (implicit anti-patterns from ICP definition)
  - Unique value: Positive ICP criteria that implies anti-patterns (B2B vs. B2C, invoice-based vs. shopping cart)

**Dimensional Mapping:**
- WHO dimension: Anti-persona exclusion criteria → [strategic_lens.yaml:578-627]
- WHY dimension: Business model constraints that create misalignment → [strategic_lens.yaml:537-549]
- Strategic fit scoring: Anti-personas receive 0-2/10 scores, removing them from sales pipeline

---

## Transcript Validation

**Validation signals:** (will be added as transcripts process)
- [ ] **Anti-persona frequency:** How often do disqualified profiles appear in inbound leads?
- [ ] **Conversion rate validation:** Do any anti-personas convert despite disqualification?
- [ ] **Churn patterns:** If anti-personas slip through, do they churn faster?
- [ ] **Revenue validation:** Do ACH-only AP customers generate zero revenue as hypothesized?
- [ ] **Refinement signals:** Are there edge cases that should be added to anti-ICP list?

**Status progression:**
- baseline → validating (after 1st transcript confirms anti-persona rejection logic)
- validating → validated (after 2nd+ transcripts show clear anti-ICP patterns)
- validated → canonical (after 5th+ transcripts quantify cost of mis-qualified anti-personas)

**Expected evolution:**
- Anti-ICP list may expand as new misalignment patterns emerge
- ACH-only AP positioning may shift if product launches AP revenue features
- Strategic fit weights may be refined based on actual churn and LTV data
- Edge case criteria may be added for nuanced scenarios (e.g., hybrid B2B/B2C)
