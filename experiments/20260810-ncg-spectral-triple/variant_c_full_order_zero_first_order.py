"""K4 in full generality (step 2 of the two-part gap named at the end of
k4_explicit_s3_via_conjugate_twist.py): build an actual A, J on
H_full = H_matter (x) H_generation for Variant C's H_generation = O(+)O(+)O
(v,s,c, 24-real / 24-complex-dim after complexifying), and run the SAME
order-zero / first-order machinery that killed the earlier SU(3)-triplet
branch (main_experiment_A_Dfull_triality.py) -- not just "does Y commute
with the triality generator U" (already answered: 100/300 nontrivial real
directions), but "does the NCG axiom set itself, independent of U, force
Y=0 the way it did for the killed branch, or not" -- and then INTERSECT the
two answers, since a Y that is triality-covariant but forbidden by
order-zero/first-order would still mean K4 fails.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION. Staged, gated.

SCOPE DECISIONS, stated explicitly because they are choices, not derivations
(same discipline as main_experiment's own docstring):
  - H_generation is COMPLEXIFIED (O(+)O(+)O (x)_R C, 24-complex-dim), to use
    the SAME order-zero/first-order/J-antilinear machinery already validated
    for the killed branch, rather than inventing a separate real-Clifford-
    module axiom set that would not be comparable to the pre-registered
    K1-K4 conditions (which were written for the complex-Hilbert-space
    Connes convention throughout this thread).
  - J_generation = swap(s,c) (x) complex-conjugation, v FIXED. This is not
    an arbitrary choice: 8s/8c are the chirality-conjugate pair (Gamma_chiral
    eigenvalues +-1), 8v is self-dual -- the same role 3/3bar played for the
    killed branch's C^3(+)C^3bar, with v as the natural extra spectator leg
    (a generalisation from 2 legs to 3, not a new idea).
  - A acts on the "s" leg ONLY (one-leg bimodule trick, exactly as required
    to avoid the order-zero failure mode already found and fixed once in
    main_experiment): identity on v and c. J's right-action then produces
    the algebra's image on c (the leg J swaps s into), never touching the
    same leg as pi(a) -- mirroring the working 3/3bar construction exactly.
  - Y_gen: general complex-Hermitian 24x24 (576 real parameters) -- the
    direct analogue of main_experiment's complex-Hermitian 6x6 Y, not the
    real-symmetric 24x24 (300 params) k4_explicit_s3_via_conjugate_twist.py
    used for its narrower "commutes with U" question. Both are legitimate
    objects; this script's Y_gen matches the convention main_experiment's
    D_full/order-zero/first-order machinery was built for.
"""

import numpy as np

rng = np.random.default_rng(20260811)

# =============================================================================
# STAGE 0 -- H_matter: reused verbatim from main_experiment_A_Dfull_triality.py
# (N=3 truncation, same D_matter, gamma_matter).
# =============================================================================
print("=" * 88)
print("STAGE 0 -- H_matter (reused, N=3 truncation)")
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
print(f"  dim(H_matter)={dim_matter}, gamma^2=I: {g2}, {{gamma,D}}=0: {anticomm}")
if not (g2 and anticomm):
    raise SystemExit("STAGE 0 FAILED; stop")
print("  STAGE 0 PASSED\n")

# =============================================================================
# STAGE 1 -- octonion multiplication + su(3) on Im(O) (reused verbatim from
# k4_explicit_s3_via_conjugate_twist.py Stage 1a, dimensions re-verified).
# =============================================================================
print("=" * 88)
print("STAGE 1 -- octonion su(3) generators on the 8-dim leg (reused, re-verified)")
print("=" * 88)
QUAT_MULT = np.zeros((4, 4, 4))
_qtab = {
    (0, 0): (1, 0),
    (0, 1): (1, 1),
    (0, 2): (1, 2),
    (0, 3): (1, 3),
    (1, 0): (1, 1),
    (1, 1): (-1, 0),
    (1, 2): (1, 3),
    (1, 3): (-1, 2),
    (2, 0): (1, 2),
    (2, 1): (-1, 3),
    (2, 2): (-1, 0),
    (2, 3): (1, 1),
    (3, 0): (1, 3),
    (3, 1): (1, 2),
    (3, 2): (-1, 1),
    (3, 3): (-1, 0),
}
for (a, b), (sign, c) in _qtab.items():
    QUAT_MULT[a, b, c] = sign


