"""H1e pre-registered test: does AGN feedback (K0, central entropy) explain the
partial correlation r(delta_M, E_ICM | M_WL) found in NR-010/011/012?

Data: cccp_mahdavi2013_merged.csv (Mahdavi et al. 2013, [VERIFIED-DIRECT-READ]).
Criteria: experiments/20260713-h1e-agn-feedback-confound/claim.md
"""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
from scipy import stats

DATA_PATH = Path(__file__).parent / "cccp_mahdavi2013_merged.csv"


def load_columns() -> dict[str, np.ndarray]:
    rows = []
    with DATA_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not row["K0_keVcm2"] or not row["wX"]:
                continue
            rows.append(row)

    return {
        "delta_M": np.array([float(r["delta_M_1e14Msun"]) for r in rows]),
        "E_ICM": np.array([float(r["E_ICM_proxy_MgasTx"]) for r in rows]),
        "M_WL": np.array([float(r["M_WL_1e14Msun"]) for r in rows]),
        "K0": np.array([float(r["K0_keVcm2"]) for r in rows]),
        "wX": np.array([float(r["wX"]) for r in rows]),
    }


def residualize(y: np.ndarray, controls: np.ndarray) -> np.ndarray:
    x = np.column_stack([controls, np.ones(len(y))])
    beta, _, _, _ = np.linalg.lstsq(x, y, rcond=None)
    pred = x @ beta
    return y - pred


def partial_corr(x: np.ndarray, y: np.ndarray, controls: np.ndarray) -> tuple[float, float]:
    rx = residualize(x, controls)
    ry = residualize(y, controls)
    return stats.pearsonr(rx, ry)


def main() -> None:
    d = load_columns()
    n = len(d["delta_M"])
    print(f"N clusters (K0 + wX both available) = {n}")

    r_base, p_base = partial_corr(d["delta_M"], d["E_ICM"], d["M_WL"].reshape(-1, 1))
    print(f"\nBaseline r(delta_M, E_ICM | M_WL) = {r_base:.4f}  p={p_base:.3e}")

    controls_k0 = np.column_stack([d["M_WL"], d["K0"]])
    r_key, p_key = partial_corr(d["delta_M"], d["E_ICM"], controls_k0)
    print(f"KEY TEST  r(delta_M, E_ICM | M_WL, K0)  = {r_key:.4f}  p={p_key:.3e}")

    r_k0_dM, p_k0_dM = partial_corr(d["K0"], d["delta_M"], d["M_WL"].reshape(-1, 1))
    r_k0_eicm, p_k0_eicm = partial_corr(d["K0"], d["E_ICM"], d["M_WL"].reshape(-1, 1))
    print(f"\nSecondary: r(K0, delta_M | M_WL) = {r_k0_dM:.4f}  p={p_k0_dM:.3e}")
    print(f"Secondary: r(K0, E_ICM  | M_WL) = {r_k0_eicm:.4f}  p={p_k0_eicm:.3e}")

    r_k0_wx, p_k0_wx = stats.pearsonr(d["K0"], d["wX"])
    print(f"\nA2 check: raw r(K0, wX) = {r_k0_wx:.4f}  p={p_k0_wx:.3e} (paper reports Spearman 0.52+-0.10)")

    controls_wx = np.column_stack([d["M_WL"], d["wX"]])
    r_key_wx, p_key_wx = partial_corr(d["delta_M"], d["E_ICM"], controls_wx)
    print(f"A2 check: r(delta_M, E_ICM | M_WL, wX) = {r_key_wx:.4f}  p={p_key_wx:.3e} (NR-012 baseline)")

    print("\n--- Verdict per pre-registered criteria (claim.md) ---")
    if abs(r_key) < 0.20 and (abs(r_k0_dM) > 0.30 or abs(r_k0_eicm) > 0.30) and min(p_k0_dM, p_k0_eicm) < 0.10:
        verdict = "PROMOTE"
    elif abs(r_key) > 0.40 and p_key < 0.10:
        verdict = "KILL"
    else:
        verdict = "INCONCLUSIVE"
    print(f"|r_key|={abs(r_key):.4f}  ->  {verdict}")


if __name__ == "__main__":
    main()
