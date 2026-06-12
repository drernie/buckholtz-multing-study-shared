"""Tests for BETA-1 controlled replication audit.

Coverage:
  - spread() computation and edge cases
  - verdict_from_spreads() all 5 outcomes
  - BETA-0 reference baseline (must show DIVERGE)
  - load_responses() file parsing and FILL_IN skipping
  - run_audit() end-to-end with mock data
  - Safety label enforcement
  - Report JSON written correctly
"""

import csv
import json
import math
from pathlib import Path

import pytest

from scripts.beta1_controlled_replication import (
    BETA0_REFERENCE,
    CONVERGENCE_THRESHOLD,
    MIN_SERVICES_FOR_VERDICT,
    SAFETY_LABELS,
    _beta0_analysis,
    load_responses,
    run_audit,
    spread,
    verdict_from_spreads,
)

# ---------------------------------------------------------------------------
# spread()
# ---------------------------------------------------------------------------


def test_spread_basic_ratio():
    assert spread([1.0, 2.0]) == pytest.approx(2.0)


def test_spread_identical_values():
    assert spread([3.5, 3.5, 3.5]) == pytest.approx(1.0)


def test_spread_three_values():
    # max/min = 4.5 / 0.78 ≈ 5.769
    result = spread([4.5, 4.25, 0.78])
    assert result == pytest.approx(4.5 / 0.78, rel=1e-4)


def test_spread_single_value_returns_inf():
    assert math.isinf(spread([4.5]))


def test_spread_zero_value_returns_inf():
    assert math.isinf(spread([0.0, 4.5]))


def test_spread_negative_value_returns_inf():
    assert math.isinf(spread([-1.0, 4.5]))


def test_spread_empty_list_returns_inf():
    assert math.isinf(spread([]))


# ---------------------------------------------------------------------------
# verdict_from_spreads()
# ---------------------------------------------------------------------------


def test_verdict_converge():
    assert verdict_from_spreads(1.5, 1.8, 3) == "CONVERGE"


def test_verdict_converge_at_threshold_minus_epsilon():
    # just below 2.0 → converge
    assert verdict_from_spreads(1.999, 1.999, 3) == "CONVERGE"


def test_verdict_diverge_both():
    assert verdict_from_spreads(5.8, 94.7, 3) == "DIVERGE"


def test_verdict_diverge_at_threshold():
    # exactly 2.0 → diverge (not strictly less than)
    assert verdict_from_spreads(2.0, 2.0, 3) == "DIVERGE"


def test_verdict_partial_d_only():
    # β_d converges, β_q diverges
    assert verdict_from_spreads(1.5, 5.0, 3) == "PARTIAL_D_ONLY"


def test_verdict_partial_q_only():
    # β_d diverges, β_q converges
    assert verdict_from_spreads(3.0, 1.5, 3) == "PARTIAL_Q_ONLY"


def test_verdict_insufficient_services_two():
    assert verdict_from_spreads(1.0, 1.0, 2) == "INSUFFICIENT_SERVICES"


def test_verdict_insufficient_services_zero():
    assert verdict_from_spreads(1.0, 1.0, 0) == "INSUFFICIENT_SERVICES"


def test_verdict_min_services_boundary():
    # exactly at minimum → valid verdict
    assert verdict_from_spreads(1.0, 1.0, MIN_SERVICES_FOR_VERDICT) == "CONVERGE"


# ---------------------------------------------------------------------------
# BETA-0 reference baseline
# ---------------------------------------------------------------------------


def test_beta0_reference_has_three_services():
    assert len(BETA0_REFERENCE) == 3


def test_beta0_beta_d_spread():
    bd = [v["beta_d"] for v in BETA0_REFERENCE.values()]
    s = spread(bd)
    # 4.5 / 0.78 ≈ 5.77
    assert s == pytest.approx(4.5 / 0.78, rel=1e-2)


def test_beta0_beta_q_spread():
    bq = [v["beta_q"] for v in BETA0_REFERENCE.values()]
    s = spread(bq)
    # 18.0 / 0.19 ≈ 94.7
    assert s == pytest.approx(18.0 / 0.19, rel=1e-2)


def test_beta0_analysis_verdict_diverge():
    result = _beta0_analysis()
    assert result["verdict"] == "DIVERGE"


def test_beta0_analysis_spread_d_above_threshold():
    result = _beta0_analysis()
    assert result["beta_d_spread"] >= CONVERGENCE_THRESHOLD


def test_beta0_analysis_spread_q_above_threshold():
    result = _beta0_analysis()
    assert result["beta_q_spread"] >= CONVERGENCE_THRESHOLD


