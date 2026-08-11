# P11 — a screened (massive) mediator breaks the double layer with no assumed asymmetry, but this collides with the project's own masslessness requirement

**Date:** 2026-08-12 · checks the second, still-untouched escape route named
by `FINDING_P4_two_field_does_not_rescue_background.md` §4: *"a `ψ` with its
own distinct propagator (screened/massive on cosmological scales, effectively
massless at cluster/solar-system scales — the same class of mechanism as
chameleon/Vainshtein/symmetron screening in modified gravity)."* P9 tested a
different candidate (assumed angular asymmetry `ε`); P10 tested a third
(velocity/momentum coupling, found absent). This is P4's own second escape
route, still open, checked directly.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P11_yukawa_screening_breaks_double_layer.py`, ruff clean, one
positive control (massless limit reproduces the exact double-layer zero) and
two self-consistency checks (angular uniformity; radial falloff) all pass
before anything new is trusted.

**Read before citing: §4 below states a real, unresolved tension between
this finding and this project's own P1 derivation. This is not a caveat to
skim — it is the load-bearing open question the finding itself creates.**

**[CORRECTED after skeptic review, same day.] The raw math is CONFIRMED-REAL
— an independent skeptic re-derivation (closed-form analytic formula for the
shell's Yukawa exterior potential) matched the numerical results to 4+
significant figures at three tested `μ` values, and the Yukawa dipole
formula was independently re-derived from first principles and found
identical. §4's handling of the masslessness tension is WEAKENED, not
falsified: the tension itself was flagged honestly, but the specific
citation of "chameleon/Vainshtein/symmetron-class" screening as the
resolving mechanism is WRONG-DIRECTION (those mechanisms screen *near*
matter and un-screen cosmologically — the opposite of what this
construction needs) and has been corrected below to the mechanism the
skeptic showed actually works: a plain fixed-mass Yukawa field, no
environmental/density-dependent screening required at all. CHECK 1's
framing (angular uniformity "confirms spherical symmetry of the effect")
is also softened — see the corrected note in §3.**

---

## 1. The question, and why it's different from P9's

`FINDING_dipole_shell_is_a_double_layer.md` found that a uniform, radially-
aligned dipole shell has an exterior potential of exactly zero — this is a
property specific to the **massless** (Coulomb, `1/dist`) Green's function.
Newton's shell theorem makes the exterior potential of *any* spherically
symmetric shell depend only on its total charge and the field point's
distance, **not on the shell's own radius** — so two infinitesimally
displaced concentric monopole shells (the mathematical limit that defines a
dipole layer) cancel exactly for any exterior point, regardless of where
exactly the shell sits.

For a **Yukawa** (massive) Green's function `exp(-μ·dist)/dist`, the
exterior potential of a uniform shell is genuinely radius-dependent (the
standard result includes a `sinh(μa)/(μa)` prefactor that varies with shell
radius `a`) — so the same infinitesimal-displacement limit should **not**
cancel. Unlike P9 (which needed to *assume* an angular asymmetry `ε` with no
derived source) or P10 (which checked for velocity-coupling and found none),
this candidate needs **no new assumption about the source at all** — only a
finite mediator mass, which P4 already named as a live, physically
motivated (chameleon-class) possibility.

## 2. The check

Reused P9's exact numerical method (direct quadrature of the dipole surface-
layer potential over a sphere), replacing the Coulomb kernel with a Yukawa
one. Hand-derived and verified: for `G(dist)=exp(-μ·dist)/dist`,

```
Φ_dipole = τ · (n̂·diff) · (μ·dist+1) · exp(-μ·dist) / dist³
```

which reduces exactly to P9's `τ·dot/dist³` when `μ=0` — checked as the
first positive control before trusting anything new:

```
Phi_outside(r=2A, mu=0) = -1.306e-16   (exact zero, matches
                                         FINDING_dipole_shell_is_a_double_layer.md)
```

The shell was kept **perfectly angularly uniform** throughout (`τ(θ')=τ₀`,
constant — no `ε`, no assumed asymmetry of any kind).

## 3. The result

**Nonzero for every finite `μ` tested, with no angular asymmetry assumed:**

