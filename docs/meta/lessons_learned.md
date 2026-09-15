# Lessons Learned — Process & Tooling

> ℹ️ **`PROCESS` tier — workflow lessons, not findings (flagged 2026-09-14,
> navigation pass).** Append-only by design; its date is not staleness. The
> scope note immediately below is load-bearing and easy to miss: **falsified
> scientific claims are not here**, they are in `null_results/` with the full
> template. Nothing in this file is evidence for or against any physical claim.
> For findings: [`PROGRAM_CLOSEOUT_LEDGER.md`](../../PROGRAM_CLOSEOUT_LEDGER.md).
>
> *Moved from the repository root to `docs/meta/` on 2026-09-14, when
> the root was reduced to live documents only. Its former path was
> `lessons_learned.md`.*

**Scope note:** this file is for *workflow/tooling* lessons — how we work, not what we
found. Falsified *scientific* claims belong in `null_results/` with the full FL template
(Claim / Why falsified / Kill Analysis / Relaxation Map / Forbidden use) — do not put a
scientific null result here just because it "felt like a lesson." Cross-reference instead.

---

## 2026-07-22 — "Narrow test, class claim" — over-generalizing one branch to a theory family

The P3 fσ8 test (docs/128) modeled ONE dipole channel (intrinsic-random orientation),
ONE parametrization (scale-independent constant), ONE data point (z=0.07), at FIXED
Ωm — and the draft conclusion generalized to "MULTING dipole is degenerate with ΛCDM
at linear order." A context-asymmetry skeptic FALSIFIED it on five independent holes,
the strongest being an untested SECOND physical channel (induced/tidal polarization,
Blanchet DDM) that the isotropic-averaging argument simply does not cover. The clean
0.06σ data match and a working positive control made the draft LOOK solid — the gap
was in physics *scope*, not numerics.

**Takeaway:** when a test fixes a branch/parametrization/dataset/nuisance-parameter,
the licensed claim is scoped to exactly those choices — generalizing to "the theory
class is degenerate" silently asserts the untested branches behave the same. The
tell: a clean result with a working control still deserves a skeptic pass on
*coverage* ("what did I hold fixed, and does a real alternative violate it?"), not
just on correctness. This is the 4th skeptic catch this session and the first on
physics-modeling scope rather than an internal error — and it re-routed P3 into Q006
(the Lagrangian), turning an "interesting theory question" into a load-bearing
kill-condition.

## 2026-07-21 — "Algebraic revival of a physical null" — a named failure mode the skeptic caught

Ran the P1 Factorization Gate to test whether NR-016's obstruction could be lifted.
Found (sympy-exact) that `F_oP` factorizes into a global 2×2 matrix kernel with
per-object charge `(m_i, k_i r_i)` — cleanly escaping the *algebraic* single-kernel
problem NR-016 hit. It was tempting to read this as "NR-016's obstruction is
non-fatal, Shtanov is revived." A context-asymmetry skeptic pass (given only the
algebra + the interpretation, not the reasoning) named the exact error: **the
obstruction is not algebraic but about cosmological CLOSURE — the evolution law for
`k_i r_i` is missing from the corpus, so resolving the algebra leaves the closure
question fully open.** The factorization was itself motivated by wanting to rescue
the mapping (AOG-5 fail). (Second-order lesson, added same day after user review: the
skeptic itself over-stated this as "no conserved background *exists*" — a same-model
pass is Weak-Medium independence and cannot certify non-existence; the honest label
is "MISSING from corpus," and the robust check is the `docs/126` counterexample. Even
the tool that catches overclaims can overclaim.)

**Takeaway (the pattern, worth naming):** when a killed result gets "revived" by a
cleaner equation-level rewrite, check whether the rewrite touches the *reason* it was
killed or only the *symptom*. If the original kill was physical (conservation,
symmetry, dimensionality) and the revival is algebraic (factorization, change of
variables, reparametrization), the revival is cosmetic — the null stands. This is the
**third** skeptic catch this session (NR-015 statistical, NR-016 universality
assumption, this one algebraic-vs-physical) and the cleanest illustration that the
context-asymmetry pass earns its cost specifically on *self-authored* results that
look too tidy. Full content: `docs/125`; the surviving algebraic fact is a pearl
(2026-07-21), not a bridge.

## 2026-07-19 — Skeptic review caught a silent universality assumption in a literature-application claim

Applied Shtanov & Sahni (arXiv:1010.6205, real, verified) to `F_oP` — mapped the
two-body potential into their `φ(r)=-(G/r)f(r)` form via `φ≡V(r)/(m_A m_P)`, got a
clean, computer-algebra-verified `G_eff=G` result (dipole/quadrupole vanish from
background `H(z)`). Independent context-asymmetry skeptic review found the mapping
silently assumed `B`, `C` (dipole/quadrupole coefficients) were bilinear in
`(m_A,m_P)` alone — checking the primary source directly (not memory) showed `k_A`
is defined as "internal kinetic energy of object-A," a per-cluster physical
quantity, not something reducible to a mass product. The universal-kernel
requirement Shtanov & Sahni's whole derivation depends on was not actually met.
Full writeup: `docs/124`, formally registered as `null_results/20260719-nr016...`.

