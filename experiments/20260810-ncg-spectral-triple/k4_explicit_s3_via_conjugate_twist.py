"""K4, step 1: find the explicit order-3 S_3 triality generator by EXHAUSTIVE
SEARCH over (permutation, conjugation-twist) pairs, instead of trusting a
recalled formula for a non-associative algebra.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION. Staged, gated.

WHY A SEARCH, NOT A DERIVED FORMULA. explicit_s3_automorphism.py found: naive
same-basis cyclic relabeling of the octonion structure constants C8_conj
fails on the full 8-dim O (residual 2.0), and speculated a "companion
twist/rotation" was needed. Re-deriving the exact twist symbolically from
octonion identities by hand is exactly the class of error this project's own
rules warn about (non-associative algebra, sign/convention traps
everywhere -- "an identity SymPy returns is not proof by itself"). Since
conjugation of a REAL BASIS VECTOR e_k is just a sign (+1 for k=0, -1
otherwise) rather than a change of basis direction, the space of candidate
"permutation + conjugation-pattern" symmetries is FINITE (6 permutations x 8
conjugation subsets = 48 candidates) and can be checked EXHAUSTIVELY, directly
on random vectors, with zero reliance on memory.

FIRST, A CONSISTENCY FIX. rebuild_ob11_spinor_lift.py / variant_c_...py build
Gamma_chiral via the Pauli-tensor Jordan-Wigner construction (COMPLEX 16-dim
Dirac spinors of Cl(8,0)_C, chirality eigenspaces 8-COMPLEX-dim each).
explicit_s3_automorphism.py builds Gamma directly from octonion
multiplication (REAL 16-dim, O(+)O, chirality eigenspaces 8-REAL-dim each --
the Majorana-Weyl real form that exists specifically because 8=0 mod 8 in
the real Clifford classification). These are DIFFERENT representations
(a complexification is not the same object as its real form), so before
building anything on top of the octonion-direct Gamma, this file re-verifies
Variant C's key finding (does the octonion-lifted su(3) commute with
Gamma_chiral?) IN THIS representation specifically -- closing a real
cross-file consistency gap rather than silently assuming compatibility.

A BUG CAUGHT AND REMOVED (recorded, not hidden). The first version of Stage 2
searched through an intermediate re-indexed tensor R[p,q,r]=C8[q,r,p] as a
translation layer between the tensor-level search and the operator-level
trilinear_T used later. That translation had an index-order error: the
"tautological" 3-cycle it identified was NOT tautological when checked
directly (residual 2.0, not 0), and the "real" 3-cycle it identified did NOT
reproduce trilinear_T on random vectors either (residual ~11, not 0) -- both
candidates were artifacts of the R-layer bug, not of the underlying algebra.
Fixed by removing the R layer entirely: the search below operates directly on
trilinear_T from the start, checked on random (non-basis) vectors in every
trial, so there is no translation step left to get wrong.
"""

import itertools

import numpy as np

rng = np.random.default_rng(9090)

# =============================================================================
# STAGE 0 -- octonion multiplication (reused, verified in explicit_s3_automorphism.py).
# =============================================================================
print("=" * 88)
print("STAGE 0 -- octonion multiplication (reused)")
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


def qmul(p: np.ndarray, q: np.ndarray) -> np.ndarray:
    return np.einsum("i,j,ijk->k", p, q, QUAT_MULT)


def qconj(p: np.ndarray) -> np.ndarray:
    return p * np.array([1, -1, -1, -1])


def omul(x: tuple, y: tuple) -> tuple:
    a, b = x
    c, d = y
    return (qmul(a, c) - qmul(qconj(d), b), qmul(d, a) + qmul(b, qconj(c)))


def oconj(x: tuple) -> tuple:
    a, b = x
    return (qconj(a), -b)


