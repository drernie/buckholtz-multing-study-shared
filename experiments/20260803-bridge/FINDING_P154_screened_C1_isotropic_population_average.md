# FINDING P154 — the screened-kernel C1 analog: isotropic population average
# vanishes at the physically relevant scale, independently confirming P153

**Date:** 2026-08-28
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 math
(independent verification of `P153`'s central claim, via a genuinely
different method, per `research-methodology.md`'s Independent Verification
Strength Ladder — "independently-written code" tier, not a rerun of the
same formula)
**Verdict:** `SCREENED-ISOTROPIC-WASHOUT-CONFIRMED-AT-FINITE-R`
**Origin:** dispatched directly in response to a context-asymmetric skeptic
review of `FINDING_P153`, which found P153's central `G_eff`-based
argument has an unresolved order-of-limits problem for a screened kernel
specifically: `G_eff`'s `r→∞` real-space limit is trivially zero for
*any* screened correction (the tail past `r~1/μ` is killed by
construction), so `G_eff=0` may not be informative about whether the
correction has a genuine, finite, background-relevant contribution. The
skeptic's own Fourier-space check (`FT[exp(−μr)/r] = 1/(k²+μ²)`, finite
and nonzero as `k→0`) suggested a Yukawa correction *does* have nonzero
long-wavelength content, and proposed the cheapest differentiating test:
rerun `docs/127`'s own **C1** methodology (isotropic-orientation
population average at *finite* `r`, not an `r→∞` limit) with a
Yukawa-screened kernel, at the physically relevant scale (`r~few/μ`).
**Script:** `P154_screened_C1_isotropic_population_average.py` (symbolic
sympy derivation of the screened dipole force, 3 positive controls before
any new numeric result is trusted, ruff clean, does not touch the
881-test suite; runtime ~1 min)

## 1. Method — reuse `docs/127`'s own C1 code, screened kernel

`scripts/c1_anisotropic_dipole_nbody.py` (`docs/127`, 2026-07-22)
established, for the massless dipole force `F_dip ∝ [p−3(p·r̂)r̂]/r³`,
summed over a filled ball of isotropically-oriented objects: the
ensemble-mean tidal coefficient is consistent with zero
(`⟨n̂⟩=0` washout), while a coherent (non-isotropic) *aligned* control
gives a definite nonzero tidal — proving the test *can* detect a real
signal, not merely that it's too weak to see anything.

`P154` derives the Yukawa-screened dipole **force** symbolically (sympy),
starting from `Φ = −p·∇[exp(−μr)/r]` (independently re-derived, not
copied from `P11`, which only needed the *potential*):

```
Φ_dipole(r; p, μ) = (p·r)·(μr²+r)·exp(−μr)/r⁵
```

**Positive control 1:** `μ=0` limit exactly matches `p·r/r³` — passed.
**Positive control 2:** the `μ=0` force must exactly match
`c1_anisotropic_dipole_nbody.py`'s own declared `[p−3(p·r̂)r̂]/r³` form —
**failed on the first attempt** (self-caught, before dispatching anything
further): the textbook electric-dipole-field sign is `E=−∇Φ`, but `C1`'s
own docstring declares `F_dip∝[p−3(p·r̂)r̂]/r³`, which is the *opposite*
overall sign from `−∇Φ`. This is a labelling/convention choice in the
already-established, already-skeptic-reviewed `C1` code — an overall
sign flip changes neither "is the isotropic mean zero" nor "is the
aligned control nonzero" — not a physics bug, but the positive control
correctly caught the mismatch before trusting anything downstream. Fixed
by matching `C1`'s own convention (`F=+∇Φ`); positive control 2 then
passes exactly (symbolic difference `[0,0,0]`).

## 2. Result

At `μ=1` (working in units of `1/μ`, so the ball's extent directly
represents "how many screening lengths"), ball `[0.5,5.0]/μ`:

```
ALIGNED (non-isotropic control) : -1.03e+01   (definite)
RANDOM  ensemble mean (N=4000)  : +2.45e-01 ± 6.99e-01 (SEM)   z=+0.35σ
```

**Scale-robustness scan** (positive control 3's own concern: is this
special to `R_MAX=5`?), `R_MAX ∈ {1,2,5,10,20}/μ`, reduced `N=800` per
scale for speed:

| `R_MAX` (in `1/μ`) | aligned (definite) | isotropic mean ± SEM | z-score |
|---|---|---|---|
| 1  | `+4.35e+03` | `−7.57e+02 ± 1.09e+03` | `−0.69σ` |
| 2  | `−1.49e+03` | `−2.78e+01 ± 6.13e+01` | `−0.45σ` |
| 5  | `−1.63e+00` | `−1.55e+00 ± 1.92e+00` | `−0.81σ` |
| 10 | `+3.47e+00` | `+8.51e-02 ± 7.15e-02` | `+1.19σ` |
| 20 | `+5.01e-02` | `+9.14e-03 ± 3.60e-03` | `+2.54σ` |

All five scales: isotropic mean consistent with zero (`|z|<3`), aligned
control definite and nonzero at every scale — the washout is **not**
special to one arbitrarily chosen ball extent.

## 3. What this establishes about the skeptic's order-of-limits concern

