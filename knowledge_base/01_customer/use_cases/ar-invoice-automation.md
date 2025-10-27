---
name: ar-invoice-automation
title: Accounts Receivable Invoice Automation
description: Automated invoice delivery and payment collection with email/SMS, payment portal, and credit card surcharge management
domain: customer
node_type: use_case
status: validated
last_updated: 2025-10-24
frequency: high
transcripts_referenced:
  - 2025-07-15_erik-meza-colton
  - 2025-08-14_carson-crawford-lake-carolina
adoption_rate: "2 out of 4 transcripts (plus passive mention in others)"
tags:
  - accounts-receivable
  - invoice-automation
  - payment-collection
  - credit-card-surcharge
  - cash-flow
related_docs:
  - "[[invoice-automation-adoption]]"
  - "[[payment-portal-setup]]"
  - "[[surcharge-management]]"
---

# Use Case: Accounts Receivable Invoice Automation

## Summary
Businesses sending invoices to customers need automated delivery (email/SMS), easy payment options (ACH/credit card), and the ability to pass credit card fees to customers without violating surcharge laws.

## Description
AR invoice automation addresses the full invoice-to-cash cycle:
1. **Invoice creation:** Manual in Nickel or auto-sync from QuickBooks
2. **Invoice delivery:** Automated email/SMS with payment link
3. **Payment options:** Zero-fee ACH or credit card (with surcharge)
4. **Payment collection:** Branded payment portal, embedded website links
5. **Reconciliation:** Auto-post payments to QuickBooks in real-time

This use case is particularly powerful for businesses with:
- **High invoice volume:** 20+ invoices per month
- **Customer payment friction:** Slow-paying customers, check collection challenges
- **Credit card fee burden:** Absorbing 2.9% credit card fees eating margins
- **Manual processes:** Emailing invoices, tracking payments manually, chasing customers

## Fit Assessment

### Excellent Fit Indicators
- **Invoice volume:** 20+ invoices per month
- **Customer base:** B2B or B2C with digital-savvy customers
- **Payment methods:** Customers pay by ACH, check, or credit card
- **QuickBooks users:** Want automated sync from QB to Nickel
- **Cash flow sensitivity:** Need faster payment collection
- **Margin protection:** Want to pass credit card fees to customers
- **Multi-channel delivery:** Need email, SMS, and web portal options

### Moderate Fit Indicators
- **Invoice volume:** 10-20 invoices per month
- **Some manual preference:** Want review before sending invoices
- **Mixed customer base:** Some customers tech-savvy, others prefer traditional methods
- **Credit card usage:** 10-30% of customers pay by card

### Poor Fit Indicators
- **Very low volume:** Less than 10 invoices per month
- **B2B enterprise customers:** Fortune 500 who demand net-30/60 terms and refuse credit card fees
- **Check-only customers:** Customer base unwilling to adopt electronic payments
- **Complex invoicing:** Need multi-page complex invoices with line-item detail (Nickel invoicing is simple)

## Indicators from Transcripts

### Erik Meza (NLT LLC)
**Quote:** "All the customers, they pay ACH, every single one of them. So we typically give... Are you offering any kind of option to pay via credit card? I it's very rare, to be honest with you. Very, very rare."
- **Current state:** 100% ACH, no credit card option offered
- **Customer type:** Fortune 500 companies (Amazon, etc.)
- **Objection:** Skeptical customers will pay by card due to their negotiating power
- **Opportunity:** Untapped AR volume, may not have integration activated

**Colton's counter:** "Out of the 10,000 customers that we have... about 17% of all invoices are paid via credit card"
- **Data point:** 17% credit card adoption rate across Nickel customer base
- **Customer benefits:** Credit card points, 40-day float, business reasons
- **Surcharge passing:** Automatic, no fee to merchant

**Outcome:** Erik agreed to "keep that in mind" and explore AR volume with accounting team for potential volume discount qualification.

### Carson Crawford (Lake Carolina HOA)
**Quote:** "We were trying to find a cheaper option for our residents" + "I did notice that you guys offered a free ACH which I think is more online of what our board wants"
- **Organization:** 2,500-homeowner HOA
- **Annual assessment:** $1,150-1,260 per homeowner
- **Total AR volume:** ~$3M annually
- **Current pain:** ZAGO charges 4% credit card, $3.95 ACH fees
- **Desired state:** Free ACH, optional credit card with fee passed to homeowner

**Quote:** "We're wanting to go to more of, like, a... pay as you go... we don't care if you make one payment. We don't care if you make 12 payments. We don't care if you make 52 payments."
- **Use case:** Flexible payment plans (covered in recurring billing use case)
- **Payment portal:** "They just go click, hey, go click payments and be done with it"
- **Multi-channel:** Must send physical invoice by bylaws, but also email and web portal

