"""
Cheap follow-up named in pearl_registry/INDEX.md (temperature-profile row):
does hot_fraction predict WHIM_fraction beyond what mass alone already
explains? No new API calls -- reuses whim_n71_temperature_profile.csv.

IMPORTANT compositional-data caveat, checked and reported explicitly
here (not glossed over): cold_fraction + whim_fraction + hot_fraction =
100% EXACTLY for every cluster, by construction (they are a 3-way split
of the same annulus mass). Since cold_fraction is typically small (a
few percent), whim_fraction ~= 100 - hot_fraction - cold_fraction is
ALMOST a direct arithmetic complement of hot_fraction. A strong raw
negative correlation between hot and WHIM fraction is therefore expected
near-mechanically from the closed-composition constraint itself, NOT
necessarily as new physical evidence -- this must be stated plainly
before interpreting the number as confirming anything.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import csv
import math
import statistics as st
from pathlib import Path

IN_CSV = Path(__file__).parent / "whim_n71_temperature_profile.csv"


def pearson(x: list[float], y: list[float]) -> float:
    n = len(x)
    mx, my = st.mean(x), st.mean(y)
    cov = sum((x[i] - mx) * (y[i] - my) for i in range(n)) / n
    return cov / (st.stdev(x) * st.stdev(y))


def t_p(r: float, n: int) -> tuple[float, str]:
    df = n - 2
    t = r * math.sqrt(df) / math.sqrt(1 - r**2)
    at = abs(t)
    p = "<0.001" if at > 3.46 else "<0.01" if at > 2.65 else "<0.05" if at > 1.99 else "n.s."
    return t, p


def detrend_vs_logmass(y: list[float], log_m: list[float], n: int) -> list[float]:
    mean_lm, mean_y = st.mean(log_m), st.mean(y)
    b = sum((log_m[i] - mean_lm) * (y[i] - mean_y) for i in range(n)) / sum(
        (log_m[i] - mean_lm) ** 2 for i in range(n)
    )
    a = mean_y - b * mean_lm
    return [y[i] - (a + b * log_m[i]) for i in range(n)]


def main() -> None:
    rows = list(csv.DictReader(open(IN_CSV)))
    n = len(rows)
    log_m = [math.log10(float(r["m200_msun"])) for r in rows]
    cold = [float(r["cold_fraction_pct"]) for r in rows]
    whim = [float(r["whim_fraction_pct_recomputed"]) for r in rows]
    hot = [float(r["hot_fraction_pct"]) for r in rows]

    print(f"N = {n}")
    print("\n=== Compositional-constraint sanity check ===")
    sums = [cold[i] + whim[i] + hot[i] for i in range(n)]
    print(f"cold+whim+hot: min={min(sums):.4f} max={max(sums):.4f} (should be ~100 exactly)")
    print(
        f"cold_fraction: mean={st.mean(cold):.2f}%  stdev={st.stdev(cold):.2f}%  (small, as expected)"
    )

    print("\n=== Raw correlation: hot_fraction vs whim_fraction ===")
    r_raw = pearson(hot, whim)
    t_raw, p_raw = t_p(r_raw, n)
    print(f"r(hot, whim) = {r_raw:.4f} (t={t_raw:.2f}, p{p_raw})")
    print(
        "Expected near -1 close to mechanically, since whim ~= 100 - hot - cold and "
        "cold is small -- this raw number is NOT independent physical evidence by itself."
    )

    print("\n=== What the compositional constraint alone would predict ===")
    # If cold were EXACTLY 0 for every cluster, whim = 100 - hot exactly, r = -1.000.
    # The actual r's departure from -1 is entirely attributable to cold_fraction's
    # own (small) variation -- compute that expected floor explicitly.
    implied_whim = [100.0 - hot[i] for i in range(n)]
    r_pure_arithmetic = pearson(hot, implied_whim)
    print(f"r(hot, 100-hot) [pure arithmetic complement, ignoring cold] = {r_pure_arithmetic:.4f}")

    print("\n=== Mass-detrended residual correlation (the actually informative test) ===")
    hot_resid = detrend_vs_logmass(hot, log_m, n)
    whim_resid = detrend_vs_logmass(whim, log_m, n)
    r_resid = pearson(hot_resid, whim_resid)
    t_resid, p_resid = t_p(r_resid, n)
    print(
        f"r(hot_residual, whim_residual | log M200) = {r_resid:.4f} (t={t_resid:.2f}, p{p_resid})"
    )
    print(
        "This still inherits the compositional near-tautology (hot and whim remain "
        "arithmetic near-complements after detrending each separately) -- it is NOT a "
        "clean escape from the closed-composition issue, just the same test with mass "
        "removed from both sides. Interpret alongside the raw number and the pure-"
        "arithmetic floor above, not in isolation."
    )


if __name__ == "__main__":
    main()
