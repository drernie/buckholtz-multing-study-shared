# docs/144 — new MULTING preprint (202608.0943): SH0ES is a fitted point, not a held-out prediction target — verified directly from the PDF

**Date:** 2026-08-14
**Origin:** TJB's revised Reddit headline (2026-08-13/14 thread, docs/143) claims "the
unconstrained fit lands within a fraction of a percent of SH0ES's measured H₀ — without
that value being imposed." This doc verifies what that claim actually rests on, against
the primary source: the new public preprint, "Multi-Tier Newtonian Gravity: A Cosmic-Node-
Based Alternative to LCDM for the Hubble Tension" (Buckholtz, Preprints.org 202608.0943v1,
dated August 2026), attached by TJB himself to the 2026-08-13 email as
`260808 1235 to_MULT_260717_0525_v82.pdf`.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · NO_AUTHOR_ERROR · OUR_RECONSTRUCTION · L0 descriptive
**Source:** direct `Read` of the local PDF (40 pages; abstract, methods, results, and
discussion sections read in full — pp. 1–28), not a web fetch or a summary. Per this
project's own evidence policy, this is genuinely `[VERIFIED]`, not `[INFERRED]` from a
paraphrase — WebFetch/curl/browser attempts against the live preprints.org page all
failed (Akamai bot-block, 403) before the PDF became available locally.

## 1. What the abstract and Sec. II G establish — confirmed as stated

**[VERIFIED]** Abstract: "By fitting 33 data points (31 Cosmic Chronometer H(z)
measurements (0<z<1.97), SH0ES, and a DESI DR2 Lyman-alpha measurement at z=2.33),
MULTING produces a well-identified solution family that reduces the Planck-SH0ES tension,
while performing as well as or somewhat better than flat ΛCDM, fixed at its standard
published values, on both chi-squared and Pearson-r across all 33 points."

**[VERIFIED]** Sec. II G, restated even more explicitly: "Our framework treats SH0ES and
DESI as data points, each carrying its own tight (compared to the 31 Cosmic Chronometer
points) uncertainty, alongside the 31 Cosmic Chronometer points, and jointly optimizes all
three free parameters, unconstrained, against the resulting 33-point ensemble."

**Consequence, confirmed:** the headline's "without imposing that value" is defensible in
the narrow sense that `H₀` is not a *fixed constant*; it is a *free parameter jointly
fitted* to a dataset that includes SH0ES itself. Landing near SH0ES is consistent with a
correctly-converged joint fit, not with an independent prediction. This is exactly the
distinction the correspondence thread (docs/143) already flagged, now confirmed against
the primary text rather than inferred.

## 2. Two findings NOT captured in the pre-verification discussion — corrections to register

**(a) The "refit ΛCDM vs. refit MULTING" comparison the thread proposed as still-needed is
already IN the paper (Table II, pp. 12–13) — not a missing test.**

**[VERIFIED]** TJB reports a second benchmark: "The second benchmark lets ΛCDM take the
same advantage of SH0ES's precision that MULTING's own fit does: freely optimizing `H₀`
and `Ωₘ` against the same 33 points, rather than holding them fixed at Planck. This
adjusted ΛCDM, like MULTING's own unconstrained fit, is pulled toward SH0ES by its tight
uncertainty, landing at `H₀=71.83`, `Ωₘ=0.2724`: `χ²₃₃=16.31`, `r₃₃=0.9632`."

Result of that fair comparison: "Only MULTING's two best rows (the unconstrained case,
`χ²₃₃=15.75`, and the SH0ES-anchored comparison case, `χ²₃₃=15.78`) outperform this second
benchmark [on `χ²`]... MULTING still edges ΛCDM out, though narrowly, rather than
substantially."

