# CLAIM P196 Addendum — propagating Duffy et al. (2008)'s own quoted
# concentration scatter through the Δ178→500 shape correction

**Date:** 2026-09-06
**Continues:** `FINDING_P196`, which named "the Duffy et al. 2008
concentration relation's own real scatter (∼0.1 dex, not propagated as
an uncertainty band here)" as an explicit, untested candidate
explanation for part of the corrected `1.47×` residual.
**Authorization:** explicit user go-ahead ("да, продолжай с
concentration-scatter, действуй автономно выполни все что возможно"),
2026-09-06.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive.

## What is newly verified before this file (primary source, not memory)

`[VERIFIED-arXiv:0804.2486]`, full text fetched this session: Duffy et
al. (2008) report, for the exact "Full" NFW `Δ=200` sample this
project's own `duffy2008_concentration` already uses (`A=5.71±0.12,
B=-0.084±0.006, C=-0.47±0.04`, confirmed to match Table 1 exactly):
**`σ(log₁₀c₂₀₀)=0.15`** dex, lognormal (their §3, citing Jing 2000 for
the lognormal form). This is a real, quoted number, not this project's
own estimate.

**A second, separate, and directionally important fact from the same
source, not previously used in this thread**: Duffy et al.'s own Fig. 4
compares their simulated median `c(M)` against real X-ray-observed
cluster concentrations (Buote et al. 2007, Schmidt & Allen 2007, ∼70
groups/clusters, median `z=0.1`) — "the observationally inferred
concentrations are significantly greater than the predicted medians."
The paper offers two candidate explanations, neither resolved in the
paper itself: the simulated concentrations may be too low (missing
baryonic physics), or the X-ray sample may be biased toward
high-concentration (high-luminosity) objects. **This is a real,
documented, one-directional (not symmetric) effect — separate from the
symmetric scatter this file quantifies.**

## New estimand element specific to this file

**Population**: same 123 HeCS-SZ clusters, same `M200c`, same
`Δ=178→500` NFW shape-correction pipeline as `P196`'s own Step 2b —
only the concentration input is changed, per the Minimal Relaxation
Rule.

**Endpoint 1**: Monte Carlo propagation of `c200 ~ lognormal(Duffy+08
median, σ(log₁₀c)=0.15)` (N=2000 draws per cluster) through Step 2b,
reporting the resulting per-cluster 16th/50th/84th percentile of the
corrected ratio, and the population-level scatter this adds.

**Endpoint 2**: does concentration-scatter propagation (symmetric,
zero-mean in log-space by construction) meaningfully reduce, explain,
or leave unchanged (a) the `1.47×` MEAN offset, and (b) the `11.1%`
cluster-to-cluster scatter already measured in `P196`?

**Falsifiable predicate, stated honestly before running**: symmetric
lognormal scatter propagated through a deterministic, smooth pipeline
cannot shift the MEAN of the output by more than a small (second-order,
Jensen-inequality-driven) amount — this file does **not** expect
Endpoint 1 to explain the `1.47×` offset, and says so before running,
to avoid the appearance of a post-hoc rescue. What IS open and
genuinely tested: how much of the `11.1%` cluster-to-cluster SCATTER
is attributable to concentration uncertainty alone.

**MCID (pre-registered)**: concentration scatter is judged a material
contributor to the observed `11.1%` scatter if the MC-propagated
per-cluster scatter (median absolute spread across the 16-84th
percentile range, aggregated) accounts for `>30%` of the observed
population variance in `ratio_2b`. Below that, concentration
uncertainty is a minor contributor and the `11.1%` scatter is mostly
driven by something else (real cluster-to-cluster diversity, `M200c`
measurement/systematic uncertainty, or Girardi's own formula's own
residual scatter).

## What this does NOT establish

1. Does not, and is not expected to, explain the `1.47×` mean-offset
   residual — symmetric scatter is the wrong kind of correction for
   that; the documented systematic bias (real clusters run
   higher-concentration than Duffy+08's simulations) is the candidate
   mechanism for the mean offset, and is explicitly NOT quantitatively
   tested here (would require digitizing Fig. 4 or fetching the
   Buote/Schmidt&Allen concentration measurements — out of scope for
   this addendum, named as the next open step if this line continues).
2. Does not re-run or re-verify `P196`'s own positive controls or Step
   8a skeptic findings — reused as already established.
3. Does not draft or send anything to TJB.
4. `NO_AUTHOR_ERROR`.
