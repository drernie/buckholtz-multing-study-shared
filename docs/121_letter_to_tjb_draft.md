# docs/121 — Letter to TJB: Three Questions (Draft)
# Status: DRAFT · NOT_SENT · AWAITING_USER_REVIEW
# Prepared: 2026-06-17
# NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

---

## Subject

Follow-up on reproducibility work: three questions on β_d, IDM thermal history, and H(z) sign

---

## Letter Text (English)

Dear Thomas,

Thank you again for the detailed call on June 14 and for sharing the procedure document
(docs/117). Following your Step 1 approach, I have been running the reconstruction
with real cluster catalogs (MCXC + XMM + Moresco CC) and have reached a point where
three questions would substantially clarify the next steps.

---

**Question 1 — β_d rescaling**

In Table A1, the AI service uses β_d = 4.5. When I compute k_A = E_ICM/c² from
cluster X-ray temperatures (kT ~ 3–8 keV, f_gas ~ 0.15), I obtain:

    k_A / M ≈ 1.3 × 10⁻⁶  (for a median MCXC cluster)

This means the dipole force fraction at cluster scale is:

    ε = β_d × (k_A/M) × (r_A/D) ≈ β_d × 1.3×10⁻⁶ × (R500/D)

For β_d = 4.5 and D = R500: ε ≈ 6 × 10⁻⁶ (completely negligible).
For the H(z) test at cosmological distances (D ~ 100 Mpc): ε ≈ 10⁻¹⁰ (even smaller).

The Gemini service in your appendix gives β_d ≈ 2×10⁴, which raises ε to ~3% at
cluster boundary (D ≈ R500) — marginally non-negligible. However, these numbers assume
r_A/D ≈ 1 (near-contact geometry). For the actual H(z) test at cosmological separations
D ≫ r_A, the dipole fraction shrinks by a further factor r_A/D (e.g., ~0.016 for D~50 Mpc),
so the β_d needed to reach a 1% signal grows by 1–2 additional orders of magnitude.
How the dipole remains observable across these scales is precisely what I cannot reconcile.

**My question:** Is there a physical argument for why β_d should be large (~10³–10⁴)?
For example, does β_d encode a ratio of internal sub-structure scales that is not
captured by the bulk E_ICM/c² definition? Or is β_d treated as a pure fitting
parameter whose value will be determined by data?

Knowing this would clarify whether to proceed with a physics-motivated prior on β_d
or a free-parameter fit.

---

**Question 2 — IDM thermal history**

Your paper states that each IDM isomer has its own photons, gluons, and weak bosons
(a mirror Standard Model sector), with interactions confined within each isomer
(reach = 1 per EM instance). This means cross-isomer coupling is gravitational only.

If the dark sectors were never thermally coupled to ordinary matter (only gravitational
production, rate ~ (H/M_Pl)²  ~ 10⁻⁸ per Hubble time at BBN energies), then:

    ΔN_eff ~ N_dark_nu × (T_dark/T_SM)⁴ × (4/7) ≈ 0

for T_dark/T_SM < 0.38, consistent with Planck 2018 (N_eff = 2.99 ± 0.17).

However, this same gravitational-only history implies that dark baryons could not
form through standard baryogenesis channels (no dark weak interactions with SM bath).

**My question:** Is the intended reading of IDM that each dark sector has its own
independent baryogenesis mechanism (producing dark baryons at the same asymmetry η
as the SM sector independently), or is the dark sector assumed to be in thermal
equilibrium with SM at some early epoch (with decoupling before BBN)?

The distinction matters for whether IDM dark matter is cold (favored) or hot (disfavored).

---

**Question 3 — H(z) dipole sign**

In an unconstrained polynomial fit to the 27 Moresco CC H(z) measurements:

    H(z) = A(1+z)² + B(1+z)³ + C(1+z)⁴

I find positive coefficients [+, +, +], while the MULTING force law predicts [+, −, +]
(with the dipole term contributing a repulsive, negative component to H(z)).

This may indicate that the dipole contribution in the H(z) signal is negligible
at current observational precision (consistent with ε << 1 at β_d = 4.5), or it
may indicate a sign issue in the mapping from F_oP to H(z).

**My question:** Is there a physical reason the effective dipole coefficient in
H(z) could appear positive (e.g., a sign convention difference between the force
law and the cosmological application, or a partial cancellation with the quadrupole)?

---

## Supporting Context (not in letter body — for reference)

Computed results supporting these questions:
- chi2_idm.py: N=5 integer isomers excluded at ~5.8σ by Planck 2018 (ω_DM/ω_b = 5.366;
  σ_total = √(σ_DM² + (N·σ_b)²) = 0.00142 — both Planck uncertainties propagated)
- eq32_verify.py: C9 confirmed 0.17σ (strong asset for H4 empirical relations)
- beta_rescaling.py: β gap = 4 orders (cluster) / 7 orders (cosmological)
- Pearson r = 0.62 (MCXC n=443), 0.70 (XMM n=22); ΔAIC = +2.5 vs ΛCDM

All labeled NOT_VALIDATION · OUR_RECONSTRUCTION as discussed.

---

## Closing

These three questions would allow me to either complete a clean reproducibility
report or identify the precise gate for further theoretical development. I remain
happy to present the full 36-point reconstruction once these are clarified.

With best regards,
Sergey Boyko
Ronin Institute for Independent Scholarship
ORCID: 0009-0009-2178-5701

---

*DRAFT_NOT_SENT · Review before sending · docs/121 · 2026-06-17*
