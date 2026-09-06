"""Wire experiments/20260906-evidence-authority/E16_e15_propagated_through_refit.py
into pytest tests/ -q -- added in the same session it was written, per this
project's own established discipline (a new E-script without pytest
coverage is exactly the blind spot closed earlier today).
"""

from __future__ import annotations

from E16_e15_propagated_through_refit import (
    CORR_F1,
    CORR_F2,
)
from E16_e15_propagated_through_refit import (
    test_optimizer_confirms_closed_form_identity as _e16_test_optimizer,
)
from E16_e15_propagated_through_refit import (
    test_positive_control_closed_form_identity as _e16_test_closed_form,
)
from E16_e15_propagated_through_refit import (
    test_positive_control_zero_scatter_reduces_to_uncorrected as _e16_test_zero_scatter,
)


def test_positive_control_zero_scatter_reduces_to_uncorrected():
    _e16_test_zero_scatter()


def test_positive_control_closed_form_identity():
    _e16_test_closed_form()


def test_optimizer_confirms_closed_form_identity():
    _e16_test_optimizer()


def test_correction_factors_match_e15():
    """Regression guard: CORR_F1/CORR_F2 must match E15's own reported
    values (1.1276, 1.6164) at the same real sigma=0.49 -- these two
    scripts must never silently drift apart on the same input."""
    assert abs(CORR_F1 - 1.1276) < 0.0005
    assert abs(CORR_F2 - 1.6164) < 0.0005
