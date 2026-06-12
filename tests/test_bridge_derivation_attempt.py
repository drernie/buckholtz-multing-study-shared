"""
Tests for bridge_derivation_attempt.py

Labels: TABLE_A1_DATA · OUR_RECONSTRUCTION · INTERNAL_DIAGNOSTIC_ONLY
Scope:  NOT_AUTHOR_CONFIRMED · NOT_VALIDATION
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from bridge_derivation_attempt import (
    H_FLRW_DATA,
    H_MULT_DATA,
    Z_DATA,
    analyze_nonmonotonicity,
    candidate_cluster_density,
    candidate_constant_eps,
    candidate_power_law,
    compute_epsilon,
    compute_ratio,
    run_derivation,
)

# ── Core metric: ε(z) ────────────────────────────────────────────────────────


def test_epsilon_zero_for_equal_inputs():
    """ε = 0 when H_MULT == H_FLRW."""
    assert compute_epsilon(100.0, 100.0) == 0.0


def test_epsilon_positive_when_mult_greater():
    """ε > 0 when H_MULT > H_FLRW (MULTING boosts H)."""
    eps = compute_epsilon(83.1, 75.0)
    assert eps > 0.0


def test_epsilon_formula_spot_check():
    """ε = (83.1/75.0)² − 1 ≈ 0.2277 at z=0.40."""
    eps = compute_epsilon(83.1, 75.0)
    expected = (83.1 / 75.0) ** 2 - 1.0
    assert math.isclose(eps, expected, rel_tol=1e-12)
    assert math.isclose(eps, 0.2277, abs_tol=0.001)


def test_ratio_formula():
    """ratio = H_MULT / H_FLRW."""
    assert math.isclose(compute_ratio(83.1, 75.0), 83.1 / 75.0, rel_tol=1e-12)


def test_epsilon_all_positive_in_table_a1():
    """All Table A1 entries have H_MULT > H_FLRW → ε > 0 throughout."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    assert all(e > 0.0 for e in eps_values)


def test_epsilon_count_matches_z():
    """ε values, z values, and H arrays all have the same length."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    assert len(eps_values) == len(Z_DATA) == len(H_FLRW_DATA) == len(H_MULT_DATA)


# ── Non-monotonicity: the central finding ────────────────────────────────────


def test_eps_is_non_monotonic():
    """Key finding: ε(z) is non-monotonic [VERIFIED from Table A1]."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    nm = analyze_nonmonotonicity(Z_DATA, eps_values)
    assert nm["is_monotonic"] is False


def test_eps_peak_at_z040():
    """ε(z) peaks at z=0.40 (cluster number density peak in ΛCDM)."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    nm = analyze_nonmonotonicity(Z_DATA, eps_values)
    assert math.isclose(nm["eps_peak_z"], 0.40, abs_tol=0.01)


def test_eps_peak_value():
    """ε peak ≈ 0.228 at z=0.40."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    nm = analyze_nonmonotonicity(Z_DATA, eps_values)
    assert math.isclose(nm["eps_peak_value"], 0.2277, abs_tol=0.001)


def test_eps_minimum_at_z500():
    """ε(z) minimum at z=5.0 (pre-cluster-formation epoch)."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    nm = analyze_nonmonotonicity(Z_DATA, eps_values)
    assert math.isclose(nm["eps_min_z"], 5.0, abs_tol=0.01)


def test_eps_min_value():
    """ε minimum ≈ 0.048 at z=5.0."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    nm = analyze_nonmonotonicity(Z_DATA, eps_values)
    assert math.isclose(nm["eps_min_value"], 0.0481, abs_tol=0.001)


def test_eps_range_large():
    """ε spans > 0.15 — too large for single-parameter bridge."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    nm = analyze_nonmonotonicity(Z_DATA, eps_values)
    assert nm["eps_range"] > 0.15


# ── Candidate 1: constant ε FAILS ────────────────────────────────────────────


def test_candidate_constant_eps_fails():
    """Constant-ε bridge fails because ε(z) is non-monotonic."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    result = candidate_constant_eps(eps_values)
    assert result["verdict"] == "FAILS"


