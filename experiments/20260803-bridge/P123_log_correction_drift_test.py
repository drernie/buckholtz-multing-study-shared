"""P123 -- Does power_law_log's own log-correction r drift toward 0 (which
would favor plain power_law's convergent reading) or stabilize away from 0
(which would favor its own divergent reading), as the fit window is pushed
CLOSER to the untouched hold-out boundary FINDING_P122 established?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE, user-directed ("го все по очереди" -- work through the open
items in order), first of the two follow-ups FINDING_P122 itself named.
FINDING_P122 found TWO best-fitting models disagree on whether the
deviation-energy integral converges: plain power_law (q~0.502>1/2,
converges) vs power_law_log (q~0.485-0.49<1/2, diverges), with
power_law_log MEASURABLY beating power_law on held-out prediction at
every one of 6 tested windows. Across those windows, power_law_log's own
r drifted: -0.131 -> -0.115 -> -0.108 -> -0.102 -> -0.098 -> -0.094 --
monotonically toward 0 as the fit window grew. FINDING_P122 named the
natural next check but did not run it: does this drift CONTINUE toward 0
(suggesting power_law_log's own advantage is a finite-sample artifact that
would vanish with enough data, and the TRUE law is closer to plain
power_law after all), or does it STABILIZE at some nonzero value (meaning
the log-correction is a persistent, real feature)?

THE DESIGN: reuses FINDING_P122's own already-computed T_END=1e13
trajectory and its own untouched hold-out probes ({360000, 375000, 390000}
decades) UNCHANGED -- extends its N_cut sequence from {50000..300000} with
5 MORE points closer to the boundary: {310000, 320000, 330000, 340000,
350000}, still comfortably short of the nearest hold-out probe (360000),
preserving a real gap. Fits BOTH power_law and power_law_log at each new
N_cut, tracks r's trend, and re-checks held-out prediction accuracy at
this finer resolution near the boundary.

CONTROLS: reuses FINDING_P122's own already-validated positive control
(REFERENCE branch pipeline) -- not re-run here since the underlying
fit/predict machinery is identical and already verified; this file adds
new N_cut VALUES to the same machinery, not new mechanics. Regression:
the FIRST 6 points of this file's own extended sequence must reproduce
FINDING_P122's own committed q/r values exactly (same window definitions,
same trajectory).

WHAT THIS FILE DOES NOT DO: touch the hold-out probes themselves (they
stay exactly as FINDING_P122 defined them). Push T_END past
FINDING_P119's own established ceiling. Claim a rigorous asymptotic
theorem -- even a stabilizing r over a wider tested range remains evidence
on a finite domain. Vary Lambda or other (k, IC) combinations. Quote any
k[h/Mpc]. Touch MULTING itself (Gate 1).
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


p122 = _load("P122_forward_extrapolation_test.py", "p122_for_p123")
p121 = p122.p121
p120 = p122.p120
p119 = p122.p119

a_star = p122.a_star
PHIDOT_INIT = p122.PHIDOT_INIT
LAMBDA_FIXED = p122.LAMBDA_FIXED
T_END = p122.T_END

# FINDING_P122's own committed values, reproduced here as a hard regression
# check (not re-derived assumptions) -- these are what P122 actually found.
P122_KNOWN_Q = {
    50000: 0.502396,
    100000: 0.502077,
    150000: 0.501964,
    200000: 0.501905,
    250000: 0.501865,
    300000: 0.501834,
}
P122_KNOWN_R = {
    50000: -0.131307,
    100000: -0.115383,
    150000: -0.107575,
    200000: -0.102159,
    250000: -0.097877,
    300000: -0.094296,
}
REGRESSION_TOL = 1e-4


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P123 -- does power_law_log's own r drift toward 0, or stabilize,")
    print("        as the fit window approaches FINDING_P122's hold-out boundary?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    astar = a_star(LAMBDA_FIXED)
    ln_astar = np.log(astar)
    phidot_prob = 0.1 * PHIDOT_INIT
    ic0 = {"phidot0": phidot_prob}

    s_c = p119.run_lna(1.0, 1.0, 0.3, T_END, lam_cc=LAMBDA_FIXED, **ic0)
    n_a, c_a = p120.contrast_at_N(s_c, 1.0, 1.0, LAMBDA_FIXED, T_END, 200000)
    ln_a_reach = s_c.y[0, -1]
    reach_decades = (ln_a_reach - ln_astar) / np.log(10)
    print(f"\n    T_END={T_END:.0e} reaches a_reach/a_star = 10^{reach_decades:.1f}")

    # FINDING_P122's own hold-out probes, defined LOCALLY inside its main() (not a
    # module attribute this file can read back) -- reproduced verbatim, unchanged.
    HOLD_OUT_DECADES = (360000.0, 375000.0, 390000.0)
    N_CUTS_ORIGINAL = (50000, 100000, 150000, 200000, 250000, 300000)
    N_CUTS_NEW = (310000, 320000, 330000, 340000, 350000)
    N_CUTS_ALL = N_CUTS_ORIGINAL + N_CUTS_NEW
    assert all(d < min(HOLD_OUT_DECADES) for d in N_CUTS_ALL), "must stay below hold-out"
    gap = min(HOLD_OUT_DECADES) - max(N_CUTS_ALL)
    print(f"    gap between largest N_cut and nearest hold-out probe: {gap:.0f} decades")
    N_FIT_POINTS = 400

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL -- REGRESSION against FINDING_P122's own committed q/r values")
    print("-" * 78)
    probe_ns, probe_vals = [], []
    for dec in HOLD_OUT_DECADES:
        n_p, v_p = p122.probe_value(n_a, c_a, dec, ln_astar)
        probe_ns.append(n_p)
        probe_vals.append(v_p)

    rows = []
    reg_ok = True
    for n_cut in N_CUTS_ALL:
        decades_grid_min = float((n_a.min() - ln_astar) / np.log(10))
        n_arr, c_arr = p122.sample_window(n_a, c_a, decades_grid_min, n_cut, ln_astar, N_FIT_POINTS)
        fits = p122.fit_all_models(n_arr, c_arr)
        errs = p122.held_out_errors(fits, probe_ns, probe_vals)
        q_pow = fits["power_law"][1][2] if fits["power_law"][1] is not None else None
        popt_pll = fits["power_law_log"][1]
        q_pll = popt_pll[2] if popt_pll is not None else None
        r_pll = popt_pll[3] if popt_pll is not None else None
        rows.append({"n_cut": n_cut, "q_pow": q_pow, "q_pll": q_pll, "r_pll": r_pll, "errs": errs})

        if n_cut in P122_KNOWN_Q:
            rel_q = abs(q_pow / P122_KNOWN_Q[n_cut] - 1.0) if q_pow else float("inf")
            rel_r = abs(r_pll / P122_KNOWN_R[n_cut] - 1.0) if r_pll else float("inf")
            ok = rel_q < REGRESSION_TOL and rel_r < REGRESSION_TOL
            reg_ok &= ok
            print(
                f"    N_cut=10^{n_cut:<7g}  q_pow={q_pow:.6f} (known {P122_KNOWN_Q[n_cut]:.6f})  "
                f"r_pll={r_pll:.6f} (known {P122_KNOWN_R[n_cut]:.6f})  {'OK' if ok else 'MISMATCH'}"
            )
    print(f"  REGRESSION CONTROL {'PASSES' if reg_ok else 'FAILS'}")
    if not reg_ok:
        print("  *** STOP -- does not reproduce FINDING_P122's own committed values.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("MAIN RESULT -- extended q/r trend, {310000..350000} decades new")
    print("-" * 78)
    for r in rows:
        q_pow_s = f"{r['q_pow']:.6f}" if r["q_pow"] is not None else "NO-FIT"
        q_pll_s = f"{r['q_pll']:.6f}" if r["q_pll"] is not None else "NO-FIT"
        r_pll_s = f"{r['r_pll']:.6f}" if r["r_pll"] is not None else "NO-FIT"
        errs = r["errs"]
        err_str = ", ".join(
            f"{name}={'NO-FIT' if e is None else f'{e:.4%}'}" for name, e in errs.items()
        )
        marker = " (NEW)" if r["n_cut"] in N_CUTS_NEW else ""
        print(
            f"    N_cut=10^{r['n_cut']:<7g}{marker}  q_pow={q_pow_s}  q_pll={q_pll_s}  "
            f"r_pll={r_pll_s}  held-out: {err_str}"
        )

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)

    new_rows = [r for r in rows if r["n_cut"] in N_CUTS_NEW and r["r_pll"] is not None]
    all_rows = [r for r in rows if r["r_pll"] is not None]
    if len(new_rows) < 3:
        print("  -> NOT ENOUGH CONVERGED power_law_log FITS in the extension. Infrastructure.")
        return 1

    r_series = [(r["n_cut"], r["r_pll"]) for r in all_rows]
    r_vals_all = [v for _c, v in r_series]
    cuts_all = [c for c, _v in r_series]
    print(f"  full r(N_cut) sequence: {[(c, round(v, 5)) for c, v in r_series]}")

    # DECADE-NORMALIZED rate, not raw point-to-point deltas -- the original 6
    # points are spaced 50000 decades apart, the 5 new ones only 10000 apart, so
    # a raw delta comparison makes the newer steps look artificially smaller
    # regardless of whether the underlying per-decade rate actually leveled off.
    # This is the SAME trap FINDING_P119's own retracted PLATEAU-FOUND draft
    # fell into (naive last-step % change, misled by the scan's own shrinking
    # step size) -- caught here before writing anything up, not after.
    rates = [
        (r_vals_all[i + 1] - r_vals_all[i]) / (cuts_all[i + 1] - cuts_all[i])
        for i in range(len(r_vals_all) - 1)
    ]
    print("  decade-normalized rate of r's change, per consecutive pair:")
    for i, rate in enumerate(rates):
        print(f"    {cuts_all[i]:>7} -> {cuts_all[i + 1]:>7}: rate/decade={rate:.4e}")
    new_rates = rates[-len(new_rows) :]
    rate_still_shrinking = all(
        abs(new_rates[i + 1]) < abs(new_rates[i]) for i in range(len(new_rates) - 1)
    )
    last_rate_ratio = abs(new_rates[-1]) / abs(new_rates[0]) if new_rates[0] != 0 else float("inf")
    rate_leveled = (
        last_rate_ratio > 0.7
    )  # rate barely changing -> approaching a fixed nonzero slope

    print(
        f"\n  |rate| still shrinking monotonically across the new extension: {rate_still_shrinking}"
    )
    print(f"  ratio of last new-segment rate to first new-segment rate: {last_rate_ratio:.3f}")
    print(
        f"  rate considered LEVELED (ratio > 0.7, i.e. barely decelerating further): {rate_leveled}"
    )

    q_pow_last = all_rows[-1]["q_pow"]
    q_pll_last = all_rows[-1]["q_pll"]
    print(f"\n  q_pow at largest tested N_cut: {q_pow_last:.6f}")
    print(f"  q_pll at largest tested N_cut: {q_pll_last:.6f}")
    print(f"  r_pll at largest tested N_cut: {all_rows[-1]['r_pll']:.6f}")

    if rate_still_shrinking and not rate_leveled:
        print("\n  -> RATE STILL DECELERATING, TREND UNRESOLVED. |r|'s decade-normalized")
        print("     rate of change keeps shrinking through the entire new extension (not")
        print("     leveling off to a fixed nonzero slope) -- consistent with r still")
        print("     trending toward SOME limit, but this file's own tested range cannot")
        print("     distinguish whether that limit is zero (favoring plain power_law's")
        print("     convergent reading) or a nonzero value (favoring power_law_log's")
        print("     divergent reading). A NAIVE last-3-points spread check on this same")
        print("     data would have wrongly reported PLATEAUED -- caught and replaced")
        print("     with this decade-normalized rate check before being trusted.")
    elif rate_leveled:
        print("\n  -> RATE LEVELS OFF. The decade-normalized rate of r's change has")
        print("     stopped decelerating meaningfully within the new extension --")
        print("     consistent with r approaching a fixed, nonzero asymptote rather than")
        print("     zero, supporting power_law_log's own divergent reading over plain")
        print("     power_law's convergent one.")
    else:
        print("\n  -> AMBIGUOUS TREND. This extension does not decisively resolve")
        print("     FINDING_P122's own model-ambiguity finding either way.")

    print("\n  NOT ESTABLISHED:")
    print("   * a rigorous asymptotic theorem for r's true limiting value -- this file")
    print("     tests a wider but still finite window, not the N->infinity limit.")
    print("   * which model (power_law vs power_law_log) correctly describes the TRUE")
    print("     tail law -- this file characterizes the TREND, it does not adjudicate.")
    print("   * that G_E itself is affected by any of this -- it remains established")
    print("     (FINDING_P120/P122) as convergent for any q>0, independent of this")
    print("     file's own result.")
    print("   * anything at Lambda values, or (k, IC) combinations, other than the")
    print("     one tested.")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
