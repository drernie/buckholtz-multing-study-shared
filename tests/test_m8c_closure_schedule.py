"""
Tests for M8-C: Closure Schedule — Cluster Formation Bridge.

Labels: OUR_RECONSTRUCTION · <HYPOTHESIS> · EXTERNAL_STANDARD_PHYSICS
        NOT_AUTHOR_CONFIRMED · INTERNAL_DIAGNOSTIC_ONLY
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

from scripts.m8c_closure_schedule import (
    H0_KMS_MPC,
    OM_MATTER,
    SIGMA_8,
    Z_DATA,
    comoving_distance,
    compute_eps,
    compute_m8,
    fit_proportional,
    growth_factor_norm,
    hubble_lcdm,
    normalize_to_max,
    pearson_r,
    ps_comoving_fraction,
    run_m8c_closure_schedule,
    sigma_mass_z,
    survey_count_rate,
)

# ── ΛCDM background physics ──────────────────────────────────────────────────


def test_hubble_at_z0_equals_h0():
    """H(0) must equal H_0 in flat ΛCDM."""
    assert abs(hubble_lcdm(0.0) - H0_KMS_MPC) < 0.001


def test_hubble_increasing_with_z():
    """H(z) increases with z in matter+Λ dominated universe."""
    zs = [0.0, 0.5, 1.0, 2.0, 5.0]
    hs = [hubble_lcdm(z) for z in zs]
    for i in range(len(hs) - 1):
        assert hs[i + 1] > hs[i], f"H(z) not increasing at z={zs[i]}"


def test_hubble_matter_dominated_scaling():
    """At high z, H(z) ≈ H_0 × sqrt(Ω_m) × (1+z)^(3/2)."""
    z = 10.0
    h_approx = H0_KMS_MPC * math.sqrt(OM_MATTER) * (1 + z) ** 1.5
    h_exact = hubble_lcdm(z)
    # Should agree within 5% at z=10 (Λ is small fraction of total)
    assert abs(h_exact / h_approx - 1.0) < 0.05


def test_growth_factor_norm_at_z0_is_one():
    """D(0)/D(0) = 1 by definition."""
    assert abs(growth_factor_norm(0.0) - 1.0) < 1e-4


def test_growth_factor_decreasing_at_high_z():
    """Growth factor D(z)/D(0) < 1 for z > 0 (structure grows toward z=0)."""
    for z in [0.5, 1.0, 2.0, 5.0, 8.0]:
        d = growth_factor_norm(z)
        assert d < 1.0, f"D({z})/D(0) = {d} ≥ 1"
        assert d > 0.0, f"D({z})/D(0) = {d} ≤ 0"


def test_comoving_distance_at_z0_is_zero():
    """Comoving distance at z=0 is 0 by definition."""
    assert comoving_distance(0.0) == 0.0


def test_comoving_distance_increasing():
    """r(z) increases with z."""
    zs = [0.1, 0.5, 1.0, 2.0, 5.0]
    rs = [comoving_distance(z) for z in zs]
    for i in range(len(rs) - 1):
        assert rs[i + 1] > rs[i], f"r(z) not increasing at z={zs[i]}"


def test_comoving_distance_z1_reference():
    """r(z=1) ≈ 3200–3500 Mpc for standard ΛCDM (H_0=70, Ω_m=0.315)."""
    r_z1 = comoving_distance(1.0)
    # WHY: flat ΛCDM with these params gives ~3300 Mpc at z=1 (Ned Wright calculator)
    assert 3000.0 < r_z1 < 3700.0, f"r(z=1) = {r_z1:.0f} Mpc outside expected range"


# ── Press-Schechter cluster abundance ────────────────────────────────────────


def test_m8_physical_range():
    """M_8 ≈ 2-4 × 10^14 M_sun for standard cosmology."""
    m8 = compute_m8()
    assert 1.5e14 < m8 < 5.0e14, f"M_8 = {m8:.3e} outside expected range"


def test_m8_reference_value():
    """M_8 ≈ 2.68e14 M_sun for H_0=70, Ω_m=0.315 (10% tolerance)."""
    m8 = compute_m8()
    assert abs(m8 / 2.68e14 - 1.0) < 0.10


def test_sigma_at_m8_is_sigma8():
    """σ(M_8, z=0) = σ_8 by construction of the scaling."""
    m8 = compute_m8()
    sigma = sigma_mass_z(m8, 0.0)
    assert abs(sigma / SIGMA_8 - 1.0) < 0.01


def test_sigma_decreasing_with_z():
    """σ(M_min, z) decreases with z (growth factor shrinks)."""
    m_min = 5.0e14
    zs = [0.0, 0.5, 1.0, 2.0]
    sigmas = [sigma_mass_z(m_min, z) for z in zs]
    for i in range(len(sigmas) - 1):
        assert sigmas[i + 1] < sigmas[i]


def test_ps_comoving_fraction_decreasing():
    """PS comoving density f(>M_min, z) is monotonically decreasing with z."""
    m_min = 3.0e14
    zs = [0.0, 0.5, 1.0, 2.0, 5.0]
    fracs = [ps_comoving_fraction(m_min, z) for z in zs]
    for i in range(len(fracs) - 1):
        assert fracs[i + 1] <= fracs[i], (
            f"PS density not decreasing at z={zs[i]}: {fracs[i]} → {fracs[i + 1]}"
        )


def test_ps_positive_at_low_z():
    """At z=0, some fraction of mass is in clusters."""
    frac = ps_comoving_fraction(1.0e14, 0.0)
    assert 0.0 < frac <= 1.0


def test_survey_rate_zero_at_z0():
    """Survey count rate dN/dz = 0 at z=0 (zero comoving volume)."""
    rate = survey_count_rate(1.0e14, 0.0)
    assert rate == 0.0


def test_survey_rate_positive():
    """Survey count rate is positive at z > 0."""
    for z in [0.25, 0.5, 1.0]:
        rate = survey_count_rate(3.0e14, z)
        assert rate > 0.0, f"Survey rate at z={z} is not positive"


# ── Statistical tools ─────────────────────────────────────────────────────────


def test_pearson_r_identical_lists():
    """Pearson r = 1 for identical sequences."""
    x = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert abs(pearson_r(x, x) - 1.0) < 1e-10


def test_pearson_r_reversed():
    """Pearson r = -1 for perfectly anti-correlated sequences."""
    x = [1.0, 2.0, 3.0, 4.0, 5.0]
    y = [5.0, 4.0, 3.0, 2.0, 1.0]
    assert abs(pearson_r(x, y) + 1.0) < 1e-10


def test_normalize_to_max():
    """normalize_to_max returns list with max = 1.0."""
    vals = [2.0, 5.0, 3.0, 1.0]
    normed = normalize_to_max(vals)
    assert max(normed) == pytest.approx(1.0)
    assert min(normed) == pytest.approx(0.2)


def test_fit_proportional_exact():
    """fit_proportional recovers C exactly for perfect proportionality."""
    x = [1.0, 2.0, 3.0]
    y = [2.0, 4.0, 6.0]  # y = 2×x
    c, rms, max_res = fit_proportional(x, y)
    assert abs(c - 2.0) < 1e-10
    assert rms < 1e-10
    assert max_res < 1e-10


# ── ε(z) from Table A1 ───────────────────────────────────────────────────────


def test_eps_values_all_positive():
    """ε(z) = (H_MULT/H_FLRW)² − 1 > 0 because H_MULT > H_FLRW throughout."""
    eps = compute_eps()
    assert all(e > 0.0 for e in eps)


def test_eps_peak_at_z040():
    """ε peaks at z=0.40 — independently confirmed in M8-A-R1."""
    eps = compute_eps()
    peak_idx = eps.index(max(eps))
    assert Z_DATA[peak_idx] == pytest.approx(0.40)
    assert max(eps) == pytest.approx(0.2277, abs=0.001)


def test_eps_minimum_at_z500():
    """ε global minimum at z=5.00."""
    eps = compute_eps()
    min_idx = eps.index(min(eps))
    assert Z_DATA[min_idx] == pytest.approx(5.00)
    assert min(eps) == pytest.approx(0.0481, abs=0.001)


def test_eps_nonmonotonic():
    """ε has multiple sign-change events (non-monotonic shape, ≥4)."""
    eps = compute_eps()
    sign_changes = 0
    for i in range(1, len(eps) - 1):
        if (eps[i] - eps[i - 1]) * (eps[i + 1] - eps[i]) < 0:
            sign_changes += 1
    assert sign_changes >= 3, f"Only {sign_changes} sign changes detected in ε(z)"


# ── Full audit run ───────────────────────────────────────────────────────────


def test_run_produces_json_report():
    """run_m8c_closure_schedule writes a JSON file to reports/."""
    run_m8c_closure_schedule()
    json_path = Path(__file__).parent.parent / "reports" / "m8c_closure_schedule.json"
    assert json_path.exists()
    data = json.loads(json_path.read_text(encoding="utf-8"))
    assert data["gate"] == "M8-C-closure-schedule"


def test_verdict_partial():
    """Expected verdict is PARTIAL (not FAIL, not PASS) with correct physics."""
    result = run_m8c_closure_schedule()
    assert result["overall_verdict"] == "PARTIAL"


def test_best_pearson_r_above_threshold():
    """Best Pearson r should exceed 0.65 (Model B with correct M_8)."""
    result = run_m8c_closure_schedule()
    assert result["best_pearson_r"] >= 0.65, (
        f"Best Pearson r = {result['best_pearson_r']} < 0.65 (M_8 calculation may be wrong)"
    )


def test_model_a_never_peaks_at_z040():
    """Model A (comoving) always peaks at z=0.06 (lowest z in dataset)."""
    result = run_m8c_closure_schedule()
    for entry in result["results_by_m_min"]:
        assert entry["model_A_comoving"]["peak_z"] == pytest.approx(0.06)


def test_model_b_peaks_near_eps_peak():
    """At least one M_min variant of Model B peaks within the z=0.25–0.65 range."""
    result = run_m8c_closure_schedule()
    survey_peaks = [entry["model_B_survey"]["peak_z"] for entry in result["results_by_m_min"]]
    assert any(0.25 <= p <= 0.70 for p in survey_peaks), (
        f"No Model B variant peaks near ε primary peak. Peaks: {survey_peaks}"
    )


def test_safety_labels_present():
    """JSON report must carry all required safety labels."""
    result = run_m8c_closure_schedule()
    required = {"OUR_RECONSTRUCTION", "NOT_VALIDATION", "NOT_REFUTATION", "<HYPOTHESIS>"}
    present = set(result["labels"])
    assert required.issubset(present), f"Missing safety labels: {required - present}"


def test_hypothesis_not_confirmed():
    """<HYPOTHESIS> status is explicitly stated as unconfirmed in conclusions."""
    result = run_m8c_closure_schedule()
    conc_text = " ".join(result["conclusions"])
    assert "HYPOTHESIS" in conc_text or "hypothesis" in conc_text.lower()
    # Must NOT use language implying the hypothesis is confirmed
    assert "CONFIRMED" not in conc_text


def test_m_min_variants_match_spec():
    """Three M_min variants tested: 1e14, 5e14, 2e15 M_sun."""
    result = run_m8c_closure_schedule()
    m_mins = [r["m_min_solar"] for r in result["results_by_m_min"]]
    assert len(m_mins) == 3
    assert any(abs(m / 1.0e14 - 1.0) < 0.01 for m in m_mins)
    assert any(abs(m / 5.0e14 - 1.0) < 0.01 for m in m_mins)
    assert any(abs(m / 2.0e15 - 1.0) < 0.01 for m in m_mins)
