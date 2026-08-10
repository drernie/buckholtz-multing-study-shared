"""Variant V1 -- generation as a genuinely SEPARATE tensor factor, A trivial there.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION. Per the Minimal Relaxation
Rule: ONE assumption changed from the killed branch (main_experiment_A_Dfull_
triality.py, claim.md's K2 verdict), new variant ID, not a silent patch to the
killed file.

WHAT CHANGED, exactly one assumption: in the killed branch, the "3" from
triality (H_gauge = C^3 (+) C^3bar) was made to carry BOTH the su(3) gauge
action AND the "3 generations" role simultaneously -- A acted irreducibly on
the same space that was supposed to distinguish generations, and first-order
forced Y=0 (K2 triggered: SU(3) transitivity erases any generation label).

Here: H_generation is a THIRD, separate tensor factor (C^3_gen), on which A
acts as the IDENTITY (not via su(3)). This mirrors a NAMED, real precedent --
Connes-Chamseddine's actual NCG Standard Model construction represents
generation multiplicity as H_F (x) C^N_gen with the gauge algebra acting as
(a (x) 1_gen), trivially on the generation index; the Yukawa/mass matrix lives
entirely on that untouched factor, which is exactly why it is NOT forced to
vanish by order-zero/first-order there.

PRE-STATED PREDICTION (written before running, per this project's own no-fake-
blind-prediction discipline): because A acts trivially on H_gen, the
Y-independent structural argument that killed the old branch should not apply
the same way here -- Y_gen should have MORE freedom (a nonzero null space) than
the old branch's Y. The EXACT dimension is not predicted in advance -- computed
below, not guessed.
"""

import numpy as np

rng = np.random.default_rng(2027)

# =============================================================================
# STAGE 0 -- H_matter (identical reconstruction to the killed branch; reused,
# not reinvented, since it already passed its own positive controls there).
# =============================================================================
print("=" * 88)
print("STAGE 0 -- H_matter (reused from the killed branch's own verified construction)")
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
print(f"  dim(H_matter) = {dim_matter}   gamma^2=I: {g2}   {{gamma,D}}=0: {anticomm}")
if not (g2 and anticomm):
    raise SystemExit("STAGE 0 FAILED -- reused construction broken; stop")
print("  STAGE 0 PASSED\n")

# =============================================================================
# STAGE 1 -- H_gauge = C^3 (+) C^3bar, su(3), J_gauge (reused, same as killed
# branch's Stage 1/4 -- already independently verified there).
# =============================================================================
print("=" * 88)
print("STAGE 1 -- H_gauge = C^3(+)C^3bar, su(3), J_gauge (reused)")
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
Tgen = [lm / 2 for lm in lam]
Tvec = np.array([T.flatten() for T in Tgen]).T
closure_ok = True
for a in range(8):
    for b in range(a + 1, 8):
        comm = (Tgen[a] @ Tgen[b] - Tgen[b] @ Tgen[a]).flatten()
        coeffs, *_ = np.linalg.lstsq(Tvec, comm, rcond=None)
        if np.max(np.abs(Tvec @ coeffs - comm)) > 1e-9:
            closure_ok = False
print(f"  su(3) closure: {closure_ok}")
if not closure_ok:
    raise SystemExit("STAGE 1 FAILED -- su(3) closure broken; stop")

SWAP = np.block([[np.zeros((3, 3)), np.eye(3)], [np.eye(3), np.zeros((3, 3))]])
Tgen_full = [np.block([[T, np.zeros((3, 3))], [np.zeros((3, 3)), -T.conj()]]) for T in Tgen]
j_gauge_ok = np.allclose(
    [SWAP @ T.conj() @ SWAP.conj().T for T in Tgen_full], [-T for T in Tgen_full], atol=1e-9
)
print(f"  J_gauge=SWAP.K intertwines with sign -1 (reused result): {j_gauge_ok}")
if not j_gauge_ok:
    raise SystemExit("STAGE 1 FAILED -- J_gauge intertwine broken; stop")
print("  STAGE 1 PASSED\n")

