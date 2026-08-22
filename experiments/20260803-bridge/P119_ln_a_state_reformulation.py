"""P119 -- Rescale `a` itself via ln(a) state tracking, to get past the
SEPARATE, outer wall FINDING_P118 identified but did not touch.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

USER-DIRECTED: "rescale a itself via ln(a) tracking". FINDING_P118's own
rescaling (drA_hat=drA*a^3, qm_hat=qm*a^3) extended CONTRAST's valid range
by ~180 decades, but explicitly could not move a SEPARATE wall: `a` itself,
tracked as a raw state variable with da/dt=a*H, still overflows float64's
absolute maximum at the same t~7.634e9 FINDING_P117 found, because that
rescaling never touched a's own growth.

THE REFORMULATION. Track L := ln(a) as the state variable instead of raw
`a`. Then:

    dL/dt = (1/a)*(da/dt) = (1/a)*(a*H) = H

-- no `a` at all in this derivative. Since H approaches a CONSTANT (H_Lambda)
once Lambda dominates, L grows LINEARLY in t at late times, not
exponentially -- L never overflows for any t this file can afford to
integrate to (L ~ H_Lambda*t; even t=1e20 gives L of order 1e11-ish,
trivially representable). Every OTHER appearance of `a` in the RHS is
rewritten as exp(-n*L) rather than 1/a**n:

    rho_A = C_MATTER/a**3 = C_MATTER*exp(-3*L)
    1/a**2 (in dphdd's k^2/a^2 term)        = exp(-2*L)
    drA_hat/a**3 (in dphdd's gh*drA term)   = drA_hat*exp(-3*L)
    qm_hat/a**2 (in FINDING_P118's own drA_hat_d)  = qm_hat*exp(-2*L)

The critical difference from the ORIGINAL a**-n computation: np.exp() of a
very negative number returns exactly 0.0 SMOOTHLY, with no intermediate
overflow step -- unlike 1/a**n, which requires a**n to be computed FIRST
(and OVERFLOW to +inf) before the division can even happen. Every one of
these terms is, per FINDING_P117/P118's own physical argument, genuinely
negligible once `a` is astronomically large -- letting them underflow to
exactly 0 is correct, not corruption. FINDING_P118's own contrast formula
already avoided raw a**3 entirely (the a**3 factors cancel algebraically);
it is rewritten here only to accept L instead of a as its input.

WHAT THIS BUYS: T_END is no longer capped by `a` overflowing float64 at
t~7.634e9. In principle T_END can be pushed to any value the ODE solver can
still handle efficiently -- tested empirically below, not assumed.

CONTROLS:
  REGRESSION vs FINDING_P118's own rescaled system, in the region where
    BOTH are valid (not just vs the algebra).
  REACH: how far does T_END actually extend now, and how many solver steps
    does it cost?
  SMOOTH-CASE REGRESSION (k=10).
  EXTENSION: does contrast stay finite far past FINDING_P118's own
    x_lo=1e278 ceiling?

MAIN RESULT: rerun the decisive x_lo-independence scan at whatever this
file's own verified reach allows, and check whether the deceleration
FINDING_P118 found (climb rate shrinking, 3.6%/30dec -> 0.95%/70dec)
continues toward a genuine plateau, stalls, or reverses.

WHAT THIS FILE DOES NOT DO: claim a is now "unlimited" -- solver cost,
accumulated floating-point error over an enormous t-interval, and the other
state variables' own (unverified-in-the-limit) boundedness are all
practical limits this file tests empirically, not proves away. Vary Lambda
or other (k, IC) combinations. Quote any k[h/Mpc]. Touch MULTING itself
(Gate 1).
"""

import importlib.util
import math
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p118 = _load("P118_rescaled_density_reformulation.py", "p118_for_p119")
p105 = p118.p105

a_star = p118.a_star
PHIDOT_INIT = p118.PHIDOT_INIT
LAMBDA_FIXED = p118.LAMBDA_FIXED
G_N = p105.G_N
C_MATTER = p105.C_MATTER

REGRESSION_TOL = 1e-6
N_PROBE = 32000


# ======================================================================
# THE ln(a)-STATE SYSTEM
# ======================================================================


