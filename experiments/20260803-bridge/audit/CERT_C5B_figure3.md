# Certificate C5B — the provenance of "Figure 3"

**Verdict: the premise of the question is wrong.**
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive

**Standing instruction observed:** no conclusion from C1 or C5A is transferred
here. Everything below rests on evidence about this object alone.

---

## The finding

**There is no Figure 3 in the published v6 preprint. There are no figures at
all.**

```
occurrences of "figure" (case-insensitive) in
  buckholtz_preprints202511.0598.v6_pymupdf-clean.md   :  0
  buckholtz_supplementary202511.0598.v6.md             :  0
```

Both counts are zero. `[VERIFIED-GREP]`

The object this project has been calling "Figure 3", and building an entire
bridge programme to reproduce, is a **different artefact**: an email attachment,
`multing_intro_figure_v6 (1).pdf`, received 2026-08-02, held outside the
repository. Our own analysis scripts record the path:

```
scripts/a1_digitize_tjb_figure.py:28   PDF = C:\Users\serge\Downloads\multing_intro_figure_v6 (1).pdf
scripts/a2_shape_only_test.py:35       (same)
scripts/b1_statefinder.py:29           (same)
```

Three analyses — digitisation, shape-only test, statefinder — all targeted an
email attachment while the reasoning around them spoke of "the published Figure
3". `[VERIFIED-GREP]`

## Why this matters more than a naming slip

Table A1 and the emailed figure are **different objects with different
provenance chains**:

| | Table A1 | the emailed figure |
|---|---|---|
| status | published, preprint v6, p. 39 | unpublished email attachment |
| date | preprint, posted 21 May 2026 | 2 August 2026 |
| redshift range | `z = 0 … 8.5` | `z = −0.2 … 2.4`, including a future branch |
| provenance | stated in the caption | **not established** |

C5A settled Table A1. **It settles nothing about this figure**, and the fact that
the two share a subject does not license carrying one verdict to the other. That
is precisely the transfer the standing instruction forbids, and until now the
project had been making it implicitly by calling the attachment "Figure 3".

## What the figure itself shows

`[VERIFIED-EXTRACTION]` from the PDF's own text layer:

- axis labels `redshift z` and `H(z) [km/s/Mpc]`
- redshift axis spanning **−0.2 to 2.4** — so it includes `z < 0`
- three annotated redshifts: `z=0`, `z=1.07`, `z=1.965`
- the legend line: **"MULTING (spotlighted case), dotted = future (z < 0)"**

`z = 1.965` is the upper limit of the cosmic-chronometer compilation in this
repository. The figure therefore marks the edge of the observational range
explicitly, which is to the author's credit and was the basis of our earlier
honest-diagram work.

## An attempted test, and why its result is not reported as a finding

The natural question is whether the plotted MULTING curve is a rendering of Table
A1's `H_MULT` column. A quick extraction of the PDF's vector paths, compared
against Table A1 over the nine rows inside the figure's redshift range, gave a
best match of **9.84 % rms** — no column tracked within 2 %.

**That result is not reported as evidence, because the extraction is not good
enough to carry it.** It took every polyline longer than 40 points and sorted by
x; among the six such paths are almost certainly axis furniture, gridlines and
error bars, and there is no guarantee the MULTING curve was among the ones
compared. A 10 % mismatch is equally consistent with "different construction" and
with "compared the wrong polyline".

The repository already contains a proper digitiser — `a1_digitize_tjb_figure.py`,
with a recorded calibration error of 0.03 % — and the correct next step is to run
the comparison through it rather than through a five-line reimplementation.

## Status against the frozen options

```
REPRODUCIBLE_OPERATOR              not established
DATA_CONDITIONED_CONSTRUCTION      not established
GRAPHICAL_INTERPOLATION            not established
NON_IDENTIFIABLE                   not established
```

**None of the four applies yet.** The prior question — *which object are we
auditing* — had not been answered, and answering it is this certificate's whole
content. The four-way status determination remains open and now has a
well-defined subject.

## What is established

1. The v6 preprint contains no figures. `[VERIFIED-GREP]`
2. The audited object is an unpublished email attachment of 2026-08-02, outside
   the repository. `[VERIFIED-GREP]` on our own scripts' recorded paths.
3. It spans `z ∈ [−0.2, 2.4]` with a labelled future branch, and marks
   `z = 1.965`. `[VERIFIED-EXTRACTION]`
4. It is not the same object as Table A1, and no verdict transfers between them.

## What is not established

Whether the figure's curve derives from Table A1, from a separate computation,
from an interpolation, or from something else. Whether it was produced by an AI
service. Whether the same fitted `β` values underlie it. All of these require
running the proper digitiser and, for the provenance question, evidence that does
not exist in the repository.

## Consequences for the record

Every earlier result derived from this object — the A1 digitisation, the A2
shape-only test, the B1 statefinder, the B2 extrapolation envelope, and the
honest-diagram script — characterises **an unpublished 2026-08-02 email
attachment**, not a published figure. Their conclusions are unaffected; their
subject line must be corrected wherever it says "Figure 3" or "the published
figure".

## Next action

Run `a1_digitize_tjb_figure.py`'s calibrated extraction against
`data/table_a1_source_verified.csv` and settle whether the curve is a rendering
of the table. That is a determinate question with existing tooling, and it is the
last cheap step before the four-way status can be assigned.
