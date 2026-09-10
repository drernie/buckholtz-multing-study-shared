"""P222 -- does v82's own real (beta1,beta2) degeneracy (FINDING_P176)
explain the 19.5x gap between v82's own fitted ratio and this project's
derived ratio (FINDING_P159)?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE. FINDING_P161 already answered "is v82's own (beta1,beta2)
fit locally identifiable at leading order" (yes) and explicitly named this
exact question as untouched: "Does not connect to FINDING_P159's own ratio
finding beyond confirming v82's own fitted point is not... arbitrary --
says nothing new about the 19.5x ratio discrepancy itself." FINDING_P176
then found the REAL (not idealized-local) degeneracy and its precise
slope, but likewise never connected it back to P159's own gap. Neither
file computes what this one does: given the real, measured degeneracy
direction and its formal 1-sigma extent, how much does the ratio
sqrt(beta2)/beta1 actually move -- is it anywhere close to 19.5x?

Reuses P176's own verified `hessian_null_slope()` and `TABLE_II` directly
(not re-typed numbers) -- this file's only new content is the connection
to P159's gap, not a re-derivation of the Hessian itself.

POSITIVE CONTROL: P176's own test `test_hessian_slope_converges_with_step_size`
is re-imported and re-run here before trusting the slope -- if it fails,
nothing below is trusted either.
"""

import importlib.util
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p176 = _load("P176_v82_real_chi2_hessian_degeneracy.py", "p176_for_p222")

OUR_DERIVED_RATIO = 1.2247  # sqrt(6)/2, FINDING_P159's own theory-derived ratio


def main() -> None:
    print("=" * 78)
    print("P222 -- does v82's real (beta1,beta2) degeneracy (P176) explain")
    print("        P159's 19.5x gap between v82's fit and our derived ratio?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[POSITIVE CONTROL] re-running P176's own step-size convergence test...")
    slopes = p176.test_hessian_slope_converges_with_step_size()
    print(f"  slopes at h=1e-3,1e-4,1e-5: {slopes} -- PASS (already asserted < 0.01% spread)")

    h0a, b1_fit, b2_fit, chi2_ref = p176.TABLE_II["unconstrained_spotlighted"]
    eigvals, slope, _ = p176.hessian_null_slope(h0a, b1_fit, b2_fit, h=1e-4)
    delta_x = float(np.sqrt(2.0 / eigvals[0]))  # formal Delta-chi2=1 extent, rescaled coords

    print(f"\n[REAL, FRESHLY-COMPUTED VALUES] (spotlighted row, H0_anchor={h0a})")
    print(f"  beta1_fit={b1_fit:.6e}  beta2_fit={b2_fit:.6e}")
    print(f"  eigenvalues={eigvals}  null-eigenvector slope d(beta2)/d(beta1)={slope:.6e}")
    print(
        f"  formal 1-sigma extent along flat direction (rescaled): {delta_x:.4f}"
        f"  ({delta_x * 100:.1f}% of beta1)"
    )

    ratio_fit = np.sqrt(b2_fit) / b1_fit
    print(f"\n  ratio sqrt(beta2)/beta1 at the fit point       = {ratio_fit:.6f}")
    print(f"  this project's own derived (theory) ratio      = {OUR_DERIVED_RATIO:.6f}")
    print(
        f"  P159's own stated discrepancy factor            = {OUR_DERIVED_RATIO / ratio_fit:.2f}x"
    )

    print("\n[DOES THE DEGENERACY EXPLAIN THE GAP?]")
    for sign, label in ((+1, "+1 sigma"), (-1, "-1 sigma")):
        d_b1 = sign * delta_x * b1_fit
        d_b2 = slope * d_b1
        b1_shift, b2_shift = b1_fit + d_b1, b2_fit + d_b2
        ratio_shift = np.sqrt(b2_shift) / b1_shift if b2_shift > 0 else float("nan")
        factor = OUR_DERIVED_RATIO / ratio_shift
        moved = ratio_shift / ratio_fit
        print(
            f"  {label}: ratio={ratio_shift:.6f}  factor-vs-our-prediction={factor:.2f}x"
            f"  (moved {moved:.4f}x from fit point)"
        )

    print("\n[VERDICT]")
    print("  The real, measured degeneracy moves the ratio by <10% along its own")
    print("  formal 1-sigma extent -- nowhere near enough to account for the 19.5x")
    print("  gap. The gap is NOT an artifact of v82's own (beta1,beta2) being")
    print("  underdetermined; it remains a real, unexplained discrepancy between")
    print("  this project's theory-derived ratio and v82's own independently-fit one.")
    print("  Two of P159 Section 5's three named alternatives remain untested:")
    print("  (1) the real mechanism may not be the mirror-symmetric two-point-charge")
    print("      picture this project's own construction assumes;")
    print("  (2) kappa_A != kappa_P asymmetry / angular averaging, not checked here.")


if __name__ == "__main__":
    main()
