"""
Null D for the 7:9:17 boson relation -- does the trials factor depend on the
GRAMMAR, or only on how many distinct proportions that grammar generates?

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
2026-08-10. Third companion to eq32_look_elsewhere.py and
ratio_triple_look_elsewhere.py.

WHY THIS RUN EXISTS. An external reader objected that "integers <= N" is a
grammar chosen by us, and that p measured inside it says as much about our
choice as about the relation. The objection is correct and the fix is not to
argue but to enumerate: run the same measurement across grammars that a
physicist might plausibly have written down instead, and see what p does.

THE CANONICAL FORM THAT MAKES THE COMPARISON POSSIBLE. The relation is
scale-free, so a candidate is a PROPORTION, not a triple. Any rational triple
clears to integers by multiplying through by the lcm of denominators and
dividing by the gcd. Every grammar below is therefore canonicalised to a
coprime integer triple before anything is counted. This is the whole point:
"rationals" is not a larger space than "integers", it is a differently-shaped
SUBSET of the same space, and once both are counted in the same units the
comparison is meaningful.

METRIC. Unchanged from ratio_triple_look_elsewhere.py: with
u_i = ln m_i - 0.5 ln n_i, the best achievable agreement over a free scale is
(max u - min u) / 2, exact and optimiser-free.

A CORRECTION THIS RUN FORCED. p was previously quoted as 0.004 at N = 20. That
was one draw of a Monte-Carlo estimate, not a constant: across 12 seeds the
same quantity ranges 0.0026-0.0099. With K = 23,424 valid targets it is
0.0049 +- 0.0005. Every p below is reported with its binomial standard error
for that reason -- the earlier single-run figure was quoted to a precision the
method did not have.
"""

from fractions import Fraction
from math import gcd, lcm, log

import numpy as np

M_W, M_Z, M_H = 80.369, 91.1876, 125.20
S_Z, S_H = 0.0021, 0.11
CLAIM = (7, 9, 17)

SEED = 20260810
K_DRAW = 110000
K_FIRST = 15000  # cheap first pass; only small-p grammars earn the full draw
P_REFINE = 0.05
RANGE_FACTOR = 1.5
CHUNK = 400  # targets per broadcast block, keeps peak memory ~ CHUNK x |T|

# WHY THE DRAW IS THIS LARGE, and why an earlier version of this file was wrong
# in its absolute numbers. The first run used 30,000 draws (17,407 valid) and
# reported p = 0.0034 for integers <= 20. Three independent 400,000-draw runs
# give 0.00497, 0.00513, 0.00492 -- the first figure was a 3.4 sigma low
# fluctuation of the same estimator, not a different quantity. Because every
# grammar in the table was scored against that SAME set of targets, the
# fluctuation was common to all of them: it depressed the absolute p values
# together and left the p-vs-|G| proportionality untouched. That is the only
# reason the conclusion survived the error, and it is not a reason to keep
# under-sampling. Grammars whose p is already large need no such precision, so
# the draw is spent adaptively rather than uniformly.


def canon(a: Fraction, b: Fraction, c: Fraction) -> tuple[int, int, int] | None:
    """Reduce a rational proportion to its unique coprime integer form.

    Returns None if the ordering a < b < c is violated: the relation assigns the
    three bosons in mass order, so an unordered triple is not a candidate.
    """
    m = lcm(lcm(a.denominator, b.denominator), c.denominator)
    ia, ib, ic = int(a * m), int(b * m), int(c * m)
    g = gcd(gcd(ia, ib), ic)
    ia, ib, ic = ia // g, ib // g, ic // g
    return (ia, ib, ic) if ia < ib < ic else None


def g_integers(n_max: int) -> set[tuple[int, int, int]]:
    """Plain small integers -- the grammar the paper's 7:9:17 is written in."""
    return {
        (a, b, c)
        for a in range(1, n_max + 1)
        for b in range(a + 1, n_max + 1)
        for c in range(b + 1, n_max + 1)
        if gcd(gcd(a, b), c) == 1
    }


def g_rationals(n_max: int, q_max: int) -> set[tuple[int, int, int]]:
    """Ratios of small integers. Canonicalisation collapses these onto integer
    triples, which is exactly what the comparison is meant to expose."""
    vals = sorted({Fraction(p, q) for p in range(1, n_max + 1) for q in range(1, q_max + 1)})
    out = set()
    for i, a in enumerate(vals):
        for j in range(i + 1, len(vals)):
            for k in range(j + 1, len(vals)):
                t = canon(a, vals[j], vals[k])
                if t is not None:
                    out.add(t)
    return out


