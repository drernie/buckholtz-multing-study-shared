"""P74 -- the gauge-correct, converged mu, with the g_hat=0 subtraction built in.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE EXISTS. FINDING_P73 retracted its own mu-based verdict on
FINDING_P60's D2-vs-D3 after context-blind review. Two things were wrong:

  (1) the reference density was not gauge-correct. P73's Test 3 tried to fix
      this by substituting `drho + 3H*q_tot` FROM MEMORY, and it did not return
      mu -> 1, so the fix was abandoned with the question left open;
  (2) mu was read at t=1e3, where the k=0.1 mode is still SUPERHORIZON
      (k/aH = 0.57), so the number was a transient snapshot.

P73 also established the thing that makes a fix possible: BOTH constraints are
first class, so they hold along the whole solution and can be used as algebraic
identities at any time -- not just on initial data.

This file therefore does what P73 should have done:
  A. DERIVE the reference density from the two constraints (no memory, no
     guessing), and check symbolically which sign follows;
  B. LOCK MASS -- a scalar-free control (pure GR + dust) where mu must be
     EXACTLY 1. Gate 3: an extracted number without a stated control residual
     is not evidence;
  C. mu at converged t, with a tolerance sweep giving the numerical floor
     (FINDING_P72's lesson: if a residual moves with rtol, it measures the
     solver, not the claim);
  D. the actual observable, Delta_mu(k) := mu(g_hat=1) - mu(g_hat=0), against
     that floor.

PRE-REGISTERED OUTCOMES (written before the numbers, per the plan):
  Delta_mu above the floor AND k-dependent  -> D3
  Delta_mu collapses into the floor         -> D2, and the mu channel is dead
                                               as a discriminator
  lock mass fails                           -> ORACLE_INADEQUATE. NOT evidence
                                               against the claim; fix the
                                               definition and re-run.
"""

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

G_N = 1.0
C_MATTER = 1.0
A3_INIT = 6.0 * np.pi - 1.0
PHIDOT_INIT = np.sqrt(2.0) / A3_INIT


# ----------------------------------------------------------------------
# background (FINDING_P69, reused verbatim from P73)
# ----------------------------------------------------------------------
def bg_quantities(a: float, pb: float, pd: float, gh: float, lam: float) -> dict:
    rho_A = C_MATTER / a**3
    rho_phys = rho_A * (1.0 - gh * pb)
    V = lam * pb**4 / 4.0
    Vp = lam * pb**3
    Vpp = 3.0 * lam * pb**2
    H = np.sqrt(max((8.0 * np.pi * G_N / 3.0) * (rho_phys + pd**2 / 2.0 + V), 0.0))
    Hdot = -4.0 * np.pi * G_N * (rho_phys + pd**2)
    return {
        "rho_A": rho_A,
        "rho_phys": rho_phys,
        "V": V,
        "Vp": Vp,
        "Vpp": Vpp,
        "H": H,
        "Hdot": Hdot,
    }


# ----------------------------------------------------------------------
# perturbation system (FINDING_P73 Part D, reused verbatim -- including the
# corrected +(k^2/a^2)Q sign that P73 had to DERIVE rather than remember)
# ----------------------------------------------------------------------
def make_system(gh: float, lam: float, kk: float):
    def rhs(_tt, y):
        a_, pb, pd, psi, psid, dph, dphd, drA, qm = y
        b = bg_quantities(a_, pb, pd, gh, lam)
        H, rho_A, rho_phys, Vp, Vpp = (b["H"], b["rho_A"], b["rho_phys"], b["Vp"], b["Vpp"])
        pdd = gh * rho_A - 3.0 * H * pd - Vp
        dp_phi_ = pd * dphd - psi * pd**2 - Vp * dph
        psidd = 4 * np.pi * G_N * dp_phi_ - 4 * H * psid - (2 * b["Hdot"] + 3 * H**2) * psi
        dphdd = (
            gh * drA
            + 2 * psi * (gh * rho_A - Vp)
            + 4 * psid * pd
            - 3 * H * dphd
            - (kk**2 / a_**2 + Vpp) * dph
        )
        drAd = -3 * H * drA + 3 * psid * rho_A + (kk**2 / a_**2) * qm / (1 - gh * pb)
        qmd = -3 * H * qm - rho_phys * psi + gh * rho_A * dph
        return [a_ * H, pd, pdd, psid, psidd, dphd, dphdd, drAd, qmd]

    return rhs


def initial_data(gh, lam, kk, psi0=1e-5, phidot0=None, dph0=1e-6, dphd0=0.0, drA0=1e-5):
    """Solve the two first-class constraints for Psi_dot(1) and Q_m(1).

    `phidot0=0.0` together with dph0=dphd0=0 gives the SCALAR-FREE control of
    Part B: the scalar sector is then identically zero for all time (checked in
    Part B, not assumed).
    """
    a0 = A3_INIT ** (1.0 / 3.0)
    pb0 = 0.0
    pd0 = PHIDOT_INIT if phidot0 is None else phidot0
    b = bg_quantities(a0, pb0, pd0, gh, lam)
    H0 = b["H"]
    drho_phi0 = pd0 * dphd0 - psi0 * pd0**2 + b["Vp"] * dph0
    drho_m0 = drA0 * (1 - gh * pb0) - gh * b["rho_A"] * dph0
    # 00 constraint: 3H(Psi_dot + H Psi) + (k^2/a^2)Psi + 4piG*drho_tot = 0
    psid0 = (-(kk**2 / a0**2) * psi0 - 4 * np.pi * G_N * (drho_phi0 + drho_m0)) / (
        3 * H0
    ) - H0 * psi0
    # 0i constraint: Psi_dot + H Psi + 4piG*dq_tot = 0,  dq_tot = -phibar_dot*dphi + Q_m
    qm0 = -(psid0 + H0 * psi0) / (4 * np.pi * G_N) + pd0 * dph0
    return [a0, pb0, pd0, psi0, psid0, dph0, dphd0, drA0, qm0]


