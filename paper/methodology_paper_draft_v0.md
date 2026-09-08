# DRAFT v0.1 · NOT_FOR_SUBMISSION · has NOT passed the Submission Gate

**Status:** revised 2026-09-08 after a context-blind Step 8a skeptic pass
on the v0 draft itself found nine real, independently-verified defects
(one severe enough to change the headline claim) and one technical
challenge that was investigated and resolved in the draft's favor. Full
record: `paper/METHODOLOGY_PAPER_DRAFT_CORRECTIONS_after_step8a.md` — read
it alongside this file; it is not superseded by these edits, it is the
record of why they were made. File paths below are given; **no commit
hashes are given in this file**, correcting a false claim the v0 status
line made. What has **not** happened yet: a second skeptic pass on this
revision, the per-claim `[VERIFIED]`-marker checklist for the *changed*
sections, a text↔figure consistency check, or the mandatory 24-hour
cooling-off period (`~/.claude/rules/integrity.md` § Submission Gate). Do
not quote, cite, or send this document externally until those have run and
a human has said so explicitly.

---

# Context-Blind Adversarial Verification Catches Defects That Naive Verification Misses: A Longitudinal Case Study

## Abstract (draft)

We report a longitudinal, within-project case study of an AI-assisted
research workflow that (a) runs a structured falsification protocol
(pre-registered claim, positive/negative controls, a context-blind
adversarial review step before any result is promoted) and (b) keeps a
permanent, append-only record of every retraction, with root causes
classified against a pre-existing taxonomy. Over a single working session
(2026-09-07), the same protocol found and confirmed defects in **five
research artifacts across two lineages** — one root claim and three
findings independently derived from that claim's own retraction, plus one
unrelated artifact — later confirmed by independent, tool-based
re-verification of every load-bearing claim in each defect report.
**Three of those five are not independent samples of the protocol's
effectiveness; they are downstream residue of the fourth's own review
step**, a fact this draft's own first version initially missed and a
second, context-blind review of the draft itself caught (§4, §8) — which
we report as part of the evidence, not as an embarrassment to edit around.
We characterize the defects by root cause, find that one observed failure
mode is a plausible extension to our own pre-existing 11-category
taxonomy (three others we initially proposed as new turned out, on
inspection prompted by the same review step, to already be instances of
an existing category), and report a separate, pre-registered pilot
benchmark comparing this protocol against an ambient-default baseline,
whose result was **inconclusive** on every reading, including the
original, less favorable one, which we report alongside the corrected one
rather than in its place. We position this as a methodology contribution
independent of the physics domain (cosmological model reconstruction) in
which it was produced — and, doubly so, as its own worked example: a
review pass with no access to why the first draft was written caught
errors the writing process itself could not.

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

