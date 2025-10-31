#!/usr/bin/env python3
"""
Create batch manifest files for parallel transcript processing.

Splits 165 transcripts into 17 batches of ~10 transcripts each.
Output: _AGENT_WORKSPACE/transcript_batches/batch_{01..17}.txt
"""

import os
from pathlib import Path
from typing import List

# Configuration
TRANSCRIPTS_DIR = Path("knowledge_base/meetings_md")
BATCHES_DIR = Path("_AGENT_WORKSPACE/transcript_batches")
BATCH_SIZE = 10

def get_transcript_files() -> List[Path]:
    """Get all transcript markdown files, sorted by filename."""
    transcripts = sorted(TRANSCRIPTS_DIR.glob("*.md"))
    # Exclude schema files
    transcripts = [t for t in transcripts if not t.name.startswith("_")]
    return transcripts

def create_batches(transcripts: List[Path], batch_size: int) -> List[List[Path]]:
    """Split transcripts into batches."""
    batches = []
    for i in range(0, len(transcripts), batch_size):
        batch = transcripts[i:i + batch_size]
        batches.append(batch)
    return batches

def write_batch_manifest(batch_id: int, batch_files: List[Path]) -> None:
    """Write batch manifest file."""
    manifest_path = BATCHES_DIR / f"batch_{batch_id:02d}.txt"
    with manifest_path.open("w") as f:
        for filepath in batch_files:
            f.write(f"{filepath}\n")
    print(f"[OK] Created {manifest_path.name} ({len(batch_files)} transcripts)")

def main():
    # Create output directory
    BATCHES_DIR.mkdir(parents=True, exist_ok=True)

    # Get all transcript files
    transcripts = get_transcript_files()
    print(f"\nFound {len(transcripts)} transcripts in {TRANSCRIPTS_DIR}")

    # Create batches
    batches = create_batches(transcripts, BATCH_SIZE)
    print(f"Creating {len(batches)} batches (batch size: {BATCH_SIZE})\n")

    # Write manifest files
    for batch_id, batch_files in enumerate(batches, start=1):
        write_batch_manifest(batch_id, batch_files)

    # Summary
    print(f"\n[OK] Batch creation complete!")
    print(f"  Total transcripts: {len(transcripts)}")
    print(f"  Total batches: {len(batches)}")
    print(f"  Batch size: {BATCH_SIZE} (last batch: {len(batches[-1])})")
    print(f"  Output directory: {BATCHES_DIR}/")

if __name__ == "__main__":
    main()