O_BASIS = [(np.eye(4)[i], np.zeros(4)) for i in range(4)] + [
    (np.zeros(4), np.eye(4)[i]) for i in range(4)
]


def to_oct(v8: np.ndarray) -> tuple:
    return (v8[:4], v8[4:])


def from_oct(x: tuple) -> np.ndarray:
    return np.concatenate(x)


C8 = np.zeros((8, 8, 8))
for i in range(8):
    for j in range(8):
        C8[i, j, :] = from_oct(omul(O_BASIS[i], O_BASIS[j]))

x8_test = rng.normal(size=8)
prod = from_oct(omul(to_oct(x8_test), oconj(to_oct(x8_test))))
if not np.allclose(prod, np.array([np.sum(x8_test**2)] + [0] * 7)):
    raise SystemExit("STAGE 0 FAILED; stop")
print("  composition-algebra positive control: PASSED\n")

# =============================================================================
# STAGE 1 -- Gamma(e_a), Gamma_chiral, from octonion multiplication directly
# (reused construction from explicit_s3_automorphism.py, re-verified here).
# =============================================================================
print("=" * 88)
print("STAGE 1 -- octonion-direct Gamma(e_a), Cl(8,0), Gamma_chiral (reused, re-verified)")
print("=" * 88)


def Gamma_matrix(a: int) -> np.ndarray:
    G = np.zeros((16, 16))
    ea = to_oct(np.eye(8)[a])
    ea_bar = oconj(ea)
    for k in range(8):
        ek = np.eye(8)[k]
        G[8:, k] = from_oct(omul(ea_bar, to_oct(ek)))
        G[:8, 8 + k] = from_oct(omul(ea, to_oct(ek)))
    return G


Gam = [Gamma_matrix(a) for a in range(8)]
cliff_ok = all(
    np.max(np.abs(Gam[a] @ Gam[b] + Gam[b] @ Gam[a] - 2.0 * (a == b) * np.eye(16))) < 1e-9
    for a in range(8)
    for b in range(8)
)
print(f"  full Cl(8,0) on all 64 pairs: {cliff_ok}")
if not cliff_ok:
    raise SystemExit("STAGE 1 FAILED; stop")

GammaChiral = np.eye(16)
for a in range(8):
    GammaChiral = GammaChiral @ Gam[a]
eigvals = np.linalg.eigvalsh((GammaChiral + GammaChiral.T) / 2)
n_plus, n_minus = int(np.sum(eigvals > 0)), int(np.sum(eigvals < 0))
print(f"  Gamma_chiral: 16 = 8s({n_plus}) (+) 8c({n_minus}), real: {(n_plus, n_minus) == (8, 8)}")
if (n_plus, n_minus) != (8, 8):
    raise SystemExit("STAGE 1 FAILED -- chirality split wrong; stop")
print("  STAGE 1 PASSED\n")

# =============================================================================
# STAGE 1a -- CONSISTENCY FIX: re-verify Variant C's key finding (su(3)
# commutes with Gamma_chiral) IN THIS representation, not borrowed from the
# Pauli-tensor one. Reuses rebuild_ob11_triality.py's su(3)-on-Im(O)
# construction (unchanged, that part is representation-independent -- it is
# an 8x8 real matrix acting on the octonion coordinates themselves) and lifts
# it via S(X) = (1/4) sum X_ab Gamma_a Gamma_b using THIS file's Gamma.
# =============================================================================
print("=" * 88)
print("STAGE 1a -- re-verify su(3) commutes with Gamma_chiral, octonion-direct rep")
print("=" * 88)
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
    raise SystemExit("STAGE 1a FAILED; stop")
su3_basis_8 = []
for M7 in su3_basis_7:
    M8 = np.zeros((8, 8))
    M8[1:8, 1:8] = M7
    su3_basis_8.append(M8)


def lift(X8: np.ndarray) -> np.ndarray:
    S = np.zeros((16, 16))
    for a in range(8):
        for b in range(8):
            if X8[a, b] != 0:
                S += 0.25 * X8[a, b] * (Gam[a] @ Gam[b])
    return S


