"""BRIDGE B0 — is Table A1 a usable background for a bridge reconstruction?

Before reconstructing what source MULTING must supply, the background it is
supplied against has to be identified. The published table carries a column
labelled "H_FLRW: LCDM expansion rate", so the natural move is to express the
target in the author's own background rather than one we choose.

This script checks whether that is possible. It asks four questions of the
published table alone, with no reference to MULTING:

  Q1  Are the (z, t) pairs consistent with any flat LCDM age relation?
  Q2  Is the H_FLRW column the expansion history of a standard cosmology?
  Q3  Does H derived from the table's own (z, t) pairs match any H column?
  Q4  Do the H_obs entries lie inside the range where cosmic chronometers exist?

The answers determine whether the bridge's target reconstruction can be done in
the author's background (preferred) or must be done in one we state explicitly
and label as ours (fallback).

Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive
This audits an published table for internal consistency. It does not evaluate
the MULTING model, and no result here supports or refutes it.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.integrate import quad
from scipy.optimize import differential_evolution

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "experiments" / "20260803-bridge" / "artifacts"
GYR = 977.7922  # (1/Gyr) -> km/s/Mpc

# Planck 2018 TT,TE,EE+lowE+lensing, flat LCDM. Stated, not fitted.
PLANCK = {"H0": 67.36, "Om": 0.3153, "Ob": 0.04930}


def lcdm_age(z: float, h0: float, om: float) -> float:
    def integrand(x: float) -> float:
        return 1.0 / ((1 + x) * h0 * np.sqrt(om * (1 + x) ** 3 + (1 - om)))

    return quad(integrand, z, np.inf)[0] * GYR


def q1_time_redshift(df: pd.DataFrame) -> dict:
    z = df["z"].to_numpy(float)
    t = df["time_gyr"].to_numpy(float)
    t_lcdm = np.array([lcdm_age(zz, PLANCK["H0"], PLANCK["Om"]) for zz in z])
    diff = t - t_lcdm
    steps = np.diff(t)
    return {
        "t_table": t.tolist(),
        "t_lcdm": np.round(t_lcdm, 3).tolist(),
        "diff_gyr": np.round(diff, 3).tolist(),
        "max_abs_diff_gyr": float(np.max(np.abs(diff))),
        "ratio_at_highest_z": float(t[-1] / t_lcdm[-1]),
        "time_column_is_integer_grid": bool(np.allclose(steps[1:], -1.0)),
    }


def q2_which_cosmology(df: pd.DataFrame) -> dict:
    z = df["z"].to_numpy(float)
    hf = df["H_FLRW"].to_numpy(float)

    def flat_lcdm(zz, p):
        return p[0] * np.sqrt(p[1] * (1 + zz) ** 3 + (1 - p[1]))

    def flat_wcdm(zz, p):
        return p[0] * np.sqrt(p[1] * (1 + zz) ** 3 + (1 - p[1]) * (1 + zz) ** (3 * (1 + p[2])))

    def power_law(zz, p):
        return p[0] * (1 + zz) ** p[1]

    def cpl(zz, p):
        de = (1 - p[1]) * (1 + zz) ** (3 * (1 + p[2] + p[3])) * np.exp(-3 * p[3] * zz / (1 + zz))
        return p[0] * np.sqrt(p[1] * (1 + zz) ** 3 + de)

    models = [
        ("flat LCDM", flat_lcdm, [(50, 90), (0.01, 0.99)]),
        ("flat wCDM", flat_wcdm, [(50, 90), (0.01, 0.99), (-2.5, 0.5)]),
        ("power law H~(1+z)^n", power_law, [(50, 90), (0.1, 2.0)]),
        ("CPL w0-wa", cpl, [(50, 90), (0.01, 0.99), (-2.5, 0.5), (-3.0, 3.0)]),
    ]
    fits = {}
    for name, fn, bounds in models:
        with np.errstate(invalid="ignore"):
            res = differential_evolution(
                lambda p, _fn=fn: float(np.max(np.abs(np.nan_to_num(_fn(z, p), nan=1e9) / hf - 1))),
                bounds,
                seed=1,
                tol=1e-10,
            )
        fits[name] = {
            "max_rel_residual": float(res.fun),
            "params": [float(v) for v in res.x],
            "Omega_m": float(res.x[1])
            if len(res.x) > 1 and name != "power law H~(1+z)^n"
            else None,
        }

    planck_pred = PLANCK["H0"] * np.sqrt(PLANCK["Om"] * (1 + z) ** 3 + (1 - PLANCK["Om"]))
    return {
        "fits": fits,
        "planck_vs_table": {
            "z": z.tolist(),
            "H_planck": np.round(planck_pred, 1).tolist(),
            "H_FLRW_table": hf.tolist(),
            "ratio": np.round(planck_pred / hf, 3).tolist(),
        },
        "baryon_floor": PLANCK["Ob"],
    }


def q3_h_from_zt(df: pd.DataFrame) -> dict:
    z = df["z"].to_numpy(float)
    t = df["time_gyr"].to_numpy(float)
    order = np.argsort(t)
    dzdt = np.gradient(z[order], t[order], edge_order=2)
    h_zt = np.empty_like(z)
    h_zt[order] = -dzdt / (1 + z[order]) * GYR
    out = {"H_from_zt": np.round(h_zt, 1).tolist()}
    for col in ("H_obs", "H_FLRW", "H_MULT"):
        d = h_zt / df[col].to_numpy(float) - 1.0
        out[f"median_abs_rel_dev_vs_{col}"] = float(np.median(np.abs(d)))
    return out


def q4_observational_support(df: pd.DataFrame) -> dict:
    cc_path = ROOT / "data" / "hz_cc.csv"
    if not cc_path.exists():
        return {"cc_available": False}
    cc = pd.read_csv(cc_path)
    zmax = float(cc["z"].max())
    z = df["z"].to_numpy(float)
    return {
        "cc_available": True,
        "cc_n": int(len(cc)),
        "cc_z_range": [float(cc["z"].min()), zmax],
        "table_rows_above_cc_range": int(np.sum(z > zmax)),
        "table_rows_total": int(len(z)),
        "z_values_above": z[z > zmax].tolist(),
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(ROOT / "data" / "table_a1_source_verified.csv", comment="#").dropna(
        subset=["z", "H_FLRW"]
    )

    print("=" * 78)
    print("BRIDGE B0 — is Table A1 a usable background?")
    print("NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION | L0 descriptive")
    print("=" * 78)

    r1 = q1_time_redshift(df)
    print("\n[Q1] are the (z, t) pairs a flat-LCDM age relation?")
    print(f"     time column is an integer-Gyr grid : {r1['time_column_is_integer_grid']}")
    print(f"     max |t_table - t_LCDM|             : {r1['max_abs_diff_gyr']:.2f} Gyr")
    print(f"     t_table / t_LCDM at the highest z  : {r1['ratio_at_highest_z']:.2f}x")

    r2 = q2_which_cosmology(df)
    print("\n[Q2] is H_FLRW the expansion history of a standard cosmology?")
    print(f"     {'model':22s} {'max resid':>10}  {'Omega_m':>8}")
    for name, f in r2["fits"].items():
        om = f["Omega_m"]
        print(
            f"     {name:22s} {f['max_rel_residual']:9.2%}  {om if om is not None else float('nan'):8.4f}"
        )
    print(f"     baryon density alone is Omega_b = {r2['baryon_floor']:.4f}")
    print(
        f"     Planck LCDM at z = {df['z'].iloc[-1]:.1f}: {r2['planck_vs_table']['H_planck'][-1]:.0f}"
        f"  vs table {r2['planck_vs_table']['H_FLRW_table'][-1]:.1f} km/s/Mpc"
    )

    r3 = q3_h_from_zt(df)
    print("\n[Q3] does H derived from the table's own (z, t) pairs match any H column?")
    for col in ("H_obs", "H_FLRW", "H_MULT"):
        print(f"     vs {col:7s}: median |rel dev| = {r3[f'median_abs_rel_dev_vs_{col}']:7.1%}")

    r4 = q4_observational_support(df)
    print("\n[Q4] do the H_obs entries lie where cosmic chronometers exist?")
    if r4["cc_available"]:
        print(
            f"     CC data: n = {r4['cc_n']}, z in [{r4['cc_z_range'][0]:.3f}, {r4['cc_z_range'][1]:.3f}]"
        )
        print(
            f"     table rows above that range: {r4['table_rows_above_cc_range']} of "
            f"{r4['table_rows_total']}, at z = {r4['z_values_above']}"
        )

    best = min(f["max_rel_residual"] for f in r2["fits"].values())
    usable = bool(best < 0.02 and r1["max_abs_diff_gyr"] < 0.5)
    print("\n" + "-" * 78)
    print(f"VERDICT: Table A1 usable as the bridge's background = {usable}")
    if not usable:
        print("  The target reconstruction cannot be expressed in the author's own")
        print("  background. It must be done in a background WE state explicitly and")
        print("  label as ours. Any rho_X, p_X so obtained is conditional on that")
        print("  choice and is not a property of the published model.")
    print("-" * 78)

    (OUT / "b0_table_a1_audit.json").write_text(
        json.dumps(
            {"Q1": r1, "Q2": r2, "Q3": r3, "Q4": r4, "background_usable": usable},
            indent=2,
        )
    )
    print(f"\n  artifact -> {OUT / 'b0_table_a1_audit.json'}")


if __name__ == "__main__":
    main()
