"""P33 -- a matter-sector functional-form observation: MULTING's own
monopole coupling, once supplemented by a standard (assumed, not sourced)
free-particle kinetic term, has the same algebraic form as the matter-sector
piece of a conformally-coupled scalar-tensor theory.

CORRECTED 2026-08-14, after context-blind skeptic review, same day. FIVE
real issues fixed -- this is a genuine downgrade of the finding's central
claim, not just framing:
  (1) The "-m*c kinetic term ... verified this session by direct re-read of
      two_field_action_closure.py" claim was FALSE. Independently
      re-confirmed before accepting the skeptic's correction: grepped the
      actual source file for any gravitational-sector or matter-kinetic
      content -- ZERO matches. two_field_action_closure.py contains ONLY
      the scalar field's own kinetic term (1/2)(d phi)^2 and the worldline
      INTERACTION terms; no standalone "-m*c*int(dtau)" term is written
      down anywhere. The "-m*c" piece is a standard, textbook-obvious
      assumption THIS FINDING SUPPLIES (any sensible relativistic particle
      needs one), not something read from the file. Fixed: explicitly
      labeled as a supplied assumption, not a re-verified fact.
  (2) "Reduces exactly to the known flat-space form" implied the source's
      own bracket produces this. It does not -- the source's own bracket
      is "[g*m_i + p_i . grad]phi", holding BOTH monopole and dipole terms
      together; "the known flat-space form" this script covariantizes is
      P33's OWN constructed sum (assumed kinetic + monopole interaction
      only), not literally what is in the file. Fixed: language corrected
      to say this reduces to THIS FINDING's OWN constructed flat-space
      form, not "the" flat-space form as if unique/sourced.
  (3) THE CONSEQUENTIAL ONE -- the "literature-grounded classification"
      claim overreached. Independently re-verified before accepting:
      grepped two_field_action_closure.py for ANY gravitational-sector
      content (Einstein-Hilbert term, Ricci scalar, metric determinant) --
      ZERO matches, confirming the skeptic's point. "Jordan frame" and
      "Einstein frame" are two DESCRIPTIONS OF ONE FULLY-SPECIFIED THEORY
      whose data includes the metric's OWN gravitational action -- MULTING's
      action, as reconstructed and worked with throughout this entire
      project, has NO gravitational sector specified anywhere, not even
      implicitly named as "standard GR". Importing the literature's known
      consequence ("the metric's own field equations remain standard GR")
      is therefore a statement about the CITED PAPER'S theory, which DOES
      have both frames properly defined via an Einstein-Hilbert action --
      NOT a statement that has been established for MULTING. The matter-
      sector FUNCTIONAL-FORM match (m_eff(phi) ~ A(phi)) is real and
      survives; the imported GRAVITATIONAL consequences do not, without an
      ADDITIONAL, UNVERIFIED assumption (that MULTING's own gravitational
      sector, wherever it is specified, is standard, unmodified GR) that
      this finding does not establish. Fixed: downgraded throughout,
      title changed, VERDICT rewritten.
  (4) Evidence-marking conflated "the quote is accurate" with "the quote is
      evidence about MULTING." The arXiv:1804.07180 quote is [VERIFIED-
      WEBFETCH] as an accurate transcription of THAT PAPER's own theory --
      it is NOT thereby verified evidence ABOUT MULTING, since MULTING has
      not been shown to BE an instance of the class that quote describes
      (see point 3). Fixed: marker split explicitly.
  (5) SYMPY-TAUTOLOGY REGRESSION -- P32's own corrected script (built
      earlier the SAME DAY) explicitly added the disclaimer "the
      substantive claim is established by reading two_field_action_closure.py,
      not by sympy arithmetic" after its own skeptic review caught the same
      pattern. This script did NOT carry that lesson forward despite being
      built minutes later -- a real, avoidable regression, not a new
      mistake. Fixed: same disclaimer now added here.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def total_monopole_action_density(g, m, c, phi):
    """This finding's OWN constructed sum: a SUPPLIED, standard relativistic
    free-particle kinetic term (-m*c per dtau -- NOT present anywhere in
    two_field_action_closure.py, independently re-confirmed by grep before
    this correction) PLUS the already-established interaction term (+g*m*phi,
    genuinely present in the source). This is P33's own constructed object,
    not a term-for-term transcription of the source's own bracket (which
    also contains the separate dipole term, scoped out here)."""
    kinetic_assumed = -m * c
    interaction_from_source = g * m * phi
    return kinetic_assumed + interaction_from_source


def effective_mass_factor(total_density, m, c):
    """Factor the total density as -m*c*[effective mass factor]. This is
    elementary algebraic distribution, not an independent verification of
    any physics claim -- the substantive claims are about what IS and IS
    NOT present in the source action (see module docstring), established
    by reading the file, not by this arithmetic."""
    return sp.simplify(-total_density / (m * c))


def main():
    g, m, phi, c, alpha = sp.symbols("g m phi c alpha", positive=False)

    print("=" * 78)
    print("P33 -- matter-sector functional-form observation (CORRECTED)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[STEP 1] This finding's OWN constructed total (NOT a term-for-term")
    print("  transcription of the source action -- the -m*c kinetic term is a")
    print("  SUPPLIED, standard assumption, absent from two_field_action_closure.py")
    print("  (independently re-confirmed by grep -- zero matches for any matter")
    print("  kinetic term in that file):")
    total = total_monopole_action_density(g, m, c, phi)
    print(f"  S_total/dtau = -m*c + g*m*phi = {total}")

    print("\n[STEP 2] Algebraic distribution (elementary, not independent")
    print("  verification -- CONSISTENT WITH CONSTRUCTION, not 'confirmed'):")
    eff_factor = effective_mass_factor(total, m, c)
    print(f"  effective mass factor = {eff_factor}")
    m_eff = m * eff_factor
    print(f"  m_eff(phi) = m * [{eff_factor}] = {sp.expand(m_eff)}")

    consistency = sp.simplify(-m * c * eff_factor - total)
    print(f"  Consistency check (trivial distribution, should be 0): {consistency}")
    assert consistency == 0

    print("\n[STEP 3] Covariant form of THIS FINDING's OWN constructed sum (dtau ->")
    print("  proper time along a curved-spacetime worldline) -- reduces to THIS")
    print("  finding's own flat-space construction, NOT to 'the' flat-space form of")
    print("  the source's own bracket (which also has the separate dipole term,")
    print("  scoped out, per FINDING_P32's own established caveat):")
    print("  S_i = -c * int(dtau_curved) * m_eff(phi(x_i)),   m_eff(phi) = m*(1 - (g/c)*phi)")
    print("  This is a scalar (covariant) action with the FUNCTIONAL FORM of a")
    print("  mass-varying particle -- the SAME matter-sector form conformally-coupled")
    print("  scalar-tensor theories have IN THEIR EINSTEIN FRAME.")

    print("\n[STEP 4] Coefficient match to the standard A(phi) form (symbol-matching")
    print("  on a linear equation, not a substantive computation):")
    A_standard = 1 + alpha * phi
    alpha_identified = sp.solve(sp.Eq(m_eff / m, A_standard), alpha)[0]
    print("  Standard form: A(phi) = 1 + alpha*phi")
    print(f"  m_eff/m = {sp.simplify(m_eff / m)}")
    print(f"  Matched alpha = {alpha_identified}")
    assert alpha_identified == -g / c

    print("\n[STEP 5] What this match does NOT license (CORRECTED after skeptic")
    print("  review -- the consequential catch):")
    print("  'Jordan frame' and 'Einstein frame' are two DESCRIPTIONS OF ONE FULLY-")
    print("  SPECIFIED THEORY whose data includes the metric's OWN gravitational")
    print("  action. two_field_action_closure.py has NO gravitational-sector content")
    print("  anywhere (independently re-confirmed by grep: zero matches for any")
    print("  Einstein-Hilbert / Ricci / metric-determinant term). The quote below")
    print("  (arXiv:1804.07180 eq. 1) is [VERIFIED-WEBFETCH] as an accurate")
    print("  transcription of THAT PAPER'S OWN theory -- it is NOT thereby verified")
    print("  evidence ABOUT MULTING, since MULTING has not been shown to BE an")
    print("  instance of the class that quote describes:")
    print('  "The SM degrees of freedom {psi} move on geodesics determined by')
    print('   the Jordan-frame metric g_munu = A^2(chi) * g_munu_tilde"')
    print("  Importing 'the metric field equations remain standard GR' as an")
    print("  established fact ABOUT MULTING requires an ADDITIONAL, UNVERIFIED")
    print("  assumption this finding does not establish: that MULTING's own")
    print("  gravitational sector (wherever specified) is standard, unmodified GR.")

    print("\n" + "=" * 78)
    print("VERDICT -- CORRECTED after context-blind skeptic review, same day")
    print("=" * 78)
    print("MULTING's own monopole coupling, IF supplemented by a standard (assumed,")
    print("not sourced) free-particle kinetic term, has the SAME MATTER-SECTOR")
    print("FUNCTIONAL FORM as conformally-coupled matter would have in the Einstein")
    print("frame of a standard scalar-tensor theory -- alpha=-g/c. This is a real,")
    print("verified structural observation. It does NOT establish that MULTING IS")
    print("such a theory, since MULTING's own action (as reconstructed throughout")
    print("this project) specifies no gravitational sector at all -- the literature's")
    print("consequences about the metric's OWN field equations describe the CITED")
    print("PAPER's theory, not MULTING, until an explicit, separately-justified")
    print("assumption about MULTING's own gravitational sector is added. This finding")
    print("narrows to: a matter-sector functional-form match, worth recording, NOT a")
    print("literature-grounded classification of MULTING itself. FINDING_P32's own")
    print("Part B (the definitional-mismatch argument, which needs no such assumption)")
    print("remains the stronger, better-grounded point -- this finding is a smaller,")
    print("more conditional supplement to it, not an independent strengthening.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
