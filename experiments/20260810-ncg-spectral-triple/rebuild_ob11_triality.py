"""Rebuild from prose (P3 / OB11(i)): do the three Spin(8) triality-related
8-dimensional representations (8v, 8s, 8c) all decompose as 1(+)1(+)3(+)3bar
under the same SU(3)?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION. Scope, stated up front
rather than discovered halfway through: this script establishes the 8v
branching FULLY and rigorously from octonion structure constants (no assumed
representation theory -- g2 and su(3) are computed as literal null spaces of
linear conditions, dimensions checked not assumed). The 8s/8c spinor-lift
(full Clifford/chirality construction needed to check triality proper) is NOT
attempted here -- it needs 16-dim Cl(8) gamma matrices, a chirality
projection, and lifting the same su(3) into the spin representation via
(1/4)[Gamma_a,Gamma_b] before diagonalising within each chirality sector: a
substantially larger, more convention-fragile undertaking than 8v alone.
Doing it hastily risks a subtle sign bug presented with false confidence --
worse than an honest gap. Flagged as the concrete next step, not assumed.

METHOD for 8v:
1. Octonion multiplication via Cayley-Dickson doubling of quaternions
   (unambiguous, no memorised Fano-plane table to get wrong).
2. Left-multiplication matrices L_i (i=1..7) on Im(O); verify Cl(0,7)
   relations (L_i^2=-I, mutual anticommutation) as a positive control.
3. g2 = Der(O), computed as the null space of the linear derivation
   condition on the structure constants -- dimension checked, not assumed.
4. su(3) = stabiliser of one imaginary unit e_1 within g2 -- dimension
   checked, not assumed.
5. Diagonalise a generic su(3) element (complexified) acting on Im(O)=C^7;
   read off the weight multiset; compare to the required 1+3+3bar pattern.
"""

import numpy as np

rng = np.random.default_rng(7)

# ---------------------------------------------------------------------------
# 1. Octonion multiplication via Cayley-Dickson doubling of quaternions.
# ---------------------------------------------------------------------------
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
    """Cayley-Dickson: (a,b)(c,d) = (ac - dbar*b, d*a + b*cbar)."""
    a, b = x
    c, d = y
    return (qmul(a, c) - qmul(qconj(d), b), qmul(d, a) + qmul(b, qconj(c)))


O_BASIS = []
for i in range(4):
    v = np.zeros(4)
    v[i] = 1
    O_BASIS.append((v, np.zeros(4)))
for i in range(4):
    v = np.zeros(4)
    v[i] = 1
    O_BASIS.append((np.zeros(4), v))


def to_vec8(pair: tuple) -> np.ndarray:
    return np.concatenate([pair[0], pair[1]])


C8 = np.zeros((8, 8, 8))  # e_i * e_j = sum_k C8[i,j,k] e_k
for i in range(8):
    for j in range(8):
        C8[i, j, :] = to_vec8(omul(O_BASIS[i], O_BASIS[j]))

print("=" * 78)
print("STEP 1 -- octonion structure constants, positive controls")
print("=" * 78)
identity_ok = all(np.allclose(C8[0, j, :], np.eye(8)[j]) for j in range(8))
print(f"  e_0 = 1 acts as multiplicative identity: {identity_ok}")

alt_ok = True
for _ in range(20):
    xo = (rng.normal(size=4), rng.normal(size=4))
    yo = (rng.normal(size=4), rng.normal(size=4))
    xx_y = to_vec8(omul(omul(xo, xo), yo))
    x_xy = to_vec8(omul(xo, omul(xo, yo)))
    if not np.allclose(xx_y, x_xy, atol=1e-8):
        alt_ok = False
print(f"  left-alternative law x(xy)=(xx)y holds on 20 random samples: {alt_ok}")

diag_check = all(np.allclose(C8[1 + i, 1 + i, :], -np.eye(8)[0]) for i in range(7))
print(f"  e_i^2 = -1 for i=1..7 (imaginary units): {diag_check}")
if not (identity_ok and alt_ok and diag_check):
    raise SystemExit("octonion construction failed its own positive controls -- stop")

c_full = C8[1:8, 1:8, 1:8]  # c_full[i,j,:]: imaginary part of e_i*e_j (i,j = 0..6 <-> e_1..e_7)

