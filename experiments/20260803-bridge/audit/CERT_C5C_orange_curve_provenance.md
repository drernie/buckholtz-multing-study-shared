# Certificate C5C — provenance of the orange curve

**Artifact ID (permanent, replaces "Figure 3"):**

```
ARTIFACT_EMAIL_2026-08-02_MULTING_INTRO_V6
  file      multing_intro_figure_v6.pdf
  created   2026-07-30 18:09:58 UTC   (PDF creationDate)
  received  2026-08-02 16:01 local     (downloaded twice, one minute apart)
  location  outside the repository
```

**Verdict: `UNPUBLISHED_NON_IDENTIFIABLE_ARTIFACT`** — one targeted pass, stop
condition met. Three generative hypotheses excluded, one new one opened.

**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive

---

## 1. The tool is identified

```
creator   : Matplotlib v3.10.8, https://matplotlib.org
producer  : Matplotlib pdf backend v3.10.8
fonts     : DejaVuSans, DejaVuSans-Oblique (Type3)   — matplotlib defaults
XMP       : none      layers: none      embedded files: none
```
`[VERIFIED-METADATA]`

**Consequence: G5 (a conceptual curve drawn by hand) is EXCLUDED.** The figure was
produced by Python code. That code exists, or existed. It is not in this
repository, not in `Downloads`, and no `.py`, `.svg`, `.pptx`, `.xlsx` or
`.nb` source for it was found. `[VERIFIED-SEARCH]`

This does **not** exclude an AI service: a service can emit matplotlib code. It
excludes only free-hand drawing.

## 2. A version chain exists, and the earlier link is legible

`image002.png` (2026-07-21 19:59 local, the inline attachment of the 2026-07-20
message) is the same figure one revision earlier:

| | `image002.png`, 2026-07-20 | `..._v6.pdf`, 2026-07-30 |
|---|---|---|
| CC data | "Real cosmic chronometer data (**31 points**)" | "Cosmic chronometer data (**31 points**)" |
| DESI | "DESI (independent, high-z)" at z = 2.33 | "DESI (independent, z=2.33)" |
| SH0ES | "SH0ES local measurement" | "SH0ES local measurement (z = 0.0233)" |
| z range | −0.1 … 2.4 | −0.2 … 2.4 |
| boundary marked | "calibrated data ends, extrapolation begins" at z ≈ 1.965 | `z=1.965` |
| the curve | "**MULTING (anchored to SH0ES)**" | "MULTING (spotlighted case)" |
| ΛCDM | "ΛCDM (anchored to Planck)" | "ΛCDM, fixed Planck (Ω_m = 0.315)" |

Same construction, refined. The July caption states the anchoring outright:
**the curve is normalised to SH0ES**, the reference to Planck.
`[VERIFIED-SOURCE]`

**A third file, and it is ours, not the author's.**
`multing_hz_audit_publication_diagnostic.pdf` (2026-07-21 16:36 UTC) is this
project's own honest-diagram output — its caption reads *"digitized from the
supplied PNG; its generating equation and training provenance remain
unresolved"* and it uses the repository's **27-point** audit set, not the
author's 31. It must not be cited as evidence about the author's figure.
`[VERIFIED-SOURCE]`

## 3. `z = 1.07` is explained, and it is not physics

The legend gives four line styles for **one** curve:

```
dotted  = future (z < 0)
solid   = data-grounded (0 <= z <= 1.07)
dashed  = CC-calibrated only
dotted  = beyond calibration
```

The four drawn segments tile the range without overlap and join smoothly:

```
seg 0  z=[-0.200,-0.001]  H=[86.5, 73.9]
seg 1  z=[+0.008,+1.064]  H=[73.6,135.9]
seg 2  z=[+1.073,+1.958]  H=[136.6,208.0]     135.9 -> 136.6 across the break
seg 3  z=[+1.967,+2.500]  H=[208.7,247.1]     208.0 -> 208.7 across the break
```

A curvature scan finds **no kink** at either annotated redshift:

```
z = 1.070   |d2H/dz2| local max  4.29  vs median 12.07   ratio 0.4x
z = 1.965   |d2H/dz2| local max 13.42  vs median 12.07   ratio 1.1x
```
`[VERIFIED-EXTRACTION]`

