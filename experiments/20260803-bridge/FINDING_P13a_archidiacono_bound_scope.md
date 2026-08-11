# P13a — Archidiacono et al.'s CMB+BAO bound constrains a different parameter than the one P11/P12 investigated

**Date:** 2026-08-12 · checks the cheapest lead from the literature sweep: does
Archidiacono, Castorina, Redigolo & Salvioni 2025 (arXiv:2204.08484)'s
already-published Planck+DESI bound `β<0.0054` (95% CL) directly constrain
this project's own `μ~H₀/c` fixed-mass mechanism (P11/P12)?
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Method:** structural/dimensional-analysis check (Gate-2-style: does the
external target actually measure the quantity we want to bound?), citing
already-verified results in this project (`FINDING_dipole_shell_is_a_double_layer.md`,
P1's own action) rather than new computation.

**Read before citing: the naive mapping does NOT work, for a structural
reason, not an unproven-assumption reason. §2 below is the load-bearing
argument.**

---

## 1. The question

Archidiacono et al. study a scalar `φ` with mass `m_φ≲H₀` coupled to dark
matter, and derive `β<0.0054` (95% CL) for the ratio of the fifth force's
strength to ordinary gravity, using Planck CMB + DESI DR2 BAO. This project's
P11 found a fixed-mass Yukawa mediator with `μ~H₀/c` breaks the exact
background double-layer cancellation of the k-sector; P12 confirmed this is
self-consistent with the near-field derivation of `β_d=2, β_q=√6`. **Does
Archidiacono's bound apply to this project's `μ~H₀/c` mechanism — i.e., is
the k-sector's dipole coupling already excluded, or bounded, by existing
data?**

## 2. The structural mismatch — two different couplings in the same action

This project's own field action (`two_field_action_closure.py`, P1) has
**two logically independent coupling constants**:

```
S = ∫d⁴x[(1/2)(∂φ)²] + Σᵢ∫dτ [ g·mᵢ + pᵢ·∇ ] φ(xᵢ),   pᵢ = κ·kᵢ·rᵢ/c²
```

- **`g`** — the coefficient of the **monopole** term (`φ` coupled to mass
  `m`, exactly like an ordinary scalar fifth force). This is the term P1's
  own text says "renormalises `G`, absorbed."
- **`κ`** — the coefficient inside the **dipole** term `pᵢ` (`φ` coupled to
  the second charge `k`). This is what fixes `β_d=2, β_q=√6` and everything
  P9–P12 investigated.

**These are separate parameters.** Archidiacono et al.'s model is a pure
scalar-monopole fifth force — `φ` sourced by mass alone, exactly the `g·m`
term above, with no dipole/quadrupole structure at all. Their `β` is
precisely a bound on `g` (or, more precisely, on the ratio of `φ`'s
monopole-exchange strength to Newtonian gravity). **It says nothing about
`κ` directly** — `κ` and `g` could, in principle, take any independent
values in this project's own action.

## 3. Why this isn't just an unproven-assumption gap — it's a symmetry gap

The mismatch is sharper than "nobody has related `g` and `κ` yet." It is
this project's **own already-verified result** that makes the two channels
structurally invisible to each other at the order Archidiacono's analysis
operates on:

`FINDING_dipole_shell_is_a_double_layer.md` proved that a spherically
symmetric (isotropically averaged) distribution of radially-aligned k-sector
dipoles produces **exactly zero** exterior force/potential — the double
layer result, verified to `~1e-16` against a monopole-shell positive
control. Archidiacono et al.'s CMB+BAO methodology is a **linear,
background/near-background cosmological perturbation analysis** — by
construction, it is sensitive to a smooth, (near-)isotropic modification of
the total mass-energy content and its clustering, i.e. to a **monopole**
coupling. A pure dipole coupling (`κ`, before any P9/P11-style
angular-asymmetry or screening-induced symmetry breaking is invoked)
contributes **exactly zero** to the isotropic background/linear observables
their analysis is built on — this is the same double-layer zero already
established in this project, not a new assumption.

**Consequence:** Archidiacono's `β<0.0054` bound cannot, even in principle,
be read as a bound on `κ`/`β_d`/`β_q` by simple parameter mapping — their
analysis is blind to a pure dipole coupling for exactly the reason this
project's own P9 finding identified. The bound genuinely applies to a
*different* channel (`g`) that this project has never independently fixed,
constrained, or even discussed as a distinct quantity.

## 4. What WOULD make the bound relevant — and why it isn't checked here

Two ways `g` could become linked to the k-sector question after all,
neither established in this project:

1. **If a future construction requires `g` and `κ` to be related** (e.g. a
   UV-completion or symmetry argument fixing both from a single coupling),
   Archidiacono's bound on `g` would then propagate into a bound on `κ`.
   No such relation exists in this project's current action — `g` and `κ`
   enter as independent terms.
2. **If P11's own symmetry-breaking mechanism (the fixed-mass-induced
   angular asymmetry, or an assumed `ε`) is large enough to leak a
   monopole-like contribution into the isotropic/background sector** —
   this has not been checked. P9/P11's calculations were for the exterior
   field of an idealized shell; whether a *realistic*, imperfectly
   isotropic ensemble of such shells sources any residual monopole-like
   term at the order Archidiacono's analysis is sensitive to is a genuinely
   open, uncomputed question.

Neither is addressed here — this finding establishes only that the **naive,
direct** mapping ("`β_d` is a fifth-force-to-gravity ratio, check it
against `β<0.0054`") does not hold, not that no connection could ever be
established.

## 5. Bottom line

**P13a does not kill, bound, or validate P11's fixed-mass mechanism.** It
establishes that the cheapest available literature check does not apply as
initially hoped — Archidiacono et al.'s bound constrains a structurally
different coupling (`g`, monopole) than the one this project's own bridge
track has been investigating (`κ`, dipole/quadrupole). This is itself a
useful, NULL-shaped result: it closes off a specific, cheap test that
looked promising, and it sharpens exactly what a REAL observational test of
the k-sector mechanism would require (either relating `g` to `κ`, or
finding an observable that is NOT blind to a pure dipole coupling — the
same requirement `FINDING_dipole_shell_is_a_double_layer.md` already named:
*"an observable that does NOT isotropically average the dipole away"*).

## What this does NOT establish

1. **That the k-sector's cosmological signal is unconstrained by existing
   data.** It may well be constrained by some other analysis — this
   finding only rules out this ONE specific, cheap mapping attempt.
2. **That `g` and `κ` are unrelated in any deeper theory.** Only that
   nothing in this project's own construction currently relates them.
3. **A resolution of whether Archidiacono's bound, if `g` and `κ` were
   related by some future argument, would exclude or permit `μ~H₀/c`.**
   That arithmetic was not done, because the premise (a stated `g`-`κ`
   relation) does not yet exist.
4. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory, and not a claim about
   any error in Archidiacono et al.'s own paper (their analysis is correct
   for the monopole fifth force it studies).

## Reproduction

No new computation — this is a structural/dimensional-analysis argument.
The two load-bearing prior results it cites are independently reproducible:
`python experiments/20260803-bridge/two_field_action_closure.py` (shows the
separate `g`, `κ` terms in the printed action) and the double-layer zero in
`FINDING_dipole_shell_is_a_double_layer.md` (own reproduction instructions
there).