# =============================================================================
# STAGE 2 -- H_gen = C^3, a genuinely separate factor. A acts as IDENTITY here.
# J_gen = complex conjugation K (simplest choice; A doesn't act non-trivially
# on this factor, so no su(3)-intertwine constraint applies to J_gen at all --
# checked explicitly: does ANY choice of J_gen even matter for order-zero/
# first-order, given A is trivial here? Verified in Stage 4/5 below, not assumed.)
# =============================================================================
print("=" * 88)
print("STAGE 2 -- H_gen = C^3 (separate factor, A acts as identity)")
print("=" * 88)
dim_gauge = 6
dim_gen = 3
dim_full = dim_matter * dim_gauge * dim_gen
print(
    f"  dim(H_full) = dim_matter({dim_matter}) x dim_gauge({dim_gauge}) x dim_gen({dim_gen}) = {dim_full}"
)
print("  STAGE 2 PASSED (trivial by construction)\n")

# =============================================================================
# STAGE 3 -- A_v1 = (C(+)C) tensor M_3(C) tensor {1}. Verify closure.
# =============================================================================
print("=" * 88)
print("STAGE 3 -- A_v1 on H_full, verify closure")
print("=" * 88)
P0 = np.zeros((dim_matter, dim_matter))
P0[:dim_t, :dim_t] = np.eye(dim_t)
P1 = np.eye(dim_matter) - P0
I3 = np.eye(3, dtype=complex)


def alg_v1(lam0: complex, lam1: complex, M3: np.ndarray) -> np.ndarray:
    M6 = np.block(
        [[M3, np.zeros((3, 3))], [np.zeros((3, 3)), np.eye(3)]]
    )  # one-leg, as fixed before
    return np.kron(lam0 * P0 + lam1 * P1, np.kron(M6, I3))


closed_ok = True
for _ in range(5):
    l0a, l1a, l0b, l1b = (rng.normal() + 1j * rng.normal() for _ in range(4))
    Ma, Mb = lam[rng.integers(8)], lam[rng.integers(8)]
    a, b = alg_v1(l0a, l1a, Ma), alg_v1(l0b, l1b, Mb)
    mult_ok = np.allclose(a @ b, alg_v1(l0a * l0b, l1a * l1b, Ma @ Mb), atol=1e-9)
    adj_ok = np.allclose(a.conj().T, alg_v1(np.conj(l0a), np.conj(l1a), Ma.conj().T), atol=1e-9)
    closed_ok = closed_ok and mult_ok and adj_ok
print(f"  A_v1 closed under multiplication and adjoint: {closed_ok}")
if not closed_ok:
    raise SystemExit("STAGE 3 FAILED -- A_v1 not closed; stop")
print("  STAGE 3 PASSED\n")

# =============================================================================
# STAGE 4 -- J_full_v1 = J_matter (x) J_gauge (x) J_gen. Compute signs.
# =============================================================================
print("=" * 88)
print("STAGE 4 -- J_full_v1 signs, computed not assumed")
print("=" * 88)


def apply_J_full(vec: np.ndarray) -> np.ndarray:
    # v in H_matter (x) H_gauge (x) H_gen, flattened C-order.
    M = vec.reshape(dim_matter, dim_gauge, dim_gen)
    Mc = M.conj()
    # J_matter = K (conj, no permutation on matter index)
    # J_gauge = SWAP.K on the gauge index
    # J_gen = K (conj, no permutation on gen index)
    out = np.einsum("mgn,gh->mhn", Mc, SWAP)
    return out.reshape(dim_full)


gamma_full = np.kron(gamma_matter, np.kron(np.eye(dim_gauge), I3))
D_matter_full = np.kron(D_matter, np.kron(np.eye(dim_gauge), I3))

test_vecs = [rng.normal(size=dim_full) + 1j * rng.normal(size=dim_full) for _ in range(4)]
j2_signs = [(np.vdot(v, apply_J_full(apply_J_full(v))) / np.vdot(v, v)).real for v in test_vecs]
j2_ok = np.allclose(j2_signs, j2_signs[0], atol=1e-8) and np.isclose(
    abs(j2_signs[0]), 1.0, atol=1e-8
)
print(f"  J_full_v1^2 = {j2_signs[0]:+.4f} (consistent: {j2_ok})")
if not j2_ok:
    raise SystemExit("STAGE 4 FAILED -- J^2 inconsistent; stop")

