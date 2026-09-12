# FINDING — periodic-wrap dilution bias: NOT confirmed; the naive
# reading of "mean delta" was itself a measurement-of-the-wrong-
# quantity error, caught before being written up; open-boundary is
# not a clean reference either; the whole question stays open

**Continues:** `CLAIM_flamingo_subvolume_periodic_wrap_bias.md`
(committed BEFORE the script ran) → `FINDING_flamingo_subvolume_
replication.md`'s own Step 8a skeptic item 2. **User-requested.**
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Result (real, live `hdfstream` data, SAME 10 already-frozen
## `(cube_id, local_N)` pairs, periodic vs. open-boundary `rho_NN`)

```
Mean swap fraction (nn_idx differs periodic vs open): 17.7%
rho_NN periodic: mean=0.0145, SD=0.2069
rho_NN open:     mean=-0.0394, SD=0.2321
signed delta (open-periodic): mean=-0.0539, SD=0.0994

|rho_NN| >= 0.42: periodic 0/10, open 1/10 (cube 8: -0.27 -> -0.46)
```

## Independent skeptic review (Step 8a, context-blind) — the review
## caught a real error in MY OWN initial reading of the signed-mean
## number, not just a problem with the underlying design

Full text preserved in the session record. **Every quantitative claim
independently re-derived before use** — all confirmed to the third
decimal place (paired t-test on signed delta: `t=-1.71, p=0.12`, `95%`
CI `[-0.125, 0.017]`; amplitude test `|rho_p|-|rho_o|`:
`mean=-0.0067, t=-0.19, p=0.86`; exactly `5` of `10` cubes dilute,
`5` of `10` inflate; Wilcoxon signed-rank `W=12, p=0.13`).

1. **Is open-boundary a clean ground truth (`WEAKENED`)?**
   `medNN_open >= medNN_periodic` for every cube — a mathematical
   certainty, not a finding. But this cuts both ways: open-boundary
   treatment FORCES an edge halo whose true universe-scale neighbor
   lies just outside the sub-cube to report some farther, still-inside
   halo instead — its OWN distortion, not obviously smaller or more
   "correct" than periodic's wrap artifact. **Neither estimator has
   access to the true, pre-cut, whole-FLAMINGO nearest neighbor** — a
   real ground-truth comparison needs a THIRD reference (global NN
   computed across all `5000` halos before cutting into sub-cubes),
   not attempted here.
2. **Does the data support the claimed direction (periodic dilutes
   toward zero) (`FALSIFIED` — the single most important correction)?**
   **My own initial read used the SIGNED mean delta (`-0.0539`) as if
   it confirmed dilution — this measures the wrong quantity.** The
   dilution-toward-zero hypothesis is about `|rho|` shrinking, not
   about `rho` becoming more negative on average (a signed shift moves
   already-positive cubes toward inflation and already-negative cubes
   toward MORE dilution in the opposite sense — conflating two
   different effects). **The correctly-specified test, `|rho_
   periodic| - |rho_open|`, gives `mean=-0.0067, SD=0.114, t=-0.19,
   p=0.86`** — indistinguishable from zero, and exactly `5` of `10`
   cubes go each direction (dilution/inflation). **No systematic
   dilution effect is detectable in this data.**
3. **Cube 8's threshold crossing (`FALSIFIED` as evidence of a
   suppressed anomaly).** `-0.27` (periodic) `-> -0.46` (open) is a
   swing of `~0.19`, well within one sampling SE at `N=30`
   (`~1/sqrt(N-3)~=0.19`), on the cube with the HIGHEST swap fraction
   (`33.3%` — i.e. the LEAST stable comparison point among the `10`,
   not the most informative one). A single flip among `10` noisy
   estimates is the expected shape of noise, not a signal — a real
   suppressed anomaly would need cube 8 to cross the threshold under
   BOTH treatments, which it does not.
4. **Statistical power (`NEEDS-REAL-DATA`).** Signed-delta `95%` CI
   (`[-0.125, 0.017]`) includes zero; amplitude-delta `p=0.86` is a
   dead heat. Detecting a real `~0.05`-magnitude systematic bias with
   `SD~0.10` at `80%` power would need roughly `n~=34` sub-cubes —
   FLAMINGO's own `1000/302.6267` box only ever offers `27` non-
   overlapping slots at most, so even using every available sub-cube
   (not just the `10` that geometrically matched) would fall short.
5. **Most honest overall conclusion (`WEAKENED`, combination).** The
   periodic-wrap dilution bias hypothesis is **neither confirmed nor
   ruled out** by this test: (a) the amplitude test that directly
   addresses it shows nothing (`p=0.86`), (b) `n=10` is underpowered
   for the effect size in question, and (c) the comparator itself
   (open-boundary) carries its own, differently-shaped, unquantified
   distortion, so even a clean statistical result would not have
   settled the question against a genuine ground truth.

**Response (Step 8a matrix): all five points accepted. Item 2 is a
real, substantive correction — the skeptic caught that MY OWN initial
reading (the signed mean delta "confirms" dilution) measured the wrong
quantity; the skeptic's own arithmetic (`t`-tests, CI, Wilcoxon) was
then independently re-derived and confirmed exact before accepting the
verdict, per this session's own audit-verification discipline (an
agent's `[VERIFIED]` is this project's `[INFERRED]` until re-checked)
— catching an initial framing error is credited to the skeptic here,
not claimed as self-caught.**

## What this DOES establish

- **The naive "periodic dilutes toward zero" story is NOT supported
  by a proper amplitude-based test on this data** — a real,
  substantive negative result, not merely "inconclusive by default."
- **A genuinely new, portable methodological lesson**: a signed mean
  shift between two paired estimators does not, by itself, test a
  "shrinks toward zero" (dilution/attenuation) hypothesis — the
  correctly-specified test operates on `|value|`, not `value`. Using
  the wrong one can manufacture apparent support for a directional
  story that the data do not actually contain.
- **Open-boundary treatment is confirmed to have its own, different,
  unquantified bias** (forced farther-neighbor substitution for edge
  halos) — it is not a valid reference/ground-truth for this
  comparison, only a different approximation.
- **`17.7%` of halos in these sub-cubes get a different identified
  nearest neighbor depending on boundary treatment** — a real,
  substantial sensitivity of the whole sub-volume design to this
  choice, even though its effect on `rho_NN` itself is not
  statistically resolvable at this `n`.

## What this does NOT establish

1. Does NOT confirm the periodic-wrap dilution bias exists.
2. Does NOT rule out the periodic-wrap dilution bias — genuinely open,
   would need a real pre-cut global-NN reference and more sub-volumes
   than FLAMINGO's own `1000/302.6267` grid can supply.
3. Does NOT change `FINDING_flamingo_subvolume_replication.md`'s own
   INCONCLUSIVE verdict on TNG300's `rho_NN=-0.42` — if anything, this
   removes one candidate explanation ("the null-looking `0/10` result
   was probably a wrap artifact") without replacing it with a
   confirmed alternative.
4. Not a claim about v82's own theory (`NO_AUTHOR_ERROR`).

## Status

**Genuinely open, and the real value of this test is a caught
methodological error in how "dilution" was initially read, not a
resolved physics or bias question.** The concrete next step this test
itself names — a true pre-cut, whole-FLAMINGO global NN calculation as
the actual ground truth, compared against both periodic and open sub-
cube estimates — is real, would settle the ground-truth question
cleanly, and is not attempted here.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
