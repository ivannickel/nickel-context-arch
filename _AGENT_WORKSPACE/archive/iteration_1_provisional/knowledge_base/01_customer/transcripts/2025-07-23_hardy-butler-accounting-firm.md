---
source_file: knowledge_base/meetings_md/008_hardy-butler-and-colton-ofarrell_2025-07-23.md
processed_date: 2025-10-24
meeting_date: 2025-07-23
meeting_duration_min: 39.9
sales_rep: Colton O'Farrell
customer_contact: Hardy Butler
customer_emails:
  - hardy.butler@gmail.com
  - hardy.butler@teamblackline.com
company_context: CPA/bookkeeping/fractional CFO firm with 15 employees and 150 clients
revenue_range: Above $1M annually
deal_outcome: Interest in testing, requested demo for team member
transcript_number: "008"

pain_points:
  - id: pp_008_001
    category: pricing
    subcategory: platform-fees
    quote: "I want to be able to send ACH payments in low volume or frankly on an as needed basis without paying an absurd monthly platform fee"
    context: Hardy's primary motivation for exploring Nickel - needs low-volume ACH without expensive platform fees
    intensity: high
    line_reference: 25

  - id: pp_008_002
    category: pricing
    subcategory: bank-fees
    quote: "For our smaller clients who need to be able to make an ACH payment occasionally from time to time. I don't want to have to pay $7 to a bank"
    context: Bank fees are prohibitive for low-volume clients
    intensity: high
    line_reference: 29

  - id: pp_008_003
    category: security
    subcategory: check-fraud
    quote: "There's no question that with all the check washing that's going on out there, that an electronic payment is by far the safest method to go"
    context: Check washing fraud driving need for electronic payments
    intensity: medium
    line_reference: 31

  - id: pp_008_004
    category: business-sustainability
    subcategory: vendor-viability
    quote: "I don't want to partner with someone that's... I want to make sure you have a sustainable business model"
    context: Concern about partnering with unsustainable free solutions
    intensity: high
    line_reference: 27

  - id: pp_008_005
    category: pricing
    subcategory: melio-changes
    quote: "We used to use Melio... but that's gotten less desirable... it was 'cause it was a free option, a free alternative"
    context: Melio no longer free, driving search for alternatives
    intensity: medium
    line_reference: 23-25

  - id: pp_008_006
    category: workflow
    subcategory: ach-complexity
    quote: "I need to be able to make an ACH payment inexpensively as needed, as if it were a bank transaction and not an act of Congress"
    context: Current ACH processes are too complex and expensive
    intensity: high
    line_reference: 37

  - id: pp_008_007
    category: volume-mismatch
    subcategory: bill-com-overkill
    quote: "Just because someone has the volume to go on bill.com, if your platform and solution is pretty slick and good, hell, we'll consider that"
    context: Bill.com works for high-volume clients but too much for small clients
    intensity: medium
    line_reference: 37

  - id: pp_008_008
    category: workflow
    subcategory: multi-entity-management
    quote: "We probably have three or four different entities that have the different properties... We would require each of those entities to have their own separate account"
    context: Managing multiple entities requires separate accounts
    intensity: low
    line_reference: 113-114

  - id: pp_008_009
    category: workflow
    subcategory: accounting-firm-access
    quote: "If I create... a firm account... I can invite members of my firm... And then I can allocate access to different clients"
    context: Needs multi-user firm structure with client-level permissions
    intensity: medium
    line_reference: 131

  - id: pp_008_010
    category: workflow
    subcategory: selective-sync
    quote: "If I generate 150 invoices every month, I don't want them all sinking over if I'm doing a soft launch with Nickel"
    context: Cannot selectively sync specific clients during pilot phase
    intensity: medium
    line_reference: 137

