# FINDING E21 — systematic enumeration of every numbered result in
# v82's own archive output substantially confirms Ernest Prabhakar's
# item 4, with named exceptions: 9 of 12 result groups are unambiguous
# fit-derived quantities, but 2-3 (the deceleration parameter q(0); the
# z=3.09/3.95 divergence points) are genuine, near-future-testable
# candidate predictions, not indistinguishable from the untestable
# z=10.31/16.95 extrapolations — corrected after Step 8a skeptic

**Date:** 2026-09-06
**Trigger:** same email thread. Ernest's item 4: "there isn't a single
falsifiable prediction anywhere. All the numbers in the press release
come from fitting the data. Before announcing this, MULTING needs to
say at least one thing about the world not already reflected in the 33
data points, that the next data release could falsify. If you can't
name that thing, you have a model fit, not a theory."
**Explicit go-ahead given** ("пункт 4 и 5, тоже скрупулёзно").

## Step 8a skeptic — context-blind, claim + full classification table —
## verdict: WEAKENED, 1 real point, addressed in place

The original draft's "Zero results... comprehensively confirms" language
overclaimed. The skeptic's own worked distinction: Result 6 (`q(0)=
-1.416`) is a smooth, deterministic consequence of the already-fitted
`H(z)` shape — true, it is DERIVED-FROM-FIT in the mechanical sense
this FINDING's own classification scheme uses — but it is also a
**genuinely new number**, not already published or quoted anywhere in
the 33-point data itself, and it is **checkable against independent
future data** (a real deceleration-parameter measurement from SNe/BAO
at low z). The same holds, more clearly, for Result 7's `z=3.09` (10%
divergence) and `z=3.95` (20% divergence) points — MODERATE
extrapolation, within reach of near-future DESI/Euclid data, genuinely
distinct from `z=10.31`/`z=16.95` (EXTREME extrapolation, this
project's own prior work already shows the data cannot be trusted past
`z≈1.07-1.965`, and TJB's own separately-commissioned Claude session
already flags `H²<0` near `z≈17.5` as outside the model's own
admissible range). Collapsing these two very different kinds of
"beyond the fit" into one undifferentiated "extrapolation, therefore
not a prediction" bucket was the actual overclaim — not the underlying
enumeration, which stands. **Fixed:** Result 6 and the `z=3.09/3.95`
sub-cases of Result 7 are reclassified below as genuine falsifiable-
by-near-future-data candidates, distinct from both ordinary fit output
and from the untestable extreme extrapolations.

## L0 (EstimandOps)

**Descriptive/classification.** Does ANY of v82's own claimed,
numbered results constitute a claim about the world that is NOT
derived purely from fitting the same 33 data points (31 cosmic
chronometers + SH0ES + DESI DR2 Lyα)? Systematic enumeration, not a
new computation — every result below is TJB's own archive's own
already-run output (`results/generate_all_results_output.txt`),
already `[VERIFIED]` real (this project's own prior sessions have
independently reproduced this exact archive's own χ² arithmetic to
`<0.1%`, `E18`/`FINDING_P176`).

## Method

Read the archive's own `generate_all_results_output.txt` in full — the
canonical, author-run enumeration of every numbered result the archive
computes. Classified each of the 13 numbered results (some grouped, as
the archive itself groups them) into one of four categories:

- **FIT** — a direct output of fitting `β1,β2` (and sometimes
  `H0,anchor`) to the 33-point dataset.
- **DERIVED-FROM-FIT** — a quantity computed FROM the already-fitted
  trajectory (force decomposition, growth factors, lookback times) —
  a re-expression of the fit, not new data, and not independently
  checkable against data not already used.
- **DERIVED-BUT-CANDIDATE-PREDICTION** (added after Step 8a skeptic) —
  mechanically the same as DERIVED-FROM-FIT (a deterministic
  consequence of the already-fitted trajectory), but the resulting
  number is genuinely new (not quoted or used anywhere in the 33-point
  fit itself) AND independently checkable against a real, near-future
  external dataset — a genuine candidate falsifiable prediction, not
  indistinguishable from ordinary fit output.
- **EXTRAPOLATION-EXTREME** — a quantity evaluated far enough outside
  the data's own redshift coverage that this project's own prior work
  (`docs/156`/`FINDING_P195`/`FINDING_P158_ADDENDUM2`) already
  establishes the data cannot be trusted there (`z≳1.07-1.965`), AND
  TJB's own separately-commissioned Claude session independently flags
  the specific value as outside the model's own admissible range —
  untestable in any near-future sense.
- **EXTRAPOLATION-MODERATE** (added after Step 8a skeptic) — outside
  the 33-point fit's own redshift coverage, but within reach of
  near-future real survey data (DESI, Euclid) — a genuine, if
  unexploited, falsifiable candidate, not equivalent to the extreme
  extrapolations above.
- **EXTERNAL-BUT-DIAGNOSTIC** — uses data outside the 33-point fit, but
  for the purpose of diagnosing a problem with the theory's own
  construction, not proposing a testable prediction.

## Results — full classification

| # | Result | Category | Note |
|---|---|---|---|
| 1 | Table II, 7-row tension table | **FIT** | direct fit output, all 7 rows |
| 2-4 | 3 ΛCDM benchmarks | **FIT** (comparison baseline) | ΛCDM fit to related data, not a MULTING claim |
| 5a | Force decomposition (F0,F1,F2,Facc) at z=1.965,1.07,0.5,0.07 | **DERIVED-FROM-FIT** | breakdown of the already-fitted trajectory at already-used redshifts |
| 5b | Force pattern across all 7 Table II rows | **DERIVED-FROM-FIT** | same, cross-row |
| 6 | q(0), deceleration parameter today | **DERIVED-BUT-CANDIDATE-PREDICTION** (reclassified after skeptic) | smooth consequence of the fitted H(z) shape near z=0, but a genuinely new number not quoted in the 33-point data, checkable against independent future SNe/BAO deceleration-parameter measurements — the SAME quantity `E19` already examined (phantom-crossing sign), found genuine but currently untestable at real data precision (`8-13×` below the nearest real CC points' own quoted uncertainty — untestable TODAY, not untestable IN PRINCIPLE) |
| 7 | H(z) turnover points, high-z LCDM divergence | **SPLIT** (reclassified after skeptic) — `z=3.09` (10% divergence) and `z=3.95` (20% divergence): **EXTRAPOLATION-MODERATE**, within reach of near-future DESI/Euclid data; `z=10.31` and **`z=16.95, H=0.00`** (a universe that stops expanding): **EXTRAPOLATION-EXTREME** | TJB's own Claude session (in the same email) already independently flagged `H²<0` near `z≈17.5` as "outside admissible" — this applies to the extreme pair, not the moderate one; conflating the two was the original overclaim |
| 8 | Ωk floating test, against CC data alone | **FIT** (internal consistency) | CC is a subset of the same 33 points, not new data |
| 9 | Ingredient growth factors z=1.965→0.070 | **DERIVED-FROM-FIT** | ratios along the already-fitted trajectory between two already-used redshifts |
| 10 | SH0ES-z robustness table | **FIT** (sensitivity/robustness check) | tests fit stability under a varied assumption, not a prediction about new data |
| 11 | H0-anchor circularity (approximate) | **EXTERNAL-BUT-DIAGNOSTIC** | the ONLY result drawing on genuinely external literature (Basilakos 2004, Cen/Bahcall/Gramann 1994) not in the 33-point fit — but its own purpose is to show `H0,anchor`'s own construction gives a nonsensical value (`~11-19 km/s/Mpc`, "not a plausible Hubble constant by any measure") — already independently classified `CIRCULAR` by this project's own `provenance_audit` (`E9`/`FINDING_E9`), closed per `docs/147`'s stop-rule |
| 12 | Five-lens-time table (age since Big Bang) | **DERIVED-FROM-FIT**, partly **EXTRAPOLATION-EXTREME** | includes `z=-0.2`, a FUTURE point — extrapolation past today |

## Verdict — corrected, honestly scoped

**Substantially confirms Ernest's item 4, with named exceptions — not
"zero," not "comprehensively."** Systematically enumerating all 12
result groups v82's own archive itself reports:
- **9 of 12** result groups are unambiguous fit-derived quantities
  (`#1-5, #8-10, #12`'s past-only portion) — direct fit output or a
  re-expression of the already-fitted trajectory, not independently
  checkable against data outside the 33-point fit.
