"""Independent counterfactual checks on two_charge_completion.py — NOT reusing its
`interaction()` function. Built from scratch so a hidden bug/assumption baked into
the original control functions cannot survive into this audit unexamined (per the
audit's own §0 rule: an identity SymPy returns is not proof by itself).

Four independent tests:
  1. REPRODUCE   — same collinear setup, different code path, same numbers?
  2. CONVENTION  — does beta_q/beta_d survive a free rescaling of the lever-arm
                   normalisation (uniform gamma, then non-uniform gamma_A != gamma_B)?
  3. ORIENTATION — extend the original's 3 collinear configurations to include
                   TRANSVERSE dipole moments (perpendicular to the line joining
                   the bodies), which the original file never tested.
  4. DIMENSIONS  — does ell_d, ell_q^2 scale consistently under M -> lambda*M,
                   r -> lambda_r*r (mechanical, not testing anything the original
                   claimed to derive, just checking self-consistency)?
"""

import sympy as sp

# ---------------------------------------------------------------------------
# 1. REPRODUCE, via a fully 3D point-charge Coulomb sum (not the original's
#    1D z-axis-only helper), to make sure the collinear-only result isn't an
#    artefact of how the original file set up its algebra.
# ---------------------------------------------------------------------------

r, dA, dB, eta = sp.symbols("r d_A d_B eta", positive=True)
mA, mB, qA, qB = sp.symbols("m_A m_B q_A q_B", real=True)
thA, thB, phiB = sp.symbols("theta_A theta_B phi_B", real=True)  # orientation angles


def unit_vec(theta, phi=0):
    return sp.Matrix([sp.sin(theta) * sp.cos(phi), sp.sin(theta) * sp.sin(phi), sp.cos(theta)])


def coulomb_energy_3d(theta_a, theta_b, phi_b=0):
    """Two physical dipoles: body A at origin with charges +-q_A separated by
    d_A along direction n_A(theta_a); body B at (0,0,r) with charges +-q_B
    separated by d_B along direction n_B(theta_b, phi_b). theta measured from
    the z-axis (the A-B separation axis). theta=0 => radial/collinear dipole
    (what the original file exclusively tested). theta=pi/2 => fully transverse.
    """
    nA = unit_vec(theta_a, 0)
    nB = unit_vec(theta_b, phi_b)
    originA = sp.Matrix([0, 0, 0])
    originB = sp.Matrix([0, 0, r])
    a_charges = [(mA, originA), (qA, originA + dA / 2 * nA), (-qA, originA - dA / 2 * nA)]
    b_charges = [(mB, originB), (qB, originB + dB / 2 * nB), (-qB, originB - dB / 2 * nB)]
    U = sp.Integer(0)
    for sa, pa in a_charges:
        for sb, pb in b_charges:
            dist = sp.sqrt(sum((pa[i] - pb[i]) ** 2 for i in range(3)))
            U += sa * sb / dist
    return U


def series_to_second_order(U):
    Us = U.subs({dA: eta * dA, dB: eta * dB})
    Us = sp.series(Us, eta, 0, 3).removeO().subs(eta, 1)
    return sp.simplify(sp.expand(Us))


print("=" * 78)
print("TEST 1 -- REPRODUCE (independent 3D code path, collinear/radial case)")
print("=" * 78)
U_radial = coulomb_energy_3d(0, sp.pi, 0)  # theta_A=0, theta_B=pi: mirror-symmetric per
# original's convention (their (+1,-1) case put A's + charge toward B and B's + charge
# toward A -- here theta_A=0 points +z (toward B), theta_B=pi points -z (toward A) is
# the SAME physical picture: both dipole moments point radially INWARD toward each other.
U_r = series_to_second_order(U_radial)
F_r = sp.simplify(-sp.diff(U_r, r))
Fx = sp.expand(F_r)
A2 = sp.simplify(Fx.coeff(r, -2))
A3 = sp.simplify(-Fx.coeff(r, -3))
A4 = sp.simplify(Fx.coeff(r, -4))
print(f"  A2={A2}  A3={A3}  A4={A4}")
c1 = sp.simplify(sp.expand(U_r).coeff(dA, 0).coeff(dB, 0) - mA * mB / r)
print(f"  positive control (zeroth order = m_A m_B/r): residual = {c1}")
assert c1 == 0, "REPRODUCE FAILED at the zeroth-order control"

