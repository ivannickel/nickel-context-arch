---
title: Use Cases - Overview
description: Summary of top 6 use cases identified from customer transcript analysis
domain: customer
node_type: index
status: validated
last_updated: 2025-10-24
transcripts_analyzed: 4
total_use_cases: 6
---

# Nickel Use Cases - Top 6 from Transcript Analysis

This directory contains detailed use case documents derived from analysis of 4 customer discovery transcripts:
1. **Erik Meza (NLT LLC)** - 2025-07-15 - Volume discount inquiry, AP/AR expansion
2. **Carson Crawford (Lake Carolina HOA)** - 2025-08-14 - Large HOA recurring billing
3. **Hardy Butler (Accounting Firm)** - 2025-07-23 - Multi-client enablement, low-volume ACH
4. **Jeff Streich (Prime Renovations NYC)** - 2025-07-23 - High-value contractor payments

## Use Cases by Adoption Frequency

### HIGH Frequency (3-4 out of 4 transcripts)

#### 1. QuickBooks Integration
**File:** `quickbooks-integration.md`
**Adoption:** 4 out of 4 transcripts (100%)
**Summary:** Seamless QuickBooks Online integration for automated payment processing and real-time sync

**Key indicators:**
- Erik: Office manager handles QB, integration status unclear
- Carson: Asked about QB requirement, confirmed optional
- Hardy: Uses QB Online Accountant for 150 clients, needs selective sync
- Jeff: Setting up Procore-QB flow, abandoned QB Pay for better solution

**Plan fit:** Core or Plus, depending on volume and features needed
**Revenue impact:** Enables adoption, reduces friction, drives retention

---

#### 2. High-Volume AP Processing
**File:** `high-volume-ap-processing.md`
**Adoption:** 3 out of 4 transcripts (75%)
**Summary:** Processing large quantities or high-dollar AP transactions with ACH and wire transfers, eliminating checks and bank fees

**Key indicators:**
- Erik: $500-800K annual credit card AP + $50-100K monthly ACH
- Hardy: Enabling clients with AP needs, avoiding $7 bank fees
- Jeff: $300K average payments to subcontractors, $3M annual volume scaling to $10M

**Plan fit:** Core for under $25K/transaction, Plus for $25K-$1M transactions
**Revenue impact:** Plus plan driver ($35-45/month), high engagement

---

#### 3. AR Invoice Automation
**File:** `ar-invoice-automation.md`
**Adoption:** 2 out of 4 transcripts (50%, plus implicit in others)
**Summary:** Automated invoice delivery and payment collection with email/SMS, payment portal, and credit card surcharge management

**Key indicators:**
- Erik: 100% ACH currently, untapped AR expansion opportunity
- Carson: 2,500 homeowners, $3M annual AR volume, replacing expensive ZAGO
- Jeff: Primarily wire transfers, occasional credit card requests
- Hardy: Implicit for firm invoicing

**Plan fit:** Core for basic invoicing, Plus for recurring billing and custom portal
**Revenue impact:** Increases platform stickiness, credit card processing fees (2.99%)

---

### MEDIUM Frequency (1-2 out of 4 transcripts)

#### 4. Large-Scale Recurring Billing
**File:** `large-scale-recurring-billing.md`
**Adoption:** 1 out of 4 transcripts (25%, but applicable to HOAs, subscriptions, memberships)
**Summary:** Automated recurring payment collection for HOAs, property management, subscriptions, and membership organizations at scale

**Key indicators:**
- Carson: 2,500 homeowners, annual $1,150-1,260 assessment, flexible payment plan needs
- Current pain: ZAGO charges $3.95 per ACH, 4% credit card
- Desired: Weekly, monthly, or annual payment flexibility for homeowners

**Plan fit:** Plus plan required ($35-45/month) for recurring billing
**Revenue impact:** Plus plan driver, high-volume transactions, strong retention (annual contracts)

---

#### 5. Multi-Entity Payment Management
**File:** `multi-entity-payment-management.md`
**Adoption:** 2 out of 4 transcripts (50%)
**Summary:** Managing payments across multiple legal entities (LLCs, properties, subsidiaries) with separate accounting and banking requirements

**Key indicators:**
- Hardy: CPA firm (150 client entities) + rental properties (3-4 entities)
- Jeff: Uses Relay's multi-account structure for project-based organization
- Need: Separate accounts per entity with centralized access

