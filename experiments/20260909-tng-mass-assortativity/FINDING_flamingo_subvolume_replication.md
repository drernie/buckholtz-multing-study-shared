# FINDING — FLAMINGO 27-subvolume replication: INCONCLUSIVE, and the
# headline "0/10" is itself not evidence — badly underpowered, plus
# two real, unquantified design biases both pointing toward zero

**Continues:** `CLAIM_flamingo_subvolume_replication.md` (committed
BEFORE the script ran) → `FINDING_tng300_own_population_rho_nn_and_
band.md`'s own named next step ("independent replication in a larger,
genuinely different volume"). **User-requested.**
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Result (real, live `hdfstream` data, 27 non-overlapping TNG300-
## sized sub-cubes carved from FLAMINGO's real 1000 Mpc box)

```
Sub-cubes matched (geometric criterion found a local N): 10 / 27
rho_NN distribution (n=10): mean=0.0145, SD=0.2069
  min=-0.2723, max=0.2902
|rho_NN| >= 0.42 (matches TNG300's own N=35 anomaly): 0 / 10 (0.0%)
SE of the mean: 0.0654
```

## Independent skeptic review (Step 8a, context-blind) — six questions

Full text preserved in the session record. **Every quantitative claim
in the skeptic's own report was independently re-derived before use**
(`audit-verification-gate.md`) — all of them confirmed exactly (two-
sided tail at `z=2.06`: `3.95%`; `P(0/10)`: `66.8%`; exact `95%` upper
bound on the tail rate given `0/10`: `25.9%`; `chi^2` `95%` CI on the
true SD given `n=10, s=0.207`: `[0.142, 0.378]`).

1. **Selection bias between matched and unmatched sub-cubes
   (`WEAKENED`).** The `17` unmatched sub-cubes are NOT explained by
   having too few halos (their `n_avail` range overlaps the matched
   ones' entirely). Matching depends on the local NN-separation-vs-`N`
   PROFILE landing in the target window at some candidate `N` — a
   property of local clustering strength. **A real, unaddressed
   concern**: the `10` matched sub-cubes may be a density-filtered,
   non-representative sub-sample of FLAMINGO's own large-scale
   structure, not a fair draw — and local clustering strength is
   plausibly not independent of the mass-mass correlation question
   itself. Not quantified in this test.
2. **Artificial local-periodic treatment (`WEAKENED`, with a named
   directional bias).** Each sub-cube's own minimum-image NN
   calculation can, for an edge halo, substitute an unrelated,
   spuriously-"close" neighbor from the wrapped opposite face for the
   halo's TRUE physical nearest neighbor (which may lie in an adjacent,
   excluded sub-cube). Given the target NN scale (`~40-45` Mpc) is a
   substantial fraction of the `302.6267` Mpc sub-cube side, this
   affects a large fraction of the volume, not an edge case. **Two
   predictable, same-direction effects**: (a) apparent NN separations
   are systematically SHORTENED (biasing the matched local `N` lower
   than a genuinely independent box of that size would need), and (b)
   many "nearest neighbors" identified this way are effectively random
   pairings, DILUTING `rho_NN` toward zero relative to whatever a truly
   independent box would show. **Not bounded in this test** — the
   concrete, cheap fix (rerun with open/non-periodic boundaries per
   sub-cube, compare) is named, not attempted here.
3. **Tie-break rule integrity (`CONFIRMED-REAL`).** Directly re-read:
   `pick_local_n` scores candidates using ONLY `median`/`mean` NN
   separation; `rho_NN` is computed only AFTER a local `N` is already
   selected, in the caller. The geometric selection genuinely cannot
   see the correlation it will later produce. Matches the claim's own
   pre-specified design exactly.
4. **SD agreement (`WEAKENED`).** Empirical SD (`n=10`): `0.207`,
   TNG300's own permutation-null SD: `0.204`, analytic `1/sqrt(N-2)`
   at `N=35`: `0.174`. Point-estimate agreement looks striking, but the
   `95%` CI on the TRUE underlying SD given only `10` draws is
   `[0.142, 0.378]` — wide enough to be consistent with `-0.42` being
   anywhere from a `~2%` to a `~15%`-or-more tail event. The agreement
   is suggestive, not a confirmed match.
5. **Is `0/10` evidence of anomaly (`FALSIFIED` — the single most
   important correction)?** Under the shared noise floor this test
   itself estimates (`SD~0.20`), TNG300's `-0.42` is a `~4%` two-sided
   tail event. **`P(0` exceedances in `10` independent draws `| tail
   rate=3.95%) = 66.8%`** — observing exactly zero is the MOST LIKELY
   outcome even if TNG300's result is ordinary noise. The exact `95%`
   upper bound on the true tail rate given `0/10` is `25.9%` — the data
   are equally consistent with a `4%` tail rate and a `20%` tail rate.
   **`0/10` is not evidence for the noise-explanation; it is simply
   what an underpowered test looks like.** Reaching real power against
   a `~4%` tail hypothesis would need roughly `n>=74` independent draws
   (Poisson-rule-of-thumb, expected `>=3` events at `80%` power) — this
   test has `10`, a shortfall of roughly `7x`.
6. **Overall honest verdict (`WEAKENED` toward `INCONCLUSIVE`).**
   Neither (a) "TNG300's result is ordinary small-`N` noise" nor (b)
   "TNG300's result is a genuine anomaly" is established. (a) is
   consistent with the data but not confirmed by it (per item 5); (b)
   is not positively supported, but the two named design biases (items
   1-2) both push toward UNDER-detecting a real signal if one exists,
   so "no anomaly seen" is not a clean finding either.

**Response (Step 8a matrix): all six points accepted, none dismissed.
Item 5 in particular corrects a real overclaim risk — the raw "0/10"
headline, taken at face value, would have repeated the SAME class of
error (a null result treated as informative without checking its own
power) already caught twice earlier in this branch (the withdrawn
"13 sigma" claim, the "just outside the 99% CI" over-read) — caught
here BEFORE it was written into any conclusion, not after.**

## What this DOES establish

- **A real, working design for carving genuinely independent, TNG300-
  sized sub-volumes out of a much larger simulation, using the SAME
  blind selection protocol as every prior test in this branch** — `10`
  of `27` sub-cubes yielded a usable, honestly-blind local match. This
  is a reusable capability for any future test needing more independent
  small-`N` draws than a single simulation box can offer.
- **The empirical noise floor this test measures (`SD~0.21`, `n=10`) is
  broadly consistent with (not confirmed identical to) TNG300's own
  permutation-null and analytic SDs** — no evidence FLAMINGO's small-`N`
  noise floor is dramatically different from TNG300's.
- **The test is genuinely underpowered to say whether TNG300's
  `-0.42` is rare or common** — `n=10` independent draws cannot
  meaningfully discriminate a `~4%` tail rate from a `~25%` one.
- **Two real, named, unquantified design biases (environmental
  selection of which sub-cubes match; periodic-wrap dilution toward
  zero) both plausibly push this test's own results toward `0`** —
  meaning even the (weak) `0/10` headline may be partly an artifact of
  the method, not purely a statement about the underlying physics.

## What this does NOT establish

1. Does NOT confirm TNG300's `-0.42` is ordinary sampling noise.
2. Does NOT confirm TNG300's `-0.42` is a genuine, TNG300-specific
   anomaly.
3. Does NOT bound the size of the periodic-wrap dilution bias — named,
   not quantified. The cheap fix (open-boundary comparison per
   sub-cube) is not attempted here.
4. Does NOT check whether matched and unmatched sub-cubes differ
   systematically on an outcome-independent clustering statistic — the
   cheap fix (compute a fixed-`N` NN statistic regardless of band-
   matching, compare matched vs. unmatched) is not attempted here.
5. Does NOT resolve Hypothesis A vs. B from the FLAMINGO addendum
   (that question concerns `rho_band`, separate from this test).
6. Not a claim about v82's own theory (`NO_AUTHOR_ERROR`).

## Status

**Genuinely INCONCLUSIVE — and the specific value of this test is
methodological, not (yet) a resolved physics answer.** The most
important result is procedural: a null-looking "0/10" headline was
caught and correctly downgraded to "uninformative, given its own power"
BEFORE being written up as a finding, via the same context-blind
skeptic discipline that caught two related overclaims earlier in this
branch. The concrete next steps this test itself names (relax the
band or use a jittered grid for more matched sub-cubes; quantify the
periodic-wrap bias via an open-boundary comparison; check matched-vs-
unmatched selection bias directly) are real, cheap, and not yet run.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
