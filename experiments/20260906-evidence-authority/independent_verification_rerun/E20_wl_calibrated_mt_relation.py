"""E20 -- closes FINDING_T0_is_not_free.md's own named open question #1:
"which M-T normalization is the ~7 keV from, hydrostatic or weak-lensing
calibrated?" Answers Ernest Prabhakar's item 5, the 3.3-3.6 keV vs ~7 keV
tension, with a REAL, retrievable, weak-lensing-calibrated M-T relation
(the "~7 keV" figure in TJB's own assumptions.yaml was previously
[UNKNOWN] -- A&A returns HTTP 403 to automated requests).

Source: Kettula et al. 2014 (arXiv:1410.8769), "CFHTLenS: Weak lensing
calibrated scaling relations for low mass clusters of galaxies" --
CFHTLenS+COSMOS+CCCP, 70 systems spanning ~2 orders of magnitude in
mass, genuinely weak-lensing calibrated (not hydrostatic). Table 2,
M500-Tx relation, real fitted parameters, fetched directly from the
paper's own HTML source this session.

Equation (11) of the paper: log10(A*E(z)^nA / A0) = log10(N) + alpha *
log10(B*E(z)^nB / B0). For M-T: A=M (nA=1), B=T (nB=0), pivot
M0=5e14 Msun, T0=5.0 keV (the paper's own stated pivot).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

# Kettula et al. 2014, Table 2, M500-Tx relation -- real, quoted values,
# INCLUDING the real intrinsic scatter (sigma_log(A|B)) column, added
# after Step 8a skeptic point 4 (precision was originally overclaimed --
# a bare point estimate with no uncertainty band).
KETTULA_M0_MSUN = 5.0e14
KETTULA_T0_KEV = 5.0
KETTULA_FITS = {
    "all_data_uncorrected": {"alpha": 1.68, "log10N": 0.08, "sigma_dex": 0.14},
    "bias_corrected": {"alpha": 1.52, "log10N": 0.05, "sigma_dex": 0.07},
}

# v82's own archive text, assumptions.yaml, scaling_law_parameters.M0_note
# (quoted verbatim, checked per Step 8a skeptic point 2's own decisive,
# cheap kill-test): "Node mass normalization M(z=0). Theoretical input;
# not independently data-grounded." -- M0 is NOT explicitly stated to be
# an M500 in the observational (weak-lensing-measurable) sense Kettula's
# relation is calibrated on. R_of_z does use a Delta=500 RADIUS
# convention internally, but that does not by itself establish M0 is
# meant as an external M500. This is a real, disclosed, UNRESOLVED
# category-identity gap -- the comparison below is conditional on it,
# not free of it.
V82_M0_NOTE = "Node mass normalization M(z=0). Theoretical input; not independently data-grounded."

# v82's own M0 (this project's own already-verified value, E18/FINDING_T0_is_not_free)
V82_M0_MSUN = 6.0e14
V82_T0_KEV = 3.7163  # already independently verified, FINDING_T0_is_not_free.md
TJB_QUOTED_WL_T_KEV = 7.0  # the archive's own quoted, previously-[UNKNOWN] figure


def kettula_predicted_temperature(mass_msun, fit_key, z=0.0, om=0.30, ol=0.70):
    """Invert Kettula+2014's own eq (11) at z=0 (E(z)=1, matching how
    T0/M0 are quoted as z=0 normalizations in both this relation and
    v82's own archive) to get the predicted T for a given mass."""
    fit = KETTULA_FITS[fit_key]
    alpha, log10N = fit["alpha"], fit["log10N"]
    N = 10.0**log10N
    # log10(M/M0) = log10(N) + alpha*log10(T/T0)  [at z=0, E(z)=1]
    # => T = T0 * (M / (M0*N))^(1/alpha)
    ratio = mass_msun / (KETTULA_M0_MSUN * N)
    return KETTULA_T0_KEV * ratio ** (1.0 / alpha)


def test_positive_control_pivot_recovered():
    """At M=M0*N (the relation's own effective pivot), the predicted T
    must equal T0 exactly, by construction of the inversion algebra."""
    for fit_key, fit in KETTULA_FITS.items():
        N = 10.0 ** fit["log10N"]
        m_pivot = KETTULA_M0_MSUN * N
        t = kettula_predicted_temperature(m_pivot, fit_key)
        assert abs(t - KETTULA_T0_KEV) < 1e-9, (fit_key, t)


