# Transcript Processing Orchestration Plan

**Created:** 2025-10-30
**Purpose:** Parallel processing of 165 sales call transcripts for strategic frontmatter classification
**Target:** High-quality classification in 3-5 minutes, ~$0.15 total cost

---

## Token Economics (Napkin Math)

### Per Transcript Metrics
Based on analysis of `knowledge_base/meetings_md/`:
- **Full transcript:** ~6,780 tokens average
- **First 200 lines:** ~1,500 tokens (sufficient for classification)
- **Output frontmatter:** ~300 tokens

### Cost Analysis by Batch Size

**Using Haiku (Recommended):**
- Input: $0.25/M tokens
- Output: $1.25/M tokens

| Batch Size | # Agents | Input Tokens | Output Tokens | Total Cost | Time Est |
|------------|----------|--------------|---------------|------------|----------|
| 5 tx/agent | 33 agents | 313,500 | 49,500 | $0.14 | 2-3 min |
| 10 tx/agent | 17 agents | 289,000 | 51,000 | $0.13 | 2-3 min |
| 15 tx/agent | 11 agents | 269,500 | 49,500 | $0.13 | 3-4 min |

**Using Sonnet (Not Recommended for This Task):**
- Input: $3/M tokens
- Output: $15/M tokens
- 10 tx/agent cost: $1.64 (12x more expensive, no quality gain)

### Recommendation: 10 transcripts per agent with Haiku

**Why this is optimal:**
- ✅ **Cost-effective:** $0.13 total (< $0.01 per transcript)
- ✅ **Fast:** 2-3 minutes with 17 parallel agents
- ✅ **Quality:** Agent sees 10 examples, learns patterns, maintains consistency
- ✅ **Safe context:** 17K tokens per agent (well within limits)
- ✅ **Error handling:** If 1 agent fails, only 10 transcripts affected

---

## Orchestration Architecture

### Phase 1: Batch Creation (10 seconds)
Create 17 batches of 10 transcripts each (sorted by filename for reproducibility)

```bash
# Pseudo-code
transcripts = sort(glob("knowledge_base/meetings_md/*.md"))
batches = chunk(transcripts, size=10)
# Batch 1: 001-010
# Batch 2: 011-020
# ...
# Batch 17: 161-165 (5 transcripts)
```

### Phase 2: Parallel Agent Execution (2-3 minutes)
Launch 17 agents concurrently, each processing one batch

**Agent Specification:**
- **Model:** Haiku (fast + cheap)
- **Task:** Read schema, classify 10 transcripts, output frontmatter
- **Instructions:** Read only first 200 lines per transcript
- **Output:** YAML frontmatter block for each transcript

**Agent Prompt Template:**
```
You are a sales call classifier. Your task is to add strategic frontmatter to sales call transcripts.

SCHEMA: [Include _TRANSCRIPT_FRONTMATTER_SCHEMA.md]

INSTRUCTIONS:
1. For each transcript, read ONLY the first 200 lines (sufficient for classification)
2. Use filename patterns to infer call_type
3. Scan content for keyword matches (strategic signals)
4. Output ONLY the NEW frontmatter fields (do not duplicate existing Circleback fields)
5. Be consistent across all transcripts in this batch

BATCH: You will process 10 transcripts. Maintain consistency in classification logic.

TRANSCRIPTS:
[For each transcript: filename + first 200 lines]

OUTPUT FORMAT:
For each transcript, output:
---
FILE: {filename}
FRONTMATTER:
```yaml
call_type: discovery
deal_stage: discovery
...
```
---
```

### Phase 3: Result Validation (30 seconds)
Automated quality checks:
- ✅ All 165 transcripts processed
- ✅ No duplicate frontmatter keys
- ✅ Priority distribution: ~20% high, ~50% medium, ~30% low
- ✅ At least 70% of transcripts have ≥1 strategic signal flag = true

### Phase 4: Merge Frontmatter (60 seconds)
For each transcript:
1. Read existing file
2. Parse existing Circleback frontmatter
3. Append new strategic classification fields
4. Write back to file

---

## Execution Sequence

