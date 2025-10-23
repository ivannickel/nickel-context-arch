---
description: Generate and add compliant YAML frontmatter to current document
---

Analyze the currently open document and generate appropriate YAML frontmatter that complies with taxonomy standards.

## Process

1. **Infer Domain**
   - Detect from file path (00_foundation, 01_customer, etc.)
   - If ambiguous, ask user to clarify

2. **Suggest File Type**
   - Based on content analysis and domain
   - Use standard file types from Section 7.2 of guide

3. **Extract Topics and Personas**
   - Scan content for keywords matching universal topics library
   - Identify mentioned personas (CISO, VP Engineering, etc.)
   - Suggest 3-7 most relevant topics

4. **Recommend Related Docs**
   - Analyze content to identify related concepts
   - Always include at least 1 Tier 1 hub document
   - Suggest cross-domain strategic links
   - Aim for 5-7 `related_docs` recommendations

5. **Generate Complete YAML Block**
   - Follow template from Section 7.1
   - Use proper formatting (lowercase-with-hyphens, ALL_CAPS, etc.)
   - Include domain tag in tags array (CRITICAL for Foam color-coding)

## Output Format

Present the generated frontmatter for user approval before insertion:

```yaml
---
name: DOCUMENT_NAME_FROM_FILENAME
description: [Inferred one-sentence description]
domain: [inferred-domain]
file_type: [suggested-type]
canonical_source: false  # true if appears to be authoritative strategy doc
last_updated: [today's-date]

tags:
  - [domain-tag]  # REQUIRED for Foam color-coding
  - [function-tag-1]
  - [function-tag-2]

personas:
  - [suggested-persona-1]
  - [suggested-persona-2]

topics:
  - [topic-1]
  - [topic-2]
  - [topic-3]

related_docs:
  - "[[tier-1-hub-document]]"  # Always include at least 1 Tier 1 hub
  - "[[related-doc-1]]"
  - "[[related-doc-2]]"
  - "[[related-doc-3]]"
---
```

## Example

For a document in `01_customer/call_transcripts/` about a CISO discussing security backlog:

```yaml
---
name: ACME_CORP_CISO_DISCOVERY_CALL
description: Discovery call with ACME Corp CISO discussing security backlog and remediation challenges
domain: customer
file_type: call_transcript
canonical_source: false
last_updated: 2025-10-11

tags:
  - customer  # REQUIRED domain tag
  - customer-intelligence
  - pain-patterns

personas:
  - ciso
  - head-appsec

topics:
  - backlog-management
  - manual-triage-burden
  - automated-remediation
  - merge-rate

related_docs:
  - "[[All Call Summaries]]"
  - "[[Call Exec Summary]]"
  - "[[MEDDPICC_and_Personas#ciso-persona]]"
  - "[[CISO_and_AppSec_Pain_Points_Summary]]"
  - "[[comprehensive_market_and_customer_intelligence_context]]"
---
```

Ask user to confirm before inserting at the top of the file.
