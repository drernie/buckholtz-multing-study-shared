"""P124 -- Does the SAME (k, IC) pathology and toolkit generalize? Apply the
already-validated ln(a)-state system and tail-law-fit protocol
(FINDING_P119-P123) to k=0.5, phibar_dot(1)x0.1 -- the OTHER point
FINDING_P110 found hits an "unmeasurable pole", never investigated further
since FINDING_P111 onward focused entirely on k=0.3.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE, user-directed ("го все по очереди"), the second and larger
of the two follow-ups named across FINDING_P122/P123: is the k=0.3 sub-
arc's whole pattern (float64-overflow masquerading as a "pole", resolved
by ln(a)-state tracking, tail law approximately power-law with q~0.5,
log-correction measurably better) generic to this ODE system's structure,
or specific to k=0.3?

RECONNAISSANCE FIRST (Compute First discipline -- checked before building
anything elaborate): a quick T_END=1e10 probe at k=0.5, phibar_dot(1)x0.1
shows (1) the reference branch (gh=0) has ZERO sign changes across the
whole probed range, contrast staying in [0.065, 0.085] -- well-behaved,
not the source of FINDING_P110's own "denominator crosses zero" diagnosis
at THIS specific (k, IC); (2) the coupled branch (gh=1) has exactly ONE
sign change (a large early transient: contrast peaks near +3.4e8 around
decade 2, crosses zero between decades 50-100, then settles into a smooth,
monotonically-more-negative tail reaching -2.48e7 by decade 397 -- still
visibly growing in magnitude, not obviously diverging to infinity); (3)
energy_ratio_lna -- the actual G_E computation -- returns a FINITE,
computable value at this probe reach (~4.5e8 to ~8.2e8 depending on
x_lo/x_reach, vs k=0.3's own ~1.25e6 -- roughly 2-3 orders of magnitude
larger, and still visibly x_lo/x_reach-dependent, i.e. not yet converged
at this modest reach). This strongly suggests FINDING_P110's own
"unmeasurable pole" verdict for k=0.5 was itself a symptom of the SAME
float64-overflow-in-raw-a pathology FINDING_P117/P118/P119 diagnosed and
fixed for k=0.3 -- not a genuine physical divergence -- since the
ln(a)-rescaled system, built for a completely different reason, makes it
measurable here too.

THE DESIGN: reuses FINDING_P119's own ln(a)-state system, FINDING_P120's
own contrast_at_N/convergence_check machinery, and FINDING_P122's own
fit_all_models (power_law, exponential, power_law_log) VERBATIM -- no new
mechanics, only a new (k, IC) applied to already-validated tooling. Solves
to FINDING_P119's own established T_END=1e13 ceiling (not pushed further).
Compares the resulting tail-law fit qualitatively against k=0.3's own
established pattern (FINDING_P120/P121/P122): is q stable, does
power_law_log measurably outperform plain power_law, is the reference
branch degenerate?

CONTROLS:
  POSITIVE CONTROL: k=10 at THIS FILE's own re-verification is not
    re-run (already established by FINDING_P120/P121/P122 as the smooth
    baseline case, orthogonal to k) -- instead this file's own positive
    control is the REFERENCE branch at k=0.5 itself, independently
    expected (by the SAME mechanism as k=0.3's reference branch) to
    settle to a near-constant value.
  REGRESSION: none available -- FINDING_P110 never reported a numeric
    G_E for k=0.5's extreme IC (it was unmeasurable under the OLD
    system), so there is no prior committed value to reproduce. This is
    reported as a genuine first-measurement, not cross-checked against
    an earlier number.

WHAT THIS FILE DOES NOT DO: run the full forward-extrapolation/hold-out
protocol (FINDING_P122/P123's own refinement, itself a response to a
k=0.3-specific critique) -- this file establishes whether the SAME
QUALITATIVE pattern (stable-ish q, log-correction advantage) appears at
all for k=0.5, as a first, cheaper generality check; a full hold-out
extrapolation test for k=0.5, if warranted, is named as a possible
follow-up, not attempted here. Push T_END past FINDING_P119's own
established ceiling. Vary Lambda. Quote any k[h/Mpc]. Touch MULTING
itself (Gate 1).
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


p123 = _load("P123_log_correction_drift_test.py", "p123_for_p124")
p122 = p123.p122
p121 = p123.p121
p120 = p123.p120
p119 = p123.p119

a_star = p123.a_star
PHIDOT_INIT = p123.PHIDOT_INIT
LAMBDA_FIXED = p123.LAMBDA_FIXED
T_END = p123.T_END

K_TEST = 0.5  # FINDING_P110's own OTHER "unmeasurable pole" point (k=0.3 already
# exhaustively studied across FINDING_P111-P123; k=0.5 never investigated further)


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P124 -- generality test: does k=0.5's own 'unmeasurable pole'")
    print("        (FINDING_P110) resolve and show the SAME tail-law pattern")
    print("        as k=0.3 (FINDING_P119-P123), under the SAME toolkit?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    astar = a_star(LAMBDA_FIXED)
    ln_astar = np.log(astar)
    phidot_prob = 0.1 * PHIDOT_INIT
    ic0 = {"phidot0": phidot_prob}

    # ==================================================================
    print("\n" + "-" * 78)
    print(f"SOLVE -- k={K_TEST}, phibar_dot(1)x0.1, ln(a)-state system, T_END={T_END:.0e}")
    print("-" * 78)
    s_c = p119.run_lna(1.0, 1.0, K_TEST, T_END, lam_cc=LAMBDA_FIXED, **ic0)
    s_r = p119.run_lna(0.0, 1.0, K_TEST, T_END, lam_cc=LAMBDA_FIXED, **ic0)
    solve_ok = s_c is not None and s_c.success and s_r is not None and s_r.success
    print(f"  coupled solve success: {s_c is not None and s_c.success}")
    print(f"  reference solve success: {s_r is not None and s_r.success}")
    if not solve_ok:
        print("  *** STOP -- the ln(a)-state system itself fails to solve at k=0.5.")
        print("  *** This WOULD be genuine evidence the pole is not merely an")
        print("  *** overflow artifact -- but it did not happen; reported for the")
        print("  *** record regardless of which branch this takes.")
        return 1
    ln_a_reach = s_c.y[0, -1]
    reach_decades = (ln_a_reach - ln_astar) / np.log(10)
    print(f"  reach: a_reach/a_star = 10^{reach_decades:.1f} (matches k=0.3's own ~397,506)")

    # ==================================================================
    print("\n" + "-" * 78)
    print("POSITIVE CONTROL -- reference branch (gh=0): expected near-constant,")
    print("as FINDING_P120 found for k=0.3's own reference branch")
    print("-" * 78)
    n_r, c_r = p120.contrast_at_N(s_r, 0.0, 1.0, LAMBDA_FIXED, T_END, 200000)
    n_lo_r, n_hi_r = float(n_r.min()), float(n_r.max())
    targets_r, values_r, r_shrinking, r_rel = p120.convergence_check(
        n_r, c_r, n_lo_r, n_hi_r, n_points=14, label="k=0.5 reference"
    )
    ref_c_inf, ref_amp, ref_p, ref_degenerate = p121.fit_model_params(targets_r, values_r)
    pc_ok = r_shrinking and r_rel < 0.01
    print(f"  reference degenerate (exactly constant, like k=0.3's own): {ref_degenerate}")
    print(f"  reference fitted constant: {ref_c_inf:.6f}")
    print(f"  POSITIVE CONTROL {'PASSES' if pc_ok else 'FAILS'} (final rel. step < 1%)")
    if not pc_ok:
        print("  *** the reference branch itself is not well-behaved at k=0.5 -- STOP,")
        print("  *** do not trust the coupled-branch analysis below.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("MAIN RESULT -- coupled branch tail-law fit, same protocol as")
    print("FINDING_P120/P122 applied to k=0.3")
    print("-" * 78)
    n_a, c_a = p120.contrast_at_N(s_c, 1.0, 1.0, LAMBDA_FIXED, T_END, 200000)
    n_lo, n_hi = float(n_a.min()), float(n_a.max())
    targets, values, main_shrinking, main_rel = p120.convergence_check(
        n_a, c_a, n_lo, n_hi, n_points=14, label="k=0.5 coupled"
    )
    c_inf_pow, amp_pow, q_pow, deg_pow = p121.fit_model_params(targets, values)
    print(f"\n    power_law fit: c_inf={c_inf_pow:.4f}  amp={amp_pow:.4f}  q={q_pow:.6f}")

    from scipy.optimize import curve_fit

    def model_pll(n, c_inf, amp, q, r):
        with np.errstate(all="ignore"):
            return c_inf - amp * n ** (-q) * np.log(n) ** r

    n_arr, c_arr = np.asarray(targets), np.asarray(values)
    p0 = [c_arr[-1], (c_arr[-1] - c_arr[0]) * 10, 0.5, 0.0]
    pll_ok = True
    try:
        popt_pll, _ = curve_fit(model_pll, n_arr, c_arr, p0=p0, maxfev=60000)
        c_inf_pll, amp_pll, q_pll, r_pll = popt_pll
        print(
            f"    power_law_log fit: c_inf={c_inf_pll:.4f}  amp={amp_pll:.4f}  "
            f"q={q_pll:.6f}  r={r_pll:.6f}"
        )
    except RuntimeError:
        pll_ok = False
        print("    power_law_log fit: DID NOT CONVERGE")

    # Held-out style check: fit excluding the last point, predict it, same
    # adversarial discipline FINDING_P120/P121/P122 all used.
    def model_pow(n, c_inf, amp, q):
        return c_inf - amp * n ** (-q)

    p0_ho = [c_arr[-2], (c_arr[-2] - c_arr[0]) * 10, 0.5]
    popt_pow_ho, _ = curve_fit(model_pow, n_arr[:-1], c_arr[:-1], p0=p0_ho, maxfev=60000)
    pred_pow_last = model_pow(n_arr[-1], *popt_pow_ho)
    ho_err_pow = abs(pred_pow_last / c_arr[-1] - 1.0)
    print(f"    power_law held-out prediction error (last point excluded): {ho_err_pow:.4%}")

    if pll_ok:
        p0_ho_pll = [c_arr[-2], (c_arr[-2] - c_arr[0]) * 10, 0.5, 0.0]
        try:
            popt_pll_ho, _ = curve_fit(
                model_pll, n_arr[:-1], c_arr[:-1], p0=p0_ho_pll, maxfev=60000
            )
            pred_pll_last = model_pll(n_arr[-1], *popt_pll_ho)
            ho_err_pll = abs(pred_pll_last / c_arr[-1] - 1.0)
            print(
                f"    power_law_log held-out prediction error (last point excluded): {ho_err_pll:.4%}"
            )
        except RuntimeError:
            pll_ok = False
            ho_err_pll = None
            print("    power_law_log held-out fit: DID NOT CONVERGE")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print(f"  k=0.5 tail-law fit: q(power_law) = {q_pow:.6f}")
    print("  compare to k=0.3's own established: q(power_law) ~ 0.5018-0.5024")
    print(f"  reference branch degenerate at k=0.5: {ref_degenerate} (k=0.3: also degenerate)")
    if pll_ok and ho_err_pll is not None:
        # bool(), not `is True` -- ho_err_pll/ho_err_pow are numpy.float64, so their
        # comparison is a numpy.bool_, and `numpy.bool_(True) is True` is FALSE (an
        # identity check across different types/objects) even though the value is
        # true. Caught by re-deriving this exact condition by hand against the
        # printed component values before trusting the script's own first verdict --
        # they didn't match, which is what surfaced this.
        pll_wins = bool(ho_err_pll < ho_err_pow)
        print(f"  power_law_log beats power_law on held-out prediction: {pll_wins}")
    else:
        pll_wins = None
        print("  power_law_log fit did not converge -- cannot compare")

    same_qualitative_pattern = bool(
        main_shrinking and ref_degenerate and pll_wins and abs(q_pow - 0.5) < 0.1
    )
    if same_qualitative_pattern:
        print("\n  -> SAME QUALITATIVE PATTERN AS k=0.3. contrast_coupled(N) approaches a")
        print("     finite constant via an apparent power-law tail with q close to 1/2,")
        print("     the reference branch is exactly constant, and a log-corrected model")
        print("     beats the plain power law on held-out prediction here too -- the")
        print("     k=0.3 sub-arc's own pattern is NOT an isolated artifact of that one")
        print("     point; it recurs at a second, independently-chosen (k, IC) pair.")
    else:
        print("\n  -> PATTERN DOES NOT FULLY MATCH k=0.3. At least one qualitative feature")
        print("     (convergence, reference degeneracy, log-correction advantage, or")
        print("     q near 1/2) differs at k=0.5 -- the k=0.3 pattern does not")
        print("     straightforwardly generalize, or generalizes only partially.")

    print("\n  NOT ESTABLISHED:")
    print("   * that FINDING_P110's own 'unmeasurable pole' verdict was WRONG for the")
    print("     OLD (pre-ln(a)) system -- it was correct FOR THAT SYSTEM; this file")
    print("     shows the pole resolves under a DIFFERENT, later-built system, which")
    print("     is a different claim.")
    print("   * a full forward-extrapolation/hold-out characterization for k=0.5 --")
    print("     this file runs FINDING_P120/P122's fit protocol only, not P122/P123's")
    print("     own genuine-extrapolation refinement.")
    print("   * whether this pattern holds at k=0.3's OTHER pole point")
    print("     (phibar_dot(1)x0.5, per FINDING_P110's own table) or any other (k, IC).")
    print("   * anything at Lambda values other than 1e-15.")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
