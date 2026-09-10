"""
Robustness check on moresco_bc03_vs_m11_refit.py's MATERIAL verdict.

FINDING_E5 (2026-09-06) flagged an UNVERIFIED caveat on exactly 2 of the 15
Moresco-matched points (z=0.7812, z=1.037): it was never checked whether the
BC03 vs M11 re-analysis held the same fit method at z>0.7 -- if not, part of
their large excursion (-15.75%, -26.48%, vs a tight +6.80% uniform shift on
the other 12/15 points) is method difference, not pure SPS choice.

Since the main script's MATERIAL verdict could be dominated by exactly these
2 flagged points, this reruns the same fit with them EXCLUDED (i.e. those 2
CC_POINTS keep their original BC03 value untouched, only the 13 "clean"
Moresco points get swapped to M11) to see whether materiality survives on
the part of the shift E5 itself called load-bearing and trustworthy.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
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
MCID_DCHI2 = 2.0
EXCURSION_Z = {0.7812, 1.037}  # FINDING_E5's own named unresolved excursions

zd = np.array([p[0] for p in CC_POINTS])
Hd_bc03 = np.array([p[1] for p in CC_POINTS])
sd = np.array([p[2] for p in CC_POINTS])
z33 = np.concatenate([zd, [Z_SHOES], [Z_DESI]])
s33 = np.concatenate([sd, [SIG_SHOES], [SIG_DESI]])
ZFINE = np.sort(np.unique(np.concatenate([np.linspace(0, Z_DESI, 500), z33])))


def fetch_table(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    import pandas as pd

    lines = [ln for ln in r.text.strip().splitlines() if ln.strip() and not ln.startswith("#")]
    rows = [ln.split(",") for ln in lines]
    df = pd.DataFrame(rows).iloc[:, :3]
    df.columns = ["z", "Hz", "errHz"]
    return df.astype({"z": float, "Hz": float, "errHz": float})


def chi2_fn(H33_local, h0_anchor, beta1, beta2):
    Hm = H_of_z_kms(ZFINE, h0_anchor, beta1, beta2, Z_SHOES)
    if np.any(np.isnan(Hm)):
        return 1e12
    Hp = np.interp(z33, ZFINE, Hm)
    return np.sum(((Hp - H33_local) / s33) ** 2)


def opt_multing(H33_local, x0):
    h0, b1, b2 = x0

    def f(p):
        return chi2_fn(H33_local, p[0], p[1] * b1, p[2] * b2)

    res = minimize(
        f, (h0, 1.0, 1.0), method="Nelder-Mead",
        options={"xatol": 1e-8, "fatol": 1e-9, "maxiter": 20000},
    )
    return res.fun, (res.x[0], res.x[1] * b1, res.x[2] * b2)


def main() -> None:
    bc03 = fetch_table(BC03_URL)
    m11 = fetch_table(M11_URL)

    idx_all = []
    for i, (z, h) in enumerate(zip(zd, Hd_bc03, strict=True)):
        for _, row in bc03.iterrows():
            if abs(z - row["z"]) < 0.005 and abs(h - row["Hz"]) < 1.0:
                idx_all.append(i)
                break
    idx_all = np.array(idx_all)

    # exclude the 2 flagged excursion points from the SUBSTITUTION (keep
    # their BC03 value), substitute M11 only on the remaining 13 "clean" pts
    idx_clean = np.array([i for i in idx_all if not any(abs(zd[i] - ez) < 0.01 for ez in EXCURSION_Z)])
    print(f"Clean (non-excursion) Moresco points used for substitution: {len(idx_clean)} of {len(idx_all)}")

    h_m11_clean = np.array([m11.loc[(m11["z"] - zd[i]).abs().idxmin(), "Hz"] for i in idx_clean])

    def build_h33(override_idx, override_vals):
        Hd = Hd_bc03.copy()
        if override_vals is not None:
            Hd[override_idx] = override_vals
        return np.concatenate([Hd, [H_SHOES], [H_DESI]])

    x0 = TABLE_II["unconstrained_spotlighted"][:3]
    H33_bc03 = build_h33(idx_all, None)
    f_bc03, params_bc03 = opt_multing(H33_bc03, x0)
    print(f"BC03 baseline: chi2={f_bc03:.4f}")

    H33_m11_clean = build_h33(idx_clean, h_m11_clean)
    f_m11_clean, params_m11_clean = opt_multing(H33_m11_clean, x0)
    print(f"M11 refit (13 clean points only, 2 excursions left at BC03): chi2={f_m11_clean:.4f}")

    dchi2 = f_bc03 - f_m11_clean
    print(f"\nDelta chi2 (BC03 - M11-clean-only) = {dchi2:+.4f}  (MCID={MCID_DCHI2})")
    print(f"Delta H0_anchor = {params_m11_clean[0] - params_bc03[0]:+.3f} km/s/Mpc")
    print(f"Delta beta1 (%) = {100*(params_m11_clean[1]/params_bc03[1]-1):+.2f}%")
    print(f"Delta beta2 (%) = {100*(params_m11_clean[2]/params_bc03[2]-1):+.2f}%")
    verdict = "MATERIAL" if abs(dchi2) >= MCID_DCHI2 else "NOT MATERIAL"
    print(f"Verdict (clean-13-points-only): {verdict}")


if __name__ == "__main__":
    main()
