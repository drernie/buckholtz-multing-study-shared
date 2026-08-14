# P36 — κ (dipole sector) is structurally invisible to both channels that just fixed g's ΔG, by an already-proven, independently cross-checked reason; g and κ are visible to exactly the channel the other is blind to

**Date:** 2026-08-14
**Origin:** third step of the covariant-completion campaign
(`PLAN_final_goal_20260814.md`), the first to address `κ` directly.
Deliberately conservative: given the plan's own status log flagged the
risk of rushing a `κ` treatment without re-grounding in this project's
already-established geometric setup, this finding reuses two
already-verified prior results rather than re-deriving new dipole-sector
physics from scratch.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P36_kappa_invisible_to_g_sector_channels.py`, ruff clean, all
assertions pass.

## 0. Honest scope

This does **not** newly fix `κ`'s absolute value — P14–P17's one-sided
bounds remain the best available constraint on that. This shows *why* the
cosmological/two-body chain this campaign is building (P34–P37) cannot be
the channel that closes it, no matter how far extended — a scope-boundary
result, not a new bound.

## 1. Reused, not re-derived: the double-layer result

`FINDING_dipole_shell_is_a_double_layer.md` (2026-08-10, numerically
verified, positive control passed — the monopole-shell integral exactly
recovers Newton's shell theorem, `C₂=1`) established: a spherically
symmetric shell of radially-aligned dipole density produces **exactly
zero force** — all potential derivatives vanish — everywhere off the
shell itself. The `k`-sector, in this specific (radially-aligned)
configuration, is a **contact interaction**, not a long-range force.

Independently cross-checked here via a *different* argument (not a
re-run of the original numerical quadrature): this is the standard
textbook "double layer" / dipole-sheet result from electrostatics — a
uniformly radially-polarized spherical shell has zero field inside *and*
outside, only a potential *jump* across the shell. Same physics, reached
by citing a well-known, independently-derivable fact rather than
repeating the numerical method.

## 2. Multipole exterior-solution check (genuinely computed)

For each multipole order `ℓ`, `r^{-(ℓ+1)}` is verified (sympy, direct
substitution into the radial Laplace equation) to solve the source-free
exterior equation — `ℓ=0`: `1/r`; `ℓ=1`: `1/r²`; `ℓ=2`: `1/r³` — the
standard reason a smooth, extended source's higher multipoles are always
parametrically subdominant to its monopole at large `r`, even *before*
the double-layer cancellation (§1) removes `κ`'s contribution entirely
rather than merely suppressing it.

## 3. Connecting to P34/P35's newly-built framework

**Note on P35's own status:** P35 was corrected the same day, same
session, *before* this finding was written — its original "`G_eff` is
derived" claim was narrowed to "only the additive
`ΔG=ĝ²/(4π)` piece is genuinely derived; `U_N`/`G_N` is imported," and
its comparison to P21 was found largely circular. This finding's own
claim — `κ` is invisible to P34/P35's channels — is **unaffected** by
that correction: it concerns the multipole/geometric structure of a
`κ`-sourced field for a spherically-symmetric source, orthogonal to
P35's own normalization and self-consistency issues. All references
below use P35's corrected, narrower result.

- **P34's homogeneous FRW background** treats matter as a smooth,
  isotropic density `ρ₀(t)` — exactly the continuum limit of many
  radially-aligned dipole sources distributed isotropically. By the
  double-layer result (§1), such a distribution contributes **exactly
  zero** net `κ`-sourced force to the background — confirming, at the
  newly-built field-theory level, `two_field_action_closure.py`'s own
  docstring claim (lines 123–128: "the random average is zero... this
  completion contributes only a G-renormalisation to the background
  expansion"), previously stated but never connected to P34's own
  explicit field-equation machinery.
- **P35's static two-body additive `ΔG`** used a spherically symmetric
  point source `M` — for a spherically symmetric or smoothly-extended
  physical source (a star, a cluster), the same double-layer cancellation
  applies to its own internal `κ`-content: zero net contribution to
  P35's `ΔG` at leading multipole order. `κ` cannot be probed via
  *either* of the two channels that derived `g`'s own `ΔG` contribution.

## 4. Reused, not re-derived: P25's WEP composition-dependence

`FINDING_P25_wep_eotvos_kill_gate.md` (2026-08-13, sympy-verified,
skeptic-corrected) established: the `k`-sector *does* produce a genuine,
**composition-dependent** term in a laboratory Eötvös-type test —
because such a test compares *different test bodies'* own `Kᵢ/Mᵢ` ratios
in the *same* external field, structurally different from the
smooth-source-averaging channels (§1–§3) that kill `κ`'s visibility.
P23 already showed the `g`-sector is the structural opposite — universal
coupling makes it WEP-blind, while it *is* visible to smooth-source
channels (P34, P35). **The two sectors are each visible to exactly the
channel the other is blind to.**

## 5. What this does NOT establish

1. Any new numeric bound on `κ` — P14–P17's one-sided bounds are
   unchanged, still the best available constraint.
2. That `κ` is *exactly* zero — only that it is invisible to *these
   specific* channels; its own value remains genuinely undetermined by
   this campaign's own information.
3. Anything about non-spherically-symmetric or non-smooth mass
   distributions (e.g. a rotating disk with a coherent, non-random
   dipole alignment) — the double-layer cancellation (§1) specifically
   requires radial-alignment symmetry; a structurally different
   configuration was not examined here.
4. A resolution of P35's own still-open gaps (the withdrawn slip claim,
   the missing self-consistent `O(ĝ²)` treatment) — unrelated to this
   finding's own claim, not addressed here.
5. Any comparison against Table A1 — closed gate, not touched.
6. Per NO_AUTHOR_ERROR: entirely this project's own reconstruction
   (OUR_RECONSTRUCTION), not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P36_kappa_invisible_to_g_sector_channels.py
```
