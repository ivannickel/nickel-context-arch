# Context Engineering Operating System
**Meta-Synthesis: Unified Pattern Reference from Wave 1 & Wave 2 Analysis**

**Agent 06: Meta-Synthesis**
**Generated**: 2025-10-08
**Input Sources**: 5 completed reports (Wave 1: Structural, Roles, Attribution | Wave 2: L0-L6, Graph Maintenance)
**Framework Sources**: 3 base patterns + 7 novel patterns
**Mission**: Consolidate 12 patterns into ONE unified reference guide for context engineering

---

## 1. Executive Summary

This operating system synthesizes patterns from 5 completed reports and 10 framework patterns into a unified reference for context engineering. The goal is **pattern reuse** across GTM orchestration projects through systematic pattern selection, integration guidance, and implementation roadmaps.

### What This Document Provides

**12 Unified Patterns** (3 base + 7 novel + 2 integration patterns):
- Quick reference table with selection criteria
- Decision tree for pattern selection
- Pattern compatibility matrix
- Cross-wave integration guidance

**Not Another Report**: This is a **working reference** - use it to select patterns, not to understand their details. For deep dives, reference source reports.

### Key Integration Insights

**Pattern Families Discovered**:
1. **Structural Patterns** (How to organize): Function-Based → Layer-Based → Domain-Based
2. **Orchestration Patterns** (How agents flow): Sequential Cascade → Domain Graph → Parallel Fanout
3. **Attribution Patterns** (How to track): Inline → Front Matter → Disposal Lineage
4. **Execution Patterns** (How to run): Research Protocol → Synthesis Protocol → Refactor Protocol

**Critical Success Factors**:
- Match structure to timeline (Function <3mo, Domain 6mo+)
- Use evidence flagging to prevent confidence inflation
- Implement graph health monitoring for long-lived systems
- Plan disposal from day one

**Non-Obvious Discovery**: The most sophisticated systems (Pixee) evolved **retrospectively** under production pressure, not from initial design. Advanced patterns solve problems that only appear at scale.

---

## 2. Unified Pattern Library

### 2.1 Pattern Quick Reference

| # | Pattern Name | Category | When to Use | Source |
|---|--------------|----------|-------------|--------|
| **BASE PATTERNS** |
| 1 | Function-Based Structure | Structural | <3 month projects, 1-3 people | Wave 1 Structural |
| 2 | Layer-Based Structure | Structural | 3-6 months, mixed teams (strategy+eng) | Wave 1 Structural |
| 3 | Domain-Based Structure | Structural | 6+ months, 3-10 people, knowledge base | Wave 1 Structural |
| **ORCHESTRATION PATTERNS** |
| 4 | Sequential Cascade (L0-L6) | Orchestration | Deep layered intelligence, each layer builds on previous | Framework + Wave 2 L0-L6 |
| 5 | Domain Graph Navigation | Orchestration | Long-lived architecture, cross-domain integration | Framework + Wave 2 Graph |
| 6 | Research→Code Translation | Orchestration | Data pipelines, spec before implementation | Framework |
| **NOVEL PATTERNS** |
| 7 | Parallel Fanout-Fanin | Orchestration | Multi-dimensional analysis, time-sensitive | Novel Pattern 4 |
| 8 | Iterative Refinement Loop | Orchestration | Quality-gated iteration, self-improvement | Novel Pattern 5 |
| 9 | Probabilistic Router | Orchestration | Variable input quality, graceful degradation | Novel Pattern 6 |
| 10 | Hierarchical Decomposition | Orchestration | Complex multi-faceted tasks, dynamic scaling | Novel Pattern 7 |
| **INTEGRATION PATTERNS** |
| 11 | Attribution System (3-level) | Cross-cutting | Evidence tracking (VERIFIED/INFERRED/UNKNOWN) | Wave 1 Attribution |
| 12 | Graph Maintenance System | Cross-cutting | Context compression, disposal lineage | Wave 2 Graph Maintenance |

### 2.2 Pattern Descriptions

#### STRUCTURAL PATTERNS (Choose ONE as project foundation)

**Pattern 1: Function-Based Structure**
- **Structure**: Flat 4-level hierarchy, role specialization (agents/, research/, routing/)
- **Metrics**: 4.4 files/directory, 4 levels deep, NO wikilinks, NO front matter
- **Trade-off**: Low maintenance, minimal scalability

**Pattern 2: Layer-Based Structure**
- **Structure**: Research (docs/) + Execution (apps/) separation with data staging pipeline
- **Use**: Mixed strategy-engineering teams, data-driven campaigns (Recur: 6-week campaign)
- **Metrics**: 0.09 files/directory, 4-5 levels, data staging (raw→normalized→enriched)
- **Trade-off**: Moderate complexity, code integration

