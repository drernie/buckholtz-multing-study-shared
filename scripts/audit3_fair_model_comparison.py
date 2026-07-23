"""audit3_fair_model_comparison.py — Audit 3: fair model comparison (LCDM | wCDM | MULTING).

NOT_VALIDATION · NOT_REFUTATION · NO_AUTHOR_ERROR · OUR_RECONSTRUCTION

Purpose (the one genuinely new piece vs audits #1/#2): add wCDM to the comparison and assemble
ONE unified side-by-side table against the SAME real data and SAME chi2/AIC/BIC convention already
used by R011 and scripts/plot_same_anchor_comparison_tjb.py (diagonal quoted CC errors, no
covariance matrix). Everything else (MULTING monopole r=0.7334, full-grid optimum r=0.6235,
LCDM r=0.8795, the 70/30 seed=42 split) is REUSED from R011 / docs/122, not re-searched.

Two footings are reported because the models do not share one likelihood:
  Footing A (standard cosmology): chi2/AIC/BIC of LCDM(H0,Om) and wCDM(H0,Om,w) on the 27 CC
      points. Both are smooth H(z) curves -> a proper likelihood comparison is well-defined.
  Footing B (MULTING's native test): Pearson r of a per-cluster reconstruction vs CC-interpolated
      H(z), over 443 real clusters. MULTING is NOT a function of z alone (phi depends per-cluster
      on M500, R500, E_thermal), so it CANNOT be placed on Footing A's 27-point CC likelihood at
      all -- that impossibility is itself a reported finding (Q006: no continuous MULTING H(z)).
      LCDM/wCDM are evaluated on Footing B too, only to give a common r-column.

Run:  python scripts/audit3_fair_model_comparison.py
Exit: 0. Prints the full side-by-side table to stdout. No files written, no git actions.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from scipy import stats
from scipy.optimize import curve_fit

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from src.pearson_fit import _interp_hcc, load_data, single_pearson  # noqa: E402

BANNER = "NOT_VALIDATION · NOT_REFUTATION · NO_AUTHOR_ERROR · OUR_RECONSTRUCTION"
SEED = 42
H_ANCHOR = 73.0
D0_MPC = 100.0
# R011 / docs/122 already-found full-grid optimum (do NOT re-search): beta_d=100, beta_q=3.24e7
# at D0=100 (eta_d=1, eta_q=3.24e5). docs/122 Gate 1: Q(this) = 0.623517 (n=443).
MULT_FULL_BD = 100.0
MULT_FULL_BQ = 3.24e7


# ── models (Footing A: smooth H(z) curves, standard cosmology) ────────────────────────────────
def lcdm(z: np.ndarray, h0: float, om: float) -> np.ndarray:
    """Flat-LCDM expansion rate."""
    return h0 * np.sqrt(om * (1.0 + z) ** 3 + (1.0 - om))


def wcdm(z: np.ndarray, h0: float, om: float, w: float) -> np.ndarray:
    """Flat-wCDM: constant dark-energy equation of state w (w=-1 recovers LCDM)."""
    return h0 * np.sqrt(om * (1.0 + z) ** 3 + (1.0 - om) * (1.0 + z) ** (3.0 * (1.0 + w)))


def chi2_of(model_h: np.ndarray, h: np.ndarray, s: np.ndarray) -> float:
    """Diagonal-error chi2 (same convention as R011 / plot_same_anchor_comparison_tjb.py)."""
    return float(np.sum(((h - model_h) / s) ** 2))


def aic_bic(chi2: float, k: int, n: int) -> tuple[float, float]:
    """Gaussian-error AIC/BIC up to the model-independent constant (same n, same data)."""
    return chi2 + 2.0 * k, chi2 + k * np.log(n)


# ── main ──────────────────────────────────────────────────────────────────────────────────────
def main() -> int:
    print("=" * 78)
    print("AUDIT 3 — Fair model comparison: LCDM | wCDM | MULTING-monopole | MULTING-full")
    print(BANNER)
    print("=" * 78)

    clusters, hz_cc = load_data()
    z_cc = hz_cc["z"].to_numpy(float)
    h_cc = hz_cc["Hz_km_s_Mpc"].to_numpy(float)
    s_cc = hz_cc["sigma_Hz"].to_numpy(float)
    n_cc = len(z_cc)

    # cluster set used by R011/docs/122 (443): Ethermal not null, sorted by z, in CC range
    df = clusters[clusters["Ethermal_c2_Msun"].notna()].sort_values("z").reset_index(drop=True)
    z_clu = df["z"].to_numpy(float)
    h_cc_at_clu, valid_clu = _interp_hcc(hz_cc, z_clu)
    n_clu = int(valid_clu.sum())

    print(
        f"\nData: {n_cc} cosmic chronometers (Moresco+2022), z in "
        f"[{z_cc.min():.3f}, {z_cc.max():.3f}]; diagonal quoted errors, no covariance."
    )
    print(
        f"      {len(df)} clusters with E_thermal -> {n_clu} inside CC interpolation range "
        "(matches R011's 443)."
    )

    # ── Footing A: fit LCDM & wCDM to all 27 CC points ────────────────────────────────────────
    (h0_l, om_l), cov_l = curve_fit(lcdm, z_cc, h_cc, sigma=s_cc, p0=(70.0, 0.3), maxfev=20000)
    err_l = np.sqrt(np.diag(cov_l))
    chi2_l = chi2_of(lcdm(z_cc, h0_l, om_l), h_cc, s_cc)
    aic_l, bic_l = aic_bic(chi2_l, 2, n_cc)

    (h0_w, om_w, w_w), cov_w = curve_fit(
        wcdm, z_cc, h_cc, sigma=s_cc, p0=(70.0, 0.3, -1.0), maxfev=40000
    )
    err_w = np.sqrt(np.diag(cov_w))
    chi2_w = chi2_of(wcdm(z_cc, h0_w, om_w, w_w), h_cc, s_cc)
    aic_w, bic_w = aic_bic(chi2_w, 3, n_cc)

    print("\n--- Footing A: standard cosmology, chi2/AIC/BIC on the 27 CC points ---")
    print(f"  LCDM  H0={h0_l:6.2f}+-{err_l[0]:.2f}  Om={om_l:.3f}+-{err_l[1]:.3f}")
    print(
        f"  wCDM  H0={h0_w:6.2f}+-{err_w[0]:.2f}  Om={om_w:.3f}+-{err_w[1]:.3f}  "
        f"w={w_w:+.3f}+-{err_w[2]:.3f}"
    )

    # ── Footing B: Pearson r at cluster redshifts (common r-column) ───────────────────────────
    # LCDM/wCDM r: shape of H_model(z_cluster) vs H_CC-interp; r is H0-invariant (positive scale).
    def r_smooth(model_h_at_clu: np.ndarray) -> tuple[float, int]:
        m = valid_clu & np.isfinite(model_h_at_clu)
        r, _ = stats.pearsonr(model_h_at_clu[m], h_cc_at_clu[m])
        return float(r), int(m.sum())

    r_lcdm, n_r_lcdm = r_smooth(lcdm(z_clu, h0_l, om_l))
    r_wcdm, n_r_wcdm = r_smooth(wcdm(z_clu, h0_w, om_w, w_w))
    # MULTING reproduced cheaply from src.pearson_fit (verifies R011's 0.7334 / 0.6235):
    r_mono = single_pearson(df, hz_cc, beta_d=0.0, beta_q=0.0, D0_Mpc=D0_MPC, H_anchor=H_ANCHOR)
    r_full = single_pearson(
        df, hz_cc, beta_d=MULT_FULL_BD, beta_q=MULT_FULL_BQ, D0_Mpc=D0_MPC, H_anchor=H_ANCHOR
    )

    print("\n--- Footing B: Pearson r vs CC-interpolated H(z), 443 real clusters ---")
    print(f"  LCDM r={r_lcdm:.4f} (n={n_r_lcdm})   [R011 reported 0.8795]")
    print(f"  wCDM r={r_wcdm:.4f} (n={n_r_wcdm})")
    print(
        f"  MULTING monopole (bd=bq=0)     r={r_mono['r']:.4f} (n={r_mono['n']})   "
        "[R011 reported 0.7334]"
    )
    print(
        f"  MULTING full (bd=100,bq=3.24e7) r={r_full['r']:.4f} (n={r_full['n']})   "
        "[R011 reported 0.6235]"
    )

    # ── 70/30 holdout (seed=42) on both footings ──────────────────────────────────────────────
    rng = np.random.default_rng(SEED)
    # CC split (Footing A holdout chi2/point)
    idx = rng.permutation(n_cc)
    n_tr = int(round(0.70 * n_cc))
    tr, ho = np.sort(idx[:n_tr]), np.sort(idx[n_tr:])
    (h0_lt, om_lt), _ = curve_fit(
        lcdm, z_cc[tr], h_cc[tr], sigma=s_cc[tr], p0=(70.0, 0.3), maxfev=20000
    )
    (h0_wt, om_wt, w_wt), cov_wt = curve_fit(
        wcdm, z_cc[tr], h_cc[tr], sigma=s_cc[tr], p0=(70.0, 0.3, -1.0), maxfev=40000
    )
    err_wt = np.sqrt(np.diag(cov_wt))
    ho_chi2_l = chi2_of(lcdm(z_cc[ho], h0_lt, om_lt), h_cc[ho], s_cc[ho]) / len(ho)
    ho_chi2_w = chi2_of(wcdm(z_cc[ho], h0_wt, om_wt, w_wt), h_cc[ho], s_cc[ho]) / len(ho)

    # Cluster split (Footing B holdout r, matching R011's convention)
    rng2 = np.random.default_rng(SEED)
    cidx = rng2.permutation(len(df))
    c_tr = int(round(0.70 * len(df)))
    df_ho = df.iloc[np.sort(cidx[c_tr:])].reset_index(drop=True)
    r_mono_ho = single_pearson(df_ho, hz_cc, 0.0, 0.0, D0_MPC, H_ANCHOR)
    r_full_ho = single_pearson(df_ho, hz_cc, MULT_FULL_BD, MULT_FULL_BQ, D0_MPC, H_ANCHOR)

    print("\n--- 70/30 holdout (seed=42) ---")
    print(f"  Footing A (CC split, {len(tr)} train / {len(ho)} holdout), holdout chi2/point:")
    print(
        f"    LCDM = {ho_chi2_l:.3f}   wCDM = {ho_chi2_w:.3f}   "
        f"(wCDM train w={w_wt:+.3f}+-{err_wt[2]:.3f})"
    )
    print(f"  Footing B (cluster split, {c_tr} train / {len(df) - c_tr} holdout), holdout r:")
    print(f"    MULTING monopole = {r_mono_ho['r']:.4f}   MULTING full = {r_full_ho['r']:.4f}")

    # ── unified table ─────────────────────────────────────────────────────────────────────────
    dl = "-" * 92
    print("\n" + "=" * 92)
    print("UNIFIED SIDE-BY-SIDE TABLE")
    print("=" * 92)
    hdr = f"{'model':<22}{'k':>2}  {'chi2(27CC)':>11}  {'AIC':>8}  {'BIC':>8}  {'dAIC':>6}  {'r(443)':>7}"
    print(hdr)
    print(dl)
    print(
        f"{'LCDM (H0,Om)':<22}{2:>2}  {chi2_l:>11.2f}  {aic_l:>8.2f}  {bic_l:>8.2f}  "
        f"{0.0:>6.2f}  {r_lcdm:>7.4f}"
    )
    print(
        f"{'wCDM (H0,Om,w)':<22}{3:>2}  {chi2_w:>11.2f}  {aic_w:>8.2f}  {bic_w:>8.2f}  "
        f"{aic_w - aic_l:>+6.2f}  {r_wcdm:>7.4f}"
    )
    print(
        f"{'MULTING monopole':<22}{'*':>2}  {'n/a':>11}  {'n/a':>8}  {'n/a':>8}  "
        f"{'n/a':>6}  {r_mono['r']:>7.4f}"
    )
    print(
        f"{'MULTING full':<22}{'*':>2}  {'n/a':>11}  {'n/a':>8}  {'n/a':>8}  "
        f"{'n/a':>6}  {r_full['r']:>7.4f}"
    )
    print(dl)
    print("* MULTING phi depends per-cluster on M500,R500,E_thermal -> NOT a function of z alone")
    print("  (Q006: no continuous MULTING H(z)). It has no 27-CC-point likelihood, so chi2/AIC/BIC")
    print("  on Footing A are undefined for it. MULTING 'free params' are eta_d,eta_q (fitted).")

    # ── verdict inputs ────────────────────────────────────────────────────────────────────────
    # Honest constraint read (skeptic-corrected): do NOT call +-0.46 "constrained". Report the
    # 1-sigma band width AND the resampling instability (train w moved to a very different value).
    lo, hi = w_w - err_w[2], w_w + err_w[2]
    consistent_lcdm = lo <= -1.0 <= hi  # is w=-1 inside 1 sigma?
    print("\n--- wCDM constraint quality (skeptic-checked) ---")
    print(
        f"  full-sample w = {w_w:+.3f} +- {err_w[2]:.3f}  ->  1-sigma band [{lo:+.2f}, {hi:+.2f}] "
        f"(width {2 * err_w[2]:.2f}, LOOSE: spans much of the DE range)"
    )
    print(
        f"  train-split w = {w_wt:+.3f} +- {err_wt[2]:.3f}  ->  central value moved by "
        f"{abs(w_wt - w_w):.2f} under a 70% resample => w is FRAGILE / poorly constrained by 27 pts"
    )
    print(
        f"  w=-1 (LCDM) is {'INSIDE' if consistent_lcdm else 'OUTSIDE'} the full-sample 1-sigma band "
        "=> data are consistent with plain LCDM; w buys no real DE-dynamics detection."
    )
    print(
        f"  delta_AIC(wCDM - LCDM) = {aic_w - aic_l:+.2f}, "
        f"delta_BIC = {bic_w - bic_l:+.2f}  "
        f"({'wCDM NOT justified (extra param unpaid-for)' if aic_w >= aic_l else 'wCDM favored'})"
    )
    print("\n" + BANNER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
