---
name: foundation_seeder
description: "ONE-TIME agent that processes raw_context documents to seed 00_foundation/ baseline nodes before transcript processing begins"
node_type: agent_specification
domain: system
agent_role: foundation_initialization
execution_pattern: one_time_seed
version: 1.0
status: ready
created: 2025-10-30
last_updated: 2025-10-30
depends_on:
  - knowledge_base/raw_context/*.md (with frontmatter)
  - strategic_lens.yaml v1.2+
outputs:
  - knowledge_base/00_foundation/icp/*.md
  - knowledge_base/00_foundation/positioning/*.md
  - knowledge_base/00_foundation/value_props/*.md
  - knowledge_base/00_foundation/competitive_intel/*.md
  - knowledge_base/00_foundation/product/*.md
  - knowledge_base/00_foundation/business_model/*.md
  - knowledge_base/00_foundation/market/*.md
next_agent: dimensional_extractors (after foundation seeded)
orchestration_ref: ORCHESTRATION_ARCHITECTURE.md
evidence_standard: VERIFIED|INFERRED|UNKNOWN
---

# Foundation_Seeder Agent

**Role:** Foundation Initialization - ONE-TIME Execution
**Pattern:** Sequential processing of raw_context corpus
**Execution:** BEFORE transcript processing begins
**Version:** 1.0
**Created:** 2025-10-30

---

## Purpose

Extract strategic context from Nickel's 68 raw_context documents to create 20-30 **baseline foundation nodes** that establish the company's stated strategy, ICP, positioning, and capabilities BEFORE validating against transcripts.

**Critical Responsibilities:**
- Process 68 raw_context documents (already has frontmatter from parallel agents)
- Create 20-30 atomic nodes in `knowledge_base/00_foundation/`
- Status: baseline (will be validated by transcripts later)
- Confidence: medium (5-6 on 0-10 scale)
- Evidence attribution: VERIFIED with raw_context sources

**This is NOT:**
- Transcript processing (different agent)
- Creating deliverables (nodes only)
- Customer intelligence (that comes from transcripts)

---

## Input Requirements

### Required Files

**Raw Context Corpus:**
- Location: `knowledge_base/raw_context/*.md`
- Count: 68 documents
- Frontmatter: Already applied by parallel agents
- Signal strength: high (20), medium (30), low (18)

**Strategic Lens:**
- `knowledge_base/strategic_lens.yaml` v1.2+
- Contains dimensional priorities and node lifecycle rules

---

## Foundation Extraction Categories

### 1. ICP & Segmentation (`00_foundation/icp/`)

**Extract from raw_context:**
- Firmographic criteria (revenue, employee count, vertical)
- Revenue qualification system (Shrimp/Fish/Whale/Kraken)
- Ideal verticals and sub-segments
- Anti-ICP signals
- Ivan's constraints (margins, headcount, transaction type, AR vs AP)

**Nodes to create:**
```yaml
icp-definition.md:
  status: baseline
  confidence: 6.0
  sources: ["ICP Summary & Use Cases.md", "Ivan call transcript"]
  content:
    - Firmographic criteria
    - Revenue tiers with strategic fit weights
    - Ivan's critical constraints (margins <30%, headcount <10, sales-led)
    - Business model constraints (AR vs AP)

ideal-verticals.md:
  status: baseline
  confidence: 5.5
  sources: ["ICP Summary.md", "Nickel core positioning.md"]
  content:
    - Building Materials & Construction
    - Wholesale & Distribution
    - Manufacturing
    - Transportation & Logistics
    - Large-Ticket B2B Services

anti-icp.md:
  status: baseline
  confidence: 6.0
  sources: ["Ivan call transcript", "ICP Summary.md"]
  content:
    - High-margin professional services
    - E-commerce / shopping cart
    - Large accounting teams (ERP-dependent)
    - ACH-only AP customers
    - Retail stores, software, healthcare, restaurants
```

---

### 2. Positioning (`00_foundation/positioning/`)

**Extract from raw_context:**
- Positioning statement
- Target segments
- Category definition
- Competitive differentiation points

**Nodes to create:**
```yaml
positioning-statement.md:
  status: baseline
  confidence: 6.0
  sources: ["Nickel core positioning statement.md"]
  content:
    - "First all-in-one Supplier Finance platform"
    - Target: Building supply companies, 2-100 employees
    - Differentiation: vs industry-agnostic, vs sketchy lenders

target-segments.md:
  status: baseline
  confidence: 5.5
  sources: ["ICP Summary.md", "GTM Build Updates"]
  content:
    - Payment Upgraders (save money, speed up payments)
    - Cash-Savvy Sellers (net terms without risk)
    - Full Stack Automators (supercharge credit department)

category-definition.md:
  status: baseline
  confidence: 5.0
  sources: ["Nickel core positioning.md"]
  content:
    - Supplier Finance platform (not just payment processor)
    - AR automation + Working capital + Collections
```

---

### 3. Value Propositions (`00_foundation/value_props/`)

**Extract from raw_context:**
- Core value props
- Segment-specific propositions
- Differentiation from competitors

**Nodes to create:**
```yaml
supplier-finance-platform.md:
  status: baseline
  confidence: 6.0
  sources: ["Nickel core positioning.md", "ICP Summary.md"]
  content:
    - All-in-one solution (vs point solutions)
    - Eliminate payment delays
    - Offer net terms without credit department
    - Automate manual credit decisions

payment-upgrader-value-prop.md:
  status: baseline
  confidence: 5.5
  sources: ["ICP Summary.md"]
  content:
    - Save money on payment processing
    - Speed up payments (reduce DSO)
    - Eliminate check hassles

cash-savvy-seller-value-prop.md:
  status: baseline
  confidence: 5.5
  sources: ["ICP Summary.md"]
  content:
    - Give customers net terms
    - Get paid immediately
    - No cashflow risk
    - No credit department needed

full-stack-automator-value-prop.md:
  status: baseline
  confidence: 5.5
  sources: ["ICP Summary.md"]
  content:
    - Supercharge existing credit department
    - Automate lien management
    - Scale underwriting without headcount
```

---

### 4. Competitive Intelligence (`00_foundation/competitive_intel/`)

**Extract from raw_context:**
- Tier 1 direct competitors
- Tier 2 adjacent solutions
- Tier 3 point solutions
- Tier 4 status quo
- Pricing, positioning, differentiation

**Nodes to create:**
```yaml
melio.md:
  status: baseline
  confidence: 5.0
  sources: ["ICP Summary.md", "GTM Build Update"]
  content:
    - Tier: 1 (Direct)
    - Category: AR Automation
    - Positioning: Industry-agnostic, larger company focus
    - Pricing: $90/month (vs Nickel $35-45)
    - Differentiation: Nickel is industry-specific, better for building supply
    - Validation needed: Customer satisfaction, win/loss rates

bill-com.md:
  status: baseline
  confidence: 5.0
  sources: ["ICP Summary.md"]
  content:
    - Tier: 1 (Direct)
    - Category: AR/AP Automation
    - Positioning: Industry-agnostic, enterprise focus
    - Differentiation: Nickel serves SMBs better, less complex

quickbooks-status-quo.md:
  status: baseline
  confidence: 6.0
  sources: ["ICP Summary.md"]
  content:
    - Tier: 4 (Status Quo)
    - PRIMARY COMPETITOR: Most prospects using QB currently
    - Must integrate seamlessly (CRITICAL blocker)
    - Pricing: $30-200/month

competitive-landscape.md:
  status: baseline
  confidence: 5.5
  sources: ["ICP Summary.md"]
  content:
    - 4-tier framework (Direct, Adjacent, Point Solutions, Status Quo)
    - Tier 1: Melio, Bill.com
    - Tier 2: Invoice factoring, legacy processors
    - Tier 3: Credit apps, lien management
    - Tier 4: QuickBooks, bank lines of credit
```

---

### 5. Product Capabilities (`00_foundation/product/`)

**Extract from raw_context:**
- Core features
- Integrations
- Payment methods
- Technical capabilities
- Roadmap signals

**Nodes to create:**
```yaml
quickbooks-integration.md:
  status: baseline
  confidence: 7.0
  sources: ["ICP Summary.md", "GTM Build Update"]
  content:
    - Two-way sync with QuickBooks Online
    - UNIVERSAL REQUIREMENT (100% mention rate in Iteration 1)
    - Primary status quo replacement
    - CRITICAL blocker if missing

ar-automation.md:
  status: baseline
  confidence: 6.0
  sources: ["ICP Summary.md"]
  content:
    - Automated invoice sending
    - Payment reminders
    - Reconciliation
    - Applicable to all 3 ICP tiers

payment-methods.md:
  status: baseline
  confidence: 6.0
  sources: ["ICP Summary.md", "GTM Build Update"]
  content:
    - Free ACH payments
    - Credit card processing (18.2% of core customers use)
    - Apple Pay (live to top customers)
    - International payments (coming soon)

net-terms-extension.md:
  status: baseline
  confidence: 6.0
  sources: ["ICP Summary.md"]
  content:
    - Extend 30-90 day terms to customers
    - Supplier gets paid immediately
    - Nickel underwrites credit risk
    - Target: Cash-Savvy Sellers, Full Stack Automators

core-capabilities.md:
  status: baseline
  confidence: 6.0
  sources: ["Nickel core positioning.md", "ICP Summary.md"]
  content:
    - AR automation
    - Payment processing (ACH + CC)
    - Credit application & underwriting
    - Lien management
    - Collections automation
```

---

### 6. Business Model & Metrics (`00_foundation/business_model/`)

**Extract from raw_context:**
- Revenue model
- Pricing structure
- Key metrics
- Unit economics (if available)

**Nodes to create:**
```yaml
revenue-model.md:
  status: baseline
  confidence: 6.0
  sources: ["Ivan call transcript", "GTM Build Update"]
  content:
    - Revenue source: Credit card transaction fees
    - AR customers: High fit (mix of CC + ACH)
    - AP customers: Binary (all CC = good, all ACH = no revenue)
    - CRITICAL constraint: Must generate CC transaction volume

pricing.md:
  status: baseline
  confidence: 5.5
  sources: ["ICP Summary.md"]
  content:
    - Free tier: Basic payment processing
    - Paid tiers: $35-45/month
    - Competitive vs Melio ($90/mo), Bill.com (enterprise pricing)

key-metrics.md:
  status: baseline
  confidence: 6.0
  sources: ["GTM Build Update", "ICP Summary.md"]
  content:
    - Leading Indicator of Retention (LIR): 50% receivables on Nickel
    - August 2025: $35.2M TPV, $26.2M core TPV
    - AR percentage: 36.7% overall, 49.3% core
    - CC adoption: 13.6% overall, 18.2% core
    - 27 deals closed, $86M company revenue
```

---

### 7. Market Context (`00_foundation/market/`)

**Extract from raw_context:**
- Industry trends
- Segment performance
- GTM evolution
- Market sizing (if available)

**Nodes to create:**
```yaml
industry-trends.md:
  status: baseline
  confidence: 5.5
  sources: ["GTM Build Update"]
  content:
    - ACH adoption increasing (150+ clicks/week on ACH content)
    - LLM citation growing (ChatGPT/Perplexity visibility)
    - B2B credit card usage rising (18.2% core, up from baseline)
    - AR product leadership (49.3% of core TPV)

segment-analysis.md:
  status: baseline
  confidence: 5.0
  sources: ["ICP Summary.md", "GTM Build Updates"]
  content:
    - Building Materials & Construction: Primary
    - Wholesale & Distribution: Secondary (strong fit)
    - Manufacturing: Secondary
    - Transportation & Logistics: Secondary
    - Performance data: Needs transcript validation

gtm-evolution.md:
  status: baseline
  confidence: 5.0
  sources: ["GTM Build Updates"]
  content:
    - Evolution from AP-focused to AR-led
    - QuickBooks integration critical path
    - Apple Pay launched to top customers
    - International payments roadmap
```

---

## Extraction Process

### Step 1: Filter High-Signal Raw_Context (15 min)

**Use frontmatter to identify priority docs:**
```yaml
signal_strength: high
contains_icp: true
contains_metrics: true
contains_competitive: true
contains_customer_evidence: true
```

**Expected high-signal docs (~20):**
- ICP Summary & Use Cases
- Nickel core positioning statement
- GTM Build Updates (monthly)
- Funnel Stages and Definitions
- Classification Prompts
- Ivan call transcript

---

### Step 2: Extract by Category (2-3 hours)

**For each foundation category:**
1. Read all relevant raw_context docs
2. Extract claims with line-level citations
3. Create atomic node with:
   - YAML frontmatter (node_type, status, confidence, sources)
   - Content with evidence attribution
   - Context_lineage with source docs
   - No fabrication - only VERIFIED claims

**Evidence Attribution Standard:**
```markdown
[VERIFIED: ICP Summary.md:42-45] - Direct quote confirms X
[VERIFIED: Ivan call:2025-10-30] - Critical constraint on margins
[INFERRED: 3 GTM updates] - Trend deduced from monthly reports
[UNKNOWN] - Cannot verify without additional data
```

---

### Step 3: Cross-Reference Strategic Lens (30 min)

**Ensure foundation nodes align with lens:**
- WHO dimension: ICP criteria match lens personas
- WHAT dimension: Value props match lens pain points
- WHY dimension: Competitive intel matches lens threats
- HOW dimension: Product capabilities match lens requirements
- WHERE_WHEN dimension: Funnel stages match lens journey
- META dimension: Market trends match lens insights

---

### Step 4: Calculate Baseline Confidence (15 min)

**Confidence formula:**
```yaml
base_confidence (baseline): 5.0
source_boost: log10(source_count + 1) × 1.5
evidence_quality_multiplier: 0.8-1.2

Example:
  icp-definition.md:
    sources: 3 docs (ICP Summary, Ivan call, positioning)
    evidence_quality: high (direct quotes, quantified)
    confidence = 5.0 + (log10(4) × 1.5) × 1.2 = 5.0 + (0.602 × 1.5) × 1.2 = 6.08 → 6.1
```

---

### Step 5: Generate Node Output (30 min)

**Per node structure:**
```markdown
---
node_type: icp_definition | positioning | value_prop | competitive_intel | product_capability | business_model | market_context
status: baseline
confidence: 5.0-7.0
created: 2025-10-30
last_updated: 2025-10-30
sources:
  - ICP Summary & Use Cases.md
  - Ivan call transcript
tags: [foundation, icp, firmographic-criteria]
validation_status: awaiting_transcript_validation
transcript_validations: 0
---

# [Node Title]

**Status:** Baseline (from raw_context, awaiting transcript validation)
**Confidence:** [X.X]/10
**Sources:** [X raw_context documents]

[VERIFIED: source:lines] content here...

## Context Lineage

**Source Documents:**
- `knowledge_base/raw_context/ICP Summary.md` (lines 42-67)
  - Unique value: Firmographic criteria and revenue tiers

- `knowledge_base/raw_context/Ivan_call_transcript.md` (lines 89-134)
  - Unique value: Critical margin/headcount/transaction constraints

**Dimensional Mapping:**
- WHO dimension: [relevant strategic_lens section]
- Strategic fit weight: [from lens]

## Transcript Validation

**Validation signals:** (will be added as transcripts process)
- [ ] Frequency count (how many transcripts mention this)
- [ ] Persona examples (which personas validate this)
- [ ] Quantification (transcript-provided metrics)
- [ ] Contradictions (if transcript evidence refutes baseline)

**Status progression:**
- baseline → validating (after 1 transcript validation)
- validating → validated (after 2 transcript validations)
- validated → canonical (after 5 transcript validations)
```

---

## Output Structure

**Total nodes created:** 20-30

**By category:**
```yaml
00_foundation/
├── icp/                        # 3-5 nodes
│   ├── icp-definition.md
│   ├── ideal-verticals.md
│   └── anti-icp.md
│
├── positioning/                # 3-4 nodes
│   ├── positioning-statement.md
│   ├── target-segments.md
│   └── category-definition.md
│
├── value_props/                # 3-4 nodes
│   ├── supplier-finance-platform.md
│   ├── payment-upgrader-value-prop.md
│   ├── cash-savvy-seller-value-prop.md
│   └── full-stack-automator-value-prop.md
│
├── competitive_intel/          # 4-6 nodes
│   ├── melio.md
│   ├── bill-com.md
│   ├── quickbooks-status-quo.md
│   └── competitive-landscape.md
│
├── product/                    # 5-6 nodes
│   ├── quickbooks-integration.md
│   ├── ar-automation.md
│   ├── payment-methods.md
│   ├── net-terms-extension.md
│   └── core-capabilities.md
│
├── business_model/             # 3-4 nodes
│   ├── revenue-model.md
│   ├── pricing.md
│   └── key-metrics.md
│
└── market/                     # 3-4 nodes
    ├── industry-trends.md
    ├── segment-analysis.md
    └── gtm-evolution.md
```

---

## Quality Checklist

- [ ] All nodes have YAML frontmatter with status: baseline
- [ ] All nodes have confidence scores (5.0-7.0 range)
- [ ] All claims have [VERIFIED: source:lines] attribution
- [ ] No fabricated content (UNKNOWN used when cannot verify)
- [ ] Context_lineage complete with source docs and line ranges
- [ ] Strategic_lens dimensional mapping present
- [ ] Transcript validation section included (empty initially)
- [ ] 20-30 nodes total across 7 categories

---

## Critical Constraints

✅ **MUST:**
- Status = baseline (not emergent, validated, or canonical)
- Confidence = 5.0-7.0 (medium range, will increase with transcripts)
- Evidence attribution = VERIFIED with raw_context sources
- Transcript validation section included but empty

❌ **MUST NOT:**
- Create nodes from transcripts (that's dimensional extractors' job)
- Mark nodes as validated/canonical (needs transcript evidence)
- Fabricate claims not in raw_context
- Skip evidence attribution

---

## Execution Time

**Target:** 3-5 hours (ONE-TIME)

**Breakdown:**
- Filter high-signal raw_context: 15 min
- Extract by category (7 categories): 2-3 hours
- Cross-reference strategic lens: 30 min
- Calculate baseline confidence: 15 min
- Generate node output: 30-45 min
- Quality validation: 15-20 min

---

## Handoff to Next Agent

**After Foundation_Seeder completes:**

1. **20-30 baseline nodes exist** in `knowledge_base/00_foundation/`
2. **Status:** All nodes = baseline, confidence = 5-7
3. **Ready for transcript processing** - Dimensional extractors can now:
   - Extract customer patterns (new nodes)
   - Validate foundation patterns (update baseline nodes)
   - Build connections (wiki-links)
4. **Context Weaver runs periodically** to enrich foundation nodes with transcript validation signals

---

**Version:** 1.0
**Status:** READY FOR EXECUTION
**Execution:** ONE-TIME before transcript processing
**Next:** Dimensional Extractors begin processing transcripts