**Pattern 3: Domain-Based Structure**
- **Structure**: Numbered domains (00-06) + _system meta-layer for governance
- **Use**: Long-lived knowledge bases, ongoing client work (Pixee: multi-year engagement)
- **Metrics**: 0.78 files/directory, 5-6 levels, 1,229 wikilinks, comprehensive YAML
- **Trade-off**: High maintenance, maximum scalability and reusability

#### ORCHESTRATION PATTERNS (Choose based on agent flow needs)

**Pattern 4: Sequential Cascade (L0-L6)**
- **Flow**: Agent 1A (L0-L2) → Agent 1B (L3-L4) → Agent 2 (L5-L6)
- **Key Feature**: Evidence-level flagging prevents cascade failures
- **Time**: 90-135 min per account for complete L0-L6 analysis

**Pattern 5: Domain Graph Navigation**
- **Flow**: Graph-based traversal via wikilinks, front matter routing
- **Use**: Cross-domain knowledge integration with maintenance agents
- **Key Feature**: 60% file reduction (150+→60) with 0% insight loss through systematic consolidation
- **Time**: 5-week refactor cycle (Foundation → Discovery → Synthesis → Implementation → Archive)

**Pattern 6: Research→Code Translation**
- **Flow**: Research agents define specs → Python implements specs
- **Use**: Data processing pipelines, systematic ETL (Recur: 100-point scoring model)
- **Key Feature**: Traceability from code back to originating research agent
- **Time**: 7-agent cascade defining 143-field data model

**Pattern 7: Parallel Fanout-Fanin**
- **Flow**: Input → Multiple parallel agents → Synthesis agent aggregates
- **Use**: Multi-dimensional analysis of same input (Wave 1: structural, roles, attribution)
- **Key Feature**: Reduces latency by N (number of parallel agents)
- **Time**: 1/N of sequential processing time

**Pattern 8: Iterative Refinement Loop**
- **Flow**: Agent executes → Quality gate → If <threshold, refine & re-run → Output
- **Use**: Quality-critical tasks where iteration improves outcome
- **Key Feature**: Self-improving agents with gap identification
- **Time**: 3-5 iterations typical, each addressing previous gaps

**Pattern 9: Probabilistic Router**
- **Flow**: Classification → Route by confidence (High→Specialist, Low→Human)
- **Use**: Variable input quality requiring graceful degradation
- **Key Feature**: Adaptive thresholds based on historical accuracy
- **Time**: Real-time routing decisions

**Pattern 10: Hierarchical Decomposition**
- **Flow**: Master decomposes task → Sub-agents (recursive) → Reassemble
- **Use**: Complex tasks with dynamic complexity (simple=1 level, complex=3+)
- **Key Feature**: Adapts depth to task complexity
- **Time**: Scales with decomposition depth

#### CROSS-CUTTING PATTERNS (Apply across all patterns)

**Pattern 11: Attribution System (3-level)**
- **Mechanism**: VERIFIED (public confirmation) | INFERRED (logical deduction with reasoning) | UNKNOWN (gap flagged)
- **Use**: Prevent confidence inflation, enable staleness detection
- **Integration**: Apply to all research outputs regardless of orchestration pattern

**Pattern 12: Graph Maintenance System**
- **Mechanism**: 5-phase consolidation (Audit → Consolidate → Validate → Archive)
- **Use**: Long-lived systems with content sprawl (>50 files)
- **Integration**: Add to Domain-Based structure, apply Iterative Refinement to compression
- **Metrics**: Coupling, Coherence, Redundancy, Orphans, Freshness (composite health score)

---

## 3. Pattern Selection Framework

### 3.1 Decision Tree (Text-Based)

```
START: What are you building?

PROJECT TIMELINE?
├─ <3 months
│  ├─ Single deliverable? → Function-Based Structure (Pattern 1)
│  └─ Code pipeline? → Layer-Based Structure (Pattern 2)
│
├─ 3-6 months
│  ├─ Strategy + Engineering? → Layer-Based (Pattern 2)
│  └─ Pure strategy/content? → Function-Based extended (Pattern 1)
│
└─ 6+ months
   ├─ Knowledge base required?
   │  ├─ Yes + AI orchestration → Domain-Based (Pattern 3)
   │  └─ Yes, no AI → Layer-Based extended (Pattern 2)
   └─ Client handoff? → Domain-Based (Pattern 3)

AGENT ORCHESTRATION NEEDS?
├─ Layered intelligence (each builds on previous)
│  └→ Sequential Cascade (Pattern 4)
│
├─ Long-lived knowledge with cross-domain
│  └→ Domain Graph Navigation (Pattern 5)
│
├─ Data processing pipeline
│  └→ Research→Code Translation (Pattern 6)
│
├─ Multi-dimensional analysis (time-sensitive)
│  └→ Parallel Fanout-Fanin (Pattern 7)
│
├─ Quality iteration required
│  └→ Iterative Refinement (Pattern 8)
│
├─ Variable input quality
│  └→ Probabilistic Router (Pattern 9)
│
└─ Complex task decomposition
   └→ Hierarchical Decomposition (Pattern 10)

CROSS-CUTTING NEEDS? (Apply to any pattern above)
├─ Evidence tracking → Attribution System (Pattern 11)
└─ Content sprawl >50 files → Graph Maintenance (Pattern 12)
```

