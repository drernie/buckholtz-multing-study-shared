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
