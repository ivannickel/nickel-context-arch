---
description: Run comprehensive health check on knowledge graph structure and compliance
---

Execute a comprehensive health assessment of the knowledge graph per the Knowledge Graph Management Guide (Section 5.3).

## Health Checks

1. **Orphaned Documents**
   - Find documents with no incoming `[[wiki-links]]`
   - Identify documents missing from any `related_docs` arrays

2. **Frontmatter Completeness**
   - Scan all .md files in active domains (00-05)
   - Calculate % with valid YAML frontmatter
   - Report documents missing required fields

3. **Hub Connectivity**
   - Verify all domains link to at least 1 Tier 1 hub
   - Check bi-directional links from hubs to spokes
   - Identify weak hub connections

4. **Broken Wiki-Links**
   - Parse all `[[wiki_links]]` in documents
   - Check if target files exist
   - Validate section anchors if present

5. **Archive Exclusion**
   - Verify `.foamignore` properly excludes `07_archive/**`
   - Check no active documents accidentally in archive

## Report Format

Generate a report with:

```markdown
# Knowledge Graph Health Report
Generated: [timestamp]

## Overall Health Score: X/100

### 🔴 Critical Issues (Require Immediate Fix)
- X orphaned documents found
- X documents missing required frontmatter fields
- X broken wiki-links detected

### 🟡 Warnings (Should Address Soon)
- X documents with <3 related_docs
- X customer/content docs missing personas
- X documents with no Tier 1 hub link

### 🟢 Healthy Metrics
- Frontmatter completeness: XX%
- Average links per document: X.X
- Hub connectivity: XX%

## Detailed Findings

### Orphaned Documents (No Incoming Links)
1. path/to/document1.md
2. path/to/document2.md

### Missing Required Frontmatter
1. path/to/document3.md - Missing: tags, topics
2. path/to/document4.md - Missing: domain tag in tags array

### Broken Wiki-Links
1. In document5.md: [[non_existent_doc]] - Target not found
2. In document6.md: [[doc#invalid-anchor]] - Section anchor invalid

## Recommendations
- [ ] Add frontmatter to X documents
- [ ] Link orphaned documents to appropriate hubs
- [ ] Fix broken wiki-links
- [ ] Add domain tags to X documents
```

Use Glob, Grep, and Read tools to scan the graph systematically across all active domains.
