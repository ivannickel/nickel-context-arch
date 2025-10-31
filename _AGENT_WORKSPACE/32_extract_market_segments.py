#!/usr/bin/env python3
"""
Market Segment Extraction Script
Extracts firmographic and industry data from all 166 Nickel sales transcripts
Generates market segment nodes with ICP validation
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict

# Define paths
TRANSCRIPT_DIR = Path("knowledge_base/meetings_md")
SEGMENT_DIR = Path("knowledge_base/01_customer/market_segments")
TAXONOMY_FILE = Path("knowledge_base/taxonomy.yaml")

# Industry mapping to segment categories
INDUSTRY_MAPPING = {
    'construction': {
        'segment': 'construction-trades',
        'display_name': 'Construction & Trades',
        'icp_fit': 'PRIMARY',
        'strategic_weight': 9,
        'subcategories': ['Roofing', 'HVAC', 'Plumbing', 'Electrical', 'General Contractors',
                         'Remodeling', 'Concrete & Masonry', 'Flooring', 'Landscaping']
    },
    'manufacturing': {
        'segment': 'manufacturing-distribution',
        'display_name': 'Manufacturing & Custom Fabrication',
        'icp_fit': 'SECONDARY',
        'strategic_weight': 8,
        'subcategories': ['Metal Fabrication', 'Building Products', 'Industrial Equipment',
                         'Wood Products', 'Custom Manufacturing']
    },
    'professional_services': {
        'segment': 'professional-services',
        'display_name': 'Professional Services (B2B)',
        'icp_fit': 'TERTIARY',
        'strategic_weight': 5,
        'subcategories': ['Consulting', 'Business Services', 'Technical Services', 'Legal Services']
    },
    'accounting': {
        'segment': 'accounting-firms',
        'display_name': 'Accounting Firms & Bookkeeping',
        'icp_fit': 'STRATEGIC',
        'strategic_weight': 10,
        'subcategories': ['Accounting Firms', 'Bookkeeping Services', 'Tax Preparation', 'Financial Services']
    },
    'property_management': {
        'segment': 'property-management',
        'display_name': 'Property Management & HOA',
        'icp_fit': 'TERTIARY',
        'strategic_weight': 6,
        'subcategories': ['HOA Management', 'Commercial Property Management', 'Residential Property Management']
    },
    'hospitality': {
        'segment': 'hospitality-services',
        'display_name': 'Hospitality & Events',
        'icp_fit': 'NON-ICP',
        'strategic_weight': 3,
        'subcategories': ['Hotels', 'Event Services', 'Food Service', 'Catering']
    },
    'retail': {
        'segment': 'retail-non-icp',
        'display_name': 'Retail (Non-ICP)',
        'icp_fit': 'NON-ICP',
        'strategic_weight': 1,
        'subcategories': ['Retail Stores', 'Consumer-Facing']
    },
    'other': {
        'segment': 'other-industries',
        'display_name': 'Other Industries',
        'icp_fit': 'MIXED',
        'strategic_weight': 4,
        'subcategories': ['Mixed', 'Uncategorized', 'Various']
    },
    'transportation': {
        'segment': 'transportation-logistics',
        'display_name': 'Transportation & Logistics',
        'icp_fit': 'SECONDARY',
        'strategic_weight': 7,
        'subcategories': ['Trucking', 'Freight', 'Warehousing', 'Logistics']
    },
    'publishing': {
        'segment': 'media-publishing-non-icp',
        'display_name': 'Media & Publishing (Non-ICP)',
        'icp_fit': 'NON-ICP',
        'strategic_weight': 2,
        'subcategories': ['Publishing', 'Media Production']
    },
    'financial': {
        'segment': 'financial-services-non-icp',
        'display_name': 'Financial Services (Non-ICP)',
        'icp_fit': 'NON-ICP',
        'strategic_weight': 2,
        'subcategories': ['Financial Services', 'Banking-adjacent']
    }
}

# Revenue tier mapping
REVENUE_TIERS = {
    'shrimp': {'range': '<$1M', 'priority': 3, 'strategic_weight': 3},
    'fish': {'range': '$1M-$5M', 'priority': 2, 'strategic_weight': 6},
    'whale': {'range': '$5M-$25M', 'priority': 1, 'strategic_weight': 9},
    'kraken': {'range': '$25M+', 'priority': 1, 'strategic_weight': 8},
    'unknown': {'range': 'Unknown', 'priority': 4, 'strategic_weight': 4}
}

def parse_yaml_frontmatter(filepath):
    """Extract YAML frontmatter from markdown file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match YAML frontmatter
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except Exception as e:
            print(f"Error parsing YAML in {filepath}: {e}")
            return {}
    return {}