commute_ok = all(
    np.max(np.abs(lift(M8) @ GammaChiral - GammaChiral @ lift(M8))) < 1e-9 for M8 in su3_basis_8
)
print(f"  [S(X_a), Gamma_chiral] = 0 for all 8 su(3) generators, THIS rep: {commute_ok}")
if not commute_ok:
    raise SystemExit(
        "STAGE 1a: su(3) does NOT commute with Gamma_chiral in the octonion-direct rep "
        "-- Variant C's finding does NOT transfer here. This is the answer, not a bug. Stop."
    )
print("  -> Variant C's finding CONFIRMED independently, in the representation this file")
print("     actually needs for the triality construction (not borrowed unchecked).")
print("  STAGE 1a PASSED\n")

# =============================================================================
# STAGE 2 -- exhaustive search done DIRECTLY on the operator-level trilinear
# form, checked on random vectors from the start (no intermediate re-indexed
# tensor layer -- see module docstring for the bug that layer caused and how
# it was caught).
# =============================================================================
print("=" * 88)
print("STAGE 2 -- exhaustive search directly on trilinear_T, random vectors from the start")
print("=" * 88)
conj_sign = np.array([1.0 if k == 0 else -1.0 for k in range(8)])


def trilinear_T(v: np.ndarray, s: np.ndarray, c: np.ndarray) -> float:
    """T(v,s,c) = <c, v_bar . s>, matching explicit_s3_automorphism.py's
    T_new(a,i,j) = <e_j, ea_bar . e_i> exactly (v<->a, s<->i, c<->j)."""
    v_bar = oconj(to_oct(v))
    prod = from_oct(omul(v_bar, to_oct(s)))
    return float(np.dot(c, prod))


def conj8(v: np.ndarray) -> np.ndarray:
    return v * conj_sign


# cross-check: does trilinear_T on basis vectors reproduce the direct C8_conj
# definition explicit_s3_automorphism.py verified? (independent confirmation
# this IS the same object, before searching for its symmetries)
C8_conj_direct = np.zeros((8, 8, 8))
for a in range(8):
    for i in range(8):
        C8_conj_direct[a, i, :] = from_oct(omul(oconj(to_oct(np.eye(8)[a])), to_oct(np.eye(8)[i])))
C8_conj_via_T = np.zeros((8, 8, 8))
for a in range(8):
    for i in range(8):
        for j in range(8):
            C8_conj_via_T[a, i, j] = trilinear_T(np.eye(8)[a], np.eye(8)[i], np.eye(8)[j])
diff_known = float(np.max(np.abs(C8_conj_via_T - C8_conj_direct)))
print(f"  trilinear_T on basis vectors matches the direct C8_conj definition: {diff_known:.2e}")
if diff_known > 1e-9:
    raise SystemExit("STAGE 2: trilinear_T does not match its own reference definition; stop")

N_TRIALS = 20
v_trials = [rng.normal(size=8) for _ in range(N_TRIALS)]
s_trials = [rng.normal(size=8) for _ in range(N_TRIALS)]
c_trials = [rng.normal(size=8) for _ in range(N_TRIALS)]
lhs_trials = [trilinear_T(v_trials[k], s_trials[k], c_trials[k]) for k in range(N_TRIALS)]

hits = []
arg_names = ["v", "s", "c"]
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
            hits.append((perm, conj_mask, max_resid))

print(f"  exact matches over {N_TRIALS} random trials each (residual < 1e-9): {len(hits)} of 48")
for perm, conj_mask, resid in hits:
    order = [arg_names[perm[i]] for i in range(3)]
    print(
        f"    T(v,s,c) = T({order[0]},{order[1]},{order[2]}) with conj on {conj_mask}, resid={resid:.1e}"
    )
