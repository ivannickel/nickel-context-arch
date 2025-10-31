# Agent Specification: Nickel Transcript Knowledge Graph Processor

**Mission:** Process 15-20 Nickel sales call transcripts into a structured knowledge graph using Phase 2 (Nucleation) patterns from the Knowledge Graph Nucleation System.

**Context:** First batch processing to discover emergent patterns, validate seed taxonomy, and establish graph foundation.

**Execution Time:** 2-4 hours
**Output:** Structured knowledge graph with 15-20 processed transcripts + emergent taxonomy report

---

## CRITICAL: Understanding the System

You are implementing **Phase 2: Nucleation** from the knowledge graph nucleation framework documented in:
- `../../../../../../../knowledge_base/research/meta_analysis/knowledge_graph_nucleation/`

**Key Patterns to Apply:**
1. **Pattern 4: Parallel Fanout-Fanin** - Extract multiple perspectives simultaneously
2. **Pattern 5: Iterative Refinement Loop** - Discover emergent taxonomy through iteration

**Your Role:** You are the orchestrator agent that runs the nucleation workflow.

---

## Input Sources

### Primary Source
**Location:** `knowledge_base/meetings_md/`
**Format:** Markdown files with transcripts (already extracted from CSV)
**Count:** 17 files visible, process first 15 for Iteration 1

**Files to Process (First Batch):**
```
001_abbas-rezaei-and-colton-ofarrell_2025-07-15.md
002_erik-meza-and-colton-ofarrell_2025-07-15.md
003_prime-renovations-ny-nickel_2025-07-23.md
004_carson-crawford-and-colton-ofarrell_2025-08-14.md
007_frank-delbrouck-and-colton-ofarrell_2025-08-19.md
008_hardy-butler-and-colton-ofarrell_2025-07-23.md
009_ashland-roofing-nickel-2nd-review-call_2025-09-25.md
010_amps-facility-solutions-nickel-kickoff-call_2025-09-29.md
011_american-home-renewal-inc-nickel_2025-07-18.md
012_matthew-and-colton-ofarrell_2025-08-20.md
013_jay-omanson-and-colton-ofarrell_2025-08-12.md
014_brandon-rogers-and-colton-ofarrell_2025-07-14.md
015_hassan-colton-nickel_2025-07-31.md
016_conner-rusch-and-colton-ofarrell_2025-07-18.md
017_sharika-and-colton-ofarrell_2025-08-13.md
```

### Seed Taxonomy (Provisional)
Based on Nickel POC scope and reconnaissance:

```yaml
domains:
  - foundation
  - customer
  - content
  - market

context_types:
  pain_points:
    - credit-card-limits
    - payment-processing-complexity
    - manual-data-entry
    - accounts-receivable-challenges
    - compliance-burden

  objections:
    - pricing-too-expensive
    - insufficient-volume
    - self-hosted-requirement
    - integration-complexity

  personas:
    - construction-buyer
    - distribution-buyer
    - b2b-services-buyer
    - cfo
    - office-manager

  use_cases:
    - high-volume-ap
    - large-transaction-processing
    - ar-automation
    - quickbooks-integration

  competitors:
    - traditional-banks
    - payment-processors
    - billcom
    - other-ap-ar-software
```

**Expected Evolution:** 20-40% new tags will emerge beyond this seed.

---

## Output Structure

### Directory Structure to Create

```
knowledge_base/
├── 00_foundation/
│   ├── nickel_icp_and_positioning.md        ← Stub for now
│   └── README.md                              ← Navigation guide
│
├── 01_customer/
│   ├── _synthesis/
│   │   └── [Stubs for Phase 3]
│   │       ├── customer_exec_summary.md
│   │       ├── pain_points_summary.md
│   │       └── objection_handling_guide.md
│   │
│   ├── transcripts/
│   │   ├── 2025-07-15_abbas-rezaei-colton.md     ← Processed with frontmatter
│   │   ├── 2025-07-15_erik-meza-colton.md
│   │   └── ... (15-20 total)
│   │
│   ├── pain_points/
│   │   ├── credit-card-limits.md
│   │   ├── payment-processing-complexity.md
│   │   └── ... (discovered patterns)
│   │
│   ├── objections/
│   │   ├── pricing-too-expensive.md
│   │   ├── insufficient-volume.md
│   │   └── ...
│   │
│   ├── personas/
│   │   ├── construction-buyer.md
│   │   └── ...
│   │
│   ├── use_cases/
│   │   ├── high-volume-ap.md
│   │   └── ...
│   │
│   └── README.md
│
├── 02_content/
│   ├── _synthesis/
│   └── README.md
│
├── 03_market/
│   ├── _synthesis/
│   ├── competitor_analysis/
│   └── README.md
│
├── taxonomy.yaml                               ← Updated with emergent tags
├── ontology.yaml                               ← Universal ontology
└── CURRENT_TAXONOMY_SNAPSHOT.md                ← Baseline health metrics
```

