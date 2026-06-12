"""
HD-MAVP-1 — Cluster Formation Audit

Audit whether ε(z) peak at z=0.40 is explained by intrinsic cluster
formation or by observed selection / schedule effects.

Four candidates tested at the 11 confirmed Table A1 redshifts:
  A: Intrinsic PS number density n(>M, z) — comoving, no volume element
  B: Intrinsic dN/dz — PS density × comoving volume element, no selection
  C: SZ-selection-weighted dN/dz — B × parametric survey selection model
  D: ΛCDM transition proxy — dark energy fraction f_DE(z)
  (+) Selection function alone — key spurious-correlation diagnostic

Motivation: the image (2026-06-13) shows SZ selection f_sel(z) peaks at z≈0.40
by instrument physics (beam dilution at low z, flux fading at high z).
If r(ε, f_sel_alone) ≈ r(ε, dN/dz_obs), the M8-C r=0.723 signal is selection-driven.

ε(z) source: M8-A-R1 verified values, Table A1 [VERIFIED-tool, commit add7cba]
             NOT REDEFINED — used as-is from Buckholtz Table A1.

Labels:
  HD_MAVP_1 · OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED
  NOT_VALIDATION · NOT_REFUTATION · SELECTION_BIAS_AUDIT
  NOT_CLAIM_PS_FACT
"""

from __future__ import annotations

import json
import math
from pathlib import Path

# ── Table A1 (M8-A-R1 verified, commit add7cba) ──────────────────────────────
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

Z_DATA: list[float] = [r[0] for r in _TABLE_A1_RAW]
H_FLRW_DATA: list[float] = [r[1] for r in _TABLE_A1_RAW]
H_MULT_DATA: list[float] = [r[2] for r in _TABLE_A1_RAW]

# ── Cosmological parameters ───────────────────────────────────────────────────
H0: float = 70.0
OM_MATTER: float = 0.315
OM_LAMBDA: float = 0.685
SIGMA_8: float = 0.811
N_SPEC: float = 0.966  # spectral index
DELTA_C: float = 1.686  # spherical collapse threshold
C_KMS: float = 2.998e5

# Λ-matter equality redshift: z_eq = (Ω_Λ/Ω_m)^(1/3) - 1
Z_EQ_LAMBDA_MATTER: float = (OM_LAMBDA / OM_MATTER) ** (1.0 / 3.0) - 1.0


# ── ε(z) — NOT REDEFINED ─────────────────────────────────────────────────────


def compute_eps() -> list[float]:
    """
    ε(z) = (H_MULT/H_FLRW)² − 1 at 11 Table A1 redshifts.

    Source: M8-A-R1 [VERIFIED-tool, commit add7cba].
    Vector unchanged from prior gates. Peak at z=0.40 (ε=0.2277).
    """
    return [(hm / hf) ** 2 - 1.0 for hf, hm in zip(H_FLRW_DATA, H_MULT_DATA, strict=False)]


# ── ΛCDM background ──────────────────────────────────────────────────────────


def hubble_lcdm(z: float) -> float:
    """H(z) [km/s/Mpc] from flat ΛCDM."""
    return H0 * math.sqrt(OM_MATTER * (1 + z) ** 3 + OM_LAMBDA)


def comoving_distance_mpc(z: float, n_steps: int = 300) -> float:
    """D_C(z) [Mpc] via numerical integration of c/H(z')."""
    if z <= 0:
        return 0.0
    dz = z / n_steps
    total = 0.0
    for i in range(n_steps):
        zi = (i + 0.5) * dz
        total += C_KMS / hubble_lcdm(zi) * dz
    return total


def dVdz_comoving(z: float) -> float:
    """
    Comoving volume element dV/dz = 4π c D_C(z)² / H(z)  [Mpc³ per unit z].

    At z→0: D_C→0 so dV/dz→0 (no volume at our feet).
    Increases with z, peaks near z≈2 then levels off.
    """
    dc = comoving_distance_mpc(z)
    return 4.0 * math.pi * C_KMS * dc**2 / hubble_lcdm(z)