if not hits:
    raise SystemExit(
        "STAGE 2: no (permutation, conjugation) pair reproduces trilinear_T on random "
        "vectors. No simple sign-twist symmetry exists at the operator level. Recording "
        "this honestly -- the tensor-level structure does not lift as hoped. Stop."
    )
print("  STAGE 2 PASSED\n")

# =============================================================================
# STAGE 3 -- select an order-3 element among the hits (a genuine 3-cycle of
# the argument roles, not identity or a transposition).
# =============================================================================
print("=" * 88)
print("STAGE 3 -- select the order-3 generator")
print("=" * 88)


def perm_order(p: tuple) -> int:
    n = len(p)
    cur = list(range(n))
    o = 0
    while True:
        cur = [p[c] for c in cur]
        o += 1
        if cur == list(range(n)):
            return o


three_cycles = [(perm, mask) for perm, mask, _ in hits if perm_order(perm) == 3]
print(f"  order-3 elements among the {len(hits)} hits: {len(three_cycles)}")
for perm, mask in three_cycles:
    order = [arg_names[perm[i]] for i in range(3)]
    print(f"    T(v,s,c)=T({order[0]},{order[1]},{order[2]}) conj_mask={mask}")
if not three_cycles:
    raise SystemExit(
        "STAGE 3: the hits found (identity/transpositions only) contain no order-3 "
        "element -- the S_3 structure hoped for is not fully present. Stop, honestly."
    )
GEN_PERM, GEN_MASK = three_cycles[0]
print(
    f"  using generator: perm={GEN_PERM} (v,s,c -> {[arg_names[i] for i in GEN_PERM]}),"
    f" conj_mask={GEN_MASK}"
)
print("  STAGE 3 PASSED\n")

# =============================================================================
# STAGE 4 -- build the candidate order-3 operator U on H_generation = O(+)O(+)O
# (v (+) s (+) c, 24-real-dim) implementing this generator, and verify U^3 = I
# as an INDEPENDENT structural check (not implied by the trilinear-form match
# alone -- it is a genuine additional constraint on the specific linear map).
# =============================================================================
print("=" * 88)
print("STAGE 4 -- build U on H_generation=O(+)O(+)O, verify U^3 = I")
print("=" * 88)
CONJ8 = np.diag(conj_sign)  # 8x8, the conjugation operator as a matrix


def build_cycle_operator(perm: tuple, mask: tuple) -> np.ndarray:
    """U sends the CONTENT of slot perm[k] (optionally conjugated) into
    output slot k. I.e. out[k] = (conj if mask[perm[k]] else id)(in[perm[k]]).
    Built directly from the same (perm,mask) that made T(v,s,c)=T(twisted-
    and-permuted args) hold -- so U(v,s,c) should be an automorphism of T."""
    U = np.zeros((24, 24))
    for k in range(3):
        src = perm[k]
        block = CONJ8 if mask[src] else np.eye(8)
        U[8 * k : 8 * k + 8, 8 * src : 8 * src + 8] = block
    return U


U = build_cycle_operator(GEN_PERM, GEN_MASK)
U3 = U @ U @ U
resid_order3 = float(np.max(np.abs(U3 - np.eye(24))))
print(f"  U^3 = I: residual = {resid_order3:.2e}")
is_orthogonal = float(np.max(np.abs(U.T @ U - np.eye(24))))
print(f"  U orthogonal (U^T U = I): residual = {is_orthogonal:.2e}")