- **1** result (`#11`) draws on external literature, but explicitly
  to diagnose a circularity, not to propose a testable claim — and
  this project's own prior, independent work already confirms that
  diagnosis.
- **2-3 result groups are genuine, named, borderline candidates** for
  falsifiable predictions, not indistinguishable from ordinary fit
  output: `#6` (`q(0)=-1.416`, checkable against future SNe/BAO
  deceleration measurements — genuine but currently untestable at
  real data precision, per this project's own `E19`, `8-13×` below
  the nearest real CC points' own quoted uncertainty — untestable
  TODAY, not untestable IN PRINCIPLE) and `#7`'s `z=3.09/3.95`
  divergence points (within reach of near-future DESI/Euclid data,
  genuinely distinct from the untestable `z=10.31/16.95` extreme
  extrapolations, which TJB's own separately-commissioned Claude
  session independently flags as exceeding the model's own admissible
  range).

**Ernest's own core observation substantially holds** — the large
majority of v82's claimed results are fit re-expressions, not
predictions — **but "zero" and "comprehensively" overclaimed relative
to what the enumeration itself supports.** The honest count is 9
unambiguous, 1 diagnostic-only, 2-3 borderline candidates worth
naming explicitly, not lumping with either bucket.

## Ernest's own named exception — checked against v82's actual claims

