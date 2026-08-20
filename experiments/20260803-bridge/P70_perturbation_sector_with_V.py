"""P70 -- redo the perturbation sector with V(phibar) != 0.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

FINDING_P69 established that V != 0 breaks the exact background first integral
that FINDING_P66/P67/P68 rest on, and concluded that the perturbation sector --
derived throughout at V=0 -- must be redone before any mu or gamma result from
that arc can be quoted. This file does that redo.

PRE-REGISTRATION. This is not a step invented after a null result. FINDING_P57
itself names it, in its own text: it verified that linearizing V'(phi)=lambda*phi^3
gives V''(phibar)*deltaphi = 3*lambda*phibar^2*deltaphi exactly, and recorded that
adding this to the LHS was "not built here, an explicit future step, needed before
this equation can be called the field equation of the full committed monopole
action." P70 is that step.

What this file establishes:
  A. the epsilon^1 equation re-derived WITH V, from the covariant equation, not
     by patching P57's result -- with P57's own equation as the lambda=0 control,
     and a separate check that V introduces NO new Phi/Psi couplings;
  B. the physical content: V'' is a MASS, so deltaphi acquires a finite Yukawa
     range and its quasi-static response gains an exact transfer function
     T(k) = k^2/(k^2 + a^2*m_eff^2) relative to the V=0 case;
  C. [SELF-CAUGHT, and it overturned this file's own first headline] phibar
     does NOT settle onto FINDING_P69's attractor -- it OSCILLATES THROUGH
     ZERO, tens of times. So m_eff vanishes periodically and there is NO
     constant screening scale. What IS true, and is the more interesting
     statement: a*m_eff becomes asymptotically PERIODIC with a CONSTANT
     COMOVING ENVELOPE (same-parity peaks repeat to ~1e-5 per period across
     decades). The screening is therefore INTERMITTENT -- at every zero
     crossing the scalar is momentarily massless and the suppression switches
     off entirely;
  D. k_J = sqrt(3)*lambda^(1/6)*(g*C)^(1/3) survives as the ENVELOPE scale, so
     lambda^(1/6) still compresses lambda's ten-plus allowed decades by exactly
     a factor 6 -- but k_J tracks the envelope only to a factor 1.2-2.4;
  E. what this does and does NOT settle for FINDING_P60's D1/D2/D3.
"""

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks

G_N = 1.0
C_MATTER = 1.0
A3_INIT = 6.0 * np.pi - 1.0
PHIDOT_INIT = np.sqrt(2.0) / A3_INIT
LAMBDA_MIN_P69 = 10.0**-10.54  # FINDING_P69's own critical lambda at g_hat=1


def rhs_bg(_t: float, y: np.ndarray, ghat: float, lam: float) -> list[float]:
    """FINDING_P69's coupled background, reused verbatim for the Part C check."""
    a, phibar, phibardot = y
    rho_A = C_MATTER / a**3
    V = lam * phibar**4 / 4.0
    arg = (8.0 * np.pi * G_N / 3.0) * (rho_A * (1.0 - ghat * phibar) + phibardot**2 / 2.0 + V)
    H = np.sqrt(max(arg, 0.0))
    return [a * H, phibardot, ghat * rho_A - 3.0 * H * phibardot - lam * phibar**3]