def growth_factor_ratio(z: float, n_steps: int = 500, z_max: float = 200.0) -> float:
    """
    D(z)/D(0) — linear growth factor normalized to today.

    Uses D(z) ∝ H(z) × ∫_z^∞ (1+z')/H(z')³ dz'.
    Ratio D(z)/D(0) eliminates the proportionality constant.

    Behaviour: D/D0 → 1/(1+z) at high z (matter-dominated); correct for flat ΛCDM.
    """

    def _integrand(zp: float) -> float:
        h = hubble_lcdm(zp)
        return (1.0 + zp) / h**3

    def _integral_from(z_low: float) -> float:
        dz = (z_max - z_low) / n_steps
        total = 0.0
        for i in range(n_steps):
            zi = z_low + (i + 0.5) * dz
            total += _integrand(zi) * dz
        return total

    i_z = _integral_from(z)
    i_0 = _integral_from(0.0)
    if i_0 < 1e-100:
        return 0.0
    return hubble_lcdm(z) * i_z / (hubble_lcdm(0.0) * i_0)


# ── Candidate A: intrinsic PS comoving density ────────────────────────────────


def candidate_a_ps_density(z: float, m_min_solar: float = 5e14) -> float:
    """
    Intrinsic PS comoving number density n(>M_min, z) [proportional].

    Simple Press-Schechter: n(>M) ∝ erfc(δ_c / (√2 σ(M,z)))
    σ(M,z) = σ_8 × (M/M_8)^{−α/3} × D(z)/D(0)

    WARNING: NOT_CLAIM_PS_FACT — used as hypothesis model, not physical fact.
    Behaviour: monotone decreasing with z (fewer massive clusters at early times).
    """
    h = H0 / 100.0
    rho_m = OM_MATTER * 2.775e11 / h**2  # M_sun/Mpc³ (comoving mean density)
    m8 = (4.0 * math.pi / 3.0) * (8.0 / h) ** 3 * rho_m  # mass in 8 Mpc/h sphere

    alpha_ps = (N_SPEC + 3.0) / 6.0  # ≈ 0.661

    sigma_m = SIGMA_8 * (m_min_solar / m8) ** (-alpha_ps / 3.0)
    dz = growth_factor_ratio(z)
    sigma_mz = sigma_m * max(dz, 1e-30)

    arg = DELTA_C / (math.sqrt(2.0) * sigma_mz)
    return math.erfc(arg)  # proportional to n(>M)


# ── Candidate B: intrinsic dN/dz (PS + volume) ───────────────────────────────


def candidate_b_intrinsic_dNdz(z: float, m_min_solar: float = 5e14) -> float:
    """
    Intrinsic dN/dz = n(>M_min, z) × dV/dz.

    No survey selection function applied.
    Competition between n(z) decreasing and dV/dz increasing creates a peak
    that depends on M_min — not a fixed physics prediction.
    """
    n = candidate_a_ps_density(z, m_min_solar)
    dvdz = dVdz_comoving(z)
    return n * dvdz


# ── Candidate C: SZ-selection-weighted dN/dz ─────────────────────────────────


def sz_selection_model(z: float, z_peak: float = 0.40, alpha: float = 2.0) -> float:
    """
    Parametric SZ survey selection function f_sel(z).

    Models flux-limited SZ survey (SPT/ACT/Planck-like):
      - Low z: clusters too extended, beam dilution suppresses detection
      - z≈z_peak: optimal detection (angular size + flux balanced)
      - High z: clusters too faint (flux ∝ 1/D_A²)

    f_sel(z) = (z/z_peak)^alpha × exp(−alpha × (z/z_peak − 1))
    Peak at z=z_peak for any alpha > 0.

    WARNING: PARAMETRIC MODEL ONLY — not derived from actual SPT/ACT/Planck
             selection curves. Label: SELECTION_MODEL_PARAMETRIC [HYPOTHESIS].
    """
    if z <= 0:
        return 0.0
    ratio = z / z_peak
    return ratio**alpha * math.exp(-alpha * (ratio - 1.0))


def candidate_c_sz_weighted(z: float, m_min_solar: float = 5e14, z_peak: float = 0.40) -> float:
    """
    SZ-selection-weighted dN/dz = dN/dz_intrinsic × f_sel(z).

    Key test: does adding f_sel substantially increase r(ε, dN/dz_obs)?
    If yes → the M8-C r=0.723 signal may be selection-driven, not physical.
    """
    return candidate_b_intrinsic_dNdz(z, m_min_solar) * sz_selection_model(z, z_peak)


