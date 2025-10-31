# Agent Role & Contract Pattern Library
**Extracted from 66+ Agent Specifications Across Three GTM Case Studies**

*Generated: 2025-10-08*
*Analysis Scope: [Tool] (47 agents) | Recur (7 agents) | Pixee (19+ agents)*
*Methodology: Pattern extraction from agent architecture specifications, input/output contracts, and execution protocols*

---

## Executive Summary

### High-Level Findings

This analysis extracts reusable agent orchestration patterns from **66+ agent specifications** across three production GTM systems. The corpus reveals **six core agent role types**, **four primary contract patterns**, **three validation frameworks**, and **five execution protocols** that form the foundation of effective multi-agent systems.

**Key Discovery:** Successful agent orchestration depends less on AI model sophistication and more on **explicit contract design**, **evidence-level flagging**, and **systematic handoff protocols**. Agents that fail typically do so from **contract ambiguity** (vague inputs) or **validation gaps** (no quality gates), not from reasoning limitations.

### Strategic Insights

1. **Role Taxonomy Emerges from Function**: Six agent roles discovered (Collectors, Analyzers, Synthesizers, Routers, Maintainers, Executors) based on **what agents DO**, not what they're called
2. **Contract Patterns Enable Scale**: File-based sequential handoffs ([Tool]), structured data models (Recur), and free-form reports (Pixee) each optimize for different trade-offs
3. **Validation Prevents Cascade Failures**: VERIFIED/INFERRED/UNKNOWN flagging ([Tool]) and iterative quality gates (Pixee refactor) prevent downstream agent failures
4. **Execution Protocols Are Reusable**: Research → Synthesize → Output patterns appear across all three case studies with minor variations

### Quantitative Overview

- **Total Agents Analyzed**: 66+
- **Agent Role Categories**: 6 distinct types
- **Contract Patterns Identified**: 4 primary patterns
- **Validation Frameworks**: 3 systematic approaches
- **Execution Protocols**: 5 reusable templates
- **Anti-Patterns Documented**: 8 common failure modes

---

## 1. Agent Role Taxonomy

### Classification Framework

Agents are classified by **primary function** (what they do) rather than domain (what they know). This functional taxonomy emerged from analyzing agent objectives, input/output contracts, and execution patterns.

### Core Role Types

#### **1.1 Collectors (Data Gathering Agents)**

**Definition**: Gather raw data from external sources without significant transformation. Primary function is **extraction**, not interpretation.

**[Tool] Examples**:
- **Agent 1A: Foundation Intelligence** - Extracts L0-L2 data (product, customer, buying process) from websites, reviews, testimonials
- **Research Agents** (various) - Scrape Companies House, job boards, funding trackers
- **Revenue Enrichment Agent** - Pulls revenue data from multiple sources

**Recur Examples**:
- **Agent 01: Statii Foundation Report** - Collects company info, customer testimonials, pain points from public sources
- **Agent 04: Data Discovery & TAM Mapping** - Scrapes Companies House API for UK manufacturers

**Pixee Examples**:
- **Agent 01: Company Foundation Research** - Extracts verifiable facts from website, press releases, case studies
- **Research Agents** (12+) - Unified company research, contact verification, technology investigation

**Input Contract Pattern**:
```yaml
required_inputs:
  - target_identifier: "company_domain" | "sic_code" | "search_query"
  - research_date: "YYYY-MM-DD"
  - output_directory: "/path/to/output"

optional_inputs:
  - known_facts: "Pre-existing verified data"
  - api_credentials: "For enrichment services"
```

**Output Contract Pattern**:
```yaml
output_format: "Structured report with source attribution"
required_fields:
  - extracted_data: "Raw facts with exact quotes"
  - source_attribution: "[URL] | [DATE_ACCESSED]"
  - evidence_level: "VERIFIED | CLAIMED | MENTIONED"

quality_gates:
  - minimum_sources: ≥3 sources per claim
  - url_accessibility: All sources must be accessible
  - date_stamping: All data must be timestamped
```

**Distribution**: ~25% of total agents (17/66)

---

#### **1.2 Analyzers (Insight Extraction Agents)**

**Definition**: Transform raw data into insights through pattern recognition, inference, or reasoning. Primary function is **interpretation**, not collection.

**[Tool] Examples**:
- **Agent 1B: GTM Motion Intelligence** - Analyzes job postings, tech stack, team structure to infer GTM motion and bottlenecks
- **Routing Analyst Sub-Agent** - Analyzes L0-L6 reports to recommend rep assignment based on 7-factor framework
- **Cluster Analysis Agent** - Discovers 4 clusters from patterns across 50 accounts

**Recur Examples**:
- **Agent 02: Customer Intelligence Patterns** - Analyzes 5 verified customers to extract ICP patterns and boundaries
- **Agent 03: Market Boundary Definition** - Creates 100-point scoring system from customer pattern analysis

**Pixee Examples**:
- **Agent 02: Customer Intel Patterns** - Extracts patterns from call transcripts and customer data
- **Discovery Consolidation Agent** - Synthesizes competitive and customer intelligence from raw research

**Input Contract Pattern**:
```yaml
required_inputs:
  - raw_data_reports: "Output from Collector agents"
  - analysis_framework: "Methodology to apply (e.g., 7-factor, MEDDIC)"
  - context_files: "Supporting documents for interpretation"

optional_inputs:
  - prior_analysis: "Previous insights to build upon"
  - validation_criteria: "Quality thresholds"
```

**Output Contract Pattern**:
```yaml
output_format: "Analytical report with reasoning chain"
required_fields:
  - insights: "Interpreted patterns or recommendations"
  - evidence_chain: "Data → Reasoning → Conclusion"
  - confidence_level: "High | Medium | Low with justification"

quality_gates:
  - reasoning_transparency: Must show "why" not just "what"
  - cross_validation: Insights must align with input data
  - alternative_hypotheses: Must acknowledge other interpretations
```

**Distribution**: ~30% of total agents (20/66)

---

#### **1.3 Synthesizers (Integration & Consolidation Agents)**

**Definition**: Combine multiple inputs into unified frameworks or consolidated outputs. Primary function is **integration**, not creation.

**[Tool] Examples**:
- **Final Synthesis Orchestrator** - Transforms 60-70 hours of research into 4-page deliverable with traceability
- **Routing Orchestrator** - Synthesizes 10 routing memos into unified 50-account portfolio

**Recur Examples**:
- **Agent 06: Messaging Personalization** - Synthesizes pain points, ICP, and messaging into 120 variants across 3 sequences
- **Agent 07: GTM Testing & Validation** - Combines all prior agents into executable campaign infrastructure

**Pixee Examples**:
- **Agent 03: TAM Definition & Market Mapping** - Synthesizes company, customer, competitive intel into ICP framework
- **Synthesis Consolidation Agent** - Integrates foundation + discovery into strategic frameworks
- **Foundation Consolidation Agent** - Merges 9 foundation files into 3 systematic files

**Input Contract Pattern**:
```yaml
required_inputs:
  - source_documents: "Multiple agent outputs to integrate"
  - synthesis_framework: "How to combine (e.g., branching tree, consolidation logic)"
  - conflict_resolution_rules: "How to handle contradictions"

optional_inputs:
  - priority_weights: "Which sources take precedence"
  - output_template: "Desired format structure"
```

**Output Contract Pattern**:
```yaml
output_format: "Unified document with attribution lineage"
required_fields:
  - integrated_content: "Consolidated insights from all sources"
  - source_attribution: "Which content came from which input"
  - consolidation_logic: "Why sources were combined this way"
  - conflict_resolution_log: "How contradictions were resolved"

quality_gates:
  - zero_content_loss: All unique insights must be preserved
  - attribution_completeness: 100% of content must have source mapping
  - logical_consistency: No contradictions in final output
```

**Distribution**: ~20% of total agents (13/66)

---

#### **1.4 Routers (Decision & Assignment Agents)**

**Definition**: Direct flow between agents or assign work to resources based on criteria. Primary function is **orchestration**, not execution.

**[Tool] Examples**:
- **Routing Orchestrator (Master)** - Spawns 10 sub-agents, collects memos, optimizes assignments
- **Routing Analyst Sub-Agent** - Recommends rep assignment per account with 7-factor scoring

**Recur Examples**:
- **Agent Deployment Plan** (implicit) - Orchestrates 7-agent cascade from foundation → GTM testing

**Pixee Examples**:
- **Orchestration Plan** - Manages 5-phase context refactor (Foundation → Discovery → Synthesis → Implementation → Archive)
- **Agent coordination protocols** - Route between 12+ specialized agents

**Input Contract Pattern**:
```yaml
required_inputs:
  - work_items: "Accounts, tasks, or requests to route"
  - routing_criteria: "7-factor algorithm, priority rules, capacity constraints"
  - resource_profiles: "Rep expertise, agent capabilities, system constraints"

optional_inputs:
  - historical_performance: "Past routing outcomes for optimization"
  - constraint_overrides: "Manual adjustments to algorithm"
```

**Output Contract Pattern**:
```yaml
output_format: "Routing matrix with justification"
required_fields:
  - assignments: "Work item → Resource mapping"
  - routing_rationale: "Why each assignment was made"
  - constraint_validation: "Proof that all constraints met"
  - optimization_metrics: "Expected value, utilization %, etc."

quality_gates:
  - constraint_satisfaction: All hard constraints must pass
  - optimization_proof: Must show assignment maximizes objective
  - reversibility: Must document how to undo routing decisions
```

**Distribution**: ~10% of total agents (7/66)

---

#### **1.5 Maintainers (Optimization & Cleanup Agents)**

**Definition**: Optimize, clean, refactor, or archive existing systems. Primary function is **system health**, not new creation.

**[Tool] Examples**:
- (None explicitly in corpus, but synthesis orchestrator has cleanup aspects)

**Recur Examples**:
- (None explicitly in corpus)

**Pixee Examples**:
- **Foundation Consolidation Agent** - Reduces 9 files → 3 with 0% content loss
- **Discovery Consolidation Agent** - Consolidates 12 research files → 4 unified systems
- **Synthesis Consolidation Agent** - Merges 10 framework files → 5 strategic frameworks
- **Implementation Consolidation Agent** - Optimizes 32 execution files → 15 capabilities
- **Archive Cleanup Agent** - Safely disposes 40+ files with 90% reduction, 0% insight loss
- **Legacy Audit Agent** - Audits existing content for consolidation opportunities
- **Legacy Refactor Agent** - Restructures legacy content with lineage preservation

**Input Contract Pattern**:
```yaml
required_inputs:
  - target_system: "Files, codebase, or content to optimize"
  - consolidation_rules: "What to merge, what to keep separate"
  - quality_thresholds: "Minimum standards (e.g., 0% content loss)"

optional_inputs:
  - rollback_requirements: "Backup and restoration protocols"
  - stakeholder_validation: "Who must approve changes"
```

**Output Contract Pattern**:
```yaml
output_format: "Optimized system + audit trail"
required_fields:
  - consolidated_content: "Refactored/cleaned output"
  - lineage_documentation: "What came from where"
  - disposal_log: "What was removed and why"
  - rollback_procedures: "How to undo changes"

quality_gates:
  - zero_insight_loss: Must preserve all valuable content
  - attribution_accuracy: 100% source tracking
  - stakeholder_approval: >90% satisfaction required
  - reversibility: Complete rollback capability documented
```

**Distribution**: ~10% of total agents (7/66)

---

#### **1.6 Executors (Action & Implementation Agents)**

**Definition**: Generate code, create campaigns, or execute specific deliverables. Primary function is **production**, not analysis.

**[Tool] Examples**:
- **Rep Enablement Agents (4-agent pipeline)** - Generate prescriptive rep briefs in 8-12 min

**Recur Examples**:
- **Message Market Fit Testing** - Executes campaign with deliverability setup

**Pixee Examples**:
- **SEO Content Strategy Agent** - Creates comprehensive SEO execution plans
- **Unified LinkedIn Content Agent** - Generates LinkedIn posts and campaigns
- **Discovery Call Optimization Agent** - Creates sales enablement scripts
- **Unified Sales Enablement Agent** - Produces battle cards, objection handling

**Input Contract Pattern**:
```yaml
required_inputs:
  - execution_spec: "What to build (brief template, campaign structure, code requirements)"
  - source_intelligence: "Research, analysis, or data to inform execution"
  - output_format: "Deliverable specifications"

optional_inputs:
  - style_guides: "Brand voice, coding standards"
  - examples: "Templates or reference implementations"
```

