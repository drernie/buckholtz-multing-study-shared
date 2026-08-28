"""P155 -- force-level N-body test for MULTING's own quadrupole tier
(docs/125's kappa_qq term), closing the gap FINDING_P154 itself flagged
as not yet done: "a full quadrupole-force N-body analog... was not built."

WHY THIS SCRIPT EXISTS: P154 §Step 3 closed the quadrupole-tier washout
question with an ELEMENTARY check (E[n_hat_A . n_hat_P] = 0 for two
independent isotropic unit vectors) -- correct and sufficient to answer
"is the relevant averaging mechanism zero", but not a FORCE-LEVEL,
tidal-coefficient N-body sum in the same rigor class as P154's own dipole
test (Step 2) or docs/127's original C1 (scripts/c1_anisotropic_dipole_
nbody.py). This script builds that missing piece.

STRUCTURAL FACT THIS RELIES ON (two_charge_completion.py, 2026-08-10,
predates this session -- NOT a new assumption): MULTING's "quadrupole"
tier is the DIPOLE-DIPOLE interaction between two objects' own dipole
moments (k_A*k_P is literally "a product of two bodies' DIPOLE moments",
per that file's own header), not a single-body rank-2 moment. So the
relevant force-level test is: place ONE test object that ITSELF carries
a dipole moment (not a bare mass, unlike C1/P154's test particle) at
(0,0,delta), and measure the tidal coefficient of the dipole-dipole
FORCE it feels from a background population of randomly-oriented dipole
sources -- the direct force-level analog of what P154 did for the
mass-dipole (F_km) channel, now for the dipole-dipole (F_kk) channel.

METHOD -- derive, don't assume: build the dipole-dipole force from the
SAME, already-verified building block P154 established (Phi_dipole =
-(p . grad)[exp(-mu r)/r], and F=+grad(Phi) as the project's own,
c1-matching sign convention) by applying the identical logic ONE LEVEL
UP: the energy of a test dipole p_test sitting in the field sourced by a
source dipole p_src is U_dd = p_test . grad[Phi_dipole(r; p_src, mu)]
(the same p.grad(field) coupling this project's own action, S=integral
of [g*m + p.grad]phi, uses throughout -- not a new coupling rule), and
the force on the test dipole is F_dd = +grad(U_dd), matching the SAME
+grad (not the textbook -grad) convention P154 already established and
verified against c1_anisotropic_dipole_nbody.py. This keeps the whole
derivation chain -- Phi_dipole -> U_dd -> F_dd -- built from ONE
consistent sign rule, applied twice, rather than composing two
independently-guessed conventions (which is exactly how the last sign
bug in P154 happened).

POSITIVE CONTROL: the mu=0 limit of U_dd must match the standard
dipole-dipole interaction formula (up to the SAME overall sign P154's
own Phi/F convention already carries relative to the textbook one -- see
P154's own documented correction) -- checked symbolically before
trusting anything numeric.

NOT_VALIDATION -- NOT_REFUTATION -- OUR_RECONSTRUCTION. Nothing here is a
claim about MULTING's own theory (NO_AUTHOR_ERROR); this bounds only this
project's own reconstruction of whether the quadrupole (dipole-dipole)
tier's background contribution genuinely vanishes under isotropic
averaging, at the force level, not merely via the elementary independence
argument P154 used.
"""

from __future__ import annotations

import sys

import numpy as np
import sympy as sp

# ---------------------------------------------------------------------------
# STEP 1 -- derive the screened dipole-dipole FORCE symbolically, reusing
# P154's own already-verified Phi_dipole building block, applying the SAME
# +grad convention twice (not two independently-chosen sign rules).
# ---------------------------------------------------------------------------

x, y, z, mu = sp.symbols("x y z mu", real=True)
pAx, pAy, pAz = sp.symbols("pAx pAy pAz", real=True)  # source (background) dipole
pTx, pTy, pTz = sp.symbols("pTx pTy pTz", real=True)  # test dipole
r_vec = sp.Matrix([x, y, z])
p_src = sp.Matrix([pAx, pAy, pAz])
p_test = sp.Matrix([pTx, pTy, pTz])
r = sp.sqrt(x**2 + y**2 + z**2)

print("=" * 78)
print("P155 -- quadrupole (dipole-dipole) tier: force-level N-body test")
print("=" * 78)