def qmul(p, q):
    return np.einsum("i,j,ijk->k", p, q, QUAT_MULT)


def qconj(p):
    return p * np.array([1, -1, -1, -1])


def omul(x, y):
    a, b = x
    c, d = y
    return (qmul(a, c) - qmul(qconj(d), b), qmul(d, a) + qmul(b, qconj(c)))


def oconj(x):
    a, b = x
    return (qconj(a), -b)


def to_oct(v8):
    return (v8[:4], v8[4:])


def from_oct(x):
    return np.concatenate(x)


O_BASIS = [(np.eye(4)[i], np.zeros(4)) for i in range(4)] + [
    (np.zeros(4), np.eye(4)[i]) for i in range(4)
]
C8 = np.zeros((8, 8, 8))
for i in range(8):
    for j in range(8):
        C8[i, j, :] = from_oct(omul(O_BASIS[i], O_BASIS[j]))

c_full = C8[1:8, 1:8, 1:8]
eye7 = np.eye(7)
antisym_basis = []
for a in range(7):
    for b in range(a + 1, 7):
        M = np.zeros((7, 7))
        M[a, b], M[b, a] = 1, -1
        antisym_basis.append(M)
n_anti = len(antisym_basis)
rows = []
for i in range(7):
    for j in range(7):
        eiej = c_full[i, j, :]
        for lw in range(7):
            row = np.zeros(n_anti)
            for b_idx, B in enumerate(antisym_basis):
                lhs_l = (B @ eiej)[lw]
                Xei, Xej = B @ eye7[i], B @ eye7[j]
                rhs1_l = np.einsum("k,k->", Xei, c_full[:, j, lw])
                rhs2_l = np.einsum("k,k->", Xej, c_full[i, :, lw])
                row[b_idx] = lhs_l - rhs1_l - rhs2_l
            rows.append(row)
_, s, vh = np.linalg.svd(np.array(rows), full_matrices=False)
g2_dim = int(np.sum(s < 1e-8 * s[0]))
g2_coords = vh[vh.shape[0] - g2_dim :, :]
g2_basis = [sum(g2_coords[r, b] * antisym_basis[b] for b in range(n_anti)) for r in range(g2_dim)]
e1 = eye7[0]
action_matrix = np.array([M @ e1 for M in g2_basis]).T
_, s2, vh2 = np.linalg.svd(action_matrix, full_matrices=True)
n_rank = int(np.sum(s2 > 1e-8 * (s2[0] if len(s2) else 1.0)))
su3_dim = action_matrix.shape[1] - n_rank
su3_coords = vh2[vh2.shape[0] - su3_dim :, :]
su3_basis_7 = [sum(su3_coords[r, k] * g2_basis[k] for k in range(g2_dim)) for r in range(su3_dim)]
print(f"  dim(g2)={g2_dim} (expect 14), dim(su3)={su3_dim} (expect 8)")
if g2_dim != 14 or su3_dim != 8:
    raise SystemExit("STAGE 1 FAILED; stop")
su3_basis_8 = []
for M7 in su3_basis_7:
    M8 = np.zeros((8, 8))
    M8[1:8, 1:8] = M7
    su3_basis_8.append(M8)
print("  STAGE 1 PASSED\n")

# =============================================================================
# STAGE 2 -- H_generation = C (x)_R (O(+)O(+)O), 24-complex-dim, ordered
# [v(8), s(8), c(8)]. A_gen = the algebra generated by su3_basis_8 acting on
# the s-block ALONE (one-leg trick), identity elsewhere -- closure computed,
# not assumed, mirroring main_experiment's own Burnside check.
# =============================================================================
print("=" * 88)
print("STAGE 2 -- H_generation=C^24 (v,s,c), A_gen closure on the s-leg (Burnside-style)")
print("=" * 88)
dim_gen = 24
V0, S0, C0 = 0, 8, 16  # block offsets


def embed_s_leg(M8: np.ndarray) -> np.ndarray:
    """Acts as M8 on the s-block (indices 8:16), identity on v and c."""
    M = np.eye(dim_gen, dtype=complex)
    M[S0 : S0 + 8, S0 : S0 + 8] = M8
    return M


