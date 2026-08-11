# P6 — perturbative order of each MULTING tier, and why no forecasting pipeline is needed

**Date:** 2026-08-11 · answers the cheapest-next-step named at the end of P4
(`FINDING_P4_two_field_does_not_rescue_background.md` §8): derive the
perturbative order of `F_m, F_km, F_kk`, find the first nonzero
gauge-invariant observable, forecast effect size against a real survey
*before* building any analysis pipeline.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Method:** order-of-magnitude scaling argument, reusing already-verified
numbers from two prior findings in this directory — not a from-scratch
linear-perturbation-theory derivation. Flagged `[INFERRED]` throughout, not
`[VERIFIED]`, for exactly that reason — see §5.

---

## 1. The three tiers, in perturbation order

MULTING's force law has three radial tiers, `F(r) = -GA2/r² + GA3/r³ - GA4/r⁴`,
with `A2 ~ m_Am_B`, `A3 ~ (k_Am_B+m_Ak_B)`, `A4 ~ k_Ak_B` (P1, `two_charge_
completion.py`). Embedding this in a cosmological density field
`ρ(x)=ρ̄(1+δ(x))`:

- **`F_m` (monopole, `A2`).** Ordinary gravity. Background piece (`ρ̄`) sources
  `H̄(z)` via the Friedmann equations directly, not through this pairwise-force
  route at all. Perturbation piece sources `Φ` via the ordinary Poisson
  equation, `O(δ)`. Nothing new — this tier is the standard ΛCDM baseline, not
  a discriminator.

- **`F_km` (dipole, `A3`).** Requires ONE power of the `k`-charge's dipole
  moment. Regardless of which mechanism sources that moment — P1's intrinsic
  `p_i=κk_ir_i/c²` with orientation averaging, or the gradient-induced picture
  P4 raised and the skeptic left open — getting a nonzero, non-averaged-away
  cosmological signal requires correlating the moment's orientation with SOME
  preferred direction. The only direction available at leading order is
  `∇δ`/`∇Φ`, itself `O(δ)`. So `F_km`'s first nonzero contribution is `O(δ)`
  — **linear order**.

- **`F_kk` (quadrupole, `A4`).** Built from a PRODUCT of two such moments (one
  per body), each carrying the same `O(δ)` suppression. First nonzero
  contribution is `O(δ²)` — **second order**. This matches Blanchet & Le Tiec
  2008's own proven theorem for dipolar dark matter (indistinguishable from
  ΛCDM at first order, distinguishable only at second) — cited correctly this
  time, per P6's own predecessor's literature correction (P4 §6).

**Mechanism ambiguity does not change this table.** Whether the moment is
intrinsic-with-tidal-correlation or gradient-induced only rescales an `O(1)`
geometric prefactor (how efficiently orientation correlates with `∇δ`) — it
does not change which power of `δ` each tier enters at. That power is fixed by
counting how many `k`-charges (each needing one derivative/correlation to be
nonzero) a term carries: zero for `F_m`, one for `F_km`, two for `F_kk`.

## 2. First nonzero gauge-invariant observables

- **`F_km` (linear):** a genuine additional force `∝ ∇Φ`, same direction as
  gravity's own gradient. Rescales the effective coupling between mass and
  peculiar force — testable via the growth rate (`fσ8(z)`, redshift-space
  distortions) or, if scale-dependent (plausible, since the dipole tier picks
  up an extra derivative relative to gravity's `1/r²` — different `k`-scaling
  in Fourier space is expected but not derived here), via the gravitational
  slip / `E_G` statistic (lensing vs. dynamics).
- **`F_kk` (quadratic):** bispectrum / CMB non-Gaussianity, nonlinear growth,
  or — concretely, and already built in this project — **pairwise kSZ**,
  which directly probes correlated *pairs* of tracers and is exactly the
  natural two-point/`k_Ak_B`-sensitive statistic. Chapter 4.3 already ran this
  test (`f7_ksz_dipole_limit`, no detection, `p=0.49`, consistent with
  `ℓ_d=0`) — §4 below explains why that null was never in doubt regardless of
  whether MULTING's mechanism is real.

## 3. The forecast — reusing already-verified numbers, not new machinery

`FINDING_unsuppressed_observable_periastron.md` (2026-08-10, `[VERIFIED-SYMPY]`,
J0737-3039 reproduced to 0.04%) already computed the one number this forecast
actually needs: the dimensionless suppression `ℓ_d/r = 2β_d(k/mc²)(r_A/r_sep)`
for real cluster pairs, from this project's own 548-cluster sample:

```
cluster pair, cosmological:  (k/mc²) = 1.7e-6   r_A/r_sep = 1.0e-2   ell_d/r per beta_d = 3.5e-8
```

Combined with the two-charge completion's own derived (not fitted) values
`β_d=2`, `ℓ_q²/ℓ_d²=0.375` (`FINDING_two_charge_completion.md` §4):

```
ell_d/r        = beta_d * 3.5e-8               = 7.0e-8       <- F_km / linear tier, ~ dG_eff/G
ell_q^2/r^2    = 0.375 * (ell_d/r)^2           = 1.8e-15      <- F_kk / quadratic tier
```