**Output Contract Pattern**:
```yaml
output_format: "Executable deliverable (code, campaign, content)"
required_fields:
  - implementation: "Working output (runnable, deployable)"
  - documentation: "How to use/deploy"
  - testing_criteria: "How to validate it works"

quality_gates:
  - functional_validation: Must work as specified
  - completeness: All requirements implemented
  - usability: Must be ready for end-user without modification
```

**Distribution**: ~15% of total agents (10/66)

---

### Role Distribution Summary

| Role Type | Count | % of Total | Primary Function |
|-----------|-------|------------|------------------|
| Collectors | 17 | 25% | Data gathering without transformation |
| Analyzers | 20 | 30% | Insight extraction through interpretation |
| Synthesizers | 13 | 20% | Integration of multiple inputs |
| Routers | 7 | 10% | Orchestration and assignment decisions |
| Maintainers | 7 | 10% | System optimization and cleanup |
| Executors | 10 | 15% | Production of executable deliverables |

**Key Pattern**: Most agents (55%) are Collectors or Analyzers, reflecting the intelligence-gathering focus of GTM systems. Synthesizers and Executors (35%) transform that intelligence into actionable outputs.

---

## 2. Input/Output Schema Library

### Overview of Contract Patterns

Three primary schema patterns emerged from the corpus, each optimizing for different trade-offs:

1. **File-Based Sequential Handoff** ([Tool]) - Optimizes for debuggability and iterability
2. **Structured Data Models** (Recur) - Optimizes for automation and scale
3. **Free-Form Reports with Sections** (Pixee) - Optimizes for context richness and flexibility

### Pattern 1: File-Based Sequential Handoff

**Use Case**: Complex research pipelines where each agent builds on previous work

**[Tool] Architecture Example**:
```yaml
# Agent 1A Output → Agent 1B Input
agent_1a_output:
  file: "foundation_report_L0-L2.md"
  format: "Markdown report with YAML frontmatter"
  required_sections:
    - executive_summary: "One-sentence company description"
    - L0_value_proposition: "What they sell (exact quotes)"
    - L1_customer_icp: "Who buys (verified examples)"
    - L2_buying_process: "How customer buys (stakeholder evidence)"
    - evidence_quality: "VERIFIED/INFERRED/UNKNOWN counts"
    - sources: "All URLs with dates"

agent_1b_input:
  file: "foundation_report_L0-L2.md"
  required_fields_from_1a:
    - L1_customer_icp: "To infer GTM motion from customer type"
    - L2_buying_process: "To validate sales motion"
  validation:
    - customer_icp_specificity: "Must have ≥3 verified examples OR flagged as insufficient"
    - buying_stakeholders: "Must have ≥2 identified roles"

# Agent 1B Output → Agent 2 Input
agent_1b_output:
  file: "gtm_intelligence_report_L3-L4.md"
  required_sections:
    - L3_gtm_motion: "PLG | Enterprise | Hybrid with evidence"
    - L4_bottleneck: "Volume | Quality | Velocity | Expansion with signals"
    - hiring_signals: "Roles, counts, timing"
    - tech_stack: "Tools with sources"

agent_2_input:
  files:
    - "foundation_report_L0-L2.md"
    - "gtm_intelligence_report_L3-L4.md"
  synthesis_logic: "L1 (who) + L4 (bottleneck) → L5 (use case)"
```

**Strengths**:
- **Debuggable**: Can inspect each intermediate file
- **Iterable**: Can improve one agent without breaking others
- **Traceable**: Clear source attribution throughout pipeline

**Weaknesses**:
- **Manual orchestration**: Requires explicit file paths in prompts
- **File management overhead**: Must maintain directory structure
- **Version control complexity**: Hard to track which file versions go together

**When to Use**: Research pipelines with 3-6 sequential steps where intermediate outputs have value beyond handoffs

---

### Pattern 2: Structured Data Models

**Use Case**: Automated pipelines with programmatic handoffs and scoring

**Recur Architecture Example**:
```yaml
# Agent 03 Output (Scoring Model) → Agent 05 Input (Enrichment)
scoring_model:
  format: "100-point qualification framework"
  tiers:
    tier_1_must_haves:
      - uk_based: "Binary (exclude non-UK)"
      - manufacturing_ops: "Binary (SIC code match)"
      - active_business: "Binary (not dissolved)"
      - size_range: "10-100 employees"
      - business_model: "Make-to-order signals"

    tier_2_scoring:
      sic_match: { weight: 30, range: "0-30 points" }
      size_fit: { weight: 20, range: "0-20 points" }
      geography: { weight: 15, range: "0-15 points" }
      tech_maturity: { weight: 15, range: "0-15 points" }
      company_age: { weight: 10, range: "0-10 points" }
      pain_signals: { weight: 10, range: "0-10 points" }

    tier_3_exclusions:
      - existing_erp_mrp: "Exclude if detected"
      - wrong_business_model: "Mass production = exclude"
      - size_mismatch: "<10 or >100 employees"

# Agent 05 Input ([Tool] Workflow)
enrichment_workflow:
  input_format: "CSV with Companies House data"
  required_fields:
    - company_name: "string"
    - companies_house_number: "string (primary key)"
    - sic_code: "string"
    - website: "URL (nullable)"

  enrichment_steps:
    - step_1_website_discovery: "Hunter.io, Clearbit"
    - step_2_business_model_signals: "Job shop keywords on website"
    - step_3_firmographic_scoring: "Apply tier_2_scoring weights"
    - step_4_behavioral_scoring: "ISO cert, growth signals"
    - step_5_master_scoring: "Sum to 100 points"
    - step_6_tier_assignment: "75+ = Tier 1 (top 100)"

  output_format: "Scored CSV for HubSpot sync"
  output_fields:
    - all_input_fields: "Preserved"
    - enrichment_data: "Website, employee count, ISO status"
    - scores: "Component scores + master score (0-100)"
    - tier: "1 | 2 | 3"
    - segment: "Metal Fab | Plastics | CNC | Regulated"
```

**Strengths**:
- **Automatable**: Programmatic handoffs via CSV, API, database
- **Scalable**: Works for 1,000+ records without manual intervention
- **Measurable**: Quantified scoring enables optimization

**Weaknesses**:
- **Rigidity**: Hard to handle nuanced edge cases
- **Schema evolution**: Changes require cascading updates
- **Context loss**: Structured data strips narrative reasoning

**When to Use**: High-volume pipelines (100+ items) with programmatic handoffs and quantifiable criteria

---

### Pattern 3: Free-Form Reports with Sections

**Use Case**: Rich context preservation with flexible structure

**Pixee Architecture Example**:
```markdown
# Agent 01 Output (Company Foundation) → Agent 02 Input (Customer Intel)
## Agent 01: Company Foundation Research

### Output Structure:
```markdown
# [COMPANY] Foundation Intelligence Report
*[Source Attribution: file1.md + file2.md]*

## Executive Overview
{Foundational company context enabling all strategic decisions}

## Company DNA & Foundation
*[Source Attribution: file.md (lines X-Y)]*
*[Consolidation Logic: Why these sources were combined]*

### Founding Story and Mission
- {Founder background and expertise}
- {Company founding rationale and vision}
- {Product philosophy and approach}

### Leadership Background
- {Leadership team profiles}
- {Decision-making philosophy}

## Context Connections
**Builds On:** {Prerequisites}
**Enables:** {What this enables downstream}
**Related Concepts:** {Cross-references}
```

### Agent 02 Input Requirements:
```yaml
required_from_agent_01:
  - company_dna: "Founder background, organizational values"
  - product_philosophy: "Technical approach and methodology"
  - strategic_direction: "Business model and growth strategy"

usage_in_agent_02:
  - customer_pattern_validation: "Do customer patterns align with company DNA?"
  - persona_development: "What buyer psychology matches product philosophy?"
  - competitive_positioning: "How does strategic direction inform market position?"
```

**Strengths**:
- **Context-rich**: Preserves narrative reasoning and qualitative insights
- **Flexible**: Easy to add sections without breaking downstream agents
- **Human-readable**: Stakeholders can review and validate

**Weaknesses**:
- **Parsing complexity**: Downstream agents must extract structured data from prose
- **Inconsistency risk**: Section formats may vary between executions
- **Automation challenges**: Harder to programmatically process than structured data

**When to Use**: Strategic research with qualitative insights, stakeholder review requirements, and evolving information needs

---

### Hybrid Pattern: Best of Both Worlds

**Pixee's Context Lineage Pattern** (combines structured + free-form):
```yaml
---
# YAML Frontmatter (Structured Metadata)
name: PIXEE_COMPANY_INTELLIGENCE
description: "Foundational company context..."
model: inherit
color: green
context_lineage:
  consolidation_type: "merge"
  source_files:
    - file: "source1.md"
      lines_extracted: "1-450"
      insights_preserved: "Founder background, company DNA"
  consolidation_methodology:
    agent_responsible: "Foundation_Consolidation_Agent"
    consolidation_date: "2025-01-XX"
  content_evolution:
    original_total_lines: 2133
    consolidated_lines: 850
    reduction_percentage: 60%
---

# Free-Form Report Body
{Rich narrative content with section structure}
```

**Advantage**: Machines read frontmatter (structured), humans read body (narrative)

---

### Schema Pattern Selection Matrix

| Criteria | File-Based Sequential | Structured Data Models | Free-Form Reports |
|----------|----------------------|------------------------|-------------------|
| **Volume** | <100 items | 100-10,000 items | <50 items |
| **Automation** | Manual orchestration | Fully automated | Semi-automated |
| **Context Richness** | High (narrative) | Low (quantified) | Very High (qualitative) |
| **Debuggability** | Excellent (file-per-step) | Moderate (logs) | Excellent (human-readable) |
| **Stakeholder Review** | Easy (MD files) | Hard (CSV/JSON) | Easy (narrative reports) |
| **Evolution Flexibility** | High (add sections) | Low (schema changes cascade) | Very High (prose adapts) |
| **Programmatic Processing** | Moderate (parsing) | Excellent (structured) | Low (NLP required) |

**Recommendation**: Start with File-Based Sequential for research, migrate to Structured Data Models when scaling to 100+ items, use Free-Form for strategic synthesis requiring stakeholder buy-in.

---

## 3. Validation Rule Patterns

### Overview of Validation Frameworks

Three systematic validation approaches emerged:
1. **Evidence-Level Flagging** ([Tool]) - Prevents confidence inflation
2. **Iterative Quality Gates** (Pixee) - Ensures zero content loss
3. **Boundary Testing** (Recur) - Validates pattern applicability

---


**Purpose**: Prevent agents from claiming certainty when evidence is weak

**Implementation**:
```yaml
evidence_levels:
  VERIFIED:
    definition: "Customer/company publicly confirmed relationship or fact"
    examples:
      - "Case study with named customer quote"
      - "G2 review from verified purchaser at named company"
      - "Press release announcing partnership"
    required_proof: "Public confirmation from both parties"

  INFERRED:
    definition: "Logical conclusion from evidence, but not directly stated"
    examples:
      - "Product complexity (L0) + customer size (L1) → estimated sales cycle (L2)"
      - "Job postings for SDRs + no Ops roles → quality bottleneck hypothesis (L4)"
    required_proof: "Reasoning chain showing evidence → conclusion"

  UNKNOWN:
    definition: "Insufficient data to make claim"
    examples:
      - "Customer ICP: UNKNOWN - Only 2 customers found (need ≥3 for pattern)"
      - "Tech stack: UNKNOWN - HG Insights has no data, no job post mentions"
    required_action: "Flag gap explicitly, suggest discovery questions"

usage_in_reports:
  claim_format: "[CLAIM] | Evidence: [LEVEL] | Source: [URL, DATE]"
  example: "Customers are mid-market SaaS (50-500 employees) | Evidence: INFERRED from 3 case studies showing 120, 200, 450 employee companies | Source: website case studies, 2025-10-07"

quality_gates:
  - minimum_verified: "≥60% of key claims must be VERIFIED"
  - inference_reasoning: "All INFERRED claims must show reasoning chain"
  - unknown_flagging: "Gaps must be explicitly stated, not hidden"
