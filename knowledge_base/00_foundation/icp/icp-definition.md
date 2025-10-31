---
node_type: icp_definition
status: baseline
confidence: 6.2
created: 2025-10-30
last_updated: 2025-10-30
sources:
  - ICP Summary & Use Cases 7085d388732a44caaa41db763f531999.md
  - Classification Prompts 271508663b748051a9aff7653337f5a6.md
  - strategic_lens.yaml v1.2
tags: [foundation, icp, firmographic-criteria, revenue-qualification]
validation_status: awaiting_transcript_validation
transcript_validations: 0
---

# ICP Definition

**Status:** Baseline (from raw_context, awaiting transcript validation)
**Confidence:** 6.2/10
**Sources:** 3 raw_context documents

## Overview

Nickel's Ideal Customer Profile (ICP) is defined by a multi-tier qualification system (Shrimp/Fish/Whale/Kraken) based on revenue bands, combined with firmographic and industry criteria. The north star metric is the **Leading Indicator of Retention (LIR)**: customers who process **50% of their monthly receivables on Nickel**.

[VERIFIED: ICP Summary.md:45-46] The ICP is explicitly defined as "a moving target for an early stage startup" with continuous updates based on customer cohorts that exceed the LIR threshold.

## Revenue Qualification System

[VERIFIED: Classification Prompts.md:64-69] Nickel uses a four-tier revenue qualification system:

**Revenue Tiers:**
- **Shrimp:** <$1M annual revenue
- **Fish:** $1M-$5M annual revenue
- **Whale:** $5M-$25M annual revenue
- **Kraken:** ≥$25M annual revenue

**Priority Tier Mapping:**
[VERIFIED: Classification Prompts.md:88-91]
- **Tier 1 (Highest Priority):** Any ICP industry company OR non-ICP Whale/Kraken
- **Tier 2 (Medium Priority):** Non-ICP Fish
- **Tier 3 (Low Priority):** Non-ICP Shrimp

## Firmographic Criteria

**Company Size:**
[VERIFIED: ICP Summary.md:55-60]
- **Payment Upgraders & Cash-Savvy Sellers:** Under $50M revenue OR 100 employees, 1-5 locations
- **Full Stack Automators:** Under $250M revenue OR 500 employees, dozens of locations

[VERIFIED: strategic_lens.yaml:514-520] **Critical constraint from Ivan:**
- **Employee Count Sweet Spot:** 2-100 employees (accounting teams <10 staff)
- **Reasoning:** Large accounting teams (10+ staff) need ERP integrations Nickel doesn't provide
- **Key Signal:** "Small headcount moving large money" is a critical fit indicator

**Margin Profile:**
[VERIFIED: strategic_lens.yaml:522-528] **Ivan's critical ICP refinement:**
- **Ideal:** Low margins (<30%) + large transactions
- **Reasoning:** 3% credit card fee has 5-10x impact on low-margin businesses
- **Example:** "$80K cost, $100K sale, $20K margin → $2.4K fee = 12% of margin"
- **Anti-fit:** High-margin services (100% margins on time) where 3% fee is negligible

**Transaction Profile:**
[VERIFIED: strategic_lens.yaml:530-535]
- **Ideal:** Large, negotiated B2B transactions ($5K+ average)
- **Transaction Type:** Sales-led, invoice-based (NOT shopping cart)
- **Anti-fit:** E-commerce, high-volume low-value transactions

**Business Model Constraints:**
[VERIFIED: strategic_lens.yaml:537-549] **Revenue dependency critical for qualification:**
- **AR Customers:** STRONG fit - customers naturally choose payment method (mix of CC + ACH), high revenue potential
- **AP Customers:** BINARY fit - either all CC (good) or all ACH (no current revenue)
- **Strategic Fit Weights:** AR = 10/10, AP = 5/10
- **Note:** Nickel's revenue model depends on credit card transaction fees, making payment method mix critical

## Industry Verticals

[VERIFIED: ICP Summary.md:56-59] **Primary target across all tiers:**
- **Building Materials** (Pre-built, specialty, custom: windows, doors, lighting, millwork, kitchen & bath fixtures)

[VERIFIED: strategic_lens.yaml:456-487] **Secondary high-fit industries:**
- **Construction & Trades:** General contractors, electrical, plumbing, HVAC, roofing, concrete, masonry, carpentry
- **Manufacturing:** Metal fabrication, building products, custom manufacturing, wood products
- **Wholesale & Distribution:** Building materials, electrical supplies, plumbing supplies, HVAC equipment, industrial supplies
- **Transportation & Logistics:** Trucking & freight, specialized transport, warehousing
- **Large-Ticket B2B Services:** Equipment rental, heavy equipment services, event services

**Construction Project Types:**
[VERIFIED: ICP Summary.md:62]
- **Payment Upgraders/Cash-Savvy:** Single family, multi-family, small commercial
- **Full Stack Automators:** All non-industrial projects

## Context Lineage

**Source Documents:**
- `knowledge_base/raw_context/ICP Summary & Use Cases.md` (lines 41-116)
  - Unique value: Three-tier persona framework, firmographic criteria, LIR definition, real customer examples

- `knowledge_base/raw_context/Classification Prompts.md` (lines 32-138)
  - Unique value: Revenue tier definitions, priority tier mapping, ICP keyword signals, qualification logic

- `knowledge_base/strategic_lens.yaml` (lines 456-607)
  - Unique value: Ivan's critical refinements (margin profile, headcount constraints, transaction type, business model constraints)

**Dimensional Mapping:**
- WHO dimension: Core persona definitions → [strategic_lens.yaml:409-608]
- Strategic fit weight calculation: Revenue tier × Industry match × Margin profile × Transaction type
- Meta dimension: Market segmentation → [strategic_lens.yaml:1102-1125]

## Transcript Validation

**Validation signals:** (will be added as transcripts process)
- [ ] **Frequency count:** How many transcripts match ICP criteria vs. non-ICP
- [ ] **Persona validation:** Which of the 3 ICP tiers appear most frequently
- [ ] **Revenue tier distribution:** Actual Shrimp/Fish/Whale/Kraken split
- [ ] **Margin profile confirmation:** Do low-margin customers (<30%) exhibit higher fit?
- [ ] **Transaction size validation:** Average transaction values for high-fit customers
- [ ] **Contradictions:** If transcript evidence refutes any baseline ICP criteria

**Status progression:**
- baseline → validating (after 1st transcript matches ICP criteria)
- validating → validated (after 2nd+ transcript revalidations)
- validated → canonical (after 5th+ transcript revalidations with quantified patterns)

**Expected evolution:**
- Revenue tier sweet spot may shift based on LIR achievement rates
- Industry vertical priorities may adjust based on conversion and retention data
- Margin profile threshold may be refined with quantified examples
- Employee count constraints may be validated or adjusted