---

## Execution Workflow

### ITERATION 1: First Batch (15 transcripts)

#### Step 1: Setup Structure (5 minutes)

**Task:** Create directory structure

**Commands:**
```bash
cd knowledge_base

# Create foundation
mkdir -p 00_foundation

# Create customer domain with subdirs
mkdir -p 01_customer/_synthesis
mkdir -p 01_customer/transcripts
mkdir -p 01_customer/pain_points
mkdir -p 01_customer/objections
mkdir -p 01_customer/personas
mkdir -p 01_customer/use_cases

# Create content domain
mkdir -p 02_content/_synthesis

# Create market domain
mkdir -p 03_market/_synthesis
mkdir -p 03_market/competitor_analysis
```

**Output:** Clean directory structure ready for population

---

#### Step 2: Process First 5 Transcripts (Parallel Fanout-Fanin)

**Pattern:** Launch 3 extraction perspectives per transcript in parallel

**For Each Transcript (e.g., `001_abbas-rezaei...md`):**

**Agent 1: Pain Point Extractor**
```yaml
task: "Extract all customer pain points mentioned in this transcript"
output:
  pain_points:
    - name: "insufficient-volume-for-discount"
      quote: "800,000 in credit card spend isn't really enough to hit threshold"
      speaker: "Colton"
      context: "Explaining volume requirements for rate discount"

    - name: "customers-prefer-ach-over-credit-card"
      quote: "all the customers, they pay ACH, every single one of them"
      speaker: "Erik"
      context: "Objection to using Nickel for AR"
```

**Agent 2: Objection Extractor**
```yaml
task: "Extract all sales objections and how they were handled"
output:
  objections:
    - objection: "pricing-too-expensive"
      quote: "800,000 annually... not enough to hit threshold"
      response: "Explained need for $2M+ volume + AR usage for discounts"
      outcome: "Objection not fully resolved, prospect considering"

    - objection: "customers-wont-use-credit-card"
      quote: "all the customers, they pay ACH"
      response: "Shared data: 17% of invoices paid via credit card across 10K customers"
      outcome: "Prospect open to considering"
```

**Agent 3: Persona & Use Case Extractor**
```yaml
task: "Extract persona indicators and use case patterns"
output:
  persona_signals:
    - persona: "distribution-buyer"
      indicators:
        - "Fortune 500 companies as customers"
        - "50-100K transaction sizes"
        - "5-10 ACH/month"
      confidence: 0.85

  use_cases:
    - use_case: "high-volume-ap-processing"
      indicators:
        - "500K-800K annual AP spend"
        - "5-10 ACH transactions monthly"
      fit: "Below volume threshold (needs $2M+)"

    - use_case: "quickbooks-integration"
      indicators:
        - "Operating on QuickBooks Online"
        - "Office manager handles"
      fit: "Good match for automation"
```

**Synthesis Agent: Consolidate**
```
Input: 3 extraction outputs per transcript
Output: Single processed transcript markdown with frontmatter
```

**Execute this pattern for first 5 transcripts in parallel.**

**Output:** 5 processed transcripts with rich frontmatter + extracted patterns

---

#### Step 3: Generate Pattern Documents (30 minutes)

From the 5 extracted transcripts, create pattern documents:

