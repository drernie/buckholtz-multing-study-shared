# Table A1 Independent Recomputation

**Status:** INTERNAL_CONTRIBUTION_DRAFT | INTERNAL_DIAGNOSTIC_ONLY
**Labels:** NOT_SENT | NOT_VALIDATION | NOT_REFUTATION | AUTHOR_CONFIRMATION_REQUIRED
**Classification:** H_FLRW_PROVENANCE_MISMATCH | ASSUMED_BASELINE_ONLY | NOT_AUTHOR_ERROR

> This is **NOT an author-error claim**. It is an internal reconstruction mismatch under an assumed baseline; the source baseline for the H_FLRW column is not yet recovered.

---

## Summary

- **Total rows:** 12
- **H_FLRW exact matches (<0.1 km/s/Mpc):** 1/12
- **H_FLRW close matches (<0.5 km/s/Mpc):** 1/12
- **Sigma_FLRW exact matches (<0.1):** 0/12
- **Max H_FLRW discrepancy:** 710.55 km/s/Mpc
- **Max sigma_FLRW discrepancy:** 10.691

---

## Row 1 (z=0) Diagnostic

**Best matching hypothesis:** Hypothesis A (standard)

**Hypothesis test results:**
- Hypothesis A (standard convention): ❌ NO MATCH
- Hypothesis B (anchor row): ❌ NO MATCH
- Hypothesis C (alternate sigma): ❌ NO MATCH

**Details:**
- Reported sigma_FLRW: -5.600
- Recomputed (standard): 5.091
- Recomputed (fractional): 0.076712
- Reported sigma_MULT: 1.300
- Recomputed (anchor): 0.000

---

## Discrepancies

Found 11 rows with H_FLRW difference > 0.1 km/s/Mpc:

- z=0.060: reported=68.1, recomputed=69.4, diff=-1.30 km/s/Mpc
- z=0.140: reported=69.3, recomputed=72.3, diff=-3.03 km/s/Mpc
- z=0.250: reported=71.5, recomputed=76.9, diff=-5.35 km/s/Mpc
- z=0.400: reported=75.0, recomputed=83.9, diff=-8.89 km/s/Mpc
- z=0.650: reported=83.0, recomputed=97.7, diff=-14.67 km/s/Mpc
- z=1.000: reported=95.7, recomputed=120.7, diff=-24.96 km/s/Mpc
- z=1.500: reported=114.8, recomputed=159.6, diff=-44.80 km/s/Mpc
- z=2.100: reported=140.3, recomputed=213.9, diff=-73.57 km/s/Mpc
- z=3.200: reported=187.6, recomputed=330.3, diff=-142.75 km/s/Mpc
- z=5.000: reported=265.2, recomputed=558.7, diff=-293.55 km/s/Mpc
- z=8.500: reported=398.5, recomputed=1109.0, diff=-710.55 km/s/Mpc

---

## Assumptions Used

# Assumptions Used in Table A1 Recomputation

## ASSUMPTION 1

**Statement:** H_FLRW uses flat ΛCDM with H0=67.4, Ω_m=0.315, Ω_Λ=0.685

**Evidence:** assumed_standard

**Source:** Planck 2018 cosmology + H0 from Table A1 z=0

**Confidence:** high

**Alternative:** Could use different cosmology (e.g., Ω_m from paper if specified)


## ASSUMPTION 2

**Statement:** Sigma convention is normalized: (H_obs - H_model) / sigma_H

**Evidence:** inferred_from_context

**Source:** Standard residual convention in cosmology

**Confidence:** medium

**Alternative:** Could be absolute residual or fractional error


## ASSUMPTION 3

**Statement:** Row 1 (z=0) treatment unknown — testing 3 hypotheses

**Evidence:** unknown_guessed

**Source:** No explicit statement in paper

**Confidence:** low

**Alternative:** Standard / Anchor / Alternate sigma — to be diagnosed


## ASSUMPTION 4

**Statement:** β_d = 4.5, β_q = 18.0 from Table A1 caption

**Evidence:** explicit_in_paper

**Source:** preprints202511.0598.v6.pdf, Appendix A.3, Table A1 caption

**Confidence:** high

**Alternative:** None (explicitly stated)


---

## Interpretation

**NONE — this is a pure arithmetic report.**

No physics claims are made.
No validation or refutation of MULTING theory.
Results contingent on author confirming cosmological parameters.

---

**Generated:** 2026-05-29
**Author approval required before sharing**