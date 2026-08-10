"""
Look-elsewhere correction for Eq.32, using this project's own NR-009 enumeration.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
2026-08-10.

WHY. NR-009 killed the S3-geometry explanation of Eq.32's (4/3) prefactor by
enumerating ~456 equally-simple (prefactor, exponent) families coinciding at n=3.
That enumeration was never turned on the claim it was defending. This does that.

The distinction being measured. "Eq.32 holds at 1.0 sigma" is a statement about
the PDG uncertainty on m_tau GIVEN the formula. It is not the probability of
finding such a formula somewhere in an admissible expression space. Only the first
had ever been computed.

THREE ERRORS FOUND WHILE WRITING THIS, all caught by controls rather than reading.
They are recorded because each is a reusable trap.

  1. r**n computed as exp(n*log(r)). Rounding pushed the anchor outside its own
     tolerance and the scan returned zero hits, including the expression it was
     seeded with. Powers are taken directly below.

  2. m_tau = 1776.86 MeV was used -- the PDG-2022-era value that paper/main.tex
     itself flags as corrected on 2026-07-11. The real deviation is ~4x larger
     than the one that gave. The anchor check did not catch it because it compared
     against a remembered figure rather than the current artifact: both sides of
     the comparison came from the same stale source. The anchor below is taken
     from paper/main.tex's own stated LHS/RHS = 1.000608.

  3. A first "statability" filter required an expression's own uncertainty to be
     smaller than its deviation. That is circular, and it excluded Eq.32 itself --
     whose uncertainty (0.061 %) exceeds its deviation (0.059 %), which is exactly
     what a 1.0 sigma agreement means. The filter below uses a fixed threshold
     independent of how close the expression lands.

WHY THE FILTER MATTERS, concretely. Unfiltered, the closest competitor to Eq.32 is
12 x (m_c/m_u)^15 at 0.057 %. It is not a competitor: m_u carries ~17 % uncertainty
and the exponent 15 multiplies it, so that expression's own uncertainty is ~265 %.
It cannot be stated to 0.06 % at all. Counting it would inflate the trials factor
with expressions that could never be claimed as precision relations.
"""

from fractions import Fraction

import numpy as np

# --- PDG 2024: (value in GeV, relative uncertainty) --------------------------
# WHY these values: m_tau and m_e are taken from paper/main.tex Sec. ssec:eq32,
# which states m_tau = 1776.93 +- 0.09 MeV and m_e = 0.51100 MeV, together with
# the note that an earlier draft used the PDG-2022-era 1776.86.
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

PAPER_LHS_OVER_RHS = 1.000608  # paper/main.tex, Sec. ssec:eq32

# --- search space, declared before scanning ----------------------------------
PREFACTORS = sorted({Fraction(a, b) for a in range(1, 13) for b in range(1, 13)})
RATIOS = [
    (f"{a}/{b}", MASSES[a][0] / MASSES[b][0], float(np.hypot(MASSES[a][1], MASSES[b][1])))
    for a in MASSES
    for b in MASSES
    if a != b and MASSES[a][0] > MASSES[b][0]
]
EXPONENTS = range(1, 25)

# WHY a fixed threshold: an expression is admitted as a candidate *precision*
# relation if it could be stated to better than 0.5 % at all, independently of
# where it lands. See error 3 above for what a deviation-linked threshold does.
SIGMA_MAX = 0.005
N_NULL = 4000
SEED = 20260810