```
mu=0.01 (mu*A=0.01): Phi_outside(r=2A) = +2.052944e-04
mu=0.10 (mu*A=0.10): Phi_outside(r=2A) = +1.716461e-02
mu=0.50 (mu*A=0.50): Phi_outside(r=2A) = +1.974800e-01
mu=1.00 (mu*A=1.00): Phi_outside(r=2A) = +3.128214e-01
mu=2.00 (mu*A=2.00): Phi_outside(r=2A) = +2.242650e-01
mu=5.00 (mu*A=5.00): Phi_outside(r=2A) = +1.693546e-02
```

Peaks around `μA~1`, decaying toward both `μ→0` (recovering the exact zero)
and `μ→∞` (the screened force becomes too short-range to reach the field
point at all) — physically sensible, not a numerical artefact.

Two self-consistency checks, both passing before this is trusted:

- **Angular uniformity.** At fixed `r=2A, μ=0.5`, four points (north pole,
  south pole, equator, 45°) all give **identical** `Φ=1.97479951e-01` to 8
  significant figures (spread `2.5e-16`). **[CORRECTED framing after
  skeptic review]** — this does not independently confirm new physics: the
  source configuration (uniform `τ`, each dipole element pointing radially
  outward at its own location) is fully rotationally invariant *by
  construction*, so the exterior field, if nonzero, is *guaranteed by
  symmetry alone* to depend only on `r`. What this check actually verifies
  is narrower but still useful — **quadrature fidelity**: that the
  numerical integration method itself preserves the symmetry already
  present in the input, ruling out a polar-axis-biased artefact of the
  `dblquad` implementation. A genuine bug could in principle still pass a
  sparse 4-point check by coincidence (all four points sit on high-symmetry
  axes), so this is a code-hygiene check, not independent physical
  evidence for the result.
- **Radial falloff.** `Φ·r²` is **not** constant across `r=1.2A`–`8A`
  (unlike P9's `μ=0` case, where it was exactly constant) — confirming this
  is a genuinely finite-range, screened effect, not a disguised ordinary
  `1/r²` dipole tail.

## 4. The critical tension — not resolved here, the actual open question

**This project's own `two_field_action_closure.py` (P1) already proved**
that `β_q/β_d = √6/2` — this project's headline, zero-free-parameter result
— **holds if and only if the mediator is exactly massless**: `Λ(r) =
K'''(r)K'(r)/K''(r)² = 3/2` exactly, for every `r`, only for `K=1/s`
(massless); a Yukawa kernel makes `Λ` `r`-dependent and `≠3/2`.

**So invoking a finite `μ` to explain a nonzero cosmological signal directly
conflicts with this project's own derivation of `β_d=2, β_q=√6`** — *unless*
the mediator is effectively massless at the scale where `β_q/β_d` was
derived and would need to hold (cluster/local scale) and effectively
massive/screened only at cosmological scale.

**[CORRECTED after skeptic review — the mechanism named below was
wrong-direction.]** ~~This is exactly the structure of a real, established
modified-gravity mechanism class (chameleon, Vainshtein, symmetron
screening — density- or scale-dependent effective mass)~~ — **this citation
was incorrect.** Chameleon, symmetron, and Vainshtein screening all work in
the opposite direction from what this construction needs: they make the
fifth force **short-range (screened) near matter** (dense environments,
e.g. inside/near a galaxy cluster) and **long-range (unscreened) in voids /
cosmologically**. This project needs the reverse — **unscreened at
cluster/local scale** (so `Λ=3/2` holds and `β_q/β_d=√6/2` survives) and
**screened cosmologically**. Naming that mechanism class as precedent
falsely implies a well-studied family already licenses the needed
behaviour; it does not.

**The mechanism that would actually work, found by the skeptic review, is
simpler and needs no environmental/density-dependent screening at all: a
plain, ordinary fixed-mass Yukawa field with `μ ~ H₀/c`.** At cluster scale
(`r ~ few Mpc`), `μr ~ 10⁻⁴`, so the massive-kernel correction to `Λ=3/2` is
`O((μr)²) ~ 10⁻⁸` — indistinguishable from exactly massless in any current
or foreseeable test, so `β_q/β_d=√6/2` survives to ~8 decimal places. At
cosmological scale (`r ~ 1/H₀`), `μr ~ 1`, and the double layer breaks
exactly as shown in §3. This is not a density-dependent screening
mechanism at all — "scale" here means ordinary Fourier `k` versus a fixed
Compton wavelength `1/μ`, ratioed against the *distance being probed*
(cluster separation vs. Hubble radius), not against local matter density.
**A real, nontrivial consequence for P1's own headline claim:** P1's own
"`β_q/β_d=√6/2 ⟺` mediator exactly massless" should be read, for the
purpose of physical viability, as *"⟺ `μ` negligible at the derivation
scale"* — a small but real softening of P1's "exactly" language that a
fixed, cosmologically-relevant `μ~H₀/c` satisfies trivially at cluster
scale. **Still genuinely unresolved:** whether such a fixed-mass extension
is actually constructible without breaking the near-field `A₃, A₄` ladder
structure, and whether `μ~H₀/c` specifically (as opposed to some other
scale) gives an observable magnitude — neither checked here.

## What this does NOT establish

1. **That this project's construction actually has, or is compatible with,
   a fixed-mass extension.** Nothing here derives one, or checks whether
   one is even constructible without breaking the near-field `A₃, A₄`
   ladder structure that fixed `β_d=2, β_q=√6` in the first place.
   **[Corrected: earlier language here cited "scale-dependent screening,"
   which per the skeptic review is not actually what this construction
   needs — see §4's correction. The open item is a plain fixed-mass field,
   not a density-dependent screening mechanism.]**
2. **A specific value of `μ`**, or whether `μ~H₀/c` specifically (as
   opposed to some other scale) gives an observable magnitude. `μ` here is
   a bare toy parameter, exactly as `ε` was in P9 — this finding trades one
   unmotivated free parameter (an assumed angular asymmetry) for a
   different one (a mediator mass), not a fully closed derivation. Unlike
   P9's `ε`, `μ~H₀/c` at least has a natural physical scale to test against
   — but that test has not been run here.
3. **That P9's and P10's results are superseded.** They checked different,
   independent candidates (assumed asymmetry; velocity-coupling) and their
   own verdicts stand on their own terms — this is a fourth candidate, not
   a replacement for the first three.
4. **A resolution of whether the k-sector's cosmological `O(δ)` (or even
   background-order) contribution is real.** This shows one more mechanism
   *could* produce a nonzero signal, under an as-yet-unverified additional
   assumption (scale-dependent screening) — not that it *does*.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction (P1's
   two-field/two-charge completion), not a claim about TJB's own unpublished
   theory.

