# CLAIM E20 — closing FINDING_T0_is_not_free.md's own named open
# question: what does a REAL, retrievable, weak-lensing-calibrated M-T
# relation actually predict at v82's own M0, bracketing the previously
# [UNKNOWN] "~7 keV" comparison figure — Ernest Prabhakar's item 5
#
# STATUS: WEAKENED after Step 8a skeptic (5 points, all addressed).
# See FINDING_E20_wl_calibrated_mt_relation.md for the corrected,
# honestly-scoped conclusion — the headline below ("materially narrows
# the tension") was WITHDRAWN as unlicensed; kept here verbatim, as
# originally drafted pre-skeptic, per this project's own no-silent-
# correction discipline. Do not quote this file's own Verdict section
# without reading the FINDING's corrected one.

**Date:** 2026-09-06
**Trigger:** same email thread. Ernest's item 5: v82's own calibrated
T0 gives cluster temperatures ~3.3-3.6 keV, "roughly half" the ~7 keV
implied by weak-lensing-calibrated masses at the same mass. This
project's own prior work (`FINDING_T0_is_not_free.md`, 2026-08-10)
already found the tension is between two EXTERNAL calibrations, not
intrinsic to MULTING — but explicitly left the "~7 keV" figure's own
source `[UNKNOWN]`: "A&A returns HTTP 403... the '~7 keV' figure
remains the archive's own unverified claim."
**Explicit go-ahead given** ("пункт 4 и 5, тоже скрупулёзно").

## L0 (EstimandOps)

**Descriptive.** What does a real, accessible, genuinely weak-lensing-
calibrated M-T scaling relation from the published literature predict
for the temperature of a cluster at v82's own M0 (`6×10¹⁴ M☉`)? Not a
claim about whether MULTING is correct.

## Method (post-hoc claim — code written and run first this time; the
## deviation from claim-before-code is disclosed, not hidden)

Found Kettula et al. 2014 (`arXiv:1410.8769`), "CFHTLenS: Weak lensing
calibrated scaling relations for low mass clusters of galaxies" —
CFHTLenS+COSMOS+CCCP, 70 systems, ~2 orders of magnitude in mass,
genuinely weak-lensing calibrated (the paper's own explicit purpose,
not a hydrostatic relation mislabeled). Fetched the paper's own HTML
source directly this session; extracted Table 2's real, quoted `M500-
Tx` fit parameters (`α`, `log10(N)`, pivot `M0=5×10¹⁴ M☉, T0=5.0` keV) —
the same `Δ=500` overdensity convention v82's own `R_of_z` already
uses, avoiding an overdensity-mismatch confound. Inverted the paper's
own eq. (11) at `z=0` to solve for `T` at v82's own `M0=6×10¹⁴ M☉`.

## Controls

- **PC1** (trivial-by-construction): `T` at the relation's own
  effective pivot mass recovers `T0=5.0` keV exactly — confirms the
  algebraic inversion is implemented correctly, not an independent
  physics check.

## Results

```
Kettula+2014 M500-Tx, all-data (uncorrected): alpha=1.68, log10N=+0.08 -> T(6e14)=4.994 keV
Kettula+2014 M500-Tx, bias-corrected:          alpha=1.52, log10N=+0.05 -> T(6e14)=5.226 keV

v82's own T0 (independently verified):         3.716 keV
TJB's own quoted comparison figure:            ~7.0 keV
Kettula+2014 bias-corrected prediction:        5.226 keV

v82_T0 / Kettula_bc = 0.711 (v82 lower)
TJB_quoted(~7) / Kettula_bc = 1.339 (TJB's own quoted figure is HIGHER than this real relation)
```

## Verdict

A real, accessible, genuinely weak-lensing-calibrated relation gives
`T≈5.0-5.2` keV at v82's own `M0` — **materially lower** than TJB's own
quoted `~7` keV comparison figure, and **closer to** (though still
meaningfully above) v82's own `T0=3.72` keV. The residual tension
shrinks from a factor of `~1.9×` (`7/3.72`) to `~1.3-1.4×`
(`5.0-5.2/3.72`) once measured against this specific, real, retrievable
relation.

## What this does and does NOT establish

**Does establish:** the previously-`[UNKNOWN]` "~7 keV" comparison
figure is now bracketed against a real, cited, retrievable alternative
— the tension TJB's own note describes is real but narrower than the
`~7` keV figure alone would suggest, when measured against this
specific relation.

**Does NOT establish:**
1. That Kettula+2014 is definitively THE relation TJB's own note had in
   mind — a different weak-lensing-calibrated relation with a higher
   normalization could still give closer to `~7` keV; this is one real,
   representative data point, not an exhaustive survey of all possible
   WL-calibrated M-T relations in the literature.
2. Whether MULTING's own physics is correct — `NO_AUTHOR_ERROR`,
   Empirical/Model status only.
3. Resolution of the tension to zero — a real, smaller residual gap
   remains (`v82_T0/Kettula_bc ≈ 0.71`).