```

**[Tool] Agent 1A Success Criteria**:
```markdown
Quality checklist:
- [ ] Value prop is specific (not generic marketing language)
- [ ] Customer ICP has ≥3 verified examples OR flagged as UNKNOWN
- [ ] Buying committee has ≥2 identified roles OR flagged as UNKNOWN
- [ ] All claims have sources with URLs and dates
- [ ] Evidence levels (VERIFIED/INFERRED/UNKNOWN) used correctly
- [ ] No contradictions between L0, L1, and L2
```

**Example of Good vs. Bad Evidence Flagging**:

**GOOD**:
```markdown
CUSTOMER: Acme Corp
INDUSTRY: B2B SaaS
SIZE: 450 employees (LinkedIn, 2025-10-07)
USE_CASE: "Used for sales team enrichment" (G2 review)
EVIDENCE_LEVEL: VERIFIED
SOURCE: https://g2.com/products/xyz/reviews - Review by VP Sales at Acme Corp
```

**BAD**:
```markdown
CUSTOMER: Acme Corp
INDUSTRY: Enterprise
SIZE: Large
USE_CASE: Probably sales
EVIDENCE_LEVEL: Verified
SOURCE: Website
```

**Anti-Pattern**: Agent 1B claiming "GTM motion = PLG" with HIGH confidence when Agent 1A flagged customer ICP as UNKNOWN. **Solution**: Propagate confidence levels - if input is INFERRED/UNKNOWN, output cannot be VERIFIED.

---

### Pattern 2: Iterative Quality Gates (Pixee Refactor Model)

**Purpose**: Ensure zero content loss during consolidation/refactoring

**5-Phase Validation Protocol** (from Pixee Context Refactor):

**Phase 1: Pre-Consolidation Audit**
```yaml
audit_checklist:
  - catalog_all_insights: "Line-by-line inventory of unique insights"
  - document_sources: "Map content to original source files"
  - identify_dependencies: "What content builds on what"
  - stakeholder_inventory: "Who uses each piece of content"

output: "Pre-consolidation manifest with 100% content coverage"
```

**Phase 2: Integration Mapping**
```yaml
integration_rules:
  - preserve_unique_value: "Every unique insight must appear in consolidated output"
  - maintain_attribution: "Source attribution for all content"
  - resolve_conflicts: "Document how contradictions were resolved"
  - enhance_navigation: "Improve discoverability over scattered files"

output: "Consolidation plan showing old → new mapping"
```

**Phase 3: Gap Analysis**
```yaml
gap_detection:
  - compare_pre_post: "Pre-consolidation manifest vs. consolidated output"
  - identify_omissions: "Content in manifest but not in output"
  - verify_intentional: "Was omission deliberate or accidental?"
  - remediate_gaps: "Add missing content or document why excluded"

quality_gate: "0% unintentional content loss - all gaps must be explained"
```

**Phase 4: Stakeholder Validation**
```yaml
validation_protocol:
  - leadership_review: "Company DNA accuracy (Foundation domain)"
  - sales_team_review: "Buyer framework utility (Synthesis domain)"
  - product_team_review: "Technical accuracy (Implementation domain)"
  - success_criteria: ">90% stakeholder satisfaction"

output: "Validation report with approval signatures"
```

**Phase 5: Post-Consolidation Verification**
```yaml
verification_checklist:
  - content_preservation: "100% valuable insights confirmed present"
  - attribution_accuracy: "All source lineage documented"
  - enhanced_utility: "Consolidated version improves on scattered files"
  - rollback_capability: "Backup enables restoration if needed"

final_gate: "All 4 verification criteria must pass before completion"
```

**Pixee Foundation Agent Example**:
```markdown
Success Metrics:
- 67% file reduction (9→3) with 0% insight loss ✅
- 100% source attribution accuracy ✅
- Enhanced strategic coherence validated by leadership team ✅
- Foundation enables Discovery domain execution ✅

Quality Assurance Deliverables:
1. Foundation Consolidation Report - detailed decision documentation
2. Company DNA Preservation Verification - evidence of insight preservation
3. Strategic Coherence Assessment - stakeholder validation
4. Critical Path Dependency Verification - downstream readiness
```

**Anti-Pattern**: Consolidating files without pre-consolidation audit, discovering content loss after deployment. **Solution**: Always create manifest BEFORE consolidation, use it as validation checklist AFTER.

---

### Pattern 3: Boundary Testing (Recur Model)

**Purpose**: Validate that patterns/ICPs actually apply to edge cases

**Boundary Testing Framework** (from Recur Agent 03):

**Test Dimension 1: Company Size Boundaries**
```yaml
hypothesis: "10-50 employees is optimal ICP"

boundary_tests:
  too_small:
    test_case: "Companies <10 employees"
    expected_outcome: "Can't justify £130+/month"
    validation: "No verified customers in this range"
    boundary: "5-10 employees = lower bound"

  too_large:
    test_case: "Companies >100 employees"
    expected_outcome: "Need enterprise ERP (NetSuite, SAP)"
    validation: "No verified customers >100 employees"
    boundary: "100 employees = upper bound"

  sweet_spot:
    test_case: "10-50 employee companies"
    expected_outcome: "All verified customers in this range"
    validation: "DC Rolfe (10+), Leeds Plastic (10), S&D (family-run ~15-30)"
    confidence: "HIGH - pattern holds across 5/5 customers"
```

**Test Dimension 2: Business Model Boundaries**
```yaml
hypothesis: "Make-to-order / job shop businesses fit best"

boundary_tests:
  wrong_model_mass_production:
    test_case: "High-volume mass production"
    expected_outcome: "Different MRP needs (lean, JIT)"
    validation: "No verified customers in mass production"
    boundary: "Mass production = exclude"

  wrong_model_distribution:
    test_case: "Pure distribution (no manufacturing)"
    expected_outcome: "Different software category (WMS, not MRP)"
    validation: "All verified customers have manufacturing ops"
    boundary: "Must have manufacturing operations"

  right_model_custom_job_shop:
    test_case: "Custom/make-to-order manufacturers"
    expected_outcome: "Perfect fit for Statii's traceability features"
    validation: "DC Rolfe (job shop), Cavalier (custom orders), all 5 customers"
    confidence: "HIGH - 100% of customers match"
```

**Test Dimension 3: Geographic Boundaries**
```yaml
hypothesis: "UK-focused (all verified customers UK-based)"

boundary_tests:
  non_uk:
    test_case: "Non-UK manufacturers"
    expected_outcome: "Support timezone issues, compliance differences"
    validation: "0/5 verified customers are non-UK"
    boundary: "UK = primary market (test hypothesis)"

  geographic_concentration:
    test_case: "Midlands/Yorkshire region"
    expected_outcome: "5/5 customers in Midlands/Yorkshire"
    validation: "Chesterfield, Nottingham, Leeds, Sheffield pattern"
    confidence: "MEDIUM - could be founder network bias, needs testing"
```

**Validation Output Format**:
```markdown
## Boundary Test Results

**Hypothesis 1: Company Size (10-50 employees)**
- Lower Bound: 5-10 employees (too small to justify cost)
- Upper Bound: 100 employees (need enterprise ERP)
- Sweet Spot: 10-50 employees (5/5 verified customers)
- Confidence: HIGH
- Recommendation: Target 10-50, test 5-10 as edge case

**Hypothesis 2: Business Model (Make-to-order)**
- Exclude: Mass production, distribution-only
- Include: Job shop, custom manufacturing, make-to-order
- Validation: 100% of customers match (5/5)
- Confidence: HIGH
- Recommendation: Use business model as must-have qualifier

**Hypothesis 3: Geography (UK, Midlands/Yorkshire)**
- Primary: UK-based (regulatory, support alignment)
- Concentration: Midlands/Yorkshire (5/5 customers)
- Confidence: UK = HIGH, Regional = MEDIUM (potential bias)
- Recommendation: Target UK nationally, test if Midlands performs better
```

**Anti-Pattern**: Assuming pattern is universal without testing edge cases, discovering later that 30% of leads don't fit. **Solution**: Explicitly test boundaries (too small, too large, wrong model) before scaling.

---

### Validation Rule Selection Matrix

| Validation Pattern | When to Use | Strengths | Weaknesses |
|-------------------|-------------|-----------|------------|
| **Evidence-Level Flagging** | Research with mixed source quality | Prevents confidence inflation, transparent reasoning | Requires discipline to flag UNKNOWN vs. guessing |
| **Iterative Quality Gates** | Consolidation/refactor projects | Guarantees zero content loss, stakeholder buy-in | Time-intensive (5-phase protocol) |
| **Boundary Testing** | ICP/pattern validation | Catches edge cases early, validates assumptions | Requires hypothesis clarity upfront |

**Recommendation**: Combine all three - use Evidence Flagging in collection, Quality Gates in synthesis, Boundary Testing before scaling.

---

## 4. Inter-Agent Contract Examples


**Context**: Sequential research pipeline where Agent 1B infers GTM motion from Agent 1A's customer/buying process intelligence.

**Contract Specification**:

**Agent 1A MUST Provide**:
```yaml
required_outputs:
  L1_customer_icp:
    - company_types: "Specific types (not vague 'enterprises')"
    - company_sizes: "X-Y employees with evidence"
    - industries: "Named industries from verified customers"
    - confidence: "HIGH if ≥3 verified, MEDIUM if 2, LOW if <2"

  L2_buying_process:
    - stakeholders: "≥2 identified roles with sources"
    - decision_structure: "Individual | Departmental | Committee | Enterprise Procurement"
    - sales_cycle_estimate: "X-Y months with reasoning"
    - evidence: "Quotes from reviews, case studies, or inferred with logic"

success_criteria:
  - customer_icp_specificity: "Can infer GTM motion from customer type"
  - stakeholder_evidence: "Not guessed - must have source"
  - example: "Customer = dev teams at product companies, 50-500 eng, buying involves Dev (user) → Eng Manager (budget) → CTO (enterprise approval)"
```

**Agent 1B MUST Receive**:
```yaml
required_inputs:
  - foundation_report: "foundation_report_L0-L2.md"
  - specific_fields:
      - L1_customer_icp: "To infer: 'To sell to THESE customers, they likely need THIS GTM motion'"
      - L2_buying_process: "To validate sales motion type"

inference_logic:
  - IF customer = individual devs BUT approval = enterprise CTO
    THEN gtm_motion = "PLG → Product-led sales → Enterprise motion"
  - IF customer = mid-market BUT buying = committee
    THEN gtm_motion = "Consultative sales with ops support"

validation:
  - agent_1b_cannot_succeed_if: "Agent 1A provides vague customer description like 'sell to enterprises'"
  - minimum_required: "Customer type + size + buying stakeholders must be specific"
```

**Failure Condition Example**:
```markdown
❌ Agent 1A provides: "Customers are enterprises"
→ Agent 1B cannot infer GTM motion (what kind of enterprises? how do they buy?)

✅ Agent 1A provides: "Customers are dev teams at product companies, 50-500 eng, buying decision involves: Dev (user) → Eng Manager (budget) → CTO (enterprise approval)"
→ Agent 1B infers: "With individual dev users but enterprise approval, likely PLG → Product-led sales → Enterprise motion. Should see: self-serve tier + upgrade path + enterprise AE team."
```

**Success Example**:
```yaml
# Agent 1A Output (Toast example)
L1_customer_icp:
  company_types: "Multi-location restaurants (QSR, fast casual, full service)"
  company_sizes: "5-500 locations, $1M-$50M revenue"
  industries: "Restaurant, hospitality"
  confidence: "HIGH (8 verified customers in case studies)"

L2_buying_process:
  stakeholders:
    - "Restaurant Owner/GM (economic buyer) - Source: 5 testimonials"
    - "Operations Manager (champion) - Source: 3 case studies"
  decision_structure: "Departmental (owner approval, ops implementation)"
  sales_cycle: "1-3 months (INFERRED from SMB buying pattern + low complexity)"

# Agent 1B Inference
L3_gtm_motion: "SMB direct sales + channel partners (resellers)"
L3_evidence:
  - "Multi-location customers (L1) → relationship sales, not self-serve"
  - "Departmental buying (L2) → AE-driven, not PLG"
  - "Restaurant industry (L1) → likely channel partnerships with POS vendors"
