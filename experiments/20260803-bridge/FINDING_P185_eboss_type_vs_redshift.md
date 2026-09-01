# FINDING P185 — eBOSS quasar-BAO point breaks the redshift-vs-
# measurement-type confound left open by P184

**Date:** 2026-09-01
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (evaluation of a specific confound-
breaking test — not a new physics claim)
**Continues/answers:** `FINDING_P184`'s "NEW, UNRESOLVED" item — DESI
is simultaneously the only BAO-type point AND the most extreme-
redshift point in the real 33-point dataset, so its outsized
leave-one-out influence could be driven by either property, and
`P184` explicitly named "no second BAO-type point at another z" as
the reason this could not be separated within the existing dataset.
The user asked for a literature search for exactly such a point; a
research Agent found a real, independently-published candidate
(Neveux et al. 2020, eBOSS DR16 quasar BAO, z=1.480) — a real BAO-type
measurement at a NON-extreme redshift, inside the existing
cosmic-chronometer range.
**Script:** `P185_eboss_type_vs_redshift.py` (numpy/scipy/numdifftools,
4 tests, ruff clean, project test suite still passes, 881+ tests).
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** the eBOSS point's literature value and
> its conversion to H(z) are correctly sourced and computed; the
> leave-one-out comparison is correct once computed with a numerically
> robust method (adaptive Hessian) — the first draft's fixed-step
> method was shown to be unreliable for this specific construction and
> is retained only as a documented limitation, not as evidence.
> **Ontological/mechanistic interpretation status:** narrows but does
> not close `FINDING_P182`'s measurement-type-vs-redshift confound —
> specifically to quasar-clustering BAO vs Lyman-alpha-forest BAO
> (DESI's own tracer), which remains untested.
> **Causal/cosmological claim status:** N/A.

## Correction (2026-09-01, context-asymmetric skeptic-caught, applied
before finalizing — code verified present in the dispatch)

A skeptic review raised 6 attacks against the first draft (which used
only the original fixed-step finite-difference Hessian, the same
h1=1e-5 convention validated in `P176`-`P184`). Two were checked
directly before accepting, and one of those two led to an active
numerical fix rather than just a caveat.

**CONFIRMED BY DIRECT CHECK, THEN FIXED — per-point noise inflates the
z-score denominator.** The skeptic's strongest attack: Set B's
full-sample angle is fixed-step-fragile (documented below), and this
noise likely also contaminates the *individual* leave-one-out angles
used to compute `std(other_7)` in the z-score denominator, mechanically
biasing eBOSS's z-score toward looking "ordinary" for a numerical, not
physical, reason. Checked directly: all 7 CC-point leave-one-out
angles in Set B showed comparable-or-larger step-size sensitivity than
eBOSS's own drop. The attack was correct. **Fix:** switched to
`numdifftools.Hessian` (adaptive Richardson extrapolation) as the
file's primary method — confirmed it reproduces Set A's known-correct
angle (~0.0193, matching `P178`-`P184`) and gives a much tighter,
fair, apples-to-apples comparison for both sets under the *same*
numerical method. Re-ran the full leave-one-out analysis across 3
independent step configurations (`step=None` fully adaptive, `1e-4`,
`1e-3`): **DESI z-scores = {9.89, 14.63, 9.74}** (always the max of 8),
**eBOSS z-scores = {0.52, 0.89, 0.45}** (never the max — and at every
configuration, the actual maximum leave-one-out deviation in Set B
belongs to the ordinary cosmic-chronometer point at z=1.037, not
eBOSS). The fix strengthened the finding rather than undermining it —
the qualitative result survives a genuine, independently-verified
improvement in numerical rigor.

**ACCEPTED, NARROWS THE CONCLUSION — categorical slippage between
quasar-clustering BAO and Lyman-alpha-forest BAO.** eBOSS DR16
(Neveux et al. 2020) is a quasar-clustering BAO measurement; DESI's
own z=2.33 point is a **Lyman-alpha forest** BAO measurement — a
different tracer with different systematics. Testing with eBOSS does
NOT test the specific measurement type DESI represents. The
conclusion is narrowed accordingly: this file provides evidence
against "quasar-clustering BAO measurement type" as the driver, not
against "BAO measurement type" in general — Lyman-alpha-forest BAO at
a non-extreme redshift remains an untested, live alternative.

**ACCEPTED, UNADDRESSED LIMITATION — r_d conversion uncertainty not
propagated.** eBOSS's D_H(z)/r_d = 13.26±0.55 was converted to
H(z)=153.707±6.375 km/s/Mpc using r_d_fid=147.09 Mpc (Planck-2018-like,
the standard BOSS/eBOSS/DESI convention). This fiducial value's own
uncertainty was not swept or propagated into the quoted sigma, and was
not independently cross-checked against TJB's own DESI-point
provenance. Left as a documented, unaddressed limitation.

**ACCEPTED, UNADDRESSED LIMITATION — "residual size at insertion"
confound.** Is eBOSS's H(z) value simply unusually close to the
existing CC-point trend at z≈1.48, rather than genuinely "ordinary" in
a leave-one-out sense for a deeper reason? Not directly tested. Partly
(not fully) reassured by the finding that the actual maximum
leave-one-out deviation in Set B belongs to an ordinary CC point
(z=1.037), not eBOSS itself — if eBOSS were simply an easy insertion
point, that alone would not explain why a genuinely unrelated CC point
also outranks it.

