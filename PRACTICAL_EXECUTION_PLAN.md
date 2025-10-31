# Practical Execution Plan: Lens Creation → Transcript Processing

**Date:** 2025-10-30
**Context:** You have high-value Nickel context + upgraded dimensional system
**Location:** Cursor window for nickel_gtm_context_architecture directory
**Goal:** Create strategic lens → Process transcripts with dimensional extractors

---

## Current State Assessment

### ✅ What You Have
1. **Iteration 1 Complete** - 5 transcripts processed (traditional nucleation)
   - 88% quality baseline
   - 67 patterns in taxonomy.yaml v1.2.0
   - 31 knowledge graph nodes
   - 4 strategic discoveries (3 need validation)

2. **High-Value Nickel Context** - Direct from stakeholder
   - ICP definition
   - Competitive intelligence
   - Positioning/messaging
   - Strategic priorities

3. **Upgraded System Specs** - Dimensional + Pixee methodology
   - Strategic lens schema defined
   - 6 dimensional extractors spec'd
   - Context lineage standard
   - Validation checkpoint framework

4. **Raw Transcripts Available** - 160 remaining (165 total)
   - GTM Build Update meetings (weekly sync calls)
   - Strategy sessions
   - Onboarding guides
   - Customer feature requests
   - Domain context docs

### ❌ What You Don't Have (Yet)
1. `strategic_lens.yaml` - Needs to be created from taxonomy + Nickel context
2. Dimensional annotation files - Will be created during processing
3. Agent extractor implementations - Can use specs as prompts
4. Validation Report 1 - Will be generated after sample batch

---

## What You're Overthinking

### ❌ SKIP: Retroactive Dimensional Annotations for Iteration 1
**Why:** You said "take updated system + high value context to create lenses then process transcripts"
- You're moving forward, not backward
- Iteration 1 (5 transcripts) already extracted via traditional nucleation
- 31 existing nodes are sufficient foundation
- **Don't retrofit** - preserve as-is, start fresh with dimensional on remaining 160

**Impact:** Saves 2-3 hours of retroactive annotation work

### ❌ SKIP: Context Lineage Retrofit for 31 Existing Nodes
**Why:** You're processing forward, not auditing backward
- Existing 31 nodes have quotes/sources (good enough)
- Line-level attribution is nice-to-have, not blocker
- Apply Pixee standard to NEW nodes only

**Impact:** Saves 30-45 min of retrofit work

### ❌ SKIP: Formal Checkpoint 1 Validation Meeting
**Why:** You already received "high-value context" from Nickel
- Context intake already happened (informally)
- You have strategic priorities direct from stakeholder
- No need for formal 90-min validation meeting yet
- Validate through results (sample batch quality)

**Impact:** Saves 2 hours of meeting prep + execution

### ❌ SKIP: Agent Implementation Files
**Why:** You're working in Cursor with Claude Code
- Agent specs are prompts, not implementations
- Use extractor specs as system prompts directly
- No need to write Python/TS agent code
- Claude Code IS the agent runtime

**Impact:** Saves 4-6 hours of implementation work

---

## What You're NOT Overthinking (Keep These)

### ✅ KEEP: Strategic Lens Creation
**Why:** This is your guidance system
- Encodes Nickel's priorities as data
- Enables strategic_fit scoring
- Guides dimensional extraction focus
- **Critical foundation piece**

**Time:** 60-90 min (one-time investment)

### ✅ KEEP: Dimensional Extraction Approach
**Why:** This scales quality
- 6 parallel perspectives per transcript
- Strategic_fit scoring per extraction
- Systematic coverage (not emergent luck)
- Preserves 88% quality at scale

**Time:** 2-3 hours per 10 transcripts

### ✅ KEEP: Context Lineage for NEW Nodes Only
**Why:** Attribution matters for future audit
- Line-level references enable verification
- Unique_value explains why source matters
- Apply to new extractions only (not retroactive)

**Time:** Built into extraction process (no extra time)

### ✅ KEEP: Sample Batch Validation Thinking
**Why:** Prevents scaling misaligned patterns
- Process 10-20 transcripts first
- Check pattern revalidation rate
- Adjust lens if needed before scaling
- But: No formal meeting required (self-validate)

**Time:** 2 hours analysis after sample batch

---

## Simplified Execution Flow

### Phase 1: Create Strategic Lens (60-90 min)

**Input:**
- `taxonomy.yaml` v1.2.0 (67 patterns from Iteration 1)
- High-value Nickel context (ICP, positioning, priorities)

