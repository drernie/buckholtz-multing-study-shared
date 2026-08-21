"""P75 -- which relations survive EVERY admissible completion?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

THE QUESTION, and why it is not the obvious one. The campaign has been asking
"which completion of the local law is correct?" -- a scalar with V(phi)? a
different mass law m(phi)? Every answer needs an observable that separates them,
and FINDING_P74 just showed the mu channel is ill-posed pointwise in t. So invert
it: instead of asking which completion is right, ask WHAT MUST BE TRUE OF ALL OF
THEM. An invariant needs no discriminating observable to be worth having.

This is not a new programme with no track record. It already has one confirmed
instance and one confirmed counter-instance, both established before the question
was posed -- which is exactly the positive/negative control pair Gate 3 demands:

  POSITIVE  FINDING_P58: Q^0_A = -g_hat*rhobar*phibar_dot holds "EXACT in
            g_hat*phibar, no truncation, ANY V(phi)" -- V' cancels entirely.
            Route B gives rhobar_dot + 3H*rhobar = rhobar*(dln m/dphi)*phibar_dot
            for ANY m(phi). Two invariants, already proven.
  NEGATIVE  FINDING_P66: a^3*phibar_dot = sqrt(2) + g_hat*(t-1) is NOT invariant
            -- FINDING_P69 broke it by restoring V, since
            d/dt(a^3*phibar_dot) - g_hat*C = -a^3*V'.

A test that cannot tell those two apart discriminates nothing, so this file runs
BOTH through the same machinery before testing anything new.

THE COMPLETION FAMILY. Two free functions, left as unspecified sympy Functions:
    V(phi)   the potential                     -- P45's quartic is one choice
    M(phi)   the mass law, m(phi)/m_0, M(0)=1  -- P33's (1 - g_hat*phi) is one
                                                  choice, P68's exp(-g_hat*phi)
                                                  another
Everything is derived for general V and M, then specialised to the committed
model as a positive control (it MUST reproduce FINDING_P73's results verbatim).

WHAT IS TESTED:
  A. controls -- does the machinery reproduce P58 (invariant) and P66 (not)?
  B. the first-class constraint algebra dC00/dt = -3H*C00 + (k^2/a^2)*C0i:
     do the coefficients survive general V and general M?
  C. the H-dot obstruction of FINDING_P71: same question.
  D. an explicit ledger of what is and is not completion-invariant.
"""

import sympy as sp

t = sp.Symbol("t", positive=True)
k, G = sp.symbols("k G_N", positive=True)
a = sp.Function("a")(t)
phib = sp.Function("phibar")(t)
rhoA = sp.Function("rho_A")(t)  # BARE density n_bar*m_0; rho_A*a^3 = C (P58)
H = sp.diff(a, t) / a

V = sp.Function("V")
M = sp.Function("M")
Vb, Vpb, Vppb = V(phib), sp.diff(V(phib), phib), sp.diff(V(phib), phib, 2)
Mb, Mpb, Mppb = M(phib), sp.diff(M(phib), phib), sp.diff(M(phib), phib, 2)

rho_phys = rhoA * Mb

Psi = sp.Function("Psi")(t)
dphi = sp.Function("dphi")(t)
drhoA = sp.Function("drho_A")(t)
Qm = sp.Function("Q_m")(t)

drho_phi = sp.diff(phib, t) * sp.diff(dphi, t) - Psi * sp.diff(phib, t) ** 2 + Vpb * dphi
dp_phi = sp.diff(phib, t) * sp.diff(dphi, t) - Psi * sp.diff(phib, t) ** 2 - Vpb * dphi
drho_m = drhoA * Mb + rhoA * Mpb * dphi
drho_tot = drho_phi + drho_m
dq_tot = -sp.diff(phib, t) * dphi + Qm

