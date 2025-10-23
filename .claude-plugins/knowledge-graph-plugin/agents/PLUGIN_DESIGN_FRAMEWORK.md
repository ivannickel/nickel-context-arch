# Plugin Design Framework
## Engineering Excellence Meets Product Value

**Version:** 1.0.0
**Last Updated:** 2025-10-11
**Purpose:** Comprehensive framework for designing high-value, elegant, and powerful Claude Code plugins

---

## Philosophy: Two Mental Models

### Engineering Excellence: Jeff Dean's Principles

**Core Tenets:**
1. **Simplicity Over Cleverness** - The best systems are immediately understandable
2. **Composability** - Small, well-defined pieces that combine powerfully
3. **Measurable Impact** - Optimize for what actually matters (latency, throughput, user value)
4. **Abstractions That Scale** - Work equally well for 10 users and 10 million users
5. **Failure Mode Design** - Systems should degrade gracefully and communicate clearly

**Why Dean?**
- Built systems that scaled to billions of users (MapReduce, BigTable, Spanner)
- Focused on fundamentals: performance, reliability, maintainability
- Believed in measuring everything and optimizing based on data
- Championed simplicity in architecture over architectural astronautics

### Product Excellence: John Carmack's Principles

**Core Tenets:**
1. **Developer Tools Mastery** - Engines that empower entire industries (id Tech, Doom engine)
2. **Abstraction Design** - APIs that are both simple AND powerful
3. **First Principles Thinking** - Strip away convention to find core truth
4. **Pragmatic Perfectionism** - Ship working systems, iterate ruthlessly based on real usage
5. **Developer Empathy** - Understand the "pit of success" - make the right thing the easy thing

**Why Carmack?**
- Built tools that empowered millions of developers and modders
- Mastered the balance between power and accessibility
- Understood that developer experience IS the product
- Shipped revolutionary tools while maintaining backward compatibility
- Code readability and architecture elegance were core values

---

## The Four-Phase Framework

### **Phase 1: Problem Clarity (Carmack's "What are we actually solving?")**

**Objective:** Achieve crystal-clear understanding of the problem before writing a single line of code.

#### Critical Questions (Must Answer All):

**1. What manual process are we eliminating?**
```
❌ Bad: "Help developers work better"
✅ Good: "Eliminate 15-minute manual frontmatter validation process that happens 20x/day"

Measurement: Time saved per invocation × frequency = ROI
```

**2. What's the 80% use case?**
```
❌ Bad: "Support all possible YAML validation scenarios"
✅ Good: "Validate 6 required fields + domain tag presence in markdown files"

Design Rule: Build for 80%, provide escape hatch for 20%
```

**3. What's the success metric?**
```
❌ Bad: "Users are happier"
✅ Good: "Reduce frontmatter errors from 45% to <5% in 30 days"

If you can't measure it, you can't optimize it.
Metrics should be:
- Quantifiable (numbers, not feelings)
- Time-bounded (when will we measure?)
- Attributable (caused by plugin, not other factors)
```

**4. Who is the user?**
```
Solo Developer:
- Tolerate sparse docs
- Expect customization
- High technical bar

Team (5-20):
- Need clear docs
- Require consistency
- Moderate technical bar

Open Source Community:
- Demand comprehensive docs
- Expect examples
- Variable technical bar

Design Implication: User type determines quality bar, documentation depth, error messaging verbosity
```

#### Validation Checklist:

- [ ] Can explain problem in one sentence
- [ ] Can describe user workflow "before plugin" vs "after plugin"
- [ ] Have identified success metric with target number
- [ ] Know user persona and quality bar
- [ ] Can list manual steps being automated

**Output:** Problem Statement Document

```markdown
## Problem Statement

**Current State:** [Describe painful manual process]
**Target State:** [Describe ideal automated workflow]
**Success Metric:** [X% reduction in Y or Z minutes saved per day]
**User Persona:** [Solo dev / Team / Community]
**80% Use Case:** [Core functionality that serves most users]
**20% Edge Cases:** [Advanced scenarios requiring escape hatches]
```

---

### **Phase 2: Architecture Minimalism (Dean's "Simplest thing that could work")**

**Objective:** Find the minimum viable component set that solves the problem elegantly.

#### Architecture Decision Tree:

