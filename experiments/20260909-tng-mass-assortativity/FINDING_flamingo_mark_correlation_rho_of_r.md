# FINDING — mass-marked rho(r) on M500c-selected FLAMINGO clusters:
# no mass-assortativity signal detected across 5-150 Mpc at the
# best-powered scale (N=5000); N=200/N=1000 partially untestable, not
# partially null

**Date:** 2026-09-13
**Claim tested:** `CLAIM_flamingo_mark_correlation_rho_of_r.md`
**Script:** `flamingo_mark_correlation_rho_of_r.py`
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Result (raw output, real FLAMINGO data, live `hdfstream` download)

```
=== Positive control: cell-block synthetic marks on REAL N=1000 positions (cell=50.0 Mpc) ===
   r_mpc       dd    rho(r)  null_mean  null_std       z   p_emp
     8.8       10    0.9712     0.0148    0.3446    2.78   0.000
    11.1       12    0.8183    -0.0056    0.2945    2.80   0.000
    13.9       12    0.6266     0.0056    0.3044    2.04   0.040
    17.4       33    0.6073     0.0095    0.1764    3.39   0.000
    21.8       38    0.5816    -0.0115    0.1784    3.33   0.000
    27.4       76    0.3309     0.0081    0.1156    2.79   0.005
    34.4      105    0.2526    -0.0067    0.0958    2.71   0.010
    43.1      163    0.0991     0.0023    0.0729    1.33   0.215
    54.1      293   -0.0300     0.0013    0.0625   -0.50   0.595
    67.8      510   -0.1474    -0.0034    0.0434   -3.32   0.000
    85.1      924   -0.0467    -0.0053    0.0318   -1.30   0.130
   106.8     1783    0.0353    -0.0018    0.0239    1.55   0.125
   133.9     3572   -0.0280    -0.0008    0.0174   -1.57   0.110

=== M500c-selected FLAMINGO clusters, N=200 ===
   r_mpc       dd    rho(r)       z   p_emp
    54.1       12   -0.3203   -1.06   0.245
    67.8       28   -0.2979   -1.44   0.135
    85.1       36   -0.2074   -1.25   0.285
   106.8       65   -0.0663   -0.54   0.575
   133.9      147   -0.0795   -0.99   0.360
   (10 of 15 bins, ALL r<54 Mpc, untestable: dd<10)

=== M500c-selected FLAMINGO clusters, N=1000 ===
   r_mpc       dd    rho(r)       z   p_emp
     8.8       10    0.0281    0.04   0.945
    11.1       12    0.1296    0.47   0.650
    13.9       12   -0.3052   -1.02   0.365
    17.4       33    0.0471    0.17   0.815
    21.8       38    0.0942    0.52   0.555
    27.4       76   -0.0118   -0.11   0.890
    34.4      105   -0.0728   -0.88   0.490
    43.1      163    0.0109    0.14   0.950
    54.1      293    0.0456    0.67   0.410
    67.8      510    0.0004   -0.06   1.000
    85.1      924    0.0020    0.10   0.945
   106.8     1783   -0.0314   -1.25   0.185
   133.9     3572   -0.0041   -0.19   0.835
   (2 of 15 bins, r=5.6/7.0 Mpc, untestable: dd<10)

=== M500c-selected FLAMINGO clusters, N=5000 (all 15 bins testable) ===
   r_mpc       dd    rho(r)       z   p_emp
     5.6       49   -0.1134   -0.80   0.425
     7.0       95   -0.1189   -1.19   0.290
     8.8      179   -0.0477   -0.62   0.530
    11.1      236    0.1513    2.35   0.015
    13.9      371   -0.0395   -0.77   0.445
    17.4      532    0.0151    0.17   0.730
    21.8      740   -0.0258   -0.86   0.565
    27.4     1255    0.0345    1.20   0.225
    34.4     1992    0.0293    1.34   0.175
    43.1     3674    0.0095    0.61   0.560
    54.1     6413    0.0009   -0.09   0.920
    67.8    12241    0.0081    0.84   0.390
    85.1    23253    0.0045    0.76   0.525
   106.8    44611   -0.0032   -0.53   0.525
   133.9    88947    0.0018    0.62   0.535
```

