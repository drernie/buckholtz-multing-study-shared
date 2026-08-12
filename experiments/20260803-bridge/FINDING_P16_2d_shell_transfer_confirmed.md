# P16 — P15's self-vs-cross result transfers to the actual 2D spherical shell, with one honest dimensional wrinkle

**Date:** 2026-08-12 · directly answers the gap `FINDING_P15`'s own
context-blind skeptic review flagged (point d/e) and P15's own "What this
does NOT establish" §1-2 named: P15 tested a 1D ring, which does **not**
itself satisfy `FINDING_dipole_shell_is_a_double_layer.md`'s (P9) shell
theorem — so whether P15's self-vs-cross scaling behavior actually
transfers to the real 2D spherical-shell geometry P9 computed was
asserted there, not shown.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P16_2d_shell_transfer_check.py`, ruff clean. Reuses P15's own
verified self-energy formula (`(8π/3)p²/r_min³`, from `FINDING_P14`) and
dipole-dipole cross-term formula (already general in 3D — only P15's
position generator was ring-specific) unchanged; only the geometry
(points-on-a-sphere instead of a ring) is new.

## Scope limit, stated up front

This tests whether the **self-vs-cross field-energy scaling** found on
the ring transfers to a real spherical-shell distribution. It does **not**
re-verify P9's own exterior-potential zero for a discrete (finite-`N`)
shell — that is a different calculation (summing exterior *potential*
contributions, not field *energy*) and is not attempted here. Per
NO_AUTHOR_ERROR: entirely about this project's own reconstruction.

## Method

`N` points distributed quasi-uniformly on a sphere via a Fibonacci lattice
(a standard, well-known sphere-sampling technique, not a novel method),
each carrying a radially-aligned dipole — matching P9's own configuration
and the one `two_charge_completion.py`'s derivation selects. Same three
regimes as P15, re-run on the sphere:

- **Regime A'** — naive shrink: `p_i=p_total/N` (total dipole moment
  conserved, as in P15's Regime A). `r_min_i` tied to the sphere's own
  natural nearest-neighbor spacing decrease, which scales as `~1/√N` (NOT
  `~1/N` as on a ring — a genuine geometric difference, handled explicitly
  rather than reusing the ring's tie blindly).
- **Regime C'** — `r_min` held **fixed** (a genuine physical core size),
  same `p_i` shrink. Sphere analog of P15's Regime C.
- **Regime B'** — realistic: `p_i` and `r_min` **fixed** at real cluster
  values (identical numbers to P15's Regime B: `k/mc²=1.7×10⁻⁶`, cluster
  radius `1.5 Mpc`), sphere radius grown with `N` to hold the
  separation-to-size ratio fixed at `20:1`.

## Results

```
Regime A' (r_min ~ 1/sqrt(N), tied to natural spacing decrease):
  N=  8: self=1.047198e+06   N= 32: self=2.094395e+06
  N=128: self=4.188790e+06   N=512: self=8.377580e+06
  -> self grows as sqrt(N) EXACTLY (ratio 8.0002 for a 64x increase in N,
     sqrt(64)=8) -- diverges as N->infinity, confirming the qualitative
     "shrinking r_min with N diverges" pattern, but with a DIFFERENT power
     law than the ring's N^2 (see "One honest wrinkle" below).

Regime C' (r_min FIXED):
  N=  8: self=1.047198e+06   N= 32: self=2.617994e+05
  N=128: self=6.544985e+04   N=512: self=1.636246e+04
  -> self falls as 1/N (matches theory exactly: self_i~p_i^2/r_min^3~1/N^2,
     summed over N elements ~1/N), confirming the OPPOSITE scaling from
     Regime A' -- transfers cleanly, same as on the ring.

Regime B' (realistic, fixed 20:1 separation-to-size):
  N=  8: cross/self=1.384e-04   N= 32: cross/self=1.377e-04
  N= 64: cross/self=1.366e-04   N=128: cross/self=1.359e-04
  |total/self| = 1.0001 at every tested N.
```

## One honest wrinkle: Regime A' diverges as `√N`, not `N²`

The ring's self-energy diverged as `N²` because a ring's nearest-neighbor
spacing shrinks as `1/N` exactly (circumference/N). A sphere's spacing
shrinks as `1/√N` (area/N, then square-rooted) — a real geometric fact,
not a modeling choice. Tying `r_min_i` to the sphere's own natural spacing
(rather than blindly reusing the ring's `1/N` rule) gives
`self_i ~ p_i²/r_min_i³ ~ N⁻²·N^1.5 = N^{-0.5}`, so `self_total = N·N^{-0.5}
= N^{0.5}` — still divergent, but at a much slower rate. **The qualitative
conclusion (naive shrinking of a finite `r_min` alongside `N` diverges,
does not vanish) transfers; the specific power law does not, and
correctly should not** — it is a real consequence of dimensionality, not
an error to paper over.

## Bottom line

**P15's central result — self-energy is real, additive, and dominant for
a realistic, discrete, well-separated population — transfers cleanly to
the actual P9-shell geometry class.** Regime B' reproduces the same
qualitative outcome as P15's Regime B (cross utterly subdominant,
`~1.4×10⁻⁴` here vs. P15's `~4×10⁻⁵` on the ring — same order of
magnitude, geometry-specific numeric value as expected, not identical).
Regimes A' and C' also transfer qualitatively (diverge when `r_min`
shrinks with `N`; vanish when `r_min` is held fixed), closing the specific
gap the P15 skeptic review named. This directly strengthens `FINDING_P15`
§5's "strongly supports reading (a)" language toward something closer to
"transfers to the actual shell geometry" — though see "What this does NOT
establish" below for what is still not shown.

## What this does NOT establish

1. **P9's own exterior-potential zero for a discrete shell.** This
   computed field *energy* (self+cross), not exterior *potential* — a
   discrete-shell analog of P9's own exact calculation (summing exterior
   potential contributions and checking they stay near zero as `N` grows)
   would be a distinct, complementary test, not attempted here.
2. **Precision beyond order-of-magnitude.** The Fibonacci-lattice spacing
   estimate (`nn_spacing_estimate`) is an average, not an exact
   nearest-neighbor computation — fine for the qualitative
   scaling-transfer question asked here, not for a precise magnitude.
3. **A resolution of `κ`'s unfixed absolute scale** (`FINDING_P14`'s
   separate, still-open finding) — unaffected by this result either way.
4. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P16_2d_shell_transfer_check.py
```