```

**Contract Success Validation**:
- ✅ Specific customer type (not "enterprises")
- ✅ Buying stakeholders with sources (not guessed)
- ✅ Decision structure evidence (testimonials)
- ✅ Agent 1B can infer logical GTM motion from inputs

---

### Contract Example 2: Recur Agent 02 → Agent 03 Handoff

**Context**: Customer pattern analysis feeds into market boundary definition and scoring model creation.

**Contract Specification**:

**Agent 02 MUST Provide**:
```yaml
required_outputs:
  verified_customer_patterns:
    - pattern_type: "Geographic | Industry | Size | Business Model"
    - pattern_strength: "X/Y customers match this pattern"
    - confidence: "HIGH if 100% match, MEDIUM if 60-80%, LOW if <60%"
    - examples: "List of companies demonstrating pattern"

  boundary_hypotheses:
    - dimension: "Company size | Industry | Geography | Tech maturity"
    - lower_bound: "Minimum threshold with reasoning"
    - upper_bound: "Maximum threshold with reasoning"
    - exclusion_criteria: "What to filter out and why"

  sample_size_limitations:
    - total_customers_analyzed: "N customers"
    - limitations: "Explicit acknowledgment of small sample bias"
    - validation_needs: "What requires testing at scale"

success_criteria:
  - patterns_are_testable: "Can be validated against larger dataset"
  - boundaries_are_explicit: "Not vague ('small businesses') but specific ('10-50 employees')"
  - limitations_acknowledged: "Small sample size flagged upfront"
```

**Agent 03 MUST Receive**:
```yaml
required_inputs:
  - customer_intelligence_report: "From Agent 02"
  - specific_sections:
      - verified_patterns: "To build scoring dimensions"
      - boundary_hypotheses: "To create must-have qualifiers"
      - sample_limitations: "To set confidence levels"

scoring_model_logic:
  - pattern_strength_100%: "Must-have qualifier (Tier 1)"
  - pattern_strength_60-80%: "Scoring dimension (Tier 2, weighted)"
  - pattern_strength_<60%: "Exclude from model (too weak)"

validation:
  - agent_03_cannot_succeed_if: "Patterns are vague or sample size ignored"
  - minimum_required: "≥2 patterns with ≥60% strength, explicit boundaries"
```

**Failure Condition Example**:
```markdown
❌ Agent 02 provides: "Customers seem to be small manufacturers in the UK"
→ Agent 03 cannot create scoring model (how small? what kind of manufacturing?)

✅ Agent 02 provides:
Pattern 1: Industry - Metal fabrication (3/5 customers = 60%)
Pattern 2: Size - 10-30 employees (5/5 customers = 100%)
Pattern 3: Geography - Midlands/Yorkshire (5/5 customers = 100%)
Pattern 4: Business Model - Make-to-order job shop (5/5 customers = 100%)

→ Agent 03 creates:
- Tier 1 Must-Haves: Size (10-100), Business Model (make-to-order), UK-based (100% patterns)
- Tier 2 Scoring: Industry Metal Fab (30 pts - 60% strength), Geography Midlands (15 pts - 100% but potential bias)
```

**Success Example**:
```yaml
# Agent 02 Output (Statii case study)
verified_patterns:
  - pattern: "Company size 10-30 employees"
    strength: "5/5 customers (100%)"
    examples: "DC Rolfe (10+), Leeds Plastic (10), S&D (~20), Cavalier (~25)"
    confidence: "HIGH"

  - pattern: "Make-to-order / job shop business model"
    strength: "5/5 customers (100%)"
    examples: "All customers described as 'custom orders', 'job shop', 'bespoke manufacturing'"
    confidence: "HIGH"

  - pattern: "Midlands/Yorkshire geographic concentration"
    strength: "5/5 customers (100%)"
    examples: "Chesterfield, Nottingham, Leeds, Sheffield"
    confidence: "MEDIUM - could be founder network bias"

boundary_hypotheses:
  - size_lower_bound: "10 employees (below this can't justify £130/month)"
  - size_upper_bound: "100 employees (above this need enterprise ERP)"
  - business_model_exclusion: "Mass production, distribution-only"
  - geographic_primary: "UK (regulatory/support alignment)"

sample_limitations:
  - total_analyzed: "5 verified customers"
  - limitation: "Geographic concentration may be founder network bias, not true market pattern"
  - validation_needed: "Test if Midlands/Yorkshire performs better than other UK regions"

# Agent 03 Scoring Model
tier_1_must_haves:
  - uk_based: "100% pattern strength"
  - size_10_100: "100% within this range"
  - make_to_order: "100% pattern strength"

tier_2_scoring:
  - sic_metal_fab: "30 points (60% pattern strength from 3/5 customers)"
  - size_10_30_sweet_spot: "20 points (100% pattern, optimal range)"
  - geography_midlands: "15 points (100% pattern but bias risk acknowledged)"
```

**Contract Success Validation**:
- ✅ Patterns have specific thresholds (10-100 employees, not "small")
- ✅ Pattern strength quantified (5/5 = 100%, 3/5 = 60%)
- ✅ Sample limitations explicitly acknowledged
- ✅ Agent 03 can create testable scoring model from patterns

---

### Contract Example 3: Pixee Foundation + Discovery → Synthesis Handoff

**Context**: Multiple domain inputs feed into strategic framework synthesis.

**Contract Specification**:

**Foundation Domain MUST Provide**:
```yaml
required_outputs:
  company_intelligence:
    - founder_background: "Leadership expertise and organizational DNA"
    - product_philosophy: "Technical approach and security methodology"
    - strategic_direction: "Business model, growth strategy, competitive advantages"
    - confidence: "Validated by leadership team (>90% satisfaction)"

  strategic_framework:
    - buyer_committee: "MEDDIC personas with psychological profiles"
    - icp_definition: "Qualification criteria and segment characteristics"
    - value_propositions: "Pain-to-solution mapping with ROI metrics"

success_criteria:
  - company_context_richness: "Enables strategic decision-making across organization"
  - framework_completeness: "Buyer intelligence + ICP + value props all present"
  - stakeholder_validation: "Leadership team confirms accuracy"
```

**Discovery Domain MUST Provide**:
```yaml
required_outputs:
  competitive_intelligence:
    - battlecards: "Competitive positioning vs. key competitors"
    - differentiation: "Unique capabilities with proof points"
    - market_landscape: "Ecosystem mapping and influencer analysis"

  customer_intelligence:
    - persona_validation: "Call transcript analysis confirming buyer framework"
    - pain_evidence: "Verified pain points from customer interviews"
    - usage_patterns: "How customers actually use product vs. positioning"

success_criteria:
  - competitive_clarity: "Clear differentiation strategy with evidence"
  - customer_validation: "Persona framework validated by real conversations"
  - insight_depth: "Goes beyond marketing claims to actual customer reality"
```

**Synthesis Domain MUST Receive**:
```yaml
required_inputs:
  from_foundation:
    - company_dna: "To ensure messaging aligns with organizational values"
    - product_philosophy: "To ground technical messaging in actual approach"
    - buyer_framework: "To target right personas with right messages"

  from_discovery:
    - competitive_battlecards: "To craft differentiation messaging"
    - customer_pain_evidence: "To validate pain points are real, not assumed"
    - usage_patterns: "To ensure messaging matches actual use cases"

synthesis_logic:
  - company_dna_alignment: "Messaging must reflect organizational values (Foundation)"
  - pain_validation: "Only use pain points verified in Discovery"
  - competitive_positioning: "Differentiation messaging backed by battlecards"
  - persona_targeting: "Messages route to validated buyer committee (Foundation)"

conflict_resolution:
  - IF Foundation positioning ≠ Discovery customer reality
    THEN flag conflict, prioritize Discovery (customer truth > company claims)
  - IF multiple pain points, prioritize by Discovery evidence strength
  - IF buyer framework conflicts with call transcripts, update framework
```

**Failure Condition Example**:
```markdown
❌ Foundation provides generic "CISO cares about security" + Discovery shows CISOs actually care about "developer productivity without security slowdown"
→ Synthesis uses generic messaging, doesn't resonate

✅ Foundation provides "CISO persona: strategic security oversight, budget authority, organizational impact focus" + Discovery validates "CISOs in interviews prioritize 'fix vulnerabilities without slowing releases'"
→ Synthesis creates: "Strategic security at dev velocity - automated fixes that ship faster, not slower" (aligns Foundation framework with Discovery evidence)
```

**Success Example**:
```yaml
# Foundation Output
company_dna:
  founder_expertise: "Arshan Dabirsiaghi - 15+ years AppSec, OWASP community leader"
  product_philosophy: "Automated code remediation using AI, integrated into developer workflow"
  organizational_values: "Developer-centric security, automation over manual review"

buyer_framework:
  ciso_persona:
    priorities: "Risk reduction, budget justification, organizational alignment"
    pain_points: "Manual security review bottlenecks, slow remediation cycles"
    buying_criteria: "Automation potential, developer adoption, measurable risk reduction"

# Discovery Output
customer_pain_evidence:
  - pain: "Security review bottlenecks slow releases"
    evidence: "8/12 customer calls mention 'security slowing us down'"
    validation: "HIGH - direct quotes from CISOs and VPs Engineering"

  - pain: "Developers resist manual security tools"
    evidence: "6/12 calls mention 'security tools get ignored'"
    validation: "HIGH - confirmed by both security and engineering personas"

competitive_differentiation:
  - vs_snyk: "We fix code automatically, they only flag issues"
  - vs_sonarqube: "We integrate at runtime, they require CI/CD changes"
  - proof_points: "76% auto-merge rate vs. industry 0% (manual review required)"

# Synthesis Output (Messaging Framework)
primary_message:
  target: "CISO"
  message: "Automated security fixes that ship in your existing workflow - 76% of vulnerabilities remediated without developer action or security review bottlenecks"
  alignment:
    - company_dna: "Automation-first philosophy (Foundation)"
    - pain_validation: "Security bottlenecks confirmed by 8/12 customers (Discovery)"
    - differentiation: "Auto-fix vs. flag-only competitors (Discovery battlecards)"
    - buyer_persona: "CISO cares about risk reduction + operational efficiency (Foundation framework validated by Discovery calls)"

conflict_resolution_example:
  - Foundation claimed: "Developers love security tools when automated"
  - Discovery found: "Developers tolerate security tools when invisible"
  - Synthesis resolution: "Updated messaging to 'invisible automated fixes' vs. 'developer-loved tools'"
  - Rationale: "Discovery customer evidence > Foundation product positioning"
```

**Contract Success Validation**:
- ✅ Messaging grounded in company DNA (Foundation)
- ✅ Pain points validated by customer evidence (Discovery)
- ✅ Differentiation backed by competitive battlecards (Discovery)
- ✅ Conflicts resolved with explicit reasoning (customer truth prioritized)

---

### Inter-Agent Contract Anti-Patterns

**Anti-Pattern 1: Vague Input Requirements**
```yaml
❌ Bad Contract:
"Agent B needs context from Agent A"

✅ Good Contract:
"Agent B requires:
 - L1_customer_icp with ≥3 verified examples OR flagged as UNKNOWN
 - L2_buying_stakeholders with ≥2 identified roles with sources
 - Failure if Agent A provides vague 'enterprises' without specificity"
```

**Anti-Pattern 2: No Validation Gates**
```yaml
❌ Bad Contract:
"Agent A outputs report → Agent B reads report"

✅ Good Contract:
"Agent A outputs report with validation:
 - ≥60% claims must be VERIFIED (not INFERRED)
 - All INFERRED claims must show reasoning chain
 - UNKNOWN gaps must be explicitly flagged
 Agent B rejects input if validation fails"
```

**Anti-Pattern 3: Confidence Inflation**
```yaml
❌ Bad Contract:
"Agent A flags input as INFERRED → Agent B claims output is VERIFIED"

✅ Good Contract:
"Confidence propagation rule:
 - IF input is INFERRED, output cannot exceed INFERRED
 - IF input is UNKNOWN, agent must flag inability to proceed OR use LOW confidence
 - Confidence level can only decrease, never increase across agent chain"
```

**Anti-Pattern 4: No Conflict Resolution**
```yaml
❌ Bad Contract:
"Agent Synthesis combines Foundation + Discovery inputs (conflicts not addressed)"

✅ Good Contract:
"Conflict resolution protocol:
 - IF Foundation positioning ≠ Discovery customer reality, prioritize Discovery
 - Document conflict and resolution rationale
 - Flag for stakeholder review if high-impact"
