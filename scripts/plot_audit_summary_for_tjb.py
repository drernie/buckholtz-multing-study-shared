"""Attachment 2 for the consolidated-audit letter to Dr. Buckholtz.

One figure carrying the control and the result together, because the result is
only readable once the control is visible: the digitiser recovers the *known*
blue curve as flat Planck LCDM to 0.002 %, so the 21 % mismatch between the
orange curve and Table A1's H_MULT column is a property of the artifacts and
not of our extraction.

Reads   : the emailed figure PDF (curve geometry, selected by colour)
          data/table_a1_source_verified.csv
Writes  : reports/audit_summary_for_tjb.png  (and .pdf)
Exit 0. Prints the control residual and the divergence table to stdout.
"""

from __future__ import annotations

from pathlib import Path

import fitz
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

REPO = Path(__file__).resolve().parents[1]
PDF = Path(r"C:\Users\serge\Downloads\multing_intro_figure_v6 (1).pdf")
A1_CSV = REPO / "data" / "table_a1_source_verified.csv"
OUT = REPO / "reports" / "audit_summary_for_tjb"

# Axis calibration of the emailed figure, established in scripts/a1_digitize_tjb_figure.py
X0, XS = 88.35, 171.4917
Y0, YS, H0V = 345.72, 1.504700, 50.0
ORANGE = (0.8509804010391235, 0.3490196168422699, 0.14901961386203766)
BLUE = (0.16470588743686676, 0.47058823704719543, 0.8392156958580017)


def _zx(x: float) -> float:
    return (x - X0) / XS


def _hy(y: float) -> float:
    return H0V + (Y0 - y) / YS


def _same(a, b, tol: float = 1e-6) -> bool:
    return a is not None and all(abs(u - v) < tol for u, v in zip(a, b, strict=True))


def _points(item) -> list:
    pts: list = []
    for e in item["items"]:
        if e[0] == "l":
            pts += [e[1], e[2]]
        elif e[0] == "c":
            pts += [e[1], e[2], e[3], e[4]]
    return pts


def extract(drawings, colour) -> tuple[np.ndarray, np.ndarray]:
    """Curve geometry for one colour, deduplicated and sorted in z."""
    segs = [
        np.array([[_zx(p.x), _hy(p.y)] for p in _points(it)])
        for it in drawings
        if _same(it.get("color"), colour) and len(_points(it)) > 20
    ]
    a = np.vstack(segs)
    a = a[np.argsort(a[:, 0])]
    _, keep = np.unique(np.round(a[:, 0], 5), return_index=True)
    a = a[np.sort(keep)]
    return a[:, 0], a[:, 1]


def flat_lcdm(z, h0, om):
    return h0 * np.sqrt(om * (1 + z) ** 3 + (1 - om))


def rms_pct(model, obs) -> float:
    return 100.0 * float(np.sqrt(np.mean(((model - obs) / obs) ** 2)))


