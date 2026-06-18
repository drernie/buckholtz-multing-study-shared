"""
pearson_fit.py — MULTING Pearson r test on MCXC+PSZ2 cluster data.
NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

TJB Step 4: Pearson r between H_MULTING(z) and H_CC(z).

Physical basis for D(z):
  D = D_0/(1+z)  [proper inter-cluster scale; decreases with z → phi increases]
  phi = M500/D² - 2·T_i·β_d·R500/D³ + (T_i·β_q·R500)²/D⁴
  H_MULTING[i] = H_0 · sqrt(phi[i] / phi_ref)   ref = lowest-z cluster

G1 BLOCKER (from HD-MAVP audit): analytic bridge F_oP→H(z) is not derived
in the preprint. D=D_0/(1+z) is our phenomenological hypothesis only.
All β values obtained here are OUR_RECONSTRUCTION, not TJB-endorsed.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import interpolate, stats

sys.path.insert(0, str(Path(__file__).parent.parent))

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

_NOT_VALIDATION = "NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION"
_DATA_DIR = Path(__file__).parent.parent / "data"


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    clusters = pd.read_csv(_DATA_DIR / "clusters_clean.csv")
    hz_cc = pd.read_csv(_DATA_DIR / "hz_cc.csv")
    return clusters, hz_cc


def _interp_hcc(hz_cc: pd.DataFrame, z_arr: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Interpolate H_CC at cluster redshifts. Returns (H_cc_interp, valid_mask)."""
    z_cc = hz_cc["z"].values
    Hz_cc = hz_cc["Hz_km_s_Mpc"].values
    z_min, z_max = z_cc.min(), z_cc.max()
    f = interpolate.interp1d(z_cc, Hz_cc, kind="linear", bounds_error=False, fill_value=np.nan)
    H_cc = f(z_arr)
    in_range = (z_arr >= z_min) & (z_arr <= z_max)
    valid = np.isfinite(H_cc) & in_range
    return H_cc, valid


def grid_search_pearson(
    df: pd.DataFrame,
    hz_cc: pd.DataFrame,
    beta_d_log_range: tuple[float, float] = (2.0, 8.0),
    beta_q_log_range: tuple[float, float] = (2.0, 8.0),
    D0_Mpc: float = 100.0,
    n_pts: int = 50,
    H_anchor: float = 73.0,
    label: str = "",
) -> dict:
    """
    Grid search over (beta_d, beta_q) to maximize Pearson r(H_MULTING, H_CC).
    D = D0_Mpc/(1+z) for all clusters.
    """
    z = df["z"].values
    m_A = df["M500c_Msun"].values
    k_A = df["Ethermal_c2_Msun"].values
    r_A = df["R500c_Mpc"].values

    # D decreases with z → phi increases with z → H_MULTING increases with z (matches H_CC)
    D = D0_Mpc / (1.0 + z)
    D2, D3, D4 = D**2, D**3, D**4

    # Precompute per-cluster coefficients (independent of beta)
    term_m = m_A / D2  # monopole: doesn't depend on beta
    coeff_d = 2.0 * k_A * r_A / D3  # dipole: multiply by beta_d
    coeff_q2 = (k_A * r_A) ** 2 / D4  # quadrupole: multiply by beta_q²

    # Interpolate H_CC once
    H_cc_at_z, valid_cc = _interp_hcc(hz_cc, z)
    if valid_cc.sum() < 5:
        return {"r": np.nan, "n": 0, "label": label}

    bd_vals = np.logspace(beta_d_log_range[0], beta_d_log_range[1], n_pts)
    bq_vals = np.logspace(beta_q_log_range[0], beta_q_log_range[1], n_pts)

    best_r = -2.0
    best_bd = np.nan
    best_bq = np.nan
    best_n = 0

    for bd in bd_vals:
        for bq in bq_vals:
            phi = term_m - bd * coeff_d + bq**2 * coeff_q2
            pos = np.isfinite(phi) & (phi > 0)
            if pos.sum() < 5:
                continue
            phi_ref = phi[pos][0]  # lowest-z cluster as anchor
            H_m = np.where(pos, H_anchor * np.sqrt(np.maximum(phi / phi_ref, 0.0)), np.nan)
            final = pos & valid_cc & np.isfinite(H_m) & (H_m > 0) & (H_m < 1e6)
            n = final.sum()
            if n < 5:
                continue
            r_val, p_val = stats.pearsonr(H_m[final], H_cc_at_z[final])
            if np.isfinite(r_val) and r_val > best_r:
                best_r = r_val
                best_bd = bd
                best_bq = bq
                best_n = n

    return {
        "r": float(best_r),
        "beta_d": float(best_bd),
        "beta_q": float(best_bq),
        "n": best_n,
        "D0_Mpc": D0_Mpc,
        "label": label,
    }


def single_pearson(
    df: pd.DataFrame,
    hz_cc: pd.DataFrame,
    beta_d: float,
    beta_q: float,
    D0_Mpc: float,
    H_anchor: float = 73.0,
) -> dict:
    """Pearson r for a single (beta_d, beta_q, D0) triplet."""
    z = df["z"].values
    m_A = df["M500c_Msun"].values
    k_A = df["Ethermal_c2_Msun"].values
    r_A = df["R500c_Mpc"].values
    D = D0_Mpc / (1.0 + z)
    D2, D3, D4 = D**2, D**3, D**4
    phi = m_A / D2 - 2.0 * beta_d * k_A * r_A / D3 + (beta_q * k_A * r_A) ** 2 / D4
    pos = np.isfinite(phi) & (phi > 0)
    if pos.sum() < 5:
        return {"r": np.nan, "n": 0}
    phi_ref = phi[pos][0]
    H_m = np.where(pos, H_anchor * np.sqrt(np.maximum(phi / phi_ref, 0.0)), np.nan)
    H_cc_at_z, valid_cc = _interp_hcc(hz_cc, z)
    final = pos & valid_cc & np.isfinite(H_m) & (H_m > 0) & (H_m < 1e6)
    if final.sum() < 5:
        return {"r": np.nan, "n": 0}
    r_val, p_val = stats.pearsonr(H_m[final], H_cc_at_z[final])
    return {"r": float(r_val), "p": float(p_val), "n": int(final.sum())}


