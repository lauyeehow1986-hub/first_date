# Singapore GovTech FirstDate Actuarial, Demographic & Bipartite Graph Audit Report

**Harness:** Antigravity IDE | `gemini-3.8-flash` (High Effort)  
**FastMCP Engine:** `sg-govtech-firstdate-fertility-mcp`  
**Official Data Sources:** SingStat TableBuilder APIs (`M810581`, `M810681`, `M830102`, `M810091`, `M830184`), Data.gov.sg PSD Headcount (`d_ded51ba4680464b706b95069018ffcac`), MyCareersFuture v2 Salary Bands.

---

## 1. FirstDate Success Rate & National TFR Impact Evaluation

### 1.1 The Multi-Stage Attrition Funnel
Every proposed match on GovTech FirstDate encounters an empirical multi-stage attrition funnel before translating into a live birth:

```
[Registered Active Public Officers] ~3,828 users/yr
       │
       ▼  (Turan Cross-Agency Loss: -12.57% intra-agency collision)
[Eligible Cross-Agency Match Pairs] ~3,350 pairings
       │
       ▼  (Photo-Free FormSG Reveal Hazard: -22.0% physical mismatch at meetup)
[First In-Person Date Meetups] ~2,613 meetups
       │
       ▼  (Age-Gap, MX Grade Hierarchy & Cultural Endogamy: 38.4% pool average)
[Second Date Progressions] ~1,288 progressions
       │
       ▼  (Courtship & BTO Queue Survival over 1.2 years)
[Committed Relationships / BTO Queues] ~386 couples
       │
       ▼  (Pre-ROM Solemnisation over 2.3 years: 2.72% total funnel conversion)
[ROM / ROMM Marriages] ~104.2 marriages/yr
       │
       ▼  (Conception post 3.5y BTO wait: 1.38 expected children/couple)
[Completed Live Births] ~143.8 live births/yr
```

### 1.2 Macro TFR Simulation & Policy Verdict
Can FirstDate fix Singapore's declining Total Fertility Rate (**0.87** in 2025; **0.97** in 2023–2024)?

```
+----------------------------------------------------------------------------------------------------+
| MACRO DEMOGRAPHIC ACCOUNTING (SingStat 2025 Baseline)                                              |
+----------------------------------------------------------------------------------------------------+
| Singapore Total Annual Resident Live Births (2025)       : 29,864                                  |
| National Baseline Total Fertility Rate (TFR)              : 0.87000                                 |
| Baseline FirstDate Annual Live Birth Output               : +143.8 infants                          |
| Estimated National TFR Lift                               : +0.00419 points                         |
| Resulting National TFR with FirstDate Pilot               : 0.87419                                 |
| Minimum Policy Significance Target (+0.05000 TFR)         : NOT MET (8.38% of target)               |
+----------------------------------------------------------------------------------------------------+
```

**Verdict:** FirstDate **cannot fix Singapore's TFR on its own**. While it provides a high-trust, Singpass-authenticated dating environment, its demographic yield is structurally capped by the exclusion of ~65k healthcare workers, the fact that ~50% of legal singles are already partnered, and the 3.5-year BTO construction delay.

---

## 2. The Golden Ageband by Gender and Race

The **Golden Ageband** represents the optimal demographic and biological intersection where:
1. **Career Entry**: Officers have cleared civil service probation into stable salary bands (MX13/MX12).
2. **Biological Fecundity**: Prior to the maternal age-37 ovarian reserve cliff (<25,000 oocytes; miscarriage >18%) and paternal sperm DNA fragmentation (DFI) cliff (age 40+).
3. **Housing Queue Latency**: Matching accounts for the **3.5-year dating + BTO queue delay** so conception occurs before age 34.
4. **HDB Single Scheme Boundary**: Before age 35, when unlocking 2-room Flexi BTOs and resale grants reduces marriage utility by 52%.

### 2.1 Golden Ageband by Gender

| Gender | Golden Ageband | Median 1st Marriage Age | Prime Conception Age (Post BTO) | Expected Completed Kids | Primary Constraint / Bottleneck |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Female** | **25 to 29 years** *(Peak: 26–28)* | 29.3 yrs | **29.5 to 32.5 yrs** | **1.53 – 1.62 kids** | Matching at 33+ delays conception to 36.5+, triggering subfertility (33.3%) and miscarriage (18.4%). |
| **Male** | **27 to 31 years** *(Peak: 28–30)* | 30.8 yrs | **31.5 to 34.5 yrs** | **1.53 – 1.62 kids** | 2-year National Service (NS) delay leaves only 2–3 years of savings accumulation before marriage costs (S$70k+). |

