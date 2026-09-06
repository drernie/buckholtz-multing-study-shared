"""E15 -- quantify v82's own named, self-flagged, unquantified gap (v82.md:
1060-1063, "we have not attempted to quantify this difference") between
evaluating the force law at a representative thermal energy and averaging it
over the real population scatter FINDING_E13 measured.

Mechanism, verified directly in multing_core.py:112-122:
    F1 = beta1 * (-G) * 2*M*(k/c^2)*(R/d)/d^2     -- LINEAR in k
    F2 = beta2 * (-G) * (k/c^2)^2*(R^2/d^2)/d^2   -- QUADRATIC in k^2
k = k_of(z) is linear in Mgas_of(z), so k's own log-scatter equals
Mgas's -- FINDING_E13's sigma_{Mgas|T}=0.49 (ln-normal), holding T fixed.

Same structural setup FINDING_P157 identified (linear vs quadratic force
term) and FINDING_P158 built machinery for -- P158's own scatter was
explicitly "illustrative, not real". This file uses a real, sourced one.

See CLAIM_E15_jensen_gap_real_scatter.md -- MCID pre-registered before
this file was run.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(
    0,
    str(
        Path(__file__).resolve().parents[2]
        / "data/source_material"
        / "zenodo_21204955_supplemental/code"
    ),
)
from multing_core import forces  # noqa: E402

SIGMA = 0.49  # FINDING_E13: sigma_{Mgas|T}, ln-normal, Ramos-Ceja+2025 Sec 4.4
N_MC = 5_000_000
RNG = np.random.default_rng(20260906)
# TJB's own Table II, unconstrained_spotlighted row -- reused for the sign-
# structure check (Step 8a skeptic, A5), not for a re-fit.
B1_FIT, B2_FIT = 1.4335e10, 7.8067e17
REAL_DATA_ZS = (0.07, 0.25, 1.00, 2.00, 2.33)


def analytic_correction_f1(sigma: float) -> float:
    """E[F1]/F1(k_med) for F1 linear in k, k=k_med*X, ln(X)~N(0,sigma^2).
    E[X] = exp(sigma^2/2)."""
    return float(np.exp(sigma**2 / 2.0))


def analytic_correction_f2(sigma: float) -> float:
    """E[F2]/F2(k_med) for F2 quadratic in k. E[X^2] = exp(2*sigma^2)."""
    return float(np.exp(2.0 * sigma**2))


def monte_carlo_corrections(sigma: float, n: int, rng: np.random.Generator) -> tuple[float, float]:
    """Direct sampling cross-check: k = k_med * X, X = exp(sigma*Z), Z~N(0,1)."""
    z = rng.standard_normal(n)
    x = np.exp(sigma * z)
    return float(np.mean(x)), float(np.mean(x**2))


def test_positive_control_zero_scatter_gives_unity() -> None:
    assert abs(analytic_correction_f1(0.0) - 1.0) < 1e-12
    assert abs(analytic_correction_f2(0.0) - 1.0) < 1e-12


def test_positive_control_mc_matches_analytic(
    sigma: float, n: int, rng: np.random.Generator
) -> None:
    mc_f1, mc_f2 = monte_carlo_corrections(sigma, n, rng)
    an_f1, an_f2 = analytic_correction_f1(sigma), analytic_correction_f2(sigma)
    rel_f1 = abs(mc_f1 - an_f1) / an_f1
    rel_f2 = abs(mc_f2 - an_f2) / an_f2
    assert rel_f1 < 0.005, f"F1 correction: MC={mc_f1:.5f} analytic={an_f1:.5f} ({rel_f1:.3%})"
    assert rel_f2 < 0.005, f"F2 correction: MC={mc_f2:.5f} analytic={an_f2:.5f} ({rel_f2:.3%})"


if __name__ == "__main__":
    test_positive_control_zero_scatter_gives_unity()
    print("PC1 sigma=0 gives unity correction for both F1 and F2: PASS")

    test_positive_control_mc_matches_analytic(SIGMA, N_MC, RNG)
    print(f"PC2 Monte Carlo (N={N_MC:,}) matches closed-form log-normal moments to <0.5%: PASS\n")

    corr_f1 = analytic_correction_f1(SIGMA)
    corr_f2 = analytic_correction_f2(SIGMA)
    ratio = corr_f2 / corr_f1

    print("=" * 78)
    print(f"Jensen's-gap correction factors at sigma_{{Mgas|T}} = {SIGMA} (E13, ONE contributing")
    print("  layer of k's scatter -- see caveat below, NOT the total scatter in k)")
    print("=" * 78)
    print(
        f"  F1 (dipole,   linear in k):    E[F1]/F1(k_med) = exp(sigma^2/2) = {corr_f1:.4f}"
        f"  ({100 * (corr_f1 - 1):+.1f}%)"
    )
    print(
        f"  F2 (quadrupole, quadratic in k): E[F2]/F2(k_med) = exp(2*sigma^2) = {corr_f2:.4f}"
        f"  ({100 * (corr_f2 - 1):+.1f}%)"
    )
    print(
        f"\n  Differential correction (F2 vs F1): exp(1.5*sigma^2) = {ratio:.4f}"
        f"  ({100 * (ratio - 1):+.1f}%)"
    )
    print("  This is a force-TERM-level statement only -- see below for why it does NOT")
    print("  predict an actual re-fit shift in beta2/beta1 (Step 8a skeptic, A4).")

    print("\n" + "=" * 78)
    print("Sign-structure check (Step 8a skeptic, A5): does pop-averaging push F_total")
    print("UP or DOWN net? F_total = F0 - F1 + F2 - F_accretion -- F1 and F2 corrections")
    print("pull in OPPOSITE directions. Crossover at |F2|/|F1| = 0.128/0.616 = 0.208.")
    print("Computed with TJB's own real fitted (beta1,beta2) and his own forces(), at the")
    print("real data redshifts (not a hypothetical):")
    print("=" * 78)
    crossover = (corr_f1 - 1.0) / (corr_f2 - 1.0)
    for z in REAL_DATA_ZS:
        _, f1, f2 = forces(z, B1_FIT, B2_FIT)
        r = abs(f2) / abs(f1)
        print(
            f"  z={z:5.2f}  |F2|/|F1|={r:.4f}  (crossover {crossover:.4f})  "
            f"net pop-avg push on F_total: {'UP' if r > crossover else 'DOWN'}"
        )
    print("  -> UP at every real data point: population-averaging is not sign-ambiguous")
    print("     in practice, whatever its overall applicability (see caveats below).")

    print("\n" + "=" * 78)
    print("What this does NOT establish (Step 8a skeptic corrections, all real)")
    print("=" * 78)
    print("  1. sigma=0.49 is scatter in Mgas AT FIXED T only. k also depends on T itself")
    print("     (via the self-similar M-T step), whose own scatter this project has NOT")
    print("     measured (still UNQUANTIFIED, FINDING_E9). If independent, scatters add in")
    print("     quadrature -- the TRUE scatter in k is likely LARGER than 0.49, making")
    print("     these correction factors a lower-bound-flavored PARTIAL estimate, not a")
    print("     total. Partial cancellation (if T,Mgas are anti-correlated in the shared")
    print("     calibration sample) is also possible -- not checked.")
    print("  2. Whether 'population-averaging' is even the right frame is genuinely")
    print("     ambiguous: v82's own text ('a single representative value... not a")
    print("     scattered population') is compatible with EITHER (a) the node IS meant to")
    print("     represent a population average, in which case this correction is real and")
    print("     v82's point-evaluation is biased, OR (b) the node is a canonical/fitted")
    print("     value and the relevant uncertainty is the SMALL calibration error on the")
    print("     fit itself (B=2.24+-0.03), not the full population scatter. This file")
    print("     computes under reading (a) and does not argue for it over (b).")
    print("  3. The force-term corrections above are NOT a computed re-fit of beta1,beta2.")
    print("     H(z) is a NONLINEAR function of F_total, and this project's own earlier")
    print("     work (E8/E11) found a real (beta1,beta2) near-degeneracy -- an actual")
    print("     re-fit would move along that degeneracy direction, not rescale each term")
    print("     independently. What survives is the FORCE-LAW-LEVEL statement only.")

    print("\n" + "=" * 78)
    print("MCID (pre-registered in CLAIM_E15, force-term level only): MATERIAL if |ratio-1|>10%")
    print("=" * 78)
    material = abs(ratio - 1.0) > 0.10
    print(
        f"  |ratio - 1| = {abs(ratio - 1.0):.1%}  ->  {'MATERIAL' if material else 'not material'}"
        f"  (at the force-term level; NOT a re-fit prediction, see caveats above)"
    )
