---
document_type: operational_guide
date: 2025-10-30
author: Najeer Ahmed
source: internal_doc

topics:
  - team_operations
  - product_strategy

signal_strength: low

contains_icp: false
contains_metrics: false
contains_competitive: false
contains_customer_evidence: false

file_size: 1.5K
processed: false
lens_extracted: false
---

# Fraud Prevention / Risk Rules

Area: 🤖 Engineering
Owner: Najeer Ahmed
Status: Outdated
Type: How-To

Registration:

- Require SSN, EIN, Domain (covered by Alloy)
- Require Plaid for all businesses → If no plaid, case-by-case basis (3 months bank statements etc.)
- Suggestions to address account takeover fraud
    - Require a copy of ID from the business owner
    - Manually call the business to confirm before we approve the account (optional, high value accounts)

AP:

- Require Plaid for all payment method → Same as no plaid registration
- Check balance on every AP payment
- Ensure a valid email on the recipient

AR:

- If payout bank account balance is not 2-3x greater than incoming payment, then slow down payout.
- If incoming payment is more than $X dollars, then require plaid for ACH
- Potentially use a bank account validation service
- Valid customer emails for AR (accept gmail due to consumer end-users)

Future:

- Start building out the data/labels/etc. for a risk model