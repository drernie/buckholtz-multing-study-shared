"""
Second application of the look-elsewhere checklist -- not a re-run of the
p ~ |G|^0.95 "law" (FINDING_null_d_grammar.md explicitly forbids comparing p
across grammars of different dimensionality with unharmonised nulls), but the
two parts of that checklist which ARE domain-independent and do not require
any cross-comparison: (1) does Eq.32's own look-elsewhere p track the SIZE of
its OWN declared grammar, the way 7:9:17's did within its own family; and
(2) is Eq.32 ISOLATED from its nearest statable competitor, the way Result 3
tested for 7:9:17 -- or is it sitting in a dense cluster?

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
2026-09-08. Extends eq32_look_elsewhere.py (2026-08-10) -- same anchor, same
MASSES table, same statability filter and threshold. Does NOT reopen the
Eq.32 mechanism-hunt (NR-019/NR-024, exhausted, closed) -- this asks about
the STATISTICAL SIGNIFICANCE of the numerical match, not its cause.

WHY THIS EXISTS. pearl_registry/INDEX.md (2026-08-10 row) framed
p ~ |G|^0.95 as a portable "law" and proposed testing it on a second relation
(explicitly naming Eq.32). FINDING_null_d_grammar.md, the SAME experiment,
SAME day, already disclaims exactly that framing: the exponent is not a
discovered law (it is the expected nearest-neighbour density scaling), and
comparing p across relations of different grammar dimensionality is invalid.
This script applies the checklist's two genuinely portable, non-forbidden
parts to Eq.32's OWN grammar family only -- never comparing its p or its
|G| to 7:9:17's.
"""

from fractions import Fraction

import numpy as np

# --- Same anchor as eq32_look_elsewhere.py, not re-derived -------------------
MASSES = {
    "e": (0.51100e-3, 3e-7),
    "mu": (105.6583755e-3, 2e-8),
    "tau": (1776.93e-3, 0.09 / 1776.93),
    "u": (2.16e-3, 0.38 / 2.16),
    "d": (4.67e-3, 0.33 / 4.67),
    "s": (93.4e-3, 6.0 / 93.4),
    "c": (1.27, 0.02 / 1.27),
    "b": (4.18, 0.03 / 4.18),
    "t": (172.69, 0.30 / 172.69),
    "W": (80.377, 0.012 / 80.377),
    "Z": (91.1876, 0.0021 / 91.1876),
    "H": (125.25, 0.17 / 125.25),
    "p": (0.93827, 1e-8),
}
ALPHA_EM = 1 / 137.036
M_PLANCK = 1.220890e19
TARGET = ALPHA_EM / ((MASSES["e"][0] / M_PLANCK) ** 2)
SIGMA_MAX = 0.005
N_NULL = 4000
SEED = 20260810

RATIOS = [
    (f"{a}/{b}", MASSES[a][0] / MASSES[b][0], float(np.hypot(MASSES[a][1], MASSES[b][1])))
    for a in MASSES
    for b in MASSES
    if a != b and MASSES[a][0] > MASSES[b][0]
]
EQ32_DEV = abs((4 / 3) * (MASSES["tau"][0] / MASSES["e"][0]) ** 12 / TARGET - 1)


def statable_items(pq_max: int, n_max: int) -> list[tuple[str, str, int, float, float]]:
    """One declared grammar: prefactors p/q with p,q<=pq_max, integer exponents
    1..n_max, any mass ratio. Same statability filter as eq32_look_elsewhere.py
    (fixed 0.5% threshold, independent of where an expression lands -- see that
    file's error #3 for why a deviation-linked threshold would be circular)."""
    prefactors = sorted(
        {Fraction(a, b) for a in range(1, pq_max + 1) for b in range(1, pq_max + 1)}
    )
    out = []
    for p in prefactors:
        for rn, r, su in RATIOS:
            for n in range(1, n_max + 1):
                su_n = n * su
                if su_n > SIGMA_MAX:
                    continue
                val = float(p) * r**n
                if 0 < val < 1e300:
                    out.append((str(p), rn, n, val, su_n))
    return out


