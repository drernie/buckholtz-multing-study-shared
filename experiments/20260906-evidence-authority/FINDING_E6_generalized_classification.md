# FINDING E6 — a generalized input-provenance classification, grounded
# in three independent published examples from other people's work

**Date:** 2026-09-06
**Continues:** `E1`-`E5`. Executes option 2 ("generalize the three-class
system into something that isn't a paper about one preprint"), explicit
go-ahead given.

**Scope discipline set in advance:** the stated risk for this option was
"if the examples all come from v82, this is a paper about one person,
not a method — need at least two from other people's work." That bar is
met: **all three worked examples below are from other authors**, and
v82 appears only as the source of the classification vocabulary being
extended.

## The gap this closes

`FINDING_E4` mapped v82's inputs onto TJB's own three classes (Class I
data-proximate / Class II retained-theoretical / Class III circular).
`FINDING_E5` then showed the classification has a **missing field**:
cosmic chronometer `H(z)` is correctly Class I — it assumes no
expansion history — and *simultaneously* carries a `~6.8%` uniform
systematic from the stellar-population model, `100%` correlated across
redshift bins, absent from its quoted error bar.

**One label cannot carry both facts.** "Class I" answers *which
assumption was avoided*. It says nothing about *what the input depends
on instead*, and that second thing is what actually propagates into a
`χ²`.

## The extension: two fields, not one

| field | question | example (CC `H(z)`) |
|---|---|---|
| **avoided** | which assumption does this input NOT make? (TJB's Class I/II/III) | expansion history — genuinely not assumed |
| **incurred** | what does it depend on instead, and is that dependence *in the quoted uncertainty*? | SPS model, SFH, IMF, stellar library: `~9%` mean, correlated across bins, **NOT in `errHz`** |

Plus the rule `FINDING_E3`'s skeptic pass produced, which generalizes
beyond cosmology:

> **Check the whole pipeline, not the named step.** A technique can
> genuinely escape the specific circularity it was designed to escape
> and re-import the same class of assumption at a different step —
> calibration, background subtraction, sample selection. `E3`'s kSZ
> case: the velocity channel escapes "redshift minus assumed Hubble
> flow", then the analysis assumes a fiducial `H₀` to convert angles
> into the separations it reports.

## Three worked examples, none of them from v82

**1. Cosmic chronometers — same galaxies, two stellar-population
models.** `[VERIFIED — measured this session, FINDING_E5]` Moresco's
own two published tables, identical source papers and redshift grid,
differing only in SPS model (BC03 vs M11): a uniform `+6.80%` shift
across 12 of 15 points, spread `0.99` pp. *Avoided:* expansion history.
*Incurred:* stellar-population modelling, `100%` correlated across
bins, quantified by the community itself
(`[VERIFIED-arXiv:2003.07362]`) and excluded from the quoted `errHz` by
construction.

**2. Type Ia supernovae — same supernovae, two light-curve fitters.**
`[VERIFIED-arXiv:1010.4014]` Bengochea (2010), *"Supernova light-curve
fitters and Dark Energy"*, finds that **"the same SN Ia set built with
two different light-curve fitters behaves as two separate and distinct
supernova sets."** Structurally identical to example 1: one set of
observations, two processing models, two datasets. *Avoided:* an
assumed distance-redshift relation. *Incurred:* the standardization
model — the light-curve fitter, its training sample, its colour law.

**3. BAO — the "standard ruler" whose length is a theoretical
prediction.** `[VERIFIED-arXiv:2405.12498]` Liu et al. (2024) state it
directly: *"The sound horizon is a key theoretical prediction of the
cosmological model that depends on the speed of sound and the rate of
expansion in the early universe."* An entire sub-literature exists
precisely to calibrate that ruler *without* the early-universe model —
Verde et al., *"The length of the low-redshift standard ruler"*
(`[VERIFIED-arXiv:1607.05297]`); Heavens, Jimenez & Verde
(`[VERIFIED-arXiv:1409.6217]`), which is a model example of the
**incurred** field done right: it enumerates its own residual
assumptions explicitly ("we make only the following minimal
assumptions: homogeneity and isotropy; a metric theory of gravity;
a smooth expansion history"). Roukema et al.
(`[VERIFIED-arXiv:1506.05478]`) go further and question the premise in
their own title: *"Is the baryon acoustic oscillation peak a
cosmological standard ruler?"*

**What the three share:** in each case the input is correctly described
as escaping one specific assumption, that description is true, and each
one nevertheless carries a *different* model dependence large enough to
matter — which is visible only if someone asks the second question.

## Honest status of this as a contribution

**Not claimed:** that this two-field extension is novel. A novelty
check has **not** been run (`/novelty-assessment` not invoked), and the
constituent pieces are all borrowed: the three classes are TJB's, the
"enumerate your residual assumptions" practice is standard in the
model-independent-cosmology literature (Heavens et al. is a worked
example of it), and this project's own `docs/151` already separates
empirical / ontological / causal status for *results* rather than
inputs. **Anyone claiming this as new must run the novelty check
first.**

**What is genuinely this project's own:** the `+6.80%` measurement in
example 1 (computed here from Moresco's tables, with a positive control
on source-paper identity), the observation that the three examples share
one structure, and the pipeline rule from `E3`.

**Realistic assessment:** this is a usable framework for auditing an
input chain, and a plausible seed for the "publication independent of
my work" TJB suggested — but it is an *assembly of existing practice*,
and the honest framing in any write-up is "collected and made explicit",
not "discovered".

## What this does NOT establish

1. Not novel until a real novelty check says so.
2. Does not establish that applying the second field changes any
   published conclusion — `E5` explicitly did not rerun v82's fits or
   this project's own Fisher forecasts with the full covariance.
3. Examples 2 and 3 are cited from their authors' own abstracts and
   framing; unlike example 1, **their numbers were not independently
   recomputed here**. They are `[VERIFIED-arXiv]` as citations, not as
   reproductions.
4. `NO_AUTHOR_ERROR` — v82 supplies vocabulary being extended, not a
   target of criticism.