**Example: Pain Point Document**
```markdown
---
name: CREDIT_CARD_LIMITS
description: Customers hit credit card limits when making large B2B purchases, need alternative payment
domain: customer
node_type: pattern
status: emergent
last_updated: 2025-10-24
tags:
  - customer
  - pain-points
  - credit-limits
  - payment-processing
topics:
  - b2b-payment-limits
  - credit-card-constraints
  - large-transaction-processing
related_docs:
  - "[[high-volume-ap]]"
  - "[[payment-processing-complexity]]"
  - "[[nickel_icp_and_positioning]]"
validated_by: []  # Will populate in Phase 3
---

# Credit Card Limits Pain Point

**Pattern Discovered:** 2025-10-24 (Iteration 1, 5 transcripts processed)
**Frequency:** 3/5 transcripts mention variations of this pain
**Confidence:** High (multiple independent mentions)

## Description

B2B buyers frequently hit credit card limits when trying to make large purchases ($50K-$100K+), preventing them from earning points or taking advantage of payment float. This is especially acute for construction and distribution companies with large material orders.

## Evidence from Transcripts

### Transcript 1: Erik Meza (Distribution)
> "50 to 100 thousand dollars... anywhere between 500,000 to maybe 800,000 annually"

**Context:** Discussing AP transaction volumes and credit card spend limits.

### Transcript 2: [Another mention]
[Quote and context]

## Associated Personas

- [[construction-buyer]]
- [[distribution-buyer]]
- [[b2b-services-buyer]]

## Related Pain Points

- [[insufficient-volume-for-discounts]]
- [[accounts-receivable-challenges]]

## Nickel Solution Mapping

**How Nickel Addresses:**
- High credit limits available for B2B transactions
- Combined AP + AR approach increases total volume for discounts
- Credit card points on business spend

**Competitive Advantage:**
- Traditional processors: Lower limits or don't specialize in B2B
- Banks: Limited credit card programs for AP

## Next Steps for Validation

- [ ] Confirm pattern in next 10 transcripts (Iteration 2)
- [ ] Quantify frequency across full transcript corpus
- [ ] Extract more customer quotes for synthesis docs
```

**Repeat for:**
- 3-5 pain point documents
- 3-5 objection documents
- 2-3 persona documents
- 2-3 use case documents

**Output:** ~15 pattern documents with emergent tags

---

#### Step 4: Emergent Tag Discovery (15 minutes)

**Task:** Identify tags used but NOT in seed taxonomy

**Process:**
1. Scan all generated frontmatter
2. Compare tags to seed taxonomy YAML
3. Group by frequency
4. Classify by type (pain, objection, persona, etc.)

**Example Output:**
```yaml
emergent_tags_iteration1:
  discovered_count: 12 new tags

  pain_points:
    - insufficient-volume-for-discounts (frequency: 3 transcripts)
    - customers-prefer-ach (frequency: 2 transcripts)
    - fortune-500-customer-requirements (frequency: 2 transcripts)

  objections:
    - cant-promise-ar-adoption (frequency: 2 transcripts)

  personas:
    - fortune-500-distributor (frequency: 2 transcripts)

  use_cases:
    - payment-term-discount-optimization (frequency: 2 transcripts)

  competitors:
    - paypal-zelle-venmo (frequency: 1 transcript) # Low frequency, may consolidate
```

**Validation:**
- ✅ Keep tags with frequency >= 2 transcripts
- ❌ Flag single-use tags for review (may be noise or need more data)

---

#### Step 5: Update Taxonomy YAML (10 minutes)

```yaml
# Add to taxonomy.yaml

version: 1.0.0
status: iterating # Phase 2 Nucleation in progress
iteration: 1
docs_processed: 5

domains:
  - name: foundation
    status: active
  - name: customer
    status: active
  - name: content
    status: active
  - name: market
    status: active

context_types:
  pain_points:
    # Seed tags
    - name: credit-card-limits
      status: validated  # Observed in 3/5 transcripts
      frequency: 3
      discovered: seed

    # Emergent tags
    - name: insufficient-volume-for-discounts
      status: emergent
      frequency: 3
      discovered: 2025-10-24
      notes: "Customers under $2M threshold can't get rate discounts"

    - name: customers-prefer-ach
      status: emergent
      frequency: 2
      discovered: 2025-10-24
      notes: "Objection: customers won't pay via credit card, prefer ACH"

# ... Continue for all context types

evolution_metrics:
  iteration_1:
    seed_tags_used: 8 (60%)
    seed_tags_unused: 5 (40%)
    emergent_tags_discovered: 12 (40% growth)
    tag_stability: 60%
    decision: "Run Iteration 2 (not yet stable)"
```