### 3.2 Pattern Compatibility Matrix

| Pattern | Compatible With | Incompatible With | Integration Notes |
|---------|----------------|-------------------|-------------------|
| **Function-Based** | Sequential Cascade, Parallel Fanout, Attribution | Domain Graph (overkill) | Best for short-term, minimal structure |
| **Layer-Based** | Research→Code, Sequential Cascade, Attribution | Graph Maintenance (insufficient structure) | Bridge between simple and sophisticated |
| **Domain-Based** | Domain Graph, Graph Maintenance, Attribution | Function-Based (too simple) | Required for long-lived systems |
| **Sequential Cascade** | Function/Layer/Domain structures, Attribution | Parallel Fanout (sequential only) | Core orchestration for research |
| **Domain Graph** | Domain-Based structure, Graph Maintenance | Function-Based (needs wikilinks) | Requires metadata infrastructure |
| **Research→Code** | Layer-Based, Attribution | Domain Graph (different paradigms) | Systematic spec→implementation |
| **Parallel Fanout** | Function/Layer structures, Attribution | Sequential Cascade (by definition) | Time-sensitive analysis |
| **Iterative Refinement** | Any orchestration pattern, Graph Maintenance | Real-time systems (latency) | Quality-critical tasks |
| **Probabilistic Router** | Any structure, Attribution | Deterministic pipelines | Graceful degradation |
| **Hierarchical Decomp** | Domain-Based, Sequential Cascade | Function-Based (too complex) | Very complex tasks only |
| **Attribution System** | ALL patterns | None | Universal cross-cutting |
| **Graph Maintenance** | Domain-Based only | Function/Layer (insufficient metadata) | Long-lived systems only |

### 3.3 Pattern Selection by Project Characteristics

**Small Project (1-3 people, <3 months, $50K-$200K)**
- Structure: Function-Based (Pattern 1)
- Orchestration: Sequential Cascade (Pattern 4) OR Parallel Fanout (Pattern 7)
- Attribution: Minimal (URLs + dates only)
- Maintenance: None (disposable)

**Medium Project (2-5 people, 3-6 months, $200K-$1M)**
- Structure: Layer-Based (Pattern 2)
- Orchestration: Sequential Cascade (Pattern 4) + Research→Code (Pattern 6)
- Attribution: Standard (Evidence levels + methodology docs)
- Maintenance: Git-based version control

**Large Project (3-10+ people, 6+ months, $1M+)**
- Structure: Domain-Based (Pattern 3)
- Orchestration: Domain Graph (Pattern 5) + Iterative Refinement (Pattern 8)
- Attribution: Comprehensive (YAML frontmatter + disposal lineage)
- Maintenance: Graph Maintenance System (Pattern 12)

---

## 4. Cross-Wave Integration

### 4.1 How Structural + Orchestration Patterns Connect

**Integration Logic**: Structure defines WHERE knowledge lives, Orchestration defines HOW agents move through it.

**Function-Based + Sequential Cascade** ([Tool] Model):
- Structure: agents/, research/, routing/ directories
- Orchestration: Agent 1A → Agent 1B → Agent 2 linear flow
- File handoffs: foundation_report_L0-L2.md → gtm_intelligence_report_L3-L4.md
- **Why it works**: Flat structure supports simple linear pipeline

**Domain-Based + Domain Graph** (Pixee Model):
- Structure: 00_foundation/ → 06_apps/ with _system/ meta-layer
- Orchestration: Wikilink navigation, front matter routing
- Maintenance: 5-phase consolidation agents compress graph
- **Why it works**: Rich metadata enables graph-based navigation and systematic maintenance

**Layer-Based + Research→Code** (Recur Model):
- Structure: docs/ (research) + apps/ (code) separation
- Orchestration: 7-agent research cascade → Python implementation
- Traceability: Code comments reference originating agent specs
- **Why it works**: Clean research/execution boundary enables spec-first development

### 4.2 How Attribution + Orchestration Integrate

