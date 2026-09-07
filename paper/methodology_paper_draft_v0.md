# DRAFT v0 · NOT_FOR_SUBMISSION · has NOT passed the Submission Gate

**Status:** first structural draft, written 2026-09-07. Every factual claim
below is `[VERIFIED]` against this project's own committed record (commit
hashes and file paths given throughout) — nothing is invented for the
draft. What has **not** happened yet: a context-blind skeptic pass on this
document itself, the ≥9-item pre-submission checklist, a text↔figure
consistency check, or the mandatory 24-hour cooling-off period
(`~/.claude/rules/integrity.md` § Submission Gate). Do not quote, cite, or
send this document externally until all four have run and a human has
said so explicitly.

---

# Context-Blind Adversarial Verification Catches Defects That Naive Verification Misses: A Longitudinal Case Study

## Abstract (draft)

We report a longitudinal, within-project case study of an AI-assisted
research workflow that (a) runs a structured falsification protocol
(pre-registered claim, positive/negative controls, a context-blind
adversarial review step before any result is promoted) and (b) keeps a
permanent, append-only record of every retraction, with root causes
classified against a pre-existing taxonomy. Over a single working session
(2026-09-07), the same protocol applied to six independently-produced
research artifacts caught defects in all six, later confirmed by
independent, tool-based re-verification of every load-bearing claim in
each defect report. We characterize the defects by root cause, find that
four of the observed failure modes are not covered by our own
pre-existing 11-category taxonomy and propose extensions, and report a
separate, pre-registered pilot benchmark (`N=16`) comparing this protocol
against an ambient-default baseline, whose result was **inconclusive**
(McNemar `p=1.0`, underpowered as pre-registered) — reported honestly as a
negative/null pilot result, not omitted. We argue the case-study evidence
and the pilot's null result are not in tension: the case studies show the
protocol catches defects when applied; the pilot shows a `12`-task
comparison cannot detect the effect size, which is exactly what its own
pre-registration predicted before any data existed. We position this as a
methodology contribution independent of the physics domain (cosmological
model reconstruction) in which it was produced.

## 1. Introduction

### 1.1 The problem

AI-assisted research produces claims quickly. Distinguishing a load-bearing
result from a plausible-sounding one that will not survive scrutiny is the
actual bottleneck — not claim generation. Existing practice mostly relies
on the same reasoning process that produced a claim to also check it,
which is exactly where confirmation bias is least detectable.

### 1.2 What we did, in one sentence

We ran a fixed, pre-specified protocol — falsifiable claim, positive and
negative controls, then a **context-blind** adversarial review (the
reviewer receives only the claim and the artifact, never the reasoning
chain, prior successes, or session history) — on every research artifact
produced in one working day, and kept every finding, retraction, and root
cause in a permanent, git-committed record.

### 1.3 Contribution