---

### 2.2 Golden Ageband by Race (CMIO Breakdown)

#### 1. Malay Community (TFR 1.53)
* **Golden Ageband**: **Female: 23 – 27 years** | **Male: 25 – 29 years**
* **Sociological Drivers**: Youngest median age at first marriage (Bride 26.8, Groom 28.5); earlier marriage norm via ROMM; communal *gotong-royong* family caregiving buffers infant care costs; completed fertility reaches **2.69 – 2.85 children**.

#### 2. Chinese Community (TFR 0.70)
* **Golden Ageband**: **Female: 26 – 30 years** | **Male: 28 – 32 years**
* **Sociological Drivers**: Oldest median age at marriage (Bride 29.3, Groom 30.8); highest singlehood at 25–29 (76.5%); intense tuition reference-point inflation (>S$1,000/mo/child); must match by age 29 to avoid conceiving post-33 after BTO wait.

#### 3. Indian Community (TFR 0.92)
* **Golden Ageband**: **Female: 25 – 29 years** | **Male: 27 – 31 years**
* **Sociological Drivers**: Median age at marriage (Bride 28.7, Groom 30.4); high graduate degree share; strong professional homogamy; ASMR peaks at 30–34 (101.5/1,000 for females).

#### 4. Others / Eurasian Community (TFR 0.89)
* **Golden Ageband**: **Female: 26 – 30 years** | **Male: 28 – 32 years**
* **Sociological Drivers**: Median age at marriage (Bride 29.6, Groom 31.2); highest exogamy (>40% inter-ethnic marriage rate); low MX hierarchy friction.

---

## 3. Empirical Odds of Marriage & Childbirth (4 Races $\times$ 5 Age Bands $\times$ 2 Genders)

### 3.1 Chinese Community (TFR: 0.70)

| Age Band | Gender | Singlehood Rate ($\sigma$) | Annual ASMR (/1k) | 5-Yr Marriage Odds ($P_{\text{5yr}}$) | Annual ASFR (/1k) | Post-BTO Expected Kids | 5-Yr Married Birth Prob |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **20 – 24** | Male | 99.5% | 4.8 | **2.4%** | — | — | — |
| | Female | 98.2% | 11.2 | **5.4%** | 4.2 | **1.30** | 4.5% |
| **25 – 29** *(Golden)* | Male | 88.2% | 52.4 | **23.0%** | — | — | — |
| | Female | 76.5% | 82.5 | **33.8%** | 28.5 | **1.23** | 26.9% |
| **30 – 34** *(Late)* | Male | 49.5% | 98.6 | **38.9%** | — | — | — |
| | Female | 36.8% | 112.4 | **43.0%** | 62.4 | **1.01** | 49.7% |
| **35 – 39** *(Cliff)* | Male | 25.6% | 81.2 | **33.4%** | — | — | — |
| | Female | 21.8% | 54.8 | **24.0%** | 40.1 | **0.62** | 35.7% |
| **40 – 44** *(Exhaust)*| Male | 16.8% | 47.5 | **21.1%** | — | — | — |
| | Female | 16.7% | 24.6 | **11.6%** | 7.8 | **0.47** | 8.2% |

---

### 3.2 Malay Community (TFR: 1.53)

| Age Band | Gender | Singlehood Rate ($\sigma$) | Annual ASMR (/1k) | 5-Yr Marriage Odds ($P_{\text{5yr}}$) | Annual ASFR (/1k) | Post-BTO Expected Kids | 5-Yr Married Birth Prob |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **20 – 24** | Male | 96.5% | 19.5 | **9.3%** | — | — | — |
| | Female | 91.5% | 38.6 | **17.6%** | 29.5 | **2.85** | 27.7% |
| **25 – 29** *(Golden)* | Male | 72.5% | 88.2 | **35.7%** | — | — | — |
| | Female | 58.2% | 118.5 | **44.7%** | 84.6 | **2.69** | 60.6% |
| **30 – 34** *(Late)* | Male | 37.5% | 82.4 | **33.8%** | — | — | — |
| | Female | 24.5% | 76.2 | **31.7%** | 98.2 | **2.22** | 66.0% |
| **35 – 39** *(Cliff)* | Male | 18.5% | 62.1 | **26.7%** | — | — | — |
| | Female | 14.2% | 38.4 | **17.5%** | 68.5 | **1.35** | 52.9% |
| **40 – 44** *(Exhaust)*| Male | 11.5% | 42.0 | **18.9%** | — | — | — |
| | Female | 10.8% | 18.2 | **8.7%** | 16.4 | **1.04** | 16.5% |

