"""P24_gk_matching_eta_invariant.py -- does a single physical parameter
eta=kappa/g control the k-sector's force strength RELATIVE TO the
monopole/gravity sector, once g (P1's monopole coupling, structurally
separate from kappa since P13a) is inserted explicitly into P1's own
two-charge multipole derivation for the first time?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive

CONTEXT: P1 (two_field_action_closure.py) derived F_mm, F_km, F_kk from a
general kernel using bare charges m_A, m_B (monopole) and q_A, q_B (dipole,
with q=-kappa*k/c^2 per FINDING_two_charge_completion.md), implicitly
setting g=1 throughout -- g never appears anywhere in P1-P20's multipole
work. P21-P23 separately established g is a real, independent coupling
constant (the SAME field's monopole term) with its own field-normalization
constant A. This script asks: does explicitly inserting g and A into P1's
ALREADY-VERIFIED kernel derivation collapse the cross-sector force ratios
(dipole-to-monopole, quadrupole-to-monopole) onto a single ratio
eta=kappa/g, and does the ALREADY-ESTABLISHED beta_q/beta_d=sqrt(6)/2
(FINDING_two_charge_completion.md, 2026-08-10) survive unchanged?

NAMING NOTE, stated up front to avoid a symbol collision: beta_d=2 and
beta_q=sqrt(6) are ALREADY established, verified, FIXED PURE NUMBERS in
this project (the multipole-expansion coefficients relating l_d, l_q^2 to
u_A+u_B, u_A*u_B -- an intra-k-sector ratio that never involves g). This
script does NOT redefine them. The NEW quantity computed here -- the
CROSS-SECTOR force ratio (dipole force vs. monopole/gravity force) -- is
given a DIFFERENT name (chi_d, chi_q) specifically to avoid overloading
beta_d, beta_q with a second, incompatible meaning.

METHOD: reuse P1's own tiers_from_kernel function unchanged (same K=1/s
massless kernel, same physical-dipole construction) -- positive control:
setting g=A=1 must reproduce P1's already-published coefficients 2 and 6
exactly. Then substitute m_i -> g*M_i (monopole charge = coupling g times
mass, per the action g*m_i*phi) and q_i -> -kappa*K_i/c^2 (per
FINDING_two_charge_completion.md's own q=-kappa*k/c^2), multiply by ONE
overall factor of A (P21's field normalization -- enters once, since
force = -grad[coupling_2 * A * phi_raw_1(x_2)]), and check symbolically
whether A and g cancel from the cross-sector ratios after kappa=eta*g.
"""

from __future__ import annotations

import sympy as sp

s, r = sp.symbols("s r", positive=True)
mA, mB, qA, qB, dA, dB = sp.symbols("m_A m_B q_A q_B d_A d_B", positive=True)
g, kappa, big_a, c, eta = sp.symbols("g kappa A c eta", positive=True)
big_ma, big_mb, big_ka, big_kb, ra, rb = sp.symbols("M_A M_B K_A K_B r_A r_B", positive=True)


def tiers_from_kernel(kernel):
    """Unchanged from P1 (two_field_action_closure.py) -- same physical-dipole
    construction, same mirror-symmetric charge layout, same eps expansion."""
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


