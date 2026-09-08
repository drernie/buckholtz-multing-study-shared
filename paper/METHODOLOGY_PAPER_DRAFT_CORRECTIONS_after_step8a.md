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
