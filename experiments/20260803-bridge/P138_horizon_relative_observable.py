"""P138 -- H2: design an IC-robust observable by anchoring on e-folds
SINCE HORIZON CROSSING (per-k), not on a fixed absolute scale factor.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE. Round-2 strategic arbiter's H2, entered after BOTH cheap
diagnostics failed with no mechanism found: FINDING_P135 refuted "pole at
anchor"; FINDING_P136 refuted "early-transient amplitude sensitivity".
Neither pole nor early-amplitude explains why P79's eps/separation is
IC-sensitive at low k. A THIRD candidate mechanism, not yet tested,
motivates this file's own design (not just another diagnosis): P79's own
anchors (a1, a2) are FIXED scale-factor values, the same for every k. But
different k modes cross the horizon (k = a*H) at different times -- a
low-k mode crosses LATE, so by a FIXED anchor it has had FEWER e-folds
since crossing to relax toward the universal subhorizon growing-mode
attractor than a high-k mode that crossed early. This would explain BOTH
why low k is worse (less relaxation time by a common fixed anchor) AND
why it is smooth, not a pole (FINDING_P135): a slowly-decaying transient
tail superposed on the attractor, not a singularity.

DESIGN: instead of P79's own fixed (a1, a2), anchor on (a_hc(k)*e^N1,
a_hc(k)*e^N2) -- N1, N2 e-folds in ln(a) AFTER horizon crossing for THAT
k, found by solving k = a(t)*H(t) along the actual trajectory being
measured (background quantities only, via P78's own bg_of -- reused, not
rederived). If this is the right axis, the SAME lever-robustness test
P79 ran (G3-style: eps/separation stability under phibar_dot(1) x0.1..x2)
should now PASS at k=1,2,3 -- where the fixed-anchor version failed.

PRE-REGISTERED OUTCOMES (before any number is computed):
  HORIZON-RELATIVE-ROBUST   the separation's lever-spread, measured at
      horizon-relative anchors, is <10% (P79's own G3 threshold) at
      k in {1,2,3} -- the SAME k where the fixed-anchor version failed
      5.2x/4.4x/sign-flip. A genuine candidate replacement observable.
  HORIZON-RELATIVE-REFUTED  spread remains >=10% (or a sign flip) at any
      of k in {1,2,3} -- horizon-crossing timing is not the mechanism
      either; the anchor axis is not the fix.
  PARTIAL  robust at some k, not others.

CONTROLS:
  POSITIVE CONTROL: k=10 (P76's own clean point) must ALSO be robust
      under this new anchoring, at a comparable or better level than its
      own fixed-anchor result -- if the new anchoring breaks a
      previously-clean point, it is not a strict improvement.
  SANITY CHECK: horizon-crossing time t_hc(k) must be found uniquely
      (a*H monotone decreasing in the tested window) for every k tested
      -- if not, this anchoring is ill-posed for that k and is reported
      as such, not silently skipped.
  REUSE: run/contrast/bg_of/mass_law/t_of_a imported from P78's own
  module (via P79's re-export), not reimplemented.

WHAT THIS FILE DOES NOT DO: claim this IS the mechanism (correlation
with the outcome of a robustness gate is not a mechanistic proof -- see
FINDING_P136's own caveat, same discipline applies here). Rerun G1/G2/G5
under this anchoring -- only G3 (lever), the most decisive gate in P79's
own protocol, is retested here. Vary Lambda, G_N, or any external
constant. Quote any k[h/Mpc]. Touch MULTING itself (Gate 1).
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.optimize import brentq

_HERE = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location("p79_ref", os.path.join(_HERE, "P79_low_k_window.py"))
p79 = importlib.util.module_from_spec(_sp)
sys.modules["p79_ref"] = p79
_sp.loader.exec_module(p79)

run, contrast, t_of_a = p79.run, p79.contrast, p79.t_of_a
PHIDOT, LAM, GH = p79.PHIDOT, p79.LAM, p79.GH
p78 = sys.modules["p78_ref"]
bg_of, mass_law, T_END = p78.bg_of, p78.mass_law, p78.T_END

KS = (1.0, 2.0, 3.0, 10.0)
LEVERS = (0.1, 0.5, 1.0, 2.0)
N1, N2 = 2.0, 15.0  # e-folds after horizon crossing for the two anchors


def aH_of(sol, name, gh, lam, tv):
    a_, pb, pd = sol.sol(tv)[:3]
    M, Mp, _ = mass_law(name, gh)
    b = bg_of(a_, pb, pd, gh, lam, M, Mp)
    return a_ * b["H"], a_


def t_hc(sol, name, gh, lam, kk):
    """Time at which k = a*H (horizon crossing), by root-finding on aH(t)-k."""

    def f(tv):
        aH, _ = aH_of(sol, name, gh, lam, tv)
        return aH - kk

    f1, f2 = f(1.0), f(T_END)
    if f1 * f2 > 0:
        return None  # no crossing in [1, T_END] -- reported, not hidden
    return brentq(f, 1.0, T_END, xtol=1e-8, rtol=1e-12)


def eps_horizon_relative(name, gh, kk, rtol=1e-10, **ic):
    """eps computed at anchors N1/N2 e-folds after horizon crossing, not
    at a fixed absolute scale factor. Returns None if either the k=gh run
    or the k=0 reference run has no horizon crossing in range.
    """
    out = []
    for g in (gh, 0.0):
        s = run(name, g, LAM, kk, rtol=rtol, **ic) if ic else run(name, g, LAM, kk, rtol=rtol)
        thc = t_hc(s, name, g, LAM, kk)
        if thc is None:
            return None
        _, a_hc = aH_of(s, name, g, LAM, thc)
        a1_target, a2_target = a_hc * np.exp(N1), a_hc * np.exp(N2)
        t1, t2 = t_of_a(s, a1_target), t_of_a(s, a2_target)
        if t1 is None or t2 is None:
            return None
        c2, c1 = contrast(s, name, g, LAM, t2), contrast(s, name, g, LAM, t1)
        out.append((c2 / c1, a1_target, a2_target))
    (g1, a1a, a2a), (g0, a1b, a2b) = out
    # the two branches' own a1/a2 need not coincide (different g -> slightly
    # different background -> slightly different horizon-crossing a); use
    # each branch's OWN (a1,a2) for its own ln(a2/a1) normalisation, exactly
    # as P78/P79's eps_of does per-branch (see FINDING_P76 "why the reference
    # is per-completion").
    return np.log(g1) / np.log(a2a / a1a) - np.log(g0) / np.log(a2b / a1b)


def sep_hr(kk, rtol=1e-10, **ic):
    a = eps_horizon_relative("exponential", GH, kk, rtol=rtol, **ic)
    b = eps_horizon_relative("linear", GH, kk, rtol=rtol, **ic)
    return None if (a is None or b is None) else a - b


def main() -> int:
    print("=" * 78)
    print("P138 -- H2: horizon-crossing-relative anchoring, an IC-robustness test")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ------------------------------------------------------------ sanity
    print("\n" + "-" * 78)
    print("SANITY CHECK -- does k=aH have a unique root in [1, T_END] for every k?")
    print("-" * 78)
    print(f"\n    {'k':<8}{'t_hc':<18}{'a_hc'}")
    ok_all = True
    for kk in KS:
        s = run("linear", GH, LAM, kk)
        thc = t_hc(s, "linear", GH, LAM, kk)
        if thc is None:
            print(f"    {kk:<8}{'NO CROSSING IN RANGE':<18}")
            ok_all = False
            continue
        _, a_hc = aH_of(s, "linear", GH, LAM, thc)
        print(f"    {kk:<8}{thc:<18.6e}{a_hc:.6e}")
    if not ok_all:
        print("\n  *** at least one k has no horizon crossing in [1, T_END] --")
        print("      this anchoring scheme is ill-posed there. STOP for that k.")

    # -------------------------------------------------------------- gate
    print("\n" + "-" * 78)
    print(f"G3-STYLE LEVER TEST -- horizon-relative anchors (N1={N1}, N2={N2} e-folds),")
    print("phibar_dot(1) x0.1..x2, threshold <10% (matching P79's own G3)")
    print("-" * 78)
    print(f"\n    {'lever':<10}" + "".join(f"{'k=' + str(k):<20}" for k in KS))
    rows = {}
    for f in LEVERS:
        vals = []
        for kk in KS:
            v = sep_hr(kk, phidot0=f * PHIDOT)
            vals.append(v)
        rows[f] = vals
        printable = [f"{v:<20.6e}" if v is not None else f"{'N/A':<20}" for v in vals]
        print(f"    x{f:<9.1f}" + "".join(printable))

    print(f"\n    {'k':<8}{'min':<18}{'max':<18}{'spread':<12}{'G3 verdict'}")
    results = {}
    for i, kk in enumerate(KS):
        vs = [rows[f][i] for f in LEVERS if rows[f][i] is not None]
        if len(vs) < len(LEVERS):
            print(f"    {kk:<8}{'incomplete data (some anchors unreachable)':<40}")
            results[kk] = "INCOMPLETE"
            continue
        if all(v > 0 for v in vs) or all(v < 0 for v in vs):
            sp_ = max(vs) / min(vs)
            verdict = "PASS" if sp_ < 1.10 else "FAIL"
            results[kk] = verdict
            print(f"    {kk:<8}{min(vs):<18.6e}{max(vs):<18.6e}{sp_:<12.4f}{verdict}")
        else:
            results[kk] = "FAIL (sign flip)"
            print(f"    {kk:<8}{'sign flip across lever sweep':<40}FAIL")

    # ------------------------------------------------------------ verdict
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    control_ok = results.get(10.0) == "PASS"
    print(f"\n  POSITIVE CONTROL (k=10): {results.get(10.0)}")
    if not control_ok:
        print("  *** control does not pass under the new anchoring either --")
        print("      this scheme is not a strict improvement. Treat all results")
        print("      below with that caveat.")

    unstable = {kk: results[kk] for kk in (1.0, 2.0, 3.0)}
    n_pass = sum(1 for v in unstable.values() if v == "PASS")
    if n_pass == 3:
        print("\n  -> HORIZON-RELATIVE-ROBUST. All three previously-failing k values")
        print("     (1, 2, 3) now pass the SAME <10% lever-robustness threshold P79")
        print("     used, under horizon-crossing-relative anchoring. A genuine")
        print("     candidate replacement observable -- not yet a mechanism proof.")
    elif n_pass > 0:
        print(f"\n  -> PARTIAL. {n_pass}/3 previously-failing k values now pass.")
        print(f"     Detail: {unstable}")
    else:
        print("\n  -> HORIZON-RELATIVE-REFUTED. Horizon-crossing timing is not the")
        print("     fix either -- all three previously-failing k values still fail")
        print("     under this anchoring.")

    print("\n  NOT ESTABLISHED regardless of outcome:")
    print("   * a mechanistic proof, even if PASS -- correlation with a gate")
    print("     passing is not a causal demonstration.")
    print("   * G1/G2/G5 under this anchoring -- not rerun here.")
    print("   * anything observational -- internal units, NO_BRIDGE_FITTING in force")
    print("   * anything about MULTING itself (Gate 1): both completions are OURS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
