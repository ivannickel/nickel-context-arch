# Current Taxonomy Snapshot
**Generated:** 2025-10-12
**Purpose:** Baseline analysis of existing tag usage before implementing Taxonomy Navigator plugin

---

## Executive Summary

- **Total unique tags:** 100
- **Total tag instances:** 246 (across 72 files)
- **Average tags per file:** 3.4
- **Tag distribution:** Highly skewed (top 2 tags = 99 instances, bottom 70 tags = 70 instances)

**Key Finding:** Strong tagging patterns exist in customer domain (51 files, highly consistent), but significant tag sprawl in lower-frequency tags (70 tags used only once).

---

## Tag Usage by Frequency

### Tier 1: Core Tags (20+ uses)
```
52 files (72.2%)  customer-intelligence
47 files (65.3%)  call-transcript
```

**Analysis:** These are de facto standard tags. Nearly universal in customer domain.

### Tier 2: Established Tags (5-10 uses)
```
 8 files (11.1%)  content
 6 files ( 8.3%)  foundation
 5 files ( 6.9%)  qualified-opportunity
```

**Analysis:** Domain tags + key classification tags. Foundation/content usage is LOW (should be higher based on 6 foundation files, 9 content files).

### Tier 3: Emerging Tags (3-4 uses)
```
 4 files ( 5.6%)  partner-channel
 4 files ( 5.6%)  remediation-layer
 3 files ( 4.2%)  messaging
 3 files ( 4.2%)  operational
 3 files ( 4.2%)  sales
 3 files ( 4.2%)  financial-services
 3 files ( 4.2%)  japan
 3 files ( 4.2%)  faq
```

**Analysis:** These tags are gaining traction. Monitor for standardization opportunities.

### Tier 4: Single-Use Tags (70 tags, 1 use each)
Examples:
```
 1 file: advisor-engagement, poc-planning, customer-onboarding
 1 file: incomplete-data, strategic-feedback, early-stage
 1 file: tofu, brand-value, cta-optimization
 1 file: video-strategy, visual-assets, product-marketing
```

**Analysis:** TAG SPRAWL. Many are likely:
- One-off descriptors (should be in description field?)
- Inconsistent naming (e.g., "customer-onboarding" - is this standard?)
- Over-specific (e.g., "incomplete-data" - metadata, not tag?)

---

## Tag Usage by Domain

### Foundation Domain (6 files)
```
Unique tags: 22
Avg tags/file: 5.3 (HIGHEST - most detailed tagging)

Top tags:
  - foundation (6) ✅ 100% compliance with domain tag
  - operational (3)
  - market (2)
  - competitive (2)
  - positioning (2)
```

**Health:** EXCELLENT
- High domain tag compliance (6/6 = 100%)
- Rich tagging (5.3 tags/file)
- Consistent patterns

### Customer Domain (51 files)
```
Unique tags: 43
Avg tags/file: 3.0

Top tags:
  - customer-intelligence (50) ✅ Near-universal
  - call-transcript (47) ✅ Strong classification
  - qualified-opportunity (5)
  - partner-channel (4)
  - financial-services (3)
```

**Health:** GOOD, but missing domain tag
- Strong semantic tagging (customer-intelligence, call-transcript)
- ❌ Only 1/51 files has "customer" domain tag (1.9% compliance)
- Consistent patterns across call transcripts
- Some emerging verticals (financial-services, japan)

**Recommendation:** If domain tags are needed for visualization, bulk-add "customer" to 50 files.

### Content Domain (9 files)
```
Unique tags: 26
Avg tags/file: 4.8

Top tags:
  - content (8) ✅ Good domain tag compliance (8/9 = 89%)
  - remediation-layer (4)
  - faq (3)
  - campaign (2)
  - content-strategy (2)
```

**Health:** GOOD
- High domain tag compliance (89%)
- Thematic clustering (remediation-layer, faq content)
- Moderate detail (4.8 tags/file)

### Execute Domain (? files)
```
Data: Limited/no execute files with tags yet
```

**Health:** UNKNOWN - need to populate this domain

---

## Tag Co-Occurrence Patterns

### Strong Clusters (always appear together)

