# CLAIM E18 — independent reproduction of v82's own fit, answering
# Ernest Prabhakar's item 6 ("let Tom Lawrence, Sergey, or a practicing
# cosmologist reproduce the fitting results")
#
# STATUS: DONE, corrected after Step 8a skeptic (WEAKENED, 5 points, all
# fixed in place). Corrected framing: "re-executes and extends TJB's
# own already-archived, independently-IMPLEMENTED script" -- not a
# from-scratch reimplementation. See FINDING_E18 for full detail.

**Date:** 2026-09-06
**Trigger:** TJB's forwarded email thread (Ernest Prabhakar → TJB →
Sergey, 2026-09-04/06) — Ernest's 6-point critique paused a press
release; item 6 states nobody outside TJB has run the Zenodo archive,
and names Sergey explicitly as someone who could. TJB's own email to
Sergey asks directly: "Have you performed or can you perform the action
Ernie suggests in item 6?"
**Explicit go-ahead given**, scoped to item 6 only ("сначала пункт 6...
давай это сделаем максимально скурпулезно").

## L0 (EstimandOps)

**Descriptive.** Does an outside party (this project, not TJB), running
TJB's own already-archived, independently-implemented verification
code — completely unmodified except an unavoidable file-path fix —
reproduce the published Table II fit results? This is not a claim about
whether MULTING is correct; it is a claim about whether the numbers in
the paper are what the archived code computes, checked by someone
other than the author.

## What already exists (context, not duplicated)

- `data/source_material/zenodo_21204955_supplemental/process_documentation/
  independent_verification/multing_fit.py` — a self-contained script
  TJB's own archive states was written by "a genuinely independent AI
  session (a different tool, fresh conversation, given only
  `regenerate_prompt.md`'s prompt and `assumptions.yaml`)" — i.e.
  independently IMPLEMENTED, not a copy of `multing_core.py`. Per this
  archive's own `INDEX.md` (2026-09-02), this is already recognized as
  this project's strongest-yet instance of the Independent Verification
  Strength Ladder's "Different model" (Medium) tier.
- **The real gap this claim closes:** that verification was run within
  TJB's own process (archived by him, under his control) — not by an
  outside party. `FINDING_P176` (2026-08-31) is this project's own
  reproduction, but reuses TJB's own `multing_core.py` functions
  verbatim and only checks 2 of 7 Table II rows with a local
  re-optimization from ONE nearby starting guess (its own "What this
  file does NOT establish" #5 names the gap: no full multi-start global
  search).

## Falsifiable predicate and pre-registered MCID

**Predicate:** running the archive's own independently-implemented
script, unmodified except path resolution, on this project's own
machine, reproduces the published `unconstrained_spotlighted` row
(`H0_anchor=73.22, β1=1.4335e10, β2=7.8067e17, χ²₃₃=15.75, r₃₃=0.9659`)
to the paper's own stated precision, AND all 6 remaining Table II rows'
χ² values are reproduced at their published `(β1,β2,H0_anchor)` triples,
AND a genuinely wide-range global optimizer (not just nearby-start
local search) finds no lower minimum than the published one for the
free row.

**MCID:** MATERIAL DISCREPANCY if any reproduced χ² differs from its
published value by `>1%`, or if a global search finds a `χ²` more than
`1` unit lower than the published minimum (a real, better fit TJB's own
local search missed) OR discovers a materially different `(β1,β2)`
achieving comparable `χ²` (a distinct degenerate solution TJB did not
report).

## Method

1. Hash the exact archive files used (script + `assumptions.yaml`) for
   provenance, before touching them.
2. Run the archive's own `independent_verification/multing_fit.py`
   completely fresh, path-fixed only (diff-verified: no formula,
   constant, or numeric literal changed — only path resolution and
   ruff's own whitespace formatting).
3. Extend: reproduce `χ²₃₃` at ALL 7 Table II rows' own published
   `(β1,β2,H0_anchor)` triples (positive control against the paper's
   own numbers, not just the 1-2 rows previously checked).
4. Extend: run `scipy.optimize.differential_evolution`, a genuinely
   different, population-based global optimizer (not Nelder-Mead from a
   nearby guess), across a wide bound
   (`β1∈[0.3,3.0]×10¹⁰, β2∈[1.5,15.0]×10¹⁷, H0_anchor∈[60,80]`) on the
   free `unconstrained_spotlighted` row, to check for a missed global
   minimum or an undiscovered degenerate solution.

## Controls

- **Positive control:** the archive's own independent script must
  reproduce `H0_anchor=73.2160, χ²₃₃=15.7515, r₃₃=0.9659,
  β1=1.433479e10, β2=7.806760e17` — the exact numbers the archive's own
  `INDEX.md`/README already claim its internal AI session got. If this
  project's own fresh run does NOT match those exact numbers, something
  about the archive, this environment, or that internal claim itself is
  wrong — a real, falsifiable check, not tautological.
- **Negative control:** deliberately perturb one input constant (e.g.
  `Om_planck`) by a large, obviously-wrong amount and confirm `χ²`
  changes substantially — confirms the reproduction is sensitive to
  inputs, not silently returning a cached/hardcoded number.

## What this does and will NOT establish

1. Whether MULTING is physically correct — `NO_AUTHOR_ERROR`, empirical/
   model status only, per `docs/151`.
2. Whether the fit itself is scientifically meaningful (AIC/BIC,
   falsifiability, mechanism-consistency — separate, already-answered
   items 1/2/5, not this claim's scope).
3. A GLOBAL guarantee that no better minimum exists anywhere in
   parameter space — `differential_evolution` over a wide but finite,
   stated bound is strong evidence, not an exhaustive proof.
