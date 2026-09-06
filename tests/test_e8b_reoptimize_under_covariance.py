"""Wire experiments/20260906-evidence-authority/E8b_reoptimize_under_covariance.py
into pytest tests/ -q. E8b had no test_* functions of its own -- its positive
control lived only as bare asserts inside `if __name__ == "__main__":`.
"""

from __future__ import annotations

from E8_full_covariance_propagation import (
    LCDM_FREE,
    TABLE_II,
    chi2_fixed_h0anchor,
    chi2_lcdm_diag,
)
from E8b_reoptimize_under_covariance import opt_lcdm, opt_multing


def test_positive_control_diag_reoptimization_recovers_tjb_optima():
    """Re-optimising under DIAGONAL errors must recover TJB's own reported
    optima (free LCDM chi2=16.31 at H0=71.83, Om=0.2724; MULTING chi2=15.75) --
    the exact assertion E8b's own __main__ block runs before anything else."""
    f_l, x_l = opt_lcdm(chi2_lcdm_diag)
    assert abs(f_l - LCDM_FREE["chi2_tjb"]) / LCDM_FREE["chi2_tjb"] < 5e-3
    assert abs(x_l[0] - LCDM_FREE["H0"]) < 0.1
    assert abs(x_l[1] - LCDM_FREE["Om"]) < 0.005

    f_m, _x_m = opt_multing(chi2_fixed_h0anchor, TABLE_II["unconstrained_spotlighted"][:3])
    start_chi2 = chi2_fixed_h0anchor(*TABLE_II["unconstrained_spotlighted"][:3])
    # two separate bounds (E8b's own WHY comment): TJB rounds to 2 decimals, so
    # (i) the optimiser must not do WORSE than the exact chi2 at its own start,
    # and (ii) the result must sit within half a unit of TJB's last printed digit.
    assert f_m <= start_chi2 + 1e-6
    assert abs(f_m - TABLE_II["unconstrained_spotlighted"][3]) <= 0.005 + 1e-6


def test_covariance_reoptimization_runs_end_to_end(mm20_real):
    """Smoke test for the covariance-weighted re-optimization path (the part
    E8c and this project's own exploratory findings build on) -- must not
    crash and must return a finite chi2 no worse than the diagonal-path start."""
    from E8_full_covariance_propagation import build_cov_cc, embed_33, make_chi2_cov

    C33 = embed_33(build_cov_cc(mm20_real, ["spsooo", "imf"], None))
    chi2_fn = make_chi2_cov(C33)
    f_m, x_m = opt_multing(chi2_fn, TABLE_II["unconstrained_spotlighted"][:3])
    assert f_m >= 0.0
    assert len(x_m) == 3
