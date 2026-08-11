# P6 — perturbative order of each MULTING tier, and what the amplitude forecast does and does not establish

**Date:** 2026-08-11, corrected same day after context-blind skeptic review
(Step 8a) · answers the cheapest-next-step named at the end of P4
(`FINDING_P4_two_field_does_not_rescue_background.md` §8): derive the
perturbative order of `F_m, F_km, F_kk`, find the first nonzero
gauge-invariant observable, forecast effect size against a real survey
*before* building any analysis pipeline.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Method:** order-of-magnitude scaling argument, reusing already-verified
numbers from two prior findings in this directory — not a from-scratch
linear-perturbation-theory derivation. Flagged `[INFERRED]` throughout, not
`[VERIFIED]`, for exactly that reason — see §5.

**[CORRECTED after skeptic review — read before the rest of this file.]** The
first version of this finding claimed the linear-tier signal was "~7 million
times below Euclid" and concluded "no forecasting pipeline is warranted,"
full stop. A context-blind skeptic pass found three real problems, not
quibbles: (1) that "7 million" was simply a misread of my own arithmetic —
the correct ratio is closer to 140,000×, an error independent of anything
the skeptic checked, caught only in redoing the numbers cleanly for this
correction; (2) the single most load-bearing step — reusing a suppression
factor computed for a *specific two-body orbit* (`r_A/r_sep`, a finite-size
factor tied to one orbital separation) as if it were the coupling
coefficient in a *smoothed, cosmological* force-density context — is not
derived and may not transfer; removing that factor raises the predicted
signal by ~100×, which still leaves it undetectable but by a much smaller,
less comfortable margin (~3 orders of magnitude, not ~5); (3) "mechanism-
independent" was over-stated — the two-charge completion's own `A↔B`
symmetry argument already fixes the mechanism (mirror-symmetric induced
polarisation, the Blanchet-DDM branch), so the claim should cite that
specific result, not claim independence from it. All three are fixed in
place below, not silently. The headline conclusion is downgraded from "no
pipeline needed, full stop" to "no full observational-forecast pipeline is
needed to establish current undetectability, which survives under both
candidate readings of the cross-context reuse question — but the smaller,
genuinely open task of deriving the smoothed-limit coupling coefficient
remains undone, and a separate, independent, and far more decisive
constraint (the pulsar bound on `β_d`, conditional on how `k` is defined)
was under-weighted in the first version and is now given its proper
prominence in §3a."

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

**[CORRECTED after skeptic review — "mechanism-independent" was over-stated.]**
The first version of this section claimed the order-counting holds regardless
of mechanism, rescaling only an `O(1)` prefactor either way. A skeptic pass
found this both wrong as stated and unnecessary: `FINDING_two_charge_
completion.md` §3 does NOT leave the mechanism open — MULTING's own `F_d`
being symmetric under `A↔B` **forces** the mirror-symmetric configuration
(each body's moment radially aligned on the other, i.e. induced polarisation)
and excludes both the parallel and the intrinsic-random configurations. That
file's own text names this the branch that "does enter linear growth (Blanchet
DDM)." So the correct statement is narrower and stronger, not "independent of
mechanism": on the ONE mechanism the completion's own symmetry argument
actually selects (induced/Blanchet-DDM-type polarisation, not intrinsic-random
averaging), the moment IS correlated with a local field gradient by
construction, and the order-counting below applies to that specific,
already-established branch. The intrinsic-random branch — which this project's
own P1 §3 computed separately and found averages to exactly zero — is not a
live alternative for MULTING's own force law; it was already excluded, not a
second case this order-counting needs to cover. That power is fixed by
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
J0737-3039 reproduced to 0.04%) already computed the dimensionless suppression
`ℓ_d/r = 2β_d(k/mc²)(r_A/r_sep)` for real cluster pairs, from this project's
own 548-cluster sample:

```
cluster pair, cosmological:  (k/mc²) = 1.7e-6   r_A/r_sep = 1.0e-2   ell_d/r per beta_d = 3.5e-8
```