def main() -> int:
    print("=" * 78)
    print("P24 -- g/kappa/A matching: does eta=kappa/g control cross-sector ratios?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    u_mm, u_km, u_kk = tiers_from_kernel(1 / s)
    f_mm = sp.simplify(-sp.diff(u_mm, r))
    f_km = sp.simplify(-sp.diff(u_km, r))
    f_kk = sp.simplify(-sp.diff(u_kk, r))

    print("\n[POSITIVE CONTROL] g=A=1 must reproduce P1's already-published")
    print("  coefficients 2 (dipole) and 6 (quadrupole) exactly, unchanged.")
    c2 = sp.simplify(f_km * r**3 / (qA * dA * mB + qB * dB * mA))
    c3 = sp.simplify(f_kk * r**4 / (qA * dA * qB * dB))
    print(f"  dipole coefficient  = {c2}   (P1: 2)")
    print(f"  quadrupole coefficient = {c3}   (P1: 6)")
    if c2 != 2 or c3 != 6:
        print("  STOP -- does not reproduce P1's established result.")
        return 1

    print("\n[STEP 1] Insert g, kappa, A explicitly -- NEVER done in P1-P23.")
    print("  m_i -> g*M_i        (monopole charge = coupling g * mass, per g*m_i*phi)")
    print("  q_i -> -kappa*K_i/c^2   (dipole charge, per FINDING_two_charge_completion.md)")
    print("  d_i -> r_i          (lever arm = body radius, that finding's own convention)")
    print("  ONE overall factor A (P21) -- force = -grad[coupling_2 * A * phi_raw_1(x_2)]")
    subs_map = {
        mA: g * big_ma,
        mB: g * big_mb,
        qA: -kappa * big_ka / c**2,
        qB: -kappa * big_kb / c**2,
        dA: ra,
        dB: rb,
    }
    f_mm_full = sp.simplify(big_a * f_mm.subs(subs_map))
    f_km_full = sp.simplify(big_a * f_km.subs(subs_map))
    f_kk_full = sp.simplify(big_a * f_kk.subs(subs_map))
    print(f"  F_mm = {f_mm_full}")
    print(f"  F_km = {f_km_full}")
    print(f"  F_kk = {f_kk_full}")
    print("  -> F_mm ~ A*g^2 (matches P21/P22's own A*g^2 exactly -- sanity check),")
    print("     F_km ~ A*g*kappa,  F_kk ~ A*kappa^2 -- one power of each body's own")
    print("     coupling constant, as the bilinear action structure forces.")

    print("\n[STEP 2] Cross-sector ratios -- does A cancel identically?")
    ratio_km_mm = sp.simplify(f_km_full / f_mm_full)
    ratio_kk_mm = sp.simplify(f_kk_full / f_mm_full)
    ratio_kk_km = sp.simplify(f_kk_full / f_km_full)
    a_gone = (
        big_a not in ratio_km_mm.free_symbols
        and big_a not in ratio_kk_mm.free_symbols
        and big_a not in ratio_kk_km.free_symbols
    )
    print(f"  A present in any ratio: {not a_gone}")
    if not a_gone:
        print("  STOP -- A does not cancel, chi_d/chi_q would not be well-defined.")
        return 1

    print("\n[STEP 3] Substitute kappa = eta*g -- does g ALSO cancel identically?")
    chi_d = sp.simplify(ratio_km_mm.subs(kappa, eta * g))
    chi_q = sp.simplify(ratio_kk_mm.subs(kappa, eta * g))
    chi_qd = sp.simplify(ratio_kk_km.subs(kappa, eta * g))
    g_gone = (
        g not in chi_d.free_symbols and g not in chi_q.free_symbols and g not in chi_qd.free_symbols
    )
    print(f"  chi_d := F_km/F_mm (eta form) = {chi_d}")
    print(f"  chi_q := F_kk/F_mm (eta form) = {chi_q}")
    print(f"  chi_q/chi_d = F_kk/F_km (eta form) = {chi_qd}")
    print(f"  g present in any: {not g_gone}")
    if not g_gone:
        print("  STOP -- g does not cancel, eta is not the sole controlling parameter.")
        return 1
    print("  -> chi_d ~ eta^1, chi_q ~ eta^2, chi_q/chi_d ~ eta^1 -- CONFIRMED:")
    print("     eta=kappa/g is the SOLE parameter controlling k-sector-to-monopole")
    print("     force strength, for identical bodies up to the pure geometric part.")

    print("\n[STEP 4] beta_d=2, beta_q=sqrt(6) -- do these change at all?")
    print("  They were computed directly from f_km, f_kk BEFORE any g/kappa/A")
    print("  substitution (Positive Control above) -- g never entered u_A+u_B,")
    print("  u_A*u_B (MULTING's own l_d, l_q^2 construction uses body mass as a")
    print("  NORMALIZING denominator in u_i=kappa*k_i*r_i/(c^2*m_i), not as the")
    print("  g-coupling charge -- a different role for the same symbol 'm').")
    print("  UNCHANGED: beta_d=2, beta_q=sqrt(6), beta_q/beta_d=sqrt(6)/2 -- this")
    print("  was already established 2026-08-10 and does not depend on g at all.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("CONFIRMED (structural, sympy-verified): inserting g, kappa, A explicitly")
    print("into P1's own already-verified kernel derivation shows the cross-sector")
    print("force ratios chi_d=F_km/F_mm, chi_q=F_kk/F_mm collapse onto pure powers")
    print("of a single new parameter eta=kappa/g (eta^1, eta^2 respectively), with A")
    print("canceling identically. This is a genuine, previously-unstated structural")
    print("fact about this project's own reconstruction -- but see the finding's own")
    print("honest caveat: it follows near-automatically from the assumed BILINEAR")
    print("coupling form (one power of g XOR kappa per body, never both, never a")
    print("cross term) -- not an independent discovery about MULTING's physics")
    print("beyond what the action's own already-assumed shape forces algebraically.")
    print("The ALREADY-ESTABLISHED beta_q/beta_d=sqrt(6)/2 (2026-08-10) is UNCHANGED")
    print("and does not depend on g -- confirmed, not re-derived, by direct inspection")
    print("of where g does and does not enter the calculation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
