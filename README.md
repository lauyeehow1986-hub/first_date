# Singapore GovTech FirstDate Actuarial, Bipartite Graph & WebGIS Fertility Kit (Antigravity Gemini 3.8 Flash High Effort)

Quantitative actuarial, demographic, geospatial, and multipartite graph simulation kit evaluating Singapore marriage and parenthood schemes (GovTech FirstDate) across the Public Service.

## Included Components
- `ANTIGRAVITY_MASTER_PROMPT.md`: Copy-pasteable master prompt for Antigravity IDE (`gemini-3.8-flash` high effort).
- `docs/ACTUARIAL_DEMOGRAPHIC_AUDIT_REPORT.md`: Comprehensive actuarial evaluation of FirstDate vs Singapore's TFR (0.87), Golden Agebands by gender/race, and CMIO marriage/childbirth odds matrices.
- `skills/sg-govtech-firstdate-fertility-engine/`: Complete multi-file skill (`SKILL.md`, `scripts/`, `references/`).
- `mcp-servers/firstdate_fertility_mcp_server.py`: FastMCP server connecting SingStat TableBuilder APIs, Data.gov.sg CKAN endpoints, MyCareersFuture v2 salary bands, Cross-Agency Gale-Shapley Graph Solver, and Lifecycle Fertility/Child-Cost Actuary.
- `mcp-servers/firstdate_graph_agent_loop.py`: Closed-loop Heterogeneous Multipartite Graph & Counterfactual Policy Optimizer.
- `mcp-servers/compute_demographic_odds.py`: CMIO Race $\times$ Ageband $\times$ Gender odds and completed fertility matrix generator.
- `mcp_config.json` & `.agents/hooks.json`: Drop-in Antigravity IDE MCP and agent hook configuration files.