**Attribution Prevents Cascade Failures**:
- Sequential Cascade: If Agent 1A flags customer ICP as UNKNOWN, Agent 1B cannot claim HIGH confidence on GTM motion
- Propagation rule: Confidence can only decrease across agent chain, never increase

**Evidence Levels by Pattern**:
- Function-Based: Minimal attribution (URLs + dates)
- Layer-Based: Methodology documentation (how data gathered)
- Domain-Based: Full lineage (YAML frontmatter + disposal logs)

### 4.3 How L0-L6 + Graph Maintenance Connect

**L0-L6 Generates Content, Graph Maintenance Compresses**:
- Graph Maintenance consolidates via domain agents (Pixee: 150+ → 60 files)
- **Synergy**: Research creates content, maintenance keeps it navigable

**Compression Principles Applied to L0-L6 Outputs**:
- Consolidate overlapping L0-L2 foundation reports (common product/customer patterns)
- Preserve unique L3-L4 bottleneck insights (company-specific)
- Archive superseded L5-L6 use cases (one-time permissionless value concepts)

### 4.4 How Roles + Contracts + Attribution Form Validation System

**Role Types from Wave 1** map to **Orchestration Patterns**:
- Collectors (25%) → Use Attribution Pattern 11 with VERIFIED/CLAIMED evidence
- Analyzers (30%) → Use Sequential Cascade Pattern 4 with INFERRED reasoning chains
- Synthesizers (20%) → Use Domain Graph Pattern 5 with consolidation lineage
- Maintainers (10%) → Use Graph Maintenance Pattern 12 exclusively

**Contract Patterns Enforce Attribution**:
- File-Based Handoff: Agent B validates Agent A's evidence levels before proceeding
- Structured Data: Scoring models inherit confidence from pattern analysis
- Free-Form Reports: Frontmatter documents source attribution for all content

### 4.5 The Complete Integration Stack

```
LAYER 1: STRUCTURE (Choose one foundation)
├─ Function-Based (fast, low maintenance)
├─ Layer-Based (mixed team, code integration)
└─ Domain-Based (long-lived, knowledge base)

LAYER 2: ORCHESTRATION (Agent flow)
├─ Sequential Cascade (layered intelligence)
├─ Domain Graph (cross-domain navigation)
├─ Research→Code (spec-driven implementation)
├─ Parallel Fanout (multi-dimensional)
└─ Iterative Refinement (quality-gated)

LAYER 3: ATTRIBUTION (Evidence tracking)
├─ Inline (URLs + dates + evidence levels)
├─ Structured (Methodology docs + tiers)
└─ Comprehensive (YAML + disposal lineage)

LAYER 4: MAINTENANCE (System health)
├─ Git-based (implicit, version control)
└─ Graph Maintenance (explicit, compression agents)

LAYER 5: VALIDATION (Quality gates)
├─ Evidence flagging (VERIFIED/INFERRED/UNKNOWN)
├─ Contract validation (Agent B requires X from Agent A)
└─ Health metrics (Coupling, Coherence, Redundancy, Orphans, Freshness)
```

**Example Full Stack** (Pixee Model):
1. Structure: Domain-Based (Pattern 3)
2. Orchestration: Domain Graph (Pattern 5) + Iterative Refinement (Pattern 8)
3. Attribution: Comprehensive YAML (Pattern 11)
4. Maintenance: Graph Maintenance (Pattern 12)
5. Validation: Health score monitoring + stakeholder validation (>90%)

---

## 5. Anti-Pattern Catalog

### 5.1 Structural Anti-Patterns

**Over-Engineering**
- Symptom: Domain-Based structure for 4-week project
- Impact: Maintenance overhead exceeds project value
- Remediation: Use Function-Based for <3 month projects

**Under-Engineering**
- Symptom: Function-Based for 12-month engagement
- Impact: Content sprawl, navigation chaos, maintenance debt
- Remediation: Migrate to Domain-Based with _system/ meta-layer

**Mixing Without Purpose**
- Symptom: Random numeric prefixes (some dirs numbered, others not)
- Impact: Inconsistent navigation, no clear organizational logic
- Remediation: Define domain taxonomy upfront (00-06 pattern)

**Distributed Archives**
- Symptom: archive/ subdirectories scattered across all domains
- Impact: Future cleanup costs, difficult to assess what's safe to dispose
- Remediation: Centralized archive (04_archive/) with disposal logs

### 5.2 Orchestration Anti-Patterns

**Mega-Agent**
- Symptom: Single agent doing all L0-L6 research
- Impact: Loses modularity, debugging difficulty, can't iterate layers
- Remediation: Decompose into L0-L2 (Agent 1A) + L3-L4 (Agent 1B) + L5-L6 (Agent 2)