if __name__ == "__main__":
    test_positive_control_pivot_recovered()
    print("PC1 [TRIVIAL-BY-CONSTRUCTION] T(pivot mass) recovers T0 exactly for both fits: PASS\n")

    print("=" * 100)
    print(
        "Kettula et al. 2014 (arXiv:1410.8769), Table 2, M500-Tx -- REAL weak-lensing-calibrated relation"
    )
    print(
        f"Pivot: M0={KETTULA_M0_MSUN:.1e} Msun, T0={KETTULA_T0_KEV} keV (the paper's own stated pivot)"
    )
    print("=" * 100)
    for fit_key, fit in KETTULA_FITS.items():
        t_pred = kettula_predicted_temperature(V82_M0_MSUN, fit_key)
        print(
            f"  {fit_key:24s}: alpha={fit['alpha']:.2f}, log10(N)={fit['log10N']:+.2f}"
            f"  ->  T(M={V82_M0_MSUN:.1e} Msun) = {t_pred:.3f} keV"
        )

    t_bc = kettula_predicted_temperature(V82_M0_MSUN, "bias_corrected")
    t_unc = kettula_predicted_temperature(V82_M0_MSUN, "all_data_uncorrected")

    print("\n" + "=" * 100)
    print("Three-way comparison at v82's own M0 = 6e14 Msun")
    print("=" * 100)
    print(
        f"  v82's own T0 (this project, independently verified, FINDING_T0_is_not_free): {V82_T0_KEV:.3f} keV"
    )
    print(
        f"  TJB's own assumptions.yaml quoted comparison figure (previously [UNKNOWN] source): ~{TJB_QUOTED_WL_T_KEV:.1f} keV"
    )
    print(
        f"  Kettula+2014 REAL weak-lensing-calibrated M500-Tx, bias-corrected:     {t_bc:.3f} keV"
    )
    print(
        f"  Kettula+2014 REAL weak-lensing-calibrated M500-Tx, uncorrected:        {t_unc:.3f} keV"
    )

    ratio_v82_to_kettula_bc = V82_T0_KEV / t_bc
    ratio_tjb_to_kettula_bc = TJB_QUOTED_WL_T_KEV / t_bc
    print(
        f"\n  v82_T0 / Kettula_bias_corrected  = {ratio_v82_to_kettula_bc:.3f}   (v82 is {'LOWER' if ratio_v82_to_kettula_bc < 1 else 'HIGHER'})"
    )
    print(
        f"  TJB_quoted(~7) / Kettula_bias_corrected = {ratio_tjb_to_kettula_bc:.3f}   (TJB's own quoted figure is {'LOWER' if ratio_tjb_to_kettula_bc < 1 else 'HIGHER'} than this real relation)"
    )

    print("\n" + "=" * 100)
    print("PART D -- real intrinsic scatter, propagated [added per Step 8a skeptic point 4:")
    print("the original draft reported a bare point estimate with no uncertainty band]")
    print("=" * 100)
    bc = KETTULA_FITS["bias_corrected"]
    scatter_factor = 10.0 ** bc["sigma_dex"]
    t_bc_lo, t_bc_hi = t_bc / scatter_factor, t_bc * scatter_factor
    print(
        f"  Kettula+2014's own quoted intrinsic scatter (bias-corrected M500-Tx): "
        f"sigma_log(A|B)={bc['sigma_dex']:.2f} dex = factor {scatter_factor:.3f}"
    )
    print(
        f"  T(6e14) point estimate: {t_bc:.3f} keV; +/-1 intrinsic-scatter band: [{t_bc_lo:.2f}, {t_bc_hi:.2f}] keV"
    )
    print(
        f"  v82's own T0={V82_T0_KEV:.3f} keV sits {'INSIDE' if t_bc_lo <= V82_T0_KEV <= t_bc_hi else 'OUTSIDE (below)'}"
        f" this +/-1-intrinsic-scatter band."
    )

    print("\n" + "=" * 100)
    print(
        "Interpretation [corrected after Step 8a skeptic, WEAKENED, 5 points -- see FINDING_E20's"
    )
    print(
        "own Response Matrix. Headline 'materially narrows the tension' WITHDRAWN as unlicensed.]"
    )
    print("=" * 100)
    print(
        f"  A REAL, genuinely weak-lensing-calibrated M-T relation (Kettula+2014, Delta=500) gives"
        f" T~{t_bc:.2f} keV (bias-corrected) at a MASS OF THE SAME NUMBER as v82's own M0 -- but see the"
        f" CAVEAT below before treating this as a direct physical comparison."
    )
    print(
        "\n  CAVEAT [decisive check, per Step 8a skeptic point 2]: v82's own archive text"
        f' (assumptions.yaml, M0_note) states M0 is: "{V82_M0_NOTE}" -- NOT explicitly stated to be'
        " an M500 in the observational, weak-lensing-measurable sense Kettula's relation is calibrated"
        " on. v82's R_of_z does use a Delta=500 RADIUS convention internally, but that alone does not"
        " establish M0 itself is meant as an external, WL-comparable M500. This category-identity"
        " question is UNRESOLVED here, not resolved in either direction."
    )
    print(
        "\n  CAVEAT [per Step 8a skeptic point 3]: only ONE paper (2 sub-variants of the same fit) was"
        " checked, out of a real literature with genuine paper-to-paper dispersion in M-T normalization"
        " (Mahdavi+2013, Hoekstra+2015, von der Linden+2014, and others were found in the same search"
        " but not cross-checked). Whether the published range of REAL WL-calibrated M-T relations at"
        " this mass spans up to TJB's own quoted ~7 keV is NOT established here -- a real, named,"
        " unclosed gap, not a settled comparison."
    )
    print(
        "\n  What IS established, conditional on the M0-identity caveat above: IF v82's M0 is read as"
        f" an M500 in Kettula's sense, this one real relation predicts T~{t_bc:.2f} keV (+/-1 intrinsic"
        f" scatter: [{t_bc_lo:.2f},{t_bc_hi:.2f}] keV) -- below TJB's own quoted ~7 keV, and v82's own"
        f" T0={V82_T0_KEV:.2f} keV sits outside this band on the low side. This narrows, but does NOT"
        " close, the gap between v82's own T0 and this one specific, real, external relation -- subject"
        " to the two caveats above, neither resolved."
    )
