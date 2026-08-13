# P29 — Archidiacono's own field equations confirm an absolute growth channel exists, and reveal their coupling topology is DM-only-sourced, not universal

**Date:** 2026-08-13
**Origin:** direct continuation of `FINDING_P28`'s own corrected §4 point 1
— flagged, but not checked there, whether Archidiacono et al.'s actual
CMB+BAO pipeline (beyond the toy differential-growth model P28 used) has
independent sensitivity to absolute matter-growth amplitude. This finding
goes to their own field equations (via WebFetch, not general
modified-gravity-literature reasoning) to check directly.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P29_archidiacono_own_equations_absolute_growth.py`

## 0. Honest scope, stated before anything else

**Evidence-quality caveat, stated up front:** the quoted equations below
come from two WebFetch calls against `arxiv.org/html/2204.08484`, mediated
by a summarization model — not a direct read of the paper's raw LaTeX
source. This is a real, structural limitation of the tool available in
this session (the `WebFetch` tool converts and summarizes; it does not
return verbatim source). Two independent, differently-worded queries
against the same page returned **consistent** equation text both times
(cross-checked below), which raises confidence above a single query, but
this is still `[VERIFIED-WEBFETCH]`, one tier below directly reading a
source file — not `[VERIFIED-BASH]`. If a future finding can access the
paper's raw source (e.g. the arXiv LaTeX source download), it should
re-verify these equations directly and upgrade the marker.

This finding does **not** derive any new numeric bound, does not
reconstruct Archidiacono et al.'s actual MCMC likelihood, and does not
resolve whether their `β<0.01` bound, reinterpreted for a universal
coupling, would be tighter or looser than the DM-only case. It establishes
two narrower, more concrete points: (1) their own model has a mechanism
for absolute (not just differential) growth enhancement, strengthening
`FINDING_P28`'s corrected retraction with direct textual evidence rather
than general-literature plausibility; and (2) their fifth force has a
different source-receiver topology than MULTING's own universal `g`,
a distinction `FINDING_P22`'s original β-mapping did not check.

## 1. Source verification (two independent WebFetch queries, cross-checked)

Query 1 (broad: "does the paper discuss σ8/S8, and universal coupling
degeneracies?") returned, among other content, their Poisson-type equation
(their eq. 4.4):

> "k²δs = −a² 4πGₙβ(∂log mχ(s)/∂s) ρ̄χδχ"

and quoted their own text characterizing eq. 4.16 as containing "a new
contribution to the potential... as well as a suppression of Ωₘ below unity
due to the fraction of the total energy density" — i.e., a term that
affects the **DM density equation directly**, not only a relative quantity.

Query 2 (targeted: "confirm precisely whether the Poisson-type source
includes a baryon term, and whether baryons feel the fifth force directly")
returned the **same** equation 4.4 (verbatim match against query 1),
their DM Euler equation (eq. 4.2):

> "θ'χ + (ℋ + ∂log mχ(s)/∂s · s̄') θχ − k²(Ψ + ∂log mχ(s)/∂s · δs) = 0"

and a baryon growth equation from the coupled system around eq. 4.16:

> "δ''b + ℋδ'b − (3/2)Ωm ℋ²(fχδχ + (1−fχ)δb) = 0"

The two queries' quotes of eq. 4.4 match verbatim — the strongest
cross-check available without raw-source access.

## 2. Method and result

**(a) Structural comparison — is Archidiacono's coupling the same
functional form as a universal coupling, just rescaled?** No. Their eq.
4.4's source term contains only `ρ̄_χδ_χ` (dark matter density
perturbation) — no `δ_b` term appears anywhere in it (verified: `delta_b
not in dm_only.free_symbols`, sympy). A genuinely universal coupling (P23's
reading of MULTING's `g` — proportional to inertial mass for *every*
species, exactly as gravity itself is) would source its Poisson-type
equation from the **total** matter perturbation `δ_tot = f_χδ_χ +
(1−f_χ)δ_b`, which structurally requires a baryon contribution. These are
not the same functional form under a relabeling of the coupling strength —
one is DM-self-sourced, the other is source-democratic across species. A
future re-mapping of Archidiacono's `β` bound onto MULTING's universal `g`
(as `FINDING_P22` originally did) needs to account for this topology
difference, not just rescale the coupling magnitude.

**(b) Does Archidiacono's own DM-only model still produce an absolute
growth effect, even though the fifth-force term itself only appears in the
DM equation?** Yes. Their own quoted baryon growth equation is sourced by
`(3/2)Ω_mH²(f_χδ_χ + (1−f_χ)δ_b)` — a term with nonzero derivative with
respect to `δ_χ` (verified symbolically: `∂/∂δ_χ = (3/2)Ω_mH²f_χ ≠ 0`).
Baryons carry no direct fifth-force term, but they **do** respond to
enhanced DM clustering through ordinary gravity, since baryon growth is
sourced by the *total* matter perturbation, which includes the
(fifth-force-enhanced) `δ_χ`. Combined with the paper's own characterization
of eq. 4.16 as containing "a new contribution to the potential" affecting
the DM equation directly, this confirms: **even in their own DM-only
model, an absolute (not merely differential) growth-of-structure channel
exists** — the fifth force boosts DM's own growth, which then, via
standard gravity, also boosts baryon growth, alongside the differential
DM-baryon lag their abstract highlights as the paper's headline novel
signature.

## 3. Consequence for `FINDING_P28`'s correction

This directly **strengthens** `FINDING_P28`'s corrected retraction with
concrete textual evidence, replacing what was previously argued only from
general modified-gravity-literature plausibility. It does **not** resolve
what P28 §4 point 2 (corrected) left open — whether a *universal*
reinterpretation of their `β` bound would be tighter, looser, or simply
inapplicable — because point (a) above shows their model's topology
(DM-sourced-only) is not the same as the universal topology MULTING's `g`
requires. If anything, this adds a **third**, independent reason (beyond
P28's differential-blindness argument and P23's target-population argument)
why `FINDING_P22`'s direct numeric mapping of `β` onto `A·g²` needs
re-examination: the coupling topologies are structurally different, not
just scoped to different populations.

## 4. What this does NOT establish

1. **A numeric bound of any kind.** No MCMC, no likelihood, no re-derived
   `β` value. Purely a structural/equation-level comparison.
2. **That Archidiacono's `σ8`/`S8` is explicitly varied or reported as a
   derived parameter in their fit.** The two WebFetch queries could not
   confirm this from the available (summarized) text — flagged as
   genuinely `[UNKNOWN]`, not assumed either way.
3. **A resolution of whether a universal-coupling reinterpretation of their
   bound would be tighter or looser than the DM-only case.** Only that the
   two cases are structurally different couplings, not a rescaling of one
   into the other — a prerequisite question for that comparison, not the
   comparison itself.
4. **A revision of `FINDING_P22`'s numeric `A·g²≲1.05×10⁻¹⁰` figure.** Not
   attempted; this finding only adds a further caveat on the mapping's
   applicability, joining P23's and P28's already-recorded caveats.
5. **Verbatim-source confidence.** Per §0, these equations are
   WebFetch-mediated (summarized), not directly read from source — treat
   as `[VERIFIED-WEBFETCH]`, one tier below a direct file read, pending
   future re-verification against raw LaTeX if available.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction of
   the coupling structure and a published external paper's own equations —
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P29_archidiacono_own_equations_absolute_growth.py
```
