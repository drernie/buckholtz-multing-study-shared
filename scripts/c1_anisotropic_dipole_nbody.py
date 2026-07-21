"""c1_anisotropic_dipole_nbody.py — test caveat C1 of docs/125/127.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

C1 (the one route that could overturn "background H is q-blind"): P2 and the
G_ab check treated the dipole as a SCALAR radial 1/r^3 force. But the MULTING dipole
is physically an ODD multipole — a VECTOR (the preprint, Eqs. 14-17 + the text at
p.12, describes it as object-A being two spatially-separated sub-masses, so the
effect depends on the ORIENTATION of A's internal axis relative to the line to P).
Does keeping the full anisotropic vector character reintroduce a dipole contribution
to the background expansion?

Method (genuinely different from P2's scalar-radial limit and the G_ab MC): a small
N-body summation with each background object carrying a real dipole moment vector
p_j = q * n_hat_j, interacting with a mass test particle via the exact anisotropic
monopole-dipole force
    F_dip ∝ [ p_j - 3 (p_j·r_hat) r_hat ] / r^3
(the standard dipole field, direction-dependent, not scalarised). The tidal
coefficient d(F_z)/d(delta) on a displaced test particle is measured by finite
difference, summed over a uniform ball of objects, for two orientation ensembles:

  - RANDOM (isotropic) orientations  -> the physical background case (assumption A1)
  - ALIGNED orientations (all p_j ∥ z) -> POSITIVE CONTROL (a coherent, NON-isotropic
    dipole field; violates A1, but proves the anisotropic force is real & detectable)

Prediction (to verify, not assume): the monopole-dipole force is LINEAR in p_j, and
for isotropic orientations <n_hat_j> = 0, so the background (mean-field) dipole tidal
contribution averages to ZERO — a DIFFERENT and more robust washout mechanism than
P2's r->inf limit (odd-multipole isotropy). The aligned control gives a definite
nonzero tidal -> the force is real; alignment (not the scalar reduction) is what
would be needed to source the background, and alignment violates the isotropic
background. Consistent with the beta_cv.py pearl ("dipole degenerate with LCDM at
FIRST order; distinguishable only at SECOND order").

Run:  python scripts/c1_anisotropic_dipole_nbody.py
Exit: 0 if C1 does NOT overturn the washout (random-orientation background ~ 0 while
      the aligned control is nonzero), else 1.
"""

from __future__ import annotations

import sys

import numpy as np

N_OBJ = 4000  # background objects in the ball
N_REAL = 4000  # orientation realizations to average the random ensemble
R_MIN, R_MAX = 0.5, 5.0  # ball shell [r_min, r_max] (r_min avoids the UV near field)
DELTA = 1e-3  # finite-difference test displacement along z
SEED = 20260722  # fixed seed (reproducible; passed explicitly, not Date/rand global)


def _ball_positions(rng: np.random.Generator, n: int) -> np.ndarray:
    """Uniform positions in the spherical shell [R_MIN, R_MAX]."""
    u = rng.uniform((R_MIN / R_MAX) ** 3, 1.0, n)
    r = R_MAX * u ** (1 / 3)
    cost = rng.uniform(-1, 1, n)
    sint = np.sqrt(1 - cost**2)
    phi = rng.uniform(0, 2 * np.pi, n)
    return np.column_stack([r * sint * np.cos(phi), r * sint * np.sin(phi), r * cost])


def _dipole_tidal_z(pos: np.ndarray, dip: np.ndarray) -> float:
    """Finite-difference d(F_z)/d(delta) of the anisotropic monopole-dipole force
    on a mass test particle at (0,0,+-DELTA), summed over objects.

    F_dip_j ∝ [ p_j - 3 (p_j·r_hat) r_hat ] / r^3,  r_vec = x_test - X_j.
    """

    def Fz(delta: float) -> float:
        rv = np.array([0.0, 0.0, delta]) - pos  # (n,3): test - object
        r = np.linalg.norm(rv, axis=1)
        rhat = rv / r[:, None]
        pdotr = np.einsum("ij,ij->i", dip, rhat)
        f = (dip - 3 * pdotr[:, None] * rhat) / r[:, None] ** 3  # (n,3)
        return float(np.sum(f[:, 2]))

    return (Fz(DELTA) - Fz(-DELTA)) / (2 * DELTA)


