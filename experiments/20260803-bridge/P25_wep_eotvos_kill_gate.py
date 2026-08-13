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

METHOD: reuse P24's own already-verified F_km expression (sympy, symbolic,
not re-derived by hand) for the acceleration of a light test body B
falling toward a heavy fixed source A. Split a_B into a
composition-INDEPENDENT term (source properties only) and a composition-
DEPENDENT term (proportional to the test body's OWN K_B/M_B). Compute the
standard Eotvos parameter eta_Eotvos = 2|a_1-a_2|/|a_1+a_2| for two test
bodies of different composition in the SAME source field, symbolically.
Then compare the PREDICTED functional form (not a fabricated number)
against what a real external EP-test bound would require -- explicitly
flagged as NOT independently verified this session if no fetch is done.
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
    """Unchanged from P1/P24 -- same physical-dipole construction."""
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
    u_km = u.coeff(qA, 1).coeff(mB, 1) * qA * mB + u.coeff(qB, 1).coeff(mA, 1) * qB * mA
    return sp.simplify(u_km)


def acceleration_of_test_body(m_test, k_test, r_test):
    """a = F_km/M_test for a light test body (M_test, K_test, r_test) falling
    toward the fixed source (M_A, K_A, r_A), using P24's own substitution
    convention (m_i->g*M_i, q_i->-kappa*K_i/c^2, d_i->r_i, one overall A)."""
    u_km = tiers_from_kernel(1 / s)
    f_km = sp.simplify(-sp.diff(u_km, r))
    subs_map = {
        mA: g * big_ma,
        mB: g * m_test,
        qA: -kappa * big_ka / c**2,
        qB: -kappa * k_test / c**2,
        dA: ra,
        dB: r_test,
    }
    f_km_full = sp.simplify(big_a * f_km.subs(subs_map))
    return sp.simplify(f_km_full / m_test)


def main() -> int:
    print("=" * 78)
    print("P25 -- WEP/Eotvos kill-gate: does the k-sector violate composition")
    print("       independence, and if so, how?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    a1 = acceleration_of_test_body(big_m1, big_k1, r1)
    a2 = acceleration_of_test_body(big_m2, big_k2, r2)
    print("\n[STEP 1] Acceleration of two test bodies (1, 2), same source A,")
    print("  reusing P24's own F_km expression unchanged.")
    print(f"  a_1 = F_km(body 1)/M_1 = {a1}")
    print(f"  a_2 = F_km(body 2)/M_2 = {a2}")

    a1_c = sp.collect(sp.expand(a1), big_k1)
    a2_c = sp.collect(sp.expand(a2), big_k2)
    print(f"\n  a_1 split: {a1_c}")
    print(f"  a_2 split: {a2_c}")
    print("  -> each accel = [source-only term, SAME for both bodies]")
    print("                + [term proportional to the TEST body's OWN K_i/M_i]")

    print("\n[STEP 2] Difference and Eotvos parameter -- does the source-only")
    print("  term cancel out of a_1-a_2, leaving a PURE composition-dependent")
    print("  residual?")
    delta_a = sp.simplify(a1 - a2)
    delta_a_expanded = sp.expand(delta_a)
    print(f"  a_1 - a_2 = {delta_a_expanded}")

    # Isolate: does the source-only piece (proportional to K_A, independent of
    # K_1,K_2,M_1,M_2) actually cancel in the difference?
    source_only_term = sp.expand(a1).coeff(big_ka, 1) - sp.expand(a2).coeff(big_ka, 1)
    print(f"  source-only (K_A) coefficient in a_1 minus in a_2: {sp.simplify(source_only_term)}")
    cancels = sp.simplify(source_only_term) == 0
    print(f"  -> source-only term cancels identically: {cancels}")
    if not cancels:
        print("  STOP -- unexpected structure, the split assumed above is wrong.")
        return 1

    eta_eotvos = sp.simplify(2 * sp.Abs(delta_a_expanded) / sp.Abs(a1 + a2))
    print(f"\n  eta_Eotvos = 2|a_1-a_2|/|a_1+a_2| = {eta_eotvos}")

    print("\n[STEP 3] The composition-dependence signature")
    print("  Setting K_1/M_1 = K_2/M_2 (SAME charge-to-mass-times-radius ratio)")
    print("  should force a_1=a_2 exactly -- a positive control on this result.")
    equal_ratio_test = sp.simplify(
        delta_a_expanded.subs({big_k2: big_k1 * big_m2 * r1 / (big_m1 * r2)})
    )
    print(f"  a_1-a_2 with K_2 chosen so K_2*r_2/M_2 = K_1*r_1/M_1: {equal_ratio_test}")
    if equal_ratio_test != 0:
        print("  STOP -- composition-matched bodies still differ, structure is wrong.")
        return 1
    print("  -> CONFIRMED: a_1=a_2 exactly when K_i*r_i/M_i matches -- the")
    print("     violation is driven PURELY by the dipole-moment-per-mass ratio")
    print("     K_i*r_i/M_i (equivalently p_i/M_i, the body's own dipole moment")
    print("     per unit mass), not by mass or radius alone.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("CONFIRMED (structural, sympy-verified): the k-sector (kappa) coupling")
    print("predicts a GENUINE, nonzero composition-dependent acceleration")
    print("difference between two test bodies with different K_i*r_i/M_i (dipole")
    print("moment per unit mass) in the same source field -- this is EXACTLY the")
    print("kind of signature real Eotvos-type equivalence-principle experiments")
    print("are built to detect, unlike the g-sector (P23), which is degenerate")
    print("with G and structurally invisible to such tests.")
    print()
    print("NOT DONE HERE: comparing this predicted functional form against a")
    print("real external EP-test bound (e.g. MICROSCOPE) requires an independently")
    print("verified numeric sensitivity AND a real value/estimate for K_i*r_i/M_i")
    print("across different materials -- neither attempted in this script. The")
    print("kill-gate question (does this survive existing WEP limits) remains open")
    print("pending that external, verified numeric comparison.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
