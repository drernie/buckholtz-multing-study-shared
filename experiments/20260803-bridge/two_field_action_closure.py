"""P1: close the two-field theory -- is beta_q/beta_d = sqrt(6)/2 inevitable?

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
2026-08-10 · plan item P1 after the external review of the bridge track.

THE QUESTION. The two-charge construction produced beta_d = 2, beta_q = sqrt(6)
with "zero free parameters after kappa". An external reviewer asked the right
question: is the ratio 2:sqrt(6) an inevitable physical prediction, or an
artefact of the specific construction (physical dipoles made of point charges,
lever arm identified with r_A)?

THE METHOD. Reduce the construction to its skeleton. All three force tiers come
from derivatives of ONE exchange kernel K(s):

    U_mm  =  m_A m_B K(r)                       -> F_mm ~ -K'
    U_km  ~  (q d) m  K'(r)   (radial dipole)   -> F_km ~ -K''
    U_kk  ~  (q d)^2  K''(r)                    -> F_kk ~ -K'''

so every normalisation of the dipole moment (kappa, the lever-arm convention
zeta*r_A, even the identification q = -kappa k/c^2) enters ell_d once and
ell_q^2 twice and CANCELS from the combination

    Lambda(r)  =  ell_q^2 / ell_d^2 * (u_A+u_B)^2/(u_A u_B)|_identical...

more precisely, the kernel part of ell_q^2/ell_d^2 is the invariant

    Lambda(r)  =  K'''(r) K'(r) / K''(r)^2

and the claim to test is: Lambda = 3/2, constant, if and only if K = 1/s
(massless mediator). If a massive (Yukawa) mediator changes Lambda, the ratio
prediction is tied to masslessness, not to the point-charge scaffolding.
"""

import sympy as sp

s, r, mu = sp.symbols("s r mu", positive=True)
mA, mB, qA, qB, dA, dB = sp.symbols("m_A m_B q_A q_B d_A d_B", positive=True)


def tiers_from_kernel(K):
    """Expand the mirror-symmetric two-dipole energy for a general kernel K(s),
    to second order in both lever arms; return (U_mm, U_km, U_kk) coefficients.

    Same charge layout as two_charge_completion.py's fixed configuration:
    A = {m_A at 0, +q_A at d_A/2, -q_A at -d_A/2},
    B = {m_B at r, -q_B at r+d_B/2, +q_B at r-d_B/2}  (mirror-symmetric).
    """
    a_ch = [(mA, 0), (qA, dA / 2), (-qA, -dA / 2)]
    b_ch = [(mB, r), (-qB, r + dB / 2), (qB, r - dB / 2)]
    eps = sp.Symbol("eta", positive=True)
    u = sum(
        ca * cb * K.subs(s, (zb - za).subs({dA: eps * dA, dB: eps * dB}))
        for ca, za in a_ch
        for cb, zb in b_ch
    )
    u = sp.series(u, eps, 0, 3).removeO().subs(eps, 1)
    u = sp.expand(sp.simplify(u))
    u_mm = u.coeff(mA, 1).coeff(mB, 1) * mA * mB
    u_km = u.coeff(qA, 1).coeff(mB, 1) * qA * mB + u.coeff(qB, 1).coeff(mA, 1) * qB * mA
    u_kk = u.coeff(qA, 1).coeff(qB, 1) * qA * qB
    return sp.simplify(u_mm), sp.simplify(u_km), sp.simplify(u_kk)


