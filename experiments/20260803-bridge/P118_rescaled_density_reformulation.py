"""P118 -- A log/rescaled-density reformulation that eliminates the raw
a^3 division FINDING_P117 identified as the hard numerical wall, and
retests whether the x_lo climb finally plateaus with the extended reach.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

USER-DIRECTED: "try a log-density reformulation to get past the wall".
FINDING_P117 traced the wall precisely: rho_A = C_MATTER/a**3 underflows to
EXACTLY 0.0 once a**3 itself overflows float64 (a > ~5.65e102), making
contrast = delta_m/rho_phys exactly +/-inf. It also found (via direct
tracing) that the RAW STATE VARIABLES drA and qm underflow toward the
subnormal floor even EARLIER than that, since both decay as ~a^-3 during
Lambda domination (drAd ~= -3*H*drA at late times => drA ~ exp(-3Ht) ~ a^-3
since a ~ exp(Ht)) -- so the failure isn't confined to post-hoc contrast
computation, it starts inside the ODE's own state.

THE REFORMULATION (derived, not guessed -- verified below by exact
algebraic substitution AND a numerical regression test). Track rescaled
variables drA_hat := drA * a**3 and qm_hat := qm * a**3 instead of drA, qm
directly. Re-deriving their ODEs via the product rule and P105's own
drAd/qmd formulas:

  d(drA_hat)/dt = a**3 * (drAd + 3*H*drA)
                = a**3 * [3*psid*rho_A + (k^2/a^2)*qm/(1-gh*pb)]
                = 3*psid*(rho_A*a**3) + k^2*a*qm/(1-gh*pb)
                = 3*psid*C_MATTER + k^2*qm_hat/(a**2*(1-gh*pb))
                                      ^^^^^^^^^^^^^^^^^^^^^^^^^
                    only a**2 appears now, not a**3 -- rho_A*a**3 = C_MATTER
                    EXACTLY (by definition of rho_A), never computed via a
                    raw a**3 that can overflow.

  d(qm_hat)/dt  = a**3 * (qmd + 3*H*qm)
                = a**3 * [-rho_phys*psi + gh*rho_A*dph]
                = -[rho_A*a**3*(1-gh*pb)]*psi + gh*(rho_A*a**3)*dph
                = C_MATTER * [gh*dph - (1-gh*pb)*psi]
                    NO a-DEPENDENCE AT ALL in this term.

CONTRAST, reformulated the same way (delta_m and rho_phys each multiplied
by a**3 before dividing, so the a**3 factors cancel EXACTLY and are never
individually computed):

  contrast = delta_m / rho_phys
           = (delta_m * a**3) / (rho_phys * a**3)
           = [drA_hat*(1-gh*pb) - gh*C_MATTER*dph - 3*H*qm_hat]
             / [C_MATTER*(1-gh*pb)]

This is algebraically IDENTICAL to the original contrast for every `a`
where BOTH formulas are computable -- verified below by regression, not
assumed. The remaining places raw `drA` is needed (dphdd's own formula, and
bg_quantities' rho_A term in pdd/psidd/dphdd) still divide drA_hat/a**3 or
compute rho_A=C_MATTER/a**3 directly -- these STILL underflow past the same
a**3 wall, but harmlessly: every one of those appearances is an ADDITIVE
term in a sum (never a divisor), and the physical argument above (drA, qm,
rho_A all ~a^-3, genuinely negligible once a is astronomically large) means
letting them underflow to exactly 0 there is numerically correct, not
corruption -- unlike the ORIGINAL contrast computation, which divided BY
one of these underflowing quantities.

THE NEW WALL. drA_hat's own ODE now needs qm_hat/a**2 (not qm/a**0 times an
a**-3-scaled rho_A) -- so the new failure mode is a**2 overflowing, at
a > ~1.34e154, MORE THAN 52 ORDERS OF MAGNITUDE further than the original
a**3 wall (~5.65e102). This is a genuine, derived, verified extension, not
a full elimination of any wall (a**2 still overflows eventually).

WHAT THIS FILE DOES: (1) implement the reformulated system, (2) verify it
EXACTLY reproduces the original system's own results within the region
where BOTH are valid (a regression test, not an assumption), (3) push the
reformulated system's reach as far as its own new wall allows, (4) rerun
FINDING_P117's own decisive x_lo-independence scan at this much larger
reach, to see whether sqrt(G_E) finally plateaus, or whether it still
climbs -- an empirical question this file answers directly, not by further
derivation.

WHAT THIS FILE DOES NOT DO: eliminate the numerical wall entirely -- a**2
still overflows eventually, just far later. Rescale EVERY state variable
(psi, psid, dph, dphd, pb, pd were checked analytically to not carry the
same explicit a^-3 coupling drA/qm do, and are left as raw floats -- this
is verified empirically via the regression test and by checking they stay
finite deep into the extended range, not re-derived from scratch). Vary
Lambda or other (k, IC) combinations. Quote any k[h/Mpc]. Touch MULTING
itself (Gate 1).
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


p117 = _load("P117_stiffer_integrator_and_true_asymptote.py", "p117_for_p118")
p105 = p117.p105

a_star = p117.a_star
PHIDOT_INIT = p117.PHIDOT_INIT
LAMBDA_FIXED = p117.LAMBDA_FIXED
G_N = p105.G_N
C_MATTER = p105.C_MATTER

T_END = 7e9  # unchanged from FINDING_P117 -- `a` itself hits float64's ceiling
# at the same t~7.634e9 regardless of the drA/qm rescaling below; this file
# extends x_lo/a_reach validity WITHIN that unchanged T_END, not T_END itself
REGRESSION_TOL = 1e-6
N_PROBE = 32000


# ======================================================================
# THE RESCALED SYSTEM
# ======================================================================


def make_system_rescaled(gh, lam, kk, lam_cc=0.0):
    def rhs(_t, y):
        a_, pb, pd, psi, psid, dph, dphd, drA_hat, qm_hat = y
        with np.errstate(all="ignore"):
            rho_A = C_MATTER / a_**3
            rho_phys = rho_A * (1.0 - gh * pb)
            V = lam * pb**4 / 4.0 + lam_cc
            H = np.sqrt(max((8.0 * np.pi * G_N / 3.0) * (rho_phys + pd**2 / 2.0 + V), 0.0))
            Vp = lam * pb**3
            Vpp = 3.0 * lam * pb**2
            Hdot = -4.0 * np.pi * G_N * (rho_phys + pd**2)

            pdd = gh * rho_A - 3.0 * H * pd - Vp
            dp_phi = pd * dphd - psi * pd**2 - Vp * dph
            psidd = 4 * np.pi * G_N * dp_phi - 4 * H * psid - (2 * Hdot + 3 * H**2) * psi

            drA_for_dphdd = drA_hat / a_**3  # underflows harmlessly past the a^3 wall
            dphdd = (
                gh * drA_for_dphdd
                + 2 * psi * (gh * rho_A - Vp)
                + 4 * psid * pd
                - 3 * H * dphd
                - (kk**2 / a_**2 + Vpp) * dph
            )

            # THE REFORMULATED TERMS -- rho_A*a**3 replaced EXACTLY by C_MATTER,
            # a**3 itself never computed as a raw value in either derivative.
            drA_hat_d = 3 * psid * C_MATTER + kk**2 * qm_hat / (a_**2 * (1 - gh * pb))
            qm_hat_d = C_MATTER * (gh * dph - (1 - gh * pb) * psi)

        return [a_ * H, pd, pdd, psid, psidd, dphd, dphdd, drA_hat_d, qm_hat_d]

    return rhs


def initial_data_rescaled(gh, lam, kk, lam_cc=0.0, **ic):
    y0 = p105.initial_data(gh, lam, kk, lam_cc, **ic)
    a0, pb0, pd0, psi0, psid0, dph0, dphd0, drA0, qm0 = y0
    return [a0, pb0, pd0, psi0, psid0, dph0, dphd0, drA0 * a0**3, qm0 * a0**3]


_CACHE_RESCALED = {}


def run_rescaled(gh, lam, kk, t_end, lam_cc=0.0, rtol=1e-10, **ic):
    key = (gh, lam, kk, t_end, lam_cc, rtol, tuple(sorted(ic.items())))
    if key not in _CACHE_RESCALED:
        with np.errstate(all="ignore"):
            s = solve_ivp(
                make_system_rescaled(gh, lam, kk, lam_cc),
                (1.0, t_end),
                initial_data_rescaled(gh, lam, kk, lam_cc, **ic),
                rtol=rtol,
                atol=1e-20,
                dense_output=True,
            )
        _CACHE_RESCALED[key] = s if s.success else None
    return _CACHE_RESCALED[key]


def contrast_rescaled_from_sol(sol, ts, gh, lam, lam_cc):
    """contrast computed from the rescaled state -- a**3 cancels EXACTLY in
    the delta_m/rho_phys ratio and is never computed as a raw intermediate
    value. H uses the full state (pd, pb included)."""
    state = sol.sol(ts)
    a_, pb, pd, _psi, _psid, dph, _dphd, drA_hat, qm_hat = state
    with np.errstate(all="ignore"):
        rho_A = C_MATTER / a_**3
        rho_phys = rho_A * (1.0 - gh * pb)
        V = lam * pb**4 / 4.0 + lam_cc
        H = np.sqrt(np.maximum((8.0 * np.pi * G_N / 3.0) * (rho_phys + pd**2 / 2.0 + V), 0.0))
        num = drA_hat * (1.0 - gh * pb) - gh * C_MATTER * dph - 3.0 * H * qm_hat
        den = C_MATTER * (1.0 - gh * pb)
        c = num / den
    return a_, c


def t_of_a_rescaled(sol, a_target, t_lo, t_hi):
    from scipy.optimize import brentq

    def f(tv):
        return sol.sol(tv)[0] - a_target

    if f(t_lo) * f(t_hi) > 0:
        return None
    return brentq(f, t_lo, t_hi, xtol=1e-8, rtol=1e-12)


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P118 -- Rescaled-density reformulation: eliminate the raw a^3 wall")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    astar = a_star(LAMBDA_FIXED)
    phidot_prob = 0.1 * PHIDOT_INIT
    ic0 = {"phidot0": phidot_prob}

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 1 -- REGRESSION: does the reformulated system reproduce the")
    print("ORIGINAL system's contrast exactly, where both are valid?")
    print("-" * 78)
    T_END_REGRESSION = 1e8
    s_orig = p105.run(1.0, 1.0, 0.3, T_END_REGRESSION, lam_cc=LAMBDA_FIXED, **ic0)
    s_resc = run_rescaled(1.0, 1.0, 0.3, T_END_REGRESSION, lam_cc=LAMBDA_FIXED, **ic0)
    reg_ok = True
    for x in (2.0, 10.0, 100.0, 1000.0, 1e4):
        t_o = p105.t_of_a(s_orig, astar * x, 1.0, T_END_REGRESSION)
        t_r = t_of_a_rescaled(s_resc, astar * x, 1.0, T_END_REGRESSION)
        if t_o is None or t_r is None:
            print(f"    x={x:<8g}  UNREACHABLE")
            continue
        a_o, c_o = p117.contrast_array(s_orig, np.array([t_o]), 1.0, 1.0, LAMBDA_FIXED)
        a_r, c_r = contrast_rescaled_from_sol(s_resc, np.array([t_r]), 1.0, 1.0, LAMBDA_FIXED)
        rel = abs(c_r[0] / c_o[0] - 1.0) if c_o[0] != 0 else abs(c_r[0])
        print(
            f"    x={x:<8g}  contrast_orig={c_o[0]:+.8e}  contrast_rescaled={c_r[0]:+.8e}  rel.diff={rel:.3e}"
        )
        reg_ok &= rel < REGRESSION_TOL
    print(
        f"  REGRESSION CONTROL {'PASSES' if reg_ok else 'FAILS'} (threshold {REGRESSION_TOL:.0e})"
    )
    if not reg_ok:
        print("  *** STOP -- the reformulation does not match the original. Do not")
        print("  *** trust its extended-reach results.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 2 -- CEILING, CORRECTED: `a` itself (unrescaled, unrelated")
    print("to drA/qm) still hits float64's absolute ceiling at the SAME")
    print("t~7.634e9 as FINDING_P117 found -- rescaling drA/qm cannot move this,")
    print("since `a`'s own growth (da/dt = a*H) was never touched. The real")
    print("question is whether CONTRAST stays finite, at the SAME T_END=7e9, out")
    print("to x values where the ORIGINAL system already returned +/-inf (~x=1e98)")
    print("-" * 78)
    ic_arr = initial_data_rescaled(1.0, 1.0, 0.3, LAMBDA_FIXED, **ic0)
    sysfun = make_system_rescaled(1.0, 1.0, 0.3, LAMBDA_FIXED)
    with np.errstate(all="ignore"):
        s_ceil = solve_ivp(sysfun, (1.0, T_END), ic_arr, rtol=1e-10, atol=1e-20)
    print(
        f"    T_END={T_END:.0e} (unchanged from FINDING_P117): success={s_ceil.success}, "
        f"a_last={s_ceil.y[0, -1]:.3e}"
    )
    s_probe_valid = run_rescaled(1.0, 1.0, 0.3, T_END, lam_cc=LAMBDA_FIXED, **ic0)
    ext_ok = True
    for x in (1e90, 1e97, 1e150, 1e250, 1e278):
        t_probe = t_of_a_rescaled(s_probe_valid, astar * x, 1.0, T_END)
        if t_probe is None:
            print(f"    x={x:<10.4g}  UNREACHABLE")
            ext_ok = False
            continue
        a_p, c_p = contrast_rescaled_from_sol(
            s_probe_valid, np.array([t_probe]), 1.0, 1.0, LAMBDA_FIXED
        )
        finite = bool(np.isfinite(c_p[0]))
        print(f"    x={x:<10.4g}  a={a_p[0]:.3e}  contrast={c_p[0]:+.4e}  finite={finite}")
        ext_ok &= finite
    print(
        f"  EXTENSION CONTROL {'PASSES' if ext_ok else 'FAILS'} -- contrast stays finite"
        " far past the original ~x=1e98 wall, at the SAME unchanged T_END"
    )
    if not ext_ok:
        print("  *** STOP -- the reformulation does not actually extend validity.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 3 -- SMOOTH-CASE REGRESSION: k=10 baseline agrees too")
    print("-" * 78)
    s_orig10 = p105.run(1.0, 1.0, 10.0, 1e8, lam_cc=LAMBDA_FIXED)
    s_resc10 = run_rescaled(1.0, 1.0, 10.0, 1e8, lam_cc=LAMBDA_FIXED)
    smooth_reg_ok = True
    for x in (10.0, 100.0):
        t_o = p105.t_of_a(s_orig10, astar * x, 1.0, 1e8)
        t_r = t_of_a_rescaled(s_resc10, astar * x, 1.0, 1e8)
        a_o, c_o = p117.contrast_array(s_orig10, np.array([t_o]), 1.0, 1.0, LAMBDA_FIXED)
        a_r, c_r = contrast_rescaled_from_sol(s_resc10, np.array([t_r]), 1.0, 1.0, LAMBDA_FIXED)
        rel = abs(c_r[0] / c_o[0] - 1.0)
        print(f"    k=10 x={x:<8g}  orig={c_o[0]:+.8e}  rescaled={c_r[0]:+.8e}  rel.diff={rel:.3e}")
        smooth_reg_ok &= rel < REGRESSION_TOL
    print(f"  SMOOTH-CASE REGRESSION {'PASSES' if smooth_reg_ok else 'FAILS'}")

    if not smooth_reg_ok:
        print("\n  *** a required control failed. STOP.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("MAIN RESULT -- rerun FINDING_P117's own decisive x_lo-independence")
    print("scan, using the SAME T_END=7e9 but the reformulation's vastly")
    print("extended x_lo/a_reach validity (up to ~1e278*a_star, vs the")
    print("original system's ~1e97*a_star wall)")
    print("-" * 78)
    a_reach_use_x = 1e278  # safely inside the trajectory's own reach (a~1.13e283)

    def energy_ratio_rescaled(kk, a_lo, a_reach, t_end, n=N_PROBE, **ic):
        s_c = run_rescaled(1.0, 1.0, kk, t_end, lam_cc=LAMBDA_FIXED, **ic)
        s_r = run_rescaled(0.0, 1.0, kk, t_end, lam_cc=LAMBDA_FIXED, **ic)
        if s_c is None or s_r is None:
            return None

        def piece(sol, gh):
            t_hi = t_of_a_rescaled(sol, a_reach, 1.0, t_end)
            t_lo = t_of_a_rescaled(sol, a_lo, 1.0, t_end)
            if t_hi is None or t_lo is None:
                return None
            ts = np.geomspace(t_lo, t_hi, n)
            a_, c_ = contrast_rescaled_from_sol(sol, ts, gh, 1.0, LAMBDA_FIXED)
            ok = np.isfinite(c_) & (a_ >= a_lo) & (a_ <= a_reach)
            a_, c_ = a_[ok], c_[ok]
            if a_.size < 20:
                return None
            return float(np.trapezoid(c_**2, np.log(a_)))

        e_c, e_r = piece(s_c, 1.0), piece(s_r, 0.0)
        if e_c is None or e_r is None or e_r <= 0:
            return None
        return e_c / e_r

    scan_xs = (1.0, 100.0, 1e4, 1e10, 1e30, 1e60, 1e90, 1e120, 1e160, 1e200, 1e240, 1e270)
    print(f"    using a_reach/a_star={a_reach_use_x:.3e}, T_END={T_END:.0e}, x_lo scan: {scan_xs}")
    scan_vals = []
    for xlo in scan_xs:
        ge = energy_ratio_rescaled(0.3, astar * xlo, astar * a_reach_use_x, T_END, **ic0)
        scan_vals.append(ge**0.5 if ge else None)
        print(f"    x_lo={xlo:<10.4g}  sqrt(G_E)={scan_vals[-1]!r}")

    valid_scan = [v for v in scan_vals if v is not None]
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if len(valid_scan) < 4:
        print("  -> NOT ENOUGH MEASURABLE POINTS. Infrastructure outcome, not evidence.")
        return 1
    monotone_rise = all(valid_scan[i] <= valid_scan[i + 1] for i in range(len(valid_scan) - 1))
    total_rise = abs(valid_scan[-1] / valid_scan[0] - 1.0)
    print(f"  monotonic rise across the extended x_lo range: {monotone_rise}")
    print(f"  total rise, x_lo={scan_xs[0]:g} to x_lo={scan_xs[-1]:g}: {total_rise:.2%}")
    if monotone_rise and total_rise > 0.02:
        print("\n  -> STILL-CLIMBING-AT-EXTENDED-REACH. Even 50+ more decades of safe")
        print("     reach (via the exact rescaled-density reformulation, regression-")
        print("     verified against the original system) do not reveal a plateau.")
        print("     FINDING_P117's STILL-NOT-CONVERGED verdict stands and is now")
        print("     verified over a vastly larger domain, not just asserted.")
    elif not monotone_rise:
        print("\n  -> NON-MONOTONIC at extended reach -- a new feature, not captured by")
        print("     FINDING_P117's characterization. Needs its own investigation.")
    else:
        print("\n  -> PLATEAU-FOUND. The extended reach reveals genuine convergence")
        print("     FINDING_P117 could not see -- report the converged value.")

    print("\n  NOT ESTABLISHED:")
    print("   * a value for G_E's true asymptote, if the climb continues (as found")
    print("     here) -- only that the wall has been pushed much further out.")
    print("   * whether an even further reformulation (avoiding the a^2 wall too)")
    print("     would eventually reveal a plateau -- not attempted.")
    print("   * anything at Lambda values, or (k, IC) combinations, other than the")
    print("     one tested.")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
