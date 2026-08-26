"""P141 -- decisive test for docs/148's mode-projection hypothesis:
does the subdominant-mode decay rate (measured as eps's own convergence
rate to its late-time asymptote) vary monotonically with k?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE. docs/148 (user-directed inverse-problem synthesis for
bottleneck 4) collected the 5 constraints already established by P135/
P136/P138/P139 into one table and derived the sole candidate mechanism
class that satisfies all of them: mode-projection/two-branch. The IC
lever sets the projection weight onto a fast-decaying ("transient") vs
slow-decaying ("attractor") mode; scale-dependence (why the effect
vanishes at high k) emerges IF the decay-rate SEPARATION between the two
modes itself depends on k -- faster separation at high k washes out the
IC-dependent transient before the late-time anchor is ever reached;
slower separation at low k lets it persist. This is the genuinely new
prediction docs/148 named, not used in constructing the hypothesis
itself.

THE MEASUREMENT, reusing FINDING_P76's own machinery rather than
inventing a new fitting procedure. eps(k) := d ln G / d ln a is already
measured, in FINDING_P76's own table, at a SEQUENCE of increasingly late
windows (@1e5, @1e6, @1e7, @8e7) -- how fast that sequence CONVERGES to
its own asymptotic value IS the subdominant mode's own relative decay
rate. Model: eps(N) = eps_inf + C * N^(-q), N := ln(a2/a1) e-folds from a
fixed early reference a1, fit q (the convergence exponent) from the late
points where power-law convergence should dominate. Large q = fast
convergence = subdominant mode already negligible = IC-independence by
the anchor (matches the k=10/30 "clean" behavior FINDING_P76 itself
found). Small q = slow convergence = subdominant mode still contributing
at the anchor = IC-sensitivity survives (matches the k=1/2/3 instability
FINDING_P79/P135/P136/P138 all found).

PRE-REGISTERED OUTCOMES (before any number is computed):
  MODE-PROJECTION-CONFIRMED   the fitted convergence exponent q(k)
      increases monotonically (or near-monotonically, allowing small
      numerical noise) with k across k in {1,2,3,10} -- faster
      convergence at high k, exactly the pattern needed to explain why
      IC-sensitivity washes out there but persists at low k.
  MODE-PROJECTION-REFUTED     q(k) does not vary monotonically with k --
      the convergence-rate story does not track the already-established
      k-dependence of IC-sensitivity (P79's own G1/G3 pattern).
  PARTIAL   q(k) trends the right direction for some k pairs but not
      others, or the fit itself is unreliable (poor residuals) at some k.

CONTROLS:
  POSITIVE CONTROL: the fit method itself, applied to a KNOWN power-law
      convergence (a synthetic eps(N) = 0.05 + 2.0*N**(-1.5), noise-free)
      must recover q=1.5 to within a small tolerance -- validates the
      fitting machinery before trusting it on the real (noisier)
      trajectories.
  CROSS-CHECK: q(k) is fitted TWICE per k -- once using all 4 window
      points (@1e5..@8e7), once using only the 3 latest (@1e6..@8e7) --
      if the two fits disagree substantially, the "power-law regime" has
      not been reached yet and q(k) is not trustworthy at that k,
      reported as such rather than silently averaged.
  REUSE: eps() imported directly from P79's own module (itself importing
      P78's) -- the SAME function used throughout this campaign's own
      eps(k) measurements, not a new implementation.

WHAT THIS FILE DOES NOT DO: test IC-lever-dependence of q(k) itself
(a secondary, bonus check named in docs/148 but not required for the
primary GO/STOP decision) -- only the canonical lever=x1 is used here,
matching P76's own original measurement. Build a full two-exponential
decomposition of contrast(t) directly (a harder, more error-prone fit);
the convergence-rate proxy is used instead, deliberately, because it
reuses already-verified machinery. Vary Lambda, G_N, or C_MATTER. Quote
any k[h/Mpc]. Touch MULTING itself (Gate 1).
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.optimize import curve_fit

_HERE = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location("p79_ref", os.path.join(_HERE, "P79_low_k_window.py"))
p79 = importlib.util.module_from_spec(_sp)
sys.modules["p79_ref"] = p79
_sp.loader.exec_module(p79)

run, eps, LAM, GH = p79.run, p79.eps, p79.LAM, p79.GH

KS = (1.0, 2.0, 3.0, 10.0)
A2_TIMES = (1e5, 1e6, 1e7, 8e7)


def power_law_convergence(n, eps_inf, c, q):
    return eps_inf + c * n ** (-q)


def fit_q(ns, epsilons):
    """Fit eps(N) = eps_inf + C*N^(-q). Returns (eps_inf, c, q, residual)."""
    n_arr, e_arr = np.array(ns), np.array(epsilons)
    p0 = [e_arr[-1], (e_arr[0] - e_arr[-1]) * n_arr[0], 1.0]
    try:
        popt, _ = curve_fit(power_law_convergence, n_arr, e_arr, p0=p0, maxfev=20000)
        resid = np.sqrt(np.mean((power_law_convergence(n_arr, *popt) - e_arr) ** 2))
        return popt[0], popt[1], popt[2], resid
    except RuntimeError:
        return None, None, None, None


def main() -> int:
    print("=" * 78)
    print("P141 -- mode-projection decisive test: does eps's own convergence")
    print("rate q(k) increase monotonically with k?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ------------------------------------------------------------ control
    print("\n" + "-" * 78)
    print("POSITIVE CONTROL -- recover a KNOWN synthetic q from noise-free data")
    print("-" * 78)
    synth_n = np.array([5.0, 10.0, 15.0, 20.0])
    synth_eps = 0.05 + 2.0 * synth_n ** (-1.5)
    e_inf, c, q_fit, resid = fit_q(synth_n, synth_eps)
    control_ok = q_fit is not None and abs(q_fit - 1.5) < 0.01
    print(f"    true q=1.5, fitted q={q_fit}, residual={resid}")
    print(f"    control {'PASSES' if control_ok else 'FAILS'}")
    if not control_ok:
        print("\n  *** the fitting machinery itself is not trustworthy. STOP.")
        return 1

    # -------------------------------------------------------------- main
    print("\n" + "-" * 78)
    print("MAIN MEASUREMENT -- eps(k) at 4 increasingly late windows, lever=x1")
    print("-" * 78)
    s_ref = run("linear", 0.0, LAM, 1.0)
    a1 = s_ref.sol(1e4)[0]

    results = {}
    for kk in KS:
        print(f"\n  k = {kk}")
        s = run("linear", GH, LAM, kk)
        ns, epsilons = [], []
        for t2 in A2_TIMES:
            a2 = s.sol(t2)[0]
            n = np.log(a2 / a1)
            e = eps("linear", GH, kk, a1, a2)
            ns.append(n)
            epsilons.append(e)
            print(f"    t2={t2:<10.0e}  N={n:<10.4f}  eps={e:.6f}")

        e_inf_full, c_full, q_full, resid_full = fit_q(ns, epsilons)
        e_inf_late, c_late, q_late, resid_late = fit_q(ns[1:], epsilons[1:])
        print(f"    fit (all 4 points):    eps_inf={e_inf_full}, q={q_full}, resid={resid_full}")
        print(f"    fit (latest 3 points): eps_inf={e_inf_late}, q={q_late}, resid={resid_late}")
        agree = (
            q_full is not None
            and q_late is not None
            and abs(q_full - q_late) < 0.5 * max(abs(q_full), abs(q_late), 1e-6)
        )
        print(f"    fits agree (power-law regime reached): {agree}")
        results[kk] = {"q_full": q_full, "q_late": q_late, "agree": agree}

    # ------------------------------------------------------------ verdict
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    print(f"\n    {'k':<8}{'q (full fit)':<16}{'q (late fit)':<16}{'trustworthy?'}")
    q_series = []
    for kk in KS:
        r = results[kk]
        q_full_s = f"{r['q_full']:.4f}" if r["q_full"] is not None else "FIT-FAILED"
        q_late_s = f"{r['q_late']:.4f}" if r["q_late"] is not None else "FIT-FAILED"
        print(f"    {kk:<8}{q_full_s:<16}{q_late_s:<16}{r['agree']}")
        if r["agree"]:
            q_series.append((kk, r["q_late"]))

    if len(q_series) < 3:
        print("\n  -> INCONCLUSIVE. Fewer than 3 of the 4 k values gave a")
        print("     trustworthy convergence-rate fit -- not enough trustworthy")
        print("     points to assess monotonicity honestly.")
    else:
        qs_sorted_by_k = [q for _, q in sorted(q_series, key=lambda x: x[0])]
        monotone = all(
            qs_sorted_by_k[i] <= qs_sorted_by_k[i + 1] + 1e-9
            for i in range(len(qs_sorted_by_k) - 1)
        )
        print(
            f"\n    trustworthy (k, q) pairs, sorted by k: {sorted(q_series, key=lambda x: x[0])}"
        )
        if monotone:
            print("\n  -> MODE-PROJECTION-CONFIRMED. The convergence exponent q(k)")
            print("     increases monotonically across the trustworthy k values --")
            print("     eps converges FASTER to its asymptote at high k (subdominant")
            print("     mode negligible by the anchor) and SLOWER at low k (still")
            print("     contributing), matching the already-established pattern of")
            print("     where IC-sensitivity persists vs. washes out.")
        else:
            print("\n  -> MODE-PROJECTION-REFUTED. q(k) does not increase monotonically")
            print("     across the trustworthy k values -- the convergence-rate story")
            print("     does not track the already-established IC-sensitivity pattern.")

    print("\n  NOT ESTABLISHED regardless of outcome:")
    print("   * IC-lever-dependence of q(k) itself -- only lever=x1 tested here,")
    print("     a secondary check docs/148 named but did not require for GO/STOP.")
    print("   * a full two-exponential decomposition of contrast(t) directly --")
    print("     the convergence-rate proxy is used instead, deliberately.")
    print("   * anything observational -- internal units, NO_BRIDGE_FITTING in force")
    print("   * anything about MULTING itself (Gate 1): both completions are OURS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