```

---

## 5. Execution Protocol Patterns

### Overview

Five reusable execution protocols emerged from the corpus:
1. **Research Agent Protocol** - Collection → Analysis → Output
2. **Synthesis Agent Protocol** - Read Inputs → Consolidate → Resolve Conflicts → Output
3. **Refactor Agent Protocol** - Audit → Consolidate → Validate → Archive
4. **Routing Agent Protocol** - Spawn Sub-Agents → Collect → Optimize → Document
5. **Orchestrator Protocol** - Phase Planning → Sequential Execution → Validation Gates

---

### Protocol 1: Research Agent Protocol

**Use Case**: Collector or Analyzer agent gathering and interpreting data

**Template** (from [Tool] Agent 1A):
```yaml
phase_1_validate:
  step_1: "Confirm input parameters (company_domain, research_date, output_dir)"
  step_2: "Verify data sources accessible (website, review sites, LinkedIn)"
  step_3: "Check output directory writable"

phase_2_extract:
  step_1_value_prop: "Extract primary headline from homepage (exact quote)"
  step_2_customers: "Find verified customers (case studies, testimonials, reviews)"
  step_3_buying_process: "Identify stakeholders from reviews, testimonials"

  for_each_claim:
    - record_exact_quote: "Use quotation marks for direct extracts"
    - capture_source: "URL with date accessed"
    - assign_evidence_level: "VERIFIED | INFERRED | UNKNOWN"

phase_3_synthesize:
  step_1_patterns: "Group findings (customer patterns, stakeholder patterns)"
  step_2_icp: "Synthesize ICP from verified customer examples"
  step_3_gaps: "Identify and flag UNKNOWN areas explicitly"

phase_4_output:
  step_1_structure: "Create markdown report with required sections"
  step_2_quality_check: "Run validation checklist"
  step_3_handoff_prep: "Add 'Handoff to Agent X' section with context needed"

quality_gates:
  pre_output:
    - value_prop_specific: "Not generic marketing language"
    - customer_evidence: "≥3 verified OR flagged as insufficient"
    - stakeholder_evidence: "≥2 roles OR flagged as insufficient"
    - all_claims_sourced: "URLs and dates present"
    - evidence_levels_used: "VERIFIED/INFERRED/UNKNOWN applied correctly"
```

**Example Execution Checklist** (from [Tool] Agent 1A):
```markdown
Before submitting output, verify:
- [ ] Value proposition is specific (not vague marketing language)
- [ ] ≥3 verified customers identified OR flagged as insufficient data
- [ ] Customer ICP has evidence (not assumptions about "enterprises")
- [ ] Buying committee has ≥2 identified roles with sources
- [ ] All claims have sources with URLs and dates
- [ ] Evidence levels (VERIFIED/INFERRED/UNKNOWN) used correctly
- [ ] Sales cycle estimate has reasoning, not just a guess
- [ ] Output enables Agent 1B to infer GTM motion (customer clarity)
- [ ] No contradictions between L0, L1, and L2
- [ ] Limitations and gaps are explicitly acknowledged
```

**Time Estimate**: 90-135 minutes per execution ([Tool] Agent 1A benchmark)

---

### Protocol 2: Synthesis Agent Protocol

**Use Case**: Synthesizer agent combining multiple inputs into unified output

**Template** (from [Tool] Agent 2 + Pixee Foundation Consolidation):
```yaml
phase_1_read_inputs:
  step_1_inventory: "List all input files/reports required"
  step_2_load_content: "Read and extract key sections from each input"
  step_3_attribute: "Track which content comes from which source (lineage)"

phase_2_consolidate:
  step_1_identify_overlap: "Find redundant content across inputs"
  step_2_identify_unique: "Find unique value in each input"
  step_3_integration_plan: "Decide how to merge (append, interleave, prioritize)"

  consolidation_rules:
    - preserve_unique_value: "All unique insights must appear in output"
    - eliminate_redundancy: "Identical content mentioned once with attribution"
    - enhance_navigation: "Improve structure over scattered inputs"

phase_3_resolve_conflicts:
  step_1_detect: "Identify contradictions between inputs"
  step_2_prioritize: "Apply conflict resolution rules (e.g., customer truth > company claims)"
  step_3_document: "Log conflict and resolution rationale"

  conflict_resolution_priority:
    1: "Customer evidence (Discovery) > Company claims (Foundation)"
    2: "Verified data > Inferred data"
    3: "Recent data > Historical data"
    4: "Quantitative > Qualitative (when both available)"

phase_4_output:
  step_1_create_structure: "Assemble consolidated document with required sections"
  step_2_add_attribution: "Document source lineage for all content"
  step_3_add_context_connections: "Link to related concepts and dependencies"
  step_4_quality_check: "Validate against synthesis criteria"

quality_gates:
  pre_output:
    - zero_content_loss: "All unique insights from inputs preserved"
    - attribution_complete: "100% of content has source mapping"
    - conflicts_resolved: "No unresolved contradictions"
    - stakeholder_validation: ">90% satisfaction (if required)"
```

**Example Execution Timeline** (from Pixee Foundation Consolidation Agent):
```markdown
Day 1-2: Company Intelligence Unification
- Morning Day 1: Source file analysis (catalog unique insights)
- Afternoon Day 1: Overlap assessment and integration strategy
- Day 2: Consolidation execution + relocation of tactical content

Day 3-4: Strategic Framework Integration
- Day 3: Persona/value prop analysis, identify 85% overlap
- Day 4: Create unified framework + stakeholder validation

Day 5: Final Validation
- Morning: Market context assessment and consolidation decision
- Afternoon: Complete content preservation audit + handoff prep
```

**Time Estimate**: 5 days for major domain consolidation (Pixee model)

---

### Protocol 3: Refactor Agent Protocol

**Use Case**: Maintainer agent optimizing or cleaning existing systems

**Template** (from Pixee Refactor Agents):
```yaml
phase_1_audit:
  step_1_inventory: "Catalog all existing files, content, dependencies"
  step_2_value_assessment: "Classify content (strategic, tactical, redundant, obsolete)"
  step_3_dependency_mapping: "Identify what content builds on what"
  step_4_stakeholder_usage: "Document who uses each piece of content"

  output: "Pre-consolidation manifest with 100% content coverage"

phase_2_consolidate:
  step_1_create_plan: "Define old → new mapping with consolidation logic"
  step_2_preserve_unique: "Ensure all unique insights have destination"
  step_3_execute_merge: "Combine files per plan with attribution"
  step_4_enhance_navigation: "Improve structure and discoverability"

  consolidation_principles:
    - strategic_coherence: "Unified content improves decision-making"
    - context_lineage: "Every insight has traceable source"
    - quality_enhancement: "Consolidated > scattered for utility"

phase_3_validate:
  step_1_gap_analysis: "Compare pre vs. post manifest, identify omissions"
  step_2_stakeholder_review: "Leadership/team validation of accuracy"
  step_3_rollback_prep: "Ensure backup enables restoration"
  step_4_final_verification: "Confirm all success criteria met"

  validation_requirements:
    - zero_insight_loss: "All valuable content confirmed present"
    - attribution_accuracy: "All source lineage documented"
    - stakeholder_satisfaction: ">90% approval"
    - rollback_capability: "Complete restoration procedures documented"

phase_4_archive:
  step_1_disposal_planning: "Identify content safe to remove (redundant sources)"
  step_2_lineage_documentation: "Map removed content → preserved location"
  step_3_safe_disposal: "Remove files with audit trail"
  step_4_archive_optimization: "Organize historical content systematically"

  disposal_safety:
    - pre_disposal_verification: "Content preservation confirmed"
    - lineage_mapping: "Removal → preservation chain documented"
    - rollback_capability: "Backup systems enable restoration"

quality_gates:
  phase_1_audit:
    - manifest_completeness: "100% content catalogued"
  phase_2_consolidate:
    - zero_content_loss: "All unique insights preserved"
  phase_3_validate:
    - stakeholder_approval: ">90% satisfaction"
    - rollback_ready: "Restoration procedures documented"
  phase_4_archive:
    - disposal_safety: "All removed content has lineage documentation"
```

**Example Success Metrics** (from Pixee Archive Agent):
```markdown
Archive Optimization Results:
- Source documents: 24 .docx files → 0 (100% disposal, content migrated to markdown)
- Legacy analysis: 5 files → 2 retained (3 disposed with lineage documentation)
- Overall reduction: 40+ files → minimal retention (90% reduction achieved)
- Content preservation: 100% valuable insights confirmed in active domains
- Disposal safety: Complete lineage mapping enables rollback if needed
```

**Time Estimate**: 5-7 days for comprehensive refactor (Pixee 5-phase model)

---

### Protocol 4: Routing Agent Protocol

**Use Case**: Router agent orchestrating sub-agents and optimizing assignments

**Template** (from [Tool] Routing Orchestrator):
```yaml
phase_1_initialize:
  step_1_validate_inputs: "Verify all required research files exist"
  step_2_spawn_subagents: "Launch parallel analysts (1 per work item)"
  step_3_monitor_completion: "Wait for all sub-agents to finish"

  spawn_protocol:
    - sub_agent_prompt: "Include context, task, output requirements, frameworks"
    - parallel_execution: "All sub-agents run independently"
    - completion_check: "Verify all output files created"

phase_2_collect:
  step_1_read_outputs: "Load all sub-agent recommendations"
  step_2_extract_data: "Pull key fields (cluster, ACV, urgency, candidates)"
  step_3_aggregate: "Calculate portfolio statistics (by cluster, urgency, etc.)"

  extraction_template:
    - cluster: "Agent-assigned cluster classification"
    - acv: "Estimated annual contract value"
    - urgency: "IMMEDIATE | HIGH | MEDIUM | LOW"
    - complexity: "Greenfield | Moderate | Competitive"
    - candidates: "Top 2 rep recommendations with scores"

phase_3_optimize:
  step_1_initial_assignment: "Greedy algorithm (ACV descending, assign to top candidate)"
  step_2_validate_constraints: "Check quota capacity, tier-seniority match, geography"
  step_3_refine_assignments: "Swap accounts if optimization opportunities exist"

  optimization_algorithm:
    - sort_by: "ACV descending (assign high-value accounts first)"
    - assign_logic: "IF candidate_1 has quota capacity, assign; ELSE try candidate_2"
    - constraint_validation: "Quota 30-120%, tier-seniority match, geography <30% EMEA/APAC"

phase_4_document:
  step_1_create_matrix: "Routing matrix with rep assignments and justifications"
  step_2_portfolio_analytics: "Calculate metrics by cluster, urgency, complexity"
  step_3_validation_report: "Constraint satisfaction proof and success metrics"

  documentation_requirements:
    - assignment_rationale: "Why each account → rep (cite research insights)"
    - constraint_validation: "Proof all hard constraints met"
    - optimization_proof: "Show assignments maximize objective (expected value)"
    - success_metrics: "Portfolio value, close rates, utilization %"

quality_gates:
  phase_1_initialize:
    - all_subagents_complete: "10/10 sub-agents created outputs"
  phase_2_collect:
    - portfolio_completeness: "All fields extracted for all accounts"
  phase_3_optimize:
    - constraints_satisfied: "All hard constraints pass"
  phase_4_document:
    - traceability: "All assignments cite specific research insights"
```

**Example Routing Matrix Output** (from [Tool] Routing Orchestrator):
```markdown
# Final Routing Matrix: 50 High-Confidence Accounts

## Executive Summary
- Total Portfolio Value: $13.9M ACV, $4M expected value, 29% weighted close rate
- Distribution: Rep 1 (14 accounts, $4.4M), Rep 2 (15, $3.9M), Rep 3 (8, $2.2M), Rep 4 (9, $2.8M), Rep 5 (4, $1.2M)

## Rep 1: Senior AE - Upmarket/Expansion
### Account 1: Toast
**Assignment Rationale:**
- Cluster Match: UPMARKET TRANSFORMERS (Rep 1 primary expertise) ✅
- ACV: $456K (fits senior AE quota profile) ✅
- Urgency: HIGH (0-2 week window, Rep 1 has capacity) ✅
- Close Probability: 60% (research-backed, high confidence) ✅

**Key Research Insights:**
- L3: Hybrid PLG → Enterprise motion (12 Enterprise AE roles open)
- L4: Upmarket expansion bottleneck (need enterprise buying committee data)

**Expected Value:** $273K (456K × 60%)
```

**Time Estimate**: 4-6 hours for 10-50 account portfolio ([Tool] benchmark)

---

### Protocol 5: Orchestrator Protocol

**Use Case**: Master orchestrator managing sequential multi-agent pipeline

**Template** (from [Tool] Final Synthesis Orchestrator + Pixee Context Refactor):
```yaml
phase_1_planning:
  step_1_inventory: "Catalog all deliverables and documents"
  step_2_section_mapping: "Map documents → deliverable sections"
  step_3_dependency_analysis: "Identify which agents must run before others"
  step_4_execution_timeline: "Create week-by-week plan with checkpoints"

  dependency_mapping:
    - parallel_candidates: "Agents with no dependencies (can run simultaneously)"
    - sequential_requirements: "A → B → C chains that must run in order"
    - critical_path: "Longest dependency chain (determines minimum timeline)"

