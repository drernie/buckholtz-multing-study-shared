"""P001 redesigned test (NR-012 addendum, next_check 2026-07-15): does the
delta_M/E_ICM partial correlation survive when the thermal proxy is M_gas
ALONE (not multiplied by T_X)?

Motivation (surfaced independently by boyko-agent test, 2026-07-18):
delta_M = M_WL - M_hydro, and M_hydro is a hydrostatic mass estimate --
standard hydrostatic-mass formulas use the temperature profile T(r) as an
input. E_ICM_proxy = M_gas * T_X also contains T_X directly. So T_X may sit
on BOTH sides of the correlation via different paths (E_ICM directly,
delta_M indirectly via M_hydro), which could inflate the partial correlation
independent of any real physical confound. NR-012's addendum already flagged
half of this (E_ICM's T_X component) as circular when used as a covariate;
this test checks the other half: does a T_X-FREE thermal proxy (M_gas alone)
still carry the signal?

Data: cccp_mahdavi2013_merged.csv (Mahdavi et al. 2013, [VERIFIED-DIRECT-READ],
same file used by H1c/H1e).
"""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
from scipy import stats

DATA_PATH = (
    Path(__file__).parent.parent.parent
    / "20260713-h1e-agn-feedback-confound"
    / "artifacts"
    / "cccp_mahdavi2013_merged.csv"
)


def load_columns() -> dict[str, np.ndarray]:
    rows = []
    with DATA_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not row["M_Gas_1e14Msun"] or not row["T_X_keV"]:
                continue
            rows.append(row)

    return {
        "delta_M": np.array([float(r["delta_M_1e14Msun"]) for r in rows]),
        "E_ICM": np.array([float(r["E_ICM_proxy_MgasTx"]) for r in rows]),
        "M_WL": np.array([float(r["M_WL_1e14Msun"]) for r in rows]),
        "M_Gas": np.array([float(r["M_Gas_1e14Msun"]) for r in rows]),
        "T_X": np.array([float(r["T_X_keV"]) for r in rows]),
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
    print(f"N clusters (M_Gas + T_X both available) = {n}")

    controls_mwl = d["M_WL"].reshape(-1, 1)
    controls_mwl_tx = np.column_stack([d["M_WL"], d["T_X"]])

    r_base, p_base = partial_corr(d["delta_M"], d["E_ICM"], controls_mwl)
    print(
        f"\nBaseline (for reference) r(delta_M, E_ICM=M_Gas*T_X | M_WL) = {r_base:.4f}  p={p_base:.3e}"
    )

    # WHY: this is the EXACT pre-registered criterion from pearl_registry
    # row 34 (2026-07-01): "partial r(delta_M, M_gas | M_WL, T_x)" --
    # controlling for BOTH M_WL and T_x, not M_WL alone. Controlling for T_x
    # too is what makes this a genuine test of M_gas's independent
    # contribution, since M_gas and T_x are themselves correlated (~0.71 at
    # fixed M_WL, computed below) and T_x is the component already flagged
    # as circular (NR-012 addendum).
    r_key, p_key = partial_corr(d["delta_M"], d["M_Gas"], controls_mwl_tx)
    print(
        f"KEY TEST (exact pre-registration) r(delta_M, M_Gas | M_WL, T_X) = {r_key:.4f}  p={p_key:.3e}"
    )

    # WHY: a point estimate alone overstates confidence at N=50 (skeptic review,
    # 2026-07-18) -- report the bootstrap CI alongside it so the verdict reflects
    # actual statistical precision, not just the central value.
    rng = np.random.default_rng(42)
    n_boot = 10_000
    boots = []
    idx = np.arange(n)
    for _ in range(n_boot):
        sample = rng.choice(idx, size=n, replace=True)
        try:
            r_b, _ = partial_corr(d["delta_M"][sample], d["M_Gas"][sample], controls_mwl_tx[sample])
            if not np.isnan(r_b):
                boots.append(r_b)
        except np.linalg.LinAlgError:
            continue
    boots_arr = np.array(boots)
    ci_lo, ci_hi = np.percentile(boots_arr, [2.5, 97.5])
    print(
        f"Bootstrap 95% CI ({len(boots_arr)}/{n_boot} valid resamples): [{ci_lo:.4f}, {ci_hi:.4f}]"
    )

    r_key_loose, p_key_loose = partial_corr(d["delta_M"], d["M_Gas"], controls_mwl)
    print(
        f"Secondary (looser, T_x NOT controlled) r(delta_M, M_Gas | M_WL) = {r_key_loose:.4f}  p={p_key_loose:.3e}"
    )

    r_gas_tx, p_gas_tx = partial_corr(d["M_Gas"], d["T_X"], controls_mwl)
    print(
        f"\nContext: r(M_Gas, T_X | M_WL) = {r_gas_tx:.4f}  p={p_gas_tx:.3e} (how entangled are the two factors of E_ICM)"
    )

    r_dm_tx, p_dm_tx = partial_corr(d["delta_M"], d["T_X"], controls_mwl)
    print(
        f"Context: r(delta_M, T_X | M_WL) = {r_dm_tx:.4f}  p={p_dm_tx:.3e} (does T_X alone predict delta_M -- the M_hydro-side leakage; NOT pre-registered, unexpected finding)"
    )

    print(
        "\n--- Verdict per pre-registered criteria (pearl_registry row 34, ONLY the SURVIVES line was actually pre-registered on 2026-07-01) ---"
    )
    print("SURVIVES: |r_key|>0.40, same sign as baseline, p<0.10")
    print(
        "NOT-SURVIVES: everything else -- mechanism (definitional-artifact vs common-driver) is NOT distinguished by this test, see NR-015"
    )
    if abs(r_key) > 0.40 and p_key < 0.10 and np.sign(r_key) == np.sign(r_base):
        verdict = "SURVIVES -- M_gas independent of T_X still carries the signal"
    else:
        verdict = "NOT-SURVIVES -- pre-registered SURVIVES prediction is falsified; do not over-interpret as ARTIFACT-CONFIRMED, see NR-015 Skeptic Response Matrix"
    print(f"|r_key|={abs(r_key):.4f}  CI=[{ci_lo:.4f},{ci_hi:.4f}]  ->  {verdict}")


if __name__ == "__main__":
    main()
