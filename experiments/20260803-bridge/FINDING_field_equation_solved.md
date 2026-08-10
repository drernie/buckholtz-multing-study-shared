# Solving the field equation removes the divergence — and separates the two theories

**Date:** 2026-08-10 · unblock step 2 of `FINDING_lq2_test_outcome.md`
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Scripts:** `field_equation_vs_superposition.py` (ruff clean), symbolic work inline

---

## 1. The field equation collapses exactly — the divergence was in the method

For `L = ½f(Φ)|∇Φ|² − ρΦ`, substituting the canonical field `χ` defined by
`dχ/dΦ = √f`, every nonlinear term cancels (`sympy`, treating `|∇χ|` and `∇²χ`
as independent):

```
div(f grad Phi) - (1/2) f'|grad Phi|^2   ==   sqrt(f) * lap(chi)
```

So `∇²χ = ρ·Φ'(χ)`, and **in vacuum `∇²χ = 0` exactly, to all orders in ε**.

`χ` therefore obeys a *linear* equation. It superposes, and Newton's shell
theorem holds for it exactly — `C₂(ρ) ≡ 1`, the one shell factor that never
diverged. `C₃` and `C₄` never appear in the field picture at all.

**The divergence found yesterday was an artefact of the method, not a property of
the theory.** Expanding `Φ(χ)` in powers of ε *first* and then superposing each
`1/rⁿ` term separately assumes linear superposition — which is exactly what the
nonlinear kinetic sector forbids. The correct recipe is the reverse order:

> solve **one linear Poisson equation** for `χ` with the real matter
> distribution, then apply the **algebraic** map
> `Φ(χ) = [(1+3εχ)^{2/3} − 1]/(2ε)`, giving `F = −(1+3εχ)^{−1/3}∇χ`.

Finite for any `ρ`, no shell integrals, no regulator.

## 2. The pairwise-kSZ model, rebuilt and now well-posed

Three separately-superposed kernels — two of which do not exist — are replaced by
one Newtonian kernel modulated by the potential:

```
p_kSZ(r) = -A * K_2(r) * (1 + lam * chihat(r))^(-1/3)
```

with `χ̂(r) = χ(r)/χ(100 Mpc)` built from the same `ξ(r)`, and one new parameter
`λ = 3εχ(r_ref)`. **One** parameter, not two, because the field picture leaves no
independent `ℓ_q`.

| | result |
|---|---|
| Newtonian (`λ=0`) | χ² = 20.8109, 15 bins |
| best fit | **λ = +0.050**, χ² = 20.7827 |
| improvement | **Δχ² = 0.028** for 1 dof — no preference for the nonlinearity |
| 95 % interval | **λ ∈ [−0.238, +2.077]** |
| finite grid points | 3874/4001 (the rest are the unphysical `1+λχ̂ < 0` branch) |

Contrast: the superposition model had **zero** finite grid points.

**Degeneracy check, run because the result would otherwise be meaningless.** A
smooth modulation of an amplitude-profiled kernel can simply be reabsorbed by the
amplitude. It is not: `χ̂` spans 0.001–3.46 across the fitted range, and the
modulation varies by 40 % / 99 % / 228 % at λ = 0.5 / 2 / 10. The constraint is
real, if weak.

Indicative translation (exact only if `χ ∝ 1/r`, which the pairwise `χ` is not):
`λ ∈ [−0.24, +2.08]` ↔ `ℓ_d ~ [−8, +69] Mpc`, best `ℓ_d ~ 1.7 Mpc`. **This is the
first constraint on the covariant completion's single parameter that does not
depend on an arbitrary regulator.**

## 3. Two honest problems the field picture exposes

**IR boundary condition, unspecified.** `Φ` depends on `χ` *absolutely*, not only
through `∇χ`, so the theory is **not invariant under `χ → χ + const`**. The zero
point is physical. Measured, not assumed:

| `r_max` | `χ(25)` | `χ(100)/χ(25)` |
|---|---|---|
| 225 Mpc | 2.9237e+02 | 0.2888 |
| 500 Mpc | 2.9238e+02 | 0.2888 |
| 1000 Mpc | 2.9247e+02 | 0.2891 |
| 3000 Mpc | 2.9248e+02 | 0.2890 |

The *shape* converges; the *absolute value* is set by a boundary condition at
infinity that MULTING does not supply. In a cosmological setting, where the mean
density contributes, this is not a technicality — it is a missing part of the
theory's definition.

