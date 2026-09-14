# Decisions — Buckholtz IDM/MULTING Audit

> ℹ️ **`PROCESS` tier — standing decisions, still binding (flagged 2026-09-14,
> navigation pass).** This file is not a status report, so its last-modified
> date is not staleness: a decision stays in force until explicitly revisited.
> Read it as constraints on new work, not as a description of current findings.
> For current findings: [`START_HERE.md`](START_HERE.md).

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

**Priority ladder (P0–P6, re-ordered again 2026-07-21 AFTER P2 executed):**
```
P0  fix the corpus + get author's answer on the F_oP→H(z) procedure   [blocked on TJB]
P1  non-uniqueness lemma (docs/126)     → FALSIFIED at background level by P2 (docs/127)
P2  constructive counterexample (docs/127)  → DONE: ΔH=0 under S&S background closure
C1  anisotropic vector-dipole N-body (docs/127)  → DONE: background washout survives
    (mean tidal 0.15σ from 0); dipole signal is 2nd-order structure, not background H
P3  does the dipole affect linear fσ8?  → PARTIALLY DONE (docs/128): broad claim
    FALSIFIED by skeptic; intrinsic-random branch is ΛCDM-equivalent, but the
    INDUCED-POLARIZATION branch is UNTESTED and routes into Q006
Q006 construct the MULTING Lagrangian (docs/129)  → DONE (Lagrangian built + verified)
    BUT broad "ξ=0 ⇒ ΛCDM-degenerate" closure FALSIFIED by skeptic. Sharpened to ONE
    named missing parameter η (scalar tidal response of k: k→k₀+η|∇∇Φ|²τ). η unfixed
    by corpus → [BLOCKED on TJB η OR a covariant completion OR a k-rigidity theorem]
P4  covariant completion (CANDIDATE-L1) → FAILS weak-field matching on the REPULSIVE
    dipole sign (docs/131): structure matchable (sombrero, alignment derived), but
    MULTING's repulsive dipole needs k_A/c² (positive mass-energy) to anti-gravitate,
    against the equivalence principle. [covariant program CLOSED at reconstruction level]
P5  Candidate G as independent phenomenological benchmark
P6  MCMC / CC / DESI — only after a surviving closure exists
```
**L1 outcome (docs/131, 2026-07-22) — arc endpoint:** the natural covariant completion
(Blanchet-Le Tiec polarizable medium) FAILS to reproduce MULTING's *repulsive* dipole
with a stable, positive-energy, ghost-free, EP-respecting static local action. The
1/r³ ∝ k_A m_B STRUCTURE matches (fixed-magnitude "sombrero" dipole, alignment DERIVED
by energy minimization), but the energy-minimized alignment is ATTRACTIVE; MULTING's
repulsion is the unstable maximum. Decisive: k_A is internal kinetic ENERGY, so k_A/c²
is a positive mass (the 1/c² in F_d = the mass-energy factor), which gravitates
attractively (EP) — a repulsive dipole from it violates EP. Escapes closed by 2 cheap
checks (k_A-as-free-charge: closed, k_A IS energy; vector mediator: gives 1/r not 1/r³).
**Whole cosmological arc P1→L1 now converges to a single physical bottom line:** under a
reconstruction, MULTING's cosmological sector is invisible to background H(z) (P2) and
linear fσ8 (P3), and its *repulsive* dipole resists a stable local covariant realization
(L1) — it is under-specified (η, Q006) AND in tension with the EP if read as
energy-gravity. NOT_REFUTATION: every gap/tension is a modeling choice only TJB can
resolve. No further in-session progress without TJB or a labeled model-extension.

**P3 outcome (docs/128, 2026-07-22):** the broad "linear fσ8 degenerate" claim was
skeptic-FALSIFIED (5 holes: induced-polarization branch untested; fixed-Ωm bound
artifact; scale-independent parametrization; single z-point; ≥6 other first-order
probes ignored). Only a NARROW claim survives (intrinsic-random branch = ΛCDM-equiv).
The dipole's cosmological-signature question closes NEITHER at the background (P2) NOR
at linear fσ8 (P3) — it inherits the corpus's central open question **Q006 (the
Lagrangian)**, which decides whether the induced-polarization channel exists.
**Q006 outcome (docs/129, 2026-07-22):** the non-relativistic Lagrangian was built and
verified (sympy residual=0), but the broad closure "ξ=0 ⇒ ΛCDM-degenerate" was
skeptic-FALSIFIED — "author does not model internal dynamics" is a modeling omission,
not a physical zero, and a SCALAR tidal-heating channel η (k responding to ∇∇Φ, needing
no orientation vector) is compatible with the corpus and controls the linear-growth
signature. Net: the whole cosmological branch now hinges on ONE named, corpus-unfixed
parameter η — a sharper open question than "the Lagrangian is missing", but still
BLOCKED on TJB (or a labeled extension). NOT_REFUTATION: MULTING is under-specified in
the sector cosmology needs, not refuted.
**P2 outcome (docs/127) changed the direction:** under the Shtanov–Sahni background
closure, background `H(z)` is UNIQUELY `G_eff=G` (ΛCDM-like) and completely `q`-blind
— the dipole/quadrupole background couplings vanish (`G·lim[f-rf']=0` for `1/r²`,
`1/r³`, for any even time-dependent `q`). So there is NO background non-uniqueness to
prove and NO background no-go to state (both moot). The scoped no-go (former P4) is
retired at the background level. The audit statement sharpened from "MULTING's H is
ambiguous" to "MULTING's dipole/quadrupole/isomer apparatus is INVISIBLE to background
H(z) under S&S; any signature must be in structure formation." Scoped to the S&S
closure (caveat C1: a covariant/N-body closure keeping dipole anisotropy could differ).

- **P1 Factorization Gate — RESULT (2026-07-21, sympy-verified + skeptic-reviewed,
  SPLIT VERDICT):** the algebra is CONFIRMED — a single scalar kernel FAILS (confirms
  NR-016); a **2×2 matrix kernel** with per-object charge `Q_i=(m_i, q_i)`,
  `q_i≡k_i r_i`, reproduces F_oP EXACTLY (global entries κ_mm=G, κ_mq=Gβ_d/c²,
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
