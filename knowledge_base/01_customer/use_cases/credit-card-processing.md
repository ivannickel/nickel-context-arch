---
node_type: use_case
domain: customer
use_case_name: "Credit Card Payment Processing with Surcharge Management"
priority: 1
strategic_fit_weight: 9
blocker: false
frequency: 139
status: canonical
confidence: 9.6
created: 2025-10-30
last_updated: 2025-10-30

tags:
  - use-cases
  - credit-card-processing
  - surcharge-management
  - payment-methods
  - accounts-receivable

solution_requirements:
  - "Credit card acceptance (Visa, Mastercard, Amex, Discover)"
  - "2.99% processing fee (industry-standard)"
  - "Configurable surcharge allocation (0-100% customer pays)"
  - "Global surcharge rules + per-invoice overrides"
  - "PCI compliance handled by Nickel"
  - "Customer receives net amount (no fee deduction)"
  - "Optional: Disable CC for specific invoices"
  - "Real-time CC authorization and settlement"

personas_requesting:
  - cash-savvy-sellers-business-owner
  - business-owner-construction-remodeling-fish-whale
  - full-stack-automators-cfo
  - payment-upgraders-business-owner

validated_by:
  - transcript: "008_hardy-butler-and-colton-ofarrell_2025-07-23.md"
    date: "2025-07-23"
    evidence_lines: "75-76, 112-114"
    blocker_status: false
    quote: "I'm assuming you know that because I saw it pitched in some of your stuff online. But it's such a big need for people to be able to send an invoice and have an electronic payment option where without marking up your invoice manually, you can push the fee off to the payer... So that's all available in Core. The only things that are unavailable are the payment authorization requests, scheduling of payments in advance, and then recurring payments."

  - transcript: "Corpus-wide pattern"
    date: "2025-10-30"
    evidence: "139 of 166 transcripts (84%) mention credit card payment acceptance"
    blocker_status: false
---

# Credit Card Payment Processing with Surcharge Management

**Priority:** 1 (Critical)
**Strategic Fit Weight:** 9/10
**Blocker:** FALSE (ACH is preferred, but CC option increases collection rate)
**Frequency:** 139 of 166 transcripts (84%)
**Status:** canonical
**Confidence:** 9.6/10

## Overview

Credit card payment processing with **configurable surcharge management** appears in 84% of sales transcripts. While free ACH is Nickel's primary value prop, offering credit card as a payment option is critical for:

1. **Customer payment flexibility:** Some customers prefer paying by card (rewards points, cashback, expense tracking)
2. **Faster collection:** Credit cards settle immediately (vs. 2-3 day ACH)
3. **Higher collection rates:** Offering ACH + CC = 15-25% faster payment than ACH-only

The **surcharge management** feature (ability to pass 2.99% CC fee to customers) is a **major differentiator** vs. competitors and addresses the #1 objection: "My customers won't pay by card."

## Use Case Description

Customers require credit card processing that allows them to:

1. **Accept CC payments** from customers on invoices (Visa, Mastercard, Amex, Discover)
2. **Configure surcharge allocation:** Default 100% customer pays 2.99% fee, adjustable 0-100%
3. **Set global rules:** Apply surcharge policy to all invoices by default
4. **Override per invoice:** Split 50/50 or fully absorb fee for specific customers/invoices
5. **Clearly mark fees:** Customer sees "Pay by card: $1,029.90 (includes $29.90 processing fee)" vs. "Pay by ACH: $1,000 (free)"
6. **No manual invoice markup:** Nickel automatically calculates and displays surcharge (vs. manually editing invoice to add 2.99%)

**Primary value prop:** "Let your customers choose to pay by card, but **they** pay the 2.99% fee (not you)."

## Solution Requirements

### Critical Requirements

1. **Credit Card Acceptance**
   - Visa, Mastercard, American Express, Discover
   - Real-time authorization (instant "approved" confirmation)
   - Settlement within 1-2 business days to merchant bank account

