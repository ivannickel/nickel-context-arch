# Orchestrator Agent Brief v2.0: Nickel GTM Context Architecture Execution

**Status:** Phase 0 Complete → Ready for Corpus-Wide Extraction
**Updated:** 2025-10-30
**Approach:** Corpus-Wide Specialist Agents (NOT Per-Transcript Iteration)

---

## Mission

You are the orchestrator agent responsible for executing corpus-wide extraction across 165 sales call transcripts to build a comprehensive GTM intelligence knowledge graph for Nickel (payment platform company).

**Project:** Nickel GTM Context Architecture
**System Type:** Iterative context layering with corpus-wide pattern detection
**Execution Pattern:** 6 specialist agents × 1 corpus (parallel)
**Total Execution Time:** 4-5 hours (vs 40+ hours for per-transcript approach)
**Complexity:** Breadth + depth "oil drilling" strategy, cross-transcript frequency tracking

---

## What Just Happened (Context)

### ✅ Phase 0 Complete (Foundation Seeded)

The foundation layer has been seeded from 68 raw_context documents:

**Created:**
- 12 baseline nodes in `knowledge_base/00_foundation/`
  - `icp/icp-definition.md`
  - `icp/ideal-verticals.md`
  - `icp/anti-icp.md`
  - `positioning/positioning-statement.md`
  - `positioning/target-segments.md`
  - `product/quickbooks-integration.md`
  - `product/core-capabilities.md`
  - `value_props/supplier-finance-platform.md`
  - `business_model/revenue-model.md`
  - `business_model/key-metrics.md`
  - `competitive_intel/competitive-landscape.md`
  - `market/industry-trends.md`

**Status:** All nodes have `status: baseline`, ready for transcript validation

### ⚠️ Execution Approach Changed (CRITICAL)

**OLD Approach (REJECTED):**
- 6 extractors per transcript × 165 transcripts = 990 agent executions
- Sequential per-transcript processing
- 40+ hours execution time
- Inefficient, redundant processing

**NEW Approach (CORPUS-WIDE):**
- 6 specialist agents × 1 corpus = 6 parallel executions
- Each agent uses lexical search (Grep) to find relevant transcripts corpus-wide
- Process filtered subset deeply (40-120 transcripts per agent)
- Build cross-transcript patterns with frequency data
- 2-3 hours execution time

This is the "oil drilling strategy":
1. **Breadth:** Survey entire corpus with lexical search (Grep)
2. **Filter:** Identify high-signal transcripts for each domain
3. **Depth:** Process filtered subset deeply
4. **Extract:** Build cross-transcript patterns with frequencies

---

## Critical Concepts (Read Carefully)

### 1. Corpus-Wide Processing (NOT Per-Transcript)

**WRONG (what we rolled back from):**
```
For transcript 1:
  Spawn WHO/WHAT/WHY/HOW/WHERE_WHEN/META extractors
  Output: dimensional_annotations/transcript_1/*.yaml

For transcript 2:
  Spawn WHO/WHAT/WHY/HOW/WHERE_WHEN/META extractors
  Output: dimensional_annotations/transcript_2/*.yaml

...repeat 165 times (990 agent executions, 40+ hours)
```

**RIGHT (corpus-wide approach):**
```
WHO Corpus Analyst:
  Grep: Find ALL transcripts with persona signals (finds ~80-100)
  Process: Read and extract from filtered subset
  Output: Create/update nodes in knowledge_base/01_customer/personas/
  Build: Frequency data (persona X appeared in Y of 165 transcripts)

WHAT Corpus Analyst:
  Grep: Find ALL transcripts with pain signals (finds ~100-120)
  Process: Read and extract from filtered subset
  Output: Create/update nodes in knowledge_base/01_customer/pain_points/
  Build: Frequency data

...6 agents total, all run in PARALLEL (6 executions, 2-3 hours)
```