if resid_order3 > 1e-9:
    print("\n  U as built is NOT order 3. Trying the inverse-cycle generator")
    print("  (the other 3-cycle among the hits, if any) before giving up.")
    other_3cyc = [h for h in three_cycles if h != (GEN_PERM, GEN_MASK)]
    fixed = False
    for perm2, mask2 in other_3cyc:
        U2 = build_cycle_operator(perm2, mask2)
        r2 = float(np.max(np.abs(U2 @ U2 @ U2 - np.eye(24))))
        print(f"    alternate perm={perm2} mask={mask2}: U^3=I residual {r2:.2e}")
        if r2 < 1e-9:
            U, GEN_PERM, GEN_MASK = U2, perm2, mask2
            fixed = True
            break
    if not fixed:
        raise SystemExit(
            "STAGE 4: no order-3 element among the found symmetries actually gives an "
            "order-3 OPERATOR (the trilinear-form-level 3-cycle does not lift to an "
            "order-3 linear map with this direct block construction). Stop, honestly."
        )
print("  STAGE 4 PASSED -- explicit order-3 operator built and verified\n")

# =============================================================================
# STAGE 5 -- does U genuinely intertwine the su(3) action across the three
# legs? I.e. is U a symmetry not just of T but of the FULL su(3)-equipped
# structure -- U (lift(X) (+) lift(X) (+) lift(X)) U^-1 =?= (lift(X) (+)
# lift(X) (+) lift(X)) for the DIAGONAL su(3) action already shown (Stage 1a)
# to preserve each 8-dim leg separately. If U commutes with the diagonal
# su(3) action, U is a genuine automorphism of (H_generation, su(3)-action),
# not merely of the bare trilinear form.
# =============================================================================
print("=" * 88)
print("STAGE 5 -- does U commute with the diagonal su(3) action on v(+)s(+)c?")
print("=" * 88)


def lift8(X8: np.ndarray) -> np.ndarray:
    """su(3) acting on a single 8-dim leg via the SAME Lie-algebra element
    X8 in the vector (v) representation -- the natural 'diagonal' action
    since v, s, c all carry equivalent 8-dim su(3) content (rebuild_ob11_
    spinor_lift.py's identical-multiset-of-weights finding)."""
    return X8  # su(3) acts on the 8-dim octonion coordinates directly as X8 itself


commute_su3 = True
max_resid_su3 = 0.0
for M8 in su3_basis_8:
    diag_action = np.zeros((24, 24))
    for k in range(3):
        diag_action[8 * k : 8 * k + 8, 8 * k : 8 * k + 8] = lift8(M8)
    comm = U @ diag_action - diag_action @ U
    r = float(np.max(np.abs(comm)))
    max_resid_su3 = max(max_resid_su3, r)
    if r > 1e-6:
        commute_su3 = False
print(
    f"  [U, su(3)_diagonal] = 0 for all 8 generators: {commute_su3} (max resid {max_resid_su3:.2e})"
)
if not commute_su3:
    print("\n  U does NOT commute with the diagonal su(3) action -- it permutes the three")
    print("  legs but does not respect their su(3) structure as built. Recorded honestly:")
    print("  U is a symmetry of the bare trilinear form only, not yet of the full")
    print("  (H_generation, su(3)) structure needed for K4's covariance requirement.")
else:
    print("\n  U IS a genuine automorphism of (H_generation, su(3)-action): it permutes the")
    print("  three 8-dim legs cyclically while leaving the su(3) action itself invariant.")
print("  STAGE 5 COMPLETE (informational either way, not a hard stop)\n")

# =============================================================================
# STAGE 6 -- K4's actual content, reduced to a clean linear-algebra question.
# For D_full = D_matter(x)I_gen + gamma_matter(x)Y_gen (the same ansatz used
# throughout main_experiment_A_Dfull_triality.py) and U_t = I_matter(x)U,
# covariance U_t D_full U_t^-1 = D_full reduces EXACTLY to U Y_gen U^-1 =
# Y_gen -- independent of whatever D_matter/gamma_matter turn out to be, so
# this can be tested now without building a full D_matter apparatus for
# Variant C (a separate, larger undertaking, not attempted here). Does a
# NONTRIVIAL (not proportional to identity) real-symmetric Y_gen commuting
# with U exist? This is the direct Variant-C analogue of how K2 was tested
# for the killed branch (searching the commutant/null-space of a symmetry
# constraint), same method, different symmetry.
# =============================================================================
print("=" * 88)
print("STAGE 6 -- K4 reduced: does a nontrivial Y_gen commute with U?")
print("=" * 88)
print("  U_t D_full U_t^-1 = D_full, with D_full = D_matter(x)I + gamma_matter(x)Y_gen")
print("  and U_t = I_matter(x)U, reduces to: U Y_gen U^-1 = Y_gen  (D_matter-independent)\n")

