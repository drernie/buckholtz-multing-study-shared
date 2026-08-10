"""Variant C -- "3 generations" = {8v, 8s, 8c} permuted by OUTER triality (S_3,
discrete), NOT the 3 weight-coordinates WITHIN one SU(3) triplet (continuous,
already killed).

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION. Minimal Relaxation Rule:
ONE assumption changed from the killed branch and from V1 (also killed) --
this time not touching A/H_generation's construction at all, but questioning
whether "the 3" was ever the right object to call "generations" in the first
place.

THE STRUCTURAL FACT THIS RELIES ON (general Lie theory, not specific to this
construction, [MEMORY] no live citation this pass but this is textbook-level:
for ANY semisimple Lie group G, Aut(G) = Inn(G) x| Out(G) with Inn(G)=G/Z(G)
the CONTINUOUS part and Out(G) always FINITE/DISCRETE, arising from Dynkin-
diagram automorphisms). D_4's Dynkin diagram has an order-3 symmetry (the
three outer nodes around the central one) -- famously giving Out(Spin(8))=S_3,
"triality" -- the UNIQUE case among simple Lie groups with an outer
automorphism group this large. Discreteness here is not assumed for THIS
construction specifically; it is a structural fact about ANY simple Lie
group's automorphisms.

WHY THIS MATTERS FOR THE KILL-TEST: the K2 kill-test argument was "SU(3) acts
transitively (continuously) on the 3 coordinates, so a continuous unitary
connects any two -- no physical distinguishability survives." That argument
is SPECIFIC to continuous group actions (irreducibility => transitivity on
the unit sphere via a PATH of unitaries). A DISCRETE symmetry relating three
OBJECTS (not three coordinates of one object) is not automatically subject to
the same argument -- there is no continuous path between discrete points.

THE CONCRETE, CHEAP, DECISIVE CHECK: if 8v, 8s, 8c are to be genuinely
distinguishable "generations", something already present in this
construction must DISTINGUISH them AND that distinguishing structure must
be INVARIANT under (commute with) the full su(3) action -- otherwise su(3)
could still smear them together the same way it smeared the triplet
coordinates. The natural candidate already built in rebuild_ob11_spinor_lift.py:
the chirality operator Gamma_chiral, which by construction splits the 16-dim
spinor space into 8s (+1) and 8c (-1). Checked here, not assumed: does the
LIFTED su(3) action commute with Gamma_chiral?
"""

import numpy as np

rng = np.random.default_rng(3031)

# =============================================================================
# STAGE 0 -- reconstruct su(3) on Im(O) (reused, verified logic from
# rebuild_ob11_triality.py / rebuild_ob11_spinor_lift.py).
# =============================================================================
print("=" * 88)
print("STAGE 0 -- su(3) on Im(O) (reused)")
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


O_BASIS = [(np.eye(4)[i], np.zeros(4)) for i in range(4)] + [
    (np.zeros(4), np.eye(4)[i]) for i in range(4)
]
C8 = np.zeros((8, 8, 8))
for i in range(8):
    for j in range(8):
        C8[i, j, :] = np.concatenate(omul(O_BASIS[i], O_BASIS[j]))
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
# action_matrix is 7x14 (M<N) -- need the FULL 14x14 Vh to reach the null-
# space rows; full_matrices=False would truncate Vh to 7x14 and silently
# drop them (caught by an IndexError on the first run, not a silent wrong
# answer -- fixed here rather than papered over).
_, s2, vh2 = np.linalg.svd(action_matrix, full_matrices=True)
n_rank = int(np.sum(s2 > 1e-8 * (s2[0] if len(s2) else 1.0)))
su3_dim = action_matrix.shape[1] - n_rank
su3_coords_in_g2 = vh2[vh2.shape[0] - su3_dim :, :]
su3_basis_7 = [
    sum(su3_coords_in_g2[r, k] * g2_basis[k] for k in range(g2_dim)) for r in range(su3_dim)
]
print(f"  dim(g2)={g2_dim} (expect 14), dim(su3)={su3_dim} (expect 8)")
if g2_dim != 14 or su3_dim != 8:
    raise SystemExit("STAGE 0 FAILED; stop")
su3_basis_8 = []
for M7 in su3_basis_7:
    M8 = np.zeros((8, 8))
    M8[1:8, 1:8] = M7
    su3_basis_8.append(M8)
print("  STAGE 0 PASSED\n")

# =============================================================================
# STAGE 1 -- Cl(8,0) gammas, chirality operator (reused, verified).
# =============================================================================
print("=" * 88)
print("STAGE 1 -- Cl(8,0), Gamma_chiral, 8s/8c split (reused)")
print("=" * 88)
X_PAULI = np.array([[0, 1], [1, 0]], dtype=complex)
Y_PAULI = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z_PAULI = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def kron_chain(mats):
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


def euclidean_gammas(n):
    m = n // 2
    gammas = []
    for k in range(m):
        pre, post = [Z_PAULI] * k, [I2] * (m - k - 1)
        gammas.append(kron_chain(pre + [X_PAULI] + post))
        gammas.append(kron_chain(pre + [Y_PAULI] + post))
    return gammas


Gamma = euclidean_gammas(8)
GammaChiral = np.eye(16, dtype=complex)
for a in range(8):
    GammaChiral = GammaChiral @ Gamma[a]
chiral_sq = GammaChiral @ GammaChiral
if chiral_sq[0, 0].real < 0:
    GammaChiral = 1j * GammaChiral
