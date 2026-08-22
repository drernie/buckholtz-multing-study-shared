"""P87 -- is eta^0.299 a power law at all, and what sets the amplitude?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

THE OPEN GAP, AND WHY THE THIRD ATTEMPT STARTS SOMEWHERE ELSE.

FINDING_P80 measured D := d eps/d g_pert at g_bg = 0, k = 10, against
eta = phibar_dot(1)/phibar_dot_ref, and found it ODD in eta to 1.1 percent,
exactly zero at eta = 0 -- and NOT linear: D/eta spreads 4.32x and a log-log fit
gives D ~ eta^0.299. Two explanations were built and both failed:

  (1) "D is linear in phibar_dot at the measurement epoch" -- an INVALID test,
      not a negative result: it sampled an oscillating field at one instant, and
      the four samples alternated in sign.
  (2) the same claim with a matched RMS envelope -- exponents 0.390 and 0.257.

Both attempts hunted for the MEANING of 0.299. This one asks a cheaper and more
destructive question first:

    IS 0.299 THE EXPONENT OF A POWER LAW AT ALL?

FINDING_P80 reported the exponent and the spread but NOT the fit residual. If the
residual is large, "eta^0.299" is a summary statistic of a curve that is not a
power law, and looking for its physical meaning is looking for a ghost. P83 hit
exactly this: its g_crit ~ eta^-0.048 carried log-residuals of 0.039, and the
finding had to say "approximate trend, not an established power law". The same
check was never run on 0.299.

WHAT IS NEW SINCE P80, and it supplies a real prediction rather than a fit.
D is measured at g_bg = 0, so the background scalar has NO source term: it is a
FREE field in V = lam*phibar^4/4 with initial velocity eta*PHIDOT and phibar(1)=0.
Ignoring Hubble damping over the first quarter-period, energy conservation gives

    phibar_dot0^2 / 2  =  lam * phibar_peak^4 / 4     =>   phibar_peak ~ eta^(1/2)

and the diamond scan already established that the first oscillation peak is the
epoch that matters (min(1-g*phibar) sits exactly there). So phibar_peak is a
quantity with independent standing, not one invented to fit D.

PRE-REGISTERED OUTCOMES:
  E-NOTALAW    the log-log residual over the measured range is large (>= 0.02,
               the scale at which P83 already refused to call its own fit a power
               law) -> 0.299 is a summary of a non-power-law curve, the gap
               dissolves, and the correct action is to stop explaining it.
  E-LAW-K      the residual is small AND the exponent is stable across k -> it is
               a real power law of the model, and the remaining question is what
               sets it.
  E-LAW-LOCAL  the residual is small but the exponent MOVES with k -> it is a
               local slope of a k-dependent family, which is a weaker object than
               "the exponent" and must be quoted with its k.

Separately and independently: phibar_peak ~ eta^(1/2) either holds or it does
not, and that is reported whatever happens to D.

WHAT THIS CANNOT DO: it cannot explain 0.299 if it turns out to be real. It can
only establish whether there is something there to explain.
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, fn):
    sp = importlib.util.spec_from_file_location(name, os.path.join(_HERE, fn))
    m = importlib.util.module_from_spec(sp)
    sys.modules[name] = m
    sp.loader.exec_module(m)
    return m


p80 = _load("p80_ref", "P80_onshell_attribution.py")

LAM = 1.0
T_END = p80.T_END
PHIDOT = p80.PHIDOT
RESID_THRESHOLD = 0.02  # the scale at which P83 refused to call its fit a power law


def fit_power(x, y):
    """Return (exponent, max |log residual|, r_squared_on_logs)."""
    lx, ly = np.log(np.asarray(x, float)), np.log(np.asarray(y, float))
    p = np.polyfit(lx, ly, 1)
    pred = np.polyval(p, lx)
    resid = ly - pred
    ss_res = float(np.sum(resid**2))
    ss_tot = float(np.sum((ly - ly.mean()) ** 2))
    return float(p[0]), float(np.max(np.abs(resid))), 1.0 - ss_res / ss_tot


def D_of(eta, kk, h=1e-3):
    """P80's derivative, via P80's own eps_of so the quantity is identical."""
    pd0 = eta * PHIDOT
    a = p80.eps_of(0.0, h, LAM, kk, A1, A2, phidot0=pd0)
    b = p80.eps_of(0.0, -h, LAM, kk, A1, A2, phidot0=pd0)
    if a is None or b is None:
        return None
    return (a - b) / (2 * h)


def first_peak(eta, lam=LAM):
    """Amplitude of phibar at its FIRST turning point, at g_bg = 0.

    Returns None if no turning point exists on the span -- which is what must
    happen at lam = 0, where diamond D1 established phibar grows monotonically.
    That is control C1: a peak-finder that always finds a peak is not a
    measurement.
    """

    def rhs(_t, y):
        a_, pb, pd = y
        rho_A = p80.C_MATTER / a_**3
        arg = (8.0 * np.pi * p80.G_N / 3.0) * (rho_A + pd**2 / 2.0 + lam * pb**4 / 4.0)
        H = np.sqrt(arg) if arg > 0 else 0.0
        return [a_ * H, pd, -3.0 * H * pd - lam * pb**3]

    with np.errstate(all="ignore"):
        s = solve_ivp(
            rhs,
            (1.0, T_END),
            [p80.A3_INIT ** (1.0 / 3.0), 0.0, eta * PHIDOT],
            rtol=1e-11,
            atol=1e-22,
            dense_output=True,
        )
        if not s.success:
            return None
        tt = np.exp(np.linspace(0.0, np.log(T_END), 40000))
        pb, pd = s.sol(tt)[1], s.sol(tt)[2]
    if not np.all(np.isfinite(pb)):
        return None
    sign_change = np.where(np.diff(np.sign(pd)) != 0)[0]
    if len(sign_change) == 0:
        return None
    i = sign_change[0]
    return float(abs(pb[i])), float(tt[i])


s_ref = p80.run(0.0, 0.0, LAM, 1.0)
A1, A2 = s_ref.sol(1e4)[0], s_ref.sol(8e7)[0]


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P87 -- is eta^0.299 a power law at all?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- CONTROLS")
    print("-" * 78)

    print("\n  C1 -- the fitter must recover a KNOWN exponent. Fed y = x^0.5 it")
    print("  must return 0.5 with a residual at round-off, or every exponent")
    print("  below is uninterpretable.")
    xs = np.array([0.25, 0.5, 1.0, 2.0, 4.0])
    n_s, r_s, r2_s = fit_power(xs, xs**0.5)
    print(f"    synthetic x^0.5 -> exponent {n_s:.6f}, max log-resid {r_s:.3e}, R2 {r2_s:.9f}")
    C1 = abs(n_s - 0.5) < 1e-9 and r_s < 1e-9
    print(f"    C1 {'PASSES' if C1 else 'FAILS'}")
    if not C1:
        print("    *** the fitter is broken; nothing below can be read.")
        return 1

    print("\n  C2 -- and it must NOT report a clean power law for something that")
    print("  is not one. Fed y = 1 + log(x), a deliberately non-power curve, the")
    print("  residual must be visibly large.")
    ys = 1.0 + np.log(xs) * 0.3
    n_b, r_b, r2_b = fit_power(xs, ys)
    print(f"    synthetic 1+0.3ln(x) -> exponent {n_b:.6f}, max log-resid {r_b:.3e}")
    C2 = r_b > 1e-3
    print(f"    C2 {'PASSES' if C2 else 'FAILS'} -- the residual discriminates.")
    if not C2:
        print("    *** the residual cannot tell a power law from a non-power law.")
        return 1

    print("\n  C3 -- the peak-finder must FAIL where diamond D1 says there is no")
    print("  peak: at lam = 0 the potential has no restoring force and phibar")
    print("  grows monotonically. A finder that always finds a peak is not a")
    print("  measurement.")
    pk0 = first_peak(1.0, lam=0.0)
    print(f"    first_peak at lam = 0 : {pk0}")
    C3 = pk0 is None
    print(f"    C3 {'PASSES' if C3 else 'FAILS'} -- no peak reported where none exists.")
    if not C3:
        print("    *** the peak-finder invents peaks.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- is D(eta) a power law? The question P80 never asked.")
    print("-" * 78)
    print("  P80 reported the exponent and the spread but NOT the fit residual.")
    print("  P83 refused to call its own eta-fit a power law at a residual of")
    print("  0.039; the same standard is applied here.")
    etas = [0.25, 0.5, 1.0, 2.0]
    print(f"\n    {'k':<7}{'exponent':<14}{'max log-resid':<18}{'R2':<14}{'power law?'}")
    per_k = {}
    for kk in (3.0, 10.0, 30.0):
        ds = [D_of(e, kk) for e in etas]
        if any(d is None or d <= 0 for d in ds):
            print(f"    {kk:<7g}{'unresolved or non-positive -- not fittable':<46}")
            continue
        n, r, r2 = fit_power(etas, ds)
        per_k[kk] = (n, r, r2)
        print(
            f"    {kk:<7g}{n:<14.6f}{r:<18.4f}{r2:<14.6f}{'yes' if r < RESID_THRESHOLD else 'NO'}"
        )

    print(f"\n    threshold for calling it a power law: max log-resid < {RESID_THRESHOLD}")
    if per_k:
        worst = max(r for _, r, _ in per_k.values())
        exps = [n for n, _, _ in per_k.values()]
        print(f"    worst residual across k : {worst:.4f}")
        print("    exponents across k      : " + ", ".join(f"{e:.4f}" for e in exps))
        print(f"    exponent spread         : {max(exps) - min(exps):.4f}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- what DOES set the amplitude? The free-field prediction.")
    print("-" * 78)
    print("  At g_bg = 0 the background scalar has no source: it is a FREE field")
    print("  in V = lam*phibar^4/4 starting from phibar(1)=0 with velocity")
    print("  eta*PHIDOT. Ignoring Hubble damping over the first quarter-period,")
    print("  energy conservation gives phibar_peak ~ eta^(1/2). The diamond scan")
    print("  already established the FIRST PEAK is the epoch that matters, so")
    print("  this is a quantity with independent standing, not one invented to")
    print("  fit D.")
    print(f"\n    {'eta':<9}{'phibar_peak':<18}{'t of peak':<16}{'peak/eta^0.5'}")
    pk, pk_eta = [], []
    for e in (0.25, 0.5, 1.0, 2.0, 4.0):
        r = first_peak(e)
        if r is None:
            print(f"    {e:<9.2f}{'no peak found':<34}")
            continue
        amp, tpk = r
        pk.append(amp)
        pk_eta.append(e)
        print(f"    {e:<9.2f}{amp:<18.6e}{tpk:<16.4g}{amp / e**0.5:.6e}")
    if len(pk) >= 3:
        n_pk, r_pk, r2_pk = fit_power(pk_eta, pk)
        print(f"\n    fit: phibar_peak ~ eta^{n_pk:.6f}   max log-resid {r_pk:.4f}")
        print("    free-field prediction  : eta^0.500000")
        print(f"    difference             : {abs(n_pk - 0.5):.4f}")
        print("\n    READ: agreement means the IC-to-amplitude map is the free-field")
        print("    energy balance, MEASURED rather than assumed. Disagreement means")
        print("    Hubble damping over the first quarter-period is not negligible,")
        print("    which is itself worth knowing and is not a failure of the test.")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if not per_k:
        print("  -> NOT MEASURABLE. D could not be fitted at any k. Infrastructure")
        print("     outcome, not evidence about the exponent.")
    else:
        worst = max(r for _, r, _ in per_k.values())
        exps = [n for n, _, _ in per_k.values()]
        spread = max(exps) - min(exps)
        if worst >= RESID_THRESHOLD:
            print(f"  -> E-NOTALAW. Worst log-residual {worst:.4f} >= {RESID_THRESHOLD}.")
            print("     'eta^0.299' is a SUMMARY STATISTIC of a curve that is not a")
            print("     power law, so there is no exponent to explain and the two")
            print("     failed explanations were failing to explain a ghost.")
            print("     CORRECT ACTION: stop hunting the exponent. What survives")
            print("     from P80 is the part that WAS established -- D is odd in")
            print("     eta to 1.1 percent and exactly zero at eta = 0 -- and the")
            print("     honest statement of the rest is 'D grows sublinearly with")
            print("     eta', with no exponent quoted.")
        elif spread < 0.05:
            print(f"  -> E-LAW-K. Residual {worst:.4f} < {RESID_THRESHOLD} and the")
            print(f"     exponent is stable across k (spread {spread:.4f}). It is a")
            print("     real power law of the model and the open question becomes")
            print("     what sets its value.")
        else:
            print(f"  -> E-LAW-LOCAL. Residual {worst:.4f} is small but the exponent")
            print(f"     moves with k (spread {spread:.4f}). It is a LOCAL SLOPE of a")
            print("     k-dependent family, a weaker object than 'the exponent', and")
            print("     must always be quoted with its k.")

    print("\n  NOT ESTABLISHED:")
    print("   * WHY the exponent has whatever value it has, if it is real. This")
    print("     step can only say whether there is something there to explain.")
    print("   * anything outside eta in 0.25..4 and k in 3..30.")
    print("   * anything observational. NO_BRIDGE_FITTING untouched.")
    print("   * anything about MULTING itself (Gate 1).")
    print("   * Perelman condition 5 -- still not met.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
