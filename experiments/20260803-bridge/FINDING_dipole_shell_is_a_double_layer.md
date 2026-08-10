# The k-sector is a contact interaction: a radial-dipole shell exerts no force off itself

**Date:** 2026-08-10 · attempted the "one cheap test" named in
`FINDING_two_charge_completion.md`, and found that the test cannot exist
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** inline, reproduced below · positive control passes

---

## What was being attempted

`β_q/β_d` is predicted by three mutually exclusive structures — **1.2247**
(two-charge), **2.8284** (single-field R7), **4.0** (AI fit). An independent
determination of `ℓ_q²/ℓ_d²` separates all three at once, and the pairwise-kSZ
likelihood constrains exactly that ratio. The blocker was that `K₄` diverges under
superposition, so the plan was to rebuild it in the field picture, as was already
done for the dipole.

Rebuilding it required one prerequisite: the shell factor for a **dipole density**,
recomputed correctly. That prerequisite killed the plan.

## The result

A spherical shell carrying radially-aligned dipole density is a **double layer**.
Its potential jumps across the shell and is constant on both sides:

```
  shell radius a = 1, angular potential integral, field point at radius r

       r         Phi       dPhi/dr     d2Phi/dr2
    0.10   -2.000000      1.11e-12      0.00e+00
    0.50   -2.000000      0.00e+00     -1.78e-07
    0.90   -2.000000     -1.11e-12      2.89e-07
    1.20    0.000000     -1.69e-11      1.69e-07
    2.00    0.000000     -3.47e-13     -1.39e-09
   10.00    0.000000     -2.17e-14      6.07e-10
```

**Positive control**, run first and passing exactly: the same integral for a
*monopole* shell returns `2/a` inside and `2/r` outside — Newton's shell theorem,
`C₂ = 1`. So the geometry and quadrature are right, and the dipole result is
physics rather than a numerical artefact.

**Every derivative vanishes off the shell.** That is the load-bearing part. A point
dipole couples to `∇Φ` and a quadrupole to `∇∇Φ`, so it is not only the monopole
that feels nothing:

> **Both the `k·m` and the `k·k` tiers feel nothing from such a shell.
> The entire k-sector is a contact interaction.**

## What this says about the divergence found yesterday

The old shell factor `C₃(ρ) ~ (1−ρ)⁻¹` was not describing a long-range force. It
was a **smeared delta function at contact**, and its integral accumulates exactly
where a delta would:

| `ρ` | `C₃(ρ)` | fraction of `∫₀¹C₃` below `ρ` |
|---|---:|---:|
| 0.5 | 1.22 | 0.172 |
| 0.9 | 3.45 | 0.404 |
| 0.99 | 26.46 | 0.622 |
| 0.999 | 252.03 | 0.813 |

Nearly a fifth of the "signal" sits in the last thousandth of the range. The
regulator `ρ ≤ 1−10⁻⁹` was not a numerical convenience — it was setting the weight
of a contact term by hand.

## Consequences, in order of severity

**1. The cheap test does not exist.** The pairwise-kSZ route to `ℓ_q²/ℓ_d²` is
dead, not blocked. Rebuilding `K₄` in the field picture gives `K₄ = 0`, so the
three candidate `β_q/β_d` values cannot be separated this way. This closes the
route proposed one finding ago.

**2. The existing `ℓ_d` constraint is measuring the regulator.** Yesterday's verdict
was `UNTRUSTED-ENVIRONMENT` (the value moves 10.6 % under grid refinement). It is
now stronger and more specific: the quantity `K₃` integrates does not couple to the
observable the way the template assumes. `docs/134`'s `ℓ_d` numbers should not be
cited as constraints on a physical dipole length.

**3. A symmetry statement that does not depend on the two-charge construction at
all.** A dipole force cannot survive averaging over a statistically isotropic matter
distribution at first order, by either route available:

- dipoles **radially aligned** (induced — the configuration the two-charge
  construction *derived* as the only one matching MULTING's symmetric `F_d`)
  → double layer → zero force off contact, shown above;
- dipoles **randomly oriented** (intrinsic) → `⟨p⟩ = 0` → zero at first order.

There is no third option, so the conclusion is independent of which branch is
right. This is the same fork P3 identified; it now closes on both prongs for
isotropically-averaged observables.

## What this does NOT mean

1. It does **not** show MULTING's dipole is zero. The **two-body point-point**
   interaction is untouched: that is where the `1/r³` and `1/r⁴` terms live, and the
   whole two-charge derivation of them stands.
2. It does **not** apply to anisotropic configurations. The result is for spherically
   symmetric shells — which is exactly what the `C_k` formalism assumes, so it is
   fatal *within that formalism*, not in general. A calculation that keeps the
   quadrupolar anisotropy of the pair environment could give something non-zero.
3. It is **not** a statement about the cosmological `H(z)` claim. That would need
   the same calculation in an expanding background with the correct averaging, which
   has not been done here. Flagged as the obvious next question, not answered.

## Verdict

```
Prerequisite for rebuilding K_4        : computed
Radial-dipole shell force off-shell    : ZERO -- double layer, all derivatives vanish
Positive control (monopole shell)      : PASSED exactly, C_2 = 1
Old C_3 divergence                     : identified as a smeared contact delta,
                                         with the regulator setting its weight
The proposed cheap test                : DEAD, not blocked -- K_4^field = 0
docs/134 ell_d constraint              : should not be cited as a physical dipole length
Symmetry result                        : first-order dipole force cannot survive
                                         isotropic averaging, on either branch
Two-charge completion                  : UNAFFECTED -- its derivation is two-body
```

## Where a real test could still come from

The three `β_q/β_d` values remain unseparated. What is needed is an observable that
does **not** isotropically average the dipole away:

- an **anisotropic** estimator — the quadrupole of the pairwise velocity field, or
  the alignment of the kSZ signal with the pair axis, rather than the monopole
  kernel used here;
- a genuinely **two-body** system where the point-point force applies directly, so
  no smoothing occurs at all;
- the `E_G` / scale-dependent-bias probes P3 listed as untested, re-examined for
  whether they average isotropically in the same way.

Before any of those, the honest statement is: **no current constraint in this
repository bears on `ℓ_q²/ℓ_d²`.**
