# P28 — one specific differential signature named in Archidiacono's abstract is blind to a universal coupling; their full likelihood very plausibly is not

**Date:** 2026-08-13
**Origin:** direct extension of two already skeptic-corrected results —
P23 (`g` is a universal/composition-independent coupling, per
`MODEL_SPEC_AUDIT.md`'s own `m_A, m_P → M500` row) and P25 (equivalence-
principle tests are structurally blind to composition-independent
couplings, since EP tests specifically probe composition-*dependence*).
The natural question: does `FINDING_P22`'s own external input — Archidiacono
et al.'s β bound (arXiv:2204.08484) — share that same blind spot?
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P28_archidiacono_differential_blindness.py`

**[CORRECTED after skeptic review, same day — a real physics gap, not just
framing.]** The original title claimed Archidiacono's channel is
"structurally blind... the same way EP tests are." The skeptic's most
consequential catch (§4 point 2, original): a universal `ΔG` uniformly
enhances the sourcing of **all** matter growth, not just the DM-baryon
differential — which would show up in the **standard growth-of-structure /
σ8 / CMB-lensing channel**, a routine, load-bearing part of any CMB+BAO
likelihood fit, independent of Archidiacono's specific DM-baryon framing.
Standard modified-gravity/fifth-force literature treats structure-growth
tests as a *primary*, not secondary, probe of universal coupling shifts —
confirmed by independent reasoning before accepting (a universal shift
enhances **both** species' growth simultaneously, which is exactly what σ8
and CMB lensing measure). This means the toy model's result — the one
*specific* signature named in their abstract is blind to a universal shift
— does **not** license the practical conclusion originally drawn (that the
Archidiacono channel is "unlikely to be *the* mechanism" constraining a
universal `g`). The title, §3's framing, and §4 are corrected below. See
the Skeptic Verdict section for the full breakdown (5 sub-verdicts).

## 0. Honest scope, stated before anything else

This finding is a **structural argument plus a toy-model symbolic check**,
not a full re-derivation of Archidiacono et al.'s actual CMB+BAO likelihood
pipeline (which would require Boltzmann-code-level detail this project does
not have access to). **[Corrected]** It establishes that ~~the~~ *a*
qualitative mechanism — why a universal coupling would be invisible to
*this one specific* observable named in their abstract — using a
~~standard~~ *simplified schematic* linear-perturbation-theory structure,
verified symbolically rather than asserted. It does **not** verify that
this is the *only*, or even the *primary*, channel through which their full
analysis could constrain `g` — and §4 (corrected) now states explicitly why
the opposite is plausible for their overall likelihood.

## 1. Source re-verification (direct WebFetch, not memory)

The chain up to this point had, at one point, relied on a remembered quote
from Archidiacono et al.'s abstract, without it being recorded verbatim in
`FINDING_P22`. Per this project's own no-memory-for-external-claims
discipline, the abstract was re-fetched directly
(`https://arxiv.org/abs/2204.08484`) before building anything on it.
Confirmed accurate, verbatim from the abstract:

> "generates relative density and velocity perturbations between Dark
> Matter and baryons that grow over time"

This is Archidiacono et al.'s own description of the observable their
`β` bound is built from — a **differential/relative** quantity between two
matter species, not an absolute one.

## 2. Method

