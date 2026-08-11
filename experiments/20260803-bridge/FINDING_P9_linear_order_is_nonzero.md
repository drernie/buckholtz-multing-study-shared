# P9 — the exact background zero does not survive to linear order

**Date:** 2026-08-11 · does the actual calculation P6/P8/skeptic all named
as the real next step: extend `FINDING_dipole_shell_is_a_double_layer.md`'s
exact background (zeroth-order) calculation one perturbative order higher,
rather than assuming either answer.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P9_perturbed_shell_linear_order.py`, ruff clean, two positive
controls (Newton shell theorem; the original double-layer zero) both pass
exactly before anything new is trusted.

**[CORRECTED after skeptic review, same day.] The raw math below is
confirmed (independently re-derived by the skeptic, matched to 6 sig
figs). The headline interpretive claim — "resolves P8's undetermined
status toward NONZERO" — is FALSIFIED and has been withdrawn. §3 and the
closing verdict block are kept for the record but marked SUPERSEDED; the
corrected reading is in the new §4 "Corrected status" and the "Skeptic
verdict" section at the end. Read those before citing anything from this
file.**

---

## 1. What was extended, and how

`FINDING_dipole_shell_is_a_double_layer.md` computed that a spherical shell
of *perfectly uniform, radially-aligned* dipole surface density is a double
layer: potential constant inside, exactly zero outside, every derivative
vanishing off the shell. That result is explicitly for a perfectly isotropic
shell — its own §"What this does NOT mean" named the cosmological/perturbed
case as "the obvious next question, not answered here."

This finding reconstructs the exact same numerical method (direct
quadrature of the dipole surface-layer potential over a sphere) and adds a
small angular perturbation to the dipole density,

```
tau(theta') = tau0 * (1 + eps * cos(theta'))
```

— the natural leading (l=1) correction if the induced dipole strength
tracks an external direction, e.g. a local density-perturbation gradient.
Before trusting any new result, two positive controls were run and matched
exactly: a monopole shell reproduces Newton's shell theorem (`2/a` inside,
`2/r` outside); the *uniform* dipole shell reproduces the original finding's
double layer (constant inside, exactly zero outside, to machine precision).

## 2. The result: nonzero, linear, ordinary-dipole falloff

```
Phi_outside(north pole, r=2a)   = +5.235988e-02
Phi_outside(south pole, r=2a)   = -5.235988e-02
Phi_outside(equator,   r=2a)    =  ~0 (numerical noise, 1e-16)
```

Antisymmetric north/south, zero on the equator — the standard external
dipole-field angular pattern. Two checks confirm this is real, not an
artefact:

- **Linear in the perturbation.** `Phi/eps` is constant (`1.047198`) across
  `eps=0.01` to `0.20` — six significant figures, no drift. This is a
  genuine `O(δ)`-type effect, not a higher-order or numerical spurious term.
- **Falls off as an ordinary point dipole.** `Phi·r²` is constant
  (`0.209440`) across `r=1.2a` to `8a` — the perturbed shell's exterior
  field behaves exactly like a single point dipole's `1/r²` potential.

A second check with an `l=2` (quadrupole-type) angular perturbation,
`tau(θ')=τ₀(1+ε·P₂(cos θ'))`, also gives a nonzero exterior potential
(positive at the poles, negative at the equator) — **no angular
perturbation tried preserves the exact background zero.**

## 3. [SUPERSEDED — see §4] What this resolves — and what it still does not give

**[CORRECTED after skeptic review — this entire §3 overclaimed and is kept
only for the record. See §4 for the corrected reading.]**

**Resolves:** ~~P8's "undetermined — could plausibly be zero (if the
background's orientation-averaging symmetry survives to first order) or
nonzero (if it does not)" is resolved toward **nonzero**.~~ The exact
cancellation found for the perfectly isotropic background is fragile — it
depends on exact angular uniformity, and breaks under any angular
asymmetry, linearly, in the direction that intuition (and P6's original
argument) expected. ~~This directly validates the physical picture P6
started from and P8's skeptic review left open: perturbing the density
does restore a genuine, non-contact, long-range force at `O(δ)`.~~ **The
struck claims are FALSIFIED — see §4. The unstruck sentence (fragility of
the exact cancellation under an assumed angular asymmetry) is the only
part of this paragraph that survives.**

**Does NOT resolve:** the actual numerical coefficient. `ε` here is a bare
geometric parameter — "how much does the shell's dipole density vary in
strength with angle" — not yet connected to a physical relationship between
`ε` and `κ`, `k`, `∇δ`. Converting this geometric result into an actual
`ΔG_eff/G` forecast requires that connection, which has not been made.
**P8's retracted `~7×10⁻⁶` number is NOT restored by this finding** — this
result supports the *qualitative* direction (nonzero) that number assumed,
but does not supply or validate its *magnitude*. **[This paragraph turned
out to be the load-bearing one — see §4: the "connection that has not been
made" here is not a missing detail, it is the entire question P8 was
undetermined about.]**

**Not tested here:** the random-orientation (intrinsic, uncorrelated)
branch's own perturbative extension — whether partially correlating random
orientations with an external direction (the analogue of intrinsic-
alignment tidal correlation in weak lensing) gives a comparable nonzero
result. Only the radially-aligned branch (the one this project's own
two-charge completion derived as matching MULTING's actual `A↔B`-symmetric
`F_d`) was tested. **[This is more serious than a scope note — see §4: per
`FINDING_P4`, the untested branch is the one the project's own action
actually implements.]**

## 4. Corrected status (post-skeptic, 2026-08-11)

The raw calculation (§2) is confirmed — the skeptic independently re-derived
the closed form from scratch, matched the printed numbers to 6 significant
figures, and confirmed the linearity and `1/r²` falloff both fall out of
that closed form. **What is withdrawn is §3's claim that this resolves P8's
physical question.** Three independent problems, found by the skeptic and
verified below:

**(a) `ε` is an assumed input, not a derived consequence — and this project's
own action already answers "does a real δ produce ε>0" in the negative.**
P9 shows: *"IF an angular asymmetry `ε>0` exists in the shell's dipole
density, THEN the exterior force is nonzero, linear, dipole-like."* It does
not show that a real cosmological density perturbation `δ` actually produces
`ε>0`. That would require the induced/correlated dipole moment of a body to
respond to an external gradient direction — and `FINDING_P4_two_field_does_not_rescue_background.md`
already found that this project's own governing action
(`two_field_action_closure.py`) uses an **intrinsic** per-body moment
`p_i = κ·k_i·r_i/c²`, fixed by that body's own properties, with no
gradient-responsive term. P9 does not cite P4, and its "resolves toward
nonzero" framing implicitly assumes exactly the induced-moment mechanism P4
found the project's own action does not contain.

**(b) P9's own perturbation is the "third option" that `FINDING_dipole_shell_is_a_double_layer.md`
explicitly said does not exist.** That earlier finding's §"Consequences,
in order of severity" (item 3) states: *"dipoles radially aligned...→ double
layer → zero"*, *"dipoles randomly oriented (intrinsic) → ⟨p⟩=0 → zero"*,
*"There is no third option, so the conclusion is independent of which
branch is right."* `τ(θ')=τ₀(1+ε·cosθ')` — neither purely radially-aligned-
uniform nor purely random — **is** that third option. P9 does not supply a
symmetry-breaking mechanism that produces it; it assumes it by construction.
Presenting P9 as an "extension" of the earlier finding understates that it
contradicts that finding's own exhaustiveness claim without resolving the
contradiction.

**(c) Even under the mechanism this project actually uses (pairwise radial
alignment, from `two_charge_completion.py`), a density perturbation alone
does not obviously give `ε>0`.** For an ensemble of pairwise-radially-aligned
dipoles with number density modulated by `δ(x)` but with pair *orientation*
uncorrelated with any global axis, the local mean dipole density is
`⟨τ(x)⟩ = n(x)·⟨p̂(x)⟩_orientation`. If orientations are isotropic,
`⟨p̂⟩=0` regardless of how `n(x)` is modulated by `δ` — density modulation
times a zero orientation-average is zero. Producing `ε>0` needs an
*additional* mechanism correlating pair orientation with a global direction
(the analogue of intrinsic alignments in weak-lensing tidal fields), which
has not been shown to exist anywhere in this project.

**(d) The "matches the classical uniformly-polarized-sphere formula" framing
(informal, never committed to this file, caught before submission and
flagged to the skeptic) is independently confirmed wrong as a physical
analogy — re-run with the shell radius `a` varied (`a=1,2,3`, `r=2a` held
fixed, `2026-08-11`):**

```
a=1: Phi*r^2/(eps*a^2) = 4.188790   Phi*r^2/(eps*a^3) = 4.188790
a=2: Phi*r^2/(eps*a^2) = 4.188790   Phi*r^2/(eps*a^3) = 2.094395
a=3: Phi*r^2/(eps*a^2) = 4.188790   Phi*r^2/(eps*a^3) = 1.396263
```

The `a²`-normalized column is exactly constant (`4π/3`); the `a³`-normalized
column is not. P9's result scales as `a²` — correct for a **surface**
dipole-density perturbation, which is what was actually computed — not as
`a³`, which is what a uniformly polarized **solid** sphere (a volume
integral) would give. The numeric match at `a=1` was a coincidence of both
integrals sharing the same `∫cos²θ·sinθ dθ = 2/3` angular factor, not a sign
that the two configurations are physically equivalent. This does not affect
the raw math (§2, unaffected by this), only the (never-published) framing
that would have over-sold it.

**What P9 actually establishes, stated honestly:** the exact background
cancellation found in `FINDING_dipole_shell_is_a_double_layer.md` is not
structurally robust — *if* a mechanism existed that produced a coherent,
globally-oriented angular asymmetry in the induced dipole density, the
resulting exterior force would be nonzero, exactly linear in that asymmetry,
and fall off as an ordinary point dipole. That conditional is useful and is
now verified. **It does not resolve P8**, because the load-bearing
antecedent — whether any such mechanism exists in this project's own theory
for a real cosmological `δ` — is exactly the question P8 (and, per (a)-(c)
above, P4 and the original double-layer finding) already left open, and if
anything P4's own finding weighs against it existing for the intrinsic-moment
action this project actually wrote down. **Status: still UNDETERMINED**, not
resolved toward nonzero.

## What this does NOT establish

1. **A specific ΔG_eff/G value.** See §4 — even the qualitative (zero vs
   nonzero) resolution is withdrawn; this gives a verified conditional
   functional form (`Φ ∝ ε`, `1/r²`), not a magnitude and not a settled sign.
2. **[CORRECTED — was understated] That this connects correctly to
   MULTING's actual physics.** The perturbation `ε` is a geometric toy
   parameter on a shell, standing in for "however a real density
   perturbation modulates the induced dipole density" — and per §4(a)-(c),
   this project's own action (per `FINDING_P4`) uses an intrinsic moment
   with no shown mechanism to produce `ε>0` from a real `δ`. This is not a
   missing detail to fill in later; it is the entire open question, and the
   project's own prior findings weigh against a mechanism existing.
3. **The random-orientation branch's behavior** — per §4(a)/(c), this is
   the branch the project's own action (intrinsic moments) actually uses,
   not a secondary scope note.
4. **That P9 resolves P8's "undetermined" status.** Withdrawn — see §4.
   P9's own perturbation is the "third option"
   `FINDING_dipole_shell_is_a_double_layer.md` explicitly said does not
   exist (§4(b)); P9 supplies no mechanism producing it, only assumes it.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction
   (the shell/double-layer toy model built from P1's two-charge
   completion), not a claim about TJB's own theory.

## Skeptic verdict (context-blind, 2026-08-11)

Two separate verdicts, per Step 8a / Context Asymmetry (skeptic given only
this file, the script, and the three cited prior findings — no session
history):

- **Raw mathematical/numerical result** (nonzero exterior potential, linear
  in `ε`, `1/r²` falloff, coefficient `4π/3`): **CONFIRMED-REAL.** The
  skeptic independently re-derived the closed form `Φ_ext = (4π/3)τ₀εa²cosθ/r²`
  from scratch and matched the script's printed output to 6 significant
  figures. Soft caveat: flagged the (never-published) "matches the
  classical uniformly-polarized-sphere formula" framing as a factor
  coincidence rather than configurational equivalence — confirmed by the
  `a`-scaling re-run in §4(d).
- **Interpretive claim** ("resolves P8's undetermined status toward
  nonzero", "validates the qualitative direction"): **FALSIFIED.** Reasons:
  (1) `ε` is an imposed input, not a derived consequence of a real `δ`;
  (2) `FINDING_P4` already found the project's own action uses intrinsic,
  non-gradient-responsive moments — the mechanism P9's framing implicitly
  assumes — and P9 never cites P4; (3) `FINDING_dipole_shell_is_a_double_layer.md`
  explicitly claimed no third option beyond radially-aligned and random,
  both giving zero — P9's perturbation *is* that third option, asserted by
  construction rather than derived; (4) even under the project's actual
  pairwise-radial-alignment mechanism, an isotropic orientation average
  times a density-modulated number density is still zero — an *additional*
  alignment-correlation mechanism (analogous to intrinsic alignments in
  weak lensing) would be needed and has not been shown.

Skeptic's recommended relabeling, adopted as this file's corrected
position (§4, last paragraph): P9 resolves the **mathematical** sub-question
(would an angular asymmetry, if it existed, produce a force? — yes, linear,
dipole-like) but not the **physical** question P8 was undetermined about
(does any such asymmetry actually arise in this project's own theory for a
real `δ`? — still open, and in tension with `FINDING_P4`).

## Reproduction

```bash
python experiments/20260803-bridge/P9_perturbed_shell_linear_order.py
```

Two `assert` positive controls (Newton shell theorem; original double-layer
zero) must pass before the script proceeds — if either fails, the method
itself is broken and nothing downstream should be trusted.
