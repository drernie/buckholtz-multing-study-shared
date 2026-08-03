"""BRIDGE B1 — target reconstruction: what source must MULTING supply?

The published material gives H_MULT(z) at twelve redshifts but no operator
carrying the force law into H(z). B1 does not build that operator. It computes
the TARGET the operator would have to hit: within flat FLRW and standard GR,
what energy density and pressure must an extra component have so that the
expansion rate is exactly the published H_MULT?

    rho_X(a) = 3 H_MULT^2 / (8 pi G) - rho_m0 a^-3 - rho_r0 a^-4
    p_X(a)   = -(2 Hdot + 3 H_MULT^2) / (8 pi G) - rho_r(a)/3
    w_X      = p_X / rho_X
    A_X      = rho_X + 3 p_X          (active gravitational mass density)

Acceleration in standard GR requires rho_total + 3 p_total < 0. That is the
first kill test, and it is a test of the TARGET, not of any bridge.

Three deliberate design points:

1. The matter density is recovered from the paper's own H_FLRW column rather
   than assumed, so the target is expressed in the author's own background.
2. Hdot is computed on a family of interpolants, not one, because the published
   object is twelve points plus a drawn line. A quantity that changes sign or
   order of magnitude across the family is a property of the interpolation, not
   of the model.
3. The reconstructed w_X is compared against the paper's own reported w_eff
   column. Those are two independently published numbers that a single
   FLRW-consistent model must agree on.

Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive
Every number here is a reconstruction from published values, not a measurement.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline, PchipInterpolator
from scipy.optimize import minimize_scalar

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "table_a1_source_verified.csv"
OUT = ROOT / "experiments" / "20260803-bridge" / "artifacts"

# Critical density prefactor: rho_c = 3 H^2 / (8 pi G). Working in units where
# rho is expressed as an equivalent (km/s/Mpc)^2, so 3/(8 pi G) is a common
# factor that cancels from every ratio reported below. Ratios and signs are the
# object of this script; absolute densities are reported in those units only.
OMEGA_R0 = 9.0e-5  # radiation, photons + massless neutrinos, Planck-like


def load() -> pd.DataFrame:
    df = pd.read_csv(DATA, comment="#")
    return df.dropna(subset=["z", "H_MULT", "H_FLRW"]).reset_index(drop=True)


def recover_omega_m(z: np.ndarray, h_flrw: np.ndarray) -> tuple[float, float, float]:
    """Fit flat LCDM to the paper's own H_FLRW column.

    Returns (H0, Omega_m, max relative residual). Using the paper's background
    rather than an external one keeps the target in the author's own units.
    """
    h0 = float(h_flrw[np.argmin(z)])

    def resid(om: float) -> float:
        model = h0 * np.sqrt(om * (1 + z) ** 3 + OMEGA_R0 * (1 + z) ** 4 + (1 - om - OMEGA_R0))
        return float(np.max(np.abs(model / h_flrw - 1.0)))

    r = minimize_scalar(resid, bounds=(0.05, 0.95), method="bounded")
    return h0, float(r.x), float(r.fun)


def hdot_over_h0sq(z: np.ndarray, h: np.ndarray, kind: str) -> np.ndarray:
    """Hdot = -(1+z) H dH/dz, evaluated on a named interpolant."""
    if kind == "cubic":
        f = CubicSpline(z, h, bc_type="not-a-knot")
        dh = f.derivative()(z)
    elif kind == "pchip":
        f = PchipInterpolator(z, h)
        dh = f.derivative()(z)
    elif kind == "loglog":
        g = CubicSpline(np.log1p(z), np.log(h), bc_type="not-a-knot")
        dh = h * g.derivative()(np.log1p(z)) / (1 + z)
    elif kind == "finite":
        dh = np.gradient(h, z, edge_order=2)
    else:
        raise ValueError(kind)
    return -(1 + z) * h * dh


def reconstruct(df: pd.DataFrame, kind: str, h0: float, om: float) -> pd.DataFrame:
    z = df["z"].to_numpy(float)
    hm = df["H_MULT"].to_numpy(float)
    a = 1.0 / (1 + z)

    rho_m = om * h0**2 * a**-3
    rho_r = OMEGA_R0 * h0**2 * a**-4
    hdot = hdot_over_h0sq(z, hm, kind)

    rho_x = hm**2 - rho_m - rho_r
    p_x = -(2 * hdot + 3 * hm**2) - rho_r / 3.0

    rho_tot = hm**2
    p_tot = -(2 * hdot + 3 * hm**2)

    return pd.DataFrame(
        {
            "z": z,
            "interp": kind,
            "rho_X": rho_x,
            "p_X": p_x,
            "w_X": np.where(np.abs(rho_x) > 1e-12, p_x / rho_x, np.nan),
            "A_X": rho_x + 3 * p_x,
            "A_total": rho_tot + 3 * p_tot,
            "q": -1.0 - hdot / hm**2,
        }
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    df = load()
    z = df["z"].to_numpy(float)

    h0, om, res = recover_omega_m(z, df["H_FLRW"].to_numpy(float))
    print("=" * 78)
    print("BRIDGE B1 — target reconstruction")
    print("NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION | L0 descriptive")
    print("=" * 78)
    print("\n[1] background recovered from the paper's own H_FLRW column")
    print(f"    H0 = {h0:.2f} km/s/Mpc     Omega_m = {om:.4f}")
    print(f"    max |H_fit/H_FLRW - 1| = {res:.4%}")

    # ---- the H_w_eff column: is it a fit to H_obs or a prediction? ----
    print("\n[2] what is the published H_w_eff column?")
    for target in ("H_obs", "H_MULT", "H_FLRW"):
        d = df["H_w_eff"].to_numpy(float) / df[target].to_numpy(float) - 1.0
        print(
            f"    vs {target:7s}: max |rel dev| = {np.max(np.abs(d)):9.4%}   rms = {np.sqrt(np.mean(d**2)):.4%}"
        )

    # ---- reconstruction across the interpolant family ----
    print("\n[3] reconstructed target, across four interpolants")
    frames = [reconstruct(df, k, h0, om) for k in ("cubic", "pchip", "loglog", "finite")]
    allf = pd.concat(frames, ignore_index=True)

    piv = allf.pivot_table(index="z", columns="interp", values="w_X")
    spread = (piv.max(axis=1) - piv.min(axis=1)).abs()
    print(
        f"\n    w_X spread across interpolants: median {spread.median():.4f}, max {spread.max():.4f}"
    )

    base = frames[0]
    print(
        f"\n    {'z':>6} {'w_X req':>10} {'w_eff pub':>10} {'diff':>9} {'rho_X':>10} {'A_X':>11} {'q':>8}"
    )
    for i, row in base.iterrows():
        wpub = df["w_eff"].iloc[i]
        diff = row["w_X"] - wpub if pd.notna(wpub) else np.nan
        print(
            f"    {row['z']:6.2f} {row['w_X']:10.4f} "
            f"{wpub if pd.notna(wpub) else float('nan'):10.4f} {diff:9.4f} "
            f"{row['rho_X']:10.1f} {row['A_X']:11.1f} {row['q']:8.4f}"
        )

    # ---- kill test 1: sign of the active gravitational mass ----
    print("\n[4] KILL TEST 1 — acceleration needs rho_total + 3 p_total < 0")
    verdict = {}
    for f in frames:
        k = f["interp"].iloc[0]
        neg_lowz = bool(np.all(f.loc[f["z"] <= 0.5, "A_total"] < 0))
        n_neg = int(np.sum(f["A_total"] < 0))
        verdict[k] = {"negative_at_z_le_0.5": neg_lowz, "n_negative_of_12": n_neg}
        print(f"    {k:8s}: A_total < 0 at z<=0.5 : {neg_lowz}   negative at {n_neg}/12 nodes")

    # ---- kill test 2: does the published w_eff reproduce the published H_MULT? ----
    print("\n[5] KILL TEST 2 — integrate the published w_eff forward and compare")
    ok = df["w_eff"].notna().to_numpy()
    zw, ww = z[ok], df["w_eff"].to_numpy(float)[ok]
    lna = -np.log1p(zw)
    order = np.argsort(lna)
    integ = np.concatenate([[0.0], np.cumsum(np.diff(lna[order]) * 3 * (1 + ww[order][:-1]))])
    rho_x_w = np.empty_like(integ)
    rho_x_w[order] = np.exp(-integ)
    rho_x0 = (1 - om - OMEGA_R0) * h0**2
    h_from_w = np.sqrt(
        om * h0**2 * (1 + zw) ** 3 + OMEGA_R0 * h0**2 * (1 + zw) ** 4 + rho_x0 * rho_x_w
    )
    for target, col in (("H_MULT", "H_MULT"), ("H_obs", "H_obs"), ("H_w_eff", "H_w_eff")):
        d = h_from_w / df[col].to_numpy(float)[ok] - 1.0
        print(f"    w_eff-integrated H vs {target:8s}: max |rel dev| = {np.max(np.abs(d)):8.3%}")

    allf.to_csv(OUT / "b1_target_reconstruction.csv", index=False)
    (OUT / "b1_summary.json").write_text(
        json.dumps(
            {
                "background": {"H0": h0, "Omega_m": om, "max_rel_resid": res},
                "w_X_spread_across_interpolants": {
                    "median": float(spread.median()),
                    "max": float(spread.max()),
                },
                "kill_test_1_active_mass": verdict,
                "label": "OUR_RECONSTRUCTION / NOT_VALIDATION / NOT_REFUTATION",
            },
            indent=2,
        )
    )
    print(f"\n    artifacts -> {OUT}")


if __name__ == "__main__":
    main()
