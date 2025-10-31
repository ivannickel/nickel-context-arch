# Agent 02: Role & Contract Extractor

**Parallel Extraction Agent - Wave 1**

---

## Objective

Extract agent role classifications and input/output contract patterns from all agent specifications across three case studies to build a reusable agent design pattern library.

---

## Input Corpus


### Recur Agent Specifications
- **Path**: `gtm_engagements/02_warm_lead/recur_software_role/docs/`
- **Key Files**:
  - `01_research/01_statii_foundation_report.md` (Agent 01 spec)
  - `01_research/02_statii_customer_intelligence.md` (Agent 02 spec)
  - `01_research/03_statii_market_boundaries.md` (Agent 03 spec)
  - `01_research/04-07_*.md` (Agents 04-07 specs)
  - `CASE_STUDY_DELIVERABLES_SUMMARY.md` (meta-documentation)
- **Total**: 7 research agent specifications + implementation docs

### Pixee Agent Specifications
- **Path**: `gtm_engagements/03_active_client/pixee_ai_gtm/`
- **Key Files**:
  - `.claude/agents/` (7 GTM agents: agent_01 through agent_07)
  - `Pixee/_system/00_specialized_agents/` (12+ specialized agents)
  - `Pixee/_system/00_specialized_agents/context_refactor_agents/` (5 refactor agents)
- **Total**: 7 GTM + 12+ specialized agents

---

## Analysis Tasks

### Task 1: Agent Role Classification

**Objective**: Build agent role taxonomy based on what agents DO

**Method**:
1. Read each agent specification
2. Classify by primary function:
   - **Collectors**: Gather raw data from sources (web scraping, API calls)
   - **Analyzers**: Process data to extract insights (research, pattern finding)
   - **Synthesizers**: Combine multiple inputs into frameworks (consolidation)
   - **Executors**: Take action or generate code (implementation)
   - **Maintainers**: Optimize/clean existing systems (refactor, archive)
   - **Routers**: Direct flow between agents (orchestration)
3. Identify role patterns:
   - Research agents ([Tool] 1A, 1B; Recur 01-04; Pixee 01-02)
   - Synthesis agents ([Tool] 2; Recur 05-06; Pixee 03)
   - Execution agents (Recur 07; Pixee agents with code gen)
   - Refactor agents (Pixee context refactor 01-05)

**Output Section**: `agent_role_taxonomy`

**Deliverable**:
```markdown
## Agent Role Taxonomy

### Role 1: Collector Agents
**Purpose**: Gather raw data from external sources
**Examples**:
- Recur Agent 04: Data Discovery (Companies House API)
- Pixee Customer Intelligence: Call transcript collection

**Characteristics**:
- External API/web interaction
- Validation of data quality
- Output: Raw datasets with attribution

### Role 2: Analyzer Agents
**Purpose**: Extract insights from data
**Examples**:
- Recur Agent 02: Customer Pattern Analysis

**Characteristics**:
- Evidence-based reasoning
- Multi-source synthesis
- Output: Insights with confidence levels (VERIFIED/INFERRED/UNKNOWN)

[Continue for all roles...]
```

---

### Task 2: Input/Output Schema Extraction

**Objective**: Document what each agent consumes and produces

**Method**:
1. For each agent, extract:
   - **Input Contract**: Required inputs, optional inputs, dependencies
   - **Output Contract**: File formats, data schemas, deliverable structure
   - **Validation Rules**: Quality gates, error handling
2. Identify contract patterns:
   - File-based handoffs (Agent A writes file → Agent B reads)
   - Structured schemas (YAML, JSON, Pydantic models)
   - Free-form reports (Markdown with sections)

**Output Section**: `input_output_schema_library`

**Deliverable**:
```markdown
## Input/Output Contract Patterns


**Agent 1A Output Contract**:
```yaml
file: foundation_report_L0-L2.md
sections:
  - L0_value_proposition
  - L1_customer_icp
  - L2_buying_committee
evidence_levels: [VERIFIED, INFERRED, UNKNOWN]
```

**Agent 1B Input Contract**:
```yaml
required:
  - foundation_report_L0-L2.md
    must_contain:
      - Clear customer ICP (L1)
      - Buying process (L2)
optional:
  - clay_workspace_access
```

### Pattern 2: Structured Data Models (Recur)

**Agent 05 Output (Data Fusion)**:
```python
class CompanyModel:
    # 143 fields defined
    company_name: str
    sic_code: str
    score_firmographic: int  # 0-55
    score_behavioral: int    # 0-45
    # ... full schema in spec