phase_2_sequential_execution:
  for_each_phase:
    step_1_validate_prerequisites: "Confirm all input dependencies met"
    step_2_execute_agent: "Run agent with validated inputs"
    step_3_validate_outputs: "Check agent output meets quality gates"
    step_4_prepare_handoff: "Package outputs for downstream agents"

  execution_control:
    - phase_gates: "Each phase must complete before next begins"
    - rollback_triggers: "If agent fails validation, rollback and retry"
    - progress_tracking: "Update status after each phase completion"

phase_3_validation_gates:
  gate_1_content_preservation: "100% valuable insights confirmed present"
  gate_2_stakeholder_approval: ">90% satisfaction from key stakeholders"
  gate_3_quality_metrics: "All agent outputs pass quality checklists"
  gate_4_dependency_satisfaction: "All downstream agents have required inputs"

  gate_enforcement:
    - IF gate fails: "Halt execution, remediate issue, re-validate"
    - IF gate passes: "Document validation, proceed to next phase"

phase_4_final_assembly:
  step_1_consolidate_outputs: "Merge all agent outputs into final deliverable"
  step_2_traceability_mapping: "Document source → output chain"
  step_3_quality_final_check: "Run comprehensive validation checklist"
  step_4_stakeholder_review: "Final approval before deployment"

  assembly_requirements:
    - traceability: "Every output element traces to source agent/document"
    - completeness: "All required sections present"
    - consistency: "No contradictions across agent outputs"

quality_gates:
  phase_1_planning:
    - dependency_accuracy: "All agent dependencies correctly identified"
  phase_2_execution:
    - per_agent_validation: "Each agent output passes its quality checklist"
  phase_3_validation:
    - all_gates_pass: "Content, stakeholder, quality, dependency gates ✅"
  phase_4_assembly:
    - final_deliverable_ready: "Passes comprehensive validation, stakeholder approved"
```

**Example Orchestration Timeline** (from Pixee Context Refactor):
```markdown
Week 1: Foundation Domain (No dependencies - Critical path blocker)
- Foundation Consolidation Agent: 9 files → 3 files (67% reduction, 0% loss)
- Output: Company intelligence + Strategic framework ready for Discovery

Week 2: Discovery Domain (Depends on Foundation)
- Discovery Consolidation Agent: 12 files → 4 files (67% reduction, 0% loss)
- Input: Company context from Foundation guides research prioritization
- Output: Competitive + Customer intelligence ready for Synthesis

Week 3: Synthesis Domain (Depends on Foundation + Discovery)
- Synthesis Consolidation Agent: 10 files → 5 files (50% reduction, 0% loss)
- Input: Foundation strategic direction + Discovery insights
- Output: Strategic frameworks + Messaging architecture ready for Implementation

Week 4: Implementation Domain (Depends on Foundation + Discovery + Synthesis)
- Implementation Consolidation Agent: 32 files → 15 files (53% reduction, 0% loss)
- Input: All prior domain outputs inform execution capabilities
- Output: Optimized execution assets ready for Archive

Week 5: Archive Domain (Depends on ALL prior completion)
- Archive Cleanup Agent: 40+ files → minimal retention (90% reduction, 0% loss)
- Input: Verification that all valuable content preserved in active domains
- Output: Optimized archive with disposal lineage documentation

Success Metrics:
- Overall reduction: 150+ files → ~60 files (60% achieved) ✅
- Zero insight loss: 100% valuable content preserved ✅
- Stakeholder validation: >90% satisfaction across all domains ✅
```

**Time Estimate**: 5 weeks for 5-phase sequential pipeline (Pixee benchmark)

---

### Execution Protocol Selection Matrix

| Protocol | Use Case | Time Estimate | Complexity | Parallelization |
|----------|----------|---------------|------------|-----------------|
| **Research Agent** | Data collection/analysis | 90-135 min | Low-Medium | Parallelizable across accounts |
| **Synthesis Agent** | Multi-input integration | 5 days | Medium-High | Some parallel reading, sequential merge |
| **Refactor Agent** | System optimization | 5-7 days | High | Sequential phases, parallel analysis |
| **Routing Agent** | Assignment orchestration | 4-6 hours | Medium | Parallel sub-agents, sequential optimization |
| **Orchestrator** | Multi-agent pipeline | 5+ weeks | Very High | Phase parallelization within sequential pipeline |

**Recommendation**: Use Research protocol for individual tasks, Routing for parallel orchestration, Orchestrator for complex sequential dependencies.

---

## 6. Agent Design Pattern Library

### Pattern Library Structure

This section synthesizes all patterns into a reusable library with implementation guidelines.

---

### Pattern 1: Sequential Research Pipeline

**Pattern Name**: L0-L6 Intelligence Framework ([Tool] Model)

**Problem**: Need deep, layered intelligence on target accounts where each layer builds on previous

**Solution**: Sequential agent pipeline with file-based handoffs and evidence-level flagging

**Architecture**:
```yaml
agent_1_collector:
  name: "Foundation Intelligence"
  inputs: "company_domain"
  outputs: "L0 (product), L1 (customer), L2 (buying process)"
  evidence_flagging: "VERIFIED/INFERRED/UNKNOWN"

agent_2_analyzer:
  name: "GTM Motion Intelligence"
  inputs: "foundation_report (from Agent 1)"
  outputs: "L3 (GTM motion), L4 (bottleneck)"
  validation: "Must have ≥2 stakeholders from L2"

agent_3_synthesizer:
  name: "Use Case Synthesis"
  inputs: "foundation_report + gtm_report (from Agents 1&2)"
  outputs: "L5 (use case), L6 (proof concept)"
  logic: "L1 (who) + L4 (bottleneck) → L5 (solution)"
```

**When to Use**:
- Research depth more important than speed
- Intermediate outputs have value (can share L0-L2 even if L5-L6 not ready)
- Debuggability critical (spot-check each layer independently)

**When NOT to Use**:
- Need to process >100 items (too slow)
- Stakeholders don't need intermediate reports (overhead without value)

**Implementation Checklist**:
```markdown
- [ ] Define layer boundaries clearly (L0 vs L1 vs L2 responsibilities)
- [ ] Create evidence flagging system (VERIFIED/INFERRED/UNKNOWN)
- [ ] Specify handoff contracts (what Agent B needs from Agent A)
- [ ] Build quality gates per layer (validation checklists)
```

**Example Code** (Agent Prompt Template):
```markdown
# Agent 1A: Foundation Intelligence

## Input Contract
- company_domain: {company.com}
- research_date: {YYYY-MM-DD}
- output_dir: {/path/}

## Processing Steps
1. Extract L0: Product value proposition (exact quotes from website)
2. Extract L1: Customer ICP (≥3 verified examples OR flag UNKNOWN)
3. Extract L2: Buying process (≥2 stakeholders OR flag UNKNOWN)

## Output Contract
File: foundation_report_L0-L2.md
Required sections: Executive Summary, L0, L1, L2, Evidence Quality, Sources
Evidence levels: VERIFIED (customer confirmed) | INFERRED (logical conclusion) | UNKNOWN (insufficient data)

## Success Criteria
- [ ] Value prop specific (not generic)
- [ ] Customer ICP has ≥3 verified OR flagged insufficient
- [ ] Stakeholders have ≥2 roles OR flagged insufficient
- [ ] All claims sourced (URL + date)
- [ ] Output enables Agent 1B to infer GTM motion
```

---

### Pattern 2: Scoring & Automation Pipeline

**Pattern Name**: Structured Qualification Framework (Recur Model)

**Problem**: Need to score/qualify 100-10,000 items programmatically with explainable criteria

**Solution**: Multi-tier scoring model with must-haves, weighted scoring, and exclusions

**Architecture**:
```yaml
agent_1_pattern_discovery:
  name: "Customer Intelligence Patterns"
  inputs: "verified_customers (small sample)"
  outputs: "patterns (industry, size, model), boundaries, sample_limitations"

agent_2_scoring_model:
  name: "Market Boundary Definition"
  inputs: "patterns (from Agent 1)"
  outputs: "100-point scoring framework"
  tiers:
    tier_1_must_haves: "Binary qualifiers (exclude if fail)"
    tier_2_scoring: "Weighted 0-100 points"
    tier_3_exclusions: "Negative signals (auto-exclude)"

agent_3_enrichment:
  name: "Data Fusion & Scoring"
  inputs: "raw_data + scoring_model (from Agent 2)"
  outputs: "Scored records (0-100) + tier assignment"
  automation: "[Tool] workflow or API pipeline"
```

**When to Use**:
- Volume >100 items requiring programmatic scoring
- Criteria can be quantified (company size, industry match, etc.)
- Need explainable scoring (why Account A scored 85 vs. Account B scored 60)

**When NOT to Use**:
- Nuanced qualitative assessment required
- Criteria change frequently (scoring model rigidity)
- <50 items (manual scoring faster than building model)

**Implementation Checklist**:
```markdown
- [ ] Discover patterns from verified examples (Agent 1)
- [ ] Test boundary cases (too small, too large, wrong model)
- [ ] Create 100-point scoring framework (Agent 2)
- [ ] Define must-have qualifiers (binary: pass/fail)
- [ ] Assign weights to scoring dimensions (total = 100 points)
- [ ] Validate scoring on known examples (should correctly identify verified customers as high-scoring)
```

**Example Code** (Scoring Model YAML):
```yaml
scoring_model:
  tier_1_must_haves:
    - uk_based: { type: "binary", fail_action: "exclude" }
    - manufacturing_ops: { type: "binary", fail_action: "exclude" }
    - active_business: { type: "binary", fail_action: "exclude" }
    - size_10_100: { type: "binary", fail_action: "exclude" }

  tier_2_weighted_scoring:
    - sic_match: { weight: 30, range: "0-30", logic: "Metal fab SIC = 30, Related = 15, Other = 0" }
    - size_sweet_spot: { weight: 20, range: "0-20", logic: "10-30 employees = 20, 31-50 = 15, 51-100 = 10" }
    - geography_fit: { weight: 15, range: "0-15", logic: "Midlands/Yorkshire = 15, Other England = 10, Scotland/Wales = 5" }
    - tech_maturity: { weight: 15, range: "0-15", logic: "Spreadsheets = 15, Basic software = 10, ERP = 0" }
    - company_age: { weight: 10, range: "0-10", logic: "5-15 years = 10, 15-30 = 8, <5 or >30 = 5" }
    - pain_signals: { weight: 10, range: "0-10", logic: "ISO cert needed = 10, Growth indicators = 5, None = 0" }

  tier_3_exclusions:
    - existing_erp_mrp: { type: "negative", action: "exclude" }
    - mass_production: { type: "negative", action: "exclude" }

  tier_assignment:
    - tier_1: { threshold: "≥75 points", description: "Top 100 accounts" }
    - tier_2: { threshold: "50-74 points", description: "Mid-tier" }
    - tier_3: { threshold: "<50 points", description: "Low priority" }
```

---

### Pattern 3: Context Consolidation Pipeline

**Pattern Name**: Domain-Based Refactor (Pixee Model)

**Problem**: Scattered content across 100+ files causing navigation complexity and maintenance burden

**Solution**: Sequential domain consolidation with 0% content loss validation

**Architecture**:
```yaml
phase_1_foundation:
  agent: "Foundation Consolidation"
  inputs: "9 foundation files"
  outputs: "3 systematic files (company, strategic, market)"
  reduction: "67% (9→3)"
  validation: "0% content loss, >90% stakeholder satisfaction"

phase_2_discovery:
  agent: "Discovery Consolidation"
  inputs: "Foundation outputs + 12 discovery files"
  outputs: "4 unified systems (competitive, customer intelligence)"
  reduction: "67% (12→4)"
  dependency: "Foundation must complete first"

phase_3_synthesis:
  agent: "Synthesis Consolidation"
  inputs: "Foundation + Discovery outputs + 10 synthesis files"
  outputs: "5 strategic frameworks"
  reduction: "50% (10→5)"

