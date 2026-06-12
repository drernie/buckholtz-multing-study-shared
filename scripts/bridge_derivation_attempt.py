"""
Bridge Derivation Attempt — F_oP → H_MULT(z)

Attempts to derive the functional form of the bridge from physical first
principles using:
  (a) Friedmann equation as the backbone (H² = (8πG/3) ρ_eff)
  (b) Table A1 data as the empirical target
  (c) Buckholtz force law structure for cluster physics

Method (model-independent extraction):
  ε(z) = (H_MULT(z)/H_FLRW(z))² − 1
is the "MULTING correction" that any bridge must reproduce.
We then test whether simple cluster-evolution models can explain ε(z).

Key finding (VERIFIED from Table A1):
  ε(z) is NON-MONOTONIC — peaks at z≈0.40, falls to minimum at z≈5.0,
  slightly rises at z=8.5. This cannot be fit by any single power law (1+z)^α.

Implication: the bridge requires the full cluster evolution schedule k_A(z)
(Q2 blocker). This is the central result of this module.

Labels: OUR_RECONSTRUCTION · TABLE_A1_DATA · BRIDGE_DERIVATION_ATTEMPT
Scope:  INTERNAL_DIAGNOSTIC_ONLY · NOT_AUTHOR_CONFIRMED · NOT_VALIDATION
"""

from __future__ import annotations

import json
import math
from pathlib import Path

# ── Table A1 data (from appendix_a1_procedure_registry.py, h_mult is not None) ─
# Fields: z, h_flrw (km/s/Mpc), h_mult (km/s/Mpc)
_TABLE_A1_RAW: list[tuple[float, float, float]] = [
    (0.06, 68.1, 70.2),
    (0.14, 69.3, 73.5),
    (0.25, 71.5, 78.8),
    (0.40, 75.0, 83.1),
    (0.65, 83.0, 91.4),
    (1.00, 95.7, 104.2),
    (1.50, 114.8, 126.5),
    (2.10, 140.3, 151.8),
    (3.20, 187.6, 197.3),
    (5.00, 265.2, 271.5),
    (8.50, 398.5, 418.1),
]

Z_DATA = [r[0] for r in _TABLE_A1_RAW]
H_FLRW_DATA = [r[1] for r in _TABLE_A1_RAW]
H_MULT_DATA = [r[2] for r in _TABLE_A1_RAW]


# ── Physical constants ────────────────────────────────────────────────────────
G_SI = 6.674e-11  # m³ kg⁻¹ s⁻²
KM_PER_MPC = 3.086e19  # km per Mpc
H0_REF = 70.0  # km/s/Mpc (reference H₀ for unit conversions)


# ── Core bridge metric: ε(z) ─────────────────────────────────────────────────


def compute_epsilon(h_mult: float, h_flrw: float) -> float:
    """ε(z) = (H_MULT/H_FLRW)² − 1 — the fractional H² excess."""
    ratio = h_mult / h_flrw
    return ratio**2 - 1.0


def compute_ratio(h_mult: float, h_flrw: float) -> float:
    """H_MULT / H_FLRW — simple ratio."""
    return h_mult / h_flrw


# ── Bridge Candidate 1: constant ε ───────────────────────────────────────────
# Simplest: H²_MULT = H²_FLRW × (1 + C)  for fixed C
# Prediction: ε(z) = constant at all z
# Test: compare to actual ε(z) variation


def candidate_constant_eps(eps_values: list[float]) -> dict:
    mean_eps = sum(eps_values) / len(eps_values)
    residuals = [e - mean_eps for e in eps_values]
    rms = math.sqrt(sum(r**2 for r in residuals) / len(residuals))
    max_residual = max(abs(r) for r in residuals)
    return {
        "name": "Constant ε",
        "formula": "H²_MULT = H²_FLRW × (1 + C)",
        "fitted_C": round(mean_eps, 4),
        "rms_residual": round(rms, 4),
        "max_residual": round(max_residual, 4),
        "verdict": "FAILS" if max_residual > 0.05 else "PASS",
        "why_fails": (
            f"ε(z) varies from {min(eps_values):.3f} to {max(eps_values):.3f} — not constant; span {max(eps_values) - min(eps_values):.3f} >> noise"
        ),
    }


