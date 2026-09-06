# FINDING E18 — an outside party re-executes and extends TJB's own
# already-archived, independently-implemented verification script
# across all 7 Table II rows and a wide, multi-seed global search —
# answer to Ernest Prabhakar's item 6, corrected after Step 8a skeptic

**Date:** 2026-09-06
**Trigger:** TJB's forwarded email thread (Ernest Prabhakar's 6-point
critique paused a press release; item 6 names Sergey explicitly as
someone who could reproduce the fit; TJB's own email asks Sergey
directly whether he has done or can do this).
**Explicit go-ahead given**, scoped to item 6, "максимально скурпулезно."

## Step 8a skeptic — context-blind, claim + code + full output — verdict:
## WEAKENED, 4 real points, all corrected in place, none dismissed

Before presenting this as final, a context-blind skeptic pass reviewed
the first draft. It found the core computation real and correct, but
the FRAMING overreached on 4 points — corrected below, not glossed over:

1. **"Outside party independently REPRODUCES" overclaimed what was
   done.** The physics code (`force_terms`, `H_of_z_vec`, `chi2_of`) is
   TJB's own archive's already-independently-*implemented* script,
   byte-identical up to whitespace — this project did not re-derive the
   physics from the paper's description; it re-executed TJB's own
   already-written independent script in a different environment and
   extended it with a new global-search wrapper. **Corrected framing**:
   this is "an outside party re-executes and extends TJB's own
   already-archived, independently-implemented verification script" —
   not "independently reproduces" as a from-scratch reimplementation.
   The value is real (see below) but narrower than the first draft's
   title claimed.
2. **"Genuinely wide" global search was actually ~1 log-decade centered
   on the known answer** (`β1∈[0.3,3.0]×10¹⁰`) — not disclosed
   explicitly, and narrow enough that a skeptical reader could suspect
   it was tuned to guarantee finding the known point. **Corrected**:
   widened to 2 orders of magnitude on `β1` (`1×10⁹`–`1×10¹¹`) and 3 on
   `β2` (`1×10¹⁶`–`1×10¹⁹`), and re-run across **3 independent seeds**
   (`20260906, 1, 2`) instead of one — both now stated explicitly in
   the results, not asserted as "wide" without support.
3. **"Diff-verified" was self-reported by the same session that made
   the edit.** **Corrected**: the actual `diff` output is saved as a
   real artifact file, `independent_verification_rerun/path_fix_
   diff.txt`, inspectable independently of this write-up's own claims.
4. **"All 7 rows verified" was misleading — only the free row had been
   independently re-optimized; the other 6 were only forward-evaluated
   at TJB's own already-reported `(β1,β2)`, which is closer to
   confirming the `χ²` FUNCTION matches (environmental/platform
   equivalence) than to confirming an independent OPTIMIZER recovers
   those values.** This is the most substantive point. **Already
   self-caught and closed before the skeptic's verdict arrived** — an
   independent 2D re-optimization (no starting guess, blind global
   search) was added for all 6 fixed-`H0,anchor` rows (Part A2 below),
   run in parallel with the skeptic dispatch. Reported here as a
   genuine self-correction, not credited as if the skeptic caught it.
5. **"First time" language softened**: TJB's own archive already
   contains an internal independent-AI reproduction; this is the first
   execution **outside Dr. Buckholtz's own commissioned process**, not
   the first independent verification in an absolute sense.

**No point dismissed.** All 5 addressed in the code, the re-run output,
and this write-up — per this project's no-silent-correction discipline.

## Provenance (Gate 1, checked before touching anything)

- Source: `data/source_material/zenodo_21204955_supplemental/
  process_documentation/independent_verification/multing_fit.py` +
  `code/assumptions.yaml` — this archive's own `INDEX.md` already
  establishes Gate 1 identity (Zenodo 21204955, `isSupplementedBy` on
  22004287, SHA256-verified, 2026-09-02).
