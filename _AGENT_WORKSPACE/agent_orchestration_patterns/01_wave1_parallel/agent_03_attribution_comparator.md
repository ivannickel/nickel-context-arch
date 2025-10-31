# Agent 03: Attribution Framework Comparator

**Parallel Extraction Agent - Wave 1**

---

## Objective

Compare evidence attribution systems across three case studies to build a comprehensive attribution framework design guide for context engineering projects.

---

## Input Corpus


### Recur Attribution System
- **Path**: `gtm_engagements/02_warm_lead/recur_software_role/docs/`
- **Key Pattern**: Customer verification levels + data source attribution
- **Source Citation**: Companies House references, website validation
- **Files to Analyze**:
  - `01_research/*.md` (7 research reports with attribution)
  - `CASE_STUDY_DELIVERABLES_SUMMARY.md` (attribution philosophy)

### Pixee Attribution System
- **Path**: `gtm_engagements/03_active_client/pixee_ai_gtm/Pixee/`
- **Key Pattern**: Context lineage + disposal tracking
- **Source Citation**: Wikilinks, front matter lineage, refactor agent disposal logs
- **Files to Analyze**:
  - `_system/00_specialized_agents/context_refactor_agents/` (disposal lineage methodology)
  - `00_foundation/` through `04_archive/` (attribution in practice)

---

## Analysis Tasks

### Task 1: Attribution Schema Comparison

**Objective**: Document HOW sources are cited in each system

**Method**:
1. Extract citation formats:
   - Inline citations (within text)
   - Footer/endnote citations
   - Front matter attribution
   - Wikilink attribution
2. Identify required fields:
   - Source URL/identifier
   - Access date
   - Confidence level
   - Evidence type (case study, review, API, etc.)
3. Compare schema rigor:
   - Minimal: Source mentioned without URL/date
   - Standard: Source with URL + date
   - Comprehensive: Source + date + evidence level + extraction method

**Output Section**: `attribution_schema_comparison`

**Deliverable**:
```markdown
## Attribution Schema Comparison


**Format**:
```markdown
**Value Proposition:** "One-sentence description" [SOURCE: company.com/about, 2024-09-01]
**Evidence Level:** VERIFIED

**Customer ICP:** Mid-market SaaS companies
**Evidence Level:** INFERRED (from review site mentions, no direct statement)
[SOURCE: g2.com/reviews/product-x, 2024-09-05]

**Buying Committee:** UNKNOWN
- No public data on stakeholder structure available
```

**Required Fields**:
- Source: URL or document identifier
- Date: Access/publication date
- Evidence Level: VERIFIED | INFERRED | UNKNOWN
- Reasoning: WHY level assigned

**Rigor**: HIGH (explicit confidence, reasoning documented)

### Recur Schema: Data Source Attribution + Verification Levels

**Format**:
```markdown
**Customer**: Cavalier Sheet Metal
**Industry**: Metal fabrication (SIC 25990)
**Verification**: VERIFIED via case study [SOURCE: statii.co.uk/case-studies/cavalier]
**Evidence Level**: Direct customer testimonial with attribution

**TAM Estimate**: 1,000-2,000 companies
**Source**: Companies House API (SIC code 25990, 25730, 22290)
**Methodology**: Conservative = active companies in target SIC codes
**Date Accessed**: 2024-09-15
```

**Required Fields**:
- Source: Data provider (Companies House, website, API)
- Verification: Customer/data validation status
- Methodology: HOW data was gathered
- Date: Access date

**Rigor**: HIGH (methodology transparency, data source validation)

### Pixee Schema: Context Lineage + Disposal Tracking

**Format (Front Matter)**:
```yaml
---
created: 2024-08-01
source: customer_call_transcript_2024-07-28.md
parent_context: 00_foundation/comprehensive_market_intelligence.md
consolidated_from:
  - old_customer_intel_v1.md
  - customer_patterns_draft.md
disposal_lineage: Removed duplicate content, preserved insights in parent
---
```

**Format (Disposal Logs)**:
```markdown
## Files Disposed
- `04_archive/old_messaging_v1.md`
  - Reason: Superseded by 02_synthesis/messaging_framework.md
  - Content preserved: Key pain points migrated to parent
  - Rollback: Available in git history (commit abc123)
```

**Required Fields**:
- Created: Document creation date
- Source: Originating document/call/meeting
- Parent context: Where content lives in graph
- Consolidated from: What was merged
- Disposal lineage: What was removed and why

**Rigor**: VERY HIGH (full lineage, rollback capability, disposal transparency)
```

---

### Task 2: Evidence Level Taxonomies

**Objective**: Compare confidence/verification frameworks

