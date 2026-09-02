# FINDING P158 — Addendum 2: real halo mass function + Tinker10 bias +
# matter correlation function — WEAKENED after Step 8a skeptic pass

**Date:** 2026-09-02
**Trigger:** user go-ahead ("довести до честного вердикта сейчас") after
a real bug was caught mid-computation (ρ values violating the `|ρ|≤1`
bound), fixed, and then a Step 8a skeptic pass found two FURTHER real
problems, both independently re-verified before accepting.
**Status:** WEAKENED (Skeptic Response Matrix). A materially narrower,
more caveated positive result survives than the pre-skeptic draft
claimed — real, computed, controlled, but covering only about half of
v82's own target redshift range, not all of it.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR

---

## What this is, and how it differs from the REJECTED first attempt

`FINDING_P158_ADDENDUM_literature_grounding.md` was REJECTED because it
used a real but WRONG-QUANTITY citation. This addendum instead
**computes** `σ_lnm` and `ρ` from first principles using real,
peer-reviewed, independently-published tools (`hmf` — Murray, Power &
Robotham 2013, backed by `camb` — for the Tinker et al. 2008 mass
function; Tinker et al. 2010 Eq. 6, coefficients verified directly
against the primary source this session, for halo bias; a direct
Fourier-Bessel integral of `hmf`'s own linear power spectrum for
`ξ_mm(r)`).

## Three real bugs caught before/during writing this up — two by this
## session, one by a dispatched skeptic, all independently re-verified

1. **Wrong covariance formula** (`⟨b⟩²` instead of `Cov[lnM,b]²`) —
   caught by hand re-derivation, before any number was computed.
2. **Fixed z=0 mass floor across all redshifts** — produced `ρ` values
   in the tens of thousands, a hard violation of the `|ρ|≤1`
   Cauchy-Schwarz bound. Caught by the bound violation itself. Fixed by
   tracking v82's own z-evolving `M_of(z)/2`.
3. **First-order-in-`ξ` expansion diverges** at high bias — fixed by
   deriving the EXACT closed form,
   `Cov[lnM1,lnM2] = ξ_mm(r)·Cov[lnM,b]² / (1+⟨b⟩²ξ_mm(r))²`,
   verified by hand algebra (the `ξ²` cross-terms cancel exactly) before
   coding.

**A dispatched, context-blind Step 8a skeptic pass then found two
further, deeper problems in the (by-then internally self-consistent)
result — both independently re-verified directly, not taken on trust:**

### Problem 4 (skeptic Objection 1, confirmed and made precise) — the
### "exact" formula is exact only *within* a linearization pushed far
### past its own calibration

The skeptic's claim — "the test cannot fail, `ρ` is forced positive
regardless of physics" — was **partially an overclaim**: hand
re-derivation shows the saturating asymptotic form is
`ρ → Cov[lnM,b]² / (⟨b⟩⁴·ξ_mm(r)·Var[lnM])`, whose **sign tracks
`ξ_mm(r)`'s own sign**, not forced positive unconditionally. But the
skeptic's **practical conclusion holds**: in the saturating regime
(`⟨b⟩²ξ≫1`), `ρ` is driven toward **zero in magnitude regardless of the
real underlying physics** — meaning "`ρ>−0.5` satisfied" in that regime
is not meaningful evidence, it is what any linearized-bias calculation
does once pushed far enough past validity.

**Independently re-verified and found even more severe than the
skeptic's own estimate:** the skeptic guessed Tinker et al.'s
simulations "typically top out at `ν~10`, arguably `ν~20`." Direct
computation of `ν` at v82's own `M_of(z)/2` population floor, at each of
v82's 8 redshifts:

| z | 0.000 | 0.023 | 0.070 | 0.500 | 1.070 | 1.965 | 2.330 | 5.000 |
|---|---|---|---|---|---|---|---|---|
| ν | 5.39 | 5.46 | 5.55 | 7.31 | **10.64** | **17.40** | **20.50** | **49.97** |

`ν≈50` at `z=5` is not merely "past calibration" — it is a 50-sigma
fluctuation, astronomically beyond anything a real cosmic structure
could be, and beyond any fit ever tested against actual simulated
halos. **4 of v82's 8 own target redshifts (`z=1.07` and above) use
`ν` values the Tinker et al. (2010) fit was never validated against.**

### Problem 5 (skeptic Objection 3, confirmed) — a real units bug

`hmf`'s own power spectrum uses `Mpc/h` (its own `h=0.6766`); the
pre-skeptic draft passed v82's own separation `d(z)` (physical Mpc)
directly into the `ξ_mm(r)` integral without the `×h` conversion — a
genuine ~33% separation-scale error, independently confirmed by
computing `h` directly and comparing both conventions. Fixed.

