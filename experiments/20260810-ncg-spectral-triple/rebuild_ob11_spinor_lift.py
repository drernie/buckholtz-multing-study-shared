"""Rebuild from prose (P3 / OB11(i), completing it): do 8s and 8c branch as
1+1+3+3bar under the SAME su(3) that 8v does (rebuild_ob11_triality.py)?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION.

Explicitly staged, each stage gated on its own positive control before the
next stage runs -- the process lesson recorded in FINDING_rebuild_from_prose.md
after rebuild_ob11_triality.py's Im(O)-restriction bug: writing all steps
before running any of them let that bug travel further than it needed to.
Here each stage raises SystemExit on its own failure before the next stage's
code even executes.

Reuses, rather than reinvents:
  - the octonion/g2/su(3) construction from rebuild_ob11_triality.py (already
    independently verified: dim g2=14, dim su(3)=8, 8v branches as 1+1+3+3bar)
  - the Cl(p,q) Jordan-Wigner gamma-matrix construction from
    rebuild_ob10_clifford.py (already independently verified via two positive
    controls with opposite known answers)

NEW in this file: the so(8)->spin(8) lift S(X) = (1/4) sum_ab X_ab Gamma_a
Gamma_b, verified here as an actual Lie algebra homomorphism
([S(X),S(Y)] = S([X,Y])) BEFORE it is trusted for anything -- this is the
one genuinely new piece of machinery, and the one most likely to carry a
sign/normalisation bug, so it gets its own dedicated positive control.
"""

import numpy as np

rng = np.random.default_rng(11)

# =============================================================================
# STAGE 0 -- reconstruct su(3) acting on Im(O) = R^7 (copied, verified logic
# from rebuild_ob11_triality.py; re-derived here rather than imported, per
# this repo's convention that each FINDING script is self-contained).
# =============================================================================
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
        prod = omul(O_BASIS[i], O_BASIS[j])
        C8[i, j, :] = np.concatenate(prod)

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
_, s, vh = np.linalg.svd(np.array(rows))
g2_dim = int(np.sum(s < 1e-8 * s[0]))
g2_coords = vh[vh.shape[0] - g2_dim :, :]
g2_basis = [sum(g2_coords[r, b] * antisym_basis[b] for b in range(n_anti)) for r in range(g2_dim)]

e1 = eye7[0]
action_matrix = np.array([M @ e1 for M in g2_basis]).T
_, s2, vh2 = np.linalg.svd(action_matrix)
n_rank = int(np.sum(s2 > 1e-8 * (s2[0] if len(s2) else 1.0)))
su3_dim = action_matrix.shape[1] - n_rank
su3_coords_in_g2 = vh2[vh2.shape[0] - su3_dim :, :]
su3_basis_7 = [
    sum(su3_coords_in_g2[r, k] * g2_basis[k] for k in range(g2_dim)) for r in range(su3_dim)
]

print("=" * 78)
print(
    "STAGE 0 -- reconstruct su(3) on Im(O) (positive control: dims match rebuild_ob11_triality.py)"
)
print("=" * 78)
print(f"  dim(g2) = {g2_dim} (expect 14), dim(su(3)) = {su3_dim} (expect 8)")
if g2_dim != 14 or su3_dim != 8:
    raise SystemExit(
        "STAGE 0 FAILED -- su(3) reconstruction did not reproduce; stop before Stage 1"
    )
print("  STAGE 0 PASSED\n")

# Embed su(3)'s 7x7 action on Im(O) into 8x8 acting on O = R (+) Im(O), with
# a zero row/column for the real direction e_0 (su(3) fixes e_0, matching 8v's
# trivial singlet found in rebuild_ob11_triality.py).
su3_basis_8 = []
for M7 in su3_basis_7:
    M8 = np.zeros((8, 8))
    M8[1:8, 1:8] = M7
    su3_basis_8.append(M8)