**Method**:
1. Extract evidence classification systems:
   - [Tool]: VERIFIED / INFERRED / UNKNOWN
   - Recur: Customer verification levels, data source tiers
   - Pixee: (Check for explicit evidence levels or implicit via lineage)
2. Document taxonomy semantics:
   - What qualifies as VERIFIED vs INFERRED?
   - How are conflicts resolved (multiple sources disagree)?
   - When to flag UNKNOWN vs make educated inference?

**Output Section**: `evidence_level_taxonomies`

**Deliverable**:
```markdown
## Evidence Level Taxonomies


**VERIFIED**:
- Definition: Direct evidence from authoritative source
- Examples:
  - Customer testimonial with attribution
  - Company website explicit claim (e.g., "We serve mid-market SaaS")
  - Case study with named customer
- Threshold: Can point to specific URL + quote

**INFERRED**:
- Definition: Logical inference from multiple signals, no direct statement
- Examples:
  - Buying committee inferred from job post requirements ("reports to VP Sales")
  - Sales cycle estimated from product complexity + customer size
  - GTM motion inferred from hiring patterns + tech stack
- Threshold: 2+ signals support inference, reasoning documented

**UNKNOWN**:
- Definition: Insufficient data to make claim, even inferred
- Examples:
  - Customer geography when no public data available
  - Pricing when not published and no signals found
  - Tech stack when HG Insights has no data
- Threshold: <2 signals OR signals are speculative

**Conflict Resolution**:
- If sources disagree → mark as INFERRED, note contradiction
- If high-confidence source contradicts low-confidence → use high-confidence, mark others as conflicting
- If equally credible sources disagree → flag for human review

### Recur: Data Source Tier + Customer Verification

**Data Source Tiers**:
- **Tier 1 (Primary)**: Companies House API (government data, high reliability)
- **Tier 2 (Validated)**: Company websites with validation (scraped + verified active)
- **Tier 3 (Enriched)**: Third-party APIs (Creditsafe, tech stack data)

**Customer Verification Levels**:
- **VERIFIED Customer**: Named in case study with testimonial
- **CLAIMED Customer**: Company lists logo but no confirmation
- **MENTIONED Customer**: Referenced in content but relationship unclear

**Scoring Impact**:
- VERIFIED customers → patterns extracted as ICP criteria (high confidence)
- 5-customer sample acknowledged as limitation
- All patterns treated as hypotheses requiring testing

### Pixee: Lineage-Based Attribution (No Explicit Levels)

**Attribution via Lineage**:
- Front matter tracks: source, parent, consolidated_from
- Disposal logs track: what removed, why, where preserved
- Git history as ultimate attribution source

**Implicit Confidence**:
- Documents in `00_foundation/` = high confidence (strategic truth)
- Documents in `02_synthesis/` = frameworks (derived insights)
- Documents in `04_archive/` = historical (superseded)

**Rigor via Traceability**:
- Any claim can be traced back through lineage chain
- Disposal decisions documented with reasoning
- Rollback possible via git + disposal logs
```

---

### Task 3: Lineage Tracking Patterns

**Objective**: Document how transformations are traced over time

**Method**:
1. Identify lineage mechanisms:
   - Version history (git commits, file iterations)
   - Front matter tracking (source, parent, consolidated_from)
   - Disposal logs (what archived, why, rollback info)
   - Wikilink graphs (content relationships)
2. Analyze transformation attribution:
   - Raw data → Analysis → Insight → Framework → Execution
   - How is each transformation step attributed?
3. Document rollback capabilities:
   - Can you trace insight back to original source?
   - Can you recover disposed content?

**Output Section**: `lineage_tracking_patterns`

**Deliverable**:
```markdown
## Lineage Tracking Patterns

### Pattern 1: Git-Based Version Lineage (All Cases)

**Mechanism**: Git commit history

**Example Trace**:
```
Commit abc123: Created customer_intelligence_draft.md (raw research)
Commit def456: Updated with 5 verified customers (analysis)
Commit ghi789: Consolidated into 02_synthesis/customer_patterns.md (synthesis)
Commit jkl012: Archived customer_intelligence_draft.md (disposal)
```

**Rollback**: `git checkout abc123 -- customer_intelligence_draft.md`

**Limitations**: Requires git discipline, no semantic lineage (why changed)

### Pattern 2: Front Matter Lineage (Pixee)

**Mechanism**: YAML front matter with explicit lineage fields

**Example**:
```yaml
---
source: discovery_call_2024-07-15.md
parent_context: 00_foundation/comprehensive_market_intelligence.md
consolidated_from:
  - competitor_analysis_v1.md
  - competitive_positioning_draft.md