**Credit card surcharge positioning:**
- Homeowners pay 2.99% fee if they choose credit card
- 100% fee passed to homeowner, not HOA
- 50-state surcharge compliance confirmed

**Outcome:** Strong buying signal for Plus plan, recurring billing + free ACH + payment portal

## Nickel Capability Match

### Invoice Creation
- **Manual creation:** Create invoices directly in Nickel
- **QuickBooks sync:** Import invoices automatically from QuickBooks Online
- **CSV upload:** Bulk create invoices via CSV import
- **Customization:**
  - Line items, descriptions, amounts
  - Due dates, invoice numbers
  - Attachments (PDFs, images, documents)
  - Notes/memos

### Invoice Delivery
- **Email delivery:** Automated email with payment link and invoice attachment
- **SMS delivery:** Text message with payment link (shortlink)
- **Manual sending:** Review before sending (auto-send toggle off)
- **Automatic sending:** Auto-send invoices created in QuickBooks (toggle on)
- **Branded design:** Logo, company name, professional template

### Payment Options
- **Zero-fee ACH:** Customer pays $0 for ACH/bank transfer
- **Credit card:** Customer pays 2.99% surcharge (customizable)
- **Payment portal:** Branded portal with custom URL/domain (Plus plan)
- **Website embedding:** Embed payment portal in customer website
- **Payment links:** Unique link per invoice, shareable anywhere

### Credit Card Surcharge Management
- **Global rule:** Set default surcharge % (0-100% of 2.99% fee)
- **Per-invoice override:** Adjust surcharge for individual invoices
- **50-state compliance:** Legal in all states and jurisdictions
- **Automatic calculation:** Surcharge calculated and disclosed automatically
- **Fee structure:** 2.99% credit card processing fee

### Payment Collection
- **Real-time notifications:** Email alerts when payment received
- **Payment history:** Track all payments per customer
- **QuickBooks posting:** Automatic posting to QB in ~1 second
- **Reconciliation:** No manual reconciliation needed

### Payment Portal Features
- **Customization:**
  - Custom URL and domain (Plus plan)
  - Logo and branding
  - Background and banner images
- **Customer self-service:**
  - View outstanding invoices
  - Make one-time payments
  - Set up payment plans (if recurring billing enabled)
- **Payment options:** ACH (free) or credit card (surcharge)

## Implementation Path

### Phase 1: Assessment (Week 1)
1. **Quantify invoice volume:** How many invoices per month?
2. **Identify customer payment methods:** ACH, check, credit card mix?
3. **Assess current process:**
   - How are invoices created today? (QB, Excel, manual)
   - How are invoices sent? (Email, mail, both)
   - How do customers pay? (Check, wire, ACH, card)
4. **Determine plan fit:**
   - If recurring billing needed: Plus plan required
   - If custom payment portal URL needed: Plus plan required
   - If basic invoice send/receive: Core (free) plan works

### Phase 2: Setup (Week 1-2)
1. **Account creation:** Sign up for appropriate plan
2. **Bank connection:** Link business bank account for ACH deposits
3. **Branding setup:**
   - Upload logo
   - Customize payment portal (if Plus plan)
   - Set custom URL/domain (if Plus plan)
4. **Customer import:**
   - Option A: QuickBooks sync (auto-import customers)
   - Option B: CSV upload
   - Option C: Manual entry as invoices created
5. **Surcharge configuration:**
   - Set global surcharge rule (default 100% = customer pays full 2.99%)
   - Test surcharge calculation and disclosure

### Phase 3: Testing (Week 2-3)
1. **Create test invoice:** Send to internal team member or trusted customer
2. **Test email delivery:** Verify email format, branding, payment link
3. **Test payment portal:** Click payment link, test ACH and card payment flows
4. **Test surcharge:** Verify credit card surcharge displays correctly
5. **Test QuickBooks posting:** Confirm payment posts to QB correctly (if integrated)

### Phase 4: Soft Launch (Week 3-4)
1. **Pilot with friendly customers:** Send invoices to 5-10 loyal customers
2. **Collect feedback:** Ask about email format, payment ease, any confusion
3. **Monitor adoption:** Track payment methods (ACH vs card) and speed
4. **Refine messaging:** Adjust invoice notes, email wording based on feedback
5. **Train team:** Ensure all AR staff comfortable with workflows

### Phase 5: Full Rollout (Month 2)
1. **Expand to all customers:** Send all new invoices via Nickel
2. **Update customer communication:**
   - Email notification of new payment options
   - Update website with payment portal link
   - Include payment link in invoice reminders
3. **Migrate open invoices:** Import outstanding invoices from QB (if applicable)
4. **Enable automation:** (if desired) Toggle on auto-send for QB invoices

