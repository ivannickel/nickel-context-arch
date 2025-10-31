# Practical Execution Plan: Corpus-Wide Extraction

**Status:** Ready to Execute (Phase 0 Complete, Foundation Seeded)
**Pattern:** 6 Specialist Agents × 1 Corpus (NOT per-transcript iteration)
**Time:** 2-3 hours (all agents in parallel)
**Next Step:** Launch all 6 agents in SINGLE message

---

## Executive Summary

**What You're About To Do:**
- Launch 6 domain specialists that work across ALL 165 transcripts
- Each agent uses lexical search (Grep) to find their relevant subset (40-120 transcripts)
- Each agent processes their subset deeply, building cross-transcript patterns
- All 6 run in parallel → 2-3 hours total vs 40+ hours sequential

**Critical Understanding:**
- This is NOT "6 agents × 165 transcripts" (990 executions) ❌
- This IS "6 agents × 1 corpus" (6 parallel executions) ✅

---

## Current State Check

**Before launching, verify:**

```bash
# 1. Foundation exists (Phase 0 complete)
ls knowledge_base/00_foundation/
# Should see: icp/, positioning/, product/, competitive_intel/, etc.

# 2. Transcripts ready
ls knowledge_base/meetings_md/ | wc -l
# Should show: 165 transcript files

# 3. Directory structure exists
ls knowledge_base/01_customer/
# Should see: personas/, pain_points/, objections/, use_cases/, etc.
```

**If any missing:** Phase 0 not complete, do not proceed.

---

## Agent Launch Instructions

### Step 1: Launch All 6 Agents in Parallel

**CRITICAL:** Send a SINGLE message with 6 concurrent Task tool calls.

**Spawn Command:**

```
Launch the following 6 corpus-wide analysts in parallel:

1. WHO Corpus Analyst - Process personas, ICP signals, firmographics across all 165 transcripts
2. WHAT Corpus Analyst - Process pain points, use cases across all 165 transcripts
3. WHY Corpus Analyst - Process objections, competitive intel across all 165 transcripts
4. HOW Corpus Analyst - Process product requirements, feature gaps across all 165 transcripts
5. WHERE_WHEN Corpus Analyst - Process journey stages, triggers across all 165 transcripts
6. META Corpus Analyst - Process market context, segment insights across all 165 transcripts

Each agent should:
- Use Grep to find relevant transcripts corpus-wide (lexical search patterns below)
- Filter to high-signal subset (40-120 transcripts per domain)
- Process filtered subset deeply
- Create/update nodes in knowledge_base/01_customer/
- Build cross-transcript frequency data
- Update taxonomy.yaml with pattern frequencies
- Generate completion report
```

---

## Lexical Search Patterns (For Each Agent)

### WHO Corpus Analyst

**Domain:** Personas, buyer profiles, ICP signals, firmographics

**Grep Patterns:**
```bash
# Persona signals
Grep: pattern="(owner|ceo|cfo|coo|vp|director|controller|manager|principal|founder)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"

# Firmographic signals
Grep: pattern="(employee|staff|headcount|revenue|\$.*million|margin)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"
```

**Expected Output:**
- ~80-100 relevant transcripts identified
- 10-20 persona nodes created/updated in `knowledge_base/01_customer/personas/`
- Frequency data: persona X appeared in Y of 165 transcripts
- Status progression: emergent → validated → canonical

---

### WHAT Corpus Analyst

**Domain:** Pain points, use cases, product fit signals

**Grep Patterns:**
```bash
# Pain signals
Grep: pattern="(problem|pain|challenge|issue|struggling|difficult|frustrated)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"

# Use case signals
Grep: pattern="(quickbooks|integration|automation|process|workflow)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"
```

**Expected Output:**
- ~100-120 relevant transcripts identified
- 15-30 pain point nodes created/updated in `knowledge_base/01_customer/pain_points/`
- 10-20 use case nodes created/updated in `knowledge_base/01_customer/use_cases/`
- Frequency distribution: QuickBooks universal (89%)? Volume threshold (25%)?

---

### WHY Corpus Analyst

**Domain:** Objections, competitive intelligence, buyer motivations

**Grep Patterns:**
```bash
# Competitive mentions
Grep: pattern="(melio|relay|bill\.com|quickbooks payment|competitor|currently using)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"

# Objection signals
Grep: pattern="(concern|worried|hesitant|not sure|volume|threshold|expensive)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"
```

