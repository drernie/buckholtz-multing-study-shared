"""P114 -- Integrated Energy Growth Observable: a fundamentally different
construction from both point-sampling (FINDING_P105-P111) and window-
averaging (FINDING_P112-P113).

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

USER-DIRECTED: "try a fundamentally different observable, not window-
averaging". FINDING_P113 fixed the anchor bug in the windowed RMS/peak
observable (real progress, 286%->91%/76% spread) but the phase-shift control
still failed a 50% tolerance, traced to a structural limit: this (k, IC)
branch's |contrast(a)| has no power-law plateau wide enough to support a
window average at ANY width tested (a diagnostic-only narrower W=1.2-3
sweep still showed 80% spread). A window average is inherently a LOCAL
construction -- pick a center, average nearby -- and inherits whatever
local curvature is present there, however narrow the window.

THE OBSERVABLE. Instead of a ratio at a point, or an average over a local
window, integrate the SQUARED contrast over the ENTIRE trusted trajectory,
from the very start of integration (a0) out to a chosen reach a_reach:

    E(a_reach) := integral[a0, a_reach] contrast(a)^2 d(ln a)
    G_E(a_reach) := E_coupled(a_reach) / E_reference(a_reach)

No anchor point is needed at all -- this eliminates FINDING_P112/P113's
entire anchor-choice problem structurally, not by picking a better anchor.
A local zero-crossing (FINDING_P111's transient, or the noise-level crossing
FINDING_P112's own reconnaissance found near a/a_star=2.8e-4) contributes a
SMALL amount to the integral, because |contrast|^2 is itself small exactly
where contrast crosses zero -- it does not blow up the way a RATIO does
when its numerator or denominator crosses zero. Convergence is tested the
same way FINDING_P107 tested G_growth itself: does the value stabilize as
a_reach is pushed further, not whether it is insensitive to window width.

RECONNAISSANCE (done before finalizing controls, Compute First):
  k=10 baseline (smooth, already known-converged per FINDING_P107/P108):
    G_E converges almost immediately (2.152 at x=10 -> 2.172 at x=100,
    x=a_reach/a_star), but to sqrt(G_E)=1.474, NOT G_infinity=1.095773.
    This is EXPECTED, not a failure: G_E integrates the WHOLE growth
    history from a0, weighted toward wherever contrast^2 is largest. The
    flat convergence by x=50-100 shows the late-time (Lambda-dominated)
    contribution is already negligible relative to the accumulated total --
    G_E is a genuinely different physical quantity (history-integrated
    accumulated perturbation power) from G_growth (a late-time asymptotic
    point ratio), and the two are not expected to agree numerically. The
    positive control below therefore tests CONVERGENCE, the same criterion
    used for the k<1 case, not numerical agreement with G_infinity.
  k=0.3, phibar_dot(1)x0.1 (the target case): sqrt(G_E) rises to a peak
    (~592000 near x=100) then declines SMOOTHLY AND MONOTONICALLY toward an
    apparent asymptote around 386000-387000 by x=1e6-1e8 -- resolution-
    checked (n=4000 to n=32000 agree to 5 decimal places) and reach-checked
    (T_END pushed to 3e9, the same overflow-adjacent limit FINDING_P108
    established) -- the tightest convergence signal found anywhere in this
    k<1 investigation.

CONTROLS, ALL RUN BEFORE TRUSTING THE k=0.3 CONVERGENCE VERDICT:
  CONVERGENCE (both k=10 and k=0.3): final-step relative change as a_reach
    is pushed to its largest safely-reachable value, same style as
    FINDING_P107.
  AMPLITUDE-SCALING: scaling all three of the coupled run's nonzero-default
    perturbation ICs (psi0, dph0, drA0) together by a factor LAM should
    scale G_E by LAM^2 exactly (contrast_coupled is linear in the full IC
    vector per FINDING_P112's own corrected control; squaring it and
    integrating a homogeneous quadratic preserves that factor exactly).
    Checked directly, not assumed.
  CROSSING-ROBUSTNESS (replaces "phase-shift" -- there is no window here to
    shift; the analogous question is whether the pathological regions that
    broke every earlier observable secretly dominate this one): does
    excising a factor-2 window around the noise-level crossing, or around
    the real transition FINDING_P112 found near a/a_star=6934, change the
    total integral by more than a small amount?

PRE-REGISTERED OUTCOMES for the k=0.3 case, AFTER the controls above pass:
  GAP-CLOSES     G_E converges (within CONV_TOL) as a_reach is pushed to
                 its safe reach limit, and is not dominated by either
                 pathological region -> FINDING_P110's k<1 gap is closed
                 by this observable; report the converged value.
  STILL-OPEN     G_E does not converge even at the safe reach limit, or is
                 shown to be dominated by a pathological region -> the
                 amplitude question remains genuinely open.

AMENDMENT, POST-HOC (kept here rather than silently rewritten, per this
arc's own discipline against erasing pre-registration): a context-
asymmetric skeptic review (claim + code only, no reasoning chain) of the
first committed run found "GAP-CLOSES" overclaims what was actually shown.
Two of its points were accepted as correct and are now reflected in the
VERDICT section of main() below, not in this pre-registration text:
  (1) "a0 is the unique, non-arbitrary starting point of the physical
      trajectory" is false -- a0 = A3_INIT**(1/3) is a fixed convention
      inherited unchanged from P76 (tied to this whole arc's shared ODE
      start time t=1), not a physically privileged epoch. Its sensitivity
      was never independently tested here.
  (2) Calling this "FINDING_P110's k<1 gap closed" overclaims: G_E is
      PROVABLY a different quantity from G_growth (34% off even on the
      smooth k=10 case, by this file's own reconnaissance above), so its
      convergence does not, by itself, establish that G_growth's original
      divergence/instability has been resolved or explained -- it
      establishes something adjacent (a different, well-defined,
      control-passing quantity exists and converges), not the same thing
      under a new name. The VERDICT section below reports
      "OBSERVABLE-CONVERGES", not "GAP-CLOSES".
Two other skeptic points were partially accepted (the amplitude-scaling
control mainly verifies the linear-ODE machinery is wired correctly, not
that the anchor/domain choice is physically meaningful; the narrow
crossing-robustness excision answers a narrower question than the ~40%
lower-limit sensitivity this file's own follow-up check already found and
reported). Full response-matrix detail: FINDING_P114.md.

WHAT THIS FILE DOES NOT DO: claim G_E and G_growth measure the same thing
(they do not, by construction -- see reconnaissance above). Resolve
whether G_E's converged value could be reshaped into something numerically
comparable to G_infinity via a different weighting (e.g. weighting by
d(ln a) starting from a_star instead of a0) -- not attempted, named as a
possible follow-up only if that specific comparison is later needed. Vary
Lambda or other (k, IC) combinations. Quote any k[h/Mpc]. Touch MULTING
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


p112 = _load("P112_envelope_rms_growth_observable.py", "p112_for_p114")
p105 = p112.p105

a_star = p112.a_star
contrast_array = p112.contrast_array
PHIDOT_INIT = p112.PHIDOT_INIT
LAMBDA_FIXED = p112.LAMBDA_FIXED
P107_G_INF_K10 = p112.P107_G_INF_K10

N_PROBE = 16000  # resolution-checked: n=4000..32000 agree to 5 decimal places
CONV_TOL = 0.05  # final-step tolerance, matching FINDING_P107's spirit (2%) but a
# little more generous given this construction is genuinely novel and untested before now
SCALE_TOL = 0.02
CROSSING_TOL = 0.02


def single_energy(sol, gh, lam_cc, t_end, a_reach, n=N_PROBE, exclude=None):
    """integral[a0, a_reach] contrast(a)^2 d(ln a) for ONE run."""
    t_hi = p105.t_of_a(sol, a_reach, 1.0, t_end)
    if t_hi is None:
        return None
    ts = np.geomspace(1.0, t_hi, n)
    a_, c_ = contrast_array(sol, ts, gh, 1.0, lam_cc)
    ok = np.isfinite(c_) & (a_ > 0)
    if exclude is not None:
        lo, hi = exclude
        ok &= ~((a_ >= lo) & (a_ <= hi))
    a_, c_ = a_[ok], c_[ok]
    if a_.size < 20:
        return None
    return float(np.trapezoid(c_**2, np.log(a_)))


def energy_ratio(kk, t_end, lam_cc, a_reach, n=N_PROBE, exclude=None, **ic):
    """G_E(a_reach) = E_coupled / E_reference, same IC applied to both runs
    (mirrors P112's g_rms_peak convention)."""
    s_c = p105.run(1.0, 1.0, kk, t_end, lam_cc=lam_cc, **ic)
    s_r = p105.run(0.0, 1.0, kk, t_end, lam_cc=lam_cc, **ic)
    if s_c is None or s_r is None:
        return None
    e_c = single_energy(s_c, 1.0, lam_cc, t_end, a_reach, n, exclude)
    e_r = single_energy(s_r, 0.0, lam_cc, t_end, a_reach, n)
    if e_c is None or e_r is None or e_r <= 0:
        return None
    return e_c / e_r


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P114 -- Integrated Energy Growth Observable (not point, not window)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    astar = a_star(LAMBDA_FIXED)
    kk_prob, phidot_prob = 0.3, 0.1 * PHIDOT_INIT
    ic0 = {"phidot0": phidot_prob}

    # ==================================================================
    print("\n" + "-" * 78)
    print("POSITIVE CONTROL -- k=10 baseline: does G_E converge as a_reach grows?")
    print(f"(NOT tested against G_infinity={P107_G_INF_K10:.6f} -- G_E is a different quantity")
    print("by construction, see the module docstring's reconnaissance)")
    print("-" * 78)
    pos_rows = []
    for x, te in ((10.0, 1e8), (50.0, 1e8), (100.0, 1e8)):
        ge = energy_ratio(10.0, te, LAMBDA_FIXED, astar * x)
        pos_rows.append(ge)
        sq = ge**0.5 if ge is not None else None
        print(f"    a_reach/a_star={x:<8g} T_END={te:.0e}  G_E={ge!r}  sqrt(G_E)={sq!r}")
    valid_pos = [g for g in pos_rows if g is not None]
    pos_ok = len(valid_pos) >= 2 and abs(valid_pos[-1] / valid_pos[-2] - 1.0) < CONV_TOL
    print(f"  POSITIVE CONTROL {'PASSES' if pos_ok else 'FAILS'} (convergence, tol {CONV_TOL:.0%})")
    if not pos_ok:
        print("  *** the energy-integral machinery does not converge on the known-good")
        print("  *** case. STOP -- fix the observable before trusting the k<1 case.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("AMPLITUDE-SCALING CONTROL -- scaling psi0/dph0/drA0 together by SCALE")
    print("must scale G_E by SCALE^2 exactly")
    print("-" * 78)
    SCALE = 3.0
    ge_base = energy_ratio(kk_prob, 2e9, LAMBDA_FIXED, astar * 1e7, **ic0)
    ic_scaled = dict(ic0, psi0=1e-5 * SCALE, dph0=1e-6 * SCALE, drA0=1e-5 * SCALE)
    s_c_scaled = p105.run(1.0, 1.0, kk_prob, 2e9, lam_cc=LAMBDA_FIXED, **ic_scaled)
    s_r_base = p105.run(0.0, 1.0, kk_prob, 2e9, lam_cc=LAMBDA_FIXED, **ic0)
    e_c_scaled = single_energy(s_c_scaled, 1.0, LAMBDA_FIXED, 2e9, astar * 1e7)
    e_r_base = single_energy(s_r_base, 0.0, LAMBDA_FIXED, 2e9, astar * 1e7)
    ge_scaled = e_c_scaled / e_r_base if (e_c_scaled and e_r_base) else None
    print(f"  G_E(baseline)  = {ge_base!r}")
    print(f"  G_E(ICs x{SCALE})  = {ge_scaled!r}")
    ratio = ge_scaled / ge_base if (ge_base and ge_scaled) else float("nan")
    expect = SCALE**2
    scale_ok = not np.isnan(ratio) and abs(ratio / expect - 1.0) < SCALE_TOL
    print(
        f"  observed ratio = {ratio:.4f}  (expected {expect})  {'OK' if scale_ok else 'MISMATCH'}"
    )
    print(f"  AMPLITUDE-SCALING CONTROL {'PASSES' if scale_ok else 'FAILS'}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("CROSSING-ROBUSTNESS CONTROL -- excising a factor-2 window around each")
    print("pathological region must not change the total integral much")
    print("-" * 78)
    ge_full = ge_base
    ge_excl_noise = energy_ratio(
        kk_prob, 2e9, LAMBDA_FIXED, astar * 1e7, exclude=(14.0, 56.0), **ic0
    )
    ge_excl_trans = energy_ratio(
        kk_prob, 2e9, LAMBDA_FIXED, astar * 1e7, exclude=(3.5e8, 1.4e9), **ic0
    )
    rel_noise = abs(ge_excl_noise / ge_full - 1.0) if ge_excl_noise else float("inf")
    rel_trans = abs(ge_excl_trans / ge_full - 1.0) if ge_excl_trans else float("inf")
    print(f"  full domain           G_E={ge_full!r}")
    print(f"  excl. noise crossing  G_E={ge_excl_noise!r}  rel.diff={rel_noise:.4%}")
    print(f"  excl. real transition G_E={ge_excl_trans!r}  rel.diff={rel_trans:.4%}")
    crossing_ok = rel_noise < CROSSING_TOL and rel_trans < CROSSING_TOL
    print(
        f"  CROSSING-ROBUSTNESS CONTROL {'PASSES' if crossing_ok else 'FAILS'} "
        f"(threshold {CROSSING_TOL:.0%})"
    )

    if not (scale_ok and crossing_ok):
        print("\n  *** a required control failed. STOP -- not proceeding to an")
        print("  *** OBSERVABLE-CONVERGES verdict on an unvalidated observable.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("MAIN TEST -- k=0.3, phidot x0.1: does G_E converge as a_reach is pushed")
    print("to its safe reach limit?")
    print("-" * 78)
    a_ends = [astar * x for x in (1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8)]
    t_ends = [1e8, 1e8, 1e9, 1e9, 2e9, 3e9, 3e9]
    rows = []
    for a_reach, te in zip(a_ends, t_ends, strict=True):
        ge = energy_ratio(kk_prob, te, LAMBDA_FIXED, a_reach, **ic0)
        rows.append((a_reach / astar, ge))
        sq = ge**0.5 if ge is not None else None
        print(
            f"    a_reach/a_star={a_reach / astar:<12.4e} T_END={te:.0e}  G_E={ge!r}  sqrt(G_E)={sq!r}"
        )

    valid_rows = [(x, g) for x, g in rows if g is not None]
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if len(valid_rows) < 3:
        print("  -> NOT ENOUGH MEASURABLE POINTS. Infrastructure outcome, not evidence.")
        return 1
    last_two = [g for _x, g in valid_rows[-2:]]
    final_change = abs(last_two[-1] / last_two[-2] - 1.0) if last_two[-2] else float("inf")
    print(f"  final-step relative change in G_E (last two measured points): {final_change:.4%}")
    if final_change < CONV_TOL:
        conv_val = last_two[-1]
        print(f"\n  -> OBSERVABLE-CONVERGES. G_E converges to {conv_val:.6e}")
        print(f"     (sqrt={conv_val**0.5:.2f}) within a {CONV_TOL:.0%} final-step tolerance,")
        print("     and survives both the amplitude-scaling and (narrow) crossing-")
        print("     robustness controls. NOT reported as 'the k<1 gap closes': G_E is")
        print("     PROVABLY a different quantity from G_growth (34% off even on the")
        print("     smooth k=10 case), and a context-asymmetric skeptic review (see")
        print("     FINDING_P114.md) found this file's own lower-limit choice (a0) is")
        print("     a fixed convention inherited from P76, not independently stress-")
        print("     tested for sensitivity -- and a follow-up check found the converged")
        print("     value DOES depend materially (~40%) on how much of the transient")
        print("     region the lower limit includes. What IS established: a well-")
        print("     defined, numerically stable, control-passing quantity exists for")
        print("     this (k, IC) branch where every point-sampled/windowed attempt")
        print("     could not produce one -- a narrower, more honest claim than")
        print("     'the growth-ratio question is resolved'.")
    else:
        print("\n  -> STILL-OPEN. G_E does not converge even at the safe reach limit.")

    print("\n  NOT ESTABLISHED:")
    print("   * that G_E and G_growth measure the same physical quantity -- they do")
    print("     not, by construction (see docstring reconnaissance).")
    print("   * that FINDING_P110's original k<1 growth-RATIO question is resolved --")
    print("     it is not; G_E is a different, adjacent quantity (skeptic-corrected).")
    print("   * that a0 (inherited from P76's A3_INIT convention) is a physically")
    print("     privileged epoch rather than simply where this arc's shared ODE")
    print("     integration happens to start (skeptic-corrected; not independently")
    print("     stress-tested here).")
    print("   * anything at Lambda values, or (k, IC) combinations, other than the")
    print("     one tested.")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
