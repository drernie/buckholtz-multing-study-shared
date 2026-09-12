# FINDING — same-M_cut, full-box NN diagnostic: gate PASSES (scale
# genuinely recovered), but the correctly-specified amplitude test
# finds NO significant difference from periodic or open treatment;
# a new, real per-cube density confound is disclosed; still n=10-
# limited, still inconclusive

**Continues:** `CLAIM_flamingo_subvolume_same_mcut_global_nn.md`
(committed BEFORE the script ran) → the user's own diagnostic design,
proposed in direct response to `FINDING_flamingo_subvolume_true_
global_nn.md`'s scale-mismatch finding. **User-designed and user-
requested.**
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Result (real, live `hdfstream` data, gate evaluated BEFORE any
## rho was computed, per the frozen claim's own ordering)

```
Aggregate same-M_cut, full-box NN separation: median=41.16, mean=41.53 Mpc
GATE: PASS ([35,55] Mpc threshold, frozen before running)

rho_NN same-M_cut, full-box: mean=-0.0822, SD=0.2210, 1/10 anomalous (cube 8: -0.4457)
rho_NN periodic (reference):  mean=0.0145,  SD=0.2069, 0/10 anomalous
rho_NN open (reference):      mean=-0.0394, SD=0.2321, 1/10 anomalous (cube 8: -0.4585)
```

## Independent skeptic review (Step 8a, context-blind) — every
## quantitative claim independently re-derived before use

Full text preserved in the session record. Amplitude paired tests
independently re-computed exactly: `|periodic|-|same_mcut|`:
`mean=-0.0198, SD=0.109, t=-0.573, p=0.580`; `|open|-|same_mcut|`:
`mean=-0.0131, SD=0.107, t=-0.386, p=0.708`. Per-cube density ratios
independently confirmed (cube 12: full-box same-`M_cut` population is
`1.69x` DENSER than that cube's own local selection; cube 5: `0.76x`
LESS dense) — real, cube-by-cube variation, not a uniform match.

1. **Was the gate genuinely pre-registered (`WEAKENED` per skeptic,
   `CONFIRMED` on direct inspection)?** The skeptic, working only from
   a code EXCERPT, could not directly verify the `[35,55]` threshold
   was in the actual executed code (visible in the given text only as
   a comment) — a real, stated limit of context-blind review via
   excerpt. **Directly checked here** (not taking the skeptic's word,
   nor asserting my own without re-reading): the committed script
   (`flamingo_subvolume_same_mcut_global_nn.py`, committed alongside
   the claim before running) contains the literal line `gate_pass =
   35.0 <= overall_median <= 55.0`, matching the claim's own frozen
   text exactly. The skeptic's own mitigating point stands
   independently regardless: the actual median (`41.16`) sits
   comfortably inside even the ORIGINAL narrow `40-45` window, so
   gate-width gaming could not have mattered for this specific run.
2. **Does the gate PASS validate the scale-mismatch fix (`WEAKENED`,
   real nuance added)?** Confirmed: median/mean landed at `41.16`/
   `41.53` Mpc, nowhere near the failed attempt's `~22` Mpc — the fix
   works as designed. **New nuance from the skeptic, independently
   checked**: the ORIGINAL local (sub-cube-restricted) medians
   (`43.03`-`44.40`, printed per cube) were already fairly tight and
   close to the new global medians (`35.90`-`47.08`) — meaning the
   boundary artifact this whole diagnostic was built to detect may not
   have been very large to begin with, at least not at the median
   level. The `11.5%`-in-window figure for individual halo-instances
   is NOT a contradiction (an aggregate median can sit inside a narrow
   band while individual points scatter around it) — confirmed
   directly, not just taken on the skeptic's word.
3. **Does the pool-size change introduce a new confound (`WEAKENED` —
   a real, disclosed issue)?** Confirmed by independent recomputation:
   holding the MASS threshold fixed per cube does NOT hold candidate
   POPULATION DENSITY fixed — real cosmic variance means some cubes
   (e.g. `12`) sit in locally under-dense regions relative to the
   box-wide average at that mass cut (full-box population `1.69x`
   denser than local), while others (e.g. `5`) sit in locally
   over-dense regions (full-box population `0.76x` as dense).
   Candidate-pool size ranged `826`-`2438` across the `10` cubes — a
   real, substantial, per-cube-varying factor entangled with (not
   isolated from) the boundary-treatment question this test was
   designed to test cleanly.
4. **Does the new result meaningfully differ from periodic/open
   (`FALSIFIED` — the correctly-specified test, learning directly from
   this same branch's earlier signed-vs-amplitude lesson).** Both
   amplitude paired tests give `p>0.5` — no significant difference.
   **Cube `8` is anomalous under all three treatments** (`|rho|`
   `0.27`/`0.46`/`0.45`) — correctly read as ONE cube's own persistent
   local feature showing up three times under different NN
   definitions, NOT independent triple-confirmation (all three draw
   from the same underlying `10` sub-cubes).
5. **Most honest overall conclusion (`NEEDS-REAL-DATA` on the original
   TNG300 question; genuine but modest improvement in physical
   defensibility).** This is a real, geometrically-correct (true full-
   box periodicity, not an artificial sub-cube wrap), population-
   threshold-matched data point — an improvement in DESIGN over
   periodic/open. But it is statistically INDISTINGUISHABLE from both
   prior treatments, and `n=10` remains the binding constraint. It
   does not settle whether TNG300's `rho_NN=-0.42` is signal or noise.

**Response (Step 8a matrix): all five points accepted. Item 1's gap
(skeptic couldn't see the full code) closed by direct re-inspection of
the actual committed script, not by trusting either the skeptic's
uncertainty or my own unverified claim.**

## What this DOES establish

- **The specific scale-mismatch problem from `FINDING_flamingo_
  subvolume_true_global_nn.md` is genuinely fixed by this design** —
  the gate is real evidence the earlier failure was a population-
  density artifact of using an unmatched top-`5000` pool, not a
  fundamental flaw in scale-matching FLAMINGO sub-volumes to `40-45`
  Mpc at all.
- **Boundary treatment (artificial periodic wrap vs. open vs. true,
  physically-correct full-box periodicity) does NOT produce a
  statistically detectable difference in `rho_NN` at `n=10`** — a real,
  properly-tested negative result (not "we didn't check," but "we
  checked with the correct test and found nothing").
- **A new, real, honestly-disclosed confound**: matching a mass
  THRESHOLD across cubes does not automatically match candidate
  POPULATION DENSITY — real environmental variance breaks that
  equivalence, cube by cube.
- **Cube `8`'s persistent anomaly across every treatment tried so far**
  is a genuine, specific curiosity (one real patch of FLAMINGO with a
  consistently elevated `|rho|`) — not broad evidence, but a concrete,
  named candidate for future targeted follow-up if this branch is
  revisited.
- **Four real tests on this same `10`-cube sample (periodic, open,
  same-`M_cut` full-box, plus the invalidated top-`5000` attempt) have
  now converged on the same practical conclusion: `n=10` is the
  binding constraint, not the boundary-treatment details.** Further
  variation on THIS specific sample is unlikely to be the most
  productive next step.

## What this does NOT establish

1. Does NOT resolve whether TNG300's `rho_NN=-0.42` is signal or noise.
2. Does NOT show same-`M_cut` full-box treatment is meaningfully
   "better" in its RESULT than periodic/open — only in its DESIGN
   (physically correct periodicity, matched mass threshold).
3. Does NOT eliminate the new pool-density confound (item 3 above) —
   disclosed, not fixed.
4. Not a claim about v82's own theory (`NO_AUTHOR_ERROR`).

## Status

**A real, honestly-reported, properly-skeptic-reviewed null result —
the diagnostic branch of the user's own two-part plan is now complete.**
Per the user's own stated decision tree: the gate passed (boundary
artifacts are not confirmed as large), so the sub-cube-replication
design is NOT invalidated outright — but the resulting `rho` comparison
adds no statistical power beyond what periodic/open already showed.
The user's own second, more promising design — a single global mass
threshold on the FULL FLAMINGO box (chosen geometrically, without
looking at `rho`), one measurement, spatial-jackknife uncertainty, no
artificial sub-cubes — remains the recommended next step if this
question is worth pursuing further, and has not been attempted.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
