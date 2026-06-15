"""Tests for k_A closure test and Phase 0 D_required modules."""

from __future__ import annotations

import math

import pytest

from src.bridge_gate import (
    OUTPUT_LABEL,
    BridgeGateError,
    assert_not_mcmc,
    is_mcmc_allowed,
)
from src.bridge_phi import (
    h_from_phi_ratio,
    h_mult_from_params_list,
    phi_force_sum,
    rms_sigma_h,
)
from src.cluster_schedule import geom_mean_range, load_claude_cluster_params
from src.d_required_solver import (
    build_d_required_table,
    fit_gamma,
    gamma_sensitivity,
    solve_D_required,
)
from src.k_a_closure_test import ClosureVerdict, run_k_a_closure_test
from src.k_a_independent import (
    k_a_schedule_independent,
    k_a_virial_kinetic,
    load_k_a_csv_inferred,
)


@pytest.fixture
def claude_rows():
    return load_claude_cluster_params()


@pytest.fixture
def claude_params(claude_rows):
    from src.cluster_schedule import cluster_rows_to_params_list

    return cluster_rows_to_params_list(claude_rows)


H_OBS = [73.0, 69.0, 74.0, 79.0, 82.0, 92.0, 105.0, 125.0, 150.0, 195.0, 270.0, 420.0]
SIGMA_H = [1.0, 3.0, 4.0, 4.5, 5.0, 7.0, 8.0, 15.0, 20.0, 30.0, 50.0, 90.0]


def test_phi_force_sum_positive():
    assert phi_force_sum(3.16e14, 1e12, 1.73, 44.7, 4.5, 18.0) > 0


def test_h_from_phi_ratio_anchor():
    p = phi_force_sum(3.16e14, 1e12, 1.73, 44.7, 4.5, 18.0)
    assert abs(h_from_phi_ratio(p, p, 73.0) - 73.0) < 1e-9


def test_bridge_gate_mcmc_blocked():
    assert is_mcmc_allowed is False
    assert OUTPUT_LABEL == "NOT_VALIDATION"
    with pytest.raises(BridgeGateError):
        assert_not_mcmc("test")


def test_geom_mean_range():
    assert abs(geom_mean_range(1e11, 1e13) - 1e12) < 1.0


def test_load_claude_twelve_rows(claude_rows):
    assert len(claude_rows) == 12
    assert claude_rows[0].z == 0.0


def test_solve_D_required_anchor_roundtrip():
    m, k, r, d = 3.16e14, 1e12, 1.73, 44.7
    phi0 = phi_force_sum(m, k, r, d, 4.5, 18.0)
    d_req = solve_D_required(m, k, r, 73.0, 73.0, phi0, 4.5, 18.0)
    assert abs(d_req - d) < 1.0


def test_gamma_req_z_ge_04(claude_rows):
    table = build_d_required_table(rows=claude_rows, H_obs=H_OBS, sigma_H=SIGMA_H)
    high = [r for r in table if r.z >= 0.4]
    _d0, gamma, _r2 = fit_gamma([r.z for r in high], [r.D_required for r in high], D0=table[0].D_csv)
    assert 2.0 <= gamma <= 2.6


def test_D_req_over_csv_high_z(claude_rows):
    table = build_d_required_table(rows=claude_rows, H_obs=H_OBS, sigma_H=SIGMA_H)
    high = [r for r in table if r.z >= 3.0]
    assert all(r.ratio_D_req_over_csv < 0.8 for r in high if not math.isnan(r.ratio_D_req_over_csv))


def test_gamma_sensitivity_span(claude_rows):
    g_lo = gamma_sensitivity(sign=-1, rows=claude_rows)
    g_hi = gamma_sensitivity(sign=+1, rows=claude_rows)
    assert g_hi - g_lo > 0.1


def test_k_a_independent_positive(claude_rows):
    k = k_a_schedule_independent(claude_rows)
    assert len(k) == 12
    assert all(v > 0 for v in k)


def test_k_a_csv_inferred_length():
    assert len(load_k_a_csv_inferred()) == 12


def test_closure_test_labels(claude_rows):
    res = run_k_a_closure_test(claude_rows, H_OBS, SIGMA_H, arm="D_csv")
    assert res.label == "NOT_VALIDATION"
    assert res.is_mcmc_allowed is False
    assert res.verdict in ClosureVerdict


def test_closure_both_arms(claude_rows):
    for arm in ("D_csv", "D_eff"):
        res = run_k_a_closure_test(claude_rows, H_OBS, SIGMA_H, arm=arm)
        assert res.rms_indep_k < 999.0


def test_h_mult_anchor_row(claude_params):
    H = h_mult_from_params_list(claude_params, 4.5, 18.0, 73.0)
    assert abs(H[0] - 73.0) < 1e-9


def test_rms_sigma_perfect():
    assert rms_sigma_h([73.0, 80.0], [73.0, 80.0], [1.0, 2.0]) == pytest.approx(0.0)


def test_k_a_virial_kinetic_positive():
    assert k_a_virial_kinetic(3.16e14, 1.73) > 0