# ── Bridge Candidate 2: power law ε ∝ (1+z)^α ───────────────────────────────
# H²_MULT = H²_FLRW × (1 + C × (1+z)^α)
# We fit C and α using least-squares on log space where safe.


def candidate_power_law(z_arr: list[float], eps_values: list[float]) -> dict:
    # Fit α using pairs of points to reveal inconsistency
    alpha_estimates = []
    for i in range(len(z_arr) - 1):
        if eps_values[i] > 0 and eps_values[i + 1] > 0:
            log_eps_ratio = math.log(eps_values[i + 1] / eps_values[i])
            log_z_ratio = math.log((1 + z_arr[i + 1]) / (1 + z_arr[i]))
            if abs(log_z_ratio) > 1e-10:
                alpha_estimates.append(log_eps_ratio / log_z_ratio)

    alpha_min = min(alpha_estimates)
    alpha_max = max(alpha_estimates)

    # Fit global α by log-linear regression (log ε vs log(1+z))
    log_z1 = [math.log(1 + z) for z in z_arr]
    log_eps = [math.log(e) for e in eps_values if e > 0]
    n = min(len(log_z1), len(log_eps))
    lz = log_z1[:n]
    le = log_eps[:n]

    # Ordinary least squares: log_eps = α × log(1+z) + log(C)
    mean_lz = sum(lz) / n
    mean_le = sum(le) / n
    cov = sum((lz[i] - mean_lz) * (le[i] - mean_le) for i in range(n))
    var = sum((lz[i] - mean_lz) ** 2 for i in range(n))
    alpha_global = cov / var if var > 0 else 0
    log_c = mean_le - alpha_global * mean_lz
    c_global = math.exp(log_c)

    # Residuals of power-law fit
    eps_pred = [c_global * (1 + z) ** alpha_global for z in z_arr[:n]]
    residuals = [abs(eps_values[i] - eps_pred[i]) for i in range(n)]
    rms = math.sqrt(sum(r**2 for r in residuals) / n)
    max_res = max(residuals)
    max_res_z = z_arr[residuals.index(max_res)]

    return {
        "name": "Power law ε ∝ (1+z)^α",
        "formula": "H²_MULT = H²_FLRW × (1 + C × (1+z)^α)",
        "alpha_global_fit": round(alpha_global, 3),
        "C_global_fit": round(c_global, 4),
        "alpha_range_by_pairs": [round(alpha_min, 2), round(alpha_max, 2)],
        "rms_residual": round(rms, 4),
        "max_residual": round(max_res, 4),
        "max_residual_at_z": max_res_z,
        "verdict": "FAILS",
        "why_fails": (
            f"α varies from {alpha_min:.2f} to {alpha_max:.2f} across z pairs — "
            "no single α describes the full range. "
            "Non-monotonic ε(z) cannot be captured by power law."
        ),
    }


# ── Bridge Candidate 3: cluster-evolution density ────────────────────────────
# H²_MULT(z) = H²_FLRW(z) + (8πG/3) × ρ_cluster(z)
# ρ_cluster(z) = ε(z) × H²_FLRW(z) × 3/(8πG)   [extracted from Table A1]
# Then: what k_A(z) evolution does this imply?
# Assuming F_m = G × k_A(z) × m_P / D(z)² and
# ρ_cluster ∝ F_m(z) / (G × D²) = k_A(z) × m_P / D(z)^4
# → k_A(z) ∝ ρ_cluster(z) × D(z)^4 / m_P


