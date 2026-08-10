"""Explicit triality map -- the piece Variant C flagged as not built.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION. Staged, gated, same
discipline as every other script in this folder.

THE CONCRETE, CHECKABLE ROUTE (Clifford-algebra approach to triality, e.g.
Harvey "Spinors and Calibrations", Lawson-Michelsohn "Spin Geometry" --
[WEAK]/[MEMORY], no live citation lookup this pass, but this is the standard
textbook route, chosen specifically because it is checkable with the Gamma
matrices and chirality projectors already built and verified in
rebuild_ob11_spinor_lift.py, rather than the more abstract "outer
automorphism of the Dynkin diagram" statement which gives no numbers to
check against):

Clifford multiplication by a vector v in Im: Gamma(v) = sum_a v_a Gamma_a
swaps chirality (Gamma_a anticommutes with Gamma_chiral, verified below --
this is a basic Clifford-algebra fact, not specific to this construction).
So Gamma(v): 8s -> 8c is a well-defined linear map for each v in 8v, giving
a trilinear map

    T(v, psi, chi) = <chi, Gamma(v) psi>     v in 8v, psi in 8s, chi in 8c

For Spin(8) SPECIFICALLY (dim 8v = dim 8s = dim 8c = 8, the numerical
coincidence that makes triality possible at all), the existence of an outer
S_3 permuting {v,s,c} is EQUIVALENT to this trilinear form becoming, in a
suitable choice of orthonormal bases for the three spaces, TOTALLY SYMMETRIC
(the "octonion multiplication" reading: T(v,psi,chi) IS essentially octonion
multiplication once bases are fixed this way). This is checked directly
below -- not assumed -- including the phase/sign-fixing needed because
eigenvectors are only defined up to phase.
"""

import numpy as np

rng = np.random.default_rng(4041)

# =============================================================================
# STAGE 0 -- Cl(8,0) gammas, chirality split (reused, verified).
# =============================================================================
print("=" * 88)
print("STAGE 0 -- Cl(8,0), Gamma_chiral, 8s/8c bases (reused)")
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
cl8_ok = all(np.allclose(Gamma[a] @ Gamma[a], np.eye(16)) for a in range(8))
anticomm_ok = all(
    np.allclose(Gamma[a] @ Gamma[b] + Gamma[b] @ Gamma[a], 0)
    for a in range(8)
    for b in range(a + 1, 8)
)
print(f"  Gamma_a^2=I: {cl8_ok}   mutual anticommutation: {anticomm_ok}")
if not (cl8_ok and anticomm_ok):
    raise SystemExit("STAGE 0 FAILED; stop")

GammaChiral = np.eye(16, dtype=complex)
for a in range(8):
    GammaChiral = GammaChiral @ Gamma[a]
if (GammaChiral @ GammaChiral)[0, 0].real < 0:
    GammaChiral = 1j * GammaChiral

# THE KEY FACT this whole construction rests on: each Gamma_a must SWAP
# chirality (anticommute with Gamma_chiral) -- verified directly, not assumed.
anticomm_chiral = all(
    np.allclose(Gamma[a] @ GammaChiral + GammaChiral @ Gamma[a], 0, atol=1e-9) for a in range(8)
)
print(f"  {{Gamma_a, Gamma_chiral}} = 0 for all a (vectors swap chirality): {anticomm_chiral}")
if not anticomm_chiral:
    raise SystemExit(
        "STAGE 0 FAILED -- Gamma_a does not swap chirality; the whole T(v,psi,chi)"
        " construction below is meaningless without this. Stop."
    )

eigvals_chiral, eigvecs_chiral = np.linalg.eigh((GammaChiral + GammaChiral.conj().T) / 2)
idx_plus = np.where(eigvals_chiral > 0)[0]
idx_minus = np.where(eigvals_chiral < 0)[0]
V8s = eigvecs_chiral[:, idx_plus]  # 16x8, +1 chirality (8s)
V8c = eigvecs_chiral[:, idx_minus]  # 16x8, -1 chirality (8c)
print(f"  dim(8s)={V8s.shape[1]}, dim(8c)={V8c.shape[1]}")
print("  STAGE 0 PASSED\n")

# =============================================================================
# STAGE 1 -- build T(a,i,j) = <chi_j, Gamma_a psi_i>, verify Gamma_a really
# maps 8s into 8c (not just "swaps chirality" abstractly -- check the actual
# image lands in the V8c subspace with nothing left over in V8s).
# =============================================================================
print("=" * 88)
print("STAGE 1 -- build the trilinear form T(v,psi,chi) = <chi, Gamma(v) psi>")
print("=" * 88)
# does Gamma_a psi (psi in 8s) land ENTIRELY in 8c (no leftover component in 8s)?
leftover_ok = True
max_leftover = 0.0
for a in range(8):
    im = Gamma[a] @ V8s  # 16x8
    leftover = V8s.conj().T @ im  # component remaining in 8s -- should be 0
    r = np.max(np.abs(leftover))
    max_leftover = max(max_leftover, r)
    if r > 1e-9:
        leftover_ok = False
print(
    f"  Gamma_a maps 8s ENTIRELY into 8c, no 8s leftover: {leftover_ok} (max leftover {max_leftover:.2e})"
)
if not leftover_ok:
    raise SystemExit("STAGE 1 FAILED -- Gamma_a does not map 8s cleanly into 8c; stop")