**The λ-modulation is a different function of `r` than a `1/r³` force.** So the
field picture and the pairwise picture are not two computations of one thing;
they are different models, and only the first is well-posed.

## 4. The decisive result: the two pictures disagree on mass scaling

This is what the field equation buys that no amount of patching the shell
integrals could. For a point source, `χ = M/r`, and

```
F(r) = M/(r^(5/3) (3 M eps + r)^(1/3))
     = M/r^2 - eps M^2/r^3 + 2 eps^2 M^3/r^4 - ...
```

so `A₂ = M`, `A₃ = εM²`, `A₄ = 2ε²M³`, giving `ℓ_q² = 2ℓ_d²` as before — **but
also** `ℓ_d = εM`, i.e. **the dipole scale grows linearly with the source mass.**

MULTING says otherwise: `ℓ_d = 2β_d (E_th/c² / M) R₅₀₀`, in which the global
constant `β_d` cancels out of the *slope*. Measured directly on the project's 548
clusters (85× mass range), with no β and no H(z) fit anywhere:

| | `d ln ℓ_d / d ln M₅₀₀` |
|---|---|
| MULTING (measured) | **+0.555 ± 0.041** |
| field picture | **+1** exactly, by construction |
| separation | **10.8 σ** |

Decomposed: `E_th/c² ∝ M^{1.269}`, `R₅₀₀ ∝ M^{0.287}`, so `(E_th/M)·R₅₀₀ ∝
M^{0.556}` — the scaling comes almost entirely from `R₅₀₀`, because `E_th/M` is
nearly mass-independent. Across the sample's 85× mass range the two predictions
for `ℓ_d(heaviest)/ℓ_d(lightest)` differ by **13×** (6.3 vs 85).

**Why they differ, structurally.** The field picture generates every higher term
from powers of the *same* source, so tier `n` scales as `Mⁿ`. MULTING assigns
each tier an *independent* charge — `m` at the monopole, `k·m` at the dipole,
`k·k` at the quadrupole. A single scalar field sourced by `ρ` cannot produce
independent charges per tier.

This is the **third independent route to the same obstruction**: `CANDIDATE-L1`
found it as "multi-tier coefficient isolation," the weak-field matching found it
as the repulsive-sign/EP tension, and it now appears as a 10.8 σ mass-scaling
discrepancy measurable on real clusters. Three different methods, one conclusion.

---

## Verdict

```
Field equation solved                : YES, exactly. lap(chi) = 0 in vacuum to all
                                       orders; chi linear, Phi(chi) algebraic
Divergence                           : REMOVED -- it was the method (superposing an
                                       eps-expansion), not the theory
kSZ constraint, regulator-free       : lam = +0.050, 95% [-0.238, +2.077];
                                       Delta chi2 = 0.028 -> no preference for eps != 0
                                       Not degenerate with the amplitude (checked)
New problem exposed                  : Phi is not invariant under chi -> chi + const;
                                       the IR boundary condition is undefined
Field picture vs MULTING             : SEPARATED at 10.8 sigma on d ln(ell_d)/d ln M
                                       (+1 vs +0.555 +- 0.041, n = 548 clusters)
Status of the covariant completion   : it is a well-posed, finite, one-parameter
                                       theory -- but NOT a completion of MULTING's
                                       charge structure. Same obstruction as
                                       CANDIDATE-L1, reached independently.
```

## What this does NOT mean

1. It does **not** show MULTING is wrong. It shows this particular single-scalar
   completion has a different charge structure, so it is not MULTING's completion.
   A theory with one field per tier, or with `k` as an independent field, is
   untouched by this.
2. The `λ` bound is **not** a bound on MULTING's `β_d`. It constrains this action,
   whose `ℓ_d = εM` means something different.
3. `Δχ² = 0.028` is **not** evidence that ε = 0. It is evidence that 15 pairwise
   kSZ bins have little power on this parameter.

## What would move it next

- The 10.8 σ mass-scaling separation is the cheapest real test in the whole
  bridge track: it needs no β, no H(z), no AI-fitted number, and the data are
  already in the repository. Its weak point is that `ℓ_d^MULTING` is *derived*
  from the preprint's own definitions rather than measured — worth an independent
  check of that derivation before the number is used anywhere.
- A completion with `k` as a second field would evade §4 entirely. That, not
  patching this one, is where the covariant programme has room left.
