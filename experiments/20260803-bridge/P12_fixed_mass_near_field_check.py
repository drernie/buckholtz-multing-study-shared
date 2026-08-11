"""P12: does the fixed-mass Yukawa extension P11's skeptic proposed (mu~H0/c,
no density-dependent screening) actually leave the near-field A2/A3/A4 ladder
intact -- the specific, still-open item P11 named and did not check?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
2026-08-12. Reuses P1's own tiers_from_kernel(K) -- already general in the
exchange kernel K(s), used in P1 only to compute the massless case and the
kernel invariant Lambda(r)=K'''K'/K''^2 for a couple of named kernels -- and
applies it directly to the Yukawa kernel exp(-mu*s)/s to get the EXACT
U_mm, U_km, U_kk (and hence F_mm, F_km, F_kk), not just the invariant Lambda.

Two questions this answers directly, by computation rather than order-of-
magnitude assertion:
  1. Does MULTING's near-field power-law ladder (1/r^2, 1/r^3, 1/r^4) survive
     a small but finite mediator mass, and at what order in x=mu*r does each
     tier's leading coefficient first pick up a correction?
  2. Is P1's own kernel invariant Lambda(r) literally the same quantity as
     the actual, physically relevant ell_q^2/ell_d^2 ratio (from the real
     dipole/quadrupole charge construction) for a GENERAL kernel, or only
     for the massless one? (Checked because Lambda and ell_q^2/ell_d^2
     agreeing exactly is a P1 claim this script tests, not assumes.)
"""

import sympy as sp

s, r, mu, x = sp.symbols("s r mu x", positive=True)
mA, mB, qA, qB, dA, dB = sp.symbols("m_A m_B q_A q_B d_A d_B", positive=True)


