# P15 — self-energy survives for realistic, discrete clusters; the exact P9 zero does not literally transfer to this test geometry

**Date:** 2026-08-12 · corrected 2026-08-12 after context-blind skeptic
review · strongly supports (does not "resolve") the open tension
`FINDING_P14` §1 left unsettled: for a REALISTIC, discrete population of
finite-sized sources (real clusters), does self-energy survive as a
genuine, separate contribution, or does it cancel the way P9's exact
continuum calculation shows it must in the idealized, zero-core-size
shell limit?
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P15_discrete_vs_continuum_self_energy.py`, ruff clean. Two
textbook positive controls (collinear dipole-dipole attraction
`-2p₁p₂/d³`, perpendicular repulsion `+p₁p₂/d³`) pass before any new
result is trusted.

**[CORRECTED after skeptic review — read before the rest of this file]**
A context-blind skeptic review (Step 8a) found one real numerical error and
one significant framing overclaim in the original version. Both are fixed
below, with the original reasoning kept visible (struck through) rather
than silently edited:
1. **Numerical error:** §4 originally stated Regime B's cross/self ratio as
   `~10⁻⁹`. Independently re-verified by re-running the script: the actual
   ratio is `~4×10⁻⁵` — the `~10⁻⁹` figure was Regime A's ratio,
   misattributed to Regime B. Cross terms are still utterly subdominant in
   Regime B, just not by as many orders of magnitude as first claimed.
2. **Framing overclaim:** "Resolves" is too strong. The 1D ring used here
   does **not** itself satisfy P9's shell theorem (that is specifically a
   2D/3D symmetric-shell result), so no regime tested here literally
   reproduces or contradicts P9's cancellation — the ring can show whether
   self-energy is real in a discrete geometry, which is a related but
   weaker question. A third continuum limit (§3a, added after review) shows
   the self-vs-cross scaling genuinely depends on which quantity is held
   fixed as `N→∞`, which is the more defensible version of "different
   idealizations, not a real contradiction."

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

## 3. Regime A — a naive shrinking attempt, and what it actually showed

First attempt: shrink both dipole strength and physical size as `1/N`
(an intuitive guess at "approaching the continuum"). **This diverges**
(`self~N²`), not vanishes — checked directly, not assumed.

~~This is not a bug in the script; it is informative. ... This resolves
the "tension" the P14 skeptic review raised: it was never a real
conflict, only a category mismatch between two different mathematical
idealizations.~~

**[CORRECTED after skeptic review]** The skeptic pointed out something the
original text missed: **a 1D ring of radially-aligned dipoles never had
P9's exact-zero property to begin with.** P9's zero-exterior-field result
is a shell-theorem-type consequence of full 2D spherical symmetry; a 1D
ring carries no such theorem. So Regime A's divergence cannot literally
"reveal a mismatch with P9" — there was no P9-style cancellation present
in this geometry for it to be in tension with. What Regime A legitimately
shows is narrower but still real: shrinking a genuinely finite `r_min`
alongside `N` (rather than holding it fixed) drives self-energy to
diverge, i.e., naive "resolution → continuum" shrinking is not a safe way
to take this limit. See §3a for a cleaner test of the actual
idealization-dependence question.

## 3a. Regime C — the skeptic's alternative limit, added after review

The skeptic constructed, analytically, a second limit starting from the
*same* Regime A setup (`p_total` and ring radius both fixed, so the
surface dipole density `μ = p_total/circumference` is already constant
throughout Regime A) but holding `r_min` **fixed** — a genuine physical
core size — instead of shrinking it with `N`. Predicted: `self→0` as
`1/N`, `cross→` a finite limit — the opposite scaling from Regime A, from
an otherwise identical starting point.

Built directly into the script and run:

```
N=   8: self=+1.047198e+06  cross=+8.765563e-01  |total/self|=1.0000  (nn_spacing/r_min=78.5)
N=  32: self=+2.617994e+05  cross=+1.034669e+01  |total/self|=1.0000  (nn_spacing/r_min=19.6)
N= 128: self=+6.544985e+04  cross=+1.593820e+02  |total/self|=1.0024  (nn_spacing/r_min= 4.9)
N= 512: self=+1.636246e+04  cross=+2.541464e+03  |total/self|=1.1553  (nn_spacing/r_min= 1.2)
```

Matches the prediction: `self` falls by roughly `1/N` while `cross` grows
(from the same absolute values as Regime A, since `cross` does not depend
on `r_min`) until the two become comparable. At `N=512` the nearest-
neighbor spacing has shrunk to `1.2×r_min` — the point-dipole
approximation itself is starting to strain there, which the script now
prints explicitly rather than hiding.

**This is the more defensible version of the "different idealizations"
claim.** Regimes A and C start from the *same* dipole-density setup and
differ only in whether `r_min` shrinks with `N`; that single choice flips
self-energy from diverging to vanishing. So the self-vs-cross scaling
under `N→∞` genuinely depends on which quantity is held fixed —
confirmed with three distinct limits (A, B, C), not asserted from two.

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

~~Cross terms are `~10⁻⁹` of self-energy~~ **[CORRECTED after skeptic
review]: cross terms are `~4×10⁻⁵` of self-energy** (independently
re-verified: `cross/self = 6.55e-15/1.29e-10 ≈ 5×10⁻⁵` at `N=8`,
converging to `~3.6×10⁻⁵` by `N=128` — the `~10⁻⁹` originally stated here
was Regime A's ratio, misattributed to Regime B). Still utterly
subdominant, not approaching cancellation at any tested `N` — the
qualitative conclusion is unchanged, only the specific order of magnitude.
For this ring configuration, self-energy accounts for essentially the
entire total field energy (`99.996%`, not `99.9999999%`).

A scaling check (from the cross-term formula: `cross/self ≈ 0.29·(r_min/d)³`
for this geometry) shows the qualitative "self dominates" conclusion is
robust for any separation-to-size ratio `≥3:1`, not just the specific
`20:1` figure used here — at `5:1` the ratio would be `~2×10⁻³`, still
subdominant; only near contact-packing (`~1:1`) does cross become
comparable to self.

## 5. Bottom line

~~Resolves `FINDING_P14`'s open §1 tension~~ **[CORRECTED after skeptic
review] Strongly supports reading (a) of `FINDING_P14`'s §1, in a 1D
approximation, at physically-realistic separations — full resolution for
the 2D shell P9 actually computed remains future work.** For a realistic,
discrete, well-separated population of finite-size sources, self-energy
is the dominant channel in the field-energy sum (Regime B: `~4×10⁻⁵`
cross-to-self, robust down to `~5:1` separation ratios). Regimes A and C
together show this is not accidental: the same starting dipole-density
setup gives opposite self-vs-cross scaling depending only on whether
`r_min` shrinks with `N` — genuinely different idealizations, not one
calculation contradicting another.

What this finding does **not** show: that the 1D ring's behavior
transfers to the full 2D spherical shell P9 computed exactly (asserted as
plausible from the scaling argument, not demonstrated), or that P9's own
exact-zero geometry is itself implicated at all (the ring never had that
property to lose). **Reading (a) from `FINDING_P14`'s §1 is supported in
this narrower, 1D sense**: self-energy is a real, additive channel that a
realistic (not idealized) regularization exposes. P14's own conditional
bound (`κ≲10⁻⁶`, from `Ω_φ≲1`) is no longer conditional on the P9-vs-P14
tension specifically — the self-energy channel this finding traces is
real for the discrete case tested — though the bound's numeric value
still inherits every other caveat P14 already listed (r_min choice,
Ω_φ-vs-β mapping, `κ`'s own unfixed scale), plus this finding's own new
1D-to-2D transfer gap.

## What this does NOT establish

1. **That P9's own exact-zero geometry was tested at all.** The 1D ring
   used throughout does not satisfy P9's shell theorem regardless of
   regularization — no regime here literally reproduces or contradicts
   P9's specific cancellation. [Added after skeptic review.]
2. **A precise numeric self-energy magnitude for the true 2D shell.** This
   used a 1D ring approximation — the qualitative conclusion (self-energy
   survives, dominates over cross terms at realistic separations) is
   asserted to transfer to the full 2D case by scaling argument, not shown
   directly. The specific `|total/self|` numbers here are
   ring-geometry-specific, not directly comparable to P14's own `Ω_φ`
   figure.
3. **A resolution of `κ`'s unfixed absolute scale** (P14's separate,
   still-open finding) — that remains a distinct blocker for any absolute
   magnitude, including this channel's.
4. **That the self-energy channel is large enough to matter
   observationally.** Only that it is not cancelled — its actual
   cosmological significance still depends on `κ`'s value, unresolved.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic verdict (Step 8a, context-blind — claim + code + cited files only)

Two separate verdicts, not merged, per Falsification Ladder discipline:

**(1) Math/numerical content: WEAKENED.** Cross-term formula and both
textbook positive controls independently re-derived and confirmed exactly
(CONFIRMED-REAL). Regime A's `self~N²` divergence confirmed as a raw fact.
Regime B's specific `~10⁻⁹` magnitude claim was FALSIFIED — recomputed
directly from the code's own printed values as `~5×10⁻⁵` at `N=8`; this
correction is independently [VERIFIED-BASH] by re-running the script.

**(2) Interpretive claim ("resolves the tension"): WEAKENED.** The
underlying physical intuition — that a smooth double-layer's total field
energy is `∞ = ∞(cross) + finite(self)` rather than `0 = -x + x`, so P9's
exterior-zero and this self-energy channel are not strictly in conflict —
is defensible. But "resolves" overstated what a 1D-ring test (which never
had P9's cancellation property to test against) can show, and the
original text asserted a two-way idealization split (Regime A vs Regime
B) without noticing a third, physically-natural limit existed with yet a
different scaling. All Response Matrix items applied: the `~10⁻⁹` number
fixed (Fix), Regime C built and run to test the skeptic's alternative
limit directly (Fix), "resolves" downgraded to "strongly supports ... in
a 1D approximation" (Fix), the ring-vs-P9-geometry gap made explicit
(Accept-with-doc, new item 1 above). No response fell to "core predicate
false" — the central physical result (self-energy is real and dominant
for realistic discrete clusters) survives, corrected.

## Reproduction

```bash
python experiments/20260803-bridge/P15_discrete_vs_continuum_self_energy.py
```

The two textbook dipole-dipole positive-control asserts must pass before
the ring-sum results are trusted.