```

**Agent 06 Input (Messaging)**:
Uses CompanyModel fields for personalization routing

[Continue for all contract patterns...]
```

---

### Task 3: Validation Rule Patterns

**Objective**: Extract quality gates, error handling, gap flagging mechanisms

**Method**:
1. Scan for validation language:
   - "MUST provide", "Required outputs", "Success criteria"
   - "If insufficient data → flag UNKNOWN"
   - "Quality checklist", "Validation gates"
2. Document validation types:
   - **Pre-conditions**: What must exist before agent runs
   - **Quality gates**: Thresholds for output acceptance
   - **Error handling**: What happens when validation fails
   - **Gap flagging**: How agents indicate missing information

**Output Section**: `validation_rule_patterns`

**Deliverable**:
```markdown
## Validation Patterns


**Validation Rule**:
- All claims MUST include source URL + date
- Tag evidence level: VERIFIED | INFERRED | UNKNOWN
- If insufficient data → explicitly flag UNKNOWN, don't fabricate

**Implementation Example**:
```markdown
## L1: Who Their Customer Is
**Customer ICP:** VERIFIED
- Company type: Mid-market SaaS [SOURCE: case study X, 2024-09-01]
- Size: 50-200 employees [SOURCE: G2 reviews, 2024-08-15]

**Buying Committee:** INFERRED (no direct evidence, inferred from role mentions)
- Economic buyer: VP Sales [INFERRED from: job posting for "report to VP Sales"]

**Customer Geography:** UNKNOWN
- No public data on customer locations available
```

### Pattern 2: Iterative Quality Gates (Pixee Refactor)

**Validation Rule**:
- Target: 60% file reduction with 100% insight preservation
- If iteration 1 < 85% quality → identify gaps, re-run
- Max 3 iterations

**Implementation Example**:
```markdown
Iteration 1: 150 files → 80 files (quality: 70%, gaps: customer intelligence dispersed)
Iteration 2: Re-consolidate → 65 files (quality: 85%, gaps: duplicate frameworks)
Iteration 3: Final → 60 files (quality: 95%, meets threshold ✓)
```

[Continue for all validation patterns...]
```

---

### Task 4: Inter-Agent Contract Mapping

**Objective**: Document handoff protocols between agents

**Method**:
1. Identify agent pipelines:
   - [Tool]: 1A → 1B → 2
   - Recur: 01 → 02 → 03 → 04 → 05 → 06 → 07
   - Pixee GTM: 01 → 02 → 03 → 04 → 05 → 06 → 07
   - Pixee Refactor: Foundation → Discovery → Synthesis → Implementation → Archive
2. Extract handoff contracts:
   - What must Agent A provide for Agent B to succeed?
   - Failure conditions (when handoff breaks)
   - Success examples (good handoffs)

**Output Section**: `inter_agent_contract_examples`

**Deliverable**:
```markdown
## Inter-Agent Contracts


**Agent 1A MUST Provide**:
- Clear customer ICP (L1): Who buys, sizes, industries
- Buying process (L2): Stakeholders, cycle length, criteria

**Agent 1B MUST Receive**:
- Enough customer context to infer: "To sell to THESE customers, they likely need THIS GTM motion"

**Failure Condition**:
If Agent 1A provides vague customer description ("sell to enterprises"), Agent 1B cannot accurately infer GTM motion.

**Success Example**:
```markdown
Agent 1A provides: "Customers are dev teams at product companies, 50-500 eng,
buying decision involves: Dev (user) → Eng Manager (budget) → CTO (enterprise approval)"

Agent 1B infers: "With individual dev users but enterprise approval, likely PLG →
Product-led sales → Enterprise motion. Should see: self-serve tier + upgrade path +
enterprise AE team."
```

### Contract Example 2: Recur Agent 03 → Agent 05

**Agent 03 MUST Provide**:
- 100-point scoring system definition (firmographic 55pts + behavioral 45pts)
- Segmentation criteria (SIC codes, size bands, geography)

**Agent 05 MUST Receive**:
- Complete scoring logic (not just concepts, actual point allocations)
- Field definitions for all 143 account fields

**Handoff Mechanism**:
Agent 03 writes specification in markdown → Agent 05 translates to code

[Continue for more contract examples...]
```

---

### Task 5: Execution Protocol Patterns

**Objective**: Identify common step-by-step execution patterns

**Method**:
1. Extract agent execution steps from prompts
2. Identify recurring patterns:
   - **Research protocol**: Validate → Extract → Synthesize → Output
   - **Synthesis protocol**: Read inputs → Consolidate → Resolve conflicts → Output
   - **Refactor protocol**: Audit → Consolidate → Validate → Archive
