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
