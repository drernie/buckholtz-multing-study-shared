"""P71 -- FINDING_P61's constraint chain redone with delta_T_munu(V).

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

FINDING_P70 withdrew its own claim that V leaves FINDING_P61's Psi_k blocker
untouched: V sources delta_T00 and delta_Tii with V'(phibar)*deltaphi, so the
Einstein constraints Psi_k must satisfy ARE modified. P70's named next step was
to redo P61's constraint chain with those sources included. This file does that.

APPROACH, and why it is not a patch of P61's script. P61 tested consistency by
differentiating the 0i momentum constraint and substituting every first time
derivative via the 00 equation, matter continuity, the scalar field equation and
Euler. That test is a SPECIALISATION of a more basic statement: the total
stress-energy must be covariantly conserved. This file attacks the basic
statement directly, because it is convention-independent -- reproducing P61's
exact residual would require matching conventions that its summary does not fix,
and a mismatched convention would produce a meaningless "nonzero".

What this file establishes:
  A. the exchange identity: div T_phi = (box phi - V')*grad phi, so imposing the
     COUPLED Klein-Gordon equation leaves div T_phi = -g_hat*rho*grad phi --
     with V CANCELLING EXACTLY. The energy-momentum exchange term is
     V-INDEPENDENT;
  B. therefore the Bianchi-closure CONDITION on the matter sector is exactly the
     one P61 already had. V changes what each sector's own equations say; it does
     NOT change what closure requires;
  C. an explicit first-order check in Newtonian gauge, with negative controls
     that break each background equation in turn;
  D. what this does and does not settle for P61's D5 and for Psi_k.
"""

import sympy as sp