**Process:**
1. Open Cursor in nickel_gtm_context_architecture directory
2. Read taxonomy.yaml (67 patterns)
3. Read Nickel context documents (ICP, positioning, etc.)
4. Create `strategic_lens.yaml` with this structure:

```yaml
strategic_lens:
  version: "1.0"
  based_on: "taxonomy v1.2.0 + Nickel stakeholder context"

  who:  # From personas + Nickel ICP
    target_personas:
      - name: "Accounting Firm Buyer"
        priority: 1
        criteria: [...]
        strategic_value: "150x multiplier"
        needs_validation: true

    anti_personas:
      - name: "New Business <6 months"
        reason: "Compliance denial risk"

  what:  # From pain_points + use_cases
    critical_pain_points:
      - name: "volume-threshold-barriers"
        priority: 1
        frequency: 6
        strategic_fit: 9

    validated_use_cases:
      - name: "quickbooks-integration"
        priority: 1
        frequency: 4
        strategic_fit: 10

  why:  # From objections + competitors
    critical_objections: [...]
    competitive_threats:
      - name: "relay-financial"
        priority: 1

  how:  # From feature gaps/requirements
    feature_gaps: [...]

  where_when:  # From journey stages
    discovery_triggers: [...]

  meta:  # From market context
    market_segments: [...]
```

**Output:**
- `knowledge_base/strategic_lens.yaml` (single file)

**Validation:**
- All 67 taxonomy patterns mapped
- Nickel context integrated (ICP, priorities)
- Priority scoring (1-3) for each item
- Strategic_fit scores (0-10) for high-priority items

---

### Phase 2: Sample Batch Extraction (2-3 hours for 10 transcripts)

**Input:**
- `strategic_lens.yaml` (from Phase 1)
- 10 selected transcripts from raw_context/ (prioritize strategically)

**Selection Strategy:**
```
Pick 10 diverse transcripts:
- 3x GTM Build Updates (recent: 10/24, 10/27, 10/31)
- 2x Customer feature requests or discovery calls
- 2x ICP/positioning docs
- 1x Competitive intelligence
- 1x Onboarding/compliance related
- 1x Industry/market context
```

**Process per Transcript:**

1. **Read transcript + strategic_lens.yaml**

2. **Run 6 dimensional extractions in parallel** (use agent specs as prompts):
   - WHO: Personas, company profiles, buyer characteristics
   - WHAT: Pain points, use cases, product fit signals
   - WHY: Objections, motivations, competitive mentions
   - HOW: Product requirements, feature gaps, capabilities
   - WHERE/WHEN: Journey stage, discovery triggers, timing
   - META: Market segment, industry context, patterns

3. **For each extraction, calculate strategic_fit (0-10)**:
   ```
   Example WHO extraction:
   - Extracted persona: "Accounting Firm Buyer"
   - Strategic lens priority: 1 (highest)
   - Criteria match: 8/10
   - Strategic_fit score: 9

   Composite score = (frequency × 0.4) + (strategic_fit × 0.6)
   ```

4. **Create dimensional_annotation file** (optional, or track in memory):
   ```yaml
   # knowledge_base/dimensional_annotations/gtm_update_10_24/WHO_extraction.yaml
   dimension: "WHO"
   transcript: "10 24 25 - GTM Build Update"
   strategic_lens_version: "1.0"

   personas_extracted:
     - name: "Construction Contractor"
       priority: 2
       strategic_fit: 7
       evidence: [...]

   context_lineage:
     source_document: "10 24 25 - GTM Build Update"
     lines_extracted: "45-67, 123-156"
     unique_value: "First mention of X in weekly sync context"
   ```

5. **Create/update knowledge graph nodes**:
   - If pattern exists (from Iteration 1): Update frequency, add evidence
   - If new pattern: Create new node with full frontmatter
   - Include context_lineage in NEW nodes only

6. **Track inter-domain links** (Tier 1/2/3 importance)

**Output per Transcript:**
- 6 dimensional extractions (can be in memory, not separate files)
- 5-10 new/updated knowledge graph nodes
- Pattern frequency updates in taxonomy
- New patterns added to taxonomy

**Total Output (10 transcripts):**
- 50-100 new/updated knowledge graph nodes
- Taxonomy updated with frequencies
- Pattern revalidation data

---

### Phase 3: Sample Batch Analysis (30-60 min)