So `z = 1.07` is an **epistemic annotation** — where the author stops calling the
curve data-grounded — not a transition, not a crossing, not `q = 0`. Our earlier
guesses were all wrong: the ΛCDM crossings are at 0.152, 0.461, 2.284 and
`q = 0` is at 0.378. The segmentation is stylistic; one smooth curve underlies it.

**This is to the author's credit and is worth saying plainly:** the figure marks
its own calibration boundary in three places and distinguishes four epistemic
regimes of a single curve. That is more disclosure than Table A1 carried.

## 4. The curve is not any standard expansion history

Fits to the extracted curve, `z >= 0`, 277 points:

| family | free params | rms |
|---|---|---|
| flat ΛCDM | 2 | **3.99 %** |
| flat wCDM | 3 | 3.72 % |
| ΛCDM + curvature | 3 | 3.42 % (at Ω_k = 0.80) |
| CPL `w₀–wₐ` | 4 | 3.55 % |
| `H² = A(1+z)³ + B(1+z)ⁿ` | 3 | 3.72 % |
| `w = −1 + A tanh((z−z_t)/Δ)` — the form in ChatGPT's transcript | 5 | 1.06 % at Ω_m = −173 (degenerate) |
| `H = H_ΛCDM · (1 + δ·g(z))`, three choices of `g` | 4 | 2.8–3.1 %, all at degenerate parameters |

**The control that makes this a result rather than a fitting failure.** The same
two-parameter flat-ΛCDM fit, same code, applied to the **blue** curve on the same
figure:

```
curve     flat LCDM (2p)     verdict
blue           0.0019 %      identified by a 2-param cosmology
orange         3.9920 %      NOT identified by any cosmology tried
```

A 2000-fold asymmetry, with the extraction validated to two parts in a hundred
thousand on a curve of known identity. `[VERIFIED-EXTRACTION]`

**A test we ran and are discarding.** A cubic spline with 3 interior knots fits
the orange curve to 0.046 %. That looked like evidence for graphical
interpolation until the control was run: the same spline fits the *blue* curve to
0.0033 %, and the blue curve is ΛCDM. Spline flexibility discriminates nothing
here, so it is not offered as evidence. Only the left column above is.

## 5. What this does and does not mean

**It does not mean the curve is fabricated.** "No FLRW fluid model reproduces it"
is precisely what a genuine non-FLRW calculation would look like. MULTING claims
a modified gravitational response; a curve that resists Ω_m/w/w₀–wₐ fitting is
consistent with that claim, not evidence against it. This is the opposite of the
Table A1 situation, where the construction was identified *as* a fit.

**It does not mean the curve is correct either.** A hand-shaped smooth curve
would also resist those fits. The two hypotheses are not separated by anything in
the artifact, and no amount of further curve-fitting will separate them — that is
the stop condition, and it is met.

**What is genuinely new:** the curve is anchored to SH0ES at `z = 0`
(`H(0) = 73.9` extracted, SH0ES 73.04) and falls **below** Planck ΛCDM by
`z ≈ 2.3` — ratio range 0.980–1.088, crossing unity. Whatever generated it, it
has the shape of a Hubble-tension construction: high locally, standard-or-lower
at depth.

## 6. Status against the frozen four-way

```
REPRODUCIBLE_OPERATOR                 no — code existed (matplotlib) but is not held
PARAMETRIC_CONSTRUCTION               no — no parametrisation found within 5 params
GRAPHICAL_INTERPOLATION               not established; the test that would show it
                                      failed its own control
UNPUBLISHED_NON_IDENTIFIABLE_ARTIFACT YES

positively EXCLUDED this pass:  hand-drawn (G5) · rendering of Table A1 ·
                                rescaled ΛCDM · standard FLRW fluid cosmology
```

## 7. The question to the author, now one line

Everything above narrows an open-ended request for a model down to a
yes/no existence check about one file:

> Does the Python script that produced `multing_intro_figure_v6.pdf`
> (matplotlib, 2026-07-30) still exist?

Not to be sent without approval. Recorded here so the question is ready.

---

## Record corrections this certificate forces

| record | correction |
|---|---|
| every use of "Figure 3" / "the published figure" | → `ARTIFACT_EMAIL_2026-08-02_MULTING_INTRO_V6` |
| "created after the preprint" | → created **2026-07-30**, one revision after the 2026-07-20 chart |
| `z = 1.07` treated as a physical feature | → calibration-regime boundary, no kink present |
| `multing_hz_audit_publication_diagnostic.pdf` | → **ours**, 27-point set; never cite as the author's |