# Background + perturbation system, general V and M. Reduces to FINDING_P73's
# system at V = lambda*phi^4/4 and M = 1 - g_hat*phi (checked in Part A).
SUBS = [
    (
        sp.diff(Psi, t, 2),
        4 * sp.pi * G * dp_phi - 4 * H * sp.diff(Psi, t) - (2 * sp.diff(H, t) + 3 * H**2) * Psi,
    ),
    (
        sp.diff(dphi, t, 2),
        -Mpb * drhoA
        - 2 * Psi * (rhoA * Mpb + Vpb)
        + 4 * sp.diff(Psi, t) * sp.diff(phib, t)
        - 3 * H * sp.diff(dphi, t)
        - (k**2 / a**2 + Vppb) * dphi
        - rhoA * Mppb * dphi,
    ),
    (
        sp.diff(drhoA, t),
        -3 * H * drhoA + 3 * sp.diff(Psi, t) * rhoA + (k**2 / a**2) * Qm / Mb,
    ),
    (sp.diff(Qm, t), -3 * H * Qm - rhoA * Mb * Psi - rhoA * Mpb * dphi),
    (sp.diff(phib, t, 2), -3 * H * sp.diff(phib, t) - Vpb - rhoA * Mpb),
    (sp.diff(rhoA, t), -3 * H * rhoA),
]

C00 = 3 * H * (sp.diff(Psi, t) + H * Psi) + (k**2 / a**2) * Psi + 4 * sp.pi * G * drho_tot
C0i = sp.diff(Psi, t) + H * Psi + 4 * sp.pi * G * dq_tot
R_Hdot = sp.diff(H, t) + 4 * sp.pi * G * (rho_phys + sp.diff(phib, t) ** 2)
HDOT_SUB = sp.solve(R_Hdot, sp.diff(a, t, 2))[0]


def reduce_expr(expr, rounds=3):
    for _ in range(rounds):
        for old, new in SUBS:
            expr = expr.subs(old, new)
    return expr


def specialise(expr, ghv, lamv):
    """Committed model: V = lam*phi^4/4, M = 1 - g_hat*phi."""
    x = sp.Symbol("x_")
    return (
        expr.subs(
            [
                (V(x), lamv * x**4 / 4),
                (M(x), 1 - ghv * x),
            ]
        )
        .replace(V, lambda z: lamv * z**4 / 4)
        .replace(M, lambda z: 1 - ghv * z)
    )


