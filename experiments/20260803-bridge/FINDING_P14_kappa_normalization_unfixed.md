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

---

## 1. The physics: self-energy is a real, separate, orientation-independent channel

For `N` independent dipole sources, the total field energy splits exactly:

```
∫(∇φ_total)² d³x = Σᵢ ∫(∇φᵢ)² d³x            [self-energy: per-source, ORIENTATION-INDEPENDENT]
                  + Σ_{i≠j} ∫∇φᵢ·∇φⱼ d³x       [cross terms: THIS is what P9's double-layer kills]
```

`FINDING_dipole_shell_is_a_double_layer.md` (P9) proved the **cross-term**
piece vanishes exactly for an isotropic shell — that is a statement about
how different sources' fields interfere with each other, not about any
single source's own field energy. The **diagonal (self-energy)** term does
not care how the dipoles are oriented relative to each other; it is
present for *any* nonzero `κ`, with no assumed asymmetry (P9's `ε`) or
fixed mediator mass (P11's `μ`) required. This is a genuine, separate
channel worth checking on its own terms.

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

**Why the number is neither large nor small in any meaningful sense: `κ`'s
absolute scale has never been independently fixed anywhere in this
project.** `β_d=2` and `β_q=√6` are **dimensionless coefficients**
multiplying `(u_A+u_P)`, where `u_i≡κkᵢrᵢ/(c²mᵢ)` itself still scales
*linearly* with `κ`. P1's own "zero free parameters after `κ`" phrase means
exactly what it says: `κ` remains free. Every prior bridge-track
calculation that produced a real, checkable number did so either via a
**ratio** in which `κ` cancels (`β_q/β_d`, `ℓ_q²/ℓ_d²` — P1's kernel
invariant `Λ`) or via a **separate physical scale unrelated to `κ`**
(P11/P12's `μ~H₀/c`, a mediator *mass*, not `κ`). This self-energy
calculation is the **first one in the entire P1–P14 sequence that depends
on `κ`'s absolute magnitude directly**, rather than a ratio or a different
parameter — and building it is what revealed that magnitude was never
pinned down. The printed `3.3×10¹¹` implicitly assumed `κ~O(1)` in SI
units, with no basis; rescaling `κ` moves this number by any amount in
either direction, so as printed it carries **no information**.

## 4. Why this is a genuinely new, more fundamental gap than P13a's

P13a found `g` and `κ` are independent, unrelated couplings — a gap about
how two *different* parameters relate. This finding shows something
sharper: **`κ` alone has no fixed scale**, independent of any relationship
to `g`. Any future attempt to compute an absolute (not ratio-based)
physical quantity from the k-sector — an energy density, a force
magnitude in physical units, an observable amplitude — will hit this same
wall until `κ`'s scale is fixed by some additional physical input (e.g., a
measured value of `β_d` from real data, which this project's own
`FINDING_table_a1_provenance.md`/`MODEL_SPEC_AUDIT.md` already flag as
`BLOCKED_BY_TARGET_PROVENANCE` — Table A1's fitted `β_d=4.5` cannot be used
as ground truth, per this project's own Gate 2 discipline).

## What this does NOT establish

1. **That the self-energy channel is large or small.** The physics of the
   channel (§1–§2) is verified; its magnitude (§3) is currently undefined,
   not "big" or "negligible."
2. **A resolution of P13a's own open question** (whether Archidiacono's
   bound bears on `κ`). If anything, this finding shows that question is
   even less tractable than P13a implied — not only is the `g`↔`κ`
   relationship unknown, `κ`'s own scale is unknown.
3. **That `κ` can never be fixed.** Only that nothing in this project has
   fixed it yet, and that fixing it (from real data, independent of the
   `BLOCKED_BY_TARGET_PROVENANCE` fitted values) is a real prerequisite
   for any future absolute-magnitude calculation in this sector.
4. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P14_dipole_self_energy_omega_bound.py
```

The monopole positive-control assert must pass before the dipole result is
trusted. The script's own final verdict block states the corrected
conclusion (§3 above) directly — read it in full, not just the printed
`Ω_φ` number, which is explicitly flagged in the script's own output as
not physically meaningful as printed.
