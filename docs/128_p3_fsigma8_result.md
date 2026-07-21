# docs/128 — P3 fσ8 Test: Broad Claim FALSIFIED, Narrow Claim Survives

**Date:** 2026-07-22
**Status:** the broad claim "MULTING dipole is degenerate with ΛCDM at linear order"
is **FALSIFIED** (context-asymmetry skeptic, 5 independent holes). A narrow claim
survives; the real test is blocked on Q006 (the MULTING Lagrangian).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NOT_AUTHOR_ERROR
**Artifact:** `scripts/p3_fsigma8_growth.py` (linear-growth solver + real DESI point).
**Real data:** DESI DR1 PV survey fσ8(z=0.07) = 0.450 ± 0.055, Ωm=0.301, σ8=0.834,
"consistent with ΛCDM and GR" (arXiv:2512.03231, digitized in
`literature/refs_digitized/`).

---

## What was tested and the numeric result

A standard linear-growth ODE with a phenomenological "coherent dipole growth
strength" `A_dip` in the source term. `A_dip=0` (isotropic-random dipole, via the C1
`⟨n̂⟩=0` mechanism) reproduces the real DESI point at **0.06σ** (0.4465 vs
0.450±0.055) — a validation of the solver. A positive control (`A_dip≠0`) shifts fσ8
measurably; at fixed Ωm/σ8 the shift is bounded `|A_dip| < ~0.21`.

## Why the broad claim is FALSIFIED (skeptic, 5 holes)

The claim "MULTING dipole leaves *linear fσ8 degenerate with ΛCDM*, so the signal is
purely second-order" over-reached on five independent counts:

1. **Induced-polarization branch untested (strongest).** The `⟨n̂⟩=0` argument covers
   only *intrinsic-random* dipoles. If the dipole is **induced** by the tidal field
   (gravitational polarization, `p ∝ ∇∇Φ ∝ δ` — exactly Blanchet & Le Tiec's dipolar
   dark matter, arXiv:0901.3114), then `p` correlates with the density mode, is NOT
   random, and **does** enter linear growth. MULTING's dipole (from an object's
   internal kinetic energy × radius) is structurally compatible with tidal
   polarization; nothing derives it away. This branch is where a real linear signal
   could live, and it was not tested.
2. **Fixed-Ωm bound is an artifact.** `|A_dip|<0.21` was computed holding Ωm/σ8 fixed.
   Marginalizing over Ωm absorbs the signal — the project's own `beta_cv.py` found
   Blanchet-type dipolar DM degenerate with ΛCDM at ΔAIC=+0.74 after refitting. The
   real bound is ~3–10× looser (the degeneracy is *worse*, not the number tighter).
3. **Wrong parametrization.** `A_dip=const` is scale-independent; a real dipole
   (`1/r³` vs monopole `1/r²`) is k-dependent — needs a `μ(k,z)` form. A constant
   cannot represent, hence cannot constrain, the actual signature.
4. **One data point.** z=0.07 alone trivially matches ΛCDM (which is tuned to it). The
   discriminating information is in the *shape* of the full fσ8(z) compilation
   (6dFGS→DESI, z≈0.02–1.5, ~20 points).
5. **False hand-off to 2nd order.** "Linear dead → P(k)/bispectrum" skips ≥6 other
   first-order probes: `E_G(k,z)`, velocity-divergence `P_θθ`, scale-dependent bias,
   RSD hexadecapole (ℓ=4), `δ_g×κ_CMB` (grav. slip), void velocity profiles.

## Narrow claim that survives

> *For the **intrinsic-random-orientation** branch of MULTING dipoles (`n̂` drawn
> isotropically, uncorrelated with the local tidal field), the coherent linear-growth
> source averages to zero (C1 mechanism), so this branch is ΛCDM-equivalent for fσ8 at
> linear order, and its residual (variance-driven) signal is second-order. This does
> NOT cover the induced-polarization branch, which injects a linear-order source
> (Blanchet-like) and requires a separate `μ(k,z)` analysis, marginalized over Ωm/σ8,
> tested against the full fσ8(z) compilation and at minimum E_G(z), before any
> degeneracy claim can be made.*

## Kill-condition — routes through Q006 (the MULTING Lagrangian)

The cheapest differentiating test between the two branches: **derive the linear
response of MULTING's dipole orientation to an external tidal field `∇∇Φ` from the
MULTING Lagrangian** (this is exactly open question Q006 in `facts.json`). Let `ξ` be
the coupling coefficient `n̂ ↔ ∇∇Φ`:

- **ξ = 0 by symmetry** → the induced channel is absent → the intrinsic-only narrow
  claim survives and fσ8 is genuinely uninformative for MULTING's dipole.
- **ξ ≠ 0** → the induced channel injects `A_dip(k,z) ∝ ξ·δ` → run a `μ(k,z)` /
  `beta_cv.py`-analog analysis, marginalized over Ωm/σ8, on the full fσ8(z)
  compilation + E_G, before any degeneracy statement.

So P3's real resolution is **blocked on Q006** — the same missing-Lagrangian gap that
sits under the whole cosmological branch. This is a genuine finding: the fσ8 question
is not independently answerable; it inherits the corpus's central open question.

## Consequence for the ladder (decisions.md)

P3 is **NOT complete** — it is partially explored (intrinsic branch, LCDM-equivalent;
induced branch untested). The audit statement:

- The dipole's cosmological signature question does not close at the background (P2:
  q-blind) NOR at linear fσ8 (P3: intrinsic branch degenerate, induced branch
  untested) — it routes into **Q006 (the Lagrangian)**, which determines whether the
  induced-polarization channel exists.
- If the project wants a real linear-order test, the correct object is a `μ(k,z)`
  analysis on the full fσ8(z) compilation + E_G, contingent on Q006's ξ. This is a
  substantial piece of work, gated on the Lagrangian.

## Process note

This is the session's strongest skeptic catch: the P3 claim was drafted, looked
clean (0.06σ data match, working control), and was FALSIFIED-as-worded on physics
grounds before being recorded as a result — exactly the discipline that caught
NR-015 and NR-016. The narrow claim + the Q006 kill-condition are the honest residue.
The skeptic also surfaced a concrete reading lead: Blanchet & Le Tiec 2008–2013
(0804.3518, 0901.3114, 0812.4076) already worked out dipolar-DM cosmological
perturbations and the first-order degeneracy — a ready playbook before any
independent second-order claim.
