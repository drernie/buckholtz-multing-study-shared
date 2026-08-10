"""V1 Relaxation Map, item 1 -- A_matter built from gamma's OWN eigenprojectors
instead of D_matter's t-label. Fixes [a,gamma]=0 (the axiom V1 found violated)
but breaks [D_matter,a]=0 (which was making the old first-order homogeneous).

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION. Minimal Relaxation Rule:
one assumption changed from the killed main branch (A_matter's basis), H_gauge
kept as-is (3(+)3bar, since V1 already showed the generation side is not the
bottleneck).

THE KEY CONSEQUENCE, worked out analytically before coding (stated here, then
verified): [D_matter, a] is now NONZERO in general (checked directly earlier:
12.08 for a specific l0,l1), so the Y-INDEPENDENT part of the first-order
condition no longer vanishes automatically. The full condition becomes
INHOMOGENEOUS: [Y-independent forcing term] + [Y-dependent linear map](Y) = 0
for every (a,b) pair simultaneously. A solution Y may not exist at all --
checked here by solving the combined inhomogeneous least-squares system and
inspecting the RESIDUAL, not just a null-space dimension.
"""

import numpy as np

rng = np.random.default_rng(5051)

# =============================================================================
# STAGE 0 -- H_matter, D_matter, gamma_matter (reused, verified).
# =============================================================================
print("=" * 88)
print("STAGE 0 -- H_matter, D_matter, gamma_matter (reused)")
print("=" * 88)
N = 3
basis_t0 = [(n, s) for n in range(N) for s in (+1, -1)]
basis_t1 = [(n, s) for n in range(N) for s in (+1, -1)]
dim_t = len(basis_t0)
dim_matter = 2 * dim_t


def Dt_eigenvalue(n: int, sigma: int, t: int) -> float:
    return sigma * (n + 1.5) + (t - 0.5) * 3


D_matter = np.zeros((dim_matter, dim_matter))
for i, (n, s) in enumerate(basis_t0):
    D_matter[i, i] = Dt_eigenvalue(n, s, 0)
for i, (n, s) in enumerate(basis_t1):
    D_matter[dim_t + i, dim_t + i] = Dt_eigenvalue(n, s, 1)

gamma_matter = np.zeros((dim_matter, dim_matter))
for i, (n, s) in enumerate(basis_t0):
    j = basis_t1.index((n, -s))
    gamma_matter[dim_t + j, i] = 1
    gamma_matter[i, dim_t + j] = 1

g2 = np.allclose(gamma_matter @ gamma_matter, np.eye(dim_matter))
anticomm = np.allclose(gamma_matter @ D_matter + D_matter @ gamma_matter, 0)
print(f"  dim(H_matter)={dim_matter}  gamma^2=I: {g2}  {{gamma,D}}=0: {anticomm}")
if not (g2 and anticomm):
    raise SystemExit("STAGE 0 FAILED; stop")
print("  STAGE 0 PASSED\n")

# =============================================================================
# STAGE 1 -- NEW A_matter basis: gamma's OWN eigenprojectors, not t-labels.
# =============================================================================
print("=" * 88)
print("STAGE 1 -- A_matter from gamma's eigenprojectors")
print("=" * 88)
Pplus = (np.eye(dim_matter) + gamma_matter) / 2
Pminus = (np.eye(dim_matter) - gamma_matter) / 2
proj_ok = (
    np.allclose(Pplus @ Pplus, Pplus)
    and np.allclose(Pminus @ Pminus, Pminus)
    and np.allclose(Pplus + Pminus, np.eye(dim_matter))
)
print(f"  Pplus, Pminus are complementary projectors: {proj_ok}")
if not proj_ok:
    raise SystemExit("STAGE 1 FAILED; stop")

l0_test, l1_test = 1.3 - 0.4j, -0.9 + 0.6j
Lam_new = l0_test * Pplus + l1_test * Pminus
comm_gamma = np.max(np.abs(gamma_matter @ Lam_new - Lam_new @ gamma_matter))
comm_D = np.max(np.abs(D_matter @ Lam_new - Lam_new @ D_matter))
print(f"  [gamma, Lambda_new] = {comm_gamma:.2e} (expect 0, the FIX)")
print(f"  [D_matter, Lambda_new] = {comm_D:.4f} (expect NONZERO, the TRADE-OFF)")
if comm_gamma > 1e-9:
    raise SystemExit("STAGE 1 FAILED -- the whole point of this variant is [gamma,Lambda]=0; stop")
if comm_D < 1e-6:
    print(
        "  NOTE: [D_matter,Lambda_new] came out ~0 -- unexpected, the trade-off may not apply here"
    )
print("  STAGE 1 PASSED\n")

