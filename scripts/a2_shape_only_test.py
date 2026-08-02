"""A2 + A4 — shape-only degeneracy test and pointwise discrimination map.

A2 asks ONE descriptive question: after removing the H0 anchor, do the two
plotted curves still differ in SHAPE, and is that difference resolvable by
the CC data at all?

  E(z) = H(z)/H(0)            (anchor removed by construction)
  A2.1  max |E_M/E_L - 1| over 0 <= z <= 1.965
  A2.2  best-fit flat-LCDM (H0, Om) to the RED curve itself -> residual
  A2.3  analytic H0 profiling of each SHAPE against CC data:
            H0_hat = sum(H_i E_i / s_i^2) / sum(E_i^2 / s_i^2)
        then chi2 at the profiled anchor -> shape-only comparison

A4 decomposes the aggregate: dchi2_i = [(H_i-H_M)^2 - (H_i-H_L)^2]/s_i^2
    ranked, cumulative, and split by the author's own zones.

Curves are DIGITIZED from TJB's PDF (calibration error ~0.03%), but the red
curve is NOT model-reproduced: no equation/params are known. Any statement
here is about the PLOTTED CURVE, not about MULTING as a theory.

Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
L0: descriptive.
"""

from __future__ import annotations

import re
from pathlib import Path

import fitz
import numpy as np
import pandas as pd
from scipy.optimize import minimize

PDF = Path(r"C:\Users\serge\Downloads\multing_intro_figure_v6 (1).pdf")
REPO = Path(
    r"E:\Проверка Гипотез\работаю над проверкой гипотез"
    r"\H - 11 Dr. Thomas J. Buckholtz\buckholtz-idm-multing-mvp"
)
X0, XS, Y0, YS = 88.35, 171.4917, 345.72, 1.504700
ORANGE = (0.8509804010391235, 0.3490196168422699, 0.14901961386203766)
BLUE = (0.16470588743686676, 0.47058823704719543, 0.8392156958580017)
ZMAX = 1.965


def px2z(x):
    return (x - X0) / XS


def px2h(y):
    return 50.0 + (Y0 - y) / YS


def close(a, b, t=1e-6):
    return a is not None and all(abs(u - v) < t for u, v in zip(a, b, strict=False))


def pts_of(it):
    p = []
    for el in it["items"]:
        if el[0] == "l":
            p += [el[1], el[2]]
        elif el[0] == "c":
            p += [el[1], el[2], el[3], el[4]]
    return p


def polyline(it):
    a = np.array([[px2z(p.x), px2h(p.y)] for p in pts_of(it)])
    a = a[np.argsort(a[:, 0])]
    zz, hh = [], []
    for z, h in a:
        if zz and abs(z - zz[-1]) < 1e-9:
            hh[-1] = (hh[-1] + h) / 2
        else:
            zz.append(z)
            hh.append(h)
    return np.column_stack([zz, hh])


def lcdm(z, h0, om):
    return h0 * np.sqrt(om * (1 + z) ** 3 + (1 - om))


def load_curves():
    pg = fitz.open(PDF)[0]
    segs, blue = [], None
    for it in pg.get_drawings():
        c, w = it.get("color"), it.get("width")
        if len(pts_of(it)) <= 20 or w != 2.0:
            continue
        if close(c, ORANGE):
            segs.append(polyline(it))
        elif close(c, BLUE):
            blue = polyline(it)
    m = np.vstack(sorted(segs, key=lambda a: a[0, 0]))
    return m[np.argsort(m[:, 0])], blue


def tjb31():
    csv = pd.read_csv(REPO / "data" / "hz_cc.csv", comment="#")
    csv = csv[["z", "Hz_km_s_Mpc", "sigma_Hz"]].to_numpy(float)
    src = (REPO / "code" / "beta_cv.py").read_text(encoding="utf-8")

    def arr(n):
        block = re.search(n + r" = np.array\(\s*\[(.*?)\]", src, re.S).group(1)
        return [float(x) for x in re.findall(r"[\d.]+", block)]

    bz, bh, bs = arr("z_obs"), arr("H_obs"), arr("sigma_obs")
    extra = [
        (z, h, s)
        for z, h, s in zip(bz, bh, bs, strict=False)
        if z in (0.4004, 0.4247, 0.4497, 0.47, 0.4783)
    ]
    d = np.array([r for r in csv if abs(r[0] - 0.75) > 1e-9] + extra)
    return d[np.argsort(d[:, 0])]