**Takeaway:** the same discipline that caught NR-015 (2026-07-18, a self-authored
statistical claim) also caught a self-authored *literature-adaptation* claim one day
later — a different failure mode (silent scaling assumption vs. a mis-dated
threshold) but the same fix: adversarial review before presenting a clean-looking
derivation as established, especially when the "clean" result is a symbolic limit
that looks too tidy to be wrong.

## 2026-07-18 — Skeptic review caught an inaccurate self-authored claim before it shipped

Wrote NR-015 ("T_X shared-variable artifact") with an "ARTIFACT-CONFIRMED" verdict and a
threshold I described as "pre-registered 2026-07-01." An independent context-asymmetry
skeptic review (no session history, just the file + code) caught two real problems: the
`<0.20` sub-threshold was actually written into the script the same day as the run, not
pre-registered a month earlier; and a genuine competing explanation (dynamical state as a
common physical driver) existed and wasn't distinguished from the "definitional artifact"
reading. Confirmed with a bootstrap CI that the point estimate was statistically fragile.
Rewrote the file, softened the verdict, corrected the paper.

**Takeaway:** running a skeptic pass on your OWN high-confidence conclusion — not just on
external documents — catches things a second read of your own work does not. This session
had already applied that discipline to *external* adversarial reviews several times; this
was the first time it caught something self-authored, and it worked. See
`null_results/20260718-nr015-tx-shared-variable-artifact.md` for the full scientific
content; this entry is about the *process* that caught the error, not the error itself.

## 2026-07-18 — Testing a new agent type against a known-solved problem is a cheap, real eval

Ran the new `boyko-agent` type against H1e without telling it the answer was already known
(NR-014 existed). It found the existing kill via `null_results/` first (did not blindly
redo the work), launched its own independent verifier sub-agent for a genuine re-execution,
and surfaced an overdue pearl (the M_gas-only retest, 3 days late) that led directly to
NR-015. This is a reusable pattern for evaluating any new tool/agent in this project: give
it a task with a known ground truth, don't reveal the answer, and check whether it
discovers existing state before acting.

**Caveat:** its final responses twice got cut off mid-synthesis and needed a follow-up
message to retrieve the full report — an infrastructure limitation of long-running
background agent calls in this environment, not a capability gap in the agent itself.

## 2026-07-17/18 — A hook that logs commits can create an infinite loop if it doesn't
## recognize its own output

`~/.claude/hooks/post_commit_memory.py` (global, not project-specific) fires on every
`git commit`, including a commit that contains only the auto-log line it wrote after the
*previous* commit. Without a guard, this loops: commit → hook appends a line → committing
that line triggers the hook again → repeat. Fixed with a diff-shape check (is this commit's
entire diff just auto-log-pattern additions to one file?) rather than a commit-message
check, so it's robust regardless of what message a human or agent uses for the follow-up
commit. Not specific to this project, but repeatedly hit *in* this project's sessions —
worth knowing if a session seems to be generating an unusual number of `chore: auto-log
entry for <hash>` commits in a row.

## 2026-07-17 — Obsidian-vault MCP's prompt-injection scanner has false positives on
## ordinary markdown

Writing a note containing inline-code backticks (`` `master` ``, `` `paper/main.tex` ``)
and bare `|` characters outside table syntax twice triggered a "command_injection"
false-positive block. Removing backtick-wrapped inline code and rewording bare pipes into
prose (not table cells) resolved it. If a vault write is rejected with a generic injection
warning and the content is plainly benign markdown, suspect this before assuming the
content itself is the problem.

## 2026-08-29 — TJB's own reply caught two errors that this project's internal review
## process did not: prose paraphrase can silently drift from the finding it summarizes,
## and correspondence needs its own artifact-provenance check, separate from the analysis

The 2026-08-27 progress-report email to TJB (`correspondence/draft_tjb_report_20260826.md`,
confirmed actually sent) survived triage, contradiction-scan, and claim-decomposer before
being sent — and still contained two real problems, both caught by TJB himself in his
2026-08-29 reply, neither caught internally.

**(a) Word-choice drift when translating a finding into prose.** The letter described the
Shtanov-Sahni background-zero result as producing "an ordinary matter-dominated universe."
The actual finding it paraphrases (`FINDING_P85_internal_time_to_redshift.md`) says
"matter-dominated, **no dark energy**" — never "ordinary." The word "ordinary" was added
at letter-drafting time, presumably for readability, and changed the physical meaning:
dark matter's cosmological effect is roughly 5x ordinary matter's in standard cosmology, so
"ordinary matter-dominated" reads as a much stronger (and wrong) claim than "matter-
dominated" does. **Pattern:** every review pass this project ran (triage, contradiction-
scan, claim-decomposer) checked the letter's claims against *each other* and against the
underlying experiment files' *conclusions* — none of them diffed the letter's exact prose
against the cited finding's exact prose, word for word. A conclusion can be correctly
summarized in substance while a single added adjective changes what it says. Any future
external-facing prose that paraphrases an internal finding should get one more pass:
read the finding's own sentence back-to-back with the letter's sentence describing it, not
just re-verify the finding is still true.