The isotropic-orientation ensemble mean vanishes **at the physically
relevant, finite scale** (`r~few/μ`, not `r→∞`) — for the **same reason**
it vanishes in `C1`'s own massless case: orientation cancellation
(`⟨n̂⟩=0`), independently confirmed here for the screened kernel by a
genuinely different method (a real-space, finite-`r` N-body population
average) than `P153`'s `G_eff` real-space `r→∞` asymptotic limit. This
directly answers the skeptic's Fourier-space concern: whatever nonzero
long-wavelength content the Yukawa kernel carries in isolation
(`1/(k²+μ²)` at `k→0`, per the skeptic's own check), it does **not**
survive isotropic averaging over a realistic population of randomly
oriented dipole sources — the vector/orientation washout mechanism
(`C1`'s own mechanism, independent of `G_eff`'s radial-asymptotic
mechanism) applies to the screened case exactly as it did to the
massless one. `P153`'s `W_bg=∅` conclusion is **independently
confirmed**, not merely re-asserted via the same formula.

## 4. Correction (third context-asymmetric skeptic review, same day) —
two gaps closed: the quadrupole tier, and the scan's own weakest point

A third skeptic review of `FINDING_P153`+this file (context-blind, no
session history) found the argument above was **dipole-only**: the
`⟨n̂⟩=0` mechanism `C1`/`P154` test is specific to a rank-1 (vector)
structure. A genuine single-body rank-2 quadrupole tensor `Q_ij∝n_in_j`
does **not** wash out under isotropic averaging (`⟨n_in_j⟩=δ_ij/3≠0`) —
a real, different mechanism the file had not addressed for MULTING's
"quadrupole" tier, which `FINDING_P153`'s own §2 had (incorrectly, by
omission) treated as covered by the same dipole-only confirmation.
Separately, the scan's own largest z-score (`R_MAX=20`, `z=2.54σ` at
reduced `N=800`) was flagged as worth firming up before calling the scan
fully robust.

**Both closed, not by new assumptions but by this project's own already-
established structural fact:** `two_charge_completion.py`'s own header
(2026-08-10, predates this session) states explicitly that MULTING's
"quadrupole" tier is **not** a single-body rank-2 tensor at all — it is
`k_A·k_P`, the product of **two different bodies'** own dipole charges
("a genuine quadrupole moment of one body cannot produce
`|r_qAB|²=β_q²r_Ar_P`; a product of two bodies' DIPOLE moments does,
automatically"). The vector generalization of this cross term is
`q_A·q_P·(n̂_A·n̂_P)` — a product of **two different, independently
oriented** unit vectors, not a self-tensor. For two independent isotropic
random unit vectors, `E[n̂_A·n̂_P]=0` by elementary symmetry (the mean of
either factor alone is zero; independence factors the expectation) — a
**different, simpler** mechanism than the dipole's own force-level
N-body washout, verified numerically here (`P154` §Step 3, not merely
asserted): `E[n̂_A·n̂_P]` over `N=200000` independent pairs `=
−0.00007±0.00129` (`z=−0.05σ`) — consistent with zero.

`R_MAX=20` was rerun at the headline `N_REAL=4000` (§Step 2c): `z`
tightens from `2.54σ`→`1.96σ` — moving *toward* zero with more
statistics, as expected for a genuinely null result (a real nonzero mean
would instead have grown toward `~5.7σ`), closing that concern too.

**Updated verdict:** `SCREENED-ISOTROPIC-WASHOUT-CONFIRMED-AT-FINITE-R`
now covers **both** MULTING tiers — the dipole, by the same force-level
N-body mechanism as `docs/127`'s own `C1`, and the quadrupole, by a
distinct, simpler cross-independence argument specific to its own
established two-body-product structure, not a generic self-quadrupole
this project never claimed to have.

## What this file does NOT establish

1. **Not a claim about MULTING's own theory** (`NO_AUTHOR_ERROR`) —
   entirely this project's own reconstruction.
2. **Does not touch P11's own, different, still-open finding** (a
   *single finite shell's* near-field exterior potential, nonzero) — that
   remains a real, separate, local/structure-formation lead, per
   `FINDING_P153` §4.2, untouched by this file.
3. **Does not prove the washout for every conceivable population
   geometry** — this reuses `C1`'s own filled-ball, uniform-density
   ansatz; a population with genuine spatial-orientation correlations
   (which `docs/127`'s own `C1` finding already flagged as the *only*
   way to source a nonzero background — "the ONLY way to source the
   background is a globally coherent dipole alignment... independently
   excluded by CMB isotropy") is not re-examined here, and was already
   excluded on physical (CMB isotropy) grounds by `docs/127` itself. This
   applies to §4's quadrupole cross-independence argument too — it
   assumes `n̂_A` and `n̂_P` are genuinely independent (no cosmological
   correlation between different clusters' own internal axes); a
   correlated population is a different, unaddressed scenario.
4. **The dipole scale-robustness scan's non-headline points still use
   reduced statistics** (`N_REAL_SCAN=800` for `R_MAX∈{1,2,5,10}`; only
   `R_MAX=20`, the largest z-score, was reconfirmed at full `N=4000`,
   per §4).
5. **[Closed 2026-08-28, `P155`]** The quadrupole check (§4) originally
   verified only the elementary `E[n̂_A·n̂_P]=0` claim — a full
   force-level N-body sum was subsequently built and run
   (`P155_quadrupole_forcelevel_nbody.py`), skeptic-reviewed. Its own
   result: numerically consistent with the elementary claim here, but
   (per `P155`'s own §0 correction) analytically *reducible* to it via
   linearity, not a mechanistically independent second confirmation —
   see `FINDING_P155` for the full, correctly-scoped result.