**Key Difference:**
- OLD: Process transcripts sequentially, each gets 6 agents
- NEW: Process domains in parallel, each agent surveys entire corpus

### 2. Two-Layer Validation Loop (Unchanged)

**Foundation Layer** (`00_foundation/`): Nickel's STATED strategy from raw_context
- Example: "ICP sweet spot is $5-25M (Whale segment)"
- Status: baseline → validating → validated → canonical

**Customer Layer** (`01_customer/`): Market REALITY from transcripts
- Example: 60% of personas are $1-5M (Fish segment), not Whale
- Status: emergent → validated → canonical

**Context_Weaver validates:**
- If transcripts CONFIRM foundation → Add validation signals
- If transcripts CONTRADICT foundation → Flag contradiction

### 3. Node Lifecycle Progression (Unchanged)

**Customer nodes:**
- emergent (freq=1) → validated (freq≥2) → canonical (freq≥5)

**Foundation nodes:**
- baseline (raw_context) → validating (1 validation) → validated (2+ validations) → canonical (5+ validations)

**Confidence scores increase:**
- Formula: `base_confidence + (log10(source_count + 1) × 1.5)`
- 3.5 → 7.5 → 9.0+ based on source accumulation

---

## Your First Steps (DO THESE IMMEDIATELY)

### Step 1: Read the Practical Execution Plan (10 min)

**File:** `_AGENT_WORKSPACE/PRACTICAL_EXECUTION_PLAN.md`

This is your PRIMARY instruction manual for corpus-wide execution. Read entire document before spawning agents. It contains:

- Current state check (verify Phase 0 complete)
- Agent launch instructions (single message, 6 Task calls)
- Lexical search patterns for each agent
- Expected workflow per agent (breadth → depth → synthesis)
- Output structure after completion
- Quality gates (revalidation ≥60%, discovery ≥20%, quality ≥85%)

**CRITICAL:** This replaces the per-transcript orchestration guide. The execution pattern is fundamentally different.

### Step 2: Read the Corpus-Wide Extraction Plan (5 min)

**File:** `_AGENT_WORKSPACE/CORPUS_WIDE_EXTRACTION_PLAN.md`

Understand the oil drilling strategy:

- Why this works better (6 executions vs 990)
- How each agent uses lexical search (Grep patterns)
- Cross-transcript pattern detection with frequencies
- Agent communication & coordination (no dependencies)
- Time estimates (2-3 hours parallel execution)

### Step 3: Verify System State (5 min)

**Check Phase 0 completion:**
```bash
# Foundation exists (12 baseline nodes)
ls knowledge_base/00_foundation/*/*.md | wc -l
# Should show: 12

# Transcripts ready
ls knowledge_base/meetings_md/ | wc -l
# Should show: 165

# Customer directories exist (may be empty)
ls knowledge_base/01_customer/
# Should see: personas/, pain_points/, objections/, use_cases/, product_requirements/, discovery_triggers/, market_segments/
```

**If foundation missing:** Phase 0 not complete, abort.
**If transcripts missing:** Cannot proceed, abort.
**If customer directories missing:** Create them:

```bash
mkdir -p knowledge_base/01_customer/personas
mkdir -p knowledge_base/01_customer/pain_points
mkdir -p knowledge_base/01_customer/objections
mkdir -p knowledge_base/01_customer/use_cases
mkdir -p knowledge_base/01_customer/product_requirements
mkdir -p knowledge_base/01_customer/discovery_triggers
mkdir -p knowledge_base/01_customer/market_segments
```

### Step 4: Launch Corpus-Wide Extraction (NOW)

**Send a SINGLE message with 6 concurrent Task tool calls:**