def main() -> int:
    print("=" * 78)
    print("P75 -- completion invariants: what must hold for EVERY admissible V, M?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    gh, lam = sp.symbols("g_hat lambda", real=True)

    # ==================================================================
    # PART A -- controls. A test that cannot separate P58 from P66 is not a test
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- the control pair, run BEFORE anything new is tested")
    print("-" * 78)
    print("  A relation is COMPLETION-INVARIANT here if, after imposing the")
    print("  background equations, it holds with V and M left as unspecified")
    print("  functions. Two relations of KNOWN status go through first.")

    print("\n  A1 [POSITIVE CONTROL, FINDING_P58] the matter exchange term.")
    print("  P58: rhobar_dot + 3H*rhobar = rhobar*(dln m/dphi)*phibar_dot, ANY m.")
    print("  With rho_phys = rho_A*M(phi) and rho_A*a^3 = C:")
    lhs_a1 = sp.diff(rho_phys, t) + 3 * H * rho_phys
    rhs_a1 = rho_phys * (Mpb / Mb) * sp.diff(phib, t)
    res_a1 = sp.simplify(sp.expand(reduce_expr(lhs_a1 - rhs_a1)))
    print(f"    residual with V, M UNSPECIFIED: {res_a1}")
    assert res_a1 == 0, "P58's Route B must be reproduced -- machinery is broken"
    print("    => INVARIANT. Holds for every V and every M. P58 reproduced.")

    print("\n  A2 [NEGATIVE CONTROL, FINDING_P66/P69] the first integral.")
    print("  P66: a^3*phibar_dot = sqrt(2) + g_hat*(t-1); P69 broke it with V.")
    d_first_int = sp.simplify(sp.expand(reduce_expr(sp.diff(a**3 * sp.diff(phib, t), t))))
    print(f"    d/dt(a^3*phibar_dot) general = {d_first_int}")
    assert d_first_int != 0, "must NOT vanish -- otherwise the control is void"
    # [FIXED AFTER REVIEW] the original guard here was
    #     assert d_first_int.has(V) or d_first_int.has(sp.Derivative)
    # which is VACUOUS: H = a_dot/a, so ANY expression carrying an H satisfies
    # .has(sp.Derivative) whether or not V survived. A guard a bare H passes
    # cannot certify "V survived". Test for the V-derivative SPECIFICALLY.
    print(f"    [guard] the old .has(sp.Derivative) check is vacuous: "
          f"H.has(Derivative) = {H.has(sp.Derivative)}")
    assert d_first_int.has(sp.Derivative(V(phib), phib)), "must retain V'"
    assert d_first_int.has(sp.Derivative(M(phib), phib)), "must retain M'"
    print("    => NOT INVARIANT: it retains -a^3*V'(phibar), so it depends on the")
    print("       choice of V. P69's breakage reproduced.")
    print("\n  The machinery separates the two known cases. It discriminates.")

    # ==================================================================
    # PART B -- the first-class constraint algebra
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- is the constraint ALGEBRA completion-invariant?")
    print("-" * 78)
    print("  FINDING_P73 established, for the committed model (quartic V, linear M):")
    print("      dC00/dt = -3H*C00 + (k^2/a^2)*C0i")
    print("  The coefficients -3H and k^2/a^2 contain no V and no M. If that")
    print("  survives general V and M, the ALGEBRA is an invariant of the whole")
    print("  completion family, not a feature of one choice.")

    A_, B_ = sp.symbols("A_ B_")
    d00 = reduce_expr(sp.diff(C00, t)).subs(sp.diff(a, t, 2), HDOT_SUB)
    d00 = sp.simplify(sp.expand(d00))
    C00s = sp.simplify(C00.subs(sp.diff(a, t, 2), HDOT_SUB))
    C0is = sp.simplify(C0i.subs(sp.diff(a, t, 2), HDOT_SUB))

    expr = sp.expand(d00 - A_ * C00s - B_ * C0is)
    fields = [Psi, sp.diff(Psi, t), dphi, sp.diff(dphi, t), drhoA, Qm]
    eqs = sp.Poly(expr, *fields).coeffs()
    sol = sp.solve(eqs[:2], [A_, B_], dict=True)
    assert sol, "no (A,B) even from two coefficients -- algebra not closed"
    resid = sp.simplify(sp.expand(expr.subs(sol[0])))
    print(f"\n    residual over ALL coefficients, V and M unspecified: {resid}")
    print(f"    A = {sp.simplify(sol[0][A_])}")
    print(f"    B = {sp.simplify(sol[0][B_])}")
    inv_algebra = resid == 0
    if inv_algebra:
        assert sp.simplify(sol[0][A_] + 3 * H) == 0, "A must be -3H"
        assert sp.simplify(sol[0][B_] - k**2 / a**2) == 0, "B must be k^2/a^2"
        print("\n    => the algebra is COMPLETION-INVARIANT. dC00/dt = -3H*C00 +")
        print("       (k^2/a^2)*C0i holds for EVERY V and EVERY M, with coefficients")
        print("       that reference neither. FINDING_P73's result was not a feature")
        print("       of the quartic or of the linear mass law.")
    else:
        print("\n    => NOT invariant: the algebra depends on the completion.")

    print("\n  [POSITIVE CONTROL] specialise to the committed model and confirm the")
    print("  same coefficients come back -- so this generalises P73 rather than")
    print("  contradicting it.")
    a_sp = sp.simplify(specialise(sol[0][A_], gh, lam) + 3 * H)
    b_sp = sp.simplify(specialise(sol[0][B_], gh, lam) - k**2 / a**2)
    print(f"    A + 3H  at V=lam*phi^4/4, M=1-g_hat*phi : {a_sp}")
    print(f"    B - k^2/a^2                            : {b_sp}")
    assert a_sp == 0 and b_sp == 0, "specialisation must reproduce P73"
    print("    => P73 reproduced exactly as the special case.")

    # ==================================================================
    # PART C -- FINDING_P71's obstruction
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- is P71's obstruction completion-invariant?")
    print("-" * 78)
    print("  FINDING_P71: dC0i/dt|_{C=0} = -Psi*[H_dot + 4piG*(rho_tot + p_tot)].")
    print("  P71 proved the residual is LAMBDA-free for the quartic. Whether it is")
    print("  free of the MASS LAW too was never tested -- P68's exponential m(phi)")
    print("  is a live alternative completion, so this matters.")
    dC = reduce_expr(sp.diff(C0i, t), rounds=2)
    dC = sp.simplify(sp.expand(dC.subs(Qm, sp.solve(C0i, Qm)[0])))
    holds = sp.simplify(sp.expand(dC + Psi * R_Hdot)) == 0
    print(f"\n    dC0i/dt == -Psi*R_Hdot with V, M unspecified ?  {holds}")
    if holds:
        print("    => INVARIANT. The obstruction P71 named, and P72 removed, is the")
        print("       SAME obstruction for every completion in this family. So P72's")
        print("       closure is not specific to P69's background either.")
    else:
        print(f"    => NOT invariant; leftover = {sp.simplify(sp.expand(dC + Psi * R_Hdot))}")


    # ==================================================================
    # PART E -- POST-REVIEW: is Part B circular?
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART E -- the circularity charge, tested rather than argued")
    print("-" * 78)
    print("  A context-blind reviewer made one central charge: Part B is CIRCULAR.")
    print("  This file writes the evolution equations itself (SUBS) and then checks")
    print("  an identity among its own equations, so the closure is guaranteed by")
    print("  construction and proves nothing. That is testable in one move: BREAK")
    print("  one equation at a time and see whether the algebra still closes.")
    print("  (The reviewer had no shell and could not run this. It is run here.)")

    def closes(subs_list):
        e = sp.diff(C00, t)
        for _ in range(3):
            for old, new in subs_list:
                e = e.subs(old, new)
        e = sp.simplify(sp.expand(e.subs(sp.diff(a, t, 2), HDOT_SUB)))
        c00s = sp.simplify(C00.subs(sp.diff(a, t, 2), HDOT_SUB))
        c0is = sp.simplify(C0i.subs(sp.diff(a, t, 2), HDOT_SUB))
        ex = sp.expand(e - A_ * c00s - B_ * c0is)
        cc = sp.solve(sp.Poly(ex, *fields).coeffs()[:2], [A_, B_], dict=True)
        if not cc:
            return False
        return sp.simplify(sp.expand(ex.subs(cc[0]))) == 0

    SABOTAGES = [
        ("KG drag 3H -> 2H", 4, lambda e: e + H * sp.diff(phib, t)),
        ("KG: drop V'", 4, lambda e: e + Vpb),
        ("KG: drop rho_A*M'", 4, lambda e: e + rhoA * Mpb),
        ("Psi_ddot: 4H -> 5H", 0, lambda e: e - H * sp.diff(Psi, t)),
        ("matter continuity: 3H -> 2H", 2, lambda e: e + H * drhoA),
        ("continuity: flip the k^2*Q sign", 2, lambda e: e - 2 * (k**2 / a**2) * Qm / Mb),
        ("Euler: drop the exchange term", 3, lambda e: e + rhoA * Mpb * dphi),
        ("rho_A dilution: 3H -> 4H", 5, lambda e: e + H * rhoA),
    ]
    print(f"\n    {'deliberately broken equation':<38}{'still closes?'}")
    caught = 0
    survivors = []
    for label, idx, mutate in SABOTAGES:
        s2 = list(SUBS)
        s2[idx] = (s2[idx][0], mutate(s2[idx][1]))
        ok = closes(s2)
        if not ok:
            caught += 1
        else:
            survivors.append(label)
        print(f"    {label:<38}{'YES -- test blind here' if ok else 'no -- caught'}")
    print(f"\n    => {caught} of {len(SABOTAGES)} sabotages BREAK the closure.")
    print("       The charge of circularity is REFUTED: the system is")
    print("       over-determined (2 unknowns A,B against 6 coefficient equations),")
    print("       so closure is a real constraint on the equations, not bookkeeping.")
    assert caught >= 6, "if few sabotages are caught, the test really is circular"
    if survivors:
        print(f"\n    [BLIND SPOT, reported not hidden] {survivors} does NOT break")
        print("     the closure. The 00-constraint algebra simply does not")
        print("     constrain that term, so Part B certifies less than 'the whole")
        print("     system is right'. Named here so it is not mistaken for full")
        print("     coverage.")

    print("\n  E2 -- the reviewer also said the Bianchi framing and P71's")
    print("  'obstruction' are mutually exclusive: if propagation follows from")
    print("  covariance, there was never an obstruction to remove. Test the")
    print("  reconciliation -- Bianchi holds ON-SHELL; the obstruction is what")
    print("  appears OFF-SHELL. Re-run the closure WITHOUT imposing H-dot:")
    e2 = sp.diff(C00, t)
    for _ in range(3):
        for old, new in SUBS:
            e2 = e2.subs(old, new)
    ex2 = sp.expand(sp.simplify(sp.expand(e2)) - A_ * C00 - B_ * C0i)
    cc2 = sp.solve(sp.Poly(ex2, *fields).coeffs()[:2], [A_, B_], dict=True)
    off_shell_ok = bool(cc2) and sp.simplify(sp.expand(ex2.subs(cc2[0]))) == 0
    print(f"\n    closure WITHOUT the H-dot equation imposed: {off_shell_ok}")
    assert not off_shell_ok, "if it closed off-shell, P71's obstruction was fictional"
    print("    => it does NOT close. So both statements are true and there is no")
    print("       contradiction: Bianchi gives propagation ON-SHELL, and P71's")
    print("       obstruction is exactly the OFF-SHELL failure. But P71 is")
    print("       DEFLATED accordingly -- the 'obstruction' is the requirement to")
    print("       impose the FULL background system rather than a subset, which is")
    print("       standard GR bookkeeping, not a discovery.")

    # ==================================================================
    # PART D -- the ledger
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART D -- ledger: what is, and is not, completion-invariant")
    print("-" * 78)
    rows = [
        ("rho_A*a^3 = C (bare)", "INVARIANT", "imposed; P58's premise, n*a^3 fixed"),
        ("matter exchange form (P58 Route B)", "INVARIANT", "A1, any V and any M"),
        ("constraint algebra (P73)", "INVARIANT" if inv_algebra else "NOT", "Part B"),
        ("H-dot obstruction (P71)", "INVARIANT" if holds else "NOT", "Part C"),
        ("first integral a^3*phibar_dot (P66)", "NOT INVARIANT", "A2, retains -a^3*V'"),
        ("mu(a,k)", "UNTESTED HERE", "P74: ill-posed pointwise in t"),
    ]
    print(f"\n    {'relation':<38}{'status':<16}{'source'}")
    for r in rows:
        print(f"    {r[0]:<38}{r[1]:<16}{r[2]}")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    n_inv = sum(1 for r in rows if r[1] == "INVARIANT")
    print(f"  {n_inv} relations proven invariant across the (V, M) completion family,")
    print("  against 1 proven NON-invariant -- so the result is a separation, not a")
    print("  blanket 'everything is invariant' that would discriminate nothing.")
    print()
    print(f"  POST-REVIEW: circularity charge REFUTED ({caught}/{len(SABOTAGES)} sabotages")
    print("  break the closure), but P71's obstruction is DEFLATED to 'impose the")
    print("  full background system'. One blind spot named, not hidden.")
    print()
    print("  WHAT THIS MEANS FOR THE COMPLETION QUESTION. The structural layer --")
    print("  what the constraints are, how they propagate, what obstructs them --")
    print("  is SHARED by every completion in this family. So no amount of work on")
    print("  that layer can ever distinguish P68's exponential mass law from P69's")
    print("  quartic potential: they are structurally identical there by proof, not")
    print("  by coincidence. Discrimination has to come from the DYNAMICAL layer,")
    print("  and FINDING_P74 just showed this campaign's main dynamical channel is")
    print("  ill-posed as currently defined.")
    print()
    print("  NOT ESTABLISHED:")
    print("   * that these are ALL the invariants. This file tests named candidates;")
    print("     it does not enumerate the invariant ring. Absence of a test is not")
    print("     absence of an invariant.")
    print("   * that the (V, M) family is the whole completion space. Worldline-EFT")
    print("     and coarse-grained routes are NOT in it, and nothing here bears on")
    print("     them.")
    print("   * anything observational. These are structural identities; none of")
    print("     them predicts a number.")
    print("   * anything about MULTING itself (Gate 1): the family is OURS.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