**Expected Output:**
- ~70-90 relevant transcripts identified
- 10-20 objection nodes created/updated in `knowledge_base/01_customer/objections/`
- Competitive intel: How many Relay mentions? Satisfaction level?
- Foundation nodes UPDATED: `00_foundation/competitive_intel/*.md` with transcript evidence

---

### HOW Corpus Analyst

**Domain:** Product requirements, feature requests, integration needs

**Grep Patterns:**
```bash
# Product requirement signals
Grep: pattern="(need|require|must have|looking for|feature|integration|api)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"

# Specific integrations
Grep: pattern="(quickbooks|xero|netsuite|salesforce|hubspot)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"
```

**Expected Output:**
- ~90-110 relevant transcripts identified
- 15-25 product requirement nodes created/updated in `knowledge_base/01_customer/product_requirements/`
- QuickBooks blocker frequency validation
- W-9/1099 automation frequency? Multi-client dashboard requests?
- Foundation nodes UPDATED: `00_foundation/product/*.md` with validation signals

---

### WHERE_WHEN Corpus Analyst

**Domain:** Journey stage, discovery triggers, buying signals

**Grep Patterns:**
```bash
# Stage signals
Grep: pattern="(demo|trial|evaluation|considering|comparing|ready to|decision)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"

# Trigger events
Grep: pattern="(fraud|cash flow crisis|lost customer|new contract|growth)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"
```

**Expected Output:**
- ~60-80 relevant transcripts identified
- 8-15 discovery trigger nodes created/updated in `knowledge_base/01_customer/discovery_triggers/`
- Journey stage distribution across personas
- Time-to-close patterns by persona type

---

### META Corpus Analyst

**Domain:** Market context, segment insights, trends, macro patterns

**Grep Patterns:**
```bash
# Industry signals
Grep: pattern="(construction|building materials|wholesale|manufacturing|distribution)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"

# Market trend signals
Grep: pattern="(market|industry|trend|shift|changing|growth)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"
```

**Expected Output:**
- ~50-70 relevant transcripts identified
- 5-10 market segment nodes created/updated in `knowledge_base/01_customer/market_segments/`
- Segment distribution: building materials 40%? construction 30%?
- Validation of foundation market assumptions

---

## Expected Workflow Per Agent

**Each agent will execute this workflow independently:**

### Phase 1: Breadth Search (5-10 min)
```yaml
1. Use Grep to find relevant transcripts across entire corpus
2. Filter by extraction_priority: high/medium (from frontmatter)
3. Identify high-signal subset (40-120 transcripts)
4. Log: "Found X transcripts with [domain] signals"
```

### Phase 2: Depth Analysis (60-90 min)
```yaml
1. Read each relevant transcript
2. Extract domain-specific patterns
3. For each pattern:
   a. Check taxonomy.yaml - does pattern exist?
   b. If YES → UPDATE existing node (increment frequency, add evidence)
   c. If NO → CREATE new node (frequency: 1, status: emergent)
4. Build cross-transcript evidence chains
```

### Phase 3: Cross-Transcript Synthesis (20-30 min)
```yaml
1. Calculate frequencies: pattern appeared in X of 165 transcripts
2. Update status based on frequency:
   - freq = 1 → emergent
   - freq ≥ 2 → validated
   - freq ≥ 5 → canonical
3. Build evidence trails with quotes from multiple transcripts
4. Update taxonomy.yaml with frequencies
```

### Phase 4: Foundation Validation (15-20 min)
```yaml
1. Check if customer patterns validate foundation claims
2. Update foundation nodes with transcript evidence
3. Flag contradictions if evidence conflicts
   Example: Foundation says "Whale segment ideal" but 60% transcripts are Fish
```

### Phase 5: Output Generation (10-15 min)
```yaml
1. Write all nodes to knowledge_base/
2. Update taxonomy.yaml
3. Generate agent completion report:
   - Transcripts processed: X of 165
   - Patterns found: Y total (Z new, W updated)
   - Frequencies calculated: [list top 10]
   - Foundation validations: [list confirmations + contradictions]
   - Quality metrics: [pattern revalidation %, new discovery %]
```

---

## Output Structure After Completion