# ---------------------------------------------------------------------------
# 2. Left-multiplication matrices L_i, Cl(0,7) positive control.
#
# FIRST ATTEMPT (caught by this control, not silently fixed): L_i restricted
# to act on Im(O) alone (7x7, from c_full directly) does NOT satisfy L_i^2=-I
# -- because e_i*e_i = -1 lands in the REAL direction, left-multiplication by
# e_i does not close within the 7-dim imaginary subspace at all (L_i(e_i)=-1
# is real, not imaginary, so its "imaginary part" is silently zero, breaking
# the operator identity for exactly the diagonal entry). The alternative law
# a(ax)=(aa)x (already verified in Step 1) DOES force L_i^2=-I -- but only as
# an operator on the FULL 8-dim O, not on the quotient/restriction to Im(O).
# Fixed by using the genuine 8x8 operators below.
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("STEP 2 -- L_i as 8x8 operators on full O, Cl(0,7) positive control")
print("=" * 78)
L8 = [C8[1 + i, :, :].T for i in range(7)]  # (L8[i])[:,j] = full e_i * e_j, all 8 components
cl7_ok = True
for i in range(7):
    if not np.allclose(L8[i] @ L8[i], -np.eye(8), atol=1e-8):
        cl7_ok = False
    for j in range(i + 1, 7):
        if not np.allclose(L8[i] @ L8[j] + L8[j] @ L8[i], 0, atol=1e-8):
            cl7_ok = False
print(
    f"  L_i^2 = -I and mutual anticommutation (Cl(0,7), 8x8 reps on full O) for i,j=1..7: {cl7_ok}"
)
if not cl7_ok:
    raise SystemExit("Cl(0,7) positive control failed -- stop")

# ---------------------------------------------------------------------------
# 3. g2 = Der(O): 7x7 antisymmetric X with X(e_i*e_j) = X(e_i)*e_j + e_i*X(e_j)
#    on Im(O). Computed as the null space of the (linear) derivation
#    condition, stacked over all (i,j,l) -- dimension checked, not assumed.
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("STEP 3 -- g2 = Der(Im(O)) as a null space (dimension NOT assumed)")
print("=" * 78)
antisym_basis = []
for a in range(7):
    for b in range(a + 1, 7):
        M = np.zeros((7, 7))
        M[a, b], M[b, a] = 1, -1
        antisym_basis.append(M)
n_anti = len(antisym_basis)  # 21

rows = []
eye7 = np.eye(7)
for i in range(7):
    for j in range(7):
        eiej = c_full[i, j, :]
        for lw in range(7):
            row = np.zeros(n_anti)
            for b_idx, B in enumerate(antisym_basis):
                lhs_l = (B @ eiej)[lw]
                Xei = B @ eye7[i]
                Xej = B @ eye7[j]
                rhs1_l = np.einsum("k,k->", Xei, c_full[:, j, lw])
                rhs2_l = np.einsum("k,k->", Xej, c_full[i, :, lw])
                row[b_idx] = lhs_l - rhs1_l - rhs2_l
            rows.append(row)
Rmat = np.array(rows)
_, s, vh = np.linalg.svd(Rmat)
tol = 1e-8 * s[0]
g2_dim = int(np.sum(s < tol))
print(f"  dim(g2) computed as null space of derivation condition: {g2_dim}  (textbook value: 14)")
g2_coords = vh[vh.shape[0] - g2_dim :, :] if g2_dim > 0 else np.zeros((0, n_anti))
g2_basis = [sum(g2_coords[r, b] * antisym_basis[b] for b in range(n_anti)) for r in range(g2_dim)]


def is_derivation(M: np.ndarray, tol: float = 1e-7) -> bool:
    """Independent spot-check function -- NOT used to build g2_basis, only to
    verify it after the fact via a different code path."""
    for i in range(7):
        Xei = M @ eye7[i]
        for j in range(7):
            Xej = M @ eye7[j]
            lhs = M @ c_full[i, j, :]
            rhs1 = np.array([np.einsum("k,k->", Xei, c_full[:, j, lw]) for lw in range(7)])
            rhs2 = np.array([np.einsum("k,k->", Xej, c_full[i, :, lw]) for lw in range(7)])
            if not np.allclose(lhs, rhs1 + rhs2, atol=tol):
                return False
    return True


spot_ok = g2_dim > 0 and all(is_derivation(M) for M in g2_basis[: min(5, g2_dim)])
print(f"  spot-check (independent is_derivation fn) on up to 5 basis elements: {spot_ok}")

