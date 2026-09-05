# CLAIM P200 — Does caustic-mass sparse-sampling bias (Logan et al. 2022)
# explain part of `P197`'s `MSZ/M200c` residual?

**Date:** 2026-09-06
**Continues:** `FINDING_P199` (Gate 1/2 provenance re-check, confirmed
`P196`-`P198`'s `Δ=500` target selection; also found a real tension
between HeCS-SZ's own "not significantly biased" headline claim and
`P197`'s own `2.5×` `MSZ_equiv/M200c` finding, resolved as: the paper's
claim is about the `σ`-vs-`σ(M_SZ)` slope test, a different comparison
than a direct mass-ratio). Second of the 5-step autonomous follow-up.

## L0 (EstimandOps)

**Question type: descriptive.** Does the number of member galaxies used
to measure each cluster's caustic mass (`Ng`, a real HeCS-SZ VizieR
column, independently discovered this step by listing all available
columns — not previously used in `P196`-`P199`) correlate with the
per-cluster `MSZ_equiv/M200c` ratio, in the direction Logan et al.
(2022, arXiv:2202.08569) report for their own, independent, same-
research-group (Rines/Geller/Diaferio co-authors) sample: caustic mass
increasingly *underestimates* true mass as the number of galaxies used
to trace the caustic falls?

## Falsifiable prediction

If Logan et al.'s mechanism is a real, non-negligible contributor to
`P197`'s residual, `MSZ_equiv/M200c` should correlate **negatively**
with `Ng` (fewer galaxies → larger caustic underestimate → larger
ratio) across the 123 HeCS-SZ clusters, with a real, non-zero
(pre-registered `|r| > 0.15`, roughly matching typical published
mass-proxy-vs-sampling correlations in this literature) Pearson/
Spearman correlation.

## MCID (pre-registered before running)

- `|r| > 0.15` and `p < 0.05`: material — direction and significance
  both support the mechanism as a real, if partial, contributor.
- `|r| ≤ 0.15` or `p ≥ 0.05`: not material by this specific test — does
  not rule out the mechanism (Logan et al.'s own effect was measured on
  a cleaner, X-ray-hydrostatic-vs-caustic comparison, not SZ-vs-caustic,
  and their own well-sampled subsample already required `Ng ≥ 210`,
  likely far above what HeCS-SZ's own `Ng` column typically records) —
  but means this specific dataset cannot confirm it.

## Positive control

Reuse `P197`'s own verified `MSZ_equiv/M200c` pipeline
(`solve_halo_matching_target_delta`, already positive-control-tested in
`P197`) unmodified — this file only adds `Ng` as a new independent
variable and computes a correlation, no new mass-conversion machinery.

## What this does NOT establish

1. Does not prove Logan et al.'s mechanism operates in HeCS-SZ
   specifically — that requires their own hydrostatic-vs-caustic
   comparison method, not a correlation with `Ng` alone (a proxy test,
   not a direct replication).
2. Does not, even if `MATERIAL`, claim to fully explain `P197`'s `2.5×`
   residual — Logan et al.'s own well-sampled-subsample effect size was
   only `~12%`, an order of magnitude smaller than `P197`'s residual.
3. `NO_AUTHOR_ERROR` — about this project's own reconstruction only.

## BLOCKED — see `FINDING_P200`

The direct within-dataset test this file specifies could not run:
HeCS-SZ's own VizieR table exposes a column literally named `Ng`, but
its description is `"Display the members of this cluster within 30'"`
— a clickable UI action in VizieR's own web interface, not tabular
per-cluster galaxy-count data (`tab["Ng"]` returns the literal string
`"Ng"` for every row, confirmed directly). No numeric member-count
column is available via `astroquery` for this table. This is a data-
availability `BLOCKED`, not evidence against Logan et al.'s mechanism —
see `falsification-ladder.md`'s own discipline on this exact
distinction (`BLOCKED-INFRASTRUCTURE` is never recorded as evidence
against a claim).
