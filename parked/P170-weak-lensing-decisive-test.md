# P170 — MULTING pairwise-force power-spectrum / ΔS8 decisive test

**Date:** 2026-08-31
**Verdict:** ARCHIVE (parked) — decisive test fully specified
(`FINDING_P170`'s own Этап 7), blocked on a missing method, not missing
data per se.
**L0 (EstimandOps):** Predictive (would `MULTING`'s own force predict a
computable `ΔS8`?) — **not causal**, no claim about real-world structure
growth is made or tested here.
**Source:** `experiments/20260803-bridge/FINDING_P170_negative_space_structural_class_weak_lensing.md`
(negative-space-miner Phase 3, skeptic-corrected 2026-08-31).

---

## Proposal (one line)

Compute MULTING's own pairwise dipole+quadrupole force's contribution to
the matter power spectrum / `S8`, to test whether the H0-S8 trade-off
documented across the published literature (models that fix `H(z)` via
background-only-calibrated extra parameters often worsen structure
growth, `arXiv:2103.04045`/`2308.16183`/Galaxies 14(2),16) applies to
MULTING specifically — or whether MULTING's own already-proven
zero-isotropic-MEAN property (`FINDING_P154`/`P155`) means the
variance/lensing-visible signature is also negligible.

## Why parked, not run

**Not a data-availability block** (weak-lensing survey data — KiDS,
DES, HSC — already exists and is public; `d0=45 Mpc`, MULTING's own
characteristic separation, falls within the angular-correlation range
these surveys already probe). **The actual block is methodological**:
no existing recipe embeds a discrete, fixed-separation pairwise force
between point-like nodes into a continuous power-spectrum/perturbation-
theory calculation. Standard PT operates on smooth density fields; node
population statistics (Poisson? halo-mass-function-weighted? correlated
with the matter field?) are unspecified; which PT scheme (SPT, EFT of
LSS, a modified Boltzmann code) is undetermined. `FINDING_P170`'s own
§Этап 7 names the IV/DV/controls/falsification-criterion but explicitly
stops before solving the embedding — "a research problem, not an
implementation task."

## Parked Pearl fields (FL Parked Pearl Rule)

| Field | Content |
|---|---|
| **Original branch** | Causal-audit series Phase 3 (`FINDING_P166`-`P169`'s own named next step) — does MULTING survive an independent, non-`H(z)` structural check? |
| **What was killed** | Nothing killed — the question remains open, only the "run it now" framing is blocked. |
| **What survives** | (1) The general H0-S8 trade-off literature pattern is real and documented, transferable context for any future Hubble-tension-model audit; (2) `FINDING_P154`/`P155`'s zero-isotropic-mean result is a genuine, MULTING-specific structural reason the class-level pattern might NOT transfer — worth citing whenever this question resurfaces; (3) the Decisive Test's IV/DV/controls/falsification-criterion specification (`FINDING_P170` §Этап 7) is reusable once a method exists. |
| **Revival Condition** | (a) a PT or N-body method for embedding a discrete, fixed-separation pairwise multipole force into a power-spectrum calculation is designed (by this project or found in the literature) — **OR** (b) TJB's own future work computes this directly — **OR** (c) an existing tool/framework is found that already does the equivalent for a structurally similar (discrete pairwise, non-continuum) force law, making adaptation tractable rather than a from-scratch research problem. |
| **Related future gates** | The 2026-06-17 pearl-registry weak-lensing entry (`pearl_registry/INDEX.md`, "Euclid weak lensing DR1 should show non-geodesic cluster motions IF MULTING dipole is real at β_d≫4.5," `next_check: 2026-Q4`) — related but distinct: that entry is about a DIFFERENT, older β_d notation and a specific anomaly-detection framing; this entry is about the general power-spectrum/S8 channel. Worth cross-checking both when either is revisited. |
| **Forbidden use** | Do NOT cite this parked entry as evidence MULTING passes or fails a weak-lensing test — no calculation was performed. Do NOT treat the zero-isotropic-mean result as proof the variance is also small — that is an untested, equally-weighted alternative (`FINDING_P170` §Этап 6 H0-null), not an established fact. |

## Mandatory protocol if revived

1. **Design the embedding method FIRST** — do not attempt a numeric
   estimate before the node-population-statistics and PT-scheme choices
   are made explicit and justified.
2. **Run the methodology control before trusting any MULTING-specific
   number** — reproduce a KNOWN published force's (e.g.
   `arXiv:2510.12551`'s own interacting-DM elastic-force calculation)
   reported sign/magnitude with the same technique, per `FINDING_P170`'s
   own control design, before applying it to MULTING's own force.
3. **Re-check `FINDING_P154`/`P155`'s own caveat** (filled-ball uniform
   density + independent node orientations assumed, not excluded for a
   population with genuine spatial-orientation correlations) — the
   variance-level calculation may be more sensitive to this than the
   mean was.

---

*ARCHIVE — not a null result. Revisit only when Revival Condition is met.*
*Cross-ref: `FINDING_P170` (full negative-space-miner writeup, skeptic-corrected).*
*Cross-ref: `FINDING_P154`/`P155` (zero-isotropic-mean result this entry's H0-null leans on).*
