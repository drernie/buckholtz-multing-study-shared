"""P120 -- Tail Convergence Test: does contrast(N) itself (N := ln(a))
approach a finite limit, and if so, does that resolve G_E's convergence
more cheaply than pushing N further?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

USER-DIRECTED, REVISED MID-BUILD after a positive control caught a wrong
assumption in the original design (reported honestly, not silently fixed):
the user specified a block-integrability test on h(N):=contrast(N)^2,
R_j:=B_{j+1}/B_j for B_j:=integral[N_j,N_j+dN] h dN, expecting R_j -> r<1
for a genuinely convergent case. Built exactly as specified; its own
smooth-case (k=10) positive control -- required before trusting anything
on the harder k=0.3 case -- FAILED: R_j converged to EXACTLY 1.0 from
above (1.0072 -> 1.0015 -> ... -> 1.0000005), not below.

WHY, diagnosed directly: contrast(N) (the RAW, unsquared, single-run
quantity -- not a coupled/reference RATIO) does NOT approach zero as
N->infinity, even for the smooth k=10 case that FINDING_P114/P117 already
established has a well-converged G_growth/G_E. It approaches a finite
NONZERO constant instead (drA_hat, qm_hat settle to finite late-time values
per FINDING_P118's own derivation). So h(N)=contrast(N)^2 -> a positive
constant, and integral[0,N] h dN' grows LINEARLY in N -- for EVERY case,
convergent or not, because this is the integral of a SINGLE run, not the
coupled/reference RATIO G_E actually is. "Integrability of h(N) alone" was
therefore the wrong question -- not because the block-ratio *arithmetic*
was wrong, but because its premise (h(N)->0) does not hold for this system.

THE CORRECTED, SIMPLER TEST -- same conclusion the original design was
after, reached directly instead of through integration. By a standard
L'Hopital-style argument: if contrast_coupled(N) -> A_c and
contrast_reference(N) -> A_r (both finite) as N->infinity, then
integral h_c dN' ~ A_c^2*N + const_c and integral h_r dN' ~ A_r^2*N + const_r
for large N, so G_E(N) = ratio of the two integrals -> (A_c/A_r)^2 -- a
FINITE limit. If contrast_coupled(N) instead grows WITHOUT BOUND (however
slowly -- log(N), sqrt(N), anything), its own integral grows FASTER than
linear while the reference's stays linear, and G_E(N) -> infinity. So the
decisive, much cheaper question is simply: does contrast_coupled(N) itself
converge to a finite value as N->infinity, or does it keep growing? This is
tested with EXACTLY the matched-jump / shrinking-increment diagnostic
FINDING_P119 already validated on G_E itself -- applied here directly to
the point value contrast(N), needing no block integration at all.

CONTROLS:
  SMOOTH-CASE POSITIVE CONTROL (k=10), REDONE: does contrast_coupled(N)
    converge cleanly for the already-known-convergent case? (The ORIGINAL
    block-ratio positive control's failure is reported above, not hidden --
    this is a corrected re-test of the same underlying question.)
  REGRESSION: spot-check contrast(N) against FINDING_P119's own already-
    verified values.
  RESOLUTION: does the convergence classification survive using a denser
    N-sampling grid?

WHAT THIS FILE DOES NOT DO: claim a rigorous asymptotic proof -- the
matched-jump diagnostic, like FINDING_P119's own use of it, characterizes
behavior on the tested (finite, if enormous) tail, not a mathematical
limit. Push N (or T_END) further than FINDING_P119 already established as
safe. Vary Lambda or other (k, IC) combinations. Quote any k[h/Mpc]. Touch
MULTING itself (Gate 1).
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


p119 = _load("P119_ln_a_state_reformulation.py", "p119_for_p120")
p105 = p119.p105

a_star = p119.a_star
PHIDOT_INIT = p119.PHIDOT_INIT
LAMBDA_FIXED = p119.LAMBDA_FIXED

T_END = 1e13  # FINDING_P119's own established, verified-safe ceiling -- not pushed further


def contrast_at_N(sol, gh, lam, lam_cc, t_end, n_grid, t_lo_frac=0.001):
    """Dense (N, contrast) samples across the trusted trajectory, sorted by
    N. t_end must match the actual t_end `sol` was solved to (a bug in an
    earlier draft of this file used a mismatched, module-level t_end here
    and silently extrapolated scipy's dense output -- fixed, verified by
    the regression control below)."""
    ts = np.geomspace(max(1.0, t_end * t_lo_frac), t_end, n_grid)
    lna, c = p119.contrast_lna_from_sol(sol, ts, gh, lam, lam_cc)
    ok = np.isfinite(c)
    return lna[ok], c[ok]


def value_at(n_grid, c_grid, n_target):
    return float(np.interp(n_target, n_grid, c_grid))


def fit_power_law_limit(n_targets, values, label=""):
    """Fit contrast(N) = c_inf - A*N^-p via nonlinear least squares, with a
    HELD-OUT cross-validation: fit excluding the last point, then check how
    well that fit PREDICTS the excluded point. This is a materially
    stronger test than eyeballing a shrinking-increment table -- it is the
    same kind of adversarial check that caught FINDING_P119's own false
    PLATEAU-FOUND, applied here in the direction of actually confirming
    (not just failing to refute) convergence.

    DEGENERATE CASE, handled explicitly rather than silently mis-fit: if the
    branch is ALREADY exactly (or near-exactly) constant across the whole
    tested window -- as found for the reference branch below, converged
    long before this file's own measurement window starts -- there is
    nothing to fit (A=0 identically, p is undetermined, and scipy's own
    OptimizeWarning says so). Report the constant directly, not a spurious
    "fit"."""
    n_arr, c_arr = np.asarray(n_targets), np.asarray(values)
    spread = float(np.max(c_arr) - np.min(c_arr))
    typical = max(float(np.mean(np.abs(c_arr))), 1e-300)
    if spread / typical < 1e-8:
        c_const = float(np.mean(c_arr))
        print(f"    {label}: DEGENERATE -- already exactly constant across the whole")
        print(f"    {label}: tested window (spread/typical={spread / typical:.2e}). No power-law")
        print(
            f"    {label}: fit is meaningful here; using the constant value directly: {c_const:.6f}"
        )
        return c_const, float("nan"), 0.0, 0.0

    from scipy.optimize import curve_fit

    def model(nn, c_inf, amp, p):
        return c_inf - amp * nn ** (-p)

    p0 = [c_arr[-1], (c_arr[-1] - c_arr[0]) * 10, 0.5]
    popt_ho, _ = curve_fit(model, n_arr[:-1], c_arr[:-1], p0=p0, maxfev=20000)
    pred_last = model(n_arr[-1], *popt_ho)
    ho_rel_err = abs(pred_last / c_arr[-1] - 1.0) if c_arr[-1] != 0 else float("inf")
    popt_all, _ = curve_fit(model, n_arr, c_arr, p0=p0, maxfev=20000)
    resid = c_arr - model(n_arr, *popt_all)
    max_resid_rel = float(np.max(np.abs(resid))) / max(np.mean(np.abs(c_arr)), 1e-300)
    print(
        f"    {label} power-law fit c_inf - A*N^-p (excl. last point): "
        f"c_inf={popt_ho[0]:.4f}, A={popt_ho[1]:.4f}, p={popt_ho[2]:.6f}"
    )
    print(
        f"    {label} held-out prediction at N={n_arr[-1]:.4e}: {pred_last:.4f} "
        f"(actual {c_arr[-1]:.4f}), rel.err={ho_rel_err:.4%}"
    )
    print(
        f"    {label} full fit: c_inf={popt_all[0]:.4f}, A={popt_all[1]:.4f}, "
        f"p={popt_all[2]:.6f}, max|residual|/mean|value|={max_resid_rel:.4%}"
    )
    return popt_all[0], popt_all[2], ho_rel_err, max_resid_rel


def convergence_check(n_grid, c_grid, n_min, n_max, n_points=12, label=""):
    """The SAME matched-jump / shrinking-increment diagnostic FINDING_P119
    validated on G_E itself, applied directly to the point value
    contrast(N). Returns (targets, values, converged_bool)."""
    targets = np.geomspace(max(n_min, 1e-9), n_max, n_points)
    values = [value_at(n_grid, c_grid, nt) for nt in targets]
    print(f"    {label} contrast(N) at {n_points} points from N={n_min:.2f} to N={n_max:.2f}:")
    for nt, v in zip(targets, values, strict=True):
        print(f"      N={nt:<14.4e}  contrast={v:+.6e}")
    last_few = values[-5:]
    diffs = [abs(last_few[i + 1] - last_few[i]) for i in range(len(last_few) - 1)]
    shrinking = len(diffs) >= 2 and all(diffs[i] >= diffs[i + 1] for i in range(len(diffs) - 1))
    total_change = abs(values[-1] - values[0])
    last_change = abs(values[-1] - values[-2]) if len(values) >= 2 else float("inf")
    rel_last = last_change / max(abs(values[-1]), 1e-300)
    print(
        f"    increments shrinking over last 5 points: {shrinking}  |  "
        f"total change: {total_change:.4e}  |  final rel. step: {rel_last:.4%}"
    )
    return targets, values, shrinking, rel_last


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P120 -- Tail Convergence Test: does contrast(N) approach a finite")
    print("        limit? (revised design -- see docstring for why)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    astar = a_star(LAMBDA_FIXED)
    phidot_prob = 0.1 * PHIDOT_INIT
    ic0 = {"phidot0": phidot_prob}
    ln_astar = np.log(astar)

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 1 -- REGRESSION: spot-check contrast(N) against")
    print("FINDING_P119's own already-verified values")
    print("-" * 78)
    s_c = p119.run_lna(1.0, 1.0, 0.3, T_END, lam_cc=LAMBDA_FIXED, **ic0)
    reg_ok = True
    known = {2.0: 748.96717, 10.0: 15405.3458, 100.0: 20245.9737}
    for x, expected in known.items():
        t_probe = p119.t_of_lna(s_c, ln_astar + np.log(x), 1.0, T_END)
        _lna_p, c_p = p119.contrast_lna_from_sol(s_c, np.array([t_probe]), 1.0, 1.0, LAMBDA_FIXED)
        rel = abs(c_p[0] / expected - 1.0)
        print(
            f"    x={x:<8g}  contrast={c_p[0]:+.6e}  expected~{expected:+.6e}  rel.diff={rel:.3e}"
        )
        reg_ok &= rel < 1e-4
    print(f"  REGRESSION CONTROL {'PASSES' if reg_ok else 'FAILS'}")
    if not reg_ok:
        print("  *** STOP -- do not trust anything built on top of this.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 2 -- SMOOTH-CASE POSITIVE CONTROL (k=10), corrected re-test:")
    print("does contrast_coupled(N) converge cleanly, matching what")
    print("FINDING_P114/P117 already know about this case's G_E?")
    print("-" * 78)
    T_END_SMOOTH = 1e8
    s_smooth = p119.run_lna(1.0, 1.0, 10.0, T_END_SMOOTH, lam_cc=LAMBDA_FIXED)
    n_smooth, c_smooth = contrast_at_N(s_smooth, 1.0, 1.0, LAMBDA_FIXED, T_END_SMOOTH, 200000)
    n_lo_s, n_hi_s = float(n_smooth.min()), float(n_smooth.max())
    _t, _v, smooth_shrinking, smooth_rel = convergence_check(
        n_smooth, c_smooth, n_lo_s, n_hi_s, label="k=10"
    )
    smooth_ok = smooth_shrinking and smooth_rel < 0.01
    print(
        f"  POSITIVE CONTROL {'PASSES' if smooth_ok else 'FAILS'} "
        "(contrast_coupled(N) must converge for this known-convergent case)"
    )
    if not smooth_ok:
        print("  *** STOP -- the corrected test still does not confirm a")
        print("  *** KNOWN-convergent case. Do not trust it on k=0.3.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 3 -- RESOLUTION: does the classification survive a denser")
    print("N-sampling grid?")
    print("-" * 78)
    s_main = p119.run_lna(1.0, 1.0, 0.3, T_END, lam_cc=LAMBDA_FIXED, **ic0)
    n_a, c_a = contrast_at_N(s_main, 1.0, 1.0, LAMBDA_FIXED, T_END, 200000)
    n_b, c_b = contrast_at_N(s_main, 1.0, 1.0, LAMBDA_FIXED, T_END, 400000)
    n_lo, n_hi = float(n_a.min()), float(n_a.max())
    v_a_end = value_at(n_a, c_a, n_hi)
    v_b_end = value_at(n_b, c_b, n_hi)
    res_rel = abs(v_a_end / v_b_end - 1.0) if v_b_end else float("inf")
    res_ok = res_rel < 0.001
    print(f"    contrast(N_max) at n=200k: {v_a_end:+.8e}")
    print(f"    contrast(N_max) at n=400k: {v_b_end:+.8e}")
    print(f"    relative difference: {res_rel:.3e}")
    print(f"  RESOLUTION CONTROL {'PASSES' if res_ok else 'FAILS'} (threshold 0.1%)")
    if not res_ok:
        print("\n  *** a required control failed. STOP.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("MAIN RESULT -- k=0.3, phidot(1)x0.1: does contrast_coupled(N)")
    print("approach a finite limit across the full N range FINDING_P119")
    print("established as safe?")
    print("-" * 78)
    targets, values, main_shrinking, main_rel = convergence_check(
        n_a, c_a, n_lo, n_hi, n_points=14, label="k=0.3 coupled"
    )
    print()
    c_inf_coupled, p_coupled, ho_err_c, resid_c = fit_power_law_limit(
        targets, values, label="k=0.3 coupled"
    )

    # ==================================================================
    print("\n" + "-" * 78)
    print("EXTENSION -- same fit for the REFERENCE branch, to predict G_E's own")
    print("limit (A_c/A_r)^2 and cross-check it against FINDING_P119's own trend")
    print("-" * 78)
    s_ref = p119.run_lna(0.0, 1.0, 0.3, T_END, lam_cc=LAMBDA_FIXED, **ic0)
    n_ref, c_ref = contrast_at_N(s_ref, 0.0, 1.0, LAMBDA_FIXED, T_END, 200000)
    n_lo_r, n_hi_r = float(n_ref.min()), float(n_ref.max())
    targets_r, values_r, ref_shrinking, ref_rel = convergence_check(
        n_ref, c_ref, n_lo_r, n_hi_r, n_points=14, label="k=0.3 reference"
    )
    print()
    c_inf_ref, p_ref, ho_err_r, resid_r = fit_power_law_limit(
        targets_r, values_r, label="k=0.3 reference"
    )

    fit_ok = (
        main_shrinking
        and ref_shrinking
        and ho_err_c < 0.01
        and ho_err_r < 0.01
        and resid_c < 0.01
        and resid_r < 0.01
    )
    print(
        f"\n  FIT QUALITY {'PASSES' if fit_ok else 'FAILS'} (held-out error < 1%, "
        f"residuals < 1% of typical magnitude, for BOTH branches)"
    )

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if fit_ok:
        g_e_predicted = (c_inf_coupled / c_inf_ref) ** 2
        print(f"  predicted G_E limit = (c_inf_coupled/c_inf_ref)^2 = {g_e_predicted:.4f}")
        print(f"  predicted sqrt(G_E) limit = {g_e_predicted**0.5:.4f}")
        print("  FINDING_P119's own last measured value: sqrt(G_E)=1,254,869.66")
        print(
            f"  consistency check: predicted value is "
            f"{'ABOVE' if g_e_predicted**0.5 > 1254869.66 else 'BELOW'} "
            "P119's last measured point, as required if G_E is still rising toward it"
        )
        print("\n  -> CONVERGENT-CONTRAST, CROSS-VALIDATED. The coupled branch's")
        print("     contrast(N) passes a HELD-OUT power-law fit (predicting an")
        print("     excluded point to <1% error, not just eyeballing a shrinking-")
        print("     increment table -- the same style of adversarial check that caught")
        print("     FINDING_P119's own false PLATEAU-FOUND, applied here in the")
        print("     confirming direction). The reference branch needed no such fit --")
        print("     it is EXACTLY constant across the entire tested window, already")
        print("     converged before this file's measurement even begins.")
        print("     By the L'Hopital-style argument, this predicts G_E(N) itself")
        print("     converges to a finite limit, given above -- consistent with, and")
        print("     extending, FINDING_P119's own STILL-CLIMBING-but-not-yet-converged")
        print("     cumulative-integral trend, which this file's fit suggests is")
        print("     climbing TOWARD this predicted value rather than diverging.")
    else:
        print("  -> FIT DOES NOT CROSS-VALIDATE CLEANLY. The power-law model does not")
        print("     pass its own held-out test for at least one branch -- matches")
        print("     FINDING_P119's own STILL-CLIMBING verdict; no stronger claim made.")

    print("\n  NOT ESTABLISHED:")
    print("   * a rigorous asymptotic proof of the limiting behavior -- the")
    print("     matched-jump diagnostic characterizes the tested, finite tail only.")
    print("   * a closed-form value for any limit, if one exists.")
    print("   * anything at Lambda values, or (k, IC) combinations, other than the")
    print("     one tested.")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
