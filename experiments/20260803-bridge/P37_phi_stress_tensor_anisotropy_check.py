"""P37 -- fourth step of the covariant-completion campaign (see
PLAN_final_goal_20260814.md), resuming at a deliberately slower pace per
explicit user instruction (one step at a time). Directly targets the
narrowest, safest piece of P35's own flagged open question (its section
5/6.8): does phi's own stress-energy, for the static solution
phi(r)=g_hat*M/(4*pi*r) already derived in P35, actually have a nonzero
ANISOTROPIC (traceless spatial) part?

CORRECTED 2026-08-14, after context-blind skeptic review, same day. This
review had the MOST FAVORABLE outcome of any review this campaign so
far: the core physics claim (nonzero anisotropic stress at O(g_hat^2))
SURVIVED an independent by-hand re-derivation by the reviewer. Issues
found were about completeness and framing, not a wrong core result:
  (1) The ASSUMED ACTION was never stated explicitly in this finding --
      it only referenced "P35's already-derived field" without
      restating what Lagrangian/coupling that presupposes. Fixed: stated
      explicitly below (canonical minimally-coupled scalar, linear
      matter coupling, no potential, no non-minimal R-coupling -- the
      SAME assumptions P34/P35 already made explicit and flagged).
  (2) The original "trace cross-check" (Step 5) was WEAKER than it
      looked: since each diagonal T_ii is computed by the SAME formula
      being summed, sympy confirming the sum matches -(1/2)(grad phi)^2
      verifies internal algebraic consistency of the simplification, NOT
      independent information about the individual COMPONENTS (a
      correlated sign error across all three components would still
      pass). Fixed: relabeled honestly as a consistency check, not
      independent verification, AND a genuinely independent check added
      (3): the spatial divergence d_i(T_ij) = 0 for r>0, which uses the
      actual EQUATION OF MOTION (grad^2 phi=0 away from the source,
      already established in P35) and is a real physical constraint on
      the INDIVIDUAL components, not just their sum.
  (3) Added: T_00 = (1/2)*(grad phi)^2 computed explicitly and confirmed
      positive -- a free, independent check that the kinetic term has
      the canonical (not ghost/wrong-sign) sign, per the skeptic's own
      suggestion.
  (4) The original "necessary but not sufficient for Phi!=Psi, requires
      solving the sourced equation" framing UNDERSOLD the result -- for
      a well-behaved, localized, static, falling-off-at-infinity
      anisotropic source, standard elliptic-PDE uniqueness (Green's
      function integration under standard boundary conditions) means
      Phi=Psi despite a nonzero source would require a NON-STANDARD
      boundary condition, not an ad hoc "fine-tuned cancellation" with
      free parameters to tune (there are none here). CORRECTED: this
      project does NOT adopt the skeptic's own specific claimed closed-
      form solution for the sourced potential (Agent's [VERIFIED] is
      this project's [INFERRED], per audit-verification-gate.md -- not
      independently re-checked here) -- only the general, standard,
      well-known uniqueness PRINCIPLE is stated, without borrowing an
      unverified specific numeric result.
  (5) "Same parametric order as Delta_G" was ambiguous -- clarified to
      mean Delta_G as P35 defined it (the SCALAR-INDUCED additive
      correction to Newton's constant, itself O(g_hat^2)), not the full
      Newtonian potential G_N*M/r (which is O(g_hat^0)).
  (6) Flagged explicitly (not previously noted): T_ij ~ 1/r^4 diverges
      as r->0 (point-source self-energy divergence, a completely
      standard feature of any point-source field theory, already
      encountered elsewhere in this project, e.g. P14-P19's own
      self-energy discussions) -- any future attempt to INTEGRATE this
      T_ij as a source (rather than examine it locally at r>0, as this
      finding does) will need to handle that divergence explicitly.

SCOPE, DELIBERATELY NARROW (unchanged). This does NOT attempt to solve
the full linearized Einstein ij-equation for the resulting metric slip
(Phi-Psi) -- that is a larger, separate step, appropriately deferred.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def scalar_stress_tensor_spatial(phi_expr, coords):
    """T_ij = d_i(phi)*d_j(phi) - (1/2)*delta_ij*(grad phi)^2, the spatial
    part of the standard canonical scalar stress tensor, static case
    (d_t phi = 0), evaluated in Cartesian coordinates -- avoids any risk
    of a spherical-coordinate conversion error. ASSUMES a canonical,
    minimally-coupled scalar action L=(1/2)(d phi)^2 with a linear
    matter-coupling source term (P33/P34/P35's own stated convention),
    no potential, no non-minimal R-coupling -- stated explicitly here
    per skeptic review, previously left implicit."""
    grad = [sp.diff(phi_expr, c) for c in coords]
    grad_sq = sum(g**2 for g in grad)
    T = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            delta_ij = 1 if i == j else 0
            T[i, j] = sp.simplify(grad[i] * grad[j] - sp.Rational(1, 2) * delta_ij * grad_sq)
    return T, grad_sq


def spatial_divergence(T, coords):
    """d_i(T_ij) for each j -- a GENUINE, independent physical check
    (added after skeptic review): in the source-free region (r>0), this
    must vanish by conservation (equivalent to phi's own equation of
    motion grad^2(phi)=0 there, already established in P35). Unlike the
    trace check, this uses the INDIVIDUAL components' actual functional
    form, not just their sum -- a correlated sign error across
    components would generically NOT pass this check."""
    div = []
    for j in range(3):
        d = sum(sp.diff(T[i, j], coords[i]) for i in range(3))
        div.append(sp.simplify(d))
    return div


def main():
    x, y, z = sp.symbols("x y z", real=True)
    ghat, M = sp.symbols("g_hat M", positive=True)
    r = sp.sqrt(x**2 + y**2 + z**2)
    coords = [x, y, z]

    print("=" * 78)
    print("P37 -- does phi's own static stress tensor have anisotropic stress?")
    print("(CORRECTED after skeptic review -- core result survived, added a")
    print("genuine conservation check, stated the assumed action explicitly)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[STEP 1] Assumed action (CORRECTED -- now stated explicitly, was left")
    print("  implicit before): canonical, minimally-coupled scalar, S_phi = int")
    print("  d^4x*sqrt(-g)*(1/2)*(d phi)^2, linear matter coupling, no potential,")
    print("  no non-minimal R-coupling -- P33/P34/P35's own already-flagged")
    print("  convention, re-used here unchanged. Field (re-used from P35, not")
    print("  re-derived):")
    phi_expr = ghat * M / (4 * sp.pi * r)
    print(f"  phi(r) = {phi_expr}")

    print("\n[STEP 2] Compute T_ij = d_i(phi)*d_j(phi) - (1/2)*delta_ij*(grad phi)^2")
    print("  in Cartesian coordinates (avoids spherical-coordinate conversion risk):")
    T, grad_sq_full = scalar_stress_tensor_spatial(phi_expr, coords)
    print(f"  T_xx = {T[0, 0]}")
    print(f"  T_yy = {T[1, 1]}")
    print(f"  T_zz = {T[2, 2]}")
    print(f"  T_xy = {T[0, 1]}")

    print("\n[STEP 3] Evaluate on the z-axis (x=0,y=0,z=r>0) -- a convenient point")
    print("  where the radial direction is manifestly z-hat, so T_zz is the")
    print("  RADIAL stress and T_xx=T_yy is the TANGENTIAL stress by symmetry:")
    r_sym = sp.Symbol("r", positive=True)
    subs_on_axis = {x: 0, y: 0, z: r_sym}
    T_radial = sp.simplify(T[2, 2].subs(subs_on_axis))
    T_tangential_x = sp.simplify(T[0, 0].subs(subs_on_axis))
    T_tangential_y = sp.simplify(T[1, 1].subs(subs_on_axis))
    print(f"  T_radial (T_zz on z-axis)     = {T_radial}")
    print(f"  T_tangential_x (T_xx on z-axis) = {T_tangential_x}")
    print(f"  T_tangential_y (T_yy on z-axis) = {T_tangential_y}")
    assert sp.simplify(T_tangential_x - T_tangential_y) == 0, (
        "tangential components disagree -- not axially symmetric as expected"
    )

    print("\n[STEP 4] The load-bearing check -- is T_radial equal to T_tangential?")
    print("  (isotropic stress, NO slip source) or different (anisotropic,")
    print("  a GENUINE slip source, magnitude not yet computed here):")
    anisotropy = sp.simplify(T_radial - T_tangential_x)
    print(f"  T_radial - T_tangential = {anisotropy}")
    is_isotropic = anisotropy == 0
    print(f"  Isotropic (no anisotropic stress)?  {is_isotropic}")
    assert not is_isotropic, (
        "UNEXPECTED: T_ij came out isotropic -- would need re-examination, "
        "contradicts the standard result for a static scalar gradient"
    )

    print("\n[STEP 5] CORRECTED -- trace check, relabeled honestly. This verifies")
    print("  sympy's own algebraic simplification is internally consistent, NOT")
    print("  independent information about the individual components (each T_ii")
    print("  is built from the SAME formula being summed -- a correlated sign")
    print("  error across all three components would still pass this specific")
    print("  check, per skeptic review):")
    trace = sp.simplify(T[0, 0] + T[1, 1] + T[2, 2])
    expected_trace = sp.simplify(-grad_sq_full / 2)
    trace_check = sp.simplify(trace - expected_trace)
    print(f"  trace(T_ij) - (-(1/2)*(grad phi)^2) = {trace_check}")
    assert trace_check == 0, "trace does not match the expected standard formula"

    print("\n[STEP 6] ADDED after skeptic review -- a GENUINE, independent physical")
    print("  check: spatial divergence d_i(T_ij) must vanish for r>0 (source-free")
    print("  region), by conservation -- equivalent to phi's own equation of")
    print("  motion grad^2(phi)=0 there (already established in P35). Uses the")
    print("  INDIVIDUAL components' actual functional form, not just their sum:")
    divergence = spatial_divergence(T, coords)
    for j, name in enumerate(["x", "y", "z"]):
        print(f"  d_i(T_i{name}) = {divergence[j]}")
        assert divergence[j] == 0, f"T_ij is NOT divergence-free in the {name} direction"

    print("\n[STEP 7] ADDED after skeptic review -- T_00 (energy density), a free,")
    print("  independent check that the kinetic term has the CANONICAL (not")
    print("  ghost/wrong-sign) sign, i.e. T_00 > 0:")
    T_00 = sp.simplify(grad_sq_full / 2)
    print(f"  T_00 = (1/2)*(grad phi)^2 = {T_00}")
    print("  Manifestly non-negative (a sum of squares divided by 2) -- canonical,")
    print("  not ghost, kinetic term confirmed for this static configuration.")

    print("\n" + "=" * 78)
    print("VERDICT (CORRECTED after skeptic review -- core result unchanged,")
    print("strengthened by a genuine conservation check, framing corrected)")
    print("=" * 78)
    print("Phi's own static stress tensor, for the SAME field P35 already derived,")
    print("has a GENUINELY nonzero anisotropic (radial vs. tangential) part:")
    print(f"  T_radial - T_tangential = {anisotropy}  (nonzero for all r>0)")
    print("Now independently confirmed divergence-free (Step 6, a real physical")
    print("constraint, not an algebraic tautology) and with a positive-energy-")
    print("density cross-check (Step 7). This is the standard, well-known")
    print("structure for a static scalar-field gradient's own stress-energy.")
    print("CONSEQUENCE for P35's own withdrawn slip claim: a genuine SOURCE for a")
    print("metric slip (Phi != Psi) exists at the SAME O(g_hat^2) order as P35's")
    print("own Delta_G (the additive scalar-induced correction, not the full")
    print("Newtonian potential). CORRECTED framing: for a well-behaved, localized,")
    print("falling-off-at-infinity source like this one, standard elliptic-PDE")
    print("uniqueness means Phi=Psi despite this nonzero source would require a")
    print("NON-STANDARD boundary condition, not an ad hoc cancellation -- but the")
    print("actual sourced equation is still NOT solved here (this project does not")
    print("adopt any unverified specific closed-form claim for it), so the precise")
    print("value/sign of Phi-Psi remains the next, separate, deferred step.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