def test_candidate_constant_eps_max_residual():
    """Max residual > 0.05 when using constant-ε bridge."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    result = candidate_constant_eps(eps_values)
    assert result["max_residual"] > 0.05


def test_candidate_constant_eps_fitted_c_reasonable():
    """Fitted C is between 0.10 and 0.20 (mean of ε range)."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    result = candidate_constant_eps(eps_values)
    assert 0.10 < result["fitted_C"] < 0.20


# ── Candidate 2: power law FAILS ─────────────────────────────────────────────


def test_candidate_power_law_fails():
    """Power-law bridge fails — α is not consistent across z."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    result = candidate_power_law(Z_DATA, eps_values)
    assert result["verdict"] == "FAILS"


def test_candidate_power_law_alpha_range_wide():
    """α varies by > 5 units across z-pairs (sign change, not just magnitude)."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    result = candidate_power_law(Z_DATA, eps_values)
    alpha_span = result["alpha_range_by_pairs"][1] - result["alpha_range_by_pairs"][0]
    assert alpha_span > 5.0


def test_candidate_power_law_alpha_sign_changes():
    """α ranges from negative to positive — proving non-monotonicity."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    result = candidate_power_law(Z_DATA, eps_values)
    assert result["alpha_range_by_pairs"][0] < 0  # min α negative
    assert result["alpha_range_by_pairs"][1] > 0  # max α positive


# ── Candidate 3: Friedmann is BLOCKED ────────────────────────────────────────


def test_candidate_cluster_density_blocked():
    """Friedmann bridge is BLOCKED — requires Q2 (k_A(z) schedule from TJB)."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    result = candidate_cluster_density(Z_DATA, H_FLRW_DATA, eps_values)
    assert result["verdict"].startswith("BLOCKED")


def test_candidate_cluster_density_rho_normalized_peak_at_z040():
    """ρ_cluster normalized to peak=1 at z=0.40."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    result = candidate_cluster_density(Z_DATA, H_FLRW_DATA, eps_values)
    # Find index of z=0.40
    i_peak = Z_DATA.index(0.40)
    assert math.isclose(result["rho_cluster_kg_m3"][i_peak], 1.0, rel_tol=1e-6)


def test_candidate_cluster_density_mismatch_at_high_z():
    """ρ_cluster(z) diverges from (1+z)³ DM scaling at z > 1."""
    eps_values = [compute_epsilon(hm, hf) for hm, hf in zip(H_MULT_DATA, H_FLRW_DATA, strict=False)]
    result = candidate_cluster_density(Z_DATA, H_FLRW_DATA, eps_values)
    # At least 5 of 11 points flagged as MISMATCH
    mismatches = sum(1 for row in result["vs_dark_matter_scaling"] if row["flag"] == "MISMATCH")
    assert mismatches >= 5


# ── JSON report ───────────────────────────────────────────────────────────────


def test_json_report_written_and_valid():
    """run_derivation() writes valid JSON with all required keys."""
    result = run_derivation()

    assert result["gate"] == "bridge-derivation-attempt"
    assert result["nonmonotonicity"]["is_monotonic"] is False
    assert len(result["eps_z_table"]) == 11
    assert result["candidate_1_constant"]["verdict"] == "FAILS"
    assert result["candidate_2_power_law"]["verdict"] == "FAILS"
    assert result["candidate_3_friedmann"]["verdict"].startswith("BLOCKED")
    assert len(result["conclusions"]) >= 4

    json_path = Path(__file__).parent.parent / "reports" / "bridge_derivation_attempt.json"
    assert json_path.exists(), "JSON report not written"
    data = json.loads(json_path.read_text(encoding="utf-8"))
    assert data["gate"] == "bridge-derivation-attempt"
    assert data["nonmonotonicity"]["is_monotonic"] is False