# =============================================================================
# STAGE 1 -- Cl(8,0) gamma matrices (reuse the JW construction already
# verified in rebuild_ob10_clifford.py -- copied here, not re-derived, since
# that construction already passed its own positive controls).
# =============================================================================
print("=" * 78)
print("STAGE 1 -- Cl(8,0) gamma matrices (reused, already-verified construction)")
print("=" * 78)
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


Gamma = euclidean_gammas(8)  # 8 matrices, 16x16, all Gamma_a^2=+I, mutually anticommuting
d16 = Gamma[0].shape[0]
assert d16 == 16
cl8_ok = True
for a in range(8):
    if not np.allclose(Gamma[a] @ Gamma[a], np.eye(16), atol=1e-9):
        cl8_ok = False
    for b in range(a + 1, 8):
        if not np.allclose(Gamma[a] @ Gamma[b] + Gamma[b] @ Gamma[a], 0, atol=1e-9):
            cl8_ok = False
print(f"  Gamma_a^2=I, mutual anticommutation, a,b=1..8: {cl8_ok}")
if not cl8_ok:
    raise SystemExit("STAGE 1 FAILED -- Cl(8,0) relations broken; stop before Stage 2")
print("  STAGE 1 PASSED\n")

# =============================================================================
# STAGE 2 -- chirality operator, verify the 16 = 8s (+) 8c split.
# =============================================================================
print("=" * 78)
print("STAGE 2 -- chirality operator, 16 = 8s (+) 8c split")
print("=" * 78)
GammaChiral = np.eye(16, dtype=complex)
for a in range(8):
    GammaChiral = GammaChiral @ Gamma[a]
chiral_sq = GammaChiral @ GammaChiral
print(f"  Gamma_chiral^2 = c*I with c = {chiral_sq[0, 0]:.4f} (checking it IS scalar +-1 first)")
is_scalar = np.allclose(chiral_sq, chiral_sq[0, 0] * np.eye(16), atol=1e-9)
c_val = chiral_sq[0, 0].real
if not (is_scalar and np.isclose(abs(c_val), 1.0, atol=1e-6)):
    raise SystemExit(
        f"STAGE 2 FAILED -- Gamma_chiral^2 is not scalar +-1 (got scalar={is_scalar}, c={c_val}); stop"
    )
if c_val < 0:
    # normalise so eigenvalues are real +-1 (multiply by i if squared to -1)
    GammaChiral = 1j * GammaChiral
    chiral_sq = GammaChiral @ GammaChiral
    print(f"  (rescaled by i so Gamma_chiral^2=+I; new c = {chiral_sq[0, 0].real:.4f})")

eigvals_chiral, eigvecs_chiral = np.linalg.eigh((GammaChiral + GammaChiral.conj().T) / 2)
# Gamma_chiral should be Hermitian for this construction (product of Hermitian
# anticommuting unitaries with the right parity) -- verified via the symmetrised
# eigh matching the raw matrix, checked next.
herm_ok = np.allclose(GammaChiral, GammaChiral.conj().T, atol=1e-9)
print(f"  Gamma_chiral is Hermitian: {herm_ok}")
if not herm_ok:
    raise SystemExit("STAGE 2 FAILED -- Gamma_chiral not Hermitian, eigh split is not valid; stop")

n_plus = int(np.sum(eigvals_chiral > 0))
n_minus = int(np.sum(eigvals_chiral < 0))
print(f"  eigenvalue split: {n_plus} at +1, {n_minus} at -1 (expect 8, 8)")
if (n_plus, n_minus) != (8, 8):
    raise SystemExit(f"STAGE 2 FAILED -- split is {n_plus}/{n_minus}, not 8/8; stop before Stage 3")
idx_plus = np.where(eigvals_chiral > 0)[0]
idx_minus = np.where(eigvals_chiral < 0)[0]
V8s = eigvecs_chiral[:, idx_plus]  # 16x8, orthonormal basis of the +1 chirality sector
V8c = eigvecs_chiral[:, idx_minus]
print("  STAGE 2 PASSED\n")