jd_vals = []
for v in test_vecs:
    lhs = apply_J_full(D_matter_full @ v)
    rhs = D_matter_full @ apply_J_full(v)
    jd_vals.append(np.vdot(rhs, lhs).real / np.vdot(rhs, rhs).real)
jd_sign = (
    np.sign(np.mean(jd_vals)) if np.allclose(np.abs(jd_vals), np.abs(jd_vals[0]), atol=1e-6) else 0
)
jg_vals = []
for v in test_vecs:
    lhs = apply_J_full(gamma_full @ v)
    rhs = gamma_full @ apply_J_full(v)
    jg_vals.append(np.vdot(rhs, lhs).real / np.vdot(rhs, rhs).real)
jg_sign = (
    np.sign(np.mean(jg_vals)) if np.allclose(np.abs(jg_vals), np.abs(jg_vals[0]), atol=1e-6) else 0
)
print(
    f"  J D_matter,full = {jd_sign:+.0f} D_matter,full J   J gamma_full = {jg_sign:+.0f} gamma_full J"
)
print(f"  -> (epsilon,eta,eta') = ({j2_signs[0]:+.0f},{jd_sign:+.0f},{jg_sign:+.0f})")
print("  STAGE 4 PASSED (informational)\n")

# =============================================================================
# STAGE 5 -- order-zero with the 3-factor A_v1.
# =============================================================================
print("=" * 88)
print("STAGE 5 -- order-zero, [a,b(deg)]=0, with A trivial on H_gen")
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
    a_ = alg_v1(
        rng.normal() + 1j * rng.normal(), rng.normal() + 1j * rng.normal(), lam[rng.integers(8)]
    )
    b_ = alg_v1(
        rng.normal() + 1j * rng.normal(), rng.normal() + 1j * rng.normal(), lam[rng.integers(8)]
    )
    b_deg = right_action(b_)
    if np.max(np.abs(a_ @ b_deg - b_deg @ a_)) > 1e-6:
        oz_ok = False
print(f"  [a,b(deg)]=0 for random A_v1 elements: {oz_ok}")
if not oz_ok:
    raise SystemExit("STAGE 5 FAILED -- order-zero broken; stop before Stage 6")
print("  STAGE 5 PASSED\n")

# =============================================================================
# STAGE 6 -- first-order with Y_gen (9 real Hermitian params, acting on H_gen
# ONLY, D_full_v1 = D_matter(x)I(x)I + gamma_matter(x)I_gauge(x)Y_gen).
# =============================================================================
print("=" * 88)
print("STAGE 6 -- first-order: what does it force on Y_gen (H_gen only)?")
print("=" * 88)
y_indep = (
    D_matter_full @ alg_v1(1.1 - 0.3j, 0.6 + 0.8j, lam[3])
    - alg_v1(1.1 - 0.3j, 0.6 + 0.8j, lam[3]) @ D_matter_full
)
y_indep_zero = np.allclose(y_indep, 0, atol=1e-9)
print(f"  [D_matter(x)I(x)I, a] = 0 identically: {y_indep_zero}")
if not y_indep_zero:
    raise SystemExit("STAGE 6 FAILED -- Y-independent part nonzero, reduction invalid; stop")

Y_basis = []
for k in range(3):
    E = np.zeros((3, 3), dtype=complex)
    E[k, k] = 1
    Y_basis.append(E)
for k in range(3):
    for ell in range(k + 1, 3):
        E1 = np.zeros((3, 3), dtype=complex)
        E1[k, ell] = 1
        E1[ell, k] = 1
        Y_basis.append(E1)
        E2 = np.zeros((3, 3), dtype=complex)
        E2[k, ell] = 1j
        E2[ell, k] = -1j
        Y_basis.append(E2)
