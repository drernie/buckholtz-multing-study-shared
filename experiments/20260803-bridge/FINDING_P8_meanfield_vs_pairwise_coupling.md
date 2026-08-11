# P8 — the smoothed-limit coupling coefficient: not one number, two, depending on the observable

**Date:** 2026-08-11 · answers the genuinely open item P6 §3 left unresolved:
does the near-field two-body suppression factor `ℓ_d/r=β_d(u_A+u_P)` (carries
a finite-size `r_A/r_sep` factor tied to one specific orbital separation)
transfer as-is to a smoothed, cosmological force-density context ("Reading
1"), or does the field-theoretic coupling coefficient there drop that factor
("Reading 2", per the skeptic's alternative in P6's own correction), leaving
a ~100x amplitude gap between the two.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Method:** a physical argument (analogy to gravitational polarizability,
the same language this project's own Q006 lead — Blanchet & Le Tiec 2008 —
already uses for its own dipolar-medium model), not a full field-theoretic
derivation from P1's action. Flagged `[INFERRED]` throughout, not
`[VERIFIED]` — see "What this does NOT establish."

---

## 1. The question was never "which reading is correct" — it was "correct for what"

P6's ~100x gap came from treating "the cosmological coupling coefficient"
as if it were one number. It is not, once the two readings are traced back
to what kind of physical calculation each one actually describes:

- **Reading 1 (`ℓ_d/r=β_d(u_A+u_P)`, keeps `r_A/r_sep`)** is the near-field,
  two-body force law, evaluated at whatever separation `r` the two bodies
  sit at. Nothing about its derivation (P1, `two_charge_completion.py`)
  assumes a *small* separation — it is the exact multipole expansion of a
  physical dipole pair, valid at any `r` large compared to the bodies'
  own size. Using it at a *cosmological* separation (Mpc, not AU) is not an
  extrapolation error — it is exactly the same calculation MULTING's own
  Eq. (15) already licenses, just evaluated at a bigger `r`.
- **Reading 2 (`2β_d(k/mc²)`, drops `r_A/r_sep`)** is what a MODIFIED
  POISSON EQUATION's coupling coefficient would look like in the point-
  source/continuum limit — the coefficient of a polarization-density term
  `∇·P(x)` sourcing the field, with no reference to any particular pair's
  separation, because a continuum description has no single separation to
  reference.

**These are not competing estimates of the same thing.** They are the
correct answer to two different questions:

```
"What is the force between THIS specific pair, at THIS specific
 separation?"                                    -> Reading 1 (pairwise)

"What is the mean-field coupling that shows up in a linearised
 growth/Poisson equation sourced by the SMOOTHED density field?"
                                                   -> Reading 2 (mean-field)
```

## 2. Sorting P6's own observable list by which question it asks

P6 §2 named four candidate observables for the two tiers. Each is
unambiguously one type or the other:

```
MEAN-FIELD (smoothed density field sources a modified Poisson/growth
equation; no single pair-separation to plug into r_A/r_sep):
  - growth rate f-sigma8(z), redshift-space distortions      -> Reading 2
  - gravitational slip / E_G statistic (lensing vs dynamics) -> Reading 2
  - bispectrum / CMB non-Gaussianity (F_kk tier)              -> Reading 2

PAIRWISE (the observable IS a function of a specific pair's separation):
  - pairwise kSZ (correlates specific halo PAIRS at measured separation)
                                                                -> Reading 1
  - apsidal/periastron precession (a literal two-body orbit)   -> Reading 1
    (already used correctly, unchanged, in FINDING_unsuppressed_
    observable_periastron.md and P7)
```

**Consequence:** chapter 4.3's kSZ non-detection and P7's pulsar bound were
never in question — both are genuinely pairwise observables, and both
already used Reading 1 correctly, before this file existed. What P6 left
ambiguous was specifically the mean-field trio (fσ8, E_G, bispectrum), and
those should use Reading 2 — the LARGER, more pessimistic amplitude.

## 3. The resolved forecast, per observable class

Reusing P6's own numbers, now correctly assigned:

```
MEAN-FIELD observables (fsigma8/RSD, E_G, bispectrum) -- USE READING 2:
  dG_eff/G  (linear, F_km tier)   ~ 7.0e-6   ->  ~3.2 orders of magnitude
                                                  below Euclid-class (~1e-2)
  bispectrum deviation (F_kk)     ~ 1.8e-11  ->  still far below any
                                                  realistic non-Gaussianity
                                                  sensitivity

PAIRWISE observables (kSZ, periastron) -- USE READING 1 (unchanged):
  ell_d (per-body, absolute)      ~ 7 pc     ->  ~6.4 orders below the kSZ
                                                  survey's own 18 Mpc floor
                                                  (P6 S3, P7 -- unchanged)
```

**Both classes remain undetectable at any current or near-future survey
precision.** The mean-field class is genuinely ~2 orders of magnitude closer
to detectability than P6's original (Reading-1-only) estimate suggested —
worth stating precisely rather than leaving as an unresolved ~100x
bracket — but "~3 orders of magnitude below Euclid" is still a decisive,
not a marginal, gap. No part of this changes P6's bottom-line "no full
observational-forecast pipeline is warranted."

## 4. Why this resolution, and not the reverse assignment

Could the mean-field observables instead need Reading 1, and the pairwise
ones Reading 2? No — this is fixed by what each observable structurally
integrates over, not a free choice:

- `fσ8(z)` and `E_G` are extracted from CORRELATION FUNCTIONS / POWER
  SPECTRA of the smoothed density and velocity fields — by construction,
  averages over the whole population of pairs at ALL separations,
  weighted by the survey's own window function. There is no single `r` to
  plug into `r_A/r_sep`; the natural quantity is the coupling in the field
  equation sourcing `δ` and `v` themselves, i.e. Reading 2's polarizability
  coefficient.
- Pairwise kSZ and periastron precession are, respectively, a statistic
  computed AT a chosen pair-separation bin and a literal single orbit at
  one physical separation — `r_A/r_sep` is not just available, it is the
  quantity the observable is built around.

## What this does NOT establish

1. **This is a physical argument by analogy, not a field-theoretic
   derivation.** The actual modified Poisson equation implied by P1's
   action (`two_field_action_closure.py`) has not been solved for its
   polarization-density source term; Reading 2's `2β_d(k/mc²)` is asserted
   by structural analogy to how a polarizability coefficient would enter
   such an equation (the same "polarizable in a gravitational field"
   language this project's own Q006 lead, Blanchet & Le Tiec 2008, uses for
   an analogous model), not derived from MULTING's own action term by term.
2. **Does not address scale-dependence.** P6 §2 already flagged that the
   dipole tier likely enters with an EXTRA power of momentum transfer
   relative to gravity's own `1/k²` Poisson kernel — meaning Reading 2's
   `2β_d(k/mc²)` is itself probably an approximation to something that
   should be `k`(wavenumber)-DEPENDENT, not a single flat number. Not
   derived here; flagged as the next, genuinely open step if this branch is
   pursued further.
3. **Does not change any verdict.** Both observable classes remain
   undetectable; this resolves the SIZE of the gap for the mean-field class
   (~3 orders, not left as an unresolved ~1.2-to-5.2-order bracket), not
   whether detection is plausible.
4. Per NO_AUTHOR_ERROR: this is entirely about how to correctly apply this
   project's own reconstruction (P1) to different observable types — not a
   claim about TJB's own theory or intentions.

## Reproduction

```python
beta_d = 2
k_over_mc2_cluster = 1.7e-6
table_value_per_betad = 3.5e-8  # FINDING_unsuppressed_observable_periastron.md, WITH r_A/r_sep
r_A_over_rsep = 1.0e-2

# Reading 1 -- pairwise (kSZ, periastron; unchanged from P6/P7)
ell_d_over_r_pairwise = beta_d * table_value_per_betad          # -> 7.0e-8

# Reading 2 -- mean-field (fsigma8/RSD, E_G, bispectrum)
ell_d_over_r_meanfield = ell_d_over_r_pairwise / r_A_over_rsep  # -> 7.0e-6

euclid_target = 1e-2
import math
print("mean-field, orders below Euclid:", math.log10(euclid_target / ell_d_over_r_meanfield))
```
