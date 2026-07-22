"""T1b — identify WHO beats Eq.32 in the broadened look-elsewhere spaces.

T1 (scripts/t1_eq32_second_prediction.py) reported that Eq.32,
    (4/3) (m_tau/m_e)^12 = alpha_EM / alpha_G(m_e),
is rank #1 in the baseline space (p,q<=10, n<=24; 83,160 trials) and the
simple-coefficient space (p,q<=4; 14,520) but slips to rank #3 in the broadened
rational space (p,q<=20, n<=30; 420,750) and rank #5 once sqrt(p/q) forms are
added (841,500). T1 never printed the IDENTITY of the 2-4 candidates that beat it.

This script does exactly that and NOTHING else that T1 already covered: for each
broadened space it prints the top-5 candidates by |deviation|, each with its full
identity (coefficient form, mass pair, exponent n, deviation %), so the human can
classify every beating candidate as:
  (i)  Eq.32 ALIAS  — algebraically equivalent / trivial rewrite of Eq.32,
  (ii) EXOTIC near-miss — large p/q or sqrt form no theory motivates (its presence
       shows the broadening mostly adds unmotivated noise; the rank-loss is then a
       MECHANICAL artifact of pool size, not a rival physical relation),
  (iii) GENUINELY DISTINCT SIMPLE relation — small integers + different mass pair
       (the ONLY outcome that would reopen a physics-leaning reading).

Target is fixed at alpha_EM/alpha_G(m_e) (electron reference), identical to T1's
_rank_eq32. We do not recompute T1's ranks; we enumerate the SAME pools and expose
the ordering T1 collapsed into a single rank integer.

Run:  python scripts/t1b_competitor_id.py
Reproducible, prints only. Writes no repo artifacts. NOT_VALIDATION.
"""

from __future__ import annotations

import math

# ── constants (identical to t1_eq32_second_prediction.py) ──
MASSES = {  # MeV, PDG 2024 (facts.json R001 _pdg_correction)
    "e": 0.51099895,
    "mu": 105.6583755,
    "tau": 1776.93,
    "u": 2.16,
    "d": 4.67,
    "s": 93.4,
    "c": 1270.0,
    "b": 4180.0,
    "t": 172570.0,
    "p": 938.27208816,
    "n": 939.56542052,
}
ALPHA_EM = 1.0 / 137.035999084
G_SI = 6.67430e-11
M_E_KG = 9.1093837015e-31
HBAR = 1.054571817e-34
C_SI = 2.99792458e8
ALPHA_G_E = G_SI * M_E_KG**2 / (HBAR * C_SI)
TARGET_E = ALPHA_EM / ALPHA_G_E  # ~4.166e42, electron-reference target


def _coprime_rationals(pmax: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(1, pmax + 1) for q in range(1, pmax + 1) if math.gcd(p, q) == 1]


def _pairs() -> list[tuple[str, str]]:
    names = list(MASSES)
    return [(a, b) for a in names for b in names if MASSES[a] > MASSES[b]]


def _enumerate(coeff_forms, nmax: int):
    """Yield (relerr, coeff_value, coeff_label, hi, lo, n) over the whole pool."""
    log_target = math.log(TARGET_E)
    pairs = _pairs()
    out = []
    for cval, clabel in coeff_forms:
        log_c = math.log(cval)
        for a, b in pairs:
            log_ratio = math.log(MASSES[a]) - math.log(MASSES[b])
            for n in range(1, nmax + 1):
                relerr = abs(math.exp(log_c + n * log_ratio - log_target) - 1.0)
                out.append((relerr, cval, clabel, a, b, n))
    return out


def _is_eq32(cval: float, hi: str, lo: str, n: int) -> bool:
    return abs(cval - 4 / 3) < 1e-9 and hi == "tau" and lo == "e" and n == 12


def _report_space(label: str, coeff_forms, nmax: int, topk: int = 6) -> None:
    pool = _enumerate(coeff_forms, nmax)
    pool.sort(key=lambda r: r[0])
    total = len(pool)
    # locate Eq.32's own rank in this pool (candidates at least as good)
    eq32 = next(r for r in pool if _is_eq32(r[1], r[3], r[4], r[5]))
    eq32_rank = sum(1 for r in pool if r[0] <= eq32[0] + 1e-18)
    print("=" * 78)
    print(f"{label}")
    print(
        f"  total trials = {total:,}   Eq.32 dev = {eq32[0] * 100:.4f}%   Eq.32 rank = #{eq32_rank}"
    )
    print("=" * 78)
    print(f"  {'#':>2} {'coeff':>12} {'pair':>10} {'n':>3} {'value':>13} {'dev %':>9}  note")
    print("  " + "-" * 72)
    for i, (relerr, cval, clabel, hi, lo, n) in enumerate(pool[:topk], 1):
        val = cval * (MASSES[hi] / MASSES[lo]) ** n
        note = "<== Eq.32 itself" if _is_eq32(cval, hi, lo, n) else ""
        print(
            f"  {i:>2} {clabel:>12} {f'{hi}/{lo}':>10} {n:>3} "
            f"{val:>13.4e} {relerr * 100:>8.4f}%  {note}"
        )
    print()


def main() -> None:
    print("T1b — identity of the candidates that beat Eq.32 in broadened spaces")
    print(f"Target (fixed): alpha_EM / alpha_G(m_e) = {TARGET_E:.6e}  [electron reference]\n")

    # (b) broadened rationals: p,q<=20, n<=30  (T1 reported Eq.32 rank #3 here)
    broad = [(p / q, f"{p}/{q}") for p, q in _coprime_rationals(20)]
    _report_space("SPACE B — rationals p,q<=20, n<=30  (T1: rank #3 of 420,750)", broad, 30)

    # (c) broadened + sqrt(p/q) family  (T1 reported Eq.32 rank #5 here)
    sqrt_forms = [(math.sqrt(p / q), f"sqrt({p}/{q})") for p, q in _coprime_rationals(20)]
    _report_space(
        "SPACE C — rationals + sqrt(p/q), p,q<=20, n<=30  (T1: rank #5 of 841,500)",
        broad + sqrt_forms,
        30,
    )


if __name__ == "__main__":
    main()