**This is a structurally important, previously-unaccounted-for point beyond "SH0ES is in
the fit":** a freely-refit ΛCDM, given the *same* fitting freedom and the *same* dataset,
*also* lands close to SH0ES (`71.83` vs. SH0ES's `73.04`, well within the combined
uncertainty). This is the generic behavior of a precision-weighted joint fit — the
tightest-uncertainty point pulls any sufficiently flexible model toward it, regardless of
the model's own physics. "MULTING's best fit lands near SH0ES" is therefore **not, by
itself, distinctive evidence for MULTING's physics** — the paper's own fair benchmark
shows the same pull acting on ΛCDM. What *does* survive as a genuine (if narrow) result:
MULTING's `χ²₃₃`/`r₃₃` edge over that fairly-refit ΛCDM benchmark, honestly small
(`15.75–15.78` vs. `16.31`), not the "matching or beating" framing's implied margin.

**(b) The absence of AIC/BIC is an explicit, defended authorial choice — not an omission
still to be supplied.**

**[VERIFIED]** Sec. IV I: "Given this asymmetry, we do not report AIC or BIC anywhere in
this paper... A penalty for the number of free parameters presupposes that those
parameters were fixed independently of the data under test, an assumption that holds far
more securely for ΛCDM, given its history, than for a framework still in active
development... reporting a single AIC or BIC number would present that asymmetry as a
resolved, symmetric statistical contest, which it is not."

Registering this changes what a "decisive next step" recommendation should say: asking for
AIC/BIC would be asking TJB to do something his own paper already explains why he
deliberately did not do — not surfacing an overlooked gap.

**(c) The proposed "decisive experiment" (exclude SH0ES/DESI, fit CC-only, freeze, predict)
is a scenario TJB's own paper already flags as fragile — not a fresh, unconsidered idea.**

**[VERIFIED]** From the paper's own intro (p. 2): "Both results rest on, and do not erase,
the following underlying fragility, discussed in depth in Sec. IV K and Sec. IV M: Fit to
the Cosmic Chronometer data alone, without SH0ES or DESI included directly, our framework
exhibits a near-total cancellation between two force terms that leaves it fragile under
extrapolation." Sec. IV K (Table III) shows the mechanism directly: the dipole (`F⁽¹⁾`) and
quadrupole (`F⁽²⁾`) force-term shares are `~50%` each with opposite sign, summing to a net
of only `4–6%` — i.e., the fitted curve is the *small residual* of two much larger,
nearly-cancelling terms, which is exactly the structure that makes a fit numerically
fragile when the tight external anchors (SH0ES, DESI) are removed.

**What is NOT in the paper:** an actual reported numeric `H₀` from a CC-only fit. TJB
qualitatively flags the scenario as fragile; he does not appear to have run and reported
it as a standalone number anywhere in the 28 pages read. The "decisive experiment" from
the correspondence thread is therefore still a genuinely open, unrun test — but framing it
to TJB as if he hadn't already considered this exact concern would be inaccurate; he has,
in his own words, in his own paper.

## 3. What this does NOT establish

1. That MULTING's underlying physics is wrong, or that the paper is dishonest — the
   opposite: the paper is unusually explicit about its own limitations (Class III
   circularity in `r_X(z)` via `ρ_crit(z)`, an abandoned first-principles attempt to ground
   `H_0,anchor` that gave an implausible `~11 km/s/Mpc`, and a dedicated section, IV H,
   listing seven named circumstances where the framework "should not be expected to be
   accurate").
2. A specific numeric value for what a genuine CC-only-fit, held-out `H₀` prediction would
   be — not computed here, and not present in the paper as read.
3. Any claim about which of MULTING's or ΛCDM's underlying assumptions is correct — this
   remains a fitting-methodology and disclosure-framing question, not a physics verdict.
4. Anything about sending correspondence to TJB — this is an internal registration only;
   the project's standing correspondence protocol (formal address, no evaluative-authority
   language, share results not questions, explicit "send" required) is unchanged and not
   invoked by this doc.

## Reproduction

Primary source: `260808 1235 to_MULT_260717_0525_v82.pdf` (local, provided by the user,
originally TJB's own email attachment, 2026-08-13 thread "RE: request for an opinion
regarding a draft reddit heading"). Quotes above are verbatim from pp. 1, 2, 12, 13, 19,
20–21 of that PDF.
