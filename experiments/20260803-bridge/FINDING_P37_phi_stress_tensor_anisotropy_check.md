# P37 — φ's own static stress tensor has genuine, computed anisotropic stress at the same O(ĝ²) order as ΔG: a real slip *source* exists, its effect on Φ,Ψ not yet solved for

**Date:** 2026-08-14
**Origin:** fourth step of the covariant-completion campaign
(`PLAN_final_goal_20260814.md`), resumed at a deliberately slower pace
per explicit user instruction — one step at a time, full processing
before the next. Directly targets the narrowest, safest piece of P35's
own flagged open question (its withdrawn §5, its §6 point 8): does `φ`'s
own stress-energy, for the static solution `φ(r)=ĝM/(4πr)` P35 already
derived, actually have a nonzero anisotropic (traceless spatial) part?
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P37_phi_stress_tensor_anisotropy_check.py`, ruff clean, all
assertions pass.

## 0. Honest scope — deliberately narrow

This does **not** solve the full linearized Einstein `ij`-equation for
the resulting metric slip — that is a larger, separate step, appropriately
deferred, not attempted here. This finding only computes `φ`'s own
stress tensor `T_μν^φ` explicitly and checks whether its spatial part is
proportional to the identity (isotropic, no slip *source*) or has a
genuine traceless remainder (anisotropic — a real slip *source*, though
not yet its magnitude on the actual metric potentials `Φ,Ψ`).

**A nonzero anisotropic source is necessary but not sufficient for
`Φ≠Ψ`.** The standard linearized `ij`-trace-free Einstein equation reads
`∇²(Φ−Ψ)∝(anisotropic stress source)`; a nonzero right-hand side makes
`Φ=Ψ` require an implausible, fine-tuned cancellation *in solving that
equation* — but the equation itself is not solved here. This finding
establishes the source exists; it does not establish the sign or
magnitude of `Φ−Ψ`.

Uses the flat-background `φ(r)` from P35 (re-used, not re-derived) as the
leading-order field — standard, legitimate perturbative bookkeeping:
`φ`'s own equation only needs the flat metric to be solved correctly at
this order; its back-reaction on the metric is precisely the *next*-order
question this finding is investigating the source for, not something it
needs to have already solved to ask the question.

## 1. Method — the standard canonical scalar stress tensor, computed directly

`T_μν=∂_μφ∂_νφ−(1/2)g_μν(∂φ)²` — the same formula implicit in P34's own
`ρ_φ=φ̇²/2` (there, the homogeneous, time-only case; here, the static,
spatial-gradient-only case). Evaluated in Cartesian coordinates on
`φ(r)=ĝM/(4πr)` to avoid any risk of a spherical-coordinate conversion
error:

```
T_xx = ĝ²M²(x²−y²−z²)/(32π²r⁶)
T_yy = ĝ²M²(−x²+y²−z²)/(32π²r⁶)
T_zz = ĝ²M²(−x²−y²+z²)/(32π²r⁶)
T_xy = ĝ²M²xy/(16π²r⁶)
```

## 2. The load-bearing check — radial vs. tangential stress on the z-axis

On the `z`-axis (`x=y=0,z=r`), the radial direction is manifestly
`ẑ`, so `T_zz` is the radial stress and `T_xx=T_yy` (verified equal by
the script's own assertion) is the tangential stress by symmetry:

```
T_radial     =  +ĝ²M²/(32π²r⁴)
T_tangential =  −ĝ²M²/(32π²r⁴)
T_radial − T_tangential = ĝ²M²/(16π²r⁴)    (nonzero for all r>0)
```

**Isotropic (no anisotropic stress)?** `False` — confirmed by direct
calculation, not assumed.

## 3. Cross-check — the trace

`trace(T_ij) = Σᵢ(∂ᵢφ)² − (3/2)(∂φ)² = −(1/2)(∂φ)²` in 3 spatial
dimensions (a standard identity for this stress-tensor definition,
independently re-derived by hand before writing the assertion — the
script's own first attempt at this formula had the wrong sign, caught by
its own assertion failing on the first run, fixed before this document
was written). Confirmed exactly (script assertion, zero difference)
against the direct computation from §1 — a genuine algebraic
cross-check, not a repeat of the same computation.

## 4. What this establishes, precisely

`φ`'s own static stress-energy has genuine, nonzero anisotropic stress at
`O(ĝ²)` — the **same** parametric order as `ΔG` itself (both scale as
`ĝ²M²`). This means P35's original, withdrawn claim ("second-order-small,
no slip") could not have been correct even at the level of checking
whether a source exists — the source is present at exactly the order
that claim dismissed. This *sharpens* P35's own honest "genuinely open"
status from §5, moving it from "unknown whether a source exists" to
"a source demonstrably exists; its effect on `Φ,Ψ` is the remaining open
question."

## 5. What this does NOT establish

1. The actual value or sign of `Φ−Ψ` — requires solving the linearized
   `ij`-Einstein equation sourced by this `T_ij`, not attempted here.
2. Anything about the *cosmological* (homogeneous, P34) case — there,
   `φ(t)` has no spatial gradient at all, so this specific anisotropic-
   stress mechanism does not apply; P34's background remains isotropic
   for a different, already-established reason (homogeneity itself).
3. Whether this anisotropy, once its metric effect is solved for, would
   be large enough to matter observationally — no comparison to any
   bound performed.
4. Anything about the `κ` (dipole) sector.
5. Any comparison against Table A1 — closed gate, not touched.
6. Per NO_AUTHOR_ERROR: entirely this project's own reconstruction
   (OUR_RECONSTRUCTION), not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P37_phi_stress_tensor_anisotropy_check.py
```