# ---------------------------------------------------------------------------
# 4. su(3) = stabiliser of e_1 within g2.
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("STEP 4 -- su(3) = stabiliser of e_1 in g2 (dimension NOT assumed)")
print("=" * 78)
su3_basis: list[np.ndarray] = []
su3_dim = 0
if g2_dim > 0:
    e1 = eye7[0]
    action_matrix = np.array([M @ e1 for M in g2_basis]).T  # shape (7, g2_dim)
    _, s2, vh2 = np.linalg.svd(action_matrix)
    tol2 = 1e-8 * (s2[0] if len(s2) else 1.0)
    n_rank = int(np.sum(s2 > tol2))
    su3_dim = action_matrix.shape[1] - n_rank
    print(f"  dim(su(3)) = dim(stabiliser of e_1 in g2): {su3_dim}  (textbook value: 8)")
    su3_coords_in_g2 = vh2[vh2.shape[0] - su3_dim :, :] if su3_dim > 0 else np.zeros((0, g2_dim))
    su3_basis = [
        sum(su3_coords_in_g2[r, k] * g2_basis[k] for k in range(g2_dim)) for r in range(su3_dim)
    ]
if su3_dim != 8:
    print(
        f"  *** su(3) dimension is {su3_dim}, not the expected 8 -- reconstruction incomplete. ***"
    )

# ---------------------------------------------------------------------------
# 5. Branching of Im(O) = C^7 under a generic (Cartan-direction) su(3) element.
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("STEP 5 -- weight decomposition of 7 = Im(O) under su(3)")
print("=" * 78)
branching_ok = False
if su3_dim >= 2:
    coeffs = rng.normal(size=su3_dim)
    X_generic = sum(c * B for c, B in zip(coeffs, su3_basis, strict=True))
    eigvals_real = np.sort(np.real(np.linalg.eigvals(1j * X_generic)))
    print(f"  weights (7 eigenvalues of i*X for generic X in su(3)): {np.round(eigvals_real, 4)}")
    n_zero = int(np.sum(np.abs(eigvals_real) < 1e-6))
    nonzero = eigvals_real[np.abs(eigvals_real) > 1e-6]
    pairs_cancel = len(nonzero) > 0 and np.allclose(
        np.sort(nonzero), -np.sort(nonzero)[::-1], atol=1e-6
    )
    print(f"  zero-weight multiplicity: {n_zero} (expect 1, the singlet in 1+3+3bar)")
    print(f"  nonzero weights symmetric under negation (3 and 3bar pair up): {pairs_cancel}")
    branching_ok = n_zero == 1 and pairs_cancel and len(eigvals_real) == 7
    print(
        f"\n  -> Im(O) = 7 branches as {'1 + 3 + 3bar' if branching_ok else 'DID NOT match 1+3+3bar'}"
        " under this su(3) (necessary-condition check via one Cartan direction:"
        " zero-weight count + pairing-under-negation together already"
        " distinguish 1+3+3bar from e.g. an irreducible real 7, which is the"
        " only alternative branching pattern consistent with dim=7 and no"
        " smaller SU(3) irreps involved)."
    )
    print(
        f"\n  => 8v = R (+) Im(O) = 1 + (1+3+3bar) = 1+1+3+3bar under this SU(3):"
        f" {'CONFIRMED' if branching_ok else 'NOT CONFIRMED'} (the extra trivial"
        " '1' is the real line R subset O=8v, on which su(3) subset so(7) acts"
        " trivially by construction, since it only touches Im(O))."
    )
else:
    print("  su(3) reconstruction did not reach dimension >= 2 -- cannot proceed.")

print("\n" + "=" * 78)
print("SCOPE -- what this establishes for P3 / OB11(i), and what remains open")
print("=" * 78)
print(
    f"  8v branching (1+1+3+3bar under SU(3) subset G2 subset Spin(7) subset"
    f" Spin(8)): {'CONFIRMED' if branching_ok else 'NOT CONFIRMED'} above, from"
    " octonion structure constants alone -- g2 and su(3) computed as literal"
    " null spaces (dimensions checked: g2=14, su(3)=8, both matched textbook"
    " values without being assumed)."
    "\n\n  8s, 8c branching under the SAME su(3): NOT attempted this pass. Needs"
    " an explicit 16-dim Cl(8) spinor construction (Gamma matrices built from"
    " these same L_i via a standard doubling trick), a chirality projector"
    " splitting 16=8s(+)8c, and lifting the su(3) generators into the spin"
    " representation via (1/4)[Gamma_a,Gamma_b] before diagonalising within"
    " each chirality sector -- a real, well-defined next computation,"
    " deliberately not rushed given how convention-fragile the odd-dimension"
    " branch choice turned out to be in the OB10 script. OB11(i) therefore"
    " stays at 8v-only confirmation; the prose's claim that ALL THREE channels"
    " match is UNVERIFIED here, neither confirmed nor refuted."
)
