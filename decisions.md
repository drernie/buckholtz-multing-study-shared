# Decisions — Buckholtz IDM/MULTING Audit

Project-specific standing decisions not already captured in a single experiment's
`decision.md`. Global methodology rules (FL protocol, evidence markers, audit-verification-
gate) live in `~/.claude/rules/` and are not repeated here — this file is for decisions
specific to *this* project's scope and framing.

---

## Framing (established early, never revisited, still binding)

- **NOT_VALIDATION / NOT_REFUTATION / OUR_RECONSTRUCTION**: every artifact in this repo
  audits TJB's published claims independently; none of it constitutes validation,
  refutation, or an authoritative reconstruction of his intended method. Stated in every
  null_results/decision.md footer for a reason — do not drop it when writing new artifacts.
- **NO_AUTHOR_ERROR**: never imply TJB made a mistake. Where our reconstruction fails to
  reproduce a result, the framing is "we could not reproduce X from the published
  description," not "X is wrong."
- **No public claims** without going through the FL decision gate first (see
  `~/.claude/rules/falsification-ladder.md`), and no submission-grade claim without the
  Submission Gate in `~/.claude/rules/integrity.md`.

## Correspondence

- **NO_EMAIL_WITHOUT_APPROVAL**: drafts are created freely; sending requires the user's
  explicit, separate go-ahead each time. Applies to TJB and to any third party (e.g., The
  Three Hundred collaboration, 2026-07-18).
- **No direct data-request beyond what's needed**: outreach emails ask for the minimum
  data needed to run a specific pre-registered test, not an open-ended "send everything."

## Methodology decisions specific to the H1 program

- **K0 (central entropy) over a new radio/cavity-power catalog for AGN-feedback testing**
  (H1e, 2026-07-13): chosen because it's already in the Mahdavi 2013 table — no new
  catalog fetch needed. A direct radio/cavity-power test remains a documented, not-yet-run
  alternative (see NR-014's Relaxation Map) if a referee specifically demands it.
- **T_X must be controlled in any future H1-cluster confound test** (established 2026-07-18,
  NR-015): every one of H1a/c/d/e omitted this control. Any new confound candidate for the
  delta_M/E_ICM correlation must control for T_X from the start, not as an afterthought.
- **Report bootstrap CIs alongside point estimates for H1-program partial correlations**
  going forward (established 2026-07-18, after a skeptic review found a point estimate
  alone overstated confidence at N=50). Not yet applied retroactively to H1a/c/d/e's own
  point estimates — flagged in `progress.md`, not done.
- **H1b (WHIM) is the priority test, not further interior-ICM confound iteration**: once
  H1a/c/d/e/T_X all either failed to mediate or left the mechanism unresolved, further
  interior-ICM confound tests have diminishing value; H1b is structurally immune to the
  T_X-degeneracy question and is the correct next investment.

## External-facing documents

- **`paper/main.tex` is held to the same evidentiary standard as internal null_results
  files**, not a lower one — every correction made internally (Eq.32 mechanism, 7:9:17
  independence count, H1 confound framing) gets mirrored there before being considered
  closed. This paper has already been positioned toward eventual TJB review; treat every
  paragraph as if it will be read by him.
- **Any claim reversing a previously-reported "positive" framing gets an independent
  skeptic pass (context-asymmetry) before being finalized**, even when the author (this
  session) is confident — established after the NR-015 first draft ("ARTIFACT-CONFIRMED")
  had to be walked back following exactly such a review, 2026-07-18.

## Repository hygiene

- **Branch workflow is mandatory for every commit**: feature branch → commit → merge
  `--no-ff` → re-test → delete branch. Direct commits to `master` are hook-blocked by
  design; do not attempt to bypass.
- **Pre-commit checklist (ruff + pytest) runs before every commit**, not just before
  merge — established practice, not a formal rule file, but followed without exception
  this session (roughly 15+ commits, zero skipped checks).
- **`.claude/state/` artifacts left by hooks in experiment subdirectories are never
  committed** — they're a known side-effect of hook subprocesses inheriting the caller's
  cwd, not real project state.
