"""V1 Relaxation Map, item 2 -- is the killed main branch's Y=0 result an
artifact of the N=3 truncation, or does it survive at larger N?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION. Re-runs the ORIGINAL
(K2-killed) main-branch construction -- A_matter by t-label (commutes with
D_matter, the mechanism that made first-order homogeneous), H_gauge=3(+)3bar,
one-leg gauge action -- for N=3 (already done), N=4, N=5, checking whether
null-space dimension of the first-order constraint on Y stays 0.
"""

import numpy as np

rng = np.random.default_rng(6061)

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


def run_for_N(N: int, n_pairs: int = 6, seed: int = 6061) -> tuple[int, int]:
    rng_local = np.random.default_rng(seed)
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
    assert g2 and anticomm, f"N={N}: matter-side positive control failed"

    P0 = np.zeros((dim_matter, dim_matter))
    P0[:dim_t, :dim_t] = np.eye(dim_t)
    P1 = np.eye(dim_matter) - P0
    dim_full = dim_matter * dim_gauge

    def alg_v1(lam0, lam1, M3):
        M6 = np.block([[M3, np.zeros((3, 3))], [np.zeros((3, 3)), np.eye(3)]])
        return np.kron(lam0 * P0 + lam1 * P1, M6)

    def apply_J_full(vec):
        M = vec.reshape(dim_matter, dim_gauge)
        return (M.conj() @ SWAP.T).reshape(dim_full)

    def right_action(b):
        bstar = b.conj().T
        out = np.zeros_like(b)
        for col in range(b.shape[1]):
            e = np.zeros(b.shape[1], dtype=complex)
            e[col] = 1
            out[:, col] = apply_J_full(bstar @ apply_J_full(e))
        return out

    D_matter_full = np.kron(D_matter, np.eye(dim_gauge))

    # Y-independent part must vanish (as in the original branch) -- checked, not assumed.
    a_probe = alg_v1(1.1 - 0.3j, 0.6 + 0.8j, lam[3])
    y_indep_zero = np.allclose(D_matter_full @ a_probe - a_probe @ D_matter_full, 0, atol=1e-9)
    assert y_indep_zero, f"N={N}: Y-independent part nonzero, reduction invalid"

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

    all_rows = []
    for _ in range(n_pairs):
        a_ = alg_v1(
            rng_local.normal() + 1j * rng_local.normal(),
            rng_local.normal() + 1j * rng_local.normal(),
            lam[rng_local.integers(8)],
        )
        b_ = alg_v1(
            rng_local.normal() + 1j * rng_local.normal(),
            rng_local.normal() + 1j * rng_local.normal(),
            lam[rng_local.integers(8)],
        )
        b_deg = right_action(b_)
        for Yb in Y_basis:
            D_Y = np.kron(gamma_matter, Yb)
            comm1 = D_Y @ a_ - a_ @ D_Y
            comm2 = comm1 @ b_deg - b_deg @ comm1
            all_rows.append(comm2.flatten())

    constraint_matrix = np.array(all_rows).reshape(n_pairs, 36, -1)
    constraint_matrix = np.transpose(constraint_matrix, (0, 2, 1)).reshape(-1, 36)
    real_constraint = np.vstack([constraint_matrix.real, constraint_matrix.imag])
    _, s_y, vh_y = np.linalg.svd(real_constraint, full_matrices=False)
    null_dim = int(np.sum(s_y < 1e-6 * (s_y[0] if len(s_y) else 1.0)))
    return dim_full, null_dim


print("=" * 88)
print("N-TRUNCATION STABILITY: re-running the killed main branch at N=3,4,5")
print("=" * 88)
for N in (3, 4, 5):
    dim_full, null_dim = run_for_N(N)
    print(f"  N={N}: dim(H_full)={dim_full:4d}   null-space dimension of Y = {null_dim} / 36")

print("\n" + "=" * 88)
print("VERDICT")
print("=" * 88)
print(
    "  If null-space stays 0 across N=3,4,5, the K2 conclusion (Y=0 forced) is NOT an"
    " artifact of the small N=3 truncation -- it is a structural feature of the"
    " construction, present at every truncation depth tested. This does not prove it"
    " survives the literal N->infinity limit (not attempted -- would need a genuinely"
    " different, infinite-dimensional-operator technique), but it rules out the cheap"
    " explanation 'N=3 was just too small to see Y come alive'."
)
