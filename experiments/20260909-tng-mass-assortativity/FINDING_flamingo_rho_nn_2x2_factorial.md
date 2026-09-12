# FINDING — 2x2 factorial: selection and mass-convention are NOT
# separable at N=50; a real, dominant interaction effect exists

**Date:** 2026-09-12
**Claim tested:** `CLAIM_flamingo_rho_nn_2x2_factorial.md`
**Script:** `flamingo_rho_nn_2x2_factorial.py`
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Result (raw output, real FLAMINGO data, live `hdfstream` download)

```
Downloading full SO/200_crit/TotalMass array (real, ~61MB)...
Targeted download: positions, M200c, M500c for the SAME top 5000 (by M200c) halos...
Shared valid pool: N=5000

     N  A(sel200,cor200)  B(sel200,cor500)  C(sel500,cor200)  D(sel500,cor500)
    35            0.4607            0.4789            0.2181            0.4055
    50            0.3197            0.2013           -0.0205            0.0826
  1200           -0.0206           -0.0274           -0.0223           -0.0238

Decomposition (selection effect vs value effect):
     N  sel_eff@200corr(C-A)  sel_eff@500corr(D-B)  val_eff@200sel(B-A)  val_eff@500sel(D-C)  total(D-A)
    35               -0.2426               -0.0734               0.0182               0.1874     -0.0552
    50               -0.3402               -0.1188              -0.1184               0.1030     -0.2371
  1200               -0.0017                0.0036              -0.0067              -0.0015     -0.0032
```

`A` and `D` reproduce `FINDING_flamingo_rho_nn_m200c_vs_m500c_selection.md`
exactly at all three `N` (`N=50`: `0.3197`/`0.0826`; `N=35`:
`0.4607`/`0.4055`; `N=1200`: `-0.0206`/`-0.0238`) — a real consistency
check, not assumed.

## Independent re-verification (before dispatching the skeptic)

Computed independently in a scratchpad script (path-sum and interaction
consistency, both algebraic identities that must hold if the
decomposition is arithmetically sound):

```
N=50:  interaction (D-C)-(B-A) = (D-B)-(C-A) = +0.2215
       path1 (sel-then-val) = path2 (val-then-sel) = total = -0.2371  (both match)
N=35:  interaction = +0.1692
N=1200: interaction = +0.0053
```

## Independent skeptic review (Step 8a, context-blind — claim + code +
## raw output ONLY, no reasoning chain)

**Verdict: WEAKENED.**

(a) **Implementation correctness — HIGH confidence, CONFIRMED.** Traced
the code: `nn_idx_for()` computes nearest-neighbor pairs from `pos[idx]`
ALONE — it never sees `m200` or `m500`. Cells A/B share `idx_200`/
`nn_200`; cells C/D share `idx_500`/`nn_500`. The alternate mass is
plugged into `pearson()` only at the very last step. No accidental
re-pairing by the alternate mass is possible, by construction. One
non-bug caveat: within-set NN assignment is directional (`i→j` does not
imply `j→i`), but this asymmetry is inherited identically by both cells
in each pair, so it cancels in any A-vs-B or C-vs-D difference — it
would only matter if the write-up called these "mutual pairs," which it
should not.

(b) **Interaction term is real, large, and sign-flipping — HIGH
confidence.** `interaction = (D-C)-(B-A) = (D-B)-(C-A)` (must match by
construction; independently confirmed to the 4th decimal, matching my
own pre-skeptic scratchpad computation of `+0.2215` almost exactly).
At `N=50`, `interaction = +0.2214`, comparable to or larger than every
individual "main effect" (`0.10`–`0.34` range). The value-effect
estimate literally flips sign depending on which selection is held
fixed (`B-A = -0.1184` vs `D-C = +0.1030`) — this is not two noisy
estimates of the same quantity, it is a genuine non-additive
interaction between selection-criterion and mass-convention.

