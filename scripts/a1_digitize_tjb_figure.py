"""A1 — digitize TJB's 2026-08-02 figure and compute the statistics it omits.

The figure (multing_intro_figure_v6.pdf) shows MULTING vs LCDM over cosmic
chronometer data but carries NO error bars, NO chi2, NO model comparison.
This script extracts the actual vector paths from the PDF and computes them.

Method:
  1. Calibrate PDF coords -> (z, H) from axis tick label positions.
  2. Extract the 4 orange MULTING segments + the blue LCDM curve as polylines.
  3. Extract the black CC data markers (to check the "31 points" claim).
  4. Compute chi2 of each MODEL against the CC data actually plotted,
     and against our canonical 27-point set (data/hz_cc.csv).
  5. Report Delta-AIC under explicit assumptions about parameter counts.

EVERY number here is OUR_RECONSTRUCTION from a digitized image.
Digitization error is estimated and reported, not hidden.
Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
"""

from __future__ import annotations

from pathlib import Path

import fitz
import numpy as np
import pandas as pd

PDF = Path(r"C:\Users\serge\Downloads\multing_intro_figure_v6 (1).pdf")
CC_CSV = Path(
    r"E:\Проверка Гипотез\работаю над проверкой гипотез"
    r"\H - 11 Dr. Thomas J. Buckholtz\buckholtz-idm-multing-mvp\data\hz_cc.csv"
)

# --- calibration from tick labels (verified in prior step) ---
X0, Z0 = 88.35, 0.0
XS = 171.4917  # px per unit z
Y0, H0V = 345.72, 50.0
YS = 1.504700  # px per unit H (y decreases upward)

ORANGE = (0.8509804010391235, 0.3490196168422699, 0.14901961386203766)
BLUE = (0.16470588743686676, 0.47058823704719543, 0.8392156958580017)
DARK = (0.1725490242242813, 0.1725490242242813, 0.16470588743686676)


def px2z(x: float) -> float:
    return (x - X0) / XS


def px2h(y: float) -> float:
    return H0V + (Y0 - y) / YS


def close(a, b, t=1e-6) -> bool:
    return a is not None and all(abs(u - v) < t for u, v in zip(a, b, strict=False))


def path_points(item) -> list:
    pts = []
    for el in item["items"]:
        if el[0] == "l":
            pts += [el[1], el[2]]
        elif el[0] == "c":
            pts += [el[1], el[2], el[3], el[4]]
        elif el[0] == "re":
            pts += [el[1].tl, el[1].br]
    return pts


def polyline(item) -> np.ndarray:
    pts = path_points(item)
    arr = np.array([[px2z(p.x), px2h(p.y)] for p in pts])
    order = np.argsort(arr[:, 0])
    arr = arr[order]
    # collapse duplicate z
    zz, hh = [], []
    for z, h in arr:
        if zz and abs(z - zz[-1]) < 1e-9:
            hh[-1] = (hh[-1] + h) / 2
        else:
            zz.append(z)
            hh.append(h)
    return np.column_stack([zz, hh])


def lcdm(z, h0, om=0.315):
    return h0 * np.sqrt(om * (1 + z) ** 3 + (1 - om))


