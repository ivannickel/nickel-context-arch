---
name: multi-entity-payment-management
title: Multi-Entity Payment Management for Real Estate and Holding Companies
description: Managing payments across multiple legal entities (LLCs, properties, subsidiaries) with separate accounting and banking requirements
domain: customer
node_type: use_case
status: validated
last_updated: 2025-10-24
frequency: medium
transcripts_referenced:
  - 2025-07-23_hardy-butler-accounting-firm
  - 2025-07-23_prime-renovations-jeff-streich
adoption_rate: "2 out of 4 transcripts"
tags:
  - multi-entity
  - real-estate
  - property-management
  - accounting-firms
  - entity-structure
related_docs:
  - "[[entity-structure-setup]]"
  - "[[accounting-firm-client-management]]"
---

# Use Case: Multi-Entity Payment Management

## Summary
Business owners and accounting firms managing multiple legal entities (LLCs, properties, subsidiaries, clients) need separate payment accounts per entity while maintaining centralized visibility and simplified management.

## Description
Multi-entity payment management addresses the needs of:
- **Real estate investors:** Separate LLCs per property or property portfolio
- **Holding companies:** Parent company with multiple subsidiary entities
- **General contractors:** Separate entities per project or service line
- **Accounting firms:** Managing payments for 50-150+ client entities
- **Franchise owners:** Multiple franchise locations as separate entities

These businesses require:
- **Legal separation:** Distinct accounting per entity (corporate veil protection)
- **Banking separation:** Separate bank accounts per entity
- **Payment separation:** Separate payment processing per entity
- **Centralized management:** Single login to access all entities
- **User access control:** Grant team members access to specific entities only

## Fit Assessment

### Excellent Fit Indicators
- **Entity count:** 3-20 separate entities requiring payment processing
- **Clear entity structure:** Each entity has distinct purpose, customers, vendors
- **Separate accounting:** Each entity maintains separate books (often in QuickBooks)
- **Payment processing needs:** Each entity sends invoices or pays bills independently
- **Centralized ownership:** One owner/manager oversees all entities
- **Team access requirements:** Different staff access different entities

### Moderate Fit Indicators
- **Entity count:** 2-3 entities (may not need sophisticated multi-entity features)
- **Partial overlap:** Some customers/vendors span multiple entities
- **Simplified accounting:** Entities tracked via classes/projects vs separate QB files
- **Low volume per entity:** Each entity processes fewer than 10 payments/month

### Poor Fit Indicators
- **Single entity:** Only one legal entity (standard use case)
- **Very high entity count:** 20+ entities (may need enterprise solution)
- **Complex consolidation:** Need consolidated reporting across all entities
- **Multi-currency:** Entities operate in different currencies
- **International entities:** Entities in different countries with different regulations

## Indicators from Transcripts

### Hardy Butler (Accounting Firm)
**Firm context:**
- **Type:** CPA/bookkeeping/fractional CFO firm
- **Employees:** 15 team members
- **Clients:** 150 client entities
- **Services:** Bookkeeping, accounting, fractional CFO
- **Tech stack:** QuickBooks Online Accountant, Bill.com (high-volume clients), RAMP, Brex, Melio (phasing out)

**Multi-entity need (Accounting firm managing client entities):**
**Quote:** "If I create... a firm account... I can invite members of my firm... And then I can allocate access to different clients"
- **Requirement:** Single firm login with dropdown to access different client accounts
- **User access control:** Allocate team members to specific clients
- **Access levels:** View-only (unlimited, no seat cost) vs Manager/Admin (limited seats)
- **Deal killer concern:** "If I had to have a separate login per client, that would be a deal killer"

**Quote:** "If I have access to a client and two other members of my team have access to a client, does that take up three [seats] or does that just take up one?"
- **Clarification needed:** How do user seats work across multiple client entities?
- **Resolution:** Manager/admin seats count, view-only doesn't
- **Outcome:** Resolved - understood seat counting model

**Multi-entity need (Personal real estate entities):**
**Quote:** "We probably have three or four different entities that have the different properties... We would require each of those entities to have their own separate account"
- **Entity count:** 3-4 separate LLCs for rental properties
- **Use case:** Collect rent via ACH from commercial tenants
- **Volume per entity:** Very low (example: 2 tenants)
- **Platform fit:** Free Core plan per entity (not worth $35/month Plus per entity)
- **Tech:** QuickBooks Desktop (no integration available)

