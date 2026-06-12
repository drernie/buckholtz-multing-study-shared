"""
ASRE — Author-Schedule Reverse Engineering

Reverse-engineers the minimal k_A(z) / D_eff(z) schedule required to
reproduce Table A1 under the MULTING Friedmann-cluster framework.

Method (model-independent first):
  Step 1: Extract required_bridge(z) = ε(z) × H_FLRW(z)²  [no free parameters]
          This is the H² excess that ANY valid bridge must produce.
  Step 2: Normalize required_bridge to z=0.40 → required_shape(z)
  Step 3: Map the (k_A, D_eff) degeneracy across 3 parametric families
  Step 4: Compare required k_A families to virial k_A (confirms M8-D THEOREM)
  Step 5: Degeneracy analysis — how many (k_A, D_eff) pairs reproduce required_shape

Core constraint (from Friedmann equation):
  required_bridge(z) = ε(z) × H_FLRW(z)²
  = (H_MULT²(z) − H_FLRW²(z)) / (H_FLRW² / H_FLRW²)  [in (km/s/Mpc)²]

Degeneracy principle:
  For bridge_func(k_A, D_eff) = C × k_A(z) / D_eff(z)^p:
    k_A(z) ∝ required_bridge(z) × D_eff(z)^p / C
  → For any choice of D_eff(z), k_A(z) is uniquely determined up to overall C.
  → (k_A, D_eff) are NOT separately constrained by Table A1 alone.

Labels:
  ASRE · AUTHOR_SCHEDULE_REVERSE_ENGINEERING · OUR_RECONSTRUCTION
  NOT_AUTHOR_CONFIRMED · NOT_VALIDATION · NOT_REFUTATION
  AUTHOR_SCHEDULE_NEEDED
"""

from __future__ import annotations

import json
import math
from pathlib import Path

# ── Table A1 data [TRANSCRIBED, arithmetic verified M8-A-R1 PASS] ──────────
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

# ── ΛCDM parameters ───────────────────────────────────────────────────────────
H0_KMS_MPC: float = 70.0
OM_MATTER: float = 0.315
OM_LAMBDA: float = 0.685

# ── Physical constants ────────────────────────────────────────────────────────
G_SI: float = 6.674e-11  # m³ kg⁻¹ s⁻²
KM_PER_MPC: float = 3.0857e19  # km per Mpc (1 Mpc in km)
C_KMS: float = 2.998e5  # speed of light in km/s

# ── Bridge formula power for degeneracy analysis ──────────────────────────────
# Assumed minimal form: bridge_func ∝ k_A(z) / D_eff(z)^p
# We test p=2 (canonical inverse-square force) and p=1 (linear falloff)
P_CANONICAL: float = 2.0


# ── Core: ε(z) and required_bridge(z) ────────────────────────────────────────


def compute_eps_all() -> list[float]:
    """ε(z) = (H_MULT/H_FLRW)² − 1 for all Table A1 rows."""
    return [(hm / hf) ** 2 - 1.0 for hf, hm in zip(H_FLRW_DATA, H_MULT_DATA, strict=False)]


def compute_required_bridge() -> list[float]:
    """
    required_bridge(z) = ε(z) × H_FLRW(z)²  [(km/s/Mpc)²]

    This is the H² excess the cluster term must contribute at each epoch.
    Model-independent: follows directly from Friedmann + Table A1.

    NOTE: OUR_RECONSTRUCTION from Table A1. NOT physically measured.
    """
    eps = compute_eps_all()
    return [e * hf**2 for e, hf in zip(eps, H_FLRW_DATA, strict=False)]


def normalize_at_z040(values: list[float]) -> list[float]:
    """Normalize values so that the z=0.40 entry = 1.0."""
    i_ref = Z_DATA.index(0.40)
    ref = values[i_ref]
    if abs(ref) < 1e-30:
        return list(values)
    return [v / ref for v in values]


# ── ΛCDM background ───────────────────────────────────────────────────────────