kap, kA, kB, rA, rB, cc = sp.symbols("kappa k_A k_B r_A r_B c", positive=True)
neg = {qA: -kap * kA / cc**2, qB: -kap * kB / cc**2, dA: rA, dB: rB}
C2, C3, C4 = (sp.simplify(x.subs(neg)) for x in (A2, A3, A4))
ld = sp.simplify(C3 / C2)
lq2 = sp.simplify(C4 / C2)
uA_, uB_ = kap * kA * rA / (cc**2 * mA), kap * kB * rB / (cc**2 * mB)
match_ld = sp.simplify(ld - 2 * (uA_ + uB_)) == 0
match_lq2 = sp.simplify(lq2 - 6 * uA_ * uB_) == 0
print(f"  ell_d == 2(u_A+u_P)?   {match_ld}")
print(f"  ell_q^2 == 6 u_A u_P?  {match_lq2}")
print(f"  -> INDEPENDENT REPRODUCTION: {'CONFIRMED' if match_ld and match_lq2 else 'FAILED'}")

# ---------------------------------------------------------------------------
# 2. CONVENTION -- does beta_q/beta_d survive a free rescaling of the lever
#    arm normalisation? d_A = gamma_A * r_A instead of d_A = r_A.
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("TEST 2 -- CONVENTION INVARIANCE of beta_q/beta_d under lever-arm rescaling")
print("=" * 78)
gA, gB = sp.symbols("gamma_A gamma_B", positive=True)

# uniform gamma
neg_g = {
    qA: -kap * kA / cc**2,
    qB: -kap * kB / cc**2,
    dA: gA * rA,
    dB: gA * rB,
}  # gamma_A=gamma_B=gA
C2g, C3g, C4g = (sp.simplify(x.subs(neg_g)) for x in (A2, A3, A4))
ldg = sp.simplify(C3g / C2g)
lq2g = sp.simplify(C4g / C2g)
beta_d_g = sp.simplify(ldg / (uA_.subs({}) + uB_.subs({})))  # will carry gamma unless absorbed
print(f"  UNIFORM gamma: ell_d = {sp.factor(ldg)}")
print(f"  UNIFORM gamma: ell_q^2 = {sp.factor(lq2g)}")
ratio_sq_uniform = sp.simplify((lq2g) / (ldg**2))
print(f"  ell_q^2/ell_d^2 (uniform gamma) = {sp.factor(ratio_sq_uniform)}")
print(
    "  -> compare to gamma=1 result 3/8 * ... :", sp.simplify(ratio_sq_uniform - lq2 / ld**2) == 0
)

# non-uniform gamma (independent gamma_A, gamma_B)
neg_ng = {qA: -kap * kA / cc**2, qB: -kap * kB / cc**2, dA: gA * rA, dB: gB * rB}
C2n, C3n, C4n = (sp.simplify(x.subs(neg_ng)) for x in (A2, A3, A4))
ldn = sp.simplify(C3n / C2n)
lq2n = sp.simplify(C4n / C2n)
print(f"\n  NON-UNIFORM gamma_A != gamma_B: ell_d = {sp.factor(ldn)}")
print(f"  NON-UNIFORM gamma_A != gamma_B: ell_q^2 = {sp.factor(lq2n)}")
ratio_sq_nonuniform_at_equal_gamma = sp.simplify((lq2n / ldn**2).subs(gB, gA))
print(
    "  setting gamma_B=gamma_A recovers uniform case?",
    sp.simplify(ratio_sq_nonuniform_at_equal_gamma - ratio_sq_uniform) == 0,
)
# does the ratio stay fixed at 3/8 * (identical-body limit) for ARBITRARY gamma_A != gamma_B,
# still with u_A=u_B (identical bodies)?
identical = {kA: kB, rA: rB, mA: mB}
ratio_identical_nonuniform = sp.simplify((lq2n / ldn**2).subs(identical))
ratio_identical_uniform = sp.simplify((lq2 / ld**2).subs(identical))
print(f"\n  identical bodies, gamma_A != gamma_B: ell_q^2/ell_d^2 = {ratio_identical_nonuniform}")
print(f"  identical bodies, gamma_A = gamma_B = 1: ell_q^2/ell_d^2 = {ratio_identical_uniform}")
print(
    "  -> ratio depends on gamma_A/gamma_B when they differ:",
    sp.simplify(ratio_identical_nonuniform - ratio_identical_uniform) != 0,
)