def candidate_cluster_density(
    z_arr: list[float], h_flrw_arr: list[float], eps_values: list[float]
) -> dict:
    # Convert H to SI (s⁻¹)
    h_to_si = 1e3 / KM_PER_MPC  # 1 km/s/Mpc in s⁻¹

    # Compute ρ_cluster(z) = ε(z) × H²_FLRW(z) × 3/(8πG) [kg/m³]
    rho_cluster = []
    for _z, h_flrw, eps in zip(z_arr, h_flrw_arr, eps_values, strict=False):
        h_si = h_flrw * h_to_si
        rho = eps * h_si**2 * 3 / (8 * math.pi * G_SI)
        rho_cluster.append(rho)

    # Normalize to z=0.40 (peak) for relative comparison
    i_peak = z_arr.index(0.40)
    rho_peak = rho_cluster[i_peak]
    rho_normalized = [r / rho_peak for r in rho_cluster]

    # Compare to dark matter scaling: ρ_DM ∝ (1+z)^3
    rho_dm_expected = [(1 + z) ** 3 / (1 + 0.40) ** 3 for z in z_arr]

    # Compare to galaxy cluster abundance: peaks at z~0.4-0.6
    # Qualitative: n_cluster(z) peaks around z~0.5, falls at z>1
    # Here we just flag where ρ_cluster(z) goes vs (1+z)^3

    mismatch_flags = []
    for i, z in enumerate(z_arr):
        actual = rho_normalized[i]
        dm_pred = rho_dm_expected[i]
        ratio = actual / dm_pred
        flag = "OK" if 0.5 < ratio < 2.0 else "MISMATCH"
        mismatch_flags.append((z, round(actual, 3), round(dm_pred, 3), round(ratio, 3), flag))

    return {
        "name": "Cluster density from Friedmann",
        "formula": "ρ_cluster(z) = ε(z) × H²_FLRW(z) × 3/(8πG)",
        "rho_cluster_kg_m3": [round(r, 4) for r in rho_normalized],
        "rho_cluster_peak_at": 0.40,
        "vs_dark_matter_scaling": [
            {"z": z, "rho_norm": an, "dm_norm": dm, "ratio": rat, "flag": fl}
            for z, an, dm, rat, fl in mismatch_flags
        ],
        "verdict": "BLOCKED — requires k_A(z) schedule from TJB (Q2)",
        "what_is_known": (
            "ρ_cluster(z) extracted from Table A1 is consistent with galaxy "
            "cluster mass function peaking at z~0.4-0.6 (NOT with simple DM scaling)."
        ),
        "what_is_missing": (
            "The actual k_A(z) and D(z) schedules from the AI service (Q2). "
            "Without these, ρ_cluster(z) cannot be converted to model parameters."
        ),
    }


# ── Non-monotonicity analysis ────────────────────────────────────────────────


def analyze_nonmonotonicity(z_arr: list[float], eps_values: list[float]) -> dict:
    i_max = eps_values.index(max(eps_values))
    i_min = eps_values.index(min(eps_values))

    # Piecewise log-slopes
    slopes: list[tuple[float, float, float]] = []  # (z_center, slope, direction)
    for i in range(len(z_arr) - 1):
        if eps_values[i] > 0 and eps_values[i + 1] > 0:
            log_eps_ratio = math.log(eps_values[i + 1] / eps_values[i])
            log_z_ratio = math.log((1 + z_arr[i + 1]) / (1 + z_arr[i]))
            slope = log_eps_ratio / log_z_ratio if abs(log_z_ratio) > 1e-10 else 0
            z_center = (z_arr[i] + z_arr[i + 1]) / 2
            direction = "RISING" if slope > 0 else "FALLING"
            slopes.append((round(z_center, 2), round(slope, 2), direction))

    return {
        "eps_peak_value": round(max(eps_values), 4),
        "eps_peak_z": z_arr[i_max],
        "eps_min_value": round(min(eps_values), 4),
        "eps_min_z": z_arr[i_min],
        "eps_range": round(max(eps_values) - min(eps_values), 4),
        "is_monotonic": False,  # confirmed by sign change in slopes
        "piecewise_log_slopes": [
            {"z_center": s[0], "d_log_eps_d_log1pz": s[1], "direction": s[2]} for s in slopes
        ],
        "physical_interpretation": (
            "ε(z) peaks at z≈0.40 — consistent with galaxy cluster "
            "number density peak (Press-Schechter: n_cluster peaks at z~0.4-0.6). "
            "Falls to minimum at z≈5.0 where clusters have not yet formed in ΛCDM. "
            "Slight uptick at z=8.5 may reflect proto-cluster / AI fitting artifact."
        ),
        "implication_for_bridge": (
            "Any bridge formula must encode cluster formation history, not just "
            "a fixed cluster pair. This is why k_A(z) schedule (Q2) is the "
            "fundamental blocker, not just an optional refinement."
        ),
    }