**Input:**
- Results from 10 transcripts (Phase 2)
- Taxonomy updates
- Pattern frequency changes

**Analysis Questions:**
1. **Pattern Revalidation:** Did Iteration 1 patterns reappear?
   - accounting-firm-buyer (freq 1 → ?)
   - relay-financial (freq 1 → ?)
   - volume-threshold-barriers (freq 6 → ?)
   - Expected: 60%+ revalidation rate

2. **New Pattern Discovery:** Did new strategic patterns emerge?
   - Expected: 20%+ new patterns

3. **Quality Maintenance:** Are nodes well-formed?
   - Evidence citations present?
   - Strategic_fit scores calculated?
   - Context lineage included?
   - Expected: 85%+ quality

4. **Strategic Alignment:** Do patterns match Nickel priorities?
   - WHO: ICP personas appearing?
   - WHAT: Priority pain points surfacing?
   - WHY: Known objections/competitive threats?

**Decision:**
- ✅ PASS: Revalidation ≥60%, New discovery ≥20%, Quality ≥85%
  - → Proceed to remaining 150 transcripts
- ❌ ADJUST: Misalignment detected
  - → Update strategic_lens.yaml
  - → Process another 10 sample batch
  - → Re-analyze

**Output:**
- Sample batch analysis notes (can be simple markdown)
- Decision: Scale or adjust

---

### Phase 4: Full Corpus Processing (20-30 hours for 150 transcripts)

**If Sample Batch PASS:**

**Process:**
- Same as Phase 2, but at scale
- Batch size: 10-20 transcripts per session
- Total batches: 10-15 batches
- Continuous quality monitoring

**Output:**
- Complete knowledge graph (165 transcripts processed)
- Final taxonomy with stable patterns
- High-confidence pattern set

**Time Estimate:**
- 10 transcripts = 2-3 hours
- 150 transcripts = 30-45 hours (with efficiency gains)
- Spread across multiple sessions

---

## Step-by-Step Checklist (Cursor Window)

### Session 1: Strategic Lens (60-90 min)
```
[ ] 1. Open Cursor in nickel_gtm_context_architecture/
[ ] 2. Read taxonomy.yaml (67 patterns)
[ ] 3. Read Nickel high-value context docs
[ ] 4. Create strategic_lens.yaml (map all 67 patterns + priorities)
[ ] 5. Validate: All patterns mapped, priorities set, strategic_fit scored
```

### Session 2: Sample Batch Part 1 (90 min)
```
[ ] 1. Select 5 transcripts (diverse strategic coverage)
[ ] 2. For each transcript:
       [ ] a. Read transcript + strategic_lens.yaml
       [ ] b. Run WHO extraction (personas) → calculate strategic_fit
       [ ] c. Run WHAT extraction (pains/use cases) → calculate strategic_fit
       [ ] d. Run WHY extraction (objections/competitive) → calculate strategic_fit
       [ ] e. Run HOW extraction (product requirements) → calculate strategic_fit
       [ ] f. Run WHERE/WHEN extraction (journey) → calculate strategic_fit
       [ ] g. Run META extraction (market context) → calculate strategic_fit
       [ ] h. Create/update 5-10 knowledge graph nodes (with context_lineage)
       [ ] i. Update taxonomy with frequency changes
```

### Session 3: Sample Batch Part 2 (90 min)
```
[ ] 1. Select 5 more transcripts (complete 10 total)
[ ] 2. Repeat extraction process (2a-2i)
[ ] 3. Total: 10 transcripts processed
```

### Session 4: Analysis & Decision (30-60 min)
```
[ ] 1. Calculate pattern revalidation rate
[ ] 2. Calculate new pattern discovery rate
[ ] 3. Spot-check quality (5 random nodes)
[ ] 4. Assess strategic alignment
[ ] 5. Decision: PASS → scale | ADJUST → update lens + retry
```

### Session 5+: Full Corpus (if PASS)
```
[ ] Repeat Session 2-3 process for remaining 150 transcripts
[ ] Batch size: 10-20 per session
[ ] Monitor quality continuously
[ ] Update taxonomy ongoing
```

---

## What Success Looks Like

### After Strategic Lens (Session 1):
- ✅ Single strategic_lens.yaml file created
- ✅ All 67 taxonomy patterns mapped with priorities
- ✅ Nickel context integrated (ICP, positioning, competitive)
- ✅ Strategic_fit scoring criteria defined
- ✅ Ready to guide dimensional extraction

