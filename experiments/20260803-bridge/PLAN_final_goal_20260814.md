# Plan — toward a minimal covariant completion of MULTING (or a proof of underdetermination)

**Date:** 2026-08-14
**Authorization:** explicit user instruction, this session — set an
end-to-end goal, use all available tools/methods, work autonomously
through the day, report back with a real result. No doctor-facing
correspondence, no external communication, in this phase.
**Governing discipline (unchanged from the whole P1–P33 arc):** build →
run/verify → context-blind skeptic review (Step 8a) → apply corrections
in place with visible banners → register (`pearl_registry/INDEX.md` +
`facts.json` Q005 + `activeContext.md`) → ruff+pytest → commit → next
step. NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION labeling
continues on every artifact — this is our reconstruction of what a
covariant completion of MULTING's own action could look like, never a
claim about TJB's own unpublished theory (NO_AUTHOR_ERROR).

## 0. EstimandOps L0 (per `estimand-ops.md`, mandatory gate)

**Question type: Descriptive.** "What is the minimal, internally
consistent covariant completion of MULTING's own reconstructed action
(`two_field_action_closure.py`), and what does that completion predict for
structure growth (`μ,γ,Σ`) — or, failing that, is the completion
underdetermined by the data already in this project?" This is not a causal
question (no intervention/counterfactual) and not literally predictive in
the ICH E9(R1) sense (no new-case forecast) — it is a construction-and-
classification task, same epistemic status as P1–P33.

**Natural-language estimand statement:** *We are constructing the
minimal gravitational-sector completion of MULTING's own reconstructed
matter action, deriving its background and linear-perturbation
consequences, and comparing those consequences against the two
phenomenological ceilings already established (P22, P31) — for the sole
purpose of testing whether MULTING's own construction is self-consistent
and produces a falsifiable, frozen prediction, or whether it is
underdetermined by the information available to this project.*

**What this does NOT mean, stated up front:**
1. Does NOT establish what TJB's own unpublished theory actually contains
   — this project has never had access to TJB's own gravitational
   equations, only to the reconstructed matter-sector action and to
   published table values (Table A1) that are themselves AI-generated
   fits, not TJB's calculation (`table_a1_is_ai_output.md`, memory).
2. Does NOT license comparing any derived `H(z)` against Table A1 — that
   bridge is closed per Gate 2 (Target Provenance), already established
   this project. Any comparison in this campaign is against the
   phenomenological growth-rate ceilings (P22/P31) and against qualitative
   structure (does `γ≠1`? is there a slip?), never against Table A1.
3. Does NOT assume the answer is "MULTING has a working completion" —
   underdetermination is an equally valid, useful endpoint (see §3).

## 1. Final goal (stated once, not re-derived every step)

Follow the chain the user specified: `S → field equations → forces →
T_μν → H(z) → μ,γ,Σ → frozen prediction → independent test`. Two
acceptable endpoints, both scientifically valid, neither privileged over
the other:

- **(A) Working minimal covariant completion.** A specific, explicitly-
  stated gravitational sector (starting with the simplest possible
  choice: General Relativity, i.e. add a standard Einstein-Hilbert term —
  chosen because P33's own corrected lesson is to *never silently assume*
  a gravitational sector, so here it is added *explicitly* and *flagged*,
  not implied) that, combined with the already-reconstructed matter
  action, survives every kill-gate already established in this project
  (P22/P31 growth ceiling, P25 WEP composition-dependence structure,
  P23 universality) and yields at least one falsifiable, frozen,
  quantitative prediction distinguishable from both ΛCDM and from generic
  Q-type phenomenology (e.g. a specific `γ(a,k)≠1` slip signature).
- **(B) Underdetermination proof.** A demonstration that the data
  currently available to this project (the action's own structure, the
  existing phenomenological bounds, standard scalar-tensor literature)
  is compatible with multiple materially different gravitational
  completions that agree on every constraint so far derived — i.e., the
  bridge-track's own information content is insufficient to pick one
  completion, and no further P-step within this project's existing toolset
  can close that gap. This is a real result, not a failure.

## 2. Decomposition — small, falsifiable, single-assumption steps

Each step below gets its own `Pxx` finding + script, same format as
P1–P33. Numbering continues from P34. Order is the cheapest-differentiating-
test ordering (CLAUDE.md CDT protocol) — cheapest, most information-dense
steps first; expensive/uncertain steps (full perturbation theory) only
after the cheaper steps confirm the ground is solid.