**Silent Failures**
- Symptom: Agent proceeds with bad data without flagging gaps
- Impact: Cascade failures, downstream agents produce nonsense
- Remediation: Explicit UNKNOWN flagging, validation gates between agents

**Spec-Code Drift**
- Symptom: Code evolves independently from research specs
- Impact: Can't recreate scoring logic from documentation
- Remediation: Attribution comments in code, automated sync checks

**Graph Sprawl**
- Symptom: No compression strategy → 200+ files, impossible to navigate
- Impact: Stakeholders can't find information, agents overwhelmed by context
- Remediation: Quarterly consolidation agents (Pattern 12)

### 5.3 Attribution Anti-Patterns

**Vague Source Attribution**
- Symptom: "Source: Website" without URL or date
- Impact: Unverifiable claims, staleness undetectable
- Remediation: Enforce citation template (URL + date + location)

**Evidence Level Inflation**
- Symptom: INFERRED claims drift to VERIFIED over time through repetition
- Impact: False confidence, strategy built on assumptions
- Remediation: Quarterly confidence audits, propagate evidence levels across agent chains

**Silent Content Disposal**
- Symptom: Files deleted without documentation, knowledge lost forever
- Impact: Can't restore if disposal was premature, no audit trail
- Remediation: Disposal lineage logs (Pattern 12), backup before removal

**Orphaned Content**
- Symptom: Content with no lineage, can't determine source/purpose
- Impact: Can't validate, update, or dispose safely
- Remediation: Mandatory document headers (author, created, purpose, sources)

### 5.4 Validation Anti-Patterns

**No Quality Gates**
- Symptom: Agent A outputs report → Agent B reads report (no validation)
- Impact: Bad input propagates through entire pipeline
- Remediation: Explicit validation checklists between agents

**Confidence Inflation Across Chain**
- Symptom: Agent A flags INFERRED → Agent B claims VERIFIED
- Impact: Certainty increases without new evidence
- Remediation: Confidence can only decrease, never increase across agents

**No Conflict Resolution**
- Symptom: Foundation positioning ≠ Discovery customer reality (conflict ignored)
- Impact: Contradictory messaging, strategic confusion
- Remediation: Explicit conflict resolution protocol (prioritize customer truth)

### 5.5 Anti-Pattern Summary Table

| Anti-Pattern | Category | Detection Signal | Fix Pattern |
|--------------|----------|-----------------|-------------|
| Over-Engineering | Structural | Domain-Based for <3mo project | Use Function-Based |
| Under-Engineering | Structural | Function-Based for 12mo+ | Migrate to Domain-Based |
| Mega-Agent | Orchestration | Single agent >4 hours | Decompose (Sequential Cascade) |
| Silent Failures | Orchestration | Agent proceeds with gaps | Explicit UNKNOWN flagging |
| Spec-Code Drift | Orchestration | Code ≠ research spec | Attribution comments + sync checks |
| Graph Sprawl | Orchestration | >200 files, navigation pain | Graph Maintenance (Pattern 12) |
| Vague Attribution | Attribution | "Source: Website" | URL + date + location |
| Evidence Inflation | Attribution | INFERRED → VERIFIED drift | Quarterly confidence audits |
| Silent Disposal | Attribution | Files deleted, no log | Disposal lineage documentation |
| No Quality Gates | Validation | Agent chain no validation | Checklist between agents |
| Confidence Inflation | Validation | Certainty increases | Propagate evidence levels |
| No Conflict Resolution | Validation | Contradictions ignored | Explicit resolution protocol |

---

## 6. Implementation Roadmap

### 6.1 Phase 1: Foundation (Week 1-2)

**Objective**: Establish structural foundation and core patterns

**Activities**:
1. **Structure Selection**
   - Assess project timeline, team size, deliverable type
   - Choose Function-Based (1), Layer-Based (2), or Domain-Based (3)
   - Create directory structure per chosen pattern

2. **Attribution System Setup**
   - Define evidence taxonomy (VERIFIED/INFERRED/UNKNOWN)
   - Create citation templates (minimal, standard, or comprehensive)
   - Document quality criteria for each evidence level

3. **Validation Framework**
   - Define quality gates between agents (if multi-agent)
   - Create validation checklists per agent role
   - Establish confidence propagation rules

**Deliverables**:
- Project directory structure
- `ATTRIBUTION_STANDARDS.md` with evidence taxonomy
- `VALIDATION_CHECKLISTS.md` for agent contracts

**Success Criteria**:
- Structure matches project characteristics (timeline, team, deliverable)
- Attribution standards defined before any research begins
- Validation gates documented before agent deployment

### 6.2 Phase 2: Execution (Week 3-8)

**Objective**: Deploy orchestration patterns and execute core work

