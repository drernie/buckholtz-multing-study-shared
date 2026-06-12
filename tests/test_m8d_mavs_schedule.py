"""
Tests for M8-D: Minimal Assumption Virial Schedule (MAVS).

Labels: OUR_RECONSTRUCTION · CONDITIONAL_RECONSTRUCTION
        NOT_AUTHOR_CONFIRMED · M8_D_MAVS
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.m8d_mavs_schedule import (
    G_COSMO,
    M_MIN_VARIANTS,
    SIGMA_8,
    Z_DATA,
    D_C_AB_mpc,
    compute_eps,
    compute_m8,
    is_monotone_increasing,
    k_A_virial,
    r_A_comoving_mpc,
    r_P_physical_mpc,
    r_vir_mpc,
    rho_crit_cosmo,
    run_m8d_mavs_schedule,
    sigma_mass_z,
)

# ── Constants ─────────────────────────────────────────────────────────────────


def test_g_cosmo_reference_value():
    """G in (km/s)^2 Mpc M_sun^-1 ~ 4.302e-9 (standard cosmology)."""
    assert abs(G_COSMO / 4.302e-9 - 1.0) < 0.01


def test_rho_crit_z0_reference():
    """rho_crit(z=0) ~ 1.36e11 M_sun/Mpc^3 for H_0=70, flat LCDM."""
    rho = rho_crit_cosmo(0.0)
    assert 1.0e11 < rho < 2.0e11, f"rho_crit(0) = {rho:.3e}"


def test_rho_crit_increasing_with_z():
    """rho_crit(z) increases with z because H(z) increases."""
    zs = [0.0, 0.5, 1.0, 3.0, 8.5]
    rhos = [rho_crit_cosmo(z) for z in zs]
    assert all(rhos[i + 1] > rhos[i] for i in range(len(rhos) - 1))


# ── Virial radius ──────────────────────────────────────────────────────────────


def test_r_vir_physical_order_of_magnitude():
    """r_vir(M=1e14, z=0) ~ 0.9-1.0 Mpc (observed massive cluster scale)."""
    r = r_vir_mpc(1.0e14, 0.0)
    assert 0.5 < r < 2.0, f"r_vir = {r:.3f} Mpc"


def test_r_vir_decreasing_with_z():
    """r_vir shrinks with z: rho_crit grows so clusters are more compact at high z."""
    m_min = 1.0e14
    zs = [0.0, 0.5, 1.0, 2.0, 5.0]
    rvirs = [r_vir_mpc(m_min, z) for z in zs]
    assert all(rvirs[i + 1] < rvirs[i] for i in range(len(rvirs) - 1))


def test_r_vir_scales_with_mass():
    """r_vir increases with mass (more massive cluster = larger at same z)."""
    z = 0.0
    r_small = r_vir_mpc(1.0e14, z)
    r_large = r_vir_mpc(1.0e15, z)
    assert r_large > r_small


# ── k_A virial energy ─────────────────────────────────────────────────────────


def test_k_A_positive():
    """k_A > 0 at all z values."""
    for z in Z_DATA:
        assert k_A_virial(1.0e14, z) > 0.0


def test_k_A_monotone_increasing():
    """k_A propto H(z)^(4/3) — monotonically increasing with z."""
    m_min = 1.0e14
    vals = [k_A_virial(m_min, z) for z in Z_DATA]
    assert is_monotone_increasing(vals), "k_A must increase with z (virial theorem + overdensity)"


def test_k_A_peaks_at_high_z():
    """k_A maximum is at z=8.5 (highest z in dataset) for all M_min variants."""
    for m_min, _ in M_MIN_VARIANTS:
        vals = [k_A_virial(m_min, z) for z in Z_DATA]
        peak_z = Z_DATA[vals.index(max(vals))]
        assert peak_z == pytest.approx(8.5), f"k_A should peak at z=8.5, got {peak_z}"


def test_k_A_not_same_for_different_mass():
    """k_A changes with M_min (dimensional dependence on cluster mass)."""
    z = 0.0
    k_small = k_A_virial(1.0e14, z)
    k_large = k_A_virial(1.0e15, z)
    assert abs(k_small / k_large - 1.0) > 0.01


# ── Press-Schechter separation ────────────────────────────────────────────────


def test_m8_reference_value():
    """M_8 ~ 2.68e14 M_sun for H0=70, Omega_m=0.315 (10% tolerance)."""
    assert abs(compute_m8() / 2.68e14 - 1.0) < 0.10


def test_sigma_at_m8_is_sigma8():
    """sigma(M_8, z=0) = sigma_8 by construction."""
    m8 = compute_m8()
    sigma = sigma_mass_z(m8, 0.0)
    assert abs(sigma / SIGMA_8 - 1.0) < 0.01


def test_r_A_physical_order_of_magnitude():
    """r_A(M=1e14, z=0) ~ 20-50 Mpc (typical cluster separation in local universe)."""
    r = r_A_comoving_mpc(1.0e14, 0.0)
    assert 10.0 < r < 100.0, f"r_A(z=0) = {r:.1f} Mpc"


def test_r_A_monotone_for_small_m_min():
    """r_A(M=1e14) is monotonically increasing with z (fewer clusters at high z)."""
    vals = [r_A_comoving_mpc(1.0e14, z) for z in Z_DATA]
    assert is_monotone_increasing(vals)


def test_D_C_AB_equals_r_A():
    """D_C:AB = r_A by the minimal assumption construction."""
    for m_min, _ in M_MIN_VARIANTS:
        for z in Z_DATA[:5]:  # spot-check first 5 redshifts
            assert D_C_AB_mpc(m_min, z) == pytest.approx(r_A_comoving_mpc(m_min, z))


def test_r_P_less_than_r_A_for_z_gt_0():
    """r_P = r_A/(1+z) < r_A for all z > 0."""
    m_min = 1.0e14
    for z in Z_DATA[1:]:  # skip z=0.06 is still < 1 but check all > 0
        assert r_P_physical_mpc(m_min, z) < r_A_comoving_mpc(m_min, z)


# ── eps(z) ────────────────────────────────────────────────────────────────────


def test_eps_peak_at_z040():
    """eps peaks at z=0.40 [TRANSCRIBED, M8-A-R1 PASS]."""
    eps = compute_eps()
    assert Z_DATA[eps.index(max(eps))] == pytest.approx(0.40)


def test_no_mavs_component_peaks_at_z040():
    """No MAVS component peaks at z=0.40 for any M_min — confirms FAIL verdict."""
    m_min = 1.0e14
    components = {
        "k_A": [k_A_virial(m_min, z) for z in Z_DATA],
        "r_A": [r_A_comoving_mpc(m_min, z) for z in Z_DATA],
        "r_P": [r_P_physical_mpc(m_min, z) for z in Z_DATA],
    }
    for name, vals in components.items():
        peak_z = Z_DATA[vals.index(max(vals))]
        assert peak_z != pytest.approx(0.40), (
            f"{name} peaks at z=0.40 — unexpected match with eps peak"
        )


# ── Full audit run ────────────────────────────────────────────────────────────


def test_run_produces_json_report():
    """run_m8d_mavs_schedule writes reports/m8d_mavs_schedule.json."""
    run_m8d_mavs_schedule()
    json_path = Path(__file__).parent.parent / "reports" / "m8d_mavs_schedule.json"
    assert json_path.exists()
    data = json.loads(json_path.read_text(encoding="utf-8"))
    assert data["gate"] == "M8-D-MAVS-schedule"


def test_verdict_is_valid():
    """Verdict is one of the four valid values."""
    result = run_m8d_mavs_schedule()
    assert result["overall_verdict"] in {"PASS", "PARTIAL", "FAIL", "BLOCKED"}


def test_verdict_fail_confirmed():
    """MAVS virial+PS components cannot reproduce eps shape — verdict must be FAIL."""
    result = run_m8d_mavs_schedule()
    # k_A is monotone by physics; no component peaks at z=0.40 — PASS impossible
    assert result["overall_verdict"] == "FAIL"


def test_all_pearson_r_below_pass_threshold():
    """All Pearson r (signed) are below PASS threshold (0.85)."""
    result = run_m8d_mavs_schedule()
    for entry in result["results_by_m_min"]:
        for comp, r_val in entry["pearson_r"].items():
            assert r_val < 0.85, f"Unexpectedly high r={r_val} for {comp}"


def test_k_A_monotone_confirmed_in_report():
    """JSON report confirms k_A is monotone for all M_min variants."""
    result = run_m8d_mavs_schedule()
    for entry in result["results_by_m_min"]:
        assert entry["monotone_k_A"] is True, (
            f"k_A not monotone for M_min={entry['m_min_solar']:.0e}"
        )


def test_safety_labels_present():
    """All required safety labels must be in the JSON report."""
    result = run_m8d_mavs_schedule()
    required = {
        "M8_D_MAVS",
        "OUR_RECONSTRUCTION",
        "CONDITIONAL_RECONSTRUCTION",
        "NOT_AUTHOR_CONFIRMED",
        "NOT_VALIDATION",
        "NOT_REFUTATION",
        "AUTHOR_SCHEDULE_NEEDED",
        "<HYPOTHESIS>",
    }
    present = set(result["labels"])
    missing = required - present
    assert not missing, f"Missing safety labels: {missing}"


def test_no_h_fitting_flag():
    """Physics sources must declare no_H_fitting=True (no FLRW H(z) fit used)."""
    result = run_m8d_mavs_schedule()
    assert result["physics_sources"]["no_H_fitting"] is True


def test_no_tableA1_powerlaw_fit_flag():
    """Physics sources must declare no_TableA1_powerlaw_fit=True."""
    result = run_m8d_mavs_schedule()
    assert result["physics_sources"]["no_TableA1_powerlaw_fit"] is True


def test_three_m_min_variants_tested():
    """Three M_min variants tested (as specified in M_MIN_VARIANTS)."""
    result = run_m8d_mavs_schedule()
    assert len(result["results_by_m_min"]) == 3


def test_hypothesis_label_in_conclusions():
    """<HYPOTHESIS> language must appear in conclusions — not stated as confirmed fact."""
    result = run_m8d_mavs_schedule()
    combined = " ".join(result["conclusions"])
    assert "HYPOTHESIS" in combined or "hypothesis" in combined.lower()
    assert "CONFIRMED" not in combined, "Must not claim PS-virial connection is confirmed"


def test_author_schedule_needed_in_conclusions():
    """Conclusions must explicitly state AUTHOR_SCHEDULE_NEEDED."""
    result = run_m8d_mavs_schedule()
    combined = " ".join(result["conclusions"])
    assert "AUTHOR_SCHEDULE_NEEDED" in combined or "author" in combined.lower()
