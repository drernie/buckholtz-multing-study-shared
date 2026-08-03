# Decision — certification of C1–C4

**Date:** 2026-08-03 · All criteria frozen before any independent run.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive

---

## Verdicts

```
Table A1 reproducible operator : NO (in the available material)   C1 PASS
Table A1 transcription         : FAITHFUL after correction        C2 PASS
Naive pair-fluid virial mapping: FAIL (w = n/3, no DE EoS)        C3 PASS
Amplitude bound                : CLAIM DIRECTION CONFIRMED,
                                 OUR IMPLEMENTATION FAILED        C4 FAIL
Local force law                : NOT ADJUDICATED
Covariant MULTING+             : OPEN
Figure 3 provenance            : NOT ADJUDICATED — separate object
```

Three of four certified. The fourth failed its own frozen criterion, in the
direction that strengthens the conclusion and weakens our arithmetic.

---

## C1 — provenance · **PASS**

An independent reader, given only the source pages, not told that an AI service
was suspected, and asked four open questions, returned
`NO_REPRODUCIBLE_OPERATOR_IN_THIS_EXCERPT`.

It found four passages we had not read, all grep-verified before acceptance:
three AI services were tried; they "disagreed somewhat" on the observed `H(z)`;
disagreements on `β_d`, `β_q` "were noticeable"; and disagreements on `H(z)`
"calculated via MULTING" "were noticeable".

**The H-MULT column is determined by which service was asked, not by MULTING —
and the author says so.** This independently corroborates this project's own
BRAI measurement of a 5.8× and 95× `β` spread across three services.

**Unresolved, and answerable.** The `w_eff` prompt explicitly supplied H-data as
input. For H-MULT the excerpt says nothing either way. Whether the service had
the observations in hand is the difference between a prediction and a fit, and
Supplemental Material [251] contains the transcripts.

## C2 — transcription · **PASS**

Independent re-extraction: **0 mismatches of 132 fields** against our corrected
file; **exactly our four discrepancies** against the original, at the same
row-1 fields.

Validated three ways, two of which we had not used — including a prose
cross-check ("nine of twelve times … the other three times (13, 5, and 4)")
that confirms the time column using text not used to build the rows.

## C3 — the virial identity · **PASS**

Derived blind: the analyst was given only the two definitions and the potential
form, was not told the answer or its sign, and was told to derive rather than
recall. Returned `p/rho = n/3` via Euler's identity, verified symbolically and
across 360 configurations to 6.7 × 10⁻¹⁶.

Three refinements beyond Path A: the invariance caveat made determinate (pair-set
regularisations preserve it, functional-form regularisations break it, with the
mechanism given for each); confirmation of our sign correction, together with an
explicit refusal to draw a cosmological conclusion from it; and a caution that
`rho` and `p` are separately cutoff-dependent, raised by an analyst who did not
know C4 existed.

## C4 — amplitude · **FAIL**

```
Path A dipole at L_d = 8 Mpc :  3.9e-05
Path B dipole at L_d = 8 Mpc : ~3e-08
difference                   : 3.11 orders  ->  FAIL (rule: >2 orders)
```

**Cause.** Everything factorises through `rho_eff = n<m>`, the mass density in
clusters. Our `n = 1e-4, M = 1e15` gives `rho_eff/rho_m = 2.52` — **252 % of all
matter in the universe**. Described as a "generous ceiling"; it was outside the
mass budget. Since `rho ∝ rho_eff²`, that alone is 2.79 of the 3.11 dex.

**The claim's substance survives, strengthened**: `10⁻⁷`, range `10⁻⁸–10⁻⁶`,
three orders further from cosmological relevance than we claimed.

**Three findings that change the record.** All requested `s_min` values lie
inside the halo exclusion radius (2.89 Mpc for 10¹⁴ M☉), so quadrupole numbers
are overestimates by ~10×. The homogeneous dipole term grows *linearly* with
`s_max` and exceeds its clustering term at ~2 Gpc, so "the dipole energy density
of the universe" is not well defined without background removal — the same
structural point the C3 analyst reached independently on a different question.
And `r0 = 15–25 Mpc` is not self-consistent with mass selection above 10¹⁴ M☉.

**New structural result.** The dipole needs 10⁴–10⁵ Hubble radii to reach
`rho_crit`; the quadrupole needs only ~5–15, because it is quadratic in its
length scale. Neither is viable, but they fail by different amounts, and our
"46× the Hubble radius" figure is withdrawn.

---

## What must now change in the record

| item | action |
|---|---|
| NR-018 Ground 2 | replace Path A numbers with Path B's; record the abundance error |
| `FINDING_effective_fluid_energy_scale.md` | numbers superseded; direction stands |
| "207 Gpc = 46× Hubble radius" | **withdrawn** |
| "generous ceiling" framing | **withdrawn** — it was not a ceiling |
| NR-018 relaxation map | sharpen using C3's pair-set-vs-functional-form rule |

---

## Two errors of ours, both caught by independence, both worth naming

1. **The unphysical abundance.** An assumption called "generous" was never
   checked against the conservation law that bounds it. Expressing `rho_eff` as
   a fraction of `rho_m` makes the violation visible in one line — which is
   exactly what Path B did unprompted.
2. **Six overclaims in the first report**, corrected before this certification
   began: "no operator produced it", "no inverse-power potential accelerates"
   (missing the sign qualifier on `rho`), "Layzer–Irvine closed", "independent of
   cutoff" applied to the amplitude, "kSZ does not touch the bridge", and "all
   dark-energy models are fields".

Both are the same failure: stating a result at a scope wider than the evidence.
The project's own memory records this pattern under `feedback_evidence_inflation`.

---

## What is now established, at defensible scope

> The available material does not contain a deterministic, published,
> reproducible operator carrying the MULTING force law to the published `H(z)`;
> Table A1 is one AI service's response to a prompt, and the author labels it as
> such. Our copy of that table is faithful. A positive-density virial mapping of
> a pure inverse-power pair potential gives `w = n/3` and therefore no
> dark-energy equation of state. The interaction energy density of the cluster
> population under that mapping is of order `10⁻⁷` of critical, with a firm
> ceiling of `10⁻⁶`.

## What is not established

The local force law is untested by any of this. A covariant completion — an
action whose stress-energy sources the background, with the force law as its
non-relativistic limit — is untouched. Figure 3's provenance is a separate
object with separate evidence. Backreaction is not adjudicated. And the kSZ
constraint, while independent of Table A1, does bound any bridge relating the
same force law to structure growth.

---

## Next actions, in order of information value

1. **Read Supplemental Material [251]** — settle whether H-MULT was produced with
   the observations in hand. A provenance question with a determinate answer,
   more informative than any further modelling.
2. **Correct the record** per the table above.
3. **Separate Figure 3 from Table A1** and audit its provenance on its own
   evidence.
4. Only then: the single surviving theoretical branch, covariant MULTING+, and
   only through its three gates — weak-field matching, background normalisation
   without inserted `Ω_X`, and perturbations.

**Not to be done:** contacting the author before the supervisor approves;
building MULTING+ before the above; treating any Table A1 number as a MULTING
prediction.
