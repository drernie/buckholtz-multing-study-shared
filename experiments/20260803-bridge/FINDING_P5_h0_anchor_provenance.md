# P5: H₀-anchor provenance — the primary source checked, and what it does and does not settle

**Date:** 2026-08-10 · plan item P5 · closes the archive's own flagged Result 11
as far as the text of the primary source allows
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Source obtained:** Cen, Bahcall & Gramann 1994, "Velocity Correlations of
Galaxy Clusters", arXiv:astro-ph/9409042 (ApJ Letters, in press) — full text
retrieved and read, PDF archived at
`experiments/20260810-zenodo-archive/refs/cen_bahcall_gramann_1994_astro-ph_9409042.pdf`

---

## What the archive flagged

`Result 11` (the `H₀ ≈ 11 km/s/Mpc` "circularity" finding) combines an
inter-node separation `s₀ ~ 30 Mpc` (Basilakos 2004) with a pairwise cluster
velocity `v₁₂(s₀)` from Cen, Bahcall & Gramann (CBG) 1994's `Ω = 0.3` CDM model,
`H₀_anchor ~ v₁₂(s₀)/s₀`. The archive's own script interpolated between
`v₁₂(5 h⁻¹Mpc) = 714` km/s and zero at `50–75 h⁻¹Mpc`, using two functional
forms, and got `12–19 km/s/Mpc` against the paper's stated `~11` — flagged as
its own only non-passing check, honestly, rather than silently accepted.

## What checking the primary source adds

**`v₁₂(5 h⁻¹Mpc) = 714` km/s for Ω=0.3 CDM is exact, not assumed.** CBG's own
Table 1 tabulates it precisely: `714 km/s`, alongside `ψ_v(5)=-87`,
`σ¹ᴰ₁₂(5)=487`, `σ¹ᴰ₁₂(100)=327`. The archive's anchor value is **[VERIFIED]**
against the primary source, not merely plausible.

