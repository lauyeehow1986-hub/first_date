#!/usr/bin/env python3
"""
Demographic Odds & Actuarial Matrix Generator across CMIO Races and 5-Year Age Bands
Calibrated against SingStat 2025 TableBuilder APIs (M810581, M810681, M830102, M810091, M830184).
"""
import math
import json

RACES = ['Chinese', 'Malay', 'Indian', 'Others_Eurasian']
AGEBANDS = ['20-24', '25-29', '30-34', '35-39', '40-44']

# Age-Specific Marriage Rates (ASMR) per 1,000 unmarried
ASMR = {
    'Chinese': {
        'M': {'20-24': 4.8, '25-29': 52.4, '30-34': 98.6, '35-39': 81.2, '40-44': 47.5},
        'F': {'20-24': 11.2, '25-29': 82.5, '30-34': 112.4, '35-39': 54.8, '40-44': 24.6}
    },
    'Malay': {
        'M': {'20-24': 19.5, '25-29': 88.2, '30-34': 82.4, '35-39': 62.1, '40-44': 42.0},
        'F': {'20-24': 38.6, '25-29': 118.5, '30-34': 76.2, '35-39': 38.4, '40-44': 18.2}
    },
    'Indian': {
        'M': {'20-24': 6.2, '25-29': 58.4, '30-34': 94.1, '35-39': 75.3, '40-44': 44.8},
        'F': {'20-24': 16.4, '25-29': 91.2, '30-34': 101.5, '35-39': 48.2, '40-44': 21.5}
    },
    'Others_Eurasian': {
        'M': {'20-24': 5.5, '25-29': 54.0, '30-34': 92.5, '35-39': 77.0, '40-44': 45.2},
        'F': {'20-24': 14.0, '25-29': 85.0, '30-34': 105.0, '35-39': 51.0, '40-44': 23.0}
    }
}

# Age-Specific Fertility Rates (ASFR) per 1,000 females
ASFR = {
    'Chinese': {'20-24': 4.2, '25-29': 28.5, '30-34': 62.4, '35-39': 40.1, '40-44': 7.8},
    'Malay': {'20-24': 29.5, '25-29': 84.6, '30-34': 98.2, '35-39': 68.5, '40-44': 16.4},
    'Indian': {'20-24': 7.8, '25-29': 41.2, '30-34': 74.5, '35-39': 48.0, '40-44': 9.2},
    'Others_Eurasian': {'20-24': 6.5, '25-29': 38.0, '30-34': 71.0, '35-39': 46.5, '40-44': 8.8}
}

# Singlehood Proportions (SingStat M810581 / M810681 calibrated)
SINGLEHOOD = {
    'Chinese': {
        'M': {'20-24': 0.995, '25-29': 0.882, '30-34': 0.495, '35-39': 0.256, '40-44': 0.168},
        'F': {'20-24': 0.982, '25-29': 0.765, '30-34': 0.368, '35-39': 0.218, '40-44': 0.167}
    },
    'Malay': {
        'M': {'20-24': 0.965, '25-29': 0.725, '30-34': 0.375, '35-39': 0.185, '40-44': 0.115},
        'F': {'20-24': 0.915, '25-29': 0.582, '30-34': 0.245, '35-39': 0.142, '40-44': 0.108}
    },
    'Indian': {
        'M': {'20-24': 0.992, '25-29': 0.845, '30-34': 0.462, '35-39': 0.235, '40-44': 0.152},
        'F': {'20-24': 0.970, '25-29': 0.710, '30-34': 0.335, '35-39': 0.192, '40-44': 0.145}
    },
    'Others_Eurasian': {
        'M': {'20-24': 0.990, '25-29': 0.860, '30-34': 0.480, '35-39': 0.248, '40-44': 0.160},
        'F': {'20-24': 0.975, '25-29': 0.740, '30-34': 0.350, '35-39': 0.205, '40-44': 0.155}
    }
}

RACE_TFR_MULT = {
    'Chinese': 0.70 / 0.87,
    'Malay': 1.53 / 0.87,
    'Indian': 0.92 / 0.87,
    'Others_Eurasian': 0.89 / 0.87
}

BASE_EXPECTED_KIDS = {
    '20-24': 1.62,
    '25-29': 1.53,
    '30-34': 1.26,
    '35-39': 0.77,
    '40-44': 0.59
}


def compute_matrices():
    results = {}
    for r in RACES:
        results[r] = {}
        for ab in AGEBANDS:
            m_asmr = ASMR[r]['M'][ab]
            f_asmr = ASMR[r]['F'][ab]
            p_m_marry = (1.0 - math.exp(-5.0 * (m_asmr / 1000.0))) * 100.0
            p_f_marry = (1.0 - math.exp(-5.0 * (f_asmr / 1000.0))) * 100.0
            asfr_val = ASFR[r][ab]
            exp_kids = BASE_EXPECTED_KIDS[ab] * RACE_TFR_MULT[r]
            p_birth_5yr = (1.0 - math.exp(-5.0 * (asfr_val / 1000.0 * 2.2))) * 100.0

            results[r][ab] = {
                'singlehood_m': SINGLEHOOD[r]['M'][ab],
                'singlehood_f': SINGLEHOOD[r]['F'][ab],
                'asmr_m': m_asmr,
                'asmr_f': f_asmr,
                'p_5yr_marry_m': round(p_m_marry, 1),
                'p_5yr_marry_f': round(p_f_marry, 1),
                'asfr': asfr_val,
                'expected_completed_kids': round(exp_kids, 2),
                'p_5yr_birth_married': round(p_birth_5yr, 1),
            }
    return results


if __name__ == '__main__':
    data = compute_matrices()
    print(json.dumps(data, indent=2))
