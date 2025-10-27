---
name: low-volume-ach-for-small-clients
title: Low-Volume ACH for Small Business Clients
description: Enabling occasional ACH payments for small businesses without expensive platform fees or per-transaction charges
domain: customer
node_type: use_case
status: validated
last_updated: 2025-10-24
frequency: medium
transcripts_referenced:
  - 2025-07-23_hardy-butler-accounting-firm
adoption_rate: "1 out of 4 transcripts (accounting firm specific)"
tags:
  - low-volume
  - ach-payments
  - small-business
  - accounting-firms
  - cost-reduction
  - occasional-use
related_docs:
  - "[[accounting-firm-client-enablement]]"
  - "[[free-plan-positioning]]"
---

# Use Case: Low-Volume ACH for Small Business Clients

## Summary
Small businesses that need to make occasional ACH payments (1-10 per month) are underserved by traditional banks (expensive per-transaction fees) and enterprise AP platforms (monthly platform fees disproportionate to usage). They need a zero-cost, simple ACH solution for as-needed payments.

## Description
This use case specifically addresses the "small client problem" that accounting firms and bookkeepers face:
- **Client size:** $100K-$1M annual revenue
- **Payment volume:** 1-10 ACH payments per month
- **Payment size:** Typically $500-$5,000 per payment
- **Current state:** Paying checks or expensive bank ACH fees ($3-7 per transaction)
- **Desired state:** Electronic payments without platform fees or per-transaction costs

This segment is too small for:
- **Bill.com:** $45-60/month minimum platform fee = $540-720/year for 5 payments/month
- **Bank ACH:** $3-7 per transaction × 10 transactions/month = $360-840/year
- **QuickBooks Pay:** Per-transaction fees and slow processing (3-5 days)

But perfect for:
- **Nickel Core (Free):** $0/month, unlimited free ACH up to $25K per transaction, 2-3 day processing

## Fit Assessment

### Excellent Fit Indicators
- **Payment volume:** 1-20 ACH payments per month
- **Payment size:** Under $25K per payment (within Core plan limit)
- **Cost sensitivity:** Cannot justify platform fees for low usage
- **Simplicity preference:** Don't need complex approval workflows
- **Occasional use:** "As needed" payment cadence, not scheduled recurring
- **Check elimination goal:** Want to stop writing paper checks (fraud risk, time burden)
- **Electronic payment mandate:** Advisor (CPA, bookkeeper) pushing them to modernize

### Moderate Fit Indicators
- **Payment volume:** 10-30 ACH payments per month (may benefit from Plus plan features)
- **Mixed payment sizes:** Some over $25K (would need Plus plan)
- **Some scheduling needs:** Want to schedule a few payments in advance occasionally
- **Growing business:** May scale beyond "low volume" within 6-12 months

### Poor Fit Indicators
- **High volume:** 30+ payments per month (should consider Plus plan or Bill.com)
- **Complex workflows:** Need multi-level approvals, policy controls, budgets
- **Large payments:** Regularly pay over $25K (requires Plus plan)
- **International payments:** Paying overseas vendors (Nickel is US-only)
- **Check preference:** Resistant to electronic payments, prefer paper checks

## Indicators from Transcripts

### Hardy Butler (Accounting Firm)

**Firm context:**
- **CPA/bookkeeping/fractional CFO firm**
- **15 employees, 150 clients**
- **Annual revenue:** Above $1M
- **Current tools:** Bill.com (high-volume clients), RAMP, Brex, Intuit Bill Pay, Melio (phasing out), QuickBooks Online Accountant

**Primary pain point:**
**Quote:** "I want to be able to send ACH payments in low volume or frankly on an as needed basis without paying an absurd monthly platform fee"
- **Problem:** Small clients don't have enough volume to justify Bill.com's $45-60/month fee
- **Current state:** Bill.com works great for high-volume clients but too expensive for small ones
- **Desired state:** Zero-cost ACH solution for occasional payments

**Quote:** "For our smaller clients who need to be able to make an ACH payment occasionally from time to time. I don't want to have to pay $7 to a bank"
- **Bank fees:** $7 per ACH transaction prohibitive for occasional use
- **Example math:** 5 payments/month × $7 = $35/month = $420/year
- **Client burden:** Passing $7 fee to small client creates friction

**Quote:** "I need to be able to make an ACH payment inexpensively as needed, as if it were a bank transaction and not an act of Congress"
- **Complexity issue:** Current ACH processes too complicated
- **Friction:** Multiple steps, approvals, platforms for simple payment
- **Ideal state:** As easy as bank transfer, zero cost, no overhead