**Against real survey targets:** Euclid-class growth-rate / `G_eff`
measurements target `~1%` (`1e-2`) precision; current best combined
lensing+RSD constraints (DES/KiDS-class) sit around a few percent. The
predicted linear-tier deviation, `7e-8`, is **~7 million times smaller** than
Euclid's own target sensitivity, and the quadratic tier is a further eight
orders of magnitude down from that.

**Cross-check against the already-run kSZ test.** The pairwise-kSZ forecast's
own sensitivity floor on `ℓ_d` is `σ~18 Mpc` (`pearl_registry/INDEX.md`,
2026-08-10 periastron row). The predicted `ℓ_d` itself, from `ℓ_d/r=7e-8` at a
cluster-pair separation of a few Mpc, is `~2e-7` Mpc — about **eight orders of
magnitude below the kSZ survey's own noise floor**. Chapter 4.3's non-detection
(`p=0.49`) was therefore never informative about whether MULTING's k-sector
mechanism is real — the predicted signal was always going to be invisible to
that measurement, independent of the theory's truth value. This is a
retroactive sharpening of that earlier result's interpretation, not a
contradiction of it.

## 4. Why using the cluster number is conservative, not optimistic

Per this project's own Conserved-Budget discipline: is `3.5e-8` a fair, or a
cherry-picked-favorable, number to use for a *typical* survey tracer? The
periastron table's own scan (§1 there) shows cluster pairs are **the worst
case among gravitationally bound systems it checked** — Sun-Earth gives
`9.3e-9`, galaxy pairs `1.8e-8`, both smaller. Since virial temperature (hence
thermal `k/mc²`) scales with mass, and most RSD/lensing survey tracers
(ordinary galaxies) are far less massive than the 548-cluster sample this
number came from, a typical survey tracer's `k/mc²` — and hence its predicted
deviation from ΛCDM — is expected to be **smaller still**, not larger. Using
the cluster number is therefore a generous upper bound on the achievable
signal, not an underestimate that could be hiding a larger effect elsewhere.

## Verdict

```
F_m  (monopole)  : O(delta^0) background + O(delta) peculiar force -- standard
                    LCDM, not a discriminator.
F_km (dipole)    : first nonzero at O(delta), linear order. Predicted
                    dG_eff/G ~ 7e-8 for the best real-cluster-sample estimate
                    of the coupling strength this project has. ~7e6x below
                    Euclid-class target sensitivity.
F_kk (quadrupole): first nonzero at O(delta^2), second order. Predicted
                    ~1.8e-15. ~8 orders of magnitude below the linear tier,
                    itself already hopeless.
Already-run kSZ test (ch. 4.3): retroactively explained, not contradicted --
                    the non-detection was guaranteed by the suppression
                    scale alone, ~8 orders of magnitude below that survey's
                    own noise floor.
```

**No forecasting pipeline is warranted.** Building the linear-perturbation
Euler/Poisson system with a `k`-sector source term, running an RSD/bispectrum
forecast against real Euclid covariances, would answer a question this
order-of-magnitude estimate already answers: MULTING's k-sector, at the
coupling strength this project's own real cluster data supports, cannot
produce a cosmologically observable deviation from ΛCDM at any currently or
foreseeably achievable survey precision — at either perturbative order.

## What this does NOT establish

1. **This is a scaling argument, not a derivation.** The linear Euler/Poisson
   system with an explicit `k`-sector source term has not been written down
   or solved; the `O(δ)` and `O(δ²)` claims follow from counting derivatives/
   moments, not from a worked perturbation-theory calculation. Flagged
   `[INFERRED]`, not `[VERIFIED]`, throughout §1-§3's translation step
   specifically (§3's raw numbers themselves, reused from prior findings, ARE
   `[VERIFIED]`).
2. **Does not resolve the intrinsic-vs-induced mechanism question** P4 left
   open — argued in §1 that it doesn't need to be resolved for this
   particular conclusion, since it only affects an `O(1)` prefactor against a
   `~1e-8` base suppression that dominates either way.
3. **Does not rule out a fundamentally different completion** (not built from
   `k` as a per-body derivative-coupled charge at all) producing a larger
   cosmological signal — only this project's own actual construction (P1,
   the two-charge completion) and its measured input numbers.
4. Per NO_AUTHOR_ERROR: this says nothing about an error in TJB's own theory —
   it is this project's own reconstruction attempt's own forecast, using this
   project's own coupling-strength estimate, not TJB's.

## Reproduction

```python
beta_d = 2
beta_q2_over_d2 = 0.375  # FINDING_two_charge_completion.md, verified sqrt(6)/2 ratio squared-fraction
u_per_betad_cluster = 3.5e-8  # FINDING_unsuppressed_observable_periastron.md, table row 1

ell_d_over_r = beta_d * u_per_betad_cluster            # -> 7.0e-8
ell_q2_over_r2 = beta_q2_over_d2 * ell_d_over_r ** 2   # -> 1.84e-15
```