1. A same-day, same-project record of **six** independent artifacts, all
   caught by the identical protocol, with **every** root cause
   independently re-verified by tool (not accepted on the reviewing
   agent's word) before being counted.
2. A refined failure-mode taxonomy: our own pre-existing 11-category
   taxonomy (`docs/146`) accounted for most observed defects, but four
   observed patterns are not covered and are proposed as extensions
   (§4.4).
3. An honest, pre-registered pilot benchmark of the protocol against a
   naive baseline, reported as **inconclusive**, with the specific
   statistical reason stated rather than suppressed (§5).

## 2. Protocol (frozen)

The full protocol is the union of:
- `~/.claude/rules/falsification-ladder.md` (Full-Ladder: estimand →
  claim → controls → Step 8a context-blind skeptic → decision)
- `~/.claude/rules/audit-verification-gate.md` (a reviewing agent's own
  `[VERIFIED]` is treated as the primary author's `[INFERRED]` until
  independently re-checked by tool)
- `~/.claude/rules/estimand-ops.md` (L0 gate: descriptive / predictive /
  causal classification before any claim work begins)

Every one of the six case studies in §4 followed this exact sequence:
(1) write the claim with positive controls, (2) dispatch a **fresh**
review agent with no access to the session's reasoning history — only the
claim document and the artifact, verbatim — instructed to attempt
falsification, not confirmation, (3) independently re-verify every
load-bearing citation the reviewer returned, by direct tool use (`grep`,
re-derivation, re-running code), before accepting or rejecting anything,
(4) if falsified, write a retraction that keeps the original text verbatim
(no silent correction) and states the specific defect and its root cause.

**Context asymmetry is the load-bearing design choice.** The reviewing
agent never sees why the claim was written, only what it says and what it
rests on — this is what separates step (2) from a second pass by the same
reasoning process that produced the claim.

## 3. Taxonomy (existing)

`docs/146_failure_mode_taxonomy.md` enumerates 11 categories, each with
≥2 real historical incidents from this project, established before the
session reported here:

1. Coincidence without mechanism (post-hoc numerology)
2. Tautological control (cannot fail by construction)
3. False independence (hidden shared machinery)
4. A parameter silently held fixed instead of fully scanned
5. Transferring a narrow result to a broader claim
6. Reusing an already-weakened result at its original strength
7. A control evaluated where the tested effect is trivially zero
8. A domain heuristic applied without checking it fits the mechanism
9. A numerical/software artifact mistaken for a physical result
10. Recomposition overclaim (the sum of true parts claims more than any
    part, or their conjunction, licenses)
11. Provenance/attribution error (stale, swapped, or silently changed
    value)

## 4. Case studies (this session, 2026-09-07)

All six artifacts below were produced, reviewed, and — in every case —
found defective, inside one working day, by the identical protocol. Every
row is `[VERIFIED]`: I independently re-checked the reviewer's own
citations against source before accepting any of them (per
`audit-verification-gate.md`).

### 4.1 Summary table

| # | artifact | headline claim | verdict | dominant taxonomy category |
|---|---|---|---|---|
| 1 | `P214` | a version-comparison question was resolved | 4/5 sub-claims falsified | **new** (§4.4.1) |
| 2 | `P215` | an external physical bound "survives" | conclusion inverted | Cat. 2 (tautological control) + Cat. 6 (reused known bug) |
| 3 | `P216` | an internal scope inconsistency in a source document | falsified — hierarchy misread as conflict | **new** (§4.4.2) |
| 4 | `P217` | a cross-version parameter comparison | falsified — one-sided search | **new** (§4.4.3) |
| 5 | `P220` (T0 sub-claim) | a nuisance-parameter "scenario" breaks a model | void — exact algebraic degeneracy | **new** (§4.4.4, protocol-vs-target) |
| 6 | `P220` (headline `χ²` claim) | frozen-parameter perturbation "dwarfs" the model's margin | frozen-parameter artifact; real effect ~40x smaller after the field's own kill-test | **new** (§4.4.4, protocol-vs-target) |

Note on cases 4 vs 5-6: both are "new" patterns, but distinct mechanisms.
Case 4's defect is a **search asymmetry** -- one document swept, the other
assumed silent, for a claim that is inherently about the relationship
*between* two documents. Cases 5-6's defect is a **parameter-freezing
artifact** -- a fully self-contained property of one model's own
degeneracy structure, uninvolving any comparison across documents. An
earlier version of this table conflated the two under one label; caught
during the pre-commit read-through, corrected here (kept as a note rather
than silently fixed, since it is itself a small illustration of section
4.3's point about symmetric checking).

### 4.2 Root-cause detail (three worked examples)

**Case 2 (`P215`), Cat. 2 + Cat. 6.** The claim's own positive control
(`PC1`) tuned one free parameter to reproduce one target number — zero
degrees of freedom — and could not fail by construction. Separately, the
claim reproduced a factor-of-2 arithmetic error a **prior finding in the
same directory** (`FINDING_P7`, dated one month earlier) had already
flagged as open. The Step -3 pre-work check (search this project's own
prior work before writing a new claim) was not run.

**Case 4 (`P217`), new pattern.** The claim swept one parameter's mentions
across one of two source documents, then stated a conclusion about the
**relationship between the two documents**. The same sweep on the second
document, when eventually run, dissolved the claimed asymmetry within
minutes. The defect is not in either individual observation — both were
accurate — but in treating an asymmetry in **search effort** as if it were
an asymmetry in the **sources**.

**Case 6 (`P220` headline), new pattern.** A claim froze three fitted
parameters and perturbed two others within their own quoted uncertainty,
reporting the resulting output instability as a property of the model. A
kill-test — re-optimizing the frozen parameters at each perturbed point,
which is mathematically guaranteed to help, never hurt, since the frozen
point is one member of the re-optimization's own search space — reduced
the claimed effect by roughly two orders of magnitude at one test point
and *reversed its sign* at another (the re-optimized fit was **better**
than the original published value). The defect is conflating the
sensitivity of an analysis **protocol** (parameters held fixed) with the
sensitivity of the **target system** (parameters free to compensate).

### 4.3 What made all six catchable by the same mechanism

Despite differing content, five of the six shared a structural root:
**a one-sided procedure reported as a two-sided fact** — a search run on
one document and not its counterpart (Case 4), a control with zero
degrees of freedom presented as discriminating (Case 2), a parameter held
fixed and its resulting instability presented as intrinsic (Cases 5, 6),
a citation drawn from a document's applied section without checking its
self-limiting section (Cases 1, 3, 5). None of these five required new
data to catch — each was caught by re-running the **same available
information** more symmetrically.

### 4.4 Proposed taxonomy extensions

**4.4.1 Non-exhaustive search reported as confirmed absence.** A `grep`
or equivalent search that misses a real occurrence (through morphology,
word-gluing in a text extraction, or an unsearched synonym) is reported as
"absent," when it is actually "not found by this search." Distinct from
existing Category 9 (a *computed* artifact mistaken for a *physical*
result) — here the failure is in the search's completeness, not in a
downstream computation.

**4.4.2 Selective section reading.** A source document containing both an
applied section (where a framework or claim is used) and a self-limiting
section (where the same document states where it does not apply, or
retracts an earlier framing) is read from the first and not the second,
even when the first explicitly cross-references the second.

**4.4.3 Asymmetric verification effort mistaken for comparative evidence.**
A claim about the relationship between two sources (documents, versions,
datasets) is supported by a search or check run thoroughly on one source
and only assumed, not run, on the other. The individual observation on
the checked source can be entirely accurate; the defect is in treating an
asymmetry in *how much verification effort was spent on each side* as if
it were an asymmetry *in the sources themselves*. Detectable by running
the identical check on the previously-unchecked side before finalizing
any comparative claim — in the one case observed this session, doing so
took under a minute and reversed the claim.

**4.4.4 Protocol sensitivity mistaken for target sensitivity.** Freezing
a subset of a model's parameters and perturbing the rest produces an
apparent fragility that is an artifact of the freezing choice, not a
property of the model, whenever the frozen and perturbed parameters are
partially or fully degenerate. Detectable only by a kill-test that lets
the frozen parameters respond — merely re-running the same frozen
protocol more times (a larger Monte Carlo) does not detect it, since every
draw shares the same freezing artifact.

## 5. A companion pilot benchmark — reported honestly as inconclusive

Independent of the case studies above, this project separately ran a
**pre-registered** pilot (`experiments/adversarial-verification-
benchmark/`, `PREREGISTRATION.md`) comparing the same protocol
("treatment": explicit FL steps + a skeptic sub-call) against an
"ambient-default" baseline (the same underlying model, given a generic
instruction, with the project's always-on rules still loaded — the
ambient channel could not be fully suppressed, a limitation the
pre-registration documents explicitly) on a fixed task corpus with
seeded, known defects.

**Result:** `N=16` (reduced from a pre-registered `N=32` for session-budget
reasons, committed before the run), both arms detected `12/12` seeded
defects once a scoring-rubric gap was fixed (`Addendum 3`: a correctly
hedged, appropriately uncertain output was previously scored identically
to a confidently wrong one). McNemar's exact test: `0` discordant pairs,
`p = 1.0` **by construction**. This is exactly the underpowered/
inconclusive outcome the pre-registration's own power analysis predicted
before any data existed (`§3.1`: *"at n=26 [here n=12-13], adequately
powered only for a moderate-or-larger effect… a smaller true effect will
read as inconclusive and must be reported as inconclusive, not as
evidence of no effect"*). Kill criterion `K1` (detection rates converge)
is formally met.

**We report this without softening it.** The pilot does not confirm the
protocol's value; it also does not refute it — it was underpowered by its
own design, on a scale set for session-budget reasons, and it says so.
The case studies in §4 are not a substitute statistical test; they are a
different kind of evidence (existence proof of real catches, with root
causes), and the paper's contribution rests on both being reported
together, honestly labelled, rather than only the flattering one being
kept.

## 6. Limitations (draft, incomplete)

1. **Single project, single domain.** All six case studies and the pilot
   corpus derive from one cosmology-reconstruction project. Generalization
   to other domains is untested.
2. **Independent verification strength.** Per this project's own
   Independent Verification Strength Ladder, the review agent used
   throughout is "same model, isolated context" — the weakest tier that
   still counts as independent. No cross-model or human replication has
   been run on any of the six case studies.
3. **Sample size.** Six case studies in one day is suggestive, not
   statistical. The pilot benchmark is the attempt at a statistical test
   and is reported as inconclusive (§5).
4. **Author-verifier is the same person across all six re-verifications**
   in §4 — I (the primary agent) independently re-checked the reviewing
   agent's citations in every case, but I am not independent of the
   overall session. A stronger design would use a different verifier for
   this re-check step too.
5. **Selection into the record.** All six case studies are claims that
   this project itself produced and then reviewed — there is no
   claims-that-were-never-reviewed comparison group, so we cannot report
   a "catch rate" as a fraction of all claims made, only that six for six
   reviewed claims were found defective.

## 7. Related work (to fill in)

- Cross-Context Review (arXiv:2603.12123) — closest design template
  (seeded errors, paired conditions, paired significance tests), different
  domain (not computational science), different taxonomy.
- "The Calibration Turn" (Hongmin Li, arXiv:2606.31273) — near-identical
  conceptual vocabulary, no empirical benchmark; this work is a candidate
  first empirical instantiation.
- Seeded-defect benchmarks (FLAWS, SPOT, SoundnessBench, ReFACT,
  BadScientist) — compare models, not workflows/protocols.

## 8. What this draft still needs before Submission Gate

- [ ] Fill §7 with verified citations (DOI/arXiv IDs), not from memory.
- [ ] A precise, checkable definition of "defect" and "catch" for §4's
      table, stated before rather than after the fact (currently
      reconstructed from the session record).
- [ ] Figures: none yet. Any added must pass the text↔figure consistency
      check before Submission Gate.
- [ ] A context-blind skeptic pass on **this document itself**.
- [ ] The ≥9-item pre-submission `[VERIFIED]` checklist.
- [ ] 24-hour cooling-off after the draft is next declared "ready" —
      not before this list is otherwise complete.
- [ ] Explicit venue decision (arXiv cs.AI/cs.SE per `docs/158`, or
      elsewhere) — not decided in this draft.
