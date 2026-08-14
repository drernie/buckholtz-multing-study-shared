"""P36 -- third step of the covariant-completion campaign (see
PLAN_final_goal_20260814.md), the first to address kappa (dipole sector)
directly. Does kappa enter ANY of P34's background or P35's static
two-body Delta_G calculation, the way g does?

CORRECTED 2026-08-14, after context-blind skeptic review, same day. This
was the MOST SEVERE correction of the whole campaign so far -- nearly
every load-bearing claim in the original "connecting" section was found
unestablished, not just overstated. Summary of what changed:
  (1) dipole_layer_potential_jump_standard_result() returned a hardcoded
      True with ZERO computation, then main() called this an "independent
      cross-check via a different argument." That was false -- it is a
      CITATION (the 2026-08-10 result matches a standard textbook name),
      not a verification. The variable name itself
      ("fact_confirmed_independently") narrated a check that never
      happened. Fixed: function removed, replaced with an honest citation
      note in the docstring/prints, no claimed independent verification.
  (2) THE CONSEQUENTIAL ONE: the original script silently extended the
      2026-08-10 double-layer result -- proven for ONE specific
      configuration, dipoles radially aligned FROM A SINGLE COMMON
      CENTER, arranged on a shell around that center -- to TWO different
      geometries without justification: (a) P34's HOMOGENEOUS FRW
      background, which has NO privileged center at all (there is no
      well-defined "radial direction" for a homogeneous distribution --
      "radially aligned from a common center, distributed isotropically"
      is close to incoherent read literally); (b) a point/extended
      source's own INTERNAL kappa-content (P35's M), which requires
      ASSUMING that content is organized as radially-aligned nested
      shells -- an unmotivated, physically implausible assumption for
      real matter (thermal randomization would give RANDOM orientation,
      not coherent radial alignment). Fixed: both claims withdrawn to
      "not established by this finding," the generalization gap stated
      explicitly.
  (3) Related: the original text conflated TWO DIFFERENT theorems that
      two_field_action_closure.py's own docstring actually states
      SEPARATELY -- "the radial-dipole average is a double layer" (the
      2026-08-10 shell result, Green's-identity-based, requires coherent
      radial alignment) and "the random average is zero" (isotropic
      orientation averaging, a completely different mechanism, requires
      NO alignment at all, just randomness). This script only ever
      examined the double-layer one; citing it to explain the "random
      average" sentence was a category error. Fixed: the two arguments
      are now kept explicitly separate, and only the double-layer one
      (the one actually examined) is used.
  (4) "The two sectors are each visible to exactly the channel the other
      is blind to" overreached -- only ONE pair of channels was actually
      examined (P25's WEP test vs. this finding's own, now-narrowed,
      smooth-source argument), not a general duality. Fixed: downgraded
      to the two specific, narrower one-way statements that are actually
      supported.
  (5) The multipole exterior-solution check (Step 2) verifies a KINEMATIC
      fact (which r-powers solve the source-free equation for a given
      multipole order) -- it says nothing about which multipoles a given
      PHYSICAL source actually excites, and kappa (being intrinsically a
      DIPOLE-type source) does not naturally have a monopole moment to
      begin with, so "smooth sources are monopole-dominated" was the
      wrong framing for this specific sector. Fixed: reframed as a
      general mathematical fact only, with its actual (limited)
      relevance stated honestly.

WHAT SURVIVES (see corrected VERDICT): the 2026-08-10 double-layer result
itself, for its own specific configuration, is unaffected (that finding
was independently numerically verified, positive control passed, not
touched by this correction). P25's WEP composition-dependence result is
unaffected. What does NOT survive is this finding's own attempt to
connect them to P34/P35 -- that connection needs a real, separate
argument this finding did not supply.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def multipole_exterior_solution_check(ell_values):
    """Genuinely computed (sympy): for each multipole order l, verify
    r^(-(l+1)) solves the exterior (source-free) radial Laplace equation
    (1/r^2)*d/dr(r^2*df/dr) - l(l+1)/r^2*f = 0. This is a KINEMATIC fact
    about which radial falloffs are mathematically admissible for a
    field of definite multipole order l outside a bounded source region
    -- l=0: 1/r; l=1: 1/r^2; l=2: 1/r^3. CORRECTED: this does NOT by
    itself establish which multipoles any given physical source excites,
    and kappa's own sourcing mechanism is intrinsically dipole-type (no
    natural monopole moment), so citing this as evidence that "smooth
    sources are monopole-dominated, kappa is parametrically suppressed"
    overstated what this kinematic fact actually shows."""
    r = sp.Symbol("r", positive=True)
    results = {}
    for ell in ell_values:
        f = r ** (-(ell + 1))
        radial_laplacian = sp.diff(r**2 * sp.diff(f, r), r) / r**2
        residual = sp.simplify(radial_laplacian - ell * (ell + 1) / r**2 * f)
        results[ell] = (ell + 1, residual)
    return results


def main():
    print("=" * 78)
    print("P36 -- kappa's channel visibility (CORRECTED, substantially narrowed)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[STEP 1] Cite (NOT an independent check -- CORRECTED, the original")
    print("  claim to have 'independently cross-checked' this via textbook")
    print("  electrostatics was itself unverified, a bare 'return True' with no")
    print("  computation): FINDING_dipole_shell_is_a_double_layer.md (2026-08-10,")
    print("  numerically verified, positive control passed -- monopole shell")
    print("  exactly recovers Newton's shell theorem, C_2=1). Its result, for ONE")
    print("  SPECIFIC configuration -- dipoles radially aligned FROM A SINGLE")
    print("  COMMON CENTER, arranged on a shell around that center: EXACTLY ZERO")
    print("  force (all derivatives vanish) everywhere off the shell. This matches")
    print("  the standard textbook 'double layer' / dipole-sheet identity in")
    print("  electrostatics -- a citation of a known name, not a new verification.")

    print("\n[STEP 2] Multipole exterior-solution check (sympy, genuinely computed --")
    print("  a KINEMATIC fact about admissible falloffs only, CORRECTED not to")
    print("  overclaim physical relevance):")
    results = multipole_exterior_solution_check([0, 1, 2])
    for ell, (power, residual) in sorted(results.items()):
        print(f"  l={ell}: r^-{power} solves the radial equation (residual={residual})")
        assert residual == 0, f"r^-(l+1) does not solve the radial equation for l={ell}"
    print("  This shows WHICH falloff each multipole order WOULD have IF excited --")
    print("  it does NOT show which multipoles a given physical source excites, and")
    print("  kappa (a dipole-type source) has no natural monopole moment to begin")
    print("  with, so 'smooth sources are monopole-dominated' is the wrong framing")
    print("  for this specific sector.")

    print("\n[STEP 3] CORRECTED -- the generalization gap, the most consequential")
    print("  fix. The 2026-08-10 result (Step 1) is proven for radially-aligned")
    print("  dipoles on a shell around ONE COMMON CENTER. Two different, UNPROVEN")
    print("  extensions were originally claimed:")
    print("  (a) P34's HOMOGENEOUS FRW background has NO privileged center -- there")
    print("      is no well-defined single 'radial direction' for a homogeneous")
    print("      distribution. 'Radially aligned, distributed isotropically' does")
    print("      not describe a coherent configuration this shell result covers.")
    print("      two_field_action_closure.py's own docstring separately invokes a")
    print("      DIFFERENT argument for this case -- 'the random average is zero'")
    print("      (isotropic orientation averaging, NOT the double-layer/Green's-")
    print("      identity mechanism) -- a genuinely different theorem this finding")
    print("      did NOT examine. Conflating the two was a real error, corrected.")
    print("  (b) P35's point source M's own INTERNAL kappa-content being organized")
    print("      as radially-aligned nested shells is an ADDITIONAL, UNMOTIVATED")
    print("      assumption -- real matter's dipole content, if anything, would be")
    print("      thermally randomized (the random-average case), not coherently")
    print("      radially aligned. NOT established here.")
    print("  CORRECTED CONCLUSION: whether kappa is invisible to P34's background")
    print("  or P35's static Delta_G is an OPEN QUESTION -- this finding does not")
    print("  establish it either way for those two specific channels.")

    print("\n[STEP 4] Cite, do not re-derive: FINDING_P25_wep_eotvos_kill_gate.md")
    print("  (2026-08-13, sympy-verified, skeptic-corrected). Its result, UNCHANGED")
    print("  by this correction: the k-sector DOES produce a genuine, COMPOSITION-")
    print("  DEPENDENT term in a laboratory Eotvos-type test, because such a test")
    print("  compares DIFFERENT TEST BODIES' own K_i/M_i ratios in the SAME")
    print("  external field. P23 already showed the g-sector is WEP-blind (universal")
    print("  coupling). CORRECTED: this establishes only ONE one-way statement (kappa")
    print("  IS visible via WEP, g is NOT) -- NOT the general duality originally")
    print("  claimed ('each visible to exactly the channel the other is blind to'),")
    print("  which required Step 3's now-withdrawn claims to complete the other half.")

    print("\n" + "=" * 78)
    print("VERDICT (CORRECTED after skeptic review, same day -- substantially narrowed)")
    print("=" * 78)
    print("What survives, unaffected by this correction: the 2026-08-10 double-layer")
    print("result for ITS OWN specific configuration (radially-aligned shell around")
    print("one center), and P25's WEP composition-dependence result. WITHDRAWN: any")
    print("claim that kappa is 'structurally invisible' to P34's background or P35's")
    print("static Delta_G -- extending the shell result to those two configurations")
    print("required additional, unmotivated assumptions (a privileged center for a")
    print("homogeneous background; coherent radial alignment inside ordinary matter)")
    print("that this finding did not establish. WITHDRAWN: the 'each visible to")
    print("exactly the channel the other is blind to' duality -- only kappa's WEP-")
    print("visibility half is actually supported; g's own smooth-source-visibility")
    print("was asserted, not re-examined here for cancellations of its own. Whether")
    print("kappa enters the cosmological/two-body chain this campaign is building")
    print("remains genuinely OPEN -- not resolved in either direction by this")
    print("finding, contrary to its original conclusion.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