```
knowledge_base/
├── 01_customer/
│   ├── personas/
│   │   ├── payment-upgraders-business-owner.md  # freq: 42, status: canonical
│   │   ├── cash-savvy-sellers-business-owner.md  # freq: 38, status: canonical
│   │   ├── accounting-firm-buyer.md              # freq: 4, status: emergent
│   │   └── [7-17 more persona nodes]
│   │
│   ├── pain_points/
│   │   ├── payment-processing-fees.md            # freq: 89, status: canonical
│   │   ├── customers-asking-for-net-terms.md     # freq: 67, status: canonical
│   │   ├── volume-threshold-barriers.md          # freq: 42, status: canonical
│   │   └── [12-27 more pain nodes]
│   │
│   ├── objections/
│   │   ├── volume-threshold-too-high.md          # freq: 42, status: canonical
│   │   ├── existing-solution-satisfaction.md     # freq: 23, status: validated (Relay threat)
│   │   └── [8-18 more objection nodes]
│   │
│   ├── use_cases/
│   │   ├── quickbooks-integration.md             # freq: 147, status: canonical, blocker: true
│   │   ├── ar-automation-processing.md           # freq: 103, status: canonical
│   │   └── [8-18 more use case nodes]
│   │
│   ├── product_requirements/
│   │   ├── quickbooks-online-integration.md      # freq: 147, blocker: true
│   │   ├── w9-1099-automation.md                 # freq: 34, status: validated
│   │   ├── multi-client-dashboard.md             # freq: 4, status: emergent (accounting firms)
│   │   └── [12-22 more requirement nodes]
│   │
│   ├── discovery_triggers/
│   │   ├── fraud-incident-trigger.md             # freq: 28, status: validated
│   │   ├── net-terms-customer-requests.md        # freq: 67, status: canonical
│   │   └── [6-13 more trigger nodes]
│   │
│   └── market_segments/
│       ├── building-materials-distribution.md    # freq: 72, 44% of corpus
│       ├── construction-trades.md                # freq: 48, 29% of corpus
│       └── [3-8 more segment nodes]
│
├── 00_foundation/  (UPDATED with validation signals)
│   ├── icp/icp-definition.md                     # UPDATED: ICP validated by 89 transcripts
│   ├── competitive_intel/competitive-landscape.md # UPDATED: Relay threat confirmed (23 mentions)
│   └── product/quickbooks-integration.md         # UPDATED: Universal requirement (147 of 165)
│
└── taxonomy.yaml  (UPDATED with frequencies)
    ├── personas: [freq data for all personas across corpus]
    ├── pain_points: [freq data with canonical patterns identified]
    ├── objections: [freq data with validated handling strategies]
    ├── use_cases: [freq data with blocker flags]
    ├── product_requirements: [freq data with priority rankings]
    ├── discovery_triggers: [freq data with conversion patterns]
    └── market_segments: [freq data with segment performance]
```

---

## Quality Gates

**After all 6 agents complete, check:**

### Pattern Revalidation (Target: ≥60%)
```yaml
Baseline patterns in strategic_lens: 67
Expected revalidation: ≥40 patterns appear in corpus

Check:
- QuickBooks integration: Should be 80%+ frequency
- Volume threshold objection: Should be 20-30% frequency
- Payment processing fees pain: Should be 50%+ frequency
```

### New Discovery (Target: ≥20%)
```yaml
Expected: ≥13 new patterns NOT in strategic_lens

Examples:
- Accounting firm buyer hypothesis validation
- Relay Financial competitive threat assessment
- W-9/1099 automation frequency
- Multi-client dashboard need
```

### Quality Maintained (Target: ≥85%)
```yaml
Check:
- All nodes have frequency data ✓
- All nodes have cross-transcript evidence ✓
- Status progression logic applied ✓
- taxonomy.yaml updated ✓
- Foundation validation performed ✓
```

---

## Success Criteria

**GO Decision (Proceed to Deliverables):**
- ✅ Pattern revalidation ≥60% (40+ patterns confirmed)
- ✅ New discovery ≥20% (13+ new patterns found)
- ✅ Quality maintained ≥85%
- ✅ Frequency data shows clear winners (3-5 canonical patterns per domain)
- ✅ Foundation validations complete (contradictions flagged if any)

**REFINE Decision (Iterate):**
- ⚠️ Pattern revalidation 40-60% (adjust lens, reprocess)
- ⚠️ New discovery <20% (may be too narrow lens)
- ⚠️ Quality 70-85% (fix evidence chains, reprocess)

