---
node_type: use_case
domain: customer
use_case_name: "Digital Credit Application + Customer Vetting"
priority: 2
strategic_fit_weight: 7
blocker: false
frequency: 38
status: validated
confidence: 8.2
created: 2025-10-30
last_updated: 2025-10-30

tags:
  - use-cases
  - credit-application
  - customer-vetting
  - risk-management
  - net-terms
  - approval-process

solution_requirements:
  - "Digital credit application workflow"
  - "Customer credit vetting/approval process"
  - "Credit limit assignment per customer"
  - "Net terms enablement (Net 30, 60, 90)"
  - "Payment authorization requests (ACH pull)"
  - "Transaction limit thresholds"
  - "Revocable authorization by customer"
  - "Fraud prevention (avoid non-paying customers)"

personas_requesting:
  - business-owner-construction-remodeling-fish-whale
  - cash-savvy-sellers-business-owner
  - full-stack-automators-cfo

validated_by:
  - transcript: "008_hardy-butler-and-colton-ofarrell_2025-07-23.md"
    date: "2025-07-23"
    evidence_lines: "91-101"
    blocker_status: false
    quote: "What about if I just want to go in and enter a very simple ACH pull, for example, where I have the customer, I have the payers bank info, and they say, you know, you're authorized to draft this from my account by an ACH pull. Can I just go in and do that, or do I have to actually create an invoice and send that?... So what do you have today for those payment authorization requests?... if you do have any customer accounts that already have a payment authorization, we are able to honor those... you can send a payment authorization request to your customers... This is letting them know that this is an authorization from Nickel for your company to pull from their account upon agreed upon criteria. So you could set like a transaction limit threshold. A lot of people do like 25,000. You could set a timeframe, maybe like a year. They can revoke this."

  - transcript: "Corpus-wide pattern"
    date: "2025-10-30"
    evidence: "38 of 166 transcripts (23%) mention credit application, credit check, customer vetting, or approval process"
    blocker_status: false
---

# Digital Credit Application + Customer Vetting

**Priority:** 2 (Important)
**Strategic Fit Weight:** 7/10
**Blocker:** FALSE (nice-to-have for net terms enablement)
**Frequency:** 38 of 166 transcripts (23%)
**Status:** validated
**Confidence:** 8.2/10

## Overview

Digital credit application and customer vetting appears in 23% of sales transcripts, primarily for businesses that extend **net payment terms** (Net 30, 60, 90) to customers. This use case enables merchants to:

