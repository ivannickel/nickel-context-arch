# Corpus-Wide Extraction Plan: Oil Drilling Strategy

**Pattern:** 6 specialist agents work across ALL 165 transcripts using breadth + depth
**Execution:** All 6 agents run in parallel (NOT per-transcript iteration)
**Time:** ~3-5 hours total (vs 40+ hours for per-transcript approach)

---

## Core Concept: Agentic Lexical Search + Domain Specialization

Each agent is a **domain specialist** that:
1. Uses lexical search (Grep) to identify high-signal transcripts corpus-wide
2. Filters to relevant subset (e.g., WHO agent finds 87 transcripts mentioning personas)
3. Processes only relevant transcripts deeply
4. Builds cross-transcript patterns and frequencies
5. Creates/updates nodes with accumulated evidence

**This is like oil drilling:**
- Breadth: Survey entire field with seismic data (lexical search)
- Identify: Find promising deposits (high-signal transcripts)
- Depth: Drill deep only where oil is likely (targeted analysis)
- Extract: Pull out the resource (patterns + evidence)

---

## 6 Specialist Agents (Run in Parallel)

### Agent 1: WHO Corpus Analyst
**Domain:** Personas, buyer profiles, ICP signals, firmographics

**Breadth Search (Grep):**
```bash
# Find transcripts with persona signals
Grep: pattern="(owner|cfo|controller|vp.*finance|director|manager|principal|founder)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"

# Find transcripts with firmographic signals
Grep: pattern="(employee|staff|headcount|revenue|\$.*million|margin)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"
```

**Depth Analysis:**
- Process ~80-100 transcripts with persona signals
- Extract: Personas, company profiles, buyer characteristics
- Pattern: Accounting firm buyer (freq across corpus?), Business owner patterns
- Update: taxonomy.yaml personas section, foundation ICP nodes

**Output:**
- `knowledge_base/01_customer/personas/*.md` (10-20 persona nodes)
- Each node has frequency count (appeared in X of 165 transcripts)
- Status: emergent (freq=1) → validated (freq≥2) → canonical (freq≥5)

---

### Agent 2: WHAT Corpus Analyst
**Domain:** Pain points, use cases, product fit signals

**Breadth Search:**
```bash
# Find transcripts with pain signals
Grep: pattern="(problem|pain|challenge|issue|struggling|difficult|frustrated)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"

# Find transcripts with use case signals
Grep: pattern="(quickbooks|integration|automation|process|workflow)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"
```

**Depth Analysis:**
- Process ~100-120 transcripts with pain/use case signals
- Extract: Pain points with severity, use cases with fit indicators
- Pattern: QuickBooks universal? Volume threshold frequency?
- Quantify: Impact metrics (cost, time, revenue)

**Output:**
- `knowledge_base/01_customer/pain_points/*.md` (15-30 nodes)
- `knowledge_base/01_customer/use_cases/*.md` (10-20 nodes)
- Frequency distribution shows which pains are universal vs niche

---

### Agent 3: WHY Corpus Analyst
**Domain:** Objections, competitive intelligence, buyer motivations

**Breadth Search:**
```bash
# Find transcripts with competitive mentions
Grep: pattern="(melio|relay|bill\.com|quickbooks payment|competitor|currently using)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"

# Find transcripts with objection signals
Grep: pattern="(concern|worried|hesitant|not sure|volume|threshold|expensive)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"
```

**Depth Analysis:**
- Process ~70-90 transcripts with competitive/objection signals
- Extract: Competitive positioning, customer satisfaction, objection patterns
- Critical: Melio/Relay threat assessment (how many mentions? satisfaction level?)
- Pattern: Volume threshold objection frequency

**Output:**
- `knowledge_base/01_customer/objections/*.md` (10-20 nodes)
- `knowledge_base/00_foundation/competitive_intel/*.md` (UPDATE with transcript evidence)
- Competitive landscape validated by actual customer mentions

---

### Agent 4: HOW Corpus Analyst
**Domain:** Product requirements, feature requests, integration needs

**Breadth Search:**
```bash
# Find transcripts with product requirement signals
Grep: pattern="(need|require|must have|looking for|feature|integration|api)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"

# Find transcripts with specific integrations
Grep: pattern="(quickbooks|xero|netsuite|salesforce|hubspot)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"
```

**Depth Analysis:**
- Process ~90-110 transcripts with product requirement signals
- Extract: Critical requirements (QuickBooks blocker?), feature gaps, integration needs
- Pattern: W-9/1099 automation frequency, multi-entity dashboard requests
- Priority: Blockers vs nice-to-have

**Output:**
- `knowledge_base/01_customer/product_requirements/*.md` (15-25 nodes)
- `knowledge_base/00_foundation/product/*.md` (UPDATE with validation signals)
- Clear requirement frequency → product roadmap prioritization

---