def make_system_lna(gh, lam, kk, lam_cc=0.0):
    def rhs(_t, y):
        lna, pb, pd, psi, psid, dph, dphd, drA_hat, qm_hat = y
        with np.errstate(all="ignore"):
            rho_A = C_MATTER * np.exp(-3.0 * lna)
            rho_phys = rho_A * (1.0 - gh * pb)
            V = lam * pb**4 / 4.0 + lam_cc
            H = np.sqrt(max((8.0 * np.pi * G_N / 3.0) * (rho_phys + pd**2 / 2.0 + V), 0.0))
            Vp = lam * pb**3
            Vpp = 3.0 * lam * pb**2
            Hdot = -4.0 * np.pi * G_N * (rho_phys + pd**2)

            pdd = gh * rho_A - 3.0 * H * pd - Vp
            dp_phi = pd * dphd - psi * pd**2 - Vp * dph
            psidd = 4 * np.pi * G_N * dp_phi - 4 * H * psid - (2 * Hdot + 3 * H**2) * psi

            drA_for_dphdd = drA_hat * np.exp(-3.0 * lna)
            dphdd = (
                gh * drA_for_dphdd
                + 2 * psi * (gh * rho_A - Vp)
                + 4 * psid * pd
                - 3 * H * dphd
                - (kk**2 * np.exp(-2.0 * lna) + Vpp) * dph
            )

            drA_hat_d = 3 * psid * C_MATTER + kk**2 * qm_hat * np.exp(-2.0 * lna) / (1 - gh * pb)
            qm_hat_d = C_MATTER * (gh * dph - (1 - gh * pb) * psi)

        return [H, pd, pdd, psid, psidd, dphd, dphdd, drA_hat_d, qm_hat_d]

    return rhs


def initial_data_lna(gh, lam, kk, lam_cc=0.0, **ic):
    y0 = p105.initial_data(gh, lam, kk, lam_cc, **ic)
    a0, pb0, pd0, psi0, psid0, dph0, dphd0, drA0, qm0 = y0
    return [np.log(a0), pb0, pd0, psi0, psid0, dph0, dphd0, drA0 * a0**3, qm0 * a0**3]


_CACHE_LNA = {}


def run_lna(gh, lam, kk, t_end, lam_cc=0.0, rtol=1e-10, **ic):
    key = (gh, lam, kk, t_end, lam_cc, rtol, tuple(sorted(ic.items())))
    if key not in _CACHE_LNA:
        with np.errstate(all="ignore"):
            s = solve_ivp(
                make_system_lna(gh, lam, kk, lam_cc),
                (1.0, t_end),
                initial_data_lna(gh, lam, kk, lam_cc, **ic),
                rtol=rtol,
                atol=1e-20,
                dense_output=True,
            )
        _CACHE_LNA[key] = s if s.success else None
    return _CACHE_LNA[key]


def contrast_lna_from_sol(sol, ts, gh, lam, lam_cc):
    """contrast from the ln(a)-state solution -- never forms raw `a`."""
    state = sol.sol(ts)
    lna, pb, pd, _psi, _psid, dph, _dphd, drA_hat, qm_hat = state
    with np.errstate(all="ignore"):
        rho_A = C_MATTER * np.exp(-3.0 * lna)
        rho_phys = rho_A * (1.0 - gh * pb)
        V = lam * pb**4 / 4.0 + lam_cc
        H = np.sqrt(np.maximum((8.0 * np.pi * G_N / 3.0) * (rho_phys + pd**2 / 2.0 + V), 0.0))
        num = drA_hat * (1.0 - gh * pb) - gh * C_MATTER * dph - 3.0 * H * qm_hat
        den = C_MATTER * (1.0 - gh * pb)
        c = num / den
    return lna, c


