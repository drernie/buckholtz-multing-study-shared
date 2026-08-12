# P16 — the divergent/vanishing three-regime structure of P15 replicates on a Fibonacci-sphere lattice; the "realistic regime" comparison is weaker than first framed

~~P15's self-vs-cross result transfers to the actual 2D spherical shell,
with one honest dimensional wrinkle~~ **[CORRECTED after skeptic review —
retitled]**

**Date:** 2026-08-12 · corrected 2026-08-12 after context-blind skeptic
review · originally set out to answer the gap `FINDING_P15`'s own
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

**[CORRECTED after skeptic review — read before the rest of this file]**
A context-blind skeptic review (Step 8a) confirmed all the math
(CONFIRMED-REAL) but WEAKENED the central interpretive claim: **the
self-energy formula `self_total = N·(8π/3)p²/r_min³` has zero geometric
dependence** — confirmed by re-reading the code, it takes only `N`, `p`,
`r_min`, never a position or radius. So "Regime B' self dominates
identically on the ring and the sphere" is guaranteed the moment `p_i`
and `r_min` are fixed to the same numbers in both — it is not a
demonstration that anything transferred geometrically. Only the
cross-term ratio (which differs by a small, expected coordination-number
factor between the two geometries) carries actual geometric content.
Retitled and §"Bottom line" rewritten below; original reasoning kept
struck through rather than silently removed.

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

**[CORRECTED after skeptic review]** The `self=...` values are IDENTICAL
between P15's ring and this sphere at matched `N` — not approximately,
exactly, because `self_total` is computed from `N`, `p`, `r_min` alone
(see code: `self_total = n * float(e_self(p_strength, r_min_val))`, no
position or radius argument). Fixing `p_i` and `r_min` to the same numbers
in both geometries GUARANTEES identical self-energy; this is arithmetic,
not a geometric result. The only quantity that actually depends on the
geometry is the cross-term: `~4×10⁻⁵` on the ring vs `~1.4×10⁻⁴` here, a
factor of `~3.5` explained by coordination number (a ring has 2
effective nearest neighbors per element; a Fibonacci-sphere lattice has
roughly 6, close-packed-hexagonal-like) — a small, expected, and now
correctly attributed effect, not evidence of a large "transfer."

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

~~P15's central result... transfers cleanly to the actual P9-shell
geometry class... Regime B' reproduces the same qualitative outcome...
closing the specific gap the P15 skeptic review named.~~

**[CORRECTED after skeptic review]** What this finding actually
establishes, split by what is real geometric content and what is not:

- **Genuine transfer (Regimes A'/C'):** the *qualitative* three-regime
  structure — self-energy diverges when a finite `r_min` shrinks with `N`;
  vanishes when `r_min` is held fixed — does transfer from the ring to the
  sphere. This is real content: it did not have to come out this way, and
  the specific power law honestly differs (`√N` vs `N²`) for a stated,
  independently-checked geometric reason (nearest-neighbor spacing scales
  as `1/√N` on a sphere vs `1/N` on a ring).
- **Not a transfer test (Regime B'):** self-energy dominance in Regime B'
  is guaranteed by construction once `p_i` and `r_min` are fixed to
  identical values in both geometries — the self-energy formula has no
  geometric dependence at all. This regime is a **consistency check**,
  not evidence of geometric transfer. The only informative part of Regime
  B' is the coordination-number-driven `~3.5×` difference in the
  (subdominant) cross-term between ring and sphere, correctly explained
  above but previously mischaracterized as the headline "transfer"
  result.
- Net effect on `FINDING_P15` §5: P15's central physical claim
  (self-energy real and dominant for realistic discrete clusters) is
  **not strengthened by Regime B' specifically** — that comparison was
  never capable of testing it independently on the sphere. It IS
  supported by the genuine A'/C' transfer, which shows the underlying
  mechanism (divergent-vs-vanishing self-energy depending on regularization)
  is not an artifact of the ring's particular 1D structure.

## What this does NOT establish

1. **P9's own exterior-potential zero for a discrete shell.** This
   computed field *energy* (self+cross), not exterior *potential* — a
   discrete-shell analog of P9's own exact calculation (summing exterior
   potential contributions and checking they stay near zero as `N` grows)
   would be a distinct, complementary test, not attempted here.
2. **That Regime B' demonstrates geometric transfer.** [Added after
   skeptic review.] Self-energy dominance there is guaranteed by
   construction (the self-energy formula has no geometric dependence);
   only the small, coordination-number-driven cross-term difference
   carries actual geometric content.
3. **Precision beyond order-of-magnitude.** The Fibonacci-lattice spacing
   estimate (`nn_spacing_estimate`) is an average, not an exact
   nearest-neighbor computation (independently estimated by the skeptic
   at `~15%` above the true asymptotic minimum) — fine for the
   qualitative scaling-transfer question asked here, not for a precise
   magnitude.
4. **A resolution of `κ`'s unfixed absolute scale** (`FINDING_P14`'s
   separate, still-open finding) — unaffected by this result either way.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic verdict (Step 8a, context-blind — claim + code + cited files only)

Two separate verdicts, not merged:

**(1) Math/numerical content: CONFIRMED-REAL.** Independently re-derived
the `1/√N` sphere nearest-neighbor spacing scaling, the resulting `√N`
self-energy power law for Regime A' (confirmed algebraically exact — the
skeptic notes the printed "8.0002" for a 64× increase in `N` is a
print-precision artifact of an analytically exact `8`, if anything
understating the result's cleanliness), the `1/N` Regime C' falloff, and
the Regime B' order-of-magnitude cross/self ratio. No formula-validity
concerns found (Regime A' stays in the far-field regime at fixed
`nn_spacing/r_min≈125` throughout, confirmed algebraically even though
the script does not print this diagnostic for Regime A' the way it does
for Regime C' — a documentation gap, not a physics error, now noted here).

**(2) Interpretive claim ("confirms transfer," original title): WEAKENED.**
The A'/C' qualitative-structure transfer is real and correctly
attributed. The Regime B' comparison, and by extension the original
title's headline claim, oversold what fixing `p_i` and `r_min` to
identical geometry-independent values in both setups can actually show.
Applied per Response Matrix: title corrected (Fix), Regime B' reframed as
a consistency check rather than transfer evidence (Fix), coordination-
number explanation for the cross-term difference retained and credited
to the skeptic (Fix), Regime A' documentation gap noted (Accept-with-doc).
No response fell to core-predicate-false — the A'/C' transfer result
survives untouched.

## Reproduction

```bash
python experiments/20260803-bridge/P16_2d_shell_transfer_check.py
```
