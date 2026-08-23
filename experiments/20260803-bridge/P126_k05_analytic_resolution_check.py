"""P126 -- Does k=0.5's own contrast_coupled(N) (FINDING_P124) show the SAME
tight, self-consistent q_local plateau FINDING_P125 found for k=0.3
(q~0.466), as the universal, k-independent late-time mechanism predicts?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE, user-directed ("проверь на k=0.5" -- check it at k=0.5),
the exact follow-up FINDING_P125 itself registered as a falsifiable
prediction but did not test: "IF the SAME self-consistent optimal-c_inf +
q_local diagnostic is applied to k=0.5's own contrast_coupled(N) data
(FINDING_P124's own trajectory, already computed), it should ALSO show a
tight, stable plateau at APPROXIMATELY q~0.466 (not exactly identical,
but close, given the SAME universal, k-independent late-time mechanism
this file's own argument invokes)."

THE STAKES: FINDING_P125's own analytic mechanism (a friction-dominated,
k-independent, universal-in-N asymptotic law) was corroborated only
INDIRECTLY, via FINDING_P124's own exact q-match on FITTED power-law
exponents (q=0.502868 at BOTH k=0.3 and k=0.5). This file asks the
SHARPER, more decisive version of that same question directly on the
self-consistent, form-agnostic q value FINDING_P125 established (~0.466).

REVISED MID-BUILD after a context-asymmetric skeptic review caught a real
overclaim, reported here not hidden. A first draft found q_local matching
between k=0.3 and k=0.5 to 6 decimal places at EVERY probe point (not
just the asymptotic plateau) and called this "independent confirmation
of a universal exponent." The skeptic (given claim+code+data only, no
reasoning chain) identified the correct mechanism: q_local is INVARIANT
under any affine transformation of its input (x -> A*x+B), since
subtracting c_inf kills the offset and the log-derivative kills the
scale. If contrast_k05(N) and contrast_k03(N) are exactly affinely
related -- plausible, since these are LINEAR perturbation variables whose
only k-dependence, once k^2/a^2->0, is an overall amplitude -- the
q_local match would be a near-mathematical CONSEQUENCE of that relation,
not independent evidence. Tested directly: A_hat(N) := (contrast_k05(N)-
c_inf_k05)/(contrast_k03(N)-c_inf_k03), computed at FINDING_P120's own
regression-anchored 14 N-points -- CONFIRMED constant (A~6679, spread
<0.1%) across nearly 3 decades of N. The skeptic was right: this file's
real, defensible result is the AFFINE FACTORIZATION itself (a sharper,
more precise statement than "the exponents happen to match"), not an
independent re-confirmation of the exponent.

THE DESIGN: reuses FINDING_P124's own k=0.5 trajectory (T_END=1e13,
already established) and FINDING_P125's own q_local diagnostic and
optimal-c_inf flatness-minimization construction VERBATIM -- no new
mechanics, only a new (k, IC) applied to already-validated tooling. Does
NOT re-run the toy-model positive control (already validated in
FINDING_P125 on a KNOWN case) -- reuses that validation by reference,
consistent with FINDING_P124's own precedent of not re-validating
already-established machinery for every new k.

CONTROLS:
  SENSITIVITY, as a first step (mirrors FINDING_P125's own MAIN RESULT
    before its EXTENSION): apply q_local using k=0.5's own TWO fitted
    c_inf estimates (FINDING_P124's power_law and power_law_log fits) as
    a sanity check that the SAME c_inf-precision confound
    FINDING_P125 found at k=0.3 recurs here too -- if it does NOT (i.e.
    if k=0.5's fitted c_inf values are already precise enough for a
    clean trend), that itself would be worth reporting honestly, not
    forced to match FINDING_P125's own pattern.
  REGRESSION: the two fitted-c_inf q_local rows must be computable from
    the SAME already-established FINDING_P124 fit values (power_law
    c_inf=-48877729.588, power_law_log c_inf=-48911318.6279), not
    re-derived assumptions.

WHAT THIS FILE DOES NOT DO: re-derive the analytic mechanism itself (that
is FINDING_P125's own job, cited not repeated). Re-validate the toy model
or the q_local method's own correctness (already done in FINDING_P125).
Push T_END past FINDING_P119's own established ceiling. Vary Lambda or
other (k, IC) combinations beyond k=0.3/k=0.5. Quote any k[h/Mpc]. Touch
MULTING itself (Gate 1).
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.optimize import minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p125 = _load("P125_analytic_asymptotic_resolution.py", "p125_for_p126")
p124 = p125.p124
p123 = p125.p123
p120 = p125.p120
p119 = p125.p119

a_star = p125.a_star
PHIDOT_INIT = p125.PHIDOT_INIT
LAMBDA_FIXED = p125.LAMBDA_FIXED
T_END = p125.T_END
q_local = p125.q_local

K_TEST = 0.5

# FINDING_P124's own committed fit values, reproduced as regression anchors.
C_INF_POWER_LAW_K05 = -48877729.588
C_INF_POWER_LAW_LOG_K05 = -48911318.6279

# FINDING_P125's own self-consistent result at k=0.3, the target for comparison.
K03_SELF_CONSISTENT_Q = 0.465960
K03_SELF_CONSISTENT_C_INF = -38569.179235


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P126 -- does k=0.5's own contrast_coupled(N) show the SAME tight,")
    print("        self-consistent q_local plateau FINDING_P125 found at k=0.3?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    phidot_prob = 0.1 * PHIDOT_INIT
    ic0 = {"phidot0": phidot_prob}

    s_c = p119.run_lna(1.0, 1.0, K_TEST, T_END, lam_cc=LAMBDA_FIXED, **ic0)
    solve_ok = s_c is not None and s_c.success
    print(f"\n  k={K_TEST} coupled solve success: {solve_ok}")
    if not solve_ok:
        print("  *** STOP -- the trajectory itself failed to solve.")
        return 1
    n_a, c_a = p120.contrast_at_N(s_c, 1.0, 1.0, LAMBDA_FIXED, T_END, 200000)
    n_lo, n_hi = float(n_a.min()), float(n_a.max())

    # ==================================================================
    print("\n" + "-" * 78)
    print("SENSITIVITY -- q_local using k=0.5's own two FITTED c_inf estimates")
    print("(FINDING_P124), checking whether the SAME c_inf-precision confound")
    print("FINDING_P125 found at k=0.3 recurs here")
    print("-" * 78)
    probe_ns = np.geomspace(max(n_lo * 1.05, 1000.0), n_hi / 1.15, 12)
    fitted_results = {}
    for label, c_inf_est in (
        ("power_law's c_inf", C_INF_POWER_LAW_K05),
        ("power_law_log's c_inf", C_INF_POWER_LAW_LOG_K05),
    ):
        offset_vals = c_a - c_inf_est
        row = [q_local(n_a, offset_vals, n0, ratio=1.15) for n0 in probe_ns]
        fitted_results[label] = row
        valid = [v for v in row if v is not None]
        print(
            f"    {label} ({c_inf_est:.4f}): last 4 q_local = {[round(v, 5) for v in valid[-4:]]}"
        )

    valid_pl = [v for v in fitted_results["power_law's c_inf"] if v is not None]
    valid_pll = [v for v in fitted_results["power_law_log's c_inf"] if v is not None]
    same_confound = (
        len(valid_pl) >= 4
        and len(valid_pll) >= 4
        and np.sign(valid_pl[-1] - valid_pl[-4]) != np.sign(valid_pll[-1] - valid_pll[-4])
    )
    print(f"    same qualitative-opposite-trend confound as FINDING_P125: {same_confound}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("MAIN RESULT -- self-consistent optimal c_inf (flattest q_local),")
    print("FINDING_P125's own construction applied to k=0.5")
    print("-" * 78)
    large_n_probes = probe_ns[len(probe_ns) // 2 :]

    def flatness_score(c_inf_candidate):
        offset_vals = c_a - c_inf_candidate
        qs = [q_local(n_a, offset_vals, n0, ratio=1.15) for n0 in large_n_probes]
        qs = [q for q in qs if q is not None]
        if len(qs) < len(large_n_probes) * 0.7:
            return 1e10
        return float(np.var(qs))

    opt = minimize_scalar(
        flatness_score,
        bounds=(C_INF_POWER_LAW_LOG_K05 - 200000, C_INF_POWER_LAW_K05 + 200000),
        method="bounded",
    )
    c_inf_optimal = float(opt.x)
    print(f"    optimal (flattest-q_local) c_inf: {c_inf_optimal:.4f}")
    print(f"    (vs power_law's {C_INF_POWER_LAW_K05}, power_law_log's {C_INF_POWER_LAW_LOG_K05})")
    offset_opt = c_a - c_inf_optimal
    q_opt_row = [q_local(n_a, offset_opt, n0, ratio=1.15) for n0 in probe_ns]
    print("    q_local(N) at the self-consistent optimal c_inf:")
    for n0, ql in zip(probe_ns, q_opt_row, strict=True):
        ql_s = f"{ql:.6f}" if ql is not None else "N/A"
        print(f"      N={n0:>14.4e}  q_local={ql_s}")

    q_opt_valid = [q for q in q_opt_row if q is not None]
    large_n_opt_valid = q_opt_valid[len(q_opt_valid) // 2 :]
    opt_flat_rel = (
        (max(large_n_opt_valid) - min(large_n_opt_valid))
        / max(abs(np.mean(large_n_opt_valid)), 1e-6)
        if large_n_opt_valid
        else float("inf")
    )
    q_opt_plateau_mean = float(np.mean(large_n_opt_valid)) if large_n_opt_valid else None
    print(f"    relative spread of large-N q_local at optimal c_inf: {opt_flat_rel:.3%}")
    if q_opt_plateau_mean is not None:
        print(f"    plateau mean: {q_opt_plateau_mean:.6f}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("SKEPTIC-MANDATED CONTROL -- an independent, context-asymmetric skeptic")
    print("review of this file's own draft near-exact q_local match (6 decimal")
    print("places, every probe point, not just the plateau) flagged Trigger 4")
    print("(suspiciously perfect agreement) and identified the correct mechanism:")
    print("if contrast_k05(N) = A*contrast_k03(N) + B (an AFFINE relationship,")
    print("expected for LINEAR perturbation equations whose only k-dependence is")
    print("an overall amplitude), q_local is INVARIANT under exactly that")
    print("transformation by construction -- the match would then be a near-")
    print("mathematical consequence of linearity, not independent physics")
    print("confirmation. Testing this directly: is A_hat(N) := (contrast_k05(N)-")
    print("c_inf_k05) / (contrast_k03(N)-c_inf_k03) constant across N?")
    print("-" * 78)
    # FINDING_P120/P121/P122's own committed, regression-anchored k=0.3 raw
    # contrast(N) values at the SAME 14 N-points (the N-grid is k-independent
    # by construction -- background field a(t) has no k dependence -- verified
    # structurally, not assumed).
    n_k03_known = [
        926.34,
        1574.5,
        2676.1,
        4548.6,
        7731.2,
        13141,
        22335,
        37962,
        64524,
        109670,
        186410,
        316830,
        538510,
        915300,
    ]
    c_k03_known = [
        -3.495828e04,
        -3.580588e04,
        -3.645242e04,
        -3.694678e04,
        -3.732528e04,
        -3.761531e04,
        -3.783763e04,
        -3.800811e04,
        -3.813884e04,
        -3.823911e04,
        -3.831601e04,
        -3.837500e04,
        -3.842024e04,
        -3.845495e04,
    ]
    a_hats = []
    print("    N              dev_k03          dev_k05            A_hat")
    for n0, c3 in zip(n_k03_known, c_k03_known, strict=True):
        c5 = float(np.interp(n0, n_a, c_a))
        dev3 = c3 - K03_SELF_CONSISTENT_C_INF
        dev5 = c5 - c_inf_optimal
        a_hat = dev5 / dev3 if dev3 != 0 else None
        if a_hat is not None:
            a_hats.append(a_hat)
        a_hat_s = f"{a_hat:.4f}" if a_hat is not None else "N/A"
        print(f"    {n0:>10.1f}  {dev3:>14.4f}  {dev5:>16.4f}  {a_hat_s}")
    a_hat_mean = float(np.mean(a_hats)) if a_hats else None
    a_hat_spread_rel = (
        (max(a_hats) - min(a_hats)) / max(abs(a_hat_mean), 1e-9) if a_hats else float("inf")
    )
    affine_confirmed = a_hat_spread_rel < 0.001
    print(f"\n    A_hat mean: {a_hat_mean}")
    print(f"    A_hat relative spread across N: {a_hat_spread_rel:.4%}")
    print(f"    AFFINE FACTORIZATION CONFIRMED (spread<0.1%): {affine_confirmed}")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if q_opt_plateau_mean is None or opt_flat_rel > 0.02:
        print("  -> NOT ENOUGH VALID / NOT FLAT ENOUGH. Infrastructure outcome, or the")
        print("     self-consistent construction does not converge as cleanly at k=0.5.")
        return 1

    diff_from_k03 = q_opt_plateau_mean - K03_SELF_CONSISTENT_Q
    rel_diff = abs(diff_from_k03) / K03_SELF_CONSISTENT_Q
    close_to_k03 = abs(diff_from_k03) < 0.02  # absolute, matching FINDING_P125's own precision bar
    below_half = q_opt_plateau_mean < 0.5

    print(f"  k=0.5 self-consistent plateau: {q_opt_plateau_mean:.6f}")
    print(f"  k=0.3 self-consistent plateau (FINDING_P125): {K03_SELF_CONSISTENT_Q:.6f}")
    print(f"  difference: {diff_from_k03:+.6f}  ({rel_diff:.2%} relative)")
    print(f"  k=0.5 plateau also strictly below 1/2: {below_half}")
    print(f"  k=0.5 plateau close to k=0.3's own value (<0.02 absolute): {close_to_k03}")

    if close_to_k03 and below_half and affine_confirmed:
        print("\n  -> AFFINE-FACTORIZATION-CONFIRMED, NOT INDEPENDENT-MATCH. A first draft")
        print("     of this file's own verdict called the q_local match 'independent")
        print("     confirmation' of a universal exponent -- a context-asymmetric skeptic")
        print("     review (Trigger 4: suspiciously exact, every-probe-point agreement)")
        print("     caught this as an overclaim BEFORE commit. The real, verified finding")
        print("     is sharper and more precise: contrast_k05(N) = A*contrast_k03(N) + B")
        print(
            f"     EXACTLY, with A~{a_hat_mean:.2f} constant to {a_hat_spread_rel:.3%} across nearly"
        )
        print("     3 decades of N. Because q_local is invariant under exactly this affine")
        print("     transformation BY CONSTRUCTION, the q_local match FOLLOWS from the")
        print("     affine relationship -- it is not independent evidence beyond it.")
        print("     What IS genuinely established: the two ODE solutions' late-time SHAPE")
        print("     is k-independent up to a k-dependent overall rescaling -- consistent")
        print("     with, and a sharper statement than, the k^2/a^2->0 mechanism alone")
        print("     implied (that argument predicted a common EXPONENT; this shows a")
        print("     common FULL SHAPE FUNCTION). The deviation-energy conclusion")
        print(f"     (DIVERGES, q~{q_opt_plateau_mean:.3f}<1/2) still stands at k=0.5 -- it is not")
        print("     independently re-derived, it transfers directly from k=0.3 via the")
        print("     SAME affine relationship, which is itself the real result here.")
    elif below_half:
        print("\n  -> BELOW-HALF CONFIRMED, BUT NOT THE SAME VALUE. k=0.5's own plateau")
        print(f"     ({q_opt_plateau_mean:.4f}) is strictly below 1/2 like k=0.3's, so the")
        print("     QUALITATIVE conclusion (deviation-energy diverges) generalizes -- but")
        print(
            f"     the specific value differs meaningfully from k=0.3's ({K03_SELF_CONSISTENT_Q:.4f},"
        )
        print(f"     {rel_diff:.1%} relative difference) -- the exponent itself is NOT shown to")
        print("     be k-independent, only the qualitative 'below 1/2' feature is. This")
        print("     narrows FINDING_P125's own universal-mechanism hypothesis rather than")
        print("     confirming it in full.")
    else:
        print("\n  -> NOT CONFIRMED. k=0.5's own self-consistent plateau does not sit")
        print("     below 1/2 -- this would be a genuine surprise given FINDING_P124's own")
        print("     exact fitted-q match, worth investigating rather than dismissing.")

    print("\n  NOT ESTABLISHED:")
    print("   * why the affine constant is specifically A~6679 -- this file confirms")
    print("     the factorization exists and measures A, it does not derive A from")
    print("     first principles (would require solving the LINEAR perturbation")
    print("     equations' own k-dependent eigenvalue/amplitude, not attempted here).")
    print("   * a rigorous proof that either plateau (k=0.3 or k=0.5) continues to")
    print("     N->infinity -- both are finite-domain measurements.")
    print("   * why the specific value is ~0.466 rather than exactly 1/2 or some")
    print("     other value -- FINDING_P125 already flagged this as unresolved from")
    print("     first principles; this file does not resolve it either.")
    print("   * anything at Lambda values, or (k, IC) combinations, other than k=0.3")
    print("     and k=0.5.")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
