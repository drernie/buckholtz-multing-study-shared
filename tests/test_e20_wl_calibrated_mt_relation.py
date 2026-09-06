"""Wire experiments/20260906-evidence-authority/independent_verification_rerun/
E20_wl_calibrated_mt_relation.py into pytest tests/ -q -- added same
session, per this project's own established discipline.
"""

from __future__ import annotations

from E20_wl_calibrated_mt_relation import (
    KETTULA_FITS,
    V82_M0_MSUN,
    V82_T0_KEV,
    kettula_predicted_temperature,
)
from E20_wl_calibrated_mt_relation import (
    test_positive_control_pivot_recovered as _test_pc1,
)


def test_positive_control_pivot_recovered():
    _test_pc1()


def test_v82_t0_sits_outside_bias_corrected_scatter_band():
    """Regression guard: the headline numeric result (v82's own T0 sits
    OUTSIDE the +/-1 intrinsic-scatter band of the bias-corrected
    Kettula+2014 relation, on the low side) -- if this ever flips, the
    underlying fit constants or v82's own T0 have silently changed."""
    t_bc = kettula_predicted_temperature(V82_M0_MSUN, "bias_corrected")
    scatter_factor = 10.0 ** KETTULA_FITS["bias_corrected"]["sigma_dex"]
    t_lo, t_hi = t_bc / scatter_factor, t_bc * scatter_factor
    assert V82_T0_KEV < t_lo, (V82_T0_KEV, t_lo, t_hi)


def test_v82_t0_lower_than_both_kettula_variants():
    """v82's own T0 is lower than both Kettula+2014 sub-variants at v82's
    own M0 -- the direction of the residual gap this FINDING reports."""
    for fit_key in KETTULA_FITS:
        t_pred = kettula_predicted_temperature(V82_M0_MSUN, fit_key)
        assert V82_T0_KEV < t_pred, (fit_key, V82_T0_KEV, t_pred)
