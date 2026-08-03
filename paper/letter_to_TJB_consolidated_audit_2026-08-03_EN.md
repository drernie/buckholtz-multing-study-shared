# Letter to Dr. Buckholtz — consolidated H(z) audit

**Status: DRAFT. Not sent. The user sends, not the assistant.**
Every number below traces to a certificate in `experiments/20260803-bridge/audit/`.
Detailed derivations, the full nine-row divergence table, and the verification
counts belong in the technical memorandum, not in this letter — see "What moved
out" below.

---

**Subject:** MULTING H(z) — consolidated audit, constructive result

Dear Dr. Buckholtz,

We have finished several independent reconstruction and falsification passes
over the MULTING H(z) material. I am writing to hand you the result rather than
a list of questions.

The outcome is constructive. The analysis does not reject the local MULTING
force law. It separates what is already reproducible from the one part that
still needs a physical bridge, and it closes off one route that would otherwise
absorb a great deal of time.

**1. The local interaction's radial dependence reconstructs uniquely, up to an additive constant.**

From F(r,z) = -A2/r² + A3/r³ - A4/r⁴, the r-dependent part of the potential
follows without ambiguity:

    U(r,z) = -A2/r + A3/(2r²) - A4/(3r³) + C(z)

where C(z) is the ordinary additive freedom that leaves the local force
unchanged. The local force law remains a testable physical hypothesis, and
nothing in our work rejects it.

**2. One specific cosmological bridge — the simplest one — is not sufficient.**

For a pure inverse-power potential U ∝ r⁻ⁿ under the standard configurational
pair-fluid mapping, Euler's identity applied pair by pair, before any averaging,
gives p = (n/3)ρ, so the three MULTING terms correspond to w = 1/3, 2/3, 1 within
that mapping — none negative. This specific reading of pair-interaction energy
cannot by itself explain late-time acceleration. It says nothing against a
covariant medium, a polarisation sector, or explicit cosmological averaging, and
we have registered it as a negative result so neither of us spends further
effort on this one route.

**3. Table A1 and the later H(z) curve are two different objects.**

You flagged Table A1's status yourself — that the responses were obtained from
an online service and are "not necessarily trustworthy or directly useful." We
worked out the numerical consequence: β_d and β_q were selected by minimising
deviation from the H-data, with the curve normalised to the observed H0 at z=0.
Table A1 is best read as an exploratory, data-conditioned calibration rather
than an independent prediction — a statement about procedure, not about the
model.

The later orange curve is a separate object, not a plot of Table A1: the two
diverge to 44 % by z ≈ 2.1 — past the CC-calibration boundary your own figure
marks at z = 1.965; within that boundary the largest divergence is 36 % at
z = 1.5 — rms 21 % overall (detail on the attached figure), and the curve is
not ΛCDM re-anchored to a different H0 either. Below z = 0.4 the two
differ by a few per cent and change sign; above z = 0.4 the difference becomes
one-sided and grows systematically — a real feature of the curves, confirmed by
a positive control: fitting the same figure's blue reference curve recovers flat
ΛCDM to 0.002 % rms.

**4. The separation this leaves is the main result.**

    local MULTING force  →  [ unidentified physical bridge ]  →  H(z)

The first stage is explicit. The last stage is a numerical target curve whose
generating procedure is not identified in the material available to us. The
open problem sits entirely in the middle, and it is now considerably narrower
than it was.

**5. One local, testable prediction survives.**

Writing F(r) ∝ -1/r² + ℓ_d/r³ - ℓ_q²/r⁴, an intermediate repulsive interval
exists only when ℓ_d > 2ℓ_q — equivalently, ℓ_q ≥ ℓ_d/2 is the exact condition
for the force to stay attractive at every separation. A preliminary pass against
a catalogue of 1742 X-ray clusters found no overt contradiction, though this is
a geometric screening, not yet a statistical constraint on the parameters.

---