## Independent verification (before dispatching the skeptic)

Counted testable bins (`dd>=10`) directly from the raw output: `5`
(`N=200`) + `13` (`N=1000`) + `15` (`N=5000`) = `33` total. Under naive
independence, expected false positives at `p<0.05` = `33*0.05=1.65`.
Observed: exactly `1` (`N=5000`, `r=11.1` Mpc, `p_emp=0.015`) — BELOW
the expected noise-floor count, not above it.

## Independent skeptic review (Step 8a, context-blind — claim + code +
## raw output ONLY, no reasoning chain)

**Verdict: WEAKENED.**

(a) **Positive control — CONFIRMED functionally correct, but reveals a
real per-bin noise floor that matters for interpretation.** The strong
signal at small `r` (`rho=0.97` to `0.25`, `p_emp<=0.04`, `r=8.8-34.4`
Mpc, all within the planted `50` Mpc cell scale) is correctly detected.
The significant NEGATIVE dip at `r=67.8` Mpc (`z=-3.32`) is NOT a
pipeline bug — with only `~1000` halos across `8000` candidate `50`
Mpc cells, the cell-block construction is ONE realization of a
few-hundred-dimensional random draw, and `67.8` Mpc sits near the
cell-diagonal crossover where a single unlucky draw can produce a real
(in-this-realization) anti-correlation. **The consequential point**:
this demonstrates the pipeline's own per-bin noise floor under pure RNG
is `|z|~3`, IN A BIN WHERE THE INJECTED MECHANISM IS NOT EVEN ACTIVE —
directly undermining any reading of the real data's `z=2.35` result as
signal, since it sits inside a noise floor the pipeline itself
demonstrated on the SAME run.

(b) **Multiple comparisons — CONFIRMED, matches independent count.**
`1` of `33` testable bins nominally significant, below the naive
`1.65`-false-positive expectation. No pre-registration singled out
`(N=5000, r=11.1)` — the claim's own falsifiable prediction was about
SHAPE across all bins, so treating this one bin as anything other than
noise would be post-hoc bin selection, exactly the trap the claim's own
design was built to avoid.

(c) **Cross-bin correlation — makes the null reading STRONGER.** Shared
-halo structure across bins means a genuine physical signal would
plausibly show up across ADJACENT bins, not one isolated bin. The
`r=11.1` excursion's neighbors (`r=8.8`: `z=-0.62`; `r=13.9`: `z=-0.77`)
are null-consistent and slightly NEGATIVE — the opposite direction,
not a coherent trend. This is the pattern expected from noise, not from
a physical assortativity signal that "turns on" in one narrow bin.

(d) **Overall conclusion — fair for `N=5000`, was overreaching as
originally scoped for `N=200`/`N=1000`, corrected below.** `10` of `15`
bins at `N=200` (ALL of `r<54` Mpc — precisely where an assortativity
signal would most plausibly appear) and `2` of `15` bins at `N=1000`
were UNTESTABLE (`dd<10`), not tested-and-null. The corrected framing
(applied in this write-up): the null result is well-supported ACROSS
THE FULL RANGE only at `N=5000`; at `N=200`/`N=1000` it applies only to
the bins actually reported.

(e) **No implementation bugs.** `rng.permutation(marks)` correctly
shuffles marks only, positions/pairing untouched. `MIN_PAIRS_FOR_RHO`
gates observed and null identically (verified — no asymmetric
inclusion). Minor, non-consequential notes: `p_emp=0.000` is a
truncation at the `1/N_SHUFFLE=0.005` resolution floor, not a true
zero (standard convention `(1+count)/(N+1)` would report `>=0.005`
instead); `N_SHUFFLE=200` gives limited null-distribution resolution,
immaterial here since no real result is near a decision boundary.

