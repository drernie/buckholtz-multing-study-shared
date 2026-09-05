# CLAIM P201 — Does real X-ray concentration (Buote+07, Schmidt&Allen+07),
# instead of Duffy+08's simulated relation, change `P197`'s `MSZ→M200`
# conversion, and hence its `2.5×` `MSZ_equiv/M200c` residual?

**Date:** 2026-09-06
**Continues:** `FINDING_P200` (literature search — Logan et al. 2022's
caustic sparse-sampling bias, real but insufficient, direct correlation
test blocked by data availability). Third of the 5-step autonomous
follow-up — a new, specific, mechanistically-motivated hypothesis found
by combining two already-established project findings that were never
previously connected.

## The connection this file tests

`P196_ADDENDUM2` found that real, X-ray-measured cluster concentrations
(Buote et al. 2007, Schmidt & Allen 2007) run **2–3.4× higher** than
Duffy et al. (2008)'s simulated, dark-matter-only concentration-mass
relation — a real, quantified, `[VERIFIED-arXiv]` finding, though it
turned out not to matter for `P196`'s own ratio because `R500` cancels
algebraically there.

`P197`'s own `solve_halo_matching_target_delta` — the function that
converts `MSZ` (a real `Δ=500` mass) up to an `M200`-equivalent mass for
a fair comparison against `M200c` (caustic) — is anchored on **Duffy et
al. (2008)'s own simulated `c200(M,z)` relation**, not a real,
X-ray-measured one. This connection was never tested: does using the
*correct* (real, higher) concentration in that specific conversion step
change the size of `P197`'s own `2.5×` residual?

## L0 (EstimandOps)

**Question type: descriptive.** Holding the rest of `P197`'s pipeline
fixed, does substituting Buote+07's or Schmidt&Allen+07's own
concentration-mass relation (instead of Duffy+08's) into the `MSZ→M200`
conversion step change `mean(MSZ_equiv/M200c)` and/or `P197`'s own
`ratio_msz` (Endpoint 2)?

## Falsifiable prediction

**Mechanistic reasoning (stated before running, per Structure-Bias
Guard — reasoning in prose, not a schema):** for a fixed `Δ=500` mass, a
**higher** concentration means a **more centrally peaked** NFW profile,
which encloses relatively **less** additional mass between `R500` and
`R200` (the profile is already mostly "used up" inside `R500`). So a
higher, real concentration should produce a **smaller** `M200`-
equivalent than Duffy+08's lower, simulated concentration — predicting
`mean(MSZ_equiv/M200c)` should **fall** (move toward, not away from,
`1.0`) when real concentration is used. If this prediction holds and is
large enough, real concentration is a genuine, previously-missed
contributor to closing `P197`'s residual.

## MCID (pre-registered before running)

- `Δmean(MSZ_equiv/M200c) < -0.2` (a drop of more than `0.2` in the mean
  ratio, i.e. more than an `8%` relative move given the baseline
  `2.5049`): material, real contributor.
- Smaller or wrong-signed shift: not material — same "real but
  insufficient" pattern as every other tested candidate in this line.

## Positive controls

Reuses `P196_ADDENDUM2`'s own already-verified `buote_concentration`,
`schmidt_allen_concentration`, `delta_bryan_norman`, `delta_lahav`
(3 positive controls already passed there) and `P197`'s own already-
verified `solve_halo_matching_target_delta` machinery (2 positive
controls already passed there) — this file only combines them via one
new, small generalized solver, tested against both existing baselines
before trusting it on real data.

## What this does NOT establish

1. Does not, even if `MATERIAL`, claim to fully close `P197`'s `2.5×`
   residual — `ADDENDUM2`'s own real-concentration effect on `P196`'s
   ratio was small (`<0.6%`) precisely because `R500` cancels there;
   this file tests a structurally different step where it does NOT
   cancel, so a materially different result is possible but not
   guaranteed by that precedent.
2. Does not validate Buote/Schmidt&Allen's own samples as representative
   of HeCS-SZ's specific cluster population — same caveat already
   carried from `ADDENDUM2`.
3. `NO_AUTHOR_ERROR` — about this project's own reconstruction only.
