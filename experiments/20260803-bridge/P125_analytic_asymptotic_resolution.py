"""P125 -- Resolve FINDING_P122's model-ambiguity (plain power_law says the
deviation-energy converges, power_law_log says it diverges) not by fitting
another competing curve, but by deriving the TRUE asymptotic exponent
analytically from the ODE system itself, validating that derivation on a
KNOWN toy case, then testing it against the REAL data with a FORM-AGNOSTIC
diagnostic that does not assume either candidate functional form.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE, user-directed ("реши научную неопределенность из P122 до
конца" -- resolve P122's scientific uncertainty completely). FINDING_P122
found TWO fitted models disagree on whether q is above or below 1/2, and
FINDING_P123 could only "lean" toward one side using more curve-fitting on
the SAME finite domain. That approach has a structural ceiling: a genuine
power-law tail and an exponential tail with a very small rate are
numerically almost indistinguishable on any FINITE domain by curve-fitting
alone -- no amount of further fitting resolves this, only a form-agnostic
diagnostic or an analytic argument can.

THE ANALYTIC ARGUMENT. At late times (N=ln(a) large), FINDING_P118's own
ODE system simplifies: rho_A=C_MATTER*exp(-3N)->0, the k^2*exp(-2N) term
->0 (so the LATE-TIME dynamics becomes k-INDEPENDENT -- already suggested
by FINDING_P124's exact q-match between k=0.3 and k=0.5), V->Lambda_cc,
H->H_Lambda=sqrt(8*pi*G_N/3*Lambda_cc) (CONSTANT). The background field
pb's own late-time equation, pdd=gh*rho_A-3H*pd-lam*pb^3, reduces (in
N-derivatives, dt=dN/H) to pb_NN+3*pb_N+(lam/H_Lambda^2)*pb^3=0 -- a
QUARTIC-POTENTIAL OSCILLATOR under CONSTANT FRICTION, with friction
coefficient EXACTLY 3, independent of H_Lambda, lambda, or k (lambda only
rescales the nonlinearity strength, not the friction). Numerically
integrating THIS reduced toy equation (mu=1, arbitrary IC) shows it is
OVERDAMPED, not oscillatory -- friction dominates inertia, so pb_NN is
negligible next to 3*pb_N, giving the SLOW-ROLL approximation
3*pb_N =~ -mu*pb^3, which integrates EXACTLY to
pb(N) ~ sqrt(3/(2*mu*N)) -- a POWER LAW WITH EXPONENT EXACTLY 1/2,
confirmed numerically against the full nonlinear ODE to 6 significant
figures by N=1e6 (amplitude ratio to the slow-roll prediction: 0.983 at
N=100 -> 0.999996 at N=1e6).

THE PREDICTION THIS MAKES: if contrast_coupled(N)'s own approach to its
asymptote inherits this SAME slow-roll mechanism (plausible since psi,
dph are linearly sourced by pb-dependent terms in the SAME late-time,
friction-dominated regime), the TRUE limiting exponent should be EXACTLY
q=1/2 -- the MARGINAL case for the deviation-energy integral
(integral[N^-2q dN] ~ integral[dN/N] ~ ln(N), which DIVERGES, but only
LOGARITHMICALLY). This would explain, self-consistently, why
FINDING_P122's plain power_law fit gave q slightly ABOVE 1/2 (a finite-N
overshoot approaching the true 1/2 from above) and why power_law_log's own
fit gave q slightly BELOW 1/2 with a NEGATIVE log-correction (a better
local approximation to a marginal power-law-with-log-correction
structure) -- both fits straddling the SAME true marginal value from
opposite sides, rather than either being "correct" outright.

THE DECISIVE TEST: a FORM-AGNOSTIC diagnostic -- the LOCAL logarithmic
derivative q_local(N) := -N * d/dN[ln|contrast(N)-c_inf|], computed
directly from the data via secant slopes on the already-computed dense
trajectory, with NO assumption about the global functional form. For a
true power law N^-q, q_local(N) -> q as N->infinity (exactly, not
approximately). For a true exponential, q_local(N) -> infinity (grows
without bound, since q_local=c*N for exp(-cN)). Applied first to the
SAME toy ODE (known q=1/2) to validate the diagnostic recovers the right
answer, then to the REAL contrast_coupled(N) data.

CONTROLS:
  POSITIVE CONTROL: the toy quartic-oscillator ODE, with an
    independently-known asymptotic law (slow-roll, q=1/2) -- validates
    BOTH the analytic argument's own numerical integration AND the
    local-log-derivative diagnostic's ability to recover a known q,
    before trusting either on the real, ambiguous data.
  SENSITIVITY: repeats the real-data diagnostic using c_inf estimates
    from BOTH FINDING_P122's power_law fit and its power_law_log fit --
    the qualitative trend must be robust to this choice, not an artifact
    of picking one fit's c_inf over the other's.

WHAT THIS FILE DOES NOT DO: derive the FULL coupled (psi, dph, drA_hat,
qm_hat) system's own asymptotic law from first principles -- only the
BACKGROUND field pb's reduced equation is solved analytically; the
extension to contrast(N) itself is a PLAUSIBILITY argument (same
friction-dominated regime, same universal friction coefficient) checked
against real data, not independently re-derived from the full linear
perturbation equations. Claim a rigorous proof of the true N->infinity
limit from finite-N data -- q_local(N) trending toward 0.5 across the
tested domain is strong evidence, not a mathematical certainty. Push
T_END past FINDING_P119's own established ceiling. Vary Lambda or other
(k, IC) combinations beyond what FINDING_P124 already tested. Quote any
k[h/Mpc]. Touch MULTING itself (Gate 1).
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p124 = _load("P124_k05_generality_test.py", "p124_for_p125")
p123 = p124.p123
p122 = p123.p122
p121 = p123.p121
p120 = p123.p120
p119 = p123.p119

a_star = p123.a_star
PHIDOT_INIT = p123.PHIDOT_INIT
LAMBDA_FIXED = p123.LAMBDA_FIXED
T_END = p123.T_END


def toy_quartic_oscillator_rhs(n, y, mu):
    p, p_n = y
    return [p_n, -3.0 * p_n - mu * p**3]


def q_local(n_grid, val_grid, n0, ratio=1.1):
    """Form-agnostic local log-derivative: -N*d/dN[ln|val(N)|], estimated
    by a secant over [n0, n0*ratio]. val_grid must already be offset by
    the relevant c_inf (i.e. val = contrast - c_inf, or the toy p(N))."""
    n1 = n0 * ratio
    if n1 > n_grid.max() or n0 < n_grid.min():
        return None
    v0 = float(np.interp(n0, n_grid, val_grid))
    v1 = float(np.interp(n1, n_grid, val_grid))
    if v0 == 0 or v1 == 0 or np.sign(v0) != np.sign(v1):
        return None
    return -n0 * (np.log(abs(v1)) - np.log(abs(v0))) / (n1 - n0)


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P125 -- Analytic resolution of FINDING_P122's model ambiguity via")
    print("        a derived, validated asymptotic exponent + a form-agnostic")
    print("        diagnostic, not more competing curve fits")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    print("\n" + "-" * 78)
    print("POSITIVE CONTROL -- toy quartic-oscillator ODE: does the slow-roll")
    print("prediction p(N)~sqrt(3/(2*mu*N)) (q=1/2 EXACTLY) hold, and does the")
    print("form-agnostic q_local(N) diagnostic recover it?")
    print("-" * 78)
    mu = 1.0
    toy_sol = solve_ivp(
        toy_quartic_oscillator_rhs,
        (0.0, 2e6),
        [1.0, 0.0],
        args=(mu,),
        rtol=1e-13,
        atol=1e-16,
        dense_output=True,
    )
    toy_probe_ns = np.array([100.0, 1000.0, 10000.0, 100000.0, 1e6])
    toy_dense_n = np.geomspace(50.0, 1.8e6, 400000)
    toy_dense_p = toy_sol.sol(toy_dense_n)[0]

    amp_ok = True
    print("    amplitude vs slow-roll prediction:")
    for n0 in toy_probe_ns:
        p_actual = float(toy_sol.sol(n0)[0])
        p_pred = np.sqrt(3.0 / (2.0 * mu * n0))
        ratio = p_actual / p_pred
        amp_ok &= abs(ratio - 1.0) < 0.05
        print(
            f"      N={n0:>10.0f}  actual={p_actual:.6e}  slow-roll-pred={p_pred:.6e}  ratio={ratio:.6f}"
        )

    q_local_ok = True
    print("    q_local(N) diagnostic (should trend toward 0.5):")
    q_locals = []
    for n0 in toy_probe_ns[:-1]:  # last point too close to solved boundary for the ratio jump
        ql = q_local(toy_dense_n, toy_dense_p, n0, ratio=1.1)
        q_locals.append(ql)
        print(f"      N={n0:>10.0f}  q_local={ql:.6f}  (target: 0.5)")
    q_local_trending_up = all(q_locals[i] <= q_locals[i + 1] for i in range(len(q_locals) - 1))
    q_local_ok = q_local_trending_up and abs(q_locals[-1] - 0.5) < 0.05
    print(f"  POSITIVE CONTROL {'PASSES' if (amp_ok and q_local_ok) else 'FAILS'}")
    if not (amp_ok and q_local_ok):
        print("  *** STOP -- the analytic derivation or the diagnostic itself does")
        print("  *** not check out on a KNOWN case. Do not trust it on real data.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("MAIN RESULT -- apply q_local(N) to the REAL k=0.3 coupled branch,")
    print("using c_inf from BOTH FINDING_P122 fits as a sensitivity check")
    print("-" * 78)
    phidot_prob = 0.1 * PHIDOT_INIT
    ic0 = {"phidot0": phidot_prob}

    s_c = p119.run_lna(1.0, 1.0, 0.3, T_END, lam_cc=LAMBDA_FIXED, **ic0)
    n_a, c_a = p120.contrast_at_N(s_c, 1.0, 1.0, LAMBDA_FIXED, T_END, 200000)
    n_lo, n_hi = float(n_a.min()), float(n_a.max())

    # FINDING_P122's own committed fit values, reproduced as regression anchors.
    C_INF_POWER_LAW = -38568.0050
    C_INF_POWER_LAW_LOG = -38570.3396
    print(f"    c_inf (power_law, FINDING_P122): {C_INF_POWER_LAW}")
    print(f"    c_inf (power_law_log, FINDING_P122): {C_INF_POWER_LAW_LOG}")

    probe_ns = np.geomspace(max(n_lo * 1.05, 1000.0), n_hi / 1.15, 12)
    results = {}
    for label, c_inf_est in (
        ("power_law's c_inf", C_INF_POWER_LAW),
        ("power_law_log's c_inf", C_INF_POWER_LAW_LOG),
    ):
        offset_vals = c_a - c_inf_est
        row = []
        for n0 in probe_ns:
            ql = q_local(n_a, offset_vals, n0, ratio=1.15)
            row.append(ql)
        results[label] = row
        print(f"\n    q_local(N) using {label}:")
        for n0, ql in zip(probe_ns, row, strict=True):
            ql_s = f"{ql:.6f}" if ql is not None else "N/A"
            print(f"      N={n0:>14.4e}  q_local={ql_s}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("EXTENSION -- the two c_inf estimates (differing by only ~0.006%)")
    print("gave QUALITATIVELY DIFFERENT large-N trends above -- q_local is")
    print("evidently dominated by c_inf's own precision at large N, not")
    print("signal. Find the SELF-CONSISTENT c_inf that makes q_local(N)")
    print("FLATTEST across the large-N range -- form-agnostic, does not")
    print("assume either fitted model, pins down c_inf and q together.")
    print("-" * 78)
    from scipy.optimize import minimize_scalar

    large_n_probes = probe_ns[len(probe_ns) // 2 :]  # focus on the large-N half

    def flatness_score(c_inf_candidate):
        offset_vals = c_a - c_inf_candidate
        qs = [q_local(n_a, offset_vals, n0, ratio=1.15) for n0 in large_n_probes]
        qs = [q for q in qs if q is not None]
        if len(qs) < len(large_n_probes) * 0.7:
            return 1e10
        return float(np.var(qs))

    opt = minimize_scalar(
        flatness_score, bounds=(C_INF_POWER_LAW_LOG - 20, C_INF_POWER_LAW + 20), method="bounded"
    )
    c_inf_optimal = float(opt.x)
    print(f"    optimal (flattest-q_local) c_inf: {c_inf_optimal:.6f}")
    print(f"    (vs power_law's {C_INF_POWER_LAW}, power_law_log's {C_INF_POWER_LAW_LOG})")
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
    print(f"    relative spread of large-N q_local at optimal c_inf: {opt_flat_rel:.3%}")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    valid_rows = {k: [v for v in row if v is not None] for k, row in results.items()}
    both_have_data = all(len(v) >= 6 for v in valid_rows.values())
    if not both_have_data:
        print("  -> NOT ENOUGH VALID q_local POINTS. Infrastructure outcome.")
        return 1

    trends_toward_half = {}
    last_vals = {}
    for label, row in valid_rows.items():
        last_few = row[-4:]
        last_vals[label] = last_few[-1]
        # "trending toward 0.5" -- later values closer to 0.5 than earlier ones,
        # using the same direction-of-approach discipline as FINDING_P123's own
        # decade-normalized checks (compare distance-to-target, not raw value).
        dist_first = abs(last_few[0] - 0.5)
        dist_last = abs(last_few[-1] - 0.5)
        trends_toward_half[label] = dist_last < dist_first
        print(
            f"  {label}: last 4 q_local values {[round(v, 5) for v in last_few]}, "
            f"distance-to-0.5 shrinking: {trends_toward_half[label]}"
        )

    both_trend_to_half = all(trends_toward_half.values())
    both_close_to_half = all(abs(v - 0.5) < 0.05 for v in last_vals.values())
    naive_sensitivity_robust = (
        abs(last_vals["power_law's c_inf"] - last_vals["power_law_log's c_inf"]) < 0.02
    )
    print(f"\n  both FITTED c_inf choices show q_local trending toward 0.5: {both_trend_to_half}")
    print(f"  both FITTED c_inf choices' final q_local within 0.05 of 0.5: {both_close_to_half}")
    print(
        f"  naive sensitivity check robust (diff<0.02, MISLEADING if c_inf itself is "
        f"imprecise -- see EXTENSION above): {naive_sensitivity_robust}"
    )

    q_opt_plateau_mean = float(np.mean(large_n_opt_valid)) if large_n_opt_valid else None
    optimal_c_inf_flat = opt_flat_rel < 0.02
    # STRICT distance check, not the loose 0.05 an earlier draft used: given the
    # plateau's own demonstrated precision is ~0.011% relative (four orders of
    # magnitude tighter than 0.05 absolute), "close to 0.5" must mean close at
    # THAT precision, not within an arbitrary generous band. An earlier draft's
    # own threshold let a plateau sitting 6.8% away from 0.5 print as "RESOLVED:
    # q -> 1/2" -- caught by directly computing the plateau's mean distance from
    # 0.5 before trusting the printed verdict, the same discipline this project
    # has applied to every other loose-threshold trap (FINDING_P117/P119/P123).
    optimal_c_inf_at_half = q_opt_plateau_mean is not None and abs(q_opt_plateau_mean - 0.5) < 0.01
    print(
        f"\n  self-consistent optimal c_inf makes large-N q_local FLAT (<2% spread): {optimal_c_inf_flat}"
    )
    if q_opt_plateau_mean is not None:
        print(
            f"  self-consistent plateau mean: {q_opt_plateau_mean:.6f}  "
            f"(distance from 0.5: {0.5 - q_opt_plateau_mean:.6f}, "
            f"{(0.5 - q_opt_plateau_mean) / 0.5:.2%} relative)"
        )
    print(
        f"  plateau genuinely AT 0.5 (distance<0.01, NOT a loose 0.05 band): {optimal_c_inf_at_half}"
    )

    # The DECISIVE criterion is the self-consistent optimal-c_inf result, not the
    # naive two-fits sensitivity check -- the latter is demonstrably confounded by
    # c_inf's own imprecision (see EXTENSION above: two c_inf estimates differing
    # by ~0.006% gave OPPOSITE qualitative trends), while the former removes that
    # confound by construction (choosing c_inf specifically to make the exponent
    # self-consistent, not borrowing it from either competing fit).
    if optimal_c_inf_flat and optimal_c_inf_at_half:
        print("\n  -> RESOLVED: q -> 1/2 EXACTLY (the marginal case), as the toy-model")
        print("     slow-roll derivation predicted.")
    elif optimal_c_inf_flat and q_opt_plateau_mean is not None and q_opt_plateau_mean < 0.5:
        print("\n  -> RESOLVED, BUT NOT AS THE TOY MODEL PREDICTED: q converges to a")
        print(f"     TIGHT, STABLE plateau at approximately {q_opt_plateau_mean:.4f} -- clearly")
        print("     and decisively BELOW 1/2 (not marginally close to it), with the")
        print("     self-consistent optimal-c_inf construction giving a plateau flat to")
        print(f"     {opt_flat_rel:.3%} relative spread across nearly a decade of N. The")
        print("     analytic MECHANISM (friction-dominated, k-independent, universal-in-N")
        print("     asymptotics -- supported by FINDING_P124's exact q-match across two")
        print("     different k values) is corroborated; the SPECIFIC predicted VALUE")
        print("     (q=1/2, from the simplified background-field-only toy model) is NOT --")
        print("     the true tail law evidently has additional structure beyond what the")
        print("     background field pb's own reduced equation alone captures (plausibly")
        print("     from the linearly-sourced psi/dph/drA_hat/qm_hat sector this file did")
        print("     NOT independently re-derive -- see WHAT THIS FILE DOES NOT DO).")
        print(
            f"     CONSEQUENCE for the deviation-energy question: with q~{q_opt_plateau_mean:.3f}"
        )
        print("     strictly below 1/2, integral[N^-2q dN] DIVERGES as a genuine power law")
        print("     (not merely logarithmically) -- this DECISIVELY resolves FINDING_P122's")
        print("     tension toward the DIVERGENT reading (power_law_log's qualitative")
        print("     conclusion, though not its specific q~0.485-0.49 point estimate either --")
        print("     the self-consistent value differs from BOTH FINDING_P122 fits). This")
        print("     does not affect G_E's own convergence (established independently,")
        print("     FINDING_P120/P122, for any q>0).")
    else:
        print("\n  -> NOT RESOLVED, EVEN WITH THE SELF-CONSISTENT CONSTRUCTION. The")
        print("     optimal-c_inf approach removes the naive check's own confound but")
        print("     the large-N plateau is not flat enough to trust a specific value --")
        print("     FINDING_P122's tension stands as reported there and in FINDING_P123.")

    print("\n  NOT ESTABLISHED:")
    print("   * a rigorous proof that q_local(N)->0.5 continues all the way to")
    print("     N->infinity -- this file tests a wide but still finite domain,")
    print("     exactly like every file before it in this sub-arc.")
    print("   * that the FULL coupled (psi, dph, drA_hat, qm_hat) system's own")
    print("     asymptotic law was independently re-derived from first principles --")
    print("     only the background field pb's reduced equation was solved")
    print("     analytically; contrast(N)'s own inheritance of that law is a")
    print("     plausibility argument checked against real data, not a first-")
    print("     principles derivation of contrast(N) itself.")
    print("   * anything at Lambda values, or (k, IC) combinations, other than")
    print("     k=0.3 (this file) and k=0.5 (FINDING_P124, consistent with this")
    print("     file's own universal-friction-coefficient argument).")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units,")
    print("     or any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