```
START: "I want to automate X"
│
├─ Q: Is X a one-time task with clear input/output?
│  └─ YES → Consider: COMMAND
│  └─ NO → Continue
│
├─ Q: Does X require domain expertise or multi-step reasoning?
│  └─ YES → Consider: AGENT
│  └─ NO → Continue
│
├─ Q: Should X happen automatically in response to an event?
│  └─ YES → Consider: HOOK
│  └─ NO → Continue
│
├─ Q: Does X need external data/API integration?
│  └─ YES → Consider: MCP SERVER
│  └─ NO → Continue
│
└─ Q: Is X a combination of the above?
   └─ YES → Consider: PLUGIN (bundle of components)
```

#### Component Selection Guide:

**Use a COMMAND when:**
- Task has clear start and end
- Input is simple (string, file path, arguments)
- Output is predictable
- No state needed between invocations

**Example:** `/validate-frontmatter` - Takes current file, outputs validation report

---

**Use an AGENT when:**
- Task requires domain expertise
- Multi-step reasoning needed
- Context awareness important
- Recommendations over deterministic outputs

**Example:** `taxonomy_enforcement_agent` - Understands YAML standards, suggests context-aware fixes

---

**Use a HOOK when:**
- Automation should be invisible
- Event-driven (before/after tool use, session start)
- Enforcement or quality gates
- Should NOT require user invocation

**Example:** `PreToolUse` hook validates frontmatter before allowing file write

---

**Use an MCP SERVER when:**
- Need external API integration (GitHub, Stripe, Supabase)
- Data lives outside codebase
- Reusable across projects
- Requires authentication/state

**Example:** Supabase MCP for metadata storage, Context7 for docs

---

**Use a PLUGIN when:**
- Multiple components work together
- Cohesive domain (e.g., "knowledge graph management")
- Want versioning and distribution
- Team or community will use it

**Example:** Knowledge Graph Plugin = 3 agents + 4 commands + hooks + scripts

#### Complexity Analysis:

**Where should complexity live?**

```
WORST → Plugin Code (hard to update, users must reinstall)
  ↓
BETTER → Configuration Files (users can customize without code changes)
  ↓
BETTER → External Services (separates concerns, updates without plugin changes)
  ↓
BEST → No Complexity (solve problem differently, eliminate need for complexity)
```

**Example:**

```yaml
❌ BAD: Hardcode validation rules in Python script
⚠️  OK: Validation rules in config file users can edit
✅ GOOD: Validation rules in YAML frontmatter (self-documenting)
✨ BEST: Use JSON Schema validation (industry standard, tooling exists)
```

#### Validation Checklist:

- [ ] Chose minimum number of component types
- [ ] Each component has single responsibility
- [ ] Components are loosely coupled (can work independently)
- [ ] Complexity lives in the right place (config > code)
- [ ] Can draw component interaction diagram in 60 seconds

**Output:** Architecture Diagram

```
PLUGIN: knowledge-graph-plugin
│
├─ AGENT: navigation_agent
│  Purpose: Hub-and-spoke navigation intelligence
│  Input: User query ("find CISO pain points")
│  Output: List of relevant documents with context
│
├─ AGENT: taxonomy_enforcement_agent
│  Purpose: YAML frontmatter validation
│  Input: Document path
│  Output: Validation report with specific fixes
│
├─ COMMAND: /validate-frontmatter
│  Purpose: Validate current file's frontmatter
│  Delegates to: taxonomy_enforcement_agent
│
├─ COMMAND: /graph-health
│  Purpose: Scan entire graph for issues
│  Uses: Glob + Grep + validation logic
│
├─ HOOK: PreToolUse[Write]
│  Purpose: Block file creation if missing frontmatter
│  Calls: validate_new_file.py
│
└─ SCRIPTS: Python validation utilities
   Purpose: Reusable validation logic
   Used by: Hooks, Commands, Agents
```

---

### **Phase 3: Interface Design (Carmack's "Developer Experience IS the Product")**

**Objective:** Design interfaces that are self-documenting, intuitive, and make the right thing easy.

#### The "300ms Rule"

**Principle:** A developer should understand your plugin's purpose in 300ms of scanning.

**How to Achieve:**

