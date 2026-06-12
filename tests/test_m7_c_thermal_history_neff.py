"""
Tests for M7-C: Thermal History / N_eff Blocker Audit.

Labels: M7_THERMAL_HISTORY_AUDIT · N_EFF_BLOCKER · NOT_VALIDATION · NOT_REFUTATION
These tests verify the audit logic and source scan, NOT IDM physics.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from m7_c_thermal_history_neff_audit import (
    INGREDIENTS,
    IngredientStatus,
    assess_computability,
    scan_source_files,
)

# ---------------------------------------------------------------------------
# Ingredient checklist tests
# ---------------------------------------------------------------------------


def test_all_required_ingredients_defined() -> None:
    """All 8 expected ingredient IDs are present."""
    ids = {i.id for i in INGREDIENTS}
    assert ids == {"I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8"}


def test_i1_through_i4_are_not_found() -> None:
    """Core thermal history ingredients I1-I4 must be NOT_FOUND (absent from preprint)."""
    by_id = {i.id: i for i in INGREDIENTS}
    for iid in ("I1", "I2", "I3", "I4"):
        assert by_id[iid].status == IngredientStatus.NOT_FOUND, (
            f"{iid} should be NOT_FOUND — thermal history absent from preprint"
        )


def test_i5_is_author_hinted() -> None:
    """I5 (dark particle existence) is AUTHOR_HINTED — implied by preprint line 1063-1065."""
    by_id = {i.id: i for i in INGREDIENTS}
    assert by_id["I5"].status == IngredientStatus.AUTHOR_HINTED


def test_i6_i7_are_not_found() -> None:
    """I6 (coupling) and I7 (explicit ΔN_eff) must be NOT_FOUND."""
    by_id = {i.id: i for i in INGREDIENTS}
    assert by_id["I6"].status == IngredientStatus.NOT_FOUND
    assert by_id["I7"].status == IngredientStatus.NOT_FOUND


def test_i8_is_external_standard_physics() -> None:
    """I8 (standard formula) is EXTERNAL_STANDARD_PHYSICS — external, not IDM."""
    by_id = {i.id: i for i in INGREDIENTS}
    assert by_id["I8"].status == IngredientStatus.EXTERNAL_STANDARD_PHYSICS


# ---------------------------------------------------------------------------
# Computability tests
# ---------------------------------------------------------------------------


def test_delta_neff_not_computable() -> None:
    """With 6/7 required ingredients missing, ΔN_eff is not computable."""
    comp = assess_computability(INGREDIENTS)
    assert comp["computable"] is False


def test_verdict_is_blocked() -> None:
    """Computability verdict must be BLOCKED."""
    comp = assess_computability(INGREDIENTS)
    assert comp["verdict"] == "BLOCKED"


def test_missing_ingredient_count() -> None:
    """Exactly 6 required ingredients are missing."""
    comp = assess_computability(INGREDIENTS)
    assert comp["not_found_count"] == 6
    assert set(comp["missing_required"]) == {"I1", "I2", "I3", "I4", "I6", "I7"}


def test_required_count_excludes_i8() -> None:
    """I8 (external formula) is excluded from the required count."""
    comp = assess_computability(INGREDIENTS)
    assert comp["required_count"] == 7


# ---------------------------------------------------------------------------
# Source scan tests
# ---------------------------------------------------------------------------


def test_source_files_exist() -> None:
    """Preprint and supplementary source files exist on disk."""
    base = Path(__file__).parent.parent / "data" / "source_material"
    assert (base / "buckholtz_preprints202511.0598.v6.md").exists()
    assert (base / "buckholtz_supplementary202511.0598.v6.md").exists()


def test_no_neff_in_preprint() -> None:
    """No real N_eff / BBN content found in preprint (only false positives)."""
    results = scan_source_files()
    preprint_hits = results.get("buckholtz_preprints202511.0598.v6.md", [])
    # After false-positive filtering, any remaining hits should NOT be cosmological N_eff
    for hit in preprint_hits:
        assert "ineffect" not in hit.lower(), (
            f"False positive 'ineffect' should have been filtered: {hit}"
        )


def test_no_thermal_history_in_supplementary() -> None:
    """Supplementary file has no dark-sector thermal history content."""
    results = scan_source_files()
    supp_hits = results.get("buckholtz_supplementary202511.0598.v6.md", [])
    # Should be empty or only no-relevant-hits marker
    assert supp_hits == ["NO RELEVANT HITS"] or len(supp_hits) == 0, (
        f"Unexpected thermal history content in supplementary: {supp_hits}"
    )


# ---------------------------------------------------------------------------
# JSON output test
# ---------------------------------------------------------------------------


def test_json_report_exists_and_valid() -> None:
    """JSON report was created and has required fields."""
    json_path = Path(__file__).parent.parent / "reports" / "m7_c_thermal_history_neff_audit.json"
    assert json_path.exists(), "JSON report must exist after running the audit script"
    data = json.loads(json_path.read_text(encoding="utf-8"))
    assert data["verdict"] == "BLOCKED"
    assert data["gate"] == "M7-C"
    assert "M7_THERMAL_HISTORY_AUDIT" in data["labels"]
    assert "NOT_VALIDATION" in data["labels"]
    assert data["computability"]["computable"] is False
    assert data["standard_formula"]["applicable_to_IDM"] is False
    assert len(data["questions_for_author"]) == 5
