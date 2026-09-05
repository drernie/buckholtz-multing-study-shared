# FINDING E3 — one technique (kSZ) genuinely escapes the SPECIFIC
# circularity TJB diagnosed in its velocity channel, but does not
# demonstrate a working fix; a second (redshift drift), first proposed
# as a counterexample, does NOT apply and was withdrawn after a Step 8a
# skeptic pass

**CORRECTION (same day, before this file was ever presented as
settled):** this file's own first draft claimed, more confidently, that
"TJB's blanket claim... appears to be somewhat stronger than the
literature supports" based on two candidate techniques. A Step 8a
skeptic pass (context-blind, claim + literature only) found this
overstated: redshift drift is not a counterexample at all (wrong
observable, wrong regime — see Verdict below) and should be dropped;
kSZ is a real, scale-matched structural exception in its velocity
channel specifically, but current kSZ methodology still assumes a
fixed cosmology elsewhere in its own pipeline, so it does not
demonstrate that TJB's "not fixable" conclusion is wrong. The title and
sections below are corrected to match the Verdict, not the original,
more confident framing — left visible per this project's no-silent-
correction discipline rather than quietly rewritten.

**Date:** 2026-09-06
**Continues:** `FINDING_E2` (the `H₀,anchor` circularity itself).
Third of the 5-step autonomous follow-up.

## The specific claim being tested

`FINDING_E2` quoted TJB's own conclusion in Section IV.M: *"We do not
think this is a fixable methodology choice: a genuinely non-circular
velocity-and-distance pair for nearby clusters would require direct,
geometric distance measurements combined with spectroscopic
velocities — which is the distance-ladder methodology already used by
SH0ES. Attempting this ourselves would reconstruct one side of the
existing tension, not provide an independent third answer."*

This is a strong, general claim: that the ONLY way to avoid the
specific circularity he found (peculiar-velocity surveys already
assume an `H₀` to subtract the Hubble flow before the peculiar velocity
can be extracted) is to redo SH0ES's own distance-ladder approach.
Given `FINDING_E1`'s own literature-grounding step surfaced a mature
field of techniques built specifically to avoid exactly this class of
circularity, this specific, falsifiable sub-claim was checked directly.

## Method

Real `arxiv` searches (fetched and read this session, not from memory):
"redshift drift Sandage-Loeb test direct measurement expansion rate
without distance ladder"; "kinematic Sunyaev-Zeldovich peculiar
velocity galaxy clusters measurement without assuming Hubble flow";
"gravitational wave standard sirens Hubble constant independent
distance ladder".

## Initial result (before the skeptic pass — see Verdict below for
## what actually survived)

Two candidate techniques were initially proposed as possible
counterexamples:

1. **Redshift drift / Sandage-Loeb test.** `[VERIFIED-arXiv:astro-ph/
   0701433]` (Corasaniti, Huterer & Melchiorri, 2007) and multiple
   follow-ups (2012-2026, still active): a direct measurement of the
   *time evolution* of a fixed comoving source's redshift, taken at two
   widely-separated epochs (years to decades apart). This measures
   `ȧ/a`-type information as a genuinely kinematic signal — it never
   needs to assume an `H₀` to subtract a Hubble flow from anything,
   because it isn't built from a redshift-to-distance conversion at
   all; it directly tracks how one source's own redshift changes over
   real, elapsed time. This is structurally different from — not a
   variant of — both the SH0ES distance ladder and TJB's own attempted
   peculiar-velocity-survey route.
2. **Kinematic Sunyaev-Zeldovich effect (kSZ).** `[VERIFIED-arXiv:
   astro-ph/9507077]` (Haehnelt & Tegmark, 1995) and a substantial
   following literature (2002-2017+): infers a galaxy cluster's
   peculiar velocity from the **Doppler shift of CMB photons Compton-
   scattered by the cluster's own hot gas** — a physically distinct
   effect from redshift-based peculiar-velocity surveys. Because it
   does not start from "redshift minus an assumed Hubble-flow
   contribution," it does not appear to inherit the same circularity
   TJB diagnosed. **Real, substantive caveats found in the same
   literature, stated honestly:** kSZ signals are small, require
   precise separation from the (much larger) thermal SZ effect, and
   `[VERIFIED-arXiv:astro-ph/0208308]` (Nagai, Kravtsov & Kosowsky,
   2002) shows internal cluster gas flows can bias the inferred
   peculiar velocity — this is a real, difficult measurement, not an
   easy substitute.