def main() -> None:
    dev = abs((4 / 3) * (MASSES["tau"][0] / MASSES["e"][0]) ** 12 / TARGET - 1)
    sig_eq32 = 12 * MASSES["tau"][1]

    print("=" * 76)
    print("ANCHOR -- against paper/main.tex, not against memory")
    print("=" * 76)
    print(f"  LHS/RHS computed here : {1 + dev:.6f}")
    print(f"  LHS/RHS in the paper  : {PAPER_LHS_OVER_RHS:.6f}")
    print(
        f"  difference            : {abs(1 + dev - PAPER_LHS_OVER_RHS):.2e}"
        "   (m_Planck / alpha_EM convention)"
    )
    print(f"  deviation             : {100 * dev:.4f} %")
    print(f"  Eq.32 own uncertainty : {100 * sig_eq32:.4f} %  -> the 1.0 sigma agreement")

    items = [
        (str(p), rn, n, float(p) * r**n, n * su)
        for p in PREFACTORS
        for rn, r, su in RATIOS
        for n in EXPONENTS
        if 0 < float(p) * r**n < 1e300
    ]
    statable = [x for x in items if x[4] <= SIGMA_MAX]

    print("\n" + "=" * 76)
    print("SEARCH SPACE (declared before scanning)")
    print("=" * 76)
    print(f"  prefactors p/q, p,q <= 12       : {len(PREFACTORS)}")
    print(f"  mass ratios > 1                 : {len(RATIOS)}")
    print(f"  integer exponents 1..24         : {len(EXPONENTS)}")
    print(f"  expressions, all                : {len(items):,}")
    print(f"  expressions statable to {100 * SIGMA_MAX}%   : {len(statable):,}")

    print("\n" + "=" * 76)
    print(f"HITS WITHIN {100 * dev:.4f} % OF THE TARGET")
    print("=" * 76)
    print("  all expressions:")
    for x in sorted(
        (y for y in items if abs(y[3] / TARGET - 1) <= dev), key=lambda t: abs(t[3] / TARGET - 1)
    ):
        star = "  <- Eq.32" if (x[0], x[1], x[2]) == ("4/3", "tau/e", 12) else ""
        print(
            f"    {x[0]:>5} x ({x[1]:>7})^{x[2]:<3} dev {100 * abs(x[3] / TARGET - 1):.4f} %"
            f"  own sigma {100 * x[4]:>8.1f} %{star}"
        )
    hits = [x for x in statable if abs(x[3] / TARGET - 1) <= dev]
    print(f"\n  statable expressions only: {len(hits)}")
    for x in sorted(hits, key=lambda t: abs(t[3] / TARGET - 1)):
        star = "  <- Eq.32" if (x[0], x[1], x[2]) == ("4/3", "tau/e", 12) else ""
        print(
            f"    {x[0]:>5} x ({x[1]:>7})^{x[2]:<3} dev {100 * abs(x[3] / TARGET - 1):.4f} %"
            f"  own sigma {100 * x[4]:.4f} %{star}"
        )

    logv = np.array([np.log(x[3]) for x in statable])
    lt = np.log(TARGET)
    best_real = float(np.min(np.abs(np.expm1(logv - lt))))
    rng = np.random.default_rng(SEED)
    lts = lt + rng.uniform(-np.log(10), np.log(10), N_NULL)
    best = np.array([np.min(np.abs(np.expm1(logv - x))) for x in lts])
    p_value = float((best <= best_real).mean())

    print("\n" + "=" * 76)
    print(f"NULL -- {N_NULL} random targets, log-uniform within +/-1 decade,")
    print("        best hit taken from the SAME statable space")
    print("=" * 76)
    print(f"  real target   : {100 * best_real:.5f} %   (= Eq.32)")
    print(f"  median random : {100 * np.median(best):.5f} %")
    print(f"  10th pct      : {100 * np.percentile(best, 10):.5f} %")
    print(f"  1st pct       : {100 * np.percentile(best, 1):.5f} %")
    print(
        f"\n  look-elsewhere p = {p_value:.4f}"
        f"   (about 1 random target in {1 / p_value:.1f} does at least as well)"
    )
    print("\n  Eq.32 lies between the median and the 10th percentile of what an")
    print("  arbitrary target of this magnitude achieves. Twice better than median,")
    print("  and not extraordinary. The relation is not refuted; the cost of the")
    print("  search that found it is now measured.")


if __name__ == "__main__":
    main()
