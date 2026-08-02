"""B-1 — statefinder diagnostics on the digitized TJB curves.

Turns the inaccessible z<0 headline into quantities testable at low z NOW.

  q(z)  = -1 + (1+z) H'/H                      (deceleration)
  j(z)  = q(2q+1) + (1+z) dq/dz                (jerk)
  Om(z) = (E^2 - 1)/((1+z)^3 - 1),  E=H/H0     (Sahni et al. diagnostic)

For flat LCDM these are EXACT: Om(z) = Om constant, j(z) = 1.
So the BLUE curve is a positive control: if the pipeline does not return
Om=0.315 and j=1 on it, numerical differentiation of the digitization is
too noisy and NOTHING about the red curve may be concluded.

j(z) needs a SECOND derivative of a digitized curve — the noisiest thing
here. Stability is checked by varying the smoothing, not assumed.

Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
L0: descriptive.
"""

from __future__ import annotations

from pathlib import Path

import fitz
import numpy as np
from scipy.interpolate import UnivariateSpline

PDF = Path(r"C:\Users\serge\Downloads\multing_intro_figure_v6 (1).pdf")
X0, XS, Y0, YS = 88.35, 171.4917, 345.72, 1.504700
ORANGE = (0.8509804010391235, 0.3490196168422699, 0.14901961386203766)
BLUE = (0.16470588743686676, 0.47058823704719543, 0.8392156958580017)


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
    a = np.array([[(p.x - X0) / XS, 50.0 + (Y0 - p.y) / YS] for p in pts_of(it)])
    a = a[np.argsort(a[:, 0])]
    zz, hh = [], []
    for z, h in a:
        if zz and abs(z - zz[-1]) < 1e-9:
            hh[-1] = (hh[-1] + h) / 2
        else:
            zz.append(z)
            hh.append(h)
    return np.column_stack([zz, hh])


def load():
    pg = fitz.open(PDF)[0]
    segs, blue = [], None
    for it in pg.get_drawings():
        if it.get("width") != 2.0 or len(pts_of(it)) <= 20:
            continue
        if close(it.get("color"), ORANGE):
            segs.append(polyline(it))
        elif close(it.get("color"), BLUE):
            blue = polyline(it)
    m = np.vstack(sorted(segs, key=lambda a: a[0, 0]))
    return m[np.argsort(m[:, 0])], blue


def statefinder(curve, s, zmin=0.05, zmax=1.90, n=400):
    """Return z, q, j, Om for a digitized H(z) curve at smoothing s."""
    zc, hc = curve[:, 0], curve[:, 1]
    m = (zc >= -0.02) & (zc <= 2.05)
    spl = UnivariateSpline(zc[m], hc[m], s=s, k=4)
    z = np.linspace(zmin, zmax, n)
    H = spl(z)
    dH = spl.derivative(1)(z)
    q = -1.0 + (1.0 + z) * dH / H
    dq = np.gradient(q, z)
    j = q * (2 * q + 1) + (1 + z) * dq
    H0 = float(spl(0.0))
    E2 = (H / H0) ** 2
    Om = (E2 - 1.0) / ((1 + z) ** 3 - 1.0)
    return z, q, j, Om, H0


