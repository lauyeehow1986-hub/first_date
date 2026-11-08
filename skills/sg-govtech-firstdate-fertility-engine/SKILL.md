---
name: sg-govtech-firstdate-fertility-engine
description: Simulate and audit Singapore government matchmaking schemes (GovTech FirstDate), public officer marriage and childbirth conversion funnels, cross-agency Gale-Shapley multipartite graph matching, age-gap and MX-grade rejection matrices, HDB Single Citizen age-35 lock-in vs couple housing utility, full 0-22y child cost commitment vs Baby Bonus and 30-week parental leave offsets, clinical infertility and miscarriage hazards, and URA Planning Area/Subzone socio-economic GIS effects. Use whenever analyzing Singapore dating apps, marriage/divorce rates, TFR policy interventions, public sector demographics, or building Antigravity Gemini 3.8 Flash FastMCP demographic simulation kits.
allowed-tools: google default_api image_gen skills
---
# sg-govtech-firstdate-fertility-engine

Quantitative actuarial, demographic, geospatial (WebGIS), and multipartite graph-engineering simulation engine for evaluating Singapore marriage and parenthood interventions such as GovTech's FirstDate pilot across the Public Service and broader resident cohorts. Fuses live SingStat TableBuilder APIs, Data.gov.sg CKAN endpoints, MyCareersFuture v2 salary benchmarks, clinical fecundity/IVF curves, and URA Planning Area/Subzone socio-economic layers into an iterative agent loop for Antigravity IDE (`gemini-3.8-flash` high effort).

## When to Use

- Evaluating the effectiveness of GovTech's FirstDate pilot or state-backed matchmaking schemes against commercial dating platforms (Coffee Meets Bagel, Bumble, Hinge, Tinder, Kopi Date, Lunch Actually, Paktor, Muzz)
- Refactoring raw workforce headcounts into actual addressable unpartnered single cohorts (excluding corporatised MOH Holdings public healthcare clusters, married officers, and partnered singles in BTO queues)
- Simulating cross-agency multipartite Gale-Shapley stable matching (`a(u) != a(v)`) and computing rejection rates from age gaps, Civil Service MX-grade hierarchy imbalances, Big-5 personality/value friction, and ethnic/religious endogamy rules (ROM vs ROMM)
- Identifying the Golden Ageband for marriage and childbirth by combining age-specific marriage rates (ASMR), divorce hazards (ASDR), HDB Single Singapore Citizen (age 35+ Standard/Plus/Prime 2-room Flexi and resale) utility lock-in, and maternal/paternal biological fertility cliffs
- Auditing full 0-to-22-year child-raising financial and parental leave commitments (hospital delivery, confinement, ECDA childcare, FDW helper, tuition, transport, HFMD/viral sick leave, parent-teacher conferences) against 2025/2026 Baby Bonus, CDA, WMCR, 30-week paid parental leave, and NDR 2026 SG Child Support Package offsets
- Mapping childhood neighborhood socio-economic status (55 URA Planning Areas, 332 Subzones, 28 Postal Districts D01-D28) against adult singlehood, reference-point tuition inflation, and weekday commute time taxes

## Steps

### Step 1: Refactor the Addressable Unpartnered Cohort and Agency Graph

1. Fetch official Public Service workforce distributions from Data.gov.sg (`d_ded51ba4680464b706b95069018ffcac` for Ministry vs Statutory Board headcount and gender split; `d_b6c936cf4666cb00b5f4cba57eeef713` for age band and Junior vs Senior Executive splits).
2. Exclude corporatised public healthcare cluster employees (SingHealth, NHG Health, NUHS under MOH Holdings Pte Ltd, ~65,000 staff) when modeling FirstDate's Specified Entity scope (16 Ministries ~89,000 + >50 Statutory Boards ~69,000 = ~158,000 officers).
3. Filter by SingStat age- and sex-specific citizen/resident singlehood rates (`M810581`, `M810681`) and refactor out partnered singles using NPTD Marriage and Parenthood Survey benchmarks (~50% of legal singles aged 21-45 are already in a romantic relationship, peaking in the 25-34 BTO queue brackets).
4. Apply the Cross-Agency Multipartite Graph constraint (`a(u) != a(v)`) across Ministries (55.5% female) and Statutory Boards (51.3% male) using `scripts/firstdate_graph_agent_loop.py` to compute Turan multipartite edge capacity loss and gender-queue bottlenecks.