def null_p_and_isolation(
    items: list[tuple[str, str, int, float, float]], rng: np.random.Generator
) -> tuple[float, float, float, float]:
    """Returns (p_value, real_dev, d2_over_d1_real, d2_over_d1_null_median).

    p_value: same construction as eq32_look_elsewhere.py -- fraction of random
    log-uniform targets (within +/-1 decade of TARGET) matched at least as
    well by the BEST statable expression in this grammar.

    Isolation: for the REAL target, take the two closest statable expressions
    by |dev|; d2/d1 = second-closest / closest. Repeat for each null target
    and report the median -- mirrors Result 3 of FINDING_null_d_grammar.md
    (D2/D1 gap test), applied here to Eq.32's own grammar for the first time.
    """
    if not items:
        return float("nan"), float("nan"), float("nan"), float("nan")
    logv = np.array([np.log(x[3]) for x in items])
    lt = np.log(TARGET)

    devs_real = np.sort(np.abs(np.expm1(logv - lt)))
    d1_real = float(devs_real[0])
    d2_real = float(devs_real[1]) if len(devs_real) > 1 else float("nan")
    ratio_real = d2_real / d1_real if d1_real > 0 else float("nan")

    lts = lt + rng.uniform(-np.log(10), np.log(10), N_NULL)
    best = np.empty(N_NULL)
    ratios_null = np.empty(N_NULL)
    for i, x in enumerate(lts):
        devs = np.sort(np.abs(np.expm1(logv - x)))
        best[i] = devs[0]
        ratios_null[i] = devs[1] / devs[0] if len(devs) > 1 and devs[0] > 0 else np.nan

    p_value = float((best <= d1_real).mean())
    ratio_null_median = float(np.nanmedian(ratios_null))
    return p_value, d1_real, ratio_real, ratio_null_median


def main() -> None:
    print("=" * 88)
    print("PART 1 -- does Eq.32's own look-elsewhere p track the SIZE of its own")
    print("          declared grammar? (own harmonised null each time -- never")
    print("          compared to 7:9:17's p or |G|)")
    print("=" * 88)

    grammars = [
        ("pq<=6,  n<=12", 6, 12),
        ("pq<=12, n<=12", 12, 12),
        ("pq<=12, n<=24", 12, 24),
        ("pq<=20, n<=24", 20, 24),
        ("pq<=20, n<=36", 20, 36),
    ]

    rows = []
    print(
        f"\n  {'grammar':<16}{'|statable|':>12}{'p':>10}{'d1 (%)':>10}{'d2/d1 real':>13}{'d2/d1 null':>13}"
    )
    print("  " + "-" * 86)
    for name, pq_max, n_max in grammars:
        items = statable_items(pq_max, n_max)
        rng = np.random.default_rng(SEED)  # same seed each grammar -- shared-draw design,
        # per FINDING_null_d_grammar.md's own lesson: robust in ratios, so comparing
        # p ACROSS these rows is meaningful even though absolute levels may share a
        # fluctuation; each row's own d2/d1 comparison (real vs null) does not depend
        # on the seed being fresh, only on real and null being drawn identically.
        p, d1, ratio_real, ratio_null = null_p_and_isolation(items, rng)
        rows.append((name, len(items), p, d1, ratio_real, ratio_null))
        print(
            f"  {name:<16}{len(items):>12,}{p:>10.4f}{100 * d1:>10.4f}"
            f"{ratio_real:>13.2f}{ratio_null:>13.2f}"
        )

    print("\n  Does p track |statable grammar|, the way it did for 7:9:17?")
    sizes = np.array([r[1] for r in rows], dtype=float)
    ps = np.array([r[2] for r in rows], dtype=float)
    if np.all(ps > 0) and len(set(sizes)) > 1:
        slope, intercept = np.polyfit(np.log(sizes), np.log(ps), 1)
        pred = np.exp(intercept + slope * np.log(sizes))
        resid = np.abs(ps / pred - 1)
        print(f"  power-law fit: p = {np.exp(intercept):.3e} x |statable|^{slope:.3f}")
        print(f"  median |residual|: {100 * np.median(resid):.0f}%")
    else:
        print("  fit skipped -- a p_value was exactly zero or all grammar sizes equal.")

    print("\n" + "=" * 88)
    print("PART 2 -- isolation test (Result 3's D2/D1 gap, applied to Eq.32's own")
    print("          grammar for the first time). H1: Eq.32 sits apart from its")
    print("          nearest statable competitor. H0: it is a typical nearest")
    print("          neighbour among equally-close random targets.")
    print("=" * 88)
    best_row = max(rows, key=lambda r: r[1])  # largest grammar = most power to detect isolation
    name, n_items, p, d1, ratio_real, ratio_null = best_row
    print(f"\n  using largest grammar ({name}, |statable|={n_items:,}):")
    print(f"  observed d2/d1 (real target)      : {ratio_real:.2f}")
    print(f"  median d2/d1 (random null targets): {ratio_null:.2f}")
    if ratio_real > ratio_null:
        print("  -> Eq.32's nearest competitor is FARTHER (relatively) than typical:")
        print("     some support for isolation, not just closeness.")
    else:
        print("  -> Eq.32's nearest competitor is NO FARTHER (or closer) than typical")
        print("     random targets get: no isolation evidence beyond raw closeness --")
        print("     the same qualitative outcome Result 3 found for 7:9:17.")


if __name__ == "__main__":
    main()