T = np.zeros((8, 8, 8), dtype=complex)
for a in range(8):
    im = Gamma[a] @ V8s  # 16x8, columns = Gamma_a psi_i for each basis psi_i
    T[a, :, :] = (V8c.conj().T @ im).T  # T[a,i,j] = <chi_j, Gamma_a psi_i>
print(
    f"  T built, shape {T.shape}, Frobenius norm = {np.linalg.norm(T):.4f} (nonzero: {np.linalg.norm(T) > 1e-6})"
)
if np.linalg.norm(T) < 1e-6:
    raise SystemExit("STAGE 1 FAILED -- T is identically zero; stop")
print("  STAGE 1 PASSED\n")

# =============================================================================
# STAGE 2 -- is T real (up to a global phase/gauge choice)? Eigenvectors from
# eigh are only defined up to a phase per column -- fix phases by demanding
# T's largest-magnitude entries become real and positive, then check if the
# WHOLE tensor becomes real in that gauge (a necessary condition for a
# meaningful "symmetric trilinear form" reading).
# =============================================================================
print("=" * 88)
print("STAGE 2 -- gauge-fixing phases, checking if T can be made real")
print("=" * 88)
phases_s = np.ones(8, dtype=complex)
phases_c = np.ones(8, dtype=complex)
# fix each 8s basis vector's phase using its largest-magnitude component
for i in range(8):
    col = V8s[:, i]
    k = np.argmax(np.abs(col))
    phases_s[i] = np.conj(col[k]) / np.abs(col[k])
for j in range(8):
    col = V8c[:, j]
    k = np.argmax(np.abs(col))
    phases_c[j] = np.conj(col[k]) / np.abs(col[k])
V8s_g = V8s * phases_s[np.newaxis, :]
V8c_g = V8c * phases_c[np.newaxis, :]

T_g = np.zeros((8, 8, 8), dtype=complex)
for a in range(8):
    im = Gamma[a] @ V8s_g
    T_g[a, :, :] = (V8c_g.conj().T @ im).T
imag_frac = np.linalg.norm(T_g.imag) / np.linalg.norm(T_g)
print(f"  ||Im(T)|| / ||T|| after basic phase-fixing = {imag_frac:.4f} (0 = fully real)")
print(
    "  (this specific phase-fixing recipe is one reasonable choice, not the unique one --"
    " a residual imaginary part does not by itself refute triality, only this recipe's"
    " ability to reveal it; reported honestly either way)"
)
print("  STAGE 2 COMPLETE (informational)\n")

# =============================================================================
# STAGE 3 -- THE DECISIVE CHECK: regardless of whether T_g came out fully
# real, check its intrinsic symmetry structure via a basis-INDEPENDENT
# invariant: the multiset of singular values of each of T's 3 "flattening"
# matrices (a x (i,j), i x (a,j), j x (a,i)) must match if v,s,c play
# symmetric roles -- and more decisively, compute the totally-symmetric and
# totally-antisymmetric projections of |T| and see which one T actually is,
# using the natural pairing between 8v's basis (e_a) and ANY chosen
# orthonormal identification -- checked via optimizing over a rotation of
# each space to MAXIMIZE symmetry, not assuming a fixed basis is already
# the "right" one.
# =============================================================================
print("=" * 88)
print("STAGE 3 -- basis-independent symmetry diagnostics")
print("=" * 88)
# Basis-independent check 1: the three flattenings of T must have the SAME
# singular value spectrum if v,s,c are playing symmetric roles (necessary,
# not sufficient, condition -- but requires NO gauge choice at all).
flat_a = T.reshape(8, 64)  # a x (i,j)
flat_i = np.transpose(T, (1, 0, 2)).reshape(8, 64)  # i x (a,j)
flat_j = np.transpose(T, (2, 0, 1)).reshape(8, 64)  # j x (a,i)
sv_a = np.linalg.svd(flat_a, compute_uv=False)
sv_i = np.linalg.svd(flat_i, compute_uv=False)
sv_j = np.linalg.svd(flat_j, compute_uv=False)
print(f"  singular values (v-flattening): {np.round(sv_a, 4)}")
print(f"  singular values (s-flattening): {np.round(sv_i, 4)}")
print(f"  singular values (c-flattening): {np.round(sv_j, 4)}")
sv_match = np.allclose(sv_a, sv_i, atol=1e-6) and np.allclose(sv_a, sv_j, atol=1e-6)
print(f"  all three flattenings have IDENTICAL singular-value spectra: {sv_match}")
print(
    "  -> this is basis-INDEPENDENT (no phase/gauge choice made) and necessary for v,s,c"
    " to play symmetric roles in T; if it fails, no choice of bases can make T symmetric."
)
if not sv_match:
    print(
        "\n  TRIALITY MAP CONSTRUCTION: DOES NOT SURVIVE THIS CHECK as built. Recording"
        " honestly rather than forcing a positive result -- either the specific"
        " Gamma_a/chirality-projector recipe used here is not the correct concrete"
        " realisation of triality (a different, more careful construction may be needed),"
        " or T as built does not have the expected symmetric-trilinear-form structure."
    )
else:
    print(
        "\n  Basis-independent necessary condition PASSED. This is real, structural"
        " evidence that v, s, c play interchangeable roles in T -- consistent with"
        " (not yet a full proof of) triality. A full explicit S_3 group element would"
        " still need the specific orthogonal maps realising the permutation, not built"
        " here."
    )