3. Document protocol templates

**Output Section**: `execution_protocol_patterns`

**Deliverable**:
```markdown
## Execution Protocol Patterns

### Protocol 1: Research Agent Pattern

**Standard Steps** (observed in [Tool] 1A, 1B; Recur 01-04; Pixee 01-02):

1. **Input Validation**
   - Verify required inputs exist
   - Check data quality/completeness

2. **Data Collection**
   - Gather from prioritized sources (primary → secondary)
   - Attribute all data (source, date)

3. **Analysis**
   - Extract insights with evidence levels
   - Cross-validate across multiple sources

4. **Gap Identification**
   - Flag UNKNOWN where data insufficient
   - Document what couldn't be determined

5. **Output Generation**
   - Structured report with sections
   - Quality checklist validation
   - Sources cited

**Template**:
```markdown
# [AGENT_NAME] Report

## Executive Summary
[1-paragraph synthesis]

## Section 1: [Analysis Area]
**Finding**: [Claim]
**Evidence**: VERIFIED | INFERRED | UNKNOWN
**Source**: [URL, date]

## Evidence Quality
- VERIFIED claims: [count]
- INFERRED claims: [count]
- UNKNOWN gaps: [list]

## Sources
- [URL 1]: [what was extracted]
```

### Protocol 2: Synthesis Agent Pattern

**Standard Steps** (observed in [Tool] 2; Recur 06; Pixee 03):

1. **Context Loading**
   - Read all prerequisite agent outputs
   - Build integrated understanding

2. **Consolidation**
   - Identify common themes across inputs
   - Resolve contradictions

3. **Framework Generation**
   - Abstract patterns into reusable frameworks
   - Create templates

4. **Validation**
   - Ensure synthesis grounded in source material
   - Check for logical consistency

5. **Actionable Output**
   - Frameworks others can use
   - Decision trees, templates, guides

[Continue for more protocols...]
```

---

## Output Contract

**File**: `meta_analysis/agent_orchestration_patterns/03_outputs/wave1/role_contract_patterns.md`

**Required Sections**:
1. `agent_role_taxonomy` (Task 1)
2. `input_output_schema_library` (Task 2)
3. `validation_rule_patterns` (Task 3)
4. `inter_agent_contract_examples` (Task 4)
5. `execution_protocol_patterns` (Task 5)
6. `agent_design_pattern_library` (synthesis)
7. `anti_patterns_catalog` (what to avoid)

**Deliverable**: Agent design pattern library for building new agent systems

---

## Execution Protocol

### Step 1: Agent Corpus Scan
- List all agent files across 3 case studies
- Extract agent names, purposes, file sizes
- Build agent inventory

### Step 2: Role Classification
- Read each agent specification
- Classify by primary function (collector, analyzer, synthesizer, executor, maintainer, router)
- Build role taxonomy

### Step 3: Contract Extraction
- For each agent, extract input/output schemas
- Document validation rules
- Map inter-agent dependencies

### Step 4: Protocol Mining
- Identify common execution steps across agents
- Abstract into reusable protocol templates
- Document variations

### Step 5: Pattern Synthesis
- Consolidate findings into design pattern library
- Create anti-pattern catalog
- Build decision framework (when to use which pattern)

### Step 6: Quality Validation
- [ ] All agent files analyzed
- [ ] Each pattern has 3+ examples from case studies
- [ ] Templates are actionable
- [ ] Anti-patterns documented with remediation

---

## Success Criteria

**Completeness**:
- ✅ All 5 tasks completed
- ✅ Patterns have concrete examples from real agents

**Actionability**:
- ✅ Role taxonomy helps categorize new agents
- ✅ Contract patterns provide templates for input/output design
- ✅ Protocol patterns provide step-by-step execution guides
- ✅ Anti-patterns help avoid common mistakes

**Insight Quality**:
- ✅ Non-obvious patterns identified (not just "agents have inputs and outputs")
- ✅ Patterns explain design decisions (why contracts structured this way)
- ✅ Cross-case patterns (not just single-case observations)

---

## Estimated Execution Time

- Agent corpus scan: 10 minutes
- Role classification: 15 minutes
- Contract extraction: 20 minutes
- Protocol mining: 10 minutes
- Synthesis & documentation: 10 minutes
- **Total**: 45-60 minutes

---

## Next Agent Dependency

**Independence**: This agent has NO dependencies on other Wave 1 agents (true parallel execution)

**Downstream**: Agent 06 (Meta-Synthesis) will use this output to build unified pattern library
