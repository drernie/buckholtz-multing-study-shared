"""P25_wep_eotvos_kill_gate.py -- does the k-sector (kappa) coupling
established by P1/P21-P24 make two test bodies of DIFFERENT composition
fall at different rates toward the same source, and if so, is that
difference already excluded by real Eotvos/equivalence-principle data?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive

CONTEXT: P23's skeptic review established that a coupling EXACTLY
proportional to inertial mass (g, the monopole sector) is degenerate with
Newton's G and evades equivalence-principle (EP) tests entirely -- they
probe composition-DEPENDENCE only. The k-sector (kappa) is structurally
DIFFERENT: it couples to k_i, a body-specific "second charge" (per
FINDING_P7_k_definition_resolved_from_corpus.md), not simply to mass. If
K_i/M_i (charge-to-mass ratio) is not universal across materials -- and
nothing in this project's own files claims it is -- the k-sector should
produce a genuine, computable, composition-dependent acceleration
difference: exactly what Eotvos-type experiments are built to detect.

[CORRECTED 2026-08-13 after skeptic review -- a real completeness gap, not
a framing issue.] The original version used ONLY F_km (monopole-dipole
cross term) for the test body's acceleration. The skeptic found this
misses TWO real contributions: (1) F_mm (monopole-monopole), which
dominates the DENOMINATOR |a_1+a_2| and was silently omitted from the
original eta_Eotvos expression; (2) F_kk (dipole-dipole), which ALSO
carries a composition-dependent piece proportional to the SAME ratio
K_test*r_test/M_test as F_km's, but with opposite functional form (kappa^2
not kappa^1, 1/r^4 not 1/r^3) -- omitting it silently understated the
composition-dependent coefficient. Both are now included. The original
positive control (matching K*r/M across two bodies forces a_1=a_2) is kept
but its diagnostic LIMIT is now stated explicitly: since BOTH the F_km and
F_kk composition pieces are proportional to the identical ratio K*r/M, this
control cannot distinguish "F_kk correctly included" from "F_kk omitted
entirely" -- it passes either way. A genuinely differentiating check (the
two composition-dependent terms have DIFFERENT r-power, 1/r^3 vs 1/r^4) is
added instead.

METHOD: reuse P24's own already-verified tiers_from_kernel machinery
(sympy, symbolic, not re-derived by hand) for the FULL force (F_mm+F_km+
F_kk) between a light test body and a heavy fixed source. Split the total
acceleration into a composition-INDEPENDENT term (source properties only)
and a composition-DEPENDENT term (proportional to the test body's OWN
K_test*r_test/M_test). Compute the standard Eotvos parameter
eta_Eotvos = 2|a_1-a_2|/|a_1+a_2| for two test bodies of different
composition in the SAME source field, symbolically, using the FULL
acceleration in both numerator and denominator this time.
"""

from __future__ import annotations

import sympy as sp

s, r = sp.symbols("s r", positive=True)
mA, mB, qA, qB, dA, dB = sp.symbols("m_A m_B q_A q_B d_A d_B", positive=True)
g, kappa, big_a, c = sp.symbols("g kappa A c", positive=True)
big_ma, big_ka, ra = sp.symbols("M_A K_A r_A", positive=True)
big_m1, big_k1, r1 = sp.symbols("M_1 K_1 r_1", positive=True)
big_m2, big_k2, r2 = sp.symbols("M_2 K_2 r_2", positive=True)


def tiers_from_kernel(kernel):
    """Unchanged from P1/P24 -- same physical-dipole construction. Now
    returns all three tiers (P25 v1 used only u_km)."""
    a_ch = [(mA, 0), (qA, dA / 2), (-qA, -dA / 2)]
    b_ch = [(mB, r), (-qB, r + dB / 2), (qB, r - dB / 2)]
    eps = sp.Symbol("eta_expand", positive=True)
    u = sum(
        ca * cb * kernel.subs(s, (zb - za).subs({dA: eps * dA, dB: eps * dB}))
        for ca, za in a_ch
        for cb, zb in b_ch
    )
    u = sp.series(u, eps, 0, 3).removeO().subs(eps, 1)
    u = sp.expand(sp.simplify(u))
    u_mm = u.coeff(mA, 1).coeff(mB, 1) * mA * mB
    u_km = u.coeff(qA, 1).coeff(mB, 1) * qA * mB + u.coeff(qB, 1).coeff(mA, 1) * qB * mA
    u_kk = u.coeff(qA, 1).coeff(qB, 1) * qA * qB
    return sp.simplify(u_mm), sp.simplify(u_km), sp.simplify(u_kk)


