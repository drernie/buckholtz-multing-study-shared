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

**[CORRECTED after skeptic review, same day — Part 2 FALSIFIED, Part 1
WEAKENED.] The original §3 ("symmetry gap, not assumption gap") is wrong
and withdrawn — see the corrected §3 below. Three independent problems: (1)
the very source cited as authority, `FINDING_dipole_shell_is_a_double_layer.md`'s
own "What this does NOT mean" §3, explicitly disowns the exact cosmological
extension this finding built on it; (2) P11 — this project's OWN finding —
reports the double-layer cancellation BREAKING at exactly `μ~H₀/c`, the
regime Archidiacono's bound lives in, making "the double layer proves
blindness in this regime" self-contradictory; (3) this finding conflated a
ZERO-FORCE geometric result (a test particle outside an idealized shell)
with ZERO CONTRIBUTION TO COSMOLOGICAL OBSERVABLES (which depend on the
field's own energy density and power spectrum, not test-particle forces —
`⟨δ⟩=0` does not imply `P(k)=0`). Corrected status: this is an **open,
uncomputed assumption gap**, not a proven structural/symmetry fact. §2
(Part 1) survives narrower: no *naive* parameter mapping exists, but an
*indirect* constraint via `κ`'s contribution to `φ`'s own energy density
is unchecked, not ruled out by symmetry.**

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
monopole-exchange strength to Newtonian gravity), via a DIRECT, literal
parameter identification — `β` is not simply equal to `β_d` or any function
of `κ`/`β_d`/`β_q` alone. **[Corrected after skeptic review — the stronger
claim originally here, "it says nothing about κ directly," is WEAKENED,
not confirmed.]** `κ` and `g` are independent coefficients in the action,
so no literal, one-line substitution works — but since **the same field
`φ`** carries both couplings, `κ`'s presence could still contribute
*indirectly* to `φ`'s own background energy density, pressure, or power
spectrum (the actual quantities Archidiacono's CMB+BAO analysis
constrains) — a channel this project has not checked in either direction.
See the corrected §3 below for why the stronger "structurally invisible"
claim does not hold.

## 3. [SUPERSEDED — this section was FALSIFIED by skeptic review, kept for the record]

~~Why this isn't just an unproven-assumption gap — it's a symmetry gap~~

~~The mismatch is sharper than "nobody has related g and κ yet." It is this
project's own already-verified result that makes the two channels
structurally invisible to each other at the order Archidiacono's analysis
operates on: FINDING_dipole_shell_is_a_double_layer.md proved that a
spherically symmetric distribution of radially-aligned k-sector dipoles
produces exactly zero exterior force/potential... A pure dipole coupling
contributes exactly zero to the isotropic background/linear observables
their analysis is built on — this is the same double-layer zero already
established in this project, not a new assumption. Consequence:
Archidiacono's β<0.0054 bound cannot, even in principle, be read as a bound
on κ/β_d/β_q by simple parameter mapping.~~

**This argument is wrong, for three independent, individually-sufficient
reasons found by the skeptic:**

**(i) The cited source explicitly disowns this exact extension.**
`FINDING_dipole_shell_is_a_double_layer.md`'s own §"What this does NOT
mean" item 3 states, verbatim: *"It is not a statement about the
cosmological `H(z)` claim. That would need the same calculation in an
expanding background with the correct averaging, which has **not been done
here**. Flagged as the obvious next question, not answered."* This finding
used that exact result as authority for exactly the cosmological-blindness
claim its own source refuses to make. A cited result cannot license a
conclusion its own text explicitly declines to license.

**(ii) The regime where the argument is invoked is the regime this
project's OWN later finding shows the cited result does NOT hold.** P11
(`FINDING_P11_yukawa_screening_breaks_double_layer.md`) — built in this same
project, after the double-layer result — found that a fixed mediator mass
`μ~H₀/c` **breaks** the double-layer cancellation, with no assumed
asymmetry needed. `μ~H₀/c` is *exactly* Archidiacono's regime
(`m_φ≲H₀`). Invoking "the double layer proves blindness at this scale" is
self-contradictory: this project's own P11 already showed the double layer
does not survive at this scale.

