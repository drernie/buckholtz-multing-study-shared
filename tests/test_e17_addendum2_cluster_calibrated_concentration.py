"""Wire experiments/20260906-evidence-authority/
E17_addendum2_cluster_calibrated_concentration.py into pytest tests/ -q --
added same session, per this project's own established discipline (a new
E-script without pytest coverage recreates the exact blind spot closed
earlier today).
"""

from __future__ import annotations

from E17_addendum2_cluster_calibrated_concentration import (
    correa2015_paperIII_concentration_median,
)
from E17_addendum2_cluster_calibrated_concentration import (
    test_positive_control_concentration_is_physically_sane as _test_pc3,
)
from E17_addendum2_cluster_calibrated_concentration import (
    test_positive_control_external_reproduction as _test_pc4,
)
from E17_addendum2_cluster_calibrated_concentration import (
    test_positive_control_z_zero_boundary as _test_pc2,
)
from E17_addendum2_cluster_calibrated_concentration import (
    test_positive_control_zero_scatter_gives_unity_jensen as _test_pc1,
)


def test_positive_control_zero_scatter_gives_unity_jensen():
    _test_pc1()


def test_positive_control_z_zero_boundary():
    _test_pc2()


def test_positive_control_concentration_is_physically_sane():
    _test_pc3()


def test_positive_control_external_reproduction():
    _test_pc4()


def test_concentration_decreases_with_mass_at_fixed_z():
    """Regression guard for the sign convention Step 8a skeptic checked by
    hand: concentration must DECREASE with increasing halo mass at fixed
    z (higher-mass halos formed more recently, are less concentrated)."""
    c_low = correa2015_paperIII_concentration_median(1e12, 0.0)
    c_high = correa2015_paperIII_concentration_median(1e15, 0.0)
    assert c_high < c_low
