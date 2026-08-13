# P28 — Archidiacono's own constraint channel is structurally blind to a universal coupling, the same way EP tests are (P25)

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

## 0. Honest scope, stated before anything else

This finding is a **structural argument plus a toy-model symbolic check**,
not a full re-derivation of Archidiacono et al.'s actual CMB+BAO likelihood
pipeline (which would require Boltzmann-code-level detail this project does
not have access to). It establishes the *qualitative* mechanism — why a
universal coupling would be invisible to their specific observable — using
the same standard linear-perturbation-theory structure their own abstract
describes, verified symbolically rather than asserted. It does **not**
verify that this is the *only* channel through which their full analysis
could constrain `g`; see §3.

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

Set up the standard sub-horizon linear-growth source-term structure common
to Newtonian cosmological perturbation theory (e.g. the structure underlying
Dodelson's *Modern Cosmology* ch.7, and the same structure baryon-DM
relative-velocity literature such as Tseliakhovich & Hirata 2010 builds on):
each species' density contrast is sourced by a term
`S_i = 4π·G_eff,i·ρ_tot`. The equation of motion for the **relative**
quantity `δ_c−δ_b` — the observable Archidiacono's own abstract names — has
source term `S_c−S_b`.

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

Verified symbolically, not asserted. A **universal** `ΔG` cancels exactly
from the source term driving the relative quantity `δ_c−δ_b` — both species
receive the identical shift, so their *difference* carries no trace of it.
Only a **species-dependent** shift (Archidiacono's own DM-only model)
survives in that channel, reproducing exactly the qualitative behavior their
abstract describes ("relative... perturbations... that grow over time").

**This is the same structural pattern P25 established for equivalence-
principle tests**: a test built around a *differential/relative* observable
between two things is, by construction, blind to an effect that acts
identically on both. `FINDING_P22`'s own `β` bound — like an EP test — is
built from exactly this kind of differential quantity.

## 4. What this does NOT establish

1. **A rigorous claim about the full Archidiacono et al. CMB+BAO
   pipeline.** This finding checks a *toy*, standard-structure linear-growth
   argument that reproduces the qualitative behavior their abstract
   describes. Their actual constraint may derive from a more complete
   Boltzmann-code analysis with additional channels (e.g. CMB lensing, the
   overall matter power spectrum amplitude, `σ8`) that could have some
   residual sensitivity to a universal shift through parameter degeneracies
   not captured by this toy model. Not checked here.
2. **That `FINDING_P22`'s `A·g²≲1.05×10⁻¹⁰` soft ceiling is invalid.** It
   remains a real, if likely non-binding-on-`g`, upper bound *if* `g`
   happens to also have some DM-preferential character; what this finding
   adds is that if `g` is genuinely universal (P23's own reading), the
   Archidiacono channel specifically is unlikely to be *the* mechanism
   constraining it — sharpening, not deleting, `FINDING_P22`'s existing
   `[WEAK]`/soft-ceiling framing.
3. **A resolution of what, if anything, DOES constrain a genuinely
   universal `g`.** The direct-`G`-measurement route explored during this
   finding's own research phase (CODATA's `ΔG/G≈2.2×10⁻⁵`, itself already
   inflated ~3.9× for inter-method discrepancies) was considered but not
   built into a rigorous argument — flagged as a candidate for a future,
   separate finding, not claimed here.
4. **Anything about `κ`** — this finding, like P22 and P23, is about `g`
   only.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction of
   the coupling structure and a published external paper's own stated
   observable — not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P28_archidiacono_differential_blindness.py
```
