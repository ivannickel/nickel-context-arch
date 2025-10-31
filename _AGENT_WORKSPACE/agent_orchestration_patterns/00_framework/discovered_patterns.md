# Discovered Agent Orchestration Patterns

**Three First-Principle Orchestration Patterns from Case Study Analysis**

---

## Pattern 1: Sequential Cascade

**Observed In**: [Tool] (L0-L6), Recur (7-agent research pipeline)

### Architecture
```
Agent 1 → Output File → Agent 2 Input → Output File → Agent 3 Input → Final Deliverable
```

### Key Characteristics

**Linear Dependency Chain**:
- Each agent requires predecessor's complete output before starting
- File-based contracts define handoff points
- Explicit validation gates between agents

**Progressive Context Deepening**:
- Early agents establish foundation (L0-L2: Product → Customer → Buying Process)
- Middle agents analyze motion (L3-L4: Acquisition → Bottleneck)
- Final agents synthesize application (L5-L6: Data Need → Proof Concept)

**Contract Validation**:
- Handoff validation prevents cascade failures
- Agents flag gaps explicitly (UNKNOWN, INSUFFICIENT DATA)
- Quality checklists at each stage


```
Agent 1A (Foundation Intelligence)
    ↓ [outputs: L0-L2 foundation report]
Agent 1B (GTM Motion Intelligence)
    ↓ [outputs: L3-L4 GTM report]
Agent 2 (Use Case Synthesis)
    ↓ [outputs: L5-L6 permissionless value concept]
Final Report
```

**Contract Example**:
```yaml
# Agent 1A → Agent 1B Contract
MUST_PROVIDE:
  - Clear customer ICP (L1): Who buys, sizes, industries
  - Buying process (L2): Stakeholders, cycle length, criteria

VALIDATION:
  - If Agent 1A provides vague customer description → Agent 1B cannot infer GTM motion
  - Success: "Customers are dev teams at product companies, 50-500 eng" → enables motion inference
```

### When to Use

**Optimal For**:
- Research pipelines with clear information hierarchy
- Contexts where each layer builds on the previous
- Need for intermediate validation and gap identification
- Human-in-the-loop checkpoints desired