### After Sample Batch (Sessions 2-4):
- ✅ 10 transcripts processed with dimensional approach
- ✅ 50-100 new/updated nodes created
- ✅ Pattern revalidation ≥60% (Iteration 1 patterns reappeared)
- ✅ New discovery ≥20% (novel patterns emerged)
- ✅ Quality maintained ≥85% (evidence, attribution, strategic_fit)
- ✅ Strategic alignment confirmed (matches Nickel priorities)
- ✅ Decision made: Scale to remaining 150

### After Full Corpus (Sessions 5+):
- ✅ 165 transcripts fully processed
- ✅ Comprehensive knowledge graph with strategic_fit scores
- ✅ Stable pattern taxonomy (target 85+ stability)
- ✅ High-confidence patterns validated (frequency ≥3-5)
- ✅ Ready for GTM execution (messaging, ICP, competitive positioning)

---

## Common Pitfalls to Avoid

### ❌ Pitfall 1: Treating Agent Specs as Code to Implement
**Wrong:** "I need to write Python/TS to implement WHO_Extractor"
**Right:** "WHO_Extractor spec is my prompt - use it directly in Cursor"

### ❌ Pitfall 2: Creating All Dimensional Annotation Files
**Wrong:** "I need 160 transcripts × 6 dimensions = 960 YAML files"
**Right:** "Dimensional annotations can stay in memory - create nodes directly"

**Clarification:**
- Dimensional annotations are intermediate working files
- You CAN create them if useful for tracking
- You DON'T HAVE TO create them - can extract → node directly
- Choice: Whatever feels natural in your Cursor workflow

### ❌ Pitfall 3: Retroactively Fixing Iteration 1
**Wrong:** "I need to retrofit context_lineage to 31 existing nodes"
**Right:** "Preserve Iteration 1 as-is, apply new standard to future nodes"

### ❌ Pitfall 4: Formal Checkpoint Meetings
**Wrong:** "I need to schedule 90-min validation meeting with Ivan"
**Right:** "Analyze sample batch yourself, validate through results quality"

### ❌ Pitfall 5: Processing All 160 Before Validation
**Wrong:** "I'll process all 160, then check if approach worked"
**Right:** "Process 10 sample → validate → adjust if needed → scale"

---

## Key Decisions You Need to Make

### Decision 1: Dimensional Annotation Files - Create or Skip?

**Option A: Create Files** (structured, audit-friendly)
- Create `dimensional_annotations/[transcript]/[dimension]_extraction.yaml`
- 160 transcripts × 6 dimensions = 960 files
- Pros: Full audit trail, separate concerns, easier debugging
- Cons: More files to manage, slightly slower
- **Choose if:** You value explicit intermediate artifacts

**Option B: Direct to Nodes** (efficient, pragmatic)
- Run dimensional extraction → create nodes immediately
- No intermediate files
- Dimensional data lives in node frontmatter
- Pros: Faster, fewer files, cleaner directory
- Cons: Harder to debug extraction quality separately
- **Choose if:** You value speed and simplicity

**My Recommendation:** **Option B (Direct to Nodes)** for now
- You can always create annotation files later if needed
- Faster iteration for sample batch
- Dimensional metadata still captured in node frontmatter

### Decision 2: Sample Batch Size - 5, 10, or 20?

**Option A: 5 transcripts** (fastest validation)
- Pros: Quick feedback (60-90 min total)
- Cons: May not be representative sample

**Option B: 10 transcripts** (balanced)
- Pros: Good diversity, 2-3 hour commitment
- Cons: Medium time investment

**Option C: 20 transcripts** (thorough)
- Pros: High confidence in validation
- Cons: 4-6 hours before decision point

**My Recommendation:** **Option B (10 transcripts)**
- Enough diversity to validate approach
- Not too long before feedback
- Can split across 2 sessions (5+5)

### Decision 3: Transcript Selection - Strategic or Random?

**Option A: Strategic Selection** (purposeful)
- Target: Accounting firms, Relay mentions, compliance, ICP matches
- Pros: Validates high-priority patterns first
- Cons: May miss other patterns

**Option B: Random Selection** (representative)
- Random sample from 160 remaining
- Pros: Representative of full corpus
- Cons: May not hit strategic patterns

**Option C: Mixed** (balanced)
- 50% strategic (target high-value)
- 50% random (ensure representation)
- Pros: Best of both worlds

**My Recommendation:** **Option A (Strategic Selection)** for sample batch
- You want to validate Iteration 1 discoveries (accounting firm, Relay)
- Random sampling can happen during full corpus
- Strategic lens guides prioritization anyway

