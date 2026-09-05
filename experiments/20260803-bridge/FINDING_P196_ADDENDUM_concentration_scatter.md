# FINDING P196 Addendum — concentration scatter is not a meaningful
# contributor to either the mean offset or the cluster-to-cluster
# scatter

**Date:** 2026-09-06
**Claim:** `CLAIM_P196_ADDENDUM_concentration_scatter.md`
**Script:** `P196_addendum_concentration_scatter.py`
**Continues:** `FINDING_P196`, whose own residual (`1.47×` mean ratio
after correction, `11.1%` cluster-to-cluster scatter) named Duffy et
al. (2008)'s own concentration scatter as an untested candidate
explanation.

## Result

**Positive control**: the Monte Carlo machinery, evaluated at zero
scatter (exactly at Duffy et al. 2008's own median `c200(M,z)`),
reproduces `P196`'s own Step 2b point estimate to `<1e-6` relative
error — confirms this file's necessarily-duplicated NFW shape-
correction code is faithful to `P196`'s own function, not a new
formula.

**Monte Carlo** (`N=2000` draws per cluster, `σ(log₁₀c₂₀₀)=0.15`,
`[VERIFIED-arXiv:0804.2486]`, Duffy et al.'s own quoted value for the
exact "Full" NFW `Δ=200` sample this project already uses):

| Quantity | Value |
|---|---|
| Population mean of MC medians | **1.4665** — identical to `P196`'s own point estimate (`1.4665`), shift `= −0.0000` |
| Median per-cluster MC 1-σ half-width | **0.27%** of that cluster's own ratio |
| Implied fraction of the observed `11.1%` population scatter explained by concentration uncertainty alone | **0.1%** |

**Both pre-registered checks resolve exactly as predicted, cleanly.**
The mean-offset check confirms, to machine precision, that symmetric
lognormal scatter does not shift the mean — expected, and now verified
rather than merely argued. The MCID check (`>30%` of variance) is
missed by two orders of magnitude (`0.1%` vs `30%`) — concentration
uncertainty is **not** a meaningful driver of either the `1.47×` mean
offset or the `11.1%` scatter. The `Δ178→500` shape-correction step is
remarkably insensitive to concentration in this regime — a genuinely
informative null result, not merely an absence of information.

## What this settles and what it leaves open

**Settled**: neither the `1.47×` residual mean offset nor the `11.1%`
cluster-to-cluster scatter in `FINDING_P196`'s own corrected comparison
is explained by uncertainty in the Duffy et al. (2008) concentration-
mass relation. This rules out one specific, real, previously-named
candidate — a genuine narrowing, not a non-result.

**Left open, and now the most concrete remaining candidate**: Duffy et
al. (2008)'s own Fig. 4 (read directly this session, `[VERIFIED-
arXiv:0804.2486]`) reports that real X-ray-observed cluster
concentrations (Buote et al. 2007, Schmidt & Allen 2007, ∼70
groups/clusters) run **systematically higher** than their simulated
median — a **one-directional bias**, not scatter, which this file's
symmetric Monte Carlo cannot and does not test. Since higher
concentration changes the `R500/R178` shape ratio in a specific
direction, this is the natural next candidate for the mean-offset
residual specifically — untested here, would require either digitizing
Fig. 4 or fetching Buote/Schmidt & Allen's own concentration
measurements directly (a materially different, larger task than
propagating a quoted scatter number).

**Other untested candidates, unchanged from `FINDING_P196`**: `M200c`'s
own caustic-technique measurement systematics; Girardi's own formula's
residual/intrinsic scatter, independent of any concentration modeling.

## What this does NOT establish

1. Does not explain the `1.47×` mean offset — as pre-registered, this
   was never expected to, and the result confirms that expectation
   rather than merely asserting it.
2. Does not test the documented systematic concentration bias
   (X-ray-observed vs. simulated) — named as the concrete next
   candidate, not attempted here.
3. Does not re-verify `P196`'s own Step 8a skeptic findings — reused
   as already established; this file's own positive control (exact
   recovery of `P196`'s point estimate) is the relevant cross-check
   for the machinery specifically reused/duplicated here.
4. Does not draft or send anything to TJB — the underlying comparison
   remains not ready, per `FINDING_P196`'s own conclusion, now further
   narrowed but not resolved.
5. `NO_AUTHOR_ERROR`.

## Recommended, not authorized, next step

Test the documented systematic bias direction (real cluster
concentrations run higher than Duffy et al. 2008's simulated median)
using real X-ray concentration measurements (Buote et al. 2007 and/or
Schmidt & Allen 2007) rather than another symmetric-scatter check —
this is the one concrete, named, not-yet-attempted mechanism that
could plausibly move the mean, as opposed to the scatter, and would
require a separate, explicit go-ahead given its larger scope (fetching
and using a second real dataset, not just propagating a quoted number).
