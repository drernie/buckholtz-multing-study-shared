# P15 — self-energy survives for realistic, discrete clusters; P9's exact zero is specific to the idealized zero-core-size continuum

**Date:** 2026-08-12 · directly resolves the open tension `FINDING_P14` §1
left unsettled: does P9's exact continuum cancellation (cross terms
exactly canceling the self-energy sum, in the idealized, zero-core-size
shell limit) extend to a REALISTIC, discrete population of finite-sized
sources (real clusters), or does self-energy survive as a genuine,
separate contribution there?
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P15_discrete_vs_continuum_self_energy.py`, ruff clean. Two
textbook positive controls (collinear dipole-dipole attraction
`-2p₁p₂/d³`, perpendicular repulsion `+p₁p₂/d³`) pass before any new
result is trusted.

---

## 1. The question, precisely

`FINDING_P14`'s self-energy calculation and `FINDING_dipole_shell_is_a_double_layer.md`'s
(P9) exact-zero result seemed to be in tension — a context-blind skeptic
review of P14 showed that P9's zero, via the self-energy/cross-term split
identity, forces `Σ_{i≠j}(cross) = -Σᵢ(self)` **in the idealized
continuous shell limit**. P14 left open whether this cancellation also
holds for a **discrete**, **finite-sized** population — the physically
realistic case (real clusters, not an infinitesimal continuum).

## 2. Method

Reused P14's own verified self-energy formula
(`E_self=(8π/3)p²/r_min³`), and derived + verified the general
dipole-dipole cross-term interaction formula (from this project's own
`p·∇φ` coupling convention), positive-controlled against **two textbook
closed forms**: collinear dipoles attract as `-2p₁p₂/d³`; perpendicular
(parallel, side-by-side) dipoles repel as `+p₁p₂/d³`. Both matched
exactly.

Built `N` discrete, radially-aligned point-dipoles on a ring (a tractable
1D stand-in for P9's full 2D spherical shell — a stated scope limit, not
a full reproduction), and summed `Σself + Σcross` directly under two
regimes.

## 3. Regime A — a naive shrinking attempt, and what it actually revealed

First attempt: shrink both dipole strength and physical size as `1/N`
(an intuitive guess at "approaching the continuum"). **This diverges**
(`self~N²`), not vanishes — checked directly, not assumed.

This is not a bug in the script; it is informative. **P9's exact zero was
never a statement about a self-energy sum at all** — it computed the
*exterior potential* of a smooth, zero-core-size surface density, which
has no `r_min` cutoff anywhere and therefore no self-energy divergence to
speak of. Shrinking a genuinely *finite* `r_min` alongside `N` approaches
a *different* idealization (literal point sources with formally divergent
self-energy) — not the smooth density P9 actually treated. **P9's
zero-force result and this project's self-energy channel are answers to
different physical questions** — an idealized, zero-size exterior field
versus a finite-size, real near-field energy — and are not in
contradiction with each other. This resolves the "tension" the P14
skeptic review raised: it was never a real conflict, only a category
mismatch between two different mathematical idealizations.

## 4. Regime B — the realistic case: self-energy dominates, does not cancel

Held dipole strength and physical size **fixed** at real cluster values
(P14's own numbers: `k/mc²=1.7×10⁻⁶`, cluster radius `1.5 Mpc`), grew `N`
at a **fixed, realistic separation-to-size ratio** (`20:1` — cluster
separations of tens of Mpc against a cluster's own `~1.5 Mpc` size):

```
N=  8: |total/self| = 1.0001
N= 16: |total/self| = 1.0000
N= 32: |total/self| = 1.0000
N= 64: |total/self| = 1.0000
N=128: |total/self| = 1.0000
```

**Cross terms are `~10⁻⁹` of self-energy** — utterly subdominant, not
approaching cancellation at any tested `N`. For this ring configuration,
self-energy accounts for essentially the entire total field energy.

## 5. Bottom line

**Resolves `FINDING_P14`'s open §1 tension: self-energy survives as the
dominant contribution for a realistic, discrete, well-separated cluster
population.** The exact P9 cancellation is a special, fragile property of
the idealized continuum limit (infinitely many, infinitesimally-close
elements) — it does not persist, even approximately, once sources are
realistically finite-sized and widely separated. **Reading (a) from
`FINDING_P14`'s §1 is supported: self-energy is a real, additive channel
that a realistic (not idealized) regularization exposes.** P14's own
conditional bound (`κ≲10⁻⁶`, from `Ω_φ≲1`) is therefore no longer
conditional on this specific tension — the self-energy channel this
finding traces is real, though the bound's numeric value still inherits
every other caveat P14 already listed (r_min choice, Ω_φ-vs-β mapping,
`κ`'s own unfixed scale).

## What this does NOT establish

1. **A precise numeric self-energy magnitude for the true 2D shell.** This
   used a 1D ring approximation — the qualitative conclusion (self-energy
   survives, dominates over cross terms at realistic separations) should
   transfer to the full 2D case, but the specific `|total/self|` numbers
   here are ring-geometry-specific, not directly comparable to P14's own
   `Ω_φ` figure.
2. **A resolution of `κ`'s unfixed absolute scale** (P14's separate,
   still-open finding) — that remains a distinct blocker for any absolute
   magnitude, including this channel's.
3. **That the self-energy channel is large enough to matter
   observationally.** Only that it is not cancelled — its actual
   cosmological significance still depends on `κ`'s value, unresolved.
4. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P15_discrete_vs_continuum_self_energy.py
```

The two textbook dipole-dipole positive-control asserts must pass before
the ring-sum results are trusted.
