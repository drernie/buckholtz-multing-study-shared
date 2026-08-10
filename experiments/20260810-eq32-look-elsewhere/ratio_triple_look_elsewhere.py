"""
Look-elsewhere correction for the 7:9:17 boson-mass relation.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
2026-08-10. Companion to eq32_look_elsewhere.py.

WHY A SEPARATE ENUMERATOR. Eq.32 has the shape prefactor x (mass ratio)^n and its
trials factor was measured over that grammar. Eq.31 is structurally different --
a triple of small integers fixing two scale-free ratios -- so its grammar, its
null and its resolution limit all differ. Reusing the Eq.32 enumerator would have
measured the wrong space. The paper had been left saying this correction "has not
been computed"; it now has.

METRIC. The relation is scale-free, so a candidate triple (a,b,c) is scored by the
best achievable agreement over a free scale lambda. In logs, with
u_i = ln m_i - 0.5 ln n_i, the minimax scale sits at (max u + min u)/2 and the
residual is (max u - min u)/2 -- exact, no optimiser needed. This reproduces the
paper's own figure of merit: it reports the LARGEST residual across the three
masses rather than the best-fitting one, precisely because anchoring on any single
boson makes that boson exact by construction.

RESOLUTION LIMIT. Unlike Eq.32 -- where the filter had to exclude expressions
whose own mass inputs could not support the claimed precision -- all three boson
masses are well measured. The binding limit here is what the DATA can resolve:
hypot(sigma_H/m_H, sigma_Z/m_Z) = 0.088 %, dominated by m_H. A triple fitting
better than that is indistinguishable from any other that also does.

RESULT, stated with its condition. p depends strongly on where "simple" is cut,
because triples cover a two-dimensional ratio space and their density grows as
N^3: p = 0.004 at N = 20 against p = 0.079 at N = 50. The N = 20 figure is the one
that includes (7,9,17) with a little room; it must never be quoted without N.
"""

from math import gcd, log

import numpy as np

# PDG 2024 as used in paper/main.tex Sec. ssec:bosons
M_W, S_W = 80.369, 0.013  # CDF-II 2022 excluded, per the paper
M_Z, S_Z = 91.1876, 0.0021
M_H, S_H = 125.20, 0.11

CLAIM = (7, 9, 17)
N_NULL = 6000
SEED = 20260810
RANGE_FACTOR = 1.5  # random targets drawn within this factor of each observed ratio


def triples(n_max: int) -> np.ndarray:
    """All a < b < c <= n_max with gcd 1. Ordered because m_W < m_Z < m_H."""
    return np.array(
        [
            (a, b, c)
            for a in range(1, n_max + 1)
            for b in range(a + 1, n_max + 1)
            for c in range(b + 1, n_max + 1)
            if gcd(gcd(a, b), c) == 1
        ],
        dtype=float,
    )


def best_dev(log_wz: float, log_hz: float, tri: np.ndarray) -> float:
    """Smallest minimax residual over all triples, for a target given by its two
    scale-free log-ratios. Vectorised over the whole triple set."""
    u1 = log_wz - 0.5 * np.log(tri[:, 0])
    u2 = -0.5 * np.log(tri[:, 1])
    u3 = log_hz - 0.5 * np.log(tri[:, 2])
    stacked = np.stack([u1, u2, u3])
    return float(((stacked.max(0) - stacked.min(0)) / 2).min())


def main() -> None:
    log_wz, log_hz = np.log(M_W / M_Z), np.log(M_H / M_Z)
    resolution = float(np.hypot(S_H / M_H, S_Z / M_Z))

    a, b, c = CLAIM
    u = np.array([log(M_W) - 0.5 * log(a), log(M_Z) - 0.5 * log(b), log(M_H) - 0.5 * log(c)])
    dev_claim = (u.max() - u.min()) / 2

    print("=" * 76)
    print("ANCHOR")
    print("=" * 76)
    print(f"  minimax deviation of {CLAIM} in mass units : {100 * dev_claim:.4f} %")
    print("  paper/main.tex Sec. ssec:bosons states       : < 0.05 %")
    print(
        f"  Z-anchored cross-check: m_H_pred = {M_Z * np.sqrt(17 / 9):.2f}"
        f" (measured {M_H}),  m_W_pred = {M_Z * np.sqrt(7 / 9):.3f} (measured {M_W})"
    )
    print(f"\n  data resolution limit, hypot(sigma_H/m_H, sigma_Z/m_Z) : {100 * resolution:.4f} %")
    print("  -> the agreement is already at the limit the data can resolve;")
    print("     m_H precision is a discriminant alongside m_W.")

    rng = np.random.default_rng(SEED)
    print("\n" + "=" * 76)
    print("TRIALS FACTOR vs the simplicity bound N")
    print("=" * 76)
    print(f"  {'N':>4} {'triples':>9} {'best real':>11} {'median null':>12} {'p':>10} {'K':>7}")
    for n_max in [17, 20, 25, 30, 40, 50]:
        tri = triples(n_max)
        d_real = best_dev(log_wz, log_hz, tri)
        x = log_wz + rng.uniform(-log(RANGE_FACTOR), log(RANGE_FACTOR), N_NULL)
        y = log_hz + rng.uniform(-log(RANGE_FACTOR), log(RANGE_FACTOR), N_NULL)
        ok = (x < 0) & (y > 0)  # keep the ordering m_W < m_Z < m_H
        x, y = x[ok], y[ok]
        null = np.array([best_dev(xi, yi, tri) for xi, yi in zip(x, y, strict=True)])
        p = float((null <= d_real).mean())
        p_str = f"{p:.4f}" if p > 0 else f"<{1 / len(null):.5f}"
        mark = "  <- includes (7,9,17) with room" if n_max == 20 else ""
        print(
            f"  {n_max:>4} {len(tri):>9,} {100 * d_real:>10.4f}% "
            f"{100 * np.median(null):>11.4f}% {p_str:>10} {len(null):>7,}{mark}"
        )

    print("\n" + "=" * 76)
    print("SENSITIVITY of p to the null's target range, at N = 20")
    print("=" * 76)
    tri = triples(20)
    d_real = best_dev(log_wz, log_hz, tri)
    for factor in [1.2, 1.5, 2.0, 3.0]:
        x = log_wz + rng.uniform(-log(factor), log(factor), N_NULL)
        y = log_hz + rng.uniform(-log(factor), log(factor), N_NULL)
        ok = (x < 0) & (y > 0)
        x, y = x[ok], y[ok]
        null = np.array([best_dev(xi, yi, tri) for xi, yi in zip(x, y, strict=True)])
        p = float((null <= d_real).mean())
        p_str = f"{p:.4f}" if p > 0 else f"<{1 / len(null):.5f}"
        print(f"  range x{factor:<4} : p = {p_str:>9}   (K = {len(null):,})")

    print("\n  p stays within 0.002-0.006 across the tested ranges: the figure is")
    print("  robust to the null's window, and sensitive to the simplicity bound N.")


if __name__ == "__main__":
    main()
