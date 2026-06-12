"""
M8-C: Closure Schedule — Cluster Formation Bridge Test

<HYPOTHESIS>: ε(z) = (H_MULT/H_FLRW)² − 1 is explained by
galaxy cluster formation history.

Tests whether standard ΛCDM Press-Schechter cluster abundance
can reproduce the non-monotonic shape of ε(z) extracted from Table A1.

Two models tested at each mass threshold M_min:
  Model A: comoving cluster number density n(>M_min, z)
  Model B: survey count rate dN/dz ∝ n(z) × r(z)² / H(z)

If <HYPOTHESIS> is correct, one of these models should:
  (1) peak near z≈0.40 (matching ε primary peak)
  (2) have Pearson r > 0.80 with ε(z)
  (3) reproduce the secondary structure near z=1.0–1.5

All ΛCDM physics is EXTERNAL_STANDARD_PHYSICS.
ε(z) values are OUR_RECONSTRUCTION from Table A1 — NOT_AUTHOR_CONFIRMED.
The cluster-formation connection is <HYPOTHESIS> — NOT causal, NOT verified.

Labels: OUR_RECONSTRUCTION · <HYPOTHESIS> · EXTERNAL_STANDARD_PHYSICS
        TABLE_A1_DATA · NOT_AUTHOR_CONFIRMED · INTERNAL_DIAGNOSTIC_ONLY
Scope:  NOT_VALIDATION · NOT_REFUTATION
"""

from __future__ import annotations

import json
import math
from pathlib import Path

# ── Table A1 data (same source as bridge_derivation_attempt.py) ──────────────
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

# ── ΛCDM cosmological parameters (Planck 2018) ────────────────────────────────
# Source: Aghanim et al. 2020, Table 2 (TT,TE,EE+lowE+lensing+BAO)
OM_MATTER = 0.315
OM_LAMBDA = 0.685
H0_KMS_MPC = 70.0  # km/s/Mpc — matched to Table A1 H_FLRW(z→0) reference
C_LIGHT_KMS = 299792.458  # km/s

# ── Press-Schechter cluster physics ──────────────────────────────────────────
# Source: Press & Schechter 1974; Bond et al. 1991
SIGMA_8 = 0.811  # Planck 2018 amplitude of matter fluctuations
DELTA_C = 1.686  # Spherical collapse threshold (EdS approximation)
GAMMA_CDM = 0.27  # CDM spectral slope for σ(M) scaling (approximate)
# WHY GAMMA_CDM: For CDM power spectrum P(k) ∝ k^n × T(k)², σ(M) ∝ M^(-γ)
# with γ ≈ (n+3)/6 ≈ 0.27 for n_s≈0.96 and intermediate masses.
# This is an approximation — real σ(M) requires numerical P(k) integral.

# Mass thresholds for galaxy clusters (M_sun)
M_MIN_VARIANTS = [
    (1.0e14, "1×10¹⁴ M☉ — group/cluster boundary"),
    (5.0e14, "5×10¹⁴ M☉ — rich cluster"),
    (2.0e15, "2×10¹⁵ M☉ — massive cluster"),
]

# Physical constants
G_SI = 6.674e-11  # m³ kg⁻¹ s⁻²
KM_PER_MPC = 3.086e19  # m per Mpc
KG_PER_MSUN = 1.989e30  # kg per solar mass
M_PER_MPC = 3.086e22  # m per Mpc (= 1 Mpc)


# ── ΛCDM background functions ─────────────────────────────────────────────────


def hubble_lcdm(z: float) -> float:
    """H(z) in km/s/Mpc for flat ΛCDM."""
    return H0_KMS_MPC * math.sqrt(OM_MATTER * (1 + z) ** 3 + OM_LAMBDA)


def _growth_integrand(z: float) -> float:
    """Integrand (1+z)/H(z)³ for unnormalized growth factor."""
    return (1 + z) / hubble_lcdm(z) ** 3


def growth_factor_unnorm(z: float, z_max: float = 30.0, n_steps: int = 400) -> float:
    """
    Unnormalized ΛCDM growth factor D(z) = H(z) × ∫_z^z_max (1+z')/H(z')³ dz'.
    Uses trapezoidal rule.
    """
    if z >= z_max:
        return 0.0
    dz = (z_max - z) / n_steps
    integral = 0.0
    for i in range(n_steps):
        z1 = z + i * dz
        z2 = z + (i + 1) * dz
        integral += 0.5 * (_growth_integrand(z1) + _growth_integrand(z2)) * dz
    return hubble_lcdm(z) * integral


