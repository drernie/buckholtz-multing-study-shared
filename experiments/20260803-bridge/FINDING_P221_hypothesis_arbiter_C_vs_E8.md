# hypothesis-arbiter cycle — is the near-cancellation amplification factor
# C≈15 a mechanistic predictor of FINDING_E8's 4.0-7.6× eigenvalue sensitivity?

`NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION` · L0 causal/mechanistic
2026-09-08 · script: `P221_near_cancellation_C_vs_z.py` · ruff clean
NO_AUTHOR_ERROR — diagnostic on our own reconstruction's sensitivity, not a
claim about v82.

**Delegated by `/boyko-why-ladder` Chain C** (same day): I had computed
`C=(|F1%|+|F2%|)/|F1%+F2%|≈15` from TJB's own Table III percentages at
z=1.07 (in the `/boyko-bridge-ladder` synthesis) and attributed it
explaining-power for `FINDING_E8`'s 4.0-7.6× Hessian eigenvalue drop —
without independent verification. why-ladder correctly flagged this as
the same unchecked-mechanism-claim pattern already `REJECT`ed in `NR-019`
(Mechanism Claim Gate, `falsification-ladder.md` Step 0a), and delegated
the ambiguity to this cycle.

## Stage 1 — SPAWN (5 hypotheses)

| ID | Hypothesis | Mechanism | Basis |
|---|---|---|---|
| H0 | C and E8's 4-8× are numerically similar by coincidence, no real link | Different mathematical objects: C is a single-z force-percentage ratio; E8's figure is a 33-point-aggregated Hessian eigenvalue ratio | Different units, different aggregation level |
| H1 | C≈15 is a stable, general diagnostic — representative at any z | Near-cancellation amplifies uniformly across the dataset | The paper reports F1/F2 near-total cancellation "across all seven Table II rows" (generate_all_results.py Result 5b comment) |
| H2 | C(z) properly z-averaged (weighted like the real fit) lands near 4-8× | Individual high-C points get diluted/averaged down in the aggregate Hessian statistic | E8 aggregates over all 33 points; C=15 is only one snapshot |
| H3 | The real driver is P190's own `E1(z)/E2(z)` coefficient-function ratio, not raw `F1%/F2%` — C is a red herring | `E1(z)/E2(z)` is a different, more carefully-defined quantity (level-set slope), already shown stable to 12.7% (`FINDING_P190`) | P190 already built and tested exactly this alternative quantity for a related purpose |
| H4 | Genuinely unknown — no test connects these numbers yet | — | `docs/158` G3 ("joint uncertainty propagation") explicitly listed `NEVER done` |

## Stage 2 — KILL-DESIGN

| ID | Kill test | Cost |
|---|---|---|
| H1 | Compute `C(z)` at all 33 real data z-points (not just z=1.07); if it varies by more than ~2× across the dataset, H1 is killed | Cheap — reuses `multing_core.py` directly |
| H0/H2 | Same computation; check whether a naive aggregate of C(z) across all 33 points lands near 4-8 (supports H2) or nowhere near it (supports H0) | Same script |
| H3 | Compare `C(z)`'s stability (this script) against `FINDING_P190`'s already-measured 12.7% stability of `E1(z)/E2(z)` — if C is far less stable, H3 is favored | Comparison only, no new computation |
| H4 | Falls by elimination once H0-H3 are evaluated with existing/cheap data | — |

**Outcome map, written before running:**
```
If C(z) varies <2x across 33 points  -> H1 survives, H0 weakened
If C(z) varies >>2x across 33 points -> H1 KILLED, investigate whether the
    z=1.07 value used was representative or an outlier
If naive aggregate lands near 4-8    -> H2 strengthened
If naive aggregate is nowhere near 4-8 -> H2 weakened, H0 strengthened
If C(z) variation >> P190's 12.7%    -> H3 strengthened (C is not the
    same well-behaved quantity P190 already found and used)
```

## Stage 3 — IN-SILICO (real computation, not literature — this is an
## internal-consistency question)

**Substrate check:** `P221_near_cancellation_C_vs_z.py` loads
`multing_core.py` + `assumptions.yaml` directly from TJB's own archive
(`data/source_material/zenodo_21204955_supplemental/code/`) — same
substrate already used by `FINDING_P219`/`P220`. **Positive control passed
exactly** before trusting anything else: reproduces
`generate_all_results.py`'s own printed `headline_cases` table at all 4
of its tabulated z-values (1.965, 1.07, 0.5, 0.070) to the stated
tolerance (0.02%).

**Result — C(z) across all 33 real data points, frozen
`unconstrained_spotlighted` fit** (`β1=1.4335e10, β2=7.8067e17`):

| statistic | value |
|---|---:|
| min | 14.90 (near z≈1.43) |
| max | 747.36 (z=0.0233, the SH0ES anchor point itself) |
| median | 22.35 |
| mean | 67.41 |
| IQR | [16.09, 37.08] |
| **C at the actual nearest data point to z=1.07** (z=1.037) | **15.41** |

**Outcome: `C(z) varies by >50× across the dataset` — H1 KILLED.** The
z≈1.07 value (≈15) sits near the dataset's own *minimum*, not a
representative or "typical" value — most of the 33 points, especially
low-z ones, show far larger apparent amplification. **The naive
unweighted aggregate (harmonic-mean-style, `1/median(1/C)`) gives
22.35 — not near 4-8, and further from it than the z=1.07 snapshot was.**
H2 is weakened by this crude check (though not decisively — see Stage 4
confounder 2).