def main() -> None:
    doc = fitz.open(PDF)
    page = doc[0]
    draws = page.get_drawings()

    mult_segs, blue_curve, markers = [], None, []
    for it in draws:
        col, w = it.get("color"), it.get("width")
        pts = path_points(it)
        if close(col, ORANGE) and w == 2.0 and len(pts) > 20:
            mult_segs.append(polyline(it))
        elif close(col, BLUE) and w == 2.0 and len(pts) > 20:
            blue_curve = polyline(it)
        elif close(col, DARK) and close(it.get("fill"), DARK) and w == 1.0:
            xs = [p.x for p in pts]
            ys = [p.y for p in pts]
            cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
            markers.append((px2z(cx), px2h(cy)))

    mult = np.vstack(sorted(mult_segs, key=lambda a: a[0, 0]))
    mult = mult[np.argsort(mult[:, 0])]
    markers = np.array(sorted(markers))

    print("=" * 72)
    print("A1 — DIGITIZED TJB FIGURE (2026-08-02) + THE STATISTICS IT OMITS")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION")
    print("=" * 72)
    print(
        f"\nMULTING curve: {len(mult_segs)} segments, {len(mult)} pts, "
        f"z in [{mult[0, 0]:.3f}, {mult[-1, 0]:.3f}]"
    )
    print(
        f"LCDM curve   : {len(blue_curve)} pts, "
        f"z in [{blue_curve[0, 0]:.3f}, {blue_curve[-1, 0]:.3f}]"
    )
    print(f"Data markers extracted: {len(markers)}")

    # --- calibration sanity: LCDM should be a clean flat-LCDM with Om=0.315 ---
    h0_blue = float(np.interp(0.0, blue_curve[:, 0], blue_curve[:, 1]))
    resid = blue_curve[:, 1] - lcdm(blue_curve[:, 0], h0_blue)
    print("\n[CALIBRATION CHECK] blue curve vs analytic flat-LCDM(Om=0.315):")
    print(f"  implied H0 = {h0_blue:.2f}")
    print(
        f"  max |residual| = {np.max(np.abs(resid)):.3f} km/s/Mpc "
        f"({100 * np.max(np.abs(resid)) / h0_blue:.2f}% of H0)"
    )
    print("  -> this bounds our TOTAL digitization error (calib + path sampling)")

    # --- MULTING value at z=0 ---
    h0_mult = float(np.interp(0.0, mult[:, 0], mult[:, 1]))
    print(f"\n[ANCHORS] MULTING(z=0) = {h0_mult:.2f}   LCDM(z=0) = {h0_blue:.2f}")
    print(f"  gap at z=0 = {h0_mult - h0_blue:.2f} km/s/Mpc")

    # --- the z<0 claim ---
    zneg = mult[mult[:, 0] < 0]
    if len(zneg):
        print(f"\n[z<0 SEGMENT] {len(zneg)} pts, z in [{zneg[0, 0]:.3f}, {zneg[-1, 0]:.3f}]")
        print(
            f"  H at z={zneg[0, 0]:.2f}: MULTING={zneg[0, 1]:.1f}  "
            f"LCDM={lcdm(zneg[0, 0], h0_blue):.1f}  "
            f"divergence={zneg[0, 1] - lcdm(zneg[0, 0], h0_blue):.1f} km/s/Mpc"
        )

    # --- compare against OUR canonical CC set ---
    cc = pd.read_csv(CC_CSV, comment="#")
    zc = cc["z"].to_numpy(float)
    hc = cc["Hz_km_s_Mpc"].to_numpy(float)
    sc = cc["sigma_Hz"].to_numpy(float)

    m_at = np.interp(zc, mult[:, 0], mult[:, 1])
    l_at = np.interp(zc, blue_curve[:, 0], blue_curve[:, 1])
    chi2_m = float(np.sum(((hc - m_at) / sc) ** 2))
    chi2_l = float(np.sum(((hc - l_at) / sc) ** 2))
    n = len(zc)

    print(f"\n[CHI2 vs our canonical CC set, n={n} (Moresco+2022)]")
    print(f"  MULTING : chi2 = {chi2_m:7.2f}   chi2/n = {chi2_m / n:.3f}")
    print(f"  LCDM    : chi2 = {chi2_l:7.2f}   chi2/n = {chi2_l / n:.3f}")
    print(f"  difference: chi2(MULT) - chi2(LCDM) = {chi2_m - chi2_l:+.2f}")

    print("\n[DELTA-AIC under explicit parameter-count assumptions]")
    print("  (TJB's figure does not state how many free params MULTING has;")
    print("   LCDM here is FIXED Planck Om=0.315 + an H0 anchor -> k=1)")
    for k_m in (1, 2, 3):
        aic_m = chi2_m + 2 * k_m
        aic_l = chi2_l + 2 * 1
        d = aic_m - aic_l
        verdict = (
            "equivalent (<2)"
            if abs(d) < 2
            else "weak (2-4)"
            if abs(d) < 4
            else "moderate (4-10)"
            if abs(d) < 10
            else "strong (>10)"
        )
        fav = "LCDM" if d > 0 else "MULTING"
        print(f"  k_MULT={k_m}: dAIC = {d:+7.2f}  -> favours {fav:7s} [{verdict}]")

    # --- markers found on the figure ---
    if len(markers):
        mk = markers[(markers[:, 0] > -0.05) & (markers[:, 0] < 2.5)]
        print(
            f"\n[DATA MARKERS on figure] {len(mk)} in plot area, "
            f"z in [{mk[:, 0].min():.3f}, {mk[:, 0].max():.3f}]"
        )
        print(f"  legend claims 31 CC points; our canonical set has {n}")


if __name__ == "__main__":
    main()