---

#### Step 6: Iteration Decision (5 minutes)

**Metrics:**
```yaml
iteration_1_quality:
  transcripts_processed: 5
  tags_from_seed: 8 (60%)
  tags_emergent: 12 (40%)
  new_tag_rate: 40%
  stability_score: 60%

thresholds:
  stability_required: >= 90%
  new_tag_rate_max: <= 10%

decision: "RUN ITERATION 2 - Not yet stable"
```

**Rationale:** 40% new tag rate indicates taxonomy still evolving. Process next 10 transcripts with updated taxonomy.

---

### ITERATION 2: Next 10 Transcripts (1-2 hours)

**Process:** Repeat Steps 2-5 with remaining 10 transcripts

**Key Differences:**
- Use UPDATED taxonomy (includes Iteration 1 emergent tags)
- Expect fewer new tags (taxonomy more complete)
- Focus on validating patterns vs discovering new ones

**Expected Metrics:**
```yaml
iteration_2_quality:
  transcripts_processed: 10 (total 15)
  tags_from_updated_taxonomy: 18 (85%)
  tags_emergent_new: 3 (15%)
  new_tag_rate: 15%
  stability_score: 85%

decision: "NEAR STABLE - Consider Iteration 3 or proceed to synthesis stub creation"
```

---

## Detailed Frontmatter Template

### For Transcripts

```yaml
---
name: YYYY-MM-DD_CUSTOMER_NAME_MEETING_TYPE
description: Sales call with [customer] discussing [primary topics]
domain: customer
node_type: transcript
status: emergent
last_updated: YYYY-MM-DD
meeting_date: YYYY-MM-DD
duration_minutes: XX
participants:
  - name: "Colton O'Farrell"
    role: "Nickel Sales"
  - name: "[Customer Name]"
    role: "[Customer Role]"
    company: "[Company]"
tags:
  - customer
  - transcript
  - sales-call
  - [persona-tag]
  - [industry-tag]
topics:
  - pricing-negotiation
  - volume-requirements
  - [other-topics]
related_docs:
  - "[[pain_points_summary]]"
  - "[[objection_handling_guide]]"
  - "[[credit-card-limits]]"
  - ... (minimum 3)

# Extracted Patterns
pain_points_mentioned:
  - "[[credit-card-limits]]"
  - "[[insufficient-volume-for-discounts]]"
objections_raised:
  - "[[pricing-too-expensive]]"
  - "[[customers-prefer-ach]]"
use_cases_discussed:
  - "[[high-volume-ap-processing]]"
  - "[[quickbooks-integration]]"
personas_identified:
  - "[[distribution-buyer]]"
outcome: "qualified-opportunity|objection-unresolved|disqualified"
---

# [Meeting Title]

**Date:** YYYY-MM-DD
**Duration:** XX minutes
**Outcome:** [qualified/unresolved/disqualified]

## Summary

[2-3 sentence summary of call]

## Key Insights

**Pain Points:**
- [Bulleted pain points with quotes]

**Objections:**
- [Bulleted objections with responses]

**Use Cases:**
- [Bulleted use cases discussed]

## Full Transcript

[Original transcript preserved]

## Next Steps

- [ ] [Action items from call]
```

### For Pain Points