su3_gen_ops = [embed_s_leg(M8.astype(complex)) for M8 in su3_basis_8]
# Burnside-style closure of the associative algebra generated by these 8
# generators acting on the 8-dim s-block ALONE (identity elsewhere), i.e.
# closure of su3_basis_8 itself as an algebra on C^8 (since the s-leg is
# the only place it acts nontrivially, closure on the full 24-dim space is
# exactly closure on the 8-dim block, padded with identity elsewhere).
gen8 = [M8.astype(complex) for M8 in su3_basis_8]
span = [g.flatten() for g in gen8] + [(1j * g).flatten() for g in gen8]
frontier = list(gen8)
for _ in range(4):  # a few product-depth rounds; saturation checked below
    new_frontier = []
    for P in frontier:
        for T in gen8:
            new_frontier.append(P @ T)
    for P in new_frontier:
        vec = P.flatten()
        real_stack = np.array([np.concatenate([v.real, v.imag]) for v in span])
        target = np.concatenate([vec.real, vec.imag])
        coeffs, *_ = np.linalg.lstsq(real_stack.T, target, rcond=None)
        rec = real_stack.T @ coeffs
        if np.max(np.abs(rec - target)) > 1e-8:
            span.append(vec)
    frontier = new_frontier[:16]
real_stack = np.array([np.concatenate([v.real, v.imag]) for v in span])
A_s_real_dim = int(np.linalg.matrix_rank(real_stack, tol=1e-8))
print(f"  real-dimension of algebra generated by su(3) on the 8-dim s-leg: {A_s_real_dim}")
print("  (expected < 128=dim_R M_8(C): the 8-leg rep is REDUCIBLE, 1+1+3+3bar under su(3),")
print("   so Schur's lemma forbids full saturation -- this is expected, not a failure)")
print("  STAGE 2 PASSED (informational; A_gen below is defined directly as span{su3_gen_ops},")
print("  the generating set itself -- sufficient for order-zero/first-order, which only need")
print("  A's generators, not a closed-form description of the whole algebra)\n")

# =============================================================================
# STAGE 3 -- J_full = J_matter (x) J_generation, J_generation = swap(s,c) o
# conjugate, v fixed. Compute (J^2, JD, Jgamma) signs -- reported, not assumed.
# =============================================================================
print("=" * 88)
print("STAGE 3 -- J_full signs (computed, not assumed)")
print("=" * 88)
SWAP_SC = np.eye(dim_gen)
SWAP_SC[S0 : S0 + 8, S0 : S0 + 8] = 0
SWAP_SC[C0 : C0 + 8, C0 : C0 + 8] = 0
SWAP_SC[S0 : S0 + 8, C0 : C0 + 8] = np.eye(8)
SWAP_SC[C0 : C0 + 8, S0 : S0 + 8] = np.eye(8)
# sanity: SWAP_SC^2 = I, fixes v-block
swap_ok = np.allclose(SWAP_SC @ SWAP_SC, np.eye(dim_gen)) and np.allclose(
    SWAP_SC[V0 : V0 + 8, V0 : V0 + 8], np.eye(8)
)
print(f"  SWAP_SC^2=I and fixes v-block: {swap_ok}")
if not swap_ok:
    raise SystemExit("STAGE 3 FAILED -- SWAP_SC malformed; stop")

dim_full = dim_matter * dim_gen
I_gen = np.eye(dim_gen)
gamma_full = np.kron(gamma_matter, I_gen)
D_matter_full = np.kron(D_matter, I_gen)


def apply_J_full(vec: np.ndarray) -> np.ndarray:
    M = vec.reshape(dim_matter, dim_gen)
    Mc = M.conj()
    out = Mc @ SWAP_SC.T
    return out.reshape(dim_full)


test_vecs = [rng.normal(size=dim_full) + 1j * rng.normal(size=dim_full) for _ in range(4)]
j2_signs = []
for v in test_vecs:
    v2 = apply_J_full(apply_J_full(v))
    ratio = np.vdot(v, v2) / np.vdot(v, v)
    j2_signs.append(ratio.real)
j2_consistent = np.allclose(j2_signs, j2_signs[0], atol=1e-8) and np.isclose(
    abs(j2_signs[0]), 1.0, atol=1e-8
)
print(f"  J_full^2 = {j2_signs[0]:+.4f} * I (consistent: {j2_consistent})")
if not j2_consistent:
    raise SystemExit("STAGE 3 FAILED -- J_full^2 not a consistent scalar; stop")