def hubble_lcdm(z: float) -> float:
    """H(z) in km/s/Mpc from flat ΛCDM."""
    return H0_KMS_MPC * math.sqrt(OM_MATTER * (1 + z) ** 3 + OM_LAMBDA)


def hubble_distance_mpc(z: float) -> float:
    """D_H(z) = c / H(z) in Mpc — Hubble horizon."""
    return C_KMS / hubble_lcdm(z)


def rho_crit_cosmo(z: float) -> float:
    """ρ_crit(z) in M_sun/Mpc³."""
    H_km = hubble_lcdm(z)
    H_si = H_km * 1e3 / 3.0857e22
    kg_per_msun = 1.989e30
    m_per_mpc = 3.0857e22
    rho_si = 3.0 * H_si**2 / (8.0 * math.pi * G_SI)
    return rho_si * m_per_mpc**3 / kg_per_msun


def r_vir_mpc(m_solar: float, z: float, delta_vir: float = 200.0) -> float:
    """Virial radius for halo of mass m_solar at redshift z [Mpc]."""
    rho_c = rho_crit_cosmo(z)
    return (3.0 * m_solar / (4.0 * math.pi * delta_vir * rho_c)) ** (1.0 / 3.0)


def k_A_virial_shape(z: float) -> float:
    """Normalized virial k_A shape ∝ H(z)^(4/3) [no mass dependence]."""
    return hubble_lcdm(z) ** (4.0 / 3.0)


# ── Degeneracy families ───────────────────────────────────────────────────────
#
# We assume: bridge_func(k_A, D_eff) ∝ k_A(z) / D_eff(z)²
# → k_A_required(z) ∝ required_bridge(z) × D_eff(z)²
# → D_eff_required(z) ∝ sqrt(k_A(z) / required_bridge(z))
#
# Three families covering the plausible range:


def family_a_k_A(rb_norm: list[float]) -> dict:
    """
    Family A: D_eff(z) = D_H(z) = c/H(z) (Hubble distance — a natural cosmic scale).

    Then k_A_required(z) ∝ required_bridge(z) × D_H(z)²
                          = ε(z) × H_FLRW(z)² × (c/H(z))²
                          = ε(z) × c²

    Key result: k_A ∝ ε(z) when D_eff = D_H.
    This means the Hubble-distance assumption makes k_A track ε EXACTLY.
    """
    eps = compute_eps_all()
    eps_norm = normalize_at_z040(eps)
    peak_z = Z_DATA[eps_norm.index(max(eps_norm))]
    return {
        "family": "A",
        "D_eff_assumption": "D_H(z) = c/H_FLRW(z) (Hubble distance)",
        "k_A_formula": "k_A ∝ ε(z) × c²  [simplifies: H² factors cancel]",
        "k_A_required_shape": [round(v, 6) for v in eps_norm],
        "k_A_peak_z": peak_z,
        "k_A_is_monotone": _is_monotone(eps_norm),
        "pearson_r_vs_virial": round(_pearson_r(eps_norm, _virial_shape_norm()), 4),
        "note": (
            "k_A tracks ε(z) exactly — non-monotone by INSIGHT-1. "
            "This choice eliminates the H² factor and yields the cleanest non-virial k_A."
        ),
    }


