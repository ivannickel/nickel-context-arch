# Raw Context Frontmatter Schema

**Version:** 1.0
**Created:** 2025-10-30
**Purpose:** Standardize frontmatter for raw Nickel context documents to enable filtering and strategic analysis

---

## Schema Definition

```yaml
---
# Document Classification
document_type: "gtm_update | strategic_doc | operational_guide | meeting_note | process_doc"
date: "YYYY-MM-DD"  # Extract from filename or content
author: "Name"      # Owner/primary author
source: "notion | internal_doc | meeting_transcript"

# Strategic Categorization (multi-select)
topics:
  - icp_definition
  - competitive_intelligence
  - product_strategy
  - sales_operations
  - marketing_channels
  - customer_success
  - financial_metrics
  - team_operations

# Signal Strength for Strategic Lens
signal_strength: "high | medium | low"
  # high: ICP, positioning, competitive intel, validated metrics
  # medium: Operational updates, tactical wins, feature requests
  # low: Process docs, tool guides, one-off meetings

# Strategic Intelligence Flags
contains_icp: true | false
contains_metrics: true | false
contains_competitive: true | false
contains_customer_evidence: true | false

# Metadata
file_size: "KB"
processed: false  # Will be set to true after lens extraction
lens_extracted: false
---
```

---

## Document Type Definitions

**gtm_update:**
- Weekly/bi-weekly GTM Build Updates
- Contains metrics, wins, operations, strategy
- Primary source for validated patterns
- Example: "08 29 25 - GTM Build Update"

**strategic_doc:**
- ICP definitions, positioning statements, classification frameworks
- Core strategic intelligence
- High signal strength by default
- Example: "ICP Summary", "Nickel core positioning statement"

**operational_guide:**
- Process documentation, tool guides, onboarding materials
- Reference material, not strategic intelligence
- Low signal strength by default
- Example: "Nickel AE Onboarding Guide", "Hubspot User Guide"

**meeting_note:**
- Strategy sessions, planning meetings, decision records
- Variable signal strength (depends on topic)
- Example: "Nickel + Daydream Strategy Session"

**process_doc:**
- SOPs, workflows, approval processes
- Operational reference only
- Low signal strength
- Example: "Nickel Approval Onboarding Process"

---

## Topic Taxonomy

**icp_definition:**
- Target customer profiles
- Shrimp/Fish/Whale qualification
- Industry verticals, revenue bands
- Buyer personas

**competitive_intelligence:**
- Melio, traditional banks, payment processors
- Win/loss analysis
- Competitive positioning
- Feature comparisons

**product_strategy:**
- QuickBooks integration
- Apple Pay, international payments
- Feature priorities, roadmap
- Customer feature requests

**sales_operations:**
- Lead qualification, conversion metrics
- Deal pipeline, closed won analysis
- AE performance, territory management
- Sales process optimization

**marketing_channels:**
- SEO, content strategy
- Connected TV, paid channels
- G2 reviews, case studies
- LLM citations, organic mentions

**customer_success:**
- Onboarding, activation flows
- CSAT scores, retention metrics
- Customer segmentation (Tier 1/2/3)
- Expansion, upsell

**financial_metrics:**
- TPV (Total Payment Volume)
- AR/AP split, credit card adoption
- Transaction counts, growth rates
- Revenue, LTV, CAC

**team_operations:**
- Hiring, onboarding
- Tool implementations
- Process improvements
- Internal workflows

---

## Signal Strength Guidelines

**High Signal (Priority 1 for Lens Extraction):**
- ICP definitions
- Competitive intelligence
- Validated customer metrics (TPV, conversion, retention)
- Strategic positioning statements
- Win/loss patterns with evidence

**Medium Signal (Priority 2):**
- Tactical operational updates
- Feature launch announcements
- Sales wins with context
- Marketing channel performance
- Customer feedback patterns

**Low Signal (Priority 3, reference only):**
- Tool guides and SOPs
- Internal process documentation
- One-off meeting notes without strategic conclusions
- Administrative updates

---

## Usage for Multi-Agent Orchestration

**Batch 1 (High Signal):**
Filter by `signal_strength: high` → Process first for strategic_lens.yaml

**Batch 2 (Competitive Intel):**
Filter by `contains_competitive: true` → Extract competitive positioning

**Batch 3 (ICP & Metrics):**
Filter by `contains_icp: true` OR `contains_metrics: true` → Extract validation data

**Batch 4 (Customer Evidence):**
Filter by `contains_customer_evidence: true` → Extract use cases, pain points

---

## Example Frontmatter

**GTM Update:**
```yaml
---
document_type: gtm_update
date: 2025-08-29
author: Miguel
source: notion

topics:
  - sales_operations
  - financial_metrics
  - competitive_intelligence
  - customer_success
  - product_strategy

signal_strength: high

contains_icp: true
contains_metrics: true
contains_competitive: true
contains_customer_evidence: true

file_size: 14K
processed: false
lens_extracted: false
---
```

**Strategic Doc:**
```yaml
---
document_type: strategic_doc
date: 2025-06-15
author: Ivan
source: notion

topics:
  - icp_definition
  - competitive_intelligence

signal_strength: high

contains_icp: true
contains_metrics: false
contains_competitive: false
contains_customer_evidence: false

file_size: 6.3K
processed: false
lens_extracted: false
---
```

**Operational Guide:**
```yaml
---
document_type: operational_guide
date: 2025-04-12
author: Ray
source: internal_doc

topics:
  - team_operations

signal_strength: low

contains_icp: false
contains_metrics: false
contains_competitive: false
contains_customer_evidence: false

file_size: 823B
processed: false
lens_extracted: false
---
```

---

## Implementation Notes

**For Frontmatter Addition Agents:**
1. Read filename and first 50 lines to classify document_type
2. Extract date from filename or header
3. Scan content for topic keywords to set topics[]
4. Set signal_strength based on document_type + topics
5. Set boolean flags by scanning for keywords:
   - ICP: "ICP", "ideal customer", "target customer", "qualification"
   - Metrics: "$", "TPV", "conversion", "revenue", "%"
   - Competitive: "Melio", "competitor", "vs", "alternative"
   - Evidence: "customer", "deal", "signed up", "use case"

**For Strategic Lens Creation:**
1. Query all docs with `signal_strength: high`
2. Query all docs with `contains_icp: true` OR `contains_competitive: true`
3. Process in priority order for lens extraction
