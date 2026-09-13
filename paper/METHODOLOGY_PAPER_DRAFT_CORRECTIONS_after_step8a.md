# Corrections to `methodology_paper_draft_v0.md` after a context-blind
# Step 8a skeptic pass on the draft itself

**Date:** 2026-09-08
**Method:** one context-blind Step 8a skeptic pass on the full paper draft,
given only the document text plus source paths — no session history.
**Every load-bearing claim below was independently re-verified by me**
before acceptance (`audit-verification-gate.md`: the skeptic's `[VERIFIED]`
= my `[INFERRED]` until re-checked). Nine defects confirmed real; one
technical challenge investigated and resolved in the paper's favor.
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`

---

## 0. Verdict

**The paper's central thesis (context-blind review catches real defects) is
not damaged — this correction document is itself a demonstration of it.**
But the draft contained real, independently-verified errors, several severe
enough that the headline claims need to change: "six independent artifacts"
is not supportable as written, and §4.3's synthesis sentence contradicts
its own enumeration. This is the paper's own Category 10 (recomposition
overclaim) and Category 3 (false independence), found in the paper itself.

---

## 1. "Six independently-produced artifacts" — not supportable as written

`[VERIFIED-source]`, re-read directly:

- `FINDING_P216_v82_internal_scope_inconsistency.md:18-22`: *"**Provenance:**
  extracted from `FINDING_P214_RETRACTION_after_step8a.md` §7.1 — one of two
  results that survived that retraction and had until now no record of its
  own."*
- `FINDING_P217_beta_universality_axis_swapped_between_versions.md:19-21`:
  *"**Provenance:** extracted and **sharpened** from
  `FINDING_P214_RETRACTION_after_step8a.md` §7.2, the second of two results
  that survived that retraction with no record of its own."*
- `FINDING_P215_periastron_survives_on_degenerate_energy.md:18-20`:
  *"**Answers:** the `NEEDS-REAL-DATA` item raised by the Step 8a skeptic on
  `P214`…"*

Three of the six "independent" artifacts are explicitly derived from a
fourth (`P214`)'s own retraction. This is the paper's own Category 3 (false
independence — hidden shared machinery), applied to its own sample, and it
is stated in the paper's cited sources in the paper's own words almost
verbatim — the paper simply did not check.

**Fix:** the abstract, §1.3, and §4's framing must not say "six
independently-produced" or "six independent artifacts." A defensible
restatement: *five artifacts across two lineages — one root claim (`P214`)
and three findings extracted from its own retraction, plus one independent
lineage (`P220`)*.

## 2. §4.3's own enumeration contradicts its "five of the six" claim

`[VERIFIED]`, direct re-read of `methodology_paper_draft_v0.md:206-217`:

> *"…five of the six shared a structural root… a search run on one document
> and not its counterpart (**Case 4**), a control with zero degrees of
> freedom presented as discriminating (**Case 2**), a parameter held fixed
> and its resulting instability presented as intrinsic (**Cases 5, 6**), a
> citation drawn from a document's applied section without checking its
> self-limiting section (**Cases 1, 3, 5**)."*

Cases named: 4, 2, 5, 6, 1, 3, 5 — that is all six, with **Case 5 counted
twice** under two different, mutually-exclusive mechanisms (§4.1's own note,
written two paragraphs earlier, explicitly separates the "parameter-freezing"
mechanism from the "search asymmetry" mechanism and calls conflating them a
mistake already caught once). §4.3 re-commits the exact error §4.1 says was
corrected.

Also unsourced: Case 1 (`P214`)'s assignment to "selective section reading."
`FINDING_P214_RETRACTION_after_step8a.md` §6 attributes its own error
elsewhere: *"The zero-hit greps that P214 leaned on were run
**singular-only**… I checked for glued words and did not check for
plurals."* No self-limiting-section failure is recorded for `P214` anywhere
in its own retraction.

**Fix:** §4.3 needs to be rewritten at the scope its sources actually
support. The "one-sided procedure" frame is attributed, in the project's own
canonical files, to **P214/P215/P216/P217 only**
(`CURRENT_EVIDENCE_STATE.md:539-541`, `CLAUDE.md` PROCESS RULES) — never to
`P220`, whose own retraction names a different mechanism (*"conflating the
sensitivity of an analysis protocol with… the target system"*). §4.3 must
not extend a four-artifact pattern to six.

## 3. "Four patterns not covered by the taxonomy" — at least two overlap with existing categories

`[VERIFIED-source]`, `docs/146_failure_mode_taxonomy.md:139-167` (Category
4, "a parameter silently held fixed instead of fully scanned"), its own
worked example:

> *"PASS-B v3 claimed 'no eta_d works, r collapses to 0.145' — an external
> reviewer asked 'was eta_q profiled at every eta_d, or fixed?' — it turned
> out eta_q was silently fixed at 0. A correct profile (eta_q minimized at
> every eta_d) stays in the range r=0.60-0.73 and **never collapses**… 'v3's
> wall is withdrawn.'"*

Mapped onto Case 6 (`P220`): a parameter frozen (`β₁,β₂,H0` ↔ `eta_q`); a
scan over the others (`B,C` ↔ `eta_d`); a collapse claimed; re-profiling
dissolves it. Same mechanism, same detection method (an external question:
"was this re-profiled or fixed?"), same outcome ("wall withdrawn"). §4.4.4
is Category 4, not new.

§4.4.1 (non-exhaustive search) is not shown to be distinct from Category 4
either — Category 4's second worked example (`docs/146:154-160`) is exactly
a search-space that structurally excludes a region and reports the
resulting null as a genuine absence (a box-constrained optimizer's default
range that never includes `β_d` near zero, `NR-013`'s "box-excluded-baseline
artifact"). And §4.4.1 is not distinguished from §4.4.3 (asymmetric
verification effort) either — both are "a region of the available evidence
was never checked and its silence was read as a finding," at the scale of a
morphological variant (4.4.1) vs a whole second document (4.4.3).

**Fix:** withdraw the "four new categories" framing. Only §4.4.2 (selective
section reading) survives scrutiny as plausibly novel, and even that needs
an explicit distinctness argument against Category 6 (reusing a
result at a strength its own qualifier withdrew) before being claimed as new.

## 4. §3's "each with ≥2 real historical incidents" is false for Category 8

`[VERIFIED-source]`, `docs/146_failure_mode_taxonomy.md:252-263` (Category
8) lists exactly **one** incident (`P23`). `docs/146:423` itself already
says *"только даёт по 2-4 конкретных… примера на категорию"* is not
uniformly true. The paper propagated this without checking — itself an
instance of the paper's own Category 11.

**Fix:** change "each with ≥2 real historical incidents" to "most with ≥2,"
or state the true minimum (1, for Category 8).

## 5. §5's characterization of the AVB pilot has four separate defects

`[VERIFIED-source]` against `result_summary.md` and `PREREGISTRATION.md`:

**5a. The unfavorable original reading is omitted.** `result_summary.md:
29-35` explicitly preserves it: *"Original (pre-Addendum-3) figure, kept for
transparency, not silently replaced: counting task 004's hedge as a miss
gave baseline 13/13=100% vs. **treatment 12/13=92.3%**"* — treatment
*underperformed* baseline on the original reading. §5 states only the
corrected 12/12 tie, immediately followed by *"We report this without
softening it,"* which the omission itself contradicts.

**5b. Addendum 3 (the rubric fix that produced the 12/12 tie) was
post-hoc**, applied after seeing the results. `PREREGISTRATION.md:274`:
*"## Addendum 3 (2026-09-02, **post-Run-3**, autonomous follow-up)."* §5
cites "Addendum 3" without disclosing this timing.

**5c. "Kill criterion K1… is formally met" is false under the
pre-registration's own threshold.** `PREREGISTRATION.md:188`: K1 requires
*"p≥0.05 **AND** discordant ratio… between 0.67 and 1.5… only if **BOTH**
conditions hold."* With 0 discordant pairs the ratio is 0/0, undefined —
not inside [0.67, 1.5]. K1 does not formally fire on either reading. There
is also an internal contradiction: K1's stated consequence is *"report as
null, **not** inconclusive"* — the paper reports the result as inconclusive
while simultaneously claiming K1 is met; both cannot be true.

**5d. The quoted pre-registration text is not verbatim.** Paper: *"a
smaller true effect **will read** as inconclusive… **not as** evidence of no
effect."* `PREREGISTRATION.md:81-83`: *"A smaller true effect **reads** as
inconclusive… **never as** evidence of no effect."* The wording matches
`result_summary.md`'s own (already-altered) paraphrase, not the primary
source — meaning the paper quoted a summary while its own stated method was
verifying against primary sources.

**Fix:** restore the 13/13-vs-12/13 figure explicitly; label Addendum 3 as
post-hoc; remove or correct the "K1 is formally met" claim; fix the
quotation to match `PREREGISTRATION.md` verbatim.

## 6. Two internal, self-contained defects (no source file needed)

**6a. Phantom cross-reference.** §4.0: *"(§4.2's 'Case 4' note on
`κ`-notation is an example of the latter, and is not counted in the six)."*
§4.2's actual Case 4 paragraph is entirely about `P217`'s one-sided sweep
and contains **no** `κ` note. `κ` appears exactly once in the whole draft —
in this dangling reference to content that does not exist.

**6b. "Commit hashes… given throughout" is false.** The status header
(line 4-5) makes this claim; **zero** commit hashes appear anywhere in the
document body (`[VERIFIED]`, direct grep — only file paths are given).

**6c. Internally inconsistent magnitude for the same measurement.** §4.1
row 6: *"real effect **~40x** smaller"*; §4.2 same case: *"reduced… by
roughly **two orders of magnitude** [~100x]"*. `FINDING_P220_RETRACTION_
after_step8a.md`'s own table gives `930.3 → 14.08` (66×) at one draw and
`NaN → 41.67` (no ratio computable, since the frozen value is undefined) at
the other — neither 40 nor 100. §4.2 also states the reduction and the sign
reversal happened at *"one test point… and… another"* — the retraction's
own table shows **both** occur at the same draw (`C=−1.30`); the other draw
(`C=−0.71`) has a frozen value of `NaN`, so no ratio exists there at all.

**Fix:** correct the ratio to the actual table values, remove the phantom
`κ` reference (or write the note it should point to), remove the false
commit-hash claim, and fix which draw does what.

## 7. §2's "every one of the six followed this exact sequence" overstates the record

`[VERIFIED]`, direct search: `FINDING_P216_...md` and `FINDING_P217_...md`
contain **zero** occurrences of "positive control," "negative control," or
"controls" of any kind (`grep` returned nothing). Only `P215` and `P220`
have controls. `FINDING_P216_...md:151-153` and `FINDING_P217_...md:172`
each separately record *"No Step 8a pass on [this] itself"* at time of
writing. And `P220_joint_BC_uncertainty_propagation.py`'s own docstring
records a **documented Step 2a (Substrate Gate) violation** in the artifact
`§2` cites as the frozen protocol: an early self-check ran in an
"ephemeral, UNCOMMITTED script… a Gate-1/FL-Step-2a violation."

**Fix:** §2 must qualify "with positive controls" (true for 2 of the
underlying findings, not all), and disclose that the protocol was not
followed without deviation even within this session — which, stated
honestly, is itself consistent with and supportive of the paper's own
thesis (deviations get caught and corrected, not hidden).

## 8. Technical challenge to Case 6's refit numbers — investigated, and the numbers survive

The skeptic pass separately raised a code-level concern about
`P220_joint_BC_uncertainty_propagation.py`'s `refit_chi2` function:
(i) the frozen comparison (`chi2_33`) and the refit comparison
(`chi2_free`, as it then was) integrated on two **different** grids
(600-point `ZFINE` vs 500-point `ZFINE_REFIT`), so `χ²_refit ≤ χ²_frozen`'s
mathematical guarantee did not strictly apply to the two numbers as
computed; (ii) `Nelder-Mead`'s `xatol=1e-3` was an **absolute** tolerance
against a parameter (`β₂ ≈ 7.8×10¹⁷`) where float64 spacing is `~10²` —
unreachable in raw units — and `r.success` was never checked, so
convergence was never actually certified.

Both are real, and both are now `[FIXED]` in
`P220_joint_BC_uncertainty_propagation.py`: both objectives now share
`ZFINE`; the optimizer runs in rescaled coordinates (`x = params /
published_fit`, the same convention `FINDING_P176` already established and
verified for exactly this reason); `r.success` is checked and reported.

**Re-run result** `[VERIFIED-tool]`:

```
chi2_free(at published point) = 15.751761  vs chi2_33(mean) = 15.751567
  (differ in the 5th decimal -- residual float/interpolation-order noise,
  not a methodological gap)