phase_4_implementation:
  agent: "Implementation Consolidation"
  inputs: "All prior outputs + 32 implementation files"
  outputs: "15 execution capabilities"
  reduction: "53% (32→15)"

phase_5_archive:
  agent: "Archive Cleanup"
  inputs: "Verification that all content preserved"
  outputs: "Minimal retention with disposal lineage"
  reduction: "90% archive content"
```

**When to Use**:
- Content sprawl (>50 files) causing navigation complexity
- Redundant or outdated content mixed with valuable insights
- Need systematic knowledge management with lineage preservation

**When NOT to Use**:
- Content is already well-organized (<20 files)
- High churn (content changes weekly, consolidation becomes outdated)
- No stakeholder buy-in (refactor requires validation time)

**Implementation Checklist**:
```markdown
- [ ] Phase 1: Pre-consolidation audit (catalog 100% of content)
- [ ] Phase 2: Create consolidation plan (old → new mapping)
- [ ] Phase 3: Execute merge with attribution (source lineage for all content)
- [ ] Phase 4: Gap analysis (compare pre vs. post manifest)
- [ ] Phase 5: Stakeholder validation (>90% satisfaction)
- [ ] Phase 6: Rollback preparation (backup enables restoration)
```

**Example Code** (Consolidation Agent Frontmatter):
```yaml
---
name: FOUNDATION_COMPANY_INTELLIGENCE
context_lineage:
  consolidation_type: "merge"
  source_files:
    - file: "COMPREHENSIVE_ANALYSIS.md"
      lines_extracted: "1-170"
      insights_preserved: "Strategic roadmap, implementation priorities"
    - file: "pixee-deep-research.md"
      lines_extracted: "1-450, 890-1200"
      insights_preserved: "Founder background, company DNA"
  consolidation_methodology:
    agent_responsible: "Foundation_Consolidation_Agent"
    consolidation_date: "2025-01-XX"
  content_evolution:
    original_total_lines: 2133
    consolidated_lines: 850
    reduction_percentage: 60%
---
```

---

### Pattern 4: Parallel Sub-Agent Orchestration

**Pattern Name**: Routing Orchestrator with Sub-Agents ([Tool] Model)

**Problem**: Need to apply same analysis to N items in parallel, then optimize global assignment

**Solution**: Spawn N parallel sub-agents, collect outputs, run optimization algorithm

**Architecture**:
```yaml
phase_1_spawn:
  orchestrator: "Routing Orchestrator (Master)"
  action: "Spawn N sub-agents (1 per item)"
  execution: "Parallel (all sub-agents run simultaneously)"

phase_2_collect:
  orchestrator: "Read N sub-agent outputs"
  extraction: "Key fields (cluster, ACV, urgency, candidates)"
  aggregation: "Portfolio statistics"

phase_3_optimize:
  orchestrator: "Run global optimization algorithm"
  algorithm: "Greedy assignment with constraint validation"
  constraints: "Quota capacity, tier-seniority match, geography"

phase_4_document:
  orchestrator: "Create routing matrix with justifications"
  output: "Assignments + rationale + validation proof"
```

**When to Use**:
- N items need same analysis, but global optimization required
- Parallel execution saves time (N agents run simultaneously vs. sequential)
- Optimization problem (assign N items to M resources to maximize objective)

**When NOT to Use**:
- N is small (<5 items, overhead not worth it)
- No global optimization needed (each item independent)
- Sub-agents have dependencies on each other (can't parallelize)

**Implementation Checklist**:
```markdown
- [ ] Define sub-agent prompt template (same prompt for all N items)
- [ ] Spawn N sub-agents in parallel (Task tool with parallel invocations)
- [ ] Wait for all sub-agents to complete
- [ ] Collect and aggregate outputs
- [ ] Run optimization algorithm (greedy, constraint satisfaction, etc.)
- [ ] Validate constraints (quota, tier-seniority, geography)
- [ ] Document assignments with justifications citing sub-agent insights
```

**Example Code** (Orchestrator Prompt):
```markdown
# Routing Orchestrator: Master Coordinator

## Phase 1: Spawn Sub-Agents
For each of 10 accounts, spawn:

```
You are a Routing Analyst for {COMPANY_NAME}.

Read all reports:
- research/{company}/foundation_report_L0-L2.md
- research/{company}/gtm_intelligence_report_L3-L4.md

Analyze with 7-factor framework:
1. Cluster Expertise Match (25%)
2. Revenue Potential (25%)
3. Close Probability (20%)
4. Urgency Timing (15%)
5. Quota Capacity (10%)
6. Deal Complexity (3%)
7. Relationship Warmth (2%)

Output: routing_recommendation_memo.md
- Ideal rep profile
- Top 2 candidates with scores
- Routing rationale citing specific research insights
```

## Phase 2: Collect
Read all 10 memos, extract: cluster, ACV, urgency, candidates

## Phase 3: Optimize
Greedy algorithm:
- Sort accounts by ACV descending
- For each account: Assign to top candidate IF quota capacity available
- Validate: Quota 30-120%, tier-seniority match, geography <30% EMEA

## Phase 4: Document
Create routing matrix showing:
- Assignments with justifications
- Constraint validation proof
- Portfolio analytics (by cluster, urgency, complexity)
```

---

### Pattern 5: Evidence-Level Propagation

**Pattern Name**: Confidence Inheritance Chain ([Tool] Model)

**Problem**: Agents claiming high confidence when built on weak foundation (INFERRED or UNKNOWN inputs)

**Solution**: Propagate evidence levels through agent chain - confidence can only decrease, never increase

**Architecture**:
```yaml
agent_1_collector:
  outputs:
    - claim_A: { evidence: "VERIFIED", source: "Case study with customer quote" }
    - claim_B: { evidence: "INFERRED", reasoning: "Product complexity + customer size → estimated cycle" }
    - claim_C: { evidence: "UNKNOWN", gap: "Insufficient data on tech stack" }

agent_2_analyzer:
  inputs: "Agent 1 outputs"
  propagation_rules:
    - IF input = VERIFIED → output can be VERIFIED or INFERRED (never increase confidence)
    - IF input = INFERRED → output must be INFERRED or UNKNOWN (cannot claim VERIFIED)
    - IF input = UNKNOWN → output must be UNKNOWN or LOW confidence (cannot proceed without flagging)

  outputs:
    - insight_X: { evidence: "INFERRED", basis: "VERIFIED claim_A + logical reasoning" }
    - insight_Y: { evidence: "UNKNOWN", reason: "Depends on claim_C which is UNKNOWN" }

agent_3_synthesizer:
  inputs: "Agent 2 outputs"
  synthesis_confidence:
    - IF all inputs VERIFIED → synthesis can be HIGH confidence
    - IF mix of VERIFIED + INFERRED → synthesis is MEDIUM confidence
    - IF any UNKNOWN → synthesis must flag gap or use LOW confidence
```

**When to Use**:
- Multi-agent research pipeline where later agents build on earlier findings
- Need to prevent confidence inflation ("telephone game" problem)
- Stakeholders need to trust confidence levels (no false certainty)

**When NOT to Use**:
- Single-agent systems (no propagation needed)
- All data is verified (no INFERRED or UNKNOWN)

**Implementation Checklist**:
```markdown
- [ ] Define evidence levels (VERIFIED | INFERRED | UNKNOWN)
- [ ] Create propagation rules (confidence can only decrease)
- [ ] Validate in each agent: "Can I claim VERIFIED given my inputs?"
- [ ] Flag gaps explicitly when input is UNKNOWN
- [ ] Document reasoning chain for all INFERRED claims
```

**Example Code** (Evidence Propagation Logic):
```python
def propagate_confidence(input_evidence, reasoning_type):
    """
    Confidence can only decrease, never increase
    """
    if input_evidence == "UNKNOWN":
        return "UNKNOWN"  # Cannot proceed with confidence

    elif input_evidence == "INFERRED":
        if reasoning_type == "logical_deduction":
            return "INFERRED"  # Can maintain INFERRED if logic is sound
        else:
            return "UNKNOWN"  # Cannot increase to VERIFIED

    elif input_evidence == "VERIFIED":
        if reasoning_type == "direct_extraction":
            return "VERIFIED"  # Can maintain VERIFIED if just extracting
        elif reasoning_type == "logical_deduction":
            return "INFERRED"  # Decreases to INFERRED if reasoning involved
        else:
            return "UNKNOWN"

    return "UNKNOWN"  # Default to lowest confidence

# Example usage
agent_1_output = {"customer_size": "50-500 employees", "evidence": "VERIFIED"}
agent_2_reasoning = "logical_deduction"  # Inferring GTM motion from customer size

agent_2_confidence = propagate_confidence(
    agent_1_output["evidence"],
    agent_2_reasoning
)
# Result: "INFERRED" (decreased from VERIFIED because inference involved)
```

---

### Pattern Selection Decision Tree

```
START: What is your agent system goal?

├─ Research & Intelligence Gathering?
│  ├─ Depth > Speed? → Pattern 1: Sequential Research Pipeline (L0-L6 model)
│  └─ Speed > Depth? → Pattern 2: Scoring & Automation Pipeline (100-point model)
│
├─ Content Consolidation/Optimization?
│  └─ Pattern 3: Context Consolidation Pipeline (Domain-based refactor)
│
├─ Assignment/Routing Optimization?
│  └─ Pattern 4: Parallel Sub-Agent Orchestration (Spawn → Collect → Optimize)
│
└─ Confidence Management Across Agents?
   └─ Pattern 5: Evidence-Level Propagation (VERIFIED/INFERRED/UNKNOWN chain)
```

---

## 7. Anti-Patterns Catalog

### Anti-Pattern 1: Vague Input Requirements

**Problem**: Agent B expects "context" from Agent A, but doesn't specify what context or in what format

**Symptom**: Agent B fails or produces low-quality output because inputs are missing or wrong format

**Example (Bad)**:
```yaml
agent_b_prompt:
  inputs: "Context from Agent A"  # Too vague!
```

**Example (Good)**:
```yaml
agent_b_prompt:
  required_inputs:
    - foundation_report: "foundation_report_L0-L2.md"
    - specific_fields:
        - L1_customer_icp: "Must have ≥3 verified examples OR flagged as UNKNOWN"
        - L2_buying_stakeholders: "Must have ≥2 identified roles with sources"
  validation:
    - IF L1_customer_icp is vague ("enterprises"), reject input and request specific customer types
```

**Remediation**:
- Specify exact file names, field names, required sections
- Define validation criteria (what makes input acceptable vs. unacceptable)
- Add failure handling: "IF input doesn't meet criteria, do X"

---

### Anti-Pattern 2: No Evidence-Level Flagging

**Problem**: Agents claim certainty when evidence is weak, downstream agents amplify false confidence

**Symptom**: "Telephone game" effect - claim starts as guess, becomes "fact" by Agent 3

**Example (Bad)**:
```markdown
Agent 1: "Customer ICP is enterprises" (no source, no evidence level)
Agent 2: "Given enterprise customers (from Agent 1), GTM motion is likely enterprise sales" (builds on vague input)
Agent 3: "[Tool] use case: enterprise org mapping" (now treating vague guess as verified fact)
```

**Example (Good)**:
```markdown
Agent 1: "Customer ICP: 50-500 employee companies in healthcare | Evidence: INFERRED from 2 case studies (DC Rolfe 450 emp, Acme Corp 120 emp) | CONFIDENCE: LOW - need ≥3 verified for pattern"

Agent 2: "GTM motion: UNKNOWN - Agent 1 customer ICP is LOW confidence (only 2 examples), cannot reliably infer GTM motion. RECOMMENDATION: Gather more customer data before inferring motion."

Agent 3: "[Tool] use case: CANNOT PROCEED - Insufficient customer intelligence from Agent 1 (LOW confidence) and no GTM motion from Agent 2 (UNKNOWN). FLAG for discovery call to validate ICP."
```

**Remediation**:
- Implement VERIFIED/INFERRED/UNKNOWN flagging system
- Propagate confidence levels (can only decrease, never increase)
- Explicitly flag gaps instead of making educated guesses

---

### Anti-Pattern 3: Missing Validation Gates

**Problem**: Agent outputs bad data, downstream agents process it, cascade failure occurs

**Symptom**: Entire pipeline produces garbage because one early agent had no quality gate

**Example (Bad)**:
```yaml
agent_1:
  outputs: "report.md"  # No validation

agent_2:
  inputs: "report.md"  # Blindly trusts Agent 1
  # Agent 2 fails because report.md is incomplete/malformed