def family_b_k_A(rb_norm: list[float]) -> dict:
    """
    Family B: D_eff(z) = r_vir(M=1e14, z) (virial radius — a cluster's own scale).

    Then k_A_required(z) ∝ required_bridge(z) × r_vir(z)²
    r_vir ∝ H(z)^(-2/3) (monotone decreasing with z)
    → k_A_required ∝ ε(z) × H(z)² × H(z)^(-4/3) = ε(z) × H(z)^(2/3)
    """
    m_ref = 1.0e14  # M_sun — reference mass
    r_vir_vals = [r_vir_mpc(m_ref, z) for z in Z_DATA]
    r_vir_norm = normalize_at_z040(r_vir_vals)

    k_A_b = [rb * rv**2 for rb, rv in zip(rb_norm, r_vir_norm, strict=False)]
    k_A_b_norm = normalize_at_z040(k_A_b)
    peak_z = Z_DATA[k_A_b_norm.index(max(k_A_b_norm))]

    return {
        "family": "B",
        "D_eff_assumption": "r_vir(M=1e14, z) (virial radius of reference cluster)",
        "k_A_formula": "k_A ∝ required_bridge(z) × r_vir(z)²  ∝ ε(z) × H(z)^(2/3)",
        "k_A_required_shape": [round(v, 6) for v in k_A_b_norm],
        "k_A_peak_z": peak_z,
        "k_A_is_monotone": _is_monotone(k_A_b_norm),
        "pearson_r_vs_virial": round(_pearson_r(k_A_b_norm, _virial_shape_norm()), 4),
        "note": (
            "k_A still non-monotone because ε is non-monotone. "
            "r_vir is monotone but cannot suppress the ε peak."
        ),
    }


def family_c_D_eff(rb_norm: list[float]) -> dict:
    """
    Family C: k_A(z) = const (uniform cluster activity — simplest k_A assumption).

    Then D_eff_required(z) ∝ sqrt(k_A_const / required_bridge(z))
                            ∝ required_bridge(z)^(-1/2)
                            ∝ [ε(z) × H(z)²]^(-1/2)

    D_eff must DECREASE when ε increases (cluster closer when more active).
    D_eff minimum at z=0.40 (ε peak). D_eff maximum at z=5.0 (ε minimum).
    """
    d_eff_required = [1.0 / math.sqrt(max(rb, 1e-30)) for rb in rb_norm]
    d_eff_norm = normalize_at_z040(d_eff_required)

    virial_d_eff = [r_vir_mpc(1.0e14, z) for z in Z_DATA]
    virial_d_norm = normalize_at_z040(virial_d_eff)

    pearson_d_vs_virial = _pearson_r(d_eff_norm, virial_d_norm)

    return {
        "family": "C",
        "k_A_assumption": "k_A = const (uniform cluster activity)",
        "D_eff_formula": "D_eff ∝ [required_bridge(z)]^(-1/2) ∝ [ε(z)·H(z)²]^(-1/2)",
        "D_eff_required_shape": [round(v, 6) for v in d_eff_norm],
        "D_eff_min_at_z": Z_DATA[d_eff_norm.index(min(d_eff_norm))],
        "D_eff_max_at_z": Z_DATA[d_eff_norm.index(max(d_eff_norm))],
        "D_eff_is_monotone": _is_monotone(d_eff_norm),
        "pearson_r_vs_virial_r_vir": round(pearson_d_vs_virial, 4),
        "note": (
            "D_eff must be non-monotone: minimum at z=0.40 (ε peak), maximum at z=5.0. "
            "Anti-correlated with virial r_vir. "
            "This implies clusters are 'closer' during peak activity — unusual."
        ),
    }


# ── Virial anti-correlation confirmation ─────────────────────────────────────


