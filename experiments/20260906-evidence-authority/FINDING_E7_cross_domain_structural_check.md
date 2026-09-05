# FINDING E7 — the same failure mode outside cosmology: one strong
# structural match (LLM-as-judge), two partial ones, and an honest
# statement of where the analogy breaks

**Date:** 2026-09-06
**Continues:** `E1`-`E6`. Executes option 3 ("carry the lens into other
fields"), explicit go-ahead given.

**Discipline applied:** `/cross-domain`'s own standard — *structural
isomorphism, not metaphor*. Each candidate below is checked against the
cosmology cases on mechanism, and the ones that only *sound* similar
are marked as such rather than counted.

## The cosmology structure being matched

From `E2`/`E5`/`E6`, stated mechanically so it can be tested elsewhere:

> **A quantity `X` is measured in order to test model `M`. The
> measurement pipeline for `X` already used `M` (or something derived
> from `M`) at some step — calibration, background subtraction,
> processing model, or sample selection. The dependence is real,
> often quantified by the field itself, and usually absent from the
> quoted uncertainty on `X`.**

Two sub-shapes appeared in cosmology:
- **(a) processing-model dependence** — same raw data, different
  processing model, different `X` (CC/SPS: `+6.8%`; SNe light-curve
  fitters).
- **(b) circular calibration** — `X`'s extraction required assuming
  the answer (`H₀,anchor` via peculiar velocities; BAO's ruler length
  from early-universe physics).

## Match 1 — STRONG: LLM-as-a-judge preference leakage (shape b)

`[VERIFIED-arXiv:2502.01534]` Li et al. (2025), *"Preference Leakage: A
Contamination Problem in LLM-as-a-judge"* — the judge model and the
model (or synthetic data) being judged share a lineage, so the
evaluation is not independent of the thing evaluated.

**Why this is a real isomorphism, not a resemblance:** it has the same
mechanism as `E2`'s `H₀,anchor` case, step for step. The evaluation
instrument was itself produced using the thing under evaluation; the
resulting number looks like an independent measurement and is not; and
the dependence is invisible in the reported score. Substituting terms:
*peculiar-velocity survey → judge model*, *assumed `H₀` → shared
lineage with the generator*, *derived `H₀,anchor` → win-rate*.

## Match 2 — PARTIAL: benchmark data contamination (shape a', not a)

`[VERIFIED-arXiv:2310.18018]` Sainz et al. (2023), *"NLP Evaluation in
trouble"* — "the worst kind of data contamination happens when an LLM
is trained on the test split of a benchmark."
`[VERIFIED-arXiv:2404.10457]` Bushuiev et al. (2024), *"Revealing data
leakage in protein interaction benchmarks"* — the same in computational
biology, which extends the pattern beyond one field.

**Where the analogy holds:** a number presented as an independent
measurement of capability is partly a measurement of overlap between
train and test, and the reported score does not carry that.

**Where it breaks, stated plainly:** contamination is a *sample*
problem (the wrong rows are on both sides of a split); the cosmology
cases are a *model* problem (the processing assumed the theory).
Removing contaminated rows fixes the ML case; no row removal fixes the
CC/SPS case, because the dependence is in the analysis model, not the
sample. **Counting this as the "same" failure would be exactly the
loose-analogy move `/cross-domain` warns against** — it is a cousin,
not a twin, and any write-up must say so.

## Match 3 — WEAK, and recorded as such: genome annotation circularity

The intended third example — annotation pipelines trained on
predictions from earlier annotation pipelines, propagating an original
model's assumptions into what looks like accumulated evidence — was
**not** substantiated by a real search this session. The genomics
queries returned tooling and database papers, not the circularity
claim. `SOURCE_NOT_FOUND` for the specific claim; **it is not used as
an example**, and is recorded here only so a later attempt knows this
search was already tried and with what query shape.

## What this establishes

**The pattern is not cosmology-specific, and one match is exact.** The
LLM-as-judge case shares the full mechanism of `E2`'s circular
calibration, in a field with no shared vocabulary, method, or
community — which is what makes it evidence of a general structure
rather than a coincidence of phrasing. That single strong match plus
one honest partial is a more defensible cross-domain claim than three
loose ones would be.

**It also supplies a portable name for the two-field extension of
`E6`:** every field seems to develop its own vocabulary for *avoided*
(model-independent, cosmology-independent, held-out, blind) and to
under-specify *incurred*. The ML community's own response to
contamination — measure and report it per benchmark, rather than assert
independence — is precisely the "incurred" field being filled in.

## What this does NOT establish

1. **Not a claim that these fields are unaware.** All three cited
   papers ARE the fields noticing the problem themselves. The
   observation is that they noticed it independently, without shared
   vocabulary — not that anyone was blind.
2. Numbers from matches 1-2 were **not** independently reproduced —
   they are `[VERIFIED-arXiv]` as citations only, unlike `E5`'s own
   `+6.80%`, which was computed here.
3. Genome annotation is `SOURCE_NOT_FOUND`, not "confirmed absent" —
   one search shape was tried and failed; that is weak evidence.
4. No novelty check has been run on the general pattern. It is likely
   that "measurement pipelines assume the theory they test" exists
   under a name in philosophy of science (theory-ladenness of
   observation is the obvious candidate) — **that connection is
   unverified and must be checked before any claim of originality.**
