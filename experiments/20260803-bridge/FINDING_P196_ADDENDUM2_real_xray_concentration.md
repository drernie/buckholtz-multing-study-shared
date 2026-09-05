# FINDING P196 Addendum 2 — real X-ray concentrations confirm the
# documented direction but do not move the residual; a skeptic-caught
# algebraic identity explains why

**Date:** 2026-09-06
**Claim:** `CLAIM_P196_ADDENDUM2_real_xray_concentration.md`
**Script:** `P196_addendum2_real_xray_concentration.py`
**Continues:** `FINDING_P196_ADDENDUM` (concentration *scatter* ruled
out as a contributor); named Duffy et al. (2008)'s own documented
directional bias — real X-ray-observed concentrations run
systematically higher than simulated — as the next concrete candidate.

## Result

**Three positive controls pass**, including one added mid-analysis
after a Step 8a skeptic pass found a real gap (see Corrections below):
Bryan & Norman (1998) `Δ_vir(z=0)=101.1` independently re-derived and
matched against Buote et al.'s own quoted value; Duffy et al. (2008)'s
own relation round-trips exactly through the new machinery at `Δ=200`;
a mock halo at a genuinely non-trivial `Δ=150` (matching neither `178`,
`200`, nor `500`) with known `(M_vir, c_vir)` is recovered exactly from
its own true `M200` alone.

**Real, quoted concentration inputs** (both `[VERIFIED-arXiv]`, primary
sources fetched this session):

| Source | Type | Fitted normalization | Median c used (this sample) |
|---|---|---|---|
| Duffy et al. (2008) | N-body simulation | `c₁₄=5.71` (at `Δ=200`) | **3.71** |
| Buote et al. (2007) | 39 real X-ray systems | `c₁₄=9.0±0.4` (at Bryan-Norman `Δ_vir(z)`) | **7.06** |
| Schmidt & Allen (2007) | 34 real Chandra clusters | `c₀=7.55±0.90` (at Lahav `Δc(z)`) | **12.61** |

**Both real relations confirm the documented direction** — real
X-ray-measured concentrations run substantially higher than Duffy et
al.'s simulated median, exactly as their own Fig. 4 (read directly,
`FINDING_P196_ADDENDUM`) reported. This is not a small effect: median
concentration nearly doubles (Buote) or more than triples
(Schmidt & Allen) relative to the simulated baseline.

**But the final mean ratio barely moves**: `1.4665` (Duffy) →
`1.4703` (Buote) → `1.4747` (Schmidt & Allen) — under `0.6%` relative
change despite a `~3.4×` swing in the concentration input. The
pre-registered MCID band (`[0.95,1.05]`) is missed by all three, by
essentially the same margin.

## Why: a skeptic-caught algebraic identity, independently re-derived

A Step 8a context-blind skeptic pass on this file's own code found the
mechanistic reason, which was independently re-verified by hand before
accepting it: **`P196`'s own `ratio_2b` formula cancels `R500`
algebraically.**

```
ratio_2b = (r_vir_2a · (R500/R178)) / R500  =  r_vir_2a / R178
```

`R500` appears in both numerator and denominator and cancels exactly —
this is not new to this addendum; it was already implicit in `P196`'s
own original Step 2b, unnoticed at the time. **The final ratio depends
only on `r_vir_2a` (Girardi + the exact `z`-reference correction,
independent of any concentration source) and `R178`** — the radius of
the `M200c`-anchored NFW halo at Girardi's own `Δ=178` convention.
Since `R200` is **exactly, definitionally fixed** by the real `M200c`
alone (`R200=(3M200c/(4π·200·ρ_crit(z)))^(1/3)`, no NFW/concentration
input at all), and `R178` only depends on concentration through the
mild NFW shape ratio `R178/R200` — the SAME weak dependence
`FINDING_P196_ADDENDUM`'s Monte Carlo already found (a `0.15`-dex
scatter in `c` moves the ratio by `<0.3%`) — **any concentration
source, simulated or real, was always going to move this specific
final number only weakly, by construction of the formula itself, not
because of a coincidence between three unrelated concentration
estimates.**

