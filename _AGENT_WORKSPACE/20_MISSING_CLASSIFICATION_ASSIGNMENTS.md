# Missing Classification Agent Assignments

**Date:** 2025-10-30
**Total Missing:** 44 files (26.7% of corpus)
**Root Cause:** Original Haiku classification agents (batches 8, 9, 10, 11, 14, 16) failed to process these files

---

## Affected Batches (Original)

| Original Batch | Files Should Cover | Files Actually Missing | Failure Rate |
|----------------|-------------------|----------------------|--------------|
| Batch 8 | 071-080 | 072, 073, 077, 078 | 40% |
| Batch 9 | 081-090 | 081, 082, 084-090 | 90% |
| Batch 10 | 091-100 | 100 | 10% |
| Batch 11 | 101-110 | 101-110 | **100%** |
| Batch 14 | 131-140 | 131-140 | **100%** |
| Batch 16 | 151-160 | 151-160 | **100%** |

---

## New Agent Assignments

### Agent A (Missing Batch A) - 14 files
**Original Coverage:** Partial batches 8, 9, 10
**Files:**
1. 072_nickel-for-surgenex-reconnectfinalize_2025-10-14.md
2. 073_nickel-demo-request-andrew-campbell_2025-09-23.md
3. 077_kush-shah-and-jacob-greenberg_2025-08-15.md
4. 078_todd-cornwall-and-christian-sheerer_2025-08-07.md
5. 081_nickel-archadeck-of-central-maine-christian-pj_2025-08-25.md
6. 082_nickel-for-rotary-check-in_2025-08-29.md
7. 084_spectraflow-nickel-check-in-rollout-plan_2025-08-22.md
8. 085_nickel-demo-request-andrea-bergstrom_2025-09-09.md
9. 086_nickel-for-alliance-homecare-eom-check-in_2025-10-09.md
10. 087_nickel-for-surgenex-reconnect-check-in_2025-10-07.md
11. 088_shelbi-and-christian-sheerer_2025-08-27.md
12. 089_nickel-for-alliance-homecare-tiffany-christian-che_2025-09-25.md
13. 090_nickel-for-surgenex-christian-alex-send-out-first-_2025-10-14.md
14. 100_christian-ashley-nickel-str-management-check-in_2025-10-02.md

**Model:** Haiku (cost-effective classification)
**Expected Time:** 2-3 minutes
**Expected Cost:** ~$0.02

---

### Agent B (Missing Batch B) - 10 files
**Original Coverage:** Complete batch 11 failure
**Files:**
1. 101_nickel-demo-request-deborah-enriquez_2025-09-10.md
2. 102_nickel-demo-request-jason-molaison_2025-09-10.md
3. 103_nickel-platform-demo-charles-stafford_2025-10-16.md
4. 104_nickel-demo-sterling-chipman_2025-08-29.md
5. 105_nickel-for-blue-hills-at-round-top_2025-09-24.md
6. 106_nickel-demo-request-thanmay-kumar_2025-09-30.md
7. 107_nickel-demo-request-lyle-applbaum_2025-09-26.md
8. 108_nickel-demo-request-amanda-pettay_2025-10-16.md
9. 109_nickel-demo-request-byron-floyd_2025-09-29.md
10. 110_nickel-demo-request-ryan-jacob_2025-09-22.md

**Model:** Haiku
**Expected Time:** 2-3 minutes
**Expected Cost:** ~$0.015

---

### Agent C (Missing Batch C) - 10 files
**Original Coverage:** Complete batch 14 failure
**Files:**
1. 131_dipping-dots-x-nickel_2025-09-18.md
2. 132_sierra-club-x-nickel_2025-10-07.md
3. 133_alaska-wholesale-llc-matthew-fischer_2025-09-03.md
4. 134_nickel-platform-demo-mitesh-bhagat_2025-10-08.md
5. 135_ellen-moser-and-jacob-greenberg_2025-07-30.md
6. 136_nickel-mark-hull-jacob_2025-09-23.md
7. 137_nickel-demo-didier-garcia_2025-09-02.md
8. 138_nickel-x-dual-temp-review_2025-08-26.md
9. 139_nickel-demo-request-robert-stern_2025-09-11.md
10. 140_nickel-demo-request-kayla-rakes_2025-09-09.md

**Model:** Haiku
**Expected Time:** 2-3 minutes
**Expected Cost:** ~$0.015

---

### Agent D (Missing Batch D) - 10 files
**Original Coverage:** Complete batch 16 failure
**Files:**
1. 151_nickel-demo-request-erica-rogers_2025-10-22.md
2. 152_kurt-nickel-demo_2025-09-26.md
3. 153_nickel-platform-demo-jay-johnson_2025-09-17.md
4. 154_matt-bartini-and-jacob-greenberg_2025-09-25.md
5. 155_nickel-demo-rachel-steininger_2025-09-08.md
6. 156_commercial-c-group-nickel_2025-09-22.md
7. 157_nickel-rig-roofing_2025-10-07.md
8. 158_daniel-goodwin-and-jacob-greenberg_2025-08-14.md
9. 159_nickel-platform-demo-william-grantsynn_2025-09-25.md
10. 160_nickel-demo-request-keith-shackleford_2025-09-29.md

**Model:** Haiku
**Expected Time:** 2-3 minutes
**Expected Cost:** ~$0.015

---

## Summary

**Total Agents:** 4 parallel Haiku classification agents
**Total Files:** 44 missing classifications
**Total Expected Time:** ~3 minutes (parallel execution)
**Total Expected Cost:** ~$0.065

---

## Execution Plan

1. ✅ Create batch manifest files (batch_missing_A/B/C/D.txt)
2. Launch 4 parallel Haiku agents with TRANSCRIPT_CLASSIFIER_AGENT.md
3. Monitor completion
4. Parse results and merge into transcript files using Edit tool (NOT merge script)
5. Validate all 44 files now have strategic classification
6. Update FRONTMATTER_CLEANUP_COMPLETE.md with final status

---

**Status:** Ready to execute
**Date Created:** 2025-10-30