### Agent 5: WHERE_WHEN Corpus Analyst
**Domain:** Journey stage, discovery triggers, buying signals

**Breadth Search:**
```bash
# Find transcripts with stage signals
Grep: pattern="(demo|trial|evaluation|considering|comparing|ready to|decision)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"

# Find transcripts with trigger events
Grep: pattern="(fraud|cash flow crisis|lost customer|new contract|growth)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"
```

**Depth Analysis:**
- Process ~60-80 transcripts with journey/trigger signals
- Extract: Funnel stage distribution, discovery triggers, time-to-close patterns
- Pattern: Persona-specific journey patterns (owner = fast, CFO = slow?)
- Triggers: What events prompt Nickel search?

**Output:**
- `knowledge_base/01_customer/discovery_triggers/*.md` (8-15 nodes)
- Journey stage distribution across personas
- Time-to-close benchmarks by persona type

---

### Agent 6: META Corpus Analyst
**Domain:** Market context, segment insights, trends, macro patterns

**Breadth Search:**
```bash
# Find transcripts with industry signals
Grep: pattern="(construction|building materials|wholesale|manufacturing|distribution)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"

# Find transcripts with market trend signals
Grep: pattern="(market|industry|trend|shift|changing|growth)"
      glob="knowledge_base/meetings_md/*.md"
      output_mode="files_with_matches"
```

**Depth Analysis:**
- Process ~50-70 transcripts with market/segment signals
- Extract: Segment distribution (building materials 40%? construction 30%?)
- Pattern: Which verticals convert best? Regional patterns?
- Trends: AR vs AP adoption, credit card willingness

**Output:**
- `knowledge_base/01_customer/market_segments/*.md` (5-10 nodes)
- Segment performance data (conversion, retention, LTV)
- Validation of foundation market assumptions

---

## Execution Sequence

**Step 1: Launch All 6 Agents in Parallel** (single message, 6 Task calls)

```javascript
// SINGLE MESSAGE with 6 concurrent Task tool calls

Task 1: WHO_Corpus_Analyst
Task 2: WHAT_Corpus_Analyst
Task 3: WHY_Corpus_Analyst
Task 4: HOW_Corpus_Analyst
Task 5: WHERE_WHEN_Corpus_Analyst
Task 6: META_Corpus_Analyst
```

**Step 2: Each Agent Workflow**

```
1. Breadth Search (5-10 min):
   - Use Grep to find relevant transcripts
   - Filter by extraction_priority: high/medium
   - Identify high-signal subset (40-120 transcripts per agent)

2. Depth Analysis (60-90 min):
   - Read each relevant transcript
   - Extract domain-specific patterns
   - Check taxonomy.yaml for existing patterns (semantic matching)
   - Decision: CREATE new node OR UPDATE existing node

3. Cross-Transcript Synthesis (20-30 min):
   - Calculate frequencies (pattern appeared in X transcripts)
   - Update status (emergent → validated → canonical)
   - Build evidence trails (quotes from multiple transcripts)
   - Update taxonomy.yaml with frequencies

4. Foundation Validation (15-20 min):
   - Check if patterns validate foundation claims
   - Update foundation nodes with transcript evidence
   - Flag contradictions if evidence conflicts

5. Output Generation (10-15 min):
   - Write nodes to knowledge_base/
   - Update taxonomy.yaml
   - Generate agent report
```

**Step 3: Validation & Synthesis** (after all 6 agents complete)

- Run Validation_Analyst: Check pattern revalidation, quality metrics
- Run Context_Weaver: Build wiki-links, validate foundation comprehensively
- Decision: Quality sufficient? Proceed to deliverables.

---

## Why This Works Better

**vs Per-Transcript Iteration (6 agents × 165 transcripts):**
- ❌ 990 agent executions
- ❌ 40+ hours
- ❌ Redundant processing (reading same transcript 6 times)

**vs Single Agent Per Transcript (1 agent × 165 transcripts):**
- ❌ 165 agent executions
- ❌ 15-20 hours
- ❌ Sequential processing (slow)

**Corpus-Wide Specialist Agents (6 agents × 1 corpus):**
- ✅ 6 agent executions (parallel)
- ✅ 3-5 hours total
- ✅ Intelligent filtering (only process relevant transcripts)
- ✅ Cross-transcript pattern detection (frequencies emerge naturally)
- ✅ Efficient: WHO agent reads 87 transcripts, WHAT agent reads 103 (some overlap is fine)

---

## Lexical Search Patterns

**Effective Grep patterns per domain:**

**WHO (Personas):**
- Decision makers: `"(owner|ceo|cfo|coo|vp|director|controller|manager|principal)"`
- Company size: `"(\d+\s*(employee|staff|people|team member))"`
- Revenue signals: `"(\$\d+\s*(million|m|k|revenue|sales))"`