**Superseded — the arbitrary `desi_zscore/3` threshold.** The original
draft's test used a somewhat arbitrary divisor-based threshold. Given
the much cleaner separation under the adaptive method (DESI's minimum
across configs, 9.74, vs eBOSS's maximum, 0.89 — over a 10× gap), the
same divide-by-3 threshold is retained in the test but is no longer
load-bearing to the conclusion — the gap is decisive at any reasonable
threshold.

## 0. Premise — `NO_AUTHOR_ERROR`

This file evaluates a specific confound-breaking test against TJB's
own real cosmic-chronometer data plus one independently-published
literature point (Neveux et al. 2020); it makes no claim about v82's
own theory.

## 1. What was attempted

`FINDING_P184` left DESI's outsized leave-one-out influence
attributable to either its extreme redshift (z=2.33, the highest in
the real dataset) or its unique measurement type (the only BAO-type
point among 7 cosmic-chronometer points) — with no way to separate
these within the real 33-point dataset (no second BAO-type point at
another redshift existed there). A literature search (per the user's
request) found a real candidate: Neveux et al. 2020 (eBOSS DR16
quasar BAO, MNRAS 499, 210, arXiv:2007.08999), z_eff=1.480,
D_H(z)/r_d=13.26±0.55, converted to H(z=1.480)=153.707±6.375 km/s/Mpc.

Two parallel 8-point sets were built from the same 7 real
cosmic-chronometer points (z=1.037-1.965):
- **Set A** = 7 CC points + DESI (z=2.33) — already established in
  `P178`-`P184`.
- **Set B** = the same 7 CC points + eBOSS (z=1.480) — a new
  construction isolating "BAO type" from "extreme redshift," since
  eBOSS sits WITHIN the existing CC redshift range, not beyond it.

If eBOSS (BAO type, ordinary redshift) behaves like an outlier the way
DESI does, that would point toward measurement type as the driver. If
it behaves ordinarily, that points toward redshift extremity (or
DESI's specific position as the sample's edge/leverage point).

## 2. Results

```
Positive control: Set A full angle = 0.01945 (fixed-step, h1=1e-5),
                                      0.01932 (adaptive Hessian)
                   both match P178-184's established ~0.0193-0.0195

Set B fixed-step fragility (documented limitation, NOT used for the
final comparison): angle across h1=(2e-6, 1e-5, 2e-5) =
  [0.02015, 0.01976, 0.02023] -- not a clean plateau, unlike Set A

Set A leave-one-out (adaptive Hessian, step=1e-4):
  DESI (z=2.33) drop: 0.02002 deg -- the maximum of all 8

Set B leave-one-out (adaptive Hessian, step=1e-4):
  eBOSS (z=1.48) drop: 0.02002 deg -- NOT the maximum
  (max in Set B is the ordinary CC point at z=1.037: 0.02102 deg)

DESI z-scores across 3 adaptive configs (None, 1e-4, 1e-3):
  {9.89, 14.63, 9.74} -- always the max of 8

eBOSS z-scores across the same 3 configs:
  {0.52, 0.89, 0.45} -- never the max of 8
```

## 3. Verdict

**SUPPORTED, narrower than originally framed**: a real, independently-
published QUASAR-CLUSTERING BAO point (eBOSS DR16, z=1.48), added at a
non-extreme redshift within the existing cosmic-chronometer range,
behaves like an ORDINARY point under a fair, apples-to-apples
numerical comparison — never the maximum leave-one-out drop, z-score
0.45–0.89 at every tested configuration, versus DESI's 9.74–14.63 at
the same configurations. This is real evidence against
**quasar-clustering BAO measurement type specifically** as the driver
of DESI's outsized influence.

**NOT ESTABLISHED**: evidence against "BAO measurement type" in
general. DESI's own z=2.33 point is a **Lyman-alpha-forest** BAO
measurement — a different tracer with different systematics from
quasar-clustering BAO — which remains untested and a live alternative
explanation.

**UNCHANGED**: `FINDING_P177`'s central open question (genuine
correspondence vs. Taylor-truncation leverage) is not resolved by this
file. This file narrows, but does not close, which confound explains
`FINDING_P182`'s original observation — the balance of evidence now
points somewhat more toward redshift extremity (or DESI's specific
position as the sample's edge/leverage point) than toward measurement
type broadly, but Lyman-alpha-forest BAO specifically remains an open
alternative.

**NEW, notable but not decisive**: at every tested numerical
configuration, the actual maximum leave-one-out deviation in Set B
belongs to the ordinary cosmic-chronometer point at z=1.037, not
eBOSS — a detail consistent with "nothing eBOSS-specific is going on
in Set B," but not independently investigated further here.

## 4. What this file does NOT establish

1. **Not a claim about v82's own theory** (`NO_AUTHOR_ERROR`, §0).
2. **Does not test Lyman-alpha-forest BAO specifically** — only
   quasar-clustering BAO (eBOSS). DESI's own point is Lyman-alpha
   forest; a genuinely matched test would need a Lyman-alpha-forest
   BAO point at a non-extreme redshift, which was not found in this
   search.
3. **r_d=147.09 Mpc conversion's own systematic uncertainty was not
   propagated or swept**, and was not independently cross-checked
   against TJB's own DESI-point provenance.
4. **The "residual size at insertion" confound (is eBOSS's H(z) value
   just unusually close to the existing trend?) was not directly
   tested** — only informally weakened by the z=1.037 detail above.
5. **Does not, by itself, resolve `FINDING_P177`'s central question**
   (genuine correspondence vs. Taylor-truncation leverage).
6. **No formal statistical significance is claimed** for any reported
   z-score — leave-one-out-derived angles remain non-independent
   samples (same caveat as `P182`-`P184`).
7. **Does not establish a causal mechanism** for why redshift
   extremity (if that is the real driver) would matter to this
   geometric quantity — descriptive only.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
