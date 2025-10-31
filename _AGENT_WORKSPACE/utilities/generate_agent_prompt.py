#!/usr/bin/env python3
"""
Generate agent prompts for transcript classification batches.
"""

import sys
from pathlib import Path

def read_first_n_lines(filepath: Path, n: int = 200) -> str:
    """Read first N lines of a file."""
    with filepath.open("r", encoding="utf-8") as f:
        lines = []
        for i, line in enumerate(f):
            if i >= n:
                break
            lines.append(line)
        return "".join(lines)

def generate_batch_prompt(batch_id: int) -> str:
    """Generate classification prompt for a batch."""

    # Read batch manifest
    batch_file = Path(f"_AGENT_WORKSPACE/transcript_batches/batch_{batch_id:02d}.txt")
    with batch_file.open("r") as f:
        transcript_paths = [Path(line.strip()) for line in f if line.strip()]

    # Read schema (condensed version)
    schema_summary = """
## SCHEMA: Strategic Classification Fields

ADD these fields below existing Circleback frontmatter (do NOT duplicate existing fields):

```yaml
# === STRATEGIC CLASSIFICATION ===
call_type: discovery | demo | kickoff | review | follow_up | general
deal_stage: discovery | evaluation | activation | active | expansion | churned
customer_segment: shrimp | fish | whale | unknown

has_pain_points: true | false
has_objections: true | false
has_competitive_intel: true | false
has_use_case: true | false
has_pricing_discussion: true | false
has_integration_needs: true | false

primary_industry: construction | accounting | professional_services | manufacturing | hospitality | property_management | other
transaction_volume: sub_threshold | near_threshold | above_threshold | unknown
ar_vs_ap: ap_only | ar_only | both | unclear

processed: false
dimensional_extracted: false
extraction_priority: high | medium | low
```

## CLASSIFICATION LOGIC:

**call_type** (from filename):
- "kickoff" in filename → kickoff
- "review" in filename → review
- "follow-up" in filename → follow_up
- "demo" in filename → demo
- "and-colton" or "and-jacob" in filename → discovery
- else → general

**deal_stage** (from call_type):
- discovery → discovery
- demo → evaluation
- kickoff → activation
- review/follow_up → active

**Strategic signals** (scan content for keywords):
- has_pain_points: "pain", "problem", "challenge", "struggling", "difficult", "frustrated"
- has_objections: "concern", "worried", "expensive", "complicated", "not sure", "already using"
- has_competitive_intel: "Relay", "Melio", "Bill.com", "PayPal", "Zelle", "competitor"
- has_use_case: "workflow", "process", "how we do", "currently we"
- has_pricing_discussion: "$", "cost", "price", "rate", "discount", "savings", "2.9"
- has_integration_needs: "QuickBooks", "integration", "connect", "sync", "API"

**extraction_priority** (calculated):
- HIGH: discovery + (competitive_intel OR objections OR pricing_discussion) OR transaction_volume=above_threshold
- MEDIUM: (demo OR kickoff) AND use_case, OR has_pain_points=true
- LOW: follow_up/general OR minimal signals

**customer_segment** (from volume discussion):
- < $500K AP spend → shrimp
- $500K-$2M → fish
- > $2M → whale
- No clear indication → unknown

**transaction_volume**:
- Mentions < $500K → sub_threshold
- Mentions $800K-$2M → near_threshold
- Mentions > $2M → above_threshold
- No discussion → unknown
"""

    # Build prompt
    prompt_parts = [
        "You are a sales call transcript classifier. Your task: Add strategic frontmatter to sales call transcripts.",
        "",
        schema_summary,
        "",
        "## INSTRUCTIONS:",
        "1. For each transcript below, read ONLY the provided excerpt (first ~200 lines)",
        "2. Use filename patterns to infer call_type",
        "3. Scan content for keyword matches (case-insensitive)",
        "4. Output ONLY the NEW frontmatter fields (do not include existing Circleback fields)",
        "5. Be consistent across all transcripts in this batch",
        "",
        f"## BATCH {batch_id}: {len(transcript_paths)} TRANSCRIPTS",
        ""
    ]

    # Add each transcript excerpt
    for i, path in enumerate(transcript_paths, 1):
        filename = path.name
        excerpt = read_first_n_lines(path, n=200)

        prompt_parts.extend([
            f"### TRANSCRIPT {i}/{len(transcript_paths)}: {filename}",
            "",
            "```",
            excerpt,
            "```",
            ""
        ])

    prompt_parts.extend([
        "## OUTPUT FORMAT:",
        "",
        "For each transcript, output:",
        "```",
        "=== TRANSCRIPT: filename.md ===",
        "call_type: value",
        "deal_stage: value",
        "customer_segment: value",
        "has_pain_points: true/false",
        "has_objections: true/false",
        "has_competitive_intel: true/false",
        "has_use_case: true/false",
        "has_pricing_discussion: true/false",
        "has_integration_needs: true/false",
        "primary_industry: value",
        "transaction_volume: value",
        "ar_vs_ap: value",
        "processed: false",
        "dimensional_extracted: false",
        "extraction_priority: value",
        "```",
        "",
        "Output classification for ALL transcripts above. Be thorough and consistent."
    ])

    return "\n".join(prompt_parts)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_agent_prompt.py <batch_id>")
        sys.exit(1)

    batch_id = int(sys.argv[1])
    prompt = generate_batch_prompt(batch_id)
    print(prompt)
