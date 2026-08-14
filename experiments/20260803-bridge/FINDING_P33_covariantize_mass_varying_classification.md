# P33 — MULTING's own monopole coupling is exactly a mass-varying (conformally-coupled) scalar, a recognized class whose known consequences strengthen P32's Part B

**Date:** 2026-08-14
**Origin:** the first well-scoped step toward the full covariant-action
derivation the mechanism-frame gate (`FINDING_P32`) ultimately needs. Rather
than attempt the full `S→` Einstein equations + scalar equation + matter
equation → `μ(a,k),γ(a,k),Σ(a,k),G_matter(a,k)` extraction in one pass —
real, substantial GR work this project has explicitly and repeatedly
deferred (`FINDING_P30`, `FINDING_P32`) to avoid rushing under time
pressure — this finding answers a cheaper, well-posed sub-question first:
is MULTING's own coupling a *recognized* type in the scalar-tensor
literature, with already-established consequences?
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P33_covariantize_mass_varying_classification.py`

## 0. Honest scope, stated before anything else

This finding does **not** derive Einstein's equations, does not linearize
the metric around FRW, and does not extract `μ`, `γ`, or `Σ` directly. It
establishes a **classification** — which standard family of scalar-tensor
coupling MULTING's own action belongs to — and cites that family's
*already-established*, textbook-level consequences from real literature.
This is evidence toward resolving the mechanism-frame gate, not a
resolution of it; the full derivation remains the larger, deferred next
step (§4).

## 1. Method

`two_field_action_closure.py`'s own monopole sector: a standard
relativistic kinetic term `−mc∫dτ` plus the already-established interaction
term `+g·m·φ∫dτ` (both re-verified this session). Summed:

```
S_total/dτ = −m·c + g·m·φ
```

Factored to expose a mass-varying-particle form (`S = −c∫dτ·m_eff(φ)`):

```
m_eff(φ)/m = (c − g·φ)/c = 1 − (g/c)·φ
```

**Exact, not an approximation** — the original coupling term was already
linear in `φ`, verified symbolically (consistency check: zero difference
between the factored and original forms).

## 2. Result — covariantization and classification

The covariant form replaces flat-space `dτ` with proper time along the
particle's worldline in the (possibly curved) metric `g_μν`:

```
S_i = −c∫dτ_curved · m_eff(φ(xᵢ)),   m_eff(φ) = m·(1 − (g/c)·φ)
```

Manifestly a scalar (covariant) action, reducing exactly to the known
flat-space form when `g_μν→η_μν`. This is precisely the structure of a
**mass-varying / conformally-coupled scalar** — matter built from a
conformally-rescaled ("Jordan-frame") metric `g_μν = A(φ)²·g̃_μν`, with
`A(φ)≈1+α·φ` to linear order. Identifying MULTING's own coupling with this
standard form (sympy-verified):

```
α = −g/c
```

## 3. Literature-grounded consequence of this classification

**[VERIFIED-WEBFETCH]** Direct quote, arXiv:1804.07180 ("Fifth forces,
Higgs portals and broken scale invariance"), their eq. 1:

> "The SM degrees of freedom {ψ} move on geodesics determined by the
> Jordan-frame metric g_μν=A²(χ)g̃_μν"

— i.e., matter moves on a metric *conformally related to, but not
identical to*, the canonical Einstein-frame metric `g̃`, whose own field
equations are the standard ones this class of theory builds on.

**[WEAK — literature consensus, synthesized via WebSearch across multiple
indexed papers, not pinned to a single direct quote]**: in the Einstein
frame, the gravitational field equations take their standard (unmodified)
GR form — sourced by ordinary matter stress-energy plus the scalar's own
stress-energy, nothing else — while matter (conformally coupled in this
frame) picks up an *extra* fifth-force term in its own equation of motion.
This evidence tier is stated honestly and separately from the direct
quote above; it was not independently pinned to one canonical source this
session despite two further WebFetch attempts (both returned incomplete
content — PDF extraction failures on two other candidate papers).

**Consequence for `FINDING_P32`'s Part B:** if MULTING's own construction
follows this standard classification (plausible, given the exact structural
match in §2, but not itself proven — see §4), then the metric's own field
equations are modified *only* through `φ`'s own stress-energy backreaction
(the same channel `FINDING_P32` §4 already flagged as unaddressed) — **not**
through a direct, `Q`-type modification of the Poisson equation the way
Bean & Tangmatitham's phenomenology assumes. This strengthens `FINDING_P32`'s
Part B definitional-mismatch argument with a literature-grounded
classification, going beyond "these are different kinds of object" to "and
here is what that specific kind of object is already known to do."

## 4. What this does NOT establish

1. **Einstein's equations for MULTING's own completion.** No
   Einstein-Hilbert term has been added, no metric perturbation performed.
   This finding classifies the *matter-sector* coupling only.
2. **That MULTING's own construction actually follows the standard
   conformally-coupled template beyond the point-particle level.** The
   classification match is exact at the level of a single point particle's
   worldline action (§2) — whether this extends cleanly to the full
   multi-particle, field-theoretic completion (with `φ`'s own dynamics,
   backreaction, and the still-unaddressed dipole/`κ` sector) is not
   verified here.
3. **A quantitative bound or formula for `μ(a,k)`, `γ(a,k)`, or `Σ(a,k)`.**
   Only a qualitative classification and its known consequences.
4. **The literature-consensus claim (§3, `[WEAK]`) at `[VERIFIED]`
   strength.** Two further WebFetch attempts at a single, cleanly-quotable
   canonical source (a review paper's abstract, and a frame-equivalence
   paper's abstract) both returned insufficient detail — the broader claim
   rests on WebSearch-synthesized consensus plus one direct structural
   quote, not two independent direct quotes of the exact same statement.
5. **A resolution of `FINDING_P32`'s mechanism-frame gate.** This is
   evidence toward resolving it, via a cheaper route than a full
   derivation — not the resolution itself. The full covariant-action
   derivation (Einstein equations + scalar equation + matter equation,
   simultaneously) remains the larger, deferred next step, per the same
   caution `FINDING_P30`/`FINDING_P32` already stated.
6. **Anything about `κ`.** Entirely about the monopole (`g`) sector,
   matching every prior finding in this sub-arc.
7. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction of
   P1's action and a published external literature classification — not a
   claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P33_covariantize_mass_varying_classification.py
```