**Check washing driving urgency:**
**Quote:** "There's no question that with all the check washing that's going on out there, that an electronic payment is by far the safest method to go"
- **Security concern:** Check fraud is endemic, electronic payments safer
- **Advisor role:** Hardy is advising clients to stop writing checks
- **Transition need:** Need electronic payment option to replace checks

**Quote:** "Been pleasantly surprised actually. I expected it was gonna be much more difficult than it has been" [transitioning clients from checks to electronic]
- **Change management:** Clients adapting to electronic payments easier than expected
- **Success signal:** Hardy successfully transitioning clients with Bill.com (high-volume)
- **Gap:** Need same success for low-volume clients without Bill.com cost

**Business model sustainability concern:**
**Quote:** "I don't know how you're making money, to be quite frank, and that's one of the things I want to find out"
- **Skepticism:** Free model seems unsustainable (Melio went from free to paid)
- **Due diligence:** Hardy does angel investing, wants to validate business model
- **Trust factor:** Needs proof Nickel won't eliminate free tier like Melio did

**Quote:** "I work with a lot of early stage companies, a lot of VC backed companies. I'm guessing you're probably backed by some of something like that. And I want to make sure that we're not partnering with somebody that's... I want to make sure you have a sustainable business model"
- **Vendor risk:** Concerned about Nickel going out of business or changing pricing
- **Request:** Asked for pitch deck to validate funding, business model
- **Resolution:** Colton explained cash-positive status, 10K+ users, Series A fundraising

**Accounting firm workflow need:**
**Quote:** "If I generate 150 invoices every month, I don't want them all sinking over if I'm doing a soft launch with Nickel"
- **Selective deployment:** Wants to test with subset of clients first
- **Gap identified:** Cannot selectively sync QuickBooks clients (all-or-nothing)
- **Workaround:** Generate invoices manually in Nickel for pilot clients

**Deployment approach:**
**Quote:** "Soft rollout with loyal customers first"
- **Pilot strategy:** Test with 5-10 friendly clients
- **Validate before scaling:** Prove value before expanding to all 150 clients
- **Use cases:** Test with both low-volume (free plan) and high-volume (Plus plan) clients

## Nickel Capability Match

### Core Free Plan - Perfect Fit
- **Cost:** $0/month forever (no credit card required to start)
- **ACH payments:** Unlimited free ACH up to $25K per transaction
- **Processing time:** 2-3 day turnaround (4 PM EST cutoff)
- **No hidden fees:** Truly zero cost for ACH (no setup, no monthly, no per-transaction)
- **Active users:** Up to 3 users per account
- **QuickBooks integration:** Real-time sync with QuickBooks Online
- **Payment types:** Bill pay (AP) and invoice/payment collection (AR)

### Use Case Fit Analysis
**For small client making 5 ACH payments/month:**
- **Nickel Core:** $0/month = $0/year
- **vs. Bank ACH:** $7 × 5 × 12 = $420/year saved
- **vs. Bill.com:** $45 × 12 = $540/year saved
- **vs. Melio (now paid):** Variable pricing, typically $100-300/year saved

**For small client making 10 ACH payments/month:**
- **Nickel Core:** $0/month = $0/year
- **vs. Bank ACH:** $7 × 10 × 12 = $840/year saved
- **vs. Bill.com:** $45 × 12 = $540/year saved

**When to upgrade to Plus ($35-45/month):**
- Payments exceed $25K per transaction
- Need to schedule payments in advance
- Want recurring payment automation
- Need faster ACH (same-day to 2-day vs 2-3 day)
- More than 3 active users needed