Our present reading: the local MULTING interaction remains open and testable;
the later H(z) curve is a genuinely distinct object; the standard pair-fluid
reading of pair-interaction energy is not sufficient on its own; what remains is
to identify the sector, or averaging rule, that carries the local interaction
into a cosmological background.

We are preparing a technical memorandum with the full equations, the calibrated
extraction, and the registered negative results. In it we will describe the
later curve as a separate, code-generated artifact whose generating procedure is
not identified in the material available to us, and we will not classify it as an independent prediction without
further basis. If you have more to say about it, a line would be very welcome —
nothing here depends on a reply.

One thing is worth saying plainly, apart from the results above. The parts of
this we could audit cleanly — the caveat you yourself attached to Table A1, the
calibration boundaries marked explicitly on the later figure — were auditable
precisely because they were documented rather than smoothed over. That made
this a constructive audit rather than an adversarial one, and it is worth
acknowledging directly.

With respect,

Sergey Boyko
ORCID 0009-0009-2178-5701
Ronin Institute

---

## Attachment package (two items, plus this letter)

| # | item | source |
|---|---|---|
| 1 | one-page summary — carries `w = n/3`, the three-level diagram, and `ℓ_d > 2ℓ_q` in one place | `onepager_for_TJB_2026-08-03_EN.md` |
| 2 | the two-curve figure with the positive control and the full divergence, annotated | our extraction |

An earlier draft of this table listed the `w=n/3` excerpt, the bridge diagram,
and the local-prediction excerpt as three further separate files. They were
never built, and building them now would be redundant: all three already sit
inline in item 1. Three pieces (letter, one-pager, figure) is a package a
correspondent who rarely replies can actually get through; five smaller files
saying the same things is not.

**Excluded from the package, deliberately:** the per-service supplementary
transcripts and any table derived from them. They are unpublished
author-provided material and are gitignored under this repository's
publication-hygiene policy; only aggregate observations may be reported, and
§3 above reports only those.

## What moved out, and why

Six precision corrections were applied to the working draft before this
version, each because the earlier wording claimed slightly more than the
evidence supports:

1. **The potential's additive constant.** "Reconstructs without ambiguity" was
   true only for the r-dependent part; C(z) is real freedom, now stated.
2. **Low-z scatter is not attributed to digitisation noise.** The positive
   control put our own extraction error at 0.002 %, two orders below the
   several-per-cent scatter below z = 0.4 — calling it "noise" overclaimed a
   cause we hadn't established. Now stated as a plain, unexplained fact.
3. **"First and third levels in reasonable shape" overgeneralised.** The third
   level — the later curve — has an unidentified generating operator; only the
   first level (the force law itself) is explicit. The diagram's caption now
   says so.
4. **The cluster-catalogue test is a screening, not a likelihood fit.** "The
   force law passes it" implied a statistical test we have not run.
5. **The two "default" classifications assumed too much.** Calling the later
   curve "illustrative" by default, absent objection, stated a status we
   haven't established. The letter now states only what is verified — code
   output, unpublished, operator unidentified — and drops the "silence =
   agreement" framing entirely.
6. **"Pair-interaction energy excluded as a source" was too broad.** Only the
   standard configurational pair-fluid mapping is closed. The letter and the
   closing summary now both say "this specific mapping," not "the source."

Also moved out, for length rather than accuracy: the 360-configuration
verification count and the 7×10⁻¹⁶ precision figure, and the full nine-row
Table A1 comparison — all three now live in the memorandum and the figure, not
in the letter body. The letter kept one number per result, not the full
derivation.

## Notes on the draft

- **Form of address** is fixed by prior instruction: "Dear Dr. Buckholtz" and
  "With respect". Never "Tom", never "Dear Doctor".
- **The generating tool is not mentioned.** We know it from the file's
  metadata; saying so reads as inspection of his working files.
- **The closing paragraph of respect is new and deliberate.** It is specific,
  not generic — it credits a concrete, verified practice (self-flagged
  limitations on Table A1, explicit calibration marks on the later figure), not
  the physics itself, which remains open. It is placed last, immediately before
  the signature, so the letter's final substance is about him rather than about
  the sender.