### Jeff Streich (Prime Renovations)
**Business context:**
- **Type:** Boutique high-end general contractor
- **Current revenue:** $3M annually
- **Target revenue:** $10M annually
- **Project size:** ~$700K average per project
- **Project volume:** 10-15 projects per year
- **Scaling phase:** Just hired CFO, sales team, transitioning from owner-operator to CEO

**Multi-entity comparison (Relay Financial):**
**Quote:** "Whenever I start a new job, I could open up a new account... I can have 20 different accounts"
- **Current solution:** Relay Financial multi-account structure
- **Use case:** Separate bank account per project (e.g., "100 Park Avenue")
- **Benefit:** Direct wire deposits from clients to project-specific account
- **Dashboard:** View all accounts in single dashboard
- **Routing numbers:** Each account has unique routing/account number

**Nickel limitation:**
- **No multi-account structure:** Nickel requires separate account per entity, not sub-accounts
- **Workaround:** Use QuickBooks classes/projects to track per-project payments
- **Gap:** Cannot replicate Relay's project-based bank account model

**Business entity structure (implied):**
- Likely has Prime Renovations NYC as primary entity
- May have separate entities per major project or service line (common in construction)
- Setting up Procore-QuickBooks integration suggests formalized entity accounting

## Nickel Capability Match

### Current Multi-Entity Support
**Separate accounts per entity (as of transcripts):**
- Each legal entity requires a separate Nickel account
- Each account has:
  - Separate login (email address)
  - Separate bank connection
  - Separate customers and vendors
  - Separate invoice/payment history
  - Separate QuickBooks integration (if applicable)

**No consolidated multi-entity dashboard:**
- Cannot view all entities in single pane of glass
- Must log out and log back in to switch entities
- No consolidated reporting across entities

### Accounting Firm Use Case (Workaround)
**Quote from transcript:** "I guess one important question... as far as creating an invoice in your system, all right, would I have to do that manually per, Resident."
- Colton explained firm structure: Firm account > Invite team members > Allocate client access
- **Access control:** Firm admin controls who accesses which clients
- **Seat management:**
  - View-only users: Unlimited, no cost
  - Manager/Admin users: Limited by plan, counted as active users
- **Limitation:** If managing 150 clients, need 150 separate Nickel accounts (one per client)

### Real Estate Multi-Property Use Case
**Hardy's rental properties:**
- 3-4 separate entities (LLCs) per property or portfolio
- Each entity needs separate Nickel account
- Low volume per entity: Free Core plan works
- No integration: Using QuickBooks Desktop (not QBO)

**Workflow:**
1. Create separate Nickel account per entity (e.g., "123 Main St LLC")
2. Link entity's bank account to that Nickel account
3. Use that account only for that entity's transactions
4. Maintain separate QuickBooks file per entity (or classes in single file)

### Project-Based Payment Organization (Jeff's need)
**Current solution (Relay):** Multi-account structure with sub-accounts per project
**Nickel limitation:** No sub-account structure
**Workaround options:**
1. **QuickBooks classes:** Track projects via QB classes, single Nickel account
2. **Memo fields:** Use memo/note fields to tag project on each payment
3. **Separate entities:** If projects are legally separate entities, use separate accounts
4. **Relay + Nickel:** Use Relay for banking/project accounts, Nickel for invoicing/AR

## Implementation Path

### For Accounting Firms (150+ Client Entities)

#### Phase 1: Pilot (Month 1)
1. **Select pilot clients:** Choose 5-10 loyal, low-volume clients
2. **Create Nickel accounts:** One account per pilot client
3. **Access setup:**
   - Firm admin has login for each client account (password manager recommended)
   - Invite team members to specific client accounts
   - Set access levels (view-only vs manager)
4. **Test workflows:**
   - Invoice sending
   - Payment receiving
   - QuickBooks sync (if client uses QBO)
   - User access controls

#### Phase 2: Expansion (Month 2-3)
1. **Add client cohorts:** Expand by 10-20 clients per month
2. **Standardize setup:** Create template for new client onboarding
3. **Train team:** Ensure all team members comfortable with workflows
4. **Gather feedback:** Track pain points, feature requests

