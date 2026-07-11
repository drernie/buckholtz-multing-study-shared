"""Reference-mass robustness (no-collapse convention-flip) test for Eq.32.

Eq.32 conventionally fixes m_e as the reference mass inside alpha_G
(alpha_G = G m_ref^2 / hbar c, Dirac 1937 convention). This script asks the
no-collapse question: if the reference mass itself is allowed to vary over
all eleven candidate masses, does m_e remain the uniquely precise choice, or
does the apparent precision of Eq.32 partly reflect the size of the search
space rather than something special about the electron?

For each of the 11 reference-mass choices, this scans the SAME family used in
scan_mass_ratio_formulas.py, (p/q)(m_i/m_ref)^n with coprime p,q<=10, n<=24,
over all other masses m_i (only pairs with m_i > m_ref are scanned, so the
per-reference trial count is NOT uniform: 24,000 for m_e down to 0 for m_t,
since a mass can only serve as reference when at least one candidate mass
exceeds it). All reference pools are combined into one ranked list of
132,000 candidates (55 unordered mass pairs x 2400 coprime-prefactor/exponent
combinations) to give a properly pooled (not per-reference-best) significance
estimate for Eq.32.

Run:  python scripts/scan_reference_mass_robustness.py
Output: experiments/20260627-f4-eq32-synthesis/reference_mass_scan_result.json
"""

from __future__ import annotations

import json
import math
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "experiments" / "20260627-f4-eq32-synthesis" / "reference_mass_scan_result.json"

MASSES = {
    "e": 0.51099895,
    "mu": 105.6583755,
    "tau": 1776.93,  # PDG 2024 (supersedes 2022's 1776.86)
    "u": 2.16,
    "d": 4.67,
    "s": 93.4,
    "c": 1270.0,
    "b": 4180.0,
    "t": 172570.0,  # PDG 2024 direct measurement (supersedes 172760.0)
    "p": 938.27208816,
    "n": 939.56542052,
}
ALPHA_EM = 1 / 137.035999084
ALPHA_G_E = 1.751809e-45  # alpha_G(m_e) = G m_e^2 / (hbar c)
TARGET_E = ALPHA_EM / ALPHA_G_E

P_MAX, Q_MAX, N_MAX = 10, 10, 24


def main() -> None:
    results: list[tuple[float, str, str]] = []  # (rel_err, ref, formula)

    for ref, m_ref in MASSES.items():
        target = TARGET_E * (MASSES["e"] / m_ref) ** 2
        for i, m_i in MASSES.items():
            if i == ref:
                continue
            r = m_i / m_ref
            if r <= 1:
                continue
            for n in range(1, N_MAX + 1):
                base = r**n
                for p in range(1, P_MAX + 1):
                    for q in range(1, Q_MAX + 1):
                        if math.gcd(p, q) != 1:
                            continue  # skip non-reduced duplicates (8/6 == 4/3, etc.)
                        val = (p / q) * base
                        err = abs(val / target - 1)
                        results.append((err, ref, f"({p}/{q})(m_{i}/m_{ref})^{n}"))

    results.sort(key=lambda x: x[0])
    total = len(results)

    eq32_rank = next(
        k for k, (_, ref, f) in enumerate(results, 1) if ref == "e" and f == "(4/3)(m_tau/m_e)^12"
    )
    eq32_err = next(err for err, ref, f in results if ref == "e" and f == "(4/3)(m_tau/m_e)^12")

    n_at_least_as_good = sum(1 for err, _, _ in results if err <= eq32_err)
    p_combined = n_at_least_as_good / total

    top10 = [
        {"rank": k, "rel_err": err, "reference": ref, "formula": f}
        for k, (err, ref, f) in enumerate(results[:10], 1)
    ]

    # Next-best distinct (non-Eq.32, non-duplicate-of-Eq.32) candidate, determined
    # dynamically from the actual ranked pool rather than assumed in advance.
    next_best = next(
        (err, ref, f)
        for err, ref, f in results
        if not (ref == "e" and f in ("(4/3)(m_tau/m_e)^12", "(8/6)(m_tau/m_e)^12"))
    )

    out = {
        "total_trials_combined": total,
        "n_references_tested": len(MASSES),
        "eq32_rank_combined": eq32_rank,
        "eq32_rel_err": eq32_err,
        "n_candidates_at_least_as_good": n_at_least_as_good,
        "p_empirical_combined": p_combined,
        "next_best_distinct_candidate": {
            "formula": next_best[2],
            "reference_mass": next_best[1],
            "rel_err": next_best[0],
            "note": "distinct mass pair and coefficient from Eq.32; recorded as an independent curiosity, not evidence against Eq.32",
        },
        "top10": top10,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print(f"Total combined trials (11 references): {total:,}")
    print(f"Eq.32 rank (combined pool): #{eq32_rank}")
    print(f"Eq.32 rel_err: {eq32_err * 100:.4f}%")
    print(f"Candidates at least as good: {n_at_least_as_good}")
    print(f"Empirical p (combined): {p_combined:.2e}")
    print(f"Saved: {OUT}")


if __name__ == "__main__":
    main()