### Phase 6: Optimization (Month 2+)
1. **Analyze payment data:**
   - What % paying by ACH vs card?
   - How fast are payments collected (DSO improvement)?
   - What % of customers using payment portal?
2. **Adjust surcharge rules:** Experiment with 50%, 75%, 100% surcharge
3. **Improve cash flow:** Use recurring billing for subscription customers
4. **Reduce check usage:** Reach out to check payers, encourage electronic payment

## Success Metrics

### Cash Flow Improvement
- **Days Sales Outstanding (DSO):** 20-40% reduction typical
- **Payment speed:** Invoices paid 5-10 days faster on average
- **Collection rate:** 10-20% improvement in on-time payment rate

### Cost Savings
- **Credit card fee elimination:** If passing 100% surcharge, $0 fee burden
- **Time savings:** 5-10 minutes per invoice (no manual sending/tracking)
- **Check processing:** Eliminate check deposit trips, fraud risk

### Revenue Protection
- **Margin preservation:** 2.9% margin saved on credit card payments
- **Fee transparency:** Customers understand and accept surcharge

### Customer Experience
- **Payment ease:** One-click payment from email link
- **Payment flexibility:** Choose ACH (free) or card (points/float)
- **Self-service:** Payment portal reduces "how do I pay?" inquiries

## Competitive Positioning

### vs. QuickBooks Payments
- **Nickel advantages:**
  - Faster payment delivery
  - Better surcharge control (50-state compliant)
  - Lower/no fees
  - Customizable payment portal
- **QuickBooks advantages:**
  - Native to QuickBooks (no integration needed)
  - Familiar to existing QB users

### vs. Stripe Invoicing
- **Nickel advantages:**
  - Free ACH (Stripe charges 0.8%, $5 cap)
  - QuickBooks integration (real-time sync)
  - Surcharge management built-in
  - Simpler UX for non-technical users
- **Stripe advantages:**
  - Developer-friendly (API access)
  - International payments
  - Subscription management features

### vs. Bill.com AR
- **Nickel advantages:**
  - Lower pricing ($0-45/month vs $49+/month)
  - Simpler UX
  - Free ACH for payers
- **Bill.com advantages:**
  - Enterprise features (approvals, workflows)
  - Mature product
  - International payments

## Common Objections

### "Our customers won't pay the credit card fee"
**Answer:** Totally understand the concern. A few things we see:
1. It's optional - customers can always choose free ACH
2. 17% of invoices across our 10,000 customers are paid via credit card (even with surcharge)
3. Many customers WANT to pay by card for points, float, or business reasons
4. You're not forcing anyone - just offering the option

Try it with a few invoices and see. You might be pleasantly surprised.

### "We need to send complex multi-page invoices"
**Answer:** Nickel invoicing is designed for simplicity. If you need complex multi-page invoices (like detailed construction pay apps), you can:
1. Create invoice in your current system (Procore, Excel, etc.)
2. Attach the PDF to Nickel invoice
3. Send via Nickel for payment collection

You get the complex invoice format + easy payment experience.

### "Fortune 500 customers won't pay by credit card"
**Answer:** You're probably right - large enterprises typically pay via ACH or wire and negotiate terms aggressively. Good news: Nickel's free ACH still works great for them. The credit card option is there for the 10-20% of customers who want it (smaller clients, fast-growing companies, etc.).

### "We already use QuickBooks to send invoices"
**Answer:** Many customers do! Key benefits of Nickel:
1. **Free ACH for customers** (QB may charge them fees)
2. **Faster ACH processing** (same-day to 2-day vs 3-5 days)
3. **Better surcharge control** (50-state compliant)
4. **Custom payment portal** (embed in your website)

You can still create invoices in QB, but send via Nickel for better payment experience.

### "Our customers prefer checks"
**Answer:** Definitely hear that, especially with older customers. Most businesses see 80-90% electronic payment adoption within 3-6 months of offering the option. The key is making it SO easy that checks become the harder option. You can always accept checks during transition, but most customers prefer the speed and convenience once they try it.

## Related Use Cases
- [[quickbooks-integration]] - Integration workflow for invoice sync
- [[large-scale-recurring-billing]] - Recurring billing for subscriptions/HOA
- [[payment-portal-embedding]] - Website integration

## Adoption Frequency
**HIGH** - 2 out of 4 transcripts directly discussed AR, with implicit opportunity in others
- Erik: 100% ACH currently, untapped AR expansion opportunity, QuickBooks integration potential
- Carson: 2,500 homeowners, $3M annual AR volume, replacing expensive ZAGO solution, recurring billing needs
- Jeff: Primarily wire transfers from wealthy clients, occasional credit card requests, complex invoicing via Procore
- Hardy: Implicit AR for firm invoicing and client enablement