objections:
  - id: obj_008_001
    type: skepticism
    category: sustainability
    quote: "I don't know how you're making money, to be quite frank, and that's one of the things I want to find out"
    handling: Colton explained pricing model, subscription revenue, and cash-positive status
    resolution: Partially resolved - Hardy requested pitch deck
    line_reference: 25

  - id: obj_008_002
    type: request
    category: due-diligence
    quote: "Ask your founders if they'd be willing to send me their pitch deck for their series seed raise... I'm happy to look at it as an investor"
    handling: Colton agreed to ask founders
    resolution: Pending
    line_reference: 41

  - id: obj_008_003
    type: concern
    category: business-longevity
    quote: "I work with a lot of early stage companies, a lot of VC backed companies. I'm guessing you're probably backed by some of something like that. And I want to make sure that we're not partnering with somebody that's... I want to make sure you have a sustainable business model"
    handling: Colton explained cash-positive status, 10,000+ users, upcoming Series A
    resolution: Partially resolved
    line_reference: 27

  - id: obj_008_004
    type: feature-gap
    category: w9-1099
    quote: "I see that it's not asking for anything that would be on a W-9. So presumably we would still be responsible for obtaining that info and issuing 1099s to vendors"
    handling: Colton confirmed feature is coming but not currently available
    resolution: Acknowledged as future roadmap item
    line_reference: 83

  - id: obj_008_005
    type: limitation
    category: user-seats
    quote: "If I have access to a client and two other members of my team have access to a client, does that take up three or does that just take up one?"
    handling: Colton explained manager/admin seats count, view-only doesn't
    resolution: Resolved
    line_reference: 133-134

  - id: obj_008_006
    type: feature-gap
    category: selective-sync
    quote: "Can I selectively sync invoices?... I don't want to dump 150 invoices in a Nickel and then have to pick"
    handling: Colton explained no selective sync, recommended manual invoice creation for soft launch
    resolution: Workaround provided
    line_reference: 137-140

  - id: obj_008_007
    type: information-request
    category: banking-partners
    quote: "The last question is who are the underlying banks that you're built on"
    handling: Colton didn't know off-hand, said he'd follow up
    resolution: Pending follow-up
    line_reference: 151-152

personas:
  - id: persona_008_001
    type: accounting-firm-buyer
    firmographics:
      company_type: CPA/bookkeeping/fractional CFO firm
      employee_count: 15
      client_count: 150
      annual_revenue: Above $1M
      services: Bookkeeping, accounting, fractional CFO
    technographics:
      current_tools:
        - Bill.com (for high-volume clients)
        - RAMP
        - Brex
        - Intuit Bill Pay
        - Melio (phasing out)
        - QuickBooks Online Accountant
        - QuickBooks Desktop (for rental properties)
      integration_requirements: QuickBooks Online integration critical
    psychographics:
      sophistication_level: Very high - understands VC funding, series raises, business models
      risk_tolerance: Low - requires sustainability proof
      decision_style: Analytical, thorough due diligence
      innovation_adoption: Pragmatic - will test before full rollout
    buying_signals:
      - Does angel investing, understands startup metrics
      - Requested pitch deck for due diligence
      - Plans to test with rental properties first
      - Wants team member to see demo
      - Interested in soft rollout approach
    job_to_be_done: Enable low-volume clients to make occasional ACH payments without expensive platform fees while ensuring vendor sustainability
    line_reference: 21

  - id: persona_008_002
    type: real-estate-property-owner
    firmographics:
      property_type: Commercial rental properties
      entity_count: 3-4 separate LLCs
      tenant_volume: Low (example given: 2 tenants)
      revenue: Combined comparable to CPA practice (above $1M)
    technographics:
      current_tools:
        - QuickBooks Desktop
      integration_requirements: Minimal - just needs payment processing
    psychographics:
      sophistication_level: High (same person as accounting firm owner)
      use_case_focus: Simple payment collection from tenants
    job_to_be_done: Collect rent electronically from tenants who want landlord to initiate ACH pull
    line_reference: 87, 112-113

