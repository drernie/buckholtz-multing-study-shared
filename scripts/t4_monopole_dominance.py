"""t4_monopole_dominance.py — Is the monopole's dominance fundamental, or is the
specific (k_A r_A)^2/D^4 quadrupole FORM bad? (docs/132 task T4; R011 open question)

STRICT FALSIFICATION FRAMING — NO_BRIDGE_FITTING (facts.json _meta.constraints):
  We do NOT fit/optimize any coefficient against Table A1 or H(z). We test a FIXED,
  PRE-SPECIFIED library of single-form physical tracers phi_i(k_A, r_A, m_A, D, z),
  each with NO free parameter, and rank them by Pearson r vs the real cosmic-chronometer
  H_CC(z). Plus a permutation null (shuffle cluster pairings) and a 70/30 holdout.
  This answers "does ANY principled fixed combination beat the monopole" WITHOUT a
  coefficient search. If a different fixed form beats the monopole -> the quadrupole
  FORM was the culprit. If the monopole beats every fixed form -> monopole-dominance
  robust. A trivial (1+z) tracer (no cluster physics) is included as a reference ceiling.

Labels: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
Evidence: [VERIFIED-BASH] on real n=443 MCXC clusters vs Moresco+2022 CC H(z).
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import interpolate, stats

DATA = Path(__file__).resolve().parent.parent / "data"
H_ANCHOR = 73.0
D0 = 100.0  # Mpc; per PASS-A (docs/122) only eta=beta/D0 is observable, D0 is a scale
RNG = np.random.default_rng(20260722)


def load() -> tuple[pd.DataFrame, np.ndarray, np.ndarray]:
    clusters = pd.read_csv(DATA / "clusters_clean.csv")
    hz = pd.read_csv(DATA / "hz_cc.csv")
    df = clusters[clusters["Ethermal_c2_Msun"].notna()].sort_values("z").reset_index(drop=True)
    z_cc, H_cc = hz["z"].to_numpy(), hz["Hz_km_s_Mpc"].to_numpy()
    return df, z_cc, H_cc


def hcc_interp(z_cc: np.ndarray, H_cc: np.ndarray, z: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    f = interpolate.interp1d(z_cc, H_cc, kind="linear", bounds_error=False, fill_value=np.nan)
    Hi = f(z)
    valid = np.isfinite(Hi) & (z >= z_cc.min()) & (z <= z_cc.max())
    return Hi, valid


def r_of_phi(phi: np.ndarray, Hcc: np.ndarray, base_valid: np.ndarray) -> tuple[float, int]:
    """Pearson r between H_MULT = H_ANCHOR*sqrt(phi/phi_ref) and H_CC, over valid points."""
    pos = np.isfinite(phi) & (phi > 0) & base_valid
    if pos.sum() < 5:
        return float("nan"), int(pos.sum())
    phi_ref = phi[pos][0]  # lowest-z valid cluster as anchor (same convention as R011)
    Hm = np.where(pos, H_ANCHOR * np.sqrt(np.maximum(phi / phi_ref, 0.0)), np.nan)
    final = pos & np.isfinite(Hm) & (Hm > 0) & (Hm < 1e6)
    if final.sum() < 5:
        return float("nan"), int(final.sum())
    r, _ = stats.pearsonr(Hm[final], Hcc[final])
    return float(r), int(final.sum())


def tracer_library(z, m, k, r, D):
    """FIXED pre-specified single-form tracers. Keys = physical description. NO fit."""
    D2, D3, D4 = D**2, D**3, D**4
    return {
        "monopole  m_A/D^2 (R011 baseline)": m / D2,
        "dipole-shape  k_A*r_A/D^3": k * r / D3,
        "quadrupole-shape  (k_A*r_A)^2/D^4": (k * r) ** 2 / D4,
        "thermal monopole  k_A/D^2": k / D2,
        "radius monopole  r_A/D^2": r / D2,
        "mass only  m_A": m,
        "thermal only  k_A": k,
        "radius only  r_A": r,
        "m_A/D^3": m / D3,
        "m_A/D^4": m / D4,
        "k_A*r_A/D^2": k * r / D2,
        "m_A*k_A/D^4": m * k / D4,
        "trivial (1+z)^2  [NO cluster physics; reference ceiling]": (1.0 + z) ** 2,
    }


def main() -> None:
    print("=" * 74)
    print("T4 — Monopole dominance: fundamental, or bad quadrupole form?")
    print("NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_BRIDGE_FITTING")
    print("=" * 74)
    df, z_cc, H_cc = load()
    z = df["z"].to_numpy()
    m = df["M500c_Msun"].to_numpy()
    k = df["Ethermal_c2_Msun"].to_numpy()
    r = df["R500c_Mpc"].to_numpy()
    D = D0 / (1.0 + z)
    Hi, valid = hcc_interp(z_cc, H_cc, z)
    print(f"\nClusters with k_A=E_thermal/c^2: n={len(df)}  z=[{z.min():.3f},{z.max():.3f}]")
    print(f"CC H(z) points: {len(z_cc)}  in-range valid clusters: {int(valid.sum())}")

    lib = tracer_library(z, m, k, r, D)
    print("\n[1] FIXED tracer library (no free parameters) ranked by Pearson r vs H_CC:")
    print(f"    {'form':<52}{'r':>9}{'n':>6}")
    results = {}
    for name, phi in lib.items():
        rr, n = r_of_phi(phi, Hi, valid)
        results[name] = rr
        print(f"    {name:<52}{rr:>9.4f}{n:>6}")

    n_forms = len(lib)
    mono_key = "monopole  m_A/D^2 (R011 baseline)"
    triv_key = "trivial (1+z)^2  [NO cluster physics; reference ceiling]"
    r_mono = results[mono_key]
    r_triv = results[triv_key]
    physics_forms = {kk: vv for kk, vv in results.items() if kk != triv_key and np.isfinite(vv)}
    best_phys = max(physics_forms, key=physics_forms.get)
    beat_mono = [
        kk for kk, vv in physics_forms.items() if kk != mono_key and np.isfinite(vv) and vv > r_mono
    ]
    print(f"\n    forms tested (trials): {n_forms}")
    print(f"    monopole r = {r_mono:.4f}   trivial (1+z)^2 r = {r_triv:.4f}")
    print(f"    best cluster-physics form: {best_phys}  (r={physics_forms[best_phys]:.4f})")
    print(f"    physics forms beating the monopole: {beat_mono if beat_mono else 'NONE'}")

    # [2] Permutation null: shuffle which (k_A,r_A) attaches to which (z,m). Tests whether
    #     the monopole's r is structural or reproducible by chance re-pairing.
    print("\n[2] Permutation null (shuffle (k_A,r_A) pairing), 1000 trials, quadrupole-shape form:")
    q_real, _ = r_of_phi((k * r) ** 2 / D**4, Hi, valid)
    n_perm = 1000
    q_null = np.empty(n_perm)
    for i in range(n_perm):
        perm = RNG.permutation(len(df))
        kr = k[perm] * r[perm]
        q_null[i], _ = r_of_phi(kr**2 / D**4, Hi, valid)
    q_null = q_null[np.isfinite(q_null)]
    exceed = int((q_null >= q_real).sum())
    print(f"    real quadrupole-shape r = {q_real:.4f}")
    print(
        f"    shuffled: mean r = {q_null.mean():.4f}  95th pctile = {np.percentile(q_null, 95):.4f}"
        f"  max = {q_null.max():.4f}"
    )
    print(
        f"    real exceeds {n_perm - exceed}/{n_perm} shuffles  (p = {(exceed + 1) / (n_perm + 1):.4f})"
    )

    # [3] Holdout: does the monopole rank #1 among cluster-physics forms in BOTH splits?
    print("\n[3] 70/30 holdout (seed=42): monopole rank among cluster-physics forms per split:")
    idx = np.arange(len(df))
    RNG42 = np.random.default_rng(42)
    RNG42.shuffle(idx)
    cut = int(0.7 * len(df))
    for split_name, sub in [("train(70%)", idx[:cut]), ("holdout(30%)", idx[cut:])]:
        zc, mc, kc, rc, Dc = z[sub], m[sub], k[sub], r[sub], D[sub]
        Hc, vc = hcc_interp(z_cc, H_cc, zc)
        libc = tracer_library(zc, mc, kc, rc, Dc)
        rr = {kk: r_of_phi(vv, Hc, vc)[0] for kk, vv in libc.items() if kk != triv_key}
        ranked = sorted(((v, kk) for kk, v in rr.items() if np.isfinite(v)), reverse=True)
        mono_rank = 1 + [kk for _, kk in ranked].index(mono_key)
        print(
            f"    {split_name}: monopole r={rr[mono_key]:.4f}  rank {mono_rank}/{len(ranked)}"
            f"  (top: {ranked[0][1]} r={ranked[0][0]:.4f})"
        )

    print("\n" + "=" * 74)
    print("READ-OUT (interpret in report; script only reports numbers):")
    print("  - If NO cluster-physics form beats the monopole -> monopole-dominance robust.")
    print("  - If trivial (1+z)^2 >= all cluster-physics forms -> the cluster apparatus")
    print("    (k_A, r_A incl. the quadrupole) adds nothing over trivial redshift scaling.")
    print("  - Permutation p<0.05 with real>shuffled means the pairing carries real (non-noise)")
    print("    information, yet still underperforms the monopole -> form-level, not noise.")
    print("=" * 74)


if __name__ == "__main__":
    main()
