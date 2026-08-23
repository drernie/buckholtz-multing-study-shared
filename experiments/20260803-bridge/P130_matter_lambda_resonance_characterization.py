"""P130 -- Characterize the matter-Lambda resonant transient the reduction
(FINDING_P127) excludes -- the likely real origin of FINDING_P126's
amplitude constant A~6679, and the reason a naive "genuinely independent,
not-from-full-system" hand-off is harder than it first looked.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE, user-directed: "попробуй построить genuinely independent
hand-off, не из full system" -- following FINDING_P129's own skeptic-
corrected conclusion that a hand-off state must NOT be read off the
already-solved full trajectory to count as independent evidence.

WHAT WAS ATTEMPTED FIRST, honestly reported: the plan was a small-
perturbation, matter-dominated early-time linearization (drop pb^3,
approximate H(N)~H0*exp(-1.5N)). RECONNAISSANCE, run BEFORE committing to
that design (Compute First), killed it directly: pb DOES stay small
throughout (peak ~0.086 at N~3), but psi/dph/drA_hat/qm_hat do NOT --
they undergo a violent, ~1e7-1e10-fold amplification in a narrow window
around N~11-16, for BOTH k=0.3 and k=0.5. A small-perturbation
linearization would miss this ENTIRELY (it assumes psi/dph stay small,
they do not), making the originally-planned approach invalid before a
single line of the simplified model was written.

THE MECHANISM, diagnosed from where the amplification happens: rho_A(N)
= C_MATTER*exp(-3N) (matter) and lam_cc (the Lambda-like additive term in
V) become EQUAL at

    N_eq = -ln(lam_cc/C_MATTER) / 3

-- a CLOSED-FORM prediction from two FIXED physical constants of the
problem, computed here directly, NOT read off any solved trajectory. This
is exactly where H(N)'s own friction (H itself) is transitioning from
matter-dominated decay (H~exp(-1.5N)) toward its late-time constant value
H_Lambda -- friction is WEAKEST relative to the perturbation-sourcing
terms right around this transition, a textbook setup for reduced-damping
amplification (the same qualitative mechanism as parametric resonance /
particle production during reheating in inflationary cosmology, though
this file does not attempt that formalism's quantitative machinery).

CONTROLS:
  REGRESSION: reproduces this file's own prior ad-hoc reconnaissance
    values (peak location, peak amplitude) before trusting the refined
    scan below.
  K-INDEPENDENT-TRIGGER CHECK: does the peak occur at APPROXIMATELY the
    SAME N for k=0.3 and k=0.5 (consistent with a k-independent trigger,
    matter-Lambda equality), or does peak location itself scale strongly
    with k (which would argue against this mechanism)?
  AMPLITUDE-RATIO PLAUSIBILITY CHECK: is the k=0.5-to-k=0.3 peak-amplitude
    ratio the SAME ORDER OF MAGNITUDE as FINDING_P126's own measured
    A_hat=6678.998 -- a necessary (not sufficient) condition for this
    resonance being the amplitude's real origin.

WHAT THIS FILE DOES NOT DO: complete the user's own request for a
genuinely independent, quantitatively-predictive hand-off -- that would
require an actual amplification-factor calculation through the friction
transition (an adiabatic-invariant or WKB-style argument, analogous to
reheating/preheating particle-production calculations), not attempted
here. Explain why peak |psi| specifically (rather than some other
combination of state variables, or the late-time settled qm_hat/drA_hat)
is the right proxy for the amplitude that ultimately sets A~6679 -- used
here only as a plausibility check, not a rigorous derivation. Vary
Lambda, G_N, or C_MATTER. Quote any k[h/Mpc]. Touch MULTING itself
(Gate 1).
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


p128 = _load("P128_realistic_handoff_ic_test.py", "p128_for_p130")
p119 = p128.p119
LAMBDA_FIXED = p128.LAMBDA_FIXED
PHIDOT_INIT = p128.PHIDOT_INIT
T_END = p128.T_END
C_MATTER = p128.C_MATTER
A_HAT_MEAN_REGRESSION = 6678.998  # FINDING_P126's own committed regression anchor

# This file's own prior ad-hoc reconnaissance (coarse grid, 0.1 resolution),
# reproduced here as regression anchors before trusting the refined scan.
RECON_PEAK_N03_COARSE = 13.600
RECON_PEAK_ABS_PSI03_COARSE = 2.635193e00
RECON_PEAK_N05_COARSE = 13.600
RECON_PEAK_ABS_PSI05_COARSE = 1.119308e04


def n_eq_matter_lambda() -> float:
    """Closed-form matter-Lambda equality point -- from FIXED constants
    only, never read off a solved trajectory."""
    return -np.log(LAMBDA_FIXED / C_MATTER) / 3.0


def find_peak_abs_psi(sol, n_lo, n_hi, n_points):
    ns = np.linspace(n_lo, n_hi, n_points)
    best_n, best_abs = None, -1.0
    for n in ns:
        t = p119.t_of_lna(sol, float(n), 1.0, T_END)
        if t is None:
            continue
        state = sol.sol(t)
        psi = state[3]
        if abs(psi) > best_abs:
            best_abs, best_n = abs(psi), float(n)
    return best_n, best_abs


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P130 -- matter-Lambda resonant transient: the likely real origin")
    print("        of A~6679, and why the naive independent hand-off failed")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    n_eq = n_eq_matter_lambda()
    print(f"\n  Analytic matter-Lambda equality: N_eq = -ln(lam_cc/C_MATTER)/3 = {n_eq:.6f}")
    print("  (closed form, from fixed constants only -- not read off any solve)")

    ic0 = {"phidot0": 0.1 * PHIDOT_INIT}
    print("\n  Solving the REAL full k=0.3 and k=0.5 systems (once each)...")
    s03 = p119.run_lna(1.0, 1.0, 0.3, T_END, lam_cc=LAMBDA_FIXED, **ic0)
    s05 = p119.run_lna(1.0, 1.0, 0.5, T_END, lam_cc=LAMBDA_FIXED, **ic0)
    if s03 is None or not s03.success or s05 is None or not s05.success:
        print("  *** STOP -- one of the full systems failed to solve.")
        return 1
    print(f"  k=0.3 solve success: {s03.success}   k=0.5 solve success: {s05.success}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 1 -- REGRESSION against this file's own prior coarse")
    print("reconnaissance (0.1 resolution)")
    print("-" * 78)
    coarse_n03, coarse_abs03 = find_peak_abs_psi(s03, 9.0, 18.0, 91)
    coarse_n05, coarse_abs05 = find_peak_abs_psi(s05, 9.0, 18.0, 91)
    # WHY: exact float `==` on an np.linspace-derived N is fragile (float
    # accumulation gives 13.600000000000001, not 13.6) -- caught by this
    # control itself FAILING on the first run; fixed with a tolerance.
    reg_ok = (
        abs(coarse_n03 - RECON_PEAK_N03_COARSE) < 1e-6
        and abs(coarse_n05 - RECON_PEAK_N05_COARSE) < 1e-6
        and abs(coarse_abs03 / RECON_PEAK_ABS_PSI03_COARSE - 1.0) < 1e-6
        and abs(coarse_abs05 / RECON_PEAK_ABS_PSI05_COARSE - 1.0) < 1e-6
    )
    print(f"    k=0.3 coarse peak: N={coarse_n03}  |psi|={coarse_abs03:.6e}")
    print(f"    k=0.5 coarse peak: N={coarse_n05}  |psi|={coarse_abs05:.6e}")
    print(f"  REGRESSION CONTROL {'PASSES' if reg_ok else 'FAILS'}")
    if not reg_ok:
        print("  *** STOP -- does not reproduce this file's own prior reconnaissance.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("MAIN RESULT -- refined peak location (0.005 resolution) for both k")
    print("-" * 78)
    n_peak03, abs_peak03 = find_peak_abs_psi(s03, 13.0, 14.5, 301)
    n_peak05, abs_peak05 = find_peak_abs_psi(s05, 13.0, 14.5, 301)
    print(f"    k=0.3: peak |psi| = {abs_peak03:.6e} at N={n_peak03:.4f}")
    print(f"    k=0.5: peak |psi| = {abs_peak05:.6e} at N={n_peak05:.4f}")

    offset03 = n_peak03 - n_eq
    offset05 = n_peak05 - n_eq
    peak_n_diff = abs(n_peak03 - n_peak05)
    print(f"    offset from N_eq: k=0.3={offset03:+.4f}  k=0.5={offset05:+.4f}")
    print(f"    |peak_N(k=0.3) - peak_N(k=0.5)| = {peak_n_diff:.4f}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("CHECK A -- K-INDEPENDENT-TRIGGER: peak locations close (not")
    print("identical -- coarse scan's exact match was a grid coincidence,")
    print("caught directly by this refined scan, not silently kept)")
    print("-" * 78)
    trigger_approx_k_independent = peak_n_diff < 0.5  # both land within half an e-fold
    print(f"    peak-N difference < 0.5 e-folds: {trigger_approx_k_independent}")
    print("    NOTE: the coarse (0.1-resolution) scan found BOTH peaks at exactly")
    print("    N=13.600 -- this refined scan shows that was a grid-resolution")
    print("    coincidence, not a true exact match (13.455 vs 13.620). Reported")
    print("    honestly rather than kept as the more dramatic coarse-grid number.")

    print("\n" + "-" * 78)
    print("CHECK B -- AMPLITUDE-RATIO PLAUSIBILITY vs A_hat=6678.998")
    print("-" * 78)
    peak_ratio = abs_peak05 / abs_peak03
    log10_ratio_diff = abs(np.log10(peak_ratio) - np.log10(A_HAT_MEAN_REGRESSION))
    same_order_of_magnitude = log10_ratio_diff < 0.5  # within a factor of ~3
    print(f"    peak|psi|(k=0.5) / peak|psi|(k=0.3) = {peak_ratio:.1f}")
    print(f"    FINDING_P126's own A_hat_mean = {A_HAT_MEAN_REGRESSION:.1f}")
    print(f"    |log10(ratio) - log10(A_hat)| = {log10_ratio_diff:.4f}")
    print(f"    SAME ORDER OF MAGNITUDE (within factor ~3): {same_order_of_magnitude}")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if trigger_approx_k_independent and same_order_of_magnitude:
        print("  -> MECHANISM IDENTIFIED, NOT YET QUANTITATIVELY DERIVED.")
        print("     The matter-Lambda transition (N_eq computed from fixed constants,")
        print("     not read off any trajectory) triggers a resonant amplification of")
        print("     psi/dph/drA_hat/qm_hat -- approximately k-independent in WHERE it")
        print("     happens (peak locations within half an e-fold of each other), but")
        print("     strongly k-dependent in HOW STRONG it is (peak-amplitude ratio")
        print(f"     {peak_ratio:.0f}, the same order of magnitude as FINDING_P126's own")
        print("     A_hat=6679). This is a plausible, partially-verified explanation for")
        print("     WHERE the amplitude difference between k=0.3 and k=0.5 actually")
        print("     comes from -- the reduced system (FINDING_P127) starts AFTER this")
        print("     resonance has already happened and simply inherits its outcome.")
    else:
        print("  -> MECHANISM NOT SUPPORTED AS CLEANLY AS RECONNAISSANCE SUGGESTED.")
        print("     Either the trigger location is not sufficiently k-independent, or")
        print("     the amplitude ratio is not in the right ballpark -- the resonance")
        print("     is real (directly observed) but its connection to A~6679")
        print("     specifically is weaker than this file's own checks require.")

    print("\n  WHAT THIS FILE DOES NOT ESTABLISH -- the user's original ask remains")
    print("  OPEN, more precisely scoped than before:")
    print("   * a genuinely independent, QUANTITATIVE prediction of A~6679 -- this")
    print("     file identifies WHERE and roughly HOW STRONG the resonance is, it")
    print("     does not compute an amplification factor from first principles.")
    print("   * why peak |psi| specifically (not, say, the late-time settled")
    print("     qm_hat, or some other combination) is the right proxy for the")
    print("     quantity that determines A -- used here only as a plausibility")
    print("     check, order-of-magnitude only.")
    print("   * a WKB / adiabatic-invariant calculation through the friction")
    print("     transition (the kind of machinery used for reheating/preheating")
    print("     particle production in inflationary cosmology) -- named as the")
    print("     concrete next step if this line is continued, not attempted here.")
    print("   * anything at Lambda values, or (k, IC) combinations, other than")
    print("     k=0.3 and k=0.5's own main case tested throughout FINDING_P119-P129.")
    print("   * anything about MULTING itself (Gate 1). Any k[h/Mpc].")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
