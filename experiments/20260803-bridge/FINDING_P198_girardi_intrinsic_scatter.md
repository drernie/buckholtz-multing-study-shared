# FINDING P198 — Girardi's own internal `R_c` inconsistency shifts the
# ratio by a real ~14%, but this is an extrapolation-bound estimate,
# not a clean sensitivity test, and does not close `P196`'s gap

**Date:** 2026-09-06
**Claim:** `CLAIM_P198_girardi_intrinsic_scatter.md`
**Script:** `P198_girardi_intrinsic_scatter.py`
**Continues:** `FINDING_P197` (candidate 1, mass-measurement
systematics, real but insufficient); this file is candidate 2 of 2.

## Result

**Positive controls pass**, including a cross-check added after the
first run flagged a real, if small, discrepancy: the literal published
coefficient (`0.002`) reproduces `P196`'s own reported baseline
(`1.4665`) to `<0.001%`; the self-consistency solver's own re-derived
coefficient (`0.00197`) is within the pre-registered `<5%` tolerance of
`0.002` but not exact — the script applies the solver's own `R_c`-
sensitivity *ratio* multiplicatively to the literal `0.002`, not the
solver's own approximate re-derivation, precisely to avoid propagating
that small residual mismatch into the comparison (fixed mid-analysis,
before any headline number was reported).

**Endpoint 1**: substituting Girardi et al.'s own improved `R_c=0.05`
(`§4.3`, their own centering method, same 1998 paper) for the `R_c=0.17`
(`G95`) their published Eq. 11 actually used, in the same Eq. 9+10
self-consistency solve, shifts the implied coefficient by a real
factor of `0.8583` (`~14%` smaller).

**Endpoint 2**: applied to `P196`'s own pipeline, this moves the mean
`ratio_2b` from `1.4665` (published) to `1.2587` — real movement, but
**still outside the pre-registered MCID band `[0.95,1.05]`**. Scatter
is unchanged to 4 decimal places (`11.1462%` both rows) — **exactly**,
not approximately, because `ratio_2b` is linear in the `R_vir`
coefficient (independently re-verified below).

## Two real caveats found by a Step 8a skeptic pass, both accepted and
## reflected in this write-up (not silently absorbed into the headline
## number)

1. **The `R_c` substitution is an extrapolation, not a clean
   sensitivity test — `[independently re-verified]`.** Eq. 10's own
   rational-function coefficients (`1.193, 0.032, 0.107`) were fit *by
   G95* to G95's own galaxy-distribution data, using G95's own
   (larger) `R_c` to normalize the aperture ratio `x=A/R_c`. At the
   published `R_c=0.17`, the self-consistent `R_vir≈2 h⁻¹Mpc` gives
   `x≈12`; at the substituted `R_c=0.05`, the SAME `R_vir` gives
   `x≈40` — roughly `3.3×` further out than where the formula was
   ever calibrated. This is a real, substantive caveat, not a
   technicality: the `~14%` shift should be read as **what a specific,
   fairly aggressive extrapolation of Girardi's own formula suggests**,
   not as a validated, physically clean re-derivation. `CLAIM_P198`'s
   own stated caveat (that Eq. 10 was fit with G95's own `R_c`
   convention) already flagged this in general terms; the skeptic's
   contribution is the specific, quantified `x≈12→40` extrapolation
   distance.
2. **Endpoint 2's `123`-cluster computation is arithmetically
   predetermined by Endpoint 1's own coefficient ratio —
   `[independently re-verified by hand]`.** Since `_step2a` (`P196`'s
   own exact `z`-reference correction) is a pure multiplicative
   rescaling and `R178` does not depend on the `R_vir` coefficient at
   all, `ratio_2b` is *exactly* linear in the coefficient:
   `1.4665 × 0.8583 = 1.2589`, matching the reported `1.2587` to
   rounding. Running the full pipeline on all 123 clusters is a valid
   confirmation that no per-cluster, non-linear effect breaks this
   proportionality (a real, if narrow, check) — but it is not
   independent new information beyond Endpoint 1's own single ratio,
   and this write-up does not present it as such.

## What this settles and what it leaves open

**Settled**: Girardi et al.'s own internal `R_c` inconsistency, taken
at face value and extrapolated through their own published formula,
produces a real, quantifiable, `~14%` shift toward `1.0` — smaller
than mass-measurement systematics' own effect (`P197`, `~9%`
absolute-ratio movement with much larger scatter) but in the same
direction and of comparable order. **Neither candidate, alone, closes
`P196`'s own gap.**

**Left open**: whether the `x≈40` extrapolation itself is trustworthy
— Girardi et al. never re-fit Eq. 10's own functional form using their
own improved `R_c` convention, so this file's `~14%` number is best
read as an **upper-bound-flavored estimate under one specific,
aggressive extrapolation assumption**, not a validated correction. A
cheaper, more conservative check named by the skeptic but not run here
would evaluate the solver at an intermediate `R_c` (e.g. `0.10`) to
see whether the coefficient-vs-`R_c` relationship stays smooth/linear
approaching the extrapolated regime, or breaks down — not attempted in
this file.

## What this does NOT establish

1. Does not validate the `R_c=0.05` extrapolation as physically correct
   — flagged explicitly as an extrapolation ~3.3× beyond Eq. 10's own
   calibration range, not a clean, isolated sensitivity test.
2. Does not establish Endpoint 2's `123`-cluster run as independent
   confirmation beyond Endpoint 1's own coefficient ratio — the exact
   linearity is now understood and stated, not left as an unexplained
   (and potentially concerning) coincidence.
3. Does not close `P196`'s own residual — candidate 2 of 2 is now
   honestly resolved, same pattern as candidate 1: a real, partial,
   quantifiable effect, insufficient alone.
4. Does not draft or send anything to TJB.
5. `NO_AUTHOR_ERROR` — entirely about this project's own reconstruction
   and a re-reading of Girardi et al.'s own published paper, never a
   claim about MULTING, v82, or Dr. Buckholtz's own work.

## Where this leaves the whole `P196`→`P198` residual investigation

Across `P196`, `ADDENDUM`, `ADDENDUM2`, `P197`, and `P198`, every
named, testable candidate for the `1.47×` residual has now been
checked, honestly, with real data and real skeptic review:

| Candidate | Verdict |
|---|---|
| Concentration scatter (`ADDENDUM`) | Ruled out — negligible effect |
| Concentration source, real vs. simulated (`ADDENDUM2`) | Ruled out — structurally, `R500` cancels algebraically |
| Mass-measurement method, caustic vs. SZ (`P197`) | Real (`2.5×` mass disagreement, itself unexplained), but downstream shift insufficient and mostly arithmetic |
| Girardi's own `R_c` inconsistency (`P198`) | Real (`~14%` shift), but an extrapolation-bound estimate, insufficient alone |

**No single tested mechanism closes the gap.** The two partial,
real contributors found (`P197`'s mass-measurement effect and `P198`'s
`R_c` extrapolation) point in the same direction and are of comparable
order — worth noting as a real, if incomplete, pattern — but combining
them was not attempted here (would itself need care: `P197`'s `MSZ`
substitution and `P198`'s coefficient substitution are independent
axes and could, in principle, be applied together in a future step,
not attempted in this file). The residual remains real and
substantially unexplained.