```yaml
---
name: PAIN_POINT_NAME
description: One-sentence description of the pain pattern
domain: customer
node_type: pattern
status: emergent|validated
last_updated: YYYY-MM-DD
discovered_date: YYYY-MM-DD
tags:
  - customer
  - pain-points
  - [specific-tag]
topics:
  - [topic1]
  - [topic2]
  - [topic3]
related_docs:
  - "[[persona-doc]]"
  - "[[use-case-doc]]"
  - "[[nickel-solution-doc]]"
validated_by: []  # Populate in Phase 3

# Pattern Metadata
frequency: X  # Number of transcripts mentioning
confidence: high|medium|low
personas_affected:
  - "[[persona1]]"
  - "[[persona2]]"
---

# [Pain Point Name]

**Pattern Discovered:** YYYY-MM-DD
**Frequency:** X/Y transcripts
**Confidence:** [Level]

## Description

[Detailed description of pain pattern]

## Evidence from Transcripts

### Transcript 1: [Name]
> "[Direct quote]"

**Context:** [Situation]

[Repeat for 2-3 strongest examples]

## Associated Personas

- [[persona1]] - [Why this persona experiences this pain]
- [[persona2]] - [Why]

## Related Pain Points

- [[related-pain1]]
- [[related-pain2]]

## Nickel Solution Mapping

**How Nickel Addresses:**
- [Solution point 1]
- [Solution point 2]

**Competitive Advantage:**
- [Competitor weakness 1]
- [Competitor weakness 2]
```

---

## Quality Gates

### After Iteration 1 (5 transcripts):
- [ ] All 5 transcripts processed with frontmatter
- [ ] 10-15 pattern documents created
- [ ] Emergent tags identified and documented
- [ ] Taxonomy YAML updated
- [ ] Iteration decision made (metrics calculated)

### After Iteration 2 (15 transcripts total):
- [ ] All 15 transcripts processed
- [ ] 20-30 pattern documents created
- [ ] Tag stability >= 85% (low new tag rate)
- [ ] Zero orphan documents (all have >= 3 related_docs)
- [ ] Taxonomy ready for Phase 3 (batch processing)

### Final Output Quality:
- [ ] Domain tag compliance: 100% (first tag = domain)
- [ ] Linking compliance: 100% (>= 3 related_docs)
- [ ] Frontmatter validation: 100% (all required fields present)
- [ ] Evidence preservation: Direct quotes in pattern docs
- [ ] Attribution: All patterns cite source transcripts

---

## Output Deliverables

### 1. Processed Knowledge Graph
**Location:** `knowledge_base/`
**Contents:**
- 15-20 processed transcripts with rich frontmatter
- 20-30 pattern documents (pain points, objections, personas, use cases)
- Clean directory structure (foundation, customer, content, market)

### 2. Taxonomy Evolution Report
**File:** `_AGENT_WORKSPACE/taxonomy_evolution_report.md`
**Contents:**
```markdown
# Nickel Taxonomy Evolution Report
## Phase 2: Nucleation - Iteration 1 & 2

### Summary
- Transcripts processed: 15
- Seed tags validated: 8/13 (62%)
- Emergent tags discovered: 15 (54% growth)
- Final tag count: 28
- Tag stability: 87%

### Iteration Metrics

| Iteration | Transcripts | Seed Tags Used | Emergent Tags | New Tag Rate | Stability |
|-----------|-------------|----------------|---------------|--------------|-----------|
| 1         | 5           | 8 (60%)        | 12 (40%)      | 40%          | 60%       |
| 2         | 10          | 18 (85%)       | 3 (15%)       | 15%          | 85%       |

**Decision:** Stable enough for Phase 3 (Crystallization)

### Top Validated Patterns

#### Pain Points (by frequency)
1. credit-card-limits (8 transcripts)
2. insufficient-volume-for-discounts (7 transcripts)
3. customers-prefer-ach (5 transcripts)

#### Objections (by frequency)
1. pricing-too-expensive (9 transcripts)
2. cant-promise-ar-adoption (4 transcripts)

#### Personas Identified
1. distribution-buyer (6 transcripts)
2. construction-buyer (5 transcripts)
3. b2b-services-buyer (4 transcripts)

### Recommendations for Phase 3

1. **Synthesis Documents to Create:**
   - Customer Pain Points Summary (roll up 20+ pain point mentions)
   - Objection Handling Guide (roll up 15+ objection patterns)
   - Persona Profiles (consolidate persona indicators)

2. **Remaining Transcripts to Process:**
   - Batch 2: Process remaining ~35 transcripts from CSV
   - Use validated taxonomy (87% stable)
   - Expect <10% new tags

3. **Quality Improvements:**
   - Consolidate tag variants (e.g., "customers-prefer-ach" vs "customer-ach-preference")
   - Add more cross-linking (currently averaging 4 related_docs, target 5+)
   - Enrich pattern documents with more quotes
```

