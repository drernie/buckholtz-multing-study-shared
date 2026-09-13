# CLAIM — is the FLAMINGO/literature gamma mismatch a fit-range
# artifact (real xi(r) curvature) rather than a genuine sim-vs-
# observation shape discrepancy? (docs/162 item 9, closing diagnostic)

**Date:** 2026-09-13
**Written and committed BEFORE the decisive script runs.** Per FL Step
2b. Kept lean (Structure-Bias Guard precedent for a fully-specified
diagnostic refit of ALREADY-RECORDED data — no new FLAMINGO download,
no new statistic, only re-fitting numbers already in `FINDING_
flamingo_2pcf_m500c_estimand.md`'s own raw output). **User-requested**
("закрой docs/162 item 9 окончательно").
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

## Continues

`FINDING_flamingo_2pcf_m500c_estimand.md` found FLAMINGO's `xi(r)`
power-law fit over the full `5-150` Mpc range gives `gamma=2.1-2.6`,
systematically steeper than Basilakos & Plionis (2004)'s cited
`gamma=1.6-2.0` — flagged as a real, unresolved shape disagreement.
This diagnostic asks: is the full-range fit averaging over GENUINE
curvature in `xi(r)` (shallower at small/mid `r`, steeper at large
`r` — a real, well-known feature of correlation functions near the
transition out of the strongly-clustered small-scale regime), which
would make an UNMATCHED fit range (already named as confound #5 in the
prior FINDING, never investigated) the actual driver of the mismatch,
rather than a genuine sim-vs-observation shape difference?

## Method

Re-fit the SAME already-recorded `xi(r)` values (verbatim from
`FINDING_flamingo_2pcf_m500c_estimand.md`'s raw output, for `N in
{200, 1000, 5000}`) over four candidate `r`-ranges: full `[5,150]`
(as originally reported), small-`r` `[5,30]`, mid-range `[10,50]`
(closer to where cluster-2PCF literature studies typically fit, given
their own `r0` values are tens of Mpc, not hundreds), and large-`r`
`[30,150]`. Also compute the bin-to-bin LOCAL log-log slope as a
secondary, more direct (if noisier) curvature diagnostic.

**Falsifiable prediction**: if the mismatch is a fit-range artifact,
restricting to `[10,50]` Mpc should bring `gamma` measurably closer to
the literature's `1.6-2.0` range than the full-range fit did, AND the
large-`r`-only fit should be measurably STEEPER than the small/mid-`r`
fits (confirming genuine curvature, not just refit noise). If `gamma`
stays similarly steep (or gets steeper) under the narrower ranges, the
mismatch is NOT a fit-range artifact and remains a genuine open
question.

## What this would and would not settle

- **Would settle**: whether the specific `gamma` mismatch flagged in
  the prior FINDING is attributable to an unmatched fit range (a
  named, disclosed confound) rather than a deeper sim-vs-observation
  discrepancy.
- **Does NOT** newly validate the `r0` order-of-magnitude match (already
  established) or resolve the other four confounds (selection
  function, redshift, cluster-definition, estimator differences) named
  in the prior FINDING — those remain out of scope.
- **Does NOT** validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`).

## Skeptic pass

Mandatory (Step 8a), context-blind — specifically asked: (a) is
re-fitting over 4 overlapping, researcher-chosen ranges itself a
multiple-comparisons risk (picking whichever range looks best); (b) is
the local-slope diagnostic's noise level correctly characterized, not
overclaimed; (c) is the practical conclusion for `docs/162` item 9
honestly scoped given the small number of bins in each restricted
range (as few as `4-8`).

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