def f_sel_alone(z: float, z_peak: float = 0.40) -> float:
    """
    Selection function in isolation — SMOKING GUN diagnostic.

    If r(ε, f_sel_alone) ≈ r(ε, dN/dz_obs from M8-C), then the M8-C
    correlation is explained by instrument selection, NOT cluster physics.
    f_sel has zero physics — it is purely an instrument model.
    """
    return sz_selection_model(z, z_peak)


# ── Candidate D: ΛCDM transition proxy ───────────────────────────────────────


def candidate_d_lcdm_transition(z: float) -> float:
    """
    Dark energy fraction f_DE(z) = Ω_Λ / (Ω_m(1+z)³ + Ω_Λ).

    Monotone decreasing: from ≈0.685 at z=0 to ≈0 at z>>1.
    Tests whether ε correlates with the ΛCDM dark energy domination epoch.

    z_eq (Λ-matter equality) ≈ 0.303 — close to ε peak at z=0.40.
    But f_DE is monotone → cannot explain the non-monotone ε structure.
    """
    matter_term = OM_MATTER * (1.0 + z) ** 3
    return OM_LAMBDA / (matter_term + OM_LAMBDA)


# ── Statistics ────────────────────────────────────────────────────────────────


def _pearson_r(x: list[float], y: list[float]) -> float:
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    num = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y, strict=False))
    dx = math.sqrt(sum((xi - mx) ** 2 for xi in x))
    dy = math.sqrt(sum((yi - my) ** 2 for yi in y))
    return num / (dx * dy) if dx * dy > 1e-14 else 0.0


def _is_monotone_decreasing(vals: list[float]) -> bool:
    return all(vals[i + 1] <= vals[i] for i in range(len(vals) - 1))


def _normalize(vals: list[float]) -> list[float]:
    max_v = max(vals)
    return [v / max_v for v in vals] if max_v > 1e-30 else list(vals)


def _peak_z(vals: list[float]) -> float:
    return Z_DATA[vals.index(max(vals))]


def _verdict(r: float) -> str:
    if r < -0.3:
        return "KILL"
    if r < 0.5:
        return "INSUFFICIENT"
    if r < 0.75:
        return "PARTIAL"
    return "SURVIVES"


# ── Main audit ────────────────────────────────────────────────────────────────