1. **Clear Naming**
   ```
   ❌ BAD: processor_agent.md
   ⚠️  OK: validation_agent.md
   ✅ GOOD: taxonomy_enforcement_agent.md

   Rule: Name = Role + Domain
   ```

2. **Examples Before Documentation**
   ```yaml
   ---
   name: taxonomy-enforcement
   description: Use when validating YAML frontmatter. Checks required fields, domain tags, linking requirements.

   examples:
     - input: Document missing domain tag
       output: "Add 'foundation' to tags array"

     - input: Document with only 2 related_docs
       output: "Add 1+ more links including a Tier 1 hub"
   ---
   ```

3. **Self-Documenting Structure**
   ```
   ✅ GOOD Structure:

   plugin-name/
   ├── agents/               # "What it knows"
   ├── commands/             # "What it does"
   ├── hooks/                # "When it acts"
   ├── scripts/              # "How it works"
   └── README.md             # "Why it exists"

   Rule: Directory names should telegraph purpose
   ```

#### Frontmatter as Contract

**The Interface:**

```yaml
---
# WHAT (Required)
name: clear-noun-verb                    # Action-oriented
description: |                            # Verb-first, includes trigger and outcome
  Use this [role] when [trigger condition].
  Specializes in [domain expertise].
  Achieves [measurable outcome].

# HOW (Recommended)
tools: Read, Edit, Bash                  # Explicit tool access
color: blue                               # Visual organization

# WHEN (Critical)
examples:                                 # NOT optional - 2-3 realistic scenarios
  - context: "CISO call transcript needs frontmatter"
    user: "Add frontmatter to this file"
    assistant_action: "Uses taxonomy agent to infer domain, personas, topics"
    outcome: "Complete YAML block inserted"

# WHY (Optional but valuable)
success_metrics:                          # How to measure value
  - "Reduce frontmatter errors 45% → 5%"
  - "Save 15 min/day per developer"

error_messages:                           # Document failure modes
  - missing_domain_tag: "Add domain tag to tags array for Foam color-coding"
  - insufficient_links: "Need 3+ related_docs including 1 Tier 1 hub"
---
```

#### Progressive Disclosure

**Principle:** Simple cases should be simple. Complex cases should be possible.

```yaml
# LEVEL 1: Zero Config (Works out of the box)
/validate-frontmatter
# ✅ Validates current file with sensible defaults

# LEVEL 2: Basic Config (1-2 parameters)
/validate-frontmatter --strict
# ✅ Enables stricter validation rules

# LEVEL 3: Advanced Config (Config file)
/validate-frontmatter --config=custom-rules.yml
# ✅ Full customization for power users

Rule: Never force Level 3 complexity on Level 1 users
```

#### The "No Docs" Test

**Challenge:** Can someone use your plugin by reading code structure alone?

**Test:**

1. Clone plugin repo
2. Look at directory structure for 30 seconds
3. Can you guess what each component does?
4. Open one agent file
5. Can you invoke it correctly without reading README?

**Pass Criteria:**

```
✅ Directory structure matches mental model
✅ File names are self-explanatory
✅ Frontmatter examples show usage
✅ Error messages are actionable
✅ README is supplemental, not required
```

#### Validation Checklist:

- [ ] Passed "300ms rule" with 3 test users
- [ ] Every component has YAML frontmatter with examples
- [ ] File/directory names are self-documenting
- [ ] Implements progressive disclosure (simple → advanced)
- [ ] Passed "No Docs" test
- [ ] Error messages include fix suggestions

**Output:** Interface Specification

```markdown
## Interface Specification

### Commands
- `/validate-frontmatter` - Zero config validation
- `/graph-health` - Full graph scan with health score
- `/navigate-to-hub` - Interactive hub navigation menu
- `/add-frontmatter` - Generate frontmatter from content

### Agents
- `navigation_agent` - Invoked: "find [content type]"
- `taxonomy_enforcement_agent` - Invoked: "validate [document]"

### Hooks
- `PreToolUse[Write]` → Blocks if missing frontmatter
- `PostToolUse[Write]` → Updates graph index
- `SessionStart` → Quick health check

### Error Messages (Actionable)
- Missing domain tag → "Add 'customer' to tags array"
- Broken link → "[[missing_doc]] not found. Did you mean [[similar_doc]]?"
```

---

### **Phase 4: Validation & Iteration (Dean's "Measure Everything")**

