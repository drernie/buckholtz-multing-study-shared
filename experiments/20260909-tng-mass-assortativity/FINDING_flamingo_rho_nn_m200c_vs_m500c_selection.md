# FINDING — direct rho_NN recompute, M200c-selection vs M500c-
# selection: N=1200 (definitive estimand) UNAFFECTED, N=50 shows a
# real but statistically ambiguous shift, entangling two effects the
# design cannot separate — genuinely inconclusive, not "confirmed
# concerning"

**Continues:** `CLAIM_flamingo_rho_nn_m200c_vs_m500c_selection.md`
(committed BEFORE the script ran) → `FINDING_flamingo_m500c_m200c_
overlap.md`'s own named next step (direct statistic recompute,
replacing the overlap proxy). **User-requested.**
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Result (real, live `hdfstream` data, same shared FLAMINGO pool as
## the overlap test)

```
     N  rho_NN(M200c-sel)  rho_NN(M500c-sel)    delta
    35             0.4607             0.4055  -0.0552
    50             0.3197             0.0826  -0.2371  <-- primary
  1200            -0.0206            -0.0238  -0.0032
```

`N=1200` `M200c`-selection value (`-0.0206`) sits within `0.0025` of
this branch's own independently-established definitive-estimand result
(`-0.0231`, real spatial block-jackknife `SE=0.0476`) — a genuine,
useful internal-consistency check on this script's own correctness.

## Independent skeptic review (Step 8a, context-blind) — every
## quantitative claim independently re-derived, with one further
## tightening on my own re-derivation (below)

1. **Is the `N=50` delta (`-0.2371`) real or noise (`WEAKENED`)?**
   The naive comparison (`delta/single-sample-SD = 1.64`) is WRONG in
   TWO ways that partially cancel: treating the two `74%`-overlapping
   samples as independent overstates `SE(delta)`'s reduction from
   correlation (pushes the honest `z` DOWN from `1.64` to `1.16` under
   pure independence-correction); but the single-sample analytic SD
   itself UNDERSTATES real spatial variance — this branch's own `N=
   1200` result showed a real block-jackknife `SE` `1.65x` larger than
   the naive analytic formula. **Independently re-deriving the
   skeptic's own composition of these two corrections together (not
   just quoted): inflating the analytic SD by the same `1.65x` factor,
   THEN applying the independence-based `sqrt(2)` scaling, gives
   `z=0.71`** — WEAKER than the skeptic's own stated `"~1.2-1.7"`
   range (itself explicitly `[ГИПОТЕЗА]`-tier, not a rigorous
   derivation). **The honest range spans roughly `z~0.7-1.6` depending
   on exactly how the two corrections are composed** — genuinely NOT
   robustly distinguishable from noise on THIS evidence alone. The
   correct fix (named, not run): a real spatial block-jackknife
   computed directly ON the delta itself (not composed from two
   separately-estimated single-sample SDs), which properly captures
   both the spatial variance inflation and the sample-overlap
   correlation simultaneously.
2. **Does this design isolate "selection" from "correlated-quantity
   definition" (`FALSIFIED` as a clean isolation test)?** Confirmed: a
   real, valid gap. The design only measured the two DIAGONAL cells of
   a `2x2` factorial (select-`M200c`/correlate-`M200c`; select-
   `M500c`/correlate-`M500c`) — NOT the two off-diagonal cells (select-
   `M200c`/correlate-`M500c`; select-`M500c`/correlate-`M200c`) that
   would separate "does WHICH halos matter" from "does WHICH mass
   values matter, holding halos fixed." The observed `delta` conflates
   both effects. Cheap fix (named, not run): compute the two missing
   cells with the SAME already-downloaded data.
3. **Is the `(overlap, |delta|)` pattern independent confirmation, or
   expected/near-tautological (`WEAKENED`)?** Plausible, directionally
   consistent, but NOT mathematically forced (low overlap does not
   deterministically imply a large delta — depends also on WHERE in
   log-mass the swapped halos sit and how NN topology reshuffles for
   the SHARED halos too, not just the `13` swapped ones). **The one
   genuinely useful, directionally clear result is `N=1200`**: delta
   (`-0.0032`) is `~15x` smaller than the real jackknife `SE`
   (`0.0476`) — independently re-confirmed exactly — a real,
   well-supported "the definitive estimand is not sensitive to this
   choice" statement.
4. **Most honest overall conclusion (`WEAKENED` on the "matters at
   small N" half; well-supported on the "doesn't matter at N=1200"
   half).** Breaking the two halves apart, per the skeptic's own
   framing (independently re-verified):
   - **"Does not matter at `N=1200`" — well-supported.** `15x` margin
     against the real jackknife SE; real internal-consistency check
     against an independently-established number. **This branch's own
     "definitive global estimand" is NOT threatened by the `M200c`-
     vs-`M500c` choice.**
   - **"Can matter substantially at small `N` (matching the TNG300/
     subcube saga's own `N~30-55` scale)" — OVERSTATED.** Rests on ONE
     data point (`N=50`) whose own significance is ambiguous (`z`
     roughly `0.7-1.6`, not the naive `1.64`) and whose origin is
     unresolved (selection effect vs. value effect, per item 2). `N=
     35` shows only a small shift (`-0.055`, comfortably inside any
     reasonable SE). **Generalizing from one ambiguous point to
     "small-`N` results in this branch are at risk" is not licensed by
     this test.**

**Response (Step 8a matrix): all four points accepted, with an
additional independent tightening on item 1 (the honest z-range is
`~0.7-1.6`, not the skeptic's own quoted `~1.2-1.7` — a real, if
modest, further downgrade of the "suggestive" framing, found by
literally re-composing the same two corrections the skeptic named).**

## What this DOES establish

- **The `N=1200` "definitive global estimand" is confirmed robust to
  the `M200c`-vs-`M500c` mass-convention choice** — a real,
  well-supported, positive result for this branch's own strongest
  existing number.
- **A real internal-consistency check**: this script's own `N=1200`
  `M200c`-selection result independently reproduces the already-
  established definitive-estimand value to within `0.0025` — confirms
  correct implementation.
- **A real, but genuinely AMBIGUOUS, hint (not a confirmed finding) at
  smaller `N`**: `N=50` shows a substantial raw shift, but its
  statistical significance is weak-to-moderate at best (honest
  `z~0.7-1.6`) and its MECHANISM (selection vs. value effect) is
  unresolved by this design.
- **Two concrete, cheap, named next steps if this specific
  sub-question is pursued further**: (a) fill the `2x2` factorial's
  missing off-diagonal cells; (b) a proper joint spatial block-
  jackknife computed directly on the delta.

## What this does NOT establish

1. Does NOT establish that the `M200c`-vs-`M500c` mismatch materially
   affects any SPECIFIC already-reported `rho_NN` result from the
   TNG300/subcube saga (those used different `N`, different
   simulations, and this test does not directly touch them).
2. Does NOT separate "selection effect" from "correlated-value effect"
   — genuinely open, per item 2.
3. Does NOT provide a rigorous significance level for the `N=50`
   shift — the honest range (`z~0.7-1.6`) spans "clearly noise" to
   "borderline" depending on assumptions not resolved here.
4. Not a claim about v82's own theory (`NO_AUTHOR_ERROR`).

## Status

**A real, honestly-scoped result: the branch's own strongest number
(the `N=1200` definitive estimand) is confirmed robust; the smaller-`N`
concern remains a genuine, unresolved, but NOT confirmed, open
question.** This is a natural stopping point for this specific
sub-investigation — the two named cheap follow-ups (factorial
completion, joint block-jackknife on delta) would sharpen the `N=50`
picture further but represent additional, not-yet-requested scope.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
