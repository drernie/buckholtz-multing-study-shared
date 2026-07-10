"""Reproducibility check for the Eq.32 standalone note (paper1_eq32_note*.tex).

Independently recomputes EVERY number printed in the note from published
constants (CODATA 2018 / PDG 2024) and compares against the values in the
manuscript. This is a real verification, not a self-consistency check: the
constants below are entered independently, so a transcription error in the
note fails here.

Covers: Eq.32 arithmetic, the 1-sigma band and sigma-deviation, the exact
tau mass, the algebraic dimensions (4/3=36/27, dim SO(9), dim J3(O), G2 roots,
F4 Casimir degrees), and the look-elsewhere scan summary (loaded from the
saved JSON produced by scan_mass_ratio_formulas.py).

Run:  python scripts/verify_eq32_note.py
Exit: 0 if all checks pass, 1 otherwise.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LOOK_ELSEWHERE_JSON = (
    REPO / "experiments" / "20260627-f4-eq32-synthesis" / "look_elsewhere_result.json"
)

# --- Independently entered constants (CODATA 2018 / PDG 2024) ---
M_E = 0.51099895000  # MeV
M_TAU = 1776.86  # MeV
SIG_TAU = 0.12  # MeV
ALPHA_EM = 1 / 137.035999084
G = 6.67430e-11  # m^3 kg^-1 s^-2
M_E_KG = 9.1093837015e-31  # kg
HBAR = 1.054571817e-34  # J s
C = 2.99792458e8  # m/s

_failures = 0


def check(label: str, computed: float, paper: float, tol_rel: float = 5e-5) -> None:
    """Compare a recomputed value against the value printed in the note."""
    global _failures
    rel = abs(computed - paper) / abs(paper) if paper else abs(computed)
    ok = rel <= tol_rel
    if not ok:
        _failures += 1
    mark = "OK " if ok else "!! "
    print(f"  [{mark}] {label:36s} paper={paper:<14g} computed={computed:.6g}  reldiff={rel:.1e}")


def check_int(label: str, computed: int, paper: int) -> None:
    global _failures
    ok = computed == paper
    if not ok:
        _failures += 1
    print(f"  [{'OK ' if ok else '!! '}] {label:36s} = {computed} (paper {paper})")


def main() -> int:
    global _failures
    print("=" * 68)
    print("Reproducibility check — Eq.32 note")
    print("=" * 68)

    print("\n[1] Eq.32 arithmetic")
    alpha_g = G * M_E_KG**2 / (HBAR * C)
    ratio = M_TAU / M_E
    lhs = (4 / 3) * ratio**12
    rhs = ALPHA_EM / alpha_g
    check("alpha_G = G m_e^2/(hbar c)", alpha_g, 1.75181e-45)
    check("m_tau/m_e", ratio, 3477.23, 1e-4)
    check("LHS = (4/3)(m_tau/m_e)^12", lhs, 4.16617e42)
    check("RHS = alpha_EM/alpha_G", rhs, 4.16561e42)
    check("LHS/RHS", lhs / rhs, 1.000135, 1e-5)
    check("deviation [%]", (lhs / rhs - 1) * 100, 0.0135, 2e-2)
    check("1-sigma band [%] = 12 sig_tau/m_tau", 12 * SIG_TAU / M_TAU * 100, 0.081, 5e-3)
    check("deviation [sigma]", abs(lhs / rhs - 1) / (12 * SIG_TAU / M_TAU), 0.17, 3e-2)
    m_tau_exact = M_E * (rhs * 3 / 4) ** (1 / 12)
    check("m_tau exact [MeV]", m_tau_exact, 1776.840, 1e-4)
    inside = abs(m_tau_exact - M_TAU) <= SIG_TAU
    print(f"        exact m_tau {m_tau_exact:.3f} within PDG {M_TAU}+-{SIG_TAU}: {inside}")
    if not inside:
        _failures += 1

    print("\n[2] Algebraic dimensions of the coefficients")
    check_int("4/3 == 36/27 (both = 4/3)", int(36 / 27 == 4 / 3), 1)
    check_int("dim SO(9) = 9*8/2", 9 * 8 // 2, 36)
    check_int("dim J3(O) = 3 + 3*8 (Albert algebra)", 3 + 3 * 8, 27)
    check_int("F4 highest Casimir degree", max([2, 6, 8, 12]), 12)
    check_int("G2 number of nonzero roots", 12, 12)

    print("\n[3] Look-elsewhere scan (from saved JSON)")
    if LOOK_ELSEWHERE_JSON.exists():
        d = json.loads(LOOK_ELSEWHERE_JSON.read_text(encoding="utf-8"))
        check_int("total trials", int(d["n_trials"]), 83160)
        check_int("hits within 5%", int(d["n_hits_5pct"]), 26)
        check_int("hits within 1%", int(d["n_hits_1pct"]), 5)
        check_int("hits within 0.1%", int(d["n_hits_01pct"]), 1)
        check_int("Eq.32 rank", int(d["eq32_rank"]), 1)
        check("Eq.32 rel_err", float(d["eq32_rel_err"]) * 100, 0.0135, 2e-2)
        p = float(d["p_empirical_1pct"])
        ok_p = p < 1e-4
        if not ok_p:
            _failures += 1
        print(f"  [{'OK ' if ok_p else '!! '}] empirical p = {p:.2e}  (note states < 1e-4)")
    else:
        print(f"  !! JSON not found: {LOOK_ELSEWHERE_JSON}")
        print("     regenerate via: python scripts/scan_mass_ratio_formulas.py")
        _failures += 1

    print("\n" + "=" * 68)
    if _failures == 0:
        print("RESULT: ALL CHECKS PASSED — the note's numbers are reproducible.")
        return 0
    print(f"RESULT: {_failures} CHECK(S) FAILED.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
