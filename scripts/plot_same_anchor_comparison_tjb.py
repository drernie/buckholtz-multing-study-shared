"""plot_same_anchor_comparison_tjb.py — neutral, TJB-facing companion figure.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

This is a DESCRIPTIVE companion to `scripts/plot_hubble_anchoring.py`, built specifically for
attachment to a letter to Dr. Buckholtz. The math is identical (same chi2 fits, same real CC
data); the difference is presentation. `plot_hubble_anchoring.py` is our internal audit artifact
and its title/legend/annotation state our OWN conclusion ("the tension resolution is the anchor,
not physics") -- correct for internal use, but stating a conclusion on an image sent to the
paper's own author would contradict a letter that is carefully phrased as open questions, not
claims. This script shows the same real data and the same fits with neutral labels only: what is
plotted, not what we conclude from it. The letter's own text carries the reasoning.

Run:  python scripts/plot_same_anchor_comparison_tjb.py
Exit: 0. PNG -> reports/same_anchor_hubble_comparison.png. Fit numbers printed to stdout for
independent verification (re-derives H0_free, Om_free, and both anchored chi2 values from
scratch -- does not import or trust plot_hubble_anchoring.py's numbers).
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
OUT_PNG = REPO / "reports" / "hubble_anchor_control_comparison.png"

OM_FID = 0.317  # fiducial matter density held fixed for the anchored curves
PLANCK_H0 = 67.36  # Planck 2018 TT,TE,EE+lowE+lensing
SH0ES_H0 = 73.04  # Riess+2022 (SH0ES) local distance ladder


def lcdm(z: np.ndarray, h0: float, om: float) -> np.ndarray:
    """Flat-LCDM expansion rate."""
    return h0 * np.sqrt(om * (1.0 + z) ** 3 + (1.0 - om))


def chi2(z: np.ndarray, h: np.ndarray, s: np.ndarray, h0: float, om: float) -> float:
    return float(np.sum(((h - lcdm(z, h0, om)) / s) ** 2))


def main() -> int:
    cc = pd.read_csv(CC_CSV, comment="#")
    z = cc["z"].to_numpy(float)
    h = cc["Hz_km_s_Mpc"].to_numpy(float)
    s = cc["sigma_Hz"].to_numpy(float)

    (h0_free, om_free), cov_free = curve_fit(lcdm, z, h, sigma=s, p0=(70.0, 0.3), maxfev=10000)
    h0_free_err, om_free_err = np.sqrt(np.diag(cov_free))
    chi2_free = chi2(z, h, s, h0_free, om_free)
    chi2_planck = chi2(z, h, s, PLANCK_H0, OM_FID)
    chi2_shoes = chi2(z, h, s, SH0ES_H0, OM_FID)

    print("=" * 70)
    print("Same-anchor ΛCDM comparison — real cosmic chronometers (independent re-derivation)")
    print("NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION")
    print("=" * 70)
    print(f"  CC data      : {len(z)} points, z in [{z.min():.3f}, {z.max():.3f}]")
    print(
        f"  free fit     : H0={h0_free:.2f}+-{h0_free_err:.2f}, "
        f"Om={om_free:.3f}+-{om_free_err:.3f}  chi2={chi2_free:.2f}  "
        "(diagonal quoted CC errors, no covariance matrix)"
    )
    print(f"  Planck anchor (H0={PLANCK_H0}, Om={OM_FID}): chi2={chi2_planck:.2f}")
    print(f"  SH0ES  anchor (H0={SH0ES_H0}, Om={OM_FID}): chi2={chi2_shoes:.2f}")
    print(f"  dof = {len(z) - 2} (free fit), {len(z)} (fixed-Om anchors)")

    zg = np.linspace(0, 2.05, 300)
    fig, ax = plt.subplots(figsize=(8.2, 5.2))
    ax.errorbar(
        z,
        h,
        yerr=s,
        fmt="o",
        ms=4,
        color="#5b6675",
        ecolor="#9aa6b6",
        elinewidth=1,
        capsize=2,
        alpha=0.85,
        label=f"{len(z)} cosmic chronometers (Moresco et al. 2022)",
    )
    ax.plot(
        zg,
        lcdm(zg, SH0ES_H0, OM_FID),
        "-",
        color="#c0392b",
        lw=2.2,
        label=f"ΛCDM (Ωm={OM_FID}), H₀={SH0ES_H0} — SH0ES anchor",
    )
    ax.plot(
        zg,
        lcdm(zg, PLANCK_H0, OM_FID),
        "-",
        color="#2f6db0",
        lw=2.2,
        label=f"ΛCDM (Ωm={OM_FID}), H₀={PLANCK_H0} — Planck anchor",
    )
    ax.plot(
        zg,
        lcdm(zg, h0_free, om_free),
        "--",
        color="#1a2230",
        lw=1.4,
        alpha=0.8,
        label=(
            f"Chronometer-only free fit (diagonal errors): "
            f"H₀={h0_free:.1f}±{h0_free_err:.1f}, Ωm={om_free:.2f}±{om_free_err:.2f}"
        ),
    )
    ax.plot(
        0,
        SH0ES_H0,
        marker="D",
        ms=8,
        color="#e0891c",
        ls="none",
        label="SH0ES local H₀ (reference point, not in the chronometer-only fit)",
    )

    ax.set_xlabel("redshift  z")
    ax.set_ylabel("H(z)  [km/s/Mpc]")
    fig.suptitle(
        "Effect of H₀ anchoring in flat ΛCDM over 27 cosmic-chronometer measurements",
        fontsize=12,
        y=0.985,
    )
    ax.set_title(
        "Solid curves share the same Ωm and differ only in the adopted H₀ anchor",
        fontsize=9,
        style="italic",
        pad=8,
    )
    ax.set_xlim(-0.03, 2.05)
    ax.set_ylim(55, 215)
    ax.legend(fontsize=8, loc="upper left", framealpha=0.9)
    ax.grid(True, alpha=0.25)

    OUT_PNG.parent.mkdir(exist_ok=True)
    fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.94))
    fig.savefig(OUT_PNG, dpi=140)
    print(f"\n  saved -> {OUT_PNG.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