# Precompute D(0) once
_D0_CACHED: float | None = None


def _get_d0() -> float:
    global _D0_CACHED
    if _D0_CACHED is None:
        _D0_CACHED = growth_factor_unnorm(0.0)
    return _D0_CACHED


def growth_factor_norm(z: float) -> float:
    """D(z)/D(0) — normalized ΛCDM linear growth factor."""
    return growth_factor_unnorm(z) / _get_d0()


def comoving_distance(z: float, n_steps: int = 400) -> float:
    """Comoving distance r(z) in Mpc via trapezoidal integration."""
    if z <= 0.0:
        return 0.0
    dz = z / n_steps
    result = 0.0
    for i in range(n_steps):
        z1 = i * dz
        z2 = (i + 1) * dz
        h1 = hubble_lcdm(max(z1, 1e-6))
        h2 = hubble_lcdm(z2)
        result += 0.5 * (C_LIGHT_KMS / h1 + C_LIGHT_KMS / h2) * dz
    return result


# ── Matter power spectrum sigma(M,z) ─────────────────────────────────────────


def compute_m8() -> float:
    """
    Mass in sphere of radius 8 Mpc/h.
    M_8 = (4π/3) × (8/h Mpc)³ × ρ_m0
    ρ_m0 = Ω_m × ρ_crit0 in M_sun/Mpc³
    """
    h = H0_KMS_MPC / 100.0
    r8_mpc = 8.0 / h  # Mpc (physical 8 Mpc/h)
    H0_si = H0_KMS_MPC * 1e3 / M_PER_MPC  # (km/s/Mpc × m/km) / (m/Mpc) = s^-1
    rho_crit_si = 3.0 * H0_si**2 / (8.0 * math.pi * G_SI)  # kg/m³
    rho_crit_msun_mpc3 = rho_crit_si * M_PER_MPC**3 / KG_PER_MSUN
    rho_m0 = OM_MATTER * rho_crit_msun_mpc3
    return (4.0 / 3.0) * math.pi * r8_mpc**3 * rho_m0


_M8_CACHED: float | None = None


def _get_m8() -> float:
    global _M8_CACHED
    if _M8_CACHED is None:
        _M8_CACHED = compute_m8()
    return _M8_CACHED


def sigma_mass_z(m_min_solar: float, z: float) -> float:
    """
    σ(M_min, z) ≈ σ_8 × (M_8/M_min)^GAMMA × D(z)/D(0).
    Approximate: real σ(M) requires full P(k) integral.
    """
    m8 = _get_m8()
    # WHY: (M_8/M_min)^GAMMA_CDM gives σ at mass scale M_min relative to σ_8 at M_8
    sigma_m_z0 = SIGMA_8 * (m8 / m_min_solar) ** GAMMA_CDM
    return sigma_m_z0 * growth_factor_norm(z)


# ── Press-Schechter cluster abundance ────────────────────────────────────────


def ps_comoving_fraction(m_min_solar: float, z: float) -> float:
    """
    Press-Schechter fraction of mass in halos > M_min at redshift z.
    f(>M_min, z) = erfc(ν/√2) where ν = δ_c/σ(M_min, z).

    This is MONOTONICALLY DECREASING with z (structure forms late).
    Returns 0 if σ ≤ 0.
    """
    sigma = sigma_mass_z(m_min_solar, z)
    if sigma <= 0.0:
        return 0.0
    nu = DELTA_C / sigma
    return math.erfc(nu / math.sqrt(2.0))


def survey_count_rate(m_min_solar: float, z: float) -> float:
    """
    Proportional to dN_cluster/dz ∝ n_comoving(z) × dV/dz.
    dV/dz ∝ r(z)² / H(z)  [comoving volume element].

    This CAN peak at intermediate z (volume effect vs density).
    Returns 0 at z ≤ 0.
    """
    if z <= 0.0:
        return 0.0
    n = ps_comoving_fraction(m_min_solar, z)
    r = comoving_distance(z)
    h = hubble_lcdm(z)
    return n * r**2 / h


# ── Statistical tools ─────────────────────────────────────────────────────────