**(b) Correspondence needs its own version/artifact-provenance check, not just the
analysis's.** The letter's entire content is built on `data/source_material/
buckholtz_preprints202511.0598.v6.md` (v6) — established as the working source many weeks
earlier and never revisited before this letter was sent. TJB's own reply revealed he was
thinking of a newer version ("...v82", Zenodo 22004287, the same preprint examined
separately in `docs/144` for an unrelated question) and could not tell which version the
letter's remarks addressed. `artifact-provenance-gates.md`'s Gate 1 (Artifact Identity) is
usually applied to artifacts *inside* the analysis (a chart, a table, a dataset) — this is
the same gate applied to the **correspondence itself**: before sending an update about "your
work" to an author whose work you last pinned down weeks or months ago, re-confirm which
version you are actually referencing, especially if there is any chance the author has
revised or published a newer one in the interim. This is cheap (one question, or one check
against the author's own most recent public output) and was skipped here.

## 2026-08-30 — One file, three sequential errors, all avoidable by checking
## this project's own prior work before generating new analysis

Building `FINDING_P157` (a follow-up to `P156`, working through the "does our
Shtanov-Sahni closure apply to v82's own bridge" question), three distinct errors
were caught in sequence, in the same file, within one session:

1. **Provenance failure #1**: presented a primary-source passage (v82 Sec. IV.H,
   "Typical objects, not distributions") as newly found, when `docs/149` §4 item 4
   (written the *prior* session) already quoted it verbatim and had already noted
   its relevance to this project's own isotropic-averaging work.
2. **Provenance failure #2 (found while fixing #1)**: the file's *entire core
   reframing* — "our G_eff=0 result and v82's bridge answer structurally different
   questions" — was ALSO already stated, almost verbatim, in `docs/149` §3, written
   before `FINDING_P156` even existed. `P156` itself had failed to build on that
   observation and used a looser framing instead.
3. **Mechanism-transfer failure (found by a deliberately-dispatched context-
   asymmetric skeptic)**: having found `docs/127`'s `C1` result (isotropic
   population-average of a *vector* dipole force washes out to zero) as the
   "closest available analogy," the file used its collapse-to-zero *shape* to
   argue "stakes" for v82's own `F^(1)` force term — without checking that `F^(1)`
   (`Gβ₁(k_A m_P r_A + k_P m_A r_P)/(2c²s³)`) is a pure product of **scalars**,
   with no angular variable for `C1`'s angular-cancellation mechanism to act on.
   The two results share only a broad, largely uninformative umbrella
   ("representative value ≠ population average" — true of nearly any nonlinear
   statistic), not a shared mechanism. The mechanically appropriate tool
   (Jensen's inequality / covariance over the scalar mass distribution) was never
   applied.

**Why this matters, generalized (not just "check facts more"):** #1/#2 are the
same root cause as the already-recorded 2026-08-29 lesson ("prose paraphrase can
drift from the finding it summarizes") one level upstream — that lesson was about
drifting from a *source's* exact wording; this is about failing to grep the
*project's own* existing findings before generating new analysis on the same
question, so work already done gets silently re-presented as new. #3 is a
different, sharper failure: reaching for the nearest *available* prior result as
an analogy without checking whether its *mechanism* — not just its topic — applies
to the new context. Thematic similarity ("both are about representative values vs.
populations") is not mechanistic compatibility, and the gap between them is
exactly where an overclaim hides, because the borrowed result's *specific,
quantified* shape (a definite ±9.9 vs. a null 0.15σ) reads as far more informative
than a same-magnitude claim actually licenses once the mechanism is checked.

**How to apply going forward:** (a) before writing any new analysis on a topic
this project has plausibly already touched, `grep` the relevant `docs/*` and
`experiments/*/FINDING_*` files FIRST — a single grep is orders of magnitude
cheaper than writing, then discovering, then correcting a duplicated finding;
(b) when reusing a prior result as an analogy for a *new* formula/claim, write out
the new formula/claim first and check literally whether the borrowed mechanism's
own preconditions (here: an angular/directional degree of freedom to average
over) are present in it — "same general category" is not sufficient license to
transfer a specific quantitative shape.

## Standing gaps flagged but not yet acted on (tracked, not forgotten)

- `symbols.md` variable registry — flagged 2026-07-01 (research-methodology.md's own gap
  #2), still not created as of this entry.
- `activeContext.md`/`goals.md` memory bloat (auto-summarization hook stacking
  `[summarized]` tags without condensing) — flagged in the 2026-07-17 research-audit, not
  yet cleaned up.
- Bootstrap CIs not yet computed retroactively for H1a/c/d/e's own point estimates (only
  done for the new NR-015 test) — see `decisions.md`.
