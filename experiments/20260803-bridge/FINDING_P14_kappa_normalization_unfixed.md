# P14 — the dipole self-energy channel is real, but κ's absolute scale was never fixed, so no number from it means anything yet

**Date:** 2026-08-12 · continues `FINDING_P13a` §4 item 3: *"κ's mere
presence contributes to φ's own background energy density, pressure, or
power spectrum — regardless of whether the force it mediates
angle-averages to zero for a test particle."* This finding builds that
calculation, catches a self-introduced error in its own first draft before
sending it anywhere, and finds a genuinely new, more fundamental gap than
the one it set out to check.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P14_dipole_self_energy_omega_bound.py`, ruff clean. One
positive control (point-charge/monopole self-energy, matched to the known
closed form `q²/r_min`) passes before the new dipole result is trusted.

**Read before citing: the headline result is not the number this script
prints — it's what checking that number against its own printed claim
revealed. §3 is the load-bearing section.**

**[CORRECTED after skeptic review, same day.] Three problems found. (1)
§1's claim that self-energy is "present for any nonzero κ regardless of
orientation" is WEAKENED — the skeptic showed that P9's exact exterior
zero, combined with the split identity, forces the cross terms to exactly
cancel the self-energy sum in the *idealized continuous* shell limit,
creating a real, unresolved tension with this finding's premise that has
not been settled either way — see corrected §1. (2) §3's "carries no
information as printed" was too strong — the `κ²` scaling gives a real,
*conditional* bound (`κ≲10⁻⁶`, contingent on the self-energy channel
actually surviving Problem 1's tension) that should have been stated. (3)
§4's "new, more fundamental gap than P13a" overreached — `κ`'s unfixed
scale is not a new discovery, it is the same fact already stated in
`FINDING_two_charge_completion.md`'s own "zero free parameters after κ"
language; P14 is the first calculation to *run into* the wall, not the
first to create it. **A fourth, more serious problem, found by the
skeptic and NOT originally part of this finding's own scope: `FINDING_P7`
and `MODEL_SPEC_AUDIT.md` §4 already silently plug `κ=1` into their own
"β_d<0.12" and "even at κ=1" claims, without ever flagging it as an
assumption** — the exact error this finding caught in its own first
draft, uncaught in two already-registered, already-cited findings. Both
corrected in place, cross-referenced from here — see §5 (new).**

---

## 1. The physics: self-energy is a real, separate, orientation-independent channel

For `N` independent dipole sources, the total field energy splits exactly:

```
∫(∇φ_total)² d³x = Σᵢ ∫(∇φᵢ)² d³x            [self-energy: per-source, ORIENTATION-INDEPENDENT]
                  + Σ_{i≠j} ∫∇φᵢ·∇φⱼ d³x       [cross terms: THIS is what P9's double-layer kills]
```

`FINDING_dipole_shell_is_a_double_layer.md` (P9) proved the exterior
potential vanishes exactly for an isotropic shell — **and it is constant
(hence zero-gradient) inside too.** This finding originally read that as
purely a statement about the **cross-term** piece (interference between
different sources), leaving the **diagonal (self-energy)** term untouched
and "present for any nonzero `κ`." **[Corrected after skeptic review —
this is not settled.]** The skeptic pointed out a real consequence of `∇φ_
total=0` holding almost everywhere (off the shell surface): plugging that
into the split identity forces
`Σ_{i≠j}∫∇φᵢ·∇φⱼ ≈ −Σᵢ∫|∇φᵢ|²` in the idealized, continuous-density limit
P9 actually computed — the cross terms **exactly cancel** the self-energy
sum there, not leave it as an untouched residual. This directly conflicts
with the claim that self-energy survives regardless of orientation.

**This is now a genuine, unresolved tension, not a settled point either
way.** P9's exact cancellation was computed for a smooth, continuous
dipole *surface density* (infinitely many infinitesimal dipoles). This
finding's self-energy calculation is for **discrete, finite-sized**
sources (real clusters, each with a finite `p_i` and a finite physical
cutoff `r_min`) — a different regularization than the continuum limit, and
it is not established (by either this finding or the skeptic's argument)
whether the exact continuum cancellation extends to, or approximately
holds for, the discrete/finite-size case. Both readings remain open: (a)
self-energy is a real, additive channel that the discrete/finite-size
regularization exposes and the continuum idealization hides; or (b) the
cancellation approximately persists for a realistic population too, and
what this script computes is not a physically separate channel at all.
**Not resolved here.** This tension is a real problem for §3's numeric
exercise below, independent of the `κ`-normalization problem it was
originally built to illustrate.

## 2. Verified computation

Reused the same discipline as P9/P11/P12: positive control before new
result.

```
Control (monopole, phi=q/r):        E = 4*pi*q^2/r_min   (matches the known q^2/r_min scaling)
New (dipole, phi=p*cos(theta)/r^2): E = (8*pi/3) * p^2 / r_min^3
```

Both derived symbolically (sympy), the dipole result cross-checked by
independent hand derivation (identical). `r_min` is the natural cutoff
where the point-charge approximation breaks — this project's own
construction (`two_charge_completion.py`) identifies the internal
charge-separation length with `r_A` itself, so `r_min=r_A` (the cluster's
own physical size) is the principled choice, not arbitrary.

## 3. What actually happened when the number was checked — the real finding

Plugging in `FINDING_P6`'s own already-computed cluster number
(`k/mc²=1.7e-6`), a typical cluster radius/mass, and a Gate-4
(Conserved-Budget) upper bound on cluster number density (assume *all*
cosmic matter is packaged into such clusters — a real ceiling, per
`~/.claude/rules/artifact-provenance-gates.md`), the script printed
`Ω_φ,k-sector ~ 3.3×10¹¹`.

**The first draft of this finding's own verdict text asserted this was
"utterly negligible."** That is the exact opposite of what `3.3×10¹¹`
means, and the discrepancy was caught by checking the printed number
against the printed claim about it, before this was sent to skeptic or
presented to the user — not after.

**Why the printed number is not directly usable: `κ`'s absolute scale has
never been independently fixed anywhere in this project.** `β_d=2` and
`β_q=√6` are **dimensionless coefficients** multiplying `(u_A+u_P)`, where
`u_i≡κkᵢrᵢ/(c²mᵢ)` itself still scales *linearly* with `κ`. P1's own "zero
free parameters after `κ`" phrase means exactly what it says: `κ` remains
free. This self-energy calculation depends on `κ`'s absolute magnitude
directly, not a ratio — building it is what exposed that magnitude was
never pinned down. **[Corrected after skeptic review — two overclaims
fixed.]** First, "the first calculation... depending on κ's absolute
magnitude directly" was **wrong** — see §5, `FINDING_P7` and
`MODEL_SPEC_AUDIT.md` already silently plugged `κ=1` into their own
claims; this is the first calculation to *notice* the issue, not the
first to *have* it. Second, the printed `3.3×10¹¹` does not carry **no**
information — the calculation's own `Ω_φ,k-sector(κ)∝κ²` scaling gives a
conditional bound, `κ≲10⁻⁶` (from requiring `Ω_φ≲1`), contingent on §1's
still-unresolved self-energy-vs-cancellation tension actually resolving in
favor of the self-energy channel being real. Presented here as
conditional, not established.

## 4. Scope of this gap, corrected

**[Corrected after skeptic review — "new, more fundamental gap than
P13a's" overreached.]** `κ`'s unfixed absolute scale is not a new
discovery — it is the same fact already stated plainly in
`FINDING_two_charge_completion.md`'s own "zero free parameters after `κ`"
language, present since that finding was written. What this finding
actually contributes is *encountering* that wall in a context where it
mattered (an absolute-magnitude calculation, not a ratio), and — per §5 —
*noticing* that other findings had already silently hit the same wall
without flagging it. Any future attempt to compute an absolute (not
ratio-based) physical quantity from the k-sector — an energy density, a force
magnitude in physical units, an observable amplitude — will hit this same
wall until `κ`'s scale is fixed by some additional physical input (e.g., a
measured value of `β_d` from real data, which this project's own
`FINDING_table_a1_provenance.md`/`MODEL_SPEC_AUDIT.md` already flag as
`BLOCKED_BY_TARGET_PROVENANCE` — Table A1's fitted `β_d=4.5` cannot be used
as ground truth, per this project's own Gate 2 discipline).

## 5. Cross-cutting problem found by the skeptic: two ALREADY-REGISTERED findings have the same uncaught κ=1 assumption

**[Added after skeptic review — not in this finding's original scope, but
too load-bearing to leave uncorrected.]** The skeptic checked whether the
κ-unfixed problem this finding caught in its OWN draft also silently
affects other findings already accepted into this project's record. It
does, in two places:

- **`FINDING_P7_k_definition_resolved_from_corpus.md`**'s reproduction
  code computes `u_A_rotational = (k_A/m_Ac²)·r_A = 0.23 m`, then derives
  `β_d<0.12` — this computation sets `κ=1` implicitly (never stated). At
  `κ=0.06` instead, `u_A≈0.014 m` and the bound becomes `β_d≲2.0` —
  landing almost exactly ON this project's own derived `β_d=2`, not
  excluding it by "~1.2 orders of magnitude" as stated. **P7's exclusion
  claim is a joint constraint on `(κ,β_d)`, not a pure `β_d` bound**, and
  was never labeled as such.
- **`MODEL_SPEC_AUDIT.md` §4**'s "even at `κ=1`, no further suppression,
  5–13 orders of magnitude" observability-gap row also uses `κ=1` as an
  explicit benchmark, correctly *labeled* there — but the surrounding
  narrative ("the force is undetectable") reads as a `κ`-independent
  conclusion, when the actual gap size is `κ`-dependent.

**Both corrected in place, cross-referencing this finding**, in their own
files (`FINDING_P7...md` and `MODEL_SPEC_AUDIT.md`), not silently. Neither
correction reverses their bottom-line conclusions (P7's `β_d=2` exclusion
still likely holds under the textually-supported rotational-only reading,
per P7's own §4 secondary argument; MODEL_SPEC_AUDIT's observability gap
remains real at any physically plausible `κ`) — but both claims should now
be read as conditional on `κ`, not `κ`-independent, until `κ` is fixed.

## What this does NOT establish

1. **That the self-energy channel is real, large, or small.** §1's
   tension (self-energy vs. exact continuum cancellation) is unresolved —
   this finding does not establish the channel survives at all, only that
   if it does, its magnitude is currently unfixed by `κ`.
2. **A resolution of P13a's own open question** (whether Archidiacono's
   bound bears on `κ`). If anything, this finding shows that question is
   even less tractable than P13a implied.
3. **That `κ` can never be fixed.** Only that nothing in this project has
   fixed it yet.
4. **That P7's or MODEL_SPEC_AUDIT's bottom-line conclusions are wrong.**
   Only that their stated confidence/precision needs a `κ`-dependence
   caveat, added in place per §5.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic verdict (context-blind, 2026-08-12)

Two separate verdicts, per Step 8a / Context Asymmetry (skeptic given only
this file, the script, `two_charge_completion.py`,
`FINDING_two_charge_completion.md`, and
`FINDING_dipole_shell_is_a_double_layer.md` — no session history; the
skeptic additionally read `MODEL_SPEC_AUDIT.md` and `FINDING_P7...md` on
its own initiative to check for related issues).

- **Self-energy physics/computation**: **WEAKENED.** The split identity,
  the monopole positive control, and the dipole self-energy formula
  (`(8π/3)p²/r_min³`) were all independently hand-re-derived and confirmed
  correct. But the physical interpretation — self-energy as an always-
  present, orientation-independent channel — is not established, and may
  be wrong, in exactly the induced/radially-aligned configuration this
  project's own construction forces (§1, corrected above).
- **`κ`'s absolute scale unfixed**: **CONFIRMED-REAL for the core fact**
  (independently checked against `two_charge_completion.py` and
  `FINDING_two_charge_completion.md` — `κ` is genuinely carried
  symbolically throughout, never assigned a value), **WEAKENED for scope
  and framing** — this is not the first calculation to depend on `κ`
  absolutely (§5), and the printed number is not wholly uninformative (its
  scaling gives a real conditional bound, §3).

## Reproduction

```bash
python experiments/20260803-bridge/P14_dipole_self_energy_omega_bound.py
```

The monopole positive-control assert must pass before the dipole result is
trusted. The script's own final verdict block states the corrected
conclusion (§3 above) directly — read it in full, not just the printed
`Ω_φ` number, which is explicitly flagged in the script's own output as
not physically meaningful as printed.
