"""plot_control_figure_corrected.py — reproducible, corrected version of the sent control figure.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

The figure actually attached to the TJB letter sent 2026-07-24 ("Clarifying the construction of
the MULTING H(z) curve") was generated externally (ChatGPT code-interpreter sandbox), not by any
script in this repo -- it existed only as an image until now. This script reproduces that design
from scratch, in-repo, reusing the fitting logic already verified in
`plot_same_anchor_comparison_tjb.py` (same real CC data, same chi2 convention), with one fix
applied: the "WHAT THIS FIGURE TESTS" panel's original wording --
    "a crossing elsewhere requires a different E(z), a different Omega_m, or another
    redshift-dependent construction"
is logically redundant (Omega_m is already a parameter OF E(z)) and is corrected here to:
    "a crossing requires a different E(z) -- for example through a different Omega_m,
    curvature, w(z), or another redshift-dependent construction."

This is NOT a retroactive edit of what was already sent (that PNG, from Downloads, is what TJB
received, unchanged). This is the in-repo, reproducible, corrected reference version -- for our
own records and for any follow-up correspondence.

Run:  python scripts/plot_control_figure_corrected.py
Exit: 0. PNG -> reports/hubble_anchor_control_figure_corrected.png. All numbers re-derived from
data/hz_cc.csv, printed to stdout for independent verification.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

REPO = Path(__file__).resolve().parents[1]
CC_CSV = REPO / "data" / "hz_cc.csv"
OUT_PNG = REPO / "reports" / "hubble_anchor_control_figure_corrected.png"

OM_ANCHOR = 0.315  # fiducial matter density held fixed for the two anchored (illustrative) curves
PLANCK_H0 = 67.36  # Planck 2018 TT,TE,EE+lowE+lensing
SH0ES_H0 = 73.04  # Riess+2022 (SH0ES) local distance ladder


def lcdm(z: np.ndarray, h0: float, om: float) -> np.ndarray:
    """Flat-LCDM expansion rate."""
    return h0 * np.sqrt(om * (1.0 + z) ** 3 + (1.0 - om))


def chi2_of(z: np.ndarray, h: np.ndarray, s: np.ndarray, h0: float, om: float) -> float:
    return float(np.sum(((h - lcdm(z, h0, om)) / s) ** 2))


def main() -> int:
    cc = pd.read_csv(CC_CSV, comment="#")
    z = cc["z"].to_numpy(float)
    h = cc["Hz_km_s_Mpc"].to_numpy(float)
    s = cc["sigma_Hz"].to_numpy(float)
    n = len(z)

    (h0_free, om_free), cov_free = curve_fit(lcdm, z, h, sigma=s, p0=(70.0, 0.3), maxfev=10000)
    h0_free_err, om_free_err = np.sqrt(np.diag(cov_free))
    chi2_free = chi2_of(z, h, s, h0_free, om_free)
    chi2_planck = chi2_of(z, h, s, PLANCK_H0, OM_ANCHOR)
    chi2_shoes = chi2_of(z, h, s, SH0ES_H0, OM_ANCHOR)
    dof = n - 2
    ratio_anchors = SH0ES_H0 / PLANCK_H0

    print("=" * 78)
    print("Control figure — reproducible, corrected version (in-repo)")
    print("NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION")
    print("=" * 78)
    print(f"  CC data        : n={n}, z in [{z.min():.3f}, {z.max():.3f}]")
    print(
        f"  free fit       : H0={h0_free:.2f}+-{h0_free_err:.2f}, "
        f"Om={om_free:.3f}+-{om_free_err:.3f}"
    )
    print(f"  anchors        : Planck H0={PLANCK_H0}, SH0ES H0={SH0ES_H0}, both Om={OM_ANCHOR}")
    print(f"  chi2 free fit (H0={h0_free:.2f}, Om={om_free:.3f}) = {chi2_free:.2f} for {dof} dof")
    print(f"  chi2 Planck anchor (Om={OM_ANCHOR}) = {chi2_planck:.2f} for {dof} dof (context only)")
    print(f"  chi2 SH0ES anchor  (Om={OM_ANCHOR}) = {chi2_shoes:.2f} for {dof} dof (context only)")
    print(f"  invariant ratio H_{SH0ES_H0}/H_{PLANCK_H0} = {ratio_anchors:.4f} at every z")

    zg_data = np.linspace(0, z.max() + 0.35, 300)

    fig = plt.figure(figsize=(15.5, 9.2))
    gs = fig.add_gridspec(
        2, 2, width_ratios=(3.0, 1.15), height_ratios=(3.1, 1.0), hspace=0.32, wspace=0.05
    )
    ax = fig.add_subplot(gs[0, 0])
    ax_ratio = fig.add_subplot(gs[1, 0])
    ax_info = fig.add_subplot(gs[:, 1])
    ax_info.axis("off")

    ax.axvspan(z.max(), 2.35, color="#dce7f5", alpha=0.6, zorder=0)
    ax.axvline(z.max(), color="#4472a8", lw=1.0, ls=":", zorder=1)

    ax.errorbar(
        z,
        h,
        yerr=s,
        fmt="o",
        ms=5,
        color="#2f6db0",
        ecolor="#7fa3cc",
        elinewidth=1.1,
        capsize=2,
        alpha=0.9,
        label=f"{n} cosmic-chronometer measurements",
        zorder=3,
    )
    ax.plot(
        zg_data,
        lcdm(zg_data, PLANCK_H0, OM_ANCHOR),
        "-",
        color="#e07b1c",
        lw=2.4,
        label=f"Flat ΛCDM: H₀={PLANCK_H0}, Ωm={OM_ANCHOR}",
        zorder=4,
    )
    ax.plot(
        zg_data,
        lcdm(zg_data, SH0ES_H0, OM_ANCHOR),
        "--",
        color="#2e8b3d",
        lw=2.4,
        label=f"Flat ΛCDM: H₀={SH0ES_H0}, same Ωm={OM_ANCHOR}",
        zorder=4,
    )
    zg_free = np.linspace(0, z.max() + 0.35, 300)
    ax.plot(
        zg_free,
        lcdm(zg_free, h0_free, om_free),
        ":",
        color="#c0392b",
        lw=2.2,
        label=f"CC-only diagonal-error fit: H₀={h0_free:.2f}, Ωm={om_free:.3f}",
        zorder=4,
    )
    ax.plot(
        0,
        SH0ES_H0,
        marker="D",
        ms=9,
        color="#2f6db0",
        ls="none",
        label="SH0ES anchor (context only; not included in CC-only fit)",
        zorder=5,
    )

    z_last, h_last = z[-1], h[-1]
    ax.annotate(
        f"Last point in this {n}-point CC set\nz = {z_last:.3f}",
        xy=(z_last, h_last),
        xytext=(z_last - 0.55, h_last + 40),
        fontsize=9,
        ha="center",
        arrowprops={"arrowstyle": "->", "color": "black", "lw": 1.0},
    )

    ax.set_xlabel("Redshift $z$")
    ax.set_ylabel(r"$H(z)$  [km s$^{-1}$ Mpc$^{-1}$]")
    fig.suptitle("Control figure for the MULTING / Hubble-tension discussion", fontsize=15, y=0.985)
    ax.set_title(
        f"Effect of $H_0$ anchoring in flat ΛCDM over {n} cosmic-chronometer measurements",
        fontsize=12,
    )
    ax.set_xlim(-0.05, 2.35)
    ax.legend(fontsize=9, loc="upper left", framealpha=0.9)
    ax.grid(True, alpha=0.2)

    ratio = lcdm(zg_data, SH0ES_H0, OM_ANCHOR) / lcdm(zg_data, PLANCK_H0, OM_ANCHOR)
    ax_ratio.plot(zg_data, ratio, color="#2f6db0", lw=2.2)
    ax_ratio.axhline(1.0, color="#2f6db0", lw=1.0, ls="--", alpha=0.6)
    ax_ratio.text(
        zg_data[-1],
        ratio[-1] + 0.003,
        f"constant ratio = {ratio_anchors:.4f}",
        ha="right",
        va="bottom",
        fontsize=9,
    )
    ax_ratio.set_xlabel("Redshift $z$")
    ax_ratio.set_ylabel(rf"$H_{{{SH0ES_H0:.2f}}}(z)/H_{{{PLANCK_H0:.2f}}}(z)$", fontsize=9)
    ax_ratio.set_title(
        "Anchor-only diagnostic: the ratio is constant, so no crossing is possible", fontsize=10
    )
    ax_ratio.set_xlim(-0.05, 2.35)
    ax_ratio.grid(True, alpha=0.2)

    info_text = (
        "WHAT THIS FIGURE TESTS\n\n"
        r"$H(z) = H_0 E(z)$"
        "\n"
        r"$E(z) = \sqrt{\Omega_m(1+z)^3 + 1 - \Omega_m}$"
        "\n\n"
        "For the two anchored curves:\n"
        f"• the same $\\Omega_m$ = {OM_ANCHOR};\n"
        f"• $H_0$ = {PLANCK_H0} versus $H_0$ = {SH0ES_H0}.\n\n"
        "EXACT INVARIANT\n"
        f"$H_{{{SH0ES_H0}}}(z)/H_{{{PLANCK_H0}}}(z)$\n"
        f"= {SH0ES_H0}/{PLANCK_H0} = {ratio_anchors:.4f}\n"
        "at every redshift.\n\n"
        "THEREFORE\n"
        "• anchor-only curves cannot cross;\n"
        "• a crossing requires a different $E(z)$ —\n"
        "  for example through a different $\\Omega_m$,\n"
        "  curvature, $w(z)$, or another\n"
        "  redshift-dependent construction.\n\n"
        "DATA TREATMENT\n"
        f"• {n} CC points; diagonal errors shown;\n"
        "• neither anchored curve is fitted to them;\n"
        "• dotted curve: illustrative CC-only fit;\n"
        f"• $\\chi^2$ = {chi2_free:.2f} for {dof} dof (CC-only fit)."
    )
    ax_info.text(
        0.0,
        0.98,
        info_text,
        transform=ax_info.transAxes,
        fontsize=10,
        va="top",
        ha="left",
        linespacing=1.6,
        bbox={"boxstyle": "round,pad=0.6", "facecolor": "#e4edf7", "edgecolor": "#9fb8d6"},
    )

    fig.text(
        0.01,
        0.005,
        f"Sources/assumptions: {n}-point CC compilation reproduced from the project dataset; "
        f"Planck anchor H0={PLANCK_H0}; SH0ES anchor H0={SH0ES_H0}. Purpose: isolate the "
        "H0-anchor effect, not validate or refute MULTING. Only diagonal CC errors are "
        "displayed; no full covariance is used.",
        fontsize=7.5,
        color="#444444",
    )

    OUT_PNG.parent.mkdir(exist_ok=True)
    fig.tight_layout(rect=(0.0, 0.02, 1.0, 0.95))
    fig.savefig(OUT_PNG, dpi=150)
    print(f"\n  saved -> {OUT_PNG.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