**(iii) Conflated a zero-FORCE result with zero contribution to cosmological
OBSERVABLES.** The double-layer result is a statement about the force felt
by a test particle outside an idealized static shell — `⟨force⟩=0` under
isotropic angular averaging (a one-point average). Archidiacono et al.'s
CMB+BAO constraints are sensitive to the scalar field's own **energy
density, pressure, and power spectrum** (`Ω_φ`, `δρ_φ`, `δP_φ`, `P(k)`) —
a completely different kind of quantity. A field can have `⟨δ⟩=0` (zero
mean) while still carrying nonzero variance/power spectrum `P(k)≠0`, and a
dipole-structured coupling can still contribute to `φ`'s background energy
density and perturbation spectrum even if the *force* it mediates
angle-averages to zero for a test particle. This project has never checked
whether `κ`'s presence (regardless of the dipole force's own angular
structure) sources anything in `φ`'s own `Ω_φ`/`δρ_φ`/power spectrum — that
is a genuinely separate, uncomputed calculation.

**Corrected consequence:** whether Archidiacono's bound bears on `κ` is a
**genuinely open question**, not resolved either way by this finding. The
honest status is: *"Archidiacono's bound does not obviously apply via the
naive parameter mapping (§2), and we have not computed whether κ-sourced
field contributions leak into their observables. This is an open assumption
gap — not a symmetry theorem."*

## 4. What WOULD make the bound relevant — now the central open question, not a secondary one

**[Corrected framing after skeptic review: these are no longer "two ways it
could become relevant despite §3's blindness argument" — §3's blindness
argument is withdrawn, so these ARE the open question, unresolved either
way.]** Three channels through which Archidiacono's bound on `g` could
still bear on `κ`, none checked in this project:

1. **A future construction requires `g` and `κ` to be related** (e.g. a
   UV-completion or symmetry argument fixing both from a single coupling).
   No such relation exists in this project's current action — `g` and `κ`
   enter as independent terms — but none has been ruled out either.
2. **A realistic, imperfectly isotropic ensemble of P11-style
   asymmetric/screened shells leaks a residual monopole-like contribution
   into the isotropic/background sector**, at the order Archidiacono's
   analysis is sensitive to. Uncomputed.
3. **`κ`'s mere presence contributes to `φ`'s own background energy
   density, pressure, or power spectrum** — the actual quantities
   Archidiacono's CMB+BAO likelihood constrains — regardless of whether the
   *force* it mediates angle-averages to zero for a test particle. This is
   the channel the skeptic review identified as conflated away by the
   original (withdrawn) §3: a zero mean force (`⟨δ⟩=0`) does not imply a
   zero power spectrum (`P(k)=0`). Uncomputed.

Item 3 is the most direct candidate for a real next test — it does not
require inventing a new UV relation (item 1) or a hard geometric
calculation on a realistic asymmetric ensemble (item 2), only computing
what `κ`'s presence adds to `φ`'s own stress-energy at background/linear
order, independent of the dipole force's own angular structure.

## 5. Bottom line

**P13a does not kill, bound, or validate P11's fixed-mass mechanism —
and, after correction, does not even establish that Archidiacono's bound
is *structurally blind* to `κ`.** What survives: no *naive, direct*
parameter substitution (`β_d↔β`) works (§2), because `g` and `κ` are
independent coefficients with different physical meaning. What does
**not** survive (§3, withdrawn): the claim that this independence,
combined with the double-layer force result, proves the bound cannot bear
on `κ` even indirectly — that argument used a source against its own
explicit disclaimer, in a regime (`μ~H₀/c`) this project's own later
finding (P11) shows the cited zero does not hold, and conflated a
zero-force result with a zero-energy-density/power-spectrum claim. The
honest status is **open**: whether Archidiacono's existing data already
bears on the k-sector mechanism remains unresolved, with a concrete,
attemptable next calculation named in §4 item 3.

