"""
Tests for clean_room_v25_reimplementation.py

Labels: OUR_RECONSTRUCTION - NOT_AUTHOR_CONFIRMED - NOT_VALIDATION - NOT_REFUTATION

These tests exist specifically because Agent(reviewer) caught a real bug in this
script (h_of_z pinned to a constant instead of solved self-consistently, 2026-07-24)
that ran cleanly, produced plausible numbers, and would not have announced itself
without a targeted check. See docs/140 section 3.2 for the full account.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from clean_room_v25_reimplementation import (
    f_p_identical_nodes,
    h_accretion_frozen_anchor,
    h_branch,
    h_no_accretion,
    h_self_consistent,
    integrate_h_of_z,
    m_x,
    solve_s0,
)

BETA1 = 1.28e10
BETA2 = 7.10e17
H0_ANCHOR = 76.46
M0_WORKING = 8e14
M0_NO_SOLUTION = 4e14


def _r0_for(m0: float) -> float:
    rho_crit0 = 2.775e11 * 0.674**2
    return (3 * m0 / (4 * np.pi * 500 * rho_crit0)) ** (1.0 / 3.0)


R0_WORKING = _r0_for(M0_WORKING)
R0_NO_SOLUTION = _r0_for(M0_NO_SOLUTION)


class TestHSelfConsistentSatisfiesItsOwnEquation:
    """h_self_consistent solves mu*s*H^2 + b_coef*H - F_P = 0 exactly -- verify the
    returned H actually satisfies that equation, not just that it runs."""

    # s values chosen to be within the physically-valid (real-H) region at each
    # z for M0_WORKING -- smaller s (e.g. 10-20 Mpc) is invalid here (NaN), see
    # test_nan_where_no_real_solution below for that boundary explicitly.
    @pytest.mark.parametrize("s,z", [(50.0, 0.0), (50.0, 0.5), (50.0, 1.5)])
    def test_residual_is_zero(self, s: float, z: float) -> None:
        h_z = h_self_consistent(s, z, BETA1, BETA2, M0_WORKING, R0_WORKING)
        assert np.isfinite(h_z), "expected a real solution at this (s, z)"
        mu = m_x(z, M0_WORKING) / 2.0
        fp = f_p_identical_nodes(s, z, BETA1, BETA2, M0_WORKING, R0_WORKING)
        from clean_room_v25_reimplementation import f_acc

        residual = mu * s * h_z**2 + f_acc(z, h_z, M0_WORKING, R0_WORKING) - fp
        assert abs(residual) < 1e-6 * abs(fp)

    def test_nan_where_no_real_solution(self) -> None:
        h_z = h_self_consistent(1e-6, 0.0, BETA1, BETA2, M0_WORKING, R0_WORKING)
        assert not np.isfinite(h_z)


class TestBranchDispatch:
    """h_branch is the single dispatch point for the A/B/C ablation -- verify it
    actually routes to the right formula and rejects unknown branches."""

    def test_branch_a_matches_h_no_accretion(self) -> None:
        s, z = 50.0, 0.5
        assert h_branch("A", s, z, BETA1, BETA2, M0_WORKING, R0_WORKING, H0_ANCHOR) == pytest.approx(
            h_no_accretion(s, z, BETA1, BETA2, M0_WORKING, R0_WORKING)
        )

    def test_branch_b_matches_h_accretion_frozen_anchor(self) -> None:
        s, z = 50.0, 0.5
        expected = h_accretion_frozen_anchor(s, z, BETA1, BETA2, M0_WORKING, R0_WORKING, H0_ANCHOR)
        assert h_branch("B", s, z, BETA1, BETA2, M0_WORKING, R0_WORKING, H0_ANCHOR) == pytest.approx(
            expected
        )

    def test_branch_c_matches_h_self_consistent(self) -> None:
        s, z = 50.0, 0.5
        expected = h_self_consistent(s, z, BETA1, BETA2, M0_WORKING, R0_WORKING)
        assert h_branch("C", s, z, BETA1, BETA2, M0_WORKING, R0_WORKING, H0_ANCHOR) == pytest.approx(
            expected
        )

    def test_unknown_branch_raises(self) -> None:
        with pytest.raises(ValueError, match="Unknown branch"):
            h_branch("D", 50.0, 0.5, BETA1, BETA2, M0_WORKING, R0_WORKING, H0_ANCHOR)

    def test_branches_b_and_c_agree_only_at_z_zero(self) -> None:
        s0 = solve_s0(BETA1, BETA2, H0_ANCHOR, M0_WORKING, R0_WORKING, branch="C")
        h_b_z0 = h_branch("B", s0, 0.0, BETA1, BETA2, M0_WORKING, R0_WORKING, H0_ANCHOR)
        h_c_z0 = h_branch("C", s0, 0.0, BETA1, BETA2, M0_WORKING, R0_WORKING, H0_ANCHOR)
        assert h_b_z0 == pytest.approx(h_c_z0, rel=1e-6)

        # NOTE (2026-07-24 finding, docs/140 section 3.3b): B and C stay close
        # (within a few percent) everywhere, not just at z=0 -- so this can't
        # assert a LARGE divergence away from z=0. The real regression to guard
        # against is B silently becoming bit-identical to C (e.g. someone routes
        # branch "B" through h_self_consistent by mistake) -- a tight tolerance
        # catches that without contradicting today's actual (small-divergence)
        # finding.
        s_mid, z_mid = 50.0, 0.7
        h_b_mid = h_branch("B", s_mid, z_mid, BETA1, BETA2, M0_WORKING, R0_WORKING, H0_ANCHOR)
        h_c_mid = h_branch("C", s_mid, z_mid, BETA1, BETA2, M0_WORKING, R0_WORKING, H0_ANCHOR)
        assert h_b_mid != pytest.approx(h_c_mid, rel=1e-4)


class TestSolveS0Closure:
    def test_closure_reproduces_h0_anchor(self) -> None:
        s0 = solve_s0(BETA1, BETA2, H0_ANCHOR, M0_WORKING, R0_WORKING, branch="C")
        h_at_s0 = h_self_consistent(s0, 0.0, BETA1, BETA2, M0_WORKING, R0_WORKING)
        assert h_at_s0 == pytest.approx(H0_ANCHOR, rel=1e-8)

    def test_no_solution_mass_raises(self) -> None:
        with pytest.raises(RuntimeError, match="No s0 solves"):
            solve_s0(BETA1, BETA2, H0_ANCHOR, M0_NO_SOLUTION, R0_NO_SOLUTION, branch="C")


class TestBranchAblationRegression:
    """Encodes the 2026-07-24 finding (docs/140 section 3.3b): removing F_acc
    entirely (branch A) does NOT fix the non-monotonic shape."""

    def test_all_three_branches_peak_within_a_few_percent(self) -> None:
        peaks = {}
        for branch in ("A", "B", "C"):
            z_arr, h_arr = integrate_h_of_z(
                BETA1, BETA2, H0_ANCHOR, M0_WORKING, R0_WORKING, z_max=2.5, n_eval=100, branch=branch
            )
            peaks[branch] = float(np.nanmax(h_arr))

        assert peaks["A"] == pytest.approx(peaks["C"], rel=0.05)
        assert peaks["B"] == pytest.approx(peaks["C"], rel=0.05)

    def test_all_three_branches_are_non_monotonic(self) -> None:
        for branch in ("A", "B", "C"):
            z_arr, h_arr = integrate_h_of_z(
                BETA1, BETA2, H0_ANCHOR, M0_WORKING, R0_WORKING, z_max=2.5, n_eval=100, branch=branch
            )
            assert not np.all(np.diff(h_arr) >= -1e-6), f"branch {branch} unexpectedly monotonic"

    def test_h_at_z0_matches_anchor_for_all_branches(self) -> None:
        for branch in ("A", "B", "C"):
            z_arr, h_arr = integrate_h_of_z(
                BETA1, BETA2, H0_ANCHOR, M0_WORKING, R0_WORKING, z_max=2.5, n_eval=50, branch=branch
            )
            assert h_arr[0] == pytest.approx(H0_ANCHOR, rel=1e-6)
