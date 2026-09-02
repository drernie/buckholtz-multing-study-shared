# FINDING P158 — Addendum: literature-grounding attempt REJECTED (both
# sub-questions), real citations found but do not answer what was asked

**Date:** 2026-09-02
**Trigger:** user go-ahead to start `docs/153` §3a's "real finite-r
derivation," redirected (user-approved plan) toward literature-grounding
`FINDING_P157`/`P158`'s more precise, already-skeptic-reviewed reframing
of the same bottleneck — see `CLAIM_P158_ADDENDUM_literature_grounding.md`
for the scoping rationale.
**Status:** REJECT (of the central numeric contribution). A context-blind
skeptic pass (Step 8a) found both proxy substitutions below are category
errors — real quantities, real citations, but the wrong physical
quantity for what `FINDING_P158`'s formula needs. Independently re-
verified before accepting, per `audit-verification-gate.md`'s rule that
a skeptic's own `[VERIFIED]` is `[INFERRED]` until re-checked. Kept as
REJECT, not silently softened, following this session's own established
pattern (`FINDING_P189`, `FINDING_P189_ADDENDUM`).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR

---

## What happened, plainly

Two real, correctly-cited papers were found: Sereno & Ettori 2014
(arXiv:1407.7868, "CoMaLit-I") for sub-question (a), Tinker et al. 2010
(arXiv:1001.3162, halo bias) for sub-question (b). Both citations are
genuine — fetched directly this session, not recalled from memory. The
error was in how each was USED, not in whether either exists.

**A context-blind skeptic pass (Step 8a, given the claim + the exact
numbers, no reasoning chain) found both applications invalid on
independently-verifiable grounds:**

### (a) The σ_lnm substitution is a category error, not a defensible proxy

`σ_WL~15%`/`σ_HE~25%` (CoMaLit-I) measure **measurement-method scatter**:
how much two independent mass-estimation *techniques* (weak lensing vs.
X-ray hydrostatic equilibrium) disagree about the **same** underlying
true cluster mass. `FINDING_P158`'s own formula needs `Var[log M_true]`
— the **true, physical spread of mass across a population of distinct
clusters**. These are structurally different quantities: one is
instrument/method noise around a single true value; the other is
astrophysical diversity across many objects. Nothing connects their
magnitudes.

**Independently re-verified, not merely accepted:** the original write-up
did state this distinction explicitly as a caveat — but then used the
number anyway "as a proxy," on the stated grounds that "no better real
number was found." The skeptic's rebuttal to that specific justification
holds up: the halo/cluster mass function `dn/dlnM` is one of the
most-measured objects in cosmology, and a real `Var[log M_true]` for any
stated population definition (mass floor, redshift bin) is in principle
directly computable from it — this session's search simply did not
attempt that calculation, so "no better number exists" was false; "no
better number was searched for" would have been accurate.

**Why the error matters quantitatively, not just conceptually:** `R(p) =
exp(p·σ²(p−1)/2)` is exponential in `σ²`. A population-scatter `σ_lnM` a
factor of ~2–4× larger than the 0.14–0.25 measurement-scatter numbers
used (plausible for a population spanning even one decade in mass, since
halo/cluster mass functions are steep and skewed) does not produce a
proportionally larger enhancement — it can move the result from "a few
percent correction" to "a dominant, order-of-magnitude effect." The
addendum's own headline numbers (`F^(1)~1.04–1.12×`, `F^(2)~1.08–1.26×`)
are therefore not "the Jensen enhancement using the best available real
number" — they are the enhancement in a regime the actual physical
question does not live in.

### (b) The halo-bias-implies-positive-ρ argument conflates two different statistics

Tinker et al. 2010 establishes that halo clustering **bias** `b(M)`
increases monotonically with mass — a **large-scale, many-halo ensemble**
statement about how strongly a population of halos of a given mass
traces the density field, via the two-point correlation function
`ξ_hh(r) ~ b(M₁)b(M₂)ξ_mm(r)`.

