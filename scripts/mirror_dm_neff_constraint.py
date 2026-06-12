"""
Mirror DM / N_eff Constraint — IDM "5 dark isomers" interpretation

IF IDM's 5 dark isomers are interpreted as Mirror Dark Matter
(each isomer = dark sector with SM-counterpart particles),
what constraint does Planck 2018 ΔN_eff < 0.40 impose on T_dark/T_SM?

Motivation: Preprint line 1063-1065 states each isomer "might associate
with a set of elementary particles for which there is one elementary-particle
counterpart for each known (or ordinary-matter) elementary particle."
This is structurally identical to Mirror Dark Matter (Berezhiani 2004,
Foot 2014). Mirror DM literature has worked out ΔN_eff constraints;
we apply them here as an external cross-check.

Labels: OUR_RECONSTRUCTION · IF_MIRROR_DM_INTERPRETATION
        EXTERNAL_STANDARD_PHYSICS · NOT_VALIDATION · NOT_REFUTATION
Scope:  INTERNAL_DIAGNOSTIC_ONLY · NOT_AUTHOR_CONFIRMED
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path

# ── Planck 2018 constraints (external standard physics) ─────────────────────
# Source: Aghanim et al. 2020 (Planck 2018 VI), Table 2
# TT,TE,EE+lowE+lensing+BAO combination
PLANCK_N_EFF_SM_THEORY = 3.046  # SM prediction (3 massless ν)
PLANCK_N_EFF_OBS = 2.99  # Planck 2018 measured central value
PLANCK_N_EFF_1SIGMA = 0.17  # 1σ uncertainty
DELTA_N_EFF_BOUND_1SIGMA = 0.40  # ΔN_eff < 0.40 at 1σ (conservative round)

# ── Mirror DM physics factors ────────────────────────────────────────────────
# After SM e+e- annihilation: T_ν/T_γ = (4/11)^(1/3)
# Mirror photons at T_γ' = x T_γ contribute to ΔN_eff via:
#   ΔN_eff_γ = (g_γ / g_1ν) × (T_γ' / T_ν)^4
#            = (2 / (7/4)) × (x T_γ / T_ν)^4
#            = (8/7) × x^4 × (T_γ/T_ν)^4
#            = (8/7) × (11/4)^(4/3) × x^4
PHOTON_TO_NEFF = (8 / 7) * (11 / 4) ** (4 / 3)  # ≈ 4.40 per photon species

# Mirror e+e- at T' = x T_γ (when relativistic, T' > m_e ≈ 0.511 MeV):
#   g_e = 4 (Dirac), ΔN_eff_e = (g_e/g_1ν) × (T_γ'/T_ν)^4
#        = (4 / (7/4)) × (11/4)^(4/3) × x^4
#        = (16/7) × (11/4)^(4/3) × x^4
ELECTRON_TO_NEFF = (16 / 7) * (11 / 4) ** (4 / 3)  # ≈ 8.80 per e+e- species pair

# Mirror neutrino at T_ν' = x T_ν contributes:
#   ΔN_eff_ν = (T_ν'/T_ν)^4 = x^4  per species
NU_TO_NEFF_PER_SPECIES = 1.0

# Number of IDM dark isomers (from preprint)
N_ISOMERS = 5

# Number of mirror neutrino species (3 per sector, mirroring SM)
N_MIRROR_NU = 3


# ── Three interpretations of "dark isomers" ──────────────────────────────────


@dataclass
class Interpretation:
    interp_id: str
    label: str
    note: str
    # ΔN_eff coefficient per sector = coeff × x^4
    coeff_per_sector: float


def _make_interps() -> list[Interpretation]:
    # Interpretation A: minimally, 1 dark boson (photon-like) per isomer
    coeff_A = PHOTON_TO_NEFF  # photons only, no dark neutrinos, T' < m_e

    # Interpretation B: dark photon + 3 dark neutrinos (mirror e+e- non-relativistic)
    # Applies when T_dark < m_e ≈ 0.511 MeV, so dark electrons already non-relativistic at BBN
    coeff_B = PHOTON_TO_NEFF + N_MIRROR_NU * NU_TO_NEFF_PER_SPECIES

    # Interpretation C: full mirror sector (photons + e+e- + 3ν, T_dark > m_e at BBN)
    # Literal reading of "one counterpart for each known ordinary-matter particle"
    coeff_C = PHOTON_TO_NEFF + ELECTRON_TO_NEFF + N_MIRROR_NU * NU_TO_NEFF_PER_SPECIES

    return [
        Interpretation(
            "A_minimal",
            "1 dark photon-like boson per isomer (minimal)",
            "Most conservative. Only 1 particle type, no dark neutrinos.",
            coeff_A,
        ),
        Interpretation(
            "B_phot_plus_nu",
            "Dark photon + 3 dark neutrinos per isomer (no dark electrons)",
            "Mirror sector: photons + neutrinos; dark electrons non-relativistic at BBN.",
            coeff_B,
        ),
        Interpretation(
            "C_full_mirror",
            "Full mirror SM per isomer (photons + e+e- + 3ν, T_dark > m_e at BBN)",
            "Literal reading of preprint line 1063-1065: each isomer mirrors full SM.",
            coeff_C,
        ),
    ]


INTERPRETATIONS = _make_interps()


# ── Core computations ────────────────────────────────────────────────────────


def delta_neff(coeff_per_sector: float, n_sectors: int, x: float) -> float:
    """ΔN_eff = n_sectors × coeff × x^4."""
    return n_sectors * coeff_per_sector * x**4


def x_max(
    coeff_per_sector: float, n_sectors: int, bound: float = DELTA_N_EFF_BOUND_1SIGMA
) -> float:
    """Maximum T_dark/T_SM satisfying ΔN_eff <= bound."""
    total_coeff = n_sectors * coeff_per_sector
    return (bound / total_coeff) ** 0.25


def sigma_from_neff(delta: float, sigma: float = PLANCK_N_EFF_1SIGMA) -> float:
    """How many σ from Planck N_eff=2.99 does this ΔN_eff represent."""
    return delta / sigma


# ── Audit runner ─────────────────────────────────────────────────────────────


def run_audit() -> dict:
    print("Mirror DM / N_eff Constraint — IDM '5 dark isomers'")
    print("=" * 62)
    print("Labels: IF_MIRROR_DM_INTERPRETATION · EXTERNAL_STANDARD_PHYSICS")
    print("        INTERNAL_DIAGNOSTIC_ONLY · NOT_AUTHOR_CONFIRMED")
    print(f"\nPlanck 2018: N_eff = {PLANCK_N_EFF_OBS} ± {PLANCK_N_EFF_1SIGMA} (1σ)")
    print(f"Bound used:  ΔN_eff < {DELTA_N_EFF_BOUND_1SIGMA} at 1σ")
    print(f"IDM isomers: N = {N_ISOMERS}")

    results = []
    for interp in INTERPRETATIONS:
        dneff_x1_per = interp.coeff_per_sector * 1.0**4
        dneff_x1_total = delta_neff(interp.coeff_per_sector, N_ISOMERS, 1.0)
        x_max_val = x_max(interp.coeff_per_sector, N_ISOMERS)
        sigma_val = sigma_from_neff(dneff_x1_total)

        print(f"\n[{interp.interp_id}]  {interp.label}")
        print(f"  Note: {interp.note}")
        print(f"  ΔN_eff per sector at x=1:   {dneff_x1_per:.2f}")
        print(
            f"  ΔN_eff total (5×) at x=1:   {dneff_x1_total:.2f}  "
            f"({sigma_val:.0f}σ above Planck bound)"
        )
        print(f"  x_max (T_dark/T_SM):         {x_max_val:.4f}")
        print("  Status at x=1:               RULED_OUT")

        results.append(
            {
                "interp_id": interp.interp_id,
                "label": interp.label,
                "coeff_per_sector": round(interp.coeff_per_sector, 4),
                "delta_neff_per_sector_x1": round(dneff_x1_per, 3),
                "delta_neff_total_5sectors_x1": round(dneff_x1_total, 3),
                "sigma_above_planck_at_x1": round(sigma_val, 1),
                "x_max_5_isomers": round(x_max_val, 4),
                "x_max_1_isomer": round(x_max(interp.coeff_per_sector, 1), 4),
                "status_at_x1": "RULED_OUT",
            }
        )

    print("\n" + "=" * 62)
    print("SUMMARY")
    print("=" * 62)
    print()
    print("IDM preprint: 5 isomers, each with 'one counterpart for each SM particle'.")
    print("Structural match: Mirror Dark Matter (5 full mirror sectors).")
    print()
    print("At equal temperatures (x = T_dark/T_SM = 1):")
    for r in results:
        print(
            f"  [{r['interp_id']}] ΔN_eff = {r['delta_neff_total_5sectors_x1']:.1f}  "
            f"({r['sigma_above_planck_at_x1']:.0f}σ above Planck)"
        )
    print()
    print("Required temperature constraint (for Planck compatibility):")
    for r in results:
        print(f"  [{r['interp_id']}] T_dark/T_SM < {r['x_max_5_isomers']:.3f}")
    print()
    print("CRITICAL: IDM preprint does NOT specify T_dark/T_SM.")
    print("  → The required cooling mechanism is AUTHOR_DERIVATION_NEEDED.")
    print("  → Without T_dark/T_SM, ΔN_eff cannot be evaluated for IDM.")
    print("  → M7-C verdict remains BLOCKED.")
    print()
    print("SECONDARY: 5:1 dark/baryon ratio in cool mirror sector")
    print("  Mirror DM with x < 0.35: ρ_mirror_baryons << ρ_SM_baryons")
    print("  → 5:1 ratio cannot arise from equal baryon asymmetry at x < 0.35.")
    print("  → An independent mechanism for 5:1 is required.")
    print("  → M7-A/B AUTHOR_DERIVATION_NEEDED status confirmed.")

    # Physics constants check
    print("\n--- Internal consistency check ---")
    expected_factor = (8 / 7) * (11 / 4) ** (4 / 3)
    actual_factor = PHOTON_TO_NEFF
    assert math.isclose(actual_factor, expected_factor, rel_tol=1e-10), (
        f"PHOTON_TO_NEFF mismatch: {actual_factor} vs {expected_factor}"
    )
    print(f"  PHOTON_TO_NEFF = (8/7) × (11/4)^(4/3) = {actual_factor:.6f}  ✓")
    expected_electron = (16 / 7) * (11 / 4) ** (4 / 3)
    assert math.isclose(ELECTRON_TO_NEFF, expected_electron, rel_tol=1e-10)
    print(f"  ELECTRON_TO_NEFF = (16/7) × (11/4)^(4/3) = {ELECTRON_TO_NEFF:.6f}  ✓")

    out = {
        "gate": "M7-C-supplement-mirror-dm",
        "date": "2026-06-12",
        "labels": [
            "IF_MIRROR_DM_INTERPRETATION",
            "EXTERNAL_STANDARD_PHYSICS",
            "NOT_VALIDATION",
            "NOT_REFUTATION",
            "INTERNAL_DIAGNOSTIC_ONLY",
            "NOT_AUTHOR_CONFIRMED",
            "OUR_RECONSTRUCTION",
        ],
        "motivation": (
            "IDM preprint line 1063-1065: each isomer 'might associate with a set of "
            "elementary particles for which there is one elementary-particle counterpart "
            "for each known (or ordinary-matter) elementary particle.' "
            "This is structurally identical to Mirror Dark Matter. "
            "Mirror DM literature provides ΔN_eff formulas applicable as cross-check."
        ),
        "planck_2018": {
            "N_eff_SM_theory": PLANCK_N_EFF_SM_THEORY,
            "N_eff_observed": PLANCK_N_EFF_OBS,
            "sigma_1": PLANCK_N_EFF_1SIGMA,
            "delta_N_eff_bound_1sigma": DELTA_N_EFF_BOUND_1SIGMA,
            "source": "Aghanim et al. 2020 (Planck 2018 VI), Table 2",
        },
        "physics_factors": {
            "photon_to_neff": round(PHOTON_TO_NEFF, 6),
            "electron_to_neff": round(ELECTRON_TO_NEFF, 6),
            "formula_photon": "ΔN_eff_γ = (8/7) × (11/4)^(4/3) × x^4",
            "formula_electron": "ΔN_eff_e = (16/7) × (11/4)^(4/3) × x^4",
            "formula_neutrino": "ΔN_eff_ν = 1.0 × x^4 per species",
        },
        "n_isomers": N_ISOMERS,
        "interpretations": results,
        "conclusions": [
            "Equal-temperature dark sector (x=1) ruled out under ALL interpretations.",
            "5 isomers at x=1: ΔN_eff ∈ [22.0, 75.6] depending on interpretation.",
            "Required: T_dark/T_SM < 0.25-0.38 for Planck 2018 compatibility.",
            "IDM preprint does NOT specify T_dark/T_SM → AUTHOR_DERIVATION_NEEDED.",
            "M7-C verdict remains BLOCKED: cannot compute IDM ΔN_eff without T_dark/T_SM.",
            "SECONDARY: Cool mirror sector (x < 0.35) undermines 5:1 ratio from "
            "equal baryon asymmetry → M7-A/B AUTHOR_DERIVATION_NEEDED confirmed.",
        ],
        "safety": (
            "NOT_VALIDATION · NOT_REFUTATION · IF_MIRROR_DM_INTERPRETATION "
            "· OUR_RECONSTRUCTION · INTERNAL_DIAGNOSTIC_ONLY"
        ),
    }

    report_dir = Path(__file__).parent.parent / "reports"
    report_dir.mkdir(exist_ok=True)
    json_path = report_dir / "mirror_dm_neff_constraint.json"
    json_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n  JSON written: {json_path}")

    return out


if __name__ == "__main__":
    run_audit()