**[CORRECTED after skeptic review — this number was derived for a specific
two-body ORBIT, and porting it to a smoothed cosmological context is an
assumption, not a derivation. Two readings are given below; the first version
of this file only gave the first and mislabelled its own comparison to
Euclid.]** `r_A/r_sep` is the ratio of one body's own radius to its distance
from the OTHER body in that specific orbit — a finite-size correction to a
two-body force law. Whether that same factor also multiplies the coupling
coefficient that appears in the smoothed, many-body cosmological force
density (the term that would enter a linearised Euler equation) has not been
derived; the field-equation/point-source limit of a modified-Poisson-type
system would naturally carry the coefficient `2β_d(k/mc²)` **alone**, without
a `r_A/r_sep`-type factor, since there is no single "separation" in a
continuum description. Both readings, combined with the two-charge
completion's own derived (not fitted) values `β_d=2`, `ℓ_q²/ℓ_d²=0.375`
(`FINDING_two_charge_completion.md` §4):

```
Reading 1 -- orbital / finite-size (as originally used, table value as-is):
  ell_d/r      = beta_d * 3.5e-8                    = 7.0e-8     <- ~dG_eff/G
  ell_q^2/r^2  = 0.375 * (7.0e-8)^2                 = 1.8e-15

Reading 2 -- field-coupling / point-source (r_A/r_sep removed, per skeptic):
  ell_d/r      = (Reading 1 value) / (r_A/r_sep)    = 7.0e-6     <- ~dG_eff/G
  ell_q^2/r^2  = 0.375 * (7.0e-6)^2                 = 1.8e-11
```

**Against real survey targets, both readings, corrected comparison.** Euclid-
class growth-rate / `G_eff` measurements target `~1%` (`1e-2`) precision.

```
Reading 1: signal/target = 7.0e-6  ->  ~5.2 orders of magnitude below Euclid
Reading 2: signal/target = 7.0e-4  ->  ~3.2 orders of magnitude below Euclid
```

(The first version of this file said "~7 million times smaller" for Reading
1 — that was a misreading of `7.0e-8/1e-2 = 7.0e-6` as if the exponent's sign
made it a large number rather than a small fraction; the number itself,
`7.0e-8`, was correctly computed, only the English description of the ratio
was wrong. Corrected here.) **Under either reading, the linear tier remains
below current Euclid-class targets** — by ~5 orders of magnitude under
Reading 1, or a less comfortable but still-decisive ~3 orders under Reading
2. The quadratic tier stays hopeless under both readings (`1.8e-15` to
`1.8e-11`, still far below any realistic bispectrum/non-Gaussianity
sensitivity, which is not sub-`1e-8`-level precise on dimensionless
parameters). **Which reading is correct is not resolved by this finding** —
resolving it requires deriving the actual smoothed-limit coupling
coefficient, a genuinely open, targeted task (see the corrected Verdict
below), smaller in scope than a full survey-forecast pipeline.

**Cross-check against the already-run kSZ test, corrected.** The pairwise-kSZ
forecast's own sensitivity floor on `ℓ_d` is `σ~18 Mpc` (`pearl_registry/
INDEX.md`, 2026-08-10 periastron row). **[CORRECTED — the first version
computed the predicted `ℓ_d` by multiplying the RATIO `ℓ_d/r` by an arbitrary
"few Mpc" separation, which double-counts `r`; `ℓ_d` itself is a per-body
length, independent of any orbital separation, `ℓ_d=2β_d(k/mc²)r_A`.]** Using
`r_A~1` Mpc (the periastron table's own cluster-radius scale): `ℓ_d = 2×2×
1.7e-6×1` Mpc `= 7.0e-6` Mpc `≈ 7` pc — about **6.4 orders of magnitude below
the kSZ survey's 18 Mpc noise floor**, not the "eight orders" first claimed.
The qualitative conclusion is unchanged: chapter 4.3's non-detection (`p=0.49`)
was never informative about whether MULTING's k-sector mechanism is real, at
either the original or the corrected margin — the predicted signal was always
going to be invisible to that measurement. This remains a retroactive
sharpening of that earlier result's interpretation, not a contradiction of it,
with the numerical margin corrected.

## 3a. The far more decisive, and independently existing, constraint — added after skeptic review

**This is the single biggest gap in the first version of this file.** The
same periastron finding that supplies `ℓ_d/r=3.5e-8` also derives a direct
observational bound on `β_d` from binary-pulsar timing (J0737-3039):
`β_d < 1.2e-5` **under the reading where `k` includes broad "internal kinetic
energy of sub-objects"** (binding, rotational, degeneracy energy — the
corpus's own broader phrasing in places), versus `β_d < ~1e7`-ish headroom (no
meaningful bound) if `k` is strictly thermal kinetic energy, in which case
cold degenerate neutron-star interiors carry `u_NS~0` and the pulsar bound
evaporates. This project's own `β_d=2` (P1, derived not fitted) is:

```
2 / 1.2e-5 = ~166,667  ->  EXCLUDED by more than five orders of magnitude
             under the broad-k reading, independent of any cosmological
             question this file asks at all.