## Response to skeptic (per Step 8a Response Matrix)

- **(a) Accepted, stated explicitly** — the positive control's own
  `|z|=3.32` noise-floor excursion is now the primary reason the
  `N=5000` `r=11.1` result is read as noise, not a secondary footnote.
- **(b) CONFIRMED-REAL** — promoted unchanged, matches independent
  pre-skeptic count exactly.
- **(c) CONFIRMED-REAL, accepted as reinforcing** — added to the final
  characterization below.
- **(d) Accepted, corrected** — "no signal detected at N=200/N=1000"
  is retracted as originally worded; replaced with the explicit
  untestable-bin accounting in the Result table above and the
  conclusion below.
- **(e) Noted, no action required** — cosmetic only, no conclusion
  depends on the `p_emp` truncation convention.

## What this DOES establish

- At `N=5000` (the best-powered `M500c`-selected pool, all `15` bins
  from `5` to `150` Mpc testable), `rho(r)` shows NO robust mass-
  assortativity signal anywhere in the range — the one nominally-
  significant bin (`r=11.1`, `p=0.015`) is fully consistent with the
  multiple-comparisons noise floor (`1` of `33` tests, below the
  expected `1.65`), has null-consistent (and oppositely-signed)
  neighboring bins, and sits within the pipeline's own demonstrated
  `|z|~3` per-bin RNG noise floor (from the positive control's own
  off-target excursion).
- This is a genuinely new, independent-methodology confirmation of the
  branch's already-established null (`FINDING_flamingo_addendum_
  jackknife_band_closure.md`'s `N=1200` `rho_NN~=0`) — now on the
  SOURCE-FAITHFUL `M500c` convention (per `docs/162` item 3), across
  the FULL `5-150` Mpc separation range (not one nearest-neighbor
  distance or one fixed band), with a literature-standard mark-
  correlation-function design and a validated permutation-based
  significance test (positive control confirmed the pipeline correctly
  detects a real, comparably-sized planted signal when one exists).
- The pipeline itself (per-bin Pearson on all-pairs, mark-shuffle
  permutation null, cell-block positive control) is validated and
  reusable for any future mass-marked 2PCF-style work on this data.

## What this does NOT establish

- **Does NOT** establish a null result at `N=200` for `r<54` Mpc or at
  `N=1000` for `r<8.8` Mpc — those bins had too few pairs to test
  (`dd<10`), they are UNTESTED, not null. This is a real, disclosed
  distinction (per the skeptic's own strongest objection), not smoothed
  over.
- **Does NOT** rule out mass-assortativity structure outside the tested
  `5-150` Mpc range (e.g. very small scales below the resolution of
  this binning, or very large scales beyond `150` Mpc).
- **Does NOT** resolve richness vs. mass-rank as proxies — inherited
  limitation from the prior 2PCF estimand.
- **Does NOT** validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`).
- **Does NOT** close `docs/162` item 9's remaining shape-mismatch
  caveat (`gamma` systematically steeper than the cited literature,
  per `FINDING_flamingo_2pcf_m500c_estimand.md`) — a separate, still-
  open question about the underlying spatial clustering, not the mass-
  marking generalization built here.

## Status

The mass-marked generalization named as the next step in `FINDING_
flamingo_2pcf_m500c_estimand.md` is now built, run, and skeptic-
reviewed. At the best-powered scale (`N=5000`), it finds NO mass-
assortativity signal anywhere in `5-150` Mpc — a well-powered,
methodologically upgraded (source-faithful `M500c`, full-range,
literature-standard, permutation-tested) confirmation of this branch's
already-established null result. This closes the direct P158-
motivating question (does real mass-assortativity structure exist
between paired nodes) on the strongest design this branch has built,
while leaving `docs/162` item 9's separate shape-mismatch caveat open.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
