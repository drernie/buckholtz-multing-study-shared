"""
Combines the two robustness angles from today's work: full-covariance
propagation (full_covariance_bc03_vs_m11.py) AND exclusion of the 2
excursion points FINDING_E5 already flagged as carrying an unverified
confound (robustness_exclude_excursions.py's diagonal-only version).

Under diagonal errors, excluding those 2 points flipped the verdict
MATERIAL -> NOT MATERIAL (Delta_chi2 -5.91 -> -0.585). This checks
whether that same flip survives once the correlated modelling covariance
is used instead of the diagonal sigma_Hz.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import requests

sys.path.insert(0, str(Path(__file__).parent.parent / "20260906-evidence-authority"))
sys.path.insert(0, str(Path(__file__).parent.parent / "20260803-bridge"))

from E8_full_covariance_propagation import (  # noqa: E402
    build_cov_cc,
    embed_33,
    fetch_mm20,
    moresco_mask,
)
from E8b_reoptimize_under_covariance import opt_multing  # noqa: E402
from full_covariance_bc03_vs_m11 import make_chi2_cov_target  # noqa: E402
from P176_v82_real_chi2_hessian_degeneracy import (  # noqa: E402
    CC_POINTS,
    H_DESI,
    H_SHOES,
    TABLE_II,
)

M11_URL = "https://gitlab.com/mmoresco/CCcovariance/-/raw/master/data/HzTable_MM_M11.dat"
MCID_DCHI2 = 2.0
EXCURSION_Z = {0.7812, 1.037}

zd = np.array([p[0] for p in CC_POINTS])
Hd_bc03 = np.array([p[1] for p in CC_POINTS])


def fetch_table(url: str):
    import pandas as pd

    r = requests.get(url, timeout=30)
    r.raise_for_status()
    lines = [ln for ln in r.text.strip().splitlines() if ln.strip() and not ln.startswith("#")]
    rows = [ln.split(",") for ln in lines]
    df = pd.DataFrame(rows).iloc[:, :3]
    df.columns = ["z", "Hz", "errHz"]
    return df.astype({"z": float, "Hz": float, "errHz": float})


def main() -> None:
    m11 = fetch_table(M11_URL)
    mm20 = fetch_mm20()
    mask_all15 = moresco_mask()
    idx_all = np.where(mask_all15)[0]

    idx_clean = np.array(
        [i for i in idx_all if not any(abs(zd[i] - ez) < 0.01 for ez in EXCURSION_Z)]
    )
    print(
        f"Clean (non-excursion) Moresco points used for substitution: {len(idx_clean)} of {len(idx_all)}"
    )

    h_m11_clean = np.array([m11.loc[(m11["z"] - zd[i]).abs().idxmin(), "Hz"] for i in idx_clean])

    Hd_m11_clean = Hd_bc03.copy()
    Hd_m11_clean[idx_clean] = h_m11_clean

    target_bc03 = np.concatenate([Hd_bc03, [H_SHOES], [H_DESI]])
    target_m11_clean = np.concatenate([Hd_m11_clean, [H_SHOES], [H_DESI]])

    variants = {
        "Moresco default [spsooo+imf], only his 15 correlated": (["spsooo", "imf"], mask_all15),
        "Moresco default [spsooo+imf], all 31 correlated": (["spsooo", "imf"], None),
    }
    starts = ["unconstrained_spotlighted", "sh0es_anchored_0pct", "planck_exact_100pct"]

    print("\n" + "=" * 100)
    print(
        "Refit under FULL COVARIANCE, BC03 vs M11 (13 clean points only, 2 excursions kept at BC03)"
    )
    print("=" * 100)

    for vname, (comps, corr_mask) in variants.items():
        print(f"\n--- Covariance variant: {vname} ---")
        C33 = embed_33(build_cov_cc(mm20, comps, corr_mask))
        chi2_bc03 = make_chi2_cov_target(C33, target_bc03)
        chi2_m11c = make_chi2_cov_target(C33, target_m11_clean)

        outs_bc03 = sorted(opt_multing(chi2_bc03, TABLE_II[s][:3]) for s in starts)
        f_bc03, p_bc03 = outs_bc03[0]
        outs_m11c = sorted(opt_multing(chi2_m11c, TABLE_II[s][:3]) for s in starts)
        f_m11c, p_m11c = outs_m11c[0]

        dchi2 = f_bc03 - f_m11c
        dH0 = p_m11c[0] - p_bc03[0]
        db1_pct = 100.0 * (p_m11c[1] / p_bc03[1] - 1.0)
        db2_pct = 100.0 * (p_m11c[2] / p_bc03[2] - 1.0)
        verdict = "MATERIAL" if abs(dchi2) >= MCID_DCHI2 else "NOT MATERIAL"
        print(
            f"BC03 (full cov): chi2={f_bc03:.4f} @ H0_anchor={p_bc03[0]:.3f}\n"
            f"M11-clean (full cov): chi2={f_m11c:.4f} @ H0_anchor={p_m11c[0]:.3f}\n"
            f"Delta chi2 = {dchi2:+.4f}  Delta H0_anchor = {dH0:+.3f}  "
            f"Delta b1 = {db1_pct:+.2f}%  Delta b2 = {db2_pct:+.2f}%  -> {verdict}"
        )

    print("\n" + "=" * 100)
    print("Reference: diagonal-only clean-13-points result was Delta_chi2=-0.585 -> NOT MATERIAL")
    print("=" * 100)


if __name__ == "__main__":
    main()
