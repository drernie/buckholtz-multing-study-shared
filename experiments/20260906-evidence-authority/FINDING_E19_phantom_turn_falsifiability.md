# FINDING E19 — v82's H(z) "phantom turn" sits just past the CC data's
# 2nd-lowest sampled point (not on a future extrapolation), but the dip
# is well below the individual data points' own quoted 1σ noise there —
# plus a real, coherent, unresolved z_min discrepancy against TJB's own
# Claude session — corrected after Step 8a skeptic, 6 real points

**Date:** 2026-09-06
**Trigger:** Same email thread as `E18`/item 6. Ernest's item 3
(original): the phantom turn is not a prediction — the minimum is at
`z≈0` and the rise is only on a future-extrapolated dashed curve, not
in any data. **Ernest's own follow-up correction**: minimum is at
`z≈0.086`, not `z≈0`; "my conclusion that it is currently untestable
still stands." **Explicit go-ahead given** ("теперь пункт 3, фантомный
поворот").

## Step 8a skeptic — verdict: WEAKENED, 2 sub-claims initially FALSIFIED,
## 6 real points total, ALL corrected in place, none dismissed

**Process note, disclosed not hidden:** the first skeptic dispatch
described this experiment's method in prose rather than pasting the
actual source code — the standing project rule ("always paste the real
code") was violated a third time (`feedback_skeptic_dispatch_missing_
code.md` already names two prior recurrences). The skeptic itself
flagged this ("I don't have the actual code in front of me"). Every
point below was independently re-verified against real math and real
data by re-running the corrected code, not accepted on the skeptic's
word alone — per this project's own `audit-verification-gate.md`
("agent's own [VERIFIED] ≠ your [VERIFIED]").

1. **The original "signal-to-noise ratio" divided two PERCENTAGES with
   different denominators** (`dip%/H_model` vs `sigma%/H_data`) — not
   equivalent to an absolute-units ratio, and would silently mis-scale
   at a redshift where `H_model` and `H_data` diverge more (confirmed
   by the skeptic's own worked algebra). **Fixed**: recomputed in
   absolute `km/s/Mpc` throughout (`dip_abs / sigma_abs`).
2. **Comparing the dip only against 1-2 raw CC points' own sigma
   overestimates the true noise floor** relative to what the fit's own
   parameter-covariance-propagated uncertainty on `H_min` would give —
   a full covariance propagation is out of this experiment's scope.
   **Fixed**: the "RESOLVED" framing is withdrawn; the result is now
   stated as a lower bound against real, individual, quoted point
   uncertainty, with the caveat stated explicitly, not silently.
3. **"z_min sits within the CC data's sampled range" overclaimed
   density of coverage.** **Fixed**: reworded to "just past the 2nd-
   lowest sampled point, in a sparsely-sampled interval" — a weaker,
   more accurate claim.
4. **The z_min discrepancy against TJB's own Claude session is
   COHERENT and ONE-SIDED across BOTH Table II configurations** (this
   project's `z_min` is higher in both cases — for `sh0es_anchored_
   0pct`, `0.0963` falls OUTSIDE even TJB's own stated range
   `[0.085,0.09]`, on the same side as the first discrepancy) — not
   safely attributable to "TJB's Claude session's imprecision" without
   further checking, as the first draft implied. **Fixed**: reported
   as an unresolved, one-sided pattern, with named candidate
   explanations on BOTH sides, neither confirmed.
5. **"RESOLVED" / "refutes Ernest's ORIGINAL claim" overclaimed and
   used evaluative-authority-adjacent language** (a standing, critical
   project rule: `feedback_no_evaluative_authority_words.md`). **Fixed**:
   reworded throughout — Ernest's own corrected conclusion is
   *confirmed*, his original strict framing was *too tight* (he already
   softened it himself), not "refuted."
6. **Controls were insufficient**: `PC1` (`H(z_SHOES)=H0_anchor`) is
   trivial-by-construction, not an independent check; `SC1`'s scan
   range (`z≤0.5`) didn't rule out a second minimum at higher `z`; `RC1`
   (grid-density stability) validates numerical convergence, not
   physical correctness; the close `H_min` agreement with TJB's Claude
   session is partly circular (same closed-form formula, same published
   `β` values). **Fixed**: added a real, non-trivial positive control
   (a synthetic toy function with an analytically-known minimum, run
   through the identical machinery — recovered exactly); extended the
   sign-change scan to `z∈[1e-6,5]` (still exactly one minimum found);
   relabeled the trivial control honestly; stated the circularity
   caveat explicitly.

**No point dismissed.** All 6 addressed in the code, the printed
output, and this write-up.

## Method (full detail in `CLAIM_E19`)

Reused `E18`'s own already-verified `H_of_z_single` (TJB's own
independently-implemented function, re-executed by this project) to
grid-scan + locally refine the H(z) minimum for both
`unconstrained_spotlighted` and `sh0es_anchored_0pct`. Loaded the real,
unmodified `cosmic_chronometer_31pt.csv`.

## Results

**Part A — independently-located minimum:**
```
unconstrained_spotlighted:  z_min=0.09883, H_min=72.3576, H(today)=73.8471, dip=1.4895 km/s/Mpc
sh0es_anchored_0pct:        z_min=0.09631, H_min=72.2358, H(today)=73.6476, dip=1.4118 km/s/Mpc
```

**Part A2 — comparison against TJB's own Claude session's claimed
values, corrected framing:**
```
unconstrained_spotlighted: project z_min=0.09883 vs TJB Claude z~0.086  -> +14.9% (project HIGHER)
sh0es_anchored_0pct:        project z_min=0.09631 vs TJB Claude's [0.085,0.09] -> OUTSIDE (above)
```
Both configurations show the project's own `z_min` above TJB's Claude-
session value/range — a coherent, one-sided offset. **Not attributed to
either side's error** without further checking (candidate explanations
named: a coarser age-redshift conversion on TJB's Claude session's side;
an unverified definitional subtlety on this project's side — neither
confirmed).

**Part B — data-range check, corrected framing:**
```
Lowest-z CC point:    z=0.07, H=69.0+-19.6 km/s/Mpc
2nd-lowest-z CC point: z=0.09, H=69.0+-12.0 km/s/Mpc
Found minimum: z_min=0.0988 -- just past the 2nd-lowest sampled point,
in a sparsely-sampled interval, technically inside the data's min-max
range but NOT densely constrained.
```
This shows the minimum is not confined to a future-extrapolated
region — Ernest's own original strict framing was too tight, which he
had already softened in his own follow-up. It does not show the region
is well-constrained by data.

**Part C — signal vs. real, quoted noise, corrected to absolute units:**
```
Dip depth, absolute:                 1.490 km/s/Mpc
Real quoted sigma at nearest points: 19.6 km/s/Mpc (z=0.07), 12.0 km/s/Mpc (z=0.09)
Ratio (dip_abs / sigma_abs):         0.076x (vs lowest-z point), 0.124x (vs 2nd-lowest)
```
Measured against the actual, individual, quoted uncertainty of the two
real data points nearest the claimed minimum, the dip is well below
one sigma at both. **Explicit caveat, not resolved here**: this
compares against RAW per-point noise, not the fit's own parameter-
covariance-propagated uncertainty on `H_min`, which could in principle
be tighter — this ratio is a lower bound on detection difficulty, not a
final word.

## Controls

- **PC1** (real, non-trivial positive control, added after skeptic):
  a synthetic toy function with an analytically-known minimum
  (`z=0.15, H=70.0`) run through the identical grid+refine machinery —
  recovered exactly (`<1e-4` in `z`, `<1e-6` in `H`) — PASS.
- **PC2** (trivial-by-construction, relabeled honestly): `H(z_SHOES)`
  recovers `H0_anchor` exactly — PASS, but tests the anchoring code
  path, not the H(z) shape.
- **SC1** (extended range): `dH/dz` changes sign exactly once over
  `z∈[1e-6,5]` — rules out a second local minimum at higher `z` — PASS.
- **RC1** (numerical convergence only, not physical validation):
  `z_min` stable to 5 significant figures across a `100×` grid-density
  change — PASS.

## Verdict

Three sub-questions, each honestly separated:
1. **Data-range question**: the minimum is not on a future-extrapolated
   curve — confirmed, but the coverage there is sparse, not dense.
   Ernest's own follow-up already implicitly conceded this by fixing
   the location; this makes it explicit and quantified.
2. **Signal-vs-noise question**: against the two nearest real data
   points' own quoted uncertainty, the dip is `8-13×` smaller — Ernest's
   corrected conclusion (currently untestable) is confirmed at this
   specific, narrower scope. **Not** shown to be true against the fit's
   own (potentially tighter) parameter-covariance uncertainty — that
   remains a real, open, disclosed gap.
3. **Location-value question**: a real, `~15%`, coherent, one-sided
   discrepancy against TJB's own Claude session's claimed `z_min`,
   present in BOTH configurations — reported as genuinely unresolved,
   with named candidate explanations on both sides, not attributed to
   either party without further checking.

## What this does and does NOT establish

**Does establish:** a corrected, honestly-scoped, three-part answer to
item 3 — refining rather than "refuting" Ernest's original framing,
confirming and precisely bounding (not fully resolving) his corrected
conclusion, and surfacing a real, disclosed numerical discrepancy
against TJB's own Claude session that neither side's process caught
before now.

**Does NOT establish:**
1. Whether MULTING's physics is correct — `NO_AUTHOR_ERROR`.
2. A full detection-significance calculation against the fit's own
   parameter covariance — named as a real, unclosed gap.
3. The cause of the `z_min` discrepancy — reported, not diagnosed.
4. Anything about the other critique items — this closes item 3 only.

## Pearl Registry / next step

Two real, specific, checkable open items, worth Pearl Registry rows if
this line is revisited: (a) a full `β1/β2/H0_anchor` covariance
propagation to get a proper `σ(H_min)`, closing the Part C caveat;
(b) tracing the source of the coherent one-sided `z_min` discrepancy
against TJB's own Claude session.