(c) **No added statistical power — MEDIUM-HIGH confidence.** All four
cells are built from the SAME ~50-object FLAMINGO pool (`idx_200` and
`idx_500` overlap ~74% at `N=50`, per the prior overlap finding); B and
C are different views of nearly the same objects, not independent
replications. The prior test's honest `z~0.7-1.6` for the `N=50` total
effect is not improved by decomposing it into four cells. Skeptic's own
rough SE estimate for the interaction term (`~0.08-0.16`, giving
`interaction` at `~1.4-2.7σ`) is explicitly flagged by the skeptic
itself as not rigorously recomputed here (order-of-magnitude carried
over from this branch's earlier jackknife SE work, not a fresh
jackknife on this specific interaction quantity) — reported here as a
[HYPOTHESIS]-tier plausibility check, not a rigorous significance
claim. The real, load-bearing point does not depend on the exact
number: whatever the SE, it is **not smaller** than a single cell's own
SE, so four cells reporting four-decimal precision risk being read as
more informative than they are.

(d) **Practical conclusion — HIGH confidence: "entangled," not a clean
attribution.** The claim's own pre-registered decision rule ("if
`|C-A|` and `|D-B|` small while `|B-A|` and `|D-C|` large → value is
the driver; reverse → selection is the driver") does not fire in
either direction at `N=50`: all four differences are the same order of
magnitude (`0.10`-`0.34`), with `(B-A)` and `(D-C)` opposite in sign.
Neither branch of the claim's own decision rule is satisfied.

## Response to skeptic (per Step 8a Response Matrix)

- **(a) CONFIRMED-REAL** — promoted unchanged. No response needed.
- **(b) CONFIRMED-REAL, accepted as the primary result** — this IS the
  finding. The interaction, not a clean selection-vs-value attribution,
  is what the data show.
- **(c) FALSIFIED (my own pre-registered "if X then driver=Y" framing)
  → dismissed, replaced.** The claim.md's own decision rule assumed
  the effects would separate cleanly; they don't. This is not a defect
  in the test — the test did exactly what a factorial decomposition is
  supposed to do: it revealed that the two-factor model needs an
  interaction term, and reporting "selection is the driver" or "value
  is the driver" without that term would be the overclaim, not the
  entangled finding.
- **(d) Accepted as the honest conclusion**, stated below.

## What this DOES establish

- The 2x2 factorial decomposition is arithmetically and logically sound
  (both path-sums equal `total` independently; the interaction term is
  internally consistent under both equivalent formulas).
- At `N=50` (the primary/user-requested scale), the shift from
  select-`M200c`/correlate-`M200c` (`rho=0.32`) to select-`M500c`/
  correlate-`M500c` (`rho=0.08`) is driven by a **combination of
  selection-criterion and mass-convention that interact non-additively**
  — neither factor alone accounts for the shift, and their combined
  (interaction) contribution (`+0.22`) is comparable to or larger than
  either individual "main effect."
- At `N=1200` (the branch's "definitive" estimand), all four cells and
  their differences are tiny (`≤0.03` in magnitude) — this branch's
  strongest, most load-bearing result remains unaffected either way.
- At `N=35`, the same qualitative pattern holds (interaction `+0.17`,
  comparable to or larger than the main effects).

## What this does NOT establish

- **Does NOT** identify selection-criterion OR mass-convention as "the"
  driver of the `N=50` shift — the honest answer is that they are
  entangled at this sample size, not that one dominates.
- **Does NOT** add statistical power beyond the prior test's own honest
  `z~0.7-1.6` framing for the total `N=50` effect — the four cells are
  built from the same ~50 largely-overlapping objects, not independent
  samples.
- **Does NOT** provide a rigorous significance level for the interaction
  term itself — the `~1.4-2.7σ` figure is a rough, explicitly-flagged
  plausibility estimate, not a computed jackknife SE on this specific
  quantity.
- **Does NOT** resolve the separate, larger `docs/162` item 9 question
  (2PCF-style estimand vs. nearest-neighbor).
- **Does NOT** validate or invalidate v82's own theory (`NO_AUTHOR_ERROR`).

## Status

Step 8a-item-2 gap (from `FINDING_flamingo_rho_nn_m200c_vs_m500c_
selection.md`) is CLOSED — the factorial has been completed. The
closure's own answer is "entangled, not cleanly separable at N=50,"
not "X is the driver." This is itself the honest result, not a failed
test — a factorial that reveals a real interaction has done its job.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
