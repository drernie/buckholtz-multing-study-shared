"""P39 -- sixth step of the covariant-completion campaign (see
PLAN_final_goal_20260814.md), continuing at the deliberately slower,
one-step-at-a-time pace per explicit user instruction. Originally intended
to compare P38's Phi-Psi against FINDING_P22/P31's phenomenological
ceiling on Delta_G. Before doing that numeric comparison, this step checks
whether it is even dimensionally well-posed -- P34 and P35 BOTH explicitly
flagged "a restored, explicit-c, SI-like version matching P21's own
convention" as deferred, not-yet-done future work. This finding does that
check, mechanically (exponent bookkeeping on mass/length/time, not hand
arithmetic), and finds the gap is NOT simply "insert missing c-factors" --
it is a genuine unit-TYPE mismatch that no power of c can bridge.

SOURCE QUOTES (exact, not paraphrased -- provenance for every dimensional
claim below):

FINDING_P21_shared_phi_normalization_constraint.md Sec.1-2:
  "S = int d^4x (1/2)(d phi)^2 + sum_i int dtau [ g*m_i + p_i.grad ] phi(x_i)"
  "Taking g dimensionless (matching kappa's convention) as a working
  assumption ... [phi]_monopole = kg^0 m^2 s^-2 (from g*m*phi = energy)"

FINDING_P33_covariantize_mass_varying_classification.md line 69:
  "m_eff(phi)/m = (c - g*phi)/c = 1 - (g/c)*phi"
  (re-used unchanged by P34: "S_matter = -sum_i int dtau_i * m_i(1-ghat*phi
  (x_i)), ghat:=g/c ... re-used unchanged")

FINDING_P35_static_weak_field_closes_deltaG_loop.md Sec.3-4:
  "Delta_G = ghat^2/(4*pi)"  (an ADDITIVE correction to G_N, i.e. must
  carry G_N's own SI units, m^3 kg^-1 s^-2)

FINDING_P38_metric_slip_from_phi_anisotropic_stress.py Step 7:
  "Phi - Psi = G_N*ghat^2*M^2/(16*pi*r^2)"

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def dmul(a, b):
    """Multiply two physical quantities' dimensions (add exponents)."""
    return tuple(x + y for x, y in zip(a, b, strict=True))


def dpow(a, n):
    """Raise a dimension to a rational power (multiply exponents)."""
    n = sp.Rational(n)
    return tuple(x * n for x in a)


def ddiv(a, b):
    """Divide two dimensions (subtract exponents)."""
    return dmul(a, dpow(b, -1))


def dsub(a, b):
    """Exponent-wise difference (for 'what extra factor bridges a and b')."""
    return tuple(x - y for x, y in zip(a, b, strict=True))


# Dimension = (mass_exp, length_exp, time_exp) in SI base units (kg, m, s).
MASS, LENGTH, TIME = (1, 0, 0), (0, 1, 0), (0, 0, 1)
DIMLESS = (0, 0, 0)


def fmt(d):
    return f"kg^{d[0]} m^{d[1]} s^{d[2]}"