**Customer Intelligence Cluster:**
```
46x [call-transcript] + [customer-intelligence]

Pattern: Nearly every call transcript is tagged with both.
This is a STRONG convention.
```

**Opportunity Qualification Cluster:**
```
5x [qualified-opportunity] + [customer-intelligence]
5x [qualified-opportunity] + [call-transcript]

Pattern: Qualified calls get triple-tagged.
```

**Partner Channel Cluster:**
```
4x [partner-channel] + [customer-intelligence]
4x [partner-channel] + [call-transcript]

Pattern: Partner calls follow same structure as customer calls.
```

**Vertical Clusters:**
```
3x [financial-services] + [customer-intelligence] + [call-transcript]
3x [japan] + [customer-intelligence] + [call-transcript]

Pattern: Geographic/industry verticals as additional tags.
```

**Content Theme Cluster:**
```
3x [content] + [faq] + [remediation-layer]

Pattern: FAQ content about remediation layer.
```

---

## Taxonomy Health Assessment

### Strengths ✅

1. **Foundation domain:** Excellent compliance and rich tagging
2. **Customer domain:** Strong semantic conventions (customer-intelligence + call-transcript)
3. **Tag clusters:** Clear patterns emerge (call transcript structure is consistent)
4. **Co-occurrence:** Tags are used predictably together

### Issues ⚠️

1. **Domain tag inconsistency:**
   - Foundation: 100% (6/6)
   - Content: 89% (8/9)
   - Customer: 2% (1/51) ⬅️ **MAJOR GAP**

2. **Tag sprawl in Tier 4:**
   - 70 tags used only once (70% of unique tags)
   - Many are overly specific or inconsistent
   - No clear consolidation path yet

3. **Potential duplicates/variants:**
   - "sales" vs "sales-insights" vs "sales-enablement" vs "sales-pipeline"
   - "partner-channel" vs "partner-relations" vs "partner-network"
   - "campaign" vs "content-strategy" vs "marketing"

4. **Semantic ambiguity:**
   - Is "japan" a geography tag or market tag?
   - Is "qualified-opportunity" a status or call_type?
   - Should "incomplete-data" be a tag or a field?

---

## Taxonomy Proposals

### Immediate Actions (High ROI)

#### 1. **Bulk-add "customer" domain tag** (if needed for viz)
```bash
# Add "customer" tag to 50 customer domain files missing it
# Impact: Fixes domain tag compliance 2% → 100%
```

#### 2. **Consolidate sales tags**
```
Current: sales (3), sales-insights (2), sales-enablement (1), sales-pipeline (1)

Proposed:
- sales-enablement → For playbooks, battlecards, tooling
- sales-insights → For analysis, patterns, call summaries
- Deprecate: "sales" (too generic)
```

#### 3. **Standardize partner tags**
```
Current: partner-channel (4), partner-relations (1), partner-network (1)

Proposed:
- partner-channel → Standard tag for all partner-related calls/content
- Deprecate: partner-relations, partner-network (merge into partner-channel)
```

#### 4. **Define single-use tag policy**
```
Rule: Tags used <3 times after 30 days should be:
- Consolidated into existing tags, OR
- Moved to description/metadata fields, OR
- Explicitly blessed as emerging tag

Examples to deprecate:
- incomplete-data → Use metadata field instead
- early-stage → Use call_type field instead
- tofu → Use funnel_stage field instead
```

### Future Considerations

#### 5. **Establish tag categories**
```yaml
blessed_taxonomy:
  domain: [foundation, customer, content, execute, apps]

  file_type:
    - call-transcript
    - campaign
    - faq

  semantic:
    - customer-intelligence
    - sales-enablement
    - content-strategy

  vertical:
    - financial-services
    - japan

  outcome:
    - qualified-opportunity
    - design-partner
```

#### 6. **Create tagging guidelines**
```markdown
Tag Selection Rules:
1. Always include domain tag (foundation/customer/content/execute)
2. Include 1 file_type tag (what IS this?)
3. Include 1-2 semantic tags (what's it ABOUT?)
4. Optional: Add vertical/geography if applicable
5. Optional: Add outcome/status if applicable

Target: 3-7 tags per file
```