def tiers_from_kernel(K):
    """Identical to two_field_action_closure.py's own function -- reproduced
    here (not imported) so this script has no import-path dependency on
    that file's module-loading, while using the exact same construction."""
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
    print("P12 -- FIXED-MASS EXTENSION: does it survive the near field?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 78)

    print("\n[CONTROL] massless kernel must reproduce P1's own printed U_mm/U_km/U_kk")
    umm0, ukm0, ukk0 = tiers_from_kernel(1 / s)
    print(f"  U_mm = {umm0}")
    print(f"  U_km = {sp.factor(ukm0)}")
    print(f"  U_kk = {sp.factor(ukk0)}")
    assert sp.simplify(umm0 - mA * mB / r) == 0, "CONTROL FAILED -- U_mm mismatch"
    assert sp.simplify(ukm0 - (dA * mB * qA + dB * mA * qB) / r**2) == 0, "CONTROL FAILED -- U_km"
    assert sp.simplify(ukk0 - 2 * dA * dB * qA * qB / r**3) == 0, "CONTROL FAILED -- U_kk"
    print("  -> matches P1's own printed forms exactly.")

    print("\n[BUILD] exact Yukawa tiers, K(s) = exp(-mu*s)/s")
    K_yuk = sp.exp(-mu * s) / s
    umm, ukm, ukk = tiers_from_kernel(K_yuk)
    print(f"  U_mm = {umm}")
    print(f"  U_km = {sp.simplify(ukm)}")
    print(f"  U_kk = {sp.simplify(ukk)}")
    assert sp.simplify(umm.subs(mu, 0) - umm0) == 0, "mu=0 must recover the massless U_mm"
    assert sp.simplify(ukm.subs(mu, 0) - ukm0) == 0, "mu=0 must recover the massless U_km"
    assert sp.simplify(ukk.subs(mu, 0) - ukk0) == 0, "mu=0 must recover the massless U_kk"
    print("  -> mu=0 limit reproduces the control exactly.")

    f_mm = sp.simplify(-sp.diff(umm, r))
    f_km = sp.simplify(-sp.diff(ukm, r))
    f_kk = sp.simplify(-sp.diff(ukk, r))
    print("\n[FORCES]")
    print(f"  F_mm = {f_mm}")
    print(f"  F_km = {f_km}")
    print(f"  F_kk = {f_kk}")

    print("\n[LEADING-ORDER SURVIVAL] strip each tier's power law, series in x=mu*r")
    print("  (does the power law itself survive, and at what order does the first")
    print("   nonzero fractional correction appear?)")

    def series_fractional(F, r_power, label):
        F_x = sp.simplify(F.subs(mu, x / r) * r**r_power)
        ser = sp.series(F_x, x, 0, 6)
        print(f"  {label} * r^{r_power}, series in x: {ser}")
        return ser

    ser_mm = series_fractional(f_mm, 2, "F_mm")
    ser_km = series_fractional(f_km, 3, "F_km")
    ser_kk = series_fractional(f_kk, 4, "F_kk")

    print("\n  -> leading r^-2, r^-3, r^-4 power laws all survive exactly at x=0;")
    print("     first nonzero correction: monopole O(x^2), dipole O(x^3),")
    print("     quadrupole O(x^4) -- each higher multipole is MORE protected,")
    print("     not less. [Note, added after skeptic review: this is a real but")
    print("     CONSTRUCTION-SPECIFIC pattern (this point-charge, derivative-of-K")
    print("     build), not a general Helmholtz Green's function multipole fact --")
    print("     the standard modified-spherical-Bessel expansion gives O(x^2)")
    print("     uniformly for every multipole order, not staggered by order.]")

    print("\n[NUMERIC] fractional correction at mu*r=1e-4 (cluster scale, mu~H0/c,")
    print("  the physically-motivated scale FINDING_P11's skeptic review proposed)")

    def frac_at(ser, x_val, x_sym=x):
        """Fractional deviation from the leading (x=0) term, evaluated at
        x=x_val. Divides by the leading term SYMBOLICALLY first so the
        common m/q/d charge prefactor cancels before any numeric conversion.
        """
        expanded = sp.expand(ser.removeO())
        leading = expanded.subs(x_sym, 0)
        frac = sp.simplify((expanded - leading) / leading)
        return float(frac.subs(x_sym, x_val))

    x_cluster = 1e-4
    d_mm = frac_at(ser_mm, x_cluster)
    d_km = frac_at(ser_km, x_cluster)
    d_kk = frac_at(ser_kk, x_cluster)
    print(f"  monopole   |dF_mm/F_mm| ~ {abs(d_mm):.3e}")
    print(f"  dipole     |dF_km/F_km| ~ {abs(d_km):.3e}")
    print(f"  quadrupole |dF_kk/F_kk| ~ {abs(d_kk):.3e}")
    print("  -> all utterly negligible; the dipole/quadrupole coefficients that")
    print("     fix beta_d=2, beta_q=sqrt(6) are unaffected at cluster scale.")

    print("\n[CROSS-CHECK] is P1's own Lambda(r)=K'''K'/K''^2 the SAME quantity as")
    print("  the actual ell_q^2/ell_d^2 ratio for a general kernel, or only for K=1/s?")
    K = sp.exp(-mu * s) / s
    lam_yuk = sp.simplify(sp.diff(K, s, 3) * sp.diff(K, s, 1) / sp.diff(K, s, 2) ** 2)
    lam_series = sp.series(lam_yuk.subs(s, r).subs(mu, x / r) / sp.Rational(3, 2), x, 0, 6)
    print(f"  Lambda(x)/Lambda(0), series in x: {lam_series}")

    subs_sym = {mB: mA, qB: qA, dB: dA}  # symmetric-body case for a clean scalar ratio
    fkm_sym = sp.simplify(f_km.subs(subs_sym))
    fkk_sym = sp.simplify(f_kk.subs(subs_sym))
    ratio = sp.simplify(fkk_sym * r**4 / (fkm_sym * r**3) ** 2)
    ratio_norm = sp.simplify(ratio / ratio.subs(mu, 0))
    ratio_series = sp.series(ratio_norm.subs(mu, x / r), x, 0, 6)
    print(f"  [ell_q^2/ell_d^2](x) / [..](0), series in x: {ratio_series}")

    lam_x2_coeff = sp.Poly(lam_series.removeO(), x).coeff_monomial(x**2)
    ratio_x2_coeff = sp.Poly(ratio_series.removeO(), x).coeff_monomial(x**2)
    assert lam_x2_coeff != 0, "expected Lambda to have a nonzero O(x^2) term"
    assert ratio_x2_coeff == 0, "expected the true ratio's O(x^2) term to vanish"
    print("  -> DIFFERENT series (Lambda: leading correction O(x^2); actual ratio:")
    print("     leading correction O(x^3)) -- Lambda(r) is NOT the same quantity as")
    print("     ell_q^2/ell_d^2 for a general kernel. Their equality in P1 is a")
    print("     property specific to K=1/s (where K'(r) happens to equal -1/r^2),")
    print("     not a fact about Lambda in general. The ACTUAL ratio is even MORE")
    print("     protected (higher suppression order) than Lambda alone suggested.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("Near-field power laws (1/r^2, 1/r^3, 1/r^4)  : SURVIVE exactly at x=0,")
    print("                                                first correction at")
    print("                                                O(x^2)/O(x^3)/O(x^4)")
    print("Fractional shift at cluster scale (mu*r~1e-4) : <1e-8 for ALL three tiers")
    print("beta_d=2, beta_q=sqrt(6)                       : SURVIVE to this precision")
    print("P1's Lambda(r) == ell_q^2/ell_d^2 (general K)  : FALSE -- true only for K=1/s")
    print("Sign rule (attract/repel/attract)              : unaffected -- comes from")
    print("                                                the charge algebra, not K(s)")
    print()
    print("This closes the specific open item FINDING_P11 flagged and did not check:")
    print("a fixed-mass mu~H0/c extension is self-consistent with the near-field")
    print("derivation of beta_d=2, beta_q=sqrt(6) to a precision far beyond any")
    print("conceivable observational test.")


if __name__ == "__main__":
    main()