**Activities**:

**For Research Projects** (Sequential Cascade):
1. Deploy Agent 1A (Foundation Intelligence L0-L2)
2. Validate output against checklist (≥3 verified customers, ≥2 stakeholders)
3. Deploy Agent 1B (GTM Intelligence L3-L4)
4. Cross-validate L3 with L0-L2 (GTM motion matches buying process?)
5. Deploy Agent 2 (Use Case Synthesis L5-L6)
6. Final validation (use case solves L4 bottleneck?)

**For Data Pipelines** (Research→Code):
1. Deploy research agents (define specs: ICP, scoring, workflows)
2. Validate spec completeness (ALL logic defined, not concepts)
3. Implement code layer (Python/etc. per research specs)
4. Add attribution comments (reference originating agent/section)
5. Validate spec-code alignment (automated sync checks)

**For Knowledge Bases** (Domain Graph):
1. Populate foundation domain (company context, strategic frameworks)
2. Add discovery domain (research, competitive/customer intelligence)
3. Add synthesis domain (frameworks, messaging architecture)
4. Add implementation domain (agent prompts, campaign frameworks)
5. Implement wikilinks (cross-domain references)
6. Add YAML frontmatter (metadata for routing)

**Validation Checkpoints**:
- Weekly: Evidence level checks (VERIFIED % tracking)
- Bi-weekly: Agent output validation (contract compliance)
- Monthly: Cross-domain coherence (no contradictions)

**Deliverables**:
- Completed agent outputs (research reports, data models, or knowledge domains)
- Evidence attribution for all claims
- Validation reports documenting quality gate passes

### 6.3 Phase 3: Maintenance (Ongoing)

**Objective**: Sustain system health and prevent degradation

**Maintenance Cadence by Structure**:

**Function-Based** (Minimal Maintenance):
- **Weekly**: None (short-lived project)
- **Monthly**: None
- **Quarterly**: None
- **Annual**: Archive entire project when complete

**Layer-Based** (Moderate Maintenance):
- **Weekly**: Spec-code sync check (if using Research→Code)
- **Monthly**: Review stale content (>30 days in Discovery)
- **Quarterly**: Evidence confidence audit
- **Annual**: Archive obsolete research, preserve current

**Domain-Based** (Systematic Maintenance):
- **Weekly**: Staleness monitoring (Implementation domain >7 days old?)
- **Weekly**: Broken link check (wikilink validator)
- **Monthly**: Discovery domain refresh (competitive intelligence, customer insights)
- **Quarterly**: Full graph health assessment (coupling, coherence, redundancy, orphans, freshness)
- **Quarterly**: Domain consolidation review (any domain >20 new files?)
- **Annual**: Complete context refactor (5-agent consolidation cycle: Foundation → Discovery → Synthesis → Implementation → Archive)

**Graph Health Monitoring** (Pattern 12, Domain-Based only):
```yaml
health_score_calculation:
  coupling: 20% weight (cross-domain links 15-50 per pair)
  coherence: 30% weight (stakeholder navigation >85%)
  redundancy: 25% weight (content overlap <5%)
  orphans: 15% weight (true orphans <5%)
  freshness: 10% weight (stale files <10%)

thresholds:
  excellent: 90-100
  good: 75-89
  fair: 60-74
  poor: <60 (immediate action required)
```

**Disposal Protocol** (When content >6 months old):
1. Pre-disposal audit: Verify 100% content preservation in active domains
2. Lineage mapping: Document source → markdown → consolidation chain
3. Rollback preparation: Create backup, document restoration procedure
4. Compliance check: PII/sensitive data disposal per regulations
5. Stakeholder approval: Leadership validates disposal decisions
6. Execute disposal: Remove with complete audit trail

**Deliverables**:
- Weekly/Monthly: Monitoring reports (staleness, links, evidence levels)
- Quarterly: Graph health dashboard (composite score + action items)
- Annual: Consolidation report (file reduction %, insight preservation %)

### 6.4 Adaptation by Project Size

**Small Projects** (<$200K, <3 months, 1-3 people):
- **Phase 1**: 2-3 days (simple Function-Based structure)
- **Phase 2**: 4-8 weeks (execute core work)
- **Phase 3**: None (disposable, archive when done)
- **Total**: 5-10 weeks

**Medium Projects** ($200K-$1M, 3-6 months, 2-5 people):
- **Phase 1**: 1 week (Layer-Based structure + attribution setup)
- **Phase 2**: 10-20 weeks (research cascade + code implementation)
- **Phase 3**: Monthly reviews, quarterly audits
- **Total**: 12-24 weeks + ongoing maintenance

