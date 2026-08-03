# Letter to Dr. Buckholtz — consolidated H(z) audit

**Status: DRAFT. Not sent. The user sends, not the assistant.**
Every number below traces to a certificate in `experiments/20260803-bridge/audit/`.

---

**Subject:** MULTING H(z) — consolidated audit, constructive result

Dear Dr. Buckholtz,

We have finished several independent reconstruction and falsification passes over
the MULTING H(z) material. I am writing to hand you the result rather than a list
of questions.

The outcome is constructive. The analysis does not reject the local MULTING force
law. What it does is separate the parts of the framework that are already
reproducible from the one part that still needs a physical bridge — and it closes
off two routes that would otherwise absorb a great deal of time.

**1. The local interaction is mathematically well defined and reconstructs
uniquely.**

From the published force law

    F(r,z) = -A2(z)/r^2 + A3(z)/r^3 - A4(z)/r^4

the potential follows without ambiguity:

    U(r,z) = -A2(z)/r + A3(z)/(2 r^2) - A4(z)/(3 r^3)

There is nothing to interpret here — the reconstruction is exact. The local force
law remains a testable physical hypothesis, and nothing in our work rejects it.

**2. The simplest cosmological bridge is now closed, and closed cleanly.**

For the standard configurational pair-fluid mapping, a pure inverse-power
potential U ∝ r^(-n) gives, through Euler's identity applied pair by pair before
any averaging,

    p = (n/3) ρ

so the three MULTING terms correspond to w = 1/3, 2/3, 1 within that mapping.
None of them is negative. The direct interpretation of pair-interaction energy as
a positive-density dark-energy component is therefore not sufficient, and this
holds as an identity rather than as a numerical estimate.

We verified this symbolically and across 360 configurations, to 7 × 10⁻¹⁶.

I want to be precise about the scope: this closes the naive pair-fluid route
**only**. It says nothing against a covariant medium, a polarisation sector, a
nonlocal completion, or explicit cosmological averaging. We have registered it as
a negative result so that neither of us spends further effort there.

**3. Table A1 and the later H(z) curve are two different objects.**

You flagged the status of Table A1 yourself — that the responses were obtained
from an online service and are "not necessarily trustworthy or directly useful."
We took that caveat seriously and worked out its numerical consequences: the
supplementary transcripts show β_d and β_q were selected by minimising deviation
from the H-data, with the curve normalised to the observed H₀ at z = 0. Table A1
is therefore best read as an exploratory, data-conditioned calibration rather
than as an independent forward prediction. That is a statement about the
procedure, not about the model.

The later orange MULTING curve is a **separate object with its own provenance.**
It is not a plot of Table A1. Digitised and compared point by point, the two
diverge monotonically:

    z      curve    Table A1 H_MULT     deviation
    0.00    73.9         73.0             +1.2 %
    0.40    83.0         83.1             -0.1 %
    0.65   101.2         91.4            +10.7 %
    1.00   130.4        104.2            +25.2 %
    1.50   172.1        126.5            +36.1 %
    2.10   218.6        151.8            +44.0 %
                                    rms   21 %

Nor is it flat ΛCDM re-anchored to a different H₀: the ratio between the two
plotted curves varies by 10 % across the range and crosses unity.

**As a positive control on our own extraction**, we fitted the blue curve on the
same figure and recovered

    H0 = 67.37,   Ω_m = 0.3152,   rms 0.002 %

— flat Planck ΛCDM, to two parts in a hundred thousand. So the distinct shape of
the MULTING curve is a real property of the curve and not an artefact of our
digitisation.

One further point that deserves saying directly: your figure marks four
epistemic regimes of a single curve — future, data-grounded, CC-calibrated only,
beyond calibration — and marks the end of the calibrated range explicitly. That
is more disclosure than most published expansion-history figures carry, and it
made the audit straightforward.

**4. The main positive result is a clean separation of three levels.**

    local MULTING force  →  [ missing covariant or coarse-grained bridge ]  →  H(z)

Levels one and three are in reasonable shape. The whole remaining theoretical
problem sits in the bracket, and it is now a much narrower problem than it was.

**5. A concrete local prediction survives, and it is testable now.**

Writing the normalised force as

    F(r) ∝ -1/r^2 + ℓ_d/r^3 - ℓ_q^2/r^4

an intermediate repulsive interval exists **only** when ℓ_d > 2 ℓ_q. Equivalently,

    ℓ_q ≥ ℓ_d / 2

is the exact condition for the force to remain attractive at every separation.
This is a relation between the two length scales, not a fit, and it can be
confronted with cluster dynamics, pairwise velocities, lensing, and
kSZ-conditioned samples. We have made a first pass against a catalogue of 1742
X-ray clusters; the constraint it yields is weak, and the force law passes it.

---

Our present reading is therefore positive and, I hope, precise:

- the local MULTING interaction remains open and testable;
- the later H(z) curve is a distinct object, genuinely different in shape from
  ΛCDM;
- the direct pair-energy explanation of cosmic acceleration is insufficient;
- what remains is to specify the sector, or the averaging rule, that carries the
  local interaction into a cosmological background.

We are preparing a compact technical memorandum with the equations, the
calibrated curve extraction, the provenance audit, and the registered negative
results.

Two points in it are yours to set, and I do not want to guess at them. Unless you
tell us otherwise, we will record them as follows:

- **the orange curve** as an illustrative, calibration-marked expansion history
  whose generating procedure is not published — not as a forward prediction;
- **the effective energy** behind it as carried by an unspecified sector, since
  the pair-interaction energy itself is now excluded as its source.

If either default misstates your intent, a single line correcting it is all we
need, whenever it is convenient. If both are right, nothing is required and we
will proceed on them.

With respect,

Sergey Boyko
ORCID 0009-0009-2178-5701
Ronin Institute

---

## Attachment package (six items, nothing more)

| # | item | source |
|---|---|---|
| 1 | one-page summary of the four results | this letter, condensed |
| 2 | the two-curve figure with the positive control marked | our extraction |
| 3 | the Table A1 vs curve divergence table | `CERT_C5B_figure3.md` |
| 4 | `w = n/3` with its scope of validity | `CERT_C2_C3.md` |
| 5 | the three-level diagram `F → U → [bridge] → H(z)` | new, one panel |
| 6 | the local prediction `ℓ_d > 2 ℓ_q` | `FINDING_cluster_pair_sign_constraint.md` |

**Excluded from the package, deliberately:** the per-service supplementary
transcripts and any table derived from them. They are unpublished
author-provided material and are gitignored under this repository's
publication-hygiene policy; only aggregate observations may be reported, and
§3 above reports only those.

## Notes on the draft

- **Form of address** is fixed by prior instruction: "Dear Dr. Buckholtz" and
  "With respect" / "Respectfully". Never "Tom", never "Dear Doctor".
- **The generating tool is not mentioned.** We know it from the file's metadata;
  saying so reads as inspection of his working files and buys nothing the phrase
  "separate object with its own provenance" does not already carry.
- **The two open points are written as defaults, not questions.** A correspondent
  who does not answer questions will often correct a statement. The letter works
  if he says nothing and improves if he replies.
- **Credit is specific, not general.** The praise in §3 names an actual property
  of his figure that is genuinely better practice than Table A1 carried.