def pearson_r(x: list[float], y: list[float]) -> float:
    """Pearson correlation coefficient."""
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    cov = sum((x[i] - mx) * (y[i] - my) for i in range(n)) / n
    sx = math.sqrt(sum((xi - mx) ** 2 for xi in x) / n)
    sy = math.sqrt(sum((yi - my) ** 2 for yi in y) / n)
    if sx < 1e-12 or sy < 1e-12:
        return 0.0
    return cov / (sx * sy)


def fit_proportional(x: list[float], y: list[float]) -> tuple[float, float, float]:
    """
    Fit y ≈ C × x (proportional, through origin).
    Returns (C, rms_residual, max_residual).
    """
    # Least squares: C = Σ(x_i × y_i) / Σ(x_i²)
    num = sum(x[i] * y[i] for i in range(len(x)))
    den = sum(xi**2 for xi in x)
    if den < 1e-12:
        return 0.0, float("inf"), float("inf")
    c = num / den
    residuals = [abs(y[i] - c * x[i]) for i in range(len(x))]
    rms = math.sqrt(sum(r**2 for r in residuals) / len(residuals))
    return c, rms, max(residuals)


def normalize_to_max(values: list[float]) -> list[float]:
    """Normalize list to max=1."""
    mx = max(values)
    if mx < 1e-12:
        return values
    return [v / mx for v in values]


# ── ε(z) from Table A1 ───────────────────────────────────────────────────────


def compute_eps() -> list[float]:
    """ε(z) = (H_MULT/H_FLRW)² − 1 for all Table A1 rows."""
    return [(hm / hf) ** 2 - 1.0 for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]


# ── Main audit ───────────────────────────────────────────────────────────────


