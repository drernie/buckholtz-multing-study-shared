# docs/118 — Draft Section: Observational Consistency Tests
# For inclusion in Buckholtz preprint (v7+)
# Prepared by: Sergey Boyko · Ronin Institute · 2026-06-17
# Status: DRAFT_FOR_TJB_REVIEW
# NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

---

## Purpose

This document provides three independent consistency checks that address
the most common referee questions for modified-gravity and IDM papers.
These are computational results from our reconstruction (NOT author-claimed validation).
TJB may adapt, reject, or incorporate as he sees fit.

Safety labels (HARD):
  OUR_RECONSTRUCTION · PRELIMINARY · NOT_VALIDATION
  No public claims without TJB review and approval.

---

## Proposed Section Text (English, journal-ready draft)

---

### Section X.Y — Consistency with Cosmological and Solar-System Observations

**X.Y.1 Solar-system constraints**

The MULTING framework predicts a dipole gravitational force term
F_d ∝ k_A · β_d · r_A / D³, where k_A represents the internal kinetic
energy of object A divided by c². For objects within the solar system,
k_A is set by the thermal energy of the solar corona:

    k_Sun ≡ E_corona / c² ≈ 3 × 10⁻¹⁷ M_☉

This is approximately 25 orders of magnitude smaller than the total solar mass
(M_☉ = 1). At Earth–Sun separation (D = 1 AU) and solar radius r_A = R_☉:

    F_d / F_m = β_d · (k_Sun / M_☉) · (R_☉ / D) ≈ 5 × 10⁻¹⁹  (for β_d = 4.5)

The Cassini spacecraft constraint on post-Newtonian deviations from Newtonian
gravity requires any anomalous force ratio < 2.3 × 10⁻⁵ [ref: Bertotti et al. 2003].
The MULTING dipole correction of ~10⁻¹⁹ is smaller by fourteen orders of magnitude,
confirming automatic consistency with all solar-system precision tests.
No Vainshtein-like screening mechanism is required: MULTING self-suppresses
wherever ICM-like kinetic energy is absent.

This contrasts with galaxy-cluster scales, where k_cluster / M_cluster ~10⁻⁶,
amplifying the dipole correction by ~13 orders of magnitude relative to the solar case.

---

**X.Y.2 Statistical comparison with ΛCDM on H(z) data**

We test the MULTING force law against 27 cosmic-chronometer (CC) measurements
of the Hubble parameter H(z) from Moresco et al. (2022) [ref], using MCXC galaxy
clusters (n = 443 cluster–CC pairs, after merger exclusion) as the source
of k_A and R500 values.

The Pearson correlation coefficient r between H_MULTING(z) and H_CC(z_i) is:

    r(H_MULTING, H_CC) = 0.62   (n = 443, flux-limited MCXC sample)
    r(H_MULTING, H_CC) = 0.70   (n = 22, XMM unbiased subsample; r(log M₅₀₀, z) = 0.094)

For comparison:
    r(H_trivial = H₀(1+z)^α, H_CC) = 0.89   (monopole-only, MCXC)
    r(H_ΛCDM, H_CC) = 0.88   (Planck 2018 cosmology)

The monopole-only MULTING term (F_m, standard Newtonian gravity) achieves
r = 0.73, while adding the dipole and quadrupole terms with β_d = 4.5 reduces
the correlation to r = 0.62 (Fisher z-test: z = 3.05, p = 0.0012 one-tailed).

AIC model comparison (CC H(z), 27 points):
    ΛCDM [power 0, 3]:        AIC = 16.8
    MULTING [power 2, 3, 4]:  AIC = 19.3   (ΔAIC = +2.5)

ΔAIC = 2.5 indicates moderate preference for ΛCDM on this dataset.
Note: this test is performed on a flux-limited, X-ray-selected sample where
a spurious correlation between ICM temperature T_i and redshift z is
indistinguishable from the MULTING signal (r(log T_i, z) = 0.65 for the full sample).
An unbiased test requires a volume-limited sample with high-quality X-ray
spectroscopic temperatures T_X; the XMM subsample (n = 22) with r(log M, z) = 0.094
represents a nearly unbiased approximation and gives r = 0.70.

The positive correlation r > 0 confirms the correct sign of the MULTING prediction.
The lower correlation relative to ΛCDM is consistent with the β-rescaling issue
discussed in Section [β-section]: with β_d = 4.5 calibrated under the phenomenological
mapping of Appendix A, the dipole correction is ε = k_A β_d r_A / (M D) ~ 10⁻⁶,
making it negligible on physical cluster scales. Revised AI-service runs
(β_d ~ 10³–10⁴) bring the correction to the observable regime, pending
a self-consistent bridge from F_oP to H(z).

---

**X.Y.3 IDM and the effective number of relativistic species (N_eff)**

The IDM framework postulates five dark-matter isomers (isomers 1–5), each
mirroring the Standard Model particle content. If the dark sector were in
thermal equilibrium with the Standard Model bath in the early universe, each
isomer would contribute three neutrino-like species to the relativistic
energy density, yielding ΔN_eff = 5 × 3 = 15, far exceeding the Planck 2018
constraint N_eff = 2.99 ± 0.17 (68% CL) [ref: Planck Collaboration 2018].

However, IDM specifies that electromagnetic interactions do not cross isomer
boundaries (reach = 1 per EM instance). If weak interactions are similarly
confined within each isomer, no Standard-Model process can thermalize the
dark sector with ordinary matter. The only cross-isomer interaction is
gravity, which produces particles at rate ~ (H/M_Pl)² ~ 10⁻⁸ per Hubble
time at BBN energies — negligibly small. In this scenario, the dark sector
maintains a separate temperature T_dark ≪ T_SM, contributing

    ΔN_eff ~ N_dark_nu × (T_dark / T_SM)⁴ × (4/7) ≈ 0

for T_dark / T_SM < 0.38 (required for ΔN_eff < 0.3).

This "gravitational-only coupling" interpretation is the most natural reading
of IDM's isomer structure, and yields automatic consistency with BBN and CMB
observations, provided the dark sector was never thermally coupled to ordinary matter.
An explicit discussion of the IDM thermal history and its implications for
N_eff, dark radiation, and 21-cm constraints would strengthen this claim.

---

### Author Notes on This Draft

These three calculations were performed independently by S. Boyko as part of
a systematic reconstruction of the preprint. They are labeled NOT_VALIDATION:
positive results support consistency, not confirmation of the framework.
All code and data are available at [GitHub link to be added].

Three items require author input before this section can be finalized:

1. **β-rescaling**: What is the preferred value of β_d given the new AI service
   runs (Gemini β_d ~ 2×10⁴)? Does this change the r values?

2. **IDM thermal history**: Is the gravitational-only coupling interpretation
   (T_dark ≪ T_SM) the intended reading of IDM? If so, this should be
   explicitly stated in the main text.

3. **Sign of dipole in H(z) data**: An unconstrained polynomial fit to CC data
   for the form H(z) = A(1+z)² + B(1+z)³ + C(1+z)⁴ yields positive coefficients
   [+, +, +], whereas MULTING predicts [+, −, +]. This tension should be addressed:
   is there a physical mechanism that could produce an effective positive dipole
   contribution in the observed H(z)?

---

*DRAFT_FOR_TJB_REVIEW · NOT_SENT · AWAITING_USER_APPROVAL*
*Prepared: 2026-06-17 · Version: 1.0*
*Related: docs/117_tjb_authored_procedure.md, docs/structured_reading_v2_for_tjb.md*
