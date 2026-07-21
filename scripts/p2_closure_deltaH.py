"""p2_closure_deltaH.py — P2 constructive test of the docs/126 non-uniqueness lemma.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

docs/126 lemma: with F_oP fixed but the evolution law q_i(a)=k_i r_i unspecified,
the BACKGROUND expansion H(a) is claimed non-unique — two admissible q(a) laws
should give different H(a).

This script executes the 4-step counterexample under the Shtanov & Sahni (arXiv:
1010.6205) BACKGROUND closure (their Sec. II a-dot-dot/a equation), which is the
closure the lemma actually needs (the background H, not the Sec. III peculiar-energy
diagnostic). It includes a POSITIVE CONTROL: a deliberately-wrong closure in which q
does NOT wash out, to prove the test can detect non-uniqueness when it is present —
so a null result is a physics statement, not a broken test always returning zero.

Result (see docs/127): under the real S&S background closure, dH = 0 to machine
precision for ANY two q(a) laws, because the background coupling of every sub-1/r
term is G*lim_{r->inf}[f - r f'] = 0 (dipole 1/r^2, quadrupole 1/r^3), leaving only
the mass monopole (G_eff = G). The lemma is FALSIFIED for the background closure:
the missing q(a) does NOT make the background H(z) ambiguous under S&S. (Any q(a)
freedom lives in Sec. III structure-formation observables, not H(z) — a weaker
claim than the lemma stated.)

Run:  python scripts/p2_closure_deltaH.py
Exit: 0 always (this is a report; the scientific verdict is in the printout + docs/127).
"""

from __future__ import annotations

import numpy as np

# ---- cosmological toy background (dimensionless, E = H/H0) --------------------
OMEGA_M = 0.3
OMEGA_L = 0.7
A_GRID = np.linspace(0.1, 1.0, 91)  # scale factor a in [0.1, 1]


def q_frozen(a: np.ndarray) -> np.ndarray:
    """Law 1: frozen charge q(a) = q(a0) = const (dq/da = 0)."""
    return np.ones_like(a)


def q_virial(a: np.ndarray) -> np.ndarray:
    """Law 2: virial charge q ∝ G M(a)^2 with cluster mass growth M(a) ∝ a.

    q(a) ∝ a^2, normalized to q(1) = 1 so both laws share identical initial data
    at a0=1 (docs/126 A5). dq/da = 2a ≠ 0 — genuinely different evolution.
    """
    return a**2  # already q(1)=1


def E_real_closure(a: np.ndarray, q_of_a: np.ndarray) -> np.ndarray:
    """Shtanov-Sahni BACKGROUND closure. G_eff = G (dipole/quad couplings vanish
    by the r->inf limit, verified symbolically: G*lim[f-rf'] = 0 for 1/r^2, 1/r^3).
    So the background is pure matter + Lambda; q(a) enters NOWHERE.
    """
    del q_of_a  # deliberately unused: the whole point is q does not enter
    return np.sqrt(OMEGA_M * a**-3 + OMEGA_L)


def E_control_closure(a: np.ndarray, q_of_a: np.ndarray, omega_q: float = 0.05) -> np.ndarray:
    """POSITIVE CONTROL — a deliberately WRONG closure in which the dipole DID NOT
    wash out, so the q-charge density (rho_q ∝ n*q ∝ a^-3 * q(a)) sources an extra
    background term. This is NOT physical under S&S; it exists only to prove the
    test detects non-uniqueness when q genuinely enters. Renormalized so E(1)=1.
    """
    extra = omega_q * q_of_a * a**-3  # rho_q-sourced term ∝ q(a) a^-3
    raw = OMEGA_M * a**-3 + OMEGA_L + extra
    # renormalize to E(1)=1 by shifting the constant (Lambda-like) piece
    raw1 = OMEGA_M + OMEGA_L + omega_q * 1.0 * 1.0
    return np.sqrt(raw / raw1)


def report(label: str, closure) -> float:
    q1, q2 = q_frozen(A_GRID), q_virial(A_GRID)
    E1, E2 = closure(A_GRID, q1), closure(A_GRID, q2)
    dE = E2 - E1
    frac = np.max(np.abs(dE) / np.maximum(E1, 1e-30))
    print(f"\n{label}")
    print("  q-law 1 (frozen)  q(a)=1        dq/da=0")
    print("  q-law 2 (virial)  q(a)=a^2      dq/da=2a  (both q(1)=1, identical ICs)")
    print(f"  max |dE|          = {np.max(np.abs(dE)):.3e}")
    print(f"  max |dE|/E (frac) = {frac:.3e}")
    print(
        f"  at a=0.5:  E1={E1[A_GRID.searchsorted(0.5)]:.6f}  "
        f"E2={E2[A_GRID.searchsorted(0.5)]:.6f}  "
        f"dE={dE[A_GRID.searchsorted(0.5)]:.3e}"
    )
    return frac


def main() -> int:
    print("=" * 70)
    print("P2 — dH(a) for two admissible q(a) laws (docs/126 counterexample)")
    print("=" * 70)
    print("Noise floor for 'zero': ~1e-15 (float64 machine epsilon).")

    frac_real = report(
        "[REAL] Shtanov-Sahni background closure (G_eff=G, q absent):", E_real_closure
    )
    frac_ctrl = report(
        "[CONTROL] wrong closure where q DID NOT wash out (unphysical):", E_control_closure
    )

    print("\n" + "=" * 70)
    print("VERDICT")
    print("=" * 70)
    noise = 1e-12
    if frac_real < noise:
        print(f"  REAL closure:    dH = 0 to machine precision ({frac_real:.1e} < {noise:.0e})")
        print("                   -> lemma FALSIFIED for the S&S BACKGROUND closure.")
        print("                   -> background H(z) is UNIQUE (G_eff=G) regardless of q(a).")
    else:
        print(f"  REAL closure:    dH = {frac_real:.3e} (nonzero) -> lemma would SURVIVE.")
    if frac_ctrl > noise:
        print(f"  CONTROL closure: dH = {frac_ctrl:.3e} (nonzero, as designed)")
        print("                   -> the test CAN detect non-uniqueness when q genuinely")
        print("                      enters. So the REAL-closure null is a physics result,")
        print("                      not a broken test.")
    else:
        print(f"  CONTROL closure: dH = {frac_ctrl:.1e} -- WARNING: control failed to")
        print("                   register; the test may be broken. Do NOT trust the null.")
    print("\n  See docs/127 for the full write-up and the (weaker) claim that survives:")
    print("  q(a) freedom affects Sec.III structure-formation observables, NOT H(z).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