**The zero-crossing scale is stated as a range in the source itself,
`r ~ 50–100 h⁻¹Mpc`** (§4.1 and Conclusion 1: *"the random and bulk motions
finally dominate on large scales, r ~ 50–100 h⁻¹Mpc, where v₁₂(r) ~ 0"*). The
archive's two endpoint choices (50 and 75) both sit inside this stated range —
its interpolation was a fair reading of the source's own words, not a guess
outside them.

**`v₁₂(r)` at the specific separation needed, `r = s₀ = 30` Mpc physical
(`= 20.1 h⁻¹Mpc` at CBG's own `h=0.67`), is genuinely not tabulated anywhere in
the text.** The only numeric anchors in Table 1 are at `r = 5` and (for `ψ_v`,
`σ₁₂`) `r = 20, 100 h⁻¹Mpc` — but `v₁₂` itself is tabulated *only* at
`r = 5 h⁻¹Mpc`. The curve at intermediate separations exists solely as **Figure
3**, a plot.

## The one genuine limitation found, and it is honestly reported

Figure 3 (and Figures 1, 2, 4) did not render as extractable graphics through
this PDF pipeline — the pages contain only the caption text, the plotted
curves themselves came through blank. This is very plausibly an artefact of
1994-era PostScript/EPS figures embedded in an old LaTeX-to-PDF conversion, not
evidence the figure is missing from the actual published paper. **Digitising
Figure 3 remains a genuine, unclosed task** — exactly what the archive's own
script said it would require, now confirmed rather than assumed, and now with
a specific obstacle named (the figure needs pulling from a different rendering
path — e.g. the published ApJ Letters PDF, or a dedicated digitisation pass —
not just re-fetching the arXiv text version).

**An attempted independent cross-check does not resolve it either.** Combining
the paper's stated `v₁₂/σ₁₂` ratio behaviour (`√3` at small `r`, decreasing
monotonically to `0` at `r~100 h⁻¹Mpc`) with the two tabulated `σ₁₂` points
(`487` at `r=5`, `327` at `r=100`) and linearly interpolating both gives
`v₁₂(20.1) ~ 670` km/s → `H₀_anchor ~ 22` km/s/Mpc — a *different* number from
the archive's `12–19`, obtained by a differently-arbitrary interpolation
(linear in the ratio and in `σ₁₂`, rather than linear or exponential in `v₁₂`
directly). This is reported to show the honest state of things: **different
reasonable reconstructions from the same primary source's tabulated numbers do
not converge**, which means the range the archive already reported
(`12–19` km/s/Mpc, "same order of magnitude, not a plausible Hubble constant")
is the right level of precision to quote — tightening it further requires the
actual digitised curve, not another interpolation scheme.

## Verdict

```
v12(5 h^-1Mpc) = 714 km/s, Om=0.3 CDM   : VERIFIED against primary source (exact)
Zero-crossing scale                     : VERIFIED as the source's own stated
                                          range, r ~ 50-100 h^-1Mpc
v12(20.1 h^-1Mpc), the number needed    : NOT TABULATED anywhere in the text;
                                          exists only in Figure 3 (a plot)
Figure 3 digitisation                   : ATTEMPTED, blocked -- this PDF
                                          rendering path returns blank figures;
                                          a different source/rendering path
                                          is needed, not re-derivation
Independent cross-check                 : does not converge with the archive's
                                          range (~22 vs 12-19) -- confirms the
                                          uncertainty is real, not an artefact
                                          of the archive's specific method
Archive's Result 11 characterisation    : CONFIRMED accurate and honestly
                                          flagged; its 12-19 km/s/Mpc range
                                          should stand as reported
```

## What this does NOT establish

1. Not a resolution of Result 11 to a single number — the primary source
   simply does not tabulate it, and this was verified by reading the source,
   not assumed from the archive's own disclaimer.
2. The `s₀ ~ 30` Mpc value (Basilakos 2004) was not independently checked here
   — this pass focused entirely on the CBG 1994 side of the combination.
3. Does not touch whether `H₀_anchor ~ v₁₂(s₀)/s₀` is itself the right
   combination to form — that is the paper's own qualitative argument
   ("all three are the same order of magnitude, support the paper's claim that
   this is not a plausible Hubble constant"), not a derivation being audited
   here.

## The remaining concrete step, unblocked by this pass

Obtain Figure 3 through a path that actually renders the curve — the published
ApJ Letters version, or a direct image fetch of the arXiv figure files rather
than the combined PDF — then read `v₁₂(20.1 h⁻¹Mpc)` off it directly. Until
then, `Result 11`'s status stays exactly where the archive left it: an
order-of-magnitude, qualitatively-supported claim, not a verified number.

---

## Round 2 (2026-09-02) — the figure recovered, `v₁₂` read directly, not interpolated

**Root cause found, not just worked around.** Fetched the paper's original
1994 arXiv PostScript source directly (`https://arxiv.org/src/astro-ph/9409042`
— a single `dvips`-produced PS file, confirmed `[VERIFIED-BASH]`), and
inspected the reference PDF's own vector path data (`PyMuPDF.Page.get_drawings()`)
rather than its rendered pixels. **Every stroked path on Figures 1–4's pages
is drawn in pure white** (`color=(1.0,1.0,1.0)`), a systematic stroke-color
bug in whatever pipeline produced the currently-archived PDF from that PS
source — the path *geometry* is completely intact, only the color channel is
wrong. This is a different, more specific diagnosis than Round 1's "did not
render as extractable graphics" — that was the correct symptom, this is the
mechanism. Re-stroking the exact same paths in black recovers Figure 3
exactly (not a redrawing from a guess): `experiments/20260810-zenodo-archive/
refs/cbg1994_figure3_recolored.pdf`.

**Digitized directly from the recovered vector coordinates**, not by eye and
not by pixel-tracing a raster image — script: `experiments/20260810-zenodo-
archive/digitize_figure3_v12.py`. Axis calibration derived from the page's
own tick-mark pixel positions (log-x, linear-y), verified internally
consistent (v=500/1000/1500 ticks land within 0.1–1.4 km/s of their nominal
positions under the fitted calibration).

**Cross-check against the one independently-known anchor** (Round 1's own
`[VERIFIED]` `v₁₂(5 h⁻¹Mpc)=714` km/s, from CBG's own Table 1): digitized
value **713.6 km/s, 0.057% relative error** `[VERIFIED-BASH]`. This
confirms both the calibration and the curve-identity assignment (of the
three plotted models, the digitized curve matching this anchor is `Ω=0.3
CDM` — the model CBG's own text and this paper's own citation both mean by
"LCDM").

**The actual target bin exists in the plotted data** — `r=19.97 h⁻¹Mpc` is
close enough to the needed `r=20.10` (=`s₀·h`=30 Mpc×0.67) that this is a
direct reading, not an interpolation across a gap:

```
v12(r=19.97 h^-1Mpc) = 285.2 km/s   [plotted error range: 273.5-296.9]
H0_anchor = v12/s0 = 285.2/30 = 9.51 km/s/Mpc   (range 9.12-9.90)
```

**Comparison across every estimate this project and the archive have
produced for this same number:**

| source | H0_anchor (km/s/Mpc) |
|---|---|
| paper's own stated value | ~11 |
| archive's Result 11 (3 interpolation methods) | 12.5 – 18.7 |
| this project's Round 1 independent cross-check (v₁₂/σ₁₂ ratio) | ~22 |
| **this Round 2 (direct digitization of the actual curve)** | **9.5 (9.1–9.9)** |

The direct reading is the closest of any reconstruction to the paper's own
stated ~11 — and, unlike every prior estimate, it did not require choosing
an interpolation scheme, because the needed separation happens to sit almost
exactly on one of the paper's own plotted bins.

## Updated verdict

```
Figure 3 digitisation      : DONE. Root cause of the earlier blank render
                              (white-stroke bug in the archived PDF, not a
                              missing/corrupt figure) identified and fixed
                              by re-stroking the original vector paths.
v12(20.1 h^-1Mpc)           : 285.2 km/s [273.5, 296.9] -- direct reading,
                              cross-validated to 0.057% against the one
                              independently-known anchor point
H0_anchor                   : 9.5 km/s/Mpc [9.1, 9.9] -- tightest estimate
                              of this number produced by this project or
                              the archive to date
Circularity finding itself  : UNCHANGED -- Sec. IV.M's own argument (peculiar
                              velocity requires assuming H0 to extract) is
                              untouched by pinning down the number more
                              precisely; a tighter reconstruction of a
                              circular quantity is still circular
```

## What this does NOT establish

1. Does not resolve the underlying circularity the paper itself identifies
   (Sec. IV.M) — this only tightens the *reconstructed number*, which the
   paper's own text says it does not rely on for its main results (`H0_anchor`
   is retained as a free-floating fit parameter precisely because of this).
2. Digitization uncertainty (sub-pixel calibration precision, estimated
   ≲0.2 km/s/Mpc from the tick-matching residuals) is much smaller than the
   plotted N-body statistical error bar (9.1–9.9) — the dominant uncertainty
   remains CBG 1994's own simulation error, not this project's reading of it.
3. Does not check whether `s₀~30 Mpc` (Basilakos 2004) is itself robust —
   Round 1's own scope note (#2) still applies unchanged.

## Artifacts (Round 2)

- `experiments/20260810-zenodo-archive/digitize_figure3_v12.py` — full
  pipeline, reproducible end to end (fetch note, recolor, digitize, cross-
  check, compute).
- `experiments/20260810-zenodo-archive/refs/cbg1994_figure3_recolored.pdf`
  / `.png` — the recovered figure.

## Round 2 addendum — Figures 1, 2, 4 also recovered (same session)

The same white-stroke bug (confirmed, not assumed, per-page) affects
Figures 1, 2, and 4 identically. `recolor_remaining_figures()` in the same
script recovers all three: `cbg1994_figure{1,2,4}_recolored.pdf`/`.png` in
`refs/`. Visually confirmed legible (labels, curves, error bars all
readable) — not yet digitized into numbers, since none currently feed a
project computation the way Figure 3's `v12(r)` does.

**Attempted, not completed:** digitizing Figure 4's `σ12(r)` (Ω=0.3 CDM
curve) as a bonus check, using the same pipeline. Unlike Figure 3, the
cross-check against the one independently-known anchor
(`σ12(5h⁻¹Mpc)=487` km/s, CBG's own Table 1, already `[VERIFIED]` in
Round 1) did **not** cleanly reproduce: the PBI and LCDM curves' error
bars visually cross/touch near `r~5`, and the two candidate drawing paths
share a vertex there — the digitized midpoint (450.3) is 7.5% off the
known 487, well outside Figure 3's 0.057% match. This is a genuine
curve-identification ambiguity at this one separation, not a pipeline
bug (the far point, `r~123`, gives 332.7 vs. the known `σ12(100)=327`,
1.7% off — consistent). **Not reported as a number** — σ12 doesn't feed
the H0_anchor formula directly anyway (only v12 does, already read
cleanly from Figure 3), so there was no need to force a weak result into
the record. Left as an open, low-priority item if a future session wants
it (would need a sturdier curve-separation method near the crossing,
e.g. tracking line continuity vertex-by-vertex rather than x-banding).