**Objection 2 (population-floor sensitivity, no sweep run) is accepted
as a real, unaddressed limitation** — not run in this pass, given the
scope already expanded substantially; named explicitly below as
required before this result could be strengthened further.

## Result, after both fixes and the calibration-range check

Population: `M ≥ M_of(z)/2` (v82's own z-evolving characteristic mass,
an explicit, stated choice — not v82's own definition, which does not
exist per `FINDING_P157` §2).

| z | ν | ξ_mm(d) [Mpc/h] | ρ (exact) | status |
|---|---|---|---|---|
| 0.000 | 5.39 | 0.0547 | **+0.00451** | OK |
| 0.023 | 5.46 | 0.0220 | **+0.01007** | OK |
| 0.070 | 5.55 | 0.0378 | **+0.00526** | OK |
| 0.500 | 7.31 | 0.0567 | **+0.00084** | OK |
| 1.070 | 10.64 | 0.0494 | +0.00013 | EXTRAPOLATED |
| 1.965 | 17.40 | 0.0608 | +0.000006 | EXTRAPOLATED |
| 2.330 | 20.50 | 0.0614 | +0.000002 | EXTRAPOLATED |
| 5.000 | 49.97 | 0.0448 | +0.0000002 | EXTRAPOLATED |

**4 of 8 redshifts (`z=0` through `z=0.5`) give a `ρ` that is both
mathematically valid AND inside Tinker et al.'s own calibrated `ν`
range.** Every one of those 4 is small and positive
(`+0.0008` to `+0.010`), comfortably above `FINDING_P158`'s own
`ρ>−0.5` threshold. **The other 4 (`z≥1.07`) cannot be trusted from
this pipeline at all** — not because the arithmetic fails, but because
the input `ν` values are extrapolations the underlying fit was never
validated against.

## Skeptic Response Matrix

- **Objection 1** (saturation/no-power-to-fail) → **Accepted, with
  correction**: the mechanism is real, the specific claim ("forced
  positive") was an overclaim, corrected via independent re-derivation.
  Response: restricted the trusted result to the `ν`-in-calibration
  subset, where the saturation concern does not apply.
- **Objection 2** (no floor sensitivity sweep) → **Accepted as an open
  limitation**, not run this pass — named explicitly as required future
  work, not silently dropped.
- **Objection 3** (units mismatch) → **Accepted, confirmed, fixed** —
  independently verified via direct `h` computation before trusting.

## What this settles about `FINDING_P158`'s `CONDITIONAL-DIRECTIONAL-PREDICTION`

**Narrower than the pre-skeptic draft claimed.** For the lower portion
of v82's own redshift range (`z=0` to `z=0.5`, 4 of 8 tabulated points),
a real, computed, controlled `ρ` is small and positive, satisfying
`P158`'s `ρ>−0.5` threshold — the first genuinely computed (not
illustrative, not wrongly-proxied) grounding this session has achieved
for any part of `P158`'s conditionality. For the higher-`z` range
(`z≥1.07`), **this project still has no trustworthy `ρ` estimate** —
resolving that would require nonlinear halo bias treatment or direct
N-body pair statistics, neither attempted here.

## What this does NOT establish

1. Not a resolution of `P158`'s verdict across v82's full redshift
   range — only for `z≤0.5`, `4` of `8` tabulated points.
2. Not a floor-sensitivity-checked result — the `M_of(z)/2` choice is
   untested against nearby alternatives (`M_of(z)/4`, `M_of(z)`, a
   bounded bin). A real, named, unaddressed gap.
3. Not a validation of linear peak-background-split bias for v82's own
   specific "node" construction — a standard tool, applied, not checked
   against what v82's own nodes physically are.
4. Not an answer to `docs/153`'s 3 pre-conditions outright — a real,
   partial, honestly-scoped input to pre-condition 3's cost/consequence
   question. If anything, this REJECTs the idea that pre-condition 3 is
   cheap: even with real, standard, off-the-shelf peer-reviewed tools,
   half of v82's own redshift range remains out of reach without
   materially more specialized (nonlinear bias / N-body) work.
5. `NO_AUTHOR_ERROR`.

## Artifacts

- `CLAIM_P158_ADDENDUM2_real_mass_function.md`.
- This file (supersedes its own earlier PROMOTE-pending-skeptic draft,
  kept as this same file per this project's practice of writing the
  draft first and correcting in place when the correction happens
  before the draft is ever shown to the user — see `FINDING_P189`'s own
  precedent for the alternative, addendum-file pattern used when the
  draft WAS already shown).
- `P158_addendum2_real_mass_function.py` — all controls pass, `ruff`
  clean, now reports both mathematical validity and calibration-range
  validity explicitly, plus the fixed units conversion.
- Real sources: Tinker et al. (2008) arXiv:0803.2706, Tinker et al.
  (2010) arXiv:1001.3162 — coefficients verified against the primary
  source this session.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
