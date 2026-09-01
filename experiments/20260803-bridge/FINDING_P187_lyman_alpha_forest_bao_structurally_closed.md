# FINDING P187 — Lyman-alpha-forest BAO at non-extreme redshift is
# structurally closed, not merely unexplored

**Date:** 2026-09-01
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (literature-search closure of a named
gap — not a new physics claim)
**Continues/answers:** `FINDING_P185`'s own "does NOT establish" item 2
— the eBOSS quasar-clustering BAO test narrowed the measurement-type
confound to "quasar-clustering BAO specifically evidenced against,"
but explicitly left **Lyman-alpha-forest BAO** (DESI's own tracer) as
an untested, live alternative, since no Lyman-alpha-forest BAO point
at a non-extreme redshift had been searched for. This file runs that
search.
**Script:** none — literature search only, no computation. (Companion
computation would be identical in shape to `P185_eboss_type_vs_
redshift.py`'s Set B construction, but no candidate data point to
compute with was found — see below.)
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** the literature-search result itself
> ([VERIFIED-REAL], 3 independently fetched arXiv sources) is a solid
> negative finding with an explicit physical mechanism, not a mere
> absence-of-search.
> **Ontological/mechanistic interpretation status:** N/A — this file
> makes no claim about MULTING's mechanism.
> **Causal/cosmological claim status:** N/A.

## 0. Premise — `NO_AUTHOR_ERROR`

This file searches the public literature for a specific type of data
point (a real Lyman-alpha-forest BAO measurement at a non-extreme
redshift) to complete a confound-breaking test design from this
project's own prior work; it makes no claim about v82's own theory.

## 1. What was attempted

`FINDING_P185` used eBOSS DR16 quasar-clustering BAO (Neveux et al.
2020, z=1.480) to test whether DESI's outsized leave-one-out influence
in the v82 degeneracy thread is driven by "BAO measurement type" in
general. A context-blind skeptic review of that file correctly pointed
out that DESI's own z=2.33 point is specifically a **Lyman-alpha
forest** BAO measurement — a different tracer, different systematics,
different modeling from quasar-clustering BAO — so P185's result does
not test the specific type DESI represents.

The natural next step, named explicitly in P185's own "does NOT
establish" section and confirmed by `research-audit` (boyko-project-
radar, 2026-09-01) as "the last unconditionally-authorized step" on
this sub-question: search for a real, independently-published
Lyman-alpha-forest BAO measurement at a non-extreme redshift (i.e.
within or near the existing 7-point cosmic-chronometer range,
z=1.037-1.965) — the same search method that successfully found eBOSS
for the quasar-clustering case.

## 2. Search and results

**Query 1** — general survey of Lyman-alpha-forest BAO redshift
coverage: BOSS's own stated design goal is measuring the BAO scale
from Lyman-alpha forest quasar sightlines at z~2.5, using quasars in
2.15 ≤ z ≤ 3.5. eBOSS DR14 extended this down to 1.77 < z < 3.5.
DESI's own DR-era analyses require a minimum quasar redshift of
z=2.02 (minimum Lyman-alpha pixel redshift z≈1.96). No survey searches
below z~1.77 for this technique.
[Sources: BOSS/eBOSS DR14 Lyα-quasar cross-correlation papers,
arXiv:1904.03430; DESI early-data Lyα systematics paper,
arXiv:2402.18009.]

**Query 2** — explicit physical limit: intergalactic Lyman-alpha
forest absorption (the signal the BAO measurement depends on)
**physically disappears below z≈2**, replaced by circumgalactic
absorption — a different physical regime the standard technique
cannot use. One forward-looking forecast paper (China Space Station
Telescope, arXiv:2512.19474) explicitly targets this gap.

**Query 3** — checked the CSST forecast paper directly ([VERIFIED-REAL],
fetched abstract): confirmed **pure mock-data/forecast**, not a real
measurement — "construct mock CSST quasar spectra," "forecast
constraints." Target range 1.1 < z < 2.0, z_eff=1.59 (exactly the kind
of point this search needed) — but the telescope has not flown; this
paper reports only a projected "marginal 2.5σ detection" and "~10%
constraint on the isotropic BAO scale," not an actual number.

**Query 4** — checked whether a different tracer population could
reach lower redshift with REAL current data: a genuinely new technique
using Lyman-break galaxies (LBGs) instead of quasar sightlines
(arXiv:2507.21852, DESI DR2, "First 3D Correlation Measurement")
[VERIFIED-REAL, fetched abstract directly]. This is real data, not a
forecast — but its effective redshift is **z_eff=2.70, HIGHER than
DESI's own z=2.33**, not lower. The paper explicitly states its result
"is consistent with that from DESI DR2 quasar Lyα forest spectra at a
comparable redshift" — same epoch, not an extension to lower z. It
also does not report an actual BAO distance/H(z) value from real data
yet (correlation-function-only; BAO precision is itself only forecast
for a future wider survey).

## 3. Verdict

**GENUINELY CLOSED, not merely unexplored** — no real, published
Lyman-alpha-forest BAO measurement exists at a non-extreme redshift,
and there is an explicit, sourced physical reason why none currently
can: the intergalactic Lyman-alpha forest signal itself is not
observable below z≈2 with current survey techniques (circumgalactic
absorption dominates instead, a different physical regime). The one
real dataset probing an alternative tracer (LBGs) at a comparable
technique maturity level lands at an even HIGHER redshift (2.70) than
DESI's own point, not lower. The only work targeting the needed
redshift range is a pure forecast for a telescope that has not yet
flown.

This closes P185's own "does NOT establish" item 2 in the same sense
P185 itself closed the earlier "no cosmic-chronometer point above
z=1.965" question: **not because nobody looked, but because the
underlying physics of the measurement technique forecloses it** with
currently available real data.

**Consequence for `FINDING_P177`'s central question**: the
measurement-type-vs-redshift confound cannot be broken any further
using a real Lyman-alpha-forest BAO point, because none exists at a
useful redshift. Per `research-audit`'s own framing (2026-09-01), this
was named as the last unconditionally-authorized step on this specific
sub-question — with it now closed, the honest status of the
redshift-vs-measurement-type confound is: **quasar-clustering BAO
specifically evidenced against** (`FINDING_P185`), **Lyman-alpha-forest
BAO specifically untestable with current real data** (this file), and
`FINDING_P177`'s underlying question (genuine correspondence vs.
Taylor-truncation leverage) remains open — not because further tests
were skipped, but because the real 33-point dataset plus the real
external literature both run out of differentiating material at this
point.

## 4. What this file does NOT establish

1. **Not a claim about v82's own theory** (`NO_AUTHOR_ERROR`, §0).
2. **Does not prove Lyman-alpha-forest BAO measurement type is
   innocent** of driving DESI's outsized influence — it establishes
   only that this specific hypothesis cannot currently be tested with
   real data, which is different from testing it and finding it not
   guilty (as `FINDING_P185` did for quasar-clustering BAO).
3. **Does not resolve `FINDING_P177`'s central question.**
4. **Does not rule out a future real measurement** closing this gap —
   if the CSST mission (or an equivalent) flies and delivers a real
   z~1.5-2.0 Lyman-alpha-forest BAO measurement, this branch should be
   reopened; the pearl_registry entry for this file names that
   condition explicitly.
5. **Does not exhaustively survey every conceivable future or
   proposed technique** — only the four query directions above (survey
   redshift coverage, physical limit literature, the one concrete
   forecast paper found, and the one concrete real-data LBG-based
   alternative found). A near-future literature update could in
   principle surface something missed here.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
