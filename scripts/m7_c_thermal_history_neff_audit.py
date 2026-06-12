"""
M7-C: Thermal History / N_eff Blocker Audit

Audit whether IDM specifies enough dark-sector thermal history to compute
ΔN_eff and compare to BBN/CMB constraints.

Labels: M7_THERMAL_HISTORY_AUDIT · N_EFF_BLOCKER · NOT_VALIDATION · NOT_REFUTATION
Scope:  INTERNAL_DIAGNOSTIC_ONLY · NOT_AUTHOR_CONFIRMED
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

# ---------------------------------------------------------------------------
# Status enum
# ---------------------------------------------------------------------------


class IngredientStatus(str, Enum):  # noqa: UP042
    AUTHOR_DEFINED = "AUTHOR_DEFINED"  # explicitly given in preprint
    AUTHOR_HINTED = "AUTHOR_HINTED"  # implied but not quantified
    NOT_FOUND = "NOT_FOUND"  # searched, absent from preprint
    EXTERNAL_STANDARD_PHYSICS = "EXTERNAL_STANDARD_PHYSICS"  # external well-known
    OUR_RECONSTRUCTION = "OUR_RECONSTRUCTION"  # derived by us, not author-confirmed


# ---------------------------------------------------------------------------
# Required ingredients for ΔN_eff computation
# ---------------------------------------------------------------------------


@dataclass
class Ingredient:
    id: str
    description: str
    status: IngredientStatus
    evidence: str
    source_line: str | None = None
    note: str = ""


INGREDIENTS: list[Ingredient] = [
    Ingredient(
        id="I1",
        description="Number of relativistic dark species at BBN/recombination",
        status=IngredientStatus.NOT_FOUND,
        evidence="No statement in preprint about which dark particles are relativistic "
        "at T~MeV (BBN) or T~eV (recombination). Preprint line 1063 says each "
        "isomer 'might associate with' SM counterparts but gives no mass spectrum "
        "or thermal population statement.",
        source_line="preprint line 1063 (context only)",
        note="AUTHOR_DERIVATION_NEEDED",
    ),
    Ingredient(
        id="I2",
        description="Dark-to-visible temperature ratio T_dark/T_visible",
        status=IngredientStatus.NOT_FOUND,
        evidence="No T_dark defined anywhere in preprint or supplementary. "
        "No thermalization or entropy-injection mechanism described.",
        note="AUTHOR_DERIVATION_NEEDED",
    ),
    Ingredient(
        id="I3",
        description="Decoupling temperature of dark sector from SM bath",
        status=IngredientStatus.NOT_FOUND,
        evidence="No decoupling temperature mentioned. "
        "References to 'decoupling' in bibliography (lines 2568, 2620) "
        "are citations to other papers, not IDM statements.",
        source_line="preprint lines 2568, 2620 (bibliography only)",
        note="AUTHOR_DERIVATION_NEEDED",
    ),
    Ingredient(
        id="I4",
        description="Entropy-transfer history between dark and visible sector",
        status=IngredientStatus.NOT_FOUND,
        evidence="No entropy-transfer mechanism described. Preprint does not discuss "
        "dark-sector thermodynamics.",
        note="AUTHOR_DERIVATION_NEEDED",
    ),
    Ingredient(
        id="I5",
        description="Whether dark photons/gluons/neutrinos exist and are relativistic at BBN",
        status=IngredientStatus.AUTHOR_HINTED,
        evidence="Preprint line 1063-1065: 'Each one of the five dark-matter isomers might "
        "associate with a set of elementary particles for which there is one "
        "elementary-particle counterpart for each known (or ordinary-matter) "
        "elementary particle.' — implies dark photons/leptons/gluons may exist, "
        "but no mass, temperature, or relict density given.",
        source_line="preprint lines 1063-1065",
        note="AUTHOR_HINTED — existence implied, thermal properties absent",
    ),
    Ingredient(
        id="I6",
        description="Coupling/thermalization assumptions between dark and SM sectors",
        status=IngredientStatus.NOT_FOUND,
        evidence="No coupling constant or portal interaction described. "
        "IDM does not discuss how dark isomers were produced or whether they "
        "share a thermal bath with SM.",
        note="AUTHOR_DERIVATION_NEEDED",
    ),
    Ingredient(
        id="I7",
        description="Explicit calculation or bound for ΔN_eff",
        status=IngredientStatus.NOT_FOUND,
        evidence="No N_eff, ΔN_eff, or equivalent cosmological radiation density "
        "calculation found in preprint or supplementary. "
        "All 'Neff' grep hits in preprint are false positives ('ineffect').",
        note="AUTHOR_DERIVATION_NEEDED · NO_FORMULA_IN_SOURCE",
    ),
    Ingredient(
        id="I8",
        description="Standard ΔN_eff formula (external physics — for reference only)",
        status=IngredientStatus.EXTERNAL_STANDARD_PHYSICS,
        evidence="ΔN_eff = (4/7) × (g_D/2) × (T_dark/T_ν)^4  per extra bosonic d.o.f. "
        "(Kolb & Turner 1990; Cyburt et al. 2016 BBN review). "
        "Planck 2018: N_eff = 2.99 ± 0.17 (1σ). Extra ΔN_eff > 0.4 ruled out. "
        "This formula CANNOT be applied to IDM without I1-I6.",
        note="EXTERNAL_STANDARD_PHYSICS — cannot compute without IDM inputs I1-I6",
    ),
]


# ---------------------------------------------------------------------------
# Preprint scan
# ---------------------------------------------------------------------------

SEARCH_TERMS = [
    "N_eff",
    "Neff",
    "BBN",
    "Big Bang Nucleosynthesis",
    "thermal history",
    "decoupling",
    "T_dark",
    "dark temperature",
    "dark sector",
    "dark photon",
    "dark gluon",
    "dark neutrino",
    "entropy transfer",
    "radiation domination",
    "dark radiation",
    "relativistic dark",
]


def scan_source_files() -> dict[str, list[str]]:
    base = Path(__file__).parent.parent / "data" / "source_material"
    results: dict[str, list[str]] = {}
    for fname in [
        "buckholtz_preprints202511.0598.v6.md",
        "buckholtz_supplementary202511.0598.v6.md",
    ]:
        fpath = base / fname
        if not fpath.exists():
            results[fname] = ["FILE NOT FOUND"]
            continue
        text = fpath.read_text(encoding="utf-8")
        hits = []
        for i, line in enumerate(text.splitlines(), 1):
            for term in SEARCH_TERMS:
                if re.search(term, line, re.IGNORECASE):
                    hits.append(f"line {i}: [{term}] {line.strip()[:100]}")
                    break
        # Filter out known false positives ("ineffect", bibliography)
        real_hits = []
        for h in hits:
            stripped = h.lower()
            if "ineffect" in stripped:
                continue  # "ineffect" not "N_eff"
            real_hits.append(h)
        results[fname] = real_hits if real_hits else ["NO RELEVANT HITS"]
    return results


# ---------------------------------------------------------------------------
# Computability assessment
# ---------------------------------------------------------------------------


def assess_computability(ingredients: list[Ingredient]) -> dict[str, object]:
    required = [i for i in ingredients if i.id not in ("I8",)]
    found = [
        i
        for i in required
        if i.status in (IngredientStatus.AUTHOR_DEFINED, IngredientStatus.AUTHOR_HINTED)
    ]
    not_found = [i for i in required if i.status == IngredientStatus.NOT_FOUND]
    missing_required = list(not_found)

    computable = len(missing_required) == 0
    return {
        "computable": computable,
        "required_count": len(required),
        "found_count": len(found),
        "not_found_count": len(not_found),
        "missing_required": [i.id for i in missing_required],
        "verdict": "BLOCKED" if not computable else "PASS",
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def run_audit() -> dict[str, object]:
    print("M7-C Thermal History / N_eff Blocker Audit")
    print("=" * 60)
    print("Labels: M7_THERMAL_HISTORY_AUDIT · N_EFF_BLOCKER")
    print("Scope:  INTERNAL_DIAGNOSTIC_ONLY · NOT_VALIDATION · NOT_REFUTATION")
    print()

    # Scan source files
    scan_results = scan_source_files()
    print("--- Source file scan ---")
    for fname, hits in scan_results.items():
        print(f"\n{fname}:")
        for h in hits:
            print(f"  {h}")

    # Ingredient checklist
    print("\n--- Required ingredient checklist ---")
    for ing in INGREDIENTS:
        marker = (
            "✓"
            if ing.status
            in (
                IngredientStatus.AUTHOR_DEFINED,
                IngredientStatus.AUTHOR_HINTED,
                IngredientStatus.EXTERNAL_STANDARD_PHYSICS,
            )
            else "✗"
        )
        print(f"  [{marker}] {ing.id}: {ing.description}")
        print(f"       Status: {ing.status.value}")
        if ing.note:
            print(f"       Note:   {ing.note}")

    # Computability
    comp = assess_computability(INGREDIENTS)
    print("\n--- Computability assessment ---")
    print(f"  Required ingredients:  {comp['required_count']}")
    print(f"  Found/hinted:          {comp['found_count']}")
    print(f"  Missing:               {comp['not_found_count']}")
    print(f"  Missing IDs:           {comp['missing_required']}")
    print(f"  ΔN_eff computable:     {comp['computable']}")
    print(f"  Verdict:               {comp['verdict']}")

    # N_eff reference formula
    print("\n--- Reference formula (EXTERNAL_STANDARD_PHYSICS, cannot apply to IDM) ---")
    print("  ΔN_eff = (4/7) × (g_D/2) × (T_dark/T_ν)^4  [per extra bosonic d.o.f.]")
    print("  Planck 2018 bound: N_eff = 2.99 ± 0.17 (ΔN_eff < 0.4 at 1σ)")
    print("  Cannot compute: T_dark, g_D, T_dark/T_ν all NOT_FOUND in IDM preprint.")

    result = {
        "gate": "M7-C",
        "date": "2026-06-12",
        "labels": [
            "M7_THERMAL_HISTORY_AUDIT",
            "N_EFF_BLOCKER",
            "NOT_VALIDATION",
            "NOT_REFUTATION",
            "INTERNAL_DIAGNOSTIC_ONLY",
            "AUTHOR_DERIVATION_NEEDED",
        ],
        "verdict": comp["verdict"],
        "computability": comp,
        "ingredients": [
            {
                "id": i.id,
                "description": i.description,
                "status": i.status.value,
                "note": i.note,
                "source_line": i.source_line,
            }
            for i in INGREDIENTS
        ],
        "source_scan": scan_results,
        "standard_formula": {
            "formula": "ΔN_eff = (4/7) × (g_D/2) × (T_dark/T_ν)^4",
            "planck_bound": "N_eff = 2.99 ± 0.17 (Planck 2018); ΔN_eff < 0.4 at 1σ",
            "applicable_to_IDM": False,
            "reason": "T_dark, g_D, T_dark/T_ν all NOT_FOUND in preprint",
        },
        "questions_for_author": [
            "Q_TH1: Were the five dark isomers ever thermally populated in the early universe?",
            "Q_TH2: What is T_dark/T_visible for each dark sector?",
            "Q_TH3: At what temperature did the dark sector decouple from the SM bath?",
            "Q_TH4: Which dark-sector particles are relativistic at BBN (T~MeV) and at recombination (T~eV)?",
            "Q_TH5: What ΔN_eff does IDM predict, and how does it compare to Planck 2018?",
        ],
        "safety_footer": (
            "NOT_VALIDATION · NOT_REFUTATION · INTERNAL_DIAGNOSTIC_ONLY "
            "· NOT_AUTHOR_CONFIRMED · M7_THERMAL_HISTORY_AUDIT"
        ),
    }

    # Write JSON
    report_dir = Path(__file__).parent.parent / "reports"
    report_dir.mkdir(exist_ok=True)
    json_path = report_dir / "m7_c_thermal_history_neff_audit.json"
    json_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n  JSON written: {json_path}")

    return result


if __name__ == "__main__":
    run_audit()