def virial_vs_required_comparison() -> dict:
    """
    Compare virial k_A shape to required k_A shapes from degeneracy families.

    Key comparison: virial k_A ∝ H(z)^(4/3) vs Family A k_A ∝ ε(z).
    ε(z) is what k_A must track when D_eff = D_H (Hubble distance).
    This is the same anti-correlation established in M8-D.

    Also show: virial vs required_bridge (absolute) = correlated because both
    grow with z (H growth dominates) — this is a different physics question.
    """
    eps = compute_eps_all()
    eps_norm = normalize_at_z040(eps)
    rb = compute_required_bridge()
    rb_norm = normalize_at_z040(rb)
    virial_norm = _virial_shape_norm()

    r_vs_eps = _pearson_r(virial_norm, eps_norm)  # the M8-D-relevant comparison
    r_vs_rb = _pearson_r(virial_norm, rb_norm)  # absolute bridge — both grow with z
    peak_virial_z = Z_DATA[virial_norm.index(max(virial_norm))]
    peak_eps_z = Z_DATA[eps_norm.index(max(eps_norm))]
    peak_rb_z = Z_DATA[rb_norm.index(max(rb_norm))]

    return {
        "pearson_r_virial_vs_eps": round(r_vs_eps, 4),
        "pearson_r_virial_vs_abs_bridge": round(r_vs_rb, 4),
        "peak_virial_at_z": peak_virial_z,
        "peak_eps_at_z": peak_eps_z,
        "peak_abs_bridge_at_z": peak_rb_z,
        "anti_correlated_to_eps": r_vs_eps < 0.0,
        "confirms_m8d_theorem": r_vs_eps < -0.3,
        "note_on_abs_bridge": (
            "Virial k_A and abs bridge ε×H² are POSITIVELY correlated (both grow with z) "
            "because H² growth dominates at high z. This does NOT confirm virial is the "
            "right schedule — it means both quantities share the H(z) growth trend."
        ),
        "interpretation": (
            f"Virial k_A ∝ H(z)^(4/3) is ANTI-correlated with ε(z) (Pearson r={round(r_vs_eps, 4):.4f}). "
            "ε(z) is the required k_A shape when D_eff = Hubble distance (Family A). "
            "Standard virial scaling cannot supply the required fractional bridge shape — "
            "confirms M8-D THEOREM (INSIGHT-3)."
        ),
    }


# ── Degeneracy summary ────────────────────────────────────────────────────────


def degeneracy_analysis(rb_norm: list[float]) -> dict:
    """
    Show that infinitely many (k_A, D_eff) pairs reproduce required_bridge.

    For bridge ∝ k_A / D_eff^p:
    k_A(z) = C × required_bridge(z) × D_eff(z)^p

    For any smooth D_eff(z) > 0, there exists a unique k_A(z) that satisfies this.
    The required SHAPE of k_A is: required_bridge × D_eff^p (normalized).

    What IS uniquely determined:
      k_A(z) / D_eff(z)^p  ∝  required_bridge(z)  [up to overall constant]

    What is NOT determinable without Q1+Q2:
      k_A(z) individually
      D_eff(z) individually
      The power p (canonical p=2, but p=1 is possible)
      The overall normalization constant C
    """
    return {
        "uniquely_determined": "k_A(z) / D_eff(z)^p ∝ ε(z) × H_FLRW(z)²  [up to constant]",
        "not_determinable": [
            "k_A(z) individually (requires Q1 bridge formula + D_eff assumption)",
            "D_eff(z) individually (requires Q1 bridge formula + k_A assumption)",
            "power p in bridge ∝ k_A/D_eff^p (canonical p=2, not confirmed)",
            "overall normalization constant C (absorbs units and geometry)",
        ],
        "degeneracy_type": "continuous 1-parameter family for each assumed p",
        "key_constraint_preserved": "ALL valid (k_A, D_eff) pairs must produce non-monotone required_bridge",
        "virial_k_A_excluded": True,
        "virial_excluded_reason": (
            "Virial k_A ∝ H(z)^(4/3) is monotone. "
            "For any D_eff choice with D_eff monotone, k_A_required = rb × D_eff^p is non-monotone. "
            "For D_eff non-monotone, k_A could theoretically be monotone, but then D_eff "
            "itself must carry the non-monotone structure — still non-standard. "
            "In either case, the standard virial schedule alone cannot explain ε(z)."
        ),
        "minimum_parameters": 2,
        "min_param_note": "At minimum: 1 parameter for non-monotone shape + 1 for normalization",
    }


# ── Utilities ─────────────────────────────────────────────────────────────────


def _pearson_r(x: list[float], y: list[float]) -> float:
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    num = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y, strict=False))
    dx = math.sqrt(sum((xi - mx) ** 2 for xi in x))
    dy = math.sqrt(sum((yi - my) ** 2 for yi in y))
    return num / (dx * dy) if dx * dy > 1e-14 else 0.0