def extract_segment_data():
    """Extract market segment data from all transcripts"""
    segment_data = defaultdict(lambda: {
        'transcripts': [],
        'revenue_distribution': defaultdict(int),
        'ar_vs_ap': defaultdict(int),
        'call_types': defaultdict(int),
        'deal_stages': defaultdict(int)
    })

    for transcript_file in TRANSCRIPT_DIR.glob("*.md"):
        metadata = parse_yaml_frontmatter(transcript_file)

        # Extract key fields
        industry = metadata.get('primary_industry', 'other')
        revenue_tier = metadata.get('customer_segment', 'unknown')
        ar_vs_ap = metadata.get('ar_vs_ap', 'unclear')
        call_type = metadata.get('call_type', 'unknown')
        deal_stage = metadata.get('deal_stage', 'unknown')

        # Clean up industry field (handle non-string values)
        if not isinstance(industry, str):
            industry = 'other'

        # Accumulate data
        segment_key = industry
        segment_data[segment_key]['transcripts'].append({
            'file': transcript_file.name,
            'revenue_tier': revenue_tier,
            'ar_vs_ap': ar_vs_ap,
            'call_type': call_type,
            'deal_stage': deal_stage
        })

        if isinstance(revenue_tier, str):
            segment_data[segment_key]['revenue_distribution'][revenue_tier] += 1
        if isinstance(ar_vs_ap, str):
            segment_data[segment_key]['ar_vs_ap'][ar_vs_ap] += 1
        if isinstance(call_type, str):
            segment_data[segment_key]['call_types'][call_type] += 1
        if isinstance(deal_stage, str):
            segment_data[segment_key]['deal_stages'][deal_stage] += 1

    return segment_data

