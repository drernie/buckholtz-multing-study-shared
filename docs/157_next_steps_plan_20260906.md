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
**EstimandOps L0:** Descriptive/characterization — "how does this specific
already-published fit's parameters change under a stated, real correction
to one input's treatment," not a causal claim about MULTING's physics.
**Status:** named, not done. `E15` computed the force-TERM-level
correction (+12.8%/+61.6%) but explicitly declined to claim a β1/β2 shift,
since `H(z)` is nonlinear in `F_total` and `E8`/`E11` already found a real
(β1,β2) near-degeneracy — a naive per-term rescale would not respect it.
**Next step (cheapest form):** reuse `E8`'s own `hessian_small_eig_and_slope`
machinery, but replace the point-evaluated `F1,F2` inside `H_of_z_kms`
with population-averaged versions (multiply by `exp(σ²/2)`/`exp(2σ²)`
respectively, at `E13`'s real σ=0.49) BEFORE optimizing, then re-run
`E8b`'s own re-optimization. Bounded, well-specified, reuses only existing
tested machinery — no new physics assumption beyond what `E15` already
flagged as open (Reading A vs B of "representative value").
**Estimated cost:** small — one new script following the `E8b` pattern.

### 4. Unblock `E10` (second SNe-Ia example) via Taylor et al. 2023 SALT2/SALT3
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

Per the Cheapest Differentiating Test Protocol (`falsification-ladder.md`):
item **3** (E15 propagation) is the cheapest and most differentiating — it
reuses only already-tested machinery, has a fully bounded scope, and
directly closes a gap this project itself named twice (`E15`'s own "next
step, named not done"). Item **4** (E10/Taylor) has unknown cost until the
source is actually checked. Items 1/2 are closed and should stay closed
absent new input. Item 5 (the letter) is orthogonal to all of the above and
can be decided independently at any time.
