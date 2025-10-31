# Frontmatter Cleanup - Agent Batch Assignments

**Created:** 2025-10-30
**Purpose:** Track which cleanup agent handles which transcript batches
**Total Transcripts:** 165
**Total Cleanup Agents:** 6
**Avg Batch Size:** 27.5 transcripts per agent

---

## Agent Architecture

### Batch Size Rationale

**Token Economics:**
- Full transcript: ~6,780 tokens (too expensive)
- Frontmatter + first 100 lines: ~1,500 tokens (sufficient for sanity check)
- Output per transcript: ~500 tokens
- **Total per transcript: ~2,000 tokens**

**Per Agent:**
- 30 transcripts × 2,000 tokens = ~60K tokens
- Agent instructions: ~10K tokens
- **Total per agent: ~70K tokens** (well within 200K limit)
- Estimated time: 5-7 minutes per agent

**Parallelization:**
- 6 agents running simultaneously
- Wall-clock time: ~7 minutes
- Total cost: ~$0.60 (Sonnet for accuracy)

---

## Agent Assignments

### Agent 1: Batches 1-3 (30 transcripts)

**Original Batches:** batch_01, batch_02, batch_03

**Transcripts:**
```
001_abbas-rezaei-and-colton-ofarrell_2025-07-15.md
002_erik-meza-and-colton-ofarrell_2025-07-15.md
003_prime-renovations-ny-nickel_2025-07-23.md
004_carson-crawford-and-colton-ofarrell_2025-08-14.md
005_prime-renovations-ny-nickel_2025-07-23.md
006_erik-meza-and-colton-ofarrell_2025-07-15.md
007_frank-delbrouck-and-colton-ofarrell_2025-08-19.md
008_hardy-butler-and-colton-ofarrell_2025-07-23.md
009_ashland-roofing-nickel-2nd-review-call_2025-09-25.md
010_amps-facility-solutions-nickel-kickoff-call_2025-09-29.md
011_american-home-renewal-inc-nickel_2025-07-18.md
012_matthew-and-colton-ofarrell_2025-08-20.md
013_jay-omanson-and-colton-ofarrell_2025-08-12.md
014_brandon-rogers-and-colton-ofarrell_2025-07-14.md
015_hassan-colton-nickel_2025-07-31.md
016_conner-rusch-and-colton-ofarrell_2025-07-18.md
017_sharika-and-colton-ofarrell_2025-08-13.md
018_ramon-j-otero-and-colton-ofarrell_2025-07-31.md
019_peter-trang-and-colton-ofarrell_2025-08-01.md
020_david-berry-and-colton-ofarrell_2025-07-22.md
021_ashland-roofing-nickel-kickoff-call_2025-09-18.md
022_steve-goldstein-and-colton-ofarrell_2025-07-30.md
023_joan-schafer-and-colton-ofarrell_2025-08-25.md
024_emma-benson-and-colton-ofarrell_2025-07-23.md
025_david-kruyswijk-and-colton-ofarrell_2025-07-15.md
026_kab-consulting-inc-nickel-kick-off-call_2025-09-10.md
027_brent-rose-and-colton-ofarrell_2025-07-21.md
028_abbas-rezaei-and-colton-ofarrell_2025-07-15.md
029_deshyra-hubbard-and-colton-ofarrell_2025-07-24.md
030_brandon-kopp-and-colton-ofarrell_2025-08-05.md
```

**Output File:** `_AGENT_WORKSPACE/cleanup_reports/agent_01_report.md`

---

### Agent 2: Batches 4-6 (30 transcripts)

**Original Batches:** batch_04, batch_05, batch_06

