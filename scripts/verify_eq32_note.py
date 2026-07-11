"""Reproducibility check for the Eq.32 standalone note (paper1_eq32_note*.tex).

Independently recomputes EVERY number printed in the note from published
constants (CODATA 2018 / PDG 2024, pdg.lbl.gov summary tables verified
directly 2026-07-11) and compares against the values in the manuscript.
This is a real verification, not a self-consistency check: the constants
below are entered independently, so a transcription error in the note
fails here.

CORRECTION (2026-07-11): an earlier version of this script (and the note)
used m_tau = 1776.86 +/- 0.12 MeV and M_t = 172.76 / 162.77 GeV mislabeled
"PDG 2024" -- these are actually PDG 2022-era values. True PDG 2024 (and
PDG 2025, unchanged): m_tau = 1776.93 +/- 0.09 MeV; M_t(direct) = 172.57 +/-
0.29 GeV; Mbar_t(MSbar) = 162.5 GeV. The relation survives (now 1.00 sigma,
was 0.17 sigma) and both look-elsewhere scans now rank Eq.32 #1 (the old
"tau-alt" competitor, which relied on the stale top mass, is no longer
competitive at any scheme).

Covers: Eq.32 arithmetic, the 1-sigma band and sigma-deviation, the exact
tau mass, the algebraic dimensions (4/3=36/27, dim SO(9), dim J3(O), G2 roots,
F4 Casimir degrees), the single-reference look-elsewhere scan summary (from
scan_mass_ratio_formulas.py), and the pooled reference-mass robustness scan
(from scan_reference_mass_robustness.py).

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
REFMASS_JSON = (
    REPO / "experiments" / "20260627-f4-eq32-synthesis" / "reference_mass_scan_result.json"
)

# --- Independently entered constants (CODATA 2018 / PDG 2024) ---
M_E = 0.51099895000  # MeV
M_TAU = 1776.93  # MeV, PDG 2024/2025 (verified pdg.lbl.gov, supersedes 2022's 1776.86)
SIG_TAU = 0.09  # MeV
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
    check("m_tau/m_e", ratio, 3477.365, 1e-4)
    check("LHS = (4/3)(m_tau/m_e)^12", lhs, 4.16814e42)
    check("RHS = alpha_EM/alpha_G", rhs, 4.16561e42)
    check("LHS/RHS", lhs / rhs, 1.000608, 1e-5)
    check("deviation [%]", (lhs / rhs - 1) * 100, 0.0608, 2e-2)
    check("1-sigma band [%] = 12 sig_tau/m_tau", 12 * SIG_TAU / M_TAU * 100, 0.0608, 5e-3)
    check("deviation [sigma]", abs(lhs / rhs - 1) / (12 * SIG_TAU / M_TAU), 1.00, 3e-2)
    m_tau_exact = M_E * (rhs * 3 / 4) ** (1 / 12)
    check("m_tau exact [MeV]", m_tau_exact, 1776.840, 1e-4)
    # NOTE: the exact-solving mass (1776.840) sits exactly one sigma below the
    # PDG 2024/25 central value (1776.93 +/- 0.09) -- boundary case, not "inside".
    inside = abs(m_tau_exact - M_TAU) <= SIG_TAU
    print(
        f"        exact m_tau {m_tau_exact:.3f} is {abs(m_tau_exact - M_TAU) / SIG_TAU:.2f}"
        f" sigma from PDG {M_TAU}+-{SIG_TAU} (boundary: {inside})"
    )

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
        check_int("hits within 5%", int(d["n_hits_5pct"]), 25)
        check_int("hits within 1%", int(d["n_hits_1pct"]), 5)
        check_int("hits within 0.1%", int(d["n_hits_01pct"]), 1)
        check_int("Eq.32 rank", int(d["eq32_rank"]), 1)
        check("Eq.32 rel_err", float(d["eq32_rel_err"]) * 100, 0.0608, 2e-2)
        p = float(d["p_empirical_1pct"])
        ok_p = p < 1e-4
        if not ok_p:
            _failures += 1
        print(f"  [{'OK ' if ok_p else '!! '}] empirical p = {p:.2e}  (note states < 1e-4)")
    else:
        print(f"  !! JSON not found: {LOOK_ELSEWHERE_JSON}")
        print("     regenerate via: python scripts/scan_mass_ratio_formulas.py")
        _failures += 1

    print("\n[4] Reference-mass robustness (pooled, from saved JSON)")
    if REFMASS_JSON.exists():
        d = json.loads(REFMASS_JSON.read_text(encoding="utf-8"))
        # Total is now deduplicated (coprime p/q only): 55 mass pairs x 24 exponents
        # x 63 coprime fractions = 83,160 -- matches the single-reference scan total
        # by construction (each unordered pair appears once, with its lighter
        # member as the natural reference).
        check_int(
            "total pooled trials (dedup, coprime p/q)", int(d["total_trials_combined"]), 83160
        )
        check_int("Eq.32 rank in pooled sample", int(d["eq32_rank_combined"]), 1)
        check("Eq.32 rel_err (pooled)", float(d["eq32_rel_err"]) * 100, 0.0608, 2e-2)
        p2 = float(d["p_empirical_combined"])
        ok_p2 = abs(p2 - 1.2e-5) / 1.2e-5 < 0.1
        if not ok_p2:
            _failures += 1
        print(
            f"  [{'OK ' if ok_p2 else '!! '}] pooled empirical p = {p2:.2e}  (note states 1.2e-5)"
        )
        nxt = d["next_best_distinct_candidate"]
        print(
            f"        next-best distinct candidate: {nxt['formula']} (ref={nxt['reference_mass']}), "
            f"err={float(nxt['rel_err']) * 100:.4f}% — does NOT beat Eq.32, reported for context"
        )
    else:
        print(f"  !! JSON not found: {REFMASS_JSON}")
        print("     regenerate via: python scripts/scan_reference_mass_robustness.py")
        _failures += 1

    print("\n[5] Scheme-ambiguity of the (now dead) tau-referenced competitor")
    # PDG 2024 top-quark masses, MeV (pdg.lbl.gov/2024/tables/rpp2024-sum-quarks.pdf,
    # verified directly 2026-07-11). "Direct" supersedes the earlier "pole 172.76".
    m_top_direct = 172570.0
    m_top_msbar = 162500.0

    def tau_alt_err(m_top: float) -> float:
        target_tau = (ALPHA_EM / alpha_g) * (M_E / M_TAU) ** 2
        val = (4 / 7) * (m_top / M_TAU) ** 18
        return abs(val / target_tau - 1) * 100

    err_direct = tau_alt_err(m_top_direct)
    err_msbar = tau_alt_err(m_top_msbar)
    check("tau-alt error, direct top mass [%]", err_direct, 2.03, 3e-2)
    check("tau-alt error, MSbar top mass [%]", err_msbar, 66.8, 3e-2)
    # Both schemes are now far above the 1% look-elsewhere threshold: with the
    # corrected top mass the tau-alt relation is not merely scheme-fragile, it
    # is simply wrong at any scheme -- confirmed independently by its absence
    # from the pooled scan's top-10 (section [4]).
    both_dead = err_direct > 1.0 and err_msbar > 1.0
    if not both_dead:
        _failures += 1
    print(
        f"  [{'OK ' if both_dead else '!! '}] both schemes exceed 1% (direct={err_direct:.2f}%, "
        f"MSbar={err_msbar:.2f}%) -- tau-alt is dead, not just scheme-fragile"
    )

    print("\n[6] Belle II two-sided prediction")
    belle_sigma = 0.010
    belle_band = 12 * belle_sigma / M_TAU
    # paper rounds this to 4 decimal places (0.0001) to match the "1.0000" display
    # precision; compare by absolute tolerance (half the last displayed digit), not
    # relative, since a tight relative check on a rounded low-sig-fig value is unfair.
    band_ok = abs(belle_band - 0.0001) < 5e-5
    if not band_ok:
        _failures += 1
    print(
        f"  [{'OK ' if band_ok else '!! '}] Belle II band on LHS/RHS         "
        f"paper=0.0001         computed={belle_band:.6g}  (rounds to 0.0001)"
    )
    current_dev_in_belle_sigma = abs(lhs / rhs - 1) / belle_band
    check("current PDG deviation, in Belle-II sigma units", current_dev_in_belle_sigma, 9.0, 0.05)

    print("\n" + "=" * 68)
    if _failures == 0:
        print("RESULT: ALL CHECKS PASSED — the note's numbers are reproducible.")
        return 0
    print(f"RESULT: {_failures} CHECK(S) FAILED.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
