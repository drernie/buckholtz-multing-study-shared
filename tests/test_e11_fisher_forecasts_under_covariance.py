"""Wire experiments/20260906-evidence-authority/E11_fisher_forecasts_under_covariance.py
into pytest tests/ -q. E11 already has 4 real test_* functions, parameterised
manually inside `if __name__ == "__main__":` -- this file gives them to pytest
with the same arguments, against the frozen real mm20 fixture instead of a
live fetch.
"""

from __future__ import annotations

import numpy as np
import pytest
from E8_full_covariance_propagation import build_cov_cc, embed_33
from E11_fisher_forecasts_under_covariance import (
    E8_BASELINE_SMALL_EIG,
    P193_ZS,
    make_augmented_chi2_cov,
    small_eig,
)
from E11_fisher_forecasts_under_covariance import (
    test_analytic_matches_fd as _e11_test_analytic_matches_fd,
)
from E11_fisher_forecasts_under_covariance import (
    test_floor_sigma_inf_returns_e8_baseline as _e11_test_floor,
)
from E11_fisher_forecasts_under_covariance import (
    test_positive_control_covariance_is_actually_used as _e11_test_pc_used,
)
from E11_fisher_forecasts_under_covariance import (
    test_regression_zero_modelling_reproduces_p194 as _e11_test_regression_p194,
)
from P194_fisher_dense_scan import (
    B1_FIT,
    B2_FIT,
    BOUNDARY_Z,
    H0A_FIT,
    Z_SHOES,
    H_of_z_kms,
    _dense_zgrid_through,
)

_COMPS_BY_NAME = {"Moresco default": ["spsooo", "imf"], "stress": ["sps", "imf"]}


@pytest.fixture(scope="module")
def variants(mm20_real):
    return {
        "diag (P193/P194)": None,
        "Moresco default": embed_33(build_cov_cc(mm20_real, ["spsooo", "imf"], None)),
        "stress": embed_33(build_cov_cc(mm20_real, ["sps", "imf"], None)),
    }


def test_regression_zero_modelling_reproduces_p194(mm20_real):
    _e11_test_regression_p194(mm20_real)


@pytest.mark.parametrize("name", ["Moresco default", "stress"])
def test_floor_sigma_inf_returns_e8_baseline(variants, name):
    chi2c = make_augmented_chi2_cov(variants[name])
    _e11_test_floor(chi2c, E8_BASELINE_SMALL_EIG[name])


@pytest.mark.parametrize("name", ["Moresco default", "stress"])
def test_analytic_matches_fd_baseline_and_augmented(variants, name):
    chi2c = make_augmented_chi2_cov(variants[name])
    _e11_test_analytic_matches_fd(variants[name], chi2c, [], None, 0.05)
    _e11_test_analytic_matches_fd(variants[name], chi2c, P193_ZS, 0.10, 0.10)


@pytest.mark.parametrize("name", ["Moresco default", "stress"])
def test_positive_control_covariance_is_actually_used(mm20_real, name):
    _e11_test_pc_used(mm20_real, name, _COMPS_BY_NAME[name])


def test_ceiling_agrees_across_error_models(variants):
    """PC4: as sigma_synth->0 the synthetic term dominates and the small
    eigenvalue must agree across all 3 error models to <1% -- the ceiling
    a silently-wrong covariance construction would not reach."""
    ce = {name: small_eig(C, P193_ZS, 1e-6) for name, C in variants.items()}
    spread = (max(ce.values()) - min(ce.values())) / max(ce.values())
    assert spread < 0.01, f"ceiling spread {spread:.2%}"


def test_domain_boundary_unchanged():
    """PC5: the H(z) domain boundary depends on the fiducial model only, not
    on the error model -- must be unchanged from P194's own value."""
    zb = _dense_zgrid_through(np.array([BOUNDARY_Z + 0.05]))
    Hb = H_of_z_kms(zb, H0A_FIT, B1_FIT, B2_FIT, Z_SHOES)
    assert np.any(np.isnan(Hb[zb > BOUNDARY_Z]))
    assert not np.any(np.isnan(Hb[zb <= 16.5]))