| Step | Question | Cheapest test | Kill signal → pivots to |
|---|---|---|---|
| P34 | Explicitly augmented action `S=S_EH[g]+S_φ[φ,g]+S_matter` — does varying w.r.t. `g_μν` give a well-posed, standard-form modified Einstein equation? | Direct variation, symbolic where tractable, literature cross-check (Fujii&Maeda / Damour-Polyakov conformal-coupling field equations) against P33's own `m_eff(φ)` result | If the variation is ill-posed or requires an additional unstated assumption beyond "standard EH term" → document exactly which assumption is unavoidable, that itself is informative for endpoint (B) |
| P35 | FRW background: homogeneous `φ(t)`, modified Friedmann equation + φ's own Klein-Gordon equation with matter source | Symbolic derivation from P34's field equations restricted to FRW ansatz; sanity-check `g→0` limit reduces to ΛCDM exactly | If the background equations are **not** closed (undetermined function of time not fixed by the action) → strong evidence toward endpoint (B), document precisely which degree of freedom is unfixed |
| P36 | Linear perturbations: derive `μ(a,k)`, `γ(a,k)`, `Σ(a,k)` from P34/P35 | Standard scalar-tensor perturbation recipe (subhorizon quasi-static approximation first — cheapest, well-documented), compare to Bean&Tangmatitham's own `(Q,R)` parametrization structurally | If the quasi-static `μ,γ` come out **exactly** `Q=1,R=1` (i.e., MULTING's own completion is observationally indistinguishable from ΛCDM at this order) → real, useful null result: MULTING (this minimal completion) makes NO distinguishing prediction at linear order — document and stop this branch, do not force a distinguishing claim |
| P37 | Compare P36's `μ,γ,Σ` against P22/P31's phenomenological ceiling (`ε_g≲8.39×10⁻¹²`) and P25's WEP kill-gate | Plug the ceiling into P36's formulas, check self-consistency (does the ceiling actually forbid or allow the derived signature at observationally relevant `a,k`?) | If self-inconsistent (P36's own prediction violates a bound this project already independently established) → the minimal completion (A) is falsified, forced to either add complexity or accept (B) |
| P_κ | Separately, one honest attempt at pinning κ beyond P14–P17's existing one-sided bounds — check whether the now-available field-equation structure (P34-36) creates any NEW channel (e.g., a κ-dependent term in the derived `γ(a,k)` or in a backreaction integral) that existing data constrains, distinct from every channel P14–P17 already tried | Direct substitution of κ into P34-36's derived formulas, check whether κ enters at all, and if so whether existing bounds (pulsar timing, cosmological self-energy) newly combine with the field-equation structure to close the gap | If κ genuinely does not enter any of P34-37's formulas (i.e. the linear-order gravitational phenomenology is κ-blind, matching the multipole hierarchy argument already in P1) → document explicitly: κ is fixed only by non-gravitational (fifth-force, laboratory) channels, not by this campaign's cosmological chain — a real, useful scope-boundary result |

**Escape hatch (per `falsification-ladder.md` — required before any step
estimated to cost more than a small session's worth of reasoning):** if
P34 (the field-equation variation) turns out to require assumptions this
project cannot independently justify (e.g., a specific non-minimal
coupling to the Ricci scalar, or a choice of frame that isn't forced by
anything already established), STOP at that point, write up exactly what
choice is required and why it's not forced — that itself is the
underdetermination result (B), not a blocker to route around by guessing.

## 3. What would make this campaign a failure to avoid

- Silently assuming the gravitational sector is standard GR without
  flagging it as an assumption (exactly the error P33 was corrected for).
- Comparing any result against Table A1 (closed gate, `table_a1_is_ai_
  origin` memory note).
- Treating a null/negative result (γ=1, κ-blind, underdetermined) as a
  failure rather than a valid endpoint — per §1, both endpoints are
  genuine results.
- Skipping the skeptic-review step under time pressure — the whole P21–P33
  arc shows the skeptic catches a real, non-trivial issue on almost every
  single step; skipping it would make today's larger claims *less*
  trustworthy exactly when the claims are biggest.
- Sending anything externally (no TJB correspondence in this phase,
  matching the explicit "без всякого участия доктора" instruction).

## 4. Status log (updated as steps complete)

- 2026-08-14: Plan written. Starting P34.
- 2026-08-14: **P34 done + corrected.** Explicitly added a gravitational
  sector (standard, unmodified Einstein-Hilbert, flagged as a choice, per
  its own corrected lesson never to assume this silently) and derived the
  FRW background scalar equation `φ̈+3Hφ̇=ĝρ₀` via two derivation routes.
  Skeptic review found the "two independent routes" framing overclaimed
  (Noether's theorem guarantees their agreement — 5th occurrence of this
  session's "shared-input" pattern) and, more consequentially, that the
  claim "`ΔG` is a linear-perturbation effect, not background" was an
  unsupported leap given P34's own background-only scope. Both corrected
  in place. Commits `9e76713` (build), `4a4cc31` (correction, bundled with
  P35).
- 2026-08-14: **P35 done, skeptic review in progress.** Static, weak-field,
  point-source limit of the same action. Reused P34's action (extended to
  the general, non-homogeneous case) and P19's own already-`CONFIRMED-REAL`
  Green's function. Result: `ΔG=ĝ²/(4π)`, matching P21's own founding
  relation `A·g²=4π·ΔG` exactly with `A=1`. **This is the calculation
  that supplies what P34's correction found missing** — turns out to
  answer P34's own gap, built independently before that verdict was read.
  Commit `4a4cc31`. Context-blind skeptic review launched, specifically
  asked to check the slip-order subtlety (§5's "second-order-small"
  claim — is `φ`'s own gradient-squared stress genuinely higher-order in
  this *static* two-body picture, where `φ` itself is not a small
  cosmological perturbation, or does that reasoning improperly import a
  cosmological-perturbation-theory argument into a different expansion?)
  and whether `U_N=-G_N mM/r` is derived here or merely asserted (it is
  asserted, standard GR, not re-derived from `S_EH` — flagged as a
  possible overclaim risk in "P21's relation is derived, not restated").
  **Do not build P36 (quasi-static cosmological reduction) or cite P35's
  γ=1 claim as settled until this verdict lands and is processed.**
- 2026-08-14: **P35 corrected** (context-blind skeptic review, same day).
  Most consequential: independently re-read `FINDING_P21` directly and
  confirmed its own text already states the normalization constant's
  value is convention-dependent, not physical — the "A=1 matches P21"
  check was substantially circular. Narrowed to: only the functional
  form `ΔG∝ĝ²/(4π)` is genuinely shown, not P21's specific coefficient.
  Also withdrew the `γ=1` slip claim as a real physics error (conflated
  two different perturbation expansions) — genuinely open, not "second-
  order-small." Commit `679a4bc`.
- 2026-08-14: **P36 done** (first `κ`-sector finding, deliberately
  conservative — reuses two already-verified prior results rather than
  deriving new physics). Connects the already-proven double-layer/
  contact-interaction result to P34/P35's framework: `κ` is exactly
  invisible to both channels that derived `g`'s own `ΔG`, for a specific,
  already-established structural reason — confirming, at the field-theory
  level, `two_field_action_closure.py`'s own docstring claim. `g` and `κ`
  are each visible to exactly the channel the other is blind to. Commit
  `679a4bc`. Context-blind skeptic review launched, specifically asked to
  check whether the "double-layer shell" result (proven for a 2D shell of
  dipoles) is actually the right structure to invoke for a smooth 3D
  density and for a compact point source's own internal content — this is
  a real generalization, not shown to be automatic, and the review was
  asked to scrutinize it explicitly.
- 2026-08-14: **P36 corrected — most severe correction of the whole
  campaign.** 5 of 6 skeptic issues FALSIFIED outright, not merely
  weakened. Most consequential: silently extended the 2026-08-10
  double-layer result (proven for dipoles radially aligned from one
  common center) to P34's homogeneous background, which has no
  privileged center — an incoherent extension. Also conflated two
  genuinely different theorems the source material itself keeps separate
  (coherent-alignment double-layer vs. isotropic-orientation random
  average), and one "independent cross-check" was a bare `return True`
  with zero computation. Corrected conclusion: `κ`'s visibility to
  P34/P35's channels is withdrawn as genuinely open, not resolved in
  either direction — the closest this session has come to
  core-predicate-false. Commit `db24b15`.
- **2026-08-14, end-of-stretch assessment.** Three consecutive corrections
  (P34, P35, P36) show an escalating severity pattern: P34's issues were
  framing plus one real leap; P35 added a genuine circularity plus a real
  physics conflation; P36 was almost entirely load-bearing errors. This
  is a signal worth taking seriously, not just noting — it suggests the
  territory being covered (self-consistency at `O(ĝ²)`, and now `κ`'s
  actual channel) is genuinely harder and more error-prone than the
  earlier, more mechanical P21–P33 arc, and that continuing to push at
  the same pace risks a worse error than any caught so far. Pausing the
  campaign here is the deliberate, considered choice — not a stall.
  What is solid: `κ`-invisibility to P34/P35's channels is genuinely
  open, not resolved either way (a real, if humbler, result in its own
  right — the 2026-08-14 push found a real assumption gap in the
  project's own earlier informal reasoning about this). What is NOT
  solid enough to build further on without more care: P35's own `O(ĝ²)`
  self-consistency gap. Recommended next action for a future session:
  resume at a slower pace, with EACH step's skeptic review read and
  fully processed before drafting the next step's script (this stretch
  sometimes launched a new build before a prior skeptic verdict had
  landed — worth avoiding next time, even under time pressure).
- Interim assessment, mid-campaign: real, verified progress on the `g`
  (monopole) sector's static/two-body content — P21's founding relation
  is now derived, not merely assumed, a genuine result. The κ (dipole)
  sector was considered next (per the plan's `P_κ` item) but deliberately
  **not** rushed: a correct treatment requires re-grounding in this
  project's own already-established geometric setup (P1's specific
  radially-aligned dipole configuration, P24's `tiers_from_kernel`
  machinery, P25's WEP composition-dependence result) rather than
  reasoning from a summary of them — attempting it under time pressure
  risked contradicting or garbling an already-proven claim
  ("proven 2026-08-10" per P1's own docstring) without properly reading
  it first. Deferred to the next session slot, to be done carefully
  rather than quickly.
- **2026-08-16 housekeeping note: this log was stale from P36 to here —
  numbering ran on to P45 with content that doesn't match this table's
  own placeholder names (`P37`, `P_κ`). Documented below so a future
  session isn't misled into thinking the campaign stalled at P36.**
  Resuming after the pause above (slower, one-step-at-a-time cadence,
  each skeptic verdict read and processed before the next build — the
  exact discipline the end-of-stretch assessment recommended), the
  campaign continued deepening the `g`-sector's own field-theoretic
  content rather than immediately executing this table's own `P37`/`P_κ`:
  **P37** (T_μν anisotropic stress from `φ`'s static solution, corrected
  after skeptic — core claim survived independent re-derivation) →
  **P38** (metric slip `Φ−Ψ` from a self-derived linearized Einstein
  tensor, corrected — G₀₀ overclaim fixed, independent trace-equation
  cross-check added) → **P39** (dimensional-consistency audit finding
  P21's "`g` dimensionless" and P33's own `m_eff(φ)` formula mutually
  inconsistent — a genuine blocker, left as two unresolved readings) →
  **P40** (00-sector solved for `Ψ_φ`; combined with P38 gives
  `Φ_φ=0` exactly — a general theorem, not just this solution's
  property — and the slip ratio `γ:=Ψ/Φ=1−ĝ²M/(16πr)≠1`) → **P41**
  (verified via two independent literature fetches that this project's
  own `R:=ψ/ϕ` is `1/γ`, not `γ` — a real notation-inversion catch) →
  **P42** (found `Ω_φ`'s κ-sector normalization and `Φ−Ψ`'s `g`-sector
  normalization share the identical missing constant `A/c²`, scoped to
  P39's Reading 1 after skeptic caught a silently-picked-reading
  overclaim) → **P43** (Noether symmetry audit — shift symmetry
  confirmed; full-4D-conservation and dilatation-weight claims both
  FALSIFIED by skeptic and corrected) → **P44** (second variation `δ²L`
  — no ghost confirmed and strengthened; "any `V(φ)` breaks
  background-independence" FALSIFIED, corrected to require non-quadratic
  `V`) → **P45** (minimal `V(φ)=λφ⁴/4` closes the `w_φ=1`-forced
  stiff-fluid gap flagged in this file's own P34 entry above and closes
  P44's stability loop; two precision claims FALSIFIED by skeptic and
  corrected — a backwards near/far-source regime claim, an undersold
  mass-squared-sign result). Every step: build → skeptic (Step 8a) →
  independent re-derivation before accepting → correct → register →
  commit, per this file's own governing discipline (header). Full detail:
  `.claude/memory/archive/activeContext_pre-2026-08-14-p34-trim.md`
  (P37-P41) and `activeContext.md` archive entries (P42-P45).
  **This table's own P37 (compare derived `γ`/`μ`/`Σ` against the
  P22/P31 ceiling) and `P_κ` are still genuinely open** — P40 now
  supplies the `γ` formula that didn't exist when this table was
  written, making the original P37 finally executable. Next planned
  step (P46, real numbering): close this table's own P37 using P40's
  result.
