# FINDING — classical pairwise-kSZ estimator, Phase 1 (Fork 1b)

**Continues:** `data_acquisition_plan.md` Fork 1, option 1b ("re-implement
the classical pairwise-momentum kSZ estimator from scratch").
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`
**Scope of this file:** Phase 1 only — build and validate the estimator
*math* on synthetic data with known ground truth. Phase 2 (real ACT DR6
map + real DESI DR1 catalog + full-scale run) is separate, not started,
not costed differently than `data_acquisition_plan.md` already costed it
("~1-3 weeks", the dominant line item in that plan).

---

## What this corrects in `data_acquisition_plan.md`

That file's own ingredient table (item 2, "Access" column) said the kSZ
pairwise estimator reuses "Same `y`-map (#1)" — the ACT Compton-y map
used for the tSZ ingredient (item 1). **That is wrong for the classical
estimator.** Verified before writing any code, not assumed from memory:
Hand et al. 2012 (arXiv:1203.4219, `[VERIFIED]` via `mcp__arxiv__
download_paper`, full text read directly) use the ACT **148 GHz
brightness TEMPERATURE map** — kSZ is a frequency-independent
*temperature* distortion, physically distinct from tSZ's frequency-
dependent spectral distortion (which the y-map isolates). Their own
text: *"we treat the effective microwave temperature at 148 GHz measured
by ACT in the direction of the cluster as a noisy estimator of the
cluster's line-of-sight momentum."* The pairwise-difference statistic
(Eq. 2) is insensitive to tSZ/dust/noise by construction — those
components don't correlate with pair-separation direction — so no y-map
subtraction is needed for the basic estimator. The real-data phase will
need ACT DR6's coadded temperature-map product, not
`ilc_actplanck_ymap.fits`. `data_acquisition_plan.md`'s own item-2 row
has been corrected in place, cross-referencing this file.

---

## What was built

`pairwise_ksz_estimator.py` — the Hand et al. 2012 mean-pairwise-momentum
estimator (their Eqs. 1-3), transcribed directly from the paper's own
arXiv HTML source, not re-derived:

```
p_pair(r) = < (p_i - p_j) . r_hat_ij >

p_tilde_pair(r) = sum_{i<j} (q_i - q_j) c_ij / sum_{i<j} c_ij^2

c_ij = r_hat_ij . (r_hat_i + r_hat_j)/2
```

- `core_pairwise_estimator()` implements Eq. 2-3 exactly, generic in the
  caller's chosen line-of-sight-momentum proxy `q_i`, with delete-one-
  cluster jackknife error bars (the statistically correct choice here,
  since pairs sharing a cluster are not independent — a per-pair
  bootstrap would understate the error).
- `pairwise_momentum_from_temperature()` is a thin wrapper implementing
  the paper's own `T_kSZ,i = -N_kSZ * q_i` sign convention, kept
  separate so the core formula stays auditable line-by-line against the
  paper independent of any T-vs-q unit question.
- `toy_infall_velocity()` is an explicitly-labeled **positive-control
  signal generator, not physics** — a softened 1/r² pairwise toy
  attraction, guaranteeing coherent infall by construction.

Real (RA, Dec, z) positions are reused from `exact_pair_census.py`
(ACT-DR5 MCMF, arXiv:2406.14754), restricted to this experiment's own
established `z ∈ [0.2, 0.8]` working range (`Z_LOW`/`Z_HIGH`, same as
every sibling script in this folder) — the line-of-sight momentum field
itself is synthetic and ground-truth-known; no real ACT temperature map
has been touched.

## Validation results (N=300 real cluster positions, 7 quantile bins)

| Check | Result |
|---|---|
| Negative control (pure Gaussian noise `q`) | max &#124;z&#124; = 1.91 across 7 trusted bins (n_pairs=6407 each) — clean, no spurious signal |
| Positive control (toy softened infall) | correct (negative/infall) sign recovered in **7/7** bins, growing significance with separation (z = -8.2 to -2.5) |
| T↔q sign-convention round-trip | exact, max difference 0.00e+00 |
| Independent context-blind code review (`Agent(skeptic)`, given only the paper's Eqs. 1-3 + the raw code, no session context) | **CONFIRMED** — 8 checks (c_ij sign convention, q_diff sign consistency, no pair double-counting, diagonal safety, two-sided jackknife exclusion, T-sign-convention literal match, infall-force sign, binning off-by-one) all passed, no sign or index bug found |
| Independent spot-check of the review's own transcription (per `audit-verification-gate.md` — an agent's `[VERIFIED]` is this session's `[INFERRED]` until re-checked) | re-read the two sign-critical lines directly (`q_diff = q[:,None]-q[None,:]`, `diff_pos = pos[:,None,:]-pos[None,:,:]`) — matches the reviewer's report exactly |

**One methodological correction made mid-build, worth recording:** the
first run used fixed-width 20 Mpc bins and got 1-2-pair bins at small
separation, producing meaningless jackknife z-scores (up to ~10¹³, an
artifact of near-zero jackknife variance on a 1-pair bin, not a real
signal). Fixed by switching to quantile-based bin edges on the real
pairwise-separation distribution (equal pair count per bin by
construction) and gating any z-score report on `n_pairs >= MIN_PAIRS_
PER_BIN=30` (same discipline as `power_analysis_s_dependent.py`'s own
`MIN_STRATUM_N`). This is a statistics-validity fix, not an estimator
bug — the underlying formula was already correct in both runs.

Pre-commit checklist (`CLAUDE.md`, mandatory for non-trivial changes):
`ruff check` clean, full project test suite (991 tests) green
(unaffected — this is a new, standalone experiment-folder script, no
`src/`/`tests/` touched), independent reviewer pass CONFIRMED.

---

## What this does NOT establish

1. **Not a real-data kSZ detection.** Everything above uses a synthetic,
   ground-truth-known `q_i` — no real ACT temperature map or real DESI
   catalog cross-match has been performed.
2. **Not that the real-data run will detect anything.** The synthetic
   battery validates that the CODE correctly implements the published
   FORMULA — it says nothing about whether a real kSZ signal is
   detectable at this project's target sample size (that question
   belongs to `estimand.md`'s own synthetic four-world battery /
   power-analysis machinery, already run on a different, s-dependent
   design; this estimator has not yet been run through that machinery).
3. **Not a complete implementation.** No optical-depth weighting (used
   by later, more sophisticated pairwise-kSZ papers, e.g. Schaan et al.
   2021, to improve SNR), no beam/filter matching to real ACT DR6 map
   properties, no real per-cluster temperature extraction. The basic
   Hand et al. 2012 estimator implemented here does not require τ
   weighting for the core detection statistic — that is a real,
   separate upgrade, not yet built.

## Status

**Phase 1 (estimator math) DONE, validated.** Phase 2 (real ACT DR6
temperature map, real DESI DR1 cross-match, full-scale run) is the
genuinely multi-day-to-multi-week remainder `data_acquisition_plan.md`
already costed — not started, not authorized without a separate
go-ahead (multi-GB downloads, real compute time). Fork 1a (data request
to Gong/Bean) remains the parallel path, independent of this one.