```
Launch 6 corpus-wide analysts in parallel using oil drilling strategy:

1. WHO Corpus Analyst
   - Domain: Personas, buyer profiles, ICP signals, firmographics
   - Use Grep to find persona/firmographic signals across all 165 transcripts
   - Grep patterns:
     * "(owner|ceo|cfo|coo|vp|director|controller|manager|principal|founder)"
     * "(employee|staff|headcount|revenue|\$.*million|margin)"
   - Process relevant subset (~80-100 transcripts)
   - Create/update persona nodes in knowledge_base/01_customer/personas/
   - Build frequency data (persona X appeared in Y of 165 transcripts)
   - Update taxonomy.yaml personas section

2. WHAT Corpus Analyst
   - Domain: Pain points, use cases, product fit signals
   - Use Grep to find pain/use case signals across all 165 transcripts
   - Grep patterns:
     * "(problem|pain|challenge|issue|struggling|difficult|frustrated)"
     * "(quickbooks|integration|automation|process|workflow)"
   - Process relevant subset (~100-120 transcripts)
   - Create/update pain_points and use_cases nodes
   - Build frequency data (pain X appeared in Y transcripts)
   - Update taxonomy.yaml pain_points and use_cases sections

3. WHY Corpus Analyst
   - Domain: Objections, competitive intelligence, buyer motivations
   - Use Grep to find competitive/objection signals across all 165 transcripts
   - Grep patterns:
     * "(melio|relay|bill\.com|quickbooks payment|competitor|currently using)"
     * "(concern|worried|hesitant|not sure|volume|threshold|expensive)"
   - Process relevant subset (~70-90 transcripts)
   - Create/update objections nodes
   - UPDATE foundation competitive_intel nodes with transcript evidence
   - Build frequency data (objection X appeared in Y transcripts)
   - Update taxonomy.yaml objections section

4. HOW Corpus Analyst
   - Domain: Product requirements, feature requests, integration needs
   - Use Grep to find product requirement signals across all 165 transcripts
   - Grep patterns:
     * "(need|require|must have|looking for|feature|integration|api)"
     * "(quickbooks|xero|netsuite|salesforce|hubspot)"
   - Process relevant subset (~90-110 transcripts)
   - Create/update product_requirements nodes
   - UPDATE foundation product nodes with validation signals
   - Build frequency data (requirement X appeared in Y transcripts)
   - Validate QuickBooks blocker frequency
   - Update taxonomy.yaml product_requirements section

5. WHERE_WHEN Corpus Analyst
   - Domain: Journey stage, discovery triggers, buying signals
   - Use Grep to find journey/trigger signals across all 165 transcripts
   - Grep patterns:
     * "(demo|trial|evaluation|considering|comparing|ready to|decision)"
     * "(fraud|cash flow crisis|lost customer|new contract|growth)"
   - Process relevant subset (~60-80 transcripts)
   - Create/update discovery_triggers nodes
   - Build frequency data (trigger X appeared in Y transcripts)
   - Identify journey stage distribution across personas
   - Update taxonomy.yaml discovery_triggers section

6. META Corpus Analyst
   - Domain: Market context, segment insights, trends, macro patterns
   - Use Grep to find market/segment signals across all 165 transcripts
   - Grep patterns:
     * "(construction|building materials|wholesale|manufacturing|distribution)"
     * "(market|industry|trend|shift|changing|growth)"
   - Process relevant subset (~50-70 transcripts)
   - Create/update market_segments nodes
   - Build frequency data (segment X appeared in Y transcripts)
   - Validate foundation market assumptions
   - Update taxonomy.yaml market_segments section

All agents should:
- Work independently across entire corpus (NOT per-transcript)
- Use lexical search patterns above to filter relevant transcripts
- Semantic matching: UPDATE existing nodes vs CREATE new (check taxonomy.yaml)
- Frequency tracking: pattern appeared in X of 165 transcripts
- Status progression: emergent → validated → canonical based on frequency
- Evidence chains with cross-transcript quotes
- Update taxonomy.yaml with frequencies
- Generate completion report with:
  * Transcripts processed: X of 165
  * Patterns found: Y total (Z new, W updated)
  * Frequencies calculated: [top 10 patterns]
  * Foundation validations: [confirmations + contradictions]
  * Quality metrics: [pattern revalidation %, new discovery %]

Expected completion: 2-3 hours (all agents run in parallel)
```