def full_acceleration(m_test, k_test, r_test):
    """a = (F_mm+F_km+F_kk)/M_test -- the FULL acceleration, all three
    tiers, for a light test body (M_test, K_test, r_test) falling toward
    the fixed source (M_A, K_A, r_A). Same substitution convention as P24:
    m_i->g*M_i, q_i->-kappa*K_i/c^2, d_i->r_i, one overall A."""
    u_mm, u_km, u_kk = tiers_from_kernel(1 / s)
    f_mm = sp.simplify(-sp.diff(u_mm, r))
    f_km = sp.simplify(-sp.diff(u_km, r))
    f_kk = sp.simplify(-sp.diff(u_kk, r))
    subs_map = {
        mA: g * big_ma,
        mB: g * m_test,
        qA: -kappa * big_ka / c**2,
        qB: -kappa * k_test / c**2,
        dA: ra,
        dB: r_test,
    }
    f_total = big_a * (f_mm + f_km + f_kk).subs(subs_map)
    return sp.simplify(f_total / m_test)


def main() -> int:
    print("=" * 78)
    print("P25 -- WEP/Eotvos kill-gate: does the k-sector violate composition")
    print("       independence, and if so, how? (CORRECTED -- full mm+km+kk)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    a1 = full_acceleration(big_m1, big_k1, r1)
    a2 = full_acceleration(big_m2, big_k2, r2)
    print("\n[STEP 1] FULL acceleration (F_mm+F_km+F_kk)/M_test of two test")
    print("  bodies (1, 2), same source A -- corrected from v1's F_km-only.")
    a1_c = sp.collect(sp.expand(a1), big_k1)
    print(f"  a_1 (collected by K_1) = {a1_c}")

    print("\n[STEP 2] Does the source-only piece still cancel from a_1-a_2?")
    delta_a = sp.expand(sp.simplify(a1 - a2))
    source_only_diff = sp.simplify(delta_a.subs({big_k1: 0, big_k2: 0}))
    print(f"  a_1-a_2 with K_1=K_2=0 (pure monopole-monopole part): {source_only_diff}")
    if source_only_diff != 0:
        print("  STOP -- source-only/monopole piece does not cancel, unexpected.")
        return 1
    print("  -> CONFIRMED: the composition-INDEPENDENT part (F_mm entirely, plus")
    print("     F_km's source-only term) still cancels identically from a_1-a_2,")
    print("     even with F_mm and F_kk now included.")

    print("\n[STEP 3] The composition-dependent coefficient -- NOW includes BOTH")
    print("  the F_km piece (linear in kappa) AND the F_kk piece (quadratic in")
    print("  kappa, previously missing entirely).")
    # isolate the coefficient of K_1 (test body 1's charge) in a_1
    comp_coeff_1 = sp.simplify(sp.diff(a1, big_k1))
    print(f"  d(a_1)/d(K_1) = {comp_coeff_1}")
    print("  -> two additive pieces, verified by their DIFFERENT r-power below")
    print("     (this is the genuinely differentiating check the v1 positive")
    print("     control could NOT provide, since both pieces share the SAME")
    print("     K*r/M dependence and are indistinguishable by that test alone):")
    km_piece = -2 * big_a * g * kappa * big_ma * r1 / (c**2 * r**3 * big_m1)
    kk_piece = 6 * big_a * kappa**2 * big_ka * ra * r1 / (c**4 * r**4 * big_m1)
    check_split = sp.simplify(comp_coeff_1 - (km_piece + kk_piece))
    print(f"  F_km-derived piece (kappa^1, ~1/r^3): {km_piece}")
    print(f"  F_kk-derived piece (kappa^2, ~1/r^4): {kk_piece}")
    print(f"  residual after subtracting both from d(a_1)/d(K_1): {check_split}")
    if check_split != 0:
        print("  STOP -- the two-piece decomposition does not match.")
        return 1
    print("  -> CONFIRMED: two independent contributions, different power of")
    print("     kappa AND different power of r -- NOT a duplicate, both real.")

    print("\n[STEP 4] Corrected eta_Eotvos -- using the FULL a_1, a_2 in BOTH")
    print("  numerator and denominator (v1 used F_km alone in the denominator,")
    print("  which is wrong: F_mm dominates |a_1+a_2| in reality).")
    eta_eotvos_full = sp.simplify(2 * sp.Abs(delta_a) / sp.Abs(a1 + a2))
    print(f"  eta_Eotvos (full) = 2|a_1-a_2|/|a_1+a_2| = {eta_eotvos_full}")

    print("\n[STEP 5] Positive control -- kept, but its diagnostic LIMIT stated.")
    print("  Setting K_2*r_2/M_2 = K_1*r_1/M_1 forces a_1=a_2 -- but since BOTH")
    print("  composition-dependent pieces (kappa^1 and kappa^2) share this SAME")
    print("  ratio, this control passes whether F_kk is included or not -- it")
    print("  does NOT discriminate this specific completeness error (matches")
    print("  this project's own FINDING_two_charge_completion.md Sec.6 lesson:")
    print("  'a control that switches off the feature under test cannot test it').")
    equal_ratio_test = sp.simplify(delta_a.subs({big_k2: big_k1 * big_m2 * r1 / (big_m1 * r2)}))
    print(f"  a_1-a_2 with K_2*r_2/M_2=K_1*r_1/M_1: {equal_ratio_test}")
    if equal_ratio_test != 0:
        print("  STOP -- composition-matched bodies still differ.")
        return 1

    print("\n[STEP 6] Codimension-1 cancellation surface -- a SECOND escape route")
    print("  beyond K/M universality: does a specific relation among the")
    print("  parameters zero the TOTAL composition coefficient even when K/M is")
    print("  NOT universal?")
    total_comp_coeff = sp.simplify(km_piece + kk_piece)
    cancel_solution = sp.solve(sp.Eq(total_comp_coeff, 0), kappa)
    print(f"  Solving [F_km-piece + F_kk-piece] = 0 for kappa: {cancel_solution}")
    print("  -> a nonzero solution exists (kappa = specific ratio of g, M_A, K_A,")
    print("     r_A, r, c) -- a fine-tuned surface, not generic, but a real,")
    print("     distinct alternative to K/M universality that also hides the")
    print("     violation. Not claimed to be natural or likely -- only that it")
    print("     exists and was not named in v1.")

    print("\n" + "=" * 78)
    print("VERDICT -- CORRECTED, softened per skeptic review")
    print("=" * 78)
    print("CONFIRMED (structural, sympy-verified, now complete): the k-sector")
    print("predicts a nonzero composition-dependent acceleration difference from")
    print("TWO independent contributions (F_km linear in kappa, F_kk quadratic),")
    print("both proportional to the test body's own K*r/M -- verified via their")
    print("DIFFERENT r-power, not merely asserted. This is CONDITIONAL, not")
    print("structural-full-stop: it requires K/M to be non-universal across")
    print("materials (MODEL_SPEC_AUDIT.md flags k_A,k_P as OPEN, not resolved)")
    print("AND falls outside the codimension-1 cancellation surface (Step 6).")
    print("If K/M turns out approximately universal, the k-sector's signal is")
    print("numerically suppressed toward the g-sector's exact zero, not")
    print("qualitatively opposite to it.")
    print()
    print("NOT DONE HERE: numeric evaluation against a real EP bound (e.g.")
    print("MICROSCOPE), a real/estimated K/M variation across materials, or")
    print("whether the lab-scale physical-dipole picture (charges at +-r_i/2 of")
    print("a solid test mass) is even a coherent extension of the cluster-scale")
    print("construction motivating it -- all explicitly out of scope here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
