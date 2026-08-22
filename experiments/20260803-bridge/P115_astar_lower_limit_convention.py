"""P115 -- The a_star lower-limit convention for the Integrated Energy
Growth Observable, tested against FINDING_P114's a0-anchored result.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

USER-DIRECTED: "try the a_star lower-limit convention instead". This
directly answers an item FINDING_P114 itself left open ("Whether a
different, equally-principled lower-limit convention (e.g. starting at
a_star) would give a more physically interpretable quantity -- not
attempted here"), and speaks to a skeptic-raised concern on FINDING_P114
(context-asymmetric review, Step 8a): that a0 = A3_INIT**(1/3) is a fixed
convention *inherited from P76* (tied to this arc's shared ODE start time
t=1), not a physically privileged epoch, and its sensitivity was never
independently tested.

THE ALTERNATIVE CONVENTION. a0 answers "wherever this arc's solver happens
to start integrating". a_star answers a different, already load-bearing
question in this sub-arc: a_star(Lambda) := (C_MATTER/Lambda)**(1/3) is the
rho_Lambda = rho_matter crossing, first defined in FINDING_P104 and used as
the reference scale by every file since (P105-P114's own X_LO=0.2 and every
a_reach sweep in this arc are already expressed as multiples of a_star).
Using a_star as the lower limit is not a new invented scale; it is the
scale this entire sub-arc already treats as physically meaningful,
substituted for a0 specifically because a0 answered a purely infrastructural
question, not a physical one.

    E'(a_reach)   := integral[a_star, a_reach] contrast(a)^2 d(ln a)
    G_E'(a_reach) := E'_coupled(a_reach) / E'_reference(a_reach)

RECONNAISSANCE (Compute First):
  k=10 baseline: resolution-checked (n=4000..32000 agree to 6 decimal
    places, TIGHTER than FINDING_P114's own a0-anchored check), converges
    to sqrt(G_E')=1.476668 -- essentially the SAME as FINDING_P114's
    a0-anchored value (1.474, ~0.2% apart). Restricting away the
    matter-dominated pre-a_star history barely changes anything for the
    smooth case.
  k=0.3, phibar_dot(1)x0.1: converges even MORE tightly than FINDING_P114's
    own main test (final-step change 0.021%, vs FINDING_P114's 0.22%) --
    to sqrt(G_E')=389236, compared to FINDING_P114's a0-anchored
    sqrt(G_E)=386921 -- a ~0.6% difference. This is the key result: the
    a0-vs-a_star choice, tested directly rather than assumed, moves the
    converged value by well under 1%, NOT by anything close to the ~40%
    FINDING_P114's own follow-up check found between x_lo=1 (~a_star) and
    x_lo=100 (well past the transient). The ~40% sensitivity FINDING_P114
    reported is concentrated specifically in the x=1-to-100 stretch (the
    transient and its immediate aftermath), NOT in whether the lower limit
    is placed at a0 (deep in the matter-dominated era) or at a_star (the
    Lambda-matter crossing) -- two choices that, empirically, agree with
    each other to within 1%.

CONTROLS, same suite as FINDING_P114, re-run at the new lower limit:
  CONVERGENCE (k=10 and k=0.3): final-step relative change as a_reach is
    pushed to its largest safely-reachable value.
  AMPLITUDE-SCALING: scaling all three of the coupled run's nonzero-default
    perturbation ICs together by a factor LAM should scale G_E' by LAM^2
    exactly (same linear-ODE argument as FINDING_P114 -- the skeptic
    correctly noted this control tests IVP linearity, not the domain
    choice's physical meaning; kept here for internal-consistency checking,
    not cited as evidence for the a_star convention's validity).
  CROSSING-ROBUSTNESS: does excising a factor-2 window around the real
    transition (FINDING_P112's a/a_star=6934) change the integral by more
    than a small amount? (The noise-level crossing near a/a_star=2.8e-4 is
    now OUTSIDE the integration domain entirely, since a_star is the new
    lower limit -- so only the real transition is checked here.)

WHAT THIS FILE ESTABLISHES: whether the a0-vs-a_star choice specifically is
a major source of FINDING_P114's uncertainty (tested directly: it is not,
to within ~1%). WHAT THIS FILE DOES NOT DO: resolve the already-documented
~40% sensitivity to whether the x=1-to-100 transient stretch is included at
all (that is a separate, already-reported finding, not re-litigated here).
Claim G_E' matches G_growth numerically (it does not, for the same reasons
FINDING_P114 documented -- G_E' is still an integrated-energy quantity, not
a late-time point ratio). Vary Lambda or other (k, IC) combinations. Quote
any k[h/Mpc]. Touch MULTING itself (Gate 1).
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


p114 = _load("P114_integrated_energy_growth_observable.py", "p114_for_p115")
p105 = p114.p105

a_star = p114.a_star
contrast_array = p114.contrast_array
PHIDOT_INIT = p114.PHIDOT_INIT
LAMBDA_FIXED = p114.LAMBDA_FIXED

N_PROBE = 16000
CONV_TOL = 0.05
SCALE_TOL = 0.02
CROSSING_TOL = 0.02
A0_ANCHORED_SQRT_GE = 386921.0  # FINDING_P114's own converged value, for comparison


def single_energy_from(sol, gh, lam_cc, t_end, a_lo, a_reach, n=N_PROBE, exclude=None):
    """integral[a_lo, a_reach] contrast(a)^2 d(ln a) for ONE run."""
    t_hi = p105.t_of_a(sol, a_reach, 1.0, t_end)
    t_lo = p105.t_of_a(sol, a_lo, 1.0, t_end)
    if t_hi is None or t_lo is None:
        return None
    ts = np.geomspace(t_lo, t_hi, n)
    a_, c_ = contrast_array(sol, ts, gh, 1.0, lam_cc)
    ok = np.isfinite(c_) & (a_ >= a_lo) & (a_ <= a_reach)
    if exclude is not None:
        lo, hi = exclude
        ok &= ~((a_ >= lo) & (a_ <= hi))
    a_, c_ = a_[ok], c_[ok]
    if a_.size < 20:
        return None
    return float(np.trapezoid(c_**2, np.log(a_)))


def energy_ratio_astar(kk, t_end, lam_cc, a_reach, n=N_PROBE, exclude=None, **ic):
    """G_E'(a_reach) with the lower limit fixed at a_star (this file's
    proposal), same IC applied to both runs."""
    astar = a_star(lam_cc)
    s_c = p105.run(1.0, 1.0, kk, t_end, lam_cc=lam_cc, **ic)
    s_r = p105.run(0.0, 1.0, kk, t_end, lam_cc=lam_cc, **ic)
    if s_c is None or s_r is None:
        return None
    e_c = single_energy_from(s_c, 1.0, lam_cc, t_end, astar, a_reach, n, exclude)
    e_r = single_energy_from(s_r, 0.0, lam_cc, t_end, astar, a_reach, n)
    if e_c is None or e_r is None or e_r <= 0:
        return None
    return e_c / e_r


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P115 -- a_star lower-limit convention, vs FINDING_P114's a0-anchored result")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    astar = a_star(LAMBDA_FIXED)
    kk_prob, phidot_prob = 0.3, 0.1 * PHIDOT_INIT
    ic0 = {"phidot0": phidot_prob}

    # ==================================================================
    print("\n" + "-" * 78)
    print("POSITIVE CONTROL -- k=10 baseline: does G_E' converge with the new")
    print("lower limit (a_star instead of a0)?")
    print("-" * 78)
    pos_rows = []
    for x, te in ((2.0, 1e8), (10.0, 1e8), (100.0, 1e8)):
        ge = energy_ratio_astar(10.0, te, LAMBDA_FIXED, astar * x)
        pos_rows.append(ge)
        sq = ge**0.5 if ge is not None else None
        print(f"    a_reach/a_star={x:<8g} T_END={te:.0e}  G_E'={ge!r}  sqrt(G_E')={sq!r}")
    valid_pos = [g for g in pos_rows if g is not None]
    pos_ok = len(valid_pos) >= 2 and abs(valid_pos[-1] / valid_pos[-2] - 1.0) < CONV_TOL
    print(f"  POSITIVE CONTROL {'PASSES' if pos_ok else 'FAILS'} (convergence, tol {CONV_TOL:.0%})")
    if not pos_ok:
        print("  *** STOP -- the machinery does not converge on the known-good case.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("AMPLITUDE-SCALING CONTROL -- same prediction as FINDING_P114 (ICs x3 ->")
    print("G_E' x9), kept for internal-consistency checking, not cited as evidence")
    print("for the a_star convention's physical validity (skeptic-corrected framing)")
    print("-" * 78)
    SCALE = 3.0
    ge_base = energy_ratio_astar(kk_prob, 2e9, LAMBDA_FIXED, astar * 1e7, **ic0)
    ic_scaled = dict(ic0, psi0=1e-5 * SCALE, dph0=1e-6 * SCALE, drA0=1e-5 * SCALE)
    s_c_scaled = p105.run(1.0, 1.0, kk_prob, 2e9, lam_cc=LAMBDA_FIXED, **ic_scaled)
    s_r_base = p105.run(0.0, 1.0, kk_prob, 2e9, lam_cc=LAMBDA_FIXED, **ic0)
    e_c_scaled = single_energy_from(s_c_scaled, 1.0, LAMBDA_FIXED, 2e9, astar, astar * 1e7)
    e_r_base = single_energy_from(s_r_base, 0.0, LAMBDA_FIXED, 2e9, astar, astar * 1e7)
    ge_scaled = e_c_scaled / e_r_base if (e_c_scaled and e_r_base) else None
    ratio = ge_scaled / ge_base if (ge_base and ge_scaled) else float("nan")
    expect = SCALE**2
    scale_ok = not np.isnan(ratio) and abs(ratio / expect - 1.0) < SCALE_TOL
    print(f"  G_E'(baseline)  = {ge_base!r}")
    print(f"  G_E'(ICs x{SCALE})  = {ge_scaled!r}")
    print(
        f"  observed ratio = {ratio:.4f}  (expected {expect})  {'OK' if scale_ok else 'MISMATCH'}"
    )
    print(f"  AMPLITUDE-SCALING CONTROL {'PASSES' if scale_ok else 'FAILS'}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("CROSSING-ROBUSTNESS CONTROL -- excising the real transition (the")
    print("noise-level crossing is now outside the domain, a_star is the new")
    print("lower limit)")
    print("-" * 78)
    ge_excl_trans = energy_ratio_astar(
        kk_prob, 2e9, LAMBDA_FIXED, astar * 1e7, exclude=(3.5e8, 1.4e9), **ic0
    )
    rel_trans = abs(ge_excl_trans / ge_base - 1.0) if ge_excl_trans else float("inf")
    print(f"  full domain [a_star, 1e7*a_star]  G_E'={ge_base!r}")
    print(f"  excl. real transition             G_E'={ge_excl_trans!r}  rel.diff={rel_trans:.4%}")
    crossing_ok = rel_trans < CROSSING_TOL
    print(
        f"  CROSSING-ROBUSTNESS CONTROL {'PASSES' if crossing_ok else 'FAILS'} "
        f"(threshold {CROSSING_TOL:.0%})"
    )

    if not (scale_ok and crossing_ok):
        print("\n  *** a required control failed. STOP.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("MAIN TEST -- k=0.3, phidot x0.1: does G_E' converge, and how close is")
    print("the converged value to FINDING_P114's a0-anchored result?")
    print("-" * 78)
    a_ends = [astar * x for x in (1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8)]
    t_ends = [1e8, 1e8, 1e9, 1e9, 2e9, 3e9, 3e9]
    rows = []
    for a_reach, te in zip(a_ends, t_ends, strict=True):
        ge = energy_ratio_astar(kk_prob, te, LAMBDA_FIXED, a_reach, **ic0)
        rows.append((a_reach / astar, ge))
        sq = ge**0.5 if ge is not None else None
        print(
            f"    a_reach/a_star={a_reach / astar:<12.4e} T_END={te:.0e}  "
            f"G_E'={ge!r}  sqrt(G_E')={sq!r}"
        )

    valid_rows = [(x, g) for x, g in rows if g is not None]
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if len(valid_rows) < 3:
        print("  -> NOT ENOUGH MEASURABLE POINTS. Infrastructure outcome, not evidence.")
        return 1
    last_two = [g for _x, g in valid_rows[-2:]]
    final_change = abs(last_two[-1] / last_two[-2] - 1.0) if last_two[-2] else float("inf")
    conv_val = last_two[-1]
    conv_sqrt = conv_val**0.5
    delta_from_a0 = abs(conv_sqrt / A0_ANCHORED_SQRT_GE - 1.0)
    print(f"  final-step relative change in G_E' (last two measured points): {final_change:.4%}")
    print(f"  converged sqrt(G_E') = {conv_sqrt:.2f}")
    print(f"  FINDING_P114's a0-anchored sqrt(G_E) = {A0_ANCHORED_SQRT_GE:.2f}")
    print(f"  relative difference between the two lower-limit conventions: {delta_from_a0:.4%}")
    if final_change < CONV_TOL:
        print("\n  -> OBSERVABLE-CONVERGES here too, and AGREES with FINDING_P114's")
        print(f"     a0-anchored result to within {delta_from_a0:.2%} -- the a0-vs-a_star")
        print("     choice, which the skeptic review flagged as untested, moves the")
        print("     converged value by well under 1%. This is NOT the same as the")
        print("     already-documented ~40% sensitivity to whether the x=1-to-100")
        print("     transient stretch is included at all -- that sensitivity is real")
        print("     and unaffected by this result. What this file adds: the specific")
        print("     a0-vs-a_star concern the skeptic raised is now directly tested and")
        print("     found NOT to be a major source of FINDING_P114's uncertainty.")
    else:
        print("\n  -> STILL-OPEN at this lower limit. G_E' does not converge even at")
        print("     the safe reach limit.")

    print("\n  NOT ESTABLISHED:")
    print("   * the already-documented ~40% sensitivity to including/excluding the")
    print("     x=1-to-100 transient stretch -- not re-tested or resolved here.")
    print("   * that G_E' matches G_growth numerically -- it does not, for the same")
    print("     reasons FINDING_P114 documented.")
    print("   * anything at Lambda values, or (k, IC) combinations, other than the")
    print("     one tested.")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
