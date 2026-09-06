# 157 — Next-steps plan, 2026-09-06

Written after closing 3 blind spots from today's `boyko-project-radar` scan
(E-series pytest coverage, `src/` silent-fallback audit, `experiments/`
cross-connectivity check, `sci-code-audit`). This document is a PLAN only —
no physics step below is executed here. Per this project's standing rule
("Any physics step... needs an explicit go-ahead," `activeContext.md`),
each item still needs a separate go-ahead before work starts.

## What closing the blind spots actually found

- **`src/` silent-fallback audit:** clean. `cluster_data_pipeline.py` is the
  only network-fetching module; its 2 `except Exception` sites already log
  the real error.
- **`experiments/` cross-connectivity:** `data/hz_cc.csv`'s hash is
  byte-identical between `experiments/20260713-r011-beta-profile-nesting/`
  (July) and today's `E5`/`E8` line — the underlying Moresco H(z) table has
  not silently drifted across 2 months, despite today's dead-URL bug (which
  only ever affected the *live-fetch* path, never the hardcoded fallback
  both lines use). Also confirmed: `data/hz_cc.csv` (27 rows, this
  project's own fetch) and `CC_POINTS` in `P176` (31 points, TJB's own
  hand-transcribed set) are two genuinely different tables used by two
  different pipelines — not a duplication bug, but worth keeping distinct
  in mind, since both are called "the CC data" in prose.
- **`sci-code-audit` (first run ever):** `CODE_AUDIT_HARDENING.md` — no
  STOP-level finding. Two follow-ups queued (`CLAUDE.md` test-count sync,
  now done; `conflict_resolver.py`/`source_provenance.py` wiring decision,
  queued below).

## 🟡 Open physics/process items — status and next step

### 1. Node radius circularity (v82 Sec. II.F)
**Status:** CLOSED per `docs/147`'s stop-rule — TJB's own diagnosed
circularity (`rho_crit(z)` = Friedmann equation), confirmed by this
project's `provenance_audit` chain (`E9`, `CIRCULAR` finding). No new
mechanism has been proposed since closure.
**Next step:** none recommended. Reopen only with a genuinely new
mechanism class, per the standing reopen condition.

### 2. H0,anchor circularity (v82 Sec. IV.M)
**Status:** CLOSED, same stop-rule. `kSZ` was tested as a candidate fix in
`E3` — found to relocate, not remove, the circularity — and is parked with
explicit revival conditions in `parked/`.
**Next step:** none recommended unless a `parked/` revival condition fires.

### 3. Propagate `E15`'s Jensen's-gap correction through a real β1/β2 re-fit
**Status: DONE 2026-09-06, `experiments/20260906-evidence-authority/
FINDING_E16_e15_propagated_through_refit.md`.** Turned out to be a
closed-form identity (chi2 minimum invariant under the reparametrization),
not a numerical re-fit — corrected this doc's own prior speculation.
Step 8a skeptic: `CONFIRMED-REAL` on the algebra, `WEAKENED` on the
"identifiability degeneracy" framing (it's a hidden-nuisance-parameter
structure, resolvable once σ is known — not a flat-valley degeneracy like
`(A,g,κ)`/`(β1,β2)`). Skeptic also found a real, un-checked scope gap:
`F0`/`F_accretion` are also nonlinear in `M(z)` and would carry their own
Jensen corrections, not absorbed by this claim's `β1,β2`-only scope —
logged in `pearl_registry/INDEX.md` (Caveat Gate).

**EstimandOps L0:** Descriptive/characterization — "how does this specific
already-published fit's parameters change under a stated, real correction
to one input's treatment," not a causal claim about MULTING's physics.

### 4. Unblock `E10` (second SNe-Ia example) via Taylor et al. 2023 SALT2/SALT3
**Status: DONE 2026-09-06, `experiments/20260906-evidence-authority/
FINDING_E10_ADDENDUM_taylor2023_unblocked.md`.** Turned out to need no
reconstruction at all — Taylor+2023 already publishes the per-object
comparison itself (308 common SNe Ia, DES-SN3YR). Real result:
`Δw=+0.001±0.005`, per-object μ agree to `≈0.1` mag (binned average
`≲0.01` mag), z-trend consistent with 0. This is ~2 orders of magnitude
smaller than Kessler+2009's `Δw≈0.20` (MLCS2k2 vs SALT-II) — the
fitter-choice risk shrank as the field converged on the SALT family.
Pearl Registry entry added (methodology-convergence pattern).

