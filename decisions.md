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

## Cosmological-branch strategy (restructured 2026-07-21, session 24)

Standing decisions for the F_oP → H(z) bridge problem, superseding the informal
priority in `docs/122`/`docs/123`. The restructure was triggered by NR-016 (naive
single-kernel Shtanov mapping falsified) plus the Factorization Gate result below.

- **Candidate G is a BENCHMARK, not a bridge.** The Hamiltonian reconstruction
  `E²(z) = c₂(1+z)² + c₃(1+z)³ + c₄(1+z)⁴ + c₅(1+z)⁵` (constraints Σcᵢ=1, c₄≤0,
  c₅≥0) is `INDEPENDENT PHENOMENOLOGICAL BENCHMARK`, NOT `LITERATURE-CONFIRMED
  BRIDGE`. It is useful for identifiability / synthetic-recovery / sign-conflict /
  ΛCDM-comparison studies, but must NEVER be called the authorial `H_MULTING`.
- **Table A1 (11 points) may not be used to PROVE Candidate G** — it was part of the
  β-fitting process (circular). Independent CC-27 (cosmic chronometers) is the
  minimum honest out-of-sample test.
- **No theory-level MCMC** until a source-confirmed OR validly-derived bridge exists.
  The existing cluster implementation stays `REJECTED WITHIN IMPLEMENTATION`
  (NR-013), never transferred to the whole theory.
- **DESI/BAO only after** the geometry and the role of `r_d` are defined for a
  surviving bridge — not before.
- **Two-loop operating mode:** `MULTING SOURCE VALIDATION — WAITING FOR AUTHOR` (P0,
  blocked on TJB) runs in parallel with independent bridge research (P1+).

**Revised priority ladder (P0–P6, re-ordered 2026-07-21 after the Factorization Gate +
user review — non-uniqueness proof now precedes any no-go):**
```
P0  fix the corpus + get author's answer on the F_oP→H(z) procedure   [blocked on TJB]
P1  theorem of non-uniqueness of closure (docs/126)                   [SKETCH stated]
P2  constructive counterexample: two admissible q_i(a) laws → different H(a)  [designed]
P3  kinetic / virial coarse-graining (once a closure is chosen)
P4  scoped no-go under explicitly listed assumptions   [ONLY after P1+P2]
P5  Candidate G as independent phenomenological benchmark
P6  MCMC / CC / DESI — only after a closure is chosen
```
Note: the Universality/Factorization Gate (formerly "P1") is DONE (result below); it
fed directly into the new P1 (non-uniqueness). Covariant completion (formerly P5)
is deferred behind the non-uniqueness question — no point completing a bridge whose
closure is not even shown to be unique.

- **P1 Factorization Gate — RESULT (2026-07-21, sympy-verified + skeptic-reviewed,
  SPLIT VERDICT):** the algebra is CONFIRMED — a single scalar kernel FAILS (confirms
  NR-016); a **2×2 matrix kernel** with per-object charge `Q_i=(m_i, q_i)`,
  `q_i≡k_i r_i`, reproduces F_oP EXACTLY (global entries κ_mm=G, κ_mq=2Gβ_d/c²,
  κ_qq=Gβ_q²/c⁴; same charge `k_i r_i` serves dipole and quadrupole). But the
  interpretation "this revives Shtanov-Sahni" is **FALSIFIED** (context-asymmetry
  skeptic — a same-model isolated-context pass, Weak-Medium independence, later
  corroborated by independent human review). The evolution law for `q=k_i r_i` is
  **MISSING from the corpus** (absence of evidence, NOT proven non-existent), so
  Shtanov-Sahni's `[ρ-ϱ]` subtraction has no background for the second charge.
  **Licensed claim:** F_oP is a 2-species bilinear form with charges `(m_i, k_i r_i)`.
  **NOT licensed:** "Shtanov revived" / "matrix-component extension is the next step"
  / "the shortcut is closed" / "no background exists". Corrected status labels
  (2026-07-21): `MATRIX FACTORIZATION — PASS · COSMOLOGICAL CLOSURE FOR q — MISSING ·
  DIRECT SHTANOV — BLOCKED · NO-GO — NOT YET PROVED`. Consequence: direct
  matrix-Shtanov is BLOCKED (not closed); the correctly-scoped next step is the
  **non-uniqueness-of-closure lemma** (`docs/126`, new P1), NOT a broad no-go. See
  `docs/125` (corrected in place) + `docs/126` + `scripts/factorization_gate.py`.

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