---

## Execution Sequence (End-to-End)

### ✅ PHASE 0: Foundation Seeding (COMPLETE)

**Status:** Complete
**Output:** 12 baseline nodes in `00_foundation/`
**Next:** Proceed to Phase 1 (Corpus-Wide Extraction)

---

### PHASE 1: Corpus-Wide Extraction (2-3 hours)

**Purpose:** Build customer layer with cross-transcript patterns and frequencies

**Step 1.1: Launch All 6 Agents (NOW)**
- Send single message with 6 Task calls (see Step 4 above)
- All agents spawn and begin breadth search (lexical filtering)

**Step 1.2: Agent Execution (2-3 hours, parallel)**
Each agent independently:
1. **Breadth Search (5-10 min):** Use Grep to find relevant transcripts corpus-wide
2. **Depth Analysis (60-90 min):** Process filtered subset, extract patterns
3. **Cross-Transcript Synthesis (20-30 min):** Calculate frequencies, update status
4. **Foundation Validation (15-20 min):** Update foundation nodes with evidence
5. **Output Generation (10-15 min):** Write nodes, update taxonomy, generate report

**Step 1.3: Monitor Completion**
Each agent will return a completion report showing:
- Transcripts processed: X of 165
- Nodes created: Y new nodes
- Nodes updated: Z existing nodes
- Frequencies calculated: Top patterns with counts
- Foundation validations: Confirmations + contradictions flagged
- Quality metrics: Pattern revalidation %, new discovery %

---

### PHASE 2: Validation & Quality Check (60-90 min)

**Step 2.1: Run Validation_Analyst**

**Purpose:** Check corpus-wide extraction quality

**Metrics to validate:**

1. **Pattern Revalidation Rate (Target: ≥60%)**
   - Baseline patterns in strategic_lens: 67
   - How many appeared in corpus? Should be ≥40 patterns
   - Examples:
     * QuickBooks integration: Should be 80%+ frequency
     * Volume threshold objection: Should be 20-30% frequency
     * Payment processing fees pain: Should be 50%+ frequency

2. **New Discovery Rate (Target: ≥20%)**
   - Expected: ≥13 new patterns NOT in strategic_lens
   - Examples:
     * Accounting firm buyer hypothesis validation
     * Relay Financial competitive threat assessment
     * W-9/1099 automation frequency
     * Multi-client dashboard need

3. **Overall Quality (Target: ≥85%)**
   - All nodes have frequency data
   - All nodes have cross-transcript evidence
   - Status progression logic applied correctly
   - taxonomy.yaml updated with frequencies
   - Foundation validation signals added

**Decision Matrix:**

- **GO:** All 3 metrics pass → Proceed to Phase 3 (Synthesis)
- **REFINE:** 1-2 metrics pass → Adjust lens, reprocess subset
- **NO-GO:** 0 metrics pass → Root cause analysis, human escalation

**Step 2.2: Run Context_Weaver**

**Purpose:** Build foundation ↔ customer connections

**Tasks:**
- Validate foundation nodes with transcript evidence
- Generate wiki-links between layers
- Update node status progression
- Recalculate confidence scores
- Flag contradictions (foundation claim vs transcript reality)

**Expected output:**
- Foundation nodes updated: baseline → validating/validated
- Wiki-links added: `[[persona-slug]]` in foundation nodes
- Contradictions flagged: ICP mismatch, segment distribution, etc.

---

### PHASE 3: Synthesis & Deliverables (After Phase 2 Pass)

**Purpose:** Generate strategic roll-ups and insights

