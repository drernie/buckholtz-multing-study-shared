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

## The calibrated comparison — run, with the extraction validated first

A first quick extraction gave 9.84 % rms and was discarded as untrustworthy: it
took every polyline over 40 points and could not be shown to have isolated the
MULTING curve. The repository's digitiser selects **by colour** instead — orange
for MULTING at width 2.0, blue for ΛCDM, dark fill for the data markers. Run
that way:

```
MULTING (orange) : 4 segments, 300 points, z in [-0.200, 2.500]
LCDM    (blue)   : 37 points
data markers     : 32
```

### The extraction validates itself

Fitting flat ΛCDM to the **blue** curve returns

```
H0 = 67.37   Omega_m = 0.3152   rms = 0.002 %
```

That is Planck 2018 recovered to two parts in a hundred thousand. The digitiser
reproduces a known curve essentially exactly, so a large mismatch elsewhere is a
property of the curves and not of the extraction. `[VERIFIED-EXTRACTION]`

### Result: the figure does not render Table A1

| `z` | figure | Table A1 `H_MULT` | deviation |
|---|---|---|---|
| 0.00 | 73.9 | 73.0 | +1.2 % |
| 0.40 | 83.0 | 83.1 | −0.1 % |
| 0.65 | 101.2 | 91.4 | **+10.7 %** |
| 1.00 | 130.4 | 104.2 | **+25.2 %** |
| 1.50 | 172.1 | 126.5 | **+36.1 %** |
| 2.10 | 218.6 | 151.8 | **+44.0 %** |

```
figure vs H_MULT  : rms 21.1 %      figure vs H_obs   : rms 21.7 %
figure vs H_w_eff : rms 21.4 %      figure vs H_FLRW  : rms 29.3 %
```

Not noise: agreement within a few per cent below `z = 0.4`, then a monotone
divergence to 44 %. **No Table A1 column is rendered by this figure.**

### Which of the two is physically sensible

The divergence is one-sided, and the side matters.

| `z` | figure | Table A1 `H_MULT` | Planck ΛCDM | real cosmic chronometers |
|---|---|---|---|---|
| 1.00 | 130.4 | 104.2 | 120.6 | 105 ± 12 @ 0.78, 125 ± 17 @ 0.88 |
| 1.50 | 172.1 | 126.5 | 159.6 | 168 ± 17 @ 1.30, 160 ± 34 @ 1.36 |
| 2.10 | 218.6 | 151.8 | 213.8 | 186 ± 50 @ 1.97 |

The figure tracks the physical expansion history; Table A1 runs low. And Table
A1's own **"H-data" column** does not match the cosmic-chronometer compilation
above `z = 1`:

```
z = 1.00   Table A1 H-data = 105.0   real CC mean = 121.5   -13.6 %
z = 1.50   Table A1 H-data = 125.0   real CC mean = 159.0   -21.4 %
z = 2.10   Table A1 H-data = 150.0   real CC mean = 186.5   -19.6 %
```

So the two artefacts rest on **different observations**. Table A1's are
service-generated and drift low at high redshift; the figure's region matches
measured data. That is a second, independent reason they are separate
constructions.

### What the plotted MULTING curve is not

Fitting flat ΛCDM to the **orange** curve gives `H0 = 68.14`, `Ω_m = 0.3401` at
**3.44 % rms** — a poor fit by the standard the blue curve sets. And the ratio
between the two plotted curves varies across the range:

```
MULTING / LCDM :  mean 1.0424   sd 0.0354   min 0.9804   max 1.0878
spread 10.3 % — and it crosses unity
```

**The orange curve is therefore not ΛCDM rescaled to a different `H₀`.** It is a
genuinely different shape that crosses below ΛCDM at some redshift. Whatever
produced it, it is neither Table A1 nor a re-anchored ΛCDM.

## Status against the frozen options

```
REPRODUCIBLE_OPERATOR              not established — no operator is given anywhere
DATA_CONDITIONED_CONSTRUCTION      not established for this object
GRAPHICAL_INTERPOLATION of Table A1  EXCLUDED  <-- positive result, 21 % rms
                                                 with a validated extraction
NON_IDENTIFIABLE                   YES, as things stand
```

**Verdict: `NON_IDENTIFIABLE`, with one hypothesis positively excluded.** The
figure is not a plot of Table A1, and it is not a rescaled ΛCDM. Its operator
remains unidentified, and nothing in the repository or the published preprint
identifies it.

This is a stronger position than before: the space of candidate origins has been
narrowed by two, and the exclusion rests on an extraction validated to 0.002 %
against a known curve.

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
