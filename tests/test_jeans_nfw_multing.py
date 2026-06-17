"""Tests for N-8 Jeans+NFW+MULTING module — physics sanity, not validation."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

import jeans_nfw_multing as jm  # noqa: E402


def test_nfw_mass_recovers_M500():
    M500, c, R500 = 3e14, 4.5, 1.3
    rs = R500 / c
    rho_s = jm.nfw_rho_s(M500, c, R500)
    m = jm.nfw_mass(np.array([R500]), rho_s, rs)[0]
    assert abs(m - M500) / M500 < 1e-6


def test_nfw_mass_monotone_increasing():
    rs, rho_s = 0.29, 1e15
    r = np.linspace(0.05, 3, 50)
    m = jm.nfw_mass(r, rho_s, rs)
    assert np.all(np.diff(m) > 0)


def test_g_newton_positive_and_falls_at_large_r():
    rs, rho_s = 0.29, 1e15
    r = np.linspace(0.5, 5, 50)
    g = jm.g_newton(r, rho_s, rs)
    assert np.all(g > 0)
    # beyond the mass it should fall roughly as ~1/r^2 (decreasing)
    assert g[-1] < g[0]


def test_jeans_sigma_positive():
    rs, rho_s = 0.29, jm.nfw_rho_s(3e14, 4.5, 1.3)
    r = np.linspace(0.05, 13, 2000)
    rho = jm.nfw_rho(r, rho_s, rs)
    g = jm.g_newton(r, rho_s, rs)
    sr2 = jm.jeans_sigma_r2(r, rho, g)
    # last grid point is 0 by construction (integral_rmax^rmax = 0); check interior
    assert np.all(sr2[:-1] > 0)


def test_standard_sigma_v_realistic():
    """Massive cluster sigma_v should be ~700-1300 km/s."""
    res = jm.run()
    assert 600 < res["sigma_v_std_kms"] < 1400


def test_multing_epsilon_negligible_at_physical_kA():
    """Core claim: at k_A=E_ICM/c^2 the dipole correction is tiny (<1% at R500)."""
    rs, rho_s = 0.29, jm.nfw_rho_s(3e14, 4.5, 1.3)
    eps = jm.multing_epsilon(np.array([1.3]), 4.5, 7e8, rho_s, rs)[0]
    assert abs(eps) < 1e-2


def test_multing_effect_on_sigma_v_far_below_claimed():
    """'+7.2%' must NOT reproduce — physical effect is orders of magnitude smaller."""
    res = jm.run()
    assert abs(res["delta_percent"]) < 1.0  # nowhere near 7.2%


def test_epsilon_is_repulsive_negative():
    rs, rho_s = 0.29, jm.nfw_rho_s(3e14, 4.5, 1.3)
    eps = jm.multing_epsilon(np.array([0.5, 1.3]), 4.5, 7e8, rho_s, rs)
    assert np.all(eps < 0)  # dipole repulsion weakens gravity


def test_pytest_approx_helper():
    assert math.isclose(jm.G, 4.30091e-9, rel_tol=1e-6)