**Objective:** Instrument plugin for continuous improvement based on real usage data.

#### Usage Telemetry

**What to Measure:**

```yaml
Core Metrics:
  - invocation_count: How often is each command/agent used?
  - error_rate: % of invocations that fail
  - latency_p50/p95/p99: How long do operations take?
  - user_count: How many unique users?

Behavioral Metrics:
  - most_used_commands: Which commands see highest usage?
  - drop_off_points: Where do users get stuck?
  - error_patterns: What errors are most common?
  - time_of_day: When is plugin used most?

Value Metrics:
  - time_saved: Manual process time - automated time
  - error_reduction: Before/after error rates
  - adoption_rate: % of team using plugin
  - nps_score: Would users recommend it?
```

**Implementation Example:**

```python
# scripts/telemetry.py
import json
from datetime import datetime

def log_usage(component, action, duration_ms, success):
    """Log plugin usage for analysis"""
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "component": component,
        "action": action,
        "duration_ms": duration_ms,
        "success": success
    }

    # Append to local log file (privacy-first)
    with open(".claude/plugin_usage.jsonl", "a") as f:
        f.write(json.dumps(event) + "\n")

# Usage in command
from telemetry import log_usage

start = time.time()
try:
    result = validate_frontmatter(file_path)
    log_usage("validate-frontmatter", "validate",
              (time.time() - start) * 1000, True)
except Exception as e:
    log_usage("validate-frontmatter", "validate",
              (time.time() - start) * 1000, False)
```

#### Performance Benchmarks

**Critical Paths to Measure:**

```yaml
Startup Performance (Hooks):
  Target: <50ms for PreToolUse hooks
  Why: Blocks user action, must be near-instant
  Measure: Time from hook trigger to exit

Command Execution (Commands):
  Target: <2s for simple operations, <10s for complex
  Why: User is waiting, perception of "fast" matters
  Measure: Time from invocation to output

Memory Footprint (Agents):
  Target: <100MB for agent instances
  Why: Multiple agents may be active simultaneously
  Measure: Peak memory during agent execution

Graph Operations (Large Scale):
  Target: <30s to scan 1000 documents
  Why: Health checks should be fast enough to run frequently
  Measure: Time to process N documents
```

**Benchmarking Framework:**

```python
# scripts/benchmark.py
import time
import psutil
import statistics

def benchmark_command(command, iterations=10):
    """Benchmark command performance"""
    times = []
    memory_peaks = []

    for _ in range(iterations):
        process = psutil.Process()

        start_time = time.time()
        start_memory = process.memory_info().rss

        # Execute command
        result = execute_command(command)

        end_time = time.time()
        peak_memory = process.memory_info().rss

        times.append((end_time - start_time) * 1000)  # ms
        memory_peaks.append((peak_memory - start_memory) / 1024 / 1024)  # MB

    return {
        "p50_latency_ms": statistics.median(times),
        "p95_latency_ms": statistics.quantiles(times, n=20)[18],
        "p99_latency_ms": statistics.quantiles(times, n=100)[98],
        "avg_memory_mb": statistics.mean(memory_peaks),
        "max_memory_mb": max(memory_peaks)
    }
```

#### Feedback Loops

**Mechanisms for User Feedback:**

1. **Built-in Feedback Command**
   ```bash
   /plugin-feedback "Validation is too strict for my use case"
   # Opens GitHub issue with template
   ```

2. **Version Tracking**
   ```json
   {
     "plugin": "knowledge-graph",
     "version": "1.2.0",
     "breaking_changes": [
       "Changed domain tag requirement from optional to required"
     ],
     "migration_path": "Run /add-domain-tags to backfill existing files"
   }
   ```

3. **Deprecation Warnings**
   ```python
   @deprecated(version="2.0.0", alternative="/validate-frontmatter-v2")
   def validate_frontmatter_old(file_path):
       """Legacy validation (deprecated)"""
       warnings.warn(
           "This command will be removed in v2.0.0. "
           "Use /validate-frontmatter-v2 instead.",
           DeprecationWarning
       )
   ```

#### Iteration Strategy

**How to Use Metrics for Improvement:**