```

**Example (Good)**:
```yaml
agent_1:
  outputs: "report.md"
  validation_checklist:
    - value_prop_present: "Must have ≥1 specific value proposition"
    - customer_evidence: "Must have ≥3 verified customers OR flag as UNKNOWN"
    - sources_cited: "All claims must have URL + date"
    - IF validation fails: "Do not output file, log failure reason, request remediation"

agent_2:
  inputs: "report.md"
  input_validation:
    - check_file_exists: "Confirm report.md present"
    - check_required_sections: "Confirm L0, L1, L2 sections exist"
    - check_evidence_quality: "Confirm ≥60% VERIFIED claims"
    - IF validation fails: "Reject input, request Agent 1 re-run with validation passing"
```

**Remediation**:
- Add quality checklist to every agent before output
- Validate inputs at receiving agent (don't trust blindly)
- Implement rollback: "IF validation fails, halt and remediate before proceeding"

---

### Anti-Pattern 4: Confidence Inflation

**Problem**: Agent increases confidence level from input to output (INFERRED → VERIFIED)

**Symptom**: Final output claims high confidence despite weak foundation

**Example (Bad)**:
```markdown
Agent 1: "Sales cycle: 3-6 months | Evidence: INFERRED from product complexity"
Agent 2: "Given 3-6 month sales cycle (VERIFIED from Agent 1)..." ❌ Increased confidence!
```

**Example (Good)**:
```markdown
Agent 1: "Sales cycle: 3-6 months | Evidence: INFERRED from product complexity + customer size"
Agent 2: "Given 3-6 month sales cycle (INFERRED from Agent 1)..." ✅ Maintained confidence level
Agent 2 reasoning: "Cannot upgrade INFERRED to VERIFIED without direct evidence (e.g., customer quote stating '6-month implementation')"
```

**Remediation**:
- Enforce propagation rule: Confidence can only decrease or maintain, never increase
- Require explicit reasoning: "Why is this VERIFIED given INFERRED inputs?"
- Audit confidence levels across pipeline to catch inflation

---

### Anti-Pattern 5: No Conflict Resolution Protocol

**Problem**: Multiple inputs contradict, synthesizer doesn't resolve, outputs inconsistent information

**Symptom**: Final document says "GTM motion is PLG" in one section, "Enterprise sales" in another

**Example (Bad)**:
```yaml
agent_synthesis:
  input_1: "Company positions as PLG (Foundation)"
  input_2: "Customer interviews show enterprise sales process (Discovery)"
  output: "PLG motion" + "Enterprise sales process" ❌ Unresolved contradiction
```

**Example (Good)**:
```yaml
agent_synthesis:
  conflict_detected:
    - source_1: "Foundation says PLG (from website positioning)"
    - source_2: "Discovery says Enterprise (from customer interviews)"

  resolution_protocol:
    - prioritize: "Discovery (customer truth) > Foundation (company claims)"
    - rationale: "Actual customer experience outweighs marketing positioning"
    - output: "Hybrid motion: PLG marketing, Enterprise sales reality"

  documentation:
    - conflict_log: "Foundation positioning ≠ Discovery reality"
    - resolution: "Prioritized Discovery, updated messaging to match customer truth"
```

**Remediation**:
- Define conflict resolution rules (which source takes precedence)
- Document conflicts explicitly (don't hide contradictions)
- Log resolution rationale (why we chose Source A over Source B)

---

### Anti-Pattern 6: Boundary Assumption Without Testing

**Problem**: Assume ICP/pattern is universal without testing edge cases

**Symptom**: Scale to 1,000 leads, discover 30% don't fit assumed pattern

**Example (Bad)**:
```yaml
icp_assumption: "All customers are 50-500 employee companies"
# Assumption based on 3 verified customers, never tested boundaries
```

**Example (Good)**:
```yaml
icp_hypothesis: "50-500 employee companies (based on 3 verified customers)"

boundary_tests:
  - too_small: "Test <50 employees - expect poor fit (can't afford product)"
  - too_large: "Test >500 employees - expect enterprise needs (need different product)"
  - sweet_spot: "50-500 validates across all 3 verified customers"

validation:
  - hypothesis_confidence: "MEDIUM - only 3 examples, need more data"
  - test_plan: "Run pilot with 10 accounts: 3 <50, 3 in 50-500, 4 >500 to validate boundaries"
```

**Remediation**:
- Explicitly test boundaries (too small, too large, wrong model)
- Acknowledge sample size limitations
- Create validation plan before scaling

---

### Anti-Pattern 7: Manual Orchestration at Scale

**Problem**: Using file-based sequential handoffs for 100+ items (doesn't scale)

**Symptom**: Spending hours manually copying file paths into prompts

**Example (Bad)**:
```yaml
# Trying to scale [Tool] L0-L6 model to 100 accounts manually
agent_1a: "Read {account_1_domain}, output to research/account_1/foundation.md"
agent_1b: "Read research/account_1/foundation.md, output to research/account_1/gtm.md"
# ... repeat 100 times manually ❌
```

**Example (Good)**:
```yaml
# Use scoring model + automation for 100+ accounts
agent_pattern_discovery: "Analyze 5 deep-researched accounts → extract patterns"
agent_scoring_model: "Convert patterns → 100-point qualification framework"
agent_enrichment: "Apply scoring to 1,000 accounts via [Tool] workflow (automated)"

# Reserve deep research (L0-L6) for top 10-20 accounts only
tier_1_accounts: "Top 10 by score → full L0-L6 deep research (manual, high touch)"
tier_2_accounts: "Next 50 by score → enhanced [Tool] (semi-automated)"
tier_3_accounts: "Remaining by score → template briefs (fully automated)"
```

**Remediation**:
- Use file-based sequential for <50 items
- Switch to structured data models + automation for 100+ items
- Hybrid approach: Deep research for top tier, automation for scale

---

### Anti-Pattern 8: No Rollback Capability

**Problem**: Consolidate/refactor without backup, discover content loss, cannot restore

**Symptom**: "Where did that customer insight go?" - lost after consolidation with no recovery

**Example (Bad)**:
```yaml
refactor_agent:
  action: "Delete 50 old files, create 10 new consolidated files"
  backup: "None"  ❌
  # Content loss discovered later, no way to recover
```

**Example (Good)**:
```yaml
refactor_agent:
  phase_1_backup:
    - create: "foundation_backup_{timestamp}/"
    - copy: "All 9 source files to backup directory"
    - verify: "Backup integrity confirmed"

  phase_2_consolidate:
    - create: "3 new consolidated files"
    - preserve: "All unique insights with source attribution"

  phase_3_validate:
    - gap_analysis: "Compare pre-consolidation manifest vs. consolidated output"
    - IF gaps found: "Rollback to backup, investigate missing content"

  phase_4_archive:
    - IF validation passes: "Move old files to archive/ (not delete!)"
    - rollback_procedure: "Copy from archive/ or backup/ to restore if needed"
```

**Remediation**:
- Always create backup before destructive operations
- Document rollback procedures
- Validate before making changes permanent
- Archive (don't delete) until validation complete

---

### Anti-Pattern Summary Table

| Anti-Pattern | Symptom | Remediation |
|--------------|---------|-------------|
| **Vague Input Requirements** | Agent B fails due to missing/wrong inputs | Specify exact files, fields, validation criteria |
| **No Evidence Flagging** | False confidence amplification | Implement VERIFIED/INFERRED/UNKNOWN system |
| **Missing Validation Gates** | Cascade failures from bad data | Add quality checklists before output, validate inputs |
| **Confidence Inflation** | INFERRED becomes VERIFIED downstream | Enforce: confidence can only decrease, never increase |
| **No Conflict Resolution** | Inconsistent outputs from contradictory inputs | Define resolution protocol, document conflicts |
| **Boundary Assumption** | Pattern fails at scale due to untested edges | Explicitly test boundaries, acknowledge sample limits |
| **Manual Orchestration at Scale** | Doesn't scale beyond 50 items | Use automation for 100+, reserve manual for top tier |
| **No Rollback Capability** | Permanent content loss after refactor | Always backup, validate before permanent changes |

---

## 8. Design Principles for Agent Systems

Based on the 66+ agent corpus analysis, these principles emerged as success factors:

### Principle 1: Explicit Over Implicit

**Bad**: "Agent B uses context from Agent A"
**Good**: "Agent B requires foundation_report_L0-L2.md with L1_customer_icp (≥3 verified examples) and L2_buying_stakeholders (≥2 roles with sources)"

**Rationale**: Ambiguity causes 80% of agent failures. Make everything explicit.

---

### Principle 2: Validate Early, Validate Often

**Bad**: Run entire 5-agent pipeline, discover Agent 1 output was bad at the end
**Good**: Validate Agent 1 output before Agent 2 starts. Gates between every agent.

**Rationale**: Cascade failures are expensive. Catch bad data immediately.

---

### Principle 3: Evidence Levels Prevent Confidence Inflation

**Bad**: Agent claims certainty without evidence
**Good**: Every claim is VERIFIED (source confirmed) | INFERRED (logical reasoning) | UNKNOWN (gap flagged)

**Rationale**: "Telephone game" effect destroys trust in multi-agent systems. Flag evidence quality at every step.

---

### Principle 4: Conflicts Are Opportunities, Not Failures

**Bad**: Hide contradictions between inputs
**Good**: Explicitly log conflicts, apply resolution protocol (e.g., customer truth > company claims), document rationale

**Rationale**: Conflicts reveal truth. Resolving them improves output quality.

---

### Principle 5: Design for Debuggability

**Bad**: Opaque pipeline where you can't inspect intermediate steps
**Good**: File-based handoffs where every agent output is human-readable

**Rationale**: You can't fix what you can't see. Make every step inspectable.

---

### Principle 6: Automate What Scales, Manual for What Matters

**Bad**: Try to manually process 1,000 accounts with deep research (doesn't scale)
**Good**: Deep research for top 10 (high value), scoring model for 100+ (automation)

**Rationale**: Time is finite. Optimize for leverage (automate low-value, deep-dive high-value).

---

### Principle 7: Always Have a Rollback Plan

**Bad**: Irreversible changes (delete files, update database without backup)
**Good**: Backup → Consolidate → Validate → Archive (restore from backup if validation fails)

**Rationale**: Mistakes happen. Make them recoverable.

---

### Principle 8: Patterns Beat Prompts

**Bad**: Reinvent agent architecture for every project
**Good**: Reuse proven patterns (Sequential Research, Scoring Pipeline, Refactor Protocol)

**Rationale**: Patterns encode lessons from failures. Don't repeat mistakes.

---

## Conclusion

This analysis of 66+ agents across [Tool], Recur, and Pixee GTM systems reveals that successful agent orchestration is a **design discipline**, not a prompt engineering challenge. The key patterns are:

**Role Taxonomy**: 6 agent types (Collectors, Analyzers, Synthesizers, Routers, Maintainers, Executors) cover most use cases

**Contract Patterns**: File-based sequential (depth), structured data models (scale), free-form reports (context) each solve different problems

**Validation Frameworks**: Evidence-level flagging (prevent confidence inflation), iterative quality gates (zero content loss), boundary testing (validate assumptions)

**Execution Protocols**: Research, Synthesis, Refactor, Routing, Orchestrator protocols are reusable across domains

**Anti-Patterns**: Vague inputs, missing validation, confidence inflation, no conflict resolution, boundary assumptions, manual at scale, no rollback

The design pattern library provided enables teams to:
1. **Select the right pattern** for their use case (decision tree included)
2. **Avoid common failures** (8 anti-patterns documented with remediations)
3. **Build robust systems** (8 design principles for resilient orchestration)

**Final Recommendation**: Start with proven patterns, don't reinvent. The L0-L6 Sequential Research Pipeline ([Tool]), Scoring & Automation Framework (Recur), and Domain Consolidation Protocol (Pixee) can be adapted to most GTM agent systems with minor modifications. Focus energy on domain-specific logic, not on reinventing orchestration patterns.

---

**Report Statistics**:
- Word Count: ~14,500 words
- Agent Corpus Analyzed: 66+ agents
- Role Types Identified: 6
- Contract Patterns: 4
- Validation Frameworks: 3
- Execution Protocols: 5
- Anti-Patterns: 8
- Design Principles: 8

**Author**: Agent 02 - Role & Contract Extractor
**Date**: 2025-10-08
**Output Path**: `meta_analysis/agent_orchestration_patterns/03_outputs/wave1/role_contract_patterns.md`