### Step 0: Preparation (Manual, 1 minute)
- [x] Schema created: `knowledge_base/meetings_md/_TRANSCRIPT_FRONTMATTER_SCHEMA.md`
- [ ] Confirm raw_context frontmatter agent is running in parallel
- [ ] Verify no file locks on meetings_md directory

### Step 1: Create Batch Manifests (Automated, 10 seconds)
```bash
python _AGENT_WORKSPACE/utilities/create_transcript_batches.py
# Output: _AGENT_WORKSPACE/transcript_batches/batch_{01..17}.txt
```

Each manifest file contains 10 transcript filenames.

### Step 2: Launch 17 Parallel Agents (Orchestrator, 2-3 minutes)
```python
# Pseudo-code orchestration
agents = []
for batch_id in range(1, 18):
    batch_files = read_batch_manifest(batch_id)
    agent = Task(
        subagent_type="general-purpose",
        model="haiku",
        prompt=generate_batch_prompt(batch_files),
        description=f"Classify transcripts batch {batch_id}"
    )
    agents.append(agent)

# Wait for all agents to complete
results = await_all(agents)
```

### Step 3: Validate Results (Automated, 30 seconds)
```python
# _AGENT_WORKSPACE/utilities/validate_classification_results.py
for result in results:
    assert len(result.transcripts) == expected_count
    assert all(required_fields_present(tx) for tx in result.transcripts)

# Distribution check
priority_dist = count_by_priority(all_results)
assert 0.15 <= priority_dist['high'] <= 0.25
assert 0.45 <= priority_dist['medium'] <= 0.55

# Signal check
with_signals = count_transcripts_with_signals(all_results)
assert with_signals / 165 >= 0.70
```

### Step 4: Merge Frontmatter to Files (Automated, 60 seconds)
```python
# _AGENT_WORKSPACE/utilities/merge_frontmatter.py
for result in results:
    for transcript in result.transcripts:
        original = read_file(transcript.filename)
        existing_fm = extract_frontmatter(original)
        new_fm = merge_frontmatter(existing_fm, transcript.classification)
        updated = replace_frontmatter(original, new_fm)
        write_file(transcript.filename, updated)
```

### Step 5: Generate Processing Report (Automated, 10 seconds)
```markdown
# Transcript Classification Report

**Processed:** 165 transcripts
**Time:** 3m 24s
**Cost:** $0.13

## Classification Distribution
- Call Types: {discovery: 82, demo: 34, kickoff: 28, review: 15, follow_up: 6}
- Deal Stages: {discovery: 82, evaluation: 34, activation: 28, active: 21}
- Priority: {high: 31 (19%), medium: 84 (51%), low: 50 (30%)}

## Strategic Signal Coverage
- has_pain_points: 112 (68%)
- has_objections: 67 (41%)
- has_competitive_intel: 43 (26%)
- has_pricing_discussion: 89 (54%)

## Quality Metrics
✅ All transcripts processed
✅ Priority distribution within target range
✅ 68% of transcripts have strategic signals
✅ No validation errors

**Status:** READY FOR DIMENSIONAL EXTRACTION
```

---

## Parallel Processing with Raw Context

**Current State:**
- Raw context frontmatter: 68 files being processed by separate orchestrator
- Transcript frontmatter: 165 files (this plan)

**Coordination Strategy:**
- ✅ **Independent execution:** Both can run in parallel (different directories)
- ✅ **No file conflicts:** No shared files
- ✅ **Resource management:** Combined 17 + N agents (where N = raw_context batches)

**Timeline coordination:**
```
T+0:00  Start both orchestrators
T+0:10  Transcript batches created (17 batches)
T+0:15  Raw context batches created (N batches)
T+0:20  All agents launched in parallel
T+2:30  Transcript agents complete (17 agents)
T+3:00  Raw context agents complete (N agents)
T+3:30  Transcript frontmatter merged
T+4:00  Raw context frontmatter merged
T+4:30  Both processing reports generated
```

**No blocking dependencies:** Both workstreams are fully parallel.

---

## Risk Mitigation