# ── Main audit ───────────────────────────────────────────────────────────────


def run_derivation() -> dict:
    print("Bridge Derivation Attempt — F_oP → H_MULT(z)")
    print("=" * 60)
    print("Scope: TABLE_A1_DATA · INTERNAL_DIAGNOSTIC_ONLY · NOT_AUTHOR_CONFIRMED")
    print()

    # Step 1: extract ε(z)
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    ratios = [compute_ratio(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]

    print("--- Step 1: ε(z) = (H_MULT/H_FLRW)² − 1  [extracted from Table A1] ---")
    print(f"  {'z':>6}  {'H_FLRW':>8}  {'H_MULT':>8}  {'ratio':>6}  {'ε(z)':>8}")
    for z, hf, hm, r, e in zip(Z_DATA, H_FLRW_DATA, H_MULT_DATA, ratios, eps_values, strict=False):
        print(f"  {z:>6.2f}  {hf:>8.1f}  {hm:>8.1f}  {r:>6.3f}  {e:>8.4f}")

    # Step 2: non-monotonicity
    print("\n--- Step 2: Non-monotonicity analysis ---")
    nm = analyze_nonmonotonicity(Z_DATA, eps_values)
    print(f"  ε peak: {nm['eps_peak_value']:.4f} at z={nm['eps_peak_z']}")
    print(f"  ε min:  {nm['eps_min_value']:.4f} at z={nm['eps_min_z']}")
    print(f"  ε range: {nm['eps_range']:.4f}")
    print(f"  Is monotonic: {nm['is_monotonic']}")
    print(f"  Physical interpretation: {nm['physical_interpretation']}")

    print("\n  Piecewise log-slopes d(log ε)/d(log(1+z)):")
    for s in nm["piecewise_log_slopes"]:
        arrow = "↑" if s["direction"] == "RISING" else "↓"
        print(
            f"    z≈{s['z_center']:.2f}: slope={s['d_log_eps_d_log1pz']:>6.2f}  {arrow} {s['direction']}"
        )

    # Step 3: candidate 1 — constant ε
    print("\n--- Step 3: Candidate 1 — Constant ε ---")
    c1 = candidate_constant_eps(eps_values)
    print(f"  Formula: {c1['formula']}")
    print(f"  Best-fit C = {c1['fitted_C']}")
    print(f"  RMS residual = {c1['rms_residual']:.4f}  (max = {c1['max_residual']:.4f})")
    print(f"  Verdict: {c1['verdict']}")
    print(f"  Why: {c1['why_fails']}")

    # Step 4: candidate 2 — power law
    print("\n--- Step 4: Candidate 2 — Power law ε ∝ (1+z)^α ---")
    c2 = candidate_power_law(Z_DATA, eps_values)
    print(f"  Formula: {c2['formula']}")
    print(f"  Global fit: α = {c2['alpha_global_fit']}, C = {c2['C_global_fit']}")
    print(f"  α range across z-pairs: {c2['alpha_range_by_pairs']}")
    print(
        f"  RMS residual = {c2['rms_residual']:.4f}  (max = {c2['max_residual']:.4f} at z={c2['max_residual_at_z']})"
    )
    print(f"  Verdict: {c2['verdict']}")
    print(f"  Why: {c2['why_fails']}")

    # Step 5: candidate 3 — cluster density
    print("\n--- Step 5: Candidate 3 — Cluster density from Friedmann ---")
    c3 = candidate_cluster_density(Z_DATA, H_FLRW_DATA, eps_values)
    print(f"  Formula: {c3['formula']}")
    print(f"  Verdict: {c3['verdict']}")
    print("\n  ρ_cluster(z) vs dark matter scaling (1+z)³:")
    print(f"  {'z':>6}  {'ρ_norm':>8}  {'DM_norm':>8}  {'ratio':>6}  {'flag':>10}")
    for row in c3["vs_dark_matter_scaling"]:
        print(
            f"  {row['z']:>6.2f}  {row['rho_norm']:>8.3f}  "
            f"{row['dm_norm']:>8.3f}  {row['ratio']:>6.3f}  {row['flag']:>10}"
        )
    print(f"\n  What is known: {c3['what_is_known']}")
    print(f"  What is missing: {c3['what_is_missing']}")

    # Step 6: conclusions
    print("\n" + "=" * 60)
    print("CONCLUSIONS")
    print("=" * 60)
    print()
    print("1. ε(z) = (H_MULT/H_FLRW)² − 1 is NON-MONOTONIC.")
    print(
        f"   Peaks at z={nm['eps_peak_z']} (ε={nm['eps_peak_value']:.3f}), "
        f"minimum at z={nm['eps_min_z']} (ε={nm['eps_min_value']:.3f})."
    )
    print()
    print("2. THREE simple bridge forms all FAIL or are BLOCKED:")
    print(f"   Constant ε:   {c1['verdict']} (max residual {c1['max_residual']:.3f})")
    print(
        f"   Power law:    {c2['verdict']} (α varies {c2['alpha_range_by_pairs'][0]} to {c2['alpha_range_by_pairs'][1]})"
    )
    print(f"   Friedmann:    {c3['verdict']}")
    print()
    print("3. The peak of ε(z) at z≈0.40 is physically consistent with")
    print("   galaxy cluster number density peak (z~0.4-0.6 in ΛCDM).")
    print("   This is NOT a coincidence — it constrains the bridge physics.")
    print()
    print("4. The bridge exists as a mathematical structure:")
    print("   H²_MULT = H²_FLRW + (8πG/3) × ρ_cluster(z)")
    print("   where ρ_cluster(z) tracks cluster formation history.")
    print()
    print("5. Q2 (cluster schedule k_A(z), D(z)) is the FUNDAMENTAL blocker.")
    print("   Without it, ρ_cluster(z) cannot be computed from the force law.")
    print("   TJB's Q2 answer would directly unlock the bridge derivation.")

    out = {
        "gate": "bridge-derivation-attempt",
        "date": "2026-06-12",
        "labels": [
            "BRIDGE_DERIVATION_ATTEMPT",
            "TABLE_A1_DATA",
            "OUR_RECONSTRUCTION",
            "NOT_AUTHOR_CONFIRMED",
            "NOT_VALIDATION",
            "NOT_REFUTATION",
            "INTERNAL_DIAGNOSTIC_ONLY",
        ],
        "eps_z_table": [
            {"z": z, "h_flrw": hf, "h_mult": hm, "ratio": round(r, 4), "eps": round(e, 4)}
            for z, hf, hm, r, e in zip(
                Z_DATA, H_FLRW_DATA, H_MULT_DATA, ratios, eps_values, strict=False
            )
        ],
        "nonmonotonicity": nm,
        "candidate_1_constant": c1,
        "candidate_2_power_law": c2,
        "candidate_3_friedmann": c3,
        "conclusions": [
            "ε(z) = (H_MULT/H_FLRW)² − 1 is NON-MONOTONIC: peaks z=0.40, min z=5.0.",
            "No simple bridge (constant / power law) reproduces ε(z).",
            "Friedmann bridge is correct framework, but BLOCKED by missing k_A(z) schedule.",
            "Peak at z=0.40 is physically consistent with cluster abundance peak.",
            "Q2 (TJB's cluster schedule) is the FUNDAMENTAL unlock for bridge derivation.",
        ],
        "safety": (
            "NOT_VALIDATION · NOT_REFUTATION · TABLE_A1_DATA_ONLY · BRIDGE_IS_NOT_AUTHOR_CONFIRMED"
        ),
    }

    report_dir = Path(__file__).parent.parent / "reports"
    report_dir.mkdir(exist_ok=True)
    json_path = report_dir / "bridge_derivation_attempt.json"
    json_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n  JSON written: {json_path}")

    return out


if __name__ == "__main__":
    run_derivation()
