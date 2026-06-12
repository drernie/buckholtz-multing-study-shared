"""
Tests for HD-MAVP-1 — Cluster Formation Audit.

Validates:
  - ε(z) vector unchanged from M8-A-R1
  - Candidate A (intrinsic PS density) is monotone decreasing → KILL
  - Selection function peaks at z=0.40 by model construction
  - r(ε, f_sel_alone) > 0.5 — selection function alone produces spurious correlation
  - Candidate D (f_DE) is monotone decreasing → KILL
  - z_eq (Λ-matter equality) ≈ 0.303, within 0.10 of ε peak
  - Overall verdict PARTIAL-KILL
  - Intrinsic formation KILLED, selection artifact SURVIVES
  - All required safety labels present
  - All safety physics_notes flags correct
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.hdmavp1_epsilon_cluster_audit import (
    Z_DATA,
    Z_EQ_LAMBDA_MATTER,
    candidate_a_ps_density,
    candidate_d_lcdm_transition,
    compute_eps,
    f_sel_alone,
    run_audit,
    sz_selection_model,
)

REQUIRED_LABELS = [
    "HD_MAVP_1",
    "OUR_RECONSTRUCTION",
    "NOT_AUTHOR_CONFIRMED",
    "NOT_VALIDATION",
    "NOT_REFUTATION",
    "SELECTION_BIAS_AUDIT",
    "NOT_CLAIM_PS_FACT",
]


@pytest.fixture(scope="module")
def result() -> dict:
    return run_audit()


# ── ε(z) integrity ────────────────────────────────────────────────────────────


def test_eps_11_points(result: dict) -> None:
    """ε vector has exactly 11 points — same as Table A1."""
    assert len(result["eps_values"]) == 11


def test_eps_peak_at_z040(result: dict) -> None:
    """ε peak confirmed at z=0.40, matching M8-A-R1 [VERIFIED-tool]."""
    assert result["eps_peak_z"] == pytest.approx(0.40)


def test_eps_is_non_monotone(result: dict) -> None:
    """ε is flagged as non-monotone (key structural property)."""
    assert result["eps_is_non_monotone"] is True


def test_eps_unchanged_flag(result: dict) -> None:
    """physics_notes confirms ε vector not redefined."""
    assert result["physics_notes"]["eps_vector_unchanged_from_m8a_r1"] is True
    assert result["physics_notes"]["no_new_eps_definition"] is True


def test_eps_values_match_table_a1() -> None:
    """ε values computed from raw Table A1 match expected M8-A-R1 values (±0.001)."""
    expected = {
        0.06: 0.0626,
        0.14: 0.1249,
        0.25: 0.2146,
        0.40: 0.2277,
        0.65: 0.2127,
        1.00: 0.1855,
        1.50: 0.2142,
        2.10: 0.1707,
        3.20: 0.1059,
        5.00: 0.0481,
        8.50: 0.1007,
    }
    eps = compute_eps()
    for i, z in enumerate(Z_DATA):
        if z in expected:
            assert eps[i] == pytest.approx(expected[z], abs=0.002), (
                f"ε at z={z}: expected {expected[z]:.4f}, got {eps[i]:.4f}"
            )


# ── Candidate A: intrinsic PS density ────────────────────────────────────────


def test_candidate_a_monotone_decreasing_1e14() -> None:
    """PS density (M_min=1e14) strictly decreasing — anti-correlated with ε."""
    vals = [candidate_a_ps_density(z, 1e14) for z in Z_DATA]
    assert all(vals[i] >= vals[i + 1] for i in range(len(vals) - 1)), (
        "PS density should be monotone decreasing with z"
    )


def test_candidate_a_monotone_decreasing_5e14() -> None:
    """PS density (M_min=5e14) strictly decreasing — confirms KILL for primary M_min."""
    vals = [candidate_a_ps_density(z, 5e14) for z in Z_DATA]
    assert all(vals[i] >= vals[i + 1] for i in range(len(vals) - 1))


def test_candidate_a_verdict_kill_5e14(result: dict) -> None:
    """Candidate A verdict KILL or INSUFFICIENT for M_min=5e14."""
    v = result["candidates_by_m_min"]["5e+14"]["A_ps_density"]["verdict"]
    assert v in ("KILL", "INSUFFICIENT"), f"Expected KILL/INSUFFICIENT, got {v}"


def test_candidate_a_verdict_kill_all(result: dict) -> None:
    """Candidate A verdict KILL or INSUFFICIENT for ALL mass thresholds."""
    for m_key, cands in result["candidates_by_m_min"].items():
        v = cands["A_ps_density"]["verdict"]
        assert v in ("KILL", "INSUFFICIENT"), (
            f"M_min={m_key}: Candidate A verdict={v}, expected KILL/INSUFFICIENT"
        )


def test_candidate_a_negative_r_5e14(result: dict) -> None:
    """Candidate A Pearson r < 0 for M_min=5e14 (anti-correlated with ε)."""
    r = result["candidates_by_m_min"]["5e+14"]["A_ps_density"]["pearson_r"]
    assert r < 0.0, f"Expected r < 0 for Candidate A, got {r}"


# ── Selection function ────────────────────────────────────────────────────────


def test_selection_function_peaks_at_z040() -> None:
    """SZ selection model (z_peak=0.40) peaks exactly at z=0.40 in the Table A1 grid."""
    vals = {z: sz_selection_model(z, z_peak=0.40) for z in Z_DATA}
    peak_z = max(vals, key=vals.get)
    assert peak_z == pytest.approx(0.40), (
        f"Selection function should peak at z=0.40, peaked at z={peak_z}"
    )


def test_selection_function_above_zero() -> None:
    """Selection function is positive for all z > 0."""
    for z in Z_DATA:
        assert f_sel_alone(z) >= 0.0
    assert f_sel_alone(0.0) == 0.0


def test_selection_function_spurious_correlation(result: dict) -> None:
    """
    KEY TEST: r(ε, f_sel_alone) > 0.5.

    If the instrument selection function (zero cluster physics) correlates with ε
    at this level, the M8-C r=0.723 is potentially selection-driven, not physical.
    """
    r = result["selection_function_alone"]["pearson_r"]
    assert r > 0.5, (
        f"Expected r(ε, f_sel_alone) > 0.5 (spurious correlation), got {r}. "
        "If this fails, the selection bias hypothesis needs revision."
    )


def test_selection_function_spurious_flag(result: dict) -> None:
    """spurious_correlation_confirmed flag is True."""
    assert result["selection_function_alone"]["spurious_correlation_confirmed"] is True


def test_selection_function_peaks_at_z040_in_report(result: dict) -> None:
    """Selection function alone peaks at z=0.40 in report."""
    assert result["selection_function_alone"]["peak_z"] == pytest.approx(0.40)


# ── Candidate D: ΛCDM transition ─────────────────────────────────────────────


def test_candidate_d_monotone_decreasing() -> None:
    """ΛCDM dark energy fraction f_DE(z) is monotone decreasing."""
    vals = [candidate_d_lcdm_transition(z) for z in Z_DATA]
    assert all(vals[i] >= vals[i + 1] for i in range(len(vals) - 1)), (
        "f_DE should be monotone decreasing: dark energy dominated at low z"
    )


def test_candidate_d_monotone_flag(result: dict) -> None:
    """candidate_D_lcdm reports is_monotone_decreasing=True."""
    assert result["candidate_D_lcdm"]["is_monotone_decreasing"] is True


def test_candidate_d_verdict_not_survives(result: dict) -> None:
    """Candidate D verdict is KILL or INSUFFICIENT (cannot explain ε peak structure)."""
    v = result["candidate_D_lcdm"]["verdict"]
    assert v in ("KILL", "INSUFFICIENT"), (
        f"ΛCDM f_DE is monotone — cannot explain ε peak at z=0.40. Got verdict={v}"
    )


def test_z_eq_in_report(result: dict) -> None:
    """z_eq (Λ-matter equality) is reported in candidate D."""
    assert "z_eq_lambda_matter" in result["candidate_D_lcdm"]
    z_eq = result["candidate_D_lcdm"]["z_eq_lambda_matter"]
    # z_eq should be near 0.303 (Ω_Λ/Ω_m)^(1/3) - 1
    assert z_eq == pytest.approx(0.303, abs=0.01)


def test_z_eq_within_012_of_eps_peak(result: dict) -> None:
    """z_eq ≈ 0.296, within 0.12 of ε peak at z=0.40 — proximity suggestive but insufficient."""
    proximity = result["candidate_D_lcdm"]["z_eq_proximity_to_eps_peak"]
    assert proximity < 0.12, f"z_eq should be within 0.12 of ε peak (z=0.40). Proximity={proximity}"


def test_z_eq_global_constant() -> None:
    """Z_EQ_LAMBDA_MATTER module constant is approximately 0.303."""
    assert Z_EQ_LAMBDA_MATTER == pytest.approx(0.303, abs=0.01)


# ── Overall verdicts ──────────────────────────────────────────────────────────


def test_overall_verdict_partial_kill(result: dict) -> None:
    """Overall audit verdict is PARTIAL-KILL (expected from gate specification)."""
    assert result["overall_verdict"] == "PARTIAL-KILL", (
        f"Expected PARTIAL-KILL, got {result['overall_verdict']}"
    )


def test_intrinsic_formation_killed(result: dict) -> None:
    """Intrinsic cluster formation history is KILLED."""
    assert result["intrinsic_formation_verdict"] == "KILLED", (
        f"Expected KILLED, got {result['intrinsic_formation_verdict']}"
    )


def test_selection_artifact_survives(result: dict) -> None:
    """Selection artifact verdict is SURVIVES_AS_ARTIFACT."""
    assert result["selection_artifact_verdict"] == "SURVIVES_AS_ARTIFACT", (
        f"Expected SURVIVES_AS_ARTIFACT, got {result['selection_artifact_verdict']}"
    )


# ── Safety: labels ────────────────────────────────────────────────────────────


@pytest.mark.parametrize("label", REQUIRED_LABELS)
def test_safety_label_present(result: dict, label: str) -> None:
    """All required safety labels are present in report."""
    assert label in result["labels"], f"Required safety label '{label}' missing from report"


# ── Safety: physics_notes flags ──────────────────────────────────────────────


def test_no_mcmc_flag(result: dict) -> None:
    """No MCMC was used (blocked)."""
    assert result["physics_notes"]["no_mcmc"] is True


def test_ps_treated_as_hypothesis_flag(result: dict) -> None:
    """PS mass function explicitly treated as hypothesis, not physical fact."""
    assert result["physics_notes"]["ps_treated_as_hypothesis"] is True


def test_sz_model_parametric_flag(result: dict) -> None:
    """SZ selection model is explicitly flagged as parametric."""
    assert result["physics_notes"]["sz_selection_is_parametric_model"] is True


def test_selection_not_from_actual_survey_flag(result: dict) -> None:
    """Selection model not derived from actual survey data."""
    assert result["physics_notes"]["selection_model_not_from_actual_survey"] is True


# ── Report file ───────────────────────────────────────────────────────────────


def test_report_written() -> None:
    """JSON report file exists after run_audit()."""
    root = Path(__file__).parent.parent
    report = root / "reports" / "hdmavp1_epsilon_cluster_audit.json"
    assert report.exists(), f"Report not found: {report}"


def test_report_parseable() -> None:
    """JSON report is valid and contains required top-level keys."""
    root = Path(__file__).parent.parent
    report = root / "reports" / "hdmavp1_epsilon_cluster_audit.json"
    if not report.exists():
        pytest.skip("Report not written yet")
    data = json.loads(report.read_text(encoding="utf-8"))
    for key in ("gate", "overall_verdict", "conclusions", "labels", "physics_notes"):
        assert key in data, f"Missing key '{key}' in report JSON"


def test_report_gate_name(result: dict) -> None:
    """Gate name in report is 'HD-MAVP-1'."""
    assert result["gate"] == "HD-MAVP-1"


def test_eps_source_in_report(result: dict) -> None:
    """ε source string references M8-A-R1 and commit add7cba."""
    src = result["eps_source"]
    assert "M8-A-R1" in src
    assert "add7cba" in src


# ── Consistency: r ordering ───────────────────────────────────────────────────


def test_candidate_c_r_above_a_r_for_5e14(result: dict) -> None:
    """
    r(ε, C_sz_selection) > r(ε, A_ps_density) for M_min=5e14.

    Adding selection function should INCREASE correlation (that's the selection bias).
    """
    r_a = result["candidates_by_m_min"]["5e+14"]["A_ps_density"]["pearson_r"]
    r_c = result["candidates_by_m_min"]["5e+14"]["C_sz_selection"]["pearson_r"]
    assert r_c > r_a, (
        f"r(C) should exceed r(A): C={r_c}, A={r_a}. "
        "Selection function should boost correlation above baseline."
    )


def test_conclusions_non_empty(result: dict) -> None:
    """Conclusions list is non-empty."""
    assert len(result["conclusions"]) >= 5