### Risk 1: Agent Failure
**Probability:** Low
**Impact:** 10 transcripts not classified
**Mitigation:**
- Retry failed batch automatically
- If retry fails, split batch into 5+5 and retry

### Risk 2: Inconsistent Classification
**Probability:** Medium
**Impact:** Low (can reprocess cheaply)
**Mitigation:**
- Include 3 example classifications in agent prompt
- Use same schema across all agents
- Post-processing normalization script

### Risk 3: Context Overflow
**Probability:** Very Low (17K tokens << 200K limit)
**Impact:** Agent truncates input
**Mitigation:**
- Haiku has 200K context window
- We're using only 8.5% of capacity per agent

### Risk 4: File Write Conflicts
**Probability:** Very Low (sequential merge phase)
**Impact:** Corrupted file
**Mitigation:**
- Single-threaded merge phase (not parallelized)
- Atomic write operations
- Backup original files before merge

---

## Success Criteria

### Quality Gates
- [ ] **Coverage:** 165/165 transcripts classified (100%)
- [ ] **Consistency:** Same call_type for duplicate meetings (e.g., 002 and 006)
- [ ] **Distribution:** Priority matches expected 20/50/30 split (±5%)
- [ ] **Signal Coverage:** ≥70% transcripts have at least one strategic signal
- [ ] **Validation:** Zero schema violations

### Performance Gates
- [ ] **Time:** Complete in < 5 minutes
- [ ] **Cost:** < $0.20 total
- [ ] **Parallelism:** All 17 agents complete successfully
- [ ] **No manual intervention** required

### Readiness Gates (Before Dimensional Extraction)
- [ ] All transcripts have `extraction_priority` set
- [ ] High-priority transcripts identified (expect ~30-35)
- [ ] Can filter by strategic signals for targeted extraction
- [ ] Frontmatter validates against schema

---

## Next Steps After Completion

### Immediate (Manual Spot Check)
1. Review 5 random transcripts to validate frontmatter quality
2. Check 2-3 "high priority" transcripts match expectations
3. Verify call_type accuracy for obvious cases (kickoff, demo)

### Phase 2 Preparation (Dimensional Extraction)
1. Filter for high-priority transcripts: `extraction_priority: high`
2. Create dimensional extraction batches (6 dimensions × 165 transcripts = 990 extractions)
3. Launch WHO/WHAT/WHY/HOW/WHERE_WHEN/META extractors in parallel

### Validation Report for Ivan
Generate shortlist of top 20 discoveries for Checkpoint 1:
- Filter: `extraction_priority: high` AND (`has_competitive_intel: true` OR `has_objections: true`)
- Extract key quotes from transcripts
- Format as validation report for stakeholder review

---

## Utilities Required

### create_transcript_batches.py
```python
# Creates 17 batch manifest files
# Input: knowledge_base/meetings_md/*.md
# Output: _AGENT_WORKSPACE/transcript_batches/batch_{01..17}.txt
```

### validate_classification_results.py
```python
# Validates agent outputs against schema
# Checks distribution, coverage, consistency
# Outputs: PASS/FAIL + detailed report
```

### merge_frontmatter.py
```python
# Merges new classification into existing frontmatter
# Atomic file operations
# Backup before modification
```

### generate_processing_report.py
```python
# Creates summary statistics
# Classification distribution
# Quality metrics
# Outputs: _AGENT_WORKSPACE/TRANSCRIPT_CLASSIFICATION_REPORT.md
```

---

## Cost-Benefit Analysis

**Investment:**
- Time: 5 minutes orchestration + 2 minutes validation = 7 minutes
- Cost: $0.13 (Haiku processing)
- Setup: Schema already created

**Return:**
- **Immediate:** 165 transcripts strategically classified for targeted extraction
- **Phase 2:** Filter high-value transcripts first (save 60% extraction time)
- **Phase 3:** Enable strategic synthesis (group by industry, call type, objections)
- **Ongoing:** Reproducible process for future transcript batches

**ROI:** ~100x (7 min investment enables 12 hours of optimized extraction)

---

**Status:** Ready for execution
**Dependencies:** Schema file created ✅
**Blockers:** None
**Next Action:** Create batch creation utility script