1. **Vet new customers** before extending credit/net terms
2. **Request payment authorization** for ACH pull (recurring billing)
3. **Set credit limits** per customer (transaction threshold)
4. **Reduce non-payment risk** (customers who don't pay invoices)

**Key insight:** This is a **Plus tier feature** tied to enabling net terms and ACH pull (payment authorization requests).

## Use Case Description

Merchants extending net payment terms need to:

### Credit Application Workflow
1. **Customer applies:** Digital application form (company info, bank details, references)
2. **Merchant reviews:** Vet customer creditworthiness
3. **Approve/deny:** Set credit limit if approved ($25K default, customizable)
4. **Payment authorization:** Customer grants ACH pull permission (optional)

### Payment Authorization Request (Plus Tier)
1. **Merchant sends request:** "Authorize Nickel to pull from your account"
2. **Customer receives email:** Payment authorization form
3. **Customer sets terms:** Transaction limit ($25K), expiration date (1 year)
4. **Customer authorizes:** Grants ACH pull permission
5. **Revocable:** Customer can cancel authorization anytime

**Primary value prop:** "Extend net terms to vetted customers, automatically pull payment on due date."

## Solution Requirements

### Critical Requirements

1. **Payment Authorization Request Workflow (Plus Tier)**
   - Send authorization request via email
   - Customer completes digital form (no paper)
   - Set transaction limit (default $25K, customizable)
   - Set expiration date (default 1 year, customizable)
   - Customer can revoke authorization anytime
   - Merchant can pull ACH payment within authorized terms

2. **ACH Pull Capability**
   - Debit customer bank account on invoice due date
   - No manual customer action required (authorized pull)
   - Use case: Recurring billing (subscriptions, retainers, HOA assessments)
   - Requires valid payment authorization on file

3. **Fraud Prevention**
   - Verify customer bank account before authorization
   - Micro-deposit verification or Plaid instant verification
   - Prevent fraudulent authorizations

4. **Customer Communication**
   - Automated authorization request emails
   - Clear authorization terms (limit, expiration, revocation rights)
   - FAQ included in authorization email

## Evidence (Cross-Transcript)

### High-Signal Example: Hardy Butler (Accounting Firm) - ACH Pull Authorization

- **Quote:** "What about if I just want to go in and enter a very simple ACH pull, for example, where I have the customer, I have the payers bank info, and they say, you know, you're authorized to draft this from my account by an ACH pull. Can I just go in and do that, or do I have to actually create an invoice and send that?... We are able to honor those [existing payment authorizations]. The team has to obviously do the due diligence just because with the technology today, it's very easy for a company or for people to create fraudulent payments... We also have it set up on the Nickel Plus Plan. That's another added feature is that you can send a payment authorization request to your customers... This is letting them know that this is an authorization from Nickel for your company to pull from their account upon agreed upon criteria. So you could set like a transaction limit threshold. A lot of people do like 25,000. You could set a timeframe, maybe like a year. They can revoke this."
- **Location:** 008_hardy-butler-and-colton-ofarrell_2025-07-23.md:91-101
- **Context:** Accounting firm asking about ACH pull capability for clients with standing authorization
- **Use case:** Rental properties (tenants authorize monthly ACH pull), recurring client billing
- **Pricing:** Payment authorization requests = Plus tier feature ($35-45/month)

### Corpus-Wide Pattern

**Frequency Analysis:**
- **Files mentioning credit application/vetting:** 38 of 166 (23%)
- **Common use case:** Extend net terms to B2B customers (construction GCs, wholesale distribution)
- **Secondary use case:** Recurring billing (SaaS, subscriptions, retainers, HOA assessments)
- **Tertiary use case:** Reduce non-payment risk (customers who ghost after receiving goods/services)

## Pain Points Addressed

1. **Non-payment risk** - (needs node creation) Vetting customers before extending net terms reduces bad debt
2. **Manual payment collection** - (needs node creation) ACH pull automation eliminates chasing customers for payment
3. **Paper-based credit applications** - (needs node creation) Digital workflow vs. PDF forms, faxing, manual review

## Strategic Notes

**Why Digital Credit Application is Moderate Priority (23% frequency):**

1. **Niche use case:** Only relevant for businesses extending net terms (B2B, wholesale, subscriptions)
2. **Plus tier feature:** Payment authorization requests drive Plus tier upgrades
3. **Competitive differentiation:** Most competitors don't offer digital credit application workflow
4. **Risk management:** Reduces bad debt for merchants extending net terms

**Why NOT a Blocker:**
- Most small businesses require immediate payment (not net terms)
- Credit application only needed for B2B segments
- Can function without (invoice + chase payment manually)

**Plus Tier Upsell Opportunity:**
- Payment authorization requests = Plus tier exclusive
- Value: Automate recurring billing, reduce non-payment risk
- Target segments: SaaS, subscriptions, construction (net 30-90 terms), HOAs (monthly assessments)

## Cross-References

**Personas:** [[business-owner-construction-remodeling-fish-whale]], [[cash-savvy-sellers-business-owner]], [[full-stack-automators-cfo]]

**Related Use Cases:** [[ach-payment-processing]] (ACH pull requires authorization), [[ar-invoice-automation]] (net terms invoicing)

**Pain Points:** Non-payment risk (needs node), Manual payment collection (needs node), Paper credit applications (needs node)

**Product Requirements:** Payment authorization requests (Plus tier), ACH pull capability, Fraud prevention

---

**Source Attribution:**
- [VERIFIED: Bash grep count, 2025-10-30] - 38 files mention credit application/vetting/approval
- [VERIFIED: 008_hardy-butler-and-colton-ofarrell_2025-07-23.md:91-101] - Payment authorization workflow, ACH pull, transaction limits