**Transcripts:**
```
031_shaneque-downie-and-colton-ofarrell_2025-09-04.md
032_homes-by-triple-m-nickel-kickoff-call_2025-09-16.md
033_michael-mann-and-colton-ofarrell_2025-07-30.md
034_ashley-melton-and-colton-ofarrell_2025-07-29.md
035_belmont-custom-remodeling-llc-nickel-kickoff-call_2025-09-18.md
036_mark-hull-and-colton-ofarrell_2025-08-18.md
037_kumon-of-draper-nickel-kickoff-call_2025-09-24.md
038_marc-colton-nickel-follow-up_2025-07-28.md
039_capris-keller-and-colton-ofarrell_2025-07-14.md
040_ecogate-nickel_2025-08-28.md
041_jeff-colton-nickel-follow-up_2025-07-31.md
042_marc-stelzer-and-colton-ofarrell_2025-08-20.md
043_dan-sizelove-and-colton-ofarrell_2025-07-24.md
044_kevin-redmon-and-colton-ofarrell_2025-08-06.md
045_mateo-vosganian-and-colton-ofarrell_2025-08-13.md
046_nickel-archadeck-review-call_2025-08-21.md
047_billy-siegler-and-colton-ofarrell_2025-07-16.md
048_american-home-renewal-inc-nickel_2025-08-28.md
049_peter-trang-and-colton-ofarrell_2025-08-20.md
050_us-national-steel-nickel-kickoff-call_2025-09-11.md
051_debbie-bechtel-and-colton-ofarrell_2025-08-01.md
052_oscar-ob-garden-and-tina-boundless-data-colton-nic_2025-07-24.md
053_vinay-shah-and-colton-ofarrell_2025-08-15.md
054_mike-lovelady-and-colton-ofarrell_2025-08-09.md
055_vijaya-kumar-and-colton-ofarrell_2025-08-12.md
056_jordan-stealey-and-colton-ofarrell_2025-08-14.md
057_chris-sneed-and-colton-ofarrell_2025-08-21.md
058_abel-richard-and-colton-ofarrell_2025-08-23.md
059_patricia-zavala-and-colton-ofarrell_2025-08-26.md
060_jagadish-sudarsanam-and-colton-ofarrell_2025-08-29.md
```

**Output File:** `_AGENT_WORKSPACE/cleanup_reports/agent_02_report.md`

---

### Agent 3: Batches 7-9 (30 transcripts)

**Original Batches:** batch_07, batch_08, batch_09

**Transcripts:**
```
061_pavt-nickel-reconnect-check-in_2025-08-29.md
062_andrea-kladder-and-christian-sheerer_2025-10-06.md
063_nickel-beyondpulse-demo-walkthrough_2025-08-19.md
064_penny-guilinger-and-jacob-greenberg_2025-10-07.md
065_nickel-demo-hailey-bennett_2025-09-03.md
066_mark-moore-and-jacob-greenberg_2025-09-17.md
067_nickel-demo-ravi-patel_2025-09-18.md
068_nickel-platform-demo-cameron-cox_2025-09-09.md
069_john-rios-and-jacob-greenberg_2025-09-25.md
070_digital-marketing-group-nickel_2025-09-03.md
071_archadeck-x-nickel-discovery-call_2025-08-13.md
072_andrew-campbell-and-jacob-greenberg_2025-08-27.md
073_kush-shah-and-jacob-greenberg_2025-08-28.md
074_betram-hamilton-and-jacob-greenberg_2025-09-04.md
075_wayland-church-x-nickel_2025-10-08.md
076_spyro-katsianis-and-jacob-greenberg_2025-09-11.md
077_nickel-archadeck-utah-kickoff-call_2025-09-22.md
078_sean-weiner-and-jacob-greenberg_2025-09-16.md
079_todd-cornwall-and-jacob-greenberg_2025-09-18.md
080_nickel-demo-request-jeff-thibodeau_2025-09-25.md
081_nickel-archadeck-utah-reconnect_2025-10-04.md
082_nickel-demo-request-rotary-club_2025-09-26.md
083_kr-taxes-nickel-check-in_2025-09-13.md
084_spectraflow-x-nickel-review-call_2025-09-23.md
085_andrea-bergstrom-and-jacob-greenberg_2025-09-30.md
086_alliance-home-care-nickel-eom-check-in_2025-09-30.md
087_surgenex-nickel-reconnect-call_2025-10-01.md
088_shelbi-and-jacob-greenberg_2025-10-02.md
089_alliance-home-care-nickel-tiffany-check-in_2025-10-03.md
090_surgenex-nickel-first-transaction-call_2025-10-01.md
```

