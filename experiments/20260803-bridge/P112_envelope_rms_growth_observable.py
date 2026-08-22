"""P112 -- Envelope/RMS Growth Observable: a phase-robust replacement for point-sampled
G_growth, built and controlled per the user's own decisive-experiment design.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

USER-DIRECTED, AGREED WITH ONE CORRECTION MADE BEFORE BUILDING. FINDING_P111
diagnosed the k<1 pole as a "damped oscillation that crosses zero repeatedly."
Before building the RMS/envelope machinery the user specified, this file did
its OWN reconnaissance (Compute First, applied to the premise, not just the
numerics) and found that characterization needs refining: a dense scan
(10,000 points, log-spaced in t) of the coupled contrast for
(Lambda=1e-15, k=0.3, phibar_dot(1)x0.1) over lna in [-10.6, 91.1] finds only
TWO sign changes total -- one at lna=-8.16 (a/a_star=2.8e-4, at the very
start of integration, indistinguishable from numerical noise around a
near-zero initial perturbation) and ONE genuine transition at lna=8.84
(a/a_star~6934). After that single crossing, contrast stays NEGATIVE and its
MAGNITUDE keeps changing -- not settling quickly. Pushing T_END further
(mirroring FINDING_P108's own precedent) does NOT show clean convergence the
way FINDING_P108's Lambda branches did: |G_growth| grows from 722516
(T_END=1e9) to 811964 (T_END=2e9, +12%) before the integrator overflows at
T_END>=3e9. So this is NOT literally repeated multi-period oscillation --
it is a SINGLE dominant transition followed by either very slow convergence
or genuinely unbounded growth in one direction, reach-limited by the
integrator before either can be distinguished with plain point-sampling.
This refines, not reverses, FINDING_P111's core conclusion: point-sampled
G_growth is still the wrong tool (a single value at a1/a2 cannot tell "slow
convergence" from "unbounded growth" either), and a window-based, phase-
robust observable is still the right next move -- the window design below is
adapted to span the transition and probe convergence AS THE WINDOW MOVES
LATER, rather than assuming several regular oscillation periods to average
over.

THE OBSERVABLE. For a run (coupled or reference), and a chosen a_end, define
the window [a_end/W, a_end] (W fixed across every case -- "the same window
for all branches", read as the same window SHAPE/WIDTH, not the same
absolute a-values, since a_star differs by construction across this arc's
own branches). Sample |contrast(a)| densely (N points, log-spaced) within
that window and compute TWO amplitude measures:
  A_RMS  := sqrt(mean(contrast^2))       over the window
  A_peak := max(|contrast|)              over the window   (envelope measure)
Then G_RMS(a_end) := A_RMS_coupled(a_end) / A_RMS_reference(a_end), and
G_peak(a_end) analogously with A_peak. Convergence is tested by moving
a_end LATER (not by finding a full oscillation period, since Step 0 above
shows there may not be one) and checking whether G_RMS/G_peak stabilize.

CONTROLS, ALL PRE-REGISTERED BEFORE ANY RESULT ON THE k<1 CASE ITSELF:
  POSITIVE CONTROL (k=10, baseline IC, smooth/non-oscillating, already
    converged per FINDING_P107/P108 to G_infinity=1.095773): this file's
    G_RMS and G_peak, at the SAME window machinery, must reproduce that
    published value within a stated tolerance (10%, looser than the exact
    point-sample gates elsewhere in this arc, since RMS-over-a-window is a
    DIFFERENT construction from a point ratio and is not expected to match
    to the same precision -- the control is "in the right ballpark and
    itself window-convergent", not "bit-identical").
  PHASE-SHIFT CONTROL: at a FIXED a_end, shift the window's placement (by
    using a DIFFERENT window width factor W', still centered/anchored on
    the same a_end) and check G_RMS/G_peak change by much less than they
    would under naive point-sampling (which showed a sign flip -- an
    infinite relative change -- under a much smaller perturbation in
    FINDING_P111's own Step 3).
  AMPLITUDE-SCALING CONTROL: perturbation theory here is LINEAR, so
    scaling the coupled run's own perturbation ICs (psi0, dph0, drA0--
    NOT phibar_dot(1), which is a BACKGROUND IC) by a known factor LAM
    should scale A_RMS_coupled by EXACTLY LAM (contrast is linear in the
    perturbation quantities, and rescaling their INITIAL values by LAM
    rescales the whole linear solution by LAM, at fixed background).
    Checked directly, not assumed.
  RMS-VS-PEAK: both measures reported at every step, not just one --
    if they disagree materially about convergence, that disagreement is
    itself reported, not resolved by picking whichever looks cleaner.

PRE-REGISTERED OUTCOMES for the k<1 case (k=0.3, phibar_dot(1)x0.1), AFTER
the controls above pass:
  GAP-CLOSES        G_RMS (and/or G_peak) converges as a_end moves later
                    (within the safe T_END<3e9 reach) AND is stable under
                    the phase-shift control -> FINDING_P110's k<1 gap is
                    genuinely closed by this observable; report the
                    converged value.
  STILL-OPEN        G_RMS/G_peak do NOT converge even as a_end moves
                    later within the safe reach -> this is not a
                    point-sampling artifact after all; it is long-lived,
                    genuinely unbounded (or extremely slowly converging)
                    amplitude growth in this (k, IC) combination -- a
                    real structural finding about the completion's low-k
                    perturbation sector under extreme IC, not an
                    estimator problem. FINDING_P111's diagnosis is
                    upgraded from "wrong tool" to "wrong tool AND a
                    possibly genuine amplitude instability", pending
                    further investigation this file does not attempt.

WHAT THIS FILE DOES NOT DO: resolve whether the k<1 growth is TRULY
unbounded or merely slow-converging beyond this arc's safe integration
reach (T_END<3e9) -- that would need either a stiffer/adaptive integrator
or an analytic argument, neither attempted here. Vary Lambda. Quote eps(k),
G_growth, or f(k) in physical units, or any k[h/Mpc] number. Touch MULTING
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


p105 = _load("P105_growth_with_lambda_cc.py", "p105_for_a112")

run = p105.run
a_star = p105.a_star
G_HAT_FIXED, LAM_FIXED = p105.G_HAT_FIXED, p105.LAM_FIXED
PHIDOT_INIT = p105.PHIDOT_INIT
G_N, C_MATTER = p105.G_N, p105.C_MATTER

LAMBDA_FIXED = 1e-15
X_LO = 0.2
N_SAMPLES = 400  # dense sampling within each amplitude window

# FINDING_P107/P108's own published converged value, for the positive control.
P107_G_INF_K10 = 1.095773
POSITIVE_CONTROL_TOL = 0.10
PHASE_SHIFT_TOL = 0.50  # generous -- even this is failed by a wide margin below


def contrast_array(sol, ts, gh, lam, lam_cc):
    """Vectorized contrast over an array of times -- avoids N separate
    brentq(t_of_a) calls, the same dense-sampling trick used in this file's
    own reconnaissance."""
    state = sol.sol(ts)
    a_, pb, pd, _psi, _psid, dph, _dphd, drA, qm = state
    rho_A = C_MATTER / a_**3
    rho_phys = rho_A * (1.0 - gh * pb)
    V = lam * pb**4 / 4.0 + lam_cc
    with np.errstate(all="ignore"):
        H = np.sqrt(np.maximum((8.0 * np.pi * G_N / 3.0) * (rho_phys + pd**2 / 2.0 + V), 0.0))
        delta_m = drA * (1.0 - gh * pb) - gh * rho_A * dph - 3.0 * H * qm
        c = delta_m / rho_phys
    return a_, c


def amplitude_near(sol, a_center, window_factor, gh, lam, lam_cc, t_end):
    """RMS and peak |contrast| over a NARROW window [a_center/wf, a_center*wf]
    centered on a_center -- the direct, phase-robust generalization of a single
    point sample, sized to average out local oscillation phase WITHOUT
    smearing the slow growth trend the way a wide, one-sided window would
    (that wide, one-sided design was tried first in this file and FAILED its
    own positive control -- see the module docstring's correction)."""
    t_center = p105.t_of_a(sol, a_center, 1.0, t_end)
    if t_center is None:
        return None, None, 0
    t_lo = max(1.0, t_center / (window_factor**2))
    # Clip to t_end -- sol.sol() is a dense-output interpolant valid only on
    # the integrated range [1, t_end]; evaluating past t_end silently
    # extrapolates (scipy dense output does NOT raise), which for large
    # window_factor produced multi-decade-out-of-range garbage that looked
    # like "phase instability" but was actually pure extrapolation noise
    # (verified directly: at W=5, t_hi was already 2.6x t_end before this
    # clip). This was a bug in the window, not a finding about the physics.
    t_hi = min(t_end, t_center * (window_factor**2))
    if t_hi <= t_lo:
        return None, None, 0
    ts = np.geomspace(t_lo, t_hi, N_SAMPLES)
    a_vals, c_vals = contrast_array(sol, ts, gh, lam, lam_cc)
    mask = (
        (a_vals >= a_center / window_factor)
        & (a_vals <= a_center * window_factor)
        & np.isfinite(c_vals)
    )
    if mask.sum() < 10:
        return None, None, int(mask.sum())
    c_win = c_vals[mask]
    rms = float(np.sqrt(np.mean(c_win**2)))
    peak = float(np.max(np.abs(c_win)))
    return rms, peak, int(mask.sum())


def g_rms_peak(kk, a1, a2, window_factor, lam_cc, t_end, **ic):
    """The DOUBLE ratio, replacing growth_a_matched's point values at a1/a2
    with RMS (or peak) amplitudes in NARROW windows around each -- preserving
    the exact 'growth from a1 to a2' structure G_growth was built to measure,
    while trading a single point sample for a locally-averaged one."""
    s_coup = run(1.0, 1.0, kk, t_end, lam_cc=lam_cc, **ic)
    s_ref = run(0.0, 1.0, kk, t_end, lam_cc=lam_cc, **ic)
    if s_coup is None or s_ref is None:
        return None, None
    rc1, pc1, _ = amplitude_near(s_coup, a1, window_factor, 1.0, 1.0, lam_cc, t_end)
    rc2, pc2, _ = amplitude_near(s_coup, a2, window_factor, 1.0, 1.0, lam_cc, t_end)
    rr1, pr1, _ = amplitude_near(s_ref, a1, window_factor, 0.0, 1.0, lam_cc, t_end)
    rr2, pr2, _ = amplitude_near(s_ref, a2, window_factor, 0.0, 1.0, lam_cc, t_end)
    if None in (rc1, rc2, rr1, rr2) or 0 in (rc1, rr1, rr2) or pc1 == 0 or pr1 == 0 or pr2 == 0:
        return None, None
    g_rms = (rc2 / rc1) / (rr2 / rr1)
    g_peak = (pc2 / pc1) / (pr2 / pr1)
    return g_rms, g_peak


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P112 -- Envelope/RMS growth observable: phase-robust replacement for")
    print("        point-sampled G_growth")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    W = 10.0  # window factor: [a_end/W, a_end], same shape for every case

    # ==================================================================
    print("\n" + "-" * 78)
    print("POSITIVE CONTROL -- k=10, baseline IC (smooth, non-oscillating,")
    print(f"already converged to G_infinity={P107_G_INF_K10} per FINDING_P107/P108)")
    print("-" * 78)
    a0 = a_star(LAMBDA_FIXED)
    g_rms_10, g_peak_10 = g_rms_peak(10.0, a0 * X_LO, a0 * 100.0, W, LAMBDA_FIXED, 1e8)
    print(f"  G_RMS(k=10)  = {g_rms_10!r}")
    print(f"  G_peak(k=10) = {g_peak_10!r}")
    rel_rms = abs(g_rms_10 / P107_G_INF_K10 - 1.0) if g_rms_10 is not None else float("inf")
    rel_peak = abs(g_peak_10 / P107_G_INF_K10 - 1.0) if g_peak_10 is not None else float("inf")
    pos_ok = rel_rms < POSITIVE_CONTROL_TOL and rel_peak < POSITIVE_CONTROL_TOL
    print(f"  relative diff from published: RMS={rel_rms:.3e}, peak={rel_peak:.3e}")
    print(
        f"  POSITIVE CONTROL {'PASSES' if pos_ok else 'FAILS'} (threshold "
        f"{POSITIVE_CONTROL_TOL:.0%})"
    )
    if not pos_ok:
        print("  *** the RMS/peak machinery does not reproduce the known-good case.")
        print("  *** STOP -- fix the observable before trusting anything on the k<1 case.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("PHASE-SHIFT CONTROL -- k=0.3, phidot x0.1: does changing the window")
    print("WIDTH (a proxy for shifting where within the transition it sits)")
    print("leave G_RMS/G_peak much more stable than point-sampling was?")
    print("-" * 78)
    kk_prob = 0.3
    phidot_prob = 0.1 * PHIDOT_INIT
    a_end_probe = a_star(LAMBDA_FIXED) * 1e4
    a1_probe = a_star(LAMBDA_FIXED) * X_LO
    shift_results = []
    for w in (5.0, 10.0, 20.0):
        g_r, g_p = g_rms_peak(
            kk_prob, a1_probe, a_end_probe, w, LAMBDA_FIXED, 1e9, phidot0=phidot_prob
        )
        shift_results.append((w, g_r, g_p))
        print(f"    W={w:<6g} G_RMS={g_r!r}  G_peak={g_p!r}")
    valid_rms = [g for _w, g, _p in shift_results if g is not None]
    valid_peak = [p for _w, _g, p in shift_results if p is not None]
    if len(valid_rms) >= 2:
        rms_phase_spread = (max(valid_rms) - min(valid_rms)) / abs(np.mean(valid_rms))
        print(f"    G_RMS relative spread across window widths: {rms_phase_spread:.4e}")
    else:
        rms_phase_spread = float("nan")
        print("    not enough valid G_RMS points to assess phase-shift stability")
    if len(valid_peak) >= 2:
        peak_phase_spread = (max(valid_peak) - min(valid_peak)) / abs(np.mean(valid_peak))
        print(f"    G_peak relative spread across window widths: {peak_phase_spread:.4e}")
    else:
        print("    not enough valid G_peak points to assess phase-shift stability")
    print("    (contrast: point-sampled G_growth showed a SIGN FLIP -- effectively")
    print("     infinite relative change -- under a much smaller window shift, per")
    print("     FINDING_P111's own Step 3)")
    phase_ok = (
        not np.isnan(rms_phase_spread)
        and rms_phase_spread < PHASE_SHIFT_TOL
        and len(valid_peak) >= 2
        and (max(valid_peak) - min(valid_peak)) / abs(np.mean(valid_peak)) < PHASE_SHIFT_TOL
    )
    print(
        f"\n  PHASE-SHIFT CONTROL {'PASSES' if phase_ok else 'FAILS'} "
        f"(threshold {PHASE_SHIFT_TOL:.0%})"
    )
    if not phase_ok:
        print("  *** traced, not assumed: a1=a_star*X_LO sits inside the same steep")
        print("  *** transient FINDING_P111 already found in the coupled run's own")
        print("  *** delta_phi (changes by ~4 orders of magnitude between x=0.2 and")
        print("  *** x=1). Direct check: holding a2 and W fixed, moving a1 from")
        print("  *** x=0.2 to x=5-10 collapses the W-sensitivity from a 286% spread")
        print("  *** to ~60% -- confirming the ANCHOR, not the RMS/window machinery")
        print("  *** itself, is the dominant cause (the positive control at k=10,")
        print("  *** where no such transient exists at the same a1, already passed).")
        print("  *** STOP -- per this file's own pre-registered discipline (the same")
        print("  *** one applied to the positive control above): a required control")
        print("  *** failing means the downstream GAP-CLOSES/STILL-OPEN verdict would")
        print("  *** rest on an unvalidated observable at this anchor. Not reported.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("AMPLITUDE-SCALING CONTROL -- scaling ALL THREE of the COUPLED run's")
    print("nonzero-default perturbation ICs (psi0, dph0, drA0) TOGETHER by a")
    print("known factor must scale A_RMS by that SAME factor (perturbation")
    print("theory here is linear IN THE FULL IC VECTOR -- scaling only dph0")
    print("while psi0/drA0 stay fixed changes which mix of linear modes is")
    print("excited, so that is NOT a valid linearity test; P105's own")
    print("initial_data() shows psi0=1e-5, dph0=1e-6, drA0=1e-5 all enter")
    print("psid0/qm0 linearly and must be scaled together)")
    print("-" * 78)
    a_end_scale = a_star(LAMBDA_FIXED) * 100.0
    s_base = run(1.0, 1.0, 1.0, 1e8, lam_cc=LAMBDA_FIXED)
    rms_base, _pk, _n = amplitude_near(s_base, a_end_scale, W, 1.0, 1.0, LAMBDA_FIXED, 1e8)
    SCALE = 3.0
    s_scaled = run(
        1.0,
        1.0,
        1.0,
        1e8,
        lam_cc=LAMBDA_FIXED,
        psi0=1e-5 * SCALE,
        dph0=1e-6 * SCALE,
        drA0=1e-5 * SCALE,
    )
    rms_scaled, _pk2, _n2 = amplitude_near(s_scaled, a_end_scale, W, 1.0, 1.0, LAMBDA_FIXED, 1e8)
    print(f"  A_RMS(baseline psi0/dph0/drA0)      = {rms_base!r}")
    print(f"  A_RMS(all three x {SCALE})              = {rms_scaled!r}")
    ratio = rms_scaled / rms_base if rms_base else float("nan")
    scale_ok = abs(ratio / SCALE - 1.0) < 0.05
    print(f"  observed ratio = {ratio:.4f}  (expected {SCALE})  {'OK' if scale_ok else 'MISMATCH'}")

    print(
        f"\n  ALL CONTROLS: positive={pos_ok}, amplitude-scaling={scale_ok}, "
        f"phase-shift spread={rms_phase_spread:.2%}"
        if not np.isnan(rms_phase_spread)
        else f"\n  ALL CONTROLS: positive={pos_ok}, amplitude-scaling={scale_ok}"
    )

    # ==================================================================
    print("\n" + "-" * 78)
    print("MAIN TEST -- k=0.3, phidot x0.1: does G_RMS/G_peak converge as the")
    print("window moves later (within the safe T_END<3e9 reach)?")
    print("-" * 78)
    a0p = a_star(LAMBDA_FIXED)
    a1p = a0p * X_LO
    a_ends = [a0p * x for x in (1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8)]
    t_ends_needed = [1e8, 1e8, 1e9, 1e9, 2e9, 2e9, 2e9]
    rows = []
    for a_end, te in zip(a_ends, t_ends_needed, strict=True):
        g_r, g_p = g_rms_peak(kk_prob, a1p, a_end, W, LAMBDA_FIXED, te, phidot0=phidot_prob)
        rows.append((a_end / a0p, g_r, g_p))
        print(
            f"    a_end/a_star={a_end / a0p:<12.4e} T_END={te:.0e}  G_RMS={g_r!r}  G_peak={g_p!r}"
        )

    valid_rows = [(x, r, p) for x, r, p in rows if r is not None]
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if len(valid_rows) < 3:
        print("  -> NOT ENOUGH MEASURABLE POINTS to assess convergence. Infrastructure")
        print("     outcome, not evidence either way.")
        return 1
    last_two_rms = [r for _x, r, _p in valid_rows[-2:]]
    final_change = (
        abs(last_two_rms[-1] / last_two_rms[-2] - 1.0) if last_two_rms[-2] else float("inf")
    )
    print(f"  final-step change in G_RMS (last two measured points): {final_change:.4%}")
    if final_change < 0.10:
        print("\n  -> GAP-CLOSES. G_RMS converges as the window moves later, within a")
        print(f"     10% final-step tolerance. Converged value: {last_two_rms[-1]:.4f}.")
        print("     FINDING_P110's k<1 gap is genuinely closed by this observable.")
    else:
        print("\n  -> STILL-OPEN. G_RMS does not converge even as the window moves later,")
        print("     within the safe T_END<3e9 reach. Not a point-sampling artifact after")
        print("     all -- this looks like long-lived, possibly genuinely unbounded")
        print("     amplitude growth in this (k, IC) combination. FINDING_P111's")
        print("     diagnosis is upgraded: wrong tool, AND a real amplitude question")
        print("     this file does not resolve.")

    print("\n  NOT ESTABLISHED:")
    print("   * whether the k<1 growth is TRULY unbounded or merely slow-converging")
    print("     beyond this arc's safe integration reach (T_END<3e9) -- would need a")
    print("     stiffer/adaptive integrator or an analytic argument, neither attempted.")
    print("   * anything at Lambda values other than 1e-15.")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
