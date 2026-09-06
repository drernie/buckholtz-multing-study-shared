# FINDING P195 ADDENDUM — bounded literature search for a nonlinear/
# high-peak-height halo bias extension covering v82's z≥1.07 points:
# null result, honestly reported

**Date:** 2026-09-06
**Continues:** `FINDING_P195_floor_sensitivity_sweep.md` (covered only the
4 low-z, already-grounded target points) and `FINDING_P158_ADDENDUM2`
(named the z≥1.07 gap explicitly: `ν` from `10.64` to `49.97` across
v82's own 4 high-z target points, outside Tinker et al. (2010)'s
calibrated range, "resolving that would require nonlinear halo bias
treatment or direct N-body pair statistics, neither attempted here").

## L0 (EstimandOps)

**Descriptive.** Does a real, published, validated halo-bias treatment
exist that covers peak heights `ν≈10.6-50` — the range of v82's own 4
target redshifts `z=1.07, 1.965, 2.33, 5.0` — the way Correa+2015 Paper
III covered `E17`'s own out-of-range concentration-mass extrapolation
earlier today? Not a physics claim; a literature-availability question.

## What was done

Two targeted `arXiv` searches ("halo bias very high peak height extreme
mass rare halos calibration N-body extension beyond Tinker"; "halo bias
massive clusters high redshift peak-background split large nu validated
simulations"), 12 results total. No result addresses calibration or
validated extension specifically at `ν≳10`. Candidates considered and
ruled out:

- **Tinker et al. (2010)** (`arXiv:1001.3162`, the very fit `P158` already
  uses) — its own abstract states halo bias "approaches the predictions
  of the spherical collapse model for the rarest halos" in their
  simulations, with `~20%` peak-background-split residuals at the high-mass
  end even within their own calibrated range. No explicit `ν_max` was
  extractable from the abstract or a full-text search (the paper's full
  text was not indexed by the available tool), but the qualitative
  language ("approaches," not "matches") is itself evidence the fit was
  not built or tested at `ν~10+` — precisely the kind of soft-boundary
  language `P158_ADDENDUM2` already flagged as a reason not to trust
  extrapolation.
- **Aemulus IV halo bias emulator** (McClintock et al. 2019,
  `arXiv:1907.13167`) — a precision emulator, but built from the same
  class of finite-volume N-body suites; nothing in the abstract claims
  coverage of `ν≳10` rarity, and no full-text check was performed given
  the pattern above.
- The remaining 10 results (assembly bias, non-Gaussian bias, local bias
  measurements, peak-background-split critiques, a 2026 web-halo-model
  paper) address different questions — none targets extreme peak height.

**No same-author-lineage extension candidate, analogous to Correa Paper
II→III or Taylor 2023, turned up.** That pattern (today's own two
successful unblocks) relied on a specific follow-up paper explicitly
widening a stated range; no such paper surfaced here in a bounded search.

## Why this is plausible, not just an artifact of a short search

Peak height `ν≈10-50` corresponds to objects that are exponentially rare
in ΛCDM — `P158_ADDENDUM2` itself already called `ν≈50` (the `z=5` point)
"astronomically beyond anything a real cosmic structure could be." Even
large-volume collisionless N-body suites (Tinker's own multi-simulation
compilation, or Aemulus's Latin-hypercube boxes) contain too few objects
at that rarity to calibrate a bias relation empirically — this is a
structural limitation of the method (finite simulation volume ×
exponentially suppressed high-`ν` counts), not a gap that a slightly
longer literature search would likely close.

## Result

**`SOURCE_NOT_FOUND`** for a validated nonlinear/high-peak-height halo
bias extension covering v82's own `z≥1.07` target points, after a
bounded, real search (2 targeted arXiv queries, 12 results, one
abstract read in full, one full-text check attempted and unavailable).

Per this project's own `falsification-ladder.md` ("A null literature
search can be a strong result if there's an explicit physical reason for
the absence," `activeContext.md`'s own carried-forward lesson from
`P185`/`P187`): the absence here has a named physical reason (exponential
rarity of high-`ν` peaks vs. finite simulation volume), not just "nothing
turned up."

## What this does and does NOT establish

**Does establish:** the `z≥1.07` gap named in `FINDING_P158_ADDENDUM2`
and reconfirmed by `docs/156`/`P195` is not quickly closeable by the same
literature-grounding pattern that worked twice today (`E17`
concentration-mass, `E10` SNe fitter comparison) — those succeeded
because a same-lineage paper explicitly widened a stated range; no such
paper was found here.

**Does NOT establish:**
1. That no such treatment exists anywhere in the literature — only that
   a bounded, real search did not find one. A future, more exhaustive
   search (e.g., direct N-body pair-statistics papers targeting cluster
   pairs specifically, rather than bias fits) was not attempted.
2. Anything about whether v82's own bridge construction is correct or
   incorrect at these redshifts — only that this project's own machinery
   cannot currently validate `ρ` there.
3. `NO_AUTHOR_ERROR` — a scope statement about this project's own
   reconstruction tooling, not a claim about TJB's work.

## Verdict and next step

**Item 2 (`docs/157`'s own listed follow-up, "bottleneck-1 `ρ` coverage
to `z≥1.07`") stays genuinely open/blocked** — consistent with, not
contradicting, `docs/156`'s and `FINDING_P158_ADDENDUM2`'s own prior
2026-09-05 assessment that this "would require nonlinear halo bias
treatment or direct N-body pair statistics, neither attempted here" and
needs "materially more specialized work... neither this project nor its
existing machinery currently supports." Closing it fully would require
either a specialized N-body pair-statistics calculation (out of scope for
this project's tooling) or a future literature search finding a paper
this one missed. No further action recommended without new input (a
found paper, or an explicit decision to attempt an N-body-based
calculation).
