"""t8_icm_partial_mechanism.py — WHY does partial r(delta_M, E_ICM | M_WL) ~= -0.70 exist?
(docs/132 task T8; R010; extends NR-015)

Prior state (NR-015): the correlation collapses to r=-0.08 when T_X is also controlled; two
LIVE readings remained undistinguished — (1) DEFINITIONAL artifact (M_hydro is built from T_X
via the HSE formula, so delta_M=M_WL-M_hydro anti-correlates with T_X while E_ICM=M_gas*T_X
correlates with it), vs (2) COMMON PHYSICAL DRIVER (dynamical/merger state drives both T_X and
HSE-violation). This script (a) makes the T_X pathway explicit and reproducible, and (b) runs
the cool-core/non-cool-core stratification that NR-015's Relaxation Map row 2 flagged as the
cheapest DISCRIMINATOR between readings (1) and (2) but never executed.

Data: experiments/20260713-h1e-agn-feedback-confound/artifacts/cccp_mahdavi2013_merged.csv
      (Mahdavi et al. 2013, arXiv:1210.3689) [VERIFIED-DIRECT-READ].
Labels: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION.
"""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
from scipy import stats

CSV = (
    Path(__file__).resolve().parent.parent
    / "experiments"
    / "20260713-h1e-agn-feedback-confound"
    / "artifacts"
    / "cccp_mahdavi2013_merged.csv"
)


def load():
    rows = list(csv.DictReader(CSV.open(encoding="utf-8")))

    def col(name, rs=rows):
        return np.array([float(r[name]) for r in rs])

    return rows, col


def resid(y, X):
    X1 = np.column_stack([X, np.ones(len(y))])
    b, *_ = np.linalg.lstsq(X1, y, rcond=None)
    return y - X1 @ b


def pcorr(x, y, C):
    C = C.reshape(len(x), -1)
    return stats.pearsonr(resid(x, C), resid(y, C))


def main() -> None:
    print("=" * 74)
    print("T8 — Mechanism of partial r(delta_M, E_ICM | M_WL) ~= -0.70")
    print("NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION")
    print("=" * 74)
    rows, col = load()
    dM = col("delta_M_1e14Msun")
    E = col("E_ICM_proxy_MgasTx")
    MWL = col("M_WL_1e14Msun")
    TX = col("T_X_keV")
    Mhy = col("M_hydro_1e14Msun")
    K0 = np.array([float(r["K0_keVcm2"]) if r["K0_keVcm2"] else np.nan for r in rows])
    n = len(dM)
    print(f"\nN = {n} CCCP clusters")

    # Identity: delta_M = M_WL - M_hydro (definitional)
    id_resid = np.max(np.abs(dM - (MWL - Mhy)))
    print(
        f"[identity] max|delta_M - (M_WL - M_hydro)| = {id_resid:.3e}  "
        f"-> delta_M is DEFINED as M_WL - M_hydro (M_hydro is HSE, built from T_X)."
    )

    # Baseline
    r0, p0 = pcorr(dM, E, MWL)
    print(f"\n[baseline] r(delta_M, E_ICM | M_WL)        = {r0:+.4f}  p={p0:.2e}")

    # T_X pathway (both sides depend on T_X, opposite signs)
    r_dtx, p_dtx = pcorr(dM, TX, MWL)
    r_etx, p_etx = pcorr(E, TX, MWL)
    print(
        f"[pathway]  r(delta_M, T_X | M_WL)          = {r_dtx:+.4f}  p={p_dtx:.2e}  "
        "(M_hydro up with T_X -> delta_M down)"
    )
    print(
        f"[pathway]  r(E_ICM,  T_X | M_WL)           = {r_etx:+.4f}  p={p_etx:.2e}  "
        "(E_ICM = M_gas*T_X -> up with T_X)"
    )

    # Control for T_X -> collapse (reproduces NR-015)
    rC, pC = pcorr(dM, E, np.column_stack([MWL, TX]))
    print(
        f"[control]  r(delta_M, E_ICM | M_WL, T_X)   = {rC:+.4f}  p={pC:.2e}  "
        "(collapses -> the -0.70 is T_X-mediated)"
    )

    # DISCRIMINATOR (NR-015 Relaxation Map row 2, never run): CC vs NCC stratification.
    # If r(delta_M,T_X|M_WL) is similar in both bins -> favors reading (1) definitional.
    # If concentrated in NCC (disturbed/merging) -> favors reading (2) dynamical common-driver.
    print("\n[discriminator] cool-core vs non-cool-core split at K0 = 30 keV cm^2:")
    valid = np.isfinite(K0)
    cc = valid & (K0 < 30.0)  # cool-core (relaxed)
    ncc = valid & (K0 >= 30.0)  # non-cool-core (disturbed)
    for name, mask in [
        ("cool-core (K0<30, relaxed)", cc),
        ("non-cool-core (K0>=30, disturbed)", ncc),
    ]:
        if mask.sum() >= 5:
            rr, pp = pcorr(dM[mask], TX[mask], MWL[mask])
            print(f"    {name:<40} n={mask.sum():>2}  r(delta_M,T_X|M_WL)={rr:+.4f}  p={pp:.3f}")
        else:
            print(f"    {name:<40} n={mask.sum():>2}  (too few, skip)")
    print("\n  READ-OUT: similar strength in BOTH bins -> definitional (reading 1) favored;")
    print("            much stronger in NCC/disturbed -> dynamical common-driver (reading 2).")
    print("=" * 74)
    print("VERDICT INPUT: the -0.70 is NOT a genuinely-unexplained anomaly and NOT TJB's WHIM")
    print("mechanism (interior ICM, not cosmic-web outskirts). It is a T_X-mediated")
    print("mass-observable systematic via the HSE mass definition. The CC/NCC split above")
    print("decides whether that T_X pathway is purely definitional or partly dynamical-state.")
    print("=" * 74)


if __name__ == "__main__":
    main()