G_yukawa = sp.exp(-mu * r) / r
Phi_dipole = -(p_src.T * sp.Matrix([sp.diff(G_yukawa, v) for v in (x, y, z)]))[0, 0]
Phi_dipole = sp.simplify(Phi_dipole)

# U_dd = p_test . grad(Phi_dipole) -- SAME p.grad(field) coupling this
# project's own action uses throughout, applied to the ALREADY-VERIFIED
# Phi_dipole from P154, not a new field independently guessed.
# [PERFORMANCE NOTE, same as F_dd below: left unsimplified for speed --
# positive controls substitute concrete values first, then simplify the
# resulting small expression, which is fast and equally rigorous.]
U_dd = (p_test.T * sp.Matrix([sp.diff(Phi_dipole, v) for v in (x, y, z)]))[0, 0]
print("\nU_dd(r_vec; p_test, p_src, mu) derived (not printed in full -- large")
print("unsimplified expression; verified via substituted positive controls below).")

print("\n[POSITIVE CONTROL 1] mu=0 must match the standard dipole-dipole")
print("interaction energy (up to P154's own established +grad, not -grad,")
print("overall sign convention -- see P154's own documented sign note):")
U_dd_mu0 = sp.simplify(U_dd.subs(mu, 0))
rhat = r_vec / r
pt_dot_r = (p_test.T * rhat)[0, 0]
ps_dot_r = (p_src.T * rhat)[0, 0]
pt_dot_ps = (p_test.T * p_src)[0, 0]
# Standard (textbook) dipole-dipole energy: [p_t.p_s - 3(p_t.rhat)(p_s.rhat)]/r^3
U_standard = (pt_dot_ps - 3 * pt_dot_r * ps_dot_r) / r**3
diff_plus = sp.simplify(U_dd_mu0 - U_standard)
diff_minus = sp.simplify(U_dd_mu0 + U_standard)
print(f"  U_dd(mu=0) - U_standard = {diff_plus}")
print(f"  U_dd(mu=0) + U_standard = {diff_minus}")
if diff_minus == 0:
    print("  -> U_dd(mu=0) = -U_standard exactly: the SAME overall sign flip")
    print("     P154 already found (relative to the textbook -grad convention),")
    print("     carried through consistently. Not a new bug -- matches the")
    print("     established, already-verified pattern.")
elif diff_plus == 0:
    print("  -> U_dd(mu=0) = +U_standard exactly.")
else:
    print("  *** NEITHER sign matches the standard dipole-dipole formula.")
    print("  *** This IS a real derivation error. STOP. ***")
    sys.exit(1)
print("  -> PASSED (sign identified and documented, not silently accepted).")

# F_dd = +grad(U_dd) w.r.t. the TEST object's own position -- same +grad
# convention, third application, giving the force on the test dipole.
# [PERFORMANCE NOTE, self-caught after the first attempt hung for >10 min:
# sp.simplify() on the full 9-symbol, third-derivative expression is a
# known-slow case (many simplification strategies tried on a large
# rational-exponential expression). Simplification is a READABILITY
# nicety, not a correctness requirement -- lambdify works fine on the
# raw, unsimplified sp.diff() output, and positive controls below
# substitute concrete values FIRST (collapsing to a small expression)
# before their own, now-cheap, simplify calls. No physics or rigor is
# lost by skipping simplification of the large intermediate form.]
F_dd = sp.Matrix([sp.diff(U_dd, v) for v in (x, y, z)])

print("\n[POSITIVE CONTROL 2] mu=0 force magnitude scaling: dipole-dipole")
print("force must fall off as 1/r^4 (one power steeper than the mass-dipole")
print("force P154 tested, 1/r^3 -- dimensionally required by one extra")
print("derivative), checked on the z-component for a simple aligned case")
print("(p_test=p_src=z_hat, r_vec=(0,0,r0)):")
r0 = sp.Symbol("r0", positive=True)
F_dd_z_aligned = F_dd[2].subs(
    {mu: 0, x: 0, y: 0, z: r0, pTx: 0, pTy: 0, pTz: 1, pAx: 0, pAy: 0, pAz: 1}
)
F_dd_z_aligned = sp.simplify(F_dd_z_aligned)
print(f"  F_dd_z(aligned, mu=0, r=r0) = {F_dd_z_aligned}")
power_check = sp.simplify(F_dd_z_aligned * r0**4)
print(f"  F_dd_z * r0^4 = {power_check}  (must be r0-independent, i.e. a pure 1/r^4 falloff)")
if sp.diff(power_check, r0) != 0:
    print("  *** FAILED -- not a clean 1/r^4 falloff. STOP. ***")
    sys.exit(1)