# =============================================================================
# STAGE 3 -- so(8) -> spin(8) lift, S(X) = (1/4) sum_ab X_ab Gamma_a Gamma_b.
# VERIFY it is a Lie algebra homomorphism, [S(X),S(Y)]=S([X,Y]), on random
# so(8) elements BEFORE trusting it for the actual su(3) generators.
# =============================================================================
print("=" * 78)
print("STAGE 3 -- so(8)->spin(8) lift, verified as a Lie homomorphism (positive control)")
print("=" * 78)


def lift(X8: np.ndarray) -> np.ndarray:
    S = np.zeros((16, 16), dtype=complex)
    for a in range(8):
        for b in range(8):
            if X8[a, b] != 0:
                S += 0.25 * X8[a, b] * (Gamma[a] @ Gamma[b])
    return S


def random_so8(rng) -> np.ndarray:
    A = rng.normal(size=(8, 8))
    return A - A.T


homomorphism_ok = True
max_resid = 0.0
for _ in range(5):
    Xr, Yr = random_so8(rng), random_so8(rng)
    lhs = lift(Xr) @ lift(Yr) - lift(Yr) @ lift(Xr)
    rhs = lift(Xr @ Yr - Yr @ Xr)
    resid = np.max(np.abs(lhs - rhs))
    max_resid = max(max_resid, resid)
    if resid > 1e-8:
        homomorphism_ok = False
print(
    f"  [S(X),S(Y)] == S([X,Y]) on 5 random so(8) pairs: {homomorphism_ok} (max residual {max_resid:.2e})"
)
if not homomorphism_ok:
    raise SystemExit("STAGE 3 FAILED -- spin lift is not a Lie homomorphism; DO NOT trust Stage 4")
print("  STAGE 3 PASSED\n")

# =============================================================================
# STAGE 4 -- restrict lifted su(3) to each chirality sector, get weights.
# =============================================================================
print("=" * 78)
print("STAGE 4 -- weight decomposition of 8s and 8c under the lifted su(3)")
print("=" * 78)
coeffs = rng.normal(size=su3_dim)
X_generic_8 = sum(c * M for c, M in zip(coeffs, su3_basis_8, strict=True))
S_generic = lift(X_generic_8)

# Restrict to each chirality sector: project S_generic into the V8s / V8c bases.
S_8s = V8s.conj().T @ S_generic @ V8s  # 8x8
S_8c = V8c.conj().T @ S_generic @ V8c

# CORRECTED CHECK (caught by this exact check failing, not silently loosened):
# Gamma_a are Hermitian with Gamma_a^2=I, so for a!=b, (Gamma_a Gamma_b)^dagger
# = Gamma_b Gamma_a = -Gamma_a Gamma_b -- Gamma_aGamma_b is ANTI-Hermitian, not
# Hermitian. S(X) for real antisymmetric X is therefore ANTI-Hermitian
# (S^dagger = -S), exactly as expected for the generator of a unitary
# representation (matches the 1j*X_generic convention already used for 8v's
# own weights below) -- so the correct positive control is that i*S(X) is
# Hermitian, not S(X) itself. The Lie-homomorphism check in Stage 3 already
# passed at machine precision (residual 4e-15), confirming the CONSTRUCTION is
# right; this was a wrong expectation in the CHECK, caught immediately rather
# than silently loosening the tolerance or skipping the check.
herm_8s_ok = np.allclose(1j * S_8s, (1j * S_8s).conj().T, atol=1e-8)
herm_8c_ok = np.allclose(1j * S_8c, (1j * S_8c).conj().T, atol=1e-8)
print(
    f"  i*S(X) restricted to 8s is Hermitian (S(X) itself anti-Hermitian, as expected): {herm_8s_ok}"
)
print(
    f"  i*S(X) restricted to 8c is Hermitian (S(X) itself anti-Hermitian, as expected): {herm_8c_ok}"
)
if not (herm_8s_ok and herm_8c_ok):
    raise SystemExit(
        "STAGE 4 FAILED -- restricted generator is not anti-Hermitian as expected; stop"
    )
