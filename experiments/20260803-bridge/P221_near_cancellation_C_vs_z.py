"""
P221 -- does the near-cancellation amplification factor C(z) computed from
TJB's own force percentages track any structure relevant to FINDING_E8's
4.0-7.6x Hessian eigenvalue sensitivity, or is C(z)~15 a single-z snapshot
unrepresentative of the other 32 CC/anchor points feeding the fit?

Kill-test for hypothesis-arbiter cycle on "C~=15 vs E8's 4-8x" (delegated by
/boyko-why-ladder Chain C, 2026-09-08). Computes C(z) = (|A|+|B|)/|A+B| with
A=-F1/gross*100, B=F2/gross*100 -- SAME normalization as
generate_all_results.py's own printed "-F1"/"F2" percentages (gross =
|F0|+|F1|+|F2|+|Facc|) -- at all 33 real data z-points (31 CC + SH0ES anchor
+ DESI DR2 Lya), using the frozen 'unconstrained_spotlighted' fit.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR -- this is a diagnostic on our own reconstruction's
sensitivity, not a claim about v82 being right or wrong.
"""

import sys
from pathlib import Path

import numpy as np
import yaml

CODE_DIR = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "source_material"
    / "zenodo_21204955_supplemental"
    / "code"
)
sys.path.insert(0, str(CODE_DIR))
from multing_core import F_accretion, forces  # noqa: E402

Z_SHOES = 0.0233
Z_DESI = 2.33


def main() -> None:
    with open(CODE_DIR / "assumptions.yaml") as f:
        assumptions = yaml.safe_load(f)
    cc_points = assumptions["cosmic_chronometer_data"]["points"]
    zd = np.array([p[0] for p in cc_points])
    z33 = np.sort(np.concatenate([zd, [Z_SHOES, Z_DESI]]))

    # "unconstrained_spotlighted" Table II row, per generate_all_results.py's
    # own reproduced fit (H0_anchor=73.22) -- same values already used
    # project-wide (FINDING_P219, FINDING_P220). Positive control below
    # reproduces this file's own headline_cases table exactly before
    # trusting these at the other 29 z-points.
    b1s = 1.4335e10
    b2s = 7.8067e17

    print(f"frozen fit: beta_1={b1s:.6e}  beta_2={b2s:.6e}")

    # Positive control -- reproduce generate_all_results.py's own printed
    # headline_cases table (4 z-values, tol matches that file's own "-F1"/
    # "F2" tolerances 0.02) BEFORE trusting this script's numbers anywhere
    # else. If this fails, nothing below should be read.
    pc_expected = {
        1.965: (52.99, -46.53),
        1.07: (53.04, -46.54),
        0.5: (52.14, -47.48),
        0.070: (49.76, -49.89),
    }
    print("POSITIVE CONTROL -- reproduce generate_all_results.py's own headline_cases:")
    pc_ok = True
    for zc, (exp_a, exp_b) in pc_expected.items():
        f0, f1, f2 = forces(zc, b1s, b2s)
        facc = F_accretion(zc)
        gross = abs(f0) + abs(f1) + abs(f2) + abs(facc)
        a, b = -f1 / gross * 100, f2 / gross * 100
        ok = abs(a - exp_a) < 0.02 and abs(b - exp_b) < 0.02
        pc_ok &= ok
        print(
            f"  z={zc}: got (-F1={a:+.3f}, F2={b:+.3f})  expected ({exp_a:+.2f}, {exp_b:+.2f})  {'OK' if ok else 'FAIL'}"
        )
    assert pc_ok, "positive control failed -- do not trust anything below"
    print()

    print(f"{'z':>8}{'F1% (-F1)':>12}{'F2%':>10}{'net%':>9}{'C':>12}")
    print("-" * 55)

    rows = []
    for z in z33:
        f0, f1, f2 = forces(z, b1s, b2s)
        facc = F_accretion(z)
        gross = abs(f0) + abs(f1) + abs(f2) + abs(facc)
        a = -f1 / gross * 100
        b = f2 / gross * 100
        denom = abs(a + b)
        c = (abs(a) + abs(b)) / denom if denom > 1e-9 else float("inf")
        rows.append((z, a, b, c))
        c_str = f"{c:12.3f}" if np.isfinite(c) else f"{'inf':>12}"
        print(f"{z:8.4f}{a:12.3f}{b:10.3f}{a + b:9.3f}{c_str}")

    cs_finite = np.array([r[3] for r in rows if np.isfinite(r[3])])
    n_inf = sum(1 for r in rows if not np.isfinite(r[3]))

    print()
    print(f"n points: {len(rows)}  (finite C: {len(cs_finite)}, non-finite/undefined: {n_inf})")
    print(
        f"C at z=1.07 (the value bridge-ladder used): {[r[3] for r in rows if abs(r[0] - 1.07) < 1e-6]}"
    )
    print(f"median finite C: {np.median(cs_finite):.3f}")
    print(f"mean finite C:   {np.mean(cs_finite):.3f}")
    print(f"min/max finite C: {cs_finite.min():.3f} / {cs_finite.max():.3f}")
    print(f"IQR: [{np.percentile(cs_finite, 25):.3f}, {np.percentile(cs_finite, 75):.3f}]")

    print()
    print("Naive unweighted RMS-style aggregate (1/median(1/C), a rough proxy for")
    print("how a Hessian sum-of-squares would weight many near-cancelling terms")
    print("if each z contributed independently and roughly equally):")
    inv_c_median = np.median(1.0 / cs_finite)
    print(f"  1/median(1/C) = {1.0 / inv_c_median:.3f}")


if __name__ == "__main__":
    main()