```yaml
Metric → Insight → Action:

High Error Rate (>10%):
  Insight: Users struggling with validation rules
  Action: Add more examples, clearer error messages

High Latency P95 (>5s):
  Insight: Performance bottleneck in graph scan
  Action: Add caching, parallel processing

Low Adoption (<30% of team):
  Insight: Plugin not solving real problem OR discoverability issue
  Action: User interviews to understand barriers

Specific Command Unused:
  Insight: Feature not valuable OR naming/positioning unclear
  Action: A/B test different naming, or deprecate

Common Error Pattern:
  Insight: Missing validation rule or edge case
  Action: Add handling, update tests
```

#### Validation Checklist:

- [ ] Telemetry instrumented (respecting privacy)
- [ ] Performance benchmarks established with targets
- [ ] Feedback mechanism built-in
- [ ] Version tracking and changelog maintained
- [ ] Deprecation path defined for breaking changes
- [ ] Weekly review cadence for metrics

**Output:** Measurement Plan

```markdown
## Measurement Plan

### Success Metrics (30-day targets)
- Reduce frontmatter errors: 45% → <5%
- Time saved per validation: 15min → <30sec
- Adoption rate: 0% → >80% of team

### Performance Targets
- PreToolUse hooks: <50ms
- /validate-frontmatter: <2s
- /graph-health (1000 docs): <30s

### Telemetry (Privacy-first)
- Local logging only (.claude/plugin_usage.jsonl)
- No PII collected
- Opt-out mechanism: PLUGIN_TELEMETRY=off

### Review Cadence
- Daily: Check error logs
- Weekly: Review usage metrics
- Monthly: User interviews (3-5 users)
- Quarterly: Major iteration based on data
```

---

## Applying the Framework

### Example: Knowledge Graph Plugin Analysis

Let's apply this framework to our current plugin to identify strengths and gaps.

#### Phase 1: Problem Clarity ✅

**What We Did Right:**
- ✅ Clear problem: Manual frontmatter validation is error-prone
- ✅ Identified 80% use case: Required field validation
- ✅ User persona: Team of GTM operators using Foam

**What Needs Improvement:**
- ⚠️ Success metric is vague ("improve graph health")
  - **Fix:** "Reduce frontmatter errors from 45% to <5% in 30 days"
- ⚠️ No baseline measurement
  - **Fix:** Run `/graph-health` now to establish baseline

#### Phase 2: Architecture Minimalism ✅

**What We Did Right:**
- ✅ Minimal component set (2 agents, 4 commands, hooks)
- ✅ Clear separation of concerns
- ✅ Loosely coupled components

**What Needs Improvement:**
- ⚠️ Could start simpler (just `/validate-frontmatter`)
  - **Fix:** Phase releases: v0.1 (validation only) → v0.2 (+ navigation) → v1.0 (+ hooks)
- ⚠️ Scripts not yet implemented
  - **Fix:** Phase 2 of development (Python validation utilities)

#### Phase 3: Interface Design ⚠️

**What We Did Right:**
- ✅ Self-documenting directory structure
- ✅ Clear component naming
- ✅ Examples in agent frontmatter

**What Needs Improvement:**
- ❌ Missing success_metrics in frontmatter
  - **Fix:** Add to all agent YAML
- ❌ Error messages not yet defined
  - **Fix:** Document all failure modes with actionable fixes
- ❌ Haven't done "No Docs" test with real user
  - **Fix:** Test with team member unfamiliar with plugin

#### Phase 4: Validation & Iteration ❌

**What We Did Right:**
- Nothing yet (plugin not deployed)

**What Needs Implementation:**
- ❌ No telemetry
  - **Fix:** Add usage logging to commands
- ❌ No performance benchmarks
  - **Fix:** Benchmark validation script before deployment
- ❌ No feedback mechanism
  - **Fix:** Add `/plugin-feedback` command
- ❌ No versioning strategy
  - **Fix:** Establish semver + changelog

---

## Decision Trees

### When to Build a Plugin vs. Single Component

```
START: "I want to automate something"
│
├─ Q: Is this ONE specific task?
│  └─ YES → Build Single Component (Command or Agent)
│  └─ NO → Continue
│
├─ Q: Do multiple components need to work together?
│  └─ YES → Consider Plugin
│  └─ NO → Build Separate Components
│
├─ Q: Will others outside my project use this?
│  └─ YES → Definitely Plugin (for distribution)
│  └─ NO → Maybe Plugin (if >3 components)
│
└─ Q: Does this represent a cohesive domain?
   └─ YES → Plugin (e.g., "knowledge graph management")
   └─ NO → Separate Components (e.g., random utilities)
```