```

The entire forecast in §3 is therefore **conditional on `k` being strictly
thermal** — the same open, load-bearing definitional question `MODEL_SPEC_
AUDIT.md` already names ("OPEN, and load-bearing: the single definition of
k — every unresolved test in Sec 4 traces back to it"). If that question
resolves toward the broad reading, `β_d=2` is already dead by pulsar timing
alone, and this entire cosmological-forecast question becomes moot — no
survey, current or future, would be needed to know the answer. This is a
cheaper, more decisive, and already-existing constraint that should have been
stated before, not after, the cosmological forecast; the first version of
this file mentioned the periastron finding only for its `3.5e-8` number and
did not carry this caveat forward.

## 4. Why using the cluster number is conservative, not optimistic — for the population choice specifically

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
signal FOR THE POPULATION CHOICE specifically. **This argument does not touch
§3's separate, unresolved `r_A/r_sep` reuse question** — that is about
whether a two-body finite-size factor survives the move to a smoothed
context at all, a different axis than which population of tracers to use,
and this section says nothing about it either way.

## Verdict

```
F_m  (monopole)  : O(delta^0) background + O(delta) peculiar force -- standard
                    LCDM, not a discriminator.
F_km (dipole)    : first nonzero at O(delta), linear order, on the mechanism
                    MULTING's own symmetry already selects (Blanchet-DDM
                    branch, not a free choice -- see corrected S1).
                    Predicted dG_eff/G ~ 7e-8 (Reading 1, orbital) to ~7e-6
                    (Reading 2, field-coupling) -- ~3 to ~5 orders of
                    magnitude below Euclid-class target sensitivity under
                    EITHER reading; which reading is correct is not resolved
                    here.
F_kk (quadrupole): first nonzero at O(delta^2), second order. Predicted
                    ~1.8e-15 to ~1.8e-11 depending on reading -- hopeless
                    against any realistic bispectrum sensitivity under both.
Already-run kSZ test (ch. 4.3): retroactively explained, not contradicted --
                    the non-detection was guaranteed by the suppression
                    scale alone (~6.4 orders of magnitude below that
                    survey's own noise floor, corrected from an earlier
                    "eight orders" arithmetic slip), not informative about
                    mechanism truth either way.
Independent, cheaper, and MORE decisive constraint (S3a): beta_d=2 is
                    already excluded by pulsar timing at >5 orders of
                    magnitude IF k includes broad "kinetic energy of
                    sub-objects" rather than strictly thermal energy -- an
                    open question this project has already flagged
                    (MODEL_SPEC_AUDIT.md) and which this file's forecast is
                    entirely conditional on, upstream of any cosmological
                    consideration.