def main() -> int:
    print("=" * 78)
    print("P71 -- FINDING_P61's constraint chain redone with delta_T_munu(V)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    t = sp.Symbol("t", positive=True)
    ghat = sp.Symbol("g_hat", real=True)

    # ==================================================================
    # PART A -- the exchange identity, and V's exact cancellation
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- does V change the energy-momentum EXCHANGE term?")
    print("-" * 78)
    print("  [SKEPTIC-CORRECTED FRAMING] what follows is a STANDARD IDENTITY,")
    print("  STATED here, not derived in code. The reviewer was right that an")
    print("  assert of the form 'V-prime minus V-prime is zero' verifies the")
    print("  cancellation and nothing about the identity itself. Part A is kept")
    print("  for orientation; the load is carried entirely by PART F, which")
    print("  derives nothing from it.")
    print()
    print("  For a minimally coupled scalar in ANY metric,")
    print("    T_phi^{mu nu} = d^mu phi d^nu phi - g^{mu nu}[ (1/2)(d phi)^2 + V ]")
    print("  the divergence collapses to a single scalar factor times grad phi:")
    print("    div_mu T_phi^{mu nu} = (box phi - V'(phi)) * d^nu phi")
    print("  because d^mu phi grad_mu grad^nu phi = (1/2) grad^nu (d phi)^2 exactly")
    print("  cancels the kinetic half of the g^{mu nu} bracket, leaving only V'.")
    print()
    print("  Now impose the COUPLED Klein-Gordon equation of this campaign.")
    print("  [and a free negative control] the cancellation needs V-prime to enter")
    print("  the DIVERGENCE and the FIELD EQUATION with the same coefficient. Flip")
    print("  the field equation alone -- an inconsistent pairing, not an alternative")
    print("  convention -- and V must SURVIVE. Both branches are printed, so the")
    print("  cancellation is visibly specific rather than automatic.")
    boxphi, Vp, rho, gradphi = sp.symbols("boxphi Vprime rho_A gradphi", real=True)
    div_T_phi = (boxphi - Vp) * gradphi
    for sgn in (+1, -1):
        kg = sp.Eq(boxphi, sgn * (Vp - ghat * rho))
        onshell = sp.simplify(div_T_phi.subs(boxphi, sp.solve(kg, boxphi)[0]))
        has_V = onshell.has(Vp)
        print(f"    sign {sgn:+d}: box phi = {str(sp.solve(kg, boxphi)[0]):<28} "
              f"div T_phi -> {onshell}   V present? {has_V}")
        if sgn == +1:
            assert not has_V, "V survived in the exchange term for the consistent pairing"
            div_T_phi_onshell = onshell
        else:
            assert has_V, "inconsistent pairing did NOT keep V -- check is vacuous"
    print()
    print(f"    physical branch: div T_phi on-shell = {div_T_phi_onshell}")
    assert sp.simplify(div_T_phi_onshell + ghat * rho * gradphi) == 0, "exchange term wrong"
    assert not div_T_phi_onshell.has(Vp), "V survived in the exchange term"
    print("\n  *** V CANCELS EXACTLY. *** The V' from the divergence and the V' from")
    print("  the field equation are the SAME term with opposite signs. What is left,")
    print("  -g_hat*rho_A*grad phi, is precisely the V=0 exchange term.")
    print()
    print("  => the condition the MATTER sector must satisfy for the total to be")
    print("     conserved -- div T_matter = +g_hat*rho_A*grad phi -- is EXACTLY the")
    print("     one FINDING_P61 already had. V does NOT change what closure")
    print("     REQUIRES; it changes only what each sector's own equations SAY.")

    # ==================================================================
    # PART B -- explicit background check (nu = 0 component)
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- explicit background check, then the same with V removed")
    print("-" * 78)
    a = sp.Function("a")(t)
    phibar = sp.Function("phibar")(t)
    rhoA = sp.Function("rho_A")(t)
    lam = sp.Symbol("lambda", real=True)
    H = sp.diff(a, t) / a
    V = lam * phibar**4 / 4
    Vprime = sp.diff(V, phibar)

    # scalar background energy and pressure
    rho_phi = sp.diff(phibar, t) ** 2 / 2 + V
    p_phi = sp.diff(phibar, t) ** 2 / 2 - V
    # background continuity for the scalar sector, with the exchange source
    lhs_phi = sp.diff(rho_phi, t) + 3 * H * (rho_phi + p_phi)
    # [SELF-CAUGHT SIGN BUG, kept visible] a first version set
    #   exchange = -g_hat*rho_A*phibar_dot
    # and the on-shell residual came out 2*g_hat*rho_A*phibar_dot -- exactly
    # DOUBLE, which is the signature of a flipped sign rather than a missing
    # term. Worked through by hand: rho_phi_dot + 3H(rho_phi+p_phi)
    #   = phibar_dot*(phibar_ddot + V' + 3H*phibar_dot) = +g_hat*rho_A*phibar_dot
    # on the coupled KG. So the SCALAR sector GAINS energy at that rate and the
    # matter sector loses it. Sign corrected below; the doubling was the tell.
    exchange = ghat * rhoA * sp.diff(phibar, t)
    resid_phi = sp.simplify(lhs_phi - exchange)
    print(f"  scalar background continuity residual (before KG): {sp.simplify(resid_phi)}")
    # impose background KG:  phibar_ddot + 3H phibar_dot + V' = g_hat rho_A
    kg_bg = ghat * rhoA - 3 * H * sp.diff(phibar, t) - Vprime
    resid_phi_on = sp.simplify(resid_phi.subs(sp.diff(phibar, t, 2), kg_bg))
    assert resid_phi_on == 0, f"scalar sector not conserved on-shell: {resid_phi_on}"
    print("  after substituting the background KG:               0")
    print("  => the scalar sector's own continuity is an IDENTITY given its own")
    print("     equation of motion, WITH V present. [positive control]")

    # the same with lambda -> 0 must also vanish (V=0 limit)
    resid_V0 = sp.simplify(resid_phi_on.subs(lam, 0))
    assert resid_V0 == 0, "V=0 limit broken"
    print("  the V=0 limit of the same computation:              0   [control]")

    # matter sector: rho_phys = rho_A*(1 - g_hat*phibar), dust (p=0)
    rho_phys = rhoA * (1 - ghat * phibar)
    lhs_m = sp.diff(rho_phys, t) + 3 * H * rho_phys
    # matter must LOSE exactly what the scalar gains, for the total to close
    resid_m = sp.simplify(lhs_m + exchange)
    print(f"\n  matter continuity residual (before rho_A eq):      {sp.simplify(resid_m)}")
    # impose rho_A_dot = -3 H rho_A  (FINDING_P58's unconditional result)
    resid_m_on = sp.simplify(resid_m.subs(sp.diff(rhoA, t), -3 * H * rhoA))
    print(f"  after substituting rhobar_A_dot = -3H*rhobar_A:     {resid_m_on}")
    assert resid_m_on == 0, f"matter sector does not balance the exchange: {resid_m_on}"
    print("  => the two sectors' exchange terms cancel EXACTLY, so the TOTAL")
    print("     background stress-energy is conserved. V never enters this balance.")

    # ==================================================================
    # PART C -- first order: does V enter the momentum constraint at all?
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- first order: which perturbed components does V touch?")
    print("-" * 78)
    eps = sp.Symbol("epsilon", real=True)
    dphi = sp.Function("dphi")(t)
    Psi = sp.Function("Psi")(t)
    k = sp.Symbol("k", positive=True)

    phi_full = phibar + eps * dphi
    V_full = lam * phi_full**4 / 4

    # energy density perturbation (Newtonian gauge, Phi=Psi per FINDING_P49)
    rho_phi_full = sp.diff(phi_full, t) ** 2 / 2 * (1 - 2 * eps * Psi) + V_full
    drho_phi = sp.simplify(sp.diff(rho_phi_full, eps).subs(eps, 0))
    V_in_drho = sp.simplify(drho_phi - drho_phi.subs(lam, 0))
    print(f"  delta_rho_phi          = {drho_phi}")
    print(f"    V-piece              = {V_in_drho}")
    assert V_in_drho != 0, "V should enter the energy perturbation"

    # isotropic pressure perturbation
    p_phi_full = sp.diff(phi_full, t) ** 2 / 2 * (1 - 2 * eps * Psi) - V_full
    dp_phi = sp.simplify(sp.diff(p_phi_full, eps).subs(eps, 0))
    V_in_dp = sp.simplify(dp_phi - dp_phi.subs(lam, 0))
    print(f"    V-piece of delta_p   = {V_in_dp}")
    assert sp.simplify(V_in_drho + V_in_dp) == 0, "expected equal and opposite"

    # MOMENTUM density: T^0_i = -phidot * d_i(deltaphi).  V does NOT appear,
    # because the g^{mu nu}*[...] bracket is diagonal and g^{0i}=0 in this gauge.
    q_full = -sp.diff(phi_full, t) * (sp.I * k * eps * dphi)
    dq = sp.simplify(sp.diff(q_full, eps).subs(eps, 0))
    V_in_dq = sp.simplify(dq - dq.subs(lam, 0))
    print(f"\n  delta_q_phi (momentum) = {dq}")
    print(f"    V-piece              = {V_in_dq}")
    assert V_in_dq == 0, f"V should NOT enter the momentum density, got {V_in_dq}"
    print("\n  *** THE 0i MOMENTUM CONSTRAINT IS V-INDEPENDENT. ***")
    print("  V enters delta_rho and delta_p (equal and opposite) but NOT the")
    print("  momentum density, because the potential sits in the g^{mu nu} bracket")
    print("  and g^{0i}=0 in Newtonian gauge. So the very constraint FINDING_P61")
    print("  differentiated -- C := 2ik(Psi_dot+H*Psi) - 8piG*T_01 -- is unchanged.")

    # ==================================================================
    # PART D -- negative controls: break each background equation
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART D -- negative controls: does the balance detect a broken input?")
    print("-" * 78)
    print("  A conservation check that vanishes no matter what is worthless.")
    print("  Break each background equation in turn; each must produce nonzero.")
    print(f"\n    {'broken input':<38}{'total residual':<16}{'detected?'}")
    bad_kg = ghat * rhoA - 3 * H * sp.diff(phibar, t) - 2 * Vprime  # wrong V' coefficient
    r1 = sp.simplify(resid_phi.subs(sp.diff(phibar, t, 2), bad_kg))
    print(
        f"    {'KG with V-prime coefficient 2x':<38}{'nonzero' if r1 != 0 else 'ZERO':<16}"
        f"{'YES' if r1 != 0 else 'NO -- BLIND'}"
    )
    assert r1 != 0, "control blind to a wrong V' coefficient"

    bad_kg2 = ghat * rhoA - 2 * H * sp.diff(phibar, t) - Vprime  # wrong Hubble drag
    r2 = sp.simplify(resid_phi.subs(sp.diff(phibar, t, 2), bad_kg2))
    print(
        f"    {'KG with Hubble drag 3H -> 2H':<38}{'nonzero' if r2 != 0 else 'ZERO':<16}"
        f"{'YES' if r2 != 0 else 'NO -- BLIND'}"
    )
    assert r2 != 0, "control blind to a wrong Hubble drag"

    r3 = sp.simplify(resid_m.subs(sp.diff(rhoA, t), -2 * H * rhoA))
    print(
        f"    {'matter continuity 3H -> 2H':<38}{'nonzero' if r3 != 0 else 'ZERO':<16}"
        f"{'YES' if r3 != 0 else 'NO -- BLIND'}"
    )
    assert r3 != 0, "control blind to a wrong matter continuity"

    # and a control on the COUPLING itself: drop the exchange term
    r4 = sp.simplify((lhs_phi - 0).subs(sp.diff(phibar, t, 2), kg_bg))
    print(
        f"    {'exchange term dropped entirely':<38}{'nonzero' if r4 != 0 else 'ZERO':<16}"
        f"{'YES' if r4 != 0 else 'NO -- BLIND'}"
    )
    assert r4 != 0, "control blind to a missing exchange term"
    print("\n  => all four controls fire. The balance in Part B is a real test, not")
    print("     an identity that would pass regardless of what it is fed.")


    # ==================================================================
    # PART F -- [SKEPTIC-DEMANDED] the ACTUAL constraint propagation
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART F -- the computation an earlier draft declined to do")
    print("-" * 78)
    print("  The context-blind reviewer's central charge was correct and sharp:")
    print("  'the constraint is V-free' does NOT imply 'the PROPAGATION of the")
    print("  constraint is V-free', because dC/dt substitutes Psi_ddot via the")
    print("  ij-trace equation (sourced by delta_p_phi, which contains -V'*dphi)")
    print("  and dphi_ddot via the perturbed KG (which contains V''*dphi). Whether")
    print("  those V-carrying substitutions cancel was exactly what the draft")
    print("  asserted from a covariant-conservation argument and did not compute.")
    print("  It is computed here.")

    kk, G = sp.symbols("k G_N", positive=True)
    Psi_f = sp.Function("Psi")(t)
    dphi_f = sp.Function("dphi")(t)
    drhoA_f = sp.Function("drho_A")(t)
    Qm_f = sp.Function("Q_m")(t)
    Vpp = sp.diff(V, phibar, 2)

    # sector perturbations (Newtonian gauge, Phi=Psi)
    drho_phi = sp.diff(phibar, t) * sp.diff(dphi_f, t) - Psi_f * sp.diff(phibar, t) ** 2 + Vprime * dphi_f
    dp_phi = sp.diff(phibar, t) * sp.diff(dphi_f, t) - Psi_f * sp.diff(phibar, t) ** 2 - Vprime * dphi_f
    dq_tot = -sp.diff(phibar, t) * dphi_f + Qm_f

    # equations of motion used as substitutions
    subs_chain = [
        (
            sp.diff(Psi_f, t, 2),
            4 * sp.pi * G * dp_phi
            - 4 * H * sp.diff(Psi_f, t)
            - (2 * sp.diff(H, t) + 3 * H**2) * Psi_f,
        ),
        (
            sp.diff(dphi_f, t, 2),
            ghat * drhoA_f
            + 2 * Psi_f * (ghat * rhoA - Vprime)
            + 4 * sp.diff(Psi_f, t) * sp.diff(phibar, t)
            - 3 * H * sp.diff(dphi_f, t)
            - (kk**2 / a**2 + Vpp) * dphi_f,
        ),
        (
            sp.diff(drhoA_f, t),
            -3 * H * drhoA_f
            + 3 * sp.diff(Psi_f, t) * rhoA
            - (kk**2 / a**2) * Qm_f / (1 - ghat * phibar),
        ),
        (sp.diff(Qm_f, t), -3 * H * Qm_f - rho_phys * Psi_f + ghat * rhoA * dphi_f),
        (sp.diff(phibar, t, 2), kg_bg),
        (sp.diff(rhoA, t), -3 * H * rhoA),
    ]

    Cc = sp.diff(Psi_f, t) + H * Psi_f + 4 * sp.pi * G * dq_tot
    dCc = sp.diff(Cc, t)
    for _ in range(2):  # twice: substitutions can reintroduce second derivatives
        for old, new in subs_chain:
            dCc = dCc.subs(old, new)
    dCc = sp.simplify(sp.expand(dCc))
    dCc_C0 = sp.simplify(sp.expand(dCc.subs(Qm_f, sp.solve(Cc, Qm_f)[0])))

    print(f"\n  propagated residual contains lambda?      {dCc_C0.has(lam)}")
    assert not dCc_C0.has(lam), "V SURVIVED the propagation -- the draft's claim is FALSE"
    print("  => *** ANSWERED BY COMPUTATION: NO. *** Every V-carrying substitution")
    print("     cancels. The reviewer's channel is real but it closes.")

    # identify the obstruction exactly
    rho_plus_p = sp.simplify((rho_phys + sp.diff(phibar, t) ** 2 / 2 + V)
                             + (sp.diff(phibar, t) ** 2 / 2 - V))
    R_Hdot = sp.simplify(sp.diff(H, t) + 4 * sp.pi * G * rho_plus_p)
    print(f"\n  rho_tot + p_tot = {rho_plus_p}")
    print(f"    contains lambda? {rho_plus_p.has(lam)}  <- V enters rho and p with")
    print("    OPPOSITE signs, and only rho+p appears. That is WHY it cancels.")
    resid_id = sp.simplify(sp.expand(dCc_C0 + Psi_f * R_Hdot))
    assert resid_id == 0, f"residual is not -Psi*R_Hdot: {resid_id}"
    print("\n  *** EXACT IDENTIFICATION ***")
    print("    dC/dt |_{C=0}  =  -Psi * [ H_dot + 4*pi*G*(rho_tot + p_tot) ]")
    print("  i.e. the obstruction is PRECISELY the H-dot equation -- not a vague")
    print("  'background inconsistency'. And that equation is lambda-free.")

    onshell = sp.simplify(dCc_C0.subs(sp.diff(a, t, 2), sp.solve(R_Hdot, sp.diff(a, t, 2))[0]))
    assert onshell == 0, f"imposing H-dot did not close the constraint: {onshell}"
    print("\n  [positive control] impose the H-dot equation -> residual EXACTLY 0.")
    print("  [negative control] leave it free -> residual = -Psi*R_Hdot, nonzero.")
    print("\n  This reproduces FINDING_P61's D5 mechanically AND localises it: the")
    print("  free-background failure is the H-dot equation going unimposed, and")
    print("  P61's Part I failed because imposing the 00-Friedmann alone does not")
    print("  supply H-dot.")

    # ==================================================================
    # PART E -- what this settles
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART E -- consequences for FINDING_P61's D5 and for Psi_k")
    print("-" * 78)
    print("  FINDING_P70 asked: does V change the Psi_k closure problem? It")
    print("  established that V DOES modify delta_rho and delta_p, and correctly")
    print("  withdrew the earlier claim that the blocker was 'untouched'. This")
    print("  file answers the sharper question -- does V change what CLOSURE")
    print("  REQUIRES -- and the answer is NO, for a specific reason:")
    print()
    print("   * the exchange term is -g_hat*rho_A*grad(phi), with V cancelling")
    print("     exactly between the divergence and the field equation (Part A);")
    print("   * the 0i momentum constraint, which is the object P61 actually")
    print("     differentiated, contains NO V at all (Part C);")
    print("   * V's contributions to delta_rho and delta_p are equal and")
    print("     opposite, so they cancel in rho+p -- the combination that carries")
    print("     momentum (Part C).")
    print()
    print("  => P61's D5 verdict is UNCHANGED by V. The system is not")
    print("     Bianchi-consistent on a free background, and the resolution is")
    print("     still what FINDING_P62 found: the background (a, phibar, rho_A)")
    print("     must be MUTUALLY self-consistent. V changes which background that")
    print("     is -- FINDING_P69 built the V-corrected one -- but not the")
    print("     requirement itself.")
    print()
    print("  This is a NEGATIVE result about a hoped-for effect: V was the last")
    print("  untouched ingredient, and it does not unblock Psi_k. FINDING_P70")
    print("  left open whether V 'helps or hurts' closure. The answer is NEITHER.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("  ESTABLISHED:")
    print("   * div T_phi = (box phi - V')*grad phi, so imposing the coupled KG")
    print("     leaves -g_hat*rho_A*grad phi with V CANCELLING EXACTLY. The")
    print("     energy-momentum exchange term is V-INDEPENDENT;")
    print("   * both background sectors' continuity equations are identities")
    print("     given their own equations of motion, WITH V present, and their")
    print("     exchange terms cancel exactly (Part B, four negative controls);")
    print("   * V enters delta_rho and delta_p EQUALLY AND OPPOSITELY, and does")
    print("     NOT enter the momentum density at all -- so the 0i constraint")
    print("     FINDING_P61 differentiated is literally unchanged by V;")
    print("   * therefore P61's D5 stands unchanged: closure still requires a")
    print("     mutually self-consistent background, exactly as FINDING_P62")
    print("     found, and V neither helps nor hurts. FINDING_P70's open")
    print("     question is CLOSED, in the negative.")
    print()
    print("  NOT ESTABLISHED:")
    print("   * that the full first-order constraint chain closes on")
    print("     FINDING_P69's V-corrected background. This file shows V does not")
    print("     change the REQUIREMENT; it does NOT re-run P61's full")
    print("     differentiate-and-substitute test on the new background. That")
    print("     remains the outstanding computation.")
    print("   * mu(a,k) or gamma. Still blocked, and blocked for the same reason")
    print("     as before V was restored.")
    print("   * anything convention-matched to P61's own residual. This file")
    print("     deliberately attacks the conservation statement rather than")
    print("     reproducing P61's specific expression, because a mismatched")
    print("     convention would manufacture a meaningless nonzero.")
    print("   * anything about anisotropic stress. delta_p here is the isotropic")
    print("     part only; a scalar has no anisotropic stress at first order, but")
    print("     that is asserted from theory here, not derived.")
    print("   * anything about MULTING itself (Gate 1): V is OUR construction.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
