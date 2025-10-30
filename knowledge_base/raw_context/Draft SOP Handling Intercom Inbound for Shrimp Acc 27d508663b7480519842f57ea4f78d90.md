---
document_type: process_doc
date: 2025-10-30
author: Colton O'Farrell
source: internal_doc

topics:
  - customer_success
  - sales_operations

signal_strength: low

contains_icp: true
contains_metrics: false
contains_competitive: false
contains_customer_evidence: false

file_size: 1.8K
processed: false
lens_extracted: false
---

# Draft: SOP: Handling Intercom Inbound for Shrimp Accounts (<$1M Revenue)

Area: ☎️ Support
Owner: Colton O'Farrell
Status: Not started

## **1. Entry Point**

- Customer initiates via Intercom Help Center.
- They choose one of four options:
    1. Transaction status
    2. General help
    3. Plaid/bank linking issue
    4. Account problem

## **2. Initial Triage (Automated or Manual)**

- **Pending / RFI accounts:** Will to handle (fraud-sensitive).
- **Approved accounts:** Route based on category (below).
- *Fin AI fit:* Drafts initial reply acknowledging request, suggests next steps, surfaces KB links.
- Tag accounts based on what type of inquiry / support it is so we can start pulling data rather than one-off customer stories

## **3. Routing Rules for Shrimp Accounts**

- **Transaction status** →
    - CSM first; otherwise Will checks via Retool.
    - Template-driven updates only. No deep-dive escalation unless flagged.
- **General help** →
    - CSM responds first-pass using macro responses.
- **Plaid/bank linking** →
    - Will troubleshoots via standard checklist.
    - Escalate to engineers (Claudio/Najeer) only if Plaid API failure or bug reproduction.
- **Account problem** →
    - Will screens. If simple (name change, accountant vs business, status lookup): he tags CSM to use Retool.
    - If higher-touch but low-revenue: resolve via macro.
    - If systemic bug → engineer.

## **4. Escalation Thresholds**

- Only escalate Shrimp accounts if:
    1. Reproducible technical bug
    2. Compliance/fraud risk
    3. Strategic signal (e.g., potential to grow beyond Shrimp tier)
    

Additional variables to consider:

- Process for when someone is out of office
- Process for when someone is tied up in meetings