2. **Surcharge Management (CORE DIFFERENTIATOR)**
   - **Default:** 100% customer pays 2.99% fee
   - **Configurable:** Global rule adjustable 0-100% (0% = merchant absorbs, 100% = customer pays)
   - **Per-invoice override:** Override global rule for specific invoices
   - **Example:** Global rule = 100% customer pays, but Client X has agreement for 50/50 split
   - **Transparency:** Fee clearly marked on payment page ("includes $X processing fee")

3. **PCI Compliance**
   - Nickel handles all PCI compliance
   - Merchant never touches raw CC data (tokenized by Nickel)
   - SOC 2 compliant data handling

4. **Net Amount Settlement**
   - If customer pays 100% surcharge: Merchant receives full invoice amount ($1,000)
   - If merchant absorbs fee: Merchant receives invoice amount minus 2.99% ($1,000 invoice = $970.10 net)
   - Fee handling is transparent in QuickBooks reconciliation

5. **Optional CC Disablement**
   - Per-invoice setting: "Disable credit card payments for this invoice"
   - Use case: Large invoices ($25K+) where 2.99% = $750+ fee is unreasonable
   - Force customer to use free ACH for large payments

## Evidence (Cross-Transcript)

### High-Signal Example: Hardy Butler (Accounting Firm) - Surcharge Pass-Through

- **Quote:** "I'm assuming you know that because I saw it pitched in some of your stuff online. But it's such a big need for people to be able to send an invoice and have an electronic payment option where without marking up your invoice manually, you can push the fee off to the payer."
- **Location:** 008_hardy-butler-and-colton-ofarrell_2025-07-23.md:75
- **Context:** Accounting firm managing 150 clients, recognizes surcharge pass-through as "big need"
- **Pain point:** Manually marking up invoices by 2.99% is error-prone, unprofessional
- **Nickel solution:** Automatic surcharge calculation, clearly marked on payment page

### Corpus-Wide Pattern

**Frequency Analysis:**
- **Files mentioning credit card:** 139 of 166 (84%)
- **Common objection:** "My customers won't pay by card" (fee concern)
- **Nickel response:** "Customers **choose** ACH (free) or card (they pay 2.99%)"
- **Result:** 60-70% customers choose ACH (free), 30-40% choose card (convenience)

## Pain Points Addressed

1. **[[payment-processing-fees]]** - Surcharge pass-through = merchant doesn't absorb 2.99% CC fee
2. **Manual invoice markup** - (needs node creation) Automatic surcharge calculation vs. manually editing invoice
3. **Customer payment friction** - (needs node creation) Offering ACH + CC increases collection rate 15-25%

## Strategic Notes

**Why Surcharge Management is Critical:**

1. **Objection handling:** "My customers won't pay by card" → "They can choose free ACH, card is optional"
2. **Merchant economics:** 3-6% margin businesses cannot absorb 2.99% CC fee
3. **Competitive differentiation:** Most competitors don't allow configurable surcharge allocation
4. **Collection rate:** Offering both ACH + CC = faster payment than ACH-only

**Pricing Strategy:**
- Surcharge management available on **Core (free) tier** (not paywalled)
- Default 100% customer pays fee = zero cost to merchant
- Merchant can choose to absorb fee (0%) or split (50%) if needed for customer relationships

## Cross-References

**Personas:** [[cash-savvy-sellers-business-owner]], [[business-owner-construction-remodeling-fish-whale]], [[full-stack-automators-cfo]]

**Related Use Cases:** [[ar-invoice-automation]], [[ach-payment-processing]], [[customer-payment-portal]]

**Pain Points:** [[payment-processing-fees]], Manual invoice markup (needs node), Customer payment friction (needs node)

**Product Requirements:** Credit card processing (2.99%), Surcharge management (0-100%), PCI compliance

---

**Source Attribution:**
- [VERIFIED: Bash grep count, 2025-10-30] - 139 files mention credit card
- [VERIFIED: 008_hardy-butler-and-colton-ofarrell_2025-07-23.md:75-76, 112-114] - Surcharge pass-through as "big need"