**Tasks:**
1. Create synthesis documents (persona playbook, objection handling guide, etc.)
2. Generate strategic bridges between domains
3. Create frequency distribution reports
4. Build pattern validation matrix
5. Document contradictions and strategic implications

**Note:** Phase 3 execution details to be defined after Phase 2 validation passes.

---

## Expected Output Structure

After corpus-wide extraction completes:

```
knowledge_base/
├── 01_customer/
│   ├── personas/
│   │   ├── payment-upgraders-business-owner.md     # freq: 42, status: canonical
│   │   ├── cash-savvy-sellers-business-owner.md    # freq: 38, status: canonical
│   │   ├── accounting-firm-buyer.md                # freq: 4, status: emergent
│   │   └── [7-17 more persona nodes with frequency data]
│   │
│   ├── pain_points/
│   │   ├── payment-processing-fees.md              # freq: 89, status: canonical
│   │   ├── customers-asking-for-net-terms.md       # freq: 67, status: canonical
│   │   ├── volume-threshold-barriers.md            # freq: 42, status: canonical
│   │   └── [12-27 more pain nodes with frequency data]
│   │
│   ├── objections/
│   │   ├── volume-threshold-too-high.md            # freq: 42, status: canonical
│   │   ├── existing-solution-satisfaction.md       # freq: 23, status: validated
│   │   └── [8-18 more objection nodes with frequency data]
│   │
│   ├── use_cases/
│   │   ├── quickbooks-integration.md               # freq: 147, status: canonical, blocker: true
│   │   ├── ar-automation-processing.md             # freq: 103, status: canonical
│   │   └── [8-18 more use case nodes with frequency data]
│   │
│   ├── product_requirements/
│   │   ├── quickbooks-online-integration.md        # freq: 147, blocker: true
│   │   ├── w9-1099-automation.md                   # freq: 34, status: validated
│   │   └── [12-22 more requirement nodes with frequency data]
│   │
│   ├── discovery_triggers/
│   │   ├── fraud-incident-trigger.md               # freq: 28, status: validated
│   │   ├── net-terms-customer-requests.md          # freq: 67, status: canonical
│   │   └── [6-13 more trigger nodes with frequency data]
│   │
│   └── market_segments/
│       ├── building-materials-distribution.md      # freq: 72, 44% of corpus
│       ├── construction-trades.md                  # freq: 48, 29% of corpus
│       └── [3-8 more segment nodes with frequency data]
│
├── 00_foundation/ (UPDATED with validation signals)
│   ├── icp/icp-definition.md                       # UPDATED: validated by 89 transcripts
│   ├── competitive_intel/competitive-landscape.md  # UPDATED: Relay threat confirmed (23 mentions)
│   └── product/quickbooks-integration.md           # UPDATED: Universal requirement (147 of 165)
│
└── taxonomy.yaml (UPDATED with frequencies)
    ├── personas: [freq data for all personas across corpus]
    ├── pain_points: [freq data with canonical patterns identified]
    ├── objections: [freq data with validated handling strategies]
    ├── use_cases: [freq data with blocker flags]
    ├── product_requirements: [freq data with priority rankings]
    ├── discovery_triggers: [freq data with conversion patterns]
    └── market_segments: [freq data with segment performance]
```

---

## Critical Gotchas (From Mock Execution)

### Will Definitely Happen:

1. **Agents process sequentially instead of parallel**
   - Fix: Send SINGLE message with 6 Task calls, NOT 6 separate messages

2. **Agents try per-transcript iteration instead of corpus-wide**
   - Fix: Explicitly instruct "work across ALL 165 transcripts" in spawn command

3. **Duplicate nodes created (semantic matching fails)**
   - Fix: Each agent MUST check taxonomy.yaml before creating nodes

4. **Frequency stuck at 1 (UPDATE logic not working)**
   - Fix: Verify agents are incrementing frequencies when updating existing nodes

