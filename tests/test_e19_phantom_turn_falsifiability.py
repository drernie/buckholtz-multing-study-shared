"""Wire experiments/20260906-evidence-authority/independent_verification_rerun/
E19_phantom_turn_falsifiability.py into pytest tests/ -q -- added same
session, per this project's own established discipline.
"""

from __future__ import annotations

from E19_phantom_turn_falsifiability import (
    find_h_minimum_real,
    load_cc_data,
    signal_vs_noise_absolute,
)
from E19_phantom_turn_falsifiability import (
    test_minimum_stable_across_grid_density as _test_rc1,
)
from E19_phantom_turn_falsifiability import (
    test_positive_control_anchor_recovered_trivial as _test_pc2,
)
from E19_phantom_turn_falsifiability import (
    test_positive_control_synthetic_known_minimum as _test_pc1,
)
from E19_phantom_turn_falsifiability import (
    test_sign_change_confirms_genuine_local_minimum_extended_range as _test_sc1,
)


def test_positive_control_synthetic_known_minimum():
    _test_pc1()


def test_positive_control_anchor_recovered_trivial():
    _test_pc2()


def test_sign_change_extended_range():
    _test_sc1()


def test_minimum_stable_across_grid_density():
    _test_rc1()


def test_dip_is_well_below_nearest_point_sigma():
    """Regression guard: the dip must stay well below the two nearest
    real CC points' own quoted sigma (this file's own headline result) --
    if this ever flips, the underlying beta values or CC data have
    silently changed."""
    from E19_phantom_turn_falsifiability import TABLE_II

    row = TABLE_II["unconstrained_spotlighted"]
    z_min, H_min, H_today, _zg, _Hg = find_h_minimum_real(
        row["beta_1"], row["beta_2"], row["H0_anchor_kms"]
    )
    cc = load_cc_data()
    _z_lowest, _H_lowest, sigma_lowest = cc[0]
    _dip_abs, ratio = signal_vs_noise_absolute(H_today, H_min, sigma_lowest)
    assert ratio < 0.5, ratio