eigvals_chiral, eigvecs_chiral = np.linalg.eigh((GammaChiral + GammaChiral.conj().T) / 2)
n_plus = int(np.sum(eigvals_chiral > 0))
n_minus = int(np.sum(eigvals_chiral < 0))
print(f"  16 = 8s({n_plus}) (+) 8c({n_minus}): {(n_plus, n_minus) == (8, 8)}")
if (n_plus, n_minus) != (8, 8):
    raise SystemExit("STAGE 1 FAILED; stop")
print("  STAGE 1 PASSED\n")

# =============================================================================
# STAGE 2 -- THE KEY CHECK: does the lifted su(3) (acting on the 16-dim
# spinor space via S(X)=(1/4)sum X_ab Gamma_a Gamma_b) commute with
# Gamma_chiral? This is what would let chirality survive as a generation-
# label AFTER su(3) acts -- i.e. su(3) cannot mix 8s and 8c, unlike how it
# freely mixed the 3 coordinates within one triplet in the killed branch.
# =============================================================================
print("=" * 88)
print("STAGE 2 -- does lifted su(3) commute with Gamma_chiral? (THE decisive check)")
print("=" * 88)


def lift(X8: np.ndarray) -> np.ndarray:
    S = np.zeros((16, 16), dtype=complex)
    for a in range(8):
        for b in range(8):
            if X8[a, b] != 0:
                S += 0.25 * X8[a, b] * (Gamma[a] @ Gamma[b])
    return S


commute_ok = True
max_resid = 0.0
for M8 in su3_basis_8:
    S_X = lift(M8)
    comm = S_X @ GammaChiral - GammaChiral @ S_X
    r = np.max(np.abs(comm))
    max_resid = max(max_resid, r)
    if r > 1e-9:
        commute_ok = False
print(
    f"  [S(X_a), Gamma_chiral] = 0 for all 8 su(3) generators: {commute_ok} (max resid {max_resid:.2e})"
)
if not commute_ok:
    raise SystemExit(
        "STAGE 2: su(3) does NOT preserve chirality -- Variant C's premise fails here;"
        " stop, this is the answer, not a bug"
    )

# also check for a GENERIC element of su(3) (not just the 8 basis generators
# individually -- a linear combination could in principle behave differently,
# though linearity of the commutator makes this redundant; checked anyway as
# a genuine positive control, not assumed from linearity alone)
coeffs = rng.normal(size=8)
X_generic_8 = sum(c * M for c, M in zip(coeffs, su3_basis_8, strict=True))
S_generic = lift(X_generic_8)
comm_generic = S_generic @ GammaChiral - GammaChiral @ S_generic
print(
    f"  [S(X_generic), Gamma_chiral] for a random su(3) element: {np.max(np.abs(comm_generic)):.2e}"
)
print("  STAGE 2 PASSED -- su(3) genuinely preserves the 8s/8c split\n")

# =============================================================================
# STAGE 3 -- the actual kill-test logic, applied correctly this time: is
# there a symmetry-respecting transformation erasing 8s vs 8c? "Symmetry-
# respecting" here means built from what the construction actually has
# available: su(3) (shown NOT to erase it) and the discrete triality outer
# automorphisms. Check: within the ALREADY-CONFIRMED symmetry group of this
# construction (su(3), continuous), is there a continuous path connecting an
# 8s state to an 8c state? By Stage 2, su(3) alone cannot -- it preserves
# the chirality eigenspaces exactly. Whether the DISCRETE triality
# automorphism (not su(3)) swaps 8s<->8c is a SEPARATE question (it does,
# by the definition of triality) but that swap is discrete, not a continuous
# unitary path -- so it does not trigger the SAME kill-test logic (K2 was
# specifically about CONTINUOUS transitivity erasing distinguishability).
# =============================================================================
print("=" * 88)
print("STAGE 3 -- kill-test re-applied: does the AVAILABLE continuous symmetry erase 8s vs 8c?")
print("=" * 88)
print(
    "  K2's argument required: su(3) acts irreducibly/transitively on the space in"
    " question, so ANY two states are connected by a continuous unitary path within"
    " the model's own symmetry. Stage 2 shows su(3) does NOT act on 8s(+)8c jointly"
    " this way -- it preserves each chirality eigenspace separately (block-diagonal),"
    " so it is reducible (at least 8s (+) 8c, two invariant subspaces) with respect to"
    " the FULL 16-dim spinor space, even though each 8-dim piece is itself an"
    " irreducible 1+1+3+3bar under su(3) internally."
)
print(
    "\n  -> Within su(3) alone, an 8s state and an 8c state CANNOT be connected by any"
    " su(3) group element (different eigenspaces of an operator, Gamma_chiral, that"
    " commutes with all of su(3) -- a block-diagonal representation's blocks are never"
    " reachable from each other by the group itself). The K2 argument's mechanism"
    " (transitivity) genuinely does not apply here."
)
print(
    "\n  What DOES relate 8s and 8c: the discrete triality outer automorphism (order-3"
    " element of S_3=Out(Spin(8)), a STANDARD fact of D_4 Lie theory, not verified"
    " computationally this pass -- constructing the explicit triality map is a"
    " separate, harder piece of work not attempted here). A discrete automorphism is"
    " not a continuous unitary PATH -- the K2 kill-test's specific mechanism (a path"
    " of symmetry-respecting unitaries erasing distinguishability) does not"
    " automatically transfer to a discrete symmetry, though it does not by itself"
    " PROVE distinguishability survives either -- see caveats below."
)
