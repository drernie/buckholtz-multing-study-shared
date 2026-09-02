# FINDING P188 — Accretion-term cross-check: `_v82_shared_physics.py` vs TJB's own `multing_core.py`

**Date:** 2026-09-02
**Status:** RESOLVED — MATCH, no re-derivation needed
**Triggered by:** an action item flagged in `data/source_material/
zenodo_21204955_supplemental/INDEX.md` (written same session, before this
check): "not yet cross-checked... if absent, the project's own v82-
degeneracy numerics were computed on an incomplete force law."

## Claim checked

Does this project's own shared physics kernel
(`experiments/20260803-bridge/_v82_shared_physics.py`, used identically
across `P177`-`P185`) implement the non-isotropic mass-accretion force
correction `F_accretion(z)` that TJB's own canonical `multing_core.py`
(now at `data/source_material/zenodo_21204955_supplemental/code/
multing_core.py`) implements — and if so, does it match?

## Method

Loaded both modules directly (not by inspection alone) and compared,
across 8 redshifts spanning the paper's own data range (z=0 to z=5,
including the SH0ES and DESI anchor points): `F_accretion(z)` itself,
the full `addot_over_a` output at the paper's spotlighted
(beta_1, beta_2) = (1.4335e10, 7.8067e17), and every shared numerical
constant (17 of them, including `f_merge`, `f_coh`, `M0_kg`, `d0_m`,
`T0_keV`, and the Planck cosmology parameters). Script:
`P188_accretion_term_crosscheck.py` in this directory.

## Result — [VERIFIED, exact numeric match]

```
max relative diff, F_accretion(z) across 8 redshifts:      0.000e+00
max relative diff, addot_over_a(z) across 8 redshifts:      0.000e+00
constants (17/17):                                          all OK
VERDICT: MATCH -- accretion term present and numerically identical
```

Both `F_accretion` implementations are algebraically the same function
under different internal naming (`_v82_shared_physics.py` inlines
`f_coh * f_merge * v_infall(z)`; `multing_core.py` names that product
`dv_coh(z)` first) — confirmed identical to machine precision (0.0 exact,
not just "close"), not merely similar.

## Kill Analysis

- **Killed:** the concern that this project's own `P175`-`P187` v82-
  degeneracy numerics were computed on an incomplete force law (missing
  the accretion correction). They were not — `_v82_shared_physics.py`
  already had it, correctly, this whole time.
- **Not killed / unaffected:** nothing about the `P176` β1/β2 degeneracy
  finding itself, which was always computed with this same kernel — this
  check adds independent confirmation the kernel is correct, it does not
  change any prior numeric result.

## Correction to prior record

`data/source_material/zenodo_21204955_supplemental/INDEX.md`'s "Action
item, not yet done this session" note (fact #1 in that file's "Key facts
extracted" section) and the corresponding `pearl_registry/INDEX.md`
2026-09-02 row both stated this as an open question — that was an
unverified assumption at write time, now resolved. Both updated to point
here rather than re-stating the open flag.
