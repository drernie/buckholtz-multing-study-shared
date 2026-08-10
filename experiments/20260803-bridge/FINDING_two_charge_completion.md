# A completion with k as a second charge — it works, and it makes MULTING's own sign rule a theorem

**Date:** 2026-08-10 · takes the one route left open by `FINDING_field_equation_solved.md`
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `two_charge_completion.py`, ruff clean, three positive controls

---

## 1. The clue was in MULTING's own parametrisation

The preprint sets `|r_qAB|² = β_q² r_A r_P` — a **product of the lever arms of two
different bodies**. One body's genuine quadrupole moment cannot produce that. Two
bodies' **dipole** moments produce it automatically.

So MULTING's three tiers are not a multipole series in one charge. They are the
three bilinears of **two** charges:

| tier | charge structure | MULTING's own form |
|---|---|---|
| monopole | `m_A m_P` | `G m_A m_P` |
| dipole | `k_A m_P + m_A k_P` | `G c⁻²β_d(k_A m_P r_A + k_P m_A r_P)` — symmetric, two terms |
| "quadrupole" | `k_A k_P` | `G c⁻⁴ k_A k_P β_q² r_A r_P` |

## 2. The alternating sign rule stops being a postulate

§2.2 of the preprint *posits* that even tiers attract and odd tiers repel. In a
two-charge theory that is the binomial expansion of a single squared charge whose
parts have opposite sign:

```
(m_A - kappa k_A)(m_P - kappa k_P)
    = m_A m_P  -  kappa (k_A m_P + m_A k_P)  +  kappa^2 k_A k_P
        +                    -                        +
```

The signs are forced, not chosen. **A postulate becomes a theorem.** This is the
single most valuable thing the construction buys, and it holds independently of
every number below.

## 3. The construction, and what fixes its free choices

One massless scalar, ordinary `1/r` propagator; the second charge enters through a
**derivative coupling**, so the extra powers of `1/r` come from gradients rather
than from an exotic propagator. Local and ghost-free — which the alternatives are
not: a `1/r³` potential from a non-derivative propagator needs higher derivatives
(ghost) or a fractional kinetic operator (unparticle, where NR-019 already found
scalar-scalar exchange attractive, the wrong sign).

Each body is built as a **physical dipole** — a real pair of opposite charges at
finite separation — and the interaction is summed pair by pair over the `1/r`
kernel and then expanded, so every sign is produced by the algebra.

**Orientation is not a free choice.** MULTING's `F_d` is symmetric under A↔B.
Checked against every configuration:

| configuration | A↔B symmetric? | `A₃` term |
|---|---|---|
| parallel (both `+z`) | **no** | `2d_A m_B q_A − 2d_B m_A q_B` |
| **mirror-symmetric** | **yes** | `2d_A m_B q_A + 2d_B m_A q_B` |
| parallel (both `−z`) | **no** | `−2d_A m_B q_A + 2d_B m_A q_B` |

Only the mirror-symmetric configuration reproduces MULTING's form. Physically:
each body's moment is radially aligned on the other — **induced polarisation**,
which is precisely the branch P3 flagged as the one that *does* enter linear
growth (Blanchet DDM), not the intrinsic-random branch. That is a consequence,
not an assumption, and it re-opens the fσ8 question P3 had scoped away.

**The sign of the dipole charge is then forced too.** In that configuration
`A₃ = −2(d_A m_B q_A + d_B m_A q_B)`, which for positive `q` would make the dipole
*add* to attraction. MULTING needs it repulsive ⇒ `q` must be opposite in sign to
mass ⇒ exactly the `(m − κk)` structure §2 already implied. Two independent routes
to the same conclusion.

## 4. The numbers, with the multipole factors that were not free to choose