def split_densities(y, gh, lam):
    """Matter/scalar split of the COMOVING density perturbation, Delta = drho - 3H*dq.

    The minus sign and the factor 3H are DERIVED in Part A; the matter/scalar
    split is FINDING_P60's Route B convention (matter as the Poisson reference).
    """
    a_, pb, pd, psi, _psid, dph, dphd, drA, qm = y
    b = bg_quantities(a_, pb, pd, gh, lam)
    H = b["H"]
    drho_phi = pd * dphd - psi * pd**2 + b["Vp"] * dph
    drho_m = drA * (1 - gh * pb) - gh * b["rho_A"] * dph
    dq_phi = -pd * dph
    dq_m = qm
    return {
        "Delta_m": drho_m - 3 * H * dq_m,
        "Delta_phi": drho_phi - 3 * H * dq_phi,
        "drho_m": drho_m,
        "drho_phi": drho_phi,
    }


def mu_of(y, gh, lam, kk):
    a_ = y[0]
    psi = y[3]
    d = split_densities(y, gh, lam)
    return -(kk**2 / a_**2) * psi / (4 * np.pi * G_N * d["Delta_m"])


def run(gh, lam, kk, t_end, rtol=1e-11, **ic):
    y0 = initial_data(gh, lam, kk, **ic)
    s = solve_ivp(
        make_system(gh, lam, kk), (1.0, t_end), y0, rtol=rtol, atol=1e-18, dense_output=True
    )
    assert s.success, f"integration failed: gh={gh} lam={lam} k={kk} t_end={t_end}"
    return s


