# P13b — Blanchet et al.'s second-order non-Gaussianity template cannot be ported directly: the k-sector has no fluid description yet

**Date:** 2026-08-12 · checks the second lead from the literature sweep:
does Blanchet, Langlois, Le Tiec & Marsat 2013 (arXiv:1210.4106)'s worked
method for computing a second-order CMB non-Gaussianity signature from
dipolar dark matter apply directly to this project's own k-sector dipole —
the exact "second-order observable" `FINDING_P4` §8 named as Branch B's
natural home but never computed?
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Method:** structural/applicability check (does the borrowed formalism's
own premise hold for this project's construction?), citing this project's
own action and prior findings rather than attempting a new GR-perturbation-
theory derivation on an unverified foundation.

**Read before citing: like P13a, this is a scope-mismatch finding, not a
new numerical forecast. §2 is the load-bearing argument — it identifies a
genuine prerequisite this project has never built, not an excuse to skip
the calculation.**

**[CORRECTED after skeptic review, same day.] Two problems found, both
fixed below, not silently. (1) §2's original "no analogous field exists"
conflated two different claims — a coarse-grained k-density field is
trivial to write down (standard cosmology practice); what's actually
missing is a Blanchet-style fluid ACTION with its own internal potential
and equation of motion, a narrower and more accurate gap. (2) §3's original
"inherits the same [double-layer] zero" argument was WRONG, not merely
unverified: it conflated a first-moment cancellation (`⟨p⟩=0`) with
Blanchet's actual sourcing quantity `W`, which is QUADRATIC in the
polarization field — `⟨p⟩=0` does not imply `⟨p²⟩=0` (if it did, Blanchet's
own paper's `f_NL` would vanish too, since their model has the same
linear-order cancellation). Withdrawn and replaced in §3 below. A bounded,
explicitly `[SPECULATIVE]`-tagged order-of-magnitude estimate — the
parametric-level ask `FINDING_P4` §8 actually made — has been added as new
§4, using this project's own already-computed cluster-scale number.**

---

## 1. What Blanchet et al.'s method actually requires

Their model (per the literature-sweep summary of 1210.4106, cross-checked
against the companion foundational papers 0804.3518 and 0901.3114) is built
as a **covariant fluid action**:

```
S = ∫d⁴x √-g L[J^μ, ξ^μ, ξ̇^μ, g_μν]
```

`ξ^μ(x)` is a **dynamical field** — a smooth function of spacetime position,
with its own equation of motion (sourced by an internal potential
`W(Π_⊥)`), its own perturbation `λ^i(x)` around a "primordial" background
value, and its own time-evolution equation (a Mészáros-type equation, whose
growing-mode solution `λ^+ = y+2/3` is what ultimately sources the
second-order curvature correction `ζ=ζ_CDM+W/3`). The entire second-order
non-Gaussianity calculation is a calculation about how **this field's own
cosmological perturbation** evolves and sources `ζ`.

## 2. Does this project's k-sector have an analogous field? No — it is built as a discrete, per-body structure

This project's own action (`two_field_action_closure.py`, P1):

```
S = ∫d⁴x[(1/2)(∂φ)²] + Σᵢ∫dτ [ g·mᵢ + pᵢ·∇ ] φ(xᵢ),   pᵢ = κ·kᵢ·rᵢ/c²
```

`φ` is the only dynamical field. The "dipole moment" `pᵢ` is not a field —
it is an **algebraic function of each individual body's own `kᵢ, rᵢ`**,
evaluated at each body's worldline. There is no `ξ^μ(x)` analogue: no
smooth "k-density perturbation" defined over spacetime, no equation of
motion for such a field, and consequently no Mészáros-type evolution
equation to solve. This is not an oversight specific to this finding — it
is consistent with how every prior finding in this track (P2, P6, P7, P9)
has treated `k`: as a **per-cluster observable**, measured or estimated for
individual real objects via real catalogues (CHEX-MATE, MCXC), never
coarse-grained into a continuum cosmological field. `FINDING_P4`'s own §8
(the origin of this whole line of inquiry) asked for the perturbative
*order* of each force tier — `F_km~O(δ^?)` — which P6 answered by treating
`kᵢ` as an ordinary astrophysical cluster property entering a **pairwise**
force law, not as a field with its own `δ_k(x)` perturbation spectrum.

**Consequence [corrected]:** Blanchet's *specific* machinery — a fluid
action with its own internal potential and Mészáros-evolving perturbation
— cannot be mechanically applied, because this project has no
`ξ^μ(x)`-equivalent **field** for `k`. This is narrower than "no smooth
k-density can be defined at all" (§3 corrects that overstatement) — it is
specifically that no analogue of Blanchet's dynamical, self-sourcing field
structure exists.

## 3. What would actually be required — one trivial step, one real one, and a withdrawn claim

**[CORRECTED after skeptic review — this section originally over- and
under-stated different parts of the gap. Both fixed below.]**

**The trivial part, previously mischaracterized as impossible:** a
coarse-grained k-density field, `n_k(x,t) = Σᵢ kᵢ W(x-xᵢ)` (any standard
smoothing kernel `W`), is a one-line definition — exactly how discrete
galaxies/halos get promoted to a smooth `δ_h(x)` in ordinary cosmological
perturbation theory. Nothing in P1's action forbids writing this down.

**The real, still-unbuilt part:** what Blanchet's specific calculation
needs is not just a smooth density, but an analogue **fluid Lagrangian**
with its own internal potential `W(Π_⊥)` and equation of motion for a
polarization field — that structure does not exist for this project's
k-sector, and building it (deciding what plays the role of `ξ^μ`'s own
dynamics, not just its instantaneous coarse-grained value) is a real
research step, not a relabeling.

**Withdrawn: the claim that this coarse-grained field would "inherit the
double-layer zero."** The original argument here reasoned: an isotropic
ensemble of dipoles has `⟨p⟩=0` (P9's result), therefore the coarse-grained
field's own internal energy would also need external symmetry-breaking
(`ε` or `μ`) to be nonzero. **This is wrong.** Blanchet's `W` is
**quadratic** in the polarization field (`W~Π_⊥²`), not linear — a
first-moment cancellation (`⟨p⟩=0`) does not imply the *second* moment
(`⟨p²⟩`, i.e. the variance) is zero. An ensemble of randomly-oriented
dipoles has zero mean polarization but generically **nonzero mean-squared**
polarization (the same reason a gas of randomly-oriented electric dipoles
has zero net polarization but nonzero dielectric susceptibility — Debye's
classical result). If the original argument were correct, it would prove
Blanchet's *own* model gives `f_NL=0` too, since their model has the
identical first-order cancellation (`FINDING_P4` already cites this: DDM is
"undistinguishable from CDM at first order... differs at second order").
It does not — because their `f_NL` is sourced by the second-moment quantity
`W`, not the first-moment force.

**Corrected status:** whether a coarse-grained k-fluid's own `W`-type
quantity is nonzero **without** needing P9's `ε` or P11's `μ` is a
genuinely open, physically plausible-either-way question — not resolved
here, and not resolved in the direction the withdrawn argument claimed.

## 4. A bounded, explicitly speculative order-of-magnitude estimate

`FINDING_P4` §8 asked for a **parametric** estimate — "derive the
perturbative order... forecast the expected effect size... *before*
writing any analysis pipeline" — not a full second-order derivation. That
ask can be attempted now, using Blanchet's own formula *shape* and this
project's own already-computed cluster number, explicitly labelled
`[SPECULATIVE]` throughout (the mapping below is a guess, not a derivation):

```
Blanchet's own result:  f_NL ~ 1.5e17 * alpha^2 * x^6,   x = (xi_perp * H)_eq
                         (alpha ~ O(1); f_NL~10 needs x~2e-3)
```

The natural, but UNVERIFIED, analogue of `x` in this project is the
dimensionless cluster-scale suppression already computed in `FINDING_P6`:
`(k/mc²) = 1.7e-6`, `r_A/r_sep = 1.0e-2`, giving `ℓ_d/r ~ 3.5e-8` per
`β_d`. Taking `x_project ~ ℓ_d/r ~ 3.5e-8` (order-of-magnitude, `β_d~O(1)`)
as the crude stand-in for Blanchet's `x`:

```
f_NL_project ~ alpha^2 * (x_project)^6 / (x_Blanchet)^6 * f_NL_reference
             ~ (3.5e-8 / 2e-3)^6 = (1.75e-5)^6
             = 2.87e-29   [SPECULATIVE, verified by direct computation]
```

**This is astronomically below any conceivable detection floor** (Planck's
own `f_NL` sensitivity is `O(1–10)`, so this estimate sits `~29.5` orders
of magnitude below it) — even allowing several orders of magnitude of
uncertainty in the `x_project` mapping (which is entirely plausible, given
`x_project` is a guessed analogue, not a derived quantity), the
sixth-power scaling means this channel would need the mapping to be wrong
by roughly **29 orders of magnitude** before becoming observable. **Caveat, stated explicitly:** this number should not
be cited as a real forecast — the mapping `x_project ↔ ℓ_d/r` is not
derived, only guessed by dimensional analogy, and the sixth-power scaling
amplifies that uncertainty enormously. Its only claim is directional:
under the most natural available reading of Blanchet's formula shape
applied to this project's own already-computed suppression factor, nothing
suggests an observable second-order signal from this specific channel.

## 5. Bottom line

**P13b does not produce a rigorous new f_NL forecast**, and the §4 estimate
is explicitly speculative, not a real derivation. What it establishes:
Blanchet's *specific* fluid-action machinery needs a prerequisite this
project has not built (a k-sector fluid Lagrangian, not merely a smoothed
density); the previously-claimed reason that prerequisite "wouldn't help
anyway" (the double-layer-inheritance argument) was wrong and is withdrawn;
and a bounded, honestly-labelled parametric estimate — answering
`FINDING_P4` §8's actual, narrower ask — gives no reason to expect an
observable signal from this channel, while making zero claim to rigor.

## What this does NOT establish

1. **That a fluid description of the k-sector is impossible to build.**
   Only that a Blanchet-style *dynamical fluid action* (not merely a
   smoothed density, which is trivial) does not currently exist in this
   project, and porting Blanchet's formalism requires it as a
   precondition.
2. **A rigorous numerical forecast.** §4's estimate is explicitly
   `[SPECULATIVE]` — a guessed dimensional analogy, not a derivation. It
   should never be cited as "this project's computed `f_NL`."
3. **That second-order observables are the wrong place to look.**
   `FINDING_P4`'s own reasoning for why Branch B's natural home is
   second-order (not `H(z)` itself) is untouched by this finding.
4. **[Withdrawn, do not cite]** That a coarse-grained k-fluid's own
   internal energy `W` would "inherit the double-layer zero." It does not
   follow from `⟨p⟩=0` — see the corrected §3.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory, and not a claim that
   Blanchet et al.'s own DDM formalism is wrong for their own model (it
   isn't — it's a well-posed fluid theory; the mismatch is that this
   project's construction is not, yet, one).

## Skeptic verdict (context-blind, 2026-08-12)

Two separate verdicts, per Step 8a / Context Asymmetry (skeptic given only
this file, `two_field_action_closure.py`, `FINDING_dipole_shell_is_a_double_layer.md`,
and `FINDING_P4_two_field_does_not_rescue_background.md` — no session
history).

- **"No fluid description exists, cannot be mechanically ported"**:
  **WEAKENED.** The core observation survives at reduced strength — this
  project's action lacks an analogue of Blanchet's dynamical field
  structure — but the original framing overreached in two ways, both
  corrected in §2–§3: (i) conflated "no coarse-grained density defined"
  (trivial) with "no analogue fluid *action*" (real); (ii) §3's
  "inherits the double-layer zero" argument was a first-moment/
  second-moment error — `⟨p⟩=0` does not imply Blanchet's quadratic
  sourcing term `W~⟨p²⟩` is zero; if the logic held, it would falsify
  Blanchet's own paper too, whose `f_NL` survives the identical
  first-order cancellation. Withdrawn.
- **Declining any speculative order-of-magnitude estimate**: **WEAKENED.**
  `FINDING_P4` §8 explicitly asked for a *parametric* estimate ("derive
  the perturbative order... forecast the expected effect size... before
  writing any analysis pipeline") — not a full pipeline. The needed input
  (the cluster-scale suppression factor) already existed in `FINDING_P6`.
  Framing the original decline as "sharpening" `FINDING_P4` §8's ask was
  over-charitable; the ask was answerable and had not been answered.
  Fixed: §4 now supplies the bounded, explicitly `[SPECULATIVE]` estimate
  the skeptic recommended (`f_NL~3e-29`, ~29.5 orders below Planck's
  sensitivity), with the mapping's own uncertainty stated plainly.

Skeptic also flagged, not corrected here (lower confidence, marked
`[ГИПОТЕЗА]` in the skeptic's own review — not independently verified
against Blanchet's paper): alternative, non-fluid templates (EFT of
Large-Scale Structure; direct second-order perturbation theory from this
project's own discrete action) might reach a real forecast without a
fluid limit at all. Not pursued here — a genuinely separate, larger
undertaking, named as a candidate future direction.

## Reproduction

The `[SPECULATIVE]` estimate in §4 is directly reproducible:
`(3.5e-8/2e-3)**6` (verified via direct computation, `2.87e-29`). The rest
is a structural/applicability argument citing this project's own action
(`two_field_action_closure.py`) and the double-layer result
(`FINDING_dipole_shell_is_a_double_layer.md`), both independently
reproducible per their own instructions.