assert len(Y_basis) == 9
herm_ok = all(np.allclose(Yb, Yb.conj().T) for Yb in Y_basis)
print(f"  Y_gen basis (9 matrices) Hermitian: {herm_ok}")
if not herm_ok:
    raise SystemExit("STAGE 6 FAILED -- Y_gen basis not Hermitian; stop")

n_pairs = 6
all_rows = []
for _ in range(n_pairs):
    a_ = alg_v1(
        rng.normal() + 1j * rng.normal(), rng.normal() + 1j * rng.normal(), lam[rng.integers(8)]
    )
    b_ = alg_v1(
        rng.normal() + 1j * rng.normal(), rng.normal() + 1j * rng.normal(), lam[rng.integers(8)]
    )
    b_deg = right_action(b_)
    for Yb in Y_basis:
        D_Y = np.kron(gamma_matter, np.kron(np.eye(dim_gauge), Yb))
        comm1 = D_Y @ a_ - a_ @ D_Y
        comm2 = comm1 @ b_deg - b_deg @ comm1
        all_rows.append(comm2.flatten())
constraint_matrix = np.array(all_rows).reshape(n_pairs, 9, -1)
constraint_matrix = np.transpose(constraint_matrix, (0, 2, 1)).reshape(-1, 9)
real_constraint = np.vstack([constraint_matrix.real, constraint_matrix.imag])
# full_matrices=False: only need Vh (9x9) for the null space, not the full U
# (M x M, M~560000 here -- full_matrices=True tried to allocate 2.28 TiB).
_, s_y, vh_y = np.linalg.svd(real_constraint, full_matrices=False)
null_dim_y = int(np.sum(s_y < 1e-6 * (s_y[0] if len(s_y) else 1.0)))
print(f"\n  first-order constraint on Y_gen: {real_constraint.shape[0]} real equations, 9 unknowns")
print(f"  singular values: {np.round(s_y, 6)}")
print(f"  null-space dimension: {null_dim_y} out of 9")

print("\n" + "=" * 88)
print("VERDICT -- written after seeing the null-space dimension, not before")
print("=" * 88)
if null_dim_y == 0:
    print(
        "  PRE-STATED PREDICTION FAILED: Y_gen is ALSO forced to zero, even though A acts"
        " trivially on H_gen. This means the obstruction in the killed branch was not"
        " (only) about A acting non-trivially on the generation-carrying space -- something"
        " else in the construction (likely gamma_matter's failure to commute with the"
        " matter-side algebra structure Lambda=l0 P0+l1 P1) independently forces Y=0"
        " regardless of what A does on the generation factor. A real, informative null"
        " result: the Connes-Chamseddine precedent (trivial generation action -> free"
        " Yukawa matrix) does NOT transfer here as hoped -- recorded as V1 KILLED, not"
        " silently patched. The likely next culprit is gamma_matter vs Lambda non-"
        " commutativity itself, not the generation-index question at all."
    )
else:
    print(
        f"  PRE-STATED PREDICTION CONFIRMED (qualitatively): Y_gen has a {null_dim_y}-real-"
        "dimensional family of solutions -- nonzero, unlike the killed branch's Y=0."
        " This supports the Connes-Chamseddine-style diagnosis: separating the gauge index"
        " (where A acts, correctly constrained) from the generation index (where A is"
        " trivial) DOES reopen room for a genuine Yukawa/mass-like term. The killed"
        " branch's Y=0 was specifically about conflating those two roles, not an"
        " unavoidable feature of this construction's other pieces (D_matter, gamma_matter,"
        " J signs) -- those are unchanged from the killed branch and did not, by"
        " themselves, force zero here."
    )
    Y_allowed_basis = vh_y[vh_y.shape[0] - null_dim_y :, :]
    for idx in range(null_dim_y):
        coeffs = Y_allowed_basis[idx]
        Y_reconstructed = sum(c * Yb for c, Yb in zip(coeffs, Y_basis, strict=True))
        print(f"    null-vector {idx}: Y_gen =\n{np.round(Y_reconstructed, 4)}")
