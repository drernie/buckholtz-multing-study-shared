"""Wire experiments/20260906-evidence-authority/E17_mass_scatter_for_F0_Faccretion.py
into pytest tests/ -q -- added same session, per this project's own
established discipline (a new E-script without pytest coverage recreates
the exact blind spot closed earlier today).
"""

from __future__ import annotations

from E17_mass_scatter_for_F0_Faccretion import (
    A_COSMO_PLANCK,
    SIGMA_LOG10_C200_DUFFY08,
)
from E17_mass_scatter_for_F0_Faccretion import (
    test_positive_control_reuse_matches_p196_addendum as _e17_test_reuse,
)
from E17_mass_scatter_for_F0_Faccretion import (
    test_positive_control_z_zero_boundary as _e17_test_z_zero,
)
from E17_mass_scatter_for_F0_Faccretion import (
    test_positive_control_zero_scatter_gives_unity_jensen as _e17_test_zero_scatter,
)


def test_positive_control_zero_scatter_gives_unity_jensen():
    _e17_test_zero_scatter()


def test_positive_control_z_zero_boundary():
    _e17_test_z_zero()


def test_positive_control_reuse_matches_p196_addendum():
    _e17_test_reuse()


def test_constants_are_the_sourced_real_values():
    """Regression guard: SIGMA_LOG10_C200_DUFFY08 must match Duffy+2008's
    own quoted value, and A_COSMO_PLANCK must match Correa+2015's own
    quoted Planck-cosmology constant -- neither should silently drift."""
    assert SIGMA_LOG10_C200_DUFFY08 == 0.15
    assert A_COSMO_PLANCK == 798.0
