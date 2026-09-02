# CLAIM — P158 addendum 2: real halo mass function + bias/correlation
# derivation, replacing the REJECTED proxy attempt

**Date:** 2026-09-02
**Trigger:** user go-ahead ("давай это" on the outstanding-debts list, item
3: real bottleneck-1 derivation). Follows `FINDING_P158_ADDENDUM_
literature_grounding.md`'s REJECT — its own skeptic pass named exactly
what a real answer requires: "a `Var[log M_true]` computed from an
actual halo/cluster mass function... integrated over an explicitly
stated population definition" and "either a direct measurement of
pairwise mass covariance for close/interacting halo pairs from N-body
simulation literature... or an explicit acknowledgment that ρ should be
treated as a free sensitivity parameter."
**Scope:** this attempt uses real, peer-reviewed-grade tooling
(`hmf` — Murray, Power & Robotham 2013, the standard Python halo-mass-
function package, backed by `camb` for the linear matter power
spectrum) instead of a from-scratch implementation of Tinker et al.'s
fitting functions, to reduce implementation-error risk. `hmf` computes
`dn/dlnM(M,z)` directly using the Tinker et al. (2008) fitting function;
Tinker et al. (2010)'s bias formula (their Eq. 6) is implemented on top
of `hmf`'s own `ν=δc/σ(M)` output — a single closed-form formula with
published coefficients, not a re-fit.
**L0:** descriptive — computing two population statistics (a variance,
a pairwise correlation) from published, cited mass-function/bias
formulas is not a new causal or physics claim about MULTING/v82.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR

---

## What is being computed, precisely (avoiding the prior category errors)

**(a) `Var[ln M]`** for an EXPLICITLY STATED population: halos with
`M ≥ M0/2` at v82's own target redshifts (`z = 0.07, 0.5, 1.07, 1.965`,
v82's own Table III values), where `M0` is v82's own archive value
(`multing_core.py::M0_kg`, ≈6.0×10¹⁴ M_☉ — matches the "~5-6×10¹⁴ M_☉"
range this session has cited from `FINDING_P155`'s context). **Population
definition stated explicitly, not left implicit**, per the prior REJECT's
own naming of this as the missing piece. A mass FLOOR (not a narrow bin)
is chosen because it is the standard selection convention in cluster
cosmology (mass-limited samples), and because v82 itself gives no basis
to prefer a narrower definition (`FINDING_P157` §2 — v82 never defines
its own node population precisely).

**(b) `ρ = Cov[ln M₁, ln M₂] / Var[ln M]`** for two halos separated by
v82's own node-pair distance (`d_of(z)`, ≈40-45 Mpc across v82's own
z-range), derived from the STANDARD peak-background-split formalism for
this exact separation regime (NOT the close/merging-pair regime the
prior skeptic pass correctly flagged as a different, inapplicable
object): `ξ_hh(r; M₁,M₂) = b(M₁)b(M₂)ξ_mm(r)`, giving
`Cov[ln M₁, ln M₂] ∝ ⟨b(M)⟩² · ξ_mm(r)` for the same population as (a).
**Why this regime is the right one, stated explicitly (the prior
attempt's error was using this formalism without checking the regime):**
v82's own node separation (~40-45 Mpc) is well outside the 1-halo/
close-pair regime the prior skeptic objection was about (sub-Mpc to a
few Mpc) — it sits in the quasi-linear, 2-halo-term regime where
`ξ_hh = b₁b₂ξ_mm` is the standard, appropriate tool, not a conflation.

## Falsifiable claims under test

1. `Var[ln M]` for the stated population, at each of v82's 4 redshifts,
   computed from `hmf`'s Tinker08 mass function — a real number, not an
   illustrative range.
2. `ξ_mm(r≈40-45 Mpc)` from the linear matter power spectrum (`hmf`/
   `camb`) — expected to be small in magnitude near this separation,
   since ~40-50 Mpc/h is close to the standard ΛCDM linear correlation
   function's zero-crossing (a well-known feature, not unique to this
   calculation) — falsifiable: if `hmf`'s own power spectrum gives a
   value inconsistent with this well-known shape (e.g. order-unity at
   this scale), that is a red flag requiring investigation before
   trusting anything downstream.
3. `b(M,z)` via Tinker et al. (2010) Eq. 6, evaluated at `M=M0(z)`.
4. Combined `ρ(r=d_of(z), z)` for each of v82's 4 redshifts.

## Positive controls

- **`hmf`'s mass function**, already checked before writing this claim:
  `n(M>10¹⁴ M_☉/h, z=0) = 2.15×10⁻⁵ (Mpc/h)⁻³` — matches the standard,
  commonly-cited cluster-abundance ballpark (order `few×10⁻⁵`) for this
  threshold in a flat ΛCDM cosmology; `n(M>10¹⁵ M_☉/h, z=0) = 9.4×10⁻⁸
  (Mpc/h)⁻³`, consistent with very massive clusters (Coma-like) being
  genuinely rare at the ~1-per-(100 Mpc/h)³ scale. Both `[VERIFIED-BASH]`.
- **Tinker10 bias formula**: `b(ν)→1` as `ν→` the value corresponding to
  `M*` (the characteristic nonlinear mass, where `ν=1` by definition) —
  checked as a hard assert before trusting any other `b(M)` value.
- **`ξ_mm(r)` shape**: monotonically declining from `ξ_mm(5 Mpc/h)≈1`
  (order-unity at small scale, the well-known normalization scale) to
  near-zero around `r~30-50 Mpc/h`, with the known BAO feature near
  `r~100-110 Mpc/h` — checked qualitatively against this well-documented
  shape before trusting the specific value at `r=40-45 Mpc`.

## Negative control

Evaluate `b(M,z)` at a deliberately much smaller mass (`M=10¹² M_☉`,
well below the cluster range) and confirm it gives `b<1` (galaxy-scale
halos are known to be ANTI-biased relative to `ν=1`, or at most weakly
biased) — confirms the formula responds correctly to mass, not a
constant regardless of input.

## What this does NOT establish

1. Not a claim that v82's own "node" population is exactly "halos with
   `M≥M0/2`" — an explicit, stated, defensible choice, not v82's own
   stated definition (which does not exist, per `FINDING_P157`).
2. Not a re-derivation of Tinker et al.'s own fitting functions — reused
   via the `hmf` package, a real, independently-published, widely-used
   tool, not re-fit here.
3. Not an answer to `docs/153`'s 3 pre-conditions outright — a real,
   quantitative input to pre-condition 3's cost/consequence question,
   at the specific level of rigor this session's own skeptic pass named
   as necessary.
4. `NO_AUTHOR_ERROR` — does not say v82's own representative-value
   choice is right or wrong.

## Artifacts

- This file.
- `FINDING_P158_ADDENDUM2_real_mass_function.md` — the write-up.
- `P158_addendum2_real_mass_function.py` — the computation.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
