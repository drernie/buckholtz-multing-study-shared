# CLAIM — mass-marked generalization of rho: a real rho(r) across all
# separation bins, replacing the closed rho_NN/rho_band designs
# (docs/162 item 9, next named step)

**Date:** 2026-09-13
**Written and committed BEFORE the decisive script runs.** Per FL Step
2b/-1. **User-requested** ("построй mass-marked обобщение для rho").
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

## What this replaces

`FINDING_flamingo_2pcf_m500c_estimand.md` (docs/162 item 9's first
step) built a real 2PCF spatial-amplitude estimand but explicitly did
NOT compute a mass-assortativity statistic, naming a "mass-marked
generalization" as the next step. This claim builds it: instead of
`rho_NN` (one pair per halo, nearest-neighbor only) or `rho_band` (all
pairs, but only in one fixed 40-45 Mpc window), compute `rho(r)` — the
Pearson correlation of paired `log10(M500c)` values among ALL pairs
within EACH separation bin, across the SAME `5-150` Mpc range already
used for the `xi(r)` estimand — giving mass-assortativity as a
function of separation, not a single number at a single scale.

## Method

**Population and bins:** the SAME `M500c`-selected pools (`N in {200,
1000, 5000}`, selected directly from the full catalog) and the SAME
15 log-spaced bins (`5-150` Mpc) as `flamingo_2pcf_m500c_estimand.py`
— reusing already-validated pair-finding machinery, not rebuilding it.

**Statistic per bin:** for all unique pairs `(i,j)`, `i<j`, with
separation in the bin, compute `rho(r) = Pearson(log_m_i, log_m_j)`
(order-of-pair is arbitrary but the statistic is symmetric under
swapping `X` and `Y`, so this is well-defined — the same convention
`FINDING_flamingo_rho_nn_m200c_vs_m500c_selection.md`'s own `rho_band`
already used, generalized to every bin instead of one window).

**Significance (mark-shuffle permutation null, NOT a parametric
formula):** shuffle the mass values among the FIXED real positions
`N_SHUFFLE=200` times, recompute `rho(r)` for each shuffle, and report
the empirical two-sided p-value and z-score (`(observed -
null_mean)/null_std`) per bin. This is the SAME "shuffle marks, not
positions" design already validated in this branch's own
`FINDING_mass_assortativity_and_scatter.md` negative control — it
conditions on the real point pattern and randomizes only the marks, so
it correctly accounts for the real non-independence of pairs (the same
halo appears in many pairs) without assuming an idealized iid-pairs
formula.

**Positive control (mandatory — the prior 2PCF pipeline's own skeptic
review explicitly flagged "absence-only battery, no canary" as a real
gap; this claim closes it):** take the REAL `N=1000` `M500c`-selected
halo POSITIONS (isolating "does the mark/permutation logic work" from
"is the point process itself unusual"), but assign SYNTHETIC marks by
partitioning the box into non-overlapping `50` Mpc cubic cells, drawing
one random "cell level" per cell (`N(0,1)`), and setting each point's
mark to `cell_level + small_noise` (`N(0, 0.1)`). This creates a KNOWN,
by-construction signature: pairs within the same cell (`separation ≲
50` Mpc, dominant at small `r`) should show STRONG positive `rho(r)`;
pairs in different cells (increasingly dominant at larger `r`) should
show `rho(r) ≈ 0`. Passing means the recovered `rho(r)` shows large
positive values at small `r`, decaying toward the shuffle-null range as
`r` grows past the `~50` Mpc cell scale — a qualitative shape check,
not a single pass/fail number.

## What this would and would not settle

- **Directly answers** the original P158-motivating question (does
  mass-assortativity `rho` show real structure) on the population that
  matches v82's own mass convention (`M500c`), using a design that
  generalizes past the two single-scale statistics (`rho_NN`,
  `rho_band`) this branch already closed.
- **Does NOT** resolve richness vs. mass-rank as proxies — inherited,
  disclosed limitation from the prior 2PCF estimand.
- **Does NOT** validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`).
- **Does NOT** compute a single "the answer" number — the honest
  output is a FUNCTION of `r`, and the claim's own falsifiable
  prediction is about its SHAPE (does it show real structure anywhere,
  not "is rho positive or negative" at one arbitrary scale).

## Skeptic pass

Mandatory (Step 8a), context-blind — specifically asked: (a) does the
positive control actually validate the pipeline, and is its own
by-construction signal correctly interpreted; (b) is the mark-shuffle
permutation null correctly implemented (conditioning on real
positions, not re-drawing positions); (c) is any real signal found in
`rho(r)` on the real `M500c` population robust to the same outlier/
low-count concerns the prior 2PCF fit was flagged for; (d) is the
practical conclusion honestly scoped given the many-bins/multiple-
comparisons structure of reporting a p-value per bin.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
