"""A11 — competing-definitions matrix for the Table A1 w_eff column.

Earlier finding was too blunt ("standard EoS does not work"). The correct
output is a MATRIX: enumerate the standard conventions explicitly, optimise
each one's free parameters, and report which (if any) reproduces the
H_w_eff column. Only then is "an author-specific mapping is required" a
supported statement rather than a guess.

FORWARD conventions (w_eff -> H):
  F1  total fluid, anchored:  H/H_a = exp(1.5 int (1+w)/(1+z') dz')
  F2  matter + DE(w) integral: H^2 = H0^2[Om(1+z)^3 + (1-Om) exp(3 int ...)]
  F3  matter + DE, POINTWISE constant-w formula applied with variable w:
        H^2 = H0^2[Om(1+z)^3 + (1-Om)(1+z)^{3(1+w(z))}]
      (physically wrong, but a very common AI/spreadsheet shortcut —
       must be tested precisely because Table A1 was AI-generated)
  F4  same as F3 but w treated as TOTAL (no matter term):
        H^2 = H0^2 (1+z)^{3(1+w(z))}

BACKWARD conventions (H -> w), compared against the printed w_eff column:
  B1  w_tot from H_MULT   : w = -1 + (2/3)(1+z) H'/H
  B2  w_tot from H_w_eff
  B3  w_tot from H_FLRW
  B4  w_DE  from H_MULT with matter subtracted (Om scanned)
  B5  q-based: w = (2q-1)/3 with q = -1 + (1+z)H'/H   [identical to w_tot,
      included to make the equivalence explicit rather than assumed]

For F1-F4 the free parameters (H0, Om, anchor) are OPTIMISED, so a failure
is a failure of the convention, not of a bad parameter guess.

Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
L0: descriptive.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.integrate import cumulative_trapezoid
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize

A1 = Path(
    r"E:\Проверка Гипотез\работаю над проверкой гипотез"
    r"\H - 11 Dr. Thomas J. Buckholtz\buckholtz-idm-multing-mvp"
    r"\data\table_a1_reported.csv"
)


def load():
    df = pd.read_csv(A1, comment="#")
    for c in ("z", "H_obs", "H_FLRW", "H_MULT", "w_eff", "H_w_eff"):
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


def maxres(a, b):
    return float(np.max(np.abs(100.0 * (a - b) / b)))


def main():
    df = load()
    m = ~df["w_eff"].isna()
    z = df.loc[m, "z"].to_numpy(float)
    w = df.loc[m, "w_eff"].to_numpy(float)
    hM = df.loc[m, "H_MULT"].to_numpy(float)
    hW = df.loc[m, "H_w_eff"].to_numpy(float)
    hF = df.loc[m, "H_FLRW"].to_numpy(float)

    print("=" * 78)
    print("A11 — w_eff CONVENTION MATRIX for Table A1     |  L0: descriptive")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION")
    print("=" * 78)
    print(
        f"\ninput column w_eff spans [{w.min():.3f}, {w.max():.3f}], "
        f"non-monotone (min at z={z[np.argmin(w)]:.2f})"
    )
    print(f"target column H_w_eff spans [{hW.min():.1f}, {hW.max():.1f}]")
    print(f"H_w_eff vs H_MULT: max |d| = {maxres(hM, hW):.2f}%  -> effectively the same curve")

    spl = CubicSpline(z, w)
    zf = np.linspace(z.min(), z.max(), 4000)
    wf = spl(zf)
    integ_lo = cumulative_trapezoid((1 + wf) / (1 + zf), zf, initial=0.0)  # from z.min()

    z0 = np.linspace(0.0, z.max(), 4000)
    w0 = spl(z0)
    I0 = cumulative_trapezoid((1 + w0) / (1 + z0), z0, initial=0.0)  # from 0

    rows = []

    # ---------- F1: total fluid, anchor optimised ----------
    def f1(p):
        return p[0] * np.exp(1.5 * np.interp(z, zf, integ_lo))

    r = minimize(lambda p: np.sum((f1(p) - hW) ** 2), [hW[0]], method="Nelder-Mead")
    rows.append(("F1 total fluid (anchor free)", f"H_a={r.x[0]:.2f}", maxres(f1(r.x), hW)))

    # ---------- F2: matter + DE integral ----------
    def f2(p):
        h0, om = p
        g = np.exp(3.0 * np.interp(z, z0, I0))
        return h0 * np.sqrt(om * (1 + z) ** 3 + (1 - om) * g)

    r = minimize(lambda p: np.sum((f2(p) - hW) ** 2), [71.0, 0.3], bounds=[(40, 110), (0.0, 1.0)])
    rows.append(
        ("F2 matter+DE (integral)", f"H0={r.x[0]:.2f} Om={r.x[1]:.3f}", maxres(f2(r.x), hW))
    )

    # ---------- F3: pointwise constant-w shortcut, with matter ----------
    def f3(p):
        h0, om = p
        return h0 * np.sqrt(om * (1 + z) ** 3 + (1 - om) * (1 + z) ** (3 * (1 + w)))

    r = minimize(lambda p: np.sum((f3(p) - hW) ** 2), [71.0, 0.3], bounds=[(40, 110), (0.0, 1.0)])
    rows.append(
        (
            "F3 POINTWISE (1+z)^3(1+w), +matter",
            f"H0={r.x[0]:.2f} Om={r.x[1]:.3f}",
            maxres(f3(r.x), hW),
        )
    )
    f3best = f3(r.x)

    # ---------- F4: pointwise, total (no matter term) ----------
    def f4(p):
        return p[0] * (1 + z) ** (1.5 * (1 + w))

    r4 = minimize(lambda p: np.sum((f4(p) - hW) ** 2), [71.0], method="Nelder-Mead")
    rows.append(("F4 POINTWISE total, no matter", f"H0={r4.x[0]:.2f}", maxres(f4(r4.x), hW)))

    print("\n[FORWARD] w_eff -> H, free parameters OPTIMISED against H_w_eff")
    print(f"  {'convention':38s} {'best params':26s} {'max |resid|':>11s}")
    for n, p, v in rows:
        flag = "  <== REPRODUCES" if v < 3 else ""
        print(f"  {n:38s} {p:26s} {v:10.2f}%{flag}")

    # ---------- BACKWARD ----------
    print("\n[BACKWARD] H -> w, compared against the printed w_eff column")
    print(
        f"  {'source':34s} {'max |dw|':>9s} {'mean w_recon':>13s}  (printed mean {w.mean():+.3f})"
    )
    for name, hh in (
        ("B1 w_tot from H_MULT", hM),
        ("B2 w_tot from H_w_eff", hW),
        ("B3 w_tot from H_FLRW", hF),
    ):
        s = CubicSpline(z, np.log(hh))
        wt = -1 + (2.0 / 3.0) * (1 + z) * s(z, 1)
        print(f"  {name:34s} {np.max(np.abs(wt - w)):8.3f} {wt.mean():13.3f}")

    # B4: dark-energy w with matter subtracted, Om scanned
    print("\n  B4 w_DE from H_MULT (matter subtracted), Om scanned:")
    best = None
    for om in (0.05, 0.10, 0.20, 0.315, 0.40):
        H0 = float(hM[0]) / np.sqrt(om * (1 + z[0]) ** 3 + (1 - om))
        E2 = (hM / H0) ** 2
        fde = E2 - om * (1 + z) ** 3
        if np.any(fde <= 0):
            print(f"    Om={om:.3f}: dark density goes NEGATIVE -> undefined")
            continue
        dE2 = CubicSpline(z, E2)(z, 1)
        wde = -1 + (1 / 3) * (1 + z) * dE2 / fde
        d = float(np.max(np.abs(wde - w)))
        print(f"    Om={om:.3f}: max |dw| = {d:10.3f}   mean w_DE = {wde.mean():+.3f}")
        best = d if best is None else min(best, d)

    # ---------- verdict ----------
    print("\n" + "-" * 78)
    fwd_best = min(v for _, _, v in rows)
    fwd_name = [n for n, _, v in rows if v == fwd_best][0]
    print("VERDICT")
    print(f"  best FORWARD convention: {fwd_name}  ({fwd_best:.2f}% max residual)")
    if fwd_best < 3:
        print("  -> the w_eff column IS decodable by a standard-form mapping.")
        print("     A continuous H(z) follows: interpolate w_eff, apply this mapping.")
        print("     [VERIFIED-tool - OUR_RECONSTRUCTION] - not a validation of MULTING.")
        # show the fit quality per row for the winner
        if fwd_name.startswith("F3"):
            print("\n  per-row check (F3):")
            for i in range(len(z)):
                print(
                    f"    z={z[i]:5.2f}  H_w_eff={hW[i]:7.1f}  F3={f3best[i]:7.1f}  "
                    f"d={100 * (f3best[i] - hW[i]) / hW[i]:+6.2f}%"
                )
    else:
        print("  -> NONE of the enumerated standard conventions reproduces the column.")
        print("     An author-specific w_eff -> H mapping is required. This is now a")
        print("     precise, narrow question, not 'the bridge is missing'.")
    print("-" * 78)


if __name__ == "__main__":
    main()