# =============================================================================
# STAGE 2 -- H_gauge = 3(+)3bar, su(3), J_gauge (reused, verified).
# =============================================================================
print("=" * 88)
print("STAGE 2 -- H_gauge, su(3), J_gauge (reused)")
print("=" * 88)
i_ = 1j
lam = [
    np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex),
    np.array([[0, -i_, 0], [i_, 0, 0], [0, 0, 0]], dtype=complex),
    np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex),
    np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex),
    np.array([[0, 0, -i_], [0, 0, 0], [i_, 0, 0]], dtype=complex),
    np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex),
    np.array([[0, 0, 0], [0, 0, -i_], [0, i_, 0]], dtype=complex),
    (1 / np.sqrt(3)) * np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex),
]
SWAP = np.block([[np.zeros((3, 3)), np.eye(3)], [np.eye(3), np.zeros((3, 3))]])
dim_gauge = 6
print("  STAGE 2 PASSED (reused, dim_gauge=6)\n")

# =============================================================================
# STAGE 3 -- A_full = Lambda_new (x) M6 (one-leg gauge action, as fixed in the
# main experiment). Verify closure.
# =============================================================================
print("=" * 88)
print("STAGE 3 -- A_full closure")
print("=" * 88)


def alg_gamma(lam0: complex, lam1: complex, M3: np.ndarray) -> np.ndarray:
    Lam = lam0 * Pplus + lam1 * Pminus
    M6 = np.block([[M3, np.zeros((3, 3))], [np.zeros((3, 3)), np.eye(3)]])
    return np.kron(Lam, M6)


closed_ok = True
for _ in range(5):
    l0a, l1a, l0b, l1b = (rng.normal() + 1j * rng.normal() for _ in range(4))
    Ma, Mb = lam[rng.integers(8)], lam[rng.integers(8)]
    a, b = alg_gamma(l0a, l1a, Ma), alg_gamma(l0b, l1b, Mb)
    mult_ok = np.allclose(a @ b, alg_gamma(l0a * l0b, l1a * l1b, Ma @ Mb), atol=1e-9)
    adj_ok = np.allclose(a.conj().T, alg_gamma(np.conj(l0a), np.conj(l1a), Ma.conj().T), atol=1e-9)
    closed_ok = closed_ok and mult_ok and adj_ok
print(f"  A_full closed under multiplication and adjoint: {closed_ok}")
if not closed_ok:
    raise SystemExit("STAGE 3 FAILED; stop")
print("  STAGE 3 PASSED\n")

# =============================================================================
# STAGE 4 -- J_full = J_matter(K) (x) J_gauge(SWAP.K). Re-verify signs (should
# be unchanged from the main experiment since J itself did not change, but
# checked, not assumed -- A changed, J did not).
# =============================================================================
print("=" * 88)
print("STAGE 4 -- J_full signs (re-verified, J unchanged but re-checked)")
print("=" * 88)
dim_full = dim_matter * dim_gauge


def apply_J_full(vec: np.ndarray) -> np.ndarray:
    M = vec.reshape(dim_matter, dim_gauge)
    return (M.conj() @ SWAP.T).reshape(dim_full)


gamma_full = np.kron(gamma_matter, np.eye(dim_gauge))
D_matter_full = np.kron(D_matter, np.eye(dim_gauge))
test_vecs = [rng.normal(size=dim_full) + 1j * rng.normal(size=dim_full) for _ in range(4)]
j2_signs = [(np.vdot(v, apply_J_full(apply_J_full(v))) / np.vdot(v, v)).real for v in test_vecs]
j2_ok = np.allclose(j2_signs, j2_signs[0], atol=1e-8) and np.isclose(
    abs(j2_signs[0]), 1.0, atol=1e-8
)
print(f"  J_full^2 = {j2_signs[0]:+.4f} (consistent: {j2_ok})")
if not j2_ok:
    raise SystemExit("STAGE 4 FAILED; stop")
print("  STAGE 4 PASSED\n")

# =============================================================================
# STAGE 5 -- order-zero with the NEW A_full. Must be re-verified since A
# changed (its basis is different, even though the one-leg gauge trick and J
# themselves are unchanged).
# =============================================================================
print("=" * 88)
print("STAGE 5 -- order-zero with the new (gamma-eigenspace) A")
print("=" * 88)


def right_action(b: np.ndarray) -> np.ndarray:
    bstar = b.conj().T
    out = np.zeros_like(b)
    for col in range(b.shape[1]):
        e = np.zeros(b.shape[1], dtype=complex)
        e[col] = 1
        out[:, col] = apply_J_full(bstar @ apply_J_full(e))
    return out


oz_ok = True
for _ in range(4):
    a_ = alg_gamma(
        rng.normal() + 1j * rng.normal(), rng.normal() + 1j * rng.normal(), lam[rng.integers(8)]
    )
    b_ = alg_gamma(
        rng.normal() + 1j * rng.normal(), rng.normal() + 1j * rng.normal(), lam[rng.integers(8)]
    )
    b_deg = right_action(b_)
    if np.max(np.abs(a_ @ b_deg - b_deg @ a_)) > 1e-6:
        oz_ok = False