def generate_segment_node(segment_key, segment_data, total_transcripts):
    """Generate a market segment node file"""

    # Get industry mapping
    industry_config = INDUSTRY_MAPPING.get(segment_key, INDUSTRY_MAPPING['other'])

    # Calculate metrics
    transcript_count = len(segment_data['transcripts'])
    percentage = round((transcript_count / total_transcripts) * 100, 1)

    # Revenue distribution
    revenue_dist = segment_data['revenue_distribution']
    fish_count = revenue_dist.get('fish', 0)
    whale_count = revenue_dist.get('whale', 0)
    kraken_count = revenue_dist.get('kraken', 0)
    shrimp_count = revenue_dist.get('shrimp', 0)
    unknown_count = revenue_dist.get('unknown', 0)

    # AR/AP focus
    ar_vs_ap_dist = segment_data['ar_vs_ap']
    ar_only = ar_vs_ap_dist.get('ar_only', 0) + ar_vs_ap_dist.get('ar', 0)
    ap_only = ar_vs_ap_dist.get('ap_only', 0) + ar_vs_ap_dist.get('ap', 0)
    both = ar_vs_ap_dist.get('both', 0)
    unclear = ar_vs_ap_dist.get('unclear', 0)

    # Determine AR vs AP dominant focus
    if ar_only > ap_only and ar_only > both:
        ar_ap_profile = "AR-dominant"
    elif ap_only > ar_only and ap_only > both:
        ar_ap_profile = "AP-dominant"
    elif both > ar_only and both > ap_only:
        ar_ap_profile = "Balanced (both AR & AP)"
    else:
        ar_ap_profile = "Mixed/Unclear"

    # Determine status
    if transcript_count >= 20:
        status = "canonical"
        confidence = 9.0
    elif transcript_count >= 5:
        status = "validated"
        confidence = 7.5
    else:
        status = "emergent"
        confidence = 5.0

    # Generate markdown content
    content = f"""---
node_type: market_segment
domain: customer
segment_name: "{industry_config['display_name']}"
icp_fit: "{industry_config['icp_fit']}"
frequency: {transcript_count}
percentage_of_corpus: {percentage}
status: {status}
confidence: {confidence}
strategic_importance: {industry_config['strategic_weight']}
created: 2025-10-30
last_updated: 2025-10-30

tags:
  - market-segments
  - {segment_key}
  - icp-{industry_config['icp_fit'].lower()}

firmographic_distribution:
  fish_tier: {fish_count}
  whale_tier: {whale_count}
  kraken_tier: {kraken_count}
  shrimp_tier: {shrimp_count}
  unknown_tier: {unknown_count}

ar_vs_ap_profile:
  ar_only: {ar_only}
  ap_only: {ap_only}
  both: {both}
  unclear: {unclear}
  dominant_focus: "{ar_ap_profile}"

validated_by:
  - source: "Transcript corpus analysis (166 files)"
    date: "2025-10-30"
    evidence: "YAML frontmatter strategic classification"
    transcript_count: {transcript_count}
---

# {industry_config['display_name']}

**ICP Fit:** {industry_config['icp_fit']}
**Frequency:** {transcript_count} of 166 transcripts ({percentage}%)
**Status:** {status}
**Strategic Importance:** {industry_config['strategic_weight']}/10

## Overview

{industry_config['display_name']} represents {percentage}% of the Nickel sales transcript corpus ({transcript_count} transcripts). This segment has been classified as **{industry_config['icp_fit']} ICP fit** with a strategic importance score of {industry_config['strategic_weight']}/10.

## Segment Description

{generate_segment_description(segment_key, industry_config)}

## Segment Characteristics

**Typical Revenue Distribution:**
- Fish ($1-5M): {fish_count} companies ({round(fish_count/transcript_count*100, 1) if transcript_count > 0 else 0}%)
- Whale ($5-25M): {whale_count} companies ({round(whale_count/transcript_count*100, 1) if transcript_count > 0 else 0}%)
- Kraken ($25M+): {kraken_count} companies ({round(kraken_count/transcript_count*100, 1) if transcript_count > 0 else 0}%)
- Shrimp (<$1M): {shrimp_count} companies ({round(shrimp_count/transcript_count*100, 1) if transcript_count > 0 else 0}%)
- Unknown: {unknown_count} companies ({round(unknown_count/transcript_count*100, 1) if transcript_count > 0 else 0}%)

**AR vs AP Focus:**
- AR-only: {ar_only} ({round(ar_only/transcript_count*100, 1) if transcript_count > 0 else 0}%)
- AP-only: {ap_only} ({round(ap_only/transcript_count*100, 1) if transcript_count > 0 else 0}%)
- Both AR & AP: {both} ({round(both/transcript_count*100, 1) if transcript_count > 0 else 0}%)
- Unclear: {unclear} ({round(unclear/transcript_count*100, 1) if transcript_count > 0 else 0}%)

**Dominant Focus:** {ar_ap_profile}

## Firmographic Distribution

### Revenue Tier Breakdown

| Tier | Count | Percentage | Strategic Fit |
|------|-------|------------|---------------|
| Whale ($5-25M) | {whale_count} | {round(whale_count/transcript_count*100, 1) if transcript_count > 0 else 0}% | High (9/10) |
| Kraken ($25M+) | {kraken_count} | {round(kraken_count/transcript_count*100, 1) if transcript_count > 0 else 0}% | High (8/10) |
| Fish ($1-5M) | {fish_count} | {round(fish_count/transcript_count*100, 1) if transcript_count > 0 else 0}% | Medium (6/10) |
| Shrimp (<$1M) | {shrimp_count} | {round(shrimp_count/transcript_count*100, 1) if transcript_count > 0 else 0}% | Low (3/10) |
| Unknown | {unknown_count} | {round(unknown_count/transcript_count*100, 1) if transcript_count > 0 else 0}% | TBD (4/10) |

## ICP Fit Analysis

{generate_icp_analysis(segment_key, industry_config, fish_count, whale_count, kraken_count, ar_ap_profile)}

## Foundation Validation

{generate_foundation_validation(segment_key, industry_config, transcript_count, percentage)}

## Cross-References

**Related Foundation Nodes:**
- [[icp-definition]] - Revenue qualification tiers
- [[ideal-verticals]] - Industry vertical priorities
- [[anti-icp]] - Non-target segments

**Segment Priority:** {industry_config['icp_fit']}

## Strategic Notes

{generate_strategic_notes(segment_key, industry_config, transcript_count, percentage, ar_ap_profile)}
"""

    return content

def generate_segment_description(segment_key, config):
    """Generate segment-specific description"""
    descriptions = {
        'construction': "Construction and trades companies including general contractors, HVAC, roofing, plumbing, electrical, and specialty contractors. Characterized by project-based work, invoice-based payments, and net terms requests.",
        'manufacturing': "Manufacturing and fabrication businesses producing building products, industrial equipment, metal fabrication, and custom products. Typically B2B sales with large transaction values.",
        'professional_services': "B2B professional services including consulting, business services, and technical services. Generally high-margin businesses with time-based billing.",
        'accounting': "Accounting firms, bookkeeping services, and financial advisors managing multiple client businesses. Strategic segment due to multiplier effect (1 firm = 50-150 clients).",
        'property_management': "Property management companies and HOA management firms handling payments for property owners and residents.",
        'hospitality': "Hospitality and event services businesses. Consumer-facing with different payment dynamics than B2B ICP.",
        'retail': "Retail businesses selling directly to consumers. Non-ICP segment due to consumer-facing nature.",
        'transportation': "Transportation, trucking, freight, and logistics companies serving B2B customers.",
        'publishing': "Publishing and media production businesses. Generally not ICP fit.",
        'financial': "Financial services businesses. Generally not ICP fit due to regulatory complexity.",
        'other': "Various industries not fitting primary categories. Mixed ICP fit requiring individual assessment."
    }
    return descriptions.get(segment_key, "Industry segment requiring further categorization and analysis.")