`FINDING_P158`'s own `ρ` is a **pairwise, close-pair** quantity:
`Cov[log M₁, log M₂]` for two *specific* halos selected as a pair (or,
for v82's own purposes, a "node"). **These are not the same object, and
one does not license an inference about the other.** Conditioning on "a
companion halo exists within some small separation" is dominated by the
steep shape of the mass function itself — close pairs are typically
major-plus-minor-satellite configurations, not two similarly-massive
halos — which can produce a near-zero or even negative pairwise mass
correlation *even in a universe where large-scale bias rises with mass*.
The addendum's own "plausibility argument for positive ρ" is therefore
not licensed by the citation it rested on.

**Independently re-verified:** the logical distinction (ensemble
clustering-strength statistic vs. specific-pair covariance) is checkable
directly from what each quantity is defined to measure, independent of
any particular numeric claim, and holds up on that direct check.

## Kill Analysis

**What is killed:**
- The claim that this session's literature search "grounds" `FINDING_P158`'s
  `σ_lnm` — it does not; a real number for a different quantity was found.
- The claim that Tinker et al. 2010 gives even a *plausibility* argument
  for `ρ`'s sign — it does not; it answers a structurally different
  question.
- The numeric table (`F^(1)~1.04–1.12×`, `F^(2)~1.08–1.26×`, "consistent
  with the low end of `P158`'s illustrative table") — withdrawn. That
  framing was, on inspection, closer to tautological than confirmatory:
  a small input scatter mechanically produces a small enhancement,
  independent of whether the input was the right quantity.

**What is NOT killed:**
- The two citations themselves are real and correctly quoted — `[VERIFIED-
  REAL]` stands for what each paper actually says, only the *application*
  to this project's own question is rejected.
- `FINDING_P158`'s own Jensen's-inequality machinery and its
  `CONDITIONAL-DIRECTIONAL-PREDICTION` verdict — completely untouched;
  this addendum neither strengthens nor weakens it, having failed to
  supply usable real inputs.
- The real, correctly-scoped next steps this attempt surfaces (see below)
  — a genuine narrowing of what "the real number" would require, which
  this session's search did not attempt.

## What a real answer to each sub-question would actually require

**(a):** a `Var[log M_true]` computed from an actual halo/cluster mass
function (`dn/dlnM`, e.g. Tinker et al. 2008's own mass-function fit, not
its 2010 bias paper) integrated over an explicitly stated population
definition (mass floor, redshift range) matching whatever population v82's
own "representative node" is implicitly meant to stand in for — itself
an unresolved question, since v82 never defines that population
precisely (`FINDING_P157` §2).

**(b):** either a direct measurement of pairwise mass covariance for
close/interacting halo pairs from N-body simulation literature (subhalo/
satellite mass-function or halo-pair statistics — not attempted this
session), or an explicit acknowledgment that `ρ` should be treated as a
free sensitivity parameter swept over `[−1, 1]` with no real prior,
reporting the full sensitivity curve rather than reaching for a single
plausibility argument.

Neither of these is a small addition to this session's search — both are
real, separate research tasks, not a quick citation lookup. This is
itself informative: it means `docs/153`'s pre-condition 3 (cost vs.
consequence) should register this as **more** expensive than a first
pass suggested, not less.

## What this does NOT establish

1. Not a claim that `FINDING_P158`'s underlying mechanism (Jensen's
   inequality applied to v82's own mass-derived chain) is wrong — that
   stands, unattacked, exactly as before.
2. Not a claim that real literature grounding for either sub-question is
   impossible — only that this session's specific search did not find
   it, and named more precisely what would.
3. Not an answer to `docs/153`'s pre-conditions — if anything, this
   REJECT makes pre-condition 3's cost estimate less favorable than
   `FINDING_P158` alone suggested, since properly grounding either
   unknown is a real, separate research undertaking.
4. `NO_AUTHOR_ERROR` — entirely about this project's own literature
   search and its use, not about MULTING, v82, or Dr. Buckholtz's work.

## Artifacts

- `CLAIM_P158_ADDENDUM_literature_grounding.md` — original claim, kept
  unedited per this project's no-silent-correction convention.
- This file — the corrected write-up (REJECT), same file per this
  session's addendum-file convention (the claim.md is the historical
  record; this FINDING file is itself the correction, same pattern as
  `FINDING_P189`/`FINDING_P189_ADDENDUM`).
- Real sources cited then rejected as applied: Sereno & Ettori 2014
  (arXiv:1407.7868), Tinker et al. 2010 (arXiv:1001.3162).
- `P158_jensen_mass_averaging_v82_force_terms.py` — untouched, its own
  verdict stands unaffected.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