#### Phase 3: Optimization (Month 3+)
1. **Evaluate ROI:** Calculate time/cost savings per client
2. **Expand use cases:** Add AP (bill pay) if initially only using AR
3. **Replace incumbent:** Phase out Bill.com, Melio, etc. where Nickel fits
4. **Feature requests:** Share feedback with Nickel for product roadmap

### For Real Estate Investors (3-10 Properties)

#### Phase 1: Setup (Week 1-2)
1. **Create account per entity:**
   - Entity 1: "123 Main St LLC" (Nickel account #1)
   - Entity 2: "456 Oak Ave LLC" (Nickel account #2)
   - Entity 3: "789 Pine Rd LLC" (Nickel account #3)
2. **Link bank accounts:** Each entity's bank to its Nickel account
3. **Add tenants as customers:** Import tenant list to each property account
4. **Set up invoices:** Create rent invoices (recurring billing if Plus plan)

#### Phase 2: Testing (Week 2-3)
1. **Test rent collection:** Send invoice to one tenant per property
2. **Verify bank deposits:** Ensure funds hit correct entity bank account
3. **Test QuickBooks sync:** (if using QBO) Verify proper posting
4. **Validate separation:** Confirm no cross-contamination between entities

#### Phase 3: Rollout (Week 3-4)
1. **Notify tenants:** Inform tenants of new payment method
2. **Send all invoices:** Use Nickel for all rent collection
3. **Monitor adoption:** Track ACH vs check usage
4. **Handle issues:** Address tenant questions, failed payments

### For General Contractors (Project-Based)

#### Phase 1: Assessment (Week 1)
1. **Determine entity structure:**
   - Are projects legally separate entities? → Separate Nickel accounts
   - Are projects tracked via QB classes? → Single Nickel account
2. **Evaluate Relay alternative:**
   - If Relay's multi-account banking is critical: Keep Relay, add Nickel for AR/invoicing
   - If can track projects via QB: Use Nickel for all payment processing

#### Phase 2: Setup (Week 1-2)
**If separate entities:**
- Create Nickel account per entity
- Link entity bank account
- Import customers/vendors per entity

**If single entity with project tracking:**
- Create single Nickel account
- Use QuickBooks classes for project tracking
- Tag payments with project in memo field

#### Phase 3: Workflow Design (Week 2-3)
1. **Invoicing:** Create invoices tagged with project/class
2. **Payment collection:** Payments post to QB with correct class
3. **AP processing:** Pay subcontractors from correct project budget
4. **Reporting:** Run project-level reports in QB (Nickel data flows through)

## Success Metrics

### For Accounting Firms
- **Time savings:** 30-60 minutes per client per month (automation)
- **Client satisfaction:** Offer better payment experience than incumbent
- **Cost savings per client:** $10-50/month depending on volume
- **Team efficiency:** Fewer platforms to train on and manage

### For Real Estate Investors
- **Cost savings:** Eliminate $7 bank ACH fees per rent payment
- **Collection speed:** Faster rent collection (electronic vs checks)
- **Bookkeeping accuracy:** Automated QuickBooks posting per entity
- **Security:** Eliminate check fraud risk

### For General Contractors
- **Project tracking:** Clear separation of payments per project
- **Cash flow visibility:** Real-time project-level cash flow
- **Client communication:** Professional branded invoicing per project
- **Subcontractor payments:** Faster, cheaper payments to subs

## Competitive Positioning

### vs. Bill.com
- **Nickel advantages:**
  - Lower pricing per entity ($0-45 vs $49+)
  - Simpler UX
  - Free ACH for payers
- **Bill.com advantages:**
  - Multi-entity dashboard (consolidated view)
  - Complex approval workflows per entity
  - Better for high-volume, complex needs

### vs. Relay Financial (Banking)
- **Relay advantages:**
  - Multi-account structure with sub-accounts
  - Banking features (checking, cards)
  - $5 wire transfers
- **Nickel advantages:**
  - Unlimited free ACH (vs 10/month cap)
  - QuickBooks real-time sync
  - Invoice/AR capabilities
  - Lower pricing ($35-45 vs $90)

**Recommendation:** Relay for banking/project accounts, Nickel for invoicing/AR (complementary)

### vs. QuickBooks Multi-Entity
- **Nickel advantages:**
  - Better payment experience for customers
  - Lower/no fees
  - Faster ACH processing
- **QuickBooks advantages:**
  - Native to QB (no integration needed)
  - Can track entities via classes in single QB file

## Common Objections

### "We need a consolidated dashboard for all entities"
**Answer:** You're right, Nickel doesn't have that today. Each entity is a separate account. Workarounds:
1. **Password manager:** Store logins for all entities, quick switching
2. **Browser tabs:** Keep multiple entities open in separate tabs
3. **QuickBooks reporting:** If all entities in QB, run consolidated reports there

We hear this request often and it's on the roadmap. For now, this works for businesses with 3-20 entities.

### "We manage 150 clients - do we need 150 separate accounts?"
**Answer:** For a true multi-client accounting firm setup, yes. Each client entity is a separate account. However:
1. **Pilot first:** Test with 5-10 clients before committing to 150
2. **Selective deployment:** Use Nickel for clients where it's the best fit (Bill.com for others)
3. **Firm access:** You have access to all client accounts, team members assigned per client
4. **No cost for low-volume:** Free Core plan works for many small clients

If you need true multi-entity dashboard, Bill.com may be better fit for your scale.

### "Can I have one account with sub-accounts per project?"
**Answer:** Not today. Nickel doesn't support sub-account structure. Alternatives:
1. **QuickBooks classes:** Track projects via QB classes, single Nickel account
2. **Separate entities:** If projects are legal entities, separate Nickel accounts
3. **Relay + Nickel:** Use Relay for project banking, Nickel for invoicing/AR

### "Does each entity pay $35-45/month?"
**Answer:** Depends on needs:
- **Low volume per entity:** Use free Core plan per entity ($0/month)
- **High volume or recurring billing:** Plus plan per entity ($35-45/month)
- **Mixed:** Some entities on Core, others on Plus

Example: 5 entities, 2 high-volume (Plus), 3 low-volume (Core) = $70-90/month total vs $250+ with other platforms.

### "What if team members need access to multiple entities?"
**Answer:** No problem. Your team member can be invited to as many entity accounts as needed. Seat counting:
- **View-only access:** Unlimited across all entities, no cost
- **Manager/Admin access:** Counts as one seat per entity (on Plus plan)

Example: Team member needs Manager access to 5 client entities on Plus plan = 5 seats consumed.

## Product Gaps & Feature Requests

### Gaps Identified from Transcripts
1. **No multi-entity dashboard:** Cannot view all entities in single pane
2. **No selective QuickBooks sync:** Cannot sync subset of QB clients for pilot (accounting firms)
3. **No sub-account structure:** Cannot create project-specific accounts under parent entity
4. **No consolidated reporting:** Cannot run reports across multiple entities
5. **No entity switching:** Must log out/in to switch entities (no dropdown)

### Workarounds Available Today
1. **Password manager:** Use 1Password, LastPass to store entity logins
2. **Browser profiles:** Chrome profiles per entity for persistent logins
3. **QuickBooks classes:** Track projects/entities in single QB file
4. **Manual CSV aggregation:** Export data from each entity, consolidate in Excel

### Feature Requests for Product Team
1. **Multi-entity dashboard:** Single login, dropdown to switch entities
2. **Consolidated reporting:** Roll-up reports across entities
3. **Firm/parent account:** Master account with sub-accounts per entity/client
4. **Selective sync:** Choose which QB clients/entities to sync (accounting firms)
5. **Entity templates:** Clone entity setup for faster onboarding

## Related Use Cases
- [[accounting-firm-client-enablement]] - Accounting firms managing client payments
- [[real-estate-rent-collection]] - Property management specific workflows
- [[quickbooks-integration]] - Integration per entity

## Adoption Frequency
**MEDIUM** - 2 out of 4 transcripts discussed multi-entity needs
- Hardy Butler: CPA firm (150 clients) + rental properties (3-4 entities)
- Jeff Streich: Uses Relay's multi-account structure for project-based organization (10-15 projects)

**Common pattern:** Multi-entity needs are often secondary to primary use case (AP/AR processing) but become decision factor for sophisticated users.