def main() -> None:
    print("=" * 78)
    print("P1 -- TWO-FIELD CLOSURE: what fixes beta_q/beta_d, and what does not")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 78)

    print("\n[CONTROL + STRUCTURE]  massless kernel K = 1/s")
    umm, ukm, ukk = tiers_from_kernel(1 / s)
    print(f"  U_mm = {umm}")
    print(f"  U_km = {sp.factor(ukm)}")
    print(f"  U_kk = {sp.factor(ukk)}")
    f_km = sp.simplify(-sp.diff(ukm, r))
    f_kk = sp.simplify(-sp.diff(ukk, r))
    print(f"  F_km = {sp.factor(f_km)}   F_kk = {sp.factor(f_kk)}")
    c2 = sp.simplify(f_km * r**3 / (qA * dA * mB + qB * dB * mA))
    c3 = sp.simplify(f_kk * r**4 / (qA * dA * qB * dB))
    print(f"  tier coefficients: dipole {c2}, quadrupole {c3}   (the 2 and the 6)")

    print("\n[INVARIANCE]  rescale the dipole moment p -> lambda p (any kappa, any lever")
    print("  convention zeta*r_A):  ell_d -> lambda ell_d, ell_q^2 -> lambda^2 ell_q^2,")
    print("  so ell_q^2/ell_d^2 -- and hence beta_q/beta_d -- is EXACTLY invariant.")
    lam = sp.Symbol("lambda", positive=True)
    ld = sp.Symbol("ell_d", positive=True)
    lq2 = sp.Symbol("ell_q2", positive=True)
    print(
        f"  check: (lambda^2 lq2)/(lambda ld)^2 - lq2/ld^2 = "
        f"{sp.simplify(lam**2 * lq2 / (lam * ld) ** 2 - lq2 / ld**2)}"
    )
    print("  -> the individual beta_d = 2 depends on the convention d = r_A;")
    print("     the RATIO sqrt(6)/2 does not. Only the ratio is physical.")

    print("\n[THE KERNEL INVARIANT]  Lambda(r) = K''' K' / (K'')^2")
    for name, K in (("massless 1/s", 1 / s), ("Yukawa exp(-mu s)/s", sp.exp(-mu * s) / s)):
        lam_r = sp.simplify(sp.diff(K, s, 3) * sp.diff(K, s, 1) / sp.diff(K, s, 2) ** 2).subs(s, r)
        print(f"  {name:<22}: Lambda = {sp.simplify(lam_r)}")
    lam_yuk = sp.simplify(
        (sp.diff(sp.exp(-mu * s) / s, s, 3) * sp.diff(sp.exp(-mu * s) / s, s, 1))
        / sp.diff(sp.exp(-mu * s) / s, s, 2) ** 2
    )
    ser = sp.series(lam_yuk.subs(s, r), mu, 0, 3).removeO()
    print(f"  Yukawa, small mu*r     : Lambda = {sp.expand(ser)}")
    print("  -> Lambda = 3/2 EXACTLY for the massless kernel, at every r;")
    print("     a mediator mass makes Lambda r-dependent and != 3/2.")
    print("     So beta_q/beta_d = sqrt(6)/2 <=> the mediator is massless on the")
    print("     relevant scales. That is the physical content of the prediction.")

    print("\n[WHAT THE FIELD THEORY ADDS -- stated, each item checked or cited]")
    print("  1. ACTION:  S = int d^4x [ (1/2)(d phi)^2 ]")
    print(
        "              + sum_i int dtau [ g m_i + p_i . grad ] phi(x_i),   p_i = kappa k_i r_i/c^2"
    )
    print("     Linear source coupling to a canonical scalar: no ghost, no tachyon,")
    print("     energy bounded below. The k-charge enters via a DERIVATIVE coupling only.")
    print("  2. EP OBSTRUCTION (CANDIDATE-L1) RESOLVED BY RECLASSIFICATION: phi is a")
    print("     FIFTH FORCE, not gravity. Its m-m exchange renormalises G (attractive,")
    print("     absorbed); the repulsive dipole tier violates nothing, because the")
    print("     equivalence principle constrains gravity, not a companion scalar.")
    print("     This names the relaxed assumption CANDIDATE-L1 demanded: 'F_oP is")
    print("     pure gravity' -> 'F_oP = gravity + one scalar fifth force'.")
    print("  3. COSMOLOGICAL LIMIT: on an isotropic background the radial-dipole")
    print("     average is a double layer (zero force off-shell, proven 2026-08-10)")
    print("     and the random average is zero. So this completion contributes ONLY")
    print("     a G-renormalisation to the background expansion -- it CANNOT supply")
    print("     MULTING's H(z) eras at first order. Converges with P2's independent")
    print("     result (MULTING q-blind on background, = LCDM@73).")


if __name__ == "__main__":
    main()