**A third technique found (gravitational-wave standard sirens,
`[VERIFIED-arXiv:1710.05835]`, the LIGO/Virgo GW170817 measurement) is
a genuinely independent, non-SH0ES route to `H₀` itself** — its own
distance calibration comes from GR's own waveform physics, not a
Cepheid-based distance ladder — but it measures `H₀` in the standard
cosmological (luminosity-distance-vs-redshift) sense, for a sample of
compact-binary-merger host galaxies, not specifically the `ṡ₀/s₀` ratio
for "typical nodes" at MULTING's own `~30-60 Mpc` cluster separations.
Relevant as evidence that non-SH0ES-methodology routes to `H₀` exist at
all, less directly relevant as a plug-in fix for `H₀,anchor` specifically.

## Verdict — WEAKENED after a Step 8a skeptic pass (context-blind,
## claim + literature only), corrected here rather than presented as
## the original, more confident reading

The skeptic ran its own independent `arxiv` checks (not accepting the
sources above at face value) and found:

**Redshift drift is FALSIFIED as a counterexample to TJB's claim, not
merely weak support for it.** Every substantive paper on the technique
(`[VERIFIED-arXiv:astro-ph/0701433]` and follow-ups) frames it as a
probe of the "redshift desert" — quasar Lyman-α sources at `z~2-5` —
and, more decisively, `[VERIFIED-arXiv:1911.01467]` (Inoue, Komatsu et
al.) treats peculiar velocity as a **contaminating systematic to be
corrected OUT of the redshift-drift signal**, not as the target
observable. This is the opposite of what `H₀,anchor` needs. Redshift
drift targets a different observable, different population, and
different physical regime than TJB's own `~30-60 Mpc` cluster-pairwise
construction — it should be dropped from this argument, not merely
labeled "impractical for now."

**kSZ is a genuinely closer, scale-matched candidate, but does not
close the loop.** The skeptic found real, current (2026) kSZ pairwise-
velocity science (`[VERIFIED-arXiv:2604.14327]`, ACT collaboration)
operating at `30-230 Mpc` halo separations — directly overlapping
`H₀,anchor`'s own needed scale, a real point in this technique's favor.
The velocity-extraction channel genuinely is structurally different
from redshift-minus-Hubble-flow, as originally claimed. **But** current
kSZ practice **assumes a fixed fiducial `H₀`/ΛCDM background** to
convert redshifts and angles into the physical separations it reports,
and to calibrate the mass-observable relations used to interpret the
kSZ decrement — the circularity is **relocated from the velocity side
to the separation/calibration side of the same ratio**, not eliminated.
No current kSZ pairwise-velocity paper the skeptic found derives `H₀`
independently; all condition on an assumed one to test structure growth
instead.

**Corrected, narrower conclusion:** TJB's own scoping ("a genuinely
non-circular velocity-and-distance pair **for nearby clusters**") is
specific, and redshift drift was never a candidate for that scope at
all — citing it was an apples-to-oranges association, now withdrawn.
kSZ is the one real, scale-matched, structurally-distinct exception
worth naming — its velocity channel genuinely escapes the SPECIFIC
mechanism TJB diagnosed — but current kSZ methodology has not been
shown to escape assumed-cosmology dependence generally, only to move
it elsewhere in the same pipeline. **TJB's "not fixable" verdict is not
established as an overstatement by this finding after all** — the
honest result is narrower: kSZ's velocity channel is a genuine
structural exception worth flagging as unexamined, not a demonstrated
or even plausible working fix.

## What this does NOT establish

1. Does not demonstrate a working, non-circular measurement of
   `H₀,anchor` for MULTING's own construction — only that the general
   class of "genuinely independent kinematic technique" is broader than
   TJB's own text suggests, with real, unresolved practical caveats.
2. Does not diminish the value of TJB's own diagnosis — the specific
   circularity he found in the peculiar-velocity-survey route is real
   and correctly identified; this finding only questions the
   generality of his own "not fixable" conclusion, not the underlying
   analysis.
3. `NO_AUTHOR_ERROR` — this is a literature-grounded observation about
   general technique availability, not a claim that this project has
   solved or could easily solve `H₀,anchor`'s circularity for MULTING.
