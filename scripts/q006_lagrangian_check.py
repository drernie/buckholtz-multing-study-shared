"""q006_lagrangian_check.py — verify the constructed MULTING pair potential reproduces F_oP.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

Q006 (docs/129): the preprint specifies MULTING at the level of two-body FORCES only
(no action / Lagrangian in the corpus). A non-relativistic many-body Lagrangian can be
CONSTRUCTED because F_oP is a sum of central pair forces. This script verifies the
pair potential V_ij reproduces the preprint's radial force F_oP = F_m - F_d + F_q
(Eqs. 14-16) exactly, i.e. F_r = -dV/dr with residual 0.

IMPORTANT (skeptic-reviewed, docs/129): existence of this Lagrangian is textbook-
trivial for any central pair potential and does NOT close Q006. The cosmological
question hinges on whether the scalar charge k responds to external tidal fields
(coupling η, tidal heating) -- which the corpus neither includes nor forbids. This
script only checks the algebra of the force<->potential step, nothing about η,
covariant completion, or cosmological degeneracy.

Run:  python scripts/q006_lagrangian_check.py
Exit: 0 if -dV/dr reproduces F_oP exactly, else 1.
"""

from __future__ import annotations

import sys

import sympy as sp


def main() -> int:
    r, G, c, bd, bq, mi, mj, qi, qj = sp.symbols(
        "r G c beta_d beta_q m_i m_j q_i q_j", positive=True
    )
    # Constructed pair potential (docs/125 bilinear kernel; q_i = k_i r_i):
    V = (
        -G * mi * mj / r
        + (G * bd / (2 * c**2)) * (mi * qj + mj * qi) / r**2
        - (G * bq**2 / (3 * c**4)) * qi * qj / r**3
    )
    Fr = sp.simplify(-sp.diff(V, r))  # radial force, outward positive

    # Target: preprint Eqs. 14-16, F_oP = F_m - F_d + F_q, radial (-A/r^2 + B/r^3 - C/r^4)
    A = G * mi * mj
    B = (G * bd / c**2) * (qi * mj + qj * mi)
    Cc = (G * bq**2 / c**4) * qi * qj
    target = -A / r**2 + B / r**3 - Cc / r**4

    residual = sp.simplify(Fr - target)
    print("=" * 70)
    print("Q006 — MULTING pair potential reproduces F_oP ?")
    print("=" * 70)
    print("V_ij(r) = -G m_i m_j/r + (Gβ_d/c²)(m_i q_j + m_j q_i)/r²")
    print("          - (Gβ_q²/3c⁴) q_i q_j/r³        [q_i = k_i r_i]")
    print(f"\nresidual  (-dV/dr) - F_oP_radial  =  {residual}")
    ok = residual == 0
    print(f"\n{'PASS' if ok else 'FAIL'}: the non-relativistic many-body Lagrangian")
    print("  L = Σ ½ m_i ẋ_i² - ½ Σ_{i≠j} V_ij  reproduces F_oP by Euler-Lagrange.")
    print("\nNOTE (docs/129, skeptic-reviewed): this is a trivial existence check for a")
    print("central pair potential. It does NOT close Q006 -- the scalar tidal-response")
    print("coupling η (k responding to ∇∇Φ) is unfixed by the corpus and controls the")
    print("linear-growth signature. 'Not specified' != '= 0'.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