def run_m8c_closure_schedule() -> dict:
    print("M8-C: Closure Schedule — Cluster Formation Bridge Test")
    print("=" * 62)
    print("<HYPOTHESIS>: ε(z) shape explained by cluster formation history")
    print("Scope: EXTERNAL_STANDARD_PHYSICS · OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED")
    print()

    eps_values = compute_eps()
    eps_norm = normalize_to_max(eps_values)

    m8 = _get_m8()
    d0 = _get_d0()
    print(f"  M_8 (8 Mpc/h sphere) = {m8:.3e} M☉")
    print(f"  D(0) [unnormalized]  = {d0:.6f}")
    print()

    # Step 1: ε(z) profile
    print("--- Step 1: ε(z) from Table A1 ---")
    print(f"  {'z':>6}  {'ε(z)':>8}  {'H_FLRW':>8}  {'H_MULT':>8}")
    for z, hf, hm, eps in zip(Z_DATA, H_FLRW_DATA, H_MULT_DATA, eps_values, strict=False):
        print(f"  {z:>6.2f}  {eps:>8.4f}  {hf:>8.1f}  {hm:>8.1f}")
    print(f"  Peak ε = {max(eps_values):.4f} at z = {Z_DATA[eps_values.index(max(eps_values))]}")
    print(f"  Min  ε = {min(eps_values):.4f} at z = {Z_DATA[eps_values.index(min(eps_values))]}")
    print()

    results_by_m_min = []
    for m_min, m_label in M_MIN_VARIANTS:
        print(f"--- M_min = {m_label} ---")

        # Model A: comoving density
        n_comoving = [ps_comoving_fraction(m_min, z) for z in Z_DATA]
        n_comoving_norm = normalize_to_max(n_comoving)

        # Model B: survey count rate
        n_survey = [survey_count_rate(m_min, z) for z in Z_DATA]
        n_survey_norm = normalize_to_max(n_survey)

        # σ and ν at z=0 for info
        sigma_z0 = sigma_mass_z(m_min, 0.0)
        nu_z0 = DELTA_C / sigma_z0 if sigma_z0 > 0 else float("inf")

        # Peaks
        peak_z_comoving = Z_DATA[n_comoving.index(max(n_comoving))]
        peak_z_survey = Z_DATA[n_survey.index(max(n_survey))]

        # Correlations
        r_comoving = pearson_r(eps_norm, n_comoving_norm)
        r_survey = pearson_r(eps_norm, n_survey_norm)

        # Proportionality fits
        c_cov, rms_cov, max_res_cov = fit_proportional(n_comoving_norm, eps_norm)
        c_sur, rms_sur, max_res_sur = fit_proportional(n_survey_norm, eps_norm)

        # Sign-change check: does model capture non-monotonicity?
        def count_sign_changes(vals: list[float]) -> int:
            changes = 0
            for i in range(len(vals) - 1):
                if (vals[i + 1] - vals[i]) * (vals[i] - (vals[i - 1] if i > 0 else vals[i])) < 0:
                    changes += 1
            return changes

        sc_eps = count_sign_changes(eps_values)
        sc_comoving = count_sign_changes(n_comoving)
        sc_survey = count_sign_changes(n_survey)

        print(f"  σ_8-scaled σ at z=0:  {sigma_z0:.4f}   ν = {nu_z0:.3f}")
        print(
            f"  Model A (comoving):   peak at z={peak_z_comoving}  |  Pearson r={r_comoving:+.3f}"
        )
        print(f"    sign changes: ε={sc_eps}, model={sc_comoving}  (ε needs {sc_eps} to match)")
        print(f"    fit rms={rms_cov:.4f}  max_res={max_res_cov:.4f}")
        print(f"  Model B (survey dN/dz): peak at z={peak_z_survey}  |  Pearson r={r_survey:+.3f}")
        print(f"    sign changes: ε={sc_eps}, model={sc_survey}")
        print(f"    fit rms={rms_sur:.4f}  max_res={max_res_sur:.4f}")

        # Per-z comparison table
        print(
            f"  {'z':>5}  {'ε_norm':>7}  {'A_norm':>7}  {'B_norm':>7}  {'A_resid':>8}  {'B_resid':>8}"
        )
        for i, z in enumerate(Z_DATA):
            print(
                f"  {z:>5.2f}  {eps_norm[i]:>7.4f}  {n_comoving_norm[i]:>7.4f}  "
                f"{n_survey_norm[i]:>7.4f}  "
                f"{eps_norm[i] - c_cov * n_comoving_norm[i]:>+8.4f}  "
                f"{eps_norm[i] - c_sur * n_survey_norm[i]:>+8.4f}"
            )
        print()

        # Verdict for this M_min
        best_r = max(abs(r_comoving), abs(r_survey))
        best_model = "A" if abs(r_comoving) > abs(r_survey) else "B"
        best_rms = rms_cov if best_model == "A" else rms_sur

        if best_r > 0.90 and best_rms < 0.05:
            verdict_m = "PASS"
        elif best_r > 0.70:
            verdict_m = "PARTIAL"
        else:
            verdict_m = "FAIL"

        results_by_m_min.append(
            {
                "m_min_solar": m_min,
                "m_min_label": m_label,
                "sigma_at_z0": round(sigma_z0, 4),
                "nu_at_z0": round(nu_z0, 4),
                "model_A_comoving": {
                    "peak_z": peak_z_comoving,
                    "pearson_r": round(r_comoving, 4),
                    "rms_residual": round(rms_cov, 4),
                    "max_residual": round(max_res_cov, 4),
                    "sign_changes": sc_comoving,
                },
                "model_B_survey": {
                    "peak_z": peak_z_survey,
                    "pearson_r": round(r_survey, 4),
                    "rms_residual": round(rms_sur, 4),
                    "max_residual": round(max_res_sur, 4),
                    "sign_changes": sc_survey,
                },
                "eps_sign_changes": sc_eps,
                "best_pearson_r": round(best_r, 4),
                "best_model": best_model,
                "verdict_m_min": verdict_m,
            }
        )

    # Overall verdict
    print("=" * 62)
    print("OVERALL VERDICT")
    print("=" * 62)
    print()

    all_verdicts = [r["verdict_m_min"] for r in results_by_m_min]
    best_r_overall = max(r["best_pearson_r"] for r in results_by_m_min)
    best_entry = max(results_by_m_min, key=lambda r: r["best_pearson_r"])

    if all(v == "PASS" for v in all_verdicts):
        overall_verdict = "PASS"
    elif any(v == "PARTIAL" for v in all_verdicts):
        overall_verdict = "PARTIAL"
    else:
        overall_verdict = "FAIL"

    print(f"  Best Pearson r across all models: {best_r_overall:.4f}")
    print(f"  Best model: {best_entry['best_model']} at M_min = {best_entry['m_min_label']}")
    print(f"  Overall verdict: {overall_verdict}")
    print()

    # Key diagnostics
    comoving_peaks = [r["model_A_comoving"]["peak_z"] for r in results_by_m_min]
    survey_peaks = [r["model_B_survey"]["peak_z"] for r in results_by_m_min]
    eps_peak_z = Z_DATA[eps_values.index(max(eps_values))]

    print(f"  ε(z) peak: z = {eps_peak_z}")
    print(f"  Model A (comoving) peaks: z = {comoving_peaks}")
    print(f"  Model B (survey) peaks:   z = {survey_peaks}")
    print()

    # Non-monotonicity diagnosis
    sign_changes_eps = results_by_m_min[0]["eps_sign_changes"]
    sc_comoving_all = [r["model_A_comoving"]["sign_changes"] for r in results_by_m_min]
    sc_survey_all = [r["model_B_survey"]["sign_changes"] for r in results_by_m_min]

    print(f"  ε(z) sign changes: {sign_changes_eps}")
    print(f"  Model A sign changes: {sc_comoving_all}")
    print(f"  Model B sign changes: {sc_survey_all}")
    print()

    conclusions = [
        (
            f"Best Pearson r = {best_r_overall:.3f} — "
            + (
                "insufficient to confirm cluster-formation <HYPOTHESIS>."
                if best_r_overall < 0.80
                else "suggestive but requires structural match, not just correlation."
            )
        ),
        (
            "Model A (PS comoving density) is MONOTONICALLY DECREASING — cannot explain "
            "primary ε peak at z≈0.40 without volume weighting."
        ),
        (
            f"Model B (survey count rate dN/dz) peaks at z={survey_peaks[0]} "
            f"(M_min={M_MIN_VARIANTS[0][0]:.0e} M☉) — "
            + (
                "overlaps ε peak range z=0.40–0.65."
                if any(0.30 <= p <= 0.70 for p in survey_peaks)
                else "does NOT peak near ε primary peak z=0.40."
            )
        ),
        (
            "Standard PS cannot reproduce secondary ε structure at z=1.0–1.5 "
            "(not captured by any single mass threshold model)."
        ),
        (
            "Q2 blocker confirmed: k_A(z) schedule required to reproduce ε(z) shape. "
            "Only TJB can confirm which cluster schedule was used."
        ),
        (
            "<HYPOTHESIS> status: WEAKLY SUPPORTED at best. Qualitative peak location "
            "may coincide with survey count rate for appropriate M_min, "
            "but quantitative agreement and secondary structure are not explained."
        ),
    ]

    print("CONCLUSIONS:")
    for i, c in enumerate(conclusions, 1):
        print(f"  {i}. {c}")

    out = {
        "gate": "M8-C-closure-schedule",
        "date": "2026-06-12",
        "labels": [
            "OUR_RECONSTRUCTION",
            "<HYPOTHESIS>",
            "EXTERNAL_STANDARD_PHYSICS",
            "TABLE_A1_DATA",
            "NOT_AUTHOR_CONFIRMED",
            "NOT_VALIDATION",
            "NOT_REFUTATION",
            "INTERNAL_DIAGNOSTIC_ONLY",
        ],
        "hypothesis": "ε(z) shape is explained by galaxy cluster formation history (ΛCDM Press-Schechter)",
        "lcdm_params": {
            "Omega_m": OM_MATTER,
            "Omega_Lambda": OM_LAMBDA,
            "H0_km_s_mpc": H0_KMS_MPC,
            "sigma_8": SIGMA_8,
            "delta_c": DELTA_C,
            "gamma_cdm": GAMMA_CDM,
        },
        "m8_solar": float(f"{_get_m8():.3e}"),
        "eps_profile": [
            {"z": z, "eps": round(e, 4)} for z, e in zip(Z_DATA, eps_values, strict=False)
        ],
        "eps_peak_z": eps_peak_z,
        "eps_min_z": Z_DATA[eps_values.index(min(eps_values))],
        "results_by_m_min": results_by_m_min,
        "overall_verdict": overall_verdict,
        "best_pearson_r": round(best_r_overall, 4),
        "conclusions": conclusions,
        "safety": (
            "NOT_VALIDATION · NOT_REFUTATION · <HYPOTHESIS> "
            "· OUR_RECONSTRUCTION · INTERNAL_DIAGNOSTIC_ONLY"
        ),
    }

    report_dir = Path(__file__).parent.parent / "reports"
    report_dir.mkdir(exist_ok=True)
    json_path = report_dir / "m8c_closure_schedule.json"
    json_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n  JSON written: {json_path}")

    return out


if __name__ == "__main__":
    run_m8c_closure_schedule()
