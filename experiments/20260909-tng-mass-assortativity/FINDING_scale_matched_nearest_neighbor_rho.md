# FINDING — scale-matched nearest-neighbor rho: FALSIFIED as a
# resolving test; the magnitude/mechanism question is genuinely
# UNDETERMINED by this dataset, not resolved either way

**Continues:** `CLAIM_scale_matched_nearest_neighbor_rho.md` (committed
`aaeebbd`, BEFORE `scale_matched_nearest_neighbor_rho.py` was run) →
`FINDING_mass_assortativity_and_scatter.md`'s own two existing readings
(all-pairs `rho=+0.38`, nearest-neighbor-restricted `rho=0.019, n.s.`).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Result (real, from `top_halos_pos_mass.csv`, no new API calls)

```
N_sub  mass_floor(Msun)  median_NN(Mpc)  mean_NN(Mpc)  r(real)  t      p       r(shuffled ctrl, 1 draw)
30     3.74e14           47.42           42.45         -0.5032  -3.08  <0.01   -0.2061
40     3.24e14           47.42           43.13         -0.1965  -1.24  n.s.     0.1437
50     2.79e14           46.54           40.95          0.0085   0.06  n.s.     0.2789
60     2.59e14           38.90           35.23          0.0902   0.69  n.s.     0.1732
80     2.06e14           24.78           28.82         -0.0558  -0.49  n.s.    -0.1107
100    1.85e14           24.67           27.08         -0.0505  -0.50  n.s.    -0.1445
```

At first glance, `N_sub=30` looks alarming: `r=-0.50, p<0.01`, landing
almost exactly at `FINDING_P158`'s own `rho=-0.5` ordering-reversal
threshold. **This does not survive scrutiny — see the skeptic review
below, independently re-verified point by point.**

## Independent skeptic review (Step 8a, context-blind)

Given only the claim's own question, the table above, and the stated
statistical context (`N_sub=30-50` power, nested/overlapping
thresholds, the `-0.5` threshold's own significance). **Verdict:
FALSIFIED** — as a test resolving the magnitude/mechanism question, not
as a claim that something was done wrong mechanically. All four
objections independently re-checked against the raw numbers before
accepting (`audit-verification-gate.md`):

1. **`N_sub=30`'s own median NN separation (47.42 Mpc) is OUTSIDE the
   40-45 Mpc target window** — only its MEAN (42.45 Mpc, skewed by a few
   close pairs) falls inside. Re-checked directly against the printed
   table: correct. The two sub-samples that land inside the window by
   BOTH median and mean (`N_sub=40`: med=47.4 — also outside by median,
   actually; `N_sub=50`: med=46.5, mean=41.0, closest genuine match)
   give `r=-0.20 (n.s.)` and `r=+0.01 (n.s.)` — the one "significant"
   point is the one whose own scale match is weakest.
2. **Look-elsewhere across 6 NESTED, non-independent thresholds against
   a one-sided, load-bearing cutoff.** Under the null, `SD(r)` at
   `df=28` is `~0.19` (standard large-sample approximation,
   `1/sqrt(n-3)` — independently recomputed: `1/sqrt(27)≈0.192`,
   matches). `|r|=0.50` is `~2.6σ` raw for ONE look; scanning six
   correlated thresholds for one crossing a directional threshold is
   exactly the shape of a look-elsewhere inflation, and nesting (each
   `N_sub` is a strict subset of the next) makes standard multiple-
   comparison corrections UNDERSTATE the leakage, not overstate it.
3. **The single mass-shuffle control draw is not a null distribution.**
   Real `r=-0.50` vs. its own shuffled twin `r=-0.21` — a gap of `0.29`,
   which is `<2σ` once the shuffle draw's own noise (`~0.19` SD) is
   accounted for. A single shuffle is not evidence of a robust real-vs-
   null gap; a proper permutation-null histogram (≥1000 draws) would be
   needed to make that comparison honestly.
4. **Mass-rank thinning is not a neutral "scale-matching" procedure.**
   Selecting the top-N most massive halos simultaneously (a) shrinks the
   Pearson variable's own dynamic range and (b) preferentially selects
   halos in denser cosmic-web environments (assembly bias — well-known,
   not this project's own finding) — "increase typical NN spacing" and
   "select systematically rarer, differently-clustered environments" are
   entangled by construction, not separable by this procedure. Any
   correlation this sweep finds could reflect the selection itself, not
   physics at the target separation.
5. **No monotone trend across nested, heavily-overlapping subsamples**
   (`-0.50 → -0.20 → +0.01 → +0.09 → -0.06 → -0.05`) — re-checked
   directly: correct, no visible pattern. If a real scale-dependent
   signal existed, adjacent nested subsamples (which share most of their
   halos) should track each other; they do not.

**Response (Step 8a matrix): Accepted, no dismissal.** All five points
independently verified against the raw printed numbers, not taken on
the skeptic's word. This is not a "caveat attached to an otherwise-
standing result" — it correctly falsifies treating this sweep as a
resolving test.

## What this DOES establish

- **The magnitude/mechanism question (which of `FINDING_mass_
  assortativity_and_scatter.md`'s two readings is physically right for
  v82's own construction) is genuinely UNDETERMINED by this dataset —
  not resolved toward either reading, and NOT resolved toward the
  concerning negative/near-threshold direction either**, despite one
  raw number (`N_sub=30`) superficially suggesting that. This is a real,
  useful negative result: the honest state of this question is "cannot
  be determined from a single TNG-300 box at the relevant mass/scale
  regime," not "leans positive" or "leans negative."
- **Neither of the two existing readings** (`FINDING_mass_
  assortativity_and_scatter.md`'s all-pairs `+0.38` and nearest-
  neighbor-restricted `0.019`) **was measured at a scale that actually
  matches v82's own `s(0)=45 Mpc`** — the full 1461-halo sample's own
  typical nearest-neighbor spacing is only `9.2 Mpc`. This is a real,
  additional caveat on both existing readings, not just on this new
  attempt: `FINDING_P158`'s `rho>-0.5` conditionality, even where
  "confirmed," rests on measurements taken at the WRONG physical scale
  for v82's own construction. Recorded as a correction to the 2026-09-12
  `FINDING_P158` annotation (see below).
- A methodologically portable lesson: mass-rank thinning conflates
  "sparser sample" with "different (rarer) environment selection" — not
  a valid general-purpose way to match a simulation subsample to a
  target physical scale.

## What this does NOT establish

1. Not evidence that `rho<-0.5` at v82's own scale — the `N_sub=30`
   number that superficially suggested this does not survive scrutiny
   (see skeptic points 1-3 above).
2. Not a claim that `rho>-0.5` is safely established at v82's own scale
   either — genuinely unknown, not merely under-measured.
3. Not a claim about v82's own theory (`NO_AUTHOR_ERROR`).
4. Not the final word on the scale-matching question — a real fix
   (multiple independent simulation boxes/realizations, a permutation-
   null histogram instead of one shuffle draw, and a selection procedure
   that does not conflate rarity with mass rank) is named but not
   attempted here.

## Status

**Genuinely UNRESOLVED — recorded honestly as such, not forced toward
either the reassuring or the concerning reading.** Requires either
multiple independent TNG realizations/boxes or a fundamentally different
scale-matched selection procedure to make real progress; not attempted
further this session.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