def main():
    mult, blue = load_curves()
    d = tjb31()
    z, H, S = d[:, 0], d[:, 1], d[:, 2]

    hM0 = float(np.interp(0.0, mult[:, 0], mult[:, 1]))
    hL0 = float(np.interp(0.0, blue[:, 0], blue[:, 1]))

    print("=" * 74)
    print("A2 — SHAPE-ONLY DEGENERACY TEST   |   L0: descriptive")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION")
    print("curves DIGITIZED (~0.03%); red curve is NOT model-reproduced")
    print("=" * 74)
    print(f"\nanchors: H_MULT(0)={hM0:.2f}   H_LCDM(0)={hL0:.2f}")

    # ---- A2.1 shape ratio on the data range ----
    zg = np.linspace(0.0, ZMAX, 800)
    EM = np.interp(zg, mult[:, 0], mult[:, 1]) / hM0
    EL = np.interp(zg, blue[:, 0], blue[:, 1]) / hL0
    r = EM / EL - 1.0
    print("\n[A2.1] normalised shapes E(z)=H(z)/H(0), 0 <= z <= 1.965")
    print(
        f"  max |E_M/E_L - 1| = {np.max(np.abs(r)) * 100:.2f}%  at z={zg[np.argmax(np.abs(r))]:.3f}"
    )
    print(f"  RMS               = {np.sqrt(np.mean(r**2)) * 100:.2f}%")
    print(f"  sign changes      = {int(np.sum(np.diff(np.sign(r)) != 0))}")

    # data sensitivity for scale
    print(
        f"  (CC sensitivity: median sigma/H = {np.median(S / H) * 100:.1f}%, "
        f"best point {np.min(S / H) * 100:.1f}%)"
    )

    # ---- A2.2 best flat-LCDM fit to the RED CURVE itself ----
    zc = np.linspace(0.0, ZMAX, 400)
    hm = np.interp(zc, mult[:, 0], mult[:, 1])

    def cost(p):
        return float(np.sum((hm - lcdm(zc, p[0], p[1])) ** 2))

    res = minimize(cost, [73.0, 0.30], bounds=[(50, 100), (0.05, 0.95)])
    h0b, omb = float(res.x[0]), float(res.x[1])
    resid = hm - lcdm(zc, h0b, omb)
    rel = np.max(np.abs(resid / lcdm(zc, h0b, omb)))
    print("\n[A2.2] best flat-LCDM fitted to the RED CURVE (curve-to-curve)")
    print(f"  H0 = {h0b:.2f}   Om = {omb:.4f}")
    print(f"  max |residual| = {np.max(np.abs(resid)):.2f} km/s/Mpc  ({rel * 100:.2f}% relative)")
    hm_at = np.interp(z, mult[:, 0], mult[:, 1])
    chi2_equiv = float(np.sum(((hm_at - lcdm(z, h0b, omb)) / S) ** 2))
    print(f"  equivalent chi2 (that residual vs CC errors, n={len(z)}) = {chi2_equiv:.3f}")
    print("  -> if << 1, the red curve IS a flat-LCDM member to CC precision")

    # ---- A2.3 analytic H0 profiling of each shape ----
    print("\n[A2.3] shape-only comparison with H0 profiled analytically")
    out = {}
    for name, curve, h0ref in (("MULTING", mult, hM0), ("LCDM", blue, hL0)):
        E = np.interp(z, curve[:, 0], curve[:, 1]) / h0ref
        h0hat = float(np.sum(H * E / S**2) / np.sum(E**2 / S**2))
        c2 = float(np.sum(((H - h0hat * E) / S) ** 2))
        out[name] = (h0hat, c2)
        print(f"  {name:8s}: profiled H0 = {h0hat:6.2f}   chi2 = {c2:7.3f}")
    dchi = out["MULTING"][1] - out["LCDM"][1]
    print(f"  d_chi2 (MULT - LCDM), shape-only = {dchi:+.3f}")
    print("  (both shapes now judged at THEIR OWN best anchor: pure shape test)")

    # ---- A4 pointwise map ----
    print("\n" + "=" * 74)
    print("A4 — POINTWISE DISCRIMINATION MAP (fixed plotted curves)")
    print("=" * 74)
    hM = np.interp(z, mult[:, 0], mult[:, 1])
    hL = np.interp(z, blue[:, 0], blue[:, 1])
    dc = ((H - hM) ** 2 - (H - hL) ** 2) / S**2
    tot = float(np.sum(dc))
    print(f"\n  total d_chi2 = {tot:+.3f}   (>0 favours LCDM)")
    print("\n  top 6 by |d_chi2_i|:")
    for i in np.argsort(-np.abs(dc))[:6]:
        print(
            f"    z={z[i]:6.3f}  H={H[i]:6.1f}+-{S[i]:5.1f}  "
            f"MULT={hM[i]:6.1f} LCDM={hL[i]:6.1f}  d_chi2={dc[i]:+7.3f}"
        )
    frac = np.sum(np.sort(np.abs(dc))[-3:]) / np.sum(np.abs(dc))
    print(f"\n  top-3 points carry {frac * 100:.0f}% of total |d_chi2|")
    for lo, hi, lab in (
        (0.0, 1.07, "data-grounded 0-1.07"),
        (1.07, 1.965, "CC-calibrated 1.07-1.965"),
    ):
        m = (z >= lo) & (z <= hi)
        print(f"  zone {lab:26s} n={int(m.sum()):3d}  sum d_chi2 = {float(np.sum(dc[m])):+7.3f}")

    # leave-one-out on the aggregate
    loo = np.array([tot - dc[i] for i in range(len(z))])
    print(f"\n  leave-one-out range of total d_chi2: [{loo.min():+.3f}, {loo.max():+.3f}]")
    print(f"  sign flips under LOO: {'YES' if (loo.min() < 0) != (loo.max() < 0) else 'NO'}")


if __name__ == "__main__":
    main()
