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

---

## 📊 Core Empirical Findings

| Metric | Empirical Figure | Actuarial & Demographic Significance |
| :--- | :---: | :--- |
| **Total Public Service Headcount** | **157,997** | 88,664 in 16 Ministries (55.5% F) + 69,333 in >50 Stat Boards (51.3% M) |
| **Healthcare Cluster Exclusion** | **~65,000** | SingHealth, NHG, NUHS under MOH Holdings excluded by Clause 6.1.1 |
| **Pre-Partnered Singles** | **50.2% - 53.8%** | Legal singles already attached/in BTO queues; true addressable single pool = **20,690** |
| **Turan Cross-Agency Edge Loss** | **-12.57%** | Forbidding intra-agency matches ($a(u) \neq a(v)$) leaves 88.08% network capacity |
| **FirstDate Pilot Annual Births** | **+143.8 births/yr** | Across entire Civil Service at full 100% adoption |
| **Net TFR Lift** | **+0.00419** | **Fails the +0.05 policy significance threshold by an order of magnitude (12x short)** |
| **Golden Ageband (Female)** | **25 – 29** | Conception at 28.5–32.5 post-BTO queue; precedes age-37 ovarian follicle cliff (<25,000) |
| **Golden Ageband (Male)** | **27 – 31** | Avoids age 40+ Paternal Sperm DNA Fragmentation (+15.2% miscarriage hazard) |
| **The Singlehood Arbitrage (Age 35)** | **> S$650,000** | Retained net worth via single 2-room Flexi BTO + S$115k grants vs wedding/child/divorce costs |

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