### Component Type Selection

```
Task: "I need to validate YAML frontmatter"
│
├─ Q: Should this happen automatically?
│  ├─ YES → Hook (PreToolUse for validation gate)
│  └─ NO → Continue
│
├─ Q: Is this deterministic (same input = same output)?
│  ├─ YES → Command (/validate-frontmatter)
│  └─ NO → Agent (context-aware validation with suggestions)
│
└─ Q: Do I need both automatic AND manual?
   └─ YES → Hook + Command (hook for enforcement, command for on-demand)
```

---

## Anti-Patterns (What NOT to Do)

### 1. **Feature Creep**
```
❌ BAD:
"Let's add AI-powered content generation to the validation plugin!"

Why Bad: Unrelated concern, increases complexity, unclear user value

✅ GOOD:
"Validation plugin validates. Content generation is separate plugin."
```

### 2. **Premature Optimization**
```
❌ BAD:
"Let's build caching layer before validating single file works"

Why Bad: Complexity before value, solving problems you don't have yet

✅ GOOD:
"Ship basic validation. Add caching if benchmarks show need."
```

### 3. **Configuration Hell**
```
❌ BAD:
50 configuration options, no sensible defaults

Why Bad: Decision paralysis, high barrier to entry

✅ GOOD:
Zero-config works for 80%, 5 options cover remaining 20%
```

### 4. **Implicit Dependencies**
```
❌ BAD:
Plugin breaks if user doesn't have Python 3.11+ but never states this

Why Bad: Mystery errors, wasted debugging time

✅ GOOD:
plugin.json declares dependencies, graceful error if missing
```

### 5. **Magic Behavior**
```
❌ BAD:
Hook silently fixes files without telling user

Why Bad: Unexpected changes, loss of trust, debugging nightmare

✅ GOOD:
Hook validates, reports issues, offers to fix (with explicit consent)
```

### 6. **Documentation as Crutch**
```
❌ BAD:
Complex API that requires 10 pages of docs to understand

Why Bad: Interface is poorly designed, docs are band-aid

✅ GOOD:
Self-documenting interface, docs are supplemental examples
```

---

## Checklist: Is Your Plugin Ready to Ship?

### Phase 1: Problem Clarity
- [ ] Can explain problem in one sentence
- [ ] Have defined success metric with target number
- [ ] Know user persona and quality bar
- [ ] 80% use case is clear and documented

### Phase 2: Architecture
- [ ] Using minimum number of component types
- [ ] Each component has single responsibility
- [ ] Can draw component interaction diagram in 60 seconds
- [ ] Complexity lives in right place (config > code)

### Phase 3: Interface
- [ ] Passed "300ms rule" with 3 test users
- [ ] All components have examples in frontmatter
- [ ] Implements progressive disclosure (simple → advanced)
- [ ] Passed "No Docs" test
- [ ] Error messages are actionable

### Phase 4: Validation
- [ ] Telemetry instrumented (privacy-first)
- [ ] Performance benchmarks meet targets
- [ ] Feedback mechanism exists
- [ ] Version tracking and changelog maintained
- [ ] Have weekly review cadence planned

### Distribution
- [ ] README with clear value proposition
- [ ] Installation instructions (3 methods)
- [ ] Examples showing 80% use case
- [ ] LICENSE file
- [ ] Semantic versioning established

---

## Resources & References

### Engineering Wisdom
- **Jeff Dean on simplicity**: [Google Research Talk on System Design](https://research.google/people/jeff/)
- **Carmack on developer tools**: [.plan files archive](https://github.com/ESWAT/john-carmack-plan-archive)

### Plugin Examples
- **claude-code-templates**: https://github.com/davila7/claude-code-templates
- **Official Claude Code docs**: https://docs.claude.com/en/docs/claude-code/plugins

### Measurement & Iteration
- **DORA Metrics**: https://dora.dev/
- **Developer Experience (DevEx)**: https://queue.acm.org/detail.cfm?id=3595878

---

**This framework is a living document. Update it as you learn from building real plugins.**