use_cases:
  - id: uc_008_001
    category: accounting-firm
    subcategory: client-enablement
    title: Enable low-volume clients to send ACH payments
    description: CPA firm needs to provide ACH payment capability to smaller clients who don't have enough volume to justify Bill.com
    current_state: Smaller clients either pay expensive bank fees ($7 per ACH) or use checks (fraud risk)
    desired_state: Low-volume clients can send ACH payments affordably on as-needed basis
    value_drivers:
      - Eliminate $7 bank fees for clients
      - Reduce check fraud risk
      - Provide electronic payments without platform fee burden
    stakeholders:
      - CPA firm owner
      - CPA firm staff (15 employees)
      - Small business clients (subset of 150 total clients)
    line_reference: 25-37

  - id: uc_008_002
    category: accounting-firm
    subcategory: firm-wide-deployment
    title: Standardize payment platform across 150 clients
    description: Replace multiple payment platforms (Bill.com, RAMP, Brex, Intuit, Melio) with single solution
    current_state: Using 5+ different payment platforms across client base
    desired_state: Single platform that works for both high-volume and low-volume clients
    value_drivers:
      - Operational simplification
      - Consistent client experience
      - Reduced training overhead
      - Better than Bill.com if "pretty slick and good"
    deployment_approach: Soft rollout with loyal customers first, then expand
    line_reference: 23, 37, 135-140

  - id: uc_008_003
    category: real-estate
    subcategory: rent-collection
    title: Collect rent via ACH from commercial tenants
    description: Property owner needs tenants to pay electronically via landlord-initiated ACH pull
    current_state: Tenant willing to pay electronically but needs landlord to initiate the pull
    desired_state: Set up payment authorization and pull rent via ACH automatically
    constraints:
      - Very low volume (2 tenants in example)
      - Not worth $35/month Plus plan
      - Using QuickBooks Desktop (no integration)
    solution_approach: Use Nickel Core free plan with invoice payment links
    line_reference: 87-88

  - id: uc_008_004
    category: accounting-firm
    subcategory: invoice-surcharge-management
    title: Pass credit card fees to clients selectively
    description: Firm needs ability to charge credit card surcharge to customers by default, with option to override per client
    current_state: Not specified, but "such a big need"
    desired_state: Global surcharge rule with per-invoice override capability
    value_drivers:
      - Protect margins on credit card payments
      - Flexibility for special client agreements
      - Automated surcharge calculation and disclosure
    line_reference: 59, 96-98

  - id: uc_008_005
    category: accounting-firm
    subcategory: multi-user-client-access
    title: Manage client accounts with team access controls
    description: Firm needs single login with dropdown to access different client Nickel accounts, plus team member access controls
    current_state: Concerned about needing separate login per client (would be "deal killer")
    desired_state: Firm administrator can invite team members, allocate client-level access
    access_levels_needed:
      - View-only (unlimited, no seat cost)
      - Manager/Admin (limited seats, active users)
    line_reference: 125-134

  - id: uc_008_006
    category: accounting-firm
    subcategory: pilot-deployment
    title: Test Nickel with subset of clients before full rollout
    description: Want to pilot with select clients without syncing all 150 clients' invoices
    current_state: Would generate 150 invoices/month if full QuickBooks sync enabled
    desired_state: Selectively sync 10 clients for pilot
    gap_identified: Cannot currently do selective sync - must manually create invoices in Nickel for pilot
    workaround: Generate invoices in Nickel manually, attach QuickBooks PDFs
    line_reference: 137-140

  - id: uc_008_007
    category: accounting-firm
    subcategory: change-management
    title: Transition clients from checks to electronic payments
    description: CPA advising clients to "stop writing paper checks" due to check washing fraud
    current_state: Successfully transitioning clients with enough volume for Bill.com
    desired_state: Electronic payments for all clients regardless of volume
    adoption_notes: "Been pleasantly surprised actually. I expected it was gonna be much more difficult than it has been"
    line_reference: 33-36