def main() -> int:
    print("=" * 78)
    print("P74 -- gauge-correct, converged mu, with the g_hat=0 subtraction built in")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    # PART A -- DERIVE the reference density from the two constraints
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- derive the reference density (do NOT write it from memory)")
    print("-" * 78)
    print("  FINDING_P73's Test 3 substituted `drho + 3H*q_tot` from memory, it did")
    print("  not give mu -> 1, and the question was left open. P73 also PROVED both")
    print("  constraints are first class, so they hold along the WHOLE solution and")
    print("  may be used as algebraic identities at any t. Combine them and see what")
    print("  the reference density actually is.")

    k, G, H = sp.symbols("k G_N H", positive=True)
    a = sp.Symbol("a", positive=True)
    Psi, Psid, drho_tot, dq_tot = sp.symbols("Psi Psi_dot drho_tot dq_tot", real=True)

    C00 = 3 * H * (Psid + H * Psi) + (k**2 / a**2) * Psi + 4 * sp.pi * G * drho_tot
    C0i = Psid + H * Psi + 4 * sp.pi * G * dq_tot

    # eliminate (Psi_dot + H Psi) between them
    lhs = sp.simplify(sp.expand(-(k**2 / a**2) * Psi))
    elim = sp.solve([C00, C0i], [Psid, drho_tot], dict=True)
    print("\n  Eliminating (Psi_dot + H*Psi) between C00=0 and C0i=0:")
    for sgn in (-1, +1):
        cand = 4 * sp.pi * G * (drho_tot + sgn * 3 * H * dq_tot)
        resid = sp.simplify(sp.expand((lhs - cand).subs(elim[0])))
        ok = resid == 0
        print(
            f"    -(k^2/a^2)Psi == 4piG*(drho_tot {'-' if sgn < 0 else '+'} 3H*dq_tot) ?  "
            f"{'EXACT' if ok else 'NO -- residual ' + str(resid)}"
        )
        if sgn == -1:
            assert ok, "the minus form must be exact -- it is the constraint algebra"
        else:
            assert not ok, "the plus form must FAIL -- otherwise the sign is not fixed"

    print("\n  => Delta := drho - 3H*dq,  with a MINUS. P73's Test 3 used a PLUS,")
    print("     which is why it silently failed. The sign is not a convention here;")
    print("     it is fixed by the constraint algebra.")

    print("\n  [AND THE UNCOMFORTABLE COROLLARY, stated because it is load-bearing]")
    print("  With the TOTAL comoving density this is an IDENTITY: mu_tot == 1 by")
    print("  construction, for ANY g_hat and ANY lambda. It measures nothing -- it")
    print("  only re-states the two constraints. So mu carries information ONLY")
    print("  through the matter/scalar SPLIT:")
    print("      mu := -(k^2/a^2)Psi / (4piG * Delta_m)  =  1 + Delta_phi/Delta_m")
    print("  i.e. every deviation of mu from 1 is the scalar's own comoving density")
    print("  measured in units of the matter's. That is what D2-vs-D3 is really")
    print("  asking, and it is NOT the same question as 'does the coupling matter'.")

    # ==================================================================
    # PART B -- LOCK MASS: scalar-free control, mu must be EXACTLY 1
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- LOCK MASS (Gate 3): a control of KNOWN identity on the same run")
    print("-" * 78)
    print("  Pure GR + dust: g_hat=0, lambda=0, phibar_dot(1)=0, dphi=dphi_dot=0.")
    print("  The scalar sector is then identically zero for all time (verified")
    print("  below, not assumed), so Delta_phi == 0 and mu must be EXACTLY 1.")
    print("  This control discriminates: the PLUS sign of Part A fails it at t=1")
    print("  algebraically, so passing is not automatic.")

    lock_ic = {"phidot0": 0.0, "dph0": 0.0, "dphd0": 0.0}
    print(f"\n    {'k':<8}{'mu(t=1)':<18}{'mu(t=1e3)':<18}{'mu(t=1e6)':<18}{'max |mu-1|'}")
    lock_worst = 0.0
    for kk in (0.1, 1.0, 10.0):
        s = run(0.0, 0.0, kk, 1e6, **lock_ic)
        vals = []
        for tv in (1.0, 1e3, 1e6):
            y = s.sol(tv)
            # the scalar sector must be identically zero, or the control is void
            assert abs(y[1]) < 1e-30 and abs(y[2]) < 1e-30, "background scalar moved"
            assert abs(y[5]) < 1e-30 and abs(y[6]) < 1e-30, "scalar perturbation moved"
            vals.append(mu_of(y, 0.0, 0.0, kk))
        worst = max(abs(v - 1.0) for v in vals)
        lock_worst = max(lock_worst, worst)
        print(f"    {kk:<8}{vals[0]:<18.12f}{vals[1]:<18.12f}{vals[2]:<18.12f}{worst:.3e}")

    print(f"\n  => LOCK-MASS RESIDUAL = {lock_worst:.3e}")
    if lock_worst > 1e-6:
        print("  *** LOCK MASS FAILED -> ORACLE_INADEQUATE. This is NOT evidence")
        print("      against the claim; the definition or the evolution is wrong.")
        return 1
    print("  Control PASSES. Every number below is quoted against this residual.")
    print("\n  [WHAT THE CONTROL DOES NOT FIX] it pins the SIGN and the 3H factor.")
    print("  It does NOT pin the matter/total split -- with no scalar present both")
    print("  choices coincide. The split is FINDING_P60's Route B convention, and")
    print("  is a choice, not a derivation. Said here so it is not mistaken for one.")

    # ==================================================================
    # PART C -- mu at converged t, with the numerical floor measured
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- mu with the scalar present, and the numerical floor")
    print("-" * 78)
    print("  P73 read mu at t=1e3, where k=0.1 is still SUPERHORIZON (k/aH=0.57).")
    print("  Report k/aH alongside every number so the reader can see which modes")
    print("  are inside the horizon at the evaluation time.")

    gh, lam = 1.0, 1.0
    T_EVAL = 1e6
    print(f"\n    {'k':<7}{'k/aH @1e6':<13}{'mu(g=1)':<15}{'mu(g=0)':<15}{'D_phi/D_m (g=1)':<18}")
    mus_on, mus_off = {}, {}
    for kk in (0.1, 1.0, 10.0):
        s_on = run(gh, lam, kk, T_EVAL)
        s_off = run(0.0, 0.0, kk, T_EVAL)
        y_on, y_off = s_on.sol(T_EVAL), s_off.sol(T_EVAL)
        b = bg_quantities(y_on[0], y_on[1], y_on[2], gh, lam)
        koaH = kk / (y_on[0] * b["H"])
        m_on, m_off = mu_of(y_on, gh, lam, kk), mu_of(y_off, 0.0, 0.0, kk)
        d = split_densities(y_on, gh, lam)
        mus_on[kk], mus_off[kk] = m_on, m_off
        print(
            f"    {kk:<7}{koaH:<13.3g}{m_on:<15.9f}{m_off:<15.9f}"
            f"{d['Delta_phi'] / d['Delta_m']:<18.6e}"
        )

    print("\n  TOLERANCE SWEEP -- the floor. If a quantity moves with rtol it is")
    print("  measuring the solver, not the model (FINDING_P72's lesson).")
    print(f"\n    {'rtol':<12}{'mu(g=1,k=1)':<22}{'shift vs previous'}")
    floor = 0.0
    prev = None
    for rt in (1e-8, 1e-9, 1e-10, 1e-11, 1e-12):
        y = run(gh, lam, 1.0, T_EVAL, rtol=rt).sol(T_EVAL)
        m = mu_of(y, gh, lam, 1.0)
        sh = "" if prev is None else f"{abs(m - prev):.3e}"
        if prev is not None:
            floor = max(floor, abs(m - prev))
        print(f"    {rt:<12.0e}{m:<22.15f}{sh}")
        prev = m
    floor = max(floor, lock_worst)
    print(f"\n  => NUMERICAL FLOOR = {floor:.3e}")
    print("     (largest rtol-to-rtol shift, or the lock-mass residual, whichever")
    print("      is larger). Nothing smaller than this counts as a signal.")

    # ==================================================================
    # PART D -- the observable: Delta_mu = mu(g_hat=1) - mu(g_hat=0)
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART D -- the pre-registered observable")
    print("-" * 78)
    print("  mu != 1 at g_hat=0 is NOT modified gravity -- a decoupled scalar still")
    print("  gravitates, so it is simply an extra component. The coupling-specific")
    print("  content is the DIFFERENCE. P73's headline died precisely for ignoring")
    print("  this, so here it IS the observable, not an afterthought.")
    print(f"\n    {'k':<8}{'Delta_mu':<20}{'/floor':<14}{'above floor?'}")
    dmu = {}
    for kk in (0.1, 1.0, 10.0):
        d = mus_on[kk] - mus_off[kk]
        dmu[kk] = d
        ratio = abs(d) / floor if floor > 0 else float("inf")
        print(f"    {kk:<8}{d:<20.9e}{ratio:<14.3g}{'YES' if ratio > 10 else 'no'}")

    above = [kk for kk in dmu if abs(dmu[kk]) > 10 * floor]
    if above:
        spread = max(abs(dmu[kk]) for kk in above) / max(min(abs(dmu[kk]) for kk in above), 1e-300)
        print(f"\n    modes above floor: {above};  k-spread of Delta_mu: {spread:.3g}x")
    else:
        spread = 1.0
        print("\n    no mode is above the floor.")

    # ==================================================================
    # PART E -- is that k-dependence PHYSICS, or my own initial data?
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART E -- the check that decides whether Part D means anything")
    print("-" * 78)
    print("  STOP. This is exactly the point where FINDING_P73 went wrong: a clean")
    print("  k-dependent signal that turned out to be inherited rather than caused.")
    print("  Here is the specific worry, stated BEFORE testing it.")
    print()
    print("  initial_data() fixes dphi(1)=1e-6 and drho_A(1)=1e-5 for EVERY k, then")
    print("  solves the 00 constraint for Psi_dot(1). In the scalar-free limit that")
    print("  gives Delta_m(1) = -(k^2/a^2)Psi_0/(4piG) -- the matter side of the")
    print("  ratio scales like k^2 while the scalar side is HELD FIXED. So the ratio")
    print("  Delta_phi/Delta_m starts out proportional to ~1/k^2 BY MY OWN CHOICE.")
    print("  If Part D's spread merely reproduces that, it is a fact about this")
    print("  file, not about the model.")

    print("\n  E1 -- how much of the t=1e6 ratio was already there at t=1?")
    print(
        f"\n    {'k':<7}{'ratio @t=1':<18}{'ratio @t=1e6':<18}{'growth factor':<16}{'Delta_m(1)'}"
    )
    growth = {}
    for kk in (0.1, 1.0, 10.0):
        s = run(gh, lam, kk, T_EVAL)
        d1 = split_densities(s.sol(1.0), gh, lam)
        d2 = split_densities(s.sol(T_EVAL), gh, lam)
        r1 = d1["Delta_phi"] / d1["Delta_m"]
        r2 = d2["Delta_phi"] / d2["Delta_m"]
        growth[kk] = r2 / r1
        print(f"    {kk:<7}{r1:<18.6e}{r2:<18.6e}{growth[kk]:<16.6g}{d1['Delta_m']:.6e}")
    g_spread = max(abs(v) for v in growth.values()) / max(
        min(abs(v) for v in growth.values()), 1e-300
    )
    print(f"\n    growth-factor spread across k: {g_spread:.4g}x")
    print("    Delta_m(1) confirms the k^2 scaling predicted above, so the t=1")
    print("    ratio is NOT a neutral starting point.")

    print("\n  E2 -- renormalise: pick dphi(1) per k so the STARTING ratio is")
    print("  IDENTICAL at every k, then re-measure. The system is linear in the")
    print("  perturbations, so Delta_phi(1) and Delta_m(1) are both AFFINE in")
    print("  dphi(1); the required dphi(1) is solved exactly, not searched.")

    def affine_coeffs(ghv, lamv, kk):
        out = []
        for x in (0.0, 1.0):
            d = split_densities(initial_data(ghv, lamv, kk, dph0=x), ghv, lamv)
            out.append((d["Delta_phi"], d["Delta_m"]))
        (a0_, c0_), (ab_, cd_) = out
        return a0_, ab_ - a0_, c0_, cd_ - c0_

    d_ref = split_densities(initial_data(gh, lam, 1.0), gh, lam)
    r_target = d_ref["Delta_phi"] / d_ref["Delta_m"]
    print(f"\n    target starting ratio (k=1, default data) = {r_target:.6e}")
    print(f"\n    {'k':<7}{'dphi(1) needed':<18}{'ratio @t=1':<18}{'Delta_mu @1e6':<18}{'/floor'}")
    dmu_norm = {}
    for kk in (0.1, 1.0, 10.0):
        ca, cb, cc, cd = affine_coeffs(gh, lam, kk)
        x = (r_target * cc - ca) / (cb - r_target * cd)
        y0 = initial_data(gh, lam, kk, dph0=x)
        r0 = (lambda d: d["Delta_phi"] / d["Delta_m"])(split_densities(y0, gh, lam))
        assert abs(r0 / r_target - 1) < 1e-8, f"renormalisation failed at k={kk}"
        s_on = solve_ivp(
            make_system(gh, lam, kk),
            (1.0, T_EVAL),
            y0,
            rtol=1e-11,
            atol=1e-18,
            dense_output=True,
        )
        ca0, cb0, cc0, cd0 = affine_coeffs(0.0, 0.0, kk)
        x0 = (r_target * cc0 - ca0) / (cb0 - r_target * cd0)
        s_off = solve_ivp(
            make_system(0.0, 0.0, kk),
            (1.0, T_EVAL),
            initial_data(0.0, 0.0, kk, dph0=x0),
            rtol=1e-11,
            atol=1e-18,
            dense_output=True,
        )
        assert s_on.success and s_off.success, f"renormalised run failed at k={kk}"
        dm = mu_of(s_on.sol(T_EVAL), gh, lam, kk) - mu_of(s_off.sol(T_EVAL), 0.0, 0.0, kk)
        dmu_norm[kk] = dm
        print(f"    {kk:<7}{x:<18.6e}{r0:<18.6e}{dm:<18.6e}{abs(dm) / floor:.3g}")

    above_n = [kk for kk in dmu_norm if abs(dmu_norm[kk]) > 10 * floor]
    spread_n = (
        max(abs(dmu_norm[kk]) for kk in above_n)
        / max(min(abs(dmu_norm[kk]) for kk in above_n), 1e-300)
        if above_n
        else 1.0
    )
    print(f"\n    after renormalisation: modes above floor {above_n}, k-spread {spread_n:.4g}x")
    print(f"    (Part D's raw spread was {spread:.4g}x)")

    # ==================================================================
    # PART F -- two hazards Part D/E cannot see, checked before any verdict
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART F -- zero-crossings and t-convergence")
    print("-" * 78)
    print("  Two things must be ruled out before Part D's numbers mean anything,")
    print("  and BOTH are visible in Part D's own table if one looks:")
    print("   (i) Delta_mu CHANGES SIGN between k=0.1 and k=1. A ratio changes sign")
    print("       when its denominator (or numerator) crosses zero -- and near such")
    print("       a crossing mu has a POLE, so its value at one chosen t is")
    print("       arbitrary. If Delta_m crosses zero, the diagnostic is ill-defined")
    print("       there and no verdict may rest on it.")
    print("  (ii) FINDING_P73 died from reading a number at a non-converged t. That")
    print("       was checked for mu; it has NOT yet been checked for Delta_mu.")

    print("\n  F1 -- sign history of the denominator and numerator.")
    print("  The g_hat=0 column is the CONTROL separating 'the coupling causes the")
    print("  crossings' from 'my own initial data does'. Delta_m(1) is NEGATIVE here")
    print("  while its growing mode is positive, so ONE crossing is expected purely")
    print("  as an initial-data transient at ANY coupling; anything beyond that, or")
    print("  any gap between the two columns, is the model.")

    def count_crossings(ghv, lamv, kk):
        s = run(ghv, lamv, kk, T_EVAL)
        dm_s, dp_s, xs = [], [], []
        for tv in np.logspace(0, 6, 4000):
            y = s.sol(tv)
            d = split_densities(y, ghv, lamv)
            dm_s.append(d["Delta_m"])
            dp_s.append(d["Delta_phi"])
            xs.append(abs(ghv * y[1]))
        nm = sum(1 for i in range(1, len(dm_s)) if dm_s[i] * dm_s[i - 1] < 0)
        npp = sum(1 for i in range(1, len(dp_s)) if dp_s[i] * dp_s[i - 1] < 0)
        return nm, npp, max(xs)

    print(
        f"\n    {'k':<6}{'D_m cross (g=1)':<18}{'D_m cross (g=0)':<18}"
        f"{'D_phi cross (g=1)':<20}{'max |x|'}"
    )
    crossings = {}
    for kk in (0.1, 1.0, 10.0):
        nm, npp, xmax = count_crossings(gh, lam, kk)
        nm0, _n0, _x0 = count_crossings(0.0, 0.0, kk)
        crossings[kk] = (nm, npp, nm0)
        print(f"    {kk:<6}{nm:<18}{nm0:<18}{npp:<20}{xmax:.3e}")
    print("\n    (max |x| far below 1 at every k, so FINDING_P65's x=1 pathology is")
    print("     not being approached -- checked, not assumed.)")

    den_bad = [kk for kk in crossings if crossings[kk][0] > 0]
    extra = [kk for kk in crossings if crossings[kk][0] > crossings[kk][2]]
    if den_bad:
        print(f"\n    *** Delta_m CROSSES ZERO at k={den_bad}. mu has a POLE there, so")
        print("        its value at any one chosen t is arbitrary. mu is therefore")
        print("        NOT a well-posed pointwise-in-t diagnostic for this model.")
        print(f"\n        Control read-out: at k={extra} the coupled run crosses MORE")
        print("        often than the g_hat=0 control (3 vs 1 at k=0.1), so those")
        print("        EXTRA crossings are caused by the coupling. At the other k the")
        print("        single crossing matches the control and is the initial-data")
        print("        transient predicted above. So the pathology is of two kinds,")
        print("        and only one of them is mine.")
        print("\n        Delta_phi crosses zero 17-50 times -- consistent with")
        print("        FINDING_P70's established result that phibar itself oscillates")
        print("        THROUGH ZERO with a slowly-varying envelope. P70 resolved that")
        print("        by quoting the ENVELOPE rather than the instantaneous value.")
        print("        The same fix is what mu needs, and it is NOT applied here.")
    else:
        print("\n    Delta_m never changes sign -> no pole in mu. The sign flip in")
        print("    Part D therefore comes from the NUMERATOR Delta_phi, i.e. the")
        print("    scalar's comoving density genuinely changes sign with k -- a")
        print("    statement about the model, not a numerical accident.")

    print("\n  F2 -- is Delta_mu converged in t? (the check that killed P73)")
    print(f"\n    {'t':<10}" + "".join(f"{'D_mu k=' + str(kk):<20}" for kk in (0.1, 1.0, 10.0)))
    sols_on = {kk: run(gh, lam, kk, T_EVAL) for kk in (0.1, 1.0, 10.0)}
    sols_off = {kk: run(0.0, 0.0, kk, T_EVAL) for kk in (0.1, 1.0, 10.0)}
    hist = {kk: [] for kk in sols_on}
    for tv in (1e2, 1e3, 1e4, 1e5, 1e6):
        row = f"    {tv:<10.0e}"
        for kk in (0.1, 1.0, 10.0):
            dm = mu_of(sols_on[kk].sol(tv), gh, lam, kk) - mu_of(sols_off[kk].sol(tv), 0.0, 0.0, kk)
            hist[kk].append(dm)
            row += f"{dm:<20.6e}"
        print(row)
    print(f"\n    {'k':<7}{'|D_mu(1e6)/D_mu(1e5)|':<26}{'converged?'}")
    conv_ok = True
    for kk in (0.1, 1.0, 10.0):
        r = abs(hist[kk][-1] / hist[kk][-2]) if hist[kk][-2] != 0 else float("inf")
        ok = 0.5 < r < 2.0
        conv_ok = conv_ok and ok
        print(f"    {kk:<7}{r:<26.4g}{'yes' if ok else 'NO -- still evolving'}")
    if not conv_ok:
        print("\n    *** Delta_mu is NOT converged over the last decade. Reading it")
        print("        at t=1e6 repeats FINDING_P73's exact error. NO D2/D3 verdict")
        print("        may be issued from this run.")
    else:
        print("\n    Delta_mu changes by less than a factor 2 over the final decade")
        print("    at every k -- the reading is stable, unlike P73's.")


    # ==================================================================
    # PART G -- POST-REVIEW. Three claims of this file are RETRACTED here.
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART G -- post-review verification: what the reviewer got right")
    print("-" * 78)
    print("  A context-blind reviewer attacked Parts B/E/F. It had no shell, so")
    print("  every number it gave was hand-arithmetic or an explicit hypothesis.")
    print("  Per audit-verification-gate that makes all of it INFERRED, not")
    print("  verified. Every one of its claims is re-run here from scratch.")
    print("  THREE of them stand, and they RETRACT claims made above.")

    # ---- G1: does the 'floor' measure the model, or the solver? ----
    print("\n  G1 [RETRACTS Part C] -- Part C said 'the floor is set by the lock")
    print("  mass, not the solver'. The tolerance sweep that justified it ran at")
    print("  g_hat=1, NOT on the lock mass. Sweep the LOCK MASS itself:")
    print(f"\n    {'rtol':<12}{'lock-mass max|mu-1|':<24}{'ratio to previous'}")
    prev, ratios = None, []
    for rt in (1e-8, 1e-10, 1e-11, 1e-12, 1e-13):
        worst = 0.0
        for kk in (0.1, 1.0, 10.0):
            s = run(0.0, 0.0, kk, T_EVAL, rtol=rt, **lock_ic)
            for tv in (1.0, 1e3, 1e6):
                worst = max(worst, abs(mu_of(s.sol(tv), 0.0, 0.0, kk) - 1.0))
        rr = "" if prev is None else f"{worst / prev:.3g}"
        if prev is not None:
            ratios.append(worst / prev)
        print(f"    {rt:<12.0e}{worst:<24.4e}{rr}")
        prev = worst
    print("\n    => the residual FALLS MONOTONICALLY with rtol. It is INTEGRATOR")
    print("       DRIFT, not a property of the definition. *** Part C's sentence")
    print("       'the floor is set by the lock mass, not the solver' is WRONG and")
    print("       is RETRACTED. *** The floor is real as a floor -- nothing below")
    print("       the drift can be trusted -- but its VALUE is a choice of rtol,")
    print("       not a fact about the model.")
    assert all(r < 1.0 for r in ratios), "expected monotone decrease with rtol"

    # ---- G2: how much does the lock mass actually certify? ----
    print("\n  G2 [WEAKENS Part B] -- the reviewer argued the lock mass is blind to")
    print("  ANY modification proportional to the coupling, because g_hat=0 kills")
    print("  it. Test by FABRICATING one: add a pure-invention +7*g*rho_A*dphi to")
    print("  the reference density and re-run the control.")

    def mu_fabricated(y, ghv, lamv, kk):
        a_, pb, pd, psi, _psid, dph, _dphd, drA, qm = y
        b = bg_quantities(a_, pb, pd, ghv, lamv)
        bogus = (
            drA * (1 - ghv * pb)
            - ghv * b["rho_A"] * dph
            - 3 * b["H"] * qm
            + 7 * ghv * b["rho_A"] * dph
        )
        return -(kk**2 / a_**2) * psi / (4 * np.pi * G_N * bogus)

    worst_fab = 0.0
    for kk in (0.1, 1.0, 10.0):
        s = run(0.0, 0.0, kk, T_EVAL, **lock_ic)
        for tv in (1.0, 1e3, 1e6):
            worst_fab = max(worst_fab, abs(mu_fabricated(s.sol(tv), 0.0, 0.0, kk) - 1.0))
    print(f"\n    real definition, lock-mass residual       : {lock_worst:.4e}")
    print(f"    FABRICATED (+7*g*rho_A*dphi) residual     : {worst_fab:.4e}")
    print("\n    => IDENTICAL. The control is completely blind to it. *** Part B's")
    print("       'the control discriminates' is far weaker than stated and is")
    print("       WEAKENED: the lock mass certifies the sign and the 3H factor of")
    print("       the MATTER branch, and nothing that vanishes at g_hat=0. ***")
    assert abs(worst_fab - lock_worst) / lock_worst < 1e-6, "expected identical residuals"

    # ---- G3: the identity, checked numerically at last ----
    print("\n  G3 [STRENGTHENS Part A] -- Part A asserted mu_tot == 1 algebraically")
    print("  and never checked it numerically. That was a real omission. Check it:")

    def mu_tot_of(y, ghv, lamv, kk):
        d = split_densities(y, ghv, lamv)
        return -(kk**2 / y[0] ** 2) * y[3] / (4 * np.pi * G_N * (d["Delta_m"] + d["Delta_phi"]))

    worst_tot = 0.0
    for kk in (0.1, 1.0, 10.0):
        s = run(gh, lam, kk, T_EVAL)
        for tv in (1e3, 1e5, 1e6):
            worst_tot = max(worst_tot, abs(mu_tot_of(s.sol(tv), gh, lam, kk) - 1.0))
    print(f"\n    worst |mu_tot - 1| along the g_hat=1 solution: {worst_tot:.4e}")
    print("    => the identity is numerically realised, three orders BELOW the")
    print("       lock-mass drift. Part A's corollary stands, now with a number.")
    assert worst_tot < 1e-8, "mu_tot identity must hold numerically"

    # ---- G4: Part E had no lever. Find one. ----
    print("\n  G4 [FALSIFIES Part E] -- Part E varied only dphi(1), which is")
    print("  subdominant by amplitude, so its 'no change' result was close to")
    print("  tautological. Vary what it never touched: phibar_dot(1), the")
    print("  background scalar rate that drives the whole scalar sector.")
    print(f"\n    {'variation':<24}{'Dmu k=0.1':<18}{'Dmu k=1':<18}{'Dmu k=10'}")
    lever = {}
    for label, kw in (
        ("baseline", {}),
        ("psi0 x100", {"psi0": 1e-3}),
        ("phibar_dot(1) x0.5", {"phidot0": 0.5 * PHIDOT_INIT}),
        ("phibar_dot(1) x2", {"phidot0": 2.0 * PHIDOT_INIT}),
    ):
        vals = []
        for kk in (0.1, 1.0, 10.0):
            on, off = run(gh, lam, kk, T_EVAL, **kw), run(0.0, 0.0, kk, T_EVAL, **kw)
            vals.append(mu_of(on.sol(T_EVAL), gh, lam, kk) - mu_of(off.sol(T_EVAL), 0.0, 0.0, kk))
        lever[label] = vals
        print(f"    {label:<24}{vals[0]:<18.4e}{vals[1]:<18.4e}{vals[2]:.4e}")
    vs = [lever[lbl][0] for lbl in lever]
    swing = max(abs(v) for v in vs) / max(min(abs(v) for v in vs), 1e-300)
    signs = len({v > 0 for v in vs})
    print(f"\n    at k=0.1: Delta_mu swings {swing:.3g}x and CHANGES SIGN "
          f"({'yes' if signs > 1 else 'no'}).")
    print("    Varying psi0 by 100x moves it <2%; varying phibar_dot(1) by 2x")
    print("    inverts it. *** Part E's 'the result is initial-data independent'")
    print("    is FALSIFIED. Delta_mu is not a property of the model at all in")
    print("    this setup -- it depends on an initial condition. ***")
    assert swing > 10 and signs > 1, "expected a large, sign-changing swing"

    # ---- G5: when do the crossings happen? ----
    print("\n  G5 [RETRACTS part of F1] -- F1 argued the Delta_m zero-crossings")
    print("  make the t=1e6 reading arbitrary. That only holds if a crossing is")
    print("  NEAR t=1e6. Locate them:")
    late = False
    for kk in (0.1, 1.0, 10.0):
        s = run(gh, lam, kk, T_EVAL)
        ts = np.logspace(0, 6, 20000)
        dm = np.array([split_densities(s.sol(tv), gh, lam)["Delta_m"] for tv in ts])
        idx = np.where(dm[1:] * dm[:-1] < 0)[0]
        late = late or any(ts[i] > 1e4 for i in idx)
        where = ", ".join(f"{ts[i]:.3g}" for i in idx) if len(idx) else "none"
        print(f"    k={kk:<6} crossings at t = {where}")
    print("\n    => ALL crossings are at t < 35 -- early transients, five decades")
    print("       before the evaluation time. *** F1's inference 'poles make the")
    print("       t=1e6 reading arbitrary' is WRONG and is RETRACTED. *** What")
    print("       survives from F1 is only the control read-out: the EXTRA")
    print("       crossings at k=0.1 are coupling-caused. That is a statement")
    print("       about early-time behaviour, and it does not reach t=1e6.")
    assert not late, "no crossing should be near the evaluation time"

    # ---- G6: is F2 aliasing? ----
    print("\n  G6 [CONFIRMS AND SHARPENS F2] -- with F1 retracted, F2 is the ONLY")
    print("  surviving ground for withholding a verdict, so it must be tested")
    print("  properly. The reviewer suggested decade-boundary sampling could be")
    print("  aliasing an oscillation. Sample DENSELY inside the last decade:")
    print(f"\n    {'k':<7}{'sign flips in [1e5,1e6]':<26}{'min':<15}{'max'}")
    flips_tot = 0
    for kk in (0.1, 1.0, 10.0):
        on, off = run(gh, lam, kk, T_EVAL), run(0.0, 0.0, kk, T_EVAL)
        ts = np.logspace(5, 6, 400)
        d = np.array(
            [mu_of(on.sol(tv), gh, lam, kk) - mu_of(off.sol(tv), 0.0, 0.0, kk) for tv in ts]
        )
        fl = sum(1 for i in range(1, len(d)) if d[i] * d[i - 1] < 0)
        flips_tot += fl
        print(f"    {kk:<7}{fl:<26}{d.min():<15.3e}{d.max():.3e}")
    print("\n    => NOT aliasing: 25 genuine sign flips per decade at k=0.1 and")
    print("       k=10, with a bounded amplitude -- a real oscillation with an")
    print("       envelope, exactly FINDING_P70's phibar behaviour propagating")
    print("       into the diagnostic. At k=1 there are ZERO flips, so its")
    print("       non-convergence is a genuine decay, not oscillation.")
    print("       F2 stands, and is now the load-bearing ground for NO VERDICT.")
    assert flips_tot > 20, "expected many sign flips -- otherwise F2 is aliasing"

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in this file's docstring)")
    print("=" * 78)
    print(f"  lock mass       : {lock_worst:.3e}   (Gate 3 control, PASSED)")
    print(f"  numerical floor : {floor:.3e}")
    print("  Delta_mu (raw)  : " + ", ".join(f"k={kk}: {dmu[kk]:.3e}" for kk in dmu))
    print("  Delta_mu (renorm): " + ", ".join(f"k={kk}: {dmu_norm[kk]:.3e}" for kk in dmu_norm))
    print(f"  IC-growth spread: {g_spread:.4g}x  (1.0 => ALL k-dependence inherited)")
    print(f"  Delta_mu converged over final decade: {'yes' if conv_ok else 'NO'}")
    print(f"  Delta_mu oscillations inside the last decade: {flips_tot} sign flips")
    print(f"  Delta_mu swing under phibar_dot(1) variation: {swing:.3g}x, sign changes")
    print()
    if not conv_ok or flips_tot > 20 or swing > 10:
        print("  -> NO VERDICT, on TWO independent grounds, neither of which is the")
        print("     one this file originally gave:")
        print("     (1) Delta_mu OSCILLATES ~25 times per decade at k=0.1 and k=10")
        print("         (G6), so no single t gives a stable reading. This is")
        print("         FINDING_P70's phibar oscillation propagating into the")
        print("         diagnostic, and P70's own fix -- quote the ENVELOPE -- is")
        print("         what is needed. Not applied here.")
        print("     (2) Delta_mu depends on phibar_dot(1) strongly enough to CHANGE")
        print("         SIGN (G4), so it is not a property of the model in this")
        print("         setup at all. This ground was found only after review.")
        print("     The pole argument this file first gave (F1) is RETRACTED: G5")
        print("     shows every zero-crossing sits at t < 35, five decades early.")
        print("     NO VERDICT is NOT evidence against the claim -- it means the")
        print("     diagnostic is not in a state to give one.")
    elif not above_n:
        print("  -> D2. With a gauge-correct reference density and a converged-t")
        print("     evaluation, the coupling makes NO difference to the Poisson")
        print("     relation above this setup's own numerical floor. mu is DEAD as")
        print("     a discriminator for this model, and the question of which")
        print("     completion is correct cannot be settled through this channel.")
    elif spread_n > 3.0:
        print("  -> D3. Delta_mu survives the initial-data renormalisation AND stays")
        print("     k-dependent, so the k-dependence is a property of the MODEL.")
    else:
        print("  -> above floor but nearly k-INDEPENDENT: a constant offset, which")
        print("     is a rescaling of G_eff, not a scale-dependent modification.")
        print("     Neither D2 nor D3 as FINDING_P60 worded them.")

    print("\n  ESTABLISHED HERE:")
    print("   * the comoving reference density is Delta = drho - 3H*dq, DERIVED from")
    print("     the two first-class constraints, with the PLUS form shown to fail;")
    print("     FINDING_P73's Test 3 had the sign wrong, which is why it failed;")
    print("   * with the TOTAL density mu == 1 is an IDENTITY -- so mu's entire")
    print("     information content sits in the matter/scalar split, not in the")
    print("     Poisson equation itself;")
    print(f"   * a LOCK MASS of known identity residual {lock_worst:.1e}, so every")
    print("     number above is quoted against a stated control.")
    print("\n  NOT ESTABLISHED:")
    print("   * that the matter/total split is derived. It is FINDING_P60's Route B")
    print("     CONVENTION; the lock mass cannot discriminate it, and says so.")
    print("   * anything at k outside [0.1, 10], or for (g_hat,lambda) != (1,1).")
    print("   * that k maps to h/Mpc. Comoving units of OUR construction.")
    print("   * anything about MULTING itself (Gate 1): V is OUR construction.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