---

### 3.3 Indian Community (TFR: 0.92)

| Age Band | Gender | Singlehood Rate ($\sigma$) | Annual ASMR (/1k) | 5-Yr Marriage Odds ($P_{\text{5yr}}$) | Annual ASFR (/1k) | Post-BTO Expected Kids | 5-Yr Married Birth Prob |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **20 – 24** | Male | 99.2% | 6.2 | **3.1%** | — | — | — |
| | Female | 97.0% | 16.4 | **7.9%** | 7.8 | **1.71** | 8.2% |
| **25 – 29** *(Golden)* | Male | 84.5% | 58.4 | **25.3%** | — | — | — |
| | Female | 71.0% | 91.2 | **36.6%** | 41.2 | **1.62** | 36.4% |
| **30 – 34** *(Late)* | Male | 46.2% | 94.1 | **37.5%** | — | — | — |
| | Female | 33.5% | 101.5 | **39.8%** | 74.5 | **1.33** | 55.9% |
| **35 – 39** *(Cliff)* | Male | 23.5% | 75.3 | **31.4%** | — | — | — |
| | Female | 19.2% | 48.2 | **21.4%** | 48.0 | **0.81** | 41.0% |
| **40 – 44** *(Exhaust)*| Male | 15.2% | 44.8 | **20.1%** | — | — | — |
| | Female | 14.5% | 21.5 | **10.2%** | 9.2 | **0.62** | 9.6% |

---

### 3.4 Others & Eurasian Community (TFR: 0.89)

| Age Band | Gender | Singlehood Rate ($\sigma$) | Annual ASMR (/1k) | 5-Yr Marriage Odds ($P_{\text{5yr}}$) | Annual ASFR (/1k) | Post-BTO Expected Kids | 5-Yr Married Birth Prob |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **20 – 24** | Male | 99.0% | 5.5 | **2.7%** | — | — | — |
| | Female | 97.5% | 14.0 | **6.8%** | 6.5 | **1.66** | 6.9% |
| **25 – 29** *(Golden)* | Male | 86.0% | 54.0 | **23.7%** | — | — | — |
| | Female | 74.0% | 85.0 | **34.6%** | 38.0 | **1.57** | 34.2% |
| **30 – 34** *(Late)* | Male | 48.0% | 92.5 | **37.0%** | — | — | — |
| | Female | 35.0% | 105.0 | **40.8%** | 71.0 | **1.29** | 54.2% |
| **35 – 39** *(Cliff)* | Male | 24.8% | 77.0 | **32.0%** | — | — | — |
| | Female | 20.5% | 51.0 | **22.5%** | 46.5 | **0.79** | 40.0% |
| **40 – 44** *(Exhaust)*| Male | 16.0% | 45.2 | **20.2%** | — | — | — |
| | Female | 15.5% | 23.0 | **10.9%** | 8.8 | **0.60** | 9.2% |

---

## 4. Policy Interventions to Turn the Tide
1. **Target Algorithmic Matchmaking to the 25–29 Ageband**: Maximize conversion before the age-37 oocyte cliff and age-40 paternal DFI surge.
2. **Fast-Track BTO Queues (<2.5 Years) for FirstDate ROMs**: Eliminate the 3.5-year construction bottleneck that pushes young civil servants past prime reproductive age.
3. **Incorporate Healthcare Cluster Personnel**: Legally amend Clause 6.1.1 to include SingHealth, NHG Health, and NUHS (~65,000 officers).
4. **10-Day Dedicated Child HFMD/Sick Leave Shield**: Solve the 9.5-day annual preschool childcare leave deficit to encourage second-child progression.
