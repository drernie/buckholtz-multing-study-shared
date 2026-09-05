# FINDING P200 — Literature grounding: caustic-mass sparse-sampling
# bias is real and directionally consistent, but a direct within-dataset
# test is BLOCKED by data availability

**Date:** 2026-09-06
**Claim:** `CLAIM_P200_caustic_sparse_sampling_bias.md`
**Continues:** `FINDING_P199` (Gate 1/2 provenance re-check). Second of
the 5-step autonomous follow-up (negative-space-miner direction:
external literature search for an already-published, quantified
mechanism, rather than re-deriving one from scratch).

## What was found

A targeted `arxiv` literature search (not from memory — every source
below is `[VERIFIED-arXiv]`, fetched this session) surfaced a
same-research-group, directly on-topic paper never previously consulted
in this project:

> **Logan, Maughan, Diaferio, Duffy, Geller, Rines, Sohn (2022,
> arXiv:2202.08569), "Chandra follow up of the Hectospec Cluster
> Survey: Comparison of Caustic and Hydrostatic Masses and Constraints
> on the Hydrostatic Bias"** — co-authored by the same Rines/Geller/
> Diaferio team behind HeCS-SZ itself (the exact catalog `P196`-`P201`
> use). Compares X-ray hydrostatic to caustic masses for 44 real
> clusters drawn from the same Hectospec Cluster Survey family. Direct
> quote: *"we found evidence that the caustic method increasingly
> underestimates the mass when fewer galaxies are used to measure the
> caustics."* Their own best-sampled subsample (`≥210` member galaxies,
> `n=14`) gives `M_X/M_C = 1.12⁺⁰·¹¹₋₀.₁₀`.

This is directionally consistent with every prior finding in this
line: caustic-technique masses (`M200c` in HeCS-SZ, used throughout
`P196`-`P201`) are *understated* relative to other real mass
estimators, in a real, independently-published, same-survey-family
result — not something this project invented or extrapolated.

A cross-check of HeCS-SZ's own paper (Rines et al. 2016, arXiv:
1507.08289) text directly (not just the abstract) also resolved a real
tension noticed while searching: its Introduction states *"either the
virial theorem or the caustic technique can provide cluster mass
estimates with little bias"* — apparently in tension with `P197`'s own
`2.5×` `MSZ_equiv/M200c` finding. Reading the paper's own headline
claim in context confirms `P197`'s already-stated caveat: the "not
significantly biased" result is about the *slope* of measured `σ`
against a *theoretical virial-scaling prediction* from `M_SZ`, not a
direct ratio of the tabulated `M200c` (caustic) column to `MSZ`
(Planck) column — two different tests, not in direct tension.

## Attempted direct test — BLOCKED, not evidence against the mechanism

`CLAIM_P200` specified testing Logan et al.'s mechanism directly
against HeCS-SZ's own 123 clusters, via a per-cluster galaxy-count
column. HeCS-SZ's VizieR table (`J/ApJ/819/63/table4`) does carry a
column literally named `Ng`, but its actual `astroquery` description is
`"Display the members of this cluster within 30'"` — a clickable
web-UI action in VizieR's own interface, not tabular per-cluster
numeric data (`tab["Ng"]` returns the literal string `"Ng"` for every
row, confirmed directly). **No numeric member-count column is available
for this table via `astroquery`.**

Per `falsification-ladder.md`'s own Substrate Gate discipline, this is
recorded as `BLOCKED-INFRASTRUCTURE` (data-availability), never as
evidence against Logan et al.'s mechanism. A real test would require
either the original member-galaxy lists (a separate, larger HeCS-SZ
data product not in this table) or the Logan et al. (2022) paper's own
cluster-by-cluster table directly — out of scope for this step's time
budget; named here as a specific, well-defined next step if this line
is picked up again.

## Verdict

**Real, citable, directionally-consistent, `[VERIFIED-arXiv]` partial
mechanism** — caustic-mass underestimation with sparse galaxy sampling
is real, published, same-survey-family evidence, not a guess. Direct
quantification against HeCS-SZ's own 123-cluster data is `BLOCKED` by
data availability, not ruled out. Magnitude context: Logan et al.'s own
best-case effect (`~12%`) is an order of magnitude smaller than `P197`'s
`2.5×` residual — even if fully confirmed on this dataset, it would be
a real, partial contributor, not a resolution, matching the pattern of
every other tested candidate in this line.

## What this does NOT establish

1. Does not confirm Logan et al.'s mechanism operates at any specific
   magnitude in HeCS-SZ's own 123 clusters — the direct test is
   blocked, not negative.
2. Does not, even if eventually confirmed, claim to close `P197`'s
   `2.5×` residual on its own — see magnitude context above.
3. `NO_AUTHOR_ERROR` — about this project's own reconstruction and
   literature-search discipline, not a claim about Rines et al.'s or
   Logan et al.'s own work (both correctly and accurately quoted).
