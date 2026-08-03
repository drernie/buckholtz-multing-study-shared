# Certificate C1 — provenance of Table A1

**Verdict: PASS** (criterion frozen 2026-08-03 before the run)
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive

---

## The claim, as frozen

> The material available to us does not contain a deterministic, published,
> reproducible operator `F ↦ H` that produced Table A1. The table is presented in
> the source as the response of an online AI service to a prompt.

**PASS condition, fixed in advance:** an independent reader, given only the
source pages and no output of ours, states that the table is an AI service's
response, and finds no separate published calculation.

## Path B — independence conditions met

| condition | met |
|---|---|
| reader given only the source excerpt, no Path A output | yes |
| reader **not told** that "AI" was the suspected provenance | yes |
| reader given no repository access, no web | yes |
| reader asked four open questions, not asked to confirm a hypothesis | yes |

## Verdict returned

`NO_REPRODUCIBLE_OPERATOR_IN_THIS_EXCERPT` — the excerpt contains no rule
yielding the H-MULT column, and states affirmatively what the numbers are
instead.

## What Path B found that Path A had not

The independent reader surfaced four passages we had not read, all verified
against the source by grep before acceptance (`[VERIFIED-SOURCE]`, lines
2514–2518 and elsewhere):

> "Supplemental Material [251] provides transcripts of **three attempts** to use
> AI-based services."

> "The services **disagreed somewhat** regarding observed values of H(z), the
> Hubble parameter."

> "Disagreements regarding values, that the services suggested, **for βd and βq
> were noticeable**."

> "Disagreements between values, **calculated via MULTING**, for H(z) **were
> noticeable**."

> "AI-based services make mistakes. Users of AI-based services make mistakes."

**Why this matters more than the original finding.** Three services, given the
same model name, produced noticeably different `β_d`, `β_q` *and* noticeably
different `H(z)`. The H-MULT column is therefore not determined by MULTING; it is
determined by which service was asked. The author states this himself.

This independently corroborates the project's own earlier BRAI result — a spread
of 5.8× in `β_d` and 95× in `β_q` across three AI services — which was measured
numerically. The source now says the same thing in words.

## Two further items from Path B

**A self-referential definition in the caption.** "Regarding σ_MULT, the prompt
asked for the number of observational standard deviations that associates with
σ_MULT minus the nominal value of H-data" — σ_MULT defined via σ_MULT. Reading it
as "H-MULT minus…", by analogy with the σ_FLRW sentence one line above, checks
out arithmetically: `(70.2 − 69.0)/3.0 = 0.400` against the printed `0.4`.
Verified. Note this reproduces σ_MULT *from* H-MULT; it does not reproduce
H-MULT.

**An open question we had not isolated, and should have.** The excerpt states
that the `w_eff` prompt supplied H-data as input. For H-MULT it says nothing
either way. **Whether the service had the observations in hand when producing the
H-MULT column is unresolved from this excerpt**, and it is exactly the difference
between a prediction and a fit. This is the sharpest remaining question about
Table A1, and it is answerable — Supplemental Material [251] contains the
transcripts.

## Scope — what this certificate does not establish

- Not that no operator existed. The service applied some procedure; we observe
  that it is not published, not identifiable from the table, and not shown to
  follow from the force law.
- Not that the author misrepresented anything. His labelling is accurate and his
  own reliability caveats are stronger than ours.
- Not anything about MULTING's correctness.
- **Not anything about Figure 3**, whose provenance is a separate object with its
  own evidence, and which this excerpt does not cover.
- Not what Supplemental Material [251] or "Step 7 in the Sec. A.1 prompt"
  contain — neither is in the excerpt, and Path B correctly declined to
  speculate.

## Residual ambiguities recorded by Path B

Which service produced the table is unnamed; no date, temperature, seed or run
count is given; the H-data column's own provenance is stated only as "the prompt
asked for results from observations", with the services disagreeing on those
values too; and no admissible range is given for `β_d`, `β_q`.

---

**Next action this certificate implies:** read Supplemental Material [251] to
settle whether H-MULT was produced with the observations in hand. That is a
provenance question with a determinate answer, and it is more informative than
any further modelling.
