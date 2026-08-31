# docs/152 — "De-conflating evidence and authority": v82 §II.F/§IV.N-O
# mapped against this project's own provenance tools

**Date:** 2026-08-31
**L0 (EstimandOps):** descriptive — this note summarizes what two specific
sections of v82 say, and maps them against this project's own existing
documentation conventions. It is not a physics claim, and not a verdict
on whether TJB's own argument is correct.
**Prompted by:** TJB's 2026-08-30 23:26 email (`correspondence/
tjb_reply_20260830_2326.md`), which proposed that Sergey might develop
"de-conflating evidence and authority" as a contribution possibly
independent of MULTING, citing v82 §II.F. This note grounds that
proposal directly against the actual pages (read via PDF, not via the
email's own paraphrase) and against §IV.N-O, which turns out to be the
more direct source of the specific "Newtonian/Minkowski coordinates"
language in the email.
**Premise (`NO_AUTHOR_ERROR`):** this note reads and maps TJB's own
published argument; it does not evaluate whether that argument is
correct physics, and does not extend any verdict about this project's
own MULTING reconstruction onto it.

## 1. What §II.F actually says (v82 pp. 9-10)

Title: "Analytical formulation: empirical grounding of the model's
inputs, and of evidence more generally." TJB's own framing, quoted
directly: he offers the classification below "not only as an audit of
MULTING's own inputs, but as a general, transferable tool."

Three classes, for every quantity MULTING's equations depend on:

- **Class I, data-proximate** — grounded in near-direct measurement.
  Example given: the 31-point cosmic-chronometer `H(z)` compilation used
  to test the framework, and (conditionally) ICM thermal energy `k_X(z)`
  if grounded in directly-measured cluster X-ray scaling relations.
- **Class II, retained-theoretical** — an FLRW-flavored theoretical step,
  kept deliberately *after checking* whether a more directly empirical
  alternative would actually be less model-dependent. Example given: the
  node mass evolution law `m_X(z)`.
- **Class III, circular** — the input is constructed by assuming the very
  relation the model aims to test independently. Example given, and
  named by TJB himself as "the most serious residual dependence in the
  present computations": the node radius `r_X(z)`, when built via the
  standard R500-type definition, which sets that radius via an assumed
  critical-density evolution `ρ_crit(z) = ρ_crit,0 E(z)²` — directly
  assuming the Friedmann equation to build an input that feeds the very
  force law whose purpose is to independently predict `H(z)`.

Two extensions beyond the 3-class scheme itself, both on p.10:

1. The three classes address *calibration* — but TJB notes a fuller
   assessment extends further, into *how* evidence is sought/obtained/
   reported in the first place: reporting conventions (e.g. the
   self-similar `E(z)^γ` basis function is a convention, not a strict
   requirement of the underlying measurement) and survey design (which
   redshift ranges/halo masses/sky regions get deep follow-up, and how
   much scrutiny an anomalous result receives — both shaped by the
   dominant paradigm). He explicitly does not attempt a full audit of
   these effects, only flags them.
2. He states plainly that this classification is **not specific to
   MULTING, and does not presuppose ΛCDM's own observational pipelines
   are exempt** — BAO analyses, Type Ia supernova standardization, and
   weak-lensing shear calibration each involve their own chains of
   assumed-cosmology-dependent reduction steps that could, in principle,
   be subject to the same three-class assessment. He offers the
   classification "in the hope that it — or an improved version of it —
   might be applied symmetrically."

Closing caveat (his own words, paraphrased closely): this is meant as a
starting point for a broader, symmetric practice, not a claim that full
independence from ΛCDM is achievable by MULTING or any other framework
— redshift itself, and virtually all astronomical unit calibration,
already presuppose cosmic expansion at some level.

## 2. What §IV.N-O actually say (v82 pp. 23-25)

This is the more direct source of the specific language in TJB's email
("space-and-time coordinates that associate with Newton or with the
Minkowski metric and does not associate with notions of space-time as a
thing that has properties") — §II.F's Class III paragraph itself
cross-references it ("See also Sec. IV O.").

**§IV.N** ("Uses of general relativity and of our notions of two-body
gravity"): popular modeling associates GR's precision tests with
three-body physics — source (active, stress-energy), probe (passive,
small mass/photon), observer. Space-time coordinates that associate with
that modeling associate with the *observer*. TJB notes Newtonian physics,
and MULTING itself, associate with a source and a probe, but not
necessarily with an observer. He also raises, as an aside, that some
literature suggests space-time curvature is not necessarily fundamental
to gravity, offering the analogy: "space-time is to gravity as ether is
to electromagnetism."

**§IV.O** ("A path forward: Newtonian and Minkowski coordinates,
space-time-coordinate patches, and disentangling data from ΛCDM
context") — the section title is close to verbatim what the email
describes:

- GR is extraordinarily well tested where it has actually been tested
  *directly*: solar-system dynamics, binary pulsar timing, GPS timing
  corrections, gravitational-wave signals from compact binaries. Each of
  these is a *local*, or patch-wise, test — a specific system, a
  specific region of space-time coordinates, a specific epoch.
- The claim that a *single* global metric — the FLRW metric underlying
  ΛCDM — correctly describes the entire universe, at every place and
  every time simultaneously, is, in TJB's own words, "a distinct and
  considerably larger extrapolation from those local tests, not a direct
  consequence of them."
- TJB states explicitly this distinction is not novel to his paper — it
  is the subject of an active, decades-old research program usually
  called *cosmological averaging* or *backreaction*, sometimes "the
  cosmological fitting problem." He cites a review stating it is
  inadmissible to conclude from the excellent local verification of
  Einstein's equations that the *averaged* fields describing the
  universe as a whole also satisfy those equations in the same simple
  form, "precisely because averaging and constructing the Einstein
  tensor do not commute in general" — and connects this to present
  cosmological tensions via a cited recent review. [Reference numbers as
  they appear in his own bibliography: [8, 31] for the averaging/
  backreaction claim, [126] for the tensions connection — **not
  independently verified against an external bibliography this
  session**; see §4 below.] He does not resolve the debate, only notes
  that questioning the global extrapolation of a locally-tested theory
  is "a legitimate, actively pursued line of inquiry within mainstream
  cosmology, not a departure from it."
- The patch-wise starting point this suggests is, in his words, "not in
  tension with general relativity; it is built on structure general
  relativity itself already guarantees." The equivalence principle
  ensures only that spacetime looks locally flat (Minkowski) and
  Newtonian at low relative velocity, at any given event — it does not,
  by itself, determine how those local patches must be stitched into a
  single global structure. A framework built from Newtonian, patch-wise
  node dynamics, as MULTING attempts, "can therefore be read as taking
  that local structure as its starting point, rather than assuming the
  further, global step."

## 3. Mapping against this project's own provenance tools

| Dimension | TJB's §II.F Class I/II/III | This project's Gate 2 (`artifact-provenance-gates.md`) | This project's `docs/151` |
|---|---|---|---|
| What it classifies | A **raw input quantity** feeding a physical model (e.g. `r_X(z)`, `m_X(z)`) | A **finished claim/artifact** being considered as a validation target | An **already-built result's own verdict**, split into independent layers |
| Point in the pipeline | Upstream — before the model runs | Mid — before trusting a target for comparison | Downstream — after a claim has already been analyzed |
| The three-way split | data-proximate / retained-theoretical / circular | prediction / fit / illustration | empirical-model / ontological-interpretation / causal-claim |
| The failure it guards against | A model's apparent independence from ΛCDM is illusory because an input silently assumes the very relation being tested | A fit is used as its own validation target, reproducing the fitting procedure rather than confirming a theory | A good empirical/model result is silently read as confirmation of the mechanism or causal story that motivated it |

**Where the analogy holds:** both are the same underlying move — name
explicitly what a piece of reasoning is actually grounded in versus what
it has inherited from a background framework or process, so a reader can
judge how much of the support is independent of the paradigm/procedure
under test. Both are offered by their authors as *general, transferable*
tools rather than one-off fixes specific to a single claim (TJB says
this explicitly for Class I/II/III; this project's own `docs/151` was
itself a cross-domain transfer, from quantum-foundations' formalism/
interpretation distinction — so the move of generalizing a domain-
specific provenance discipline into a transferable convention is
something this project had already done once, independently, before
TJB's email arrived).

**Where the analogy breaks:** TJB's system classifies the epistemic
status of *data itself*, prior to any modeling — a physics-of-
measurement question. This project's tools classify the epistemic status
of *claims and artifacts* produced during a research-audit process — a
different object, at a different stage, for a different purpose (guarding
against overclaiming in an audit, not against silently importing
cosmology into a supposedly-independent measurement chain). They are
not interchangeable systems; the resemblance is in the underlying
discipline (name the provenance, don't assume it), not in the specific
mechanics.

## 4. Honest note on §IV.O's central claim

The claim that treating a single global FLRW metric as valid everywhere
is a genuine additional extrapolation beyond what local GR tests
establish is **not a fringe move** — TJB is pointing at a real,
named research area (cosmological averaging / backreaction / the
"cosmological fitting problem"), and the mechanism he cites (averaging
and constructing the Einstein tensor do not commute in general) is a
standard objection in that literature.

**What was and was not checked this session:** the reference numbers
[8, 31, 126] as they appear in TJB's own bibliography were read as
citation markers only — they were **not** independently looked up
against arXiv/ADS/an external bibliography this session. [MEMORY, not
independently verified this session] the *existence* of a cosmological-
averaging/backreaction research program under approximately these names
is consistent with general familiarity with the cosmology literature
(this area is commonly associated with names like Buchert, Ellis, and
Wiltshire in that broader literature) — but this project has not
verified TJB's specific cited works, and this note does not claim to.

## What this note does NOT establish

1. Not a claim that this project's own tools (`docs/151`, Gate 2) are
   equivalent in rigor, scope, or publication-readiness to a formal
   methodological contribution — they are internal documentation
   conventions for a research audit, built for a narrower purpose.
2. Not an evaluation of whether the backreaction/patch-wise argument in
   §IV.O is correct physics — outside this project's scope and outside
   Sergey's own stated position (`correspondence/
   draft_tjb_reply_20260830.md`: "I do not have the physics background
   to judge what belongs in the literature").
3. Not a decision about whether, or how, to develop the evidence/
   authority idea into a publication or joint contribution — that
   remains explicitly Sergey's call, not something this note or any
   draft reply should presume.
4. Does not independently verify TJB's cited references [8, 31, 126] —
   see §4.
5. Not a claim that TJB's II.F 3-class system and this project's Gate 2/
   `docs/151` are the same system under different names — see §3's
   "where the analogy breaks."

NOT_VALIDATION * NOT_REFUTATION * OUR_READING * NO_AUTHOR_ERROR
