"""factorization_gate.py — P1 Universality/Factorization Gate for F_oP

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

Question (docs/125, session 24): can Buckholtz's two-body force F_oP = F_m - F_d + F_q
(preprint Eqs. 14-17) be written as F_ij = -grad of a potential built from a kernel
that is GLOBAL (the same for every object pair), so that Shtanov & Sahni's
single-kernel cosmological bridge (arXiv:1010.6205) could apply?

Two levels are tested:
  1. single universal SCALAR kernel  F_ij = -m_i m_j d/dr phi(r)  -> FAILS (confirms NR-016)
  2. finite 2x2 MATRIX kernel with per-object charge Q_i=(m_i, q_i), q_i=k_i r_i -> EXACT

This script establishes ONLY the algebraic factorization structure. Whether the
2x2-matrix case actually revives a (multi-component) Shtanov bridge is a separate
question handled in docs/125 (under skeptic review) — passing this gate is a
PRECONDITION for attempting that extension, not proof it works.

Run:  python scripts/factorization_gate.py
Exit: 0 if the 2x2 factorization is exact (all residuals 0), 1 otherwise.
"""

from __future__ import annotations

import sys

import sympy as sp


def main() -> int:
    # per-object quantities (object i and object j)
    m_i, m_j, k_i, k_j, r_i, r_j = sp.symbols("m_i m_j k_i k_j r_i r_j", positive=True)
    # global constants of the framework
    G, c, beta_d, beta_q = sp.symbols("G c beta_d beta_q", positive=True)

    # Preprint pair-force coefficients, r-power stripped per multipole (Eqs. 14-16):
    #   monopole  F_m ~ A/r^2,  A = G m_i m_j
    #   dipole    F_d ~ B/r^3,  B = (2 G beta_d/c^2)(k_i r_i m_j + k_j r_j m_i)   [r_dA=beta_d r_A]
    #   quadrupole F_q ~ C/r^4, C = (G beta_q^2/c^4)(k_i r_i)(k_j r_j)           [r_qAB^2=beta_q^2 r_A r_P]
    A_coeff = G * m_i * m_j
    B_coeff = (G * beta_d / c**2) * (k_i * r_i * m_j + k_j * r_j * m_i)
    C_coeff = (G * beta_q**2 / c**4) * (k_i * r_i) * (k_j * r_j)

    print("=" * 70)
    print("P1 FACTORIZATION GATE — F_oP as a global pairwise kernel?")
    print("=" * 70)

    # --- Test 1: single universal scalar kernel -----------------------------
    # F_ij = -m_i m_j d/dr phi(r) requires each coeff/(m_i m_j) to be
    # pair-INDEPENDENT (a function of r and global constants only).
    print("\n[1] single universal SCALAR kernel  F_ij = -m_i m_j d/dr phi(r):")
    for name, coeff in (("monopole", A_coeff), ("dipole", B_coeff), ("quad", C_coeff)):
        reduced = sp.simplify(coeff / (m_i * m_j))
        pair_dependent = bool(reduced.free_symbols & {m_i, m_j, k_i, k_j, r_i, r_j})
        flag = "PAIR-DEPENDENT (breaks single kernel)" if pair_dependent else "ok (global)"
        print(f"    {name:9s}/(m_i m_j) = {reduced}   -> {flag}")
    print("    VERDICT: single scalar kernel FAILS (dipole & quad carry k_i r_i / m_i).")

    # --- Test 2: finite 2x2 matrix kernel -----------------------------------
    # Per-object charge vector Q_i = (m_i, q_i), q_i = k_i r_i.
    # Bilinear form Q_i^T K(r) Q_j with GLOBAL symmetric matrix K(r):
    #   kappa_mm on 1/r  (-> 1/r^2 force),  kappa_mq on 1/r^2 (-> 1/r^3),
    #   kappa_qq on 1/r^3 (-> 1/r^4).
    q_i, q_j = k_i * r_i, k_j * r_j
    kappa_mm, kappa_mq, kappa_qq = G, G * beta_d / c**2, G * beta_q**2 / c**4
    A_rec = kappa_mm * m_i * m_j
    B_rec = kappa_mq * (m_i * q_j + m_j * q_i)
    C_rec = kappa_qq * q_i * q_j

    print("\n[2] finite 2x2 MATRIX kernel  Q_i=(m_i, k_i r_i), global K(r):")
    residuals = {
        "A (monopole)": sp.simplify(A_coeff - A_rec),
        "B (dipole)": sp.simplify(B_coeff - B_rec),
        "C (quadrupole)": sp.simplify(C_coeff - C_rec),
    }
    for name, res in residuals.items():
        print(f"    residual {name:16s} = {res}")
    for entry, val in (("kappa_mm", kappa_mm), ("kappa_mq", kappa_mq), ("kappa_qq", kappa_qq)):
        print(f"    {entry} = {val}   (pair-independent / global)")

    ok = all(res == 0 for res in residuals.values())
    print(
        "\n    VERDICT: "
        + (
            "2x2 matrix kernel reproduces F_oP EXACTLY. "
            "Single charge q_i=k_i r_i serves BOTH dipole (cross q_i m_j) and "
            "quadrupole (q_i q_j)."
            if ok
            else "2x2 factorization FAILED — residual nonzero, see above."
        )
    )
    print("\n    NOTE: this establishes the algebraic factorization only. Whether a")
    print("    multi-component Shtanov-Sahni bridge follows is docs/125 (skeptic-gated):")
    print("    passing here is a PRECONDITION, not proof the cosmological extension works.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
