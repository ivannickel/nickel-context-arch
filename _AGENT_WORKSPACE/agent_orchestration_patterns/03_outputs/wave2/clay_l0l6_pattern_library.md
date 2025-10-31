# [Tool] L0-L6 Pattern Library: Layered Research Framework
**Agent 04: L0-L6 Methodology Extractor - Wave 2 Meta-Analysis**

**Generated**: 2025-10-08
**Source**: [Tool] case study 3-agent research pipeline (930-line architecture spec + agent implementations)
**Purpose**: Extract reusable L0-L6 layered research methodology with templates for GTM intelligence gathering
**Context**: Wave 1 foundation (role contracts, attribution framework) → Wave 2 deep pattern extraction

---

## 1. Executive Summary

### The L0-L6 Framework

The [Tool] case study reveals a **7-layer progressive deepening methodology** (L0-L6) for enterprise account intelligence. This framework transforms a company domain into actionable sales strategy through systematic evidence accumulation, where each layer builds on previous findings with explicit dependency chains.

**Core Innovation**: Unlike traditional research methods that gather data in parallel, the L0-L6 framework enforces **sequential layer validation**. You cannot infer GTM motion (L3) without understanding customers (L1). You cannot propose use cases (L5) without identifying bottlenecks (L4). This dependency structure prevents hallucinated insights by grounding every layer in prior verified evidence.

### Architectural Pattern

**Three-Agent Pipeline**:
- **Agent 1A**: Foundation Intelligence (L0-L2) - What they sell, who buys, how customers buy
- **Agent 1B**: GTM Motion Intelligence (L3-L4) - How they acquire customers, where they're bottlenecked
- **Agent 2**: Use Case Synthesis (L5-L6) - What data they need, how to prove value

**Progressive Deepening Logic**:
```
L0 (Product) → L1 (Customer) → L2 (Buying Process)
       ↓              ↓              ↓
       └──────────────┴──────────────┴→ L3 (GTM Motion)
                                              ↓
                                         L4 (Bottleneck)
                                              ↓
                                         L5 (Data Need)
                                              ↓
                                         L6 (Proof Concept)
```

### Evidence Attribution System

Integrated VERIFIED/INFERRED/UNKNOWN taxonomy (from Wave 1 attribution analysis):
- **VERIFIED**: Direct evidence with public confirmation (customer testimonials, exact quotes, job postings)
- **INFERRED**: Logical deduction from verified data with explicit reasoning chain
- **UNKNOWN**: Insufficient data with gap explicitly flagged

This attribution discipline prevents the common failure mode where "inferred" claims drift to "verified" status through repetition.

### Practical Applications

**When to Use L0-L6**:
- Enterprise B2B account research where buying process complexity matters
- Pre-meeting intelligence for high-value prospects (ACV $50K+)
- Building permissionless value concepts that demonstrate product fit
- Training sales teams to think strategically about account context

**When NOT to Use**:
- High-volume SMB prospecting (too slow, insufficient ROI)
- Simple transactional sales (individual buyer, short cycle)
- Existing customers with known context (use account planning frameworks instead)

### Success Metrics

The framework succeeds when:
1. **Differentiation**: Report for Company A looks substantively different from Company B
2. **Actionability**: Sales rep can build permissionless value and craft outreach without additional research
3. **Evidence Quality**: ≥60% of claims are VERIFIED or well-INFERRED with reasoning
4. **Insight Density**: Contains ≥3 non-obvious discoveries beyond surface-level facts
5. **Replicability**: Another researcher using same methodology reaches similar conclusions

---

## 2. Layer Definitions (L0-L6)

### L0: What They Sell

**Question Answered**: What is the core product/service and value proposition?

**Data Sources**:
- Primary: Company website (homepage, product pages, about page)
- Secondary: Product documentation, investor presentations, demo videos
- Tertiary: Review sites (how customers describe the product)

**Analysis Method**:
1. Extract value proposition (exact quote from homepage/product page)
2. Identify product type (SaaS, service, infrastructure, vertical vs horizontal)
3. Assess technology complexity (developer tool vs business user, integration requirements, implementation time)
4. Note differentiation claims (what makes it unique)

**Output Schema**:
```yaml
L0_value_proposition: "One-sentence description [EXACT QUOTE]"
L0_value_prop_source: "URL, accessed DATE"
L0_product_type: "Classification (SaaS, service, etc.)"
L0_technology_complexity: "High | Medium | Low"
L0_complexity_evidence:
  - "Indicator 1 (e.g., requires technical implementation)"
  - "Indicator 2 (e.g., developer-focused documentation)"
  - "Indicator 3 (e.g., integration requirements listed)"
L0_differentiation: "What makes product unique (from positioning)"
```

**Evidence Level Criteria**:
- **VERIFIED**: Exact quote from company website with URL and date
- **INFERRED**: Technology complexity assessment based on documentation depth, integration lists, implementation time mentions
- **UNKNOWN**: Pricing model if not publicly disclosed, implementation timeline if not stated

**Quality Gate**:
- [ ] Value proposition is specific (not generic "we help companies grow")
- [ ] Complexity assessment has ≥3 supporting indicators
- [ ] All claims have source URLs with dates
- [ ] Product type enables Agent 1B to predict required GTM motion

**Handoff to L1**: Product complexity informs what type of customers can adopt it (low complexity → broader market, high complexity → technical buyers)

**Example (Good)**:
```yaml
L0_value_proposition: "Build enriched lead lists 10x faster with waterfall logic and 75+ data providers"
L0_value_prop_source: "https://clay.com/product, accessed 2025-10-07"
L0_product_type: "Horizontal SaaS - Data enrichment platform"
L0_technology_complexity: "Medium"
L0_complexity_evidence:
  - "Requires understanding of data enrichment concepts (waterfall logic)"
  - "Integrates with 75+ providers (technical setup)"
  - "Self-serve product but 'enrichment experts' mentioned (suggests learning curve)"
L0_differentiation: "Waterfall enrichment (multiple providers in sequence), [Tool] tables (visual workflow builder)"
```

**Example (Bad)**:
```yaml
L0_value_proposition: "Data enrichment platform"
L0_value_prop_source: "Website"
L0_product_type: "SaaS"
L0_technology_complexity: "Medium"
```
*Problems: Vague value prop, no URL, no date, no evidence for complexity claim*

---

### L1: Who Their Customer Is

**Question Answered**: What is the customer ICP with verified examples?

**Data Sources**:
- Primary: Customer testimonials, case studies, G2/Capterra verified reviews
- Secondary: Customer logos (if verifiable), LinkedIn profiles of customer companies
- Tertiary: Press releases, conference presentations featuring customers

**Analysis Method**:
1. Find verified customers (public confirmation of relationship)
2. Extract customer characteristics: industry, size, use case, geography
3. Identify patterns (cluster by industry, size range, use case type)
4. Define ICP based on patterns (only claim pattern if ≥3 examples)
5. Flag confidence level based on sample size

**Output Schema**:
```yaml
L1_verified_customers:
  - customer_name: "Company A"
    industry: "B2B SaaS"
    size: "450 employees (LinkedIn, DATE)"
    use_case: "Sales enrichment (from testimonial)"
    evidence_level: "VERIFIED"
    evidence_source: "Case study URL or review URL"

L1_customer_patterns:
  industries:
    - industry: "B2B SaaS"
      count: 5
      examples: ["Company A", "Company B", "Company C", "Company D", "Company E"]
  sizes:
    - range: "100-500 employees"
      count: 7
      examples: ["Company A", "Company F", ...]
  use_cases:
    - use_case: "Sales prospecting/enrichment"
      count: 8
      examples: [...]

L1_customer_icp:
  company_types: ["B2B SaaS", "B2B Services", "Tech-enabled businesses"]
  size_range: "50-500 employees (based on 12 verified examples)"
  industries: ["SaaS", "Professional Services", "FinTech"]
  geographic_focus: "North America primary, EMEA secondary (inferred from HQ locations)"
  confidence: "Medium (N=12 verified customers, patterns clear but sample size limited)"
```

**Evidence Level Criteria**:
- **VERIFIED**: Customer publicly confirms relationship (testimonial with attribution, case study, verified review with badge)
- **CLAIMED**: Company claims customer on website, no public confirmation found
- **INFERRED**: Customer pattern derived from verified examples (e.g., "primarily 100-500 employee companies" based on 8/12 examples in this range)
- **UNKNOWN**: Customer size distribution if only 1-2 examples, geographic patterns if insufficient data

**Quality Gate**:
- [ ] ≥3 verified customers identified OR explicitly flagged as insufficient data
- [ ] Customer patterns have ≥3 examples before claiming as "pattern"
- [ ] ICP definition is specific (not "enterprises" without size range)
- [ ] Evidence levels marked on all customers (VERIFIED/CLAIMED)
- [ ] Confidence level stated with sample size justification

**Handoff to L2**: Customer types inform buying process complexity (50-person startups buy differently than 500-person enterprises)