**Large Projects** ($1M+, 6+ months, 3-10+ people):
- **Phase 1**: 2 weeks (Domain-Based structure + comprehensive attribution + graph setup)
- **Phase 2**: 20-40 weeks (domain population + agent orchestration)
- **Phase 3**: Weekly monitoring, monthly updates, quarterly consolidation, annual refactor
- **Total**: 24-52+ weeks + continuous maintenance

---

## 7. Success Metrics

### 7.1 Structural Metrics

**Function-Based** (Pattern 1):
```yaml
file_organization:
  - max_depth: 4 levels
  - branching_factor: 4-6 files per directory
  - total_files: <100 (if exceeds, consider migration)

navigation_efficiency:
  - time_to_find_info: <30 seconds
  - stakeholder_confusion: <10% report difficulty finding files

maintenance_burden:
  - hours_per_week: <2 hours
  - file_moves: <5 per month (stable structure)
```

**Layer-Based** (Pattern 2):
```yaml
layer_separation:
  - research_docs_purity: >90% (docs/ should be strategic only)
  - code_docs_integration: apps/docs/ exists and maintained
  - spec_code_sync: <5% drift (code matches research specs)

data_pipeline_health:
  - staging_pipeline_clarity: raw → normalized → enriched distinct
  - transformation_traceability: 100% (know where each field comes from)

maintenance_burden:
  - hours_per_week: 3-5 hours
  - spec_updates: Triggered by research changes (not ad-hoc)
```

**Domain-Based** (Pattern 3):
```yaml
domain_cohesion:
  - foundation_stability: <5 updates per month (should be stable)
  - discovery_freshness: <30 days staleness
  - synthesis_coherence: No contradictions across frameworks
  - implementation_churn: <50 file changes per month

graph_health_score:
  - composite: >85 (GOOD) or >90 (EXCELLENT)
  - coupling: 85+ (healthy cross-domain linking)
  - coherence: 90+ (stakeholder navigation success)
  - redundancy: 97+ (minimal content overlap)
  - orphans: 96+ (few true orphans)
  - freshness: 80+ (content currency)

maintenance_burden:
  - hours_per_week: 6-10 hours
  - consolidation_cycle: Quarterly (5-week refactor)
  - disposal_safety: 100% (no unintended content loss)
```

### 7.2 Execution Metrics

**Sequential Cascade** (Pattern 4):
```yaml
pipeline_performance:
  - agent_1a_time: 90-135 min per account
  - agent_1b_time: 90-135 min per account
  - agent_2_time: 30-60 min per account
  - total_time: 210-330 min (3.5-5.5 hours) per account

quality_gates:
  - l0_l2_verified_percentage: >60% claims VERIFIED
  - l3_l4_cross_validation: 100% (GTM motion matches L0-L2)
  - l5_l6_actionability: >90% (rep can execute use case)

cascade_health:
  - gap_flagging_rate: <20% (agents flag UNKNOWN for key fields)
  - confidence_inflation: 0% (INFERRED never becomes VERIFIED without new evidence)
```

**Domain Graph** (Pattern 5):
```yaml
graph_navigation:
  - wikilink_density: 8-10 links per file (core domains)
  - hub_documents: 3-5 per domain (central references)
  - broken_links: 0% (validated weekly)

consolidation_effectiveness:
  - file_reduction: 60% (150+ → ~60 files)
  - insight_preservation: 100% (verified via audits)
  - stakeholder_satisfaction: >90% (validated by user testing)
```

**Research→Code** (Pattern 6):
```yaml
translation_quality:
  - spec_completeness: 100% (all logic defined in research)
  - code_attribution: 100% (every function references originating agent)
  - spec_code_drift: <5% (automated sync checks pass)

traceability:
  - code_to_agent_mapping: 100% (can trace code back to research)
  - validation_alignment: 100% (code enforces agent-defined rules)
```

### 7.3 Attribution Metrics

**Evidence Quality** (Pattern 11):
```yaml
evidence_distribution:
  - verified_claims: >60% (public confirmation)
  - inferred_claims: 30-40% (logical deduction with reasoning)
  - unknown_gaps: <10% (explicitly flagged)

citation_completeness:
  - urls_with_dates: 100% for VERIFIED claims
  - reasoning_chains: 100% for INFERRED claims
  - gap_documentation: 100% for UNKNOWN claims

staleness:
  - foundation_content: <180 days old (acceptable)
  - discovery_content: <30 days old (requires refresh)
  - synthesis_content: <60 days old (frameworks stable)
```

### 7.4 Maintenance Metrics

