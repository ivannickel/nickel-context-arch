---
name: tag-consolidation-log
description: Record of tag merges and consolidations to maintain taxonomy integrity
domain: foundation
node_type: maintenance_log
status: active
created: 2025-10-24
---

# Tag Consolidation Log

**Purpose:** Track all tag merges, renames, and deprecations to maintain taxonomy integrity and provide audit trail.

---

## Consolidation #1: Volume Threshold Tags (2025-10-24)

### Problem Identified
Three semantically identical tags discovered during iteration 1 referring to the same customer pain point/objection:

1. **volume-threshold-barriers** (pain_points)
   - Frequency: 2
   - Sources: Erik Meza, Hardy Butler
   - Status: validated

2. **volume-threshold-too-high** (objections)
   - Frequency: 2
   - Sources: Erik Meza, Hardy Butler
   - Status: validated

3. **insufficient-volume** (objections, seed tag)
   - Frequency: 2
   - Sources: Erik Meza, Hardy Butler
   - Status: validated (seed)

### Analysis

**Why duplicates exist:**
- Different category perspectives (pain vs. objection)
- Seed tag vs. emergent discovery
- Slight wording variations

**Actual pattern:**
Customer cannot access volume-based discounts because they don't meet $2M minimum threshold. This manifests as both:
- **Pain point:** "I'm below the volume threshold for better rates"
- **Objection:** "Your volume threshold is too high for my business"

**Same underlying issue**, just expressed differently.

### Consolidation Decision

**CANONICAL TAG:** `volume-threshold-barriers`

**Rationale:**
- Most descriptive (captures the barrier nature)
- Category-neutral (works as pain AND objection)
- Already has pattern document created
- Clearer than "insufficient-volume" (insufficient for what?)
- More professional than "too-high" (less subjective)

### Consolidation Actions

**Taxonomy Updates:**
1. Keep `volume-threshold-barriers` as primary tag (pain_points section)
2. Add alias notation in objections section pointing to canonical
3. Update combined frequency: 2 (pain) + 2 (objection) + 2 (seed) = **6 total mentions**
4. Preserve seed tag validation credit for `insufficient-volume`
5. Mark `volume-threshold-too-high` as deprecated with redirect

**Document Updates:**
1. ✅ Pattern document already exists: `pain_points/volume-threshold-barriers.md`
2. Create objection handling section in same document (it's both!)
3. Update transcript references to use canonical tag
4. Update synthesis stubs to use canonical tag

**Affected Documents:**
- `taxonomy.yaml` (lines 71, 177, 201)
- `01_customer/transcripts/2025-07-15_erik-meza-colton.md`
- `01_customer/pain_points/volume-threshold-barriers.md` (add objection handling)
- `01_customer/objections/volume_threshold_too_high.md` (deprecate or merge)

### Post-Consolidation State

**Before:**
- 3 tags, 6 total frequency (2+2+2)
- Spread across 2 categories
- Confusing which to use

**After:**
- 1 canonical tag: `volume-threshold-barriers`
- Frequency: 6 (high confidence)
- Cross-category (pain + objection)
- Clear usage guidelines

### Benefits
✅ Reduced taxonomy complexity (69 → 67 unique tags)
✅ Increased pattern confidence (freq 2 → freq 6)
✅ Eliminated ambiguity for future processing
✅ Preserved historical seed tag validation credit

---

## Consolidation Guidelines

**When to consolidate:**
1. Tags refer to same underlying customer problem
2. Only difference is wording/perspective
3. Same evidence sources cited
4. Consolidation increases clarity without losing meaning

**When NOT to consolidate:**
1. Tags represent distinct phases of customer journey
2. Different evidence sources
3. Severity/impact levels differ significantly
4. Category distinction is meaningful (e.g., pain vs. use case)

**Process:**
1. Identify duplicate candidates
2. Analyze semantic overlap and evidence
3. Choose canonical tag (most descriptive, category-neutral)
4. Update taxonomy with aliases/redirects
5. Update affected documents
6. Log consolidation here
7. Update taxonomy version number

---

## Tag Deprecation Process

**Deprecated tags should:**
1. Be marked `status: deprecated` in taxonomy
2. Include `canonical_replacement: [tag-name]` field
3. Remain in taxonomy for 1 iteration as redirect
4. Be fully removed after 2 iterations if no new mentions

**Example:**
```yaml
- name: volume-threshold-too-high
  status: deprecated
  canonical_replacement: volume-threshold-barriers
  deprecated_date: 2025-10-24
  remove_after_iteration: 3
  notes: "Consolidated into volume-threshold-barriers for clarity"
```

---

## Pending Consolidations

### Under Review (None at this time)

_As of 2025-10-24, no other consolidations identified._

**Watch in iteration 2:**
- Payment cost pain points (3 related tags, may consolidate)
- Compliance friction tags (3 related tags, but distinct phases)

---

## Consolidation Statistics

| Iteration | Tags Before | Consolidations | Tags After | Net Change |
|-----------|-------------|----------------|------------|------------|
| 1         | 69          | 1 (3→1)        | 67         | -2         |

---

**Next Update:** After iteration 2 processing