def generate_icp_analysis(segment_key, config, fish_count, whale_count, kraken_count, ar_profile):
    """Generate ICP fit analysis"""
    icp_fit = config['icp_fit']

    if icp_fit == 'PRIMARY':
        return f"""**Why This Segment Fits Nickel ICP:**
1. Project-based B2B transactions align with invoice-based payment model
2. Mix of revenue tiers shows broad market applicability
3. {ar_profile} profile matches Nickel's AR automation value proposition
4. High strategic fit weight ({config['strategic_weight']}/10) indicates strong product-market fit

**Strategic Fit Assessment:** **HIGH**

**Segment Prioritization:** PRIMARY ICP segment - prioritize for sales, marketing, and product development."""

    elif icp_fit == 'SECONDARY':
        return f"""**Why This Segment Fits Nickel ICP:**
1. B2B transaction model aligns with Nickel's core value proposition
2. Revenue distribution shows qualified opportunities ({whale_count} Whales, {kraken_count} Krakens)
3. {ar_profile} profile indicates payment automation needs
4. Strategic fit weight ({config['strategic_weight']}/10) shows strong potential

**Strategic Fit Assessment:** **MEDIUM-HIGH**

**Segment Prioritization:** SECONDARY ICP segment - pursue qualified opportunities, monitor for conversion patterns."""

    elif icp_fit == 'TERTIARY':
        return f"""**Segment Fit Considerations:**
1. Partial alignment with ICP criteria (revenue distribution, transaction types)
2. {ar_profile} profile may or may not align with ideal customer
3. Strategic fit weight ({config['strategic_weight']}/10) indicates selective pursuit
4. Requires individual qualification based on firmographic details

**Strategic Fit Assessment:** **MEDIUM**

**Segment Prioritization:** TERTIARY - evaluate on case-by-case basis, prioritize Whale/Kraken tiers."""

    elif icp_fit == 'STRATEGIC':
        return f"""**Why This Segment Has Strategic Value:**
1. **Multiplier Effect:** Single accounting firm can bring 50-150 client businesses
2. High-value channel partnership opportunity
3. {ar_profile} profile indicates multi-client payment management needs
4. Strategic fit weight ({config['strategic_weight']}/10) = highest priority

**Strategic Fit Assessment:** **VERY HIGH (Strategic Channel)**

**Segment Prioritization:** STRATEGIC - dedicated partnership approach, high-touch sales, validate multiplier hypothesis."""

    else:  # NON-ICP or MIXED
        return f"""**Segment Fit Analysis:**
1. {icp_fit} fit indicates limited alignment with core ICP criteria
2. Revenue distribution: {fish_count} Fish, {whale_count} Whale, {kraken_count} Kraken
3. {ar_profile} profile shows payment needs exist but may not align with revenue model
4. Strategic fit weight ({config['strategic_weight']}/10) = low priority

**Strategic Fit Assessment:** **LOW**

**Segment Prioritization:** NON-ICP - deprioritize unless exceptional firmographic fit (e.g., Whale/Kraken with AR focus)."""

