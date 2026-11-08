#!/usr/bin/env python3
"""
Asymmetry, MX Hierarchy, AMLA Conversion & Divorce Liability Simulation Script
Calibrated to SingStat Tables M830168, M830180, M830184, M830202, and M830301.
"""
import sys
import json
from firstdate_fertility_mcp_server import (
    simulate_cross_agency_gale_shapley_graph,
    evaluate_lifecycle_fertility_and_child_cost
)

def run_asymmetry_audit():
    scenarios = [
        ("Symmetric Peers (M29 MX12 + F27 MX12)", 29, 27, "MX12", "MX12", "Chinese", "Chinese", True),
        ("Older Groom +7y (M34 MX11 + F27 MX12)", 34, 27, "MX11", "MX12", "Chinese", "Chinese", True),
        ("Older Groom +12y (M39 MX10 + F27 MX12)", 39, 27, "MX10", "MX12", "Chinese", "Chinese", True),
        ("Older Bride +3y (M27 MX13 + F30 MX12)", 27, 30, "MX13", "MX12", "Chinese", "Chinese", True),
        ("Older Bride +6y (M26 MX13 + F32 MX11)", 26, 32, "MX13", "MX11", "Chinese", "Chinese", True),
        ("Senior Male (M34 MX10 + F26 MX13)", 34, 26, "MX10", "MX13", "Chinese", "Chinese", True),
        ("Female Hypogamy (F32 MX11 + M28 MX13)", 28, 32, "MX13", "MX11", "Chinese", "Chinese", True),
        ("AMLA Inter-Faith (Chinese M + Malay F)", 29, 27, "MX12", "MX12", "Chinese", "Malay", False),
    ]

    audit_results = []
    for label, m_age, f_age, m_mx, f_mx, m_r, f_r, s_rel in scenarios:
        match_sim = simulate_cross_agency_gale_shapley_graph(
            male_age=m_age, female_age=f_age,
            male_mx_grade=m_mx, female_mx_grade=f_mx,
            male_race=m_r, female_race=f_r,
            same_religion=s_rel
        )
        fert = evaluate_lifecycle_fertility_and_child_cost(
            female_match_age=f_age, male_match_age=m_age,
            cost_tier="Civil_Service_Mid_Tier"
        )
        rom_rate = match_sim["second_date_conversion_probability"] * 0.045
        exp_kids = fert["expected_children_if_married"]
        roi_births = rom_rate * exp_kids * 100

        audit_results.append({
            "archetype": label,
            "rejection_prob_pct": round(match_sim["rejection_probability"] * 100, 1),
            "second_date_conv_pct": round(match_sim["second_date_conversion_probability"] * 100, 1),
            "est_rom_rate_pct": round(rom_rate * 100, 2),
            "expected_completed_kids": exp_kids,
            "roi_births_per_100_dates": round(roi_births, 2),
            "maternal_conception_age": fert["estimated_maternal_conception_age"],
            "paternal_conception_age": fert["estimated_paternal_conception_age"],
            "miscarriage_prob_pct": round(fert["clinical_hazards"]["effective_miscarriage_probability"] * 100, 1)
        })

    return audit_results


if __name__ == "__main__":
    results = run_asymmetry_audit()
    print(json.dumps(results, indent=2))