def main() -> int:
    dr = fitz.open(PDF)[0].get_drawings()
    zb, hb = extract(dr, BLUE)
    zo, ho = extract(dr, ORANGE)

    # --- the control: does the digitiser reproduce a curve of KNOWN identity? ---
    m = zb >= 0.0
    p_ctl, _ = curve_fit(flat_lcdm, zb[m], hb[m], p0=[70.0, 0.3], maxfev=100_000)
    ctl = rms_pct(flat_lcdm(zb[m], *p_ctl), hb[m])
    print(f"CONTROL  blue curve -> flat LCDM: H0={p_ctl[0]:.2f} Om={p_ctl[1]:.4f} rms={ctl:.4f}%")

    a1 = pd.read_csv(A1_CSV, comment="#")
    a1 = a1[a1.z <= zo.max()]
    a1_curve = np.interp(a1.z, zo, ho)
    dev = 100.0 * (a1_curve - a1.H_MULT) / a1.H_MULT
    print(f"RESULT   curve vs Table A1 H_MULT: rms={rms_pct(a1_curve, a1.H_MULT.values):.1f}%")
    for z, hc, hm, d in zip(a1.z, a1_curve, a1.H_MULT, dev, strict=True):
        print(f"   z={z:4.2f}  curve {hc:6.1f}   Table A1 {hm:6.1f}   {d:+6.1f}%")

    # ---------------------------------------------------------------- figure --
    fig, (ax, bx) = plt.subplots(
        2, 1, figsize=(8.6, 8.2), sharex=True, gridspec_kw={"height_ratios": [2.5, 1]}
    )

    ax.plot(zb, hb, color="#2a78d6", lw=2.4, label="ΛCDM curve as plotted (blue)", zorder=3)
    zz = np.linspace(0, zb.max(), 300)
    ax.plot(
        zz,
        flat_lcdm(zz, *p_ctl),
        color="k",
        lw=1.1,
        ls=(0, (6, 4)),
        zorder=4,
        label=f"flat ΛCDM fit to it — $H_0$={p_ctl[0]:.2f}, $\\Omega_m$={p_ctl[1]:.4f}",
    )
    ax.plot(zo, ho, color="#d95923", lw=2.4, label="Later email MULTING curve (orange)", zorder=3)
    ax.plot(
        a1.z,
        a1.H_MULT,
        "s",
        ms=7,
        mfc="none",
        mew=1.8,
        color="#8c1d1d",
        zorder=5,
        label="Table A1, AI-conditioned $H_{\\rm MULT}$",
    )
    ax.axvline(0.0, color="0.75", lw=0.8, ls=":")
    ax.set_ylabel("$H(z)$  [km s$^{-1}$ Mpc$^{-1}$]")
    ax.set_ylim(45, 265)
    ax.legend(loc="upper left", frameon=False, fontsize=9.5)
    ax.set_title(
        "The digitiser is validated on a known ΛCDM control, while the two\n"
        "MULTING-related artifacts remain quantitatively distinct",
        fontsize=11.0,
        pad=12,
    )
    ax.text(
        0.985,
        0.06,
        f"control residual  {ctl:.3f} %\n(flat Planck-like ΛCDM parameters recovered)",
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        fontsize=9.5,
        bbox={"boxstyle": "round,pad=0.45", "fc": "#eef4fb", "ec": "#2a78d6", "lw": 0.9},
    )

    bx.axhline(0, color="0.6", lw=0.9)
    bx.plot(
        zb[m],
        100 * (flat_lcdm(zb[m], *p_ctl) - hb[m]) / hb[m],
        color="#2a78d6",
        lw=2.2,
        label=f"blue curve vs its ΛCDM fit  ({ctl:.3f} %)",
    )
    bx.plot(
        a1.z,
        dev,
        "s-",
        ms=6.5,
        color="#8c1d1d",
        lw=1.5,
        label="email curve vs Table A1 $H_{\\rm MULT}$  (21 % rms)",
    )
    for z, d in zip(a1.z, dev, strict=True):
        if abs(d) > 8:
            bx.annotate(
                f"{d:+.0f}%",
                (z, d),
                textcoords="offset points",
                xytext=(6, -3),
                fontsize=9,
                color="#8c1d1d",
            )
    bx.set_xlabel("redshift  $z$")
    bx.set_ylabel("fractional difference  [%]")
    bx.text(
        0.985,
        0.05,
        r"$\Delta_H(z)=100\times\dfrac{H_{\rm orange}(z)-H_{A1}(z)}{H_{A1}(z)}$"
        "\n(blue series: same formula against its own ΛCDM fit)",
        transform=bx.transAxes,
        ha="right",
        va="bottom",
        fontsize=8.5,
        color="0.3",
    )
    bx.set_xlim(-0.22, 2.55)
    bx.legend(loc="upper left", frameon=False, fontsize=9.5)

    for a in (ax, bx):
        a.grid(alpha=0.25, lw=0.6)
        for sp in ("top", "right"):
            a.spines[sp].set_visible(False)

    fig.text(
        0.5,
        0.012,
        "Curves digitised by colour from the supplied figure. Squares are Table A1 "
        "$H_{\\rm MULT}$ values, not a fit.\nOur reconstruction — errors are ours.",
        ha="center",
        fontsize=8.5,
        color="0.35",
    )
    fig.tight_layout(rect=(0, 0.035, 1, 1))
    for ext in ("png", "pdf"):
        fig.savefig(f"{OUT}.{ext}", dpi=200)
    print(f"\nwrote {OUT}.png and {OUT}.pdf")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
