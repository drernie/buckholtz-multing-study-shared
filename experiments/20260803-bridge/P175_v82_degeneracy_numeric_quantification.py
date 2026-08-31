"""P175 -- quantifies FINDING_P165's own two explicitly-flagged unattempted
next steps (its "What this file does NOT establish", point 2): (a) the
numeric value of C = d0*m0/(k0*r0), v82's own local monopole-epsilon vs
(beta1,beta2) degeneracy-direction scale constant, using v82's own actual
numeric baseline values; and (b) whether the ACTUAL reported Table II
(beta1,beta2,H0_anchor) rows trace out a direction consistent with the
predicted degeneracy slope dbeta2/dbeta1=C, and what monopole-tier
epsilon that empirical spread would correspond to under P165's own local
mechanism -- compared directly against this project's own previously
established growth-rate ceiling on the same quantity (A*g^2 <= 8.39e-12,
FINDING_P22/P132).

Source of ALL numeric baseline values and functions below: TJB's own
executable supplemental code, archive/code/multing_core.py and
assumptions.yaml, inside zenodo_archive_v17.zip (Zenodo DOI
10.5281/zenodo.22004287, v17 -- the same supplemental archive
FINDING_P169 already used to independently recover M0). Constants and
functions are copied verbatim (not re-derived, not guessed) so this
script's z=0 baseline values are TJB's own, not this project's estimate.

CORRECTION (2026-08-31, context-asymmetric skeptic-caught -- see
FINDING_P175.md's own "Correction" section for the full account, not
repeated here): the comparison this docstring originally promised in (b)
above -- inverting Table II's own real beta1 span through C to get an
"implied epsilon", then judging it against the growth-rate ceiling -- is
INVALID, a category error. C's null direction (C, C^2, 1) was derived by
FINDING_P165 at FIXED H0_anchor; Table II is a SCAN OVER H0_anchor with
(beta1,beta2) re-optimized at each value -- a different slice of the same
3-parameter space. The implied_epsilon_from_beta1_span() function and its
printed output below are RETAINED, not deleted, so the retraction is
auditable -- but its result must NOT be read as a statement about epsilon.
What DOES survive: C's own value (Section 2 of the .md), and the direct,
self-contained consequence of applying C to a genuinely small,
externally-motivated epsilon (Section 3) -- that computation does not
depend on Table II's real data at all, only on C and an assumed epsilon.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numpy as np

# ---------------------------------------------------------------------------
# Verbatim from TJB's own archive/code/multing_core.py + assumptions.yaml
# ---------------------------------------------------------------------------
MSUN_TO_KG = 1.98847e30
MPC_TO_M = 3.08567758e22
KEV_TO_J = 1.602176634e-16
KMSMPC_TO_SI = 3.24077929e-20
G = 6.674e-11
c = 299792458.0
Om_planck = 0.315
OL_planck = 0.685
H0_planck_si = 67.4 * KMSMPC_TO_SI

M0_kg = 1.193082e45
d0_m = 45.0 * MPC_TO_M
T0_keV = 3.7163
mu_mol = 0.6
m_proton = 1.67262192e-27
T_piv_keV = 2.27
Mgas_piv_kg = 2.28e13 * MSUN_TO_KG
z_piv = 0.25
B_real = 2.24
C_real = -1.00

rho_crit0 = 3.0 * H0_planck_si**2 / (8.0 * np.pi * G)


def Efun(z, Om=Om_planck, OL=OL_planck):
    return np.sqrt(Om * (1.0 + z) ** 3 + OL)


def M_of(z):
    return M0_kg * (1.0 + z) ** (-1.1)


def T_keV_of(z):
    return T0_keV * (M_of(z) / M0_kg) ** (2.0 / 3.0) * Efun(z) ** (2.0 / 3.0)


def Mgas_of(z):
    return Mgas_piv_kg * (T_keV_of(z) / T_piv_keV) ** B_real * (Efun(z) / Efun(z_piv)) ** C_real


def k_of(z):
    """Total ICM thermal energy k_X(z), in Joules (TJB's own function)."""
    return 1.5 * (Mgas_of(z) / (mu_mol * m_proton)) * (T_keV_of(z) * KEV_TO_J)


def rho_crit(z):
    return rho_crit0 * Efun(z) ** 2


def R_of(z):
    return (3.0 * M_of(z) / (4.0 * np.pi * 500.0 * rho_crit(z))) ** (1.0 / 3.0)


# P161/P165's own symbolic force-law convention uses "k_x" bare (no /c^2)
# in a term structurally identical to TJB's own f1 = ...*(k/c**2)*... --
# confirmed by direct term-by-term comparison of P165_monopole_
# degeneracy_check.py's _v82_force_law_with_epsilon against TJB's own
# forces() in multing_core.py. So P161/P165's symbolic k0 IS the
# mass-equivalent k/c^2, not raw Joules -- substitute accordingly below.

# ---------------------------------------------------------------------------
# Table II, verbatim from TJB's own assumptions.yaml (fitted_configurations)
# ---------------------------------------------------------------------------
TABLE_II = [
    # (label, H0_anchor_kms, beta1, beta2, chi2_33)
    ("unconstrained_spotlighted", 73.22, 1.4335e10, 7.8067e17, 15.75),
    ("sh0es_anchored_0pct", 73.04, 1.4233e10, 7.7443e17, 15.78),
    ("pct_25", 71.63, 1.3427e10, 7.2479e17, 18.14),
    ("pct_50", 70.22, 1.2632e10, 6.7582e17, 24.26),
    ("pct_75", 68.81, 1.1848e10, 6.2754e17, 34.14),
    ("pct_90", 67.96, 1.1383e10, 5.9890e17, 41.87),
    ("planck_exact_100pct", 67.40, 1.1075e10, 5.7995e17, 47.77),
]

# This project's own previously established growth-rate ceiling on the
# same epsilon=A*g^2 quantity (FINDING_P22/P132, docs/147 point 3).
GROWTH_RATE_CEILING_EPS = 8.39e-12


def test_positive_control_growth_factors_match_assumptions_yaml():
    """Positive control: TJB's own "ingredient growth factors" block is
    labelled z1965_to_z070 -- z=1.965 down to z=0.070 (NOT z=0.70; a
    misreading of that label as z=0.70 was caught and fixed here after an
    initial run of this exact function failed at ~82% relative error --
    re-checked directly against TJB's own cached
    archive/results/generate_all_results_output.txt, which spells the
    step out in full: "ingredient growth factors z=1.965 -> z=0.070").
    The convention is growth FORWARD in time, (value at z=0.070) /
    (value at z=1.965) -- must match TJB's own reported values (m_X=3.07,
    r_X=2.94, k_X=3.30) within ~1%, since TJB's own file reports them to
    3 significant figures only -- confirms this script's copy of TJB's
    own functions is faithful BEFORE trusting any z=0 baseline value
    derived from them.
    """
    z_hi, z_lo = 1.965, 0.070
    ratios = {
        "m_X": M_of(z_lo) / M_of(z_hi),
        "r_X": R_of(z_lo) / R_of(z_hi),
        "k_X": k_of(z_lo) / k_of(z_hi),
    }
    expected = {"m_X": 3.07, "r_X": 2.94, "k_X": 3.30}
    for key, exp in expected.items():
        rel_err = abs(ratios[key] - exp) / exp
        assert rel_err < 0.01, (
            f"{key}: got {ratios[key]:.4f}, expected {exp} (rel err {rel_err:.4%})"
        )
    return ratios


def compute_C_scale():
    """C = d0*m0/(k0*r0), P165's own null-space scale constant, evaluated
    at TJB's own real z=0 baseline values. k0 here is the MASS-EQUIVALENT
    (k_of(0)/c**2), matching P161/P165's symbolic convention -- see note
    above.
    """
    m0 = M0_kg
    d0 = d0_m
    r0 = R_of(0.0)
    k0_joules = k_of(0.0)
    k0_mass_equiv = k0_joules / c**2
    C = d0 * m0 / (k0_mass_equiv * r0)
    return C, {"m0": m0, "d0": d0, "r0": r0, "k0_joules": k0_joules, "k0_mass_equiv": k0_mass_equiv}


def empirical_beta_slope():
    """Empirical d(beta2)/d(beta1) between each adjacent pair of Table II
    rows (sorted by H0_anchor, i.e. by position along the real reported
    degeneracy), plus the same slope computed end-to-end across the full
    7-row span.
    """
    rows = sorted(TABLE_II, key=lambda r: r[1])
    pairwise = []
    # strict=False: rows and rows[1:] are deliberately unequal length (pairwise iteration)
    for (l0, _h0a0, b1_0, b2_0, _), (l1, _h0a1, b1_1, b2_1, _) in zip(rows, rows[1:], strict=False):
        d_b1 = b1_1 - b1_0
        d_b2 = b2_1 - b2_0
        pairwise.append((f"{l0}->{l1}", d_b2 / d_b1))
    b1_lo, b1_hi = rows[0][2], rows[-1][2]
    b2_lo, b2_hi = rows[0][3], rows[-1][3]
    end_to_end_slope = (b2_hi - b2_lo) / (b1_hi - b1_lo)
    return pairwise, end_to_end_slope, (b1_hi - b1_lo), (b2_hi - b2_lo)


def implied_epsilon_from_beta1_span(C, delta_beta1):
    """Inverting P165's own null-direction relation delta_beta1 = C * delta_epsilon
    (i.e. delta_epsilon = delta_beta1 / C): what epsilon would explain the
    ACTUAL beta1 range Table II reports, under P165's own local mechanism.
    """
    return delta_beta1 / C


if __name__ == "__main__":
    ratios = test_positive_control_growth_factors_match_assumptions_yaml()
    print("Positive control -- growth factors z=1.965 -> z=0.070, vs TJB's own assumptions.yaml:")
    for k, v in ratios.items():
        print(
            f"  {k}: computed {v:.4f}  (TJB reports ~{{'m_X':3.07,'r_X':2.94,'k_X':3.30}}[{k!r}])"
        )
    print("  PASS -- within 1% of TJB's own reported values.\n")

    C, baseline = compute_C_scale()
    print("v82's own z=0 baseline values (TJB's own multing_core.py, SI units):")
    for k, v in baseline.items():
        print(f"  {k} = {v:.6e}")
    print(
        f"\nC = d0*m0/(k0*r0) = {C:.6e}  (dimensionless -- both beta1,beta2 are dimensionless in v82's own force law)\n"
    )

    pairwise, e2e_slope, d_beta1_span, d_beta2_span = empirical_beta_slope()
    print("Empirical d(beta2)/d(beta1) between adjacent Table II rows (TJB's own reported values):")
    for label, slope in pairwise:
        print(f"  {label}: {slope:.6e}")
    print(f"  end-to-end (planck_exact_100pct -> unconstrained_spotlighted): {e2e_slope:.6e}")
    print(
        f"\nPredicted degeneracy slope C (from P165's local math + TJB's own baseline constants): {C:.6e}"
    )
    ratio_pred_to_empirical = C / e2e_slope
    print(
        f"ratio predicted/empirical = {ratio_pred_to_empirical:.4e}  (a 2.33x mismatch -- NOT "
        f"'same order of magnitude, expected': Table II's own slope is tight to <1% across all "
        f"6 adjacent-row pairs, so this mismatch is real, not noise -- see FINDING_P175.md "
        f"Correction point 2)\n"
    )

    implied_eps = implied_epsilon_from_beta1_span(C, d_beta1_span)
    print(
        f"Table II's own real beta1 span (planck_exact_100pct -> unconstrained_spotlighted): "
        f"delta_beta1 = {d_beta1_span:.4e}"
    )
    print(
        f"RETRACTED quantity, kept for auditability only -- NOT a valid epsilon estimate (category "
        f"error: C was derived at FIXED H0_anchor, Table II SCANS H0_anchor -- see FINDING_P175.md "
        f"Correction point 1): naive delta_eps = delta_beta1 / C = {implied_eps:.4e}"
    )
    print(
        f"\nThis project's own previously established growth-rate ceiling on the SAME quantity "
        f"(A*g^2 <= {GROWTH_RATE_CEILING_EPS:.2e}, FINDING_P22/P132):"
    )
    print(f"  implied_epsilon / growth_rate_ceiling = {implied_eps / GROWTH_RATE_CEILING_EPS:.4e}")