**Output File:** `_AGENT_WORKSPACE/cleanup_reports/agent_03_report.md`

---

### Agent 4: Batches 10-12 (30 transcripts)

**Original Batches:** batch_10, batch_11, batch_12

**Transcripts:**
```
091_nickel-demo-request-shannon-rayman_2025-10-08.md
092_nickel-platform-demo-kristen-ott_2025-10-09.md
093_nickel-demo-request-vip-software_2025-09-30.md
094_nickel-platform-demo-christopher-lewis_2025-10-09.md
095_aurelie-nguyen-and-jacob-greenberg_2025-10-10.md
096_nickel-demo-request-martin-sealey_2025-10-10.md
097_nickel-demo-joel-edwards_2025-10-09.md
098_nickel-demo-request-gary-porter_2025-10-10.md
099_keith-brown-and-jacob-greenberg_2025-10-10.md
100_christian-ashley-nickel-str-management_2025-10-02.md
101_nickel-demo-terry-bates_2025-10-04.md
102_thomas-colton-and-jacob-greenberg_2025-10-13.md
103_charles-stafford-and-jacob-greenberg_2025-10-14.md
104_justin-clark-and-jacob-greenberg_2025-10-13.md
105_nickel-demo-request-robert-west_2025-10-10.md
106_teresa-shaver-and-jacob-greenberg_2025-10-14.md
107_nickel-demo-christina-ortiz_2025-10-11.md
108_amanda-pettay-and-jacob-greenberg_2025-10-15.md
109_byron-floyd-and-jacob-greenberg_2025-10-15.md
110_ryan-jacob-and-jacob-greenberg_2025-10-14.md
111_daniel-power-and-jacob-greenberg_2025-10-15.md
112_john-lheureux-and-jacob-greenberg_2025-10-15.md
113_tiffany-smith-and-jacob-greenberg_2025-10-17.md
114_nickel-demo-sikama-international_2025-10-15.md
115_mary-catherine-and-jacob-greenberg_2025-10-16.md
116_huntington-bank-nickel-meeting_2025-10-16.md
117_sam-adams-and-jacob-greenberg_2025-10-17.md
118_herchel-biddy-and-jacob-greenberg_2025-10-18.md
119_deborah-roofing-contractors-nickel_2025-10-15.md
120_nickel-demo-request-anna-reynolds_2025-10-17.md
```

**Output File:** `_AGENT_WORKSPACE/cleanup_reports/agent_04_report.md`

---

### Agent 5: Batches 13-15 (30 transcripts)

**Original Batches:** batch_13, batch_14, batch_15

**Transcripts:**
```
121_jared-williams-and-jacob-greenberg_2025-10-18.md
122_christian-taylor-and-jacob-greenberg_2025-10-18.md
123_crazy-candy-factory-nickel-review_2025-10-14.md
124_luke-and-jacob-greenberg_2025-10-20.md
125_felipe-and-jacob-greenberg_2025-10-20.md
126_natalie-x-nickel_2025-08-20.md
127_nickel-demo-saad-rangoonwala_2025-08-27.md
128_maria-x-nickel_2025-10-03.md
129_nickel-true-course-xero-integration_2025-10-07.md
130_nickel-demo-darah-smith_2025-09-05.md
131_dipping-dots-x-nickel_2025-09-18.md
132_sierra-club-x-nickel_2025-10-07.md
133_alaska-wholesale-llc-matthew-fischer_2025-09-03.md
134_nickel-platform-demo-mitesh-bhagat_2025-10-08.md
135_ellen-moser-and-jacob-greenberg_2025-07-30.md
136_nickel-mark-hull-jacob_2025-09-23.md
137_nickel-demo-didier-garcia_2025-09-02.md
138_nickel-x-dual-temp-review_2025-08-26.md
139_nickel-demo-request-robert-stern_2025-09-11.md
140_nickel-demo-request-kayla-rakes_2025-09-09.md
141_nickel-arachdeck-utah_2025-09-29.md
142_laura-golnabi-and-jacob-greenberg_2025-08-25.md
143_nickel-demo-request-margarita-iruela_2025-09-12.md
144_nickel-demo-request-lyle-brand_2025-10-03.md
145_nickel-demo-request-nathaniel-seekins_2025-09-23.md
146_nickel-demo-request-tasvir-mirza_2025-09-30.md
147_nickel-demo-request-andy-haines_2025-09-17.md
148_nickel-demo-request-jacob-sung_2025-10-01.md
149_nickel-demo-request-roby-fitzhenry_2025-10-06.md
150_nickel-weaver_2025-09-18.md
```