def test_beta0_analysis_has_required_keys():
    result = _beta0_analysis()
    for key in (
        "services",
        "beta_d_values",
        "beta_q_values",
        "beta_d_spread",
        "beta_q_spread",
        "verdict",
    ):
        assert key in result


# ---------------------------------------------------------------------------
# load_responses()
# ---------------------------------------------------------------------------


def _write_response_csv(path: Path, beta_d: float, beta_q: float) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["parameter", "value", "confidence", "notes"])
        writer.writeheader()
        writer.writerow(
            {"parameter": "beta_d", "value": str(beta_d), "confidence": "high", "notes": "test"}
        )
        writer.writerow(
            {"parameter": "beta_q", "value": str(beta_q), "confidence": "high", "notes": "test"}
        )


def test_load_responses_empty_dir(tmp_path):
    result = load_responses(tmp_path)
    assert result == {}


def test_load_responses_single_file(tmp_path):
    _write_response_csv(tmp_path / "chatgpt_response.csv", 3.5, 12.0)
    result = load_responses(tmp_path)
    assert "chatgpt" in result
    assert result["chatgpt"]["beta_d"] == pytest.approx(3.5)
    assert result["chatgpt"]["beta_q"] == pytest.approx(12.0)


def test_load_responses_three_services(tmp_path):
    _write_response_csv(tmp_path / "chatgpt_response.csv", 3.5, 12.0)
    _write_response_csv(tmp_path / "gemini_response.csv", 4.0, 14.0)
    _write_response_csv(tmp_path / "claude_response.csv", 3.8, 13.5)
    result = load_responses(tmp_path)
    assert len(result) == 3
    assert "chatgpt" in result
    assert "gemini" in result
    assert "claude" in result


def test_load_responses_skips_fill_in_template(tmp_path):
    # Template file with FILL_IN values should be skipped
    template = tmp_path / "response_template.csv"
    with template.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["parameter", "value", "confidence", "notes"])
        writer.writeheader()
        writer.writerow(
            {"parameter": "beta_d", "value": "FILL_IN", "confidence": "high", "notes": ""}
        )
        writer.writerow(
            {"parameter": "beta_q", "value": "FILL_IN", "confidence": "high", "notes": ""}
        )
    result = load_responses(tmp_path)
    # response_template.csv → service name "response_template" → no beta_d/beta_q → skipped
    assert "response_template" not in result


def test_load_responses_skips_comment_lines(tmp_path):
    path = tmp_path / "chatgpt_response.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        f.write("# This is a comment\n")
        f.write("parameter,value,confidence,notes\n")
        f.write("beta_d,4.0,high,test\n")
        f.write("beta_q,15.0,high,test\n")
    result = load_responses(tmp_path)
    assert "chatgpt" in result
    assert result["chatgpt"]["beta_d"] == pytest.approx(4.0)


# ---------------------------------------------------------------------------
# run_audit() end-to-end
# ---------------------------------------------------------------------------


def test_run_audit_awaiting_with_no_responses(tmp_path, tmp_path_factory):
    report_dir = tmp_path_factory.mktemp("reports")
    import scripts.beta1_controlled_replication as mod

    orig_reports = mod.REPORTS_DIR
    mod.REPORTS_DIR = report_dir
    try:
        result = run_audit(data_dir=tmp_path)
        assert result["beta1"]["verdict"] == "AWAITING_RESPONSES"
        assert result["beta1"]["n_services"] == 0
    finally:
        mod.REPORTS_DIR = orig_reports


def test_run_audit_converge_with_three_services(tmp_path, tmp_path_factory):
    _write_response_csv(tmp_path / "chatgpt_response.csv", 3.8, 13.0)
    _write_response_csv(tmp_path / "gemini_response.csv", 4.0, 14.0)
    _write_response_csv(tmp_path / "claude_response.csv", 3.9, 13.5)
    report_dir = tmp_path_factory.mktemp("reports")
    import scripts.beta1_controlled_replication as mod

    orig_reports = mod.REPORTS_DIR
    mod.REPORTS_DIR = report_dir
    try:
        result = run_audit(data_dir=tmp_path)
        assert result["beta1"]["verdict"] == "CONVERGE"
        assert result["beta1"]["n_services"] == 3
        # max/min for β_d: 4.0/3.8 ≈ 1.05 < 2.0
        assert result["beta1"]["beta_d_spread"] < CONVERGENCE_THRESHOLD
        assert result["beta1"]["beta_q_spread"] < CONVERGENCE_THRESHOLD
    finally:
        mod.REPORTS_DIR = orig_reports