**[Corrected after skeptic review]** Set up a *simplified schematic* of the
sub-horizon linear-growth source-term structure (loosely motivated by
Newtonian cosmological perturbation theory, e.g. Dodelson's *Modern
Cosmology* ch.7, and the DM-baryon relative-velocity literature such as
Tseliakhovich & Hirata 2010): each species' density contrast is sourced by a
term `S_i = 4π·G_eff,i·ρ_tot`. ~~This is the standard structure.~~ **This is
a one-`G_eff`-per-receiving-species collapse of what a full two-fluid
treatment would keep separate** — a general fifth force can couple
source and receiver species independently (four channels: DM–DM, DM–baryon,
baryon–DM, baryon–baryon), not one `G_eff` per species. The collapse used
here is not a general property of two-fluid cosmological perturbation
theory; it holds specifically *because* a linear scalar exchange with a
coupling proportional to inertial mass (both standard Newtonian gravity,
and — per P23 — MULTING's own `g`) is source-receiver symmetric, so all
four channels reduce to a single shared `G_eff` when the coupling is
universal. This is the same well-known fact underlying P25's EP-blindness
result (a universally-coupled scalar exchange is exactly degenerate with a
shift in `G`) — not an independent coincidence, but it is a narrower,
more model-specific justification than "the standard structure," and is
stated explicitly here rather than assumed. The equation of motion for the
**relative** quantity `δ_c−δ_b` — the observable Archidiacono's own
abstract names — has source term `S_c−S_b`.

Compared, symbolically (sympy), two cases:

- **Universal coupling** (P23's own established reading of `g`): `G_eff,c =
  G_eff,b = G+ΔG_universal` — the *same* effective-G shift for both CDM and
  baryons.
- **DM-only coupling** (Archidiacono et al.'s actual model, per their own
  abstract): `G_eff,c = G+ΔG_dm-only`, `G_eff,b = G` — baryons unaffected.

## 3. Result

```
Universal coupling: S_c − S_b = 0                          (identically)
DM-only coupling:    S_c − S_b = 4π·ρ_tot·ΔG_dm-only        (nonzero)
```

Verified symbolically, not asserted (this specific subtraction is algebraic
bookkeeping — `X−X=0` and `(X+ε)−X=ε` — the substantive physics claim is
in §2's justification for *why* this subtraction is the right one to check,
not in the subtraction itself). A **universal** `ΔG` cancels exactly from
the source term driving the relative quantity `δ_c−δ_b` — both species
receive the identical shift, so their *difference* carries no trace of it.
Only a **species-dependent** shift (Archidiacono's own DM-only model)
survives in that channel, reproducing exactly the qualitative behavior their
abstract describes ("relative... perturbations... that grow over time") for
**this one named signature**.

**[Corrected after skeptic review]** ~~This is the same structural pattern
P25 established for equivalence-principle tests: a test built around a
differential/relative observable between two things is, by construction,
blind to an effect that acts identically on both. `FINDING_P22`'s own `β`
bound — like an EP test — is built from exactly this kind of differential
quantity.~~ Both results share a *mechanism* — a universally-coupled scalar
exchange is exactly degenerate with a shift in `G`, so it cannot appear in
any observable defined purely as a *difference* between two receivers that
both see the identical shift — but they are **not the same test structure**.
P25's EP test compares two non-interacting *test bodies* falling in a common
external field; P28's channel compares two mutually-*interacting* species
growing under their own coupled self-gravity. Calling them "the same
structural pattern" overstated the parallel: it is the same underlying
degeneracy, expressed through two structurally different observables, one
of which (§4, corrected) does not obviously extend to the *other*
observables in a full CMB+BAO analysis the way it provably does for EP
tests (which have no comparable "growth amplitude" companion channel).

## 4. What this does NOT establish

1. **A rigorous claim about the full Archidiacono et al. CMB+BAO
   pipeline.** This finding checks a *toy*, simplified-schematic
   linear-growth argument that reproduces the qualitative behavior their
   abstract describes for **one specific signature**. Their actual
   constraint derives from a full Boltzmann-code CMB+BAO fit — see point 2,
   corrected, for why that fit very plausibly is **not** blind to a
   universal shift even though this one named signature is.
2. **[Corrected after skeptic review — this was the most consequential
   catch, a real physics gap, not framing.]** ~~That `FINDING_P22`'s
   `A·g²≲1.05×10⁻¹⁰` soft ceiling is invalid. It remains a real, if likely
   non-binding-on-`g`, upper bound if `g` happens to also have some
   DM-preferential character; what this finding adds is that if `g` is
   genuinely universal (P23's own reading), the Archidiacono channel
   specifically is unlikely to be *the* mechanism constraining it —
   sharpening, not deleting, `FINDING_P22`'s existing `[WEAK]`/soft-ceiling
   framing.~~ A universal `ΔG` shift uniformly enhances the *sourcing* of
   **both** species' growth simultaneously — not just their relative
   difference. That absolute enhancement is exactly what standard
   growth-of-structure observables (`σ8`, CMB lensing, the matter power
   spectrum amplitude) measure, and these are a **routine, load-bearing**
   part of any CMB+BAO parameter fit, entirely independent of whether the
   analysis is specifically designed around a DM-baryon differential
   signature. Standard modified-gravity/fifth-force literature treats
   growth-of-structure tests as a **primary**, not secondary, probe of
   exactly this kind of universal coupling shift — plausibly making a
   universal-coupling reinterpretation of Archidiacono's bound *tighter*,
   not looser, via a channel this finding did not model. **Net effect: this
   finding does NOT sharpen `FINDING_P22`'s soft ceiling in `g`'s favor.**
   What survives is narrower: the *specific* DM-baryon differential
   signature named in their abstract is blind to a universal `g` — nothing
   is established here about their *overall* likelihood's sensitivity,
   and the standard-physics expectation (per this correction) leans toward
   "not blind," the opposite of the original conclusion.
3. **A resolution of what, if anything, DOES constrain a genuinely
   universal `g`.** The direct-`G`-measurement route explored during this
   finding's own research phase (CODATA's `ΔG/G≈2.2×10⁻⁵`, `[WEAK]` —
   noted from an earlier WebSearch this session, not independently
   re-verified within this finding's own build) was considered but not
   built into a rigorous argument — flagged as a candidate for a future,
   separate finding, not claimed here. Per point 2 (corrected), the
   growth-of-structure/`σ8` channel inside Archidiacono's own likelihood is
   now a more promising candidate than the direct-`G`-measurement route,
   and is itself unexplored — flagged as the most natural next step, not
   attempted here.
4. **Anything about `κ`** — this finding, like P22 and P23, is about `g`
   only.
5. **[Added after skeptic review]** That the abstract quote (§1) licenses
   the claim that Archidiacono's `β` bound is "built from" the DM-baryon
   differential signature exclusively. The quote describes *a* physical
   signature their model produces — one motivating example from the
   abstract — not necessarily *the* observable their full likelihood
   constraint is derived from. §1's "built from" language conflated these;
   read it as "the abstract names this signature as one consequence of
   their model," not as a claim about their constraint-derivation
   methodology.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction of
   the coupling structure and a published external paper's own stated
   observable — not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P28_archidiacono_differential_blindness.py
```

## Skeptic verdict (context-blind, Step 8a, 2026-08-13)

Given only this file, the script, `FINDING_P25_wep_eotvos_kill_gate.md`
(corrected), `FINDING_P23_target_population_confirmed_universal.md`
(corrected), and `FINDING_P22_archidiacono_beta_mapping.md` (corrected) —
no session history. Five sub-verdicts, per Step 8a (not merged):

- **(a)** Sympy result matches the finding's text: **CONFIRMED-REAL** —
  the subtraction identities (`X−X=0`, `(X+ε)−X=ε`) are algebraically
  forced; no error, though the skeptic correctly noted this is a trivial
  identity, not a substantive computation — the substance is in whether
  the *setup* (§2) is justified, not in the arithmetic.
- **(b)** Toy source-term structure as "the standard... structure": **WEAKENED**
  — a general two-fluid fifth-force treatment has four separate
  source-receiver coupling channels (DM–DM, DM–baryon, baryon–DM,
  baryon–baryon), not one `G_eff` per receiving species; the collapse used
  here is justified specifically by source-receiver symmetry under a
  universal, mass-proportional coupling (the same fact underlying P25), not
  a general property of perturbation theory. *Applied: FIXED — §2 rewritten
  to state the narrower justification explicitly instead of calling it
  "standard."*
- **(c)** "Same structural pattern as P25": **WEAKENED** — real disanalogy
  between P25's non-interacting test-body kinematics and P28's mutually-
  interacting coupled-growth dynamics; both share the same underlying
  degeneracy (universal coupling ≡ shift in `G`) but are not the same test
  structure, and P25's blindness is unconditional across all EP-test-style
  observables in a way P28's is not shown to be across all CMB+BAO
  observables. *Applied: FIXED — §3 corrected to name the shared mechanism
  precisely rather than asserting pattern identity.*
- **(d)** "Archidiacono channel specifically is unlikely to be *the*
  mechanism constraining a universal `g`": **FALSIFIED** — the single most
  consequential catch. A universal `ΔG` enhances the *absolute* growth of
  both species simultaneously, which is exactly what standard
  growth-of-structure observables (`σ8`, CMB lensing, matter power spectrum
  amplitude) measure — a routine, primary part of any CMB+BAO fit,
  independent of the DM-baryon-differential framing this finding modeled.
  Independently re-derived before accepting (per doubt-driven-development
  soundness check): confirmed a universal shift boosts DM growth *more*,
  not less, than the DM-only case, since baryons also now help source it —
  the opposite of what the original conclusion implied. *Applied: FIXED —
  §4 point 2 rewritten; the finding's headline conclusion ("sharpens P22's
  ceiling in `g`'s favor") is retracted, not merely softened. Title changed
  accordingly.*
- **(e)** Abstract-quote characterization ("built from"): **WEAKENED** — the
  quote is genuine (confirmed via WebFetch, §1) but describes *a* signature
  their model produces, not necessarily *the* observable their full
  likelihood constraint derives from; conflating the two oversold the
  quote's evidentiary weight. *Applied: FIXED — §4 point 5 added.*

**Not a core-predicate-false kill of the narrow claim, but a real reversal
of the finding's practical headline.** The algebraic result survives fully:
a universal coupling is genuinely invisible to *this one* differential
signature. What was withdrawn is the leap from that narrow result to a
claim about Archidiacono's *overall* constraining power — which, per the
corrected §4, plausibly points the *opposite* direction once the standard
growth-of-structure channel is considered. The skeptic's own summary:
*"the extrapolation to 'Archidiacono's β constraint therefore doesn't bind
a universal g' is stronger than one 40-line sympy subtraction can establish
and should be softened to: the specific differential signature named in
the abstract is blind; whether the full CMB+BAO likelihood remains blind
is not shown here — and standard physics suggests it likely does not."**