**Output File:** `_AGENT_WORKSPACE/cleanup_reports/agent_05_report.md`

---

### Agent 6: Batches 16-17 (15 transcripts)

**Original Batches:** batch_16, batch_17

**Transcripts:**
```
151_nickel-demo-request-erica-rogers_2025-10-22.md
152_kurt-nickel-demo_2025-09-26.md
153_nickel-platform-demo-jay-johnson_2025-09-17.md
154_matt-bartini-and-jacob-greenberg_2025-09-25.md
155_nickel-demo-rachel-steininger_2025-09-08.md
156_commercial-c-group-nickel_2025-09-22.md
157_nickel-rig-roofing_2025-10-07.md
158_daniel-goodwin-and-jacob-greenberg_2025-08-14.md
159_nickel-platform-demo-william-grantsynn_2025-09-25.md
160_nickel-demo-request-keith-shackleford_2025-09-29.md
161_nickel-demo-request-dan-ross_2025-09-12.md
162_nickel-demo-request-darren-nye_2025-09-30.md
163_carey-x-nickel_2025-09-09.md
164_gex-nickel_2025-10-22.md
165_zak-cj_2025-10-23.md
```

**Output File:** `_AGENT_WORKSPACE/cleanup_reports/agent_06_report.md`

---

## Execution Plan

### Step 1: Create Output Directory
```bash
mkdir -p _AGENT_WORKSPACE/cleanup_reports
```

### Step 2: Spawn Agents in Parallel

Launch all 6 agents simultaneously with their assignments:
- Each agent reads FRONTMATTER_CLEANUP_AGENT.md for instructions
- Each agent gets their specific transcript list
- Each agent outputs to their designated report file

### Step 3: Monitor Completion

Track which agents have completed:
- [ ] Agent 1 (Batches 1-3) - 30 transcripts
- [ ] Agent 2 (Batches 4-6) - 30 transcripts
- [ ] Agent 3 (Batches 7-9) - 30 transcripts
- [ ] Agent 4 (Batches 10-12) - 30 transcripts
- [ ] Agent 5 (Batches 13-15) - 30 transcripts
- [ ] Agent 6 (Batches 16-17) - 15 transcripts

### Step 4: Aggregate Results

Once all agents complete:
- Review all 6 report files
- Aggregate statistics
- Identify any critical issues
- Generate final cleanup summary

---

## Success Criteria

**Cleanup is successful if:**
- ✅ All 165 transcripts have exactly ONE strategic classification block
- ✅ All 165 transcripts have valid YAML structure
- ✅ 90%+ pass sanity checks
- ✅ Any critical issues flagged for re-processing

**Cleanup is NOT successful if:**
- ❌ Files still have duplicate blocks
- ❌ YAML is malformed
- ❌ >10% of classifications obviously wrong
- ❌ Significant number of files missing classification

---

**Created:** 2025-10-30
**Status:** Ready for execution
**Total Wall-Clock Time:** ~7 minutes (parallel execution)
**Total Cost:** ~$0.60 (6 Sonnet agents)
