"""A version of Dr. Buckholtz's own figure with cosmic-chronometer error bars.

WHY: his 2026-08-02 figure plots the CC points as bare markers. The Moresco+2022
uncertainties are large (median 17, max 62 km/s/Mpc) compared with the ~3 km/s/Mpc
median separation between his two curves, so a referee will ask for them. Showing
them also reframes which part of his result is strongest: the point-by-point fit
is not where the curves separate, but the low-z MINIMUM in H(z) at z = +0.098 is
a feature flat LCDM does not have at all.

Curves are digitised from his supplied figure. Data is this project's 27-point
Moresco+2022 compilation -- HIS figure cites 31 points, so this is a suggestion
of form, not a replacement of his data.

Writes: reports/hz_with_errorbars_for_tjb.png / .pdf
"""

from __future__ import annotations

from pathlib import Path

import fitz
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

REPO = Path(__file__).resolve().parents[1]
PDF = Path(r"C:\Users\serge\Downloads\multing_intro_figure_v6 (2).pdf")
OUT = REPO / "reports" / "hz_with_errorbars_for_tjb"

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


def main() -> int:
    dr = fitz.open(PDF)[0].get_drawings()
    zo, ho = extract(dr, ORANGE)
    zb, hb = extract(dr, BLUE)
    cc = pd.read_csv(REPO / "data" / "hz_cc.csv")

    zz = np.linspace(zo.min(), zo.max(), 4000)
    hh = np.interp(zz, zo, ho)
    imin = int(np.argmin(hh))
    z_min, h_min = zz[imin], hh[imin]
    print(f"MULTING curve minimum: z = {z_min:+.3f}, H = {h_min:.1f}")
    print(f"CC sigma: median {cc.sigma_Hz.median():.1f}, max {cc.sigma_Hz.max():.1f}")

    fig, ax = plt.subplots(figsize=(9.2, 6.2))

    ax.errorbar(
        cc.z,
        cc.Hz_km_s_Mpc,
        yerr=cc.sigma_Hz,
        fmt="o",
        ms=4.5,
        color="0.25",
        ecolor="0.55",
        elinewidth=1.1,
        capsize=2.5,
        zorder=2,
        label="Cosmic chronometers, Moresco+2022 (27 pts, with $\\sigma$)",
    )
    ax.plot(
        zb, hb, color="#2a78d6", lw=2.3, zorder=3, label="ΛCDM, fixed Planck ($\\Omega_m=0.315$)"
    )
    ax.plot(zo, ho, color="#d95923", lw=2.3, zorder=4, label="MULTING (spotlighted case)")

    ax.plot([z_min], [h_min], "v", ms=11, color="#d95923", mec="k", mew=0.8, zorder=6)
    ax.annotate(
        f"minimum at $z={z_min:+.3f}$\nflat ΛCDM has none here",
        xy=(z_min, h_min),
        xytext=(0.40, 0.11),
        textcoords="axes fraction",
        fontsize=10.5,
        color="#8c3a12",
        ha="left",
        bbox={
            "boxstyle": "round,pad=0.4",
            "fc": "white",
            "ec": "#d95923",
            "lw": 0.9,
            "alpha": 0.95,
        },
        arrowprops={
            "arrowstyle": "->",
            "color": "#8c3a12",
            "lw": 1.2,
            "connectionstyle": "arc3,rad=0.2",
        },
    )

    ax.axvline(0.0, color="0.75", lw=0.8, ls=":")
    ax.axvline(1.965, color="0.75", lw=0.8, ls=":")
    ax.text(1.928, 214, "end of CC calibration", fontsize=8.5, color="0.45", rotation=90)

    ax.set_xlabel("redshift  $z$")
    ax.set_ylabel("$H(z)$  [km s$^{-1}$ Mpc$^{-1}$]")
    ax.set_xlim(-0.22, 2.52)
    ax.set_ylim(45, 275)
    ax.grid(alpha=0.25, lw=0.6)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.legend(loc="upper left", frameon=False, fontsize=9.5)
    ax.set_title(
        "The same two curves, with the chronometer uncertainties shown",
        fontsize=11.5,
        pad=10,
    )
    fig.text(
        0.5,
        0.012,
        "Curves digitised from the supplied figure. Data is a 27-point Moresco+2022 compilation; "
        "the source figure cites 31 points.\nSuggestion of form, not a replacement of the author's data.",
        ha="center",
        fontsize=8,
        color="0.4",
    )
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    for ext in ("png", "pdf"):
        fig.savefig(f"{OUT}.{ext}", dpi=200)
    print(f"wrote {OUT}.png / .pdf")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
