"""Wire experiments/20260906-evidence-authority/
E17_addendum3_sigma_sweep_and_exclusion_decomposition.py into
pytest tests/ -q -- added same session, per this project's own
established discipline.
"""

from __future__ import annotations

from E17_addendum3_sigma_sweep_and_exclusion_decomposition import (
    divergence,
    exclusion_rate_matched_comparison,
    sigma_sweep,
)
from E17_addendum3_sigma_sweep_and_exclusion_decomposition import (
    test_positive_control_percentile_matches_natural_cut as _test_pc2,
)
from E17_addendum3_sigma_sweep_and_exclusion_decomposition import (
    test_positive_control_sweep_reproduces_addendum2_at_sigma_015 as _test_pc1,
)


def test_positive_control_sweep_reproduces_addendum2_at_sigma_015():
    _test_pc1()


def test_positive_control_percentile_matches_natural_cut():
    _test_pc2()


def test_sigma_sweep_is_monotonic_with_offset_increasing():
    """Regression guard: offset(z=2.33) must increase monotonically with
    sigma across the sweep (a wider concentration scatter pulls the mean
    mass-history ratio up via the same Jensen-type mechanism E15/E17
    already established) -- if this ever breaks, the sweep's own MC
    machinery has regressed, not just its numeric headline."""
    results = sigma_sweep(n=20_000)
    offsets = [results[s][0][2.33] for s in sorted(results)]
    assert offsets == sorted(offsets), offsets


def test_exclusion_rate_matched_comparison_shift_is_small():
    """Regression guard for Addendum 3's own Part (b) conclusion: forcing
    both concentration sources to a matched exclusion rate must change the
    Duffy->Correa-III divergence shrinkage factor by less than 5% (the
    file's own printed run showed <0.1%) -- confirms the shrinkage is
    driven by the median-relation choice, not the differential truncation
    rate."""
    cmp = exclusion_rate_matched_comparison(n=20_000)
    off_dn, jen_dn, _c, _e = cmp["duffy"]["natural"]
    off_cn, jen_cn, _c2, _e2 = cmp["correa3"]["natural"]
    off_df, jen_df, _c3, _e3 = cmp["duffy"]["forced"]
    div_dn = divergence(off_dn[2.33], jen_dn[2.0][2.33])
    div_cn = divergence(off_cn[2.33], jen_cn[2.0][2.33])
    div_df = divergence(off_df[2.33], jen_df[2.0][2.33])
    shift_natural = div_dn / div_cn
    shift_matched = div_df / div_cn
    assert abs(shift_matched / shift_natural - 1.0) < 0.05