**Plan fit:** Mix of Core and Plus depending on entity volume
**Revenue impact:** Multiple account subscriptions, accounting firm channel opportunity

---

#### 6. Low-Volume ACH for Small Clients
**File:** `low-volume-ach-for-small-clients.md`
**Adoption:** 1 out of 4 transcripts (25%, but addresses widespread small business need)
**Summary:** Enabling occasional ACH payments for small businesses without expensive platform fees or per-transaction charges

**Key indicators:**
- Hardy: "I want to be able to send ACH payments in low volume... without paying an absurd monthly platform fee"
- Current pain: Banks charge $7 per ACH, Bill.com $45-60/month too expensive
- Desired: Zero-cost ACH for 1-10 payments per month

**Plan fit:** Core (free) - perfect fit, gateway to Plus upgrades
**Revenue impact:** User acquisition driver, upsell to Plus as clients grow, word-of-mouth growth

---

## Use Case Prioritization Framework

### Tier 1: Platform Adoption Drivers (Must-Have)
1. **QuickBooks Integration** - Reduces friction, enables automation, drives retention
2. **High-Volume AP Processing** - Core value prop, Plus plan revenue driver
3. **AR Invoice Automation** - Expands TAM, credit card processing revenue

### Tier 2: Revenue Accelerators (Nice-to-Have)
4. **Large-Scale Recurring Billing** - High-value contracts, strong retention, niche dominance (HOAs)
5. **Multi-Entity Payment Management** - Multiple subscriptions per customer, accounting firm channel

### Tier 3: Acquisition Magnets (Growth Levers)
6. **Low-Volume ACH for Small Clients** - Mass market appeal, word-of-mouth, upsell funnel

---

## Key Insights Across Use Cases

### Common Pain Points
1. **Expensive per-transaction fees** (banks, ZAGO, traditional processors)
2. **Slow ACH processing** (3-5 days with banks and QB Pay)
3. **Platform fees too high for low volume** (Bill.com, enterprise solutions)
4. **Check fraud risk** driving electronic payment adoption
5. **Complex integration workflows** (Procore-QB-payment processor)

### Common Objections
1. **Sustainability of free tier** (Melio burned users)
2. **QuickBooks integration concerns** (forced dependency, integration quality)
3. **Feature gaps** (W-9/1099, selective sync, multi-entity dashboard)
4. **Credit card surcharge adoption** (will customers pay the fee?)
5. **Complexity** (too many tools, learning curve)

### Plan Fit Patterns
- **Core (Free) for:**
  - Low-volume clients (under 30 payments/month)
  - Transactions under $25K
  - Basic invoice sending without recurring billing
  - Gateway users who may upgrade

- **Plus ($35-45/month) for:**
  - High-volume clients (30+ payments/month or $100K+/month)
  - Transactions over $25K (up to $1M)
  - Recurring billing needs
  - Faster ACH processing (same-day to 2-day)
  - Custom payment portal URL
  - 4+ active users

### Revenue Model Implications
- **Subscription revenue:** Plus plan upgrades as customers scale
- **Transaction revenue:** 2.99% credit card processing on AR
- **Freemium funnel:** Free Core drives adoption, Plus captures value
- **Network effects:** Accounting firms as channel (150+ clients per firm)

---

## Use Case Coverage by Customer Segment

### Small Businesses ($100K-$1M revenue)
- Low-Volume ACH for Small Clients
- QuickBooks Integration
- AR Invoice Automation (basic)

### Mid-Market ($1M-$10M revenue)
- High-Volume AP Processing
- AR Invoice Automation (advanced)
- QuickBooks Integration
- Multi-Entity Payment Management

### Accounting Firms / Bookkeepers
- Low-Volume ACH for Small Clients (client enablement)
- Multi-Entity Payment Management (150+ client entities)
- QuickBooks Integration (firm-wide standardization)

### Industry-Specific
- **HOAs / Property Management:** Large-Scale Recurring Billing
- **General Contractors:** High-Volume AP Processing, Multi-Entity (project-based)
- **Real Estate Investors:** Multi-Entity Payment Management (per-property LLCs)

---

## Competitive Landscape by Use Case

### Nickel vs. Bill.com
- **Nickel wins:** Low-volume ACH, simple workflows, lower pricing, better UX for small businesses
- **Bill.com wins:** High-volume enterprise, complex approvals, international payments, check printing