1. A same-day, same-project record of **five** artifacts across **two
   lineages** (not six independent ones — see §4, §8), caught by the
   identical protocol, with **every** root cause independently
   re-verified by tool (not accepted on the reviewing agent's word)
   before being counted.
2. A refined failure-mode taxonomy: our own pre-existing 11-category
   taxonomy (`docs/146`) accounted for most observed defects. **One**
   observed pattern (selective section reading, §4.4.2) is proposed as a
   genuinely new extension; three others we initially drafted as new were
   found, under the same review discipline this paper argues for, to
   already be instances of existing Category 4 — reported as a correction
   (§4.4, §8), not silently dropped.
3. An honest, pre-registered pilot benchmark of the protocol against a
   naive baseline, reported as **inconclusive on every reading** —
   including the original, pre-correction reading in which the treatment
   arm *underperformed* the baseline, reported alongside the corrected
   reading rather than in its place (§5).
4. A worked demonstration, inside the writing of this paper itself: a
   second, context-blind review pass on the v0 draft — using the same
   protocol §4 describes — found nine real defects in the draft's own
   claims, including the inflated artifact count in item 1 above. The
   correction record is `paper/METHODOLOGY_PAPER_DRAFT_CORRECTIONS_
   after_step8a.md`. We treat this as evidence for the paper's thesis, not
   noise to be edited away before a reader sees it.

## 2. Protocol (frozen)

The full protocol is the union of:
- `~/.claude/rules/falsification-ladder.md` (Full-Ladder: estimand →
  claim → controls → Step 8a context-blind skeptic → decision)
- `~/.claude/rules/audit-verification-gate.md` (a reviewing agent's own
  `[VERIFIED]` is treated as the primary author's `[INFERRED]` until
  independently re-checked by tool)
- `~/.claude/rules/estimand-ops.md` (L0 gate: descriptive / predictive /
  causal classification before any claim work begins)

Every one of the five case studies in §4 followed this sequence:
(1) write the claim, **with positive controls where the claim was
computational** (true for 2 of 5 — the two purely textual findings had
none, see §4's own note), (2) dispatch a **fresh** review agent with no
access to the session's reasoning history — only the claim document,
plus source file paths — instructed to attempt falsification, not
confirmation, (3) independently re-verify every load-bearing citation the
reviewer returned, by direct tool use (`grep`, re-derivation, re-running
code), before accepting or rejecting anything, (4) if falsified, write a
retraction that keeps the original text verbatim (no silent correction)
and states the specific defect and its root cause.

**Context asymmetry is the load-bearing design choice.** The reviewing
agent never sees why the claim was written, only what it says and what it
rests on — this is what separates step (2) from a second pass by the same
reasoning process that produced the claim.

**The protocol was not followed without deviation, even within this
session, and we disclose the deviations rather than smooth them over.**
Two of the five artifacts record, in their own text, that they had no
Step 8a pass at the time they were written (added afterward, in the
retraction pass). One artifact's own script docstring records a
documented Substrate Gate (Step 2a) violation — an early self-check ran
in an uncommitted, ephemeral script rather than a persisted, re-runnable
one, a gap fixed only after a *second* review pass caught it (see this
paper's own correction record). We read this as consistent with, not
contrary to, the paper's thesis: deviations from a stated protocol get
caught and fixed under continued adversarial review, rather than
accumulating silently.

## 3. Taxonomy (existing)

`docs/146_failure_mode_taxonomy.md` enumerates 11 categories, most with ≥2
real historical incidents from this project (one, Category 8, has exactly
one — corrected here after propagating `docs/146`'s own imprecise
self-description without checking it), established before the session
reported here:

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

## 4. Case studies (this session, 2026-09-07 to 2026-09-08)

**Revised 2026-09-08.** The first version of this section counted six
artifacts and proposed four new taxonomy categories. A context-blind
Step 8a review of the draft itself (§8, and the standalone correction
record `paper/METHODOLOGY_PAPER_DRAFT_CORRECTIONS_after_step8a.md`) found
both counts inflated, for reasons given below. This section states the
corrected counts directly rather than presenting the original ones and
correcting them inline — the original claims and the full reasoning for
each correction are preserved in the correction record, not deleted.

### 4.0 Definitions (stated before the table, not reconstructed after it)

**Defect**, for purposes of this section: a specific, load-bearing claim
in an artifact's headline or verdict that is either (a) contradicted by a
verbatim primary source the artifact itself cites or should have cited,
or (b) contradicted by an independent recomputation using the artifact's
own stated inputs and formulas.

**Catch**, for purposes of this section: the review step (§2, step 2)
returns a specific claim, quote, or computation that meets the Defect
definition above, **and** step 3 (independent re-verification by tool)
confirms it before the finding is accepted. A review-step output that is
*not* independently reconfirmed does not count as a catch under this
definition — this is why every row in §4.1 required my own tool-based
re-check, not just the reviewing agent's report, before being listed.

**Both definitions were written retrospectively for this draft**, after
the case studies happened, not pre-registered before the session began.
This is stated plainly as a limitation (§6) rather than presented as if
it were pre-registered — a genuinely pre-registered version of these
definitions is future work, not a claim made here.

### 4.1 Summary table — five artifacts, two lineages

**Not six independent artifacts.** `P215`, `P216`, and `P217` are not
independent samples — each is explicitly derived from `P214`'s own
retraction (`FINDING_P216_...md:18-22`: *"extracted from `FINDING_P214_
RETRACTION_after_step8a.md` §7.1"*; `FINDING_P217_...md:19-21`: near-
identical language for §7.2; `FINDING_P215_...md:18-20`: *"Answers: the
`NEEDS-REAL-DATA` item raised by the Step 8a skeptic on `P214`"*). The
honest count is **five artifacts in two lineages**: one root claim
(`P214`) and three findings drawn from its own retraction, plus one
unrelated artifact (`P220`).

| # | artifact | headline claim | verdict | dominant taxonomy category |
|---|---|---|---|---|
| 1 | `P214` (root of lineage A) | a version-comparison question was resolved | 4/5 sub-claims falsified | Cat. 9 (numerical/search artifact — singular-only grep) |
| 2 | `P215` (from `P214` §7's survivors) | an external physical bound "survives" | conclusion inverted | Cat. 2 (tautological control) + Cat. 6 (reused known bug) |
| 3 | `P216` (from `P214` §7.1) | an internal scope inconsistency in a source document | falsified — hierarchy misread as conflict | Cat. 8 (heuristic applied without checking the mechanism) |
| 4 | `P217` (from `P214` §7.2) | a cross-version parameter comparison | falsified — one-sided search | Cat. 3 (false independence, applied to a search itself) |
| 5 | `P220` (separate lineage) | multiple, see below | four real defects found, two of four survived scrutiny | Cat. 4 (parameter silently held fixed), Cat. 11 (a mislabeled comparator) |

Row 5 needs its own note. `FINDING_P220_RETRACTION_after_step8a.md`
records **four** distinct defects, not the two the first draft of this
table selectively reported: (i) a nuisance-parameter "T0 scenario" that
is void — an exact algebraic degeneracy, absorbed by refitting; (ii) a
headline `χ²`-inflation claim that is a frozen-parameter artifact,
substantially reduced (not eliminated) once the frozen parameters are
allowed to refit; (iii) a one-dimensional sensitivity scan whose `B`-row
was misread as evidence of "a sharp ridge" when it is mostly ordinary,
absorbable rescaling; (iv) a comparison benchmark (`16.31`) mislabeled
"flat-ΛCDM, Planck values" when it is a two-parameter *fit*, not fixed
Planck values (the true fixed comparator is `36.96`). The first draft of
this table counted only (i) and (ii) — the two it could route to a
category it called new — and dropped (iii) and (iv), one of which
(iv) is a clean instance of existing Category 11. Counting all four
against one artifact is the accurate accounting; splitting the artifact
into as many rows as convenient is not.

### 4.2 Root-cause detail (three worked examples)

**Case 2 (`P215`), Cat. 2 + Cat. 6.** The claim's own positive control
(`PC1`) tuned one free parameter to reproduce one target number — zero
degrees of freedom — and could not fail by construction. Separately, the
claim reproduced a factor-of-2 arithmetic error a **prior finding in the
same directory** (`FINDING_P7`, dated one month earlier) had already
flagged as open. The Step -3 pre-work check (search this project's own
prior work before writing a new claim) was not run.

**Case 4 (`P217`).** The claim swept one parameter's mentions across one
of two source documents, then stated a conclusion about the
**relationship between the two documents**. The same sweep on the second
document, when eventually run, dissolved the claimed asymmetry within
minutes. The defect is not in either individual observation — both were
accurate — but in treating an asymmetry in **search effort** as if it were
an asymmetry in the **sources**.

**Case 5 (`P220`), defect (ii).** A claim froze three fitted parameters
and perturbed two others within their own quoted uncertainty, reporting
the resulting output instability as a property of the model. A kill-test
— re-optimizing the frozen parameters at each perturbed point, which is
mathematically guaranteed to help, never hurt in the exact optimum, since
the frozen point is one member of the re-optimization's own search space
— reduced the claimed effect from a `χ²` of `930.3`/undefined down to
`14.08`/`41.67` at the two tested draws (one of which is now *better*
than the original published value). **Both draws' reduction happens at
the same draw pair, not "one point… and another"** as an earlier version
of this paragraph stated — the correction record has the exact
attribution. A second-order technical concern (whether the specific
reported numbers `14.08`/`41.67` reflected a true, converged optimum, or
an artifact of mismatched numerical grids and an unreached optimizer
tolerance) was itself raised by the same review pass that caught this
paper's other errors, investigated, and resolved: both bugs were real,
both are now fixed, and the corrected numbers are within 0.01 of the
originals with an explicit convergence check attached (correction record
§8). The underlying defect is conflating the sensitivity of an analysis
**protocol** (parameters held fixed) with the sensitivity of the
**target system** (parameters free to compensate) — and is, on
inspection, the same mechanism as existing Category 4 (§4.4).

### 4.3 What the four-artifact lineage shared, and what `P220` did not

**Scoped correction:** the original version of this section claimed "five
of the six" shared one root cause while its own enumeration named all six
artifacts (with one counted twice under two different mechanisms) — a
self-contradiction, caught by the same review pass. The corrected claim is
narrower and accurate: **the four artifacts in lineage A** (`P214`,
`P215`, `P216`, `P217`) share a structural root — **a one-sided procedure
reported as a two-sided or absolute fact**: a search run on one document
and not its counterpart (`P217`), a control with zero degrees of freedom
presented as discriminating (`P215`), a citation drawn from a document's
applied section without checking its self-limiting section (`P216`), and
a search pattern that structurally excluded a morphological variant,
reported as a confirmed absence (`P214`). None of these four required new
data to catch — each was caught by re-running the **same available
information** more symmetrically.

`P220`'s defects are a **different** mechanism — parameter-freezing
artifacts under partial degeneracy (§4.2, Case 5) — and this paper does
not claim they share lineage A's root cause. No project record before
this correction attributed `P220` to the search-asymmetry pattern; only
this paper's uncorrected first draft did, and only by miscounting the
sample.

### 4.4 Taxonomy: one plausible extension, three withdrawn

The first draft of this section proposed four "new" categories. On the
same review discipline this paper argues for, three do not survive
comparison against `docs/146`'s own existing Category 4 ("a parameter
silently held fixed instead of fully scanned"), whose own worked example
(`docs/146:139-160`) is structurally the same as `P220`'s Case 5: a
"collapse" claimed while one parameter sits frozen, dissolved once an
external reviewer asks whether it was actually re-profiled, exactly the
mechanism named in this paper's own §4.2. What the first draft called
protocol-vs-target sensitivity (former §4.4.4) **is** Category 4. What it
called non-exhaustive search reported as confirmed absence (former
§4.4.1) and asymmetric verification effort (former §4.4.3) were never
shown to be distinct from Category 4's own second worked example (a
box-constrained search range whose null result was an artifact of the
box, `docs/146:154-160`) or from each other — both are, at different
scales (a word's morphology vs. a whole second document), "a region of
the available evidence was never checked, and its silence was read as a
finding."

**One extension survives:** **selective section reading** — a source
document containing both an applied section (where a framework or claim
is used) and a self-limiting section (where the same document states
where it does not apply) is read from the first and not the second, even
when the first explicitly cross-references the second (`P216`'s case).
This is not yet shown to be fully distinct from existing Category 6
(reusing a result at a strength its own qualifier withdrew) either — a
genuinely careful distinctness argument is future work, not settled
here. It is reported as the paper's single plausible taxonomy
contribution, down from four, because that is what survived scrutiny.

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

**Result, both readings — corrected 2026-09-08, the first version of this
paragraph reported only the favorable one.** `N=16` (reduced from a
pre-registered `N=32` for session-budget reasons, committed before the
run). **Original scoring:** baseline `13/13=100%` vs. treatment
`12/13=92.3%` — **treatment underperformed baseline** on this reading.
**Corrected scoring**, after a post-hoc (`Addendum 3`, applied
*after* seeing Run 3's results) fix to a scoring-rubric gap — a correctly
hedged, appropriately uncertain output had been scored identically to a
confidently wrong one — both arms detected `12/12`. McNemar's exact test
on the corrected reading: `0` discordant pairs, `p = 1.0` **by
construction**. This is consistent with the underpowered/inconclusive
outcome the pre-registration's own power analysis predicted before any
data existed (`PREREGISTRATION.md`, verbatim: *"A smaller true effect
reads as inconclusive, and must be reported as inconclusive — never as
evidence of no effect"* — quoted directly from the primary source here,
correcting a paraphrase in the first draft of this paragraph that had
drifted from it). **Kill criterion `K1` is not formally met on either
reading, and the first draft's claim that it was is withdrawn**: `K1`
requires *both* `p≥0.05` *and* a discordant ratio between `0.67` and
`1.5` (`PREREGISTRATION.md:188`); with `0` discordant pairs the ratio is
`0/0`, undefined, not inside that band.

**We report both readings, not only the corrected one — the omission of
the original reading was itself a defect this draft's earlier version
had, caught by the same review discipline it describes.** The pilot does
not confirm the protocol's value; it also does not refute it — it was
underpowered by its own design, on a scale set for session-budget
reasons, and it says so before any data existed. The case studies in §4
are not a substitute statistical test; they are a different kind of
evidence (existence proof of real catches, with root causes), and the
paper's contribution rests on both being reported together, honestly
labelled — including the parts of each that turned out to need
correcting — rather than only the flattering reading of either being
kept.

**Open, not resolved here:** the project's own canonical files give at
least three different values for this pilot's sample size in different
places (`N=16`, `N=25`, `N=32`), the larger figures associated with a
reproducibility step (`K5`) that other project records describe as not
yet executed at `N=16`. This is an inconsistency upstream of this paper,
in the project's own state tracking, not resolved by this correction
pass — flagged rather than silently picked one way.

## 6. Limitations (draft, incomplete)

1. **Single project, single domain.** All five case studies and the pilot
   corpus derive from one cosmology-reconstruction project. Generalization
   to other domains is untested.
2. **Independent verification strength.** Per this project's own
   Independent Verification Strength Ladder, the review agent used
   throughout is "same model, isolated context" — the weakest tier that
   still counts as independent. No cross-model or human replication has
   been run on any of the five case studies. This is sharper than it looks: three of the five are not independent of a fourth (§4.1), so the effective sample for anything claiming breadth of coverage is closer to two independent lineages, not five.
3. **Sample size.** Five case studies in two lineages, in one day, is suggestive, not
   statistical. The pilot benchmark is the attempt at a statistical test
   and is reported as inconclusive (§5).
4. **Author-verifier is the same person across all re-verifications**
   in §4 — I (the primary agent) independently re-checked the reviewing
   agent's citations in every case, but I am not independent of the
   overall session. A stronger design would use a different verifier for
   this re-check step too.
5. **Selection into the record.** All five case studies are claims that
   this project itself produced and then reviewed — there is no
   claims-that-were-never-reviewed comparison group, so we cannot report
   a "catch rate" as a fraction of all claims made, only that five for five reviewed claims were found defective.
6. **The §4.0 definitions of "defect" and "catch" are retrospective, not
   pre-registered.** They were written after the case studies had
   already concluded, to make the summary table in §4.1 auditable — which
   is a real improvement over stating no definition at all, but is not
   the same evidentiary standard as a definition fixed before the data
   existed. A stronger version of this work would state the definitions
   first, then run the protocol forward against them.
7. **This draft itself needed a correction pass** (§8) — the v0 version overstated its own sample size and taxonomy-novelty claims in exactly the shapes this paper catalogs. We count this as supporting evidence for the thesis, but a reader should weigh that the authors' own first attempt at objectively counting their own results was itself inflated, and ask what that implies about claims in this paper that have not yet had a second review pass.

## 7. Related work

**Verification method for this section, stated explicitly:** every entry
below was re-checked against arXiv/Semantic Scholar on 2026-09-07,
independent of whatever prompted the name to be listed originally — this
project's own `~/.claude/rules/integrity.md` treats a citation recalled
from memory as `[UNKNOWN]` until it is. One candidate citation from an
earlier list did not survive this check (see the explicit `SOURCE_NOT_
FOUND` entry below) and is reported as such, not quietly dropped.

- **Cross-Context Review** (Tae-Eun Song, `arXiv:2603.12123`, *"Cross-
  Context Review: Improving LLM Output Quality by Separating Production
  and Review Sessions"*, 2026-03-12) — closest design template: review in
  a fresh session with no access to the producing session, i.e. the same
  context-asymmetry principle this work calls "context-blind." Different
  domain (general LLM output quality, not computational-science claims),
  and reports a paired quantitative comparison rather than a taxonomy of
  root causes.
- **"The Calibration Turn"** (Hongmin Li, `arXiv:2606.31273`, *"The
  Calibration Turn in AI-Assisted Research: A Conceptual and
  Methodological Framework for Evidence-Licensed Claims"*, 2026-06-30) —
  near-identical conceptual vocabulary (claims calibrated to evidence);
  a Perspective-style framework paper with **no empirical benchmark**.
  This work is a candidate first empirical instantiation of that
  framework, not a replication of it.
- **SPOT** (Guijin Son et al., `arXiv:2505.11855`, *"When AI Co-Scientists
  Fail: SPOT — a Benchmark for Automated Verification of Scientific
  Research"*, 2025-05-17) — 83 published papers paired with 91 real
  errors serious enough to have prompted errata or retraction,
  cross-validated with the original authors. Best LLM verifier reported
  at ≤21.1% recall / ≤6.1% precision. Directly comparable in spirit (LLMs
  as verifiers of scientific claims); evaluates verifier **models**
  against a fixed, pre-existing error set, not a **protocol** applied to
  artifacts the same system produced.
- **BadScientist** (Fengqing Jiang et al., `arXiv:2510.18003`, *"BadScientist:
  Can a Research Agent Write Convincing but Unsound Papers that Fool LLM
  Reviewers?"*, 2025-10-20) — the adversarial-generation mirror of this
  work's question: instead of asking whether a protocol catches induced
  defects, asks whether an unsound paper can be written to evade LLM
  reviewers. Complementary threat model, same broad concern (AI-generated
  research evading AI-based review).
- **ReFACT** (Yindong Wang et al., *"ReFACT: A Benchmark for Scientific
  Confabulation Detection with Positional Error Annotations"*, EACL 2026,
  1,001 expert-annotated QA pairs from r/AskScience) — a genuine benchmark
  of the same broad kind (LLM-detectable scientific error), but the task
  is span-level confabulation detection in short answers, not defect
  detection in extended research artifacts; reports LLM-as-judge
  comparative detection is *harder* than independent detection, a finding
  worth engaging with directly if this draft's own evaluator design is
  ever extended to comparative judgments.
- **SoundnessBench — name collision, resolved by reading both.** Two
  distinct papers share this exact title:
  - `arXiv:2412.03154`, *"SoundnessBench: A Soundness Benchmark for Neural
    Network Verifiers"* (2024-12-04) — **not relevant**, a formal-methods
    benchmark for NN verification tools, unrelated to research-claim
    review.
  - `arXiv:2605.30329`, *"SoundnessBench: Can Your AI Scientist Really
    Tell Good Research Ideas from Bad Ones?"* (2026-05-28) — **this is the
    relevant one**: tests whether LLMs can judge the methodological
    viability of research ideas, a generation-time analogue of this
    work's post-hoc verification question.
  Citing this benchmark by name alone, without the arXiv ID, would be
  genuinely ambiguous — worth flagging for anyone extending this related
  work section later.
- **`[SOURCE_NOT_FOUND]` — "FLAWS."** Listed as a seeded-error code-review
  benchmark in an earlier working list (`docs/158`) without a citation
  attached. Searched arXiv (title search, `186` results for the bare
  string "flaws," none matching a benchmark by this name) and Semantic
  Scholar (rate-limited on this specific query at check time — retry
  before submission, do not re-add the name without a result). No
  matching paper found. Per `integrity.md`'s hard rule against phantom
  sources: **removed from the citation list**, kept here only as a record
  of the check having been run, not as a citation.

**What genuinely distinguishes this work from all six sources above:**
none combine (a) a fixed, pre-registered protocol, (b) applied
longitudinally to a project's **own**, not externally-seeded, output,
(c) with every defect's root cause independently re-verified by tool
before being counted, and (d) an honestly-reported null result from a
companion quantitative pilot presented alongside the qualitative case
studies rather than instead of them.

## 8. This draft's own Step 8a pass — reported as evidence, not hidden

The v0 draft of this paper was itself given a context-blind Step 8a
review, using the identical protocol §2 describes: a fresh review agent,
the draft's text plus source paths only, no access to why any sentence
was written, instructed to attempt falsification. It found nine real
defects, independently re-verified by me by direct tool use before
acceptance, and one technical challenge to a numerical claim that was
investigated and — unlike the nine — resolved in the draft's favor after
a genuine code fix. Full record: `paper/METHODOLOGY_PAPER_DRAFT_
CORRECTIONS_after_step8a.md`.

The defects found were, in outline: the "six independent artifacts"
claim (three were downstream of a fourth's own retraction, §4.1); a
self-contradictory sentence in the original §4.3 (naming "five of six"
while enumerating all six, with one counted twice); two of four proposed
taxonomy extensions found to already exist under a different name in
`docs/146` (§4.4); an artifact-count inflation in §4.1 (one artifact
split into two rows to route it to a "new" category, dropping two of its
four real defects, one of which was itself an instance of an existing
category); the omission of an unfavorable statistical reading in the
original §5 (§5); a kill-criterion claimed as formally met when its own
stated threshold was not satisfied on either reading (§5); a misquote of
a primary source, copied from an already-altered secondary paraphrase
instead of the primary document (§5); a phantom internal cross-reference
to content that does not exist (§4.0); and a false claim, in this draft's
own status header, that commit hashes were given throughout the text —
none were.

**We are reporting this rather than quietly fixing it and presenting a
clean v0.1 as if it had been correct from the start**, for the same
reason the case studies in §4 are reported with their own defects intact
in the correction record rather than silently rewritten: a paper whose
central claim is that adversarial review catches real errors is not
credible if it hides the errors adversarial review found in itself. This
section is, in effect, a seventh case study — one the paper's authors
did not choose, produced by the same mechanism §4 describes, on the
paper describing that mechanism.

## 9. What this draft still needs before Submission Gate

- [x] Fill §7 with verified citations (DOI/arXiv IDs), not from memory —
      done 2026-09-07; one candidate (`FLAWS`) did not survive the check
      and was removed, not silently dropped.
- [x] A precise, checkable definition of "defect" and "catch" for §4's
      table — done 2026-09-07 (§4.0); stated explicitly as
      **retrospective, not pre-registered**, which is itself flagged as a
      limitation rather than hidden.
- [ ] Figures: none yet. Any added must pass the text↔figure consistency
      check before Submission Gate.
- [x] A context-blind skeptic pass on **this document itself** —
      **dispatched 2026-09-07, returned and fully incorporated
      2026-09-08.** `integrity.md` Gate 1. Nine defects confirmed real
      and corrected (§8, correction record); one technical challenge
      investigated and resolved without a text change (correction
      record §8). **This checklist item is done, but its own completion
      changed §1, §4, and §5 substantially — this is not a pass that
      left the surrounding text untouched.**
- [x] Per-claim `[VERIFIED]`-marker checklist (`integrity.md` Gate 2 —
      *"every claim in the artifact carries an Evidence Marker"*; no
      fixed count is specified there):

  | claim | status |
  |---|---|
  | Five artifacts exist across two lineages, each found defective per §4.0's definition | `[VERIFIED]` against the three retraction files, re-checked after the skeptic pass corrected the count from six |
  | `docs/146` has 11 pre-existing categories, most (not all) with ≥2 incidents | `[VERIFIED]` — direct `grep`, Category 8 has exactly 1 |
  | AVB pilot: original 13/13 vs 12/13, corrected 12/12, `N` inconsistent across project files | `[VERIFIED]` against `result_summary.md`, `PREREGISTRATION.md`; `N` inconsistency `[VERIFIED]` and left open (§5) |
  | Refit numbers `14.08` / `41.67` (§4.2 Case 5) | `[VERIFIED]` — re-ran the corrected `P220_joint_BC_uncertainty_propagation.py` (unified grid, checked convergence) myself, both hold with `any_start_converged=True` |
  | "Refit mathematically guaranteed to help, never hurt" (in the exact optimum) | `[VERIFIED]` for the inequality itself; the specific reported numbers are now backed by an explicit convergence check, which they were not before |
  | §7 related-work citations | `[VERIFIED]` — each re-checked against arXiv/Semantic Scholar, one (`FLAWS`) removed as `[SOURCE_NOT_FOUND]` |
  | §4.4's taxonomy-extension count | `[VERIFIED]` — corrected from 4 claimed to 1 surviving, against direct comparison with `docs/146` Category 4's own worked examples |
  | §4.3's root-cause scope | `[VERIFIED]` — corrected from "5 of 6" (self-contradictory, all 6 enumerated) to "4 of 5, `P220` excluded" |

- [ ] 24-hour cooling-off after the draft is next declared "ready" —
      not before this list is otherwise complete.
- [ ] Explicit venue decision (arXiv cs.AI/cs.SE per `docs/158`, or
      elsewhere) — not decided in this draft.
