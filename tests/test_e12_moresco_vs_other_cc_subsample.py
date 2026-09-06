"""Wire experiments/20260906-evidence-authority/E12_moresco_vs_other_cc_subsample.py
into pytest tests/ -q.
"""

from __future__ import annotations

from E12_moresco_vs_other_cc_subsample import (
    test_positive_control_regression_union_matches_direct_fit as _e12_test_pc,
)


def test_positive_control_regression_union_matches_direct_fit():
    _e12_test_pc()
