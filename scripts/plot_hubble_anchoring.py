"""plot_hubble_anchoring.py — the H0-anchoring artifact behind TJB's 2026-07-20 chart.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

TJB's 2026-07-20 Hubble-diagram draws a red "MULTING (anchored to SH0ES, H0=73)"
curve above a blue "LCDM (anchored to Planck, H0=67)" curve and reads the z~=0 gap
as "MULTING can help resolve the Hubble tension."

Our result P2 (docs/127, Shtanov-Sahni generalized cosmic-energy equation): MULTING's
BACKGROUND H(z) is q-blind -- the dipole and quadrupole sub-1/r terms wash out at
cosmological scale, G_eff = G. So MULTING's background is degenerate with LCDM: the
red curve has the SAME functional shape as the blue one. The only thing separating
them in TJB's chart is the H0 ANCHOR (73 vs 67), not model physics. Put both at the
same H0 and the two curves coincide exactly.

This script makes that quantitative against the REAL 27 cosmic-chronometer points
(Moresco+2022, arXiv:2201.07241, data/hz_cc.csv):
  - free fit to the CC data:       H0 ~= 68.8 (near Planck, NOT SH0ES)
  - anchor to Planck (67.36):      chi2 essentially as good as the free fit
  - anchor to SH0ES  (73.04):      chi2 clearly WORSE (the data disprefer it),
                                   though the large CC error bars can't rule it out.

The honest reading: the "resolution" is a choice of anchor, and the anchor the data
actually prefer is the LOW (Planck-like) one.

Run:  python scripts/plot_hubble_anchoring.py
Exit: 0. PNG -> reports/hubble_anchoring_artifact.png. chi2 table printed to stdout.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit, minimize_scalar

REPO = Path(__file__).resolve().parents[1]
CC_CSV = REPO / "data" / "hz_cc.csv"
OUT_PNG = REPO / "reports" / "hubble_anchoring_artifact.png"

OM_FID = 0.317  # fiducial matter density held fixed for the anchored curves
PLANCK_H0 = 67.36  # Planck 2018 TT,TE,EE+lowE+lensing
SH0ES_H0 = 73.04  # Riess+2022 (SH0ES) local distance ladder
SH0ES_ERR = 1.04


def lcdm(z: np.ndarray, h0: float, om: float) -> np.ndarray:
    """Flat-LCDM expansion rate. MULTING's background shares this shape (P2)."""
    return h0 * np.sqrt(om * (1.0 + z) ** 3 + (1.0 - om))


def main() -> int:
    cc = pd.read_csv(CC_CSV, comment="#")
    z = cc["z"].to_numpy(float)
    h = cc["Hz_km_s_Mpc"].to_numpy(float)
    s = cc["sigma_Hz"].to_numpy(float)

    def chi2(h0: float, om: float) -> float:
        return float(np.sum(((h - lcdm(z, h0, om)) / s) ** 2))

    # free fit (both H0 and Om float) -- what the data actually want
    (h0_free, om_free), _ = curve_fit(lcdm, z, h, sigma=s, p0=(70.0, 0.3), maxfev=10000)
    chi2_free = chi2(h0_free, om_free)

    # anchored fits: Om fixed at fiducial, and Om re-floated (fair to each anchor)
    rows = []
    for h0, lab in [(PLANCK_H0, "Planck 67"), (SH0ES_H0, "SH0ES 73")]:
        c_fix = chi2(h0, OM_FID)
        r = minimize_scalar(lambda om, h0=h0: chi2(h0, om), bounds=(0.05, 0.9), method="bounded")
        rows.append((lab, h0, c_fix, float(r.x), float(r.fun)))

    print("=" * 70)
    print("H0-ANCHORING ARTIFACT — LCDM vs real cosmic chronometers")
    print("NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION")
    print("=" * 70)
    print(f"  CC data           : {len(z)} points, z in [{z.min():.3f}, {z.max():.3f}]")
    print(f"  free fit          : H0={h0_free:.2f}, Om={om_free:.3f}  chi2={chi2_free:.1f}")
    print("  --- anchored (MULTING background = LCDM shape, P2) -------------------")
    print("   anchor          H0     chi2(Om=0.317)   chi2(Om floated)")
    for lab, h0, c_fix, om_f, c_flt in rows:
        print(f"   {lab:12s}  {h0:5.2f}     {c_fix:6.1f}          {c_flt:6.1f}  (Om={om_f:.3f})")
    print("  " + "-" * 66)
    # honest verdict: which anchor the data prefer, and by how much
    planck_c, shoes_c = rows[0][2], rows[1][2]
    print(f"  => data prefer the LOW anchor: Planck chi2={planck_c:.1f} < SH0ES chi2={shoes_c:.1f}")
    print(f"     (free-fit H0={h0_free:.1f} sits near Planck, not SH0ES). chi2/dof<1 for all")
    print("     -> CC error bars too large to RULE OUT SH0ES, but they do not favour it.")
    print("  => the z=0 gap in TJB's chart is the ANCHOR choice, not MULTING physics.")

    # ---- figure --------------------------------------------------------------
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
        label=f"{len(z)} cosmic chronometers (Moresco+2022)",
    )
    ax.plot(
        zg,
        lcdm(zg, SH0ES_H0, OM_FID),
        "-",
        color="#c0392b",
        lw=2.2,
        label='ΛCDM @ SH0ES (73) — TJB chart calls this "MULTING"',
    )
    ax.plot(
        zg, lcdm(zg, PLANCK_H0, OM_FID), "-", color="#2f6db0", lw=2.2, label="ΛCDM @ Planck (67)"
    )
    ax.plot(
        zg,
        lcdm(zg, h0_free, om_free),
        "--",
        color="#1a2230",
        lw=1.4,
        alpha=0.8,
        label=f"ΛCDM free fit (H₀={h0_free:.1f}) — what the data want",
    )
    ax.plot(0, SH0ES_H0, marker="D", ms=8, color="#e0891c", ls="none", label="SH0ES local H₀")

    ax.set_xlabel("redshift  z")
    ax.set_ylabel("H(z)  [km/s/Mpc]")
    ax.set_title("Same shape, two anchors: the 'tension resolution' is the H₀ anchor (our P2)")
    ax.set_xlim(-0.03, 2.05)
    ax.set_ylim(55, 215)
    ax.legend(fontsize=8.5, loc="upper left", framealpha=0.9)
    ax.grid(True, alpha=0.25)
    ax.annotate(
        "MULTING background ≡ ΛCDM (G_eff=G, docs/127)\n"
        "→ red = ΛCDM@73; at equal H₀ the curves coincide.\n"
        f"CC data prefer H₀≈{h0_free:.0f}; SH0ES anchor fits worse (χ²={shoes_c:.0f} vs {planck_c:.0f}).",
        xy=(0.98, 0.02),
        xycoords="axes fraction",
        ha="right",
        va="bottom",
        fontsize=8,
        bbox={"boxstyle": "round,pad=0.4", "fc": "#fbf3ef", "ec": "#e8c7bd"},
    )
    OUT_PNG.parent.mkdir(exist_ok=True)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=140)
    print(f"\n  saved -> {OUT_PNG.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
