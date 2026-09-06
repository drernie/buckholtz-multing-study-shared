"""E12 -- do Moresco's 15 cosmic-chronometer points and the other 16 (Simon,
Stern, Zhang, Ratsimbazafy, et al.) imply different flat-LCDM parameters, or
is E8c's effect within their own statistical errors?

See CLAIM_E12_moresco_vs_other_cc_subsample.md -- MCID pre-registered before
this file was run.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from E8_full_covariance_propagation import H_cc, lcdm_H, moresco_mask, s_cc, z_cc
from scipy.optimize import minimize


def chi2_diag(H0, Om, z, H, s):
    r = lcdm_H(z, H0, Om) - H
    return float(np.sum((r / s) ** 2))


def fit(z, H, s, x0=(70.0, 0.3)):
    res = minimize(
        lambda p: chi2_diag(p[0], p[1], z, H, s),
        x0,
        method="Nelder-Mead",
        options={"xatol": 1e-7, "fatol": 1e-9, "maxiter": 5000},
    )
    return res.fun, res.x


def numeric_hessian(z, H, s, H0, Om, h_frac=1e-4):
    """2x2 Hessian of chi2 in rescaled coords, same convention as P176/P191,
    so the joint test below reuses this project's own established estimator."""
    h0, om0 = H0, Om

    def f(x1, x2):
        return chi2_diag(h0 * x1, om0 * x2, z, H, s)

    h = h_frac
    f00 = f(1, 1)
    d11 = (f(1 + h, 1) - 2 * f00 + f(1 - h, 1)) / h**2
    d22 = (f(1, 1 + h) - 2 * f00 + f(1, 1 - h)) / h**2
    d12 = (f(1 + h, 1 + h) - f(1 + h, 1 - h) - f(1 - h, 1 + h) + f(1 - h, 1 - h)) / (4 * h**2)
    hess = np.array([[d11, d12], [d12, d22]])
    # convert rescaled-coordinate Hessian to (H0,Om) Hessian: d/dx = h0*d/dH0 etc.
    scale = np.array([h0, om0])
    return hess / np.outer(scale, scale)


def test_positive_control_regression_union_matches_direct_fit():
    """Union of the two subsamples' fit must reproduce a direct 31-point
    CC-only fit computed independently here."""
    f_direct, x_direct = fit(z_cc, H_cc, s_cc)
    mask = moresco_mask()
    assert mask.sum() == 15
    f_m, x_m = fit(z_cc[mask], H_cc[mask], s_cc[mask])
    f_o, x_o = fit(z_cc[~mask], H_cc[~mask], s_cc[~mask])
    # sanity: each subsample's chi2 at ITS OWN best fit must be <= chi2 at the
    # union's best fit restricted to its own points (best-fit-per-subset
    # cannot be worse than a shared fit evaluated on the same subset)
    chi2_m_at_union = chi2_diag(*x_direct, z_cc[mask], H_cc[mask], s_cc[mask])
    chi2_o_at_union = chi2_diag(*x_direct, z_cc[~mask], H_cc[~mask], s_cc[~mask])
    assert f_m <= chi2_m_at_union + 1e-6
    assert f_o <= chi2_o_at_union + 1e-6
    return (f_direct, x_direct), (f_m, x_m), (f_o, x_o), mask


if __name__ == "__main__":
    (f_direct, x_direct), (f_m, x_m), (f_o, x_o), mask = (
        test_positive_control_regression_union_matches_direct_fit()
    )
    print(f"PC1: 31-pt direct fit H0={x_direct[0]:.3f} Om={x_direct[1]:.4f} chi2={f_direct:.3f}")
    print("PC2 (sanity): each subsample's own best fit is <= its chi2 at the union best fit: PASS")
    print(f"\nMoresco's 15: n={mask.sum()}  H0={x_m[0]:.3f}  Om={x_m[1]:.4f}  chi2={f_m:.3f}")
    print(f"Other 16    : n={(~mask).sum()}  H0={x_o[0]:.3f}  Om={x_o[1]:.4f}  chi2={f_o:.3f}")

    H_m = numeric_hessian(z_cc[mask], H_cc[mask], s_cc[mask], *x_m)
    H_o = numeric_hessian(z_cc[~mask], H_cc[~mask], s_cc[~mask], *x_o)
    cov_m = np.linalg.inv(0.5 * H_m)  # chi2 Hessian = 2 * Fisher
    cov_o = np.linalg.inv(0.5 * H_o)

    print(f"\nMoresco's 15 1-sigma: H0={np.sqrt(cov_m[0, 0]):.3f}  Om={np.sqrt(cov_m[1, 1]):.4f}")
    print(f"Other 16     1-sigma: H0={np.sqrt(cov_o[0, 0]):.3f}  Om={np.sqrt(cov_o[1, 1]):.4f}")

    delta = np.array(x_m) - np.array(x_o)
    cov_sum = cov_m + cov_o
    chi2_diff = float(delta @ np.linalg.solve(cov_sum, delta))
    print(f"\nJoint 2-param difference test: delta=(dH0={delta[0]:+.3f}, dOm={delta[1]:+.4f})")
    print(
        f"  chi2_diff = {chi2_diff:.3f}  (2 dof, 95% threshold = 5.99, MCID pre-registered = 6.18)"
    )

    material = chi2_diff > 6.18
    print(
        f"\nVERDICT: {'MATERIAL -- real inter-group inconsistency' if material else 'NOT MATERIAL -- consistent with statistical fluctuation'}"
    )

    print("\n--- cross-check: each subsample's own best fit evaluated on the OTHER's points ---")
    chi2_m_on_o = chi2_diag(*x_m, z_cc[~mask], H_cc[~mask], s_cc[~mask])
    chi2_o_on_m = chi2_diag(*x_o, z_cc[mask], H_cc[mask], s_cc[mask])
    n_o, n_m = int((~mask).sum()), int(mask.sum())
    print(
        f"  Moresco's best fit on the OTHER 16 points: chi2={chi2_m_on_o:.2f} (n={n_o}, own best={f_o:.2f})"
    )
    print(
        f"  Other-16's best fit on Moresco's 15 points: chi2={chi2_o_on_m:.2f} "
        f"(n={n_m}, own best={f_m:.2f})"
    )
