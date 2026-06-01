"""Negative-Control Test Battery - SAFE_NOW Diagnostics

SAFETY: INTERNAL_ONLY, DIAGNOSTIC_ONLY, NO_VALIDATION, NO_REFUTATION

DATA SOURCE: data/table_a1_reported.csv (REAL Table A1, rows 2-12)
"""

from dataclasses import dataclass

import numpy as np
import pandas as pd

RANDOM_SEED = 42
BETA_D_RANGE = (0.5, 5.0)
BETA_Q_RANGE = (0.1, 20.0)
H0_PLANCK = 67.4
OM_PLANCK = 0.315
OL_PLANCK = 0.685

def load_table_a1_rows_2_12():
    df = pd.read_csv("data/table_a1_reported.csv", comment="#")
    df = df[df["z"] > 0].copy()
    assert len(df) == 11
    return df

def extract_h_data_and_beta(df):
    z = df["z"].values
    h_obs = df["H_obs"].values
    beta_d = 4.5
    beta_q = 18.0
    return z, h_obs, beta_d, beta_q

def compute_fit_quality(z, h_data, beta_d, beta_q):
    h_model = h_data[0] * np.sqrt((1 + z) ** (3 * (1 + beta_d)) + beta_q)
    return np.sum((h_data - h_model) ** 2)

@dataclass
class RowPermutationResult:
    original_chi2: float
    shuffled_chi2_mean: float
    p_value: float
    verdict: str

def test_row_permutation(z, h_data, beta_d, beta_q, n=100, seed=42):
    np.random.seed(seed)
    chi2_orig = compute_fit_quality(z, h_data, beta_d, beta_q)
    chi2_shuf = [compute_fit_quality(np.random.permutation(z), h_data, beta_d, beta_q) for _ in range(n)]
    p_val = np.mean(np.array(chi2_shuf) <= chi2_orig)
    verdict = "PASS" if p_val < 0.01 else "WARN" if p_val < 0.05 else "FAIL"
    return RowPermutationResult(chi2_orig, np.mean(chi2_shuf), p_val, verdict)

@dataclass
class RandomisedBetaResult:
    reported_chi2: float
    percentile: float
    verdict: str

def test_randomised_beta(z, h_data, beta_d, beta_q, n=100, seed=42):
    np.random.seed(seed)
    chi2_rep = compute_fit_quality(z, h_data, beta_d, beta_q)
    chi2_rand = [compute_fit_quality(z, h_data, np.random.uniform(*BETA_D_RANGE), np.random.uniform(*BETA_Q_RANGE)) for _ in range(n)]
    pct = np.mean(np.array(chi2_rand) > chi2_rep) * 100
    verdict = "PASS" if pct >= 90 else "WARN" if pct >= 70 else "FAIL"
    return RandomisedBetaResult(chi2_rep, pct, verdict)

@dataclass
class SyntheticLCDMResult:
    real_chi2: float
    synthetic_chi2: float
    chi2_ratio: float
    verdict: str

def test_synthetic_lcdm(z, h_data, beta_d, beta_q):
    chi2_real = compute_fit_quality(z, h_data, beta_d, beta_q)
    h_lcdm = H0_PLANCK * np.sqrt(OM_PLANCK * (1 + z)**3 + OL_PLANCK)
    best_chi2 = compute_fit_quality(z, h_lcdm, beta_d, beta_q)
    for bd in np.linspace(0.5, 5.0, 5):
        for bq in np.linspace(0.1, 20.0, 5):
            chi2_test = compute_fit_quality(z, h_lcdm, bd, bq)
            if chi2_test < best_chi2:
                best_chi2 = chi2_test
    ratio = best_chi2 / chi2_real if chi2_real > 0 else float('inf')
    verdict = "PASS" if ratio > 3.0 else "WARN" if ratio > 1.5 else "FAIL"
    return SyntheticLCDMResult(chi2_real, best_chi2, ratio, verdict)

def main():
    print("="*80)
    print("NEGATIVE-CONTROL TEST BATTERY")
    print("="*80)
    df = load_table_a1_rows_2_12()
    z, h_obs, beta_d, beta_q = extract_h_data_and_beta(df)
    print("DATA SOURCE: data/table_a1_reported.csv (rows 2-12)")
    print(f"DATA POINTS: {len(z)}")
    print(f"BETA VALUES: beta_d={beta_d}, beta_q={beta_q} (Table A1 caption)")
    print()
    r1 = test_row_permutation(z, h_obs, beta_d, beta_q)
    r2 = test_randomised_beta(z, h_obs, beta_d, beta_q)
    r3 = test_synthetic_lcdm(z, h_obs, beta_d, beta_q)
    print(f"Test 1 Row-Perm: {r1.verdict} (p={r1.p_value:.4f})")
    print(f"Test 2 Rand-Beta: {r2.verdict} ({r2.percentile:.1f}%)")
    print(f"Test 3 LCDM: {r3.verdict} (ratio={r3.chi2_ratio:.2f})")
    print()
    overall = "FAIL" if any(x.verdict == "FAIL" for x in [r1,r2,r3]) else "PASS" if all(x.verdict == "PASS" for x in [r1,r2,r3]) else "WARN"
    print(f"OVERALL: {overall}")
    print("="*80)

if __name__ == "__main__":
    main()
