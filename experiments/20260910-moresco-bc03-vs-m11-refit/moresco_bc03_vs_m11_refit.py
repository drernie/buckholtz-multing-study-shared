"""
Answers TJB's own direct question (email 2026-09-09, "thank you, plus
follow-up discussion"): "Do you think that changing from one [Moresco H(z)]
table to the other would significantly impact the 'Results'-section results
or other aspects of my work or paper?"

FINDING_E5 (2026-09-06) already established the RAW shift: switching from
BC03 to M11 shifts H(z) by a tight, uniform ~+6.8% on 12/15 points. That
finding explicitly named "whether this changes v82's own fitted results" as
a separate, unrun computation (its own "What this does NOT establish" #1).
This script runs it.

Design: take TJB's own 31-point CC_POINTS (P176_v82_real_chi2_hessian_
degeneracy.py, already positive-control-verified to reproduce his Table II
to <0.1%), identify the 15 points that are Moresco's own (moresco_mask,
z+H match against the BC03 table, reused verbatim from E8's own logic),
replace their H(z) values with the M11 table's values at the SAME redshift
(same galaxies, same z grid, same sigma_Hz kept -- this isolates the central-
value shift, not a re-derivation of the error budget), then re-optimize
(H0_anchor, beta1, beta2) under the swapped dataset using the SAME rescaled
Nelder-Mead procedure already verified in E8b to reproduce TJB's own optima
under BC03.

Positive control: BC03 refit must reproduce TJB's own published
"unconstrained_spotlighted" row (H0_anchor=73.22, beta1=1.4335e10,
beta2=7.8067e17, chi2=15.75) to the same tolerance E8b already uses.

Materiality threshold: reuses this same investigation thread's own
pre-registered MCID for Deltachi2 (CLAIM_E8_full_covariance_propagation.md,
MCID=2.0) -- not a new number invented for this script.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR -- this tests THIS PROJECT's own reconstruction of TJB's
published fit against a real, external, alternate input table. It is not a
claim about which table TJB "should" use.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import requests
from scipy.optimize import minimize

sys.path.insert(0, str(Path(__file__).parent.parent / "20260803-bridge"))

from P176_v82_real_chi2_hessian_degeneracy import (  # noqa: E402
    CC_POINTS,
    H_DESI,
    H_SHOES,
    SIG_DESI,
    SIG_SHOES,
    TABLE_II,
    Z_DESI,
    Z_SHOES,
    H_of_z_kms,
)

BC03_URL = "https://gitlab.com/mmoresco/CCcovariance/-/raw/master/data/HzTable_MM_BC03.dat"
M11_URL = "https://gitlab.com/mmoresco/CCcovariance/-/raw/master/data/HzTable_MM_M11.dat"
MCID_DCHI2 = 2.0  # reused verbatim from CLAIM_E8_full_covariance_propagation.md

zd = np.array([p[0] for p in CC_POINTS])
Hd_bc03 = np.array([p[1] for p in CC_POINTS])
sd = np.array([p[2] for p in CC_POINTS])
z33 = np.concatenate([zd, [Z_SHOES], [Z_DESI]])
s33 = np.concatenate([sd, [SIG_SHOES], [SIG_DESI]])
ZFINE = np.sort(np.unique(np.concatenate([np.linspace(0, Z_DESI, 500), z33])))


def fetch_table(url: str) -> pd.DataFrame:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    lines = [ln for ln in r.text.strip().splitlines() if ln.strip() and not ln.startswith("#")]
    rows = [ln.split(",") for ln in lines]
    df = pd.DataFrame(rows).iloc[:, :3]
    df.columns = ["z", "Hz", "errHz"]
    return df.astype({"z": float, "Hz": float, "errHz": float})


def moresco_indices(bc03: pd.DataFrame) -> np.ndarray:
    """Which of TJB's own 31 CC_POINTS are Moresco's 15 (z+H match against
    the live-fetched BC03 table, tolerance matches E8's own moresco_mask)."""
    idx = []
    for i, (z, h) in enumerate(zip(zd, Hd_bc03, strict=True)):
        for _, row in bc03.iterrows():
            if abs(z - row["z"]) < 0.005 and abs(h - row["Hz"]) < 1.0:
                idx.append(i)
                break
    return np.array(idx)


def build_h33(h_moresco_override: np.ndarray | None, idx: np.ndarray) -> np.ndarray:
    Hd = Hd_bc03.copy()
    if h_moresco_override is not None:
        Hd[idx] = h_moresco_override
    return np.concatenate([Hd, [H_SHOES], [H_DESI]])


def chi2_fn(H33_local, h0_anchor, beta1, beta2):
    Hm = H_of_z_kms(ZFINE, h0_anchor, beta1, beta2, Z_SHOES)
    if np.any(np.isnan(Hm)):
        return 1e12
    Hp = np.interp(z33, ZFINE, Hm)
    return np.sum(((Hp - H33_local) / s33) ** 2)


def opt_multing(H33_local: np.ndarray, x0: tuple[float, float, float]):
    h0, b1, b2 = x0

    def f(p):
        return chi2_fn(H33_local, p[0], p[1] * b1, p[2] * b2)

    res = minimize(
        f,
        (h0, 1.0, 1.0),
        method="Nelder-Mead",
        options={"xatol": 1e-8, "fatol": 1e-9, "maxiter": 20000},
    )
    return res.fun, (res.x[0], res.x[1] * b1, res.x[2] * b2)


def main() -> None:
    print("Fetching BC03 and M11 tables live...")
    bc03 = fetch_table(BC03_URL)
    m11 = fetch_table(M11_URL)
    print(f"  BC03: {len(bc03)} rows, M11: {len(m11)} rows")

    idx = moresco_indices(bc03)
    print(f"\nMatched {len(idx)} of TJB's 31 CC_POINTS to Moresco's BC03 table")
    assert len(idx) == 15, f"expected 15 Moresco points, matched {len(idx)}"

    # Match each of the 15 BC03-identified points to its M11 counterpart by z
    h_m11_at_matched = np.array([m11.loc[(m11["z"] - zd[i]).abs().idxmin(), "Hz"] for i in idx])
    max_z_mismatch = max(abs(m11.loc[(m11["z"] - zd[i]).abs().idxmin(), "z"] - zd[i]) for i in idx)
    print(f"Max |z| mismatch when matching BC03 point to its M11 counterpart: {max_z_mismatch:.5f}")
    assert max_z_mismatch < 0.001, "BC03/M11 tables are not on the identical z grid as assumed"

    shift_pct = 100.0 * (h_m11_at_matched / Hd_bc03[idx] - 1.0)
    print(
        f"H(z) shift BC03->M11 on these 15 points: mean={shift_pct.mean():.2f}%, "
        f"median={np.median(shift_pct):.2f}%"
    )

    print("\n=== Positive control: BC03 refit must reproduce TJB's own Table II ===")
    H33_bc03 = build_h33(None, idx)
    x0 = TABLE_II["unconstrained_spotlighted"][:3]
    f_bc03, params_bc03 = opt_multing(H33_bc03, x0)
    tjb_chi2 = TABLE_II["unconstrained_spotlighted"][3]
    print(
        f"BC03 refit: chi2={f_bc03:.4f} @ H0_anchor={params_bc03[0]:.3f}, "
        f"beta1={params_bc03[1]:.4e}, beta2={params_bc03[2]:.4e}"
    )
    print(
        f"TJB's own published: chi2={tjb_chi2}, H0_anchor={x0[0]}, beta1={x0[1]:.4e}, beta2={x0[2]:.4e}"
    )
    assert abs(f_bc03 - tjb_chi2) <= 0.01 + 1e-6, (
        f"POSITIVE CONTROL FAILED: refit chi2={f_bc03:.4f} vs TJB's {tjb_chi2} -- "
        "pipeline does not reproduce his own published fit, do not trust the M11 result below"
    )
    print("Positive control: PASS (refit matches TJB's own Table II to <=0.01 in chi2)")

    print("\n=== M11-substituted refit ===")
    H33_m11 = build_h33(h_m11_at_matched, idx)
    # Convergence check: restart from 3 different Table II rows, per E8b's
    # own convention ("requiring agreement" across independent starts).
    starts = {
        "unconstrained_spotlighted": TABLE_II["unconstrained_spotlighted"][:3],
        "sh0es_anchored_0pct": TABLE_II["sh0es_anchored_0pct"][:3],
        "planck_exact_100pct": TABLE_II["planck_exact_100pct"][:3],
    }
    results = {}
    for name, start in starts.items():
        f_m11, params_m11 = opt_multing(H33_m11, start)
        results[name] = (f_m11, params_m11)
        print(
            f"  start={name:28s} -> chi2={f_m11:.4f} @ H0_anchor={params_m11[0]:.3f}, "
            f"beta1={params_m11[1]:.4e}, beta2={params_m11[2]:.4e}"
        )

    chi2s = [r[0] for r in results.values()]
    best_name = min(results, key=lambda k: results[k][0])
    f_m11_best, params_m11_best = results[best_name]
    spread = max(chi2s) - min(chi2s)
    print(f"\nBest M11 refit (from start '{best_name}'): chi2={f_m11_best:.4f}")
    print(
        f"Spread in chi2 across the 3 independent starts: {spread:.4f} "
        f"({'consistent -- real global optimum' if spread < 0.01 else 'DID NOT CONVERGE CONSISTENTLY'})"
    )

    print("\n=== Headline: does the table swap materially change the fit? ===")
    dchi2 = f_bc03 - f_m11_best
    dH0 = params_m11_best[0] - params_bc03[0]
    db1_pct = 100.0 * (params_m11_best[1] / params_bc03[1] - 1.0)
    db2_pct = 100.0 * (params_m11_best[2] / params_bc03[2] - 1.0)
    print(
        f"Delta chi2 (BC03 - M11 best-fit)     = {dchi2:+.4f}  (MCID={MCID_DCHI2}, pre-registered in CLAIM_E8)"
    )
    print(f"Delta H0_anchor                      = {dH0:+.3f} km/s/Mpc")
    print(f"Delta beta1 (%)                       = {db1_pct:+.2f}%")
    print(f"Delta beta2 (%)                       = {db2_pct:+.2f}%")
    verdict = "MATERIAL" if abs(dchi2) >= MCID_DCHI2 else "NOT MATERIAL"
    print(f"\nVerdict by the pre-registered chi2 MCID: {verdict}")


if __name__ == "__main__":
    main()
