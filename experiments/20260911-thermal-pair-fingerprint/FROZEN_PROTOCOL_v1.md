# FROZEN PROTOCOL v1 — thermal-pair kSZ fingerprint, first real-data
# pre-registered test

**Written and committed BEFORE running the test this file governs.**
Per this project's own Falsification Ladder (Step 2b, Oracle Adequacy
Gate) and Perelman-audit "Promotion Rule": a result is only evidence if
the criteria that judge it were fixed before the result existed. This
file is that fixing. Once committed, `final_frozen_test.py` may be RUN
against it, but neither this file's criteria nor the pipeline it points
to may be edited in light of the result — any change after looking
requires a new, separately-named test (v2), not a silent amendment here.

**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`

---

## 1. Exactly what pipeline is frozen

- **Cluster population:** real ACT-DR5 MCMF catalog (arXiv:2406.14754),
  `z ∈ [0.2, 0.8]`, all clusters landing inside the ACT footprint —
  4390 real clusters, per `_load_real_cluster_positions()` in
  `run_real_data_phase2.py`. No further cuts.
- **Map:** ACT DR6.02 f150 GHz, `map_srcfree` variant (≥5σ point
  sources pre-subtracted by the ACT team) — `act_dr4dr6_coadd_AA_
  night_f150_map_srcfree.fits`, `[VERIFIED]` 5,349,890,880 bytes.
- **Extraction:** `real_map_extraction.extract_cluster_temperatures`,
  1′ aperture radius, raw pixel mean (no repixelization) — code as it
  stands at commit `a88075e`.
- **Beam correction:** `beam_correction.apply_beam_correction`, FWHM=
  1.4′ at f150 (`[VERIFIED-arXiv:2406.14754]`), multiplier 1.3210×,
  applied uniformly to every cluster's extracted T before anything
  else.
- **Outlier safety net:** MAD-based, 8σ robust threshold (see
  `run_real_data_phase2.py` STEP 2b) — applied before the estimator.
- **Estimator:** `pairwise_ksz_estimator.core_pairwise_estimator`
  (Hand et al. 2012 Eqs. 1-3), `q = -T` (N_kSZ=1, raw units — no
  physical-velocity conversion attempted, N_kSZ is unknown).
- **Bins:** 7 quantile bins on the real pairwise-separation
  distribution (equal pair count per bin by construction), same method
  as every prior run this session.
- **Detrending:** in addition to the raw result, a quadratic T(z) fit
  is subtracted and the SAME estimator re-run on the residual — both
  numbers are reported, per §3 below, not just the more favorable one.

**Frozen git commit for this pipeline: `a88075e`** (the commit that
closed both the point-source and beam-matching gaps). This protocol
file itself is committed separately, immediately after, with a later
hash — that later hash is the actual freeze point; `a88075e` names
which CODE version is frozen.

## 2. What is explicitly NOT in scope for this test

- No τ-weighting (mass-independent, per `pairwise_ksz_estimator.py`'s
  own module docstring — a real SNR improvement, not required for a
  detection statistic).
- No conversion to physical velocity (N_kSZ unknown).
- No re-tuning of bins, aperture radius, or outlier threshold based on
  this run's own result.

## 3. PROMOTE / REJECT / INCONCLUSIVE — fixed before the result exists

Report BOTH the raw (beam-corrected, outlier-flagged) result and the
z-detrended result, in the same table, always — never only the more
favorable one.

**PROMOTE** requires ALL of the following, jointly:

1. **Statistical significance on RAW data:** at least the two smallest-
   separation bins have |z| ≥ 3.
2. **Correct sign:** those same bins are NEGATIVE (pairwise infall —
   the physically expected direction per Hand et al. 2012, `p_pair(r)`
   negative for approaching pairs).
3. **Correct shape — NOT the artifact signature:** the bin of maximum
   |p_pair| is NOT the largest-separation bin. (This project's own
   2026-09-12 finding showed that a spurious, monotonically-GROWING-
   with-r signal is exactly what the redshift-selection artifact
   produces — a real infall signal should peak at small-to-moderate
   `r` and not still be growing at ~4800 Mpc, a scale with no genuine
   causal/gravitational connection between pairs.)
4. **Survives detrending:** after subtracting the T(z) trend, the same
   two smallest-separation bins retain |z| ≥ 2 (a deliberately relaxed
   bar vs. raw data's ≥3 — detrending trades some real signal for
   confound removal, per `FINDING_first_real_data_run_tsz_selection_
   confound.md`'s own honest accounting — but must not collapse to
   consistent-with-zero the way the earlier artifact did).

**REJECT** if the raw result fails condition 1 or 2 outright (no
significant, correctly-signed small-r signal at all).

**INCONCLUSIVE** — the honest middle ground, and the single most likely
outcome given this pipeline is not the final word (no τ-weighting, no
DR6-native beam/point-source products, N=4390 not survey-scale) — if:

- Condition 1-2 pass but condition 3 fails (shape matches the known
  artifact signature again — strong prior this is the SAME confound or
  a sibling one, requires new diagnosis, not a kSZ claim), OR
- Condition 1-2 pass, condition 3 passes, but condition 4 fails (signal
  present in raw data but does not survive the same detrending
  discipline already established as necessary for this dataset), OR
- Bins 1-2 fail condition 1 (not ≥3σ) but show a suggestive, correctly-
  signed, non-artifact-shaped sub-3σ pattern (worth a larger sample,
  not worth a verdict).

**Whatever the result, this test alone — regardless of verdict — does
NOT establish or refute MULTING.** Per `docs/151`'s own status-
separation rule and this file's own §2: no τ-weighting, no DR6-native
beam paper, N=4390 (not the full potential real sample), single
frequency band, no independent replication. A PROMOTE verdict here
would mean "proceed to the harder remaining work with real grounds for
optimism," not "kSZ detected" and certainly not "MULTING supported."
A REJECT or INCONCLUSIVE verdict would mean "this specific pipeline, at
this sample size, does not yet show a clean signal" — not "MULTING is
wrong."

## 4. Skeptic pass

Per Step 8a (Context Asymmetry Rule): after `final_frozen_test.py` runs
and this file's own criteria are mechanically applied to produce a
verdict, an independent context-blind `Agent(skeptic)` review is
required before the verdict is reported as final — given ONLY this
file's criteria + the actual numeric output, not this session's
reasoning chain. This matches the discipline already applied to the
kSZ estimator's own code (Phase 1) and is not optional here.
