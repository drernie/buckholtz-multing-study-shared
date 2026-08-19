"""P60 -- the decisive D1/D2/D3 re-test of FINDING_P50A's mu(a,k) using
rho_phys (physical, gravitating density) instead of rho_A (bare) as the
reference density for the Poisson-equation comparison. Direct continuation
of FINDING_P59, per the user's own explicit sequencing (fix FINDING_P56
first -- FINDING_P56 Addendum #4 -- THEN this decisive test, since P50A's
re-test needs a self-consistent variable system before it is meaningful).

SCOPE GATE (user's own, explicit, load-bearing): strictly the SAME V=0
truncation as FINDING_P50A/P57. FINDING_P45's quartic potential is NOT
added simultaneously -- if this test's headline result changes relative
to FINDING_P50A, it must be attributable to the density-semantics
correction ALONE, not conflated with a second simultaneous change.

USER'S OWN PRE-REGISTERED OUTCOMES (D1/D2/D3 -- tested here, not assumed):
  D1 -- genuine leading modification SURVIVES: lim_{k->infinity} mu_phys
        != 1 even after switching to rho_phys as the reference density.
  D2 -- COMPLETE cancellation: mu_phys = 1 identically, at every tested k
        -- FINDING_P50A's mu!=1 was a pure density-definition artifact.
  D3 -- LEADING cancellation with a residual, k-dependent correction:
        lim_{k->infinity} mu_phys = 1, but mu_phys(a,k) != 1 at finite k
        -- the user's own predicted-most-plausible outcome.

FOUNDATIONAL STEP (checked before anything downstream relies on it):
FINDING_P50A's own Parts 3+4 (T_00^(int) + T_00^(matter), BOTH built from
rho_A) are proven here to be EXACTLY, algebraically identical to a single
T_00^(matter) built directly from rho_phys -- i.e. FINDING_P59's own
Route-B logic (T_m should physically be built from rho_phys, not rho_A)
applies cleanly at the level of THIS specific Poisson-equation source, with
T_00^(int)'s own g_hat*rhobar*delta_phi term EXACTLY cancelling the SAME
term that "unfolds" from converting rho_A's own contribution to rho_phys
via FINDING_P59's own linear relation. NOT assumed -- verified directly.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def main():
    print("=" * 78)
    print("P60 -- decisive D1/D2/D3 re-test of FINDING_P50A's mu(a,k) using")
    print("rho_phys instead of rho_A as the reference density")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print("\nSCOPE GATE: strictly V=0 (FINDING_P45's quartic NOT added here --")
    print("user's own explicit isolation requirement).")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- reproduce FINDING_P50A's own Part 5 symbols and")
    print("delta_T00_total_k EXACTLY (reused, not recomputed from Christoffels")
    print("-- P50A's own Parts 1-4 already established these pieces)")
    print("-" * 78)
    G_N, k, H = sp.symbols("G_N k H", real=True, positive=True)
    delta_rho_k, delta_phi_dot_k, Psi_k = sp.symbols("delta_rho_k delta_phi_dot_k Psi_k", real=True)
    phibar_dot, rhobar_s, phibar_s = sp.symbols("phibar_dot rhobar phibar", real=True)
    a_s = sp.Symbol("a", positive=True)
    ghat = sp.Symbol("g_hat", real=True, positive=True)

    delta_phi_k = ghat * a_s**2 * delta_rho_k / k**2  # P46's quasi-static solution
    dT00_phi_k = phibar_dot * delta_phi_dot_k
    dT00_int_k = (
        -ghat * rhobar_s * delta_phi_k
        - ghat * phibar_s * delta_rho_k
        - 2 * ghat * phibar_s * rhobar_s * Psi_k
    )
    dT00_matter_k = delta_rho_k + 2 * rhobar_s * Psi_k
    dT00_total_k = sp.expand(dT00_phi_k + dT00_int_k + dT00_matter_k)
    print(f"  delta_T00_total (FINDING_P50A's own Part 5, reused) = {dT00_total_k}")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 -- rho_phys algebraic relation (FINDING_P59 Part 1), adapted")
    print("to k-space via P46's own quasi-static delta_phi_k")
    print("-" * 78)
    M = 1 - ghat * phibar_s
    delta_rho_phys_k = M * delta_rho_k - ghat * rhobar_s * delta_phi_k
    rhobar_phys_s = rhobar_s * M
    print(f"  M := 1-g_hat*phibar = {M}")
    print(f"  delta_rho_phys_k := M*delta_rho_k - g_hat*rhobar*delta_phi_k = {delta_rho_phys_k}")
    print(f"  rhobar_phys := rhobar*M = {rhobar_phys_s}")
    print("  (FINDING_P59 Part 1's own exact linear relation, delta_phi_k")
    print("  substituted with P46's quasi-static solution -- consistent with")
    print("  this file's own delta_phi_k above, not a new assumption.)")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 -- FOUNDATIONAL CHECK: does T_00^(int)+T_00^(matter) (BOTH")
    print("built from rho_A, FINDING_P50A's own Parts 3+4) EXACTLY equal a")
    print("single T_00^(matter) built directly from rho_phys? Verified BEFORE")
    print("anything downstream relies on it, not assumed.")
    print("-" * 78)
    lhs_int_plus_matter = sp.expand(dT00_int_k + dT00_matter_k)
    rhs_phys_matter_alone = sp.expand(delta_rho_phys_k + 2 * rhobar_phys_s * Psi_k)
    print(f"  T_00^(int)+T_00^(matter), both rho_A-based = {lhs_int_plus_matter}")
    print(f"  T_00^(matter) alone, built from rho_phys    = {rhs_phys_matter_alone}")
    identity_check = sp.simplify(lhs_int_plus_matter - rhs_phys_matter_alone)
    assert identity_check == 0, (
        "T_00^(int)+T_00^(matter) [rho_A] does NOT equal T_00^(matter) [rho_phys] "
        "alone -- the foundational identity this file's own Part 4+ relies on is "
        "wrong, STOP, do not proceed with the rho_phys reference construction"
    )
    print("  -> CONFIRMED, EXACTLY (not just to leading order in g_hat or 1/k^2):")
    print("     T_00^(int)'s own g_hat*rhobar*delta_phi_k term EXACTLY cancels")
    print("     the SAME term that 'unfolds' from converting rho_A's M*delta_rho_k")
    print("     contribution into rho_phys form (FINDING_P59 Part 1's relation,")
    print("     rearranged: M*delta_rho_k = delta_rho_phys_k + g_hat*rhobar*")
    print("     delta_phi_k). The rho_A-based T_00^(int)+T_00^(matter) split IS,")
    print("     algebraically, the SAME object as a single rho_phys-based")
    print("     T_00^(matter) -- FINDING_P59's Route-B logic (matter's T_munu")
    print("     should be built from rho_phys, not rho_A) applies cleanly here,")
    print("     with NO leftover interaction-sector term at all.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 -- rewritten delta_T00_total, entirely in rho_phys semantics")
    print("-- verified identical to Part 1's original (Route-A) total, not a")
    print("new physical statement, purely a relabeling licensed by Part 3")
    print("-" * 78)
    dT00_total_k_phys = sp.expand(dT00_phi_k + delta_rho_phys_k + 2 * rhobar_phys_s * Psi_k)
    reidentity_check = sp.simplify(dT00_total_k_phys - dT00_total_k)
    assert reidentity_check == 0, (
        "the rho_phys-rewritten delta_T00_total does not match the original "
        "(Route-A) delta_T00_total -- algebra error, do not proceed"
    )
    print("  -> CONFIRMED: delta_T00_total_phys == delta_T00_total EXACTLY.")
    print("     Same Einstein equation, same Psi_k solution -- ONLY the")
    print("     reference density used to NORMALIZE mu(a,k) changes below.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 5 -- reproduce FINDING_P50A's own Parts 6-8 EXACTLY (Psi_k")
    print("solved self-consistently, Part 7's closure derivation reused as a")
    print("CITED input -- delta_phi_dot_k_closed for a GENERIC enslaved-")
    print("response coefficient c, not recomputed from Christoffels here)")
    print("-" * 78)
    eq = sp.Eq(-2 * (k**2 / a_s**2) * Psi_k, 8 * sp.pi * G_N * dT00_total_k)
    sol_unclosed = sp.solve(eq, Psi_k)
    assert len(sol_unclosed) == 1
    Psi_k_unclosed = sp.simplify(sol_unclosed[0])
    print(f"  Psi_k (exact, delta_phi_dot_k still symbolic) = {Psi_k_unclosed}")

    print("\n  [Reused from FINDING_P50A's own Part 7-8, NOT recomputed --")
    print("  P50A's own context-blind skeptic review (Step 8a) already")
    print("  independently confirmed this closure via covariant divergence]")
    c_sym = sp.Symbol("c", real=True)
    Psi_dot_k_closure = c_sym * H * Psi_k
    delta_rho_dot_k_closed = -3 * H * delta_rho_k + 3 * rhobar_s * Psi_dot_k_closure
    delta_phi_dot_k_closed = sp.expand(
        ghat * a_s**2 * (2 * H * delta_rho_k + delta_rho_dot_k_closed) / k**2
    )
    Psi_k_closed_generic_c = sp.simplify(
        Psi_k_unclosed.subs(delta_phi_dot_k, delta_phi_dot_k_closed)
    )
    print("  Psi_k (closed, generic enslaved-response coefficient c) computed")
    print("  -- identical construction to FINDING_P50A's own Part 7-8.")

    Psi_GR = -4 * sp.pi * G_N * a_s**2 * delta_rho_k / k**2
    mu_generic_c = sp.simplify(Psi_k_closed_generic_c / Psi_GR)
    leading_generic_c = sp.simplify(sp.limit(mu_generic_c, k, sp.oo))
    print(f"\n  mu(a,k) [FINDING_P50A's own, rho_A-referenced], leading term = {leading_generic_c}")
    assert sp.simplify(leading_generic_c - M) == 0, (
        "reused mu_generic_c does not reproduce FINDING_P50A's own established "
        "leading term 1-g_hat*phibar -- reuse error, do not proceed"
    )
    print("  -> CONFIRMED: reproduces FINDING_P50A's own established result")
    print("     exactly (M=1-g_hat*phibar) -- the reuse above is faithful.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 6 -- NEW: Psi_GR_phys (GR sourced by delta_rho_phys, not")
    print("delta_rho_A) and mu_phys := Psi_k / Psi_GR_phys")
    print("-" * 78)
    Psi_GR_phys = -4 * sp.pi * G_N * a_s**2 * delta_rho_phys_k / k**2
    print(f"  Psi_GR_phys := -4*pi*G_N*a^2*delta_rho_phys_k/k^2 = {Psi_GR_phys}")
    mu_phys = sp.simplify(Psi_k_closed_generic_c / Psi_GR_phys)
    print(f"  mu_phys := Psi_k / Psi_GR_phys = {mu_phys}")

    ratio_check = sp.simplify(mu_phys - mu_generic_c * (delta_rho_k / delta_rho_phys_k))
    assert ratio_check == 0, (
        "mu_phys does not decompose as mu_generic_c*(delta_rho_k/delta_rho_phys_k) "
        "-- algebra error in the Psi_GR_phys construction"
    )
    print("  -> CONFIRMED: mu_phys = mu_generic_c * (delta_rho_k/delta_rho_phys_k),")
    print("     i.e. FINDING_P50A's own mu, re-normalized by the SAME bare-to-")
    print("     physical density ratio established in Part 2.")

    print("\n  [SELF-CAUGHT, before any skeptic review, prompted directly by the")
    print("  user's own red-team gate: 'the finite-k residual must survive FULL")
    print("  use of the field equation, not remain an intermediate algebra")
    print("  stage'] mu_phys still contains Psi_k as a FREE, UNRESOLVED symbol:")
    psi_k_still_free = Psi_k in mu_phys.free_symbols
    print(f"    Psi_k in mu_phys.free_symbols? {psi_k_still_free}")
    assert psi_k_still_free, (
        "expected Psi_k to remain a free symbol in mu_phys (inherited from "
        "FINDING_P50A's own generic-c closure, which substitutes Psi_dot_k="
        "c*H*Psi_k into an algebraic constraint WITHOUT re-solving the "
        "resulting self-referential equation for Psi_k) -- if this is False, "
        "the closure structure has changed and the caveat below needs revising"
    )
    print("  -> This is NOT a new gap introduced here -- it is INHERITED")
    print("     directly from FINDING_P50A's own Part 7-8 construction (reused")
    print("     verbatim above): substituting Psi_dot_k=c*H*Psi_k into the")
    print("     already-solved Psi_k_unclosed expression re-introduces Psi_k on")
    print("     the RHS, since delta_phi_dot_k_closed itself depends on Psi_k.")
    print("     The truly self-consistent Psi_k would need to satisfy a FIXED-")
    print("     POINT/ODE condition (Psi_k = F(Psi_k), or genuinely solving")
    print("     Psi_k(t)'s own time evolution) -- FINDING_P50A explicitly named")
    print("     this as 'genuinely larger scope, not attempted' and deferred")
    print("     it. THIS FILE DOES NOT CLOSE THAT GAP EITHER -- doing so is a")
    print("     separate, not-yet-attempted task (see Verdict below). The")
    print("     k->infinity limit checked next is trustworthy DESPITE this gap")
    print("     ONLY because the Psi_k-dependent terms are shown to drop out")
    print("     in that specific limit -- checked directly, not assumed.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 7 -- D1 vs {D2,D3}: does the LEADING (k->infinity) term")
    print("survive at mu_phys != 1, or does it cancel? Checked for GENERIC c,")
    print("not one specific value (same robustness standard as FINDING_P50A's")
    print("own leading-order check)")
    print("-" * 78)
    mu_phys_leading = sp.simplify(sp.limit(mu_phys, k, sp.oo))
    print(f"  lim_(k->infinity) mu_phys = {mu_phys_leading}")
    assert sp.simplify(mu_phys_leading - 1) == 0, (
        "mu_phys does NOT tend to 1 as k->infinity -- if this fails, D1 is the "
        "correct verdict (a genuine leading-order modification survives), "
        "report that, do NOT force a D2/D3 conclusion"
    )
    print("  -> D1 RULED OUT: mu_phys -> 1 EXACTLY as k->infinity, independent")
    print("     of the closure coefficient c (checked for GENERIC c, not one")
    print("     specific value -- same robustness standard FINDING_P50A itself")
    print("     used for its own leading-order mu!=1 claim). FINDING_P50A's own")
    print("     mu(a,k)->1-g_hat*phibar!=1 result was, at LEADING order, a")
    print("     density-definition artifact: once compared against the SAME")
    print("     physical density that sources it, Newtonian strength is")
    print("     recovered at k->infinity.")

    print()
    print("  Does this leading-order limit survive DESPITE the unresolved")
    print("  Psi_k self-reference flagged above, or does the limit merely push")
    print("  the problem out of view? Checked directly: the Psi_k-dependent")
    print("  terms must themselves vanish in the k->infinity limit, not just")
    print("  cancel by coincidence against something else:")
    psi_k_survives_limit = Psi_k in mu_phys_leading.free_symbols
    print(f"    Psi_k in mu_phys_leading.free_symbols? {psi_k_survives_limit}")
    assert not psi_k_survives_limit, (
        "Psi_k survives into the k->infinity limit -- the leading-order D1 "
        "verdict is NOT actually independent of the unresolved self-reference "
        "flagged above, do not report D1 as robustly ruled out"
    )
    print("  -> CONFIRMED: Psi_k drops out ENTIRELY in the k->infinity limit --")
    print("     the D1 verdict above is genuinely robust to the unresolved")
    print("     Psi_k(t) closure gap, not merely blind to it.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 8 -- D2 vs D3: is mu_phys=1 IDENTICALLY (at every k, not just")
    print("the limit)? [CORRECTED, self-caught before skeptic review -- see")
    print("Part 6's own caveat: mu_phys still contains Psi_k UNRESOLVED, so a")
    print("nonzero-formula finding here does NOT by itself decide D2 vs D3 --")
    print("it only shows the CURRENT, not-yet-fully-closed expression is")
    print("nonzero. Reported honestly as such, not overclaimed as a clean D3.]")
    print("-" * 78)
    mu_phys_minus_one = sp.together(sp.expand(mu_phys - 1))
    print(f"  mu_phys - 1 (full expression, before any k-limit) = {mu_phys_minus_one}")
    is_identically_zero = sp.simplify(mu_phys_minus_one) == 0
    print(f"  Identically zero for ALL k (not just k->infinity)? {is_identically_zero}")
    assert not is_identically_zero, (
        "mu_phys-1 simplifies to EXACTLY zero -- this does NOT by itself prove "
        "D2 (Psi_k is still unresolved, see Part 6), but it IS a genuine fact "
        "worth guarding: if this assertion fails, the honest report changes to "
        "even the formal, Psi_k-unresolved expression is zero, which would be "
        "actively informative -- do not silently let this pass uncaught"
    )
    print("  -> As a FORMAL algebraic expression (Psi_k, delta_rho_k, c, k all")
    print("     treated as free symbols), this is nonzero -- but Psi_k has NOT")
    print("     been resolved to its true self-consistent value (Part 6's own")
    print("     caveat), so this does NOT yet prove the PHYSICAL mu_phys(a,k)")
    print("     differs from 1 at finite k. It shows only that the residual")
    print("     does not vanish for GENERIC (unresolved) Psi_k -- a necessary")
    print("     but not sufficient condition for D3.")

    print()
    print("  Series expansion in 1/k (large-k, informational -- inherits the")
    print("  SAME Psi_k-unresolved caveat as the full expression above, NOT a")
    print("  clean subleading-order result):")
    series_expansion = sp.series(mu_phys, k, sp.oo, 3).removeO()
    print(f"    mu_phys (large-k series) = {series_expansion}")
    print()
    print("  [SKEPTIC-CAUGHT, Step 8a: the two claims below were computed but")
    print("  never asserted in an earlier draft -- fixed here with real")
    print("  assertions, not just print statements]")
    psi_k_in_series = Psi_k in series_expansion.free_symbols
    print(f"  Does the residual's own series contain Psi_k (unresolved)? {psi_k_in_series}")
    assert psi_k_in_series, (
        "the large-k series does NOT contain Psi_k -- the 'entangled with "
        "the unresolved Psi_k self-reference' claim below would be FALSE, "
        "do not report it if this assertion fails"
    )
    c_derivative_simplified = sp.simplify(sp.diff(series_expansion, c_sym))
    residual_coefficient_depends_on_c = c_derivative_simplified != 0
    print("  Does the finite-k residual's own leading term depend on the")
    print(f"  unclosed coefficient c? {residual_coefficient_depends_on_c}")
    assert residual_coefficient_depends_on_c, (
        "d(series_expansion)/dc simplifies to EXACTLY zero -- the residual "
        "does NOT actually depend on c, contradicting the claim below, do "
        "not report it if this assertion fails. [SKEPTIC-CAUGHT: use "
        "sp.simplify(...) != 0, not a raw sympy != comparison, which is "
        "not a reliable zero-test]"
    )
    print("  -> Confirms the residual's form is entangled with BOTH the")
    print("     unclosed c AND the unresolved Psi_k self-reference -- deciding")
    print("     D2 vs D3 requires closing Psi_k(t)'s own self-consistency")
    print("     (genuinely larger scope, FINDING_P50A's own deferred task,")
    print("     NOT attempted here either). This file does not force a")
    print("     conclusion beyond what it actually established.")

    # ------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("D1 RULED OUT, ROBUSTLY: mu_phys -> 1 EXACTLY as k->infinity, and this")
    print("survives BOTH generic-c AND the unresolved Psi_k self-reference (both")
    print("checked to drop out of the limit directly, not assumed). FINDING_P50A's")
    print("own mu(a,k)->1-g_hat*phibar (!=1) headline was, at LEADING order, a")
    print("pure density-definition artifact -- confirmed, not merely plausible.")
    print()
    print("D2 vs D3 -- GENUINELY OPEN, NOT DECIDED HERE. [Self-caught before any")
    print("skeptic review, prompted directly by the user's own red-team gate: a")
    print("finite-k residual must survive FULL use of the field equation, not")
    print("remain an intermediate algebra stage.] The finite-k mu_phys formula")
    print("still contains Psi_k as an UNRESOLVED free symbol (Part 6) -- the")
    print("generic-c closure this file reuses VERBATIM from FINDING_P50A")
    print("substitutes Psi_dot_k=c*H*Psi_k into an algebraic constraint WITHOUT")
    print("re-solving the resulting self-referential equation for Psi_k. That is")
    print("NOT a new gap -- FINDING_P50A itself named exactly this as 'requires")
    print("solving the Psi_k(t) ODE, genuinely larger scope, not attempted' -- but")
    print("it means Part 8's nonzero-residual finding is NECESSARY, not SUFFICIENT")
    print("evidence for D3: it rules out the residual being trivially, formally")
    print("zero, but does not rule out that closing Psi_k(t) properly could still")
    print("reduce it to zero (D2) once the self-consistency is enforced.")
    print()
    print("FOUNDATIONAL RESULT (Part 3-4), FULLY ESTABLISHED, NOT provisional:")
    print("FINDING_P50A's own T_00^(int)+T_00^(matter) split (both built from")
    print("rho_A) is EXACTLY, algebraically identical to a single T_00^(matter)")
    print("built from rho_phys directly -- confirms FINDING_P59's Route-B logic")
    print("(T_m should be built from rho_phys) applies cleanly to this Poisson-")
    print("equation observable too. This result does NOT depend on Psi_k's")
    print("closure at all (it holds symbol-for-symbol, Psi_k included, before any")
    print("closure is applied) -- fully robust.")
    print()
    print("PHYSICAL READING: what this file SHARPENS relative to FINDING_P50A is")
    print("not 'the leading artifact-ness is now certain vs uncertain' (it was")
    print("already FINDING_P50A's own robust leading-order claim) but WHICH")
    print("REFERENCE DENSITY that artifact-ness is measured against: switching")
    print("from rho_A to rho_phys does not change the STATUS of the leading-order")
    print("result (still an artifact, still robustly so) -- what it changes is")
    print("that the SAME already-known open question (closing Psi_k(t)) is now")
    print("ALSO the single remaining question for the finite-k density-semantics")
    print("test, not a separate, additional uncertainty. The two open items")
    print("FINDING_P50A named (subleading mu(a,k) structure; Psi_k(t) closure)")
    print("and this file's own open item (D2 vs D3) are THE SAME open item.")
    print()
    print("SCOPE, per the user's own explicit gate: V=0 truncation ONLY --")
    print("FINDING_P45's quartic potential NOT added here, deliberately, so")
    print("this result is attributable to the density-semantics correction")
    print("alone. A V!=0 extension is a separate, not-yet-attempted next step.")
    print()
    print("NOT YET DONE: (1) closing Psi_k(t)'s own self-consistency (fixed-point")
    print("or genuine ODE solution) -- the SAME task FINDING_P50A deferred,")
    print("required before D2 vs D3 can be decided; (2) the V!=0 (FINDING_P45")
    print("quartic) extension, deliberately excluded per the scope gate above;")
    print("(3) the Phi,Psi-extension of FINDING_P59's own nu=0/nu=1 results (this")
    print("file reuses FINDING_P50A's Phi,Psi-perturbed Part 7 continuity")
    print("directly, but does not itself re-derive FINDING_P59's Route-B")
    print("construction on that more general metric).")
    return {
        "mu_phys_leading": mu_phys_leading,
        "mu_phys_minus_one_series": series_expansion,
    }


if __name__ == "__main__":
    result = main()
    raise SystemExit(0 if result else 1)