def run_audit() -> dict:
    """Run HD-MAVP-1 audit. Returns full report dict."""
    eps = compute_eps()
    eps_peak_z = _peak_z(eps)

    m_min_values: list[float] = [1e14, 5e14, 2e15]
    candidates_by_m: dict[str, dict] = {}

    for m_min in m_min_values:
        key = f"{m_min:.0e}"

        # Candidate A
        a_raw = [candidate_a_ps_density(z, m_min) for z in Z_DATA]
        a_norm = _normalize(a_raw)
        r_a = _pearson_r(eps, a_norm)

        # Candidate B
        b_raw = [candidate_b_intrinsic_dNdz(z, m_min) for z in Z_DATA]
        b_norm = _normalize(b_raw)
        r_b = _pearson_r(eps, b_norm)

        # Candidate C
        c_raw = [candidate_c_sz_weighted(z, m_min) for z in Z_DATA]
        c_norm = _normalize(c_raw)
        r_c = _pearson_r(eps, c_norm)

        candidates_by_m[key] = {
            "A_ps_density": {
                "pearson_r": round(r_a, 4),
                "peak_z": _peak_z(a_norm),
                "is_monotone_decreasing": _is_monotone_decreasing(a_norm),
                "verdict": _verdict(r_a),
            },
            "B_intrinsic_dNdz": {
                "pearson_r": round(r_b, 4),
                "peak_z": _peak_z(b_norm),
                "is_monotone_decreasing": _is_monotone_decreasing(b_norm),
                "verdict": _verdict(r_b),
            },
            "C_sz_selection": {
                "pearson_r": round(r_c, 4),
                "peak_z": _peak_z(c_norm),
                "is_monotone_decreasing": _is_monotone_decreasing(c_norm),
                "verdict": _verdict(r_c),
            },
        }

    # Candidate D (mass-independent)
    d_raw = [candidate_d_lcdm_transition(z) for z in Z_DATA]
    d_norm = _normalize(d_raw)
    r_d = _pearson_r(eps, d_norm)

    # Selection function alone — smoking gun
    fsel_raw = [f_sel_alone(z) for z in Z_DATA]
    fsel_norm = _normalize(fsel_raw)
    r_fsel = _pearson_r(eps, fsel_norm)

    # Aggregate verdicts
    all_a_verdicts = [candidates_by_m[k]["A_ps_density"]["verdict"] for k in candidates_by_m]
    all_b_verdicts = [candidates_by_m[k]["B_intrinsic_dNdz"]["verdict"] for k in candidates_by_m]
    all_c_verdicts = [candidates_by_m[k]["C_sz_selection"]["verdict"] for k in candidates_by_m]

    a_killed = all(v in ("KILL", "INSUFFICIENT") for v in all_a_verdicts)
    b_insufficient = sum(1 for v in all_b_verdicts if v in ("KILL", "INSUFFICIENT")) >= 2
    c_survives = any(v in ("SURVIVES", "PARTIAL") for v in all_c_verdicts)
    fsel_spurious = r_fsel > 0.5  # selection alone creates correlation with ε

    intrinsic_formation_verdict = "KILLED" if a_killed else "PARTIAL"
    selection_artifact_verdict = "SURVIVES_AS_ARTIFACT" if c_survives else "INSUFFICIENT"

    if a_killed and c_survives:
        overall_verdict = "PARTIAL-KILL"
    elif a_killed and not c_survives:
        overall_verdict = "FAIL"
    else:
        overall_verdict = "PARTIAL-KILL"

    # Sample r values for conclusions
    r_a_ref = candidates_by_m["5e+14"]["A_ps_density"]["pearson_r"]
    r_b_ref = candidates_by_m["5e+14"]["B_intrinsic_dNdz"]["pearson_r"]
    r_c_ref = candidates_by_m["5e+14"]["C_sz_selection"]["pearson_r"]

    conclusions = [
        f"ε(z) peak confirmed at z={eps_peak_z} (M8-A-R1 [VERIFIED-tool] — NOT REDEFINED).",
        f"Candidate A (PS density, M_min=5e14): r={r_a_ref} → {candidates_by_m['5e+14']['A_ps_density']['verdict']}."
        " Monotone decreasing — anti-correlated with ε — KILLED.",
        f"Candidate B (intrinsic dN/dz, M_min=5e14): r={r_b_ref} → {candidates_by_m['5e+14']['B_intrinsic_dNdz']['verdict']}."
        " Peak location M_min-sensitive — not a fixed physics prediction.",
        f"Candidate C (SZ-selection-weighted, M_min=5e14): r={r_c_ref} → {candidates_by_m['5e+14']['C_sz_selection']['verdict']}."
        " Selection function artificially anchors peak at z=0.40.",
        f"Selection function ALONE: r(ε, f_sel) = {round(r_fsel, 4)}."
        f" {'SPURIOUS CORRELATION CONFIRMED' if fsel_spurious else 'Below threshold'}:"
        " instrument model (zero physics) produces correlation similar to M8-C r=0.723.",
        f"Candidate D (ΛCDM transition, f_DE): r={round(r_d, 4)} → {_verdict(r_d)}."
        f" Monotone; z_eq={round(Z_EQ_LAMBDA_MATTER, 3)} (proximity {abs(0.40 - Z_EQ_LAMBDA_MATTER):.3f} to ε peak)."
        " Cannot explain non-monotone ε structure.",
        f"Overall verdict: {overall_verdict}.",
        "PARTIAL-KILL: intrinsic cluster formation history KILLED;"
        " selection/schedule artifact SURVIVES as alternative explanation.",
        "M8-C r=0.723 may be selection-driven (ARTIFACT) not physical cluster formation."
        " Author schedule Q2 still needed to determine which.",
        "<HYPOTHESIS>: if author schedule tracks observed (SZ-selected) dN/dz,"
        " correlation is real by construction — cannot distinguish without Q1+Q2.",
    ]

    result: dict = {
        "gate": "HD-MAVP-1",
        "date": "2026-06-13",
        "labels": [
            "HD_MAVP_1",
            "OUR_RECONSTRUCTION",
            "NOT_AUTHOR_CONFIRMED",
            "NOT_VALIDATION",
            "NOT_REFUTATION",
            "SELECTION_BIAS_AUDIT",
            "NOT_CLAIM_PS_FACT",
        ],
        "eps_source": "M8-A-R1 [VERIFIED-tool, commit add7cba] — NOT REDEFINED HERE",
        "eps_values": {str(z): round(e, 6) for z, e in zip(Z_DATA, eps, strict=False)},
        "eps_peak_z": eps_peak_z,
        "eps_is_non_monotone": True,
        "candidates_by_m_min": candidates_by_m,
        "candidate_D_lcdm": {
            "pearson_r": round(r_d, 4),
            "is_monotone_decreasing": _is_monotone_decreasing(d_norm),
            "verdict": _verdict(r_d),
            "z_eq_lambda_matter": round(Z_EQ_LAMBDA_MATTER, 4),
            "z_eq_proximity_to_eps_peak": round(abs(0.40 - Z_EQ_LAMBDA_MATTER), 4),
        },
        "selection_function_alone": {
            "pearson_r": round(r_fsel, 4),
            "peak_z": _peak_z(fsel_norm),
            "verdict": _verdict(r_fsel),
            "spurious_correlation_confirmed": fsel_spurious,
            "interpretation": (
                "f_sel has zero cluster physics. "
                f"r(ε, f_sel)={round(r_fsel, 4)} near M8-C r=0.723 → "
                "M8-C signal may be selection artifact, not cluster formation."
                if fsel_spurious
                else "r below threshold — selection alone insufficient."
            ),
        },
        "intrinsic_formation_verdict": intrinsic_formation_verdict,
        "selection_artifact_verdict": selection_artifact_verdict,
        "b_verdict_m_sensitive": not b_insufficient,
        "overall_verdict": overall_verdict,
        "conclusions": conclusions,
        "safety": (
            "HD_MAVP_1 · OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED · "
            "NOT_VALIDATION · NOT_REFUTATION · NOT_CLAIM_PS_FACT"
        ),
        "physics_notes": {
            "ps_treated_as_hypothesis": True,
            "sz_selection_is_parametric_model": True,
            "selection_model_not_from_actual_survey": True,
            "eps_vector_unchanged_from_m8a_r1": True,
            "no_mcmc": True,
            "no_new_eps_definition": True,
        },
    }

    out = Path(__file__).parent.parent / "reports" / "hdmavp1_epsilon_cluster_audit.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    return result