print("  -> PASSED. Confirmed 1/r^4 scaling, as required.")

F_dd_func = sp.lambdify((x, y, z, mu, pTx, pTy, pTz, pAx, pAy, pAz), list(F_dd), "numpy")

print("\n" + "=" * 78)
print("[STEP 2] isotropic population average of the dipole-dipole FORCE,")
print("test dipole FIXED along z (matching C1/P154's own convention of a")
print("fixed test-object property), background dipoles isotropically")
print("random, mu=1 (ball extends to ~few/mu, physically relevant scale)")
print("=" * 78)

N_OBJ = 2000  # reduced from P154's 4000: force law is a 3rd-derivative
N_REAL = 2000  # expression, more expensive per lambdify call
MU = 1.0
R_MIN, R_MAX = 0.5, 5.0
DELTA = 1e-3
SEED = 20260828
P_TEST_FIXED = np.array([0.0, 0.0, 1.0])  # test dipole along z, fixed


def _ball_positions(rng: np.random.Generator, n: int, r_min: float, r_max: float) -> np.ndarray:
    u = rng.uniform((r_min / r_max) ** 3, 1.0, n)
    r_samp = r_max * u ** (1 / 3)
    cost = rng.uniform(-1, 1, n)
    sint = np.sqrt(1 - cost**2)
    phi = rng.uniform(0, 2 * np.pi, n)
    return np.column_stack(
        [r_samp * sint * np.cos(phi), r_samp * sint * np.sin(phi), r_samp * cost]
    )


def _quad_tidal_z(
    pos: np.ndarray, dip_src: np.ndarray, p_test_vec: np.ndarray, mu_val: float
) -> float:
    """Finite-difference d(F_dd_z)/d(delta) of the dipole-dipole force on a
    TEST DIPOLE (moment p_test_vec, fixed orientation) at (0,0,+-DELTA),
    summed over background dipole objects at `pos` with moments `dip_src`.
    """

    def Fz(delta: float) -> float:
        rv = np.array([0.0, 0.0, delta]) - pos  # (n,3): test - object
        pt = np.tile(p_test_vec, (pos.shape[0], 1))
        _, _, fz = F_dd_func(
            rv[:, 0],
            rv[:, 1],
            rv[:, 2],
            mu_val,
            pt[:, 0],
            pt[:, 1],
            pt[:, 2],
            dip_src[:, 0],
            dip_src[:, 1],
            dip_src[:, 2],
        )
        return float(np.sum(fz))

    return (Fz(DELTA) - Fz(-DELTA)) / (2 * DELTA)


