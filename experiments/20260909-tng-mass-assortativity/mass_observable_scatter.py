"""
Direct empirical measurement of cluster mass-observable scatter (sigma_lnM),
the OTHER open unknown named in FINDING_P158_jensen_mass_averaging_v82_
force_terms.md ("the real cluster mass-observable scatter at v82's target
mass/redshift range... NOT checked by that file").

Reuses the already-fetched N=71 WHIM-pilot sample (no new API calls) --
its mass range (1.28e14-7.34e14 Msun) happens to sit close to v82's own
targeted range (per this project's planning material, ~5-6e14 Msun).

Observable proxy: richness (GroupNsubs), a real observable astronomers
use for cluster mass estimation (e.g. redMaPPer-style richness-mass
relations). Convention matches the literature: fit
    log(M_true) = a + b * log(N_richness) + scatter
and report sigma_lnM|richness (scatter of TRUE mass at fixed observable),
not the inverse direction.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import csv
import math
import statistics as st
from pathlib import Path

IN_CSV = Path(__file__).parent.parent / "20260909-tng-whim-pilot" / "whim_n71_results.csv"


def main() -> None:
    rows = list(csv.DictReader(open(IN_CSV)))
    n = len(rows)
    log_m = [math.log10(float(r["m200_msun"])) for r in rows]
    log_n = [math.log10(int(r["group_nsubs"])) for r in rows]

    mean_ln, mean_lm = st.mean(log_n), st.mean(log_m)
    b = sum((log_n[i] - mean_ln) * (log_m[i] - mean_lm) for i in range(n)) / sum(
        (log_n[i] - mean_ln) ** 2 for i in range(n)
    )
    a = mean_lm - b * mean_ln
    resid = [log_m[i] - (a + b * log_n[i]) for i in range(n)]
    sigma_logM_dex = st.stdev(resid)
    sigma_lnM = sigma_logM_dex * math.log(10)

    r = sum((log_n[i] - mean_ln) * (log_m[i] - mean_lm) for i in range(n)) / (
        n * st.stdev(log_n) * st.stdev(log_m)
    )

    masses = [float(r["m200_msun"]) for r in rows]
    print(f"N = {n}")
    print(f"Mass range: {min(masses):.3e} - {max(masses):.3e} Msun (mean {st.mean(masses):.3e})")
    print(f"\nFit: log10(M_true) = {a:.3f} + {b:.3f} * log10(N_richness)")
    print(f"r(log N_richness, log M_true) = {r:.4f}")
    print("\n=== Headline: mass-observable scatter (richness proxy) ===")
    print(f"sigma_logM|richness = {sigma_logM_dex:.4f} dex")
    print(
        f"sigma_lnM|richness  = {sigma_lnM:.4f}  (natural-log units, matches P158's own sigma_lnm notation)"
    )
    print(
        "\nCaveat: richness (subhalo count) is one specific observable proxy, not a "
        "weak-lensing or X-ray mass proxy -- real published sigma_lnM values differ by "
        "proxy type. This is this project's own direct measurement for THIS proxy, on "
        "TNG300-1's own N=71 sample, not a claim about which proxy TJB's model implies."
    )


if __name__ == "__main__":
    main()