## What this does NOT establish

1. **That the k-sector's cosmological signal is unconstrained by existing
   data.** It may well be constrained by some other analysis, or even by
   Archidiacono's own data via the item-3 channel (§4) — this finding
   establishes only that the naive, literal parameter substitution fails,
   and (after correction) that the stronger "structurally blind" claim
   does not hold either.
2. **That `g` and `κ` are unrelated in any deeper theory.** Only that
   nothing in this project's own construction currently relates them.
3. **A resolution of whether Archidiacono's bound, if `g` and `κ` were
   related by some future argument, would exclude or permit `μ~H₀/c`.**
   That arithmetic was not done.
4. **[Withdrawn, do not cite]** That the double-layer force result implies
   anything about the field's own cosmological energy density or power
   spectrum. It does not — see the corrected §3.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory, and not a claim about
   any error in Archidiacono et al.'s own paper (their analysis is correct
   for the monopole fifth force it studies).

## Skeptic verdict (context-blind, 2026-08-12)

Two separate verdicts, per Step 8a / Context Asymmetry (skeptic given only
this file, `two_field_action_closure.py`, and
`FINDING_dipole_shell_is_a_double_layer.md` — no session history).

- **Part 1** (structural mismatch — `g`/`κ` independent, Archidiacono's
  `β` bounds `g` not `κ`): **WEAKENED.** The narrow core survives: no
  naive parameter mapping works, since `g` and `κ` are genuinely
  independent coefficients. But "says nothing about `κ` directly"
  overreached — since the same `φ` carries both couplings, an *indirect*
  constraint via `φ`'s own energy density/power spectrum is unchecked, not
  ruled out.
- **Part 2** (symmetry gap, not assumption gap — double-layer implies
  structural blindness): **FALSIFIED**, three independent, individually-
  sufficient reasons: (i) the cited source
  (`FINDING_dipole_shell_is_a_double_layer.md` §"What this does NOT
  mean" item 3) explicitly disowns exactly this cosmological extension —
  *"That would need the same calculation in an expanding background...
  which has not been done here"*; (ii) P11, this project's own later
  finding, reports the double-layer cancellation **breaking** at
  `μ~H₀/c` — exactly Archidiacono's regime, making "the double layer
  proves blindness here" self-contradictory; (iii) the argument conflated
  a zero-*force* geometric result (test particle outside an idealized
  shell, a one-point angular average) with zero contribution to
  cosmological *observables* (which depend on `Ω_φ`, `δρ_φ`, `P(k)` —
  `⟨δ⟩=0` does not imply `P(k)=0`). Skeptic's suggested honest reframing,
  adopted above: *"Archidiacono's bound does not obviously apply, and we
  have not computed whether κ-sourced field contributions leak into their
  observables. This is an open assumption gap — not a symmetry theorem."*

Two general methodology lessons the skeptic surfaced, worth keeping beyond
this one finding: **(a)** when a finding invokes a prior result as
authority for an *extended* claim, read that prior result's own "what this
does NOT mean" section *before* accepting the extension — an explicit
disclaimer there is a single-sufficient kill on its own. **(b)** a
zero-*force* geometric result never automatically implies zero contribution
to a *cosmological observable* — forces are one-point angular averages;
CMB/BAO likelihoods constrain energy density and power spectra, a
structurally different kind of quantity.

## Reproduction

No new computation — this is a structural/dimensional-analysis argument.
The two load-bearing prior results it cites are independently reproducible:
`python experiments/20260803-bridge/two_field_action_closure.py` (shows the
separate `g`, `κ` terms in the printed action) and the double-layer zero in
`FINDING_dipole_shell_is_a_double_layer.md` (own reproduction instructions
there) — **read together with that file's own §"What this does NOT mean"
before citing it as authority for any extension.**
