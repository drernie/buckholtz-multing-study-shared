"""
Extends moresco_bc03_vs_m11_refit.py's central-value-only BC03-vs-M11 swap
with Moresco's own full, correlated systematic covariance (E8's recipe),
instead of the diagonal sigma_Hz everyone -- this project included -- has
been using. Answers the natural follow-up the earlier script's own honest
caveat implied: does the materiality verdict survive once the modelling
covariance (100% correlated across z, NOT in the quoted errHz column,
per FINDING_E5) is actually propagated, rather than just swapping central
values under diagonal errors?

Reuses, does not reinvent: fetch_mm20/build_cov_cc/embed_33/moresco_mask
from E8_full_covariance_propagation.py (already positive-control-verified
against TJB's own Table II and against fixed/free LCDM); opt_multing from
E8b_reoptimize_under_covariance.py (rescaled Nelder-Mead, already
positive-control-verified to recover TJB's own optima).

Design choice, stated explicitly: the SAME covariance matrix (Moresco's
own default recipe, representing the community's modelling-uncertainty
BUDGET, not a specific SPS choice) is used for both the BC03 and the
M11-substituted evaluation. This isolates the effect of adding correlated
covariance on top of today's already-computed central-value shift -- it
does not ask whether M11 "deserves" a different covariance recipe than
BC03, which is a separate, harder question this script does not attempt.

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
from P176_v82_real_chi2_hessian_degeneracy import (  # noqa: E402
    CC_POINTS,
    H_DESI,
    H_SHOES,
    TABLE_II,
    Z_DESI,
    Z_SHOES,
    H_of_z_kms,
    chi2_fixed_h0anchor,
)
from scipy.linalg import cho_factor, cho_solve

BC03_URL = "https://gitlab.com/mmoresco/CCcovariance/-/raw/master/data/HzTable_MM_BC03.dat"
M11_URL = "https://gitlab.com/mmoresco/CCcovariance/-/raw/master/data/HzTable_MM_M11.dat"
MCID_DCHI2 = 2.0

zd = np.array([p[0] for p in CC_POINTS])
Hd_bc03 = np.array([p[1] for p in CC_POINTS])
z33 = np.concatenate([zd, [Z_SHOES], [Z_DESI]])
ZFINE = np.sort(np.unique(np.concatenate([np.linspace(0, Z_DESI, 500), z33])))


def fetch_table(url: str):
    import pandas as pd

    r = requests.get(url, timeout=30)
    r.raise_for_status()
    lines = [ln for ln in r.text.strip().splitlines() if ln.strip() and not ln.startswith("#")]
    rows = [ln.split(",") for ln in lines]
    df = pd.DataFrame(rows).iloc[:, :3]
    df.columns = ["z", "Hz", "errHz"]
    return df.astype({"z": float, "Hz": float, "errHz": float})


def make_chi2_cov_target(C33: np.ndarray, target33: np.ndarray):
    """Same recipe as E8's make_chi2_cov, but parameterized over an explicit
    33-length target vector instead of hardcoding P176's own module-level
    H33 -- lets the same covariance factorization score BC03's own target
    and the M11-substituted target with a single, shared implementation."""
    cf = cho_factor(C33)

    def chi2(h0a: float, b1: float, b2: float) -> float:
        Hm = H_of_z_kms(ZFINE, h0a, b1, b2, Z_SHOES)
        if np.any(np.isnan(Hm)):
            return 1e12
        r = np.interp(z33, ZFINE, Hm) - target33
        return float(r @ cho_solve(cf, r))

    return chi2


def main() -> None:
    print("Fetching BC03, M11, and Moresco's own systematic-budget table (data_MM20.dat)...")
    m11 = fetch_table(M11_URL)
    mm20 = fetch_mm20()
    mask = moresco_mask()
    assert mask.sum() == 15, f"expected 15 Moresco points, got {mask.sum()}"

    idx = np.where(mask)[0]
    h_m11_at_matched = np.array([m11.loc[(m11["z"] - zd[i]).abs().idxmin(), "Hz"] for i in idx])

    Hd_m11 = Hd_bc03.copy()
    Hd_m11[idx] = h_m11_at_matched

    target_bc03 = np.concatenate([Hd_bc03, [H_SHOES], [H_DESI]])
    target_m11 = np.concatenate([Hd_m11, [H_SHOES], [H_DESI]])

    print("\n=== Positive control 1: diagonal chi2 must reproduce TJB's Table II ===")
    x0 = TABLE_II["unconstrained_spotlighted"][:3]
    c0 = chi2_fixed_h0anchor(*x0)
    tjb_chi2 = TABLE_II["unconstrained_spotlighted"][3]
    assert abs(c0 - tjb_chi2) <= 0.01 + 1e-6, (c0, tjb_chi2)
    print(f"Diagonal chi2 at TJB's own optimum: {c0:.4f} vs TJB's {tjb_chi2}: PASS")

    variants = {
        "Moresco default [spsooo+imf], only his 15 correlated": (["spsooo", "imf"], mask),
        "Moresco default [spsooo+imf], all 31 correlated": (["spsooo", "imf"], None),
    }

    starts = ["unconstrained_spotlighted", "sh0es_anchored_0pct", "planck_exact_100pct"]

    print("\n" + "=" * 100)
    print("Refit under FULL COVARIANCE, BC03 vs M11-substituted (15 Moresco-matched points)")
    print("=" * 100)

    results = {}
    for vname, (comps, corr_mask) in variants.items():
        print(f"\n--- Covariance variant: {vname} ---")
        C33 = embed_33(build_cov_cc(mm20, comps, corr_mask))

        chi2_bc03 = make_chi2_cov_target(C33, target_bc03)  # cho_factor inside -> PC2: SPD check
        chi2_m11 = make_chi2_cov_target(C33, target_m11)
        print("PC2: Cholesky factorization of C33 succeeded (SPD covariance): PASS")

        outs_bc03 = sorted(opt_multing(chi2_bc03, TABLE_II[s][:3]) for s in starts)
        f_bc03, p_bc03 = outs_bc03[0]
        conv_bc03 = "ok" if abs(outs_bc03[1][0] - outs_bc03[0][0]) < 0.05 else "WARN-NOCONV"
        print(
            f"BC03 (full cov): chi2={f_bc03:.4f} @ H0_anchor={p_bc03[0]:.3f}, "
            f"beta1={p_bc03[1]:.4e}, beta2={p_bc03[2]:.4e}  [{conv_bc03}]"
        )

        outs_m11 = sorted(opt_multing(chi2_m11, TABLE_II[s][:3]) for s in starts)
        f_m11, p_m11 = outs_m11[0]
        conv_m11 = "ok" if abs(outs_m11[1][0] - outs_m11[0][0]) < 0.05 else "WARN-NOCONV"
        print(
            f"M11  (full cov): chi2={f_m11:.4f} @ H0_anchor={p_m11[0]:.3f}, "
            f"beta1={p_m11[1]:.4e}, beta2={p_m11[2]:.4e}  [{conv_m11}]"
        )

        dchi2 = f_bc03 - f_m11
        dH0 = p_m11[0] - p_bc03[0]
        db1_pct = 100.0 * (p_m11[1] / p_bc03[1] - 1.0)
        db2_pct = 100.0 * (p_m11[2] / p_bc03[2] - 1.0)
        verdict = "MATERIAL" if abs(dchi2) >= MCID_DCHI2 else "NOT MATERIAL"
        print(
            f"Delta chi2 (BC03-M11) = {dchi2:+.4f}  Delta H0_anchor = {dH0:+.3f}  "
            f"Delta b1 = {db1_pct:+.2f}%  Delta b2 = {db2_pct:+.2f}%  -> {verdict}"
        )
        results[vname] = {
            "chi2_bc03": f_bc03,
            "chi2_m11": f_m11,
            "dchi2": dchi2,
            "conv": (conv_bc03, conv_m11),
            "verdict": verdict,
        }

    print("\n" + "=" * 100)
    print(
        "SUMMARY -- comparison against today's diagonal-only result (Delta_chi2 = -5.91, MATERIAL)"
    )
    print("=" * 100)
    for vname, r in results.items():
        print(f"{vname}: Delta_chi2={r['dchi2']:+.4f} -> {r['verdict']}  conv={r['conv']}")


if __name__ == "__main__":
    main()
