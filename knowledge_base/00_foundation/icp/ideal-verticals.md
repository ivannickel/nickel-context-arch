---
node_type: icp_definition
status: baseline
confidence: 5.8
created: 2025-10-30
last_updated: 2025-10-30
sources:
  - ICP Summary & Use Cases 7085d388732a44caaa41db763f531999.md
  - strategic_lens.yaml v1.2
  - Classification Prompts 271508663b748051a9aff7653337f5a6.md
tags: [foundation, icp, industry-verticals, building-materials, construction]
validation_status: awaiting_transcript_validation
transcript_validations: 0
---

# Ideal Industry Verticals

**Status:** Baseline (from raw_context, awaiting transcript validation)
**Confidence:** 5.8/10
**Sources:** 3 raw_context documents

## Overview

Nickel's ideal industry verticals are defined by B2B businesses with large-ticket transactions, project-based work, and invoice-based payment workflows. The primary vertical is **Building Materials**, with strong secondary fit in construction trades, manufacturing, wholesale distribution, and logistics.

## Primary Vertical

**Building Materials**
[VERIFIED: ICP Summary.md:56-59] Identified as primary vertical across all three ICP tiers (Payment Upgraders, Cash-Savvy Sellers, Full Stack Automators)

[VERIFIED: strategic_lens.yaml:458-461] **Strategic fit weight: 10/10**

**Sub-segments:**
- Windows and doors
- Lighting and fixtures
- Millwork and cabinetry
- Kitchen & bath fixtures
- Pre-built materials
- Specialty materials
- Custom materials

**Characteristics:**
- Project-based sales cycles
- Invoice-based payments (net terms common)
- Mix of retail showroom + wholesale operations
- Regional or national buyer base

## Secondary Verticals (High Strategic Fit)

**Construction & Trades**
[VERIFIED: strategic_lens.yaml:464-467] **Strategic fit weight: 9/10**

Sub-segments:
- General Contractors
- Electrical contractors
- Plumbing contractors
- HVAC contractors
- Roofing contractors
- Concrete & Masonry
- Carpentry
- Painting contractors
- Flooring installers
- Landscaping companies

**Wholesale & Distribution**
[VERIFIED: strategic_lens.yaml:474-477] **Strategic fit weight: 9/10**

Sub-segments:
- Building materials distributors
- Electrical supply distributors
- Plumbing supply distributors
- HVAC equipment distributors
- Industrial supplies distributors

**Manufacturing**
[VERIFIED: strategic_lens.yaml:469-472] **Strategic fit weight: 8/10**

Sub-segments:
- Metal fabrication
- Building products manufacturing
- Custom manufacturing
- Wood products
- Industrial equipment manufacturing

**Transportation & Logistics**
[VERIFIED: strategic_lens.yaml:479-482] **Strategic fit weight: 7/10**

Sub-segments:
- Trucking & freight
- Specialized transport
- Warehousing services

**Large-Ticket B2B Services**
[VERIFIED: strategic_lens.yaml:484-487] **Strategic fit weight: 7/10**

Sub-segments:
- Equipment rental
- Heavy equipment services
- Event services (large-scale B2B)

## ICP Signal Keywords

[VERIFIED: Classification Prompts.md:83, strategic_lens.yaml:629-632] Keywords that indicate high-fit industry verticals:

**High-Priority Signals:**
- wholesale, distributor, trade account
- net terms, accounts receivable, invoice
- projects, contractor, supplier
- building materials

**Medium-Priority Signals:**
- RFQ (Request for Quote)
- quote, ACH, wire, check
- installations, industrial, commercial
- trucking, logistics

**Low-Priority Signals:**
- fabrication, cabinet, warehouse

## Construction Project Types

[VERIFIED: ICP Summary.md:62] Industry fit varies by construction project complexity:

**High Fit:**
- Single family residential
- Multi-family residential
- Small commercial projects

**Lower Fit:**
- Large industrial projects (complexity beyond ICP scope)

## Context Lineage

**Source Documents:**
- `knowledge_base/raw_context/ICP Summary & Use Cases.md` (lines 56-62)
  - Unique value: Building materials as primary vertical across all tiers, construction project type specifications

- `knowledge_base/raw_context/strategic_lens.yaml` (lines 456-487, 629-632)
  - Unique value: Secondary verticals with strategic fit weights, ICP signal keywords, sub-segment granularity

- `knowledge_base/raw_context/Classification Prompts.md` (lines 76-83)
  - Unique value: ICP industry definitions for classification, keyword signals for automated qualification

**Dimensional Mapping:**
- WHO dimension: Industry-based persona segmentation → [strategic_lens.yaml:456-487]
- WHAT dimension: Industry-specific pain points and use cases → [strategic_lens.yaml:639-702]
- Strategic fit weight: Industry match is 25% of composite strategic_fit score

## Transcript Validation

**Validation signals:** (will be added as transcripts process)
- [ ] **Industry frequency:** Count of transcripts by vertical (Building Materials vs. Construction vs. Manufacturing vs. Others)
- [ ] **Sub-segment patterns:** Which specific sub-segments appear most often
- [ ] **Conversion rates:** Do primary verticals (Building Materials) convert better than secondary?
- [ ] **Retention by vertical:** Does LIR (50% receivables) vary by industry?
- [ ] **Project type validation:** Confirm single/multi-family and small commercial dominance
- [ ] **Signal keyword accuracy:** Do high-priority keywords correlate with high-fit customers?

**Status progression:**
- baseline → validating (after 1st transcript confirms vertical patterns)
- validating → validated (after 2nd+ transcripts show repeatable industry clustering)
- validated → canonical (after 5th+ transcripts with quantified conversion/retention by vertical)

**Expected evolution:**
- Primary vertical may expand beyond Building Materials if other verticals show equal LIR performance
- Sub-segment priorities may be refined based on conversion and deal velocity data
- Strategic fit weights may adjust based on actual win rates and customer lifetime value
- New verticals may emerge as ICP-fit if they exhibit similar transaction profiles and pain points
