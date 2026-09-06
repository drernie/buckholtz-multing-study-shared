"""P205 -- what observable breaks FINDING_P133's rank-2 degeneracy?

P133 established that the observable set
    O1 = A g^2,   O2 = A kappa^2,   O3 = kappa / g
has rank(Jacobian) = 2 < 3 in the parameters (A, g, kappa), because
O2 = O1 * O3^2 identically. That is STRUCTURAL non-identifiability:
no amount of precision on O1, O2, O3 fixes (A, g, kappa).

This script asks the constructive question P133 did not: for a candidate
new observable of monomial form

    O4 = A^a g^b kappa^c

which exponent triples (a, b, c) actually RAISE the rank to 3?

Method: work in log space, where monomials become linear. Then
rank-raising is a linear-independence question, solvable exactly.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import sympy as sp


def log_exponent_vectors() -> tuple[sp.Matrix, list[str]]:
    """Rows are (d log O / d log A, d log O / d log g, d log O / d log kappa)."""
    rows = [
        (1, 2, 0),  # O1 = A g^2
        (1, 0, 2),  # O2 = A kappa^2
        (0, -1, 1),  # O3 = kappa / g
    ]
    return sp.Matrix(rows), ["O1 = A g^2", "O2 = A k^2", "O3 = k / g"]


def main() -> int:
    A, g, k = sp.symbols("A g kappa", positive=True)
    a, b, c = sp.symbols("a b c", real=True)

    print("=" * 70)
    print("P205 -- break condition for P133's rank-2 identifiability failure")
    print("=" * 70)

    # --- Positive control: reproduce P133's rank-2 result from the Jacobian ---
    obs = sp.Matrix([A * g**2, A * k**2, k / g])
    J = obs.jacobian([A, g, k])
    rank_direct = J.rank()
    print(f"\nPC1 [positive control] rank of Jacobian of (O1,O2,O3): {rank_direct}")
    assert rank_direct == 2, f"expected P133's rank 2, got {rank_direct}"
    print("     matches FINDING_P133 (rank 2 < 3). Control PASSES.")

    # --- The identity that causes it, verified rather than asserted ---
    residual = sp.simplify(obs[1] - obs[0] * obs[2] ** 2)
    print(f"\nPC2 [identity] O2 - O1*O3^2 simplifies to: {residual}")
    assert residual == 0, "the O2 = O1 O3^2 identity failed"
    print("     the degeneracy is exactly this identity. Control PASSES.")

    # --- Log-space: monomials become linear, so rank is a span question ---
    M, labels = log_exponent_vectors()
    print("\nLog-exponent vectors (d log O / d(log A, log g, log kappa)):")
    for row, lab in zip(M.tolist(), labels, strict=True):
        print(f"    {lab:14s} -> {row}")
    print(f"    rank in log space: {M.rank()}  (same 2, as it must be)")

    # --- The span, solved exactly ---
    alpha, beta = sp.symbols("alpha beta", real=True)
    generic = alpha * sp.Matrix([[1, 2, 0]]) + beta * sp.Matrix([[0, -1, 1]])
    sol = sp.solve(
        [sp.Eq(a, generic[0]), sp.Eq(b, generic[1]), sp.Eq(c, generic[2])],
        [alpha, beta],
        dict=True,
    )
    print(f"\nSolving (a,b,c) = alpha*(1,2,0) + beta*(0,-1,1):  {sol}")

    # Consistency of that system requires one relation among (a,b,c). Find it.
    aug = sp.Matrix([[1, 0, a], [2, -1, b], [0, 1, c]])
    cond = sp.simplify(aug.det())
    print(f"\nCompatibility condition (det of augmented system) = {cond}")
    print(f"  => (a,b,c) lies IN the degenerate span  iff  {sp.Eq(cond, 0)}")

    break_cond = sp.simplify(-cond)
    print(f"\n{'=' * 70}\nBREAK CONDITION\n{'=' * 70}")
    print("  A new observable O4 = A^a g^b kappa^c raises the rank to 3")
    print(f"  if and only if:   {break_cond} != 0")
    print("  equivalently:     2a != b + c")

    # --- Verify on concrete candidates, by actually recomputing the rank ---
    print(f"\n{'=' * 70}\nCHECK ON CANDIDATES (rank recomputed each time)\n{'=' * 70}")
    candidates = [
        ((1, 0, 0), "A alone"),
        ((0, 1, 0), "g alone"),
        ((0, 0, 1), "kappa alone"),
        ((1, 1, 1), "A g kappa"),
        ((2, 2, 0), "A^2 g^2"),
        ((1, 2, 0), "A g^2  (= O1, must NOT break)"),
        ((0, -1, 1), "kappa/g (= O3, must NOT break)"),
    ]
    for (ea, eb, ec), name in candidates:
        O4 = sp.Matrix([A**ea * g**eb * k**ec])
        J4 = sp.Matrix.vstack(obs, O4).jacobian([A, g, k])
        r = J4.rank()
        predicted = 3 if (2 * ea - eb - ec) != 0 else 2
        mark = "BREAKS " if r == 3 else "no     "
        agree = "ok" if r == predicted else "MISMATCH"
        print(f"  ({ea:2d},{eb:2d},{ec:2d}) {name:28s} rank={r}  {mark} [{agree}]")
        assert r == predicted, f"break condition mispredicted for {name}"

    print(f"\n{'=' * 70}")
    print("CONCLUSION: the degeneracy is broken by ANY observable whose")
    print("exponents violate 2a = b + c. In particular a DIRECT measurement")
    print("of any ONE of A, g, kappa alone suffices -- no combination of")
    print("further O1/O2/O3-type observables ever will, at any precision.")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