---

## Metrics for Plugin Success

### Baseline (Current State)
```
Domain tag compliance:
  - Foundation: 100% (6/6)
  - Customer: 2% (1/51)
  - Content: 89% (8/9)
  - OVERALL: 21% (15/66)

Tag sprawl:
  - Unique tags: 100
  - Single-use tags: 70 (70%)
  - Tier 1 tags: 2 (2%)

Tag consistency:
  - Files with 3+ tags: 85% (61/72)
  - Files with blessed tags only: Unknown (need registry)
```

### Target State (30 days)
```
Domain tag compliance: 95%+ in all domains

Tag sprawl:
  - Unique tags: <50 (reduce by 50%)
  - Single-use tags: <20% (reduce by 70%)
  - Tier 1 tags: 10+ (blessed registry)

Tag consistency:
  - Files with 3+ tags: 95%
  - Files with blessed tags only: 85%+
```

---

## Recommended Plugin Priorities

Based on this analysis:

### v0.1: OBSERVATION
```
Priority 1: /taxonomy-scan
  → Generate reports like this automatically
  → Track drift over time

Priority 2: /tag-usage <tag>
  → See where specific tags are used
  → Validate consolidation ideas
```

### v0.2: GOVERNANCE
```
Priority 1: /taxonomy-migrate <old> <new>
  → Bulk-rename tags (fix partner-* variants)

Priority 2: /taxonomy-propose
  → Auto-detect consolidation opportunities
  → Suggest blessed tag list based on frequency
```

### v0.3: GUIDANCE
```
Priority 1: /suggest-tags
  → For new files, suggest tags based on content + domain

Priority 2: PreToolUse hook
  → Validate against blessed taxonomy
  → Alert on single-use tags
```

---

## Appendix: Full Tag List (Alphabetical)

```
ad-copy (1)
advisor-engagement (1)
ai-agent-guide (1)
analyst-relations (1)
appsec-challenges (1)
b2b-best-practices (1)
battlecards (1)
beta-launch (1)
brand (1)
brand-value (1)
buyer-intelligence (1)
buyer-personas (1)
call-summaries (1)
call-transcript (47)
campaign (2)
category-creation (1)
category-leadership (1)
ciso-concerns (1)
competitive (2)
competitive-intelligence (2)
compliance (1)
content (8)
content-strategy (2)
conversion-optimization (1)
creator-partnerships (1)
cta-optimization (1)
customer (1)
customer-intelligence (52)
customer-onboarding (1)
customer-relationship (1)
demand-generation (1)
design-partner (1)
documentation (1)
early-stage (1)
ecosystem (1)
example (1)
exec-summary (1)
execution-standards (1)
executive-deep-dive (1)
executive-intro (2)
executive-summary (1)
existing-relationship (1)
faq (3)
faq-content (1)
financial-services (3)
foundation (6)
google-ads (1)
incomplete-data (1)
investor-relations (1)
japan (3)
japan-market (1)
keyword-research (1)
knowledge-graph (1)
linking-strategy (1)
market (2)
market-segmentation (1)
marketing (2)
meddpicc (1)
messaging (3)
middle-east (2)
navigation (1)
objection-handling (2)
operational (3)
pain-points (1)
partner-channel (4)
partner-network (1)
partner-relations (1)
pattern-analysis (1)
personas (1)
pillar-page (1)
pillar-page-planning (2)
poc-planning (1)
positioning (2)
pov-customer (2)
product-launch (1)
product-marketing (1)
qualified-opportunity (5)
remediation-layer (4)
roi-analysis (1)
sales (3)
sales-enablement (1)
sales-insights (2)
sales-pipeline (1)
sca (1)
sdr (1)
seo (2)
seo-strategy (2)
strategic-feedback (1)
style (1)
tactical (1)
taxonomy (1)
technical-documentation (1)
template (1)
tofu (1)
vertical-analysis (1)
video-strategy (1)
visual-assets (1)
voice (1)
workflow (1)
outreach (1)
```

**Total: 100 unique tags**

---

**Next Steps:** Use this baseline to design Taxonomy Navigator plugin (Phase 2: Architecture).