lineage_notes: Merged 2 draft competitive docs, preserved key differentiators
---
```

**Semantic Lineage**: Documents WHY consolidation happened, WHAT was preserved

**Rollback**: Check `consolidated_from` field → locate original files in git

### Pattern 3: Disposal Lineage Logs (Pixee Refactor Agents)

**Mechanism**: Explicit disposal documentation

**Example**:
```markdown
## Archive Agent: Disposal Report

### Disposed Files (10 total)

#### File: 04_archive/messaging_v1_old.md
- **Reason**: Superseded by 02_synthesis/messaging_framework_v3.md
- **Content Preserved**:
  - Pain point taxonomy → migrated to parent
  - 5 message templates → archived (legacy reference)
- **Rollback**: Git commit xyz789, can restore if needed
- **Dependencies**: 0 active wikilinks (safe to dispose)

#### File: 04_archive/customer_intel_raw.md
- **Reason**: Consolidated into 01_customer/all_call_summaries.md
- **Content Preserved**: 100% (no loss, just reorganization)
- **Rollback**: Git commit abc123
```

**Transparency**: Complete audit trail of disposal decisions

**Safety**: Rollback instructions + preserved content documentation

### Pattern 4: Transformation Chain Attribution (Recur)

**Mechanism**: Research spec → Code implementation traceability

**Example**:
```markdown
## Research Layer (Agent 03: Market Boundaries)
### 100-Point Scoring System
- SIC Code Match: 30 points (25990 = 30, 22290 = 25)
- Company Size: 20 points (10-30 employees = 20, 31-50 = 15)
```

**Code Layer** (feature_engineer.py):
```python
def calculate_score(company: Company) -> int:
    \"\"\"Calculate 100-point score per Agent 03 specification\"\"\"
    score = 0

    # SIC code scoring - Agent 03 Section 3.2.1
    if company.sic_code in ['25990', '25730']:
        score += 30
    elif company.sic_code == '22290':
        score += 25
    # ...
```

**Traceability**: Code comments reference originating agent + section

**Validation**: Scoring logic can be audited against research spec
```

---

### Task 4: Disposal Attribution Methodology

**Objective**: How is content archival/removal documented?

**Method**:
1. Identify disposal mechanisms:
   - Archive directories (04_archive/)
   - Git deletion with commit messages
   - Disposal lineage logs
2. Extract disposal criteria:
   - When to archive vs delete vs consolidate?
   - How to ensure no insight loss?
3. Document rollback procedures:
   - Can disposed content be recovered?
   - How long is recovery window?

**Output Section**: `disposal_attribution_methodology`

**Deliverable**:
```markdown
## Disposal Attribution Methodology

### Pixee Context Refactor: Systematic Disposal with Lineage

**Disposal Criteria**:
1. **Redundancy**: Content duplicated elsewhere (consolidate)
2. **Superseded**: Newer version exists (archive old version)
3. **Low Value**: Historical artifact with no ongoing relevance (dispose)

**Safety Protocol** (from Archive Agent spec):
1. **Pre-Disposal Audit**:
   - Verify content preserved in active documents (no loss)
   - Check for active wikilinks (dependencies)
   - Flag high-risk disposals for human review

2. **Disposal Documentation**:
   - Log: What disposed, why, where preserved
   - Rollback instructions: Git commit + restore procedure
   - Dependencies: List any broken links (to be fixed)

3. **Rollback Window**:
   - Git history: Indefinite (can always restore)
   - Disposal logs: Explicit rollback instructions documented

**Example Disposal Log**:
```markdown
### High-Confidence Disposals (40 files)
- Fully redundant content (consolidated into active docs)
- 0 insight loss
- No active wikilinks

### Pending Human Review (5 files)
- Partial overlap with active content
- May contain unique insights requiring extraction
- Recommended: Manual review before disposal
```


**Disposal Mechanism**: Git deletion or archiving to subdirectory

**Limitations**:
- No explicit disposal logs
- Rollback requires git expertise
- Reasoning in commit messages (if documented)

**Example**:
```bash
git rm old_research_draft.md
git commit -m "Removed draft, superseded by final report"
```

**Recovery**: `git checkout HEAD~1 -- old_research_draft.md`

### Disposal Best Practices (Synthesized)

1. **Explicit Logging** (Pixee model):
   - Document what disposed, why, where preserved
   - Include rollback instructions
   - Audit for insight preservation

2. **Safety Gates**:
   - Check for dependencies (wikilinks, code references)
   - Verify content preserved elsewhere (no loss)
   - Human review for high-risk disposals

3. **Rollback Capability**:
   - Git as ultimate backup
   - Disposal logs with restore procedures
   - Clear rollback window documentation
```

---

### Task 5: Anti-Patterns & Attribution Pitfalls