**Handoff to L3**: Customer ICP validates GTM motion (if customers are all SMB, shouldn't see only enterprise AEs in hiring)

**Example (Good)**:
```yaml
L1_verified_customers: [12 customers with full details...]
L1_customer_patterns:
  industries:
    - industry: "B2B SaaS"
      count: 8
      examples: ["[Tool] user A", "[Tool] user B", ...]
  sizes:
    - range: "50-200 employees"
      count: 7
    - range: "200-500 employees"
      count: 5
L1_customer_icp:
  company_types: ["B2B SaaS companies with sales teams", "Professional services firms with BDR/SDR orgs"]
  size_range: "50-500 employees (7 examples at 50-200, 5 examples at 200-500)"
  industries: ["SaaS (8 examples)", "Professional Services (3 examples)", "FinTech (1 example)"]
  confidence: "Medium (N=12 verified customers, clear B2B SaaS skew but limited services sample)"
```

---

### L2: How Customer Buys

**Question Answered**: What is the buying committee structure and decision process?

**Data Sources**:
- Primary: G2/Capterra reviews (buyers describe process), testimonials (who is quoted)
- Secondary: Case studies (who is featured), product positioning (target persona)
- Tertiary: Review comments about evaluation process, implementation timeline

**Analysis Method**:
1. Identify buying committee roles (from testimonials: who is quoted? from reviews: what roles write reviews?)
2. Classify involvement type: Economic Buyer, Technical Evaluator, End User, Champion
3. Infer sales cycle length (product complexity L0 + customer size L1 + direct evidence from reviews)
4. Extract evaluation criteria (from reviews: "We chose X because...")
5. Understand decision structure: Individual, Departmental, Committee, Enterprise Procurement

**Output Schema**:
```yaml
L2_buying_committee:
  - role: "VP Sales"
    involvement: "Economic Buyer"
    evidence: "Quoted in 3 testimonials, mentioned in 5 G2 reviews as final approver"
    source: "G2 reviews, company testimonials"
  - role: "Sales Operations Manager"
    involvement: "Technical Evaluator / End User"
    evidence: "8 G2 reviews written by Sales Ops role, mention 'built workflows'"
    source: "G2 verified purchaser reviews"
  - role: "SDR/BDR"
    involvement: "End User"
    evidence: "Testimonials mention 'our SDR team uses daily'"
    source: "Customer testimonials"

L2_sales_cycle_estimate: "1-3 months"
L2_cycle_confidence: "Medium"
L2_cycle_reasoning: "Product complexity (Medium from L0) + customer size (50-500 from L1) suggests 1-3 month cycles for SMB/Mid-market. Enterprise deals (if any) likely longer but insufficient data."
L2_cycle_direct_evidence: "One G2 review mentions '6 weeks to evaluate and implement' (2025-09-15)"

L2_evaluation_criteria:
  - criterion: "Ease of use / learning curve"
    evidence: "Mentioned in 12/20 G2 reviews as key factor"
    source: "G2 reviews (multiple)"
  - criterion: "Data coverage (number of providers)"
    evidence: "5 reviews mention 'has all the data sources we need'"
    source: "G2 reviews"
  - criterion: "Pricing / ROI vs alternatives"
    evidence: "8 reviews compare to ZoomInfo cost"
    source: "G2 reviews"

L2_decision_structure: "Departmental (Sales leadership approves, Ops implements)"
L2_decision_evidence: "Reviews indicate VP Sales approval needed, but not C-level procurement process"
```

**Evidence Level Criteria**:
- **VERIFIED**: Stakeholder mentioned in testimonial or review with attribution
- **INFERRED**: Sales cycle estimate based on L0 complexity + L1 size (with reasoning)
- **INFERRED**: Decision structure based on stakeholder seniority and review patterns
- **UNKNOWN**: Exact cycle length if no reviews mention timeline, procurement process details if not stated

**Quality Gate**:
- [ ] ≥2 buying committee roles identified with evidence sources
- [ ] Sales cycle estimate has reasoning (not just a guess)
- [ ] Evaluation criteria extracted from ≥3 reviews or testimonials
- [ ] Decision structure inference is based on stakeholder evidence
- [ ] All INFERRED claims have explicit reasoning documented

**Handoff to L3**: Buying process complexity must match GTM team structure (committee buying requires ops support, individual buying can be self-serve)

**Example (Good)**:
```yaml
L2_buying_committee:
  - role: "VP Sales / Head of Sales"
    involvement: "Economic Buyer"
    evidence: "Quoted in 3 case studies as decision maker, 5 G2 reviews mention 'VP Sales approved purchase'"
    source: "[Tool] case studies, G2 reviews"
  - role: "Sales Operations Manager"
    involvement: "Technical Evaluator / Primary User"
    evidence: "10 G2 reviews written by Sales Ops roles, testimonials mention 'Ops team built workflows'"
    source: "G2 verified reviews, testimonials"

L2_sales_cycle_estimate: "1-3 months (SMB/Mid-market), potentially 3-6 months (Enterprise)"
L2_cycle_confidence: "Medium"
L2_cycle_reasoning: "Product complexity Medium (L0) + customer size 50-500 (L1) + self-serve tier available suggests shorter cycles. Enterprise deals likely longer given committee structure."
L2_cycle_direct_evidence: "One review: 'Took 6 weeks from trial to purchase' (G2, 2025-09-15)"

L2_decision_structure: "Departmental (Sales leadership approval, no formal procurement)"
L2_decision_evidence: "Stakeholders are VP Sales / Ops level (not C-suite), reviews mention 'quick approval process'"
```

---

### L3: How They Acquire Customers

**Question Answered**: What is the GTM motion, team structure, and channel mix?

**Data Sources**:
- Primary: Job postings (LinkedIn, company careers page), LinkedIn org structure (team sizes)
- Tertiary: LinkedIn activity (what leaders post about), funding announcements

**Analysis Method**:
1. **GTM Motion Classification** - Analyze job postings for role patterns:
   - PLG indicators: Growth Engineer, Product Manager (Growth), self-serve mentions
   - Enterprise indicators: Enterprise AE, Strategic Account Manager, "Enterprise" in titles
   - SMB/Mid-market indicators: SDR, BDR, Inside Sales
   - Partner-led indicators: Channel Manager, Partner Manager, Alliance roles
   - Hybrid indicators: Both PLG and Enterprise roles present
2. **Cross-validate with L0-L2**:
   - Self-serve product (L0) + Individual buyers (L2) → PLG motion
   - Complex product (L0) + Committee buying (L2) → Enterprise motion
3. **Team Structure Analysis** - Count roles from LinkedIn by function (Sales, Marketing, Ops, CS)
4. **Channel Mix** - Identify from job descriptions (outbound, inbound, partner, PLG mentions)
5. **Tech Stack** - Extract from HG Insights, job posting tool requirements, website integration pages
6. **Geographic Coverage** - Job locations vs customer distribution (L1)

**Output Schema**:
```yaml
L3_gtm_motion_type: "Hybrid: PLG → Enterprise"
L3_gtm_motion_evidence:
  - "Self-serve product tier on website (PLG signal)"
  - "10 Growth Engineer roles posted (LinkedIn, last 60 days) - PLG motion"
  - "8 Enterprise AE roles posted (LinkedIn, last 90 days) - Enterprise layer"
  - "Job descriptions mention 'upgrade self-serve users to enterprise' - Hybrid confirmation"
L3_cross_validation:
  L0_product: "Medium complexity (can be self-serve with support) → Supports hybrid motion"
  L1_customer: "Mix of 50-200 (PLG fit) and 200-500 (Enterprise fit) → Supports hybrid"
  L2_buying: "Departmental decision (not C-suite) → Supports mid-market/growth stage motion"
  consistency: "MATCH - L3 signals align with L0-L2 context"

L3_team_structure:
  sales_model: "Hybrid: Growth-led + SDR→AE layer"
  team_sizes:
    sales: "42 employees (LinkedIn, 2025-10-07)"
    marketing: "28 employees"
    sales_ops: "6 employees"
    customer_success: "15 employees"
  source: "LinkedIn company page, accessed 2025-10-07"
  inference: "Ops team present (6 people) suggests process sophistication to support sales. CS team (15) indicates retention/expansion focus."

L3_channel_mix:
  primary: "PLG (self-serve trial) + Outbound (SDR/BDR for upgrade path)"
  secondary: "Inbound (content marketing, evident from blog activity)"
  evidence:
    - "8 SDR roles posted mention 'outbound prospecting'"
    - "Website has self-serve trial (PLG channel)"
    - "Marketing team (28 people) suggests inbound content strategy"

L3_tech_stack_gtm:
  - tool: "Salesforce"
    category: "CRM"
    source: "HG Insights via [Tool], 2025-10-07"
  - tool: "Outreach"
    category: "Sales Engagement"
    source: "Job posting requirement (SDR role)"
  - tool: "ZoomInfo"
    category: "Enrichment"
    source: "HG Insights via [Tool]"
  stack_sophistication: "Intermediate (standard CRM + engagement + enrichment)"
  gaps_observed: "No advanced ops tools visible despite 6-person ops team - may indicate manual processes or internal tooling"

L3_geographic_coverage:
  regions: ["North America (primary)", "EMEA (expansion)"]
  evidence:
    - "Job locations: 35 roles in US, 8 in UK/Germany"
    - "Customer distribution (L1): 80% North America, 15% EMEA"
  inference: "Stable North America coverage, early EMEA expansion (hiring matches customer growth)"
```

**Evidence Level Criteria**:
- **VERIFIED**: Job postings with counts and dates, LinkedIn team sizes with access date, HG Insights tool detection
- **INFERRED**: GTM motion classification (based on role patterns + L0-L2 validation), channel mix (based on team structure + website indicators)
- **UNKNOWN**: Exact sales/marketing split if LinkedIn data unclear, tech stack completeness (HG Insights may miss tools)

**Quality Gate**:
- [ ] GTM motion classification has ≥2 supporting signals with sources
- [ ] Cross-validated with L0-L2 (no contradictions between buying process and team structure)
- [ ] Team sizes have source and date (LinkedIn URL, access date)
- [ ] Tech stack has sources (HG Insights URL, job post URL, etc.)
- [ ] Channel mix is evidenced (not assumed)

**Handoff to L4**: Team structure gaps + hiring patterns → bottleneck signals

**Validation Check**: "If customers buy via committee (L2) but no ops roles exist (L3), this is a red flag suggesting velocity/quality bottleneck"

---

### L4: Where They're Bottlenecked

**Question Answered**: What is the primary GTM constraint limiting growth?

**Data Sources**:
- Primary: Job postings (hiring velocity, role types, pain points mentioned in JDs)
- Secondary: LinkedIn leadership changes (new CRO, VP Sales = strategy shift), tech stack gaps (L3)
- Tertiary: Company blog posts about challenges, funding announcements (expansion signals)

**Analysis Method**:
1. **Hiring Signal Analysis** - Count roles by type and timing:
   - ≥5 similar roles in last 30 days → Rapid scaling (bottleneck indicator)
   - ≥3 similar roles in last 90 days → Steady hiring
   - New Ops roles → Process bottleneck
   - New Enterprise AEs → Upmarket expansion bottleneck
2. **Role Description Analysis** - Read 3-5 JDs for pain points:
   - "Fix manual process" → Process bottleneck
   - "Build systems to scale" → Infrastructure bottleneck
   - "Expand to new markets" → Market expansion bottleneck
   - "Improve data quality" → Data/enrichment bottleneck
3. **Leadership Signals** - New CRO, VP Sales, Head of Ops in last 6 months = strategy shift
4. **Tech Stack Gap Analysis** - Compare actual stack (L3) to expected for motion type:
   - Enterprise motion needs: CRM + Sales Engagement + Enrichment + Ops tools
   - PLG motion needs: Product analytics + Activation tools
   - High-volume SDR needs: Enrichment + Sequencing + Dialers
5. **Cross-validation with L0-L2** - Internal consistency check:
   - If customers buy via committee (L2) but no ops roles (L3) → Velocity bottleneck
   - If customer size growing (L1 pattern) but same team structure (L3) → Quality bottleneck
   - If enterprise AEs hiring but SMB tool stack (L3) → Upmarket expansion bottleneck

**Bottleneck Taxonomy**:
- **Volume**: Need more pipeline, scaling outbound, top-of-funnel constraint
- **Quality**: Wrong targets, low conversion rates, ICP drift
- **Velocity**: Deals stuck, long cycles, need better intel or process support
- **Expansion**: New markets, new products, new segments, need new capabilities/data

**Output Schema**:
```yaml
L4_bottleneck_hypothesis:
  type: "Upmarket Expansion"
  confidence: "High"

L4_evidence:
  hiring_signals:
    - "10 Enterprise AE roles posted in last 30 days (LinkedIn Jobs, 2025-10-07)"
    - "2 Enterprise Sales Engineer roles (last 45 days)"
    - "1 VP Enterprise Sales role (posted 2025-09-15)"
    interpretation: "Rapid enterprise hiring suggests upmarket push"

  job_description_signals:
    - role: "Enterprise AE"
      quote: "Sell to Fortune 500 accounts, navigate complex procurement"
      inference: "Targeting larger accounts than historical ICP (L1 shows 50-500 employees)"
      source: "LinkedIn job post URL"
    - role: "Enterprise Sales Engineer"
      quote: "Build custom integrations for enterprise customers"
      inference: "Product needs enterprise features (complexity upgrade from L0)"
      source: "LinkedIn job post URL"

  tech_stack_signals:
    gap: "No enterprise ABM tools visible (e.g., 6sense, Demandbase)"
    current_stack: "ZoomInfo (L3) - good for SMB, weak on enterprise org mapping"
    inference: "Lack of enterprise intelligence tools creates bottleneck for complex accounts"

  leadership_signals:
    - role: "VP Enterprise Sales"
      name: "John Doe"
      joined: "2025-08-01"
      background: "Previous: Enterprise Sales at Salesforce (LinkedIn profile)"
      inference: "Enterprise sales leader hire confirms upmarket strategy"

L4_cross_validation:
  expected_from_L0_L2: "Customers buy via departmental decision (L2), product is medium complexity (L0) → Should support mid-market well"
  actual_from_L3: "Team structure optimized for 50-500 employees (current customer range L1)"
  gap_analysis: "Hiring 10 Enterprise AEs but current customers are 50-500 employees (L1) → Clear upmarket expansion signal"
  validated_bottleneck: "Upmarket Expansion - need enterprise ICP identification, enterprise org mapping, decision-maker enrichment"

L4_alternative_hypotheses:
  - hypothesis: "Volume bottleneck (need more pipeline)"
    evidence: "Marketing team is 28 people (L3), only 2 SDR roles posted"
    assessment: "REJECTED - Low SDR hiring suggests volume is not primary constraint"
  - hypothesis: "Velocity bottleneck (deals stuck)"
    evidence: "Ops team exists (6 people L3), standard tech stack (L3)"
    assessment: "REJECTED - Ops infrastructure present, no pain points in JDs about stuck deals"
```

**Evidence Level Criteria**:
- **VERIFIED**: Job posting counts with dates, specific role quotes from JDs, LinkedIn leadership profiles
- **INFERRED**: Bottleneck type (based on hiring pattern + JD analysis + cross-validation), tech stack gaps (comparing expected vs actual)
- **UNKNOWN**: Exact expansion timeline if not stated, specific pain point severity without discovery calls

**Quality Gate**:
- [ ] Bottleneck hypothesis is specific (not vague "need more leads")
- [ ] ≥3 evidence categories support hypothesis (hiring + JDs + tech stack OR leadership)
- [ ] Cross-validated with L0-L2 (internal consistency demonstrated)
- [ ] Alternative hypotheses considered and assessed
- [ ] All hiring signals have counts, dates, role types

**Handoff to L5**: Bottleneck type determines data need (Upmarket expansion → enterprise ICP identification + org mapping)

**Validation Check**: "Does L3 GTM motion support this bottleneck? If motion is PLG but bottleneck is enterprise expansion, this is a strategic shift (flag as TRANSITION)"

---

### L5: What Data They Need

**Question Answered**: What specific data problem must be solved to unblock the bottleneck?

**Data Sources**:
- This is **synthesis layer** - no new research, only reasoning from L0-L4
- Primary inputs: L4 bottleneck, L1 customer ICP, L3 GTM motion, L2 buying process

**Synthesis Logic**:
```
Bottleneck (L4) → Data Problem
+ Customer ICP (L1) → Targeting Requirements
+ GTM Motion (L3) → Enrichment Requirements
+ Buying Process (L2) → Intelligence Requirements
+ Current Tech Stack (L3) → Gap Analysis
────────────────────────────────────────
= Specific Data Need (L5)
```

**Synthesis Patterns by Bottleneck Type**:

**If L4 = Volume Bottleneck**:
- Data Need: List building at scale, prospect identification, automated enrichment
- Use L1 ICP to define "who to find more of"
- Use L3 motion to determine enrichment depth (PLG = basic, Enterprise = deep)

**If L4 = Quality Bottleneck**:
- Data Need: Better targeting criteria, ICP filtering, signal-based prioritization
- Use L1 patterns to define "what predicts good fit"
- Use L2 to identify "what signals indicate buying readiness"

**If L4 = Velocity Bottleneck**:
- Data Need: Account intelligence, org mapping, buying committee enrichment
- Use L2 to identify "who are all stakeholders"
- Use L3 to determine "what intel accelerates deals in this motion"

**If L4 = Expansion Bottleneck** (most common in [Tool] case):
- Data Need: New ICP discovery, market mapping, custom signal detection
- Use L1 to extrapolate "what does next ICP tier look like"
- Use L3 tech stack to identify "what data current tools lack for new segment"

**Output Schema**:
```yaml
L5_data_need_hypothesis: "Enterprise ICP identification and decision-maker enrichment to support upmarket expansion"

L5_derivation_logic:
  from_L4_bottleneck: "Upmarket Expansion - hiring 10 Enterprise AEs, need to target Fortune 500"
  from_L1_customer_icp: "Current customers are 50-500 employees → New ICP is 500-5000 employees"
  from_L2_buying_process: "Current buying is departmental (VP Sales) → Enterprise buying involves C-suite + procurement"
  from_L3_gtm_motion: "Hybrid PLG→Enterprise motion → Need data for both upgrade path (existing users) and new logo acquisition"
  from_L3_tech_stack: "ZoomInfo provides basic firmographics but weak on enterprise org depth and tech stack signals"
  synthesized_need: "Must identify 500-5000 employee companies matching product fit, enrich with C-level contacts, map org structure for complex sales, track expansion signals (funding, hiring, tech stack changes)"

L5_clay_use_case: "Enterprise Account Intelligence Workflow"
L5_use_case_description: |
  Build [Tool] workflow to:
  1. Identify companies matching new enterprise ICP (500-5000 employees, existing product fit signals)
  2. Enrich with decision-maker contacts (CRO, VP Sales, Head of RevOps - from L2 enterprise buying committee)
  3. Add org depth (map sales leadership structure for multi-threading)
  4. Include tech stack signals (install base data to prove product fit)
  5. Track expansion signals (funding rounds, hiring velocity in sales roles, technology changes)
  6. Push to Salesforce with enriched data for Enterprise AE team

L5_how_clay_solves_bottleneck:
  bottleneck: "Upmarket Expansion - lack of enterprise target identification"
  clay_provides: "Waterfall enrichment with 75+ providers enables comprehensive enterprise account intelligence that ZoomInfo (L3 current tool) cannot provide"
  specific_advantages:
    - "HG Insights integration for tech stack detection (product fit signals)"
    - "Org mapping capabilities for buying committee identification (needed for L2 enterprise buying process)"
    - "Custom signal detection (hiring, funding) for prioritization"
    - "Waterfall logic ensures contact coverage even for hard-to-reach enterprise accounts"
  impact: "Enterprise AEs get pre-qualified, enriched accounts with multi-threading contacts and product fit validation - dramatically reduces prospecting time and improves conversion"

L5_current_state_comparison:
  likely_current_approach: "ZoomInfo for firmographic filtering + manual LinkedIn research for contacts"
  current_limitations:
    - limitation: "ZoomInfo weak on tech stack detection"
      impact: "Cannot identify product fit signals (e.g., 'uses Salesforce + Outreach + no enrichment tool')"
      clay_solution: "HG Insights via [Tool] provides install base data for 15M+ companies"
    - limitation: "Manual LinkedIn research for org mapping"
      impact: "Time-consuming, incomplete coverage, no systematization"
      clay_solution: "Automated org enrichment + contact waterfall from multiple providers"
    - limitation: "No expansion signal tracking"
      impact: "Cannot prioritize accounts by buying readiness"
      clay_solution: "Custom enrichment for funding rounds, hiring velocity, tech changes"
  clay_advantage_summary: "[Tool] provides enterprise-grade account intelligence at scale (ZoomInfo firmographics + LinkedIn org depth + tech stack signals + expansion tracking) in unified workflow, versus current piecemeal manual approach"

L5_sophistication_match:
  their_capability_L3: "6-person Ops team, intermediate tech stack, hybrid GTM motion"
  clay_use_case_complexity: "Intermediate - not beginner (requires understanding enrichment logic) but not advanced (no custom API integrations)"
  why_it_fits: "Ops team (L3) can build and maintain workflow, complexity matches their technical sophistication (medium product complexity L0), directly supports Enterprise AE team (new hires from L4)"
```

**Evidence Level Criteria**:
- **INFERRED** (all of L5 is synthesis): Data need hypothesis is logical deduction from L0-L4 with explicit reasoning chain
- Confidence depends on L0-L4 evidence quality (if L4 bottleneck is Low confidence, L5 data need inherits that uncertainty)

**Quality Gate**:
- [ ] Data need directly solves L4 bottleneck (clear logical connection)
- [ ] Use case leverages L1 ICP (not generic, specific to their customers)
- [ ] Comparison references L3 tech stack (shows advantage over current tools)
- [ ] Sophistication matches L3 capability (not too simple or complex)
- [ ] All synthesis logic is explicit (can trace L5 back through L4→L3→L2→L1)

**Handoff to L6**: Data need becomes permissionless value concept (show them the data they need)

---

### L6: How to Prove It

**Question Answered**: What concrete proof concept can demonstrate value before purchase?

**Data Sources**:
- This is **execution design layer** - creates deliverable spec from L5
- Primary inputs: L5 data need, L1 customer ICP (for relevance), L2 buying committee (for stakeholder strategy)

**Design Principles**:
1. **Use Their Actual ICP** - Don't build generic "company enrichment", build "{THEIR_ICP} enrichment"
2. **Show Unique Data** - Must demonstrate data they can't get from current tools (L3)
3. **Make It Actionable** - They can immediately use this data (not theoretical)
4. **Prove Differentiation** - Explicitly compare to current approach (L3 tech stack)

**Output Schema**:
```yaml
L6_permissionless_value_concept:
  what_to_build: "Enterprise SaaS Companies (500-5000 employees) - Decision-Maker Intelligence Table"

  build_instructions:
    table_name: "Enterprise Expansion Targets for {COMPANY_NAME}"
    input_data: "Start with companies in B2B SaaS, 500-5000 employees, North America"
    enrichment_steps:
      - step: 1
        action: "Firmographic enrichment"
        provider: "Clearbit"
        fields: ["Employee count", "Revenue estimate", "Funding stage", "HQ location"]
      - step: 2
        action: "Tech stack detection"
        provider: "HG Insights"
        fields: ["CRM tool", "Sales engagement tool", "Current enrichment tool", "Install date"]
        purpose: "Product fit validation (identify companies using Salesforce + Outreach but lacking modern enrichment)"
      - step: 3
        action: "Decision-maker enrichment (waterfall)"
        providers: ["Apollo", "ZoomInfo", "ContactOut (fallback)"]
        fields: ["CRO", "VP Sales", "Head of Revenue Operations"]
        purpose: "Buying committee contacts (from L2 enterprise buying process)"
      - step: 4
        action: "Org depth mapping"
        provider: "LinkedIn via [Tool]"
        fields: ["Sales team size", "Sales leadership structure", "Recent sales hires"]
        purpose: "Multi-threading opportunities and expansion signals"
      - step: 5
        action: "Expansion signals"
        provider: "Crunchbase + LinkedIn"
        fields: ["Recent funding rounds", "Hiring velocity (sales roles)", "Tech stack changes"]
        purpose: "Prioritization based on buying readiness"
    output: "50-100 enterprise companies with complete decision-maker contacts, tech stack fit validation, and expansion signal scoring"

  data_to_show:
    example_record:
      company: "Acme Corp (example enterprise SaaS, 1200 employees)"
      firmographics: "B2B SaaS, $50M revenue, Series C, San Francisco"
      tech_stack_fit: "Uses Salesforce + Outreach + ZoomInfo (product fit confirmed)"
      decision_makers:
        - "Jane Smith, CRO (jane.smith@acme.com, LinkedIn profile)"
        - "Bob Johnson, VP Sales (bob.j@acme.com)"
        - "Sarah Lee, Head of RevOps (s.lee@acme.com)"
      org_depth: "45-person sales team (LinkedIn), hired 8 Enterprise AEs in last 90 days"
      expansion_signals: "Series C funding $30M (6 months ago), hiring 12 sales roles (high urgency)"
      prioritization_score: "85/100 (high fit + high urgency)"

    total_records: "100 companies matching enterprise ICP"
    unique_data_points:
      - "Tech stack fit validation (HG Insights) - ZoomInfo from L3 lacks this"
      - "Expansion signal scoring (funding + hiring) - not available in current approach"
      - "Complete org mapping with multi-threading contacts - manual in current process"

  differentiation:
    vs_zoominfo: |
      ZoomInfo (current tool from L3) provides:
      - Basic firmographics ✓
      - Contact data (limited depth at enterprise) ✓
      - No tech stack detection ✗
      - No org structure mapping ✗
      - No expansion signals ✗

      [Tool] provides all of the above PLUS:
      - Tech stack detection via HG Insights (product fit validation)
      - Org depth via LinkedIn enrichment (multi-threading capability)
      - Expansion signals via Crunchbase + LinkedIn (prioritization)
      - Waterfall enrichment (higher contact coverage for hard-to-reach enterprise accounts)

    vs_current_manual_process: |
      Current approach (inferred from L3): "ZoomInfo firmographic filter → Manual LinkedIn research for contacts → No systematic expansion tracking"
      Time per account: ~30-45 minutes manual research per enterprise account
      Coverage: Incomplete (misses contacts, no tech stack validation, subjective prioritization)

      [Tool] approach: "Automated workflow provides complete account intelligence in 5-10 minutes per account"
      Time savings: 20-35 minutes per account × 100 accounts = 33-58 hours saved
      Coverage: Systematic (complete decision-maker enrichment, tech stack validation, objective signal scoring)

  actionability:
    immediate_use: "Enterprise AE team (10 new hires from L4) can immediately use this data for outbound prospecting"
    specific_actions:
      - "Prioritize accounts by expansion signal score (call high-urgency accounts first)"
      - "Multi-thread to CRO + VP Sales + RevOps using enriched contacts"
      - "Personalize outreach with tech stack fit ('We see you use Salesforce + Outreach + ZoomInfo, here's why companies like you are switching...')"
    roi_estimate: "If 33-58 hours saved × $100/hour (loaded Enterprise AE cost) = $3,300-$5,800 value for 100-account research. [Tool] cost for this workflow: ~$500-800/month → 4-7x ROI on research efficiency alone, before accounting for conversion improvements."

L6_stakeholder_strategy:
  end_users:
    - role: "Enterprise AE (10 new hires from L4)"
      count: 10
      uses_clay_for: "Access pre-qualified, enriched enterprise accounts with multi-threading contacts"
      value: "Reduces prospecting time from 30-45 min to 5-10 min per account, increases multi-threading success with complete org maps"
    - role: "Sales Operations (6-person team from L3)"
      count: 6
      uses_clay_for: "Build and maintain enterprise enrichment workflow, push data to Salesforce"
      value: "Systematizes account research (no more manual LinkedIn lookups), enables enterprise AE team to scale"

  economic_buyer:
    role: "VP Enterprise Sales (new hire from L4) OR VP Sales (from L2 buying committee)"
    why_them: "VP Enterprise Sales owns enterprise expansion initiative (L4), OR VP Sales owns overall sales tools budget (L2)"
    cares_about: "Enterprise AE productivity (ramp time, pipeline generation), upmarket expansion success metrics (enterprise deal count, ASP increase)"
    roi_pitch: "[Tool] enables 10 Enterprise AEs to prospect 10x faster with better data, supporting upmarket expansion goal. $800/month investment vs $3,300-5,800/month time savings + improved conversion from better targeting."

  champion_candidates:
    - role: "Sales Operations Manager"
      pain: "Currently doing manual LinkedIn research to support Enterprise AEs (L4 bottleneck creates ops burden)"
      motivation: "Would advocate because [Tool] eliminates manual work, systematizes process, makes ops team more strategic"
      evidence: "6-person ops team (L3) suggests process ownership, bottleneck (L4) creates urgency for ops improvement"

  organizational_path:
    first_contact: "Sales Operations Manager (or Head of Sales Ops if team has leadership)"
    why_first:
      - "Closest to pain: Manual research burden created by enterprise expansion (L4)"
      - "Most likely to engage: Ops teams love automation and systematization"
      - "Can provide intelligence: Knows current process limitations, can validate L3 tech stack, can intro to VP Sales/Enterprise"
    initial_message: |
      "We see you're expanding into enterprise accounts (10 Enterprise AE hires in last 30 days). We built you a table of 100 enterprise SaaS companies (500-5000 employees) with:
      - Decision-maker contacts (CRO, VP Sales, RevOps - waterfall enriched)
      - Tech stack fit validation (companies using Salesforce + Outreach + ZoomInfo)
      - Expansion signals (funding, hiring velocity)

      This normally takes 30-45 min per account manually. [Tool] workflow does it in 5-10 min. Want to compare it to what you're doing now?"

    intelligence_to_gather:
      validate_L4: "Ask: 'How are you currently supporting the new Enterprise AE team with account research?' → Confirms upmarket expansion bottleneck"
      validate_L5: "Ask: 'Where do you get enterprise account data now? What's missing from ZoomInfo?' → Confirms data need hypothesis"
      validate_L6: "Ask: 'If you had this enriched data, what would your Enterprise AEs do with it?' → Confirms actionability and value"
      discover_stakeholders: "Ask: 'Who else is involved in tool decisions for the Enterprise team? Who's leading the upmarket expansion initiative?' → Maps path to economic buyer"

    multi_threading_sequence:
      step_1: "Ops Manager → Gather intel, show permissionless value, get feedback"
      step_2: "Use learnings to refine approach for VP Enterprise Sales (or VP Sales)"
      step_3: "Ops Manager champions internally: 'This solves our enterprise research bottleneck, here's the ROI'"
      step_4: "VP Enterprise Sales (or VP Sales) approves based on: AE productivity improvement + upmarket expansion support"

    path_to_decision: "Ops Manager (validate use case) → VP Enterprise Sales (decision maker) → Procurement (if needed for contract) → Decision"
```

**Evidence Level Criteria**:
- **INFERRED** (all of L6 is design): Permissionless value concept is synthesis of L5 data need + L1 ICP + L2/L3 stakeholders
- Quality depends on L0-L5 evidence chain (if L5 data need is well-supported, L6 proof concept is credible)

**Quality Gate**:
- [ ] Permissionless value uses L1 ICP (specific to their customers, not generic)
- [ ] Shows data current tools (L3) lack (explicit differentiation)
- [ ] Stakeholder strategy matches L2 buying committee + L3 team structure
- [ ] Organizational path is specific (names roles, not vague "talk to sales")
- [ ] Intelligence gathering questions validate L0-L6 hypotheses

**Success Test**: "Give this L6 to a [Tool] rep. Can they:
1. Build the permissionless value concept in [Tool]? (actionable)
2. Craft outreach to right stakeholder? (specific)
3. Conduct discovery with intelligent questions? (validates hypotheses)
4. Multi-thread based on org path guidance? (systematic)"

---

## 3. Progressive Deepening Logic

### Dependency Chain Architecture

The L0-L6 framework enforces strict layer dependencies to prevent hallucinated insights:

**Foundation Layers (L0-L2): Verifiable Facts**
```
L0 (Product) → Enables inference about who can use it
    ↓
L1 (Customer) → Validated by L0 (does product match customer sophistication?)
    ↓
L2 (Buying Process) → Validated by L1 (does buying complexity match customer size/type?)
```

**Inference Layers (L3-L4): Evidence-Based Reasoning**
```
L0 + L1 + L2 → L3 (GTM Motion)
Logic: "To sell THIS product (L0) to THESE customers (L1) who buy THIS way (L2), they must use THIS GTM motion (L3)"

Validation Check: Does L3 match L2?
- If customers buy via committee (L2), should see ops support in team structure (L3)
- If customers are SMB (L1), shouldn't see only Enterprise AEs (L3) - would indicate MISMATCH or TRANSITION

L3 (Team Structure + Hiring) → L4 (Bottleneck)
Logic: "Team structure GAPS or rapid HIRING in specific areas indicate CONSTRAINTS"

Cross-Validation with L2: Does bottleneck make sense given buying process?
- If buying process is complex (L2) but no ops support (L3) → Velocity bottleneck confirmed
```

**Synthesis Layers (L5-L6): Actionable Strategy**
```
L4 (Bottleneck) + L1 (Customer ICP) + L3 (GTM Motion) → L5 (Data Need)
Logic: "To solve THIS bottleneck (L4) for THESE customers (L1) in THIS motion (L3), they need THIS data (L5)"

L5 (Data Need) + L1 (ICP for relevance) + L2 (Stakeholders) → L6 (Proof Concept)
Logic: "To prove THIS data need (L5), show data for THEIR ICP (L1) to THESE stakeholders (L2)"
```

### Validation Gates Between Layers

**Gate 1: L0 → L1**
- Question: "Does product complexity (L0) match customer sophistication (L1)?"
- Pass: High-complexity developer tool → technical buyers (engineering teams)
- Fail: High-complexity product → non-technical SMB customers (would need explanation or is misaligned)

**Gate 2: L1 → L2**
- Question: "Does buying process complexity (L2) match customer size/type (L1)?"
- Pass: 500-employee enterprise customers (L1) → committee buying with procurement (L2)
- Fail: 50-employee startups (L1) → enterprise procurement process (L2) - unlikely

**Gate 3: L2 → L3**
- Question: "Does GTM team structure (L3) support buying process (L2)?"
- Pass: Committee buying (L2) → ops team exists to manage complexity (L3)
- Fail: Committee buying (L2) → no ops support (L3) - indicates bottleneck or misalignment

**Gate 4: L3 → L4**
- Question: "Do hiring patterns (L4) address GTM motion needs (L3)?"
- Pass: Hybrid PLG→Enterprise motion (L3) → hiring Enterprise AEs (L4) = expansion
- Fail: Enterprise motion (L3) → hiring only SDRs (L4) - conflicting signals

**Gate 5: L4 → L5**
- Question: "Does data need (L5) solve bottleneck (L4)?"
- Pass: Upmarket expansion bottleneck (L4) → enterprise ICP enrichment (L5) = directly solves
- Fail: Volume bottleneck (L4) → org mapping enrichment (L5) - doesn't address pipeline volume

**Gate 6: L5 → L6**
- Question: "Does permissionless value (L6) demonstrate data need (L5) with their ICP (L1)?"
- Pass: Data need is enterprise enrichment (L5) → show 100 enterprise companies matching their ICP (L1)
- Fail: Data need is enterprise enrichment (L5) → show SMB company list (doesn't match need)

### Common Validation Failures

**Failure 1: L3-L2 Mismatch (Ignoring Buying Process)**
- Scenario: L2 shows committee buying with 4 stakeholders, but L3 shows zero ops roles
- Diagnosis: Either company is understaffed for complexity (velocity bottleneck) OR L2 inference was wrong (need to re-examine buying process evidence)
- Fix: Flag as bottleneck in L4, or revisit L2 with stricter evidence requirements

**Failure 2: L5-L4 Disconnect (Use Case Doesn't Solve Bottleneck)**
- Scenario: L4 shows volume bottleneck (need more pipeline), but L5 proposes org mapping enrichment
- Diagnosis: Synthesis logic broke down - org mapping helps velocity (stuck deals), not volume (pipeline generation)
- Fix: Re-derive L5 from L4 using correct bottleneck type → data need mapping

**Failure 3: L6-L1 Irrelevance (Generic Permissionless Value)**
- Scenario: L1 shows customers are 50-200 employee SaaS companies, but L6 shows enrichment for 10,000+ employee enterprises
- Diagnosis: Permissionless value doesn't match their ICP - won't resonate as relevant
- Fix: Use L1 ICP explicitly in L6 design (show 50-200 employee SaaS companies, not enterprises)

---

## 4. Agent Contracts

### Contract 1: Agent 1A (L0-L2) → Agent 1B (L3-L4)

**Agent 1A MUST Provide**:
```yaml
required_outputs:
  L0_product_complexity: "High | Medium | Low (with ≥3 evidence indicators)"
  L1_customer_icp: "Specific customer types with ≥3 verified examples OR flagged as insufficient"
  L2_buying_committee: "≥2 identified stakeholder roles with evidence sources"
  L2_buying_process: "Individual | Departmental | Committee | Enterprise Procurement (with reasoning)"

quality_requirements:
  minimum_verified_customers: 3  # Or explicit UNKNOWN flag
  minimum_stakeholder_roles: 2    # Or explicit UNKNOWN flag
  evidence_attribution: "All claims must have source URL + date"
  confidence_levels: "VERIFIED/INFERRED/UNKNOWN marked on all claims"
```

**Agent 1B MUST Receive** (to perform its task):
```yaml
critical_dependencies:
  customer_context: "Detailed enough to infer: 'To sell to THESE customers, they need THIS GTM motion'"
  buying_process: "Clear enough to validate: 'GTM team structure should match buying complexity'"

validation_criteria:
  customer_icp_specificity:
    insufficient: "Sell to enterprises" (too vague)
    sufficient: "Sell to B2B SaaS companies, 50-500 employees, primarily North America" (actionable)

  buying_process_clarity:
    insufficient: "Multiple stakeholders involved" (not actionable)
    sufficient: "VP Sales (economic buyer), Sales Ops (technical evaluator), SDRs (end users) - evidence from 8 G2 reviews" (enables L3 validation)
```

**Failure Condition**:
- If Agent 1A provides: "Customers are enterprises" (vague)
- Agent 1B cannot accurately infer GTM motion (enterprise = 100 employees? 10,000 employees? Very different GTM motions)

**Success Example**:
```yaml
Agent_1A_provides:
  L1_customer_icp: "B2B SaaS companies, 50-500 employees, with sales teams (SDR/BDR orgs present)"
  L2_buying_process: "Departmental decision - VP Sales approves (3 testimonials), Sales Ops evaluates/implements (8 G2 reviews), SDRs are end users"

Agent_1B_can_infer:
  L3_gtm_motion: "Given individual dev users (L2) but departmental approval (L2) for 50-500 employee companies (L1), likely PLG → Product-led sales → Mid-market motion. Should see: self-serve tier + upgrade path + mid-market AE team."
  validation: "CHECK: Does hiring data show self-serve + AEs? If yes, hypothesis confirmed. If only Enterprise AEs, flag as transition/upmarket push."
```

### Contract 2: Agent 1B (L3-L4) → Agent 2 (L5-L6)

**Agent 1B MUST Provide**:
```yaml
required_outputs:
  L3_gtm_motion: "Specific classification (PLG | Enterprise | Hybrid | etc.) with ≥2 supporting signals"
  L3_team_structure: "Sales model (SDR→AE | AE-only | etc.), team sizes with sources"
  L3_tech_stack: "GTM tools with sources (HG Insights URL, job post URL, etc.)"
  L4_bottleneck: "Specific type (Volume | Quality | Velocity | Expansion) with evidence"
  L4_bottleneck_confidence: "High | Medium | Low with reasoning"

quality_requirements:
  gtm_motion_evidence: "≥2 signals (job postings + tech stack, OR hiring + website, etc.)"
  bottleneck_specificity:
    insufficient: "Need more pipeline" (too vague)
    sufficient: "Upmarket expansion - 10 Enterprise AE roles posted in 30 days, VP Enterprise Sales hire, tech stack lacks enterprise tools" (specific, evidenced)
  cross_validation: "L3 must be validated against L0-L2 (no contradictions flagged)"
```

**Agent 2 MUST Receive** (to perform its task):
```yaml
critical_dependencies:
  bottleneck_context: "Specific enough to determine: 'THIS bottleneck in THIS motion requires THIS data'"
  gtm_context: "Team structure + tech stack to compare: 'Current tools vs needed tools for bottleneck'"

validation_criteria:
  bottleneck_specificity:
    insufficient: "Scaling challenges" (what kind? volume? quality? velocity?)
    sufficient: "Upmarket expansion - moving from 50-500 employee customers to 500-5000 employee enterprise accounts, lack enterprise ICP identification tools" (clear data need)

  tech_stack_completeness:
    insufficient: "They use ZoomInfo" (need more context)
    sufficient: "They use ZoomInfo (L3) for firmographics, Outreach for engagement, Salesforce as CRM. Lack: enterprise ABM tools, org mapping, tech stack detection" (enables gap analysis)
```

**Failure Condition**:
- If Agent 1B provides: "Bottleneck is scaling challenges" (vague)
- Agent 2 cannot propose specific use case (scaling what? pipeline volume? deal velocity? team headcount?)

**Success Example**:
```yaml
Agent_1B_provides:
  L4_bottleneck: "Upmarket Expansion"
  L4_evidence:
    - "10 Enterprise AE roles posted in last 30 days"
    - "VP Enterprise Sales hired (2025-08-01, from Salesforce enterprise background)"
    - "Current customers 50-500 employees (L1), new hires target Fortune 500 (job descriptions)"
    - "Tech stack is ZoomInfo (L3) - good for SMB/mid-market, weak on enterprise org depth"
  L3_tech_stack:
    - "ZoomInfo (enrichment) - HG Insights, 2025-10-07"
    - "Salesforce (CRM) - HG Insights"
    - "Outreach (engagement) - job posting requirement"
    - "Gaps: No ABM tools, no org mapping, no tech stack detection"

Agent_2_can_synthesize:
  L5_data_need: "Enterprise ICP identification + decision-maker enrichment + org mapping"
  L5_reasoning:
    - "Bottleneck (L4): Upmarket expansion → Need to identify and enrich enterprise accounts"
    - "Customer ICP shift (L1): 50-500 → 500-5000 employees → Need new targeting criteria"
    - "Buying process change (L2): Departmental → C-suite + procurement → Need C-level contacts"
    - "Tech stack gap (L3): ZoomInfo lacks org depth and tech stack signals → [Tool] provides via HG Insights + org enrichment"
  L6_permissionless_value: "Show 100 enterprise SaaS companies (500-5000 employees) with C-level contacts, org maps, tech stack fit validation - data ZoomInfo cannot provide"
```

### Contract 3: Combined L0-L4 → L5-L6 Synthesis

**Agent 2 Synthesis Requirements**:
```yaml
must_synthesize:
  WHO_to_target: "From L1 customer ICP (specific company types, sizes, industries)"
  WHY_they_need_data: "From L4 bottleneck (what constraint requires what data)"
  HOW_they_currently_operate: "From L3 GTM motion + tech stack (baseline to compare against)"
  WHAT_would_solve_it: "L5 [Tool] use case (specific capability + workflow)"
  HOW_to_prove_it: "L6 permissionless value (show data for THEIR ICP to THEIR stakeholders)"

validation_logic:
  evidence_chain: "Can trace L6 use case → L5 data need → L4 bottleneck → L3 motion → L2 buying → L1 customer → L0 product"
  consistency_check: "If told someone L0-L4, would they suggest same L5-L6 use case?"
  actionability_test: "Could a sales rep build L6 permissionless value and execute outreach?"
```

**Failure Condition**:
- If use case doesn't logically flow from L0-L4 context, synthesis is flawed
- Example: L4 bottleneck is "volume" but L5 use case is "org mapping" (org mapping helps velocity, not volume)

**Validation Check Question**:
> "If I told someone the L0-L4 findings (product, customer, buying process, GTM motion, bottleneck), would they independently suggest this same L5-L6 use case?"

If answer is **NO**, the synthesis has made logical leaps not grounded in evidence - must revise L5-L6.

---

## 5. Reusable Templates

### Template: L0 - What They Sell

```markdown
## L0: What They Sell

**Value Proposition**: "{EXACT_QUOTE}"
**Source**: [URL], accessed {DATE}

**Product Type**: {SaaS | Service | Infrastructure | Platform} - {Vertical | Horizontal}

**Technology Complexity**: {High | Medium | Low}
**Evidence**:
- {INDICATOR_1: e.g., "Developer-focused documentation"}
- {INDICATOR_2: e.g., "Requires technical implementation"}
- {INDICATOR_3: e.g., "Complex integration requirements"}

**Differentiation**: {What makes product unique from positioning}
```

**Quality Checklist**:
- [ ] Value prop is exact quote (not paraphrased)
- [ ] Source has URL + date
- [ ] Complexity has ≥3 evidence indicators
- [ ] Product type enables GTM motion prediction

---

### Template: L1 - Who Their Customer Is

```markdown
## L1: Who Their Customer Is

### Verified Customers
| Customer | Industry | Size | Use Case | Evidence | Source |
|----------|----------|------|----------|----------|--------|
| {NAME} | {INDUSTRY} | {SIZE} | {USE_CASE} | VERIFIED | [URL] |
| {NAME} | {INDUSTRY} | {SIZE} | {USE_CASE} | CLAIMED | [URL] |

**Total**: {N} customers ({X} VERIFIED, {Y} CLAIMED, {Z} MENTIONED)

### Customer Patterns
**Industries** (only if ≥3 examples):
- {INDUSTRY_1}: {COUNT} customers - {NAMES}
- {INDUSTRY_2}: {COUNT} customers - {NAMES}

**Sizes** (only if ≥3 examples):
- {SIZE_RANGE_1}: {COUNT} customers - {NAMES}
- {SIZE_RANGE_2}: {COUNT} customers - {NAMES}

### Customer ICP
**Company Types**: {SPECIFIC_TYPES}
**Size Range**: {X-Y employees OR $Z-W revenue} (based on {N} examples)
**Industries**: {INDUSTRY_LIST}
**Geographic Focus**: {REGIONS} (if discernible)
**Confidence**: {High | Medium | Low} - {REASONING}
```

**Quality Checklist**:
- [ ] ≥3 verified customers OR flagged as insufficient
- [ ] Patterns only claimed if ≥3 examples
- [ ] ICP is specific (not "enterprises")
- [ ] Confidence level stated with sample size

---

### Template: L2 - How Customer Buys

```markdown
## L2: How Customer Buys

### Buying Committee
| Role | Involvement | Evidence | Source |
|------|-------------|----------|--------|
| {ROLE} | Economic Buyer | {WHERE_FOUND} | [URL] |
| {ROLE} | Technical Evaluator | {WHERE_FOUND} | [URL] |
| {ROLE} | End User/Champion | {WHERE_FOUND} | [URL] |

### Sales Cycle Estimate
**Length**: {X-Y months}
**Confidence**: {High | Medium | Low}
**Reasoning**:
- Product complexity ({L0_COMPLEXITY}) suggests {CYCLE_LENGTH}
- Customer size ({L1_SIZE}) suggests {CYCLE_LENGTH}
- {DIRECT_EVIDENCE_IF_ANY}

### Evaluation Criteria
1. {CRITERION_1}
   - Evidence: "{QUOTE_FROM_REVIEW}"
   - Source: [URL]
2. {CRITERION_2}
   - Evidence: "{QUOTE}"
   - Source: [URL]

### Decision Structure
**Type**: {Individual | Departmental | Committee | Enterprise Procurement}
**Evidence**: {WHAT_SUGGESTS_THIS}
```

**Quality Checklist**:
- [ ] ≥2 stakeholder roles identified
- [ ] Sales cycle has reasoning (not guessed)
- [ ] Evaluation criteria from ≥3 sources
- [ ] Decision structure inference has evidence

---

### Template: L3 - How They Acquire Customers

```markdown
## L3: How They Acquire Customers

### GTM Motion Classification
**Type**: {PLG | Enterprise | Hybrid | Partner-Led | etc.}

**Evidence**:
1. {SIGNAL_1} - [Source URL], {DATE}
2. {SIGNAL_2} - [Source URL], {DATE}
3. {SIGNAL_3} - [Source URL], {DATE}

**Cross-Validation with L0-L2**:
- L0 (Product): {COMPLEXITY} → Suggests {MOTION_TYPE}
- L1 (Customer): {SIZE/TYPE} → Suggests {MOTION_TYPE}
- L2 (Buying): {PROCESS} → Suggests {MOTION_TYPE}
- L3 (Signals): {MATCH or MISMATCH?}

**Confidence**: {High | Medium | Low} - {REASONING}

### Team Structure
**Sales Model**: {SDR→AE | AE-only | Growth Eng | etc.}

**Team Sizes** (LinkedIn, {DATE}):
- Sales: {X} employees
- Marketing: {Y} employees
- Ops: {Z} employees
- Customer Success: {W} employees

**Source**: [LinkedIn Company Page URL]
**Inference**: {WHAT_THIS_SUGGESTS}

### Tech Stack
| Tool | Category | Source | Date |
|------|----------|--------|------|
| {TOOL} | CRM | HG Insights | {DATE} |
| {TOOL} | Enrichment | Job posting | {DATE} |

**Gaps**: {MISSING_TOOLS_FOR_MOTION_TYPE}
```

**Quality Checklist**:
- [ ] GTM motion has ≥2 supporting signals
- [ ] Cross-validated with L0-L2 (consistency check)
- [ ] Team sizes have source + date
- [ ] Tech stack has sources for each tool

---

### Template: L4 - Where They're Bottlenecked

```markdown
## L4: Where They're Bottlenecked

### Bottleneck Hypothesis
**Type**: {Volume | Quality | Velocity | Expansion}
**Confidence**: {High | Medium | Low}

### Evidence

**Hiring Signals**:
| Role Type | Count | Date Range | Inference |
|-----------|-------|------------|-----------|
| {ROLE} | {X} | {DATES} | {WHAT_THIS_SUGGESTS} |

**Job Description Signals**:
- {ROLE}: "{QUOTE_FROM_JD}" → Suggests {BOTTLENECK_TYPE}
  Source: [Job URL]

**Tech Stack Gaps**:
- Expected for {L3_MOTION}: {EXPECTED_TOOLS}
- Actual: {WHAT_THEY_HAVE}
- Gap: {MISSING_TOOL_TYPE} → Creates {BOTTLENECK_TYPE}

**Leadership Signals**:
- {ROLE}: {NAME} joined {DATE} (from {PREVIOUS_COMPANY})
  Inference: {STRATEGY_SHIFT}

### Cross-Validation with L0-L2
**Expected** (based on L0-L2): {WHAT_TEAM_STRUCTURE_SHOULD_LOOK_LIKE}
**Actual** (from L3): {WHAT_EXISTS}
**Gap**: {MISMATCH} → Suggests {BOTTLENECK_TYPE}

**Validated Bottleneck**: {FINAL_HYPOTHESIS_WITH_CROSS_VALIDATION}
```

**Quality Checklist**:
- [ ] Bottleneck is specific (not "scaling challenges")
- [ ] ≥3 evidence types support hypothesis
- [ ] Cross-validated with L0-L2 (internal consistency)
- [ ] Alternative hypotheses considered
- [ ] Hiring signals have counts + dates

---

### Template: L5 - What Data They Need

```markdown
## L5: What Data They Need

### Data Need Hypothesis
**Problem**: {SPECIFIC_TARGETING_OR_ENRICHMENT_CHALLENGE}

### Derivation Logic
**From L4** (Bottleneck): {BOTTLENECK} → Creates data challenge: {WHAT_DATA_PROBLEM}
**From L1** (Customer ICP): {ICP} → Targeting need: {WHAT_DATA_TO_FIND_THESE}
**From L2** (Buying Process): {PROCESS} → Intel need: {WHAT_DATA_TO_NAVIGATE_BUYING}
**From L3** (GTM Motion): {MOTION} + {TECH_STACK} → Enrichment gap: {WHAT_CURRENT_TOOLS_LACK}

**Synthesized Need**: {SPECIFIC_DATA_REQUIREMENT}


**How It Works**:
1. {STEP_1} - Provider: {PROVIDER} - Output: {WHAT_THIS_PRODUCES}
2. {STEP_2} - Provider: {PROVIDER} - Output: {WHAT_THIS_PRODUCES}
3. {STEP_3} - Provider: {PROVIDER} - Output: {WHAT_THIS_PRODUCES}

**Why This Solves Bottleneck**:
- Bottleneck (L4): {CONSTRAINT}
- Use case provides: {WHAT_DATA_OR_CAPABILITY}
- Impact: {HOW_THIS_UNBLOCKS_GROWTH}

### Current State Comparison
**Likely Current Approach**: {WHAT_THEY_DO_NOW_FROM_L3}
**Limitations**:
1. {GAP_1} - Impact: {BUSINESS_COST} - [Tool] solution: {HOW_CLAY_FIXES}
2. {GAP_2} - Impact: {BUSINESS_COST} - [Tool] solution: {HOW_CLAY_FIXES}

**[Tool] Advantage**: {vs_CURRENT_TOOL}: {SPECIFIC_DIFFERENTIATION}
```

**Quality Checklist**:
- [ ] Data need directly solves L4 bottleneck
- [ ] Use case leverages L1 ICP (not generic)
- [ ] Comparison references L3 tech stack
- [ ] Sophistication matches L3 capability
- [ ] Synthesis logic is explicit (traceable)

---

### Template: L6 - How to Prove It

```markdown
## L6: How to Prove It

### Permissionless Value Concept

**What to Build**: "{USE_CASE} for {COMPANY_NAME}"

**[Tool] Table Instructions**:
1. Create table: "{TABLE_NAME}"
2. Input: {SEED_DATA_SOURCE}
3. Enrichment steps:
   - Step 1: {ENRICHMENT_TYPE} via {PROVIDER} - Fields: {FIELDS}
   - Step 2: {ENRICHMENT_TYPE} via {PROVIDER} - Fields: {FIELDS}
   - Step 3: {ENRICHMENT_TYPE} via {PROVIDER} - Fields: {FIELDS}
4. Output: {X} companies with {DATA_FIELDS}

**Data to Show**:
- {X} companies matching {L1_ICP}
- With: {UNIQUE_DATA_POINTS_CURRENT_TOOLS_LACK}
- Ready for: {ACTION_REP_CAN_TAKE}

**Differentiation**:
- vs Manual Process: Saves {TIME_ESTIMATE} per account

**Actionability**:
- Immediate use: {HOW_REP_USES_THIS_DATA}
- ROI estimate: {TIME_SAVINGS × COST OR CONVERSION_IMPROVEMENT}

### Stakeholder Strategy

**End Users** (Who uses [Tool]):
| Role | Count | Use [Tool] For | Value |
|------|-------|--------------|-------|
| {ROLE} | {X} | {WORKFLOW} | {BENEFIT} |

**Economic Buyer** (Who approves):
- Role: {ROLE_FROM_L2_OR_L3}
- Cares about: {BUSINESS_OUTCOME}
- ROI pitch: {VALUE_PROPOSITION}

**Organizational Path**:
1. First contact: {ROLE} - Why: {CLOSEST_TO_PAIN}
2. Message: "{SPECIFIC_OUTREACH_USING_L0-L6_CONTEXT}"
3. Intelligence gathering: Validate {L4_L5_L6_HYPOTHESES}
4. Multi-thread to: {ROLE_2} → {ECONOMIC_BUYER}

### Intelligence Gathering Questions
**Validate L4**: "{QUESTION_ABOUT_BOTTLENECK}"
**Validate L5**: "{QUESTION_ABOUT_DATA_NEED}"
**Validate L6**: "{QUESTION_ABOUT_VALUE}"
**Map Org**: "{QUESTION_ABOUT_STAKEHOLDERS}"
```

**Quality Checklist**:
- [ ] Uses L1 ICP (not generic)
- [ ] Shows data L3 tools lack
- [ ] Stakeholders match L2 + L3
- [ ] Org path is specific (not vague)
- [ ] Intelligence questions validate hypotheses

---

## 6. Decision Tree: When to Use L0-L6

### Pre-Qualification

**Use L0-L6 Framework When**:
- [ ] Enterprise B2B deal (ACV ≥ $50K)
- [ ] Complex buying process (multiple stakeholders)
- [ ] Long sales cycle (≥3 months typical)
- [ ] Strategic account (worth deep research investment)
- [ ] Permissionless value concept is viable (can show data/insights before purchase)

**Do NOT Use L0-L6 When**:
- [ ] High-volume SMB prospecting (research cost > deal value)
- [ ] Simple transactional sales (individual buyer, short cycle, < $10K ACV)
- [ ] Existing customers with known context (use account planning frameworks instead)
- [ ] Time-sensitive outreach (need response in < 48 hours, can't afford 2-4 hour research)
- [ ] Product doesn't lend itself to permissionless value (e.g., commoditized services)

### Layer Depth Decision

**Full L0-L6 (2-4 hours research)**:
- Strategic enterprise accounts (ACV $100K+)
- Top-tier prospects (dream customer list)
- High-stakes meetings (C-level executive engagement)
- Use case: Building comprehensive account intelligence for enterprise sales team

**L0-L3 Only (1-2 hours research)**:
- Mid-market accounts (ACV $25-100K)
- Qualified inbound leads (need context, not discovery)
- Partnership/channel discussions (need to understand their GTM)
- Use case: Pre-meeting research for sales calls

**L0-L2 Only (30-60 min research)**:
- Small deals (ACV $10-25K)
- Initial qualification (before investing in L3-L6)
- Competitive intelligence (understand competitor customers)
- Use case: Sales team needs basic account context

### Research Approach by Layer Depth

**L0-L2 Foundation (VERIFIED focus)**:
- Time: 30-60 minutes
- Sources: Website, reviews, testimonials, customer logos
- Output: Factual account foundation (product, customer, buying process)
- Quality bar: High VERIFIED %, low INFERRED %

**L3-L4 GTM Intelligence (INFERRED focus)**:
- Time: 30-90 minutes
- Sources: LinkedIn jobs, team structure, tech stack (HG Insights), leadership changes
- Output: GTM motion classification + bottleneck hypothesis
- Quality bar: Well-reasoned INFERRED claims with explicit logic, cross-validated with L0-L2

**L5-L6 Use Case Synthesis (SYNTHESIS focus)**:
- Time: 30-60 minutes
- Sources: No new research, synthesis of L0-L4
- Output: Specific data need + buildable permissionless value concept
- Quality bar: Logical coherence (L5-L6 flows from L0-L4), actionability (rep can execute)

### Quality vs Speed Trade-offs

**Maximum Quality (2-4 hours)**:
- All 7 layers (L0-L6)
- ≥70% VERIFIED claims in L0-L2
- Cross-validation gates enforced between all layers
- Alternative hypotheses considered in L4
- Comprehensive permissionless value concept in L6
- **Use for**: Top 10% of accounts (strategic value)

**Balanced Quality (1-2 hours)**:
- L0-L3 (foundation + GTM motion)
- ≥50% VERIFIED in L0-L2
- Basic cross-validation (L2-L3 consistency check)
- Single bottleneck hypothesis in L4 (if time permits)
- **Use for**: Top 30% of accounts (qualified pipeline)

**Speed Research (30-60 min)**:
- L0-L2 only (foundation)
- ≥30% VERIFIED (accept more CLAIMED/INFERRED)
- No cross-validation gates (accept inconsistencies)
- Flag gaps as UNKNOWN
- **Use for**: High-volume prospecting, initial qualification

### Adaptation Patterns

**For Different Industries**:
- **B2B SaaS** (original framework): Use as-is
- **Enterprise Services**: L2 (buying process) becomes more important (longer cycles, more stakeholders)
- **Hardware/Manufacturing**: L0 (product) needs supply chain context, L1 (customer) may need distributor/channel layer
- **Healthcare/Regulated**: L2 (buying) includes compliance/legal stakeholders, longer procurement cycles

**For Different GTM Motions**:
- **PLG Companies**: L3 focuses on self-serve → paid upgrade path, L5 may emphasize activation/retention data vs acquisition
- **Enterprise-Only**: L2 (buying) is complex committee, L4 often velocity/quality bottlenecks vs volume
- **Partner-Led**: L3 includes partner ecosystem analysis, L4 may include partner enablement bottlenecks
- **Community-Driven**: L1 (customer) includes community dynamics, L3 includes community growth metrics

---

## 7. Implementation Guide

### Step-by-Step Execution

**Phase 1: Foundation Research (L0-L2) - 30-60 minutes**

**Agent 1A Execution**:
1. **Input**: Company domain (e.g., "clay.com")
2. **Research L0** (15 min):
   - Visit homepage → Extract value prop (exact quote)
   - Read product pages → Assess complexity (look for integration requirements, technical docs)
   - Note differentiation (what makes it unique)
3. **Research L1** (20 min):
   - Find customer testimonials/case studies on website
   - Search G2/Capterra for verified reviews → Extract customer names, industries, sizes
   - LinkedIn search for customer companies → Verify sizes, industries
   - Identify patterns (≥3 examples to claim pattern)
4. **Research L2** (15 min):
   - Review testimonials → Who is quoted? (extract stakeholder roles)
   - Read G2 reviews → What roles write reviews? What do they say about buying process?
   - Infer sales cycle (product complexity L0 + customer size L1 + direct evidence)
   - Extract evaluation criteria from reviews ("We chose X because...")
5. **Output**: Foundation Report (L0-L2) saved to file
6. **Quality Check**:
   - [ ] ≥3 verified customers OR flagged as insufficient
   - [ ] ≥2 stakeholder roles identified
   - [ ] All claims have source URLs + dates
   - [ ] VERIFIED/INFERRED/UNKNOWN marked

**Phase 2: GTM Intelligence (L3-L4) - 30-90 minutes**

**Agent 1B Execution**:
1. **Input**: Foundation Report (L0-L2) from Agent 1A + Company domain
2. **FIRST: Read Foundation Report** (5 min):
   - Understand product complexity (L0)
   - Understand customer types (L1)
   - Understand buying process (L2)
3. **Research L3 - GTM Motion** (30 min):
   - LinkedIn Jobs: Search "{company_name} jobs" → Count roles by type (SDR, AE, Growth Eng, etc.)
   - LinkedIn Company Page → Team sizes (Sales, Marketing, Ops, CS)
   - HG Insights (if accessible via [Tool]) → Extract GTM tech stack
   - Classify motion (PLG, Enterprise, Hybrid, etc.) based on role patterns
   - **Cross-validate**: Does motion match L2 buying process? (committee buying → should see ops support)
4. **Research L4 - Bottleneck** (30 min):
   - Hiring velocity: Count roles posted in last 30/60/90 days
   - Read 3-5 job descriptions → Extract pain points, required tools, scale indicators
   - LinkedIn leadership: Search for new CRO, VP Sales, Head of Ops in last 6 months
   - Tech stack gap analysis: Compare actual (L3) to expected for motion type
   - **Cross-validate**: Does bottleneck make sense given L0-L2? (if committee buying but no ops → velocity bottleneck)
5. **Output**: GTM Intelligence Report (L3-L4) saved to file
6. **Quality Check**:
   - [ ] GTM motion has ≥2 supporting signals
   - [ ] Bottleneck is specific (not "scaling challenges")
   - [ ] Cross-validated with L0-L2 (no contradictions)
   - [ ] Hiring signals have counts + dates

**Phase 3: Use Case Synthesis (L5-L6) - 30-60 minutes**

**Agent 2 Execution**:
1. **Input**: Foundation Report (L0-L2) + GTM Report (L3-L4)
2. **FIRST: Read Both Reports** (10 min):
   - L0: Product type, complexity
   - L1: Customer ICP (who to target)
   - L2: Buying committee (who to reach)
   - L3: GTM motion, team structure, tech stack
   - L4: Bottleneck type
3. **Synthesize L5 - Data Need** (15 min):
   - Map bottleneck → data problem (use taxonomy: Volume → list building, Expansion → new ICP discovery, etc.)
   - Factor in L1 ICP (targeting requirements)
   - Factor in L3 motion + tech stack (enrichment requirements, current tool gaps)
   - Define specific [Tool] use case
   - Compare to current approach (L3 tech stack) to show advantages
4. **Design L6 - Permissionless Value** (15 min):
   - Design concrete [Tool] table using L1 ICP (show data for THEIR customers, not generic)
   - Specify enrichment workflow (providers, fields, output)
   - Map stakeholders: End users (L3 team structure), Economic buyer (L2 buying committee)
   - Create organizational path (who to reach first, how to multi-thread)
   - Write intelligence gathering questions (to validate L4-L6 hypotheses)
5. **Output**: [Tool] Use Case Report (L5-L6) saved to file
6. **Quality Check**:
   - [ ] Use case directly solves L4 bottleneck
   - [ ] Permissionless value uses L1 ICP
   - [ ] Comparison references L3 tech stack
   - [ ] Stakeholders match L2 + L3
   - [ ] Rep could build this in [Tool]

### Time Management

**2-Hour Research Window**:
- L0-L2: 45 minutes (Agent 1A)
- L3-L4: 45 minutes (Agent 1B)
- L5-L6: 30 minutes (Agent 2)

**4-Hour Deep Research Window**:
- L0-L2: 90 minutes (more customer verification, deeper buying process analysis)
- L3-L4: 90 minutes (more job descriptions, deeper tech stack analysis, alternative hypotheses)
- L5-L6: 60 minutes (comprehensive permissionless value, detailed stakeholder strategy)

### Common Pitfalls

**Pitfall 1: Starting L3 Without Reading L0-L2**
- Symptom: GTM motion classification doesn't match customer buying process
- Fix: Agent 1B MUST read Foundation Report first, cross-validate all L3 inferences against L0-L2

**Pitfall 2: Vague Bottleneck Hypothesis**
- Symptom: L4 says "need more pipeline" or "scaling challenges" (too generic)
- Fix: Require specific bottleneck type (Volume, Quality, Velocity, Expansion) with ≥3 evidence sources

**Pitfall 3: Generic Permissionless Value**
- Symptom: L6 shows "company enrichment table" without using their ICP
- Fix: L6 MUST use L1 ICP explicitly (show 50-500 employee SaaS companies, not "companies")

**Pitfall 4: Insufficient Evidence Attribution**
- Symptom: Claims lack sources, dates, or evidence levels
- Fix: Enforce quality gates (no claim without URL + date, all claims must have VERIFIED/INFERRED/UNKNOWN)

**Pitfall 5: Broken Synthesis Logic**
- Symptom: L5 use case doesn't solve L4 bottleneck
- Fix: Use bottleneck taxonomy strictly (Volume → list building, Velocity → org mapping, etc.)

### Success Criteria

**Report-Level Success** (for complete L0-L6):
1. **Differentiation**: Report for Company A looks substantively different from Company B (not templated boilerplate)
2. **Actionability**: Sales rep can build permissionless value and execute outreach without additional research
3. **Evidence Quality**: ≥60% VERIFIED or well-INFERRED claims (not speculation)
4. **Insight Density**: ≥3 non-obvious discoveries (beyond "they sell to enterprises")
5. **Replicability**: Another researcher using same methodology reaches similar conclusions

**Layer-Level Success**:
- **L0**: Another person can understand what the product is and does
- **L1**: Clear who the customer is (not "enterprises" but specific types)
- **L2**: Identified buying stakeholders with evidence (not guessed)
- **L3**: GTM motion matches L0-L2 context (internal consistency)
- **L4**: Bottleneck is specific enough to suggest data solution
- **L5**: Use case logically solves bottleneck and leverages L1 ICP

### Iteration Protocol

**If Research Reveals Insufficient Data**:
1. Flag gaps as UNKNOWN explicitly (don't guess)
2. Proceed with reduced context to next layer
3. Increase INFERRED vs VERIFIED ratio (acknowledge lower confidence)
4. Propose discovery questions to fill gaps
5. Flag account for "high intelligence gathering priority" in first call

**If Layers Contradict Each Other**:
1. Stop progression, resolve contradiction
2. Re-examine evidence in conflicting layer
3. Either: Fix inference error, OR Flag as TRANSITION state
4. Example: L2 shows individual buying but L3 shows enterprise AE hiring → Flag as "upmarket transition, buying process may be changing"

**If Synthesis Fails (Can't Derive L5 from L4)**:
1. Return to L4, check bottleneck specificity
2. If bottleneck is too vague ("scaling"), re-analyze with stricter criteria
3. Consider multiple bottlenecks (primary + secondary)
4. Use bottleneck taxonomy strictly (don't invent new bottleneck types)

---

## Appendix: Wave 1 Integration

This L0-L6 pattern library builds on Wave 1 meta-analysis findings:

**From Role Contract Patterns**:
- Agent 1A (Foundation Intelligence) = **Collector** role type (25% of agents)
- Agent 1B (GTM Motion Intelligence) = **Analyzer** role type (30% of agents)
- Agent 2 (Use Case Synthesis) = **Synthesizer** role type (20% of agents)

**From Attribution Framework Comparison**:
- Inline citation format (SOURCE: URL, DATE: YYYY-MM-DD) enables staleness detection
- Evidence level criteria definitions from Wave 1 directly inform L0-L6 quality gates
- Rigor scales with project lifespan: L0-L6 is tactical (high citation rigor, minimal lineage tracking)

**Integrated Quality Framework**:
```yaml
citation_schema: "Inline URL + date (from Wave 1 [Tool] pattern)"
evidence_taxonomy: "VERIFIED/INFERRED/UNKNOWN (from Wave 1 attribution framework)"
agent_roles: "Collector (L0-L1) → Analyzer (L2-L4) → Synthesizer (L5-L6) (from Wave 1 role patterns)"
contract_pattern: "File-based sequential handoff (from Wave 1 schema library)"
```

---

**End of L0-L6 Pattern Library**
*Ready for reuse in enterprise account intelligence workflows*