---

## Final Simplified Checklist

**Today (Strategic Lens):**
```
1. Open Cursor in nickel_gtm_context_architecture/
2. Read taxonomy.yaml + Nickel context docs
3. Create strategic_lens.yaml (60-90 min)
4. Validate completeness
```

**Next Session (Sample Batch - Part 1):**
```
1. Select 5 strategic transcripts
2. For each: Run 6 dimensional extractions → Create/update nodes
3. 90 min total
```

**Following Session (Sample Batch - Part 2):**
```
1. Select 5 more transcripts (total 10)
2. Repeat extraction process
3. Analyze results: Revalidation rate, new discovery, quality
4. Decision: Scale or adjust
```

**After Sample Batch Passes:**
```
1. Process remaining 150 transcripts in batches
2. 10-20 per session
3. 10-15 sessions total
```

---

## What to Ask Claude Code in Cursor

### Strategic Lens Creation:
```
"Read taxonomy.yaml and the Nickel context documents in raw_context/.
Create strategic_lens.yaml that:
1. Maps all 67 patterns from taxonomy to dimensional categories (WHO/WHAT/WHY/HOW/WHERE_WHEN/META)
2. Integrates Nickel's ICP definition, positioning, and strategic priorities
3. Assigns priority rankings (1-3) for each pattern
4. Calculates strategic_fit scores (0-10) for high-priority items
5. Flags patterns that need validation (freq=1)

Use the strategic_lens schema from NICKEL_STRUCTURE_MAPPING.md section 2.2"
```

### Dimensional Extraction (per transcript):
```
"Read [transcript_name].md and strategic_lens.yaml.

Run 6 dimensional extractions:
1. WHO: Extract personas matching target_personas in lens, calculate strategic_fit
2. WHAT: Extract pain points and use cases, score against lens priorities
3. WHY: Extract objections and competitive mentions, check against lens threats
4. HOW: Extract product requirements and feature gaps
5. WHERE/WHEN: Extract journey stage and discovery triggers
6. META: Extract market segment and industry context

For each extraction:
- Calculate strategic_fit score (0-10) using lens criteria
- Include line-level citations (line numbers)
- Add unique_value explanation (why this source matters)

Then create/update knowledge graph nodes in appropriate directories:
- personas/ for WHO extractions
- pain_points/ for WHAT pains
- use_cases/ for WHAT use cases
- objections/ for WHY extractions
- [etc]

Include context_lineage in frontmatter with:
- source_document + lines_extracted
- unique_value
- dimension
- strategic_fit score"
```

### Sample Batch Analysis:
```
"Analyze the 10 transcripts I just processed.

Calculate:
1. Pattern revalidation rate: How many Iteration 1 patterns (from taxonomy.yaml) reappeared?
2. New pattern discovery rate: How many novel patterns emerged?
3. Quality check: Review 5 random nodes - do they have evidence, strategic_fit, context_lineage?
4. Strategic alignment: Do patterns match lens priorities (WHO personas, WHAT pains, WHY objections)?

Report:
- Revalidation rate (target ≥60%)
- Discovery rate (target ≥20%)
- Quality score (target ≥85%)
- Decision: PASS (scale to 150) or ADJUST (update lens)"
```

---

## Timeline Estimate

| Session | Focus | Duration | Cumulative |
|---------|-------|----------|------------|
| 1 | Strategic Lens | 60-90 min | 90 min |
| 2 | Sample Batch (5 transcripts) | 90 min | 3 hours |
| 3 | Sample Batch (5 more) | 90 min | 4.5 hours |
| 4 | Analysis & Decision | 30-60 min | 5.5 hours |
| 5-15 | Full Corpus (150 transcripts) | 30-45 hours | 50 hours |

**Total: 50-55 hours** (vs 68 hours in original plan - saved by skipping retroactive work)

---

## You're Ready When

- ✅ Strategic lens created and validated
- ✅ Sample batch (10) processed with dimensional approach
- ✅ Pattern revalidation ≥60% confirmed
- ✅ Quality ≥85% maintained
- ✅ Strategic alignment confirmed with Nickel priorities
- ✅ Decision made: Scale to remaining 150

---

**Status:** Ready to execute in Cursor window
**Next Action:** Create strategic_lens.yaml (60-90 min)
**Success Metric:** All 67 patterns mapped + Nickel context integrated + ready for extraction