def main() -> int:
    rng = np.random.default_rng(SEED)
    pos = _ball_positions(rng, N_OBJ, R_MIN, R_MAX)
    q = 1.0

    print(f"objects={N_OBJ}  shell=[{R_MIN},{R_MAX}]/mu  mu={MU}  realizations={N_REAL}")
    print(f"test dipole orientation: FIXED along z (p_test={P_TEST_FIXED})")

    print("\n[POSITIVE CONTROL 3] mu=0 numeric sanity: aligned background (all")
    print("z-oriented) against a z-oriented test dipole must give a large,")
    print("definite, SAME-SIGN-THROUGHOUT tidal (both dipoles aligned along")
    print("the measurement axis -- the maximally coherent, non-isotropic case):")
    dip_aligned_mu0 = np.tile([0.0, 0.0, q], (N_OBJ, 1))
    tidal_aligned_mu0 = _quad_tidal_z(pos, dip_aligned_mu0, P_TEST_FIXED, 0.0)
    print(f"  ALIGNED, mu=0: tidal = {tidal_aligned_mu0:+.4e}  (nonzero expected, sanity only)")

    # --- ALIGNED control, screened (mu=MU): coherent, NON-isotropic -------
    dip_aligned = np.tile([0.0, 0.0, q], (N_OBJ, 1))
    tidal_aligned = _quad_tidal_z(pos, dip_aligned, P_TEST_FIXED, MU)

    # --- RANDOM (isotropic) background orientations, screened -------------
    tidals = np.empty(N_REAL)
    for k in range(N_REAL):
        cost = rng.uniform(-1, 1, N_OBJ)
        sint = np.sqrt(1 - cost**2)
        phi = rng.uniform(0, 2 * np.pi, N_OBJ)
        nhat = np.column_stack([sint * np.cos(phi), sint * np.sin(phi), cost])
        tidals[k] = _quad_tidal_z(pos, q * nhat, P_TEST_FIXED, MU)
    mean_rand = float(np.mean(tidals))
    sem_rand = float(np.std(tidals)) / np.sqrt(N_REAL)
    zscore = mean_rand / sem_rand if sem_rand > 0 else float("nan")

    print(f"\nQuadrupole (dipole-dipole) tidal d(F_dd_z)/d(delta), mu={MU}, test dipole fixed:")
    print(f"  ALIGNED (control, non-isotropic bg): {tidal_aligned:+.4e}  (definite)")
    print(f"  RANDOM  bg ensemble MEAN (background) : {mean_rand:+.4e} +/- {sem_rand:.2e} (SEM)")
    print(f"          -> z-score from zero           : {zscore:+.2f} sigma")

    consistent_with_zero = abs(zscore) < 3.0
    control_nonzero = abs(tidal_aligned) > 1e-6

    print("\n" + "=" * 78)
    print("[STEP 3] robustness: also randomize the TEST dipole's own orientation")
    print("per realization (fully isotropic population, not just the background)")
    print("-- a stronger, more symmetric version of Step 2's test")
    print("=" * 78)
    tidals_full = np.empty(N_REAL)
    for k in range(N_REAL):
        cost_t = rng.uniform(-1, 1)
        sint_t = np.sqrt(1 - cost_t**2)
        phi_t = rng.uniform(0, 2 * np.pi)
        p_test_k = np.array([sint_t * np.cos(phi_t), sint_t * np.sin(phi_t), cost_t])
        cost = rng.uniform(-1, 1, N_OBJ)
        sint = np.sqrt(1 - cost**2)
        phi = rng.uniform(0, 2 * np.pi, N_OBJ)
        nhat = np.column_stack([sint * np.cos(phi), sint * np.sin(phi), cost])
        tidals_full[k] = _quad_tidal_z(pos, q * nhat, p_test_k, MU)
    mean_full = float(np.mean(tidals_full))
    sem_full = float(np.std(tidals_full)) / np.sqrt(N_REAL)
    z_full = mean_full / sem_full if sem_full > 0 else float("nan")
    print(
        f"  fully isotropic (test + bg both random): mean={mean_full:+.4e} "
        f"+/-{sem_full:.2e}  z={z_full:+.2f}sigma"
    )
    full_iso_ok = abs(z_full) < 3.0

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if control_nonzero and consistent_with_zero and full_iso_ok:
        print("  Force-level N-body result MATCHES the elementary independence")
        print("  argument P154 used (E[n_hat_A.n_hat_P]=0): the quadrupole")
        print("  (dipole-dipole) tier's isotropic-population-averaged FORCE tidal")
        print("  is consistent with zero, both with a fixed test-dipole orientation")
        print(f"  (mean={mean_rand:+.2e}+/-{sem_rand:.1e}, z={zscore:+.2f}sigma) and with the test")
        print(f"  dipole's own orientation ALSO randomized (mean={mean_full:+.2e}")
        print(f"  +/-{sem_full:.1e}, z={z_full:+.2f}sigma), while the aligned control remains")
        print("  definite. This closes the force-level gap FINDING_P154 itself")
        print("  flagged as not yet built -- the elementary argument and the full")
        print("  force-law N-body computation AGREE, independently.")
        return 0
    print("  UNEXPECTED: the quadrupole force-level result does NOT match the")
    print("  elementary independence argument from P154 -- investigate before")
    print("  trusting either result further.")
    print(f"  mean_rand={mean_rand:.3e} sem={sem_rand:.1e} aligned={tidal_aligned:.3e}")
    print(f"  mean_full={mean_full:.3e} sem_full={sem_full:.1e}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