### Accounting Firm Enablement Model
1. **CPA recommends Nickel to small clients**
2. **Client signs up for free Core plan**
3. **CPA gets view-only or manager access to client account**
4. **CPA processes payments on client's behalf (or trains client to do it)**
5. **Payments sync to client's QuickBooks in real-time**
6. **CPA invoices client for bookkeeping time (not Nickel cost, since it's free)**

**Accounting firm benefit:**
- Better service to small clients (no more $7 bank fees)
- Eliminate check processing time (fraud risk, deposit trips)
- Real-time payment visibility via QuickBooks
- No software cost to pass through to client
- Standardize on one platform across all clients (Nickel for small, Bill.com for large)

## Implementation Path

### Phase 1: Accounting Firm Pilot (Week 1-2)
1. **Select pilot clients:**
   - Choose 5-10 small clients currently using checks or bank ACH
   - Ideal profile: 5-15 payments/month, under $25K per payment
   - Loyal clients willing to try new process
2. **Create Nickel accounts:**
   - One free Core account per client
   - Link client's bank account
   - Import vendors from QuickBooks (if applicable)
3. **CPA access setup:**
   - Client invites CPA firm as Manager or Admin
   - CPA can process payments on client's behalf
4. **Training:**
   - 15-minute walkthrough with client (or do it for them)
   - Show how to add vendor, create bill, pay via ACH

### Phase 2: Testing (Week 2-3)
1. **Process test payment:**
   - Select low-risk vendor (utility, subscription, familiar vendor)
   - Process ACH payment through Nickel
   - Verify 2-3 day delivery
2. **Verify QuickBooks sync:**
   - Confirm payment posts to QuickBooks correctly
   - Check categorization and vendor matching
3. **Track client feedback:**
   - Was it easy?
   - Any confusion?
   - Faster than checks?
4. **Measure time savings:**
   - Time to process payment (vs writing check, mailing, bank ACH)
   - Time saved on check deposits, reconciliation

### Phase 3: Expansion (Month 2-3)
1. **Expand pilot clients' usage:**
   - Move all AP payments to Nickel (not just test)
   - Transition away from checks and bank ACH entirely
2. **Add new pilot clients:**
   - Expand by 5-10 clients per month
   - Learn from early adopter feedback
3. **Document best practices:**
   - Create internal firm guide for Nickel setup
   - Template communication to clients about new payment method
   - FAQ for common client questions

### Phase 4: Scale (Month 3-6)
1. **Offer to all small clients:**
   - Position Nickel as standard for clients under 30 payments/month
   - Bill.com remains for high-volume clients (30+ payments/month)
2. **Train firm staff:**
   - All bookkeepers trained on Nickel workflow
   - Consistent process across all clients
3. **Measure ROI:**
   - Time saved per client per month
   - Cost saved per client per year (bank fees, platform fees eliminated)
   - Client satisfaction (easier, faster, safer than checks)

### Phase 5: Optimization (Month 6+)
1. **Refine segmentation:**
   - Which clients should be on Nickel free vs Plus vs Bill.com?
   - Based on volume, transaction size, features needed
2. **Expand use cases:**
   - Start using Nickel for AR (invoicing) for appropriate clients
   - Use for firm's own AP/AR (eat your own dog food)
3. **Refer other firms:**
   - Nickel offers $750 referral for accounting firm referrals
   - Share success with peer CPAs in local community

## Success Metrics

### Cost Savings per Client
- **Eliminate bank ACH fees:** $7 × payments/month × 12 = $420-1,680/year per client
- **Eliminate platform fees:** vs Bill.com $540/year, vs Melio $100-300/year
- **Total savings:** $500-2,000/year per small client

### Time Savings per Client
- **Payment processing:** 5-10 minutes per payment saved (vs check or bank ACH)
- **Monthly time savings:** 25-100 minutes per client (5-10 payments/month)
- **Annual time savings:** 5-20 hours per client

### Risk Reduction
- **Check fraud elimination:** 100% if all checks eliminated
- **Payment tracking:** Full audit trail vs paper check register
- **Cash flow visibility:** Real-time vs waiting for checks to clear

### Client Satisfaction
- **Ease of use:** "As easy as bank transaction" vs "act of Congress"
- **Cost savings:** $0 fee vs $7 per payment
- **Security:** Electronic payment vs check washing risk
- **Speed:** 2-3 days vs days to mail check + vendor deposit time

## Competitive Positioning

### vs. Bank ACH
- **Nickel advantages:**
  - $0 per transaction vs $3-7 per transaction
  - Better UX (faster, easier than bank online bill pay)
  - QuickBooks integration (real-time sync)
  - Multi-user access (vs single online banking login)
- **Bank advantages:**
  - Existing relationship
  - Wire transfer capability (Nickel doesn't offer wires)
  - In-person support

**Cost comparison (10 payments/month):**
- Bank: $7 × 10 × 12 = $840/year
- Nickel: $0/year
- **Savings: $840/year**

### vs. Bill.com
- **Nickel advantages:**
  - $0/month vs $45-60/month minimum ($540-720/year)
  - Simpler UX (less complex for small clients)
  - No learning curve or training needed
- **Bill.com advantages:**
  - Enterprise features (approvals, policies, budgets)
  - Check printing/mailing
  - International payments
  - Better for high-volume (30+ payments/month)

**Cost comparison (5 payments/month):**
- Bill.com: $45 × 12 = $540/year
- Nickel: $0/year
- **Savings: $540/year**

**Recommendation:** Nickel for low-volume, Bill.com for high-volume (complementary)

### vs. Melio
- **Nickel advantages:**
  - Still free (Melio eliminated free tier, lost trust)
  - Faster ACH processing (2-3 days vs 3-5 days)
  - QuickBooks real-time sync (vs batch sync)
  - No risk of pricing changes (Nickel monetizes via Plus plan, not removing free)
- **Melio advantages:**
  - Established brand
  - Some users grandfathered into old free pricing

**Why customers left Melio for Nickel:**
- Melio "gotten less desirable" after eliminating free option
- Hardy mentioned Melio specifically as incumbent he's phasing out

### vs. QuickBooks Pay
- **Nickel advantages:**
  - $0 fees vs QB Pay's per-transaction fees
  - Faster ACH (2-3 days vs 3-5 days)
  - Better surcharge control (AR side)
- **QuickBooks Pay advantages:**
  - Native to QuickBooks (no integration needed)
  - Check printing/mailing

## Common Objections

### "How do you make money if it's free?"
**Answer (from transcript):**
- **Subscription revenue:** Plus plan ($35-45/month) for higher-volume customers
- **Credit card processing:** 2.99% fee on AR credit card payments
- **Cash-positive:** Already profitable with 10,000+ customers
- **Series A fundraising:** Upcoming raise to scale, not to survive
- **Not Melio:** Won't eliminate free tier, it's core to business model

**Key message:** Free tier is sustainable, not a bait-and-switch. Nickel makes money from customers who need Plus features, not by eliminating free.

### "Our clients' payments exceed $25K"
**Answer:** Great! Two options:
1. **Plus plan:** $35-45/month, up to $1M per transaction
2. **Mixed approach:** Nickel free for most payments under $25K, bank wire for occasional large payments

For most small businesses, 90%+ of payments are under $25K, so free plan works for majority of their needs.

### "We need scheduled payments"
**Answer:** Scheduled payments are a Plus plan feature ($35-45/month). But for low-volume occasional use, most clients manually process when payment is due. If client needs scheduling, Plus plan ROI:
- $35/month = $420/year
- vs. Bank ACH: $7 × 10 payments/month = $840/year
- **Still saving $420/year even with Plus plan**

### "What if Nickel eliminates the free plan like Melio?"
**Answer (positioning from transcript):**
- **Business model difference:** Nickel monetizes via Plus plan upgrades, not by removing free
- **10,000+ free users:** Proven scale and adoption of free tier
- **Cash-positive:** Not burning cash waiting to flip pricing
- **Fundraising:** Series A is for growth, not to stay alive

**Build trust:** Offer to share pitch deck (Hardy asked for this), explain monetization strategy, highlight contrast with Melio.

### "Our clients don't want to learn new software"
**Answer:** Totally understand. Good news:
1. **15-minute setup:** Create account, link bank, start paying bills
2. **Familiar workflow:** Very similar to online banking bill pay
3. **CPA can do it for them:** You process payments on their behalf (with their approval)
4. **QuickBooks sync:** If they use QB, they don't need to touch Nickel - you can handle it

Most CPAs process payments for clients anyway, so client doesn't need to learn anything.

### "We only need this for a few clients, not worth it"
**Answer:** Perfect! That's exactly the use case:
- **No commitment:** No monthly fee, no contract, no credit card required
- **Client-by-client rollout:** Start with 1-2 clients, expand as you see value
- **No switching cost:** If a client scales up, keep using Nickel or migrate to Bill.com
- **Try it yourself first:** Use for your own firm's AP/AR to test before recommending

Zero risk, zero cost to try.

## Related Use Cases
- [[high-volume-ap-processing]] - When clients graduate from low to high volume
- [[accounting-firm-client-enablement]] - Broader accounting firm use case
- [[quickbooks-integration]] - Integration workflow

## Adoption Frequency
**MEDIUM** - 1 out of 4 transcripts discussed this specific use case (Hardy Butler)

**Why it matters:** While only explicitly discussed in one transcript, this use case addresses a widespread market need:
- Accounting firms consistently face "small client payment problem"
- Small businesses universally frustrated with bank ACH fees
- Check fraud driving urgency for electronic payment alternatives
- Melio's pricing change created market opportunity for Nickel

**Applicability:** Relevant to:
- **150,000+ CPA firms** in US
- **30+ million small businesses** with occasional payment needs
- **Bookkeepers and fractional CFOs** serving small clients
- **Small nonprofits, associations, clubs** with occasional vendor payments

This is a high-volume, low-ACV (annual contract value) use case that drives user adoption and word-of-mouth growth.