JD_signs = []
for v in test_vecs:
    lhs = apply_J_full(D_matter_full @ v)
    rhs_plus = D_matter_full @ apply_J_full(v)
    JD_signs.append(np.vdot(rhs_plus, lhs).real / np.vdot(rhs_plus, rhs_plus).real)
jd_sign = (
    np.sign(np.mean(JD_signs))
    if np.allclose(np.abs(JD_signs), np.abs(JD_signs[0]), atol=1e-6)
    else 0
)
Jgamma_signs = []
for v in test_vecs:
    lhs = apply_J_full(gamma_full @ v)
    rhs = gamma_full @ apply_J_full(v)
    Jgamma_signs.append(np.vdot(rhs, lhs).real / np.vdot(rhs, rhs).real)
jg_sign = (
    np.sign(np.mean(Jgamma_signs))
    if np.allclose(np.abs(Jgamma_signs), np.abs(Jgamma_signs[0]), atol=1e-6)
    else 0
)
print(
    f"  (epsilon,eta,eta') = ({j2_signs[0]:+.0f},{jd_sign:+.0f},{jg_sign:+.0f}) -- reported, not matched to a target"
)
print("  STAGE 3 PASSED\n")

# =============================================================================
# STAGE 4 -- order-zero: [pi(a), b(deg)] = 0 for random A-elements, Y-independent.
# =============================================================================
print("=" * 88)
print("STAGE 4 -- order-zero condition [a,b(deg)]=0 (Y-independent)")
print("=" * 88)
P0 = np.zeros((dim_matter, dim_matter))
P0[:dim_t, :dim_t] = np.eye(dim_t)
P1 = np.eye(dim_matter) - P0


def alg_elt_full(lam0: complex, lam1: complex, M8: np.ndarray) -> np.ndarray:
    return np.kron(lam0 * P0 + lam1 * P1, embed_s_leg(M8.astype(complex)))


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
    a_ = alg_elt_full(
        rng.normal() + 1j * rng.normal(),
        rng.normal() + 1j * rng.normal(),
        su3_basis_8[rng.integers(8)],
    )
    b_ = alg_elt_full(
        rng.normal() + 1j * rng.normal(),
        rng.normal() + 1j * rng.normal(),
        su3_basis_8[rng.integers(8)],
    )
    b_deg = right_action(b_)
    comm = a_ @ b_deg - b_deg @ a_
    if np.max(np.abs(comm)) > 1e-6:
        oz_ok = False
print(f"  [a, b(deg)] = 0 for random A-elements: {oz_ok}")
if not oz_ok:
    raise SystemExit(
        "STAGE 4 FAILED -- order-zero violated before Y is introduced; the s-leg-only "
        "representation + swap(s,c)-conjugate J combination is structurally inconsistent. "
        "Recorded honestly -- this is real information about the one-leg-trick choice, "
        "not a bug to silently patch. Stop."
    )
print("  STAGE 4 PASSED\n")

# =============================================================================
# STAGE 5 -- first-order: does [D_matter(x)I, a] vanish identically (so the
# Y-independent part drops out, reducing to a homogeneous constraint on Y)?
# =============================================================================
print("=" * 88)
print("STAGE 5 -- first-order: Y-independent part")
print("=" * 88)
a_probe = alg_elt_full(1.3 - 0.4j, -0.7 + 0.9j, su3_basis_8[2])
Y_indep_term = D_matter_full @ a_probe - a_probe @ D_matter_full
y_indep_zero = np.allclose(Y_indep_term, 0, atol=1e-9)
print(f"  [D_matter(x)I, a] = 0 identically: {y_indep_zero}")
if not y_indep_zero:
    raise SystemExit("STAGE 5 FAILED -- Y-independent part nonzero; reduction below invalid, stop")
print("  STAGE 5 PASSED\n")

# =============================================================================
# STAGE 6 -- solve first-order for Y_gen (complex-Hermitian 24x24, 576 real
# params). Memory-bounded: n_pairs kept small (dim_full=288, so comm2 flattens
# to 288^2=82944 rows PER Y_basis element PER pair -- checked to stay under a
# few GB before running).
# =============================================================================
print("=" * 88)
print("STAGE 6 -- first-order: solving for what it forces on Y_gen (complex-Hermitian 24x24)")
print("=" * 88)
Y_basis = []
for k in range(dim_gen):
    E = np.zeros((dim_gen, dim_gen), dtype=complex)
    E[k, k] = 1
    Y_basis.append(E)
