# FINDING E20 — a real weak-lensing-calibrated M-T relation gives
# T~5.2 keV at v82's own M0 (below TJB's quoted ~7 keV), but the
# comparison rests on an unresolved mass-definition assumption and
# checked only one paper — corrected after Step 8a skeptic, 5 points

**Date:** 2026-09-06
**Trigger:** same email thread. Ernest's item 5: v82's own T0 gives
`3.3-3.6` keV, "roughly half" the `~7` keV implied by weak-lensing-
calibrated M-T relations at the same mass. Prior work (`FINDING_T0_is_
not_free.md`, 2026-08-10) already found the tension is between two
EXTERNAL calibrations, not intrinsic to MULTING — but left the "~7 keV"
figure's own source `[UNKNOWN]` (A&A returns HTTP 403 to automated
requests).
**Explicit go-ahead given** ("пункт 4 и 5, тоже скрупулёзно").

## Step 8a skeptic — context-blind, claim + full code — verdict:
## WEAKENED, 5 real points, all addressed in place

1. **"Materially narrows the tension" was not licensed.** The
   arithmetic itself is correct (independently re-verified by the
   skeptic by hand) — but the headline conclusion required 3 additional
   sub-claims that were never tested: that Kettula+2014 is representative
   of the real literature's own dispersion, that v82's `M0` is
   comparable to Kettula's `M500`, and that a bare point estimate
   captures the comparison. **Withdrawn.**
2. **Mass-definition mismatch — the decisive check.** v82's own
   `assumptions.yaml` states `M0_note: "Node mass normalization M(z=0).
   Theoretical input; not independently data-grounded."` — **not**
   explicitly an `M500` in the observational, weak-lensing-measurable
   sense Kettula's relation is calibrated on. `R_of_z` uses a `Δ=500`
   radius convention internally, but this does not by itself establish
   `M0` is meant as an external, WL-comparable mass. **Checked directly
   against the archive's own text — genuinely unresolved, reported as
   such, not assumed either way.**
3. **Only one paper checked (2 sub-variants of the same fit), out of a
   real literature with genuine paper-to-paper dispersion** (Mahdavi
   +2013, Hoekstra+2015, von der Linden+2014, and others were found in
   the same literature search but not cross-checked). **Named as a
   real, unclosed gap** — whether the published range of real WL-
   calibrated M-T relations spans up to `~7` keV at this mass is not
   established here.
4. **Precision was overclaimed — no uncertainty band.** Fixed: added
   Kettula+2014's own quoted intrinsic scatter (`σ_log(A|B)=0.07` dex,
   bias-corrected) and propagated it into a real `±1σ` band:
   `[4.45, 6.14]` keV. `v82`'s own `T0=3.72` keV sits **outside** this
   band on the low side — a real, quantified gap remains even after
   accounting for real scatter.
5. **Post-hoc risk** (code written and run before `claim.md`) —
   disclosed explicitly in the original claim, not hidden; the
   corrections above (points 1-4) are the concrete mitigation.

**No point dismissed.**

## Method (unchanged from original)

Kettula et al. 2014 (`arXiv:1410.8769`), Table 2, `M500-Tx` relation —
real, weak-lensing-calibrated, `Δ=500` (matching v82's own `R_of_z`
convention). Inverted the paper's own eq. (11) at `z=0` to solve for
`T` at v82's own `M0=6×10¹⁴ M☉`.

## Results (corrected, with uncertainty)

```
Kettula+2014 M500-Tx, bias-corrected: T(6e14) = 5.226 keV
  intrinsic scatter sigma=0.07 dex -> +/-1sigma band: [4.45, 6.14] keV
v82's own T0 = 3.716 keV -- OUTSIDE this band, on the low side
TJB's own quoted comparison figure: ~7.0 keV -- also outside the band, on the high side
```

## Verdict — corrected, honestly scoped

**Conditional, not closed.** IF `v82`'s `M0` is read as an `M500` in
Kettula's own sense (an assumption v82's own text does not confirm),
this one real, external relation predicts `T≈5.2±0.7` keV — below
TJB's own quoted `~7` keV, and `v82`'s own `T0` sits outside even this
band on the low side. This is real information, narrower than a bare
"~7 keV, unverified" comparison, but it does **not** close Ernest's
item 5 — two real, named gaps remain open (the mass-definition
assumption; single-paper coverage of the real literature's own
dispersion).

## What this does and does NOT establish

**Does establish:** the previously-`[UNKNOWN]` "~7 keV" figure is now
bracketed against one real, cited, retrievable relation, with real
uncertainty attached — genuine progress over "unverified," but not
resolution.

**Does NOT establish:**
1. That `v82`'s `M0` is comparable to Kettula's `M500` — a real,
   unresolved category-identity question, checked directly against the
   archive's own text and found genuinely ambiguous.
2. That Kettula+2014 represents the real literature's own dispersion —
   only one paper checked; a real, named, unclosed gap.
3. Whether MULTING's physics is correct — `NO_AUTHOR_ERROR`.
4. Resolution of the tension to zero — a real, quantified residual
   remains even after accounting for real intrinsic scatter.

## Pearl Registry / next step

Two real, specific, cheap, checkable next steps if this is revisited:
(a) check whether v82's own paper (Sec. II.C, per the archive's own
note) states `M0`'s intended physical meaning explicitly; (b) repeat
the same extraction for 1-2 more real WL-calibrated M-T papers
(Hoekstra+2015, von der Linden+2014 — both already found in this
session's own literature search) to establish the real published
dispersion at this mass.
