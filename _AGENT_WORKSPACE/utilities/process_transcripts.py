#!/usr/bin/env python3
"""
CircleBack CSV to Markdown Converter
Converts meeting transcripts from CSV to individual MD files with YAML frontmatter.
Optimized for LLM token efficiency.
"""

import pandas as pd
from pathlib import Path
from datetime import datetime
import re
import yaml


def slugify(text):
    """Convert text to URL-friendly slug."""
    text = str(text).lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text[:50]  # Limit length


def format_date(iso_date):
    """Convert ISO date to YYYY-MM-DD format."""
    try:
        dt = datetime.fromisoformat(iso_date.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d')
    except:
        return 'unknown-date'


def format_time(iso_date):
    """Extract time from ISO date."""
    try:
        dt = datetime.fromisoformat(iso_date.replace('Z', '+00:00'))
        return dt.strftime('%H:%M:%S')
    except:
        return 'unknown-time'


def parse_participants(participants_str):
    """Parse participants string into list."""
    if pd.isna(participants_str):
        return []

    # Split by comma and clean up
    parts = [p.strip() for p in str(participants_str).split(',')]
    return parts


def create_frontmatter(row, meeting_number):
    """Generate YAML frontmatter from meeting data."""
    duration_sec = float(row['Duration (sec)']) if pd.notna(row['Duration (sec)']) else 0
    duration_min = round(duration_sec / 60, 1) if duration_sec > 0 else 0

    frontmatter = {
        'title': str(row['Meeting Title']).strip(),
        'date': format_date(row['Meeting Date']),
        'time': format_time(row['Meeting Date']),
        'duration_sec': duration_sec,
        'duration_min': duration_min,
        'participants': parse_participants(row['Participants']),
        'source': str(row['Source']) if pd.notna(row['Source']) else '',
        'meeting_number': meeting_number
    }

    return yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)


def process_transcript(transcript):
    """Process transcript text, preserving original format for token efficiency."""
    if pd.isna(transcript) or str(transcript).strip() == '':
        return '[No transcript available]'

    # Return as-is for maximum token efficiency
    # Format: "Speaker Name: text" is already optimal
    return str(transcript).strip()


def generate_filename(row, meeting_number):
    """Generate filename: 001_meeting-name_2025-07-23.md"""
    number = str(meeting_number).zfill(3)
    slug = slugify(row['Meeting Title'])
    date = format_date(row['Meeting Date'])

    return f"{number}_{slug}_{date}.md"


def create_markdown_file(row, meeting_number, output_dir):
    """Create individual markdown file for meeting."""
    # Generate filename
    filename = generate_filename(row, meeting_number)
    filepath = output_dir / filename

    # Create frontmatter
    frontmatter = create_frontmatter(row, meeting_number)

    # Process transcript
    transcript = process_transcript(row['Transcript'])

    # Get recording URL
    recording_url = str(row['Recording URL']) if pd.notna(row['Recording URL']) else ''

    # Assemble markdown content
    content = f"""---
{frontmatter}---

{transcript}

---

**Recording:** {recording_url}
"""

    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filename


def process_csv(csv_path, output_dir, sample_size=None):
    """
    Process CSV and generate markdown files.

    Args:
        csv_path: Path to CircleBack CSV file
        output_dir: Directory to output MD files
        sample_size: If set, only process first N meetings (for testing)
    """
    # Load CSV
    print(f"Loading CSV from: {csv_path}")
    df = pd.read_csv(csv_path)
    print(f"Found {len(df)} meetings")

    # Apply sample limit if specified
    if sample_size:
        df = df.head(sample_size)
        print(f"Processing sample: {len(df)} meetings")

    # Create output directory
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {output_dir}")

    # Process each meeting
    created_files = []
    for idx, row in df.iterrows():
        meeting_number = idx + 1
        try:
            filename = create_markdown_file(row, meeting_number, output_dir)
            created_files.append(filename)
            print(f"  [OK] Created: {filename}")
        except Exception as e:
            print(f"  [ERROR] Error processing meeting {meeting_number}: {e}")

    print(f"\n{'='*60}")
    print(f"Processing complete!")
    print(f"Created {len(created_files)} markdown files")
    print(f"Output location: {output_dir.absolute()}")

    return created_files


if __name__ == "__main__":
    # Configuration
    CSV_PATH = r"C:\Users\dietl\VSCode Projects\taste_systems\gtm_operating_system\gtm_engagements\03_active_client\nickel_ivan\nickel_gtm_context_architecture\knowledge_base\Circleback - Sheet1.csv"
    OUTPUT_DIR = r"C:\Users\dietl\VSCode Projects\taste_systems\gtm_operating_system\gtm_engagements\03_active_client\nickel_ivan\nickel_gtm_context_architecture\knowledge_base\meetings_md"

    # Run with sample or full processing
    # Set to None to process all meetings
    SAMPLE_SIZE = None  # Full run - all 165 meetings

    process_csv(CSV_PATH, OUTPUT_DIR, sample_size=SAMPLE_SIZE)