**NO-GO Decision (Abort):**
- ❌ Pattern revalidation <40% (wrong market, wrong lens)
- ❌ Quality <70% (systematic extraction failures)

---

## Execution Timeline

**Hour 0: Launch**
- Send single message with 6 Task calls
- All agents spawn and begin breadth search

**Hour 0.5: Breadth Complete**
- Each agent has identified their relevant subset
- Total transcripts processed across all agents: 400-600 (overlap expected)

**Hour 2-3: Depth Analysis Complete**
- Nodes created/updated across 6 domains
- Frequency data calculated
- Evidence chains built

**Hour 3-4: Synthesis & Validation**
- Foundation nodes updated with validation signals
- taxonomy.yaml updated with frequencies
- Agent reports generated

**Hour 4: Quality Check**
- Review quality metrics
- GO/REFINE/NO-GO decision

---

## Common Pitfalls to Avoid

### ❌ Don't Do This:
1. **Per-transcript iteration:** "Process transcript 1, then transcript 2, then..."
2. **Sequential agents:** "Wait for WHO to finish, then run WHAT"
3. **Dimensional annotations:** Creating `dimensional_annotations/[transcript]/WHO_extraction.yaml`
4. **Ignoring existing nodes:** Creating duplicates instead of updating

### ✅ Do This:
1. **Corpus-wide processing:** "Grep ALL transcripts, filter to relevant subset, process deeply"
2. **Parallel execution:** "Launch all 6 agents at once in single message"
3. **Direct node creation:** Creating/updating `knowledge_base/01_customer/personas/[name].md`
4. **Semantic matching:** Check taxonomy.yaml before creating new nodes

---

## Launch Checklist

Before executing, confirm:

- [ ] Phase 0 complete (foundation seeded, 12 baseline nodes exist)
- [ ] 165 transcripts in `knowledge_base/meetings_md/`
- [ ] Directory structure exists (`01_customer/personas/`, etc.)
- [ ] `taxonomy.yaml` exists (even if minimal)
- [ ] You understand this is 6 agents × 1 corpus (NOT per-transcript)
- [ ] You will launch all 6 agents in SINGLE message
- [ ] You know expected outputs (nodes in knowledge_base/, not dimensional_annotations/)

---

## Next Step: Execute Now

**Copy this prompt into your next message:**

```
Launch 6 corpus-wide analysts in parallel using oil drilling strategy:

1. WHO Corpus Analyst - Use Grep to find persona/firmographic signals across all 165 transcripts, process relevant subset (~80-100 transcripts), create/update persona nodes in knowledge_base/01_customer/personas/, build frequency data

2. WHAT Corpus Analyst - Use Grep to find pain/use case signals across all 165 transcripts, process relevant subset (~100-120 transcripts), create/update pain_points and use_cases nodes, build frequency data

3. WHY Corpus Analyst - Use Grep to find competitive/objection signals across all 165 transcripts, process relevant subset (~70-90 transcripts), create/update objections nodes + update foundation competitive_intel, build frequency data

4. HOW Corpus Analyst - Use Grep to find product requirement signals across all 165 transcripts, process relevant subset (~90-110 transcripts), create/update product_requirements nodes + update foundation product nodes, build frequency data

5. WHERE_WHEN Corpus Analyst - Use Grep to find journey/trigger signals across all 165 transcripts, process relevant subset (~60-80 transcripts), create/update discovery_triggers nodes, build frequency data

6. META Corpus Analyst - Use Grep to find market/segment signals across all 165 transcripts, process relevant subset (~50-70 transcripts), create/update market_segments nodes, build frequency data

Each agent:
- Works independently across entire corpus (NOT per-transcript)
- Uses lexical search patterns from CORPUS_WIDE_EXTRACTION_PLAN.md
- Semantic matching: UPDATE existing nodes vs CREATE new
- Frequency tracking: pattern appeared in X of 165 transcripts
- Status progression: emergent → validated → canonical
- Evidence chains with cross-transcript quotes
- Update taxonomy.yaml with frequencies
- Generate completion report

Expected: 2-3 hours, all agents complete in parallel
```

---

**Status:** READY TO EXECUTE
**Pattern:** Corpus-Wide Specialist Agents (6 × 1)
**Time:** 2-3 hours
**Output:** 80-130 nodes with frequency data + foundation validation