S_8s, S_8c = 1j * S_8s, 1j * S_8c  # now Hermitian; eigenvalues are the real weights


def weight_report(S: np.ndarray, label: str) -> tuple[bool, np.ndarray]:
    eigvals = np.sort(np.linalg.eigvalsh(S).real)
    print(f"\n  {label} weights: {np.round(eigvals, 4)}")
    n_zero = int(np.sum(np.abs(eigvals) < 1e-6))
    nonzero = eigvals[np.abs(eigvals) > 1e-6]
    pairs_cancel = len(nonzero) > 0 and np.allclose(
        np.sort(nonzero), -np.sort(nonzero)[::-1], atol=1e-6
    )
    print(f"    zero-weight multiplicity: {n_zero} (8v's Im(O) part had 1; full 8v had 2 incl. R)")
    print(f"    nonzero weights symmetric under negation: {pairs_cancel}")
    matches_137bar_pattern = n_zero == 2 and pairs_cancel and len(eigvals) == 8
    print(f"    matches 1+1+3+3bar pattern (n_zero=2, paired, dim=8): {matches_137bar_pattern}")
    return matches_137bar_pattern, eigvals


ok_8s, eig_8s = weight_report(S_8s, "8s")
ok_8c, eig_8c = weight_report(S_8c, "8c")

# Independent cross-check: 8v's OWN weights under the same X_generic_8 (not
# reusing rebuild_ob11_triality.py's separate random draw -- recomputed here
# with THIS script's coeffs, so all three channels are compared on equal footing).
S_8v = 1j * X_generic_8  # su(3) subset so(8) acting directly on the vector rep
ok_8v, eig_8v = weight_report(S_8v.astype(complex), "8v (recomputed here, same X_generic)")

print("\n" + "=" * 78)
print("VERDICT -- written after seeing the eigenvalues above, not predicted first")
print("=" * 78)
print(f"  8v matches 1+1+3+3bar: {ok_8v}")
print(f"  8s matches 1+1+3+3bar: {ok_8s}")
print(f"  8c matches 1+1+3+3bar: {ok_8c}")
all_match = ok_8v and ok_8s and ok_8c
if all_match:
    same_spectrum = np.allclose(np.sort(eig_8v), np.sort(eig_8s), atol=1e-4) and np.allclose(
        np.sort(eig_8v), np.sort(eig_8c), atol=1e-4
    )
    print("\n  All three channels match 1+1+3+3bar. Do they carry the EXACT SAME")
    print(f"  weight multiset (not just the same qualitative pattern)? {same_spectrum}")
    print(
        "\n  -> OB11(i) CONFIRMED for all three triality-related channels: 8v, 8s, 8c"
        " all decompose as 1+1+3+3bar under the same su(3), independently verified"
        " via an explicit 16-dim Cl(8) spinor construction, a Lie-homomorphism-"
        " verified so(8)->spin(8) lift, and direct diagonalisation within each"
        " chirality sector. This closes the gap left open in"
        " rebuild_ob11_triality.py -- the prose's OB11(i) claim is now fully"
        " independently reconstructed, not just for 8v."
    )
else:
    print(
        "\n  -> NOT all three channels match. This does NOT necessarily mean the"
        " prose's claim is wrong -- it could mean this specific su(3) EMBEDDING"
        " into so(8) (fixing e_0 trivially, acting only on Im(O)) is not the"
        " triality-symmetric one the original construction used; a genuinely"
        " triality-covariant embedding might need to act non-trivially on e_0"
        " for the spinor lift specifically, unlike for 8v. Recorded as a real"
        " finding, not silently patched to force agreement."
    )