def test_run_audit_diverge_with_beta0_pattern(tmp_path, tmp_path_factory):
    # Reproduce BETA-0 divergence under controlled conditions
    _write_response_csv(tmp_path / "chatgpt_response.csv", 0.78, 0.19)
    _write_response_csv(tmp_path / "gemini_response.csv", 4.25, 8.10)
    _write_response_csv(tmp_path / "claude_response.csv", 4.5, 18.0)
    report_dir = tmp_path_factory.mktemp("reports")
    import scripts.beta1_controlled_replication as mod

    orig_reports = mod.REPORTS_DIR
    mod.REPORTS_DIR = report_dir
    try:
        result = run_audit(data_dir=tmp_path)
        assert result["beta1"]["verdict"] == "DIVERGE"
        assert result["beta1"]["beta_d_spread"] >= CONVERGENCE_THRESHOLD
        assert result["beta1"]["beta_q_spread"] >= CONVERGENCE_THRESHOLD
    finally:
        mod.REPORTS_DIR = orig_reports


def test_run_audit_report_written(tmp_path, tmp_path_factory):
    _write_response_csv(tmp_path / "chatgpt_response.csv", 3.8, 13.0)
    _write_response_csv(tmp_path / "gemini_response.csv", 4.0, 14.0)
    _write_response_csv(tmp_path / "claude_response.csv", 3.9, 13.5)
    report_dir = tmp_path_factory.mktemp("reports")
    import scripts.beta1_controlled_replication as mod

    orig_reports = mod.REPORTS_DIR
    mod.REPORTS_DIR = report_dir
    try:
        run_audit(data_dir=tmp_path)
        report = report_dir / "beta1_controlled_replication.json"
        assert report.exists()
        with report.open(encoding="utf-8") as f:
            data = json.load(f)
        assert data["audit"] == "BETA-1"
    finally:
        mod.REPORTS_DIR = orig_reports


# ---------------------------------------------------------------------------
# Safety labels
# ---------------------------------------------------------------------------


REQUIRED_SAFETY_LABELS = [
    "BETA-1",
    "AI_CONVERGENCE_TEST",
    "OUR_RECONSTRUCTION",
    "NOT_VALIDATION",
    "NOT_REFUTATION",
    "NOT_MODELING",
    "NOT_THEORY_FALSE",
    "NOT_AUTHOR_CONFIRMED",
]


@pytest.mark.parametrize("label", REQUIRED_SAFETY_LABELS)
def test_safety_label_present(label):
    assert label in SAFETY_LABELS


def test_run_audit_report_contains_safety_labels(tmp_path, tmp_path_factory):
    report_dir = tmp_path_factory.mktemp("reports")
    import scripts.beta1_controlled_replication as mod

    orig_reports = mod.REPORTS_DIR
    mod.REPORTS_DIR = report_dir
    try:
        result = run_audit(data_dir=tmp_path)
        for label in REQUIRED_SAFETY_LABELS:
            assert label in result["labels"]
    finally:
        mod.REPORTS_DIR = orig_reports


# ---------------------------------------------------------------------------
# Report structure
# ---------------------------------------------------------------------------


def test_run_audit_has_status_implications(tmp_path, tmp_path_factory):
    report_dir = tmp_path_factory.mktemp("reports")
    import scripts.beta1_controlled_replication as mod

    orig_reports = mod.REPORTS_DIR
    mod.REPORTS_DIR = report_dir
    try:
        result = run_audit(data_dir=tmp_path)
        assert "CONVERGE" in result["status_implications"]
        assert "DIVERGE" in result["status_implications"]
        assert "AWAITING_RESPONSES" in result["status_implications"]
    finally:
        mod.REPORTS_DIR = orig_reports


def test_run_audit_convergence_threshold_in_report(tmp_path, tmp_path_factory):
    report_dir = tmp_path_factory.mktemp("reports")
    import scripts.beta1_controlled_replication as mod

    orig_reports = mod.REPORTS_DIR
    mod.REPORTS_DIR = report_dir
    try:
        result = run_audit(data_dir=tmp_path)
        assert result["convergence_threshold"] == CONVERGENCE_THRESHOLD
    finally:
        mod.REPORTS_DIR = orig_reports


def test_run_audit_beta0_reference_in_report(tmp_path, tmp_path_factory):
    report_dir = tmp_path_factory.mktemp("reports")
    import scripts.beta1_controlled_replication as mod

    orig_reports = mod.REPORTS_DIR
    mod.REPORTS_DIR = report_dir
    try:
        result = run_audit(data_dir=tmp_path)
        assert result["beta0_reference"]["verdict"] == "DIVERGE"
        assert result["beta0_reference"]["beta_d_spread"] >= CONVERGENCE_THRESHOLD
    finally:
        mod.REPORTS_DIR = orig_reports