**EstimandOps L0:** Descriptive — comparing two published fitter outputs
on the same objects, not a causal claim.
**Status:** `BLOCKED` — VizieR's `DMe` column turned out not to be
SALT-II distance-modulus error as assumed; caught before being used
wrongly.
**Next step:** fetch Taylor et al. 2023's own per-object SALT2-vs-SALT3
table (real source, not VizieR's ambiguous column) and re-attempt the
two-fitter measurement `E10` was designed for.
**Estimated cost:** medium — depends on whether the per-object table is
actually machine-readable at the source; unverified until attempted.

### 5. Send the TJB reply (`correspondence/draft_tjb_reply_20260906.md`)
**Status:** drafted, ready, not sent. Separately gated per standing
constraint — requires its own explicit go-ahead, independent of any
physics work above.

## Infra follow-ups (from `sci-code-audit`, lower priority than physics)

- **`conflict_resolver.py`/`source_provenance.py` wiring decision:** these
  implement a symbol-precedence/conflict-resolution registry, tested but
  called by nothing else in the repo. Looks like it could close the
  "symbol registry" gap #2 named as open in `~/.claude/rules/research-
  methodology.md`, but was apparently built and never wired in. Decide:
  wire it into `provenance_audit.py`'s chain (natural fit — both are
  about tracking where a value's authority comes from), or explicitly
  mark it parked/superseded if it no longer matches current needs.
- **`docs/INDEX.md` resync:** last updated 2026-07-12, its numbered
  sections stop around doc 120 — docs 121-157 (including this one) are
  not indexed. A real, dated gap; a full resync is a separate, larger
  task than this pass's scope.

## Recommended priority, if any physics step is authorized next

**Items 3, 4, and `E16`'s own Pearl Registry follow-up are ALL DONE.**
`E16` (item 3): closed-form identity. `E17` (`E16`'s Pearl follow-up):
Jensen correction MATERIAL at `z≥1`, smaller than `F1,F2`'s own; a large
separate offset finding logged. `E17` itself then validated against
Correa+2015's own published values (`FINDING_E17_ADDENDUM`): `A_cosmo`
confirmed exact; cosmology choice confirmed negligible; but this
project's own `M0=6e14 M☉` found `6×` above Duffy+2008's own stated
calibration ceiling — a real, disclosed extrapolation risk concentrated
at exactly the high-`z` points the Jensen correction was `MATERIAL` at.
`E10` (item 4): unblocked via Taylor+2023 — modern fitter-shift risk
`~100×` smaller than the 2009-era citation `E6` first used. Items 1/2 are
closed and should stay closed absent new input. Item 5 (the letter) is
orthogonal to all of the above and can be decided independently at any
time.

**Item (a) is also now DONE — `FINDING_E17_ADDENDUM2`.** Correa+2015
Paper III's own cluster-valid concentration-mass relation replaces the
Duffy extrapolation; the offset divergence shrinks from `~5×` to `~1.8×`
(a 2nd Step 8a skeptic pass caught and fixed a real arithmetic error in
the first correction attempt). Two items remain explicitly open within
this thread (`σ`-sensitivity sweep; exclusion-fraction decomposition) —
named, not attempted.

**What's actually left, if anyone picks any of it up:** (a) the two
items just named inside the `E17` thread; (b) the TJB reply draft's
send decision. None authorized without a fresh explicit go-ahead.

## 2026-09-06, later same day — items (b)/(c) from the prior list closed

**Bottleneck-1 `ρ` coverage to `z≥1.07`:** bounded real literature
search (2 arXiv queries, 12 results, Tinker et al. 2010's own abstract
read) found no validated nonlinear/high-peak-height halo-bias extension
covering `ν=10.6-50` (v82's own 4 high-z target points). `SOURCE_NOT_
FOUND`, with an explicit physical reason (exponential rarity of
high-`ν` peaks vs. finite N-body simulation volume) — a legitimate null
result per this project's own standing rule ("a null literature search
can be a strong result if there's an explicit physical reason for the
absence"). Genuinely still blocked, consistent with `docs/156`'s own
2026-09-05 assessment, not contradicting it.
`FINDING_P195_ADDENDUM_high_z_bias_literature_search.md`.

**`P202`'s own named cluster-proxy meta-analysis:** done, corrected
after Step 8a skeptic. First-draft formal statistical comparison was
`WEAKENED` on 5 real grounds (all accepted); corrected, narrower
statement survives: `P197`'s own `2.5×`/`74.5%` caustic-vs-SZ
disagreement sits well outside the `4-26%` bias / `~12%` scatter range
spanned by real, independent, published WL-vs-X-ray comparisons —
reinforcing `P202`'s qualitative macro verdict without the disqualified
mechanism-specific sub-rule. `FINDING_P202_ADDENDUM_proxy_disagreement_
meta_analysis.md`.

**Only remaining named items:** the two open sub-items inside `E17`
(`σ`-sensitivity sweep; exclusion-fraction decomposition) and the TJB
reply draft's send decision (separately gated).
