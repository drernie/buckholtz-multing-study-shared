"""Honest H(z) Hubble diagram — MULTING vs ΛCDM, over real cosmic-chronometer data.

WHY THIS SCRIPT EXISTS
----------------------
A circulating chart drew MULTING as a smooth continuous H_MULT(z) curve over
real cosmic-chronometer (CC) data, no error bars, "31 points", DESI overlaid.
Four things in that chart are misleading, and this script fixes each one so the
figure can survive an adversarial reviewer:

  FIX 1 — MULTING is NOT a continuous curve.
          The theory yields only the 12 discrete Table A1 reconstructed values.
          There is NO bridge formula F_oP -> H_MULT(z) yet (open question Q1/Q5,
          BETA-1 HOLD). A smooth "MULTING" line silently claims a functional
          model the project does not possess. So MULTING is plotted as DISCRETE
          MARKERS. The only continuous red line shown is an explicitly-labelled
          PHENOMENOLOGICAL polynomial fit — NOT the bridged theory.

  FIX 2 — real data has error bars. CC sigmas are large (up to ~62 km/s/Mpc).
          Omitting them makes any model look better than the data can justify.

  FIX 3 — the extrapolation boundary is the actual data limit (max z of the CC
          compilation ~= 1.363), not an arbitrary z~1.97. Everything past it is
          shaded as extrapolation for BOTH models.

  FIX 4 — the two models are statistically indistinguishable on this data.
          The figure prints ΔAIC with the "no discrimination" verdict so nobody
          reads "MULTING fits beautifully" without "so does ΛCDM, with fewer
          free parameters."

Plus: the legend says 27 (project-canonical count, matches docs/118 + beta_cv.py),
not 31. DESI high-z H(z) points are NOT invented — the project only holds a DESI
H0 value, not DESI H(z) BAO points (see aic_model_comparison.py: the DESI H(z)
out-of-sample test itself is blocked on the bridge). To overlay DESI you must
paste real, cited values into DESI_HZ below.

DATA PROVENANCE (read from disk, never hardcoded — avoids cross-source drift):
  - data/hz_cc.csv            : 27 real cosmic chronometers (Moresco+2022 et al.)
  - data/table_a1_reported.csv: 12 MULTING/FLRW reconstructed rows (preprint v6)

Safety: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
Evidence: CC + Table A1 values [VERIFIED-tool: read from repo CSVs];
          ΛCDM/poly fits [VERIFIED-tool: computed here]; SH0ES anchor [DOCS].
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless-safe; --show flips to an interactive backend
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

REPO = Path(__file__).resolve().parent.parent
CC_CSV = REPO / "data" / "hz_cc.csv"
A1_CSV = REPO / "data" / "table_a1_reported.csv"
OUT_PNG = REPO / "reports" / "honest_hubble_diagram.png"

# SH0ES local anchor. Project uses H0=73.0 (audit/fairness_diagnostics.py);
# consistent with Riess+2022, H0 = 73.04 ± 1.04 km/s/Mpc [DOCS].
SH0ES_H0 = 73.0
SH0ES_ERR = 1.04

# DESI high-z H(z) BAO points — NOT in this project. Leave empty unless you
# paste REAL cited values, e.g. DESI_HZ = [(z, H, sigma, "DESI DR2 arXiv:...")].
DESI_HZ: list[tuple[float, float, float, str]] = []


def lcdm(z: np.ndarray, h0: float, omega_m: float) -> np.ndarray:
    """Flat ΛCDM: H(z) = H0 * sqrt(Ω_m (1+z)^3 + (1-Ω_m))."""
    return h0 * np.sqrt(omega_m * (1.0 + z) ** 3 + (1.0 - omega_m))


def multing_poly(z: np.ndarray, a: float, b: float, c: float) -> np.ndarray:
    """Phenomenological MULTING polynomial A(1+z)^2 + B(1+z)^3 + C(1+z)^4.

    This is the reconstruction fitted to data — NOT the bridged theory, which
    has no closed H_MULT(z) form (Q1 open). Kept here only to show that the
    'smooth MULTING curve' people draw is a *fit*, not a *prediction*.
    """
    x = 1.0 + z
    return a * x**2 + b * x**3 + c * x**4


def chi2(model: np.ndarray, obs: np.ndarray, sigma: np.ndarray) -> float:
    return float(np.sum(((obs - model) / sigma) ** 2))


def aic(chi2_val: float, k: int) -> float:
    return 2.0 * k + chi2_val


def aic_verdict(delta: float) -> str:
    a = abs(delta)
    if a < 2:
        return "equivalent (<2 units → NO discrimination)"
    if a < 4:
        return "weak preference"
    if a < 10:
        return "moderate preference"
    return "strong preference"


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    if not CC_CSV.exists() or not A1_CSV.exists():
        raise FileNotFoundError(f"Expected {CC_CSV} and {A1_CSV} to exist.")
    cc = pd.read_csv(CC_CSV, comment="#")
    a1 = pd.read_csv(A1_CSV, comment="#")
    return cc, a1


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--show", action="store_true", help="open interactively instead of saving")
    ap.add_argument("--out", type=Path, default=OUT_PNG, help="output PNG path")
    args = ap.parse_args()

    cc, a1 = load_data()

    z_cc = cc["z"].to_numpy(dtype=float)
    h_cc = cc["Hz_km_s_Mpc"].to_numpy(dtype=float)
    s_cc = cc["sigma_Hz"].to_numpy(dtype=float)
    n_cc = len(z_cc)
    z_data_max = float(z_cc.max())

    z_a1 = a1["z"].to_numpy(dtype=float)
    h_mult = a1["H_MULT"].to_numpy(dtype=float)

    # ── Fits to the SAME real CC data ────────────────────────────────────────
    p_l, _ = curve_fit(
        lcdm,
        z_cc,
        h_cc,
        sigma=s_cc,
        absolute_sigma=True,
        p0=[70.0, 0.30],
        bounds=([50.0, 0.05], [100.0, 1.0]),
    )
    h0_fit, om_fit = (float(p_l[0]), float(p_l[1]))
    chi2_l = chi2(lcdm(z_cc, *p_l), h_cc, s_cc)
    aic_l = aic(chi2_l, k=2)

    p_m, _ = curve_fit(
        multing_poly,
        z_cc,
        h_cc,
        sigma=s_cc,
        absolute_sigma=True,
        p0=[50.0, -10.0, 5.0],
        maxfev=20000,
    )
    chi2_m = chi2(multing_poly(z_cc, *p_m), h_cc, s_cc)
    aic_m = aic(chi2_m, k=3)

    d_aic = aic_m - aic_l  # >0 favours ΛCDM (fewer params), <0 favours poly

    # ── Console provenance ───────────────────────────────────────────────────
    print("=" * 68)
    print("HONEST HUBBLE DIAGRAM — provenance")
    print("NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION")
    print("=" * 68)
    print(f"  CC data           : {n_cc} points, z ∈ [{z_cc.min():.3f}, {z_data_max:.3f}]")
    print(
        f"  Table A1 MULTING  : {len(z_a1)} discrete rows, z ∈ [{z_a1.min():.2f}, {z_a1.max():.2f}]"
    )
    print(
        f"  ΛCDM fit          : H0={h0_fit:.2f}, Ω_m={om_fit:.3f}  χ²={chi2_l:.1f}  AIC={aic_l:.1f}"
    )
    print(
        f"  Phenom. poly fit  : A,B,C={p_m[0]:.2f},{p_m[1]:.2f},{p_m[2]:.2f}  χ²={chi2_m:.1f}  AIC={aic_m:.1f}"
    )
    print(f"  ΔAIC (poly−ΛCDM)  : {d_aic:+.2f} → {aic_verdict(d_aic)}")
    print("  MULTING bridge    : ABSENT (Q1/Q5 open) → plotted as DISCRETE markers only")
    print(f"  DESI H(z) points  : {len(DESI_HZ)} supplied (none invented)")

    # ── Figure ───────────────────────────────────────────────────────────────
    z_grid = np.linspace(0.0, max(z_data_max, z_a1.max()), 400)
    fig, ax = plt.subplots(figsize=(11, 7))

    # Y-range fits ALL 12 Table A1 MULTING points (max ~418 at z=8.5) with headroom.
    # Derived from data so the frame never silently clips a marker.
    y_lo, y_hi = 50.0, float(max(h_cc.max(), h_mult.max())) * 1.06

    # extrapolation shading beyond real data
    ax.axvspan(z_data_max, z_grid.max(), color="0.90", zorder=0)
    ax.text(
        z_data_max + 0.05,
        y_hi * 0.97,  # track the top dynamically instead of a hardcoded y
        "calibrated data ends →\nextrapolation (both models)",
        fontsize=8,
        color="0.35",
        va="top",
    )
    ax.axvline(z_data_max, color="0.6", ls=":", lw=1)
    ax.axvline(0.0, color="0.6", ls=":", lw=1)

    # real CC data WITH error bars
    ax.errorbar(
        z_cc,
        h_cc,
        yerr=s_cc,
        fmt="o",
        color="0.30",
        ms=4,
        lw=0,
        elinewidth=1,
        capsize=2,
        label=f"Real cosmic chronometers ({n_cc} pts, Moresco+2022)",
        zorder=3,
    )

    # ΛCDM continuous fit (legitimate: it IS a closed-form model)
    ax.plot(
        z_grid,
        lcdm(z_grid, *p_l),
        "-",
        color="#1f77b4",
        lw=2,
        label=f"ΛCDM fit  (H0={h0_fit:.1f}, Ω_m={om_fit:.2f})",
        zorder=2,
    )

    # phenomenological MULTING poly — thin dashed, explicitly NOT the theory
    ax.plot(
        z_grid,
        multing_poly(z_grid, *p_m),
        "--",
        color="#d62728",
        lw=1.3,
        label="Phenomenological fit A(1+z)²+B(1+z)³+C(1+z)⁴\n(NOT bridged MULTING — Q1 open)",
        zorder=2,
    )

    # MULTING theory = DISCRETE Table A1 markers only (the honest core fix)
    ax.plot(
        z_a1,
        h_mult,
        "D",
        color="#d62728",
        ms=7,
        mfc="none",
        mew=1.6,
        label="MULTING Table A1: 12 discrete reconstructed pts (no bridge)",
        zorder=4,
    )

    # SH0ES local anchor
    ax.errorbar(
        [0.0],
        [SH0ES_H0],
        yerr=[SH0ES_ERR],
        fmt="D",
        color="#ff7f0e",
        ms=9,
        capsize=3,
        label=f"SH0ES anchor H0={SH0ES_H0} (Riess+2022)",
        zorder=5,
    )

    # optional DESI (only if user supplied real cited values)
    for i, (zd, hd, sd, _src) in enumerate(DESI_HZ):
        ax.errorbar(
            [zd],
            [hd],
            yerr=[sd],
            fmt="s",
            color="black",
            ms=8,
            capsize=3,
            label=("DESI (cited)" if i == 0 else None),
            zorder=6,
        )

    # ΔAIC honesty box
    ax.text(
        0.03,
        0.97,
        f"ΔAIC (poly − ΛCDM) = {d_aic:+.1f}\n{aic_verdict(d_aic)}\n"
        f"χ²: poly {chi2_m:.0f} (k=3) vs ΛCDM {chi2_l:.0f} (k=2)",
        transform=ax.transAxes,
        va="top",
        ha="left",
        fontsize=9,
        bbox={"boxstyle": "round", "fc": "#fffbe6", "ec": "0.6"},
    )

    ax.set_xlabel("redshift z")
    ax.set_ylabel("H(z)  [km/s/Mpc]")
    ax.set_title("Honest H(z): MULTING (discrete, unbridged) vs ΛCDM over real CC data")
    ax.set_xlim(-0.1, z_grid.max())
    ax.set_ylim(y_lo, y_hi)
    ax.legend(loc="lower right", fontsize=8, framealpha=0.95)
    ax.grid(True, alpha=0.25)
    fig.text(
        0.5,
        0.005,
        "NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION   |   "
        "MULTING shown discrete because bridge F_oP→H_MULT(z) is unresolved (Q1/BETA-1 HOLD)",
        ha="center",
        fontsize=7,
        color="0.4",
    )
    fig.tight_layout(rect=(0, 0.02, 1, 1))

    if args.show:
        matplotlib.use("TkAgg", force=True)
        plt.show()
    else:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(args.out, dpi=150)
        print(f"\n  saved → {args.out.relative_to(REPO)}")
    plt.close(fig)


if __name__ == "__main__":
    main()