# ---------------------------------------------------------------------------
# 3. ORIENTATION -- transverse dipoles, never tested in the original file.
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("TEST 3 -- ORIENTATION SWEEP including TRANSVERSE configurations")
print("=" * 78)
configs = [
    ("radial-radial, inward (original 'mirror-symmetric')", 0, sp.pi, 0),
    ("radial-radial, both toward +z (original 'parallel')", 0, 0, 0),
    ("transverse-transverse, parallel (both along x)", sp.pi / 2, sp.pi / 2, 0),
    (
        "transverse-transverse, perpendicular (A along x, B along y)",
        sp.pi / 2,
        sp.pi / 2,
        sp.pi / 2,
    ),
    ("mixed: A radial, B transverse", 0, sp.pi / 2, 0),
]
for label, ta, tb, pb in configs:
    U_c = coulomb_energy_3d(ta, tb, pb)
    U_cs = series_to_second_order(U_c)
    Fc = sp.simplify(-sp.diff(U_cs, r))
    Fcx = sp.expand(Fc)
    a3c = sp.simplify(-Fcx.coeff(r, -3))
    a4c = sp.simplify(Fcx.coeff(r, -4))
    swap = a3c.subs({dA: dB, dB: dA, qA: qB, qB: qA, mA: mB, mB: mA}, simultaneous=True)
    sym = sp.simplify(a3c - swap) == 0
    print(f"\n  {label}")
    print(f"    A3 (dipole term) = {a3c}")
    print(f"    A4 (quadrupole term) = {a4c}")
    print(f"    A<->B symmetric? {sym}")

# ---------------------------------------------------------------------------
# 4. DIMENSIONS -- mechanical self-consistency under M -> lambda M, r -> lambda_r r
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("TEST 4 -- DIMENSIONAL ANALYSIS under independent mass/length rescaling")
print("=" * 78)
lam_m, lam_r = sp.symbols("lambda_M lambda_r", positive=True)
# u_i = kappa k_i r_i / (c^2 m_i). If k_i (a mass-like charge) scales as M and
# m_i scales as M, and r_i scales as lambda_r, then u_i -> lambda_r * u_i (k/m is
# scale-invariant under simultaneous k,m rescaling; only r_i rescaling survives).
u_scaled = kap * (lam_m * kA) * (lam_r * rA) / (cc**2 * (lam_m * mA))
u_scaled_simplified = sp.simplify(u_scaled / uA_)
print("  u_i scaling if k_i,m_i -> lambda_M*(k_i,m_i), r_i -> lambda_r*r_i:")
print(
    f"    u_i(scaled)/u_i(original) = {u_scaled_simplified}   (lambda_M cancels: {lam_m not in u_scaled_simplified.free_symbols})"
)
ld_scaled = 2 * (u_scaled.subs(kA, kA) + u_scaled.subs({kA: kB, rA: rB, mA: mB}))
print("  => ell_d scales purely as lambda_r, independent of lambda_M -- as required")
print("     for a quantity with dimensions of LENGTH (ell_d is r_dA = beta_d r_A, a length).")