- SHA256 hashed BEFORE any copy/edit, this session: `multing_fit.py =
  377b49af...`, `assumptions.yaml = f469582e...`.
- Real, external diff artifact: `independent_verification_rerun/
  path_fix_diff.txt` — confirms every formula, constant, and numeric
  literal is byte-identical between the archived original and this
  project's rerun copy; the only substantive change is import/path
  resolution (`open("/tmp/assumptions.yaml")` → resolved relative to
  the script's own directory, since bash's `/tmp` and native Windows
  Python's `/tmp` resolve to different locations on this machine), plus
  ruff's automatic whitespace/PEP8 reformatting. The module-level
  refactor needed so `E18_all_rows_and_global_search.py` can import
  `chi2_of`/`H_of_z_vec` is a structural (not physics) change, noted
  explicitly per skeptic point 3.

## What was already known, and what this closes

TJB's own archive already documents an internal "genuinely independent
AI session (a different tool, fresh conversation, given only
`regenerate_prompt.md`'s prompt and `assumptions.yaml`, no access to
`multing_core.py`)" that wrote `multing_fit.py` from scratch and
reproduced the headline row — this project's own `INDEX.md` already
recognized this as the strongest Independent Verification Strength
Ladder tier ("Different model") encountered for any MULTING claim. That
verification was run within TJB's own process. `FINDING_P176`
(2026-08-31) is this project's own prior reproduction, but reuses TJB's
own `multing_core.py` functions verbatim and named its own gap: only 2
of 7 rows checked, only local re-optimization from one nearby guess.

**What this finding actually adds, stated at its corrected scope:** TJB's
own already-independently-implemented script, re-executed by an outside
party in a different environment (closing an environmental-
reproducibility gap TJB's own single-session run did not close), with
two genuinely new checks: an independent 2D re-optimization (no
starting guess) for all 6 fixed-`H0,anchor` rows, and a wide, multi-seed
3-parameter global search for the free row.

## Results

**Part 1-3 (archive's own script, run fresh, by us):**
```
beta_1     = 1.433479e+10
beta_2     = 7.806760e+17
H0_anchor  = 73.2160 km/s/Mpc
chi2_33    = 15.7515
r_33       = 0.9659
```
Matches, to every digit, the numbers TJB's own archive `INDEX.md`
claims its internal independent AI session got. Against the paper's own
rounded Table II (`73.22, 15.75, 0.9659`) — matches to stated precision.

**Part A — χ² at all 7 Table II rows' own published triples (forward
evaluation — confirms the function, not an independent optimization for
6 of the 7 rows; see Part A2):**
```
row                            chi2 (ours)  chi2 (stated)   rel diff
unconstrained_spotlighted          15.7516        15.7500     0.010%
sh0es_anchored_0pct                15.7809        15.7800     0.006%
pct_25                             18.1357        18.1400     0.023%
pct_50                             24.2555        24.2600     0.018%
pct_75                             34.1357        34.1400     0.013%
pct_90                             41.9065        41.8700     0.087%
planck_exact_100pct                47.7714        47.7700     0.003%
```
Max relative difference: **0.087%**, under the pre-registered `1%` MCID.

**Part A2 — independent 2D re-optimization (no starting guess) for the
6 fixed-`H0,anchor` rows, closing Part A's own forward-evaluation-only
limitation:**
```
row                       chi2 reopt  chi2 stated      diff  b1 shift%  b2 shift%
sh0es_anchored_0pct          15.7808      15.7800    0.005%     0.003%     0.000%
pct_25                       18.1357      18.1400    0.024%     0.003%     0.001%
pct_50                       24.2555      24.2600    0.018%     0.002%     0.001%
pct_75                       34.1357      34.1400    0.013%     0.001%     0.000%
pct_90                       41.9065      41.8700    0.087%     0.019%     0.022%
planck_exact_100pct          47.7713      47.7700    0.003%     0.003%     0.001%
```
All 6 rows independently re-derive `β1,β2` from a blind global search
(bounds 2/3 orders of magnitude wide, no nearby starting guess) to
within `0.022%` of the published values.

**Part B — wide, multi-seed 3-parameter global search on the free
(`unconstrained_spotlighted`) row:**
```
bounds: beta_1 in (1e9, 1e11), beta_2 in (1e16, 1e19), H0_anchor in (55, 90)
seeds: (20260906, 1, 2)
  seed=  20260906: beta_1=1.433479e+10  beta_2=7.806760e+17  H0_anchor=73.2160  chi2=15.7515
  seed=         1: beta_1=1.433479e+10  beta_2=7.806760e+17  H0_anchor=73.2160  chi2=15.7515
  seed=         2: beta_1=1.433479e+10  beta_2=7.806761e+17  H0_anchor=73.2160  chi2=15.7515
chi2 spread across 3 seeds: min=15.7515  max=15.7515
Global-optimum (beta_1,beta_2) vs published: 0.00% / 0.00% away
```
All 3 independent seeds converge to the same point, across a bound
spanning 2-3 orders of magnitude — not a narrow neighborhood tuned to
find the known answer. No lower minimum found; no distinct degenerate
solution surfaced. A `RuntimeWarning: invalid value encountered in
sqrt` appeared during the search — expected and handled: some trial
points in the wide bound produce unphysical `H²<0`, `chi2_of` returns
`NaN`, the objective maps that to a `1e12` penalty, steering the
optimizer away — confirmed not to corrupt the converged result.

## Controls

- **Positive control**: PC1, the unconstrained_spotlighted row
  reproduces to `<1%` — PASS (actual: `0.010%`).
- **Negative control**: NC1, perturbing `Om_planck` from `0.315` to an
  obviously-wrong `0.05` changes `χ²` by `>50%` — PASS, confirms genuine
  computation from inputs, not a cached/hardcoded number.

## Verdict

**MCID: NOT MET on either axis — no material discrepancy**, at the
corrected scope stated above. All 7 rows independently re-optimize (not
merely forward-evaluate) to within `0.087%`; a wide, multi-seed global
search finds no missed minimum and no undiscovered degenerate solution.

## What this does and does NOT establish

**Does establish:** the numbers in v82's Table II are exactly what the
archived, independently-*implemented* code (written by an AI TJB
himself commissioned, not by this project) computes — re-executed and
extended, for the first time outside TJB's own commissioned process,
across the full table, with independent re-optimization (not just
forward evaluation) for every row, and a wide, multi-seed global search
finding nothing TJB's own search missed. This is a real, useful, but
NARROWER answer to Ernest's item 6 than "this project independently
reproduced v82's fit from scratch" would claim — and should be reported
to TJB/Ernest with that narrower, accurate framing.

**Does NOT establish:**
1. Whether MULTING is physically correct — `NO_AUTHOR_ERROR`. Empirical/
   Model-status-only claim per `docs/151`'s Status Separation Rule.
2. Whether the fit is scientifically meaningful — AIC/BIC (item 1,
   `FINDING_P166`), node-radius circularity (item 2, `FINDING_E9`/
   `P199`), T0-vs-cluster-temperature tension (item 5, `FINDING_T0_is_
   not_free`) are separate, already-answered items.
3. An exhaustive, mathematically-certain proof that no other minimum
   exists anywhere in an unbounded parameter space — a wide, finite,
   multi-seed search is strong evidence, not exhaustive proof.
4. That the physics itself was independently re-derived from the
   paper's description — the physics code is TJB's own archive's
   already-independently-implemented script, re-executed and extended,
   not re-written by this project from scratch.
5. Anything about the OTHER 5 critique items — this closes item 6 only.

## Pearl Registry / next step

None named for this thread — item 6 is closed at its corrected scope.
The natural next FL step (per the user's own stated sequence) is item 3
(whether the phantom-crossing H(z) minimum is data-supported or
extrapolation-only), genuinely new, unexplored territory for this
project.