**WHAT (Pains/Use Cases):**
- Pain language: `"(problem|pain|challenge|issue|struggle|difficult|frustrat)"`
- Use case language: `"(looking for|need|want to|trying to|hoping to)"`
- Specific pains: `"(cash flow|payment|reconciliation|fraud|manual)"`

**WHY (Competition/Objections):**
- Competitors: `"(melio|relay|bill\.com|fundbox|quickbooks payment)"`
- Objection language: `"(concern|worried|hesitant|but|however|issue with)"`
- Satisfaction signals: `"(happy with|satisfied|love|works well|easy)"`

**HOW (Requirements):**
- Must-haves: `"(need|require|must have|blocker|critical)"`
- Integrations: `"(integrat|connect|sync|api|webhook)"`
- Specific tools: `"(quickbooks|xero|netsuite|salesforce)"`

**WHERE_WHEN (Journey):**
- Stage signals: `"(demo|trial|evaluat|consider|compar|decision)"`
- Urgency: `"(asap|urgent|soon|timeline|deadline)"`
- Trigger events: `"(fraud|crisis|problem|lost|new contract)"`

**META (Market/Segment):**
- Industries: `"(construction|building|wholesale|manufacturing|distribution)"`
- Trends: `"(market|industry|trend|changing|shift)"`
- Performance: `"(growth|scaling|expand)"`

---

## Agent Communication & Coordination

**No inter-agent dependencies:**
- Each agent works independently on their domain
- Overlap is GOOD (transcript relevant to multiple domains)
- No coordination needed (parallel execution)

**Shared resources:**
- All agents read: strategic_lens.yaml, taxonomy.yaml (read-only during execution)
- All agents update: taxonomy.yaml (append-only, atomic updates)
- All agents write: knowledge_base/ (different subdirectories, no conflicts)

**Conflict resolution:**
- If 2 agents create same node (rare): Manual merge after execution
- Taxonomy updates: Each agent appends to their section (personas, pain_points, etc.)
- Frequency tracking: Handled per-agent domain

---

## Output Structure

**After 6 agents complete:**

```
knowledge_base/
├── 01_customer/
│   ├── personas/ (10-20 nodes, freq data, cross-transcript evidence)
│   ├── pain_points/ (15-30 nodes, severity + frequency)
│   ├── objections/ (10-20 nodes, handling strategies)
│   ├── use_cases/ (10-20 nodes, fit indicators)
│   ├── product_requirements/ (15-25 nodes, blocker flags)
│   ├── discovery_triggers/ (8-15 nodes, trigger → conversion patterns)
│   └── market_segments/ (5-10 nodes, segment performance)
│
├── 00_foundation/ (existing baseline nodes)
│   └── (UPDATED with transcript validation signals)
│
└── taxonomy.yaml
    ├── personas: [freq data across corpus]
    ├── pain_points: [freq data]
    ├── objections: [freq data]
    ├── use_cases: [freq data]
    ├── product_requirements: [freq data]
    ├── discovery_triggers: [freq data]
    └── market_segments: [freq data]
```

**Frequency distribution emerges naturally:**
- QuickBooks integration: 147 of 165 transcripts (89%) → canonical
- Volume threshold objection: 42 of 165 (25%) → validated
- Accounting firm buyer: 4 of 165 (2%) → emergent (needs validation)

---

## Quality Metrics

**Pattern revalidation:**
- Strategic_lens.yaml baseline: 67 patterns
- Expected revalidation: ≥60% (40+ patterns appear in corpus)

**New discoveries:**
- Expected: ≥20% new patterns (13+ patterns not in lens)

**Coverage:**
- High-priority transcripts: 100% processed by at least 1 agent
- Medium-priority: 80%+ processed
- Low-priority: 50%+ processed

**Cross-domain validation:**
- Personas linked to pain points (WHO ↔ WHAT)
- Objections linked to competitive intel (WHY ↔ WHY)
- Requirements linked to use cases (HOW ↔ WHAT)

---

## Time Estimates

**Per Agent (parallel execution):**
- Breadth search: 5-10 min
- Depth analysis: 60-90 min (processing 40-120 transcripts)
- Cross-transcript synthesis: 20-30 min
- Foundation validation: 15-20 min
- Output generation: 10-15 min
- **Total per agent: 110-165 min (2-3 hours)**

**All 6 agents in parallel: 2-3 hours**

**Post-processing:**
- Validation_Analyst: 60-90 min
- Context_Weaver: 60-90 min

**Total execution: 4-5 hours** (vs 40+ hours for per-transcript approach)

---

## Next Steps

1. **Launch 6 corpus analysts in parallel** (single message, 6 Task calls)
2. **Wait for completion** (2-3 hours)
3. **Run validation** (Validation_Analyst)
4. **Run synthesis** (Context_Weaver)
5. **Quality check** (pattern revalidation ≥60%, new discovery ≥20%, quality ≥85%)
6. **Proceed to deliverables** (if quality passes)

**This is the efficient, intelligent approach.**