**Avoid When**:
- Agents can run independently (use parallel execution instead)
- Real-time processing required (latency = sum of all agents)
- Dynamic/branching logic needed (fixed pipeline doesn't support routing)

### Design Principles

1. **Clear Layer Boundaries**: Each agent should address ONE conceptual layer
2. **Explicit Contracts**: Document required inputs, expected outputs, validation rules
3. **Gap Flagging**: Agents must flag insufficient data, not fabricate
4. **Evidence Levels**: Tag claims (VERIFIED/INFERRED/UNKNOWN)
5. **Quality Gates**: Validation checklists before next agent consumes output

### Anti-Patterns

❌ **Mega-Agent**: Single agent doing all L0-L6 research (loses modularity, debugging difficulty)
❌ **Micro-Agents**: One agent per layer (L0, L1, L2 separate) → contract overhead, coupling issues
❌ **Silent Failures**: Agent proceeds with bad data without flagging gaps
❌ **Assumption Fabrication**: Agent fills gaps with assumptions vs flagging UNKNOWN

---

## Pattern 2: Domain Graph Navigation

**Observed In**: Pixee AI (00_foundation → 06_apps with _system meta-agents)

### Architecture
```
Domain Structure:
00_foundation/    → Strategic context
01_customer/      → Intelligence
02_content/       → Product launches
02_synthesis/     → Frameworks
03_execute/       → Agent library
_system/          → Meta-agents

Navigation:
- Wikilinks enable cross-domain traversal
- Front matter for routing/metadata
- Specialized agents maintain graph health
```

### Key Characteristics

**Graph-Based Context Traversal**:
- Knowledge organized in domain directories, not linear pipeline
- Wikilinks create explicit relationships between documents
- Front matter provides metadata for agent routing

**Domain Separation**:
- Foundation (strategic, rarely changes)
- Discovery (research, frequently updated)
- Synthesis (frameworks, periodic consolidation)
- Implementation (execution, high churn)
- Archive (historical, disposal candidates)

**Meta-Agents for Graph Maintenance**:
- Context Refactor Agents (5 domain consolidators)
- Legacy Audit Agents (identify decay)
- Linking QA Agents (validate graph integrity)

### Example: Pixee Context Refactor System

```
Foundation Agent → Consolidates 00_foundation/ (9 files → 3 files)
    ↓ [provides: company/strategic context]
Discovery Agent → Consolidates 01_customer/, research/ (12 files → 4 files)
    ↓ [provides: research insights]
Synthesis Agent → Consolidates 02_synthesis/ (10 files → 5 files)
    ↓ [provides: frameworks]
Implementation Agent → Consolidates 03_execute/ (32 files → 15 files)
    ↓ [provides: execution results]
Archive Agent → Prunes 04_archive/ (40+ files → minimal retention)
```

**Goal**: 150+ files → ~60 files (60% reduction) while preserving 100% insights

### When to Use

**Optimal For**:
- Long-lived context architectures (ongoing client work, multi-month projects)
- Cross-domain knowledge integration (sales + product + customer intelligence)
- Evolving knowledge bases requiring periodic compression
- Multiple agents need access to overlapping context

**Avoid When**:
- Short-lived analysis (one-off research project)
- Strictly linear dependencies (Sequential Cascade better)
- Minimal cross-referencing needed
- Context size manageable without compression

### Design Principles

1. **Domain Boundaries**: Organize by information domain, not chronology
2. **Wikilink Discipline**: Explicit links over implicit references
3. **Front Matter Standards**: Consistent metadata schemas
4. **Compression Agents**: Regular graph optimization to prevent decay
5. **Disposal Lineage**: Track what was removed and why (rollback capability)

### Anti-Patterns

❌ **Graph Sprawl**: No compression strategy → 200+ files, impossible to navigate
❌ **Broken Links**: Wikilinks not validated → dead references
❌ **Domain Bleed**: Mixed concerns (strategic + execution in same file)
❌ **No Disposal**: Everything archived forever → signal-to-noise ratio degrades

---

## Pattern 3: Research → Code Translation

**Observed In**: Recur/Statii (7 research agents → Python ETL pipeline)

### Architecture
```
Research Layer (Markdown Agents):
Agent 01: Foundation → ICP specification
Agent 02: Customer Patterns → Scoring criteria
Agent 03: Market Boundaries → Segmentation schema
Agent 04: Data Discovery → Source methodology
Agent 05: Data Fusion → Field definitions (143 account fields, 64 contact fields)
Agent 06: Messaging → Routing logic
Agent 07: Execution → Automation workflows

    ↓ [Agent outputs become implementation specs]

Code Layer (Python ETL):
companies_house_client.py → Implements Agent 04 data discovery
feature_engineer.py → Implements Agent 05 field definitions
website_classifier.py → Implements Agent 02 scoring criteria
etl_pipeline.py → Orchestrates Agent 07 workflows
```

### Key Characteristics

**Two-Layer Architecture**:
- **Research Layer**: Agents define WHAT to build (specifications, logic, schemas)
- **Code Layer**: Python implements HOW to build (execution, automation, scale)

**Agent Outputs as Specs**:
- Agent 05 defines 143-field data model → `models.py` implements Pydantic schemas
- Agent 02 defines 100-point scoring system → `feature_engineer.py` calculates scores
- Agent 07 defines monthly refresh workflow → `etl_pipeline.py` orchestrates automation

**Traceability**:
- Code comments reference originating agent/section
- Data models map to research specifications
- Validation logic enforces agent-defined rules

### Example: Scoring System Translation

**Agent 03 Research Specification**:
```markdown
## 100-Point Scoring System

### Firmographic Fit (55 points)
- SIC Code Match (30 pts): 25990/25730 = 30, 22290 = 25, 25620 = 20
- Company Size (20 pts): 10-30 employees = 20, 31-50 = 15, 50-100 = 10
- Geography (15 pts): Midlands/Yorkshire = 15, Other England = 10

### Behavioral Signals (45 points)
- ISO Certification (10 pts): ISO 9001 = 10
- Growth Signals (10 pts): Hiring in last 6mo = 10
...
```

**Python Implementation** (`feature_engineer.py`):
```python
def calculate_score(company: Company) -> int:
    """Calculate 100-point score per Agent 03 specification"""
    score = 0

    # Firmographic fit (55 pts) - Agent 03 Section 3.2
    score += calculate_sic_score(company.sic_code)  # 0-30 pts
    score += calculate_size_score(company.employees)  # 0-20 pts
    score += calculate_geo_score(company.postcode)  # 0-15 pts

    # Behavioral signals (45 pts) - Agent 03 Section 3.3
    score += calculate_iso_score(company.certifications)  # 0-10 pts
    score += calculate_growth_score(company.hiring_signals)  # 0-10 pts

    return min(score, 100)
```

### When to Use

**Optimal For**:
- Systematic data processing pipelines (ETL, enrichment, scoring)
- Complex business logic requiring specification before coding
- Need for non-technical stakeholders to review logic (markdown > code)
- Iterative refinement (change spec → regenerate code)

**Avoid When**:
- Simple one-off scripts (overhead not justified)
- Exploratory data analysis (code-first faster)
- Logic too dynamic for pre-specification
- Real-time/low-latency systems (interpretation overhead)

### Design Principles

1. **Spec Completeness**: Research agents must define ALL logic, not just concepts
2. **Traceability**: Code references originating agent/section
3. **Validation Alignment**: Code validation enforces agent-defined rules
4. **Iterative Translation**: Spec changes → code regeneration workflow
5. **Human-Readable Specs**: Non-technical stakeholders can review agent outputs

### Anti-Patterns

❌ **Vague Specs**: Agent says "score by company fit" without defining calculation
❌ **Spec-Code Drift**: Code evolves independently, no longer matches research
❌ **No Traceability**: Can't map code back to originating agent decision
❌ **Over-Specification**: Agent writes pseudo-code (defeats human-readability purpose)

---

## Pattern Comparison Matrix

| Dimension | Sequential Cascade | Domain Graph | Research→Code |
|-----------|-------------------|--------------|---------------|
| **Structure** | Linear pipeline | Graph/network | Two-layer (spec + impl) |
| **Dependencies** | Sequential | Graph traversal | Research → Code |
| **Durability** | One-time execution | Long-lived architecture | Iterative refinement |
| **Modularity** | Agent-level | Domain-level | Layer-level |
| **Primary Use** | Research/analysis | Knowledge management | Data processing |
| **Failure Mode** | Cascade failure | Graph sprawl | Spec-code drift |
| **Maintenance** | Minimal (one-off) | Compression agents | Sync on spec changes |

---

## Composite Patterns (Observed)

### Composite 1: Cascade + Graph (Pixee)
- **GTM agents** (7) operate as Sequential Cascade
- **Outputs populate** Domain Graph (00_foundation/, 01_customer/, etc.)
- **Context refactor agents** maintain graph health

### Composite 2: Cascade + Code Translation (Recur)
- **Research agents** (7) operate as Sequential Cascade
- **Final agent outputs** become code specifications
- **Python pipeline** implements research layer

### Composite 3: All Three (Hypothetical - Blueprint?)
- **Research cascade** generates specifications
- **Specs populate** long-lived domain graph
- **Code layer** implements executable portions
- **Meta-agents** maintain graph + sync spec-code

---

## Pattern Selection Decision Tree

```
START: What are you building?

├─ One-time analysis/research?
│  └─→ Sequential Cascade ([Tool] L0-L6)
│
├─ Long-lived knowledge base?
│  └─→ Domain Graph (Pixee)
│
├─ Data processing pipeline?
│  └─→ Research→Code Translation (Recur)
│
└─ All of the above?
   └─→ Composite Pattern (see 04_novel_patterns/)
```

---

## Next: Novel Patterns from First Principles

**Question**: What orchestration patterns SHOULD exist but aren't yet documented?

See: `04_novel_patterns/undiscovered_orchestration_patterns.md`