def main() -> int:
    rng = np.random.default_rng(SEED)
    pos = _ball_positions(rng, N_OBJ)
    q = 1.0  # dipole charge magnitude (q = k_i r_i); scale-free here

    print("=" * 70)
    print("C1 TEST — anisotropic (vector) dipole N-body vs background expansion")
    print("=" * 70)
    print(f"objects={N_OBJ}  shell=[{R_MIN},{R_MAX}]  realizations={N_REAL}  delta={DELTA}")

    # --- ALIGNED control: all dipoles ∥ z (coherent, NON-isotropic) ---------------
    dip_aligned = np.tile([0.0, 0.0, q], (N_OBJ, 1))
    tidal_aligned = _dipole_tidal_z(pos, dip_aligned)

    # --- RANDOM (isotropic) orientations: the physical background case ------------
    tidals = np.empty(N_REAL)
    for k in range(N_REAL):
        cost = rng.uniform(-1, 1, N_OBJ)
        sint = np.sqrt(1 - cost**2)
        phi = rng.uniform(0, 2 * np.pi, N_OBJ)
        nhat = np.column_stack([sint * np.cos(phi), sint * np.sin(phi), cost])
        tidals[k] = _dipole_tidal_z(pos, q * nhat)
    mean_rand = float(np.mean(tidals))
    std_rand = float(np.std(tidals))  # per-realization scatter (the SECOND-ORDER signal)
    sem_rand = std_rand / np.sqrt(N_REAL)  # standard error of the ENSEMBLE MEAN
    zscore = mean_rand / sem_rand  # how many SEM the mean sits from zero

    print("\nBackground dipole tidal coefficient d(F_z)/d(delta):")
    print(f"  ALIGNED (control, ∥z, non-isotropic): {tidal_aligned:+.4e}  (definite)")
    print(f"  RANDOM  ensemble MEAN (= background) : {mean_rand:+.4e}  +/- {sem_rand:.2e} (SEM)")
    print(
        f"          -> z-score from zero         : {zscore:+.2f} sigma  (|z|<~2 = consistent with 0)"
    )
    print(f"  RANDOM  per-realization STD          : {std_rand:.3e}  <- SECOND-ORDER (structure)")
    print(
        f"          NB: STD ({std_rand:.1f}) can exceed |aligned| ({abs(tidal_aligned):.1f}) -> the"
    )
    print("          dipole's real action is LARGE fluctuations (structure), not the (zero) mean.")

    # background = ensemble mean; must be consistent with zero (z-score), control nonzero
    consistent_with_zero = abs(zscore) < 3.0
    control_nonzero = abs(tidal_aligned) > 1e-6

    print("\n" + "=" * 70)
    print("VERDICT")
    print("=" * 70)
    if control_nonzero and consistent_with_zero:
        print("  C1 does NOT overturn the background washout:")
        print("   - RANDOM (isotropic) orientations: background dipole tidal is consistent")
        print(f"     with ZERO ({mean_rand:+.2e} +/- {sem_rand:.1e}) -- the LINEAR-in-p force")
        print("     averages out over orientations (<n_hat>=0), a MORE ROBUST mechanism")
        print("     than P2's scalar-radial r->inf limit (odd-multipole isotropy).")
        print("   - ALIGNED control: definite nonzero tidal -> the anisotropic vector force")
        print("     IS real and the test detects it; but coherent alignment VIOLATES the")
        print("     isotropic background (A1) and is a specific extra assumption, not the")
        print("     corpus's background. So keeping full anisotropy still gives q-blind")
        print("     background H under isotropy.")
        print("   Residual dipole physics lives at SECOND order (dipole-dipole / variance,")
        print("   structure formation), consistent with the beta_cv.py pearl -- NOT H(z).")
        return 0
    print("  UNEXPECTED: random-orientation background tidal is NOT consistent with zero,")
    print(
        f"  or control failed. mean_rand={mean_rand:.3e} sem={sem_rand:.1e} "
        f"aligned={tidal_aligned:.3e}. C1 may overturn the washout -- investigate."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