**Objective**: Document what NOT to do based on observed patterns

**Method**:
1. Identify attribution failures:
   - Missing sources
   - Vague citations ("industry reports suggest...")
   - Spec-code drift (code no longer matches research)
   - Orphaned content (no lineage)
2. Extract remediation strategies

**Output Section**: `anti_patterns_and_pitfalls`

**Deliverable**:
```markdown
## Attribution Anti-Patterns

### Anti-Pattern 1: Vague Source Attribution

❌ **Bad**: "According to industry reports, customers prefer X"

✅ **Good**: "Mid-market SaaS customers prefer X" [SOURCE: G2 reviews, 15 mentions, 2024-09-01] **Evidence**: INFERRED (pattern across reviews, no explicit survey)

**Remediation**: Always include URL + date + evidence level

---

### Anti-Pattern 2: Spec-Code Drift

❌ **Bad**:
- Research spec defines scoring logic
- Code implementation diverges over time
- No traceability from code back to spec

✅ **Good**:
```python
# Agent 03 specification: SIC 25990 = 30 points
def calculate_sic_score(sic_code: str) -> int:
    \"\"\"Calculate SIC score per Agent 03 Section 3.2.1\"\"\"
    if sic_code == '25990':
        return 30  # Agent 03: Metal fabrication priority
```

**Remediation**:
- Code comments reference originating agent + section
- Sync code updates with spec updates
- Validation tests check code matches spec

---

### Anti-Pattern 3: Silent Content Disposal

❌ **Bad**:
- Delete files without documentation
- No rollback instructions
- No verification that content preserved

✅ **Good** (Pixee model):
```markdown
## Disposal Log
File: customer_intel_v1.md
Reason: Consolidated into all_call_summaries.md
Content Preserved: 100% (no loss)
Rollback: git checkout abc123 -- customer_intel_v1.md
```

**Remediation**: Explicit disposal logs with preservation verification

---

### Anti-Pattern 4: Orphaned Content (No Lineage)

❌ **Bad**:
- File exists but no front matter, no wikilinks, no references
- Can't determine: source, purpose, relevance

✅ **Good**:
```yaml
---
source: discovery_call_2024-08-01.md
parent_context: 00_foundation/market_intelligence.md
purpose: Competitive positioning insights from call
---
```

**Remediation**: Front matter lineage on all documents

---

### Anti-Pattern 5: Evidence Level Inflation

❌ **Bad**:
- Mark inference as VERIFIED because "seems obvious"
- No documentation of reasoning

✅ **Good**:
```markdown
**GTM Motion**: Enterprise sales (INFERRED)
**Reasoning**: 3 signals support inference:
1. Job posts for Enterprise AEs (10 openings)
2. Complex product requiring POC (website)
3. Committee buying (inferred from L2 buying process)
**Confidence**: Medium (indirect evidence, no explicit confirmation)
```

**Remediation**: Document reasoning for evidence level assignment
```

---

## Output Contract

**File**: `meta_analysis/agent_orchestration_patterns/03_outputs/wave1/attribution_framework_comparison.md`

**Required Sections**:
1. `attribution_schema_comparison` (Task 1)
2. `evidence_level_taxonomies` (Task 2)
3. `lineage_tracking_patterns` (Task 3)
4. `disposal_attribution_methodology` (Task 4)
5. `anti_patterns_and_pitfalls` (Task 5)
6. `attribution_framework_design_guide` (synthesis)
7. `implementation_templates` (reusable schemas)

**Deliverable**: Attribution framework design guide for context engineering projects

---

## Success Criteria

**Completeness**:
- ✅ All 3 attribution systems analyzed
- ✅ Evidence level taxonomies documented
- ✅ Lineage mechanisms extracted
- ✅ Anti-patterns identified with remediation

**Actionability**:
- ✅ Attribution schemas can be implemented in new projects
- ✅ Evidence level taxonomies provide classification guidance
- ✅ Lineage patterns offer traceability templates
- ✅ Anti-patterns help avoid common mistakes

**Insight Quality**:
- ✅ Comparative analysis (not just individual case documentation)
- ✅ Best practices synthesized across cases
- ✅ Rigor spectrum identified (minimal → comprehensive attribution)

---

## Estimated Execution Time

- Attribution schema extraction: 10 minutes
- Evidence level analysis: 10 minutes
- Lineage pattern mining: 10 minutes
- Disposal methodology: 5 minutes
- Synthesis & documentation: 10 minutes
- **Total**: 30-45 minutes

---

## Next Agent Dependency

**Independence**: This agent has NO dependencies on other Wave 1 agents (true parallel execution)

**Downstream**: Agent 06 (Meta-Synthesis) will use this output to build unified pattern library