### 3. Updated Taxonomy YAML
**File:** `knowledge_base/taxonomy.yaml`
**Status:** Validated, 87% stable, ready for scale

### 4. Synthesis Stubs
**Location:** `knowledge_base/01_customer/_synthesis/`
**Files:**
- `customer_exec_summary.md` (stub with TODO)
- `pain_points_summary.md` (stub with TODO)
- `objection_handling_guide.md` (stub with TODO)

---

## Tools & Scripts

### Use Existing Script (If Applicable)
**File:** `process_transcripts.py`
**Check if:** This script can be adapted for extraction tasks

### Python Helper for Batch Operations
```python
# Example: Parallel extraction helper
import concurrent.futures
from pathlib import Path

def process_transcript(transcript_path, extractors):
    """Process single transcript with multiple extractors in parallel"""
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {
            executor.submit(extractor, transcript_path): name
            for name, extractor in extractors.items()
        }
        for future in concurrent.futures.as_completed(futures):
            extractor_name = futures[future]
            results[extractor_name] = future.result()
    return results

# Extractors
extractors = {
    'pain_points': extract_pain_points,
    'objections': extract_objections,
    'personas': extract_personas
}

# Process batch
transcript_dir = Path('knowledge_base/meetings_md')
for transcript in sorted(transcript_dir.glob('*.md'))[:15]:
    results = process_transcript(transcript, extractors)
    generate_processed_output(transcript, results)
```

---

## Anti-Patterns to Avoid

### ❌ Processing Sequentially
**Wrong:** Process 15 transcripts one-by-one (4+ hours)
**Right:** Use Parallel Fanout-Fanin (1-2 hours)

### ❌ Ignoring Emergent Patterns
**Wrong:** Only use seed taxonomy, force-fit all tags
**Right:** Document new tags, iterate taxonomy

### ❌ Skipping Iteration 2
**Wrong:** Stop after 5 transcripts, assume taxonomy complete
**Right:** Validate stability with second batch

### ❌ Missing Attribution
**Wrong:** Pattern documents without source citations
**Right:** Every claim has transcript citation with quote

### ❌ Orphan Documents
**Wrong:** Documents with 0-2 related_docs links
**Right:** Minimum 3 related_docs per document

---

## Success Criteria

**Speed:**
- ✅ 15 transcripts processed in 2-4 hours (vs 7+ hours manual)
- ✅ <15 min per transcript average

**Quality:**
- ✅ 85%+ tag stability achieved
- ✅ 20-30% taxonomy growth (healthy emergent discovery)
- ✅ Zero orphan documents
- ✅ 100% domain tag compliance
- ✅ Evidence preserved (direct quotes in all pattern docs)

**Readiness:**
- ✅ Batch processing workflow validated
- ✅ Taxonomy ready for Phase 3 scale (remaining 35 transcripts)
- ✅ Synthesis stubs created
- ✅ Pattern library established (20-30 docs)

---

## Next Steps After Completion

### Immediate (You'll Do)
1. Review taxonomy evolution report
2. Validate quality of processed transcripts (spot check 3-5)
3. Approve emergent tags for inclusion in taxonomy
4. Green-light Phase 3 (batch processing remaining transcripts)

### Phase 3 (Future Agent or Next Sprint)
1. Process remaining 35+ transcripts with validated taxonomy
2. Populate synthesis stubs (create actual summaries)
3. Evidence-based promotion (emergent → validated)
4. Health baseline (run taxonomy snapshot)

---

## EXECUTE NOW

**Start Here:**
1. Create directory structure (Step 1)
2. Process first 5 transcripts with Parallel Fanout-Fanin (Step 2)
3. Generate pattern documents (Step 3)
4. Identify emergent tags (Step 4)
5. Update taxonomy (Step 5)
6. Decide on Iteration 2 (Step 6)
7. Complete Iteration 2 with remaining 10 transcripts
8. Generate final deliverables

**Time Budget:** 2-4 hours total
**Output:** Tangible knowledge graph foundation + taxonomy evolution report

**GO!**
