# P8 — the smoothed-limit coupling coefficient: the mean-field number is withdrawn, not just corrected

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

**[CORRECTED after context-blind skeptic review, Step 8a — read this before
anything else in the file. This is a retraction of the headline number, not
a margin adjustment like P6/P7's corrections.]** The pairwise/mean-field
classification (§1-2) is **WEAKENED** — real intuition, not a derivation,
and it does not survive contact with two things this file failed to check
against: (a) `two_field_action_closure.py` §3 already computed, directly
and rigorously, that this SAME dipole term's smoothed/isotropic-limit
contribution is **exactly zero** — not `7×10⁻⁸`, not `7×10⁻⁶`, zero — and
this file never cited or reconciled that result; (b) `FINDING_P4_two_field_
does_not_rescue_background.md` §7 itself states the natural home of this
completion's new physics is **second-order** observables, not first order
— directly in tension with assigning the FIRST-order mean-field trio
(`fσ8`, `E_G`) to a nonzero Reading-2 number. **The specific number
`ΔG_eff/G~7×10⁻⁶` for mean-field observables is FALSIFIED as a quantitative
forecast and is withdrawn** — it was obtained by dividing Reading 1's number
by `r_A/r_sep`, not derived, and directly conflicts with the one thing this
project HAS rigorously computed in the closest comparable regime. §5 below
replaces §1-4's original claim with the corrected, honest status: the
mean-field coupling is **undetermined**, not `~7×10⁻⁶`. What survives:
Reading 1 remains correct for genuinely pairwise observables (kSZ,
periastron — unaffected), and the qualitative "still undetectable" verdict
likely survives any resolution of the missing calculation — but that is now
a weaker, more honest claim than a specific number.

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

## 3. The forecast originally proposed here — SUPERSEDED, kept for the record

**[This section is the original, now-falsified reasoning. Left in place per
this project's no-silent-edit discipline; §5 below is the corrected status.]**

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

The pairwise row is unaffected by the correction below. The mean-field row's
`~7.0e-6` number is withdrawn — see §5.

## 5. Corrected status, after skeptic review

**The zero-vs-nonzero conflict, stated precisely.** `two_field_action_
closure.py` §3 computes — not by analogy, by direct calculation — that this
completion's dipole-sourced contribution to the smoothed cosmological force
density is **exactly zero**, under isotropic/random-orientation averaging of
the intrinsic moment `p_i=κk_ir_i/c²`. That is the ONE thing this project
has rigorously computed in a regime close to what §1-4 above tried to
forecast by analogy. §1-4's Reading 2 (`~7×10⁻⁶`) was never checked against
it, and the two cannot both be treated as established: either the O(δ)
mean-field contribution genuinely differs from the O(δ⁰) background result
(possible — perturbing the density field breaks the exact isotropy that
kills the background term — but this has never been calculated, only
assumed), or the same symmetry that zeroes the background zeroes the
perturbation too (equally possible, not ruled out). **Nothing in this
project's files distinguishes these two possibilities.**

**A second, independent inconsistency, also unaddressed until now.**
`FINDING_P4_two_field_does_not_rescue_background.md` §7 states plainly:
"the natural new physics, if the dipolar/induced-moment picture is right,
lives in **second-order** cosmological observables ... not H(z)." P6 and
this file both assigned the mean-field trio (`fσ8`, `E_G` — both **first-
order**, linear observables) a nonzero forecast anyway, without addressing
why a completion whose own project-internal characterization places its new
physics at second order would show up at first order in `fσ8`/`E_G`
specifically. Not resolved here.

**Corrected verdict:** the mean-field coupling coefficient is
**UNDETERMINED**, not `~7×10⁻⁶`. It could plausibly be exactly zero (matching
the rigorously-computed background result, if the same orientation-averaging
symmetry survives to first order), a small nonzero number of unknown size
(if it does not), or genuinely scale-dependent (§"What this does NOT
establish" #2, already flagged before this correction). **No specific number
should be quoted for `fσ8`/`E_G` until the missing calculation is done.**

**What survives.** Reading 1 remains correct, and unaffected, for genuinely
pairwise observables — pairwise kSZ and periastron precession, where P6 §3
and P7's numbers stand as they were. The qualitative claim "MULTING's
k-sector, at this project's own coupling-strength estimate, is not
detectable by any near-future survey" likely survives whatever the missing
calculation eventually gives (even an O(1) rescaling of Reading 1's already-
tiny number would not reach Euclid-class sensitivity) — but that is now an
honest qualitative statement, not a specific quantitative forecast for the
mean-field trio.

**The actual next step, if this branch is pursued further** (not done
here, a bounded task, smaller than a full survey-forecast pipeline): write
the linear-order Euler equation with P1's k-sector source term included,
and redo the SAME orientation-averaging calculation `two_field_action_
closure.py` §3 already did for the background, one perturbative order
higher — determine directly whether the O(δ) contribution is zero, nonzero,
or scale-dependent, rather than assuming either.

## 4. Why this resolution, and not the reverse assignment — argument stands, conclusion doesn't

**[The classification logic below survives as a reasonable qualitative
argument for the PAIRWISE side (kSZ, periastron) — it is the MEAN-FIELD
side's leap from "no single r_A/r_sep" to "therefore ~7×10⁻⁶" that §5
withdraws. Absence of a pairwise-separation factor does not by itself
establish what the mean-field coupling IS — only that Reading 1's specific
form doesn't apply. §5's zero-vs-undetermined status is the honest
consequence.]**

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
   derivation** — and per §5, the analogy is now withdrawn as a
   quantitative forecast specifically because it was never checked against
   the one rigorous result in a comparable regime (`two_field_action_
   closure.py` §3's exact zero). The actual modified Poisson equation
   implied by P1's action has not been solved for its source term.
2. **Does not address scale-dependence** — this concern survives
   independently of §5's correction: even a properly re-derived mean-field
   coupling would likely be `k`(wavenumber)-dependent, not a flat number.
3. **Does not change the qualitative verdict, but does change the
   quantitative one.** "Undetectable at Euclid-class precision" likely
   survives for the mean-field trio regardless of how the missing
   calculation resolves (§5) — but "the number is `~7×10⁻⁶`" does not
   survive, and should not be cited as this project's forecast.
4. Per NO_AUTHOR_ERROR: this is entirely about how to correctly apply this
   project's own reconstruction (P1) to different observable types — not a
   claim about TJB's own theory or intentions.

## Skeptic verdict (Step 8a, Context Asymmetry — claim + the four cited
source files, no session history)

Two separate verdicts, not merged:

```
(1) Pairwise-vs-mean-field observable classification: WEAKENED
    -- real intuition for the pairwise side (kSZ, periastron -- unaffected);
    does not survive as a clean binary for the mean-field side, since (a)
    the bispectrum is itself parametrized by triangle configurations with
    specific scales, not "no separation anywhere" -- the skeptic's own
    example: at RSD-relevant k~0.05-0.3 h/Mpc, r_A*k ~ 0.05-0.3, neither
    Reading 1's 1e-2 nor Reading 2's "1" -- and (b) this file's own S2
    scale-dependence caveat already contradicts treating Reading 1 and
    Reading 2 as answers to different questions rather than limits of one
    scale-dependent coupling.
(2) The specific mean-field number (dG_eff/G~7e-6): FALSIFIED as a
    quantitative forecast. Obtained by dividing Reading 1 by r_A/r_sep, not
    derived; conflicts with two_field_action_closure.py's own directly-
    computed EXACT ZERO in the closest comparable regime (never cited or
    reconciled); conflicts with FINDING_P4_two_field_does_not_rescue_
    background.md S7's own statement that this completion's new physics
    lives at SECOND order, not the FIRST-order fsigma8/E_G this file
    assigned Reading 2 to (never addressed). Corrected to UNDETERMINED (S5).
```

**Cheapest next check the skeptic named, not yet done:** write the linear-
order Euler equation with P1's k-sector source term, redo the SAME
orientation-averaging calculation `two_field_action_closure.py` §3 already
did for the background, one perturbative order higher. A bounded symbolic
calculation, not a survey pipeline — this is what would actually replace
"undetermined" with a real number.

## Reproduction

```python
# Reading 1 -- pairwise (kSZ, periastron; unaffected by this correction)
beta_d = 2
table_value_per_betad = 3.5e-8  # FINDING_unsuppressed_observable_periastron.md, WITH r_A/r_sep
ell_d_over_r_pairwise = beta_d * table_value_per_betad          # -> 7.0e-8

# Reading 2's "7.0e-6" for mean-field observables is WITHDRAWN (S5) -- do
# not reproduce it as a forecast. The arithmetic (dividing by r_A/r_sep)
# still runs, but the result is not a validated prediction:
r_A_over_rsep = 1.0e-2
ell_d_over_r_meanfield_UNVALIDATED = ell_d_over_r_pairwise / r_A_over_rsep  # -> 7.0e-6, NOT a forecast
```