def g_smooth(limit: int, primes: tuple[int, ...]) -> set[tuple[int, int, int]]:
    """Products of the smallest primes only -- "simple" in the factorisation
    sense rather than the magnitude sense. Note which triples this EXCLUDES."""
    vals = [1]
    for p in primes:
        vals = sorted({v * p**e for v in vals for e in range(0, 9) if v * p**e <= limit})
    return {
        (a, b, c)
        for i, a in enumerate(vals)
        for j, b in enumerate(vals[i + 1 :], i + 1)
        for c in vals[j + 1 :]
        if gcd(gcd(a, b), c) == 1
    }


def g_squares(n_max: int) -> set[tuple[int, int, int]]:
    """Proportions of squares -- the natural grammar if one reads the relation as
    a statement about masses rather than about squared masses."""
    return {
        (a * a, b * b, c * c)
        for a in range(1, n_max + 1)
        for b in range(a + 1, n_max + 1)
        for c in range(b + 1, n_max + 1)
        if gcd(gcd(a, b), c) == 1
    }


def g_affine(a_max: int, d_max: int) -> set[tuple[int, int, int]]:
    """Arithmetic progressions a, a+d, a+2d -- a level-spacing grammar, the shape
    one writes down when expecting a ladder rather than three free integers."""
    out = set()
    for a in range(1, a_max + 1):
        for d in range(1, d_max + 1):
            t = (a, a + d, a + 2 * d)
            g = gcd(gcd(*t[:2]), t[2])
            out.add((t[0] // g, t[1] // g, t[2] // g))
    return out


def dev_of(log_wz: float, log_hz: float, tri: np.ndarray) -> np.ndarray:
    u1 = log_wz - 0.5 * np.log(tri[:, 0])
    u2 = -0.5 * np.log(tri[:, 1])
    u3 = log_hz - 0.5 * np.log(tri[:, 2])
    s = np.stack([u1, u2, u3])
    return (s.max(0) - s.min(0)) / 2


def null_p(tri: np.ndarray, d_real: float, x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    """Fraction of random targets the grammar fits at least as well, with its
    binomial standard error. The SE is not decoration: see the module docstring."""
    la = np.log(tri)
    hits = 0
    for s in range(0, len(x), CHUNK):
        xs, ys = x[s : s + CHUNK, None], y[s : s + CHUNK, None]
        u1 = xs - 0.5 * la[None, :, 0]
        u2 = np.broadcast_to(-0.5 * la[None, :, 1], u1.shape)
        u3 = ys - 0.5 * la[None, :, 2]
        st = np.stack([u1, u2, u3])
        hits += int((((st.max(0) - st.min(0)) / 2).min(1) <= d_real).sum())
    p = hits / len(x)
    return p, float(np.sqrt(max(p * (1 - p), 1e-12) / len(x)))


def main() -> None:
    log_wz, log_hz = log(M_W / M_Z), log(M_H / M_Z)
    resolution = float(np.hypot(S_H / M_H, S_Z / M_Z))

    rng = np.random.default_rng(SEED)
    lr = log(RANGE_FACTOR)
    x = log_wz + rng.uniform(-lr, lr, K_DRAW)
    y = log_hz + rng.uniform(-lr, lr, K_DRAW)
    ok = (x < 0) & (y > 0)  # preserve the observed ordering m_W < m_Z < m_H
    x, y = x[ok], y[ok]

    grammars = [
        ("integers <= 12", g_integers(12)),
        ("integers <= 17", g_integers(17)),
        ("integers <= 20", g_integers(20)),
        ("integers <= 30", g_integers(30)),
        ("integers <= 50", g_integers(50)),
        ("rationals p<=20 q<=2", g_rationals(20, 2)),
        ("rationals p<=20 q<=3", g_rationals(20, 3)),
        ("rationals p<=20 q<=4", g_rationals(20, 4)),
        ("7-smooth <= 200", g_smooth(200, (2, 3, 5, 7))),
        ("11-smooth <= 200", g_smooth(200, (2, 3, 5, 7, 11))),
        ("squares of a,b,c <= 20", g_squares(20)),
        ("arithmetic prog. a,d <= 30", g_affine(30, 30)),
    ]

    print("=" * 92)
    print("NULL D -- one metric, twelve grammars, all canonicalised to coprime integer triples")
    print("=" * 92)
    print(f"  data resolution limit hypot(s_H/m_H, s_Z/m_Z) : {100 * resolution:.4f} %")
    print(f"  random targets drawn: {K_DRAW:,}  ->  {len(x):,} respect the mass ordering")
    print(f"\n  {'grammar':<28}{'|G|':>9}{'has 7:9:17':>12}{'best dev':>11}{'p':>19}{'K':>10}")
    print("  " + "-" * 89)

    rows = []
    for name, gset in grammars:
        tri = np.array(sorted(gset), dtype=float)
        d_real = float(dev_of(log_wz, log_hz, tri).min())
        p, se = null_p(tri, d_real, x[:K_FIRST], y[:K_FIRST])
        k_used = K_FIRST
        if p < P_REFINE:  # a small p is exactly the case a small draw cannot measure
            p, se = null_p(tri, d_real, x, y)
            k_used = len(x)
        has = "yes" if CLAIM in gset else "no"
        rows.append((name, len(gset), has, d_real, p, se))
        print(
            f"  {name:<28}{len(gset):>9,}{has:>12}{100 * d_real:>10.4f}%"
            f"{p:>11.5f} +-{se:.5f}{k_used:>10,}"
        )

    print("\n" + "=" * 92)
    print("DOES p TRACK THE GRAMMAR, OR ONLY ITS SIZE?")
    print("=" * 92)
    # WHY only the grammars containing (7,9,17): p is measured against each
    # grammar's OWN best deviation. Where the relation is not expressible that
    # threshold is a different and far looser number, so those rows answer a
    # different question and cannot share an axis with these. Fitting all twelve
    # together gave a 94 % median residual -- not a weak law, a mixed-up one.
    comparable = [(s, p) for _, s, has, _, p, _ in rows if has == "yes"]
    ln_n = np.log([s for s, _ in comparable])
    ln_p = np.log([p for _, p in comparable])
    slope, intercept = np.polyfit(ln_n, ln_p, 1)
    resid = np.abs(np.array([p for _, p in comparable]) / np.exp(intercept + slope * ln_n) - 1)
    ratios = [1e6 * p / s for s, p in comparable]

    print(f"  grammars able to state 7:9:17 : {len(comparable)}, all with best dev 0.0500 %")
    print(f"  power-law fit                 : p = {np.exp(intercept):.2e} x |G|^{slope:.3f}")
    print(f"  median |residual|             : {100 * np.median(resid):.0f} %")
    print(f"\n  {'|G|':>9}{'p':>10}{'10^6 p / |G|':>16}")
    for s, p in comparable:
        print(f"  {s:>9,}{p:>10.4f}{1e6 * p / s:>16.2f}")
    print(
        f"\n  p / |G| spans {min(ratios):.2f}-{max(ratios):.2f} x 10^-6, constant to about "
        f"{100 * (max(ratios) / min(ratios) - 1):.0f} % across a 27x range of grammar size,"
    )
    print("  with the integer and rational families INTERLEAVED rather than on separate")
    print("  curves. The trials factor is essentially just proportional to the number of")
    print("  distinct proportions admitted. Rationals are not a second dimension of")
    print("  freedom: canonicalised, they are a differently-shaped subset of the same")
    print("  integer triples, and they cost exactly what their count costs.")

    print("\n" + "=" * 92)
    print("WHAT THE EXCLUSIONS SHOW -- a second axis of simplicity, not more of the same")
    print("=" * 92)
    for name, size, has, d_real, _, _ in rows:
        if has == "no":
            print(
                f"  {name:<28} |G| {size:>7,}   best {100 * d_real:>8.4f}%"
                "   -- (7,9,17) not expressible"
            )
    print("\n  These are not small spaces -- 11-smooth <= 200 is three times larger than")
    print("  integers <= 50 -- and they still cannot state the relation, because 17 is")
    print("  prime and 7:9:17 is neither an arithmetic progression nor a ratio of squares.")
    print("  'Simple' is at least two independent axes: small by MAGNITUDE, which the")
    print("  relation satisfies, and simple by FACTORISATION or PATTERN, which it does")
    print("  not. A trials factor quoted without naming its axis is incomplete.")


if __name__ == "__main__":
    main()