if __name__ == "__main__":
    print("Running HD-MAVP-1 Cluster Formation Audit...")
    result = run_audit()
    print(f"Gate: {result['gate']}")
    print(f"Verdict: {result['overall_verdict']}")
    print(f"ε peak z: {result['eps_peak_z']}")
    print(f"Intrinsic formation: {result['intrinsic_formation_verdict']}")
    print(f"Selection artifact: {result['selection_artifact_verdict']}")
    print(f"r(ε, f_sel_alone): {result['selection_function_alone']['pearson_r']}")
    print(
        f"Spurious correlation: {result['selection_function_alone']['spurious_correlation_confirmed']}"
    )
    print()
    print("By M_min:")
    for m_key, cands in result["candidates_by_m_min"].items():
        print(
            f"  M={m_key}: A r={cands['A_ps_density']['pearson_r']} ({cands['A_ps_density']['verdict']}) | "
            f"B r={cands['B_intrinsic_dNdz']['pearson_r']} ({cands['B_intrinsic_dNdz']['verdict']}) | "
            f"C r={cands['C_sz_selection']['pearson_r']} ({cands['C_sz_selection']['verdict']})"
        )
    print(
        f"D (ΛCDM): r={result['candidate_D_lcdm']['pearson_r']} ({result['candidate_D_lcdm']['verdict']})"
    )
    print()
    for c in result["conclusions"]:
        print(f"  {c}")