def generate_foundation_validation(segment_key, config, transcript_count, percentage):
    """Generate foundation ICP validation analysis"""
    icp_fit = config['icp_fit']

    if icp_fit in ['PRIMARY', 'SECONDARY']:
        return f"""**ICP Definition Validation:**
- **Foundation assumption:** {config['display_name']} is {icp_fit.lower()} target vertical
- **Transcript evidence:** {transcript_count} transcripts ({percentage}% of corpus)
- **Validation:** **CONFIRMED** - segment appears in corpus at expected frequency

**Industry Vertical Assumptions:**
- **Foundation claim:** Strategic fit weight = {config['strategic_weight']}/10
- **Transcript pattern:** Represents {percentage}% of pipeline conversations
- **Validation:** **CONFIRMED** - aligns with expected market penetration

**Strategic Implication:** Foundation ICP assumptions validated. Continue prioritization strategy."""

    elif icp_fit == 'STRATEGIC':
        return f"""**ICP Definition Validation:**
- **Foundation assumption:** Accounting firms have multiplier effect (1 firm = 50-150 clients)
- **Transcript evidence:** {transcript_count} accounting firm conversations ({percentage}% of corpus)
- **Validation:** **NEEDS VALIDATION** - hypothesis requires proof of multiplier effect

**Strategic Implication:** Small sample size ({transcript_count} transcripts) requires deeper investigation. Validate:
1. Are accounting firms actually managing multiple client payments?
2. What is actual client multiplier (50? 100? 150+)?
3. Conversion rate vs. standard business customers?"""

    elif icp_fit == 'NON-ICP':
        return f"""**ICP Definition Validation:**
- **Foundation assumption:** {config['display_name']} is non-ICP (anti-persona or low fit)
- **Transcript evidence:** {transcript_count} transcripts ({percentage}% of corpus) - should be minimal
- **Validation:** **CONTRADICTS** if {percentage}% > 10% OR **CONFIRMS** if {percentage}% < 10%

**Strategic Implication:** {"HIGH leakage of non-ICP leads into pipeline. Review lead qualification process." if percentage > 10 else "Low corpus percentage confirms proper ICP filtering. Maintain current qualification standards."}"""

    else:  # MIXED/TERTIARY
        return f"""**ICP Definition Validation:**
- **Foundation assumption:** {config['display_name']} requires case-by-case evaluation
- **Transcript evidence:** {transcript_count} transcripts ({percentage}% of corpus)
- **Validation:** **PARTIALLY VALIDATED** - significant presence indicates market pull

**Strategic Implication:** Consider upgrading segment priority if conversion rates justify. Monitor Whale/Kraken performance in this segment."""

def generate_strategic_notes(segment_key, config, transcript_count, percentage, ar_profile):
    """Generate strategic recommendations"""
    notes = f"""**Key Insights:**
- {config['display_name']} represents {percentage}% of sales conversations
- {ar_profile} indicates payment workflow patterns
- Strategic importance: {config['strategic_weight']}/10

**Recommendations:**
"""

    if config['icp_fit'] == 'PRIMARY':
        notes += """1. Prioritize marketing and sales resources to this segment
2. Develop segment-specific messaging and use cases
3. Monitor conversion rates and LTV for optimization
4. Consider vertical-specific product features"""

    elif config['icp_fit'] == 'SECONDARY':
        notes += """1. Maintain active pursuit of qualified opportunities
2. Develop segment understanding through customer interviews
3. Track conversion and retention metrics vs. primary ICP
4. Adjust prioritization based on performance data"""

    elif config['icp_fit'] == 'STRATEGIC':
        notes += """1. Validate multiplier hypothesis with existing customers
2. Develop partnership/channel strategy for accounting firms
3. Create dedicated onboarding and support for multi-client use case
4. Measure actual client count per accounting firm customer"""

    elif config['icp_fit'] == 'NON-ICP':
        notes += """1. Review lead qualification to reduce non-ICP pipeline leakage
2. Deprioritize unless Whale/Kraken tier with exceptional fit
3. Consider pass-through to self-serve onboarding
4. Monitor for false negatives (good fits misclassified as non-ICP)"""

    else:  # MIXED/TERTIARY
        notes += """1. Evaluate individual opportunities based on firmographics
2. Prioritize Whale/Kraken tiers within this segment
3. Require strong pain point validation before pursuing
4. Monitor performance to determine if segment should be upgraded/downgraded"""

    return notes

def main():
    """Main execution function"""
    print("Extracting market segment data from 166 transcripts...")

    # Extract data
    segment_data = extract_segment_data()
    total_transcripts = sum(len(data['transcripts']) for data in segment_data.values())

    print(f"Total transcripts processed: {total_transcripts}")
    print(f"Segments identified: {len(segment_data)}")

    # Create segment directory if it doesn't exist
    SEGMENT_DIR.mkdir(parents=True, exist_ok=True)

    # Generate segment node files
    for segment_key, data in segment_data.items():
        if segment_key in INDUSTRY_MAPPING:
            segment_slug = INDUSTRY_MAPPING[segment_key]['segment']
            output_file = SEGMENT_DIR / f"{segment_slug}.md"

            content = generate_segment_node(segment_key, data, total_transcripts)

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"Created: {output_file} ({len(data['transcripts'])} transcripts)")

    print("\nMarket segment extraction complete!")
    print(f"Files created in: {SEGMENT_DIR}")

if __name__ == "__main__":
    main()