**This does not make the result wrong — the numbers are real and the
positive controls hold — but it changes what the result can honestly
claim.** The finding is not "we tested whether real concentrations
close the gap and they don't" in an open-ended sense; it is the
narrower, still genuine: "the specific `Δ178→500` shape-correction
step this pipeline uses is structurally insensitive to concentration
source, because `R500` cancels out of its own defining ratio." Both
statements point to the same practical conclusion (concentration
modeling is not where the `1.47×` residual lives), but the mechanism
is now precisely understood rather than merely observed.

## Corrections applied (Step 8a context-blind skeptic pass, 2026-09-06)

1. **Item 1 (algebraic cancellation) — Accepted, reframed.** The
   skeptic's finding that `R500` cancels out of `ratio_2b` is
   independently re-verified above and changes the finding's own
   framing (see "Why" section) — not a code bug, but a more precise
   and complete explanation than "empirically insensitive," which is
   what the original draft of this file asserted without the
   mechanism.
2. **Item 2 (missing non-trivial positive control) — Accepted, fixed.**
   The original `test_positive_control_duffy_roundtrip_is_identity`
   only exercised the `Δ=200` case, where the root-find is trivial
   (residual is zero at the starting guess) — it never tested the
   `brentq` search or the `delta_obs_func` threading at a genuinely
   different `Δ`, which is exactly what Buote's and Schmidt & Allen's
   own conventions need. Fixed: added
   `test_positive_control_nontrivial_delta_roundtrip`, a mock halo at
   `Δ=150` with known `(M_vir, c_vir)`, recovered exactly (`<1e-6`
   relative error on all four quantities) from its own true `M200`
   alone — genuinely exercises the previously-untested branch.
3. **Item 3 (h-convention) — `CONFIRMED-OK`**, independently re-traced
   by hand: `M14=1e14 h⁻¹M☉` and `Mpivot=8e14 h⁻¹M☉` both correctly
   converted to physical `M☉` via `/h_local` before use.
4. **Item 4 (Schmidt & Allen's `c≈12.6` median plausibility) —
   Accepted as a real, honestly-scoped limitation, not a bug.** Their
   own pivot mass (`8×10¹⁴ h⁻¹M☉ ≈ 1.14×10¹⁵ M☉`) sits well above
   HeCS-SZ's typical cluster mass (`~3-4×10¹⁴ M☉`); combined with their
   steep fitted slope (`a=−0.45`), applying their relation to this
   sample's mass range is a real extrapolation below their own
   calibration range, not a bug in this file's implementation of their
   formula. Noted explicitly, not smoothed over.

## What this settles and what it leaves open

**Settled**: neither concentration scatter (`FINDING_P196_ADDENDUM`)
nor concentration source — simulated vs. two independent, real,
X-ray-measured relations that themselves disagree with each other by a
factor of `~2.6` in slope — meaningfully moves `P196`'s own `1.47×`
residual. This is now understood mechanistically, not just observed:
`R500` cancels algebraically from the ratio this pipeline computes,
so no concentration input, however different, could have moved it far.

**Left open, genuinely narrowed**: the residual candidates are now
`M200c`'s own measurement systematics (the HeCS-SZ catalog's caustic-
technique mass estimate, whose own known systematics were flagged but
not tested in the very first version of this line, `FINDING_P196`
itself), or Girardi's own formula's residual/intrinsic scatter
independent of any concentration modeling, or a genuine physical
signal about the `ρ_crit(z)`-circularity itself.

## What this does NOT establish

1. Does not explain the `1.47×` mean offset — now understood as
   structurally *unreachable* by any concentration-source correction
   in this specific pipeline, not merely untested.
2. Does not resolve the real Buote-vs-Schmidt&Allen disagreement —
   both used and reported, neither preferred.
3. Does not draft or send anything to TJB.
4. `NO_AUTHOR_ERROR`.

## Recommended, not authorized, next step

Given concentration (both scatter and source) is now understood to be
structurally unable to move this pipeline's own `ratio_2b`, the
recommended next candidate shifts to `M200c`'s own caustic-technique
systematics or Girardi's own intrinsic scatter — neither concentration-
related, both requiring a genuinely different investigation than this
addendum line, not a further concentration refinement.