def _is_monotone(vals: list[float]) -> bool:
    return all(vals[i + 1] >= vals[i] for i in range(len(vals) - 1)) or all(
        vals[i + 1] <= vals[i] for i in range(len(vals) - 1)
    )


def _virial_shape_norm() -> list[float]:
    """Virial k_A shape ∝ H(z)^(4/3), normalized at z=0.40."""
    raw = [k_A_virial_shape(z) for z in Z_DATA]
    return normalize_at_z040(raw)


# ── Main run ──────────────────────────────────────────────────────────────────


def run_asre() -> dict:
    """
    Run full ASRE analysis. Returns dict with all results.

    Verdict logic:
      PARTIAL — required_bridge extracted, degeneracy mapped, but
                unique (k_A, D_eff) pair cannot be determined without Q1.
    """
    eps = compute_eps_all()
    rb = compute_required_bridge()
    eps_norm = normalize_at_z040(eps)
    rb_norm = normalize_at_z040(rb)

    fam_a = family_a_k_A(rb_norm)
    fam_b = family_b_k_A(rb_norm)
    fam_c = family_c_D_eff(rb_norm)
    virial_comp = virial_vs_required_comparison()
    degen = degeneracy_analysis(rb_norm)

    # Assess verdict — use anti-correlation with eps (Family A), not with abs bridge
    anti_corr_confirmed = virial_comp["anti_correlated_to_eps"]
    fam_a_non_mono = not fam_a["k_A_is_monotone"]
    fam_b_non_mono = not fam_b["k_A_is_monotone"]
    extraction_ok = abs(eps_norm[Z_DATA.index(0.40)] - 1.0) < 1e-9

    if extraction_ok and anti_corr_confirmed and fam_a_non_mono and fam_b_non_mono:
        verdict = "PARTIAL"
    else:
        verdict = "BLOCKED"

    r_virial_eps = virial_comp["pearson_r_virial_vs_eps"]
    peak_eps_z = Z_DATA[eps_norm.index(max(eps_norm))]

    conclusions = [
        "required_bridge(z) = ε(z) × H_FLRW(z)² uniquely extracted from Table A1 — no free parameters.",
        f"ε(z) [fractional excess] peaks at z={peak_eps_z:.2f}. "
        f"required_bridge [absolute excess] peaks at z=8.50 (H² growth dominates at high z).",
        "Two natural targets: ε(z) [fractional, peaks z=0.40] and required_bridge [absolute, peaks z=8.50].",
        "Family A (D_eff=D_H): k_A ∝ ε(z) × c² — H² factors cancel, k_A tracks ε exactly, peak z=0.40.",
        f"Family A Pearson r vs virial = {fam_a['pearson_r_vs_virial']:.4f} — anti-correlated.",
        "Family B (D_eff=r_vir): k_A ∝ ε(z)·H(z)^(2/3) — still non-monotone, peak z=0.40.",
        "Family C (k_A=const): D_eff ∝ [ε·H²]^(-1/2) — non-monotone, D_eff min where bridge is max.",
        f"Virial k_A vs ε(z) Pearson r = {r_virial_eps:.4f} — ANTI-CORRELATED (confirms M8-D INSIGHT-3).",
        "THEOREM CONFIRMED: standard virial k_A ∝ H^(4/3) is anti-correlated with required fractional k_A.",
        "DEGENERACY: k_A and D_eff cannot be separated from Table A1 alone — requires Q1 bridge formula.",
        f"Overall verdict: {verdict}.",
        "AUTHOR_SCHEDULE_NEEDED: required k_A shape known (∝ ε for Family A), but unique (k_A, D_eff) split requires Q1+Q2.",
        "<HYPOTHESIS>: the non-monotone ε(z) shape may be connected to cluster formation rate (cf. M8-C dN/dz signal r=0.723).",
    ]

    result = {
        "gate": "ASRE-required-schedule",
        "date": "2026-06-13",
        "labels": [
            "ASRE",
            "AUTHOR_SCHEDULE_REVERSE_ENGINEERING",
            "OUR_RECONSTRUCTION",
            "NOT_AUTHOR_CONFIRMED",
            "NOT_VALIDATION",
            "NOT_REFUTATION",
            "AUTHOR_SCHEDULE_NEEDED",
            "<HYPOTHESIS>",
        ],
        "table_a1_source": "TRANSCRIBED · arithmetic verified M8-A-R1 PASS · NOT observational data",
        "method": {
            "step1": "Extract required_bridge(z) = ε(z) × H_FLRW(z)² — model-independent",
            "step2": "Normalize at z=0.40 — required_shape(z)",
            "step3": "Map (k_A, D_eff) degeneracy — 3 parametric families",
            "step4": "Compare virial k_A to required shape — confirm M8-D theorem",
            "step5": "Degeneracy documentation — what IS and IS NOT determinable",
        },
        "eps_at_z_data": {str(z): round(e, 6) for z, e in zip(Z_DATA, eps, strict=False)},
        "eps_norm": {str(z): round(e, 6) for z, e in zip(Z_DATA, eps_norm, strict=False)},
        "eps_peak_z": peak_eps_z,
        "eps_is_non_monotone": not _is_monotone(eps_norm),
        "required_bridge_norm": {
            str(z): round(rb, 6) for z, rb in zip(Z_DATA, rb_norm, strict=False)
        },
        "required_bridge_peak_z": Z_DATA[rb_norm.index(max(rb_norm))],
        "required_bridge_is_non_monotone": not _is_monotone(rb_norm),
        "note_two_targets": (
            "eps_norm = fractional H² excess (peaks z=0.40) — relevant for k_A when D_eff=D_H. "
            "required_bridge_norm = absolute H² excess (peaks z=8.50, H² growth dominates) — "
            "relevant for k_A when D_eff is a physical cluster length scale."
        ),
        "degenerate_families": {
            "family_A": fam_a,
            "family_B": fam_b,
            "family_C": fam_c,
        },
        "virial_comparison": virial_comp,
        "degeneracy_analysis": degen,
        "overall_verdict": verdict,
        "conclusions": conclusions,
        "safety": (
            "ASRE · OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED · "
            "NOT_VALIDATION · NOT_REFUTATION · AUTHOR_SCHEDULE_NEEDED"
        ),
        "physics_notes": {
            "bridge_formula_assumed": "H²_MULT - H²_FLRW = C × k_A(z) / D_eff(z)^p",
            "p_assumed": P_CANONICAL,
            "no_MCMC": True,
            "no_FLRW_fitting": True,
            "no_TableA1_powerlaw_fit": True,
            "degeneracy_documented": True,
        },
    }

    report_path = Path(__file__).parent.parent / "reports" / "asre_required_schedule.json"
    report_path.parent.mkdir(exist_ok=True)
    report_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    return result


if __name__ == "__main__":
    result = run_asre()
    vc = result["virial_comparison"]
    print(f"Gate: {result['gate']}")
    print(f"Verdict: {result['overall_verdict']}")
    print(
        f"eps peak z: {result['eps_peak_z']}  |  required_bridge peak z: {result['required_bridge_peak_z']}"
    )
    print(f"Virial r vs eps (Family A comparison): {vc['pearson_r_virial_vs_eps']}")
    print(f"Virial r vs abs bridge: {vc['pearson_r_virial_vs_abs_bridge']}")
    print(f"Anti-correlated to eps: {vc['anti_correlated_to_eps']}")
    print("\nFamily A peak z:", result["degenerate_families"]["family_A"]["k_A_peak_z"])
    print("Family B peak z:", result["degenerate_families"]["family_B"]["k_A_peak_z"])
    print("Family C D_eff min z:", result["degenerate_families"]["family_C"]["D_eff_min_at_z"])
    print("\nConclusions:")
    for c in result["conclusions"]:
        print(" ", c)