def main():
    print("=" * 78)
    print("P39 -- dimensional consistency audit: does P21's own g (SI, dimension-")
    print("less by stated assumption) connect consistently to P34-P38's own ghat")
    print(":=g/c, all the way through to P38's Phi-Psi? Checked mechanically, not")
    print("by hand, before attempting the planned P22/P31 numeric comparison.")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    c_dim = ddiv(LENGTH, TIME)
    G_N_dim = ddiv(dpow(LENGTH, 3), dmul(MASS, dpow(TIME, 2)))
    energy_dim = dmul(MASS, dpow(ddiv(LENGTH, TIME), 2))

    print("\n[STEP 1] Base SI dimensions (mechanical, not assumed):")
    print(f"  [c]     = {fmt(c_dim)}")
    print(f"  [G_N]   = {fmt(G_N_dim)}   (Newton's constant, SI)")
    print(f"  [energy] = {fmt(energy_dim)}")
    assert c_dim == (0, 1, -1)
    assert G_N_dim == (-1, 3, -2)

    print("\n[STEP 2] P21's own derivation of [phi], quoted verbatim above:")
    print("  g*m*phi = energy, g ASSUMED dimensionless (P21's own stated")
    print("  working assumption, not established elsewhere):")
    g_dimensionless = DIMLESS
    phi_from_p21 = ddiv(energy_dim, dmul(g_dimensionless, MASS))
    print(f"  [phi] = {fmt(phi_from_p21)}")
    assert phi_from_p21 == (0, 2, -2), "does not match P21's own stated m^2/s^2"
    print("  -> matches P21's own stated result (kg^0 m^2 s^-2) exactly.")

    print("\n[STEP 3] P33's own m_eff(phi)/m=1-(g/c)*phi, re-used unchanged by")
    print("  P34/P35/P37/P38 (quoted above). This is a ratio of two masses --")
    print("  m_eff/m -- so (g/c)*phi must be DIMENSIONLESS. Using P21's OWN phi")
    print("  from Step 2 (the SAME phi both findings say they share), what must")
    print("  [g] be for THIS specific requirement to hold?")
    g_required_by_p33 = ddiv(c_dim, phi_from_p21)
    print(f"  [g] required by P33's own formula = {fmt(g_required_by_p33)}")
    is_dimensionless = g_required_by_p33 == DIMLESS
    print(f"  Is this dimensionless (matching P21's own stated assumption)? {is_dimensionless}")
    assert not is_dimensionless, (
        "unexpected: P33's own requirement WOULD match P21's dimensionless "
        "assumption -- re-check the derivation, the claimed tension is not real"
    )
    print("  -> NO. P21's own 'g dimensionless' working assumption and P33's own")
    print("     m_eff/m formula, applied to the SAME phi both findings say they")
    print("     share, are NOT mutually consistent. This was never cross-checked")
    print("     when P33/P34 (2026-08-14) reused P21's ghat:=g/c convention.")

    print("\n[STEP 4] ghat:=g/c (P34's own definition, quoted above) under BOTH")
    print("  candidate readings of [g] -- neither privileged over the other by")
    print("  this audit alone, both checked:")
    ghat_reading1 = ddiv(g_dimensionless, c_dim)  # P21's stated assumption
    ghat_reading2 = ddiv(g_required_by_p33, c_dim)  # P33's own internal requirement
    print(f"  Reading 1 (g dimensionless, per P21):        [ghat] = {fmt(ghat_reading1)}")
    print(f"  Reading 2 (g per P33's own requirement):     [ghat] = {fmt(ghat_reading2)}")

    print("\n[STEP 5] P35's own Delta_G=ghat^2/(4*pi) (quoted above) is presented")
    print("  as an ADDITIVE correction to G_N -- U_total=-mM/r*[G_N+ghat^2/(4pi)]")
    print("  (P35 Sec.3) -- which REQUIRES [ghat^2] to equal [G_N] exactly, not")
    print("  merely be proportional to it. Checked under both readings:")
    ghat2_r1 = dpow(ghat_reading1, 2)
    ghat2_r2 = dpow(ghat_reading2, 2)
    print(f"  [ghat^2] (reading 1) = {fmt(ghat2_r1)}   == [G_N]? {ghat2_r1 == G_N_dim}")
    print(f"  [ghat^2] (reading 2) = {fmt(ghat2_r2)}   == [G_N]? {ghat2_r2 == G_N_dim}")
    assert ghat2_r1 != G_N_dim and ghat2_r2 != G_N_dim, (
        "unexpected: one reading DOES match G_N's units -- the claimed gap "
        "is not real, re-check before writing this up as a finding"
    )
    print("  -> NEITHER reading gives [ghat^2]=[G_N]. FINDING_P35's own additive")
    print("     Delta_G=ghat^2/(4*pi) is not dimensionally G_N-valued under any")
    print("     straightforward reading of g's own units from P21+P33's own text.")

    print("\n[STEP 6] Is this fixable by 'restoring explicit c-factors', as P34")
    print("  Sec.0/Sec.4 and P35 Sec.6 point 4 both characterize the deferred")
    print("  task? Check: is the RESIDUAL gap between [ghat^2] and [G_N] itself")
    print("  proportional to some power of c (dimension (0,1,-1), MASS EXPONENT")
    print("  ALWAYS ZERO)? If the residual has a NONZERO mass exponent, no power")
    print("  of c -- however large or fractional -- can ever bridge it:")
    residual_r1 = dsub(G_N_dim, ghat2_r1)
    residual_r2 = dsub(G_N_dim, ghat2_r2)
    print(f"  [G_N]/[ghat^2] (reading 1) = {fmt(residual_r1)}")
    print(f"  [G_N]/[ghat^2] (reading 2) = {fmt(residual_r2)}")
    mass_exp_r1, mass_exp_r2 = residual_r1[0], residual_r2[0]
    print(f"  mass exponent of residual (reading 1) = {mass_exp_r1}")
    print(f"  mass exponent of residual (reading 2) = {mass_exp_r2}")
    assert mass_exp_r1 != 0 and mass_exp_r2 != 0, (
        "unexpected: residual has zero mass exponent under a reading -- "
        "then a pure power of c WOULD fix it, contradicting the finding below"
    )
    print("  -> Both residuals carry a NONZERO mass exponent -- no power of c can")
    print("     supply that. 'Restore explicit c-factors' (P34/P35's own framing")
    print("     of the deferred task) UNDERSTATES what is actually missing: a")
    print("     genuinely new, MASS-DEPENDENT constant, not a pure c-power.")

    print("\n[STEP 7] Does this propagate into P38's own Phi-Psi formula? Using")
    print("  reading 1 (ghat=g/c, g dimensionless -- P21's own stated assumption,")
    print("  the more standard of the two readings), what is [Phi-Psi] as P38")
    print("  Step 7 literally wrote it (G_N*ghat^2*M^2/(16*pi*r^2))?")
    phi_minus_psi_dim = dsub(dmul(G_N_dim, dmul(ghat2_r1, dpow(MASS, 2))), dpow(LENGTH, 2))
    print(f"  [Phi-Psi] = {fmt(phi_minus_psi_dim)}")
    is_dimensionless_slip = phi_minus_psi_dim == DIMLESS
    print(
        f"  Dimensionless (required -- Phi,Psi are metric perturbations)? {is_dimensionless_slip}"
    )
    assert not is_dimensionless_slip, (
        "unexpected: Phi-Psi came out dimensionless -- the propagated gap "
        "closed somewhere unaccounted for, re-check before writing up"
    )
    print("  -> NOT dimensionless, confirming the gap propagates through P38 as")
    print("     literally written. Worth flagging (not proven, only noted): this")
    print(f"     residual, {fmt(phi_minus_psi_dim)}, has the SAME exponents")
    print("     (kg^1 m^-1 s^0) as FINDING_P17's own already-flagged Omega_phi")
    print("     units mismatch ('kg/m, not dimensionless') -- a striking, but")
    print("     NOT independently established, structural echo. See write-up.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("The 'restore explicit c-factors to match P21's own convention' task,")
    print("explicitly flagged as deferred by BOTH FINDING_P34 (Sec.0, Sec.4 point")
    print("3) and FINDING_P35 (Sec.6 point 4), is NOT a simple bookkeeping step.")
    print("Mechanically checked: P21's own 'g dimensionless' assumption and P33's")
    print("own m_eff/m=1-(g/c)*phi formula, applied to the SAME phi both findings")
    print("say they share, are mutually inconsistent -- and under EITHER reading")
    print("of g's resulting units, ghat^2 does not carry G_N's SI units, and the")
    print("residual gap has a nonzero mass exponent that NO power of c can supply.")
    print("This means: P38's Phi-Psi cannot yet be validly compared, numerically,")
    print("against FINDING_P22/P31's SI-valued Delta_G ceiling -- the originally-")
    print("planned next step for this campaign slot. That comparison remains open,")
    print("blocked on resolving this unit-type gap first, not merely restoring c.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