print(f"  [a,b(deg)]=0 for random A_full elements: {oz_ok}")
if not oz_ok:
    raise SystemExit(
        "STAGE 5 FAILED -- order-zero broken with the new A. This is itself a real"
        " finding (the gamma-eigenspace algebra is incompatible with THIS J at the"
        " order-zero level, before even reaching first-order) -- stop, do not proceed"
        " to an inhomogeneous first-order test on top of a broken order-zero."
    )
print("  STAGE 5 PASSED\n")

# =============================================================================
# STAGE 6 -- THE DECISIVE TEST: inhomogeneous first-order. Does ANY Y exist?
# =============================================================================
print("=" * 88)
print("STAGE 6 -- inhomogeneous first-order: does ANY Y satisfy it?")
print("=" * 88)
Y_basis = []
for k in range(6):
    E = np.zeros((6, 6), dtype=complex)
    E[k, k] = 1
    Y_basis.append(E)
for k in range(6):
    for ell in range(k + 1, 6):
        E1 = np.zeros((6, 6), dtype=complex)
        E1[k, ell] = 1
        E1[ell, k] = 1
        Y_basis.append(E1)
        E2 = np.zeros((6, 6), dtype=complex)
        E2[k, ell] = 1j
        E2[ell, k] = -1j
        Y_basis.append(E2)
assert len(Y_basis) == 36

n_pairs = 6
A_rows = []  # Y-dependent coefficient rows
b_rows = []  # Y-independent forcing terms (RHS, negated below)
for _ in range(n_pairs):
    a_ = alg_gamma(
        rng.normal() + 1j * rng.normal(), rng.normal() + 1j * rng.normal(), lam[rng.integers(8)]
    )
    b_ = alg_gamma(
        rng.normal() + 1j * rng.normal(), rng.normal() + 1j * rng.normal(), lam[rng.integers(8)]
    )
    b_deg = right_action(b_)

    # Y-independent forcing term: [[D_matter(x)I, a], b_deg]
    comm0 = D_matter_full @ a_ - a_ @ D_matter_full
    forcing = comm0 @ b_deg - b_deg @ comm0
    b_rows.append(forcing.flatten())

    for Yb in Y_basis:
        D_Y = np.kron(gamma_matter, Yb)
        comm1 = D_Y @ a_ - a_ @ D_Y
        comm2 = comm1 @ b_deg - b_deg @ comm1
        A_rows.append(comm2.flatten())

A_mat = np.array(A_rows).reshape(n_pairs, 36, -1)
A_mat = np.transpose(A_mat, (0, 2, 1)).reshape(-1, 36)  # (n_pairs*dim^2) x 36
b_vec = np.array(b_rows).reshape(-1)  # (n_pairs*dim^2,)

# Solve A_mat @ y = -b_vec (least squares), then check the ACTUAL residual --
# an inhomogeneous system may have NO exact solution; residual > 0 tells us
# that directly, not a null-space dimension (which only answers the
# homogeneous question).
A_real = np.vstack([A_mat.real, A_mat.imag])
rhs_real = np.concatenate([-b_vec.real, -b_vec.imag])
y_sol, residuals, rank, sv = np.linalg.lstsq(A_real, rhs_real, rcond=None)
actual_residual = np.linalg.norm(A_real @ y_sol - rhs_real)
rhs_norm = np.linalg.norm(rhs_real)
print(f"  system: {A_real.shape[0]} equations, 36 unknowns, rank={rank}")
print(f"  ||RHS (Y-independent forcing)|| = {rhs_norm:.4f}  (0 would mean homogeneous again)")
print(
    f"  ||A@y_sol - RHS|| (actual residual of the LEAST-SQUARES solution) = {actual_residual:.6f}"
)
print(f"  relative residual = {actual_residual / max(rhs_norm, 1e-12):.6f}")

print("\n" + "=" * 88)
print("VERDICT")
print("=" * 88)
if actual_residual < 1e-6 * max(rhs_norm, 1):
    print(
        "  A Y EXISTS satisfying first-order (residual ~0). The gamma-eigenspace algebra"
        " choice, despite breaking [D_matter,a]=0, still admits a consistent generation-"
        " mixing term. This would be a genuine escape from K2's conclusion via a"
        " different A_matter basis -- inspect y_sol's structure before trusting this."
    )
else:
    print(
        "  NO Y satisfies first-order exactly (residual is a real fraction of the RHS"
        " scale, not numerical noise). The inhomogeneous system is INCONSISTENT: fixing"
        " [a,gamma]=0 by switching to gamma's eigenprojectors does not just fail to help,"
        " it makes the system UNSOLVABLE rather than merely over-constrained to Y=0."
        " KILLED for a different, sharper reason than the original branch: not"
        " 'Y=0 is forced', but 'no Y satisfies the axioms at all' with this A_matter choice."
    )