With `q = −κk/c²` and lever arm `d = r_A` (MULTING's own `r_dA`):

```
ell_d   = A3/A2 = 2 kappa (k_A m_P r_A + k_P m_A r_P)/(c^2 m_A m_P)  ==  2 (u_A + u_P)
ell_q^2 = A4/A2 = 6 kappa^2 k_A k_P r_A r_P /(c^4 m_A m_P)           ==  6  u_A u_P
```

both verified identically, with `u_i ≡ κk_i r_i/(c²m_i)`. These are **exactly**
MULTING's forms `ℓ_d = β_d(u_A+u_P)`, `ℓ_q² = β_q² u_A u_P` — the multipole
expansion supplies the numerical factors **2** and **6**:

> **β_d = 2, β_q = √6, so β_q/β_d = √6/2 = 1.2247** — zero free parameters after κ.

| quantity | this construction | single-field R7 | AI-fitted β (Gate 2) |
|---|---:|---:|---:|
| `β_q/β_d` | **1.2247** | 2.8284 | 4.0000 |
| `ℓ_q²/ℓ_d²`, identical bodies | **0.375** | 2 | 4.0 |

**Attractive at every separation, strictly.** `F/A₂ = 1/r² − ℓ_d/r³ +
(3/8)ℓ_d²/r⁴` has discriminant `−ℓ_d²/2 < 0`, so no real root. Branch C's
condition was `ℓ_q² ≥ 0.25 ℓ_d²`; this gives 0.375 — satisfied with margin, and
**not by assumption**: the 3/8 is `(3/2)·u_Au_P/(u_A+u_P)²` bounded by AM-GM, with
the 3/2 coming from the factors 2 and 6.

*(A first pass claimed 1/4, a perfect square, and exact saturation of branch C's
bound. That was wrong — it dropped the multipole factors 2 and 6, assuming
`ℓ_d = κ(u_A+u_P)`, `ℓ_q² = κ²u_Au_P` instead of deriving them. Corrected above.)*

## 5. The obstruction it was built to clear — cleared

```
                          d ln ell_d / d ln M500
  MULTING (measured, n=548)     +0.555 +- 0.041
  single-field completion       +1     exactly      -> 10.8 sigma discrepancy
  this construction             ell_d = 2(u_A+u_P)  -> MULTING's own form, REPRODUCED
```

The mass-scaling obstruction was specific to a single scalar sourced by `ρ`, whose
tier `n` must scale as `Mⁿ`. Giving `k` its own charge removes it completely. The
prediction made in the previous finding — "a completion with `k` as a second field
would evade §4 entirely" — is confirmed.

## 6. Controls, including one that caught a real error

Three checks with independently known answers, all hard stops:

1. **zeroth order in both lever arms** → must be exactly `m_A m_B/r`, since a
   dipole carries no net charge. **This is the one that caught the bug.**
2. dipoles switched off → `m_A m_B/r`
3. pure dipole-dipole → `−2 p_A p_B/r³`, the textbook value

The first version computed each pair separation with a sign test that got several
pairs backwards; the symptom was terms like `2m_A q_B/r` surviving at zeroth
order. Its only control was #2 — and **setting `q = 0` removes exactly the terms
that were wrong**, so the control passed while the result was nonsense. The fix
was to stop deciding signs at all: with `r ≫ d` every separation is `z_b − z_a`.

*A control that switches off the feature under test cannot test it.* Same shape as
the digitisation-gate lesson: the control must exercise the failing path.

---

## Verdict

```
Two-charge completion exists         : YES, local, ghost-free, one 1/r propagator,
                                       second charge via derivative coupling
MULTING's alternating sign rule      : DERIVED, not postulated -- it is the binomial
                                       expansion of (m - kappa k)_A (m - kappa k)_P
Orientation                          : FIXED by A<->B symmetry of F_d -> induced
                                       (radially aligned) polarisation, not intrinsic
Sign of the k-charge                 : FORCED opposite to mass by the repulsive dipole
Mass-scaling obstruction             : CLEARED -- ell_d = 2(u_A+u_P) is MULTING's form
New zero-parameter prediction        : beta_q/beta_d = sqrt(6)/2 = 1.2247
                                       (AI-fitted value is 4.0, but that is a FIT to
                                       H(z) by an AI service -- Gate 2, not a test)
Attractive everywhere                : YES, strictly (discriminant -ell_d^2/2 < 0)
```

## What this does NOT establish

1. It does **not** show this is MULTING's completion — it shows a two-charge
   theory reproduces its charge structure, sign rule and mass scaling. The `β`
   ratio is a genuine discriminator but has no trustworthy measured value yet.
2. `β_q/β_d = 1.2247` is **not** tested against 4.0. Those β came from an AI
   service fitting `H(z)`; comparing to them tests the fit.
3. The derivative coupling is written at the level of a static two-body energy.
   A covariant action reproducing it, and its cosmological limit, are not done.
4. `d = r_A` (identifying the lever arm with the body's radius) follows MULTING's
   `r_dA = β_d r_A` but is its convention, not a derivation.

## The one cheap test this creates

`β_q/β_d` is now predicted by three mutually exclusive structures — 1.2247
(two-charge), 2.8284 (single-field), 4.0 (AI fit). Any **independent**
determination of `ℓ_q²/ℓ_d²` separates all three at once. The pairwise-kSZ
likelihood constrains exactly that ratio and needs no β conversion — but its `K₄`
kernel diverges under superposition, so it must first be rebuilt in the field
picture, as `field_equation_vs_superposition.py` did for the dipole.