**H3 comparison:** `FINDING_P190` measured its own analogous ratio,
`E1(z)/E2(z)` (level-set slope of the degeneracy direction), varying by
only **12.7%** across the same z-range. `C(z)` computed here varies by
**>5,000%** (14.9 to 747) over the same range. These are not the same
quantity behaving differently by coincidence — they are visibly
different mathematical objects, and P190's is the one already shown to
be well-behaved. **H3 is strengthened.**

## Stage 4 — RED-TEAM

**Confounder 1 (real, tempers the headline number but not the conclusion):**
`C=(|A|+|B|)/|A+B|` is mathematically singular as `A+B→0` — i.e. exactly
where `F1` and `F2` cancel *most* completely. The data's own low-z points
sit very close to that crossing (net% = −0.99 at z=0.0233, −0.13 at
z=0.070) — so the extreme 747× value is likely dominated by this
near-singularity in `C`'s own definition, not new physical information
about parameter sensitivity. **This does not rescue H1** — if anything it
strengthens the conclusion that raw `C` is a poorly-conditioned quantity
unsuitable as a general-purpose diagnostic, exactly the caution H3
already implies. But it means "the typical case is 50× worse than z=1.07"
should not be read as a precise physical statement — the correct, more
modest claim is: **`C(z)` is unstable, including a near-singularity
regime, and z=1.07 is not representative of the dataset's behavior.**

**Confounder 2 (real, limits the strength of the H2 verdict):** the
"naive unweighted aggregate" computed here does not replicate how a real
`χ²` Hessian actually weights 33 points (which weights by `1/σ²` per
point, not equally). **H2 is weakened by this check but not killed** — a
genuine `docs/158` G3-style weighted Monte Carlo propagation remains the
decisive test for whether proper weighting could land nearer 4-8×.

**Confounder 3 (untested, flagged not chased):** only the
`unconstrained_spotlighted` Table II row was checked. Whether `C(z)`'s
instability pattern holds for other rows (e.g. `sh0es_anchored_0pct`) is
not verified here.

**Oracle Adequacy:** this script's own positive control (Gameable? No —
reproduces 4 independently-stated numbers exactly, not tuned to do so.
Real vs theater? Real — uses TJB's own unmodified archive code. Negative
control? Implicit — the assert on the positive control would have failed
loudly had the substrate been wrong, as it does not need separate
staging. Reproducible? Yes, deterministic, no RNG. Measures the intent?
Yes — directly computes the quantity in question at every real data
point, not a proxy.) → **ADEQUATE**.

## Stage 5 — ARBITRATE

| ID | Status | Final confidence | Note |
|---|---|---:|---|
| H0 (coincidence) | ✅ survives, strengthened | 0.65 | The specific numerical resemblance (15 vs 4-8) is not supported once C(z)'s real range is seen |
| H1 (C stable/general) | ❌ KILLED | 0.05 | `C(z)` varies >50× across real data; z=1.07 is near the minimum |
| H2 (attenuated via averaging) | ⚠️ weakened, not killed | 0.35 | Naive aggregate doesn't land near 4-8; a real weighted G3 test is still the decisive one |
| H3 (real driver is P190's `E1(z)/E2(z)`) | ✅ survives, strengthened | 0.70 | 12.7% variation vs C's >5,000% variation — visibly different, better-behaved quantity |
| H4 (genuinely unknown) | ⚠️ superseded, not fully resolved | 0.30 | This cycle answers "is raw C the mechanism" (no); it does not fully answer "is there ANY real link between near-cancellation and E8's sensitivity" — that still needs the weighted G3 test |

**Duhem-Quine qualifier:** H1 is incompatible with the observed `C(z)`
range **given** the assumptions that (a) `unconstrained_spotlighted` is
the right fit to test, (b) the CC dataset's own 33 z-points are the
right domain, and (c) `C` as defined (raw `F1%/F2%` ratio) is the
quantity the original claim actually meant. All three are reasonable and
stated, not hidden.

**Synthesis:** 2 hypotheses survive (H0, H3), 1 killed (H1), 2 weakened
(H2, H4) — this is the "2-3 survive → needs a crucial experiment"
regime. **The crucial experiment is `docs/158`'s own already-named G3**
(joint Monte Carlo uncertainty propagation through `multing_core`,
properly weighted by each CC point's real `σ`) — not run here, still the
correct next decisive step if this thread is pursued further.

**What this cycle actually resolves, stated plainly:** the specific claim
I made in today's `/boyko-bridge-ladder` synthesis — "C≈15 explains why
E8 found 4-8× eigenvalue sensitivity" — **is not supported and is
withdrawn.** The z=1.07 snapshot was an unrepresentative, near-minimum
point, not a general diagnostic. This does not mean near-cancellation and
parameter sensitivity are unrelated in principle (H0 is not proven, only
favored on current evidence) — it means the specific numerical bridge I
drew between them was itself an unverified Mechanism Claim of exactly
the kind `NR-019`/why-ladder already taught this project to catch.

## Decision

**Correction applied to today's bridge-ladder synthesis**, same
no-silent-correction discipline as every other fix today: the "C≈15"
row in this project's running commentary should be read as **withdrawn
as an explanation for E8**, retained only as a correctly-computed but
non-representative single-z arithmetic fact.

**Pearl for the registry:** `C(z)`'s near-singularity behavior near
`F1+F2=0` crossings is itself a useful, reusable diagnostic caution for
this project's own force-decomposition tables — any future percentage
table near a sign-crossing z should carry this caveat.