def main() -> None:
    log.info(_NOT_VALIDATION)
    log.info("=" * 60)
    clusters, hz_cc = load_data()

    # Use clusters with E_thermal (Path B from PSZ2), sorted by z
    df = clusters[clusters["Ethermal_c2_Msun"].notna()].sort_values("z").reset_index(drop=True)
    log.info(f"Clusters with T_i = E_thermal/c²: {len(df)}")
    log.info(f"  z range: {df['z'].min():.3f} – {df['z'].max():.3f}")
    log.info(
        f"  T_i range: {df['Ethermal_c2_Msun'].min():.2e} – {df['Ethermal_c2_Msun'].max():.2e} M_sun"
    )
    log.info(f"  CC H(z) points: {len(hz_cc)}")

    # ── Baseline: TJB AI-generated β with D=D_0/(1+z), D_0=100 Mpc ───────────
    log.info("\n[1] TJB AI values: β_d=4.5, β_q=18.0 — D=100/(1+z) Mpc")
    res_tjb = single_pearson(df, hz_cc, beta_d=4.5, beta_q=18.0, D0_Mpc=100.0)
    log.info(f"    Pearson r = {res_tjb['r']:.4f}  (n={res_tjb['n']} pairs)")
    log.info("    NOTE: β from TJB AI estimates; T_i from real PSZ2 Y_SZ — scale mismatch expected")

    # ── Grid search: D_0=100 Mpc (fixed), wide beta range ─────────────────────
    log.info("\n[2] Grid search: D_0=100 Mpc, β range=[1e2, 1e8] × 50×50")
    res_100 = grid_search_pearson(
        df,
        hz_cc,
        beta_d_log_range=(2.0, 8.0),
        beta_q_log_range=(2.0, 8.0),
        D0_Mpc=100.0,
        n_pts=50,
        label="D0=100Mpc",
    )
    log.info(f"    Best r = {res_100['r']:.4f}")
    log.info(f"    β_d = {res_100['beta_d']:.3e}, β_q = {res_100['beta_q']:.3e}")
    log.info(f"    n pairs = {res_100['n']}")

    # ── Grid search: D_0=50 Mpc ────────────────────────────────────────────────
    log.info("\n[3] Grid search: D_0=50 Mpc, β range=[1e2, 1e8] × 50×50")
    res_50 = grid_search_pearson(
        df,
        hz_cc,
        beta_d_log_range=(2.0, 8.0),
        beta_q_log_range=(2.0, 8.0),
        D0_Mpc=50.0,
        n_pts=50,
        label="D0=50Mpc",
    )
    log.info(f"    Best r = {res_50['r']:.4f}")
    log.info(f"    β_d = {res_50['beta_d']:.3e}, β_q = {res_50['beta_q']:.3e}")
    log.info(f"    n pairs = {res_50['n']}")

    # ── Grid search: D_0=200 Mpc ───────────────────────────────────────────────
    log.info("\n[4] Grid search: D_0=200 Mpc, β range=[1e2, 1e8] × 50×50")
    res_200 = grid_search_pearson(
        df,
        hz_cc,
        beta_d_log_range=(2.0, 8.0),
        beta_q_log_range=(2.0, 8.0),
        D0_Mpc=200.0,
        n_pts=50,
        label="D0=200Mpc",
    )
    log.info(f"    Best r = {res_200['r']:.4f}")
    log.info(f"    β_d = {res_200['beta_d']:.3e}, β_q = {res_200['beta_q']:.3e}")
    log.info(f"    n pairs = {res_200['n']}")

    # ── Summary ────────────────────────────────────────────────────────────────
    best_overall = max(
        [res_100, res_50, res_200], key=lambda x: x["r"] if np.isfinite(x["r"]) else -999
    )
    log.info("\n" + "=" * 60)
    log.info(_NOT_VALIDATION)
    log.info(f"BEST Pearson r = {best_overall['r']:.4f}")
    log.info(f"  β_d = {best_overall['beta_d']:.3e}")
    log.info(f"  β_q = {best_overall['beta_q']:.3e}")
    log.info(f"  D_0 = {best_overall['D0_Mpc']:.0f} Mpc")
    log.info(f"  n pairs = {best_overall['n']}")
    log.info("")
    log.info("INTERPRETATION (OUR_RECONSTRUCTION):")
    r = best_overall["r"]
    if np.isfinite(r):
        if r > 0.85:
            log.info("  Strong positive correlation — MULTING structure consistent with H_CC data")
        elif r > 0.6:
            log.info("  Moderate positive correlation — partial consistency with H_CC data")
        elif r > 0:
            log.info("  Weak positive correlation — further β optimization needed")
        else:
            log.info("  Negative/zero correlation — D(z) hypothesis may need revision")
    log.info("")
    log.info("CAVEATS:")
    log.info("  [G1 BLOCKER] D=D_0/(1+z) is phenomenological — not from TJB derivation")
    log.info("  [G2 BLOCKER] β values are fitted, not derived from first principles")
    log.info("  T_i from PSZ2 Path B (Y_SZ×D_A², ΛCDM D_A assumed)")
    log.info("  β values NOT comparable to TJB Table A1 (different k_A scale)")
    log.info("=" * 60)


if __name__ == "__main__":
    main()