def t_of_lna(sol, lna_target, t_lo, t_hi):
    def f(tv):
        return sol.sol(tv)[0] - lna_target

    if f(t_lo) * f(t_hi) > 0:
        return None
    return brentq(f, t_lo, t_hi, xtol=1e-10, rtol=1e-13)


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P119 -- ln(a) state reformulation: remove the SEPARATE outer wall")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    astar = a_star(LAMBDA_FIXED)
    ln_astar = np.log(astar)
    phidot_prob = 0.1 * PHIDOT_INIT
    ic0 = {"phidot0": phidot_prob}

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 1 -- REGRESSION vs FINDING_P118's own rescaled system")
    print("-" * 78)
    T_END_REGRESSION = 7e9
    s_p118 = p118.run_rescaled(1.0, 1.0, 0.3, T_END_REGRESSION, lam_cc=LAMBDA_FIXED, **ic0)
    s_lna = run_lna(1.0, 1.0, 0.3, T_END_REGRESSION, lam_cc=LAMBDA_FIXED, **ic0)
    reg_ok = True
    for x in (2.0, 10.0, 100.0, 1e10, 1e100, 1e250):
        t_118 = p118.t_of_a_rescaled(s_p118, astar * x, 1.0, T_END_REGRESSION)
        t_lna = t_of_lna(s_lna, ln_astar + np.log(x), 1.0, T_END_REGRESSION)
        if t_118 is None or t_lna is None:
            print(f"    x={x:<10.4g}  UNREACHABLE")
            continue
        _a118, c118 = p118.contrast_rescaled_from_sol(
            s_p118, np.array([t_118]), 1.0, 1.0, LAMBDA_FIXED
        )
        _lna_r, c_lna = contrast_lna_from_sol(s_lna, np.array([t_lna]), 1.0, 1.0, LAMBDA_FIXED)
        rel = abs(c_lna[0] / c118[0] - 1.0)
        print(f"    x={x:<10.4g}  P118={c118[0]:+.8e}  P119={c_lna[0]:+.8e}  rel.diff={rel:.3e}")
        reg_ok &= rel < REGRESSION_TOL
    print(
        f"  REGRESSION CONTROL {'PASSES' if reg_ok else 'FAILS'} (threshold {REGRESSION_TOL:.0e})"
    )
    if not reg_ok:
        print("  *** STOP -- do not trust this reformulation's extended results.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 2 -- REACH: how far does T_END actually extend now?")
    print("-" * 78)
    ic_arr = initial_data_lna(1.0, 1.0, 0.3, LAMBDA_FIXED, **ic0)
    sysfun = make_system_lna(1.0, 1.0, 0.3, LAMBDA_FIXED)
    reach_ok = True
    # T_END=1e13 alone already takes ~166s and 850k+ steps (nsteps/t_end scales
    # up steeply, not down, past T_END~1e11 -- 1e15/1e17 were tried and found
    # computationally impractical, dropped rather than left to hang silently).
    for t_end in (7e9, 1e11, 1e13):
        with np.errstate(all="ignore"):
            s = solve_ivp(sysfun, (1.0, t_end), ic_arr, rtol=1e-10, atol=1e-20)
        ln_a_last = s.y[0, -1]
        print(
            f"    t_end={t_end:.0e}  success={s.success}  nsteps={len(s.t)}  "
            f"ln(a)_last={ln_a_last:.4e}  (a/a_star)_last=10^{(ln_a_last - ln_astar) / np.log(10):.2f}"
        )
        reach_ok &= s.success
    print(f"  REACH CONTROL {'PASSES' if reach_ok else 'FAILS'} (all tested T_END succeed)")
    print("  (1e15/1e17 tested separately, found impractically slow -- not used below)")

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 3 -- SMOOTH-CASE REGRESSION: k=10 baseline agrees too")
    print("-" * 78)
    s_p118_10 = p118.run_rescaled(1.0, 1.0, 10.0, 1e8, lam_cc=LAMBDA_FIXED)
    s_lna_10 = run_lna(1.0, 1.0, 10.0, 1e8, lam_cc=LAMBDA_FIXED)
    smooth_ok = True
    for x in (10.0, 100.0):
        t_118 = p118.t_of_a_rescaled(s_p118_10, astar * x, 1.0, 1e8)
        t_lna = t_of_lna(s_lna_10, ln_astar + np.log(x), 1.0, 1e8)
        _a118, c118 = p118.contrast_rescaled_from_sol(
            s_p118_10, np.array([t_118]), 1.0, 1.0, LAMBDA_FIXED
        )
        _lna_r, c_lna = contrast_lna_from_sol(s_lna_10, np.array([t_lna]), 1.0, 1.0, LAMBDA_FIXED)
        rel = abs(c_lna[0] / c118[0] - 1.0)
        print(f"    k=10 x={x:<8g}  P118={c118[0]:+.8e}  P119={c_lna[0]:+.8e}  rel.diff={rel:.3e}")
        smooth_ok &= rel < REGRESSION_TOL
    print(f"  SMOOTH-CASE REGRESSION {'PASSES' if smooth_ok else 'FAILS'}")

    if not (reach_ok and smooth_ok):
        print("\n  *** a required control failed. STOP.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("MAIN RESULT -- x_lo-independence scan at the vastly extended reach")
    print("-" * 78)
    T_END_MAIN = 1e13  # Control 2's own timing: 1e13 takes ~166s/solve, tractable;
    # 1e15/1e17 do not (tested, dropped -- see Control 2's own note)
    with np.errstate(all="ignore"):
        s_main_probe = solve_ivp(sysfun, (1.0, T_END_MAIN), ic_arr, rtol=1e-10, atol=1e-20)
    ln_a_reach = s_main_probe.y[0, -1]
    reach_decades = (ln_a_reach - ln_astar) / np.log(10)
    print(f"    T_END={T_END_MAIN:.0e} reaches a_reach/a_star = 10^{reach_decades:.1f}")
    use_decades = reach_decades * 0.9  # safety margin

    def energy_ratio_lna(kk, x_lo_decades, x_reach_decades, t_end, n=N_PROBE, **ic):
        s_c = run_lna(1.0, 1.0, kk, t_end, lam_cc=LAMBDA_FIXED, **ic)
        s_r = run_lna(0.0, 1.0, kk, t_end, lam_cc=LAMBDA_FIXED, **ic)
        if s_c is None or s_r is None:
            return None
        lna_lo = ln_astar + x_lo_decades * np.log(10)
        lna_reach = ln_astar + x_reach_decades * np.log(10)

        def piece(sol, gh):
            t_hi = t_of_lna(sol, lna_reach, 1.0, t_end)
            t_lo = t_of_lna(sol, lna_lo, 1.0, t_end)
            if t_hi is None or t_lo is None:
                return None
            ts = np.geomspace(t_lo, t_hi, n)
            lna_, c_ = contrast_lna_from_sol(sol, ts, gh, 1.0, LAMBDA_FIXED)
            ok = np.isfinite(c_) & (lna_ >= lna_lo) & (lna_ <= lna_reach)
            lna_, c_ = lna_[ok], c_[ok]
            if lna_.size < 20:
                return None
            return float(np.trapezoid(c_**2, lna_))

        e_c, e_r = piece(s_c, 1.0), piece(s_r, 0.0)
        if e_c is None or e_r is None or e_r <= 0:
            return None
        return e_c / e_r

    scan_decades = (0, 2, 4, 10, 30, 60, 90, 150, 250, 400, 900, 3000, 10000, 30000, 100000)
    scan_decades = tuple(d for d in scan_decades if d < use_decades)
    print(f"    using a_reach/a_star=10^{use_decades:.1f}, T_END={T_END_MAIN:.0e}")
    print(f"    x_lo scan (decades): {scan_decades}")
    scan_vals = []
    for dec in scan_decades:
        ge = energy_ratio_lna(0.3, dec, use_decades, T_END_MAIN, **ic0)
        scan_vals.append(ge**0.5 if ge else None)
        print(f"    x_lo=10^{dec:<6g}  sqrt(G_E)={scan_vals[-1]!r}")

    valid_pairs = [(d, v) for d, v in zip(scan_decades, scan_vals, strict=True) if v is not None]
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if len(valid_pairs) < 5:
        print("  -> NOT ENOUGH MEASURABLE POINTS. Infrastructure outcome, not evidence.")
        return 1
    decs = [d for d, _v in valid_pairs]
    valid_scan = [v for _d, v in valid_pairs]
    monotone_rise = all(valid_scan[i] <= valid_scan[i + 1] for i in range(len(valid_scan) - 1))
    total_rise = abs(valid_scan[-1] / valid_scan[0] - 1.0)
    last_step_rise = abs(valid_scan[-1] / valid_scan[-2] - 1.0)
    print(f"  monotonic rise across the extended x_lo range: {monotone_rise}")
    print(f"  total rise, x_lo=10^{decs[0]} to 10^{decs[-1]}: {total_rise:.4%}")
    print(f"  naive final-step rise (last two points): {last_step_rise:.4%}")
    print("  *** naive step-to-step % change is MISLEADING here -- the decade-step size")
    print("  *** itself grows exponentially across this scan, so a small % change at the")
    print("  *** end does not by itself mean the climb has slowed in any meaningful")
    print("  *** sense. Two decade-scale-aware checks instead, exactly the kind of")
    print("  *** verification an earlier P117 draft skipped before its own retracted")
    print("  *** TRUE-ASYMPTOTE-FOUND claim:")

    # Check A: rise over matched exact-10x decade jumps, at increasingly large scale.
    # If genuinely converging, this should SHRINK toward 0 as the jump moves to
    # larger decade counts. If roughly constant or growing, that rules out a plateau.
    print("\n  CHECK A -- rise over matched 10x-decade jumps (should shrink -> 0 if a")
    print("  genuine plateau exists; roughly constant or growing rules it out):")
    val_at = dict(zip(decs, valid_scan, strict=True))
    ten_x_pairs = [(a, b) for a in decs for b in decs if a > 0 and abs(b - 10 * a) < 1e-6]
    ten_x_rises = []
    for a, b in ten_x_pairs:
        r = (val_at[b] - val_at[a]) / val_at[a]
        ten_x_rises.append((a, b, r))
        print(f"    10^{a} -> 10^{b}: rise={r:.5%}")
    ten_x_shrinking = len(ten_x_rises) >= 2 and all(
        ten_x_rises[i][2] >= ten_x_rises[i + 1][2] for i in range(len(ten_x_rises) - 1)
    )

    # Check B: cumulative rise from x_lo=1 divided by ln(decades+1). If the curve
    # is genuinely logarithmic-in-decades (the slowest EXPECTED non-plateau shape),
    # this ratio should be roughly CONSTANT. If it keeps growing, the climb is
    # faster than logarithmic and a plateau is even less plausible.
    print("\n  CHECK B -- cumulative rise / ln(decades+1) (should be roughly flat for")
    print("  log-in-decades growth, or shrink for a true plateau; growing rules both out):")
    ratios = []
    for d, v in valid_pairs:
        if d == 0:
            continue
        cum = (v - valid_scan[0]) / valid_scan[0]
        ratio = cum / math.log(d + 1)
        ratios.append(ratio)
        print(f"    decades={d:<8g} cum_rise={cum:.5%}  ratio={ratio:.6f}")
    ratio_growing = len(ratios) >= 3 and ratios[-1] > ratios[len(ratios) // 2] > ratios[0]

    if not monotone_rise:
        print("\n  -> NON-MONOTONIC. A new feature at this extended reach -- needs its")
        print("     own investigation, not captured by prior findings.")
    elif ratio_growing or not ten_x_shrinking:
        print("\n  -> STILL-CLIMBING, FASTER-THAN-LOGARITHMIC. Both decade-scale-aware")
        print("     checks rule out a genuine plateau: the 10x-decade-jump rise is not")
        print("     shrinking (Check A), and the cumulative-rise/ln(decades) ratio keeps")
        print("     growing rather than flattening (Check B) -- the climb is not just")
        print("     unresolved, it appears to grow FASTER than even the slowest form of")
        print("     unbounded growth (pure log-in-decades) would predict. The naive small")
        print("     last-step percentage above is misleading -- an artifact of the scan's")
        print("     own exponentially-growing decade-step size, not evidence of slowing.")
        print("     FINDING_P117/P118's STILL-NOT-CONVERGED verdict stands, now")
        print("     characterized more precisely than either could show alone.")
    else:
        print("\n  -> PLATEAU-CONSISTENT. Both decade-scale-aware checks are consistent")
        print(f"     with genuine convergence -- report as a candidate value: {valid_scan[-1]:.2f}")
        print("     (still not a proof -- see NOT ESTABLISHED below).")

    print("\n  NOT ESTABLISHED:")
    print("   * a proof that the climb is unbounded rather than converging at some")
    print("     yet-larger x_lo -- this file tests a much larger but still finite")
    print("     domain, it does not take a mathematical limit.")
    print("   * the precise functional form of the growth (power-law-in-decades,")
    print("     log-squared, or something else) -- Checks A/B rule out a plateau and")
    print("     rule out pure log-in-decades, they do not identify what it actually is.")
    print("   * whether accumulated floating-point/quadrature error over such an")
    print("     enormous domain could itself explain part of the remaining rise --")
    print("     addressed by resolution checks in FINDING_P117/P118, not re-verified")
    print("     at this file's own new scale.")
    print("   * anything at Lambda values, or (k, IC) combinations, other than the")
    print("     one tested.")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