**Graph Health** (Pattern 12):
```yaml
health_score_tracking:
  - current_score: 87.4/100 (example from Pixee)
  - trend: +15 points over last quarter (improving)
  - action_items: 3 (high=1, medium=1, low=1)

consolidation_results:
  - foundation: 67% reduction (9→3 files, 0% loss)
  - discovery: 67% reduction (12→4 files, 0% loss)
  - synthesis: 50% reduction (10→5 files, 0% loss)
  - implementation: 53% reduction (32→15 files, 0% loss)
  - archive: 90% reduction (40+→minimal, 0% loss)

disposal_safety:
  - pre_disposal_audits: 100% completion
  - lineage_documentation: 100% (all removed content mapped)
  - rollback_tests: 100% success (quarterly validation)
```

### 7.5 Success Criteria Summary Table

| Metric Category | Small Project | Medium Project | Large Project |
|----------------|---------------|----------------|---------------|
| **Structure** | Files <100, Depth <4 | Layers clear, <5% drift | Domains cohesive, Health >85 |
| **Orchestration** | Time 3-5 hrs/account | Pipeline reliable | Graph navigable <30s |
| **Attribution** | URLs+dates 100% | Evidence levels 100% | YAML+lineage 100% |
| **Quality** | Verified >40% | Verified >50% | Verified >60% |
| **Maintenance** | <2 hrs/week | 3-5 hrs/week | 6-10 hrs/week |
| **Disposal** | Archive on complete | Quarterly review | Systematic lineage |

---

## Appendix A: Pattern Selection Cheat Sheet

### By Timeline
- **<3 months**: Function-Based + Sequential Cascade + Minimal Attribution
- **3-6 months**: Layer-Based + Research→Code + Standard Attribution
- **6+ months**: Domain-Based + Domain Graph + Comprehensive Attribution

### By Team
- **1-3 people**: Function-Based (low coordination)
- **2-5 people**: Layer-Based (mixed disciplines)
- **3-10+ people**: Domain-Based (high coordination needs)

### By Deliverable
- **Report/Analysis**: Function-Based + Sequential Cascade
- **Data Pipeline**: Layer-Based + Research→Code
- **Knowledge Base**: Domain-Based + Domain Graph + Graph Maintenance

### By Agent Needs
- **Linear dependencies**: Sequential Cascade
- **Multi-dimensional**: Parallel Fanout-Fanin
- **Quality iteration**: Iterative Refinement
- **Variable input**: Probabilistic Router
- **Complex tasks**: Hierarchical Decomposition

### By Maintenance Appetite
- **Low (disposable)**: Function-Based, Git-based version control
- **Medium (periodic)**: Layer-Based, Spec-code sync checks
- **High (systematic)**: Domain-Based, Graph Maintenance System

---

## Appendix B: Quick Start Templates

### Function-Based Template
```
project_root/
├── docs/
│   ├── 00_foundation.md
│   ├── 01_execution_plan.md
│   └── 02_deliverables.md
├── agents/
│   ├── research/
│   ├── synthesis/
│   └── execution/
├── outputs/
│   ├── {entity_1}/
│   └── {entity_2}/
├── context/
└── archive/
```

### Layer-Based Template
```
project_root/
├── docs/
│   ├── 01_research/
│   ├── 02_execution/
│   └── 03_validation/
├── apps/
│   ├── src/
│   ├── data/
│   │   ├── raw/
│   │   ├── normalized/
│   │   └── enriched/
│   ├── docs/
│   └── logs/
├── context/
└── scoping/
```

### Domain-Based Template
```
project_root/
├── _system/
│   ├── 00_specialized_agents/
│   ├── 01_foundation_cohesion/
│   └── 02_graph_health/
├── 00_foundation/
├── 01_discovery/
├── 02_synthesis/
├── 03_execute/
├── 04_archive/
└── CLAUDE.md (operational guide)
```

---

## Appendix C: Source Report References

For deep dives, reference these source reports:

**Wave 1**:
- `meta_analysis/agent_orchestration_patterns/03_outputs/wave1/structural_taxonomy_report.md`
- `meta_analysis/agent_orchestration_patterns/03_outputs/wave1/role_contract_patterns.md`
- `meta_analysis/agent_orchestration_patterns/03_outputs/wave1/attribution_framework_comparison.md`

**Wave 2**:
- `meta_analysis/agent_orchestration_patterns/03_outputs/wave2/graph_maintenance_playbook.md`

**Framework**:
- `meta_analysis/agent_orchestration_patterns/00_framework/discovered_patterns.md`
- `meta_analysis/agent_orchestration_patterns/04_novel_patterns/undiscovered_orchestration_patterns.md`

---

**Report Compiled By**: Agent 06 - Meta-Synthesis
**Date**: 2025-10-08
**Word Count**: ~4,800 words
**Synthesis Scope**: 5 Wave reports + 10 framework patterns → 12 unified patterns + integration guidance