### Nickel vs. QuickBooks Pay
- **Nickel wins:** Faster ACH, lower fees, better surcharge control, superior UX
- **QB Pay wins:** Native to QB (no integration), familiarity, check printing

### Nickel vs. Relay Financial
- **Nickel wins:** Unlimited free ACH, lower pricing, QB integration, AR capabilities
- **Relay wins:** Multi-account banking structure, $5 wires, banking features (cards, checking)

### Nickel vs. Banks (Chase, BofA, TD Bank)
- **Nickel wins:** Zero ACH fees, better UX, QB integration, faster processing
- **Banks win:** Wire capability, existing relationship, in-person support

---

## Feature Gaps Identified

### High Priority (Blocking deals or reducing adoption)
1. **Selective QuickBooks sync** - Cannot pilot with subset of QB customers (accounting firms)
2. **Multi-entity dashboard** - Cannot view all entities in single pane (real estate, accounting firms)
3. **Wire transfers** - No wire capability (lost to Relay Financial for urgent payments)
4. **W-9/1099 functionality** - Cannot collect W-9s or generate 1099s (accounting firm need)

### Medium Priority (Reducing feature parity)
5. **Payment authorization on free plan** - Only Plus plan (limits low-volume recurring use)
6. **Sub-account structure** - Cannot create project accounts under parent (contractors)
7. **Check printing/mailing** - No check option (vs Bill.com, QB Pay)
8. **International payments** - US-only (vs Bill.com, Stripe)

### Low Priority (Nice-to-have)
9. **Multi-level approval workflows** - Simple approval only (vs Bill.com)
10. **Budget controls** - No spend limits or budget tracking (vs Bill.com)

---

## Next Steps for Sales Enablement

### For Account Executives
1. **Use case qualification:** Ask discovery questions to map prospect to use case(s)
2. **Objection handling:** Reference use case docs for common objections + responses
3. **Proof points:** Share customer stories from transcripts (Erik, Carson, Hardy, Jeff)
4. **Competitive positioning:** Know when to compete vs. complement (e.g., Relay + Nickel)

### For Product Team
1. **Roadmap alignment:** Prioritize features blocking high-frequency use cases
2. **Feature gaps:** Address selective sync, multi-entity dashboard, W-9/1099
3. **Use case optimization:** Enhance workflows for top 3 use cases

### For Marketing
1. **Positioning:** Lead with QuickBooks integration and free ACH value prop
2. **Segmentation:** Create campaigns per use case (HOAs, accounting firms, contractors)
3. **Content:** Develop use case guides, customer stories, ROI calculators

---

## Document Index

| Use Case | File | Frequency | Plan Fit | Revenue Impact |
|----------|------|-----------|----------|----------------|
| QuickBooks Integration | `quickbooks-integration.md` | HIGH (4/4) | Core/Plus | Enabler |
| High-Volume AP Processing | `high-volume-ap-processing.md` | HIGH (3/4) | Plus | High |
| AR Invoice Automation | `ar-invoice-automation.md` | HIGH (2/4) | Core/Plus | High |
| Large-Scale Recurring Billing | `large-scale-recurring-billing.md` | MEDIUM (1/4) | Plus | High |
| Multi-Entity Payment Management | `multi-entity-payment-management.md` | MEDIUM (2/4) | Core/Plus | Medium |
| Low-Volume ACH for Small Clients | `low-volume-ach-for-small-clients.md` | MEDIUM (1/4) | Core | Low/User Acq |

---

## Transcript Coverage Map

| Use Case | Erik | Carson | Hardy | Jeff |
|----------|------|--------|-------|------|
| QuickBooks Integration | X | X | X | X |
| High-Volume AP Processing | X | | X | X |
| AR Invoice Automation | X | X | (Implicit) | (Implicit) |
| Large-Scale Recurring Billing | | X | | |
| Multi-Entity Payment Management | | | X | X |
| Low-Volume ACH for Small Clients | | | X | |

**Key:**
- X = Explicit discussion in transcript
- (Implicit) = Implicit or passive mention

---

## Revision History

- **2025-10-24:** Initial creation based on 4 transcript analysis
- **Source transcripts:**
  - `2025-07-15_erik-meza-colton.md`
  - `2025-08-14_carson-crawford-lake-carolina.md`
  - `2025-07-23_hardy-butler-accounting-firm.md`
  - `2025-07-23_prime-renovations-jeff-streich.md`
