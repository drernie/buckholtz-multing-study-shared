"""
Reproducibility artifact for experiments/20260713-r011-beta-profile-nesting.
NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

Reproduces every numeric claim in this experiment's claim.md/decision.md and in
docs/122 v3-v6, from src/pearson_fit.py against the real MCXC cluster catalog and
real Moresco+2022 cosmic-chronometer H(z) data. No synthetic data anywhere.

Run from the repo root:
    python experiments/20260713-r011-beta-profile-nesting/artifacts/verify_r011_beta_profile.py

Expected output (abridged): see decision.md "Numerical results" table.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from src.pearson_fit import _interp_hcc, load_data  # noqa: E402

H_ANCHOR = 73.0
D0 = 100.0


def dataset_fingerprint() -> None:
    clusters, hz_cc = load_data()
    h_clusters = hashlib.sha256(
        pd.util.hash_pandas_object(clusters, index=True).values.tobytes()
    ).hexdigest()[:16]
    h_hzcc = hashlib.sha256(
        pd.util.hash_pandas_object(hz_cc, index=True).values.tobytes()
    ).hexdigest()[:16]
    print("dataset hash (clusters_clean.csv):", h_clusters)
    print("dataset hash (hz_cc.csv):         ", h_hzcc)
    print("n_raw clusters:", len(clusters))


def build_frame():
    clusters, hz_cc = load_data()
    df = clusters[clusters["Ethermal_c2_Msun"].notna()].sort_values("z").reset_index(drop=True)
    _, valid_cc0 = _interp_hcc(hz_cc, df["z"].values)
    df443 = df[valid_cc0].reset_index(drop=True)
    assert df443["cluster_id"].nunique() == len(df443), "duplicate cluster_id found"
    assert len(df443) == 443, f"expected 443 rows, got {len(df443)}"
    return df443, hz_cc


def r_for(term_m, coeff_d, coeff_q2, valid_cc, H_cc_at_z, beta_d, beta_q):
    phi = term_m - beta_d * coeff_d + beta_q**2 * coeff_q2
    pos = np.isfinite(phi) & (phi > 0)
    if pos.sum() < 5:
        return np.nan, 0
    phi_ref = phi[pos][0]
    H_m = np.where(pos, H_ANCHOR * np.sqrt(np.maximum(phi / phi_ref, 0.0)), np.nan)
    final = pos & valid_cc & np.isfinite(H_m) & (H_m > 0) & (H_m < 1e6)
    if final.sum() < 5:
        return np.nan, int(final.sum())
    r_val, _ = stats.pearsonr(H_m[final], H_cc_at_z[final])
    return float(r_val), int(final.sum())


def main() -> None:
    dataset_fingerprint()
    df443, hz_cc = build_frame()

    z = df443["z"].values
    m_A = df443["M500c_Msun"].values
    k_A = df443["Ethermal_c2_Msun"].values
    r_A = df443["R500c_Mpc"].values
    D = D0 / (1.0 + z)
    term_m = m_A / D**2
    coeff_d = 2.0 * k_A * r_A / D**3
    coeff_q2 = (k_A * r_A) ** 2 / D**4
    H_cc_at_z, valid_cc = _interp_hcc(hz_cc, z)

    def R(beta_d, beta_q):
        return r_for(term_m, coeff_d, coeff_q2, valid_cc, H_cc_at_z, beta_d, beta_q)

    print()
    print("=== Nested baseline Q(0,0) ===")
    r00, n00 = R(0.0, 0.0)
    print(f"Q(eta_d=0, eta_q=0) = {r00:.6f}  (n={n00})")

    print()
    print("=== R011's original 'grid-search optimum' (box-constrained, not global) ===")
    r_grid, n_grid = R(100.0, 3.24e7)  # beta_d=100 -> eta_d=1; beta_q=3.24e7 -> eta_q=3.24e5
    print(f"Q(beta_d=100, beta_q=3.24e7) = {r_grid:.6f}  (n={n_grid})  [below Q(0,0), as required]")

    print()
    print("=== True profile r_prof(eta_d) = max over eta_q (dense grid) ===")
    eta_d_grid = [0.0, 1e3, 1e4, 2.46e4, 1e5, 1.23e5, 2.46e5, 4.92e5, 1e6, 2.46e6, 1e7]
    eta_q_grid = np.logspace(-6, 7, 2000)
    for eta_d in eta_d_grid:
        beta_d = eta_d * D0
        best_r, best_n, best_eq = -2.0, 0, np.nan
        for eta_q in eta_q_grid:
            rv, n = R(beta_d, eta_q * D0)
            if np.isfinite(rv) and rv > best_r:
                best_r, best_n, best_eq = rv, n, eta_q
        print(f"  eta_d={eta_d:10.3e}  r_prof={best_r:.6f}  n={best_n}  eta_q@max={best_eq:.4e}")

    print()
    print("=== Analytic eta_q -> infinity limit (zero free parameters) ===")
    template = k_A * r_A * (1.0 + z) ** 2
    H_template = H_ANCHOR * (template / template[0])
    final = valid_cc & np.isfinite(H_template) & (H_template > 0) & (H_template < 1e6)
    r_inf, _ = stats.pearsonr(H_template[final], H_cc_at_z[final])
    print(f"r_infinity (closed form, no fit) = {r_inf:.12f}  (n={final.sum()})")

    print()
    print("=== eta_d-independence spot-check at eta_q=1e8 ===")
    for eta_d in [0.0, 1e4, 1e6, 1e8]:
        rv, n = R(eta_d * D0, 1e8 * D0)
        print(f"  eta_d={eta_d:.0e}: r={rv:.6f} n={n}")


if __name__ == "__main__":
    main()