key_insights:
  business_model_validation:
    - Hardy is sophisticated buyer who does angel investing
    - Specifically concerned about sustainability of free models
    - Requested pitch deck to validate business model
    - Wants to see Series A fundraising plans
    - Noted Melio went from free to paid, creating trust issues with "free" platforms

  persona_sophistication:
    - CPA firm owner with deep financial expertise
    - Manages 150 clients across diverse industries
    - Operates own rental properties (3-4 entities)
    - Does angel investing, understands VC funding
    - Very analytical, thorough due diligence process

  buying_process:
    - Plans to test with rental properties first (low-risk)
    - Will involve team member in evaluation
    - Wants soft rollout with loyal customers
    - Requires proof of sustainability before commitment
    - Multiple validation checkpoints before full deployment

  competitive_context:
    - Currently uses Bill.com for high-volume clients
    - Melio lost trust by eliminating free tier
    - Willing to consider Nickel even for high-volume clients if "pretty slick and good"
    - Banking with Brex, RAMP for corporate cards
    - QuickBooks Online Accountant for most clients

  feature_gaps_identified:
    - W-9/1099 functionality (acknowledged as coming)
    - Selective QuickBooks sync (workaround provided)
    - Payment authorization only on Plus plan (but needed for some use cases)
    - Separate accounts required per entity (not consolidated view)

  pricing_sensitivity:
    - Willing to pay reasonable ACH fees
    - Not willing to pay platform fees for low-volume use
    - $35/month Plus plan not worth it for 2-tenant property
    - Free tier critical for pilot/testing and low-volume entities

  security_concerns:
    - Check washing fraud is major driver
    - Wants to be "diligent partner" to clients
    - Needs to validate banking partners
    - Concerned about vendor longevity and sustainability

deal_signals:
  positive:
    - "I like what I've seen. It looks good"
    - Plans to set up test case for rental properties
    - Requested team member see demo
    - Open to using for firm invoicing as test case
    - Willing to consider replacing Bill.com for high-volume clients
    - Successfully transitions clients to electronic payments already

  concerns:
    - Needs pitch deck for validation
    - Wants to know underlying banking partners
    - Concerned about business sustainability
    - Multiple feature gaps identified
    - Requires team member buy-in
    - Needs selective sync for pilot (not available)

  next_steps:
    - Hardy will test with rental property entity
    - Colton to send pitch deck request to founders
    - Colton to send recorded demo for team member
    - Colton to follow up with banking partner information
    - Team member may schedule separate demo call

competitive_intelligence:
  bill_com:
    - Used for high-volume clients
    - Works well but expensive for small clients
    - Hardy open to replacing if Nickel is comparable
    - Successfully getting clients to adopt electronic payments through Bill.com

  melio:
    - Previously used when free
    - "Gotten less desirable" after pricing changes
    - Lost trust by switching from free to paid
    - Created market opportunity for Nickel

  intuit_bill_pay:
    - Currently using for some clients
    - No specific feedback provided

  ramp_brex:
    - Used for corporate cards
    - Different use case than Nickel

  banks:
    - Charging $7 per ACH
    - Prohibitively expensive for low-volume needs
    - No digital workflow advantages

questions_for_product:
  - Can selective QuickBooks sync be added for accounting firms doing pilots?
  - What's timeline for W-9/1099 functionality?
  - Could accounting firms get consolidated multi-entity view?
  - Is there a path to payment authorization on free tier for very low volume?

questions_for_sales:
  - How to handle sophisticated buyers requesting pitch decks?
  - What materials exist to validate business model sustainability?
  - How to position against "free to paid" history of Melio?
  - What's the standard soft rollout process for accounting firms?

transcript_metadata:
  call_quality: High - detailed discussion, thorough Q&A
  buyer_engagement: Very high - asked many detailed questions
  demo_completion: Full demo with accounting firm considerations
  technical_depth: High - covered integrations, user management, workflows
  objection_handling: Good - Colton transparent about gaps and roadmap
  closing_attempt: Soft - focused on next steps and testing