## Skeptic verdict (context-blind, 2026-08-12)

Two separate verdicts, per Step 8a / Context Asymmetry (skeptic given only
this file, the script, and the three cited prior findings — no session
history):

- **Mathematical/numerical result** (Yukawa dipole formula; nonzero
  exterior potential with a uniform shell; self-consistency checks):
  **CONFIRMED-REAL.** The skeptic independently re-derived the dipole
  formula from first principles (point-charge limit) and got an identical
  result. Separately, derived a closed-form analytic formula for a uniform
  Yukawa shell's *own* exterior potential
  (`Φ_ext = P·∂/∂a[sinh(μa)/(μa)]·exp(-μr)/r`) and matched this script's
  numerical output to 4+ significant figures at three tested `μ` values
  (`0.5, 1.0, 2.0`). The radial-falloff check is genuine and meaningful.
  The angular-uniformity check, while numerically correct, was found to be
  weaker evidence than framed — see the corrected note in §3.
- **Handling of the masslessness tension (§4):** **WEAKENED.** The tension
  itself was flagged honestly and prominently (title, header, §4, verdict
  block, "does NOT establish") — no language elsewhere smuggled the effect
  back in as a working, resolved mechanism. But the specific citation of
  "chameleon/Vainshtein/symmetron-class" screening as the resolving
  mechanism was **wrong-direction**: those mechanisms screen *near* matter
  and un-screen cosmologically, the opposite of what this construction
  needs. The skeptic identified the mechanism that actually works — a
  plain fixed-mass Yukawa with `μ~H₀/c`, no density-dependent screening
  required — and flagged that P1's own "iff *exactly* massless" language
  should, for physical-viability purposes, be read as "iff `μ` negligible
  at the derivation scale." Corrected throughout §4 and the "does NOT
  establish" list above.

## Reproduction

```bash
python experiments/20260803-bridge/P11_yukawa_screening_breaks_double_layer.py
```

The `mu=0` positive control (exact reproduction of P9/`FINDING_dipole_shell`'s
zero) and the two self-consistency checks (angular uniformity, radial
falloff) must all pass before the script proceeds — if any fails, the method
itself is broken and nothing downstream should be trusted.
