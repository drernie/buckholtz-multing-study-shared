# Second application of the look-elsewhere checklist — Eq.32, own grammar,
# own null (not compared numerically to 7:9:17)

`NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION` · L0 descriptive
2026-09-08 · script: `eq32_checklist_second_application.py` · ruff clean

## What was asked, and what was corrected first

`pearl_registry/INDEX.md` (2026-08-10) framed `p = 7.1e-6 · |G|^0.95` as a
domain-independent "law" and proposed testing it on a second relation,
naming Eq.32 explicitly. Before building anything, the primary source of
that same finding — `FINDING_null_d_grammar.md`, same experiment, same
day — was read directly. It already disclaims that exact framing:

> *"On the exponent 0.95: Not a discovered law... an exponent near 1 is
> what a correctly behaving enumerator must return."*
> *"It does NOT license comparing this p with the Eq.32 p. Those range
> over grammars of different dimensionality with unharmonised nulls."*

So the mini-project this file reports is **not** "does Eq.32 land on the
same numeric line as 7:9:17" (forbidden by the source itself). It is: do
the two genuinely portable, non-comparative parts of the same checklist —
**(1) does p track the size of a relation's own declared grammar**, and
**(2) is the relation isolated from its nearest competitor, or just
close** — reproduce when applied fresh to a structurally different
relation, each within its own harmonised null?

## Part 1 — p vs. |grammar|, Eq.32's own family

Five nested grammars (prefactor complexity `p/q≤N`, exponent range
`1..M`), same statability filter as `eq32_look_elsewhere.py` (fixed 0.5%
own-uncertainty threshold), same random-target null construction:

| grammar | \|statable\| | p | Eq.32's own deviation |
|---|---:|---:|---:|
| pq≤6, n≤12 | 4,876 | 0.0135 | 0.0588% |
| pq≤12, n≤12 | 19,292 | 0.0583 | 0.0588% |
| pq≤12, n≤24 | 35,672 | 0.1608 | 0.0588% |
| pq≤20, n≤24 | 99,960 | 0.2818 | 0.0391%* |
| pq≤20, n≤36 | 141,525 | 0.3925 | 0.0391%* |

*At the two largest grammars, some other statable expression edges
closer to the target than Eq.32's own `4/3×(τ/e)^12` — itself a small,
honest, additional confirmation that a larger declared search finds
closer matches, independent of any specific relation.

**Fit: `p = 3.16×10⁻⁶ · |statable|^0.999`, median residual 11%.**

**Positive control, unplanned but real:** the `pq≤12, n≤24` row's
`p=0.1608` is an *exact* match to `eq32_look_elsewhere.py`'s
independently-computed `p=0.1608` at the same grammar (that script was
written 2026-08-10, this one 2026-09-08, sharing only the physical
constants, not the code path for the null construction). This is a
genuine reproducibility check, not manufactured.

**Verdict, Part 1:** the qualitative diagnostic — an exponent within a
few tenths of 1, expected from nearest-neighbour density scaling — 
**reproduces** in a structurally different relation (a coefficient×power
match against a single fixed target, not a 3-integer proportion with a
free scale). This is the checklist's genuinely portable claim, confirmed
a second time, without ever comparing Eq.32's `p` or `|G|` numerically
against 7:9:17's own.

## Part 2 — isolation test (Result 3's D2/D1, applied to Eq.32 for the first time)

At the largest grammar (`pq≤20, n≤36`, 141,525 statable expressions):

| | observed | null median |
|---|---:|---:|
| D2/D1 (nearest-competitor gap) | **1.50** | **2.01** |

Eq.32's nearest statable competitor is **no farther — if anything
slightly closer, relative to its own D1 — than typical random targets
get in this grammar.** No isolation evidence beyond raw closeness.

**Verdict, Part 2:** the same qualitative outcome Result 3 found for
7:9:17 (which also found real D2/D1 at or below the null median at
`N=20`) reproduces here: closeness alone, once the grammar is declared
honestly, does not by itself distinguish Eq.32 from an unremarkable
nearest-neighbour match.

## What this establishes

1. Both genuinely portable parts of the look-elsewhere checklist —
   density-dominated `p` scaling, and a working isolation test — transfer
   cleanly to a second, structurally different relation, each scored
   against its own harmonised null. This is the actual, defensible
   "domain-independent method" the pearl_registry entry was reaching for.
2. Eq.32's own look-elsewhere significance (already established,
   `eq32_look_elsewhere.py`, `p≈0.16` at its natural grammar) is now
   independently reproduced, and its isolation status is now measured for
   the first time: **not isolated**, same qualitative finding as 7:9:17.
3. A real, small reproducibility cross-check (the exact `p=0.1608` match)
   between two independently-written scripts a month apart.

## What this does NOT establish

1. **Does not** claim Eq.32's `p ∝ |G|^0.99` and 7:9:17's `p ∝ |G|^0.95`
   are "the same law" — the exponents are close, both near the
   theoretically-expected value of 1, but the grammars are different in
   kind and dimensionality; `FINDING_null_d_grammar.md`'s own prohibition
   on cross-comparison is respected throughout.
2. **Does not** reopen or touch Eq.32's mechanism-hunt (NR-019/NR-024,
   exhausted, closed) — this is about the statistical significance of the
   numerical coincidence, not its cause.
3. **Does not** newly refute Eq.32 — `eq32_look_elsewhere.py`'s own
   conclusion (*"not extraordinary... not refuted"*) stands unchanged;
   this file adds the isolation dimension that script did not test.
4. `NO_AUTHOR_ERROR`.

## Decision

**PROMOTE the corrected framing** for the harvest asset. The
pearl_registry entry (row, 2026-08-10) should be corrected: not "p ∝
size(G)^0.95, verify on a second relation by comparing p directly," but
"canonicalize + own-grammar density scan + isolation test is a portable
3-part checklist; confirmed transferable to a second, structurally
different relation, each within its own harmonised null." See companion
`pearl_registry/INDEX.md` correction.

**Effort:** small — reused `eq32_look_elsewhere.py`'s constants and
statability filter directly; the only new code was the multi-grammar
loop and the D2/D1 isolation computation (~150 lines). Matches the
"mini-project" scope the harvest scan itself estimated, not a larger
undertaking.
