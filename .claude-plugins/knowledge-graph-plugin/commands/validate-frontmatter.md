---
description: Validate YAML frontmatter of currently open file against taxonomy standards
---

Validate the currently open file's YAML frontmatter using the Taxonomy Enforcement Agent.

Check for:
- Presence of YAML frontmatter
- All required fields (name, description, domain, file_type, last_updated, tags)
- Domain tag inclusion in tags array
- Minimum 3 related_docs with at least 1 Tier 1 hub link
- Topic count (3-7 recommended)
- Persona count (2+ for customer/content domains)
- Field value formatting (lowercase-with-hyphens, ALL_CAPS, etc.)

Provide specific, actionable corrections if non-compliant with examples from the Knowledge Graph Management Guide.