refit at (B,C) = published mean : chi2 = 15.7515  any_start_converged=True
C = -1.30 (-1 sigma): chi2_refit = 14.0798  (frozen was 930.33)  any_start_converged=True
C = -0.71 (+1 sigma): chi2_refit = 41.6697  (frozen was NaN)     any_start_converged=True
```

**The headline numbers (`14.08`, `41.67`) are essentially unchanged, and now
carry an actual convergence certificate they lacked before.** The skeptic's
technical challenge was real and worth fixing, but the specific conclusion
it targeted survives — this is a case where the challenge improved the
artifact's rigor without changing its verdict, and is reported as such
rather than folded silently into "confirmed" or overstated as "refuted."

## 9. What was not independently re-verified, stated plainly

- §7's arXiv IDs — the skeptic pass itself had no network access and could
  not check them; they were independently verified by me in the prior
  session turn (direct `mcp__arxiv__search_papers` calls, IDs and titles
  matched exactly) before this correction round, so this is not an open
  item, but it is worth recording that the skeptic pass itself flagged it
  as `[NEEDS-REAL-DATA]` rather than confirming it.
- The exact leakage question (Test 6e in the skeptic's own report: does
  `FINDING_P215_...md` §1.5's citation of `P7:160-166`/`P7:173` — a file
  outside the three retractions' own listed source paths — indicate the
  review step exceeded "only the claim document and the artifact, verbatim"
  as §2 describes it) is **not resolved**. The raw dispatch prompts are not
  in the repository. Left open, not asserted either way.

## 10. Which N is the AVB pilot — flagged, not resolved here

`result_summary.md:1` says `N=16`; `CURRENT_EVIDENCE_STATE.md:34-36` cites
an `N=32` corpus with a `K5` reproducibility step the pre-registration
elsewhere says was "not yet executed" at `N=16`; a third location cites
`N=25`. This is a real inconsistency in the project's own canonical record,
**upstream of the paper** — not something to silently resolve by picking
one. Flagged here; needs a separate pass on the project's own state files,
out of scope for this correction document.

**Corrected 2026-09-08 (same day, follow-up pass — see §11 below): this
was not actually an inconsistency, and it was resolvable, and it did not
require a separate pass on the project's own state files. It required
reading two files that already existed.** Section 10 above is preserved
verbatim, per this document's own no-silent-correction discipline — it
was an honest statement of what had been checked at the time it was
written, and it undersold how easily the gap actually closed.

---

## 11. Follow-up pass, 2026-09-08 (separate from Pass 1 above): a second
## context-blind skeptic review, and the N=16/25/32 resolution

**This section documents work done AFTER §§1-10 above, in a later turn
of the same day.** It is not part of the original Step 8a pass this
document's header describes — it combines two separate things: (a) a
genuinely second, independent context-blind Step 8a pass on the *v0.1*
draft (the one produced by §§1-10's corrections), dispatched fresh with
no access to what §§1-10 found; and (b) a self-directed follow-up on
this document's own §10, which had flagged the `N` question as
"upstream… out of scope" without actually checking whether it was.

### 11a. The N=16/25/32 "inconsistency" was not upstream, and was not an
### inconsistency

Following up on §10's own flag, `Grep` for `N=16`/`N=25`/`N=32` across
the project surfaced two files neither the original paper draft nor §10
above had read: `experiments/adversarial-verification-benchmark/
result_summary_extension.md` and `experiments/adversarial-verification-
benchmark/independent_verification_report.md`, **both dated 2026-09-02**
— six days before this paper's v0 draft was first written. Reading them
in full:

- `result_summary.md` (`N=16`) is the **first** batch.
- `result_summary_extension.md` (`N=16`) is a **second** batch
  (`manifest2.json`, tasks 012-031) that **completes** the originally
  pre-registered `N=32` design — its own opening line: *"This document
  covers the SECOND 16-task batch… that completes the originally
  pre-registered 32-task corpus. It does not edit or supersede
  `result_summary.md`… both stand, and a combined reading is given at
  the end of this file."*
- The combined reading (`result_summary_extension.md` §"Combined
  reading," `independent_verification_report.md` in full) reports
  `n=25` non-hedged defect pairs (`N=32` minus 6 clean-control tasks
  minus 1 appropriately-hedged pair excluded per the first batch's own
  `Addendum 3` precedent), baseline `24/25=96.0%`, treatment
  `25/25=100%`, `1` discordant pair, McNemar `p=1.0` — and `K5`
  reproducibility **was run and passed** (`95%`, `19/20`) on this
  extension batch, contrary to what `CURRENT_EVIDENCE_STATE.md`'s
  phrasing (quoted, out of context, in §10 above) could be read as
  implying.

**`N=16`, `N=25`, and `N=32` are not three competing values for one
quantity — they are three different, correctly-labelled quantities**
(a single batch's size; the non-hedged-pair count; the total design
size). §10's framing ("at least three different values… in different
places") was accurate about the raw grep result and wrong about what it
meant — a real example, inside this paper's own correction history, of
mistaking "I found conflicting-looking numbers" for "the numbers
conflict" without reading far enough to check. **Fix applied:** §5 of
the paper was rewritten to report the completed `N=32` design, the
combined `n=25` primary comparison, the passed `K5` check, and — the
most substantively interesting part of the whole pilot, previously
absent from the paper entirely — the reproduced finding that `0` of `6`
clean-control tasks were found actually clean across both independent
batches. §1.3 (contribution 3) and the abstract were updated to match.

**Why this counts as a real finding for this paper's own thesis, not
just a paperwork fix:** the gap here was not a defect an adversarial
reviewer had to catch — it was a completeness gap this paper's own
authors introduced by not checking whether a flagged "inconsistency"
was actually one before flagging it as unresolved. It is reported here
with the same discipline §§1-10 use for the Step 8a defects, because
the discipline should not apply only to errors an external pass finds.

### 11b. Second Step 8a pass on v0.1 — `WEAKENED`, four minor defects

A fresh context-blind Step 8a review was dispatched on the v0.1 draft
(the output of §§1-10's corrections), given only the document and its
cited source paths, instructed to attempt falsification with no framing
suggesting a prior pass had already happened. Verdict: **`WEAKENED`** —
four defects found, all internal-consistency or wording issues, none
overturning a headline claim. Eleven separate falsification attempts
against other claims (lineage-derivation citations, refit numbers, the
verbatim `PREREGISTRATION.md` quote, the `K1` reasoning, Category 8's
count, docs/146's Category-4 citation, the five-artifacts/two-lineages
count) did not break the paper — recorded as such, per this project's
own skeptic protocol, not omitted.

**Defect 1 — §8 said "two of four" while §1.3, §4.4, and §9 all say
"three of four."** `[VERIFIED]` by direct re-read of all four locations
in the then-current text. §8's outline paragraph was the outlier; fixed
to "three of four," matching the rest of the paper.

**Defect 2 — §4.1 row 5's "two of four survived scrutiny" contradicted
its own accompanying paragraph**, which states all four of `P220`'s
defects are accurate ("Counting all four against one artifact is the
accurate accounting"). `[VERIFIED]` — the phrase was a leftover from an
earlier draft state and did not describe anything the current text
actually argues. Fixed to remove the unsupported fraction.

**Defect 3 — §4.2 Case 5's "Both draws' reduction happens at the same
draw pair" was confusing to the point of being misleading.** Only one
draw (`C=−1.30`) has a computable reduction at all; the other
(`C=−0.71`) goes from an undefined frozen-parameter `NaN` to a real,
converged `41.67` — not a "reduction," since there is nothing at that
draw to reduce *from*. `[VERIFIED]` against `FINDING_P220_RETRACTION_
after_step8a.md`'s own table. Fixed to state the two draws' outcomes
separately and correctly.

**Defect 4 — §8's own "nine defects" outline was itself incomplete.**
Three fixes that Pass 1 actually made and that are visible in the
current text — the Category 8 incident-count correction (§3), the
disclosure that `Addendum 3` was post-hoc (§5), and the `~40x`-vs-
`two orders of magnitude` fix (§4.2) — were never named in §8's
summary paragraph. `[VERIFIED]` by cross-checking §8's list against
§§1-10 of this document. Fixed by adding an explicit note in §8 that
its own outline is a summary, not an exhaustive inventory, naming the
three omitted items and pointing to this document as the complete
record.

**None of the four changes a number, a verdict, or a headline claim
anywhere in the paper.** All four are now fixed in the current text of
`methodology_paper_draft_v0.md`.

### 11c. Evaluator-Optimizer Guard status

Per `~/.claude/CLAUDE.md`'s Evaluator-Optimizer Guard (reviewer↔builder
cycles capped at 3): this is the **second** of at most three cycles
(Pass 1 → fix → Pass 2 → fix, now complete). A third pass is not run
here — it would need a specific reason (a further self-directed finding,
or a user request), not run reflexively up to the cap.

## 12. Pass 4 (2026-09-13) — third and final Step 8a content-adversarial-
## review cycle, user-requested claim-by-claim adversarial pass. Cap now
## CLOSED (3 of 3).

**Date:** 2026-09-13
**Trigger:** explicit user request to run a "claim-by-claim adversarial
pass" on the paper, as part of a broader program-closeout consolidation
(`PROGRAM_CLOSEOUT_LEDGER.md`, frozen baseline 2026-09-13) — not a
reflexive run to the Evaluator-Optimizer Guard's cap.
**Method:** (1) direct, tool-based verification by me of a sample of the
paper's own load-bearing claims BEFORE dispatching a skeptic (docs/146's
11-category count and Category 8's single-incident count; Category 4's
cited line-range content; P215/P216/P217/P220's own provenance lines;
every §5 AVB number against `result_summary.md`/`result_summary_
extension.md`; the two figure scripts' own assertion logic; the
correction record's own "nine defects" header count) — all CONFIRMED
CLEAN, zero discrepancies. (2) A fresh, context-blind Step 8a skeptic
dispatch on the CURRENT full v0.3 text, per the identical protocol §2 of
the paper itself describes (only the draft text + source file paths, no
session history). (3) Independent re-verification of every finding the
skeptic returned, including live re-fetching of external sources
(arXiv), before accepting or rejecting anything — the same discipline
`audit-verification-gate.md` requires for any agent's own `[VERIFIED]`.

**Skeptic verdict as returned: FALSIFIED** (one load-bearing issue) +
5 WEAKENED-level items. **Independent re-verification found the
FALSIFIED verdict itself needed calibrating** (per this repo's own
`audit-verification-gate.md`: a skeptic's own claim is `[INFERRED]`
until re-checked, not accepted at face value) — see below.

### 12.1 The "4 vs 3" finding — real, but not a literal contradiction

**Skeptic's claim:** the status header says Pass 2 found "four minor
internal-consistency/wording defects," but §8's own narrative paragraph
enumerates only three ("all three were found and fixed by the same
pass"), reading as if Pass 2 found only three in total.

**Independent re-verification:** checked §9's own checklist (not quoted
to the skeptic, since the dispatch gave the full document — but the
skeptic's own report shows it weighted §8's narrative paragraph over
§9's checklist). §9's checklist **does** enumerate exactly four Pass-2
items: (1) §8's "two of four" vs. the rest of the paper's "three of
four" phrasing, (2) §4.1 row 5's "two of four" phrasing, (3) §4.2 Case
5's "same draw pair" sentence, (4) §8's own defect list being incomplete
relative to the correction record. §8's "all three" sentence is
describing the THREE SPECIFIC OMISSIONS that item (4) itself names —
not a claim that Pass 2 found three defects in total. The header (four)
and §9 (four items) are mutually consistent; only §8's own narrative
paragraph fails to say so explicitly, which is why a careful reader
(the skeptic) could reasonably misread it as a global count.

**Verdict, recalibrated:** not a literal 4≠3 contradiction (both counts
are 4, once §9 is read) — a real self-containment gap in §8: a reader
should not need to cross-reference a checklist in a different section to
avoid miscounting a headline number, and this paper's own standard
(§6 item 7, and its whole thesis) is exactly this kind of undercounting.
**Fixed** (§8's paragraph now names the true total and points to why the
"three" is a sub-count, not the whole count) — see `methodology_paper_
draft_v0.md` §8's own 2026-09-13 correction note.

### 12.2 W1 — §1.3 item 4's "second... pass" wording

**Confirmed real.** "A second, context-blind review pass on the v0
draft" is ambiguous against the header's own Pass-1/Pass-2 numbering
(Pass 1 is the pass ON v0; Pass 2 is on v0.1) — a reader could misread
"second" as referring to Pass 2. **Fixed**: reworded to explicitly name
Pass 1 and disambiguate from Pass 2.

### 12.3 W2 — §7 citation suspicion — CHECKED, FULLY CLEAN, no fix needed

**Skeptic's concern:** three arXiv IDs "on the high end of plausible"
paper-numbers, plus SPOT's "≤21.1% recall / ≤6.1% precision" framed as
an unusual reporting convention.

**Independent re-verification (live arXiv fetch, all six citations, not
just the three flagged):** all six papers exist, real, matching titles/
authors, and every specific number or characterization the draft uses
matches the source abstract exactly —
- `2603.12123` (Cross-Context Review): abstract confirms "30 artifacts
  (code, technical documents, presentation scripts) with 150 injected
  errors, tested under four review conditions" and the SR2 finding
  ("did not beat reviewing once (p=0.11)") verbatim.
- `2606.31273` (The Calibration Turn): confirmed real author (Institute
  of Science Tokyo), confirmed "Perspective-style" framework paper with
  no empirical benchmark, matching the draft's characterization exactly.
- `2605.30329` (SoundnessBench, the relevant one): confirmed "tests
  whether LLMs can judge the methodological viability of research
  ideas," matching the draft exactly.
- `2412.03154` (SoundnessBench, the NN-verifier one): confirmed
  unrelated, formal-methods NN-verification benchmark, matching the
  draft's "not relevant" characterization exactly.
- `2505.11855` (SPOT): abstract's own verbatim text is **"none surpasses
  21.1% recall or 6.1% precision"** — mathematically identical to the
  draft's "≤21.1%/≤6.1%" framing. The skeptic's suspicion about the `≤`
  formatting does not survive contact with the source: this is exactly
  how SPOT's own authors report it.
- `2510.18003` (BadScientist): confirmed "acceptance rates up to 82.0%,"
  matching the draft's characterization.

**No fix needed.** Reported here per this paper's own stated practice
(§7's header: "every entry... re-checked... independent of whatever
prompted the name to be listed originally") of disclosing verification
that came back clean, not only verification that found something —
the same discipline `null_results/`'s own logging convention applies to
a hypothesis that survives a real attempt to kill it.

### 12.4 W3 — §5 clean-control task-ID batch split

**Confirmed real ambiguity** (not a contradiction): the underlying data
is fully coherent (`result_summary.md`: first batch's clean tasks are
`027`/`028`/`032`; `result_summary_extension.md`: extension batch's are
`029`/`030`/`031`), but the draft's own text lists all six as one
undifferentiated set, leaving "both arms, in both batches" unverifiable
from the text alone. **Fixed**: §5 now states the 3/3 split explicitly.

### 12.5 W4 — §5 `K5` verdict precision

**Confirmed real.** "`K5` passes its own `≥90%` threshold" is true only
of the 20-of-32 extension-batch subsample the paragraph itself already
discloses — but the verdict sentence itself did not repeat that scope,
risking a reader quoting "`K5` passed" without the qualifier. **Fixed**:
the verdict sentence now states the scope inline, not only in the
surrounding prose.

### 12.6 W5 — "two lineages" framing (P220 as a lineage of one)

**Assessed, not fixed.** The skeptic's point (a lineage of one is more
accurately a singleton) is defensible rhetorical criticism, not a
factual error — the paper is explicit elsewhere (§4.1, §4.3) that P220
is "one unrelated artifact," so no reader is misled about the underlying
fact. Left as a documented, considered non-fix — a future revision may
still choose to reword it, per the skeptic's own suggestion.

**None of the six items above changes a number, a verdict, or a
headline claim anywhere in the paper.** All are now fixed except 12.3
(no fix needed, verification-only) and 12.6 (assessed, deliberately not
fixed). All are now visible in the current text of `methodology_paper_
draft_v0.md`'s status header, §1.3, §5, §8, and §9.

### 12.7 Evaluator-Optimizer Guard status — CAP NOW CLOSED

This was the **third** of the capped three `reviewer`-cycle passes
(Pass 1 → fix → Pass 2 → fix → Pass 3(content) → fix, now complete).
**No further standard `reviewer`-cycle pass may run on this content**
without invoking `doubt-driven-development.md`'s Independent Review
Fallback Policy (substitute `skeptic` or `sec-auditor`, explicitly
named as a substitution, not silently normalized) — this constraint
itself now governs any future revision of this draft before Submission
Gate.

### 12.8 User-caught precision issue (2026-09-13, same day, applied
### before any sync/release action): "fixed" ≠ "independently re-verified"

**The issue:** §§12.1-12.5 above repeatedly say a finding was "fixed"
without stating, each time, that the FIX TEXT ITSELF was written by me
after the skeptic dispatch and was never seen by an independent
reviewer — only the skeptic's ORIGINAL finding (on the pre-fix text)
went through independent review. With the Evaluator-Optimizer Guard now
closed (3/3), no ordinary review cycle can check this exact post-fix
wording. This is a real distinction this project's own vocabulary
already has words for (`CORRECTED` vs. `RE-VERIFIED`) and this document
blurred it.

**Corrected framing, applied to `methodology_paper_draft_v0.md`'s own
header (2026-09-13 addendum) and repeated here:** the pre-fix draft's
status is `FALSIFIED`/`WEAKENED` per the defects found; the defects'
underlying FACTS were independently verified (§12.3's arXiv checks,
§12.4's batch-ID split, §9's own 4-item count); the CURRENT, post-fix
text is `CORRECTED, NOT RE-REVIEWED` — a real, narrower status, not
collapsible into "fixed" alone. §7 citations and §4/§5 numbers remain
`directly verified`/`directly cross-checked` regardless (those checks
were against external sources and source files, not against my own
edited wording, so they are unaffected by this distinction).

**Consequence for next steps:** no further content edits beyond obvious
typo/formatting fixes until cooling-off + venue decision. The next
legitimate check is a **release gate** (mechanical: citations, numbers,
status labels, `NOT_FOR_SUBMISSION` marker, no private data) — not a
4th evaluator-loop cycle, which the Guard's cap correctly forbids. Per
the same reasoning, this file and `methodology_paper_draft_v0.md` are
**not synced to the public reviewer repository** until the release gate
passes — the currently-public copy (frozen at the Pass-1/2/3-corrected
state, pre-Pass-4) remains accurate and honestly labeled in the
meantime; nothing about today's work makes it stale or misleading.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