def main():
    mult, blue = load()
    print("=" * 76)
    print("B-1 STATEFINDER — q(z), j(z), Om(z) from the digitized curves")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION   |   L0: descriptive")
    print("=" * 76)

    # ---------- POSITIVE CONTROL on the blue (known flat-LCDM) curve ----------
    print("\n[POSITIVE CONTROL] blue curve is flat-LCDM(Om=0.315) by construction.")
    print("  Expect: Om(z) = 0.315 constant, j(z) = 1.000 constant.\n")
    print(f"  {'smoothing s':>12} {'Om mean':>9} {'Om spread':>10} {'j mean':>8} {'j spread':>9}")
    ok_s = None
    for s in (0.0, 0.01, 0.1, 1.0, 10.0):
        z, q, j, Om, H0 = statefinder(blue, s)
        om_sp = float(np.max(Om) - np.min(Om))
        j_sp = float(np.max(j) - np.min(j))
        print(f"  {s:12.2f} {np.mean(Om):9.4f} {om_sp:10.4f} {np.mean(j):8.4f} {j_sp:9.4f}")
        if ok_s is None and om_sp < 0.02 and abs(np.mean(j) - 1) < 0.05 and j_sp < 0.2:
            ok_s = s
    if ok_s is None:
        print("\n  CONTROL FAILED at every smoothing -> j(z) not recoverable from this")
        print("  digitization. Report q(z)/Om(z) only, and NO jerk-based claim.")
    else:
        print(f"\n  CONTROL PASSED at s={ok_s} -> pipeline recovers LCDM. Using this s.")

    s_use = ok_s if ok_s is not None else 1.0

    # ---------- the two curves side by side ----------
    zb, qb, jb, Omb, H0b = statefinder(blue, s_use)
    zm, qm, jm, Omm, H0m = statefinder(mult, s_use)
    print(f"\n  H0: blue={H0b:.2f}  red={H0m:.2f}")

    print("\n[Om(z) DIAGNOSTIC]  flat-LCDM => constant. Curvature = departure.")
    print(f"  {'z':>6} {'Om_blue':>9} {'Om_red':>9} {'difference':>11}")
    for zz in (0.1, 0.3, 0.5, 0.8, 1.2, 1.6, 1.9):
        i = int(np.argmin(np.abs(zm - zz)))
        print(f"  {zz:6.2f} {Omb[i]:9.4f} {Omm[i]:9.4f} {Omm[i] - Omb[i]:+11.4f}")
    print(
        f"\n  Om_red   range = [{Omm.min():.4f}, {Omm.max():.4f}]  "
        f"spread = {Omm.max() - Omm.min():.4f}"
    )
    print(
        f"  Om_blue  range = [{Omb.min():.4f}, {Omb.max():.4f}]  "
        f"spread = {Omb.max() - Omb.min():.4f}  (control)"
    )

    print("\n[q(z) DECELERATION]")
    print(f"  {'z':>6} {'q_blue':>8} {'q_red':>8}")
    for zz in (0.1, 0.5, 1.0, 1.5, 1.9):
        i = int(np.argmin(np.abs(zm - zz)))
        print(f"  {zz:6.2f} {qb[i]:8.4f} {qm[i]:8.4f}")
    # transition redshift
    for nm, z_, q_ in (("blue", zb, qb), ("red", zm, qm)):
        sgn = np.where(np.diff(np.sign(q_)) != 0)[0]
        zt = f"{z_[sgn[0]]:.3f}" if len(sgn) else "none in range"
        print(f"  q=0 crossing ({nm}): z_t = {zt}")

    if ok_s is not None:
        print("\n[j(z) JERK]  flat-LCDM => j = 1 exactly")
        print(f"  {'z':>6} {'j_blue':>8} {'j_red':>8}")
        for zz in (0.1, 0.5, 1.0, 1.5):
            i = int(np.argmin(np.abs(zm - zz)))
            print(f"  {zz:6.2f} {jb[i]:8.4f} {jm[i]:8.4f}")
        print(
            f"\n  j_red at z=0.1: {jm[int(np.argmin(np.abs(zm - 0.1)))]:.4f} "
            f"(control blue: {jb[int(np.argmin(np.abs(zb - 0.1)))]:.4f})"
        )

    print("\n" + "-" * 76)
    print("READING")
    dom = float(np.max(np.abs(Omm - Omb)))
    print(f"  max |Om_red - Om_blue| = {dom:.4f}")
    print("  Om(z) is measurable from H(z) data alone; current CC precision on")
    print("  Om(z) is roughly 0.05-0.10 per bin, so a departure must exceed that")
    print("  to be claimed. Compare the number above against that scale.")
    print("-" * 76)


if __name__ == "__main__":
    main()