for k in range(dim_gen):
    for ell in range(k + 1, dim_gen):
        E1 = np.zeros((dim_gen, dim_gen), dtype=complex)
        E1[k, ell] = 1
        E1[ell, k] = 1
        Y_basis.append(E1)
        E2 = np.zeros((dim_gen, dim_gen), dtype=complex)
        E2[k, ell] = 1j
        E2[ell, k] = -1j
        Y_basis.append(E2)
n_Y = len(Y_basis)
assert n_Y == dim_gen * dim_gen
herm_ok = all(np.allclose(Yb, Yb.conj().T) for Yb in Y_basis[:5])
print(f"  Y basis: {n_Y} matrices (spot-checked Hermitian: {herm_ok})")

n_pairs = 4  # stability check: 2 pairs already reduced 576->1; 2 more pairs confirm it's not luck
est_rows = n_pairs * dim_full * dim_full
est_gb = (
    est_rows * n_Y * 8 * 2 / 1e9
)  # complex->real doubles the column count effectively via stacking rows
print(
    f"  planned: n_pairs={n_pairs}, dim_full={dim_full}, estimated matrix ~{est_rows * 2}x{n_Y} "
    f"(~{est_rows * 2 * n_Y * 8 / 1e9:.2f} GB) -- building per-pair, not all at once, to bound peak memory"
)

null_basis_current = np.eye(n_Y, dtype=complex)  # current candidate subspace, as columns
for pair_idx in range(n_pairs):
    a_ = alg_elt_full(
        rng.normal() + 1j * rng.normal(),
        rng.normal() + 1j * rng.normal(),
        su3_basis_8[rng.integers(8)],
    )
    b_ = alg_elt_full(
        rng.normal() + 1j * rng.normal(),
        rng.normal() + 1j * rng.normal(),
        su3_basis_8[rng.integers(8)],
    )
    b_deg = right_action(b_)
    rows = []
    for Yb in Y_basis:
        D_Y_part = np.kron(gamma_matter, Yb)
        comm1 = D_Y_part @ a_ - a_ @ D_Y_part
        comm2 = comm1 @ b_deg - b_deg @ comm1
        rows.append(comm2.flatten())
    constraint_matrix = np.array(rows).T  # (dim_full^2, n_Y)
    # restrict to the current candidate subspace (columns = null_basis_current)
    restricted = constraint_matrix @ null_basis_current  # (dim_full^2, current_dim)
    real_restricted = np.vstack([restricted.real, restricted.imag])
    _, sv, vh = np.linalg.svd(real_restricted, full_matrices=False)
    cur_dim = null_basis_current.shape[1]
    null_dim_local = int(np.sum(sv < 1e-6 * (sv[0] if len(sv) else 1.0))) + max(
        0, vh.shape[0] - min(real_restricted.shape)
    )
    # coordinates (in the restricted basis) of the null space
    null_coords = (
        vh[len(sv) - null_dim_local :, :] if null_dim_local > 0 else np.zeros((0, cur_dim))
    )
    null_basis_current = null_basis_current @ null_coords.T.astype(complex)
    print(
        f"  pair {pair_idx + 1}/{n_pairs}: candidate subspace dim {cur_dim} -> {null_basis_current.shape[1]}"
    )
    if null_basis_current.shape[1] == 0:
        break

null_dim_y = null_basis_current.shape[1]
print(f"\n  first-order null-space dimension (allowed Y_gen's): {null_dim_y} out of {n_Y}")
if null_dim_y == 0:
    print("\n  -> FIRST-ORDER FORCES Y_gen=0 EXACTLY for this (A,J) choice on Variant C's")
    print("  H_generation. This is a genuine, independent kill of the s-leg-only")
    print("  representation -- reported honestly even though it removes the covariant")
    print("  directions found in k4_explicit_s3_via_conjugate_twist.py Stage 6.")
else:
    Y_solutions = [null_basis_current[:, k].reshape(1, -1) for k in range(min(null_dim_y, 4))]
    print(f"  -> {null_dim_y}-complex-dimensional family of Y_gen's survives first-order.")