### Step 2: Compute Pairwise Rejection and Compatibility Weights

1. Evaluate edge weights `W(u, v)` in the heterogeneous property graph across four empirical penalty terms:

   - **Age-Gap Asymmetry Penalty**: Calibrate against SingStat Table `M830168` (60.2% of first marriages within 0-2 years; median groom-bride gap +1.5 years). Penalize pairings where `|Delta Age| >= 5` years or where the bride is significantly older than the groom.
   - **Seniority and MX-Grade Power Penalty**: Calibrate against PSD MX14-MX9 salary bands and SingStat Table `M830180` educational homogamy (68.7% same tier; 18.6% female hypogamy vs 12.6% male hypergamy). Apply power-imbalance rejection penalties to Senior Male (MX9/MX10) + Junior Female (MX13/MX14) pairings and hypergamy friction to Senior Female + Junior Male pairings.
   - **Ethnic, Cultural, and Religious Matrix**: Calibrate against SingStat `M830184` (80.7% intra-ethnic vs 19.3% inter-ethnic citizen marriages; ROM Civil vs ROMM Muslim conversion rules) and incorporate ethnic fertility/social norm differentials (Malay kampung extended-family support with 1.53-1.58 TFR vs Chinese competitive-parenting self-reliance with 0.70-0.83 TFR, Indian 0.91-0.92 TFR, and Eurasian/Others high exogamy).
   - **Photo-Free First-Date Reveal Hazard**: Account for physical attraction drop-off at the first in-person meetup following FirstDate's photo-free FormSG profile matching.

### Step 3: Run the Lifecycle Fertility, Housing, and Financial Microsimulation

1. Run `scripts/firstdate_fertility_mcp_server.py` or `scripts/firstdate_graph_agent_loop.py` across 5-year age bands (`21-24`, `25-29`, `30-34`, `35-39`, `40-45`).
2. Add relationship progression and HDB BTO waiting time delays (2.8 to 4.0 years) to the officer's age at matching to determine actual maternal and paternal age at first and second conception.
3. Apply clinical fecundity, natural miscarriage (`BMJ 2019` curve: 9.8% at 25-29, 10.8% at 30-34, 16.7% at 35-39, 32.2% at 40-44, 53.6% at >=45), the age-37 25,000-oocyte follicular cliff, KKH/MOH ART/IVF live birth rates (40.0% <30, 38.3% 30-35, 19.6% at 38, 8.8% at 39, 5.9% at 40-44), and the paternal `>=40` x maternal `>=35` Sperm DNA Fragmentation miscarriage jump (+15.2 percentage points to 37.2%).
4. Compute net household child-raising cashflow and career opportunity cost by comparing 0-to-22-year gross outlays (Public Anchor ~$260k, Civil Service Mid-Tier ~$564k, High-SES Private ~$1.16M) and marriage/divorce risk costs against 2025/2026 Baby Bonus, CDA, MediSave, WMCR/PTR tax reliefs, 30-week paid parental leave (`16w GPML + 4w GPPL + 10w SPL`), and the 6-day statutory childcare leave deficit during preschool HFMD/viral outbreaks.

### Step 4: Generate Interactive WebGIS Dashboard and Antigravity Kit

1. Map URA Planning Area (`d_4765db0e87b9c86336792efe8a1f7a66`), Subzone (`d_8594ae9ff96d0c708bc2af633048edfb`), and Postal District (`D01-D28`) childhood SES origins, HDB 4-room resale prices, and GHS 2025 commute durations (25-30 mins in CCR/RCR vs 45-50 mins in OCR BTO towns) into a self-contained HTML WebGIS and Bipartite Graph Simulator.
2. Validate the web app and bundle `SKILL.md`, FastMCP server scripts, agent hooks, and `ANTIGRAVITY_MASTER_PROMPT.md` into a downloadable `.zip` archive.

## Gotchas

- Never treat all legally single public officers in SingStat/Singpass records as unpartnered: roughly 50% of legal singles aged 21-45 are already in steady relationships (many waiting for BTO key collection before solemnising their marriage).
- Never use matching age as conception age: always add 3 to 5 years for dating progression, wedding preparation, and BTO construction wait times before evaluating maternal ovarian reserve and paternal sperm DNA fragmentation hazards.
- Remember that MOH ART 75% co-funding requires starting treatment before age 40 (with up to 2 co-funded cycles allowed at age 40+ only if at least one ART/IUI cycle was attempted before turning 40).