5. **Status progression not happening**
   - Fix: Agents MUST check: if freq ≥2 → status = validated, if freq ≥5 → canonical

6. **Evidence missing line numbers**
   - Fix: Require [VERIFIED: file.md:42-67] format, reject vague citations

7. **Foundation nodes not updated with validation signals**
   - Fix: WHY and HOW agents MUST update foundation competitive_intel and product nodes

8. **taxonomy.yaml not updated with frequencies**
   - Fix: Each agent MUST append to taxonomy.yaml with frequency counts

9. **Wiki-links broken (target doesn't exist)**
   - Fix: Context_Weaver verifies target node exists before adding [[link]]

10. **Contradictions not flagged**
    - Fix: Context_Weaver Step 5 runs contradiction detection logic

---

## Success Criteria

You've succeeded when:

✅ **Corpus-wide extraction complete:** All 6 agents finished, 2-3 hours execution
✅ **Nodes created/updated:** 80-130 customer nodes with frequency data
✅ **Frequency distribution clear:** 15-25 canonical patterns (freq ≥5)
✅ **Status progression working:** emergent → validated → canonical based on freq
✅ **Foundation updated:** 12 baseline nodes have validation signals added
✅ **Contradictions flagged:** Foundation vs transcript reality documented
✅ **Quality maintained:** Pattern revalidation ≥60%, new discovery ≥20%, quality ≥85%
✅ **taxonomy.yaml enriched:** Frequency counts for all patterns
✅ **Validation passed:** Checkpoint 2 = GO decision

---

## Error Recovery

### If Agent Fails:

**Non-Critical Failures:**
- Discovery trigger agent timeout → Log error, continue with other 5 agents
- Grep returns 0 results → Expected for some domains, continue

**Critical Failures:**
- Agent crashes on semantic matching → STOP, debug agent, restart
- taxonomy.yaml corrupted → STOP, restore from git, restart
- Multiple agents fail → STOP, root cause analysis

**Recovery procedure:**
1. Check agent completion reports (which agents finished?)
2. Verify taxonomy.yaml integrity (is YAML valid?)
3. Count customer nodes created (does count match expected?)
4. If partial failure, rerun failed agents only
5. If systematic failure, root cause before retrying

---

## Final Instructions

1. **Read PRACTICAL_EXECUTION_PLAN.md in full** (10 min, don't skip)
2. **Verify system state** (Phase 0 complete? 165 transcripts ready?)
3. **Launch all 6 agents in SINGLE message** (Step 4 spawn command above)
4. **Monitor completion** (2-3 hours, check agent reports as they finish)
5. **Run Validation_Analyst** (check quality gates: revalidation ≥60%, discovery ≥20%, quality ≥85%)
6. **Run Context_Weaver** (build foundation ↔ customer connections)
7. **Decision:** GO/REFINE/NO-GO based on validation results

**Execution time:** 4-5 hours total (2-3 hours extraction + 1-2 hours validation/synthesis)

**Primary references:**
- `_AGENT_WORKSPACE/PRACTICAL_EXECUTION_PLAN.md` (execution instructions)
- `_AGENT_WORKSPACE/CORPUS_WIDE_EXTRACTION_PLAN.md` (strategy explanation)

**Current directory:** `gtm_engagements/03_active_client/nickel_ivan/nickel_gtm_context_architecture/`

---

## Questions to Ask if Stuck

1. "Am I running agents in PARALLEL?" (single message, 6 Task calls)
2. "Are agents working across ALL transcripts?" (corpus-wide, not per-transcript)
3. "Is taxonomy.yaml being updated with frequencies?" (check after each agent)
4. "Are nodes being UPDATED or duplicated?" (semantic matching working?)
5. "Should I stop and escalate, or can I recover?" (critical vs non-critical failures)

---

**You have all the instructions. Phase 0 is complete. Execute Phase 1 now.**

**This is your mission. Begin with launching the 6 corpus-wide analysts. Good luck.**