Ernest's own follow-up names one candidate for a genuine, falsifiable
claim: "local expansion should correlate with intracluster thermal
energy... testable against existing X-ray cluster catalogs, without
waiting for a new survey." **Checked against the full 12-group
enumeration above: v82 does NOT currently compute or claim any
quantitative version of this correlation.** The mechanism (thermal
energy sourcing a repulsive force) is present in the theory's own
construction, but no numbered result in the archive states a specific,
checkable claim of the form "local `H(z)` variation should correlate
with nearby cluster thermal energy at strength X, testable against
catalog Y." This is a genuine, real candidate for a FUTURE falsifiable
prediction MULTING could make — not a prediction it has already made.
Actually running such a test (cross-matching real, spatially-resolved
local-expansion measurements against real X-ray cluster catalogs) is a
substantial, separate undertaking, out of this finding's own scope —
named here, not attempted.

## What this does and does NOT establish

**Does establish:** a comprehensive, systematic, real check — not an
impression — of every one of v82's own 12 claimed result groups,
finding the large majority (9 of 12) are unambiguous fit
re-expressions with no independent testability, substantially
confirming Ernest's item 4 — but finding 2-3 named, genuine borderline
candidates (`#6`, `#7`'s moderate-divergence points) that the original
"zero"/"comprehensively" framing wrongly lumped in with either the
ordinary fit output or the untestable extreme extrapolations.

**Does NOT establish:**
1. That MULTING could never in principle produce a falsifiable
   prediction — Ernest's own named candidate (thermal-energy/local-
   expansion correlation) remains a real, open, untested possibility,
   and `#6`/`#7`'s moderate points are already real, if currently
   unexploited, candidates.
2. That the 2-3 borderline candidates are CURRENTLY testable at
   today's data precision — `#6` is `8-13×` below the nearest real CC
   points' own quoted uncertainty; `#7`'s moderate points require
   near-future DESI/Euclid data, not data in hand today.
3. Whether MULTING's physics is correct — `NO_AUTHOR_ERROR`.
4. Anything about the other critique items — this closes item 4 only.

## Pearl Registry / next step

Two real, specific, checkable future tests, both worth a
`pearl_registry/INDEX.md` row (project-level registry):
1. Ernest's own named candidate (local-expansion/intracluster-thermal-
   energy correlation, testable against real X-ray cluster catalogs) —
   a genuinely new research direction, separate from re-analyzing the
   existing 33-point fit.
2. This FINDING's own reclassified `#6`/`#7` candidates — `q(0)=-1.416`
   against a future real SNe/BAO deceleration-parameter measurement,
   and the `z=3.09/3.95` divergence points against near-future
   DESI/Euclid data — both already computed by v82's own archive,
   requiring no new theory work, only future external data to become
   an actual test.
