---
node_type: use_case
domain: customer
use_case_name: "Embeddable Customer Payment Portal"
priority: 2
strategic_fit_weight: 8
blocker: false
frequency: 103
status: canonical
confidence: 9.3
created: 2025-10-30
last_updated: 2025-10-30

tags:
  - use-cases
  - payment-portal
  - customer-experience
  - self-service
  - website-integration

solution_requirements:
  - "Embeddable payment portal link"
  - "Customizable branding (logo, banner, colors)"
  - "No customer account creation required"
  - "Payment methods: ACH + Credit Card"
  - "One-stop shop for customer payments"
  - "Backup payment method (if primary fails)"
  - "Custom domain (Plus tier only)"
  - "Mobile-responsive design"

personas_requesting:
  - business-owner-construction-remodeling-fish-whale
  - cash-savvy-sellers-business-owner
  - hoa-operations-manager-property-management-whale
  - full-stack-automators-cfo

validated_by:
  - transcript: "008_hardy-butler-and-colton-ofarrell_2025-07-23.md"
    date: "2025-07-23"
    evidence_lines: "74, 118"
    blocker_status: false
    quote: "this customer payment portal that a lot of our customers really enjoy, they'll typically take that and embed it in their own website. They're able to customize it however they like... This serves as typically a one-stop shop for customers to make a payment or as a backup method if the primary method is not working. But this is completely customizable even on the free plan... a lot of our customers embed this in their own website."

  - transcript: "Corpus-wide pattern"
    date: "2025-10-30"
    evidence: "103 of 166 transcripts (62%) mention payment portal or customer payment page"
    blocker_status: false
---

# Embeddable Customer Payment Portal

**Priority:** 2 (Important)
**Strategic Fit Weight:** 8/10
**Blocker:** FALSE (nice-to-have, not required)
**Frequency:** 103 of 166 transcripts (62%)
**Status:** canonical
**Confidence:** 9.3/10

## Overview

An **embeddable customer payment portal** appears in 62% of sales transcripts. This self-service portal allows merchants to embed a Nickel payment page directly on their website, enabling customers to make payments without receiving individual invoice links.

**Primary use cases:**
1. **Website integration:** Embed "Make a Payment" link on company website
2. **Backup payment method:** If invoice email lost, customer can visit portal
3. **Self-service payments:** Customers initiate payments without merchant sending invoice
4. **Professional brand experience:** Customizable portal with merchant logo/branding

**Key differentiator:** Available on **Core (free) tier** (customizable branding), **Plus tier** adds custom domain.

## Use Case Description

Customers want to provide their customers/clients with a self-service payment portal that:

1. **Embeds on website:** "Make a Payment" button → Nickel payment portal
2. **No account creation:** Customer enters invoice # or amount, pays immediately
3. **Payment options:** ACH (free) or Credit Card (2.99% fee shown)
4. **Customizable branding:** Merchant logo, banner image, brand colors
5. **Mobile-responsive:** Works on phone, tablet, desktop
6. **One-stop shop:** Single link for all payment needs (vs. per-invoice links)

**Example workflow:**
- Website visitor clicks "Make a Payment"
- Portal loads with merchant branding
- Customer enters invoice # or payment amount
- Selects ACH (free) or Credit Card (2.99% fee)
- Payment processed, confirmation email sent

## Solution Requirements

### Critical Requirements

1. **Embeddable Link**
   - Unique portal URL per merchant: `nickelpayments.com/merchant-name`
   - Embeddable in website (direct link or iframe)
   - Shareable link (email signature, social media)

2. **Customizable Branding (Core Tier)**
   - Upload merchant logo
   - Upload banner image
   - Customize colors (optional)
   - All customization available on free Core tier

3. **Custom Domain (Plus Tier)**
   - `payments.merchantdomain.com` (vs. `nickelpayments.com/merchant`)
   - Requires DNS configuration (CNAME record)
   - Professional appearance, trust signal

4. **No Customer Account Creation**
   - Frictionless payment (no signup required)
   - Customer enters invoice # or amount
   - Immediate payment processing

5. **Payment Method Options**
   - ACH: Free (default)
   - Credit Card: 2.99% fee (clearly marked)
   - Fee allocation follows global surcharge rules

6. **Mobile-Responsive Design**
   - Works on phone, tablet, desktop
   - Optimized for mobile payment entry

## Evidence (Cross-Transcript)

### High-Signal Example: Hardy Butler (Accounting Firm) - Portal as Embedded Feature

- **Quote:** "So like I mentioned, we give all companies access to their own like payment portal or merchant link... This serves as typically a one-stop shop for customers to make a payment or as a backup method if the primary method is not working. But this is completely customizable even on the free plan. So you just go into the settings, you could adjust the banner, you know, information there. The only thing we can't do on the free plan is give you a custom URL or domain that's only available on Plus. But if you want that, we're happy to build that out for you. But what this would look like is just like so this will be a lot of our customers embed this in their own website."
- **Location:** 008_hardy-butler-and-colton-ofarrell_2025-07-23.md:118
- **Context:** Demo of payment portal feature, emphasizing embeddability and customization on free tier
- **Use cases:** One-stop shop + backup payment method
- **Pricing:** Customization free (Core), custom domain requires Plus tier

### Corpus-Wide Pattern

**Frequency Analysis:**
- **Files mentioning payment portal:** 103 of 166 (62%)
- **Common use case:** Embed "Make a Payment" on website
- **Secondary use case:** Backup if invoice email lost
- **Tertiary use case:** Self-service for recurring customers (HOAs, subscriptions)

## Pain Points Addressed

1. **Customer payment friction** - (needs node creation) Self-service portal reduces "I lost the invoice email" support tickets
2. **Website integration complexity** - (needs node creation) Embeddable link (no API integration required)
3. **Brand consistency** - (needs node creation) Customizable portal maintains merchant brand experience

## Strategic Notes

**Why Payment Portal is Valuable (62% frequency):**

1. **Reduces support burden:** "I lost the invoice" → "Visit our payment portal"
2. **Professional appearance:** Branded portal > generic payment page
3. **Website integration:** "Make a Payment" button on website footer/header
4. **Backup payment method:** If invoice email lost, portal is fallback

**Why NOT a Blocker:**
- Merchants can function with invoice-only payments (no portal required)
- Portal is enhancement to primary invoice workflow
- Optional feature for merchants with high payment volume

**Plus Tier Upsell Opportunity:**
- Custom domain (`payments.merchantdomain.com`) = professional trust signal
- Value: $35-45/month for custom domain + faster ACH + higher limits

## Cross-References

**Personas:** [[business-owner-construction-remodeling-fish-whale]], [[cash-savvy-sellers-business-owner]], [[hoa-operations-manager-property-management-whale]]

**Related Use Cases:** [[ar-invoice-automation]], [[ach-payment-processing]], [[credit-card-processing]]

**Pain Points:** Customer payment friction (needs node), Website integration complexity (needs node)

**Product Requirements:** Embeddable portal, Customizable branding (Core), Custom domain (Plus)

---

**Source Attribution:**
- [VERIFIED: Bash grep count, 2025-10-30] - 103 files mention payment portal
- [VERIFIED: 008_hardy-butler-and-colton-ofarrell_2025-07-23.md:118] - Portal demo, embeddability, Core vs Plus features