n = 24
sym_basis = []
for a in range(n):
    for b in range(a, n):
        M = np.zeros((n, n))
        if a == b:
            M[a, a] = 1.0
        else:
            M[a, b] = M[b, a] = 1.0 / np.sqrt(2.0)
        sym_basis.append(M)
n_sym = len(sym_basis)
print(f"  space of real-symmetric 24x24 matrices: dim = {n_sym} (24*25/2)")

rows = []
for M in sym_basis:
    comm = U @ M - M @ U
    rows.append(comm.reshape(-1))
comm_matrix = np.array(rows)  # n_sym x 576
_, sv, vh = np.linalg.svd(comm_matrix, full_matrices=False)
null_dim = int(np.sum(sv < 1e-8 * (sv[0] if len(sv) else 1.0)))
print(f"  dim{{Y_gen symmetric : [U,Y_gen]=0}} = {null_dim}")

null_coords = vh[len(sv) - null_dim :, :] if null_dim > 0 else np.zeros((0, n_sym))
Y_solutions = [sum(null_coords[r, k] * sym_basis[k] for k in range(n_sym)) for r in range(null_dim)]
identity_component = 0
for Ysol in Y_solutions:
    proj_onto_I = np.trace(Ysol @ np.eye(n)) / n
    resid_from_scalar = float(np.max(np.abs(Ysol - proj_onto_I * np.eye(n))))
    if resid_from_scalar < 1e-6:
        identity_component += 1
n_nontrivial = null_dim - identity_component
print(f"  of which proportional to identity (trivial, no real mixing): {identity_component}")
print(f"  GENUINELY NONTRIVIAL triality-covariant Y_gen directions: {n_nontrivial}")

if n_nontrivial > 0:
    print("\n  K4 (as reduced to this D_full ansatz): a nontrivial generation-mixing")
    print("  operator CAN respect the triality symmetry U -- the construction is not")
    print("  forced to Y_gen=0 (or pure identity) the way the killed main branch was.")
else:
    print("\n  K4 (as reduced to this D_full ansatz): NO nontrivial Y_gen commutes with U --")
    print("  triality-covariance forces Y_gen to a multiple of identity, the same")
    print("  degeneracy shape (though via a different mechanism) as the killed branch.")
print("  STAGE 6 COMPLETE\n")

print("=" * 88)
print("SUMMARY")
print("=" * 88)
print(f"  explicit order-3 triality generator U on O(+)O(+)O: BUILT, U^3=I to {resid_order3:.1e}")
print(f"  U orthogonal: {is_orthogonal:.1e}")
print(f"  U commutes with diagonal su(3): {commute_su3}")
print(f"  generator: v,s,c -> {[arg_names[i] for i in GEN_PERM]}, conjugate legs {GEN_MASK}")
print(
    f"  K4 (D_full=D_matter(x)I+gamma_matter(x)Y_gen ansatz): nontrivial Y_gen directions"
    f" commuting with U = {n_nontrivial}"
)
print("  NOT DONE: a full D_matter/gamma_matter apparatus for Variant C's H_generation was")
print("  not built here -- this tests ONLY the generation-side covariance condition, which")
print("  is what U_t D_full U_t^-1=D_full reduces to for ANY choice of D_matter under this")
print("  standard ansatz, not the complete K4 criterion in full generality.")
