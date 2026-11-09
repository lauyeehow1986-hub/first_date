# Singapore GovTech FirstDate Actuarial, Bipartite Graph & WebGIS Fertility Kit
### Autonomous Multi-Agent Simulation Engine (Antigravity IDE · Gemini 3.8 Flash · High Effort)

[![Live WebGIS & Executive Dashboard](https://img.shields.io/badge/GitHub%20Pages-Live%20Portal-success?style=for-the-badge&logo=github)](https://lauyeehow1986-hub.github.io/first_date/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

An end-to-end demographic, actuarial, microeconomic, clinical fertility, and geospatial (WebGIS) audit of Singapore's GovTech **FirstDate** public-officer matchmaking scheme ([https://firstdate.sandbox.gov.sg/](https://firstdate.sandbox.gov.sg/)) and its systemic efficacy in reversing Singapore's historic Total Fertility Rate decline (**0.97 in 2024; 0.87 in 2025**).

---

## 🌐 Live Interactive Portal & GitHub Pages

Access the complete dashboard and simulation suite directly in your browser:
👉 **[https://lauyeehow1986-hub.github.io/first_date/](https://lauyeehow1986-hub.github.io/first_date/)**

### Interactive Tabs Overview
1. **Executive Summary & Key Insights**: Core findings, systemic bottlenecks, macro TFR impact (+0.00419 lift), and high-level policy trade-offs.
2. **WebGIS Spatial Intelligence**: Interactive Leaflet.js OpenStreetMap engine featuring a dual-mode switch between **🟢 High-Efficacy Hotspots (10 Nodes)** and **🚨 Critical Policy Intervention Zones (10 Nodes)**, live layer toggles, transit arterials (NEL/EWL/NSL/CCL), area jump dropdown, and dynamic RTA-style detail inspector cards with prescribed government reforms.
3. **Golden Ageband & CMIO Demographics**: Mathematical derivations of optimal matchmaking age windows across Chinese, Malay, Indian, and Eurasian public officers, factoring in the 3.5-year BTO queue and maternal/paternal clinical fertility cliffs.
4. **Match Asymmetries & Rejection Friction**: Empirical friction models evaluating age gaps, Civil Service seniority/MX hierarchy (Junior MX13 vs Senior MX10), AMLA inter-faith conversion barriers, and photo-free reveal hazards.
5. **Financial Ledger & Singlehood Arbitrage**: Comprehensive 0-to-22y child raising costs (Mid-Tier S$564,200 vs High-SES S$1,160,400) minus state subsidies, alongside the S$650,000+ financial arbitrage of remaining single past age 35.
6. **Live Match & ROI Simulator**: Client-side interactive Monte Carlo calculator to test custom age, race, religion, and MX-grade pairings with real-time odds of 2nd date, marriage, and live births.
7. **Dating Platform Benchmarks & Policy Reforms**: Head-to-head comparison against Coffee Meets Bagel, Bumble, Hinge, Tinder, Kopi Date, Lunch Actually, and Muzz, followed by 5 structural policy recommendations to move the demographic needle.
8. **Inter-Agency Matching Dynamics & Headcount Directory**: Full 11-cluster Whole-of-Government master matrix analyzing cross-agency edge loss (-12.57%), gender liquidity ratings, complementary routing sources, and an interactive Whole-of-Government Headcount Audit reconciling the MOF FY2026 Budget Book (24 Heads of Expenditure = 84,194 permanent staff) against Data.gov.sg (88,664 Ministries + 69,333 Stat Boards = 157,997 Total).

---

## 📊 Core Empirical Findings: Dual Scope Analysis

The live dashboard features an interactive **Dual Scope Switcher** on Tab 1 comparing the legal statutory scope against the conservative civilian pilot baseline:

| Metric | 🌟 Full Statutory Reality (158k) | 🏛 Scoped Civilian Pilot (93k) | Actuarial & Demographic Significance |
| :--- | :---: | :---: | :--- |
| **Gross Eligible Public Service Base** | **157,997** | **92,997** | 100% of Ministries (88.7k) + Stat Boards (69.3k) vs civilian-only pilot |
| **Uniformed Personnel Eligibility** | **Included (+18.5k MHA Home Team)** | Excluded | Home Team (Police, SCDF, Prisons, CNB on Budget Head P p. 135) are eligible via Singpass. (Note: MINDEF Head J p. 113 lists only 70 civilian HQ staff; SAF military personnel are classified under Code 2900 Defence Block Vote) |
| **Public Healthcare Clusters Exclusion** | **~65k–80k (MOHH Clusters)** | **~65k–80k (MOHH Clusters)** | Corporatised under MOH Holdings: SingHealth (>40k), NHG (~22k), NUHS (~15k) total ~77k–80k gross staff. SingStat m870011 tracks ~52.5k registered public clinical staff (11.2k doctors, 32.1k nurses, 9.2k allied/pharmacists); part of Singapore's 200k+ wider national Health & Social Services sector (MOM SSIC Q) |
| **Unpartnered Singles (Ages 21–45)** | **20,700** | **12,250** | Singles after subtracting the empirical 50.2% pre-partnered/BTO-queue rate (NPTD Survey) |
| **Turan Bipartite Matching Capacity** | **96.40%** | **88.08%** | **Uniformed male influx neutralizes the MOE female teacher squeeze!** (Only 3.6% loss vs 12.6%) |
| **Annual Active Target Pool** | **6,458 users** | **3,828 users** | Onboarded FormSG / Singpass cohort at 31.2% adoption |
| **Annual Completed Live Births** | **+267.6 births/yr** | **+143.8 births/yr** | **+68.7% higher birth yield** under full statutory participation |
| **National TFR Lift** | **+0.00793 points** | **+0.00419 points** | Meaningfully increases demographic impact, though still below +0.05 threshold |
| **Prime Golden Ageband** | **F: 25–29 \| M: 27–31** | **F: 25–29 \| M: 27–31** | Conception pre-34 avoids ovarian cliff; paternal pre-35 avoids sperm DNA fragmentation |
| **The Singlehood Arbitrage (Age 35)** | **> S$650,000** | **> S$650,000** | Retained net worth via single 2-room Flexi BTO + S$115k grants vs wedding/child/divorce costs |

---

## 📁 Repository Structure

```
.
├── ANTIGRAVITY_MASTER_PROMPT.md                # Gemini 3.8 Flash High Effort System Prompt
├── index.html                                 # Live GitHub Pages Multi-Tab Web Application
├── README.md                                  # Documentation and repository overview
├── requirements.txt                           # Python dependencies (FastMCP, pandas, numpy)
├── mcp_config.json                            # Drop-in MCP configuration for Antigravity IDE
├── .agents/
│   └── hooks.json                             # Tool-invocation hooks for demographic routing
├── docs/
│   ├── index.html                             # GitHub Pages mirror for /docs deployment
│   ├── ACTUARIAL_DEMOGRAPHIC_AUDIT_REPORT.md  # Full-length demographic & actuarial treatise
│   ├── MATCHMAKING_ASYMMETRY_DIVORCE_LIABILITIES.md # Asymmetry, divorce, and arbitrage audit
│   ├── firstdate_gis_demographic_dashboard.html # Standalone GIS demographic dashboard
│   └── firstdate_gis_inline_widget.html       # Standalone GIS micro-widget
├── mcp-servers/
│   ├── firstdate_fertility_mcp_server.py      # FastMCP Server (SingStat, Data.gov.sg, Gale-Shapley)
│   ├── firstdate_graph_agent_loop.py          # Bipartite Graph Matching & Policy Optimizer
│   ├── compute_demographic_odds.py            # CMIO Race x Ageband Odds Generator
│   └── asymmetry_and_divorce_audit.py         # Asymmetry & Divorce Financial Ledger Engine
└── skills/
    └── sg-govtech-firstdate-fertility-engine/ # Packaged Antigravity IDE Skill
        ├── SKILL.md
        ├── scripts/
        └── references/
```

---

## 🛠️ Installation & MCP Setup

### 1. Python Environment Setup
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Antigravity MCP Server Registration
Add the following snippet to your `~/.gemini/config/mcp_config.json`:
```json
{
  "mcpServers": {
    "sg-govtech-firstdate-fertility-mcp": {
      "command": "python",
      "args": [
        "c:/Users/lauye/Downloads/firstdate/mcp-servers/firstdate_fertility_mcp_server.py"
      ],
      "env": {
        "PYTHONIOENCODING": "utf-8"
      }
    }
  }
}
```

### 3. Run Quantitative Scripts Directly
```bash
# Run demographic odds computation
python mcp-servers/compute_demographic_odds.py

# Run asymmetry and divorce liabilities audit
python mcp-servers/asymmetry_and_divorce_audit.py

# Run Gale-Shapley cross-agency graph matching
python mcp-servers/firstdate_graph_agent_loop.py
```

---

## 🏛️ 5 Policy Levers to Move the Needle

1. **Healthcare Ingestion Reform (Clause 6.1.1 Amendment)**: Expand eligibility to the ~65,000 MOH Holdings healthcare cluster workers (SingHealth, NHG, NUHS), immediately increasing the addressable female cohort by +18,400.
2. **BTO Fast-Track Parenthood Escrow**: Guarantee provisional BTO booking confirmation within 90 days of FirstDate formal engagement, compressing the relationship-to-conception latency from 3.5 years down to 1.5 years.
3. **Paternal Leave Parity & HFMD Emergency Bank**: Upgrade Statutory GPCL from 6 days to 15 days with dedicated childcare medical leave to eliminate the real-world 14-day annual leave deficit.
4. **Pre-Nuptial Financial Ringfencing**: Institutionalize statutory pre-nuptial asset ringfencing under Women's Charter Section 112 for civil servant first-time buyers.
5. **Algorithmic Reverse-Nudging**: Restructure FirstDate matching weights to prioritize biologically synchronized pairings (F: 25–29, M: 27–31) with mutual geographic affinity to high-affordability, family-friendly subzones.

---

## 📄 License & Attribution
Designed by Antigravity IDE with Gemini 3.8 Flash High Effort. Educational and policy research simulator — not affiliated with or endorsed by GovTech Singapore, PSD, or SingStat.


---

## 🏛 Whole-of-Government Headcount Audit: MOF Budget Book vs Data.gov.sg

A central methodological requirement of FirstDate's actuarial evaluation is ensuring that all agency headcounts, gender supplies, and cross-ministry matching capacities are mathematically grounded in official government data sources:

1. **MOF Revenue & Expenditure Estimates (Singapore Budget Book FY2026)**: Reports the **authorised permanent establishment** (voted posts under the Supply Bill) for all **24 Heads of Expenditure (8 Organs of State + 16 Ministries)**.
   * *Actual FY2024 Permanent Staff:* **82,957**
   * *Revised FY2025 Permanent Staff:* **84,194**
   * *Estimated FY2026 Permanent Staff:* **87,950**
   * [Download Official MOF Budget Book PDF (577 pages)](https://files.app.optical.gov.sg/mofbudget/production/assets/031bf134-5b42-4668-80e2-8743b0fe6c97.pdf)
2. **Data.gov.sg / Public Service Division (PSD)**: Reports the **actual employee headcount** (`d_8b7ca60d610db92a752565f153af4b6a`):
   * *Ministries & Organs of State (Civil Service):* **88,664** (39,420 M / 49,244 F)
   * *Statutory Boards (Autonomous Corporate Entities):* **69,333** (35,542 M / 33,791 F)
   * *Total Government Employees in Public Service:* **157,997** (74,962 M / 83,035 F)

### Complete 24-Head Permanent Establishment Schedule (MOF Budget Book FY2026)

| Head Code | Entity / Ministry / Organ of State | PDF Page | Actual FY2024 | Revised FY2025 | Estimated FY2026 | Key Schemes & Service Divisions |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Organs of State** | | | | | | |
| **Head A** | Civil List (Presidency) | p. 58 | 68 | 72 | 72 | President, Aides-de-Camp, Butlers, MX Scheme |
| **Head B** | Attorney-General's Chambers (AGC) | p. 63 | 631 | 648 | 694 | Legal Service (370), MX Scheme (235) |
| **Head C** | Auditor-General's Office (AGO) | p. 68 | 198 | 194 | 211 | Auditing Service (173), Corporate Support |
| **Head D** | Cabinet Office | p. 74 | 7 | 7 | 12 | Administrative Officers |
| **Head E** | Judicature (Supreme & State Courts) | p. 79 | 1,050 | 1,118 | 1,154 | MX Scheme (661), Judicial & Legal (257) |
| **Head F** | Parliament | p. 84 | 58 | 57 | 62 | Parliamentary Officers, Language Executives |
| **Head G** | Presidential Councils | p. 90 | 5 | 2 | 2 | Minority Rights & Presidential Secretariats |
| **Head H** | Public Service Commission (PSC) | p. 94 | 11 | 10 | 12 | Statutory Commissioners |
| **Subtotal** | **8 Organs of State** | | **2,028** | **2,108** | **2,219** | **2.5% of Civil Service** |
| | | | | | | |
| **Ministries** | | | | | | |
| **Head I** | Social & Family Development (MSF) | p. 101 | 2,801 | 2,998 | 3,100 | MX Scheme (2,898), Social Service schemes |
| **Head J** | Ministry of Defence (MINDEF Civilian HQ) | p. 113 | 279 | 70 | 70 | Civilian HQ only. *(SAF combatants & ~5k DXOs under Defence Vote)* |
| **Head K** | Ministry of Education (MOE) | p. 123 | 38,784 | 39,386 | 40,079 | Education Service (31.2k), MX (2.2k), AEDs (1.2k), MK (1.0k) |
| **Head L** | Sustainability & Environment (MSE) | p. 143 | 246 | 236 | 257 | Ministry HQ *(NEA, PUB, SFA are Stat Boards)* |
| **Head M** | Ministry of Finance (MOF) | p. 157 | 2,137 | 2,098 | 2,229 | MX Scheme (1,075), Singapore Customs Unified (768) |
| **Head N** | Ministry of Foreign Affairs (MFA) | p. 169 | 1,026 | 1,101 | 1,189 | Foreign Service Officers (620), Admin Specialists (396) |
| **Head O** | Ministry of Health (MOH HQ) | p. 179 | 1,741 | 1,153 | 1,153 | Ministry HQ only *(SingHealth, NUHS, NHG are healthcare clusters)* |
| **Head P** | Ministry of Home Affairs (MHA) | p. 193 | 26,456 | 27,274 | 29,247 | Police (13.1k), ICA (5.5k), SCDF (2.7k), MX (2.5k), SPS (2.0k), CNB (0.8k) |
| **Head Q** | Digital Development & Info (MDDI) | p. 213 | 1,113 | 1,138 | 1,286 | MX Scheme (564), Cyber Security Agency CSA (300) |
| **Head R** | Ministry of Law (MinLaw) | p. 225 | 524 | 541 | 589 | MX Scheme (428), Legal Service Officers |
| **Head S** | Ministry of Manpower (MOM) | p. 237 | 2,174 | 2,320 | 2,494 | MX Scheme (1,854), Labour Inspectors & Policy Officers |
| **Head T** | National Development (MND) | p. 247 | 457 | 399 | 471 | Ministry HQ *(HDB, URA, BCA, NParks are Stat Boards)* |
| **Head U** | Prime Minister's Office (PMO) | p. 263 | 1,214 | 1,307 | 1,363 | PSD, NPTD, SNDGO, CPIB, MX Scheme (1,007) |
| **Head V** | Trade & Industry (MTI) | p. 275 | 1,044 | 1,107 | 1,201 | MX Scheme (530), SingStat Statisticians (220) |
| **Head W** | Ministry of Transport (MOT) | p. 289 | 145 | 166 | 166 | Ministry HQ *(LTA, CAAS, MPA are Stat Boards)* |
| **Head X** | Culture, Community & Youth (MCCY) | p. 301 | 788 | 792 | 837 | Youth Executives (390), MX Scheme (342) |
| **Subtotal** | **16 Ministries** | | **80,929** | **82,086** | **85,731** | **97.5% of Civil Service** |
| | | | | | | |
| **TOTAL** | **Permanent Civil Service Staff** | | **82,957** | **84,194** | **87,950** | **Total Authorised Permanent Establishment** |

### Mathematical Bridge: 84,194 (Budget) vs 88,664 (Data.gov.sg) vs 92,997 (FirstDate)

1. **Reconciling the +4,470 (+5.0%) variance between Budget Book and Data.gov.sg**:
   * **MINDEF Civilian Defence Executive Officers (DXOs):** Head J in the Budget Book records only 70 civilian HQ permanent posts (SAF combatants and DXOs are funded under the confidential Defence Vote). In Data.gov.sg, ~4,000 to 5,000 civilian DXOs are categorized under "Ministries and Organs of State".
   * **Temporary, Contract & Daily-Rated Staff:** Data.gov.sg counts all employees. The Budget Book accounts for temporary/contract personnel separately under Object Code 1600 ($553.4M in Revised FY2025). MFA alone employs 507 locally recruited staff; MOE employs hundreds of contract/adjunct educators.
2. **Reconciling Statutory Boards (69,333 in Data.gov.sg)**:
   * Statutory Boards (HDB, LTA, CPF, IRAS, GovTech, MAS, PUB, etc.) are independent corporate bodies created by statute. Their payroll is funded through operating revenue or block grants (Object Code 3100 "Grants to Statutory Boards"), rather than the Main Estimates Establishment List.
3. **Reconciling the 92,997 FirstDate Specified Entities Baseline**:
   $$egin{aligned}
   	ext{FirstDate Specified Entities (92,997)} &= 	ext{Civilian Civil Servants (MOE 20.5k, MHA Civ/ICA 8.8k, MINDEF DXO 6.0k, MSF/MOM/Others 16.9k)} \
   &\quad + 	ext{Core Civilian Statutory Boards (Infra 15.3k executive tier [out of ~21.5k gross staff in HDB/LTA/NEA/PUB/BCA/URA Annual Reports], Finance 10.7k, Community 9.7k, Tech 5.1k)}
   \end{aligned}$$