# =============================================================================
# STAGE 7 -- intersect with triality-covariance: does the surviving Y_gen
# space overlap with directions genuinely commuting with the order-3 U built
# in k4_explicit_s3_via_conjugate_twist.py? Rebuilds U here (same search,
# same discipline) rather than importing state across files.
# =============================================================================
print("\n" + "=" * 88)
print("STAGE 7 -- intersect first-order-surviving Y_gen with triality-covariant Y_gen")
print("=" * 88)
if null_dim_y == 0:
    print("  SKIPPED -- first-order already forces Y_gen=0; no space left to intersect.")
else:
    conj_sign = np.array([1.0 if k == 0 else -1.0 for k in range(8)])

    def trilinear_T(v, s, c):
        v_bar = oconj(to_oct(v))
        prod = from_oct(omul(v_bar, to_oct(s)))
        return float(np.dot(c, prod))

    def conj8(v):
        return v * conj_sign

    N_TRIALS = 20
    v_trials = [rng.normal(size=8) for _ in range(N_TRIALS)]
    s_trials = [rng.normal(size=8) for _ in range(N_TRIALS)]
    c_trials = [rng.normal(size=8) for _ in range(N_TRIALS)]
    lhs_trials = [trilinear_T(v_trials[k], s_trials[k], c_trials[k]) for k in range(N_TRIALS)]
    import itertools

    hits = []
    for perm in itertools.permutations([0, 1, 2]):
        for conj_mask in itertools.product([0, 1], repeat=3):
            max_resid = 0.0
            for k in range(N_TRIALS):
                base = [v_trials[k], s_trials[k], c_trials[k]]
                twisted = [conj8(base[i]) if conj_mask[i] else base[i] for i in range(3)]
                args = [twisted[perm[0]], twisted[perm[1]], twisted[perm[2]]]
                rhs = trilinear_T(args[0], args[1], args[2])
                max_resid = max(max_resid, abs(lhs_trials[k] - rhs))
            if max_resid < 1e-9:
                hits.append((perm, conj_mask))

    def perm_order(p):
        n = len(p)
        cur = list(range(n))
        o = 0
        while True:
            cur = [p[c] for c in cur]
            o += 1
            if cur == list(range(n)):
                return o

    three_cycles = [(perm, mask) for perm, mask in hits if perm_order(perm) == 3]
    CONJ8 = np.diag(conj_sign)

    def build_cycle_operator(perm, mask):
        U = np.zeros((24, 24))
        for k in range(3):
            src = perm[k]
            block = CONJ8 if mask[src] else np.eye(8)
            U[8 * k : 8 * k + 8, 8 * src : 8 * src + 8] = block
        return U

    U_found = None
    for perm, mask in three_cycles:
        Uc = build_cycle_operator(perm, mask)
        if np.max(np.abs(Uc @ Uc @ Uc - np.eye(24))) < 1e-9:
            U_found = Uc
            break
    if U_found is None:
        print("  order-3 U not reproducible here (unexpected divergence from prior script) -- stop")
    else:
        U_c = U_found.astype(complex)
        rows = []
        for k in range(null_dim_y):
            Yk = null_basis_current[:, k].reshape(dim_gen, dim_gen)
            comm = U_c @ Yk - Yk @ U_c
            rows.append(comm.flatten())
        M = np.array(rows)  # (null_dim_y, dim_gen^2), rows index the candidate basis
        real_M = np.vstack([M.real, M.imag])
        _, sv2, vh2 = np.linalg.svd(real_M.T, full_matrices=False)
        overlap_dim = int(np.sum(sv2 < 1e-6 * (sv2[0] if len(sv2) else 1.0)))
        print(
            f"  of the {null_dim_y} first-order-surviving directions, {overlap_dim} ALSO commute with U"
        )
        if overlap_dim > 0:
            coords = vh2[len(sv2) - overlap_dim :, :]
            id_like = 0
            for r in range(overlap_dim):
                Ycombo = sum(
                    coords[r, k] * null_basis_current[:, k].reshape(dim_gen, dim_gen)
                    for k in range(null_dim_y)
                )
                proj = np.trace(Ycombo) / dim_gen
                if np.max(np.abs(Ycombo - proj * np.eye(dim_gen))) < 1e-6:
                    id_like += 1
            print(
                f"  of those, proportional-to-identity (trivial): {id_like}; genuinely nontrivial: {overlap_dim - id_like}"
            )

print("\n" + "=" * 88)
print("SUMMARY")
print("=" * 88)
print(f"  order-zero (s-leg-only A, swap(s,c)+conj J): {oz_ok}")
print(f"  first-order null-space dim (out of {n_Y}): {null_dim_y}")
