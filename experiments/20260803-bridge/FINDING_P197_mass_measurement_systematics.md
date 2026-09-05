# FINDING P197 — mass-measurement-method choice (caustic vs. Planck SZ)
# is real and large, but does not close `P196`'s own gap

**Date:** 2026-09-06
**Claim:** `CLAIM_P197_mass_measurement_systematics.md`
**Script:** `P197_mass_measurement_systematics.py`
**Continues:** `FINDING_P196_ADDENDUM2` (concentration structurally
ruled out); this file is candidate 1 of 2 named there.

## Result, reported honestly in two separate parts (per two rounds of
## Step 8a skeptic review)

**Endpoint 1 — direct mass comparison**: `M200c` (caustic) and `MSZ`
(Planck SZ), for the same 123 real clusters, disagree by a real, large,
**currently unexplained** factor: `mean(MSZ_equiv/M200c) = 2.50×`,
`75%` scatter, `r=0.56` (weak-to-moderate correlation for two proxies
of the same physical quantity). This is reported as an open finding in
its own right — not evidence for or against Rines et al. (2016)'s own
headline claim ("SZ mass estimates... are not significantly biased"),
which — per the second skeptic pass, `[VERIFIED-arXiv:1507.08289]` —
is about a *different* comparison (measured velocity dispersion vs. a
virial-scaling prediction from `M_SZ`), not a direct mass-ratio test.

**Endpoint 2 — the actual quantity of interest** (`ratio_2b`,
comparing Girardi's dynamical radius against the TJB-style
construction): substituting `MSZ` for `M200c` moves the mean ratio
from `1.4665` to `1.1710` — closer to `1.0`, but **still outside the
pre-registered MCID band `[0.95,1.05]`**. Per the pre-registered
criterion, this is not a resolution.

**Mechanical-explanation check** (added after the second skeptic pass):
the size of Endpoint 2's shift is consistent with simple mass-rescaling
arithmetic — `(mass_ratio)^(1/3) = 1.36` vs. the observed `ratio_2b`
shift of `1.25` — not a demonstrated independent physical convergence.
Using a larger mass (`MSZ_equiv`) mechanically shrinks `ratio_2b`
(since `ratio_2b ∝ 1/R178 ∝ 1/M^(1/3)`, per `FINDING_P196_ADDENDUM2`'s
own algebraic-cancellation finding) — most of the apparent improvement
is this arithmetic, not new information.

## Corrections applied (two rounds of Step 8a skeptic review, both
## real, both fixed)

1. **Round 1 (real bug, `CONFIRMED-REAL`)**: the first version of this
   file fed `MSZ` directly into `P196`'s own `Δ=200`-anchored NFW
   builder, without checking `MSZ`'s own overdensity convention.
   `[VERIFIED-arXiv:1507.08289]`, read directly this session, Rines et
   al. §II.2: "The Planck mass estimates are extracted from an
   aperture of `θ₅₀₀`... `r₅₀₀`" — `MSZ` is a real `Δ=500` mass. Fixed:
   a new, generalized root-finder
   (`solve_halo_matching_target_delta`), validated by two positive
   controls (exact reproduction of `P196`'s own `Δ=200` baseline; exact
   recovery of a synthetic `Δ=500` halo from its own true mass alone).
2. **Round 2 (real framing/interpretation issues, `CONFIRMED-REAL` on
   two of five probed items)**:
   - The script's own printed "sanity check" against Rines et al.'s
     "not significantly biased" claim was itself miscalibrated — that
     claim concerns a different comparison (velocity-dispersion
     consistency, not a direct mass ratio). Fixed: the message now
     states this explicitly, and the `2.50×` finding is reported as
     its own open question, not framed as contradicting Rines et al.
   - Endpoint 2's own improvement (`1.4665→1.1710`) was not
     independently validated as a *physical* convergence — the
     skeptic derived, and this file independently confirmed by
     computing both sides, that the shift is largely explained by
     pure `R∝M^(1/3)` mass-rescaling arithmetic. Fixed: added the
     explicit mechanical-explanation check, reported alongside the
     raw numbers rather than letting the "closer to 1.0" framing imply
     more than the data supports.
3. Two round-2 items (`Δ=500`-specific concentration bias risk;
   `2.50×`'s own astrophysical plausibility) were reported by the
   skeptic as `CONFIRMED-REAL` / `CANNOT-DETERMINE` limitations, not
   fixed — named explicitly in "What this does NOT establish" below,
   not smoothed over.

## What this settles and what it leaves open

**Settled**: mass-measurement-method choice is real and large — the
two real, independent, published mass estimates for the same clusters
disagree substantially (`2.50×`). This is **material** by the
pre-registered MCID (via the scatter branch), confirming candidate 1
is not a non-issue.

**Not settled — the honest, disciplined reading, not the optimistic
one**: `MSZ` does **not** close `P196`'s own gap. `ratio_2b=1.1710`
still fails the pre-registered band, and the movement it does show is
mostly arithmetic (mass-rescaling), not validated new physics. The
`2.50×` `M200c`-vs-`MSZ` disagreement is itself a real, striking,
**unexplained** finding that this file does not resolve — candidates
named but not tested: caustic-technique mass under-estimation,
Eddington bias inflating `MSZ` for low-significance SZ detections, or
`MSZ`'s own known hydrostatic-mass-bias calibration issues (a
different, well-documented systematic, orthogonal to the `Δ`-mismatch
already fixed).

## What this does NOT establish

1. Does not resolve why `M200c` and `MSZ` disagree by `2.5×` — no
   stratification by SZ detection significance or cluster mass was
   attempted (a concrete, named, not-yet-attempted next step if this
   specific sub-question is pursued further).
2. Does not establish that `Δ=500`-specific application of Duffy et
   al. (2008)'s `Δ=200`-calibrated concentration relation is free of
   its own systematic bias — the positive controls validate the
   `Δ`-conversion *arithmetic*, not whether the underlying `c(M,z)`
   model correctly describes SZ-selected cluster halos specifically
   (a real, named limitation from the second skeptic pass, not fixed).
3. Does not establish `MSZ`'s own accuracy relative to `M200c` — both
   are real, published, independent estimates; neither is preferred.
4. Does not close `P196`'s own residual — candidate 1 of 2 is now
   honestly resolved as "real effect, does not solve the problem,"
   narrowing rather than resolving the outstanding question.
5. Does not draft or send anything to TJB.
6. `NO_AUTHOR_ERROR`.

## Recommended, not authorized, next step

If this specific sub-question (why do `M200c` and `MSZ` disagree by
`2.5×`?) is worth pursuing further: stratify the `123`-cluster sample
by SZ detection significance (the catalog's own `YSZD2A` column) and
by mass, to check whether the large scatter concentrates in
low-significance/low-mass systems (Eddington bias) or is broad-based
(pointing more toward a caustic-mass or hydrostatic-bias systematic).
Not attempted here — a separate, real investigation, not a small
addendum to this file.
