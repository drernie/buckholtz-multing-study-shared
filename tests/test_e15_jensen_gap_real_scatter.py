"""Wire experiments/20260906-evidence-authority/E15_jensen_gap_real_scatter.py
into pytest tests/ -q.
"""

from __future__ import annotations

import numpy as np
from E15_jensen_gap_real_scatter import (
    B1_FIT,
    B2_FIT,
    REAL_DATA_ZS,
    SIGMA,
    analytic_correction_f1,
    analytic_correction_f2,
    forces,
)
from E15_jensen_gap_real_scatter import (
    test_positive_control_mc_matches_analytic as _e15_test_mc_matches_analytic,
)
from E15_jensen_gap_real_scatter import (
    test_positive_control_zero_scatter_gives_unity as _e15_test_zero_scatter,
)


def test_positive_control_zero_scatter_gives_unity():
    _e15_test_zero_scatter()


def test_positive_control_mc_matches_analytic():
    rng = np.random.default_rng(20260906)
    _e15_test_mc_matches_analytic(SIGMA, 200_000, rng)


def test_differential_correction_is_material():
    """FINDING_E15's headline number: the F2-vs-F1 differential correction
    exceeds the pre-registered 10% MCID at the real measured sigma=0.49."""
    ratio = analytic_correction_f2(SIGMA) / analytic_correction_f1(SIGMA)
    assert abs(ratio - 1.0) > 0.10


def test_sign_structure_pushes_up_at_all_real_data_points():
    """FINDING_E15's resolved sub-question: at TJB's own fitted (beta1,beta2)
    and his own forces(), the net population-averaging push on F_total is UP
    at every real data redshift -- regression guard for that computed table."""
    corr_f1, corr_f2 = analytic_correction_f1(SIGMA), analytic_correction_f2(SIGMA)
    crossover = (corr_f1 - 1.0) / (corr_f2 - 1.0)
    for z in REAL_DATA_ZS:
        _, f1, f2 = forces(z, B1_FIT, B2_FIT)
        assert abs(f2) / abs(f1) > crossover, z
