"""
Tests for scripts/asre_required_schedule.py — ASRE gate.

Safety: ASRE · OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED
        NOT_VALIDATION · NOT_REFUTATION · AUTHOR_SCHEDULE_NEEDED
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.asre_required_schedule import (
    Z_DATA,
    compute_eps_all,
    compute_required_bridge,
    normalize_at_z040,
    run_asre,
)

# ── Fixtures ──────────────────────────────────────────────────────────────────


@pytest.fixture(scope="module")
def result() -> dict:
    return run_asre()


@pytest.fixture(scope="module")
def eps_norm() -> list[float]:
    return normalize_at_z040(compute_eps_all())


@pytest.fixture(scope="module")
def rb_norm() -> list[float]:
    return normalize_at_z040(compute_required_bridge())


# ── Section 1: ε(z) structure ────────────────────────────────────────────────


def test_eps_peak_at_z040(result: dict) -> None:
    """ε(z) fractional excess must peak at z=0.40 (INSIGHT-1)."""
    assert result["eps_peak_z"] == pytest.approx(0.40)


def test_eps_is_non_monotone(result: dict) -> None:
    """ε(z) has 3+ sign changes — confirmed non-monotone."""
    assert result["eps_is_non_monotone"] is True


def test_eps_11_values(eps_norm: list[float]) -> None:
    """All 11 Table A1 redshifts produce valid ε values."""
    assert len(eps_norm) == 11
    assert all(e > 0.0 for e in eps_norm)


def test_eps_normalized_at_z040(eps_norm: list[float]) -> None:
    """ε(z=0.40) = 1.0 after normalization."""
    i_ref = Z_DATA.index(0.40)
    assert eps_norm[i_ref] == pytest.approx(1.0, abs=1e-9)


# ── Section 2: required_bridge peaks at z=8.50 ────────────────────────────────


def test_required_bridge_peak_at_z850(result: dict) -> None:
    """required_bridge = ε × H² peaks at z=8.50 — H² growth dominates at high z."""
    assert result["required_bridge_peak_z"] == pytest.approx(8.50)


def test_two_targets_differ(result: dict) -> None:
    """ε_peak_z (fractional) != required_bridge_peak_z (absolute) — two distinct targets."""
    assert result["eps_peak_z"] != result["required_bridge_peak_z"]


def test_required_bridge_is_non_monotone(result: dict) -> None:
    """required_bridge(z) is non-monotone — has peak structure inherited from ε."""
    assert result["required_bridge_is_non_monotone"] is True


# ── Section 3: Degeneracy families ───────────────────────────────────────────


def test_family_a_k_A_peak_at_z040(result: dict) -> None:
    """Family A (D_eff=D_H): k_A ∝ ε(z), peaks at z=0.40."""
    assert result["degenerate_families"]["family_A"]["k_A_peak_z"] == pytest.approx(0.40)


def test_family_a_k_A_non_monotone(result: dict) -> None:
    """Family A k_A is non-monotone — inherits ε structure."""
    assert result["degenerate_families"]["family_A"]["k_A_is_monotone"] is False


def test_family_b_k_A_peak_at_z040(result: dict) -> None:
    """Family B (D_eff=r_vir): k_A ∝ ε × H^(2/3), peaks at z=0.40."""
    assert result["degenerate_families"]["family_B"]["k_A_peak_z"] == pytest.approx(0.40)


def test_family_b_k_A_non_monotone(result: dict) -> None:
    """Family B k_A is non-monotone — r_vir cannot suppress the ε peak."""
    assert result["degenerate_families"]["family_B"]["k_A_is_monotone"] is False


def test_family_c_D_eff_non_monotone(result: dict) -> None:
    """Family C (k_A=const): D_eff is non-monotone — inversely proportional to bridge."""
    assert result["degenerate_families"]["family_C"]["D_eff_is_monotone"] is False


def test_family_c_D_eff_min_at_z850(result: dict) -> None:
    """Family C D_eff minimum where required_bridge is maximum — at z=8.50."""
    assert result["degenerate_families"]["family_C"]["D_eff_min_at_z"] == pytest.approx(8.50)


# ── Section 4: Virial anti-correlation ────────────────────────────────────────


def test_virial_anti_correlated_to_eps(result: dict) -> None:
    """Virial k_A ∝ H^(4/3) must be anti-correlated with ε(z) — M8-D THEOREM."""
    r = result["virial_comparison"]["pearson_r_virial_vs_eps"]
    assert r < 0.0, f"Expected r < 0, got {r}"


def test_virial_confirms_m8d_theorem(result: dict) -> None:
    """Pearson r(virial, eps) < -0.3 — confirms M8-D INSIGHT-3 (theorem, not marginal)."""
    r = result["virial_comparison"]["pearson_r_virial_vs_eps"]
    assert r < -0.3, f"Expected r < -0.3, got {r}"


def test_virial_positively_correlated_to_abs_bridge(result: dict) -> None:
    """Virial vs absolute bridge is positively correlated — both grow with H(z)."""
    r = result["virial_comparison"]["pearson_r_virial_vs_abs_bridge"]
    assert r > 0.5, f"Expected r > 0.5 (both grow with z), got {r}"


def test_anti_correlated_flag_is_true(result: dict) -> None:
    """anti_correlated_to_eps flag must be True."""
    assert result["virial_comparison"]["anti_correlated_to_eps"] is True


def test_confirms_m8d_theorem_flag_is_true(result: dict) -> None:
    """confirms_m8d_theorem flag must be True."""
    assert result["virial_comparison"]["confirms_m8d_theorem"] is True


# ── Section 5: Degeneracy documentation ──────────────────────────────────────


def test_degeneracy_not_determinable_list_present(result: dict) -> None:
    """Degeneracy analysis must explicitly list what cannot be determined."""
    not_det = result["degeneracy_analysis"]["not_determinable"]
    assert isinstance(not_det, list)
    assert len(not_det) >= 3, "Expected at least 3 undeterminable quantities documented"


def test_degeneracy_virial_excluded_flag(result: dict) -> None:
    """Virial k_A explicitly excluded from valid degeneracy family."""
    assert result["degeneracy_analysis"]["virial_k_A_excluded"] is True


def test_degeneracy_minimum_parameters(result: dict) -> None:
    """Minimum 2 parameters needed for a valid bridge — documented."""
    assert result["degeneracy_analysis"]["minimum_parameters"] >= 2


# ── Section 6: Verdict ────────────────────────────────────────────────────────


def test_verdict_partial(result: dict) -> None:
    """Overall verdict must be PARTIAL — bridge shape extracted, degeneracy documented."""
    assert result["overall_verdict"] == "PARTIAL"


def test_verdict_not_pass(result: dict) -> None:
    """Verdict is NOT PASS — unique (k_A, D_eff) pair still requires Q1+Q2."""
    assert result["overall_verdict"] != "PASS"


# ── Section 7: Safety labels ──────────────────────────────────────────────────

REQUIRED_LABELS = [
    "ASRE",
    "AUTHOR_SCHEDULE_REVERSE_ENGINEERING",
    "OUR_RECONSTRUCTION",
    "NOT_AUTHOR_CONFIRMED",
    "NOT_VALIDATION",
    "NOT_REFUTATION",
    "AUTHOR_SCHEDULE_NEEDED",
    "<HYPOTHESIS>",
]


@pytest.mark.parametrize("label", REQUIRED_LABELS)
def test_safety_label_present(result: dict, label: str) -> None:
    """Each required safety label must be in the result labels list."""
    assert label in result["labels"], f"Missing required safety label: {label}"


# ── Section 8: Physics flags ──────────────────────────────────────────────────


def test_no_mcmc_flag(result: dict) -> None:
    """no_MCMC flag must be True — MCMC remains BLOCKED."""
    assert result["physics_notes"]["no_MCMC"] is True


def test_no_flrw_fitting_flag(result: dict) -> None:
    """no_FLRW_fitting flag — bridge extracted without FLRW H(z) parameter fitting."""
    assert result["physics_notes"]["no_FLRW_fitting"] is True


def test_no_tableA1_powerlaw_fit_flag(result: dict) -> None:
    """no_TableA1_powerlaw_fit — required_bridge shape comes from Table A1 directly."""
    assert result["physics_notes"]["no_TableA1_powerlaw_fit"] is True


def test_degeneracy_documented_flag(result: dict) -> None:
    """degeneracy_documented flag must be True."""
    assert result["physics_notes"]["degeneracy_documented"] is True


# ── Section 9: JSON report written ───────────────────────────────────────────


def test_report_json_written() -> None:
    """reports/asre_required_schedule.json must exist after run_asre()."""
    repo_root = Path(__file__).parent.parent
    report_path = repo_root / "reports" / "asre_required_schedule.json"
    assert report_path.exists(), f"Report not found at {report_path}"


def test_report_json_valid() -> None:
    """JSON report must be parseable and contain 'overall_verdict'."""
    repo_root = Path(__file__).parent.parent
    report_path = repo_root / "reports" / "asre_required_schedule.json"
    if not report_path.exists():
        pytest.skip("Report not yet generated")
    data = json.loads(report_path.read_text(encoding="utf-8"))
    assert "overall_verdict" in data


def test_report_json_verdict_partial() -> None:
    """JSON report verdict must be PARTIAL."""
    repo_root = Path(__file__).parent.parent
    report_path = repo_root / "reports" / "asre_required_schedule.json"
    if not report_path.exists():
        pytest.skip("Report not yet generated")
    data = json.loads(report_path.read_text(encoding="utf-8"))
    assert data["overall_verdict"] == "PARTIAL"


# ── Section 10: Gate metadata ─────────────────────────────────────────────────


def test_gate_name(result: dict) -> None:
    """Gate identifier must match expected name."""
    assert result["gate"] == "ASRE-required-schedule"


def test_conclusions_non_empty(result: dict) -> None:
    """Conclusions list must be non-empty (qualitative summary present)."""
    assert isinstance(result["conclusions"], list)
    assert len(result["conclusions"]) >= 5


def test_conclusions_contain_degeneracy_note(result: dict) -> None:
    """At least one conclusion must mention degeneracy."""
    texts = " ".join(result["conclusions"]).lower()
    assert "degeneracy" in texts, "Degeneracy not mentioned in conclusions"


def test_conclusions_contain_author_schedule_needed(result: dict) -> None:
    """At least one conclusion must reference AUTHOR_SCHEDULE_NEEDED."""
    texts = " ".join(result["conclusions"])
    assert "AUTHOR_SCHEDULE_NEEDED" in texts