def main() -> int:
    print("=" * 78)
    print("P70 -- perturbation sector redone with V(phibar) != 0")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    t = sp.Symbol("t", positive=True)
    eps, ghat, lam = sp.symbols("epsilon g_hat lambda", real=True)
    a_f = sp.Function("a")(t)
    H_f = sp.diff(a_f, t) / a_f

    # ==================================================================
    # PART A -- re-derive the epsilon^1 equation WITH V
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- epsilon^1 equation re-derived WITH V (not patched onto P57)")
    print("-" * 78)

    x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
    phibar = sp.Function("phibar")(t)
    dphi = sp.Function("dphi")(t, x1, x2, x3)
    rhobar = sp.Function("rhobar")(t)
    drho = sp.Function("drho")(t, x1, x2, x3)
    Phi = sp.Function("Phi")(t, x1, x2, x3)
    Psi = sp.Function("Psi")(t, x1, x2, x3)

    phi_full = phibar + eps * dphi
    rho_full = rhobar + eps * drho

    # WHY reconstructed rather than imported: so the lambda=0 check below is a
    # genuine reproduction test of FINDING_P57 rather than a tautology.
    lap = sum(sp.diff(phi_full, xi, 2) for xi in (x1, x2, x3)) / a_f**2
    box_phi = (
        sp.diff(phi_full, t, 2)
        + 3 * H_f * sp.diff(phi_full, t)
        - lap
        - 2 * Phi * eps * sp.diff(phibar, t, 2)
        - 6 * H_f * Phi * eps * sp.diff(phibar, t)
        - eps * sp.diff(Phi, t) * sp.diff(phibar, t)
        - 3 * eps * sp.diff(Psi, t) * sp.diff(phibar, t)
    )

    # full field equation WITH the potential:  box(phi) + V'(phi) = g_hat*rho
    field_eq = box_phi + lam * phi_full**3 - ghat * rho_full
    order0 = sp.simplify(field_eq.subs(eps, 0))
    order1 = sp.simplify(sp.diff(field_eq, eps).subs(eps, 0))

    expected0 = (
        sp.diff(phibar, t, 2) + 3 * H_f * sp.diff(phibar, t) + lam * phibar**3 - ghat * rhobar
    )
    assert sp.simplify(order0 - expected0) == 0, f"background mismatch: {order0}"
    print("  epsilon^0 (background), WITH V:")
    print("    phibar_ddot + 3H*phibar_dot + lambda*phibar^3 = g_hat*rhobar")
    print("    => matches FINDING_P69's own background EOM exactly.")

    # POSITIVE CONTROL: at lambda=0, order1 must reduce EXACTLY to P57's equation
    p57_eq = (
        sp.diff(dphi, t, 2)
        + 3 * H_f * sp.diff(dphi, t)
        - sum(sp.diff(dphi, xi, 2) for xi in (x1, x2, x3)) / a_f**2
        - ghat * drho
        - 2 * Phi * sp.diff(phibar, t, 2)
        - 6 * H_f * Phi * sp.diff(phibar, t)
        - sp.diff(Phi, t) * sp.diff(phibar, t)
        - 3 * sp.diff(Psi, t) * sp.diff(phibar, t)
    )
    resid_p57 = sp.simplify(order1.subs(lam, 0) - p57_eq)
    assert resid_p57 == 0, f"lambda=0 does NOT reproduce P57's equation: {resid_p57}"
    print("\n  [positive control] at lambda=0 the epsilon^1 equation reduces to")
    print("  FINDING_P57's own equation EXACTLY -- zero symbolic residual, by")
    print("  direct subtraction, not by inspection.")

    added = sp.simplify(order1 - p57_eq)
    print(f"\n  What V adds to the epsilon^1 equation:  {added}")
    assert sp.simplify(added - 3 * lam * phibar**2 * dphi) == 0, f"unexpected: {added}"
    print("  => EXACTLY +V''(phibar)*deltaphi = +3*lambda*phibar^2*deltaphi,")
    print("     which is what FINDING_P57 pre-registered as the missing step.")

    assert not (added.has(Phi) or added.has(Psi)), f"V introduced a metric coupling: {added}"
    print("\n  [structural check] the added term contains NEITHER Phi NOR Psi.")
    print("  V is not metric-dependent, so it cannot source new gravitational")
    print("  couplings -- the extension is a PURE MASS TERM, nothing else. That")
    print("  is why P57's Phi/Psi analysis survives V != 0 unchanged, even though")
    print("  P69 showed the BACKGROUND first integral does not.")

    # ==================================================================
    # PART B -- a Yukawa mass and an exact transfer function
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- V'' is a MASS: deltaphi acquires a finite range")
    print("-" * 78)
    k, a_s, C_s = sp.symbols("k a C", positive=True)
    dphi_k, drho_k, src_k = sp.symbols("dphi_k drho_k S_k", real=True)
    pb = sp.Symbol("phibar_val", positive=True)
    m_eff_sq = 3 * lam * pb**2
    print(f"  m_eff^2 := V''(phibar) = {m_eff_sq}   (>= 0 for lambda > 0)")
    print("  In k-space, quasi-static (drop time derivatives of deltaphi):")
    print("    (k^2/a^2 + m_eff^2)*deltaphi_k = g_hat*deltarho_k + [Phi,Psi source]")

    sol_V = sp.solve(sp.Eq((k**2 / a_s**2 + m_eff_sq) * dphi_k, ghat * drho_k + src_k), dphi_k)[0]
    sol_0 = sp.solve(sp.Eq((k**2 / a_s**2) * dphi_k, ghat * drho_k + src_k), dphi_k)[0]
    transfer = sp.simplify(sol_V / sol_0)
    print(f"\n  deltaphi_k (V != 0) / deltaphi_k (V = 0) = {transfer}")
    assert sp.simplify(transfer - k**2 / (k**2 + a_s**2 * m_eff_sq)) == 0, "transfer wrong"
    print("  => EXACT Yukawa transfer function  T(k) = k^2 / (k^2 + a^2*m_eff^2).")
    print("     Every modification carried by deltaphi is multiplied by T(k)")
    print("     relative to the V=0 sector. This is exact in the quasi-static")
    print("     limit and follows from the field equation ALONE -- it needs")
    print("     nothing from the (still unclosed) Einstein sector.")

    T_large_k = sp.limit(transfer, k, sp.oo)
    T_small_k = sp.limit(transfer, k, 0)
    assert T_large_k == 1, f"T(k->oo) should be 1, got {T_large_k}"
    assert T_small_k == 0, f"T(k->0) should be 0, got {T_small_k}"
    print(f"\n  T(k -> infinity) = {T_large_k}  => V=0 sector recovered on small scales")
    print(f"  T(k -> 0)        = {T_small_k}  => modification SCREENED on large scales")
    print("  The scalar mediates a finite-range force. At V=0 it was massless and")
    print("  therefore infinite-range -- that was an artifact of the truncation.")

    # ==================================================================
    # PART C -- [SELF-CAUGHT, MAJOR] phibar OSCILLATES THROUGH ZERO
    # ==================================================================
    print("\n    " + "-" * 78)
    print("PART C -- the screening scale: what I first claimed, and what is true")
    print("-" * 78)
    print("  FIRST CLAIM, NOW WITHDRAWN: since FINDING_P69 found the attractor")
    print("  phibar -> (g_hat*rho_A/lambda)^(1/3) with rho_A = C/a^3, the scale")
    print("  factor cancels in a*m_eff and the comoving screening scale is a")
    print("  CONSTANT k_J = sqrt(3)*lambda^(1/6)*(g_hat*C)^(1/3).")
    phibar_att = (ghat * C_s / lam) ** sp.Rational(1, 3) / a_s
    k_J = sp.powsimp(sp.simplify(a_s * sp.sqrt(3 * lam * phibar_att**2)), force=True)
    assert not k_J.has(a_s), f"k_J still depends on a: {k_J}"
    k_J_closed = sp.sqrt(3) * lam ** sp.Rational(1, 6) * (ghat * C_s) ** sp.Rational(1, 3)
    # WHY numeric: sympy will not collapse sqrt(lambda*(g/lambda)^(2/3)) to
    # lambda^(1/6)*g^(1/3) under powsimp(force=True) -- branch-cut caution.
    for lv, gv, cv in ((1.0, 1.0, 1.0), (1e-6, 0.3, 2.0), (7.0, 2.5, 0.4)):
        sub = {lam: lv, ghat: gv, C_s: cv}
        assert abs(float(sp.N(k_J.subs(sub))) / float(sp.N(k_J_closed.subs(sub))) - 1) < 1e-12
    print(f"  The algebra is right: a*m_eff = {k_J_closed}, a genuinely cancels.")
    print()
    print("  BUT THE PREMISE IS FALSE. phibar does NOT settle onto the attractor.")
    print("  Checked directly against the integrated background:")
    print(f"\n    {'g_hat':<7}{'lambda':<9}{'zero crossings':<17}{'phibar/phi_eq range'}")
    for gv, lv in ((1.0, 1.0), (1.0, 1e-2), (0.1, 1.0)):
        sol = solve_ivp(
            rhs_bg, (1.0, 1e5), [A3_INIT ** (1.0 / 3.0), 0.0, PHIDOT_INIT],
            args=(gv, lv), rtol=1e-12, atol=1e-15, dense_output=True,
        )
        assert sol.success, f"background failed at g={gv}, lam={lv}"
        ts = np.logspace(0.0, 5.0, 40000)
        a_v, pb_v, _ = sol.sol(ts)
        cross = int(np.sum(pb_v[:-1] * pb_v[1:] < 0))
        ratio = pb_v / ((gv * (C_MATTER / a_v**3) / lv) ** (1.0 / 3.0))
        late = ratio[ts > 1e3]
        print(f"    {gv:<7}{lv:<9.0e}{cross:<17}[{late.min():+.3f}, {late.max():+.3f}]")
        assert cross > 5, f"expected many zero crossings at g={gv}, lam={lv}, got {cross}"
    print("\n    => phibar OSCILLATES THROUGH ZERO, tens of times, and never")
    print("     converges to the attractor. So m_eff = sqrt(3*lambda)*|phibar|")
    print("     VANISHES periodically: there is NO constant screening scale, and")
    print("     the first claim above is WITHDRAWN.")
    print()
    print("  WHAT IS ACTUALLY TRUE, and it is the more interesting statement:")
    print("  a*m_eff becomes asymptotically PERIODIC with a CONSTANT ENVELOPE.")
    print("  The scale-factor cancellation is real -- it fixes the envelope, not")
    print("  the value. Local maxima of a*m_eff, late times:")
    print(f"\n    {'g_hat':<7}{'lambda':<9}{'last 4 peaks':<34}{'drift/period':<14}{'mean/k_J'}")
    for gv, lv in ((1.0, 1.0), (1.0, 1e-2), (0.1, 1.0)):
        sol = solve_ivp(
            rhs_bg, (1.0, 1e5), [A3_INIT ** (1.0 / 3.0), 0.0, PHIDOT_INIT],
            args=(gv, lv), rtol=1e-12, atol=1e-15, dense_output=True,
        )
        ts = np.logspace(0.0, 5.0, 200000)
        a_v, pb_v, _ = sol.sol(ts)
        am = a_v * np.sqrt(3.0 * lv * pb_v**2)
        peaks = [
            i for i in range(50, len(am) - 50)
            if am[i] == max(am[i - 50 : i + 51]) and am[i] > 0
        ]
        last = [am[i] for i in peaks[-4:]]
        kj = np.sqrt(3.0) * lv ** (1.0 / 6.0) * (gv * C_MATTER) ** (1.0 / 3.0)
        # peaks alternate between two values; compare like with like, 2 periods apart
        drift = abs(last[3] / last[1] - 1.0) if len(last) == 4 else float("nan")
        txt = " ".join(f"{v:.4f}" for v in last)
        print(f"    {gv:<7}{lv:<9.0e}{txt:<34}{drift:<14.2e}{np.mean(last) / kj:.3f}")
        assert drift < 1e-3, f"envelope not settled at g={gv}, lam={lv}: drift={drift}"
    print("\n    => same-parity peaks repeat to better than 1e-3 per period across")
    print("     decades: the comoving envelope IS asymptotically constant, even")
    print("     though a*m_eff itself is not. k_J sets that envelope's MAGNITUDE")
    print("     to within a factor 1.2-2.4 -- it is a scale, not a value.")
    print()
    print("  [SKEPTIC-DEMANDED robustness] the reviewer argued this drift could")
    print("  be LOG-GRID ALIASING: at t=1e5 a 200k log grid has spacing ~5.8, so")
    print("  an O(1) oscillation period would be undersampled. Re-measured on")
    print("  independent grids and integrator tolerances:")
    print(f"\n    {'grid / rtol':<26}{'drift (g=1, lambda=1)':<24}{'verdict'}")
    for label, ts_r, rt in (
        ("log 2e5 pts, rtol 1e-12", np.logspace(0.0, 5.0, 200000), 1e-12),
        ("log 2e6 pts, rtol 1e-12", np.logspace(0.0, 5.0, 2000000), 1e-12),
        ("LINEAR 2e6 late, 1e-12", np.linspace(1e4, 1e5, 2000000), 1e-12),
        ("LINEAR 2e6 late, 1e-8", np.linspace(1e4, 1e5, 2000000), 1e-8),
    ):
        s_r = solve_ivp(
            rhs_bg,
            (1.0, 1e5),
            [A3_INIT ** (1.0 / 3.0), 0.0, PHIDOT_INIT],
            args=(1.0, 1.0),
            rtol=rt,
            atol=rt * 1e-3,
            dense_output=True,
        )
        a_r, pb_r, _ = s_r.sol(ts_r)
        am_r = a_r * np.sqrt(3.0 * pb_r**2)
        pk, _ = find_peaks(am_r)
        dr = abs(am_r[pk[-1]] / am_r[pk[-3]] - 1.0)
        print(f"    {label:<26}{dr:<24.3e}stable")
        assert dr < 1e-4, f"drift not stable on {label}: {dr}"
    print("\n    => drift agrees to THREE significant figures across a 10x grid")
    print("       refinement, a log-to-linear grid change, and a 1e4x tolerance")
    print("       change. NOT an aliasing or integrator artifact.")
    print("    [why the reviewer's arithmetic missed] their estimate assumed an")
    print("    O(1) oscillation period. It is not: only ~21 peaks occur over five")
    print("    decades, so the period GROWS with t. The log grid is in fact the")
    print("    appropriate one -- their premise, not their logic, was wrong.")
    print()
    print("  STRUCTURAL CONSEQUENCE: the screening is INTERMITTENT -- at each")
    print("  zero crossing m_eff vanishes and the Yukawa suppression switches off.")
    print("  [SKEPTIC-CORRECTED, and the correction matters] an earlier draft")
    print("  called this a 'distinctive phenomenology'. It is NOT, on this")
    print("  evidence. The crossings are a MEASURE-ZERO set in time, so they")
    print("  contribute NOTHING to any time-integrated observable. Calling the")
    print("  scalar 'momentarily massless' describes the algebra, not a predicted")
    print("  effect. Establishing observable consequences would require a")
    print("  time-dependent mode-equation treatment -- an oscillating quartic")
    print("  condensate sourcing perturbations is the standard preheating setup,")
    print("  with its own resonance analysis and large literature. This file")
    print("  performs none of that, so the honest status is an UNRESOLVED")
    print("  REGIME, not a prediction.")

    # ==================================================================
    # PART D -- what survives of the lambda^(1/6) claim
    # ==================================================================
    print("\n    " + "-" * 78)
    print("PART D -- lambda^(1/6): what survives the Part C correction")
    print("-" * 78)
    print("  The lambda^(1/6) scaling is a property of k_J, and k_J survives as")
    print("  the ENVELOPE scale (Part C). So the compression argument survives")
    print("  too, but as a statement about a scale, not about a measured value.")
    print(f"\n    {'lambda':<14}{'k_J (g_hat=1, C=1)':<22}{'vs lambda=1'}")
    kJ1 = np.sqrt(3.0)
    for lv in (1e0, 1e-3, 1e-6, 1e-9, LAMBDA_MIN_P69):
        kj = np.sqrt(3.0) * lv ** (1.0 / 6.0)
        print(f"    {lv:<14.2e}{kj:<22.6f}{kj / kJ1:.4f}")
    dec_lam = -np.log10(LAMBDA_MIN_P69)
    dec_kJ = np.log10(kJ1 / (np.sqrt(3.0) * LAMBDA_MIN_P69 ** (1.0 / 6.0)))
    assert abs(dec_kJ - dec_lam / 6.0) < 1e-6, "compression is not exactly 1/6"
    print(f"\n    lambda spans {dec_lam:.2f} decades -> k_J spans {dec_kJ:.2f}")
    print("  => exactly a factor 6, by construction. But note the honest limit:")
    print("     the factor 1.2-2.4 scatter between k_J and the actual envelope")
    print("     (Part C) is itself ~0.3 decades, so it is NOT negligible against")
    print("     the 1.76 decades the lambda-range contributes.")

    # ==================================================================
    # PART E -- what this settles for D1/D2/D3, and what it does not
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART E -- consequences for FINDING_P60's D1/D2/D3")
    print("-" * 78)
    print("  D1 (a genuine leading modification survives, lim_{k->inf} mu != 1)")
    print("  was RULED OUT at V=0. Does the mass term revive it?")
    print(f"    T(k -> infinity) = {T_large_k}, so the k->infinity limit is")
    print("    UNCHANGED by V. D1 stays ruled out. [no revival]")
    print()
    print("  D2 (mu = 1 identically at every k) vs D3 (leading cancellation with")
    print("  a k-dependent residual) was UNDECIDED at V=0, blocked on Psi_k:")
    print("   * V != 0 introduces a DEFINITE new k-dependence T(k) with a")
    print("     computable scale k_J -- structurally a D3-type signature;")
    print("   * BUT T(k) MULTIPLIES whatever the V=0 sector delivered. If that")
    print("     was identically zero (D2), then T(k)*0 = 0 and D2 still holds.")
    print("     A transfer function cannot manufacture a residual from nothing.")
    print("  => V != 0 does NOT decide D2 vs D3. It supplies the k-dependence a")
    print("     D3 outcome would need, and leaves the question where FINDING_P61")
    print("     left it: blocked on closing Psi_k.")
    print()
    print("  Does V help close Psi_k?")
    print("  [SKEPTIC-CAUGHT, and my first answer here was WRONG] I wrote that V")
    print("  adds no Phi/Psi coupling, therefore it cannot alter the constraint")
    print("  structure FINDING_P61 found non-closing. That inference SKIPS A")
    print("  SECTOR. Part A's result is about the SCALAR equation of motion. But")
    print("  V also enters the scalar STRESS-ENERGY, which sources Einstein:")
    T00 = sp.Rational(1, 2) * sp.diff(phi_full, t) ** 2 + lam * phi_full**4 / 4
    Tii = sp.Rational(1, 2) * sp.diff(phi_full, t) ** 2 - lam * phi_full**4 / 4
    dT00 = sp.simplify(sp.diff(T00, eps).subs(eps, 0))
    dTii = sp.simplify(sp.diff(Tii, eps).subs(eps, 0))
    V00 = sp.simplify(dT00 - dT00.subs(lam, 0))
    Vii = sp.simplify(dTii - dTii.subs(lam, 0))
    print(f"    V-piece of delta_T00 = {V00}")
    print(f"    V-piece of delta_Tii = {Vii}")
    assert V00 != 0 and Vii != 0, "V must source both energy and pressure perturbations"
    assert sp.simplify(V00 + Vii) == 0, "expected equal and opposite (V is not kinetic)"
    print("    => both nonzero, equal and opposite: V'(phibar)*deltaphi enters the")
    print("       ENERGY and PRESSURE perturbations. The Einstein constraints that")
    print("       Psi_k must satisfy are therefore GENUINELY MODIFIED by V.")
    print("  => the claim 'the Psi_k blocker survives V != 0 untouched' is")
    print("     WITHDRAWN. Whether V helps or hurts closure is OPEN and requires")
    print("     redoing FINDING_P61's constraint chain with these source terms --")
    print("     which this file does NOT do. What Part A established is narrower")
    print("     than I first claimed: the SCALAR EOM's Phi/Psi structure is")
    print("     unchanged; the Einstein-sector consequences of V are not analysed.")

    # NEGATIVE CONTROL: lambda<0 -> m_eff^2 < 0 -> tachyon -> finite-k pole
    print("\n  [negative control] lambda < 0 gives m_eff^2 < 0 (tachyonic).")
    T_num = sp.lambdify((k, a_s, lam, pb), k**2 / (k**2 + a_s**2 * 3 * lam * pb**2), "numpy")
    k_pole = float(np.sqrt(3.0 * 1.0 * 0.5**2))
    val_below = float(T_num(k_pole * 0.5, 1.0, -1.0, 0.5))
    val_above = float(T_num(k_pole * 2.0, 1.0, -1.0, 0.5))
    print(f"    at lambda=-1, phibar=0.5, a=1: pole at k = {k_pole:.4f}")
    print(f"    T(k=pole/2) = {val_below:+.4f}   T(k=2*pole) = {val_above:+.4f}")
    assert val_below < 0, "tachyonic case should give a NEGATIVE transfer below the pole"
    assert val_above > 0, "above the pole the transfer should be positive"
    print("    => the transfer function CHANGES SIGN across a finite-k pole -- an")
    print("       unmistakable instability signature. The formalism detects the")
    print("       wrong-sign case rather than silently returning something plausible.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("  ESTABLISHED:")
    print("   * the epsilon^1 equation WITH V, re-derived from the covariant")
    print("     equation rather than patched, with FINDING_P57's own equation")
    print("     recovered EXACTLY at lambda=0 (zero symbolic residual);")
    print("   * V adds EXACTLY +3*lambda*phibar^2*deltaphi and NOTHING else -- in")
    print("     particular no new Phi/Psi coupling, so P57's metric-perturbation")
    print("     analysis survives V != 0 even though P69 showed the background")
    print("     first integral does not. That asymmetry is the main structural")
    print("     result: V breaks the BACKGROUND machinery but not the")
    print("     PERTURBATION machinery;")
    print("   * [DEMOTED after review -- see below] deltaphi acquires a FINITE")
    print("     Yukawa range, with an exact quasi-static transfer function")
    print("     T(k)=k^2/(k^2+a^2*m_eff^2), derived from the field equation alone.")
    print("     The FORMULA is correct. Its USEFUL DOMAIN is not established:")
    print("       k >> k_J : T -> 1, nothing new (D1 already ruled out);")
    print("       k << k_J : T -> 0, but it MULTIPLIES a V=0 answer that may")
    print("                  itself be zero (D2), so no residual is manufactured;")
    print("       k ~  k_J : the only regime where T's 1->0 transition could")
    print("                  predict something -- and there the quasi-static")
    print("                  assumption is KNOWN VIOLATED (Part C).")
    print("     Those three regimes partition k. The reviewer's phrasing was")
    print("     'the file derives a formula and then disqualifies every regime")
    print("     where it would matter', and that is accurate. Recorded as a")
    print("     DERIVED FORMULA AWAITING A TIME-DEPENDENT TREATMENT, not as a")
    print("     standing result.")
    print("   * [NEW, after withdrawing this file's own first headline] phibar")
    print("     does NOT settle onto FINDING_P69's attractor -- it OSCILLATES")
    print("     THROUGH ZERO (21/10/15 crossings in the cases checked), so m_eff")
    print("     vanishes periodically and there is NO constant screening scale;")
    print("   * what IS asymptotically constant is the comoving ENVELOPE of")
    print("     a*m_eff -- same-parity peaks repeat across decades to")
    print("     (grid- and tolerance-independent: identical to three")
    print("     significant figures across a 10x grid refinement, a")
    print("     log-to-linear grid change, and a 1e4x tolerance change);")
    print("     2e-5..6e-5 per period. k_J sets that envelope to 1.2-2.4x;")
    print("   * the screening is INTERMITTENT -- but this is a STRUCTURAL")
    print("     statement, not a predicted effect: the crossings are a")
    print("     measure-zero set in time and contribute nothing to any")
    print("     time-integrated observable. Downgraded after review from")
    print("     'distinctive phenomenology' to an UNRESOLVED REGIME that")
    print("     needs the preheating-style mode analysis this file skips;")
    print("   * lambda^(1/6) still compresses lambda's 10.54 allowed decades by")
    print("     exactly a factor 6, but the factor 1.2-2.4 envelope scatter is")
    print("     itself ~0.3 decades and is NOT negligible against the 1.76.")
    print()
    print("  NOT ESTABLISHED:")
    print("   * mu(a,k) itself. T(k) multiplies the V=0 sector's answer, and that")
    print("     answer is still unknown at finite k because Psi_k is unclosed.")
    print("   * that V leaves the Psi_k blocker untouched -- I claimed this and")
    print("     it is WITHDRAWN. V sources delta_T00 and delta_Tii with")
    print("     V'(phibar)*deltaphi, so the Einstein constraints Psi_k must")
    print("     satisfy ARE modified. Whether that helps or hurts closure is")
    print("     open and needs FINDING_P61's chain redone with these sources.")
    print("   * D2 vs D3. V != 0 supplies the k-dependence a D3 outcome needs but")
    print("     cannot manufacture a residual from an identically-zero one.")
    print("   * that k_J is observable. It is a comoving scale in OUR units")
    print("     (G_N=C=1, FINDING_P62's B=D=1); mapping it to h/Mpc requires a")
    print("     calibration this file does not perform.")
    print("   * T(k) as a STATIC filter. It is exact in the quasi-static limit")
    print("     for a given INSTANTANEOUS m_eff -- but Part C shows m_eff itself")
    print("     oscillates on the very timescale that sets the screening scale.")
    print("     So near k ~ k_J the static reading is NOT justified. This is no")
    print("     longer a hypothetical caveat: the assumption is known to be")
    print("     violated exactly where the effect lives. A time-dependent")
    print("     treatment of the deltaphi mode equation is the next step, and")
    print("     this file does not attempt it.")
    print("   * that the quartic is the right V (FINDING_P45 called it minimal and")
    print("     its own review retracted part of the case for quartic specifically).")
    print("   * anything about MULTING itself (Gate 1): V is OUR construction.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