```

**[CORRECTED after skeptic review — downgraded from "no forecasting
pipeline is warranted, full stop."]** The current-undetectability conclusion
survives under BOTH candidate readings of the cross-context reuse question
(§3), so a full RSD/bispectrum survey-forecast pipeline, run against real
Euclid covariances, would very likely still answer "undetectable" — that
specific, large piece of work is not the right next step. But two smaller,
genuinely open tasks remain, and calling them both unnecessary was an
overclaim:

1. **Deriving the smoothed/continuum-limit coupling coefficient** (resolving
   Reading 1 vs. Reading 2, §3) — this is exactly the kind of calculation "no
   pipeline needed" was meant to head off, but it is a well-scoped, much
   smaller task than a full observational forecast, not the same thing. Not
   done here.
2. **Resolving whether `k` is strictly thermal** (§3a) is cheaper than either
   of the above and more decisive than both combined — if it resolves toward
   the broad reading, this entire forecast (and the two-charge completion's
   `β_d=2` itself) is already dead, independent of any cosmological question.
   This should be the actual next step, not a cosmological pipeline of any
   size, pending the end of the correspondence pause.

## What this does NOT establish

1. **This is a scaling argument, not a derivation.** The linear Euler/Poisson
   system with an explicit `k`-sector source term has not been written down
   or solved; the `O(δ)` and `O(δ²)` claims follow from counting derivatives/
   moments, not from a worked perturbation-theory calculation. Flagged
   `[INFERRED]`, not `[VERIFIED]`, throughout §1-§3's translation step
   specifically (§3's raw numbers themselves, reused from prior findings, ARE
   `[VERIFIED]`).
2. **Does not resolve which reading (orbital vs. field-coupling) of the
   cross-context reuse in §3 is correct** — genuinely open, ~100× apart, and
   this file explicitly does not adjudicate it (corrected from claiming a
   single confident number).
3. **Does not rule out a fundamentally different completion** (not built from
   `k` as a per-body derivative-coupled charge at all) producing a larger
   cosmological signal — only this project's own actual construction (P1,
   the two-charge completion) and its measured input numbers.
4. Per NO_AUTHOR_ERROR: this says nothing about an error in TJB's own theory —
   it is this project's own reconstruction attempt's own forecast, using this
   project's own coupling-strength estimate, not TJB's.

## Skeptic verdict (Step 8a, Context Asymmetry — claim + the three cited
source files only, no session history)

Four separate verdicts, not merged, matching this project's own Falsification
Ladder protocol:

```
(1) Perturbation-order claim (F_km->O(delta), F_kk->O(delta^2)): WEAKENED
    -- directionally right on the mechanism MULTING's own symmetry actually
    selects, but the "mechanism-independent" justification given was wrong;
    corrected in S1 to cite that mechanism specifically instead.
(2) Cross-context number-reuse forecast (dG_eff/G~7e-8): FALSIFIED as a
    single confident number -- the r_A/r_sep reuse is unresolved; both
    readings now given (S3), ~100x apart, neither adjudicated.
(3) kSZ retroactive-explanation: WEAKENED -- directionally correct, but the
    "eight orders" arithmetic mixed a per-body length with a stray
    separation factor; corrected to ~6.4 orders (S3), and the far more
    informative pulsar-timing constraint was under-weighted (added as S3a).
(4) "No pipeline needed" bottom line: FALSIFIED as originally scoped --
    depended entirely on (2). Corrected Verdict above: no FULL
    observational-forecast pipeline needed (survives under both readings),
    but the smaller coupling-coefficient derivation and the k-definition
    question both remain genuinely open, and the latter is more decisive
    than anything in this file.
```

## Reproduction

```python
beta_d = 2
beta_q2_over_d2 = 0.375  # FINDING_two_charge_completion.md, verified sqrt(6)/2 ratio squared-fraction
table_value_per_betad = 3.5e-8  # FINDING_unsuppressed_observable_periastron.md, table row 1 (WITH r_A/r_sep)
r_A_over_rsep = 1.0e-2

# Reading 1 -- orbital / finite-size, as the periastron table states it
ell_d_over_r_orbital = beta_d * table_value_per_betad          # -> 7.0e-8
ell_q2_over_r2_orbital = beta_q2_over_d2 * ell_d_over_r_orbital ** 2   # -> 1.84e-15

# Reading 2 -- field-coupling / point-source, r_A/r_sep removed
ell_d_over_r_field = ell_d_over_r_orbital / r_A_over_rsep       # -> 7.0e-6
ell_q2_over_r2_field = beta_q2_over_d2 * ell_d_over_r_field ** 2  # -> 1.84e-11

# pulsar cross-check, independent of cosmological reading
pulsar_bound_broad_k = 1.2e-5   # FINDING_unsuppressed_observable_periastron.md S4
excluded_by_factor = beta_d / pulsar_bound_broad_k              # -> ~166,667
```
