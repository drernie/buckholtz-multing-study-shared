# docs/153 — Bottleneck 1 (F→H_MULT(z)) reopen gate decision

**[2026-09-12 annotation, not a rewrite — see `FINDING_P223_finite_r_
single_pair_closure.md`]** §3a precondition 1 ("does a finite-r analog
of the S-S closure calculation even exist in closed form, or would it
require a genuinely new derivation?") is now answered: **no new
derivation was needed** — v82's own literal Eqs. (1)-(9), read directly
from the primary source, already supply everything required. `P223`
substituted v82's own force law into v82's own kinematic-translation
machinery (H1, symbolically confirmed: `k_A(z)`-dependent terms survive
in `a_ddot/a` with no internal cancellation, independently verified via
a positivity argument, not merely asserted) and independently reproduced
`docs/127`'s own `G_alpha_beta=0` result exactly for the same power-law
shapes (H2). Synthesis (H3, narrowed after a Step 8a skeptic pass): read
literally, `docs/127`'s S-S closure and v82's single-pair bridge answer
structurally different questions about a shared force-law shape — one
pair's own finite trajectory vs. a population's `r->infinity` tail
contribution — so `docs/127`'s `G_eff=0` does not constrain v82's bridge
construction, and the two are **not in contradiction**. This closes §0's
restated causal-compatibility question under the literal-text reading;
whether v82's own physical INTENT for `s(z)` carries additional,
unstated population content is explicitly out of scope (Skeptic
Objection 2, accepted). Read `FINDING_P223_finite_r_single_pair_closure.
md` alongside this document — §0's causal-compatibility bottleneck and
§3a's three preconditions below are now addressed, not the earlier
"restated, OPEN" state this document originally recorded.

**[2026-09-12 second annotation, same day — a related but SEPARATE
question, not one of §3a's own preconditions.]** `P223` above does not
touch `FINDING_P158`'s own still-open magnitude/mechanism gap (which of
two TNG-300 mass-assortativity readings is physically right for v82's
node population — see `FINDING_P158_jensen_mass_averaging_v82_force_
terms.md`'s own 2026-09-12 corrections). A same-day attempt to resolve
it via a scale-matched sub-sample was **falsified as a resolving test**
by a skeptic pass (small-sample/look-elsewhere artifact, not a real
signal) — the question stays genuinely undetermined. A live check of
whether another TNG box could fix this with more data found
**effectively no independent volume is publicly available**: same-
initial-conditions resolution/physics variants aside, the only
genuinely different boxes (`TNG100-1`, `Illustris-1`, `TNG50-1`) are
too small — a periodic box's own half-side bounds the maximum
representable pair separation, and `TNG50`'s (25.8 Mpc) is smaller than
the 40-45 Mpc target itself. A real fix needs a Gpc-class suite outside
the TNG project entirely — not attempted. Full account:
`experiments/20260909-tng-mass-assortativity/FINDING_scale_matched_
nearest_neighbor_rho.md`.

**Update, same day:** checked live — `MillenniumTNG` has the right box
size but no functioning public access (its own site still promises a
"2024" release, unfulfilled; API returns 404). **`Magneticum
Pathfinder` and `Uchuu` DO have real, currently-working public
access**, both large enough (`Magneticum Box2`: 4.5x `TNG300`'s volume;
`mini-Uchuu`: 7.4x) to materially improve on `TNG300`'s own marginal
`N=30-50` statistics at the target scale. `Magneticum` also uses a
genuinely different cosmology (WMAP7 vs. `TNG`/`Uchuu`'s shared Planck
2015 parameters) — the stronger of the two as an independent check.
Neither downloaded yet (a new download needs separate, per-turn
permission). Full account, same file as above.

**Second update, same day:** `Uchuu` turned out DOWN when actually
needed (its fast-download service explicitly marked "Temporally not
available," confirmed by a live connection timeout, not just the
label). `Magneticum Box2_hr` real cluster data (10,493 clusters,
880KB, permission granted and downloaded) was used for an independent
cross-check instead — result **FALSIFIED as a resolving test** by a
second skeptic pass: the same nested-threshold trap that killed the
`TNG300` attempt recurred (7 positive-looking values reduce to one
effective `~1.3-1.5 sigma` measurement once the `67-95%` sample overlap
is accounted for), even with a proper permutation null this time. The
magnitude/mechanism question is now independently reconfirmed
UNDETERMINED across two different simulations, not resolved by either.
Full account: `experiments/20260909-tng-mass-assortativity/
FINDING_magneticum_independent_rho_check.md`.

**Third update, same day:** `AbacusSummit` checked — real data, but
access requires account creation (`/login`/`/signup` on its own
portal), which is prohibited outright regardless of permission, so
this route is closed. `FLAMINGO` checked and used instead — real,
live, no-account `hdfstream` access (confirmed working) to a third
simulation (`~114x` [**CORRECTED 2026-09-12: actually `~36x`, arithmetic
error, no effect on any reported number — see `CLAIM_flamingo_
independent_rho_check.md`**] `TNG300`'s volume, a third distinct
cosmology). This
time the nested-sweep design flaw was fixed at the root: ONE
pre-registered `N=1200` threshold, no sweep. Result: `rho=-0.0231 ±
0.0359`, consistent with zero — the first WELL-POWERED measurement in
this thread, decisively excluding a large `rho` for the true-nearest-
neighbor observable (`|rho|>=0.10` ruled out at `~10.6 sigma`) and
placing `FINDING_P158`'s own `rho>-0.5` safety threshold `~13 sigma`
away from being violated. Does NOT contradict `TNG300`'s own all-pairs
`+0.38` reading (a structurally different observable, per Gate 1). Full
account: `experiments/20260909-tng-mass-assortativity/
FINDING_flamingo_independent_rho_check.md`.

**Fourth update, same day (2026-09-12) — correction, not a rewrite:**
the "Third update" paragraph above's `"~13 sigma"` / `"rho<=-0.5
excluded"` phrasing is **WITHDRAWN** — caught by the user, not self-
caught. That number divided the distance to `-0.5` by the permutation-
null SD, which characterizes `H0: rho=0`, not the composite hypothesis
`H0: rho<=-0.5` (the sampling variance of a correlation coefficient is
not constant in `rho`). A follow-up addendum added a real spatial
block-jackknife CI and a second observable (`rho_band`, all-pairs-in-
band on the same subsample): the qualitative conclusion survives and is
now corroborated by three independent SE estimates rather than one
borrowed number, but no defensible precise sigma-count exists this far
into the tail. The `rho_band` sub-test came out small too but is too
underpowered (`N_pairs=127`) to discriminate whether `TNG300`'s own
`+0.38` reflects a different observable or a different population —
genuinely undetermined, not resolved. Full account: `experiments/
20260909-tng-mass-assortativity/FINDING_flamingo_addendum_jackknife_
band_closure.md`.

**Fifth update, same day (2026-09-12) — user-requested discriminating
test, run:** the real next step named in the Fourth update (measure
BOTH `rho_NN` and `rho_band` on `TNG300`'s OWN population, matched to
FLAMINGO's selection protocol) has now been run. Result:
**INCONCLUSIVE.** `TNG300`'s own `N=35` matched subsample gives
`rho_NN=-0.42` (permutation `p=0.028`) — nominally an anomaly, but
NOT independent evidence (substantially overlaps the already-falsified
`N_sub=30` point) and consistent with small-`N` sampling noise;
`rho_band` unmeasurable (`N_pairs=3`). Cannot discriminate observable-
difference from population-difference. A genuine, unrelated arithmetic
error (FLAMINGO's own volume advantage over `TNG300` is `~36x`, not
the previously-stated `~114x`) was caught and corrected in the same
check — descriptive only, no effect on any prior computed result.
Full account: `experiments/20260909-tng-mass-assortativity/
FINDING_tng300_own_population_rho_nn_and_band.md`.

**Sixth update, same day (2026-09-12) — user-requested independent-
volume replication of the `N=35` anomaly, run:** carved `27` non-
overlapping, TNG300-sized sub-volumes out of FLAMINGO's real, much
larger box (different code, different cosmology), applying the SAME
blind selection protocol independently in each. `10/27` matched;
resulting `rho_NN` distribution (`mean=0.01, SD=0.21`) reached `0/10`
at `|rho_NN|>=0.42`. **Step 8a skeptic caught a critical correction
before any conclusion was drawn**: `0/10` is NOT evidence — under the
shared noise floor this test itself measures, `P(0` exceedances in
`10` draws`)~=67%` even if `-0.42` is ordinary noise; the test is
underpowered by roughly `7x`. Two further named, unquantified design
biases (environmental selection of matched sub-cubes; artificial
periodic-wrap dilution toward zero) both plausibly bias this specific
test toward `0` regardless. Verdict: genuinely INCONCLUSIVE — neither
confirms nor rules out that TNG300's own anomaly is ordinary sampling
noise. Full account: `experiments/20260909-tng-mass-assortativity/
FINDING_flamingo_subvolume_replication.md`.

**Seventh update, same day (2026-09-12) — user-requested quantification
of the periodic-wrap bias, run: NOT confirmed.** Compared `rho_NN`
under periodic vs. open-boundary treatment on the same `10` already-
selected sub-cubes. The correctly-specified test (on `|rho|`, testing
whether periodic shrinks magnitude toward zero) gave `p=0.86` — a dead
`5/10` split between dilution and inflation, no detectable systematic
effect. A first, signed-mean reading (`-0.054`) had looked like
confirmation but was itself measuring the wrong quantity (sign shift,
not amplitude shrinkage) — caught by Step 8a skeptic before being
written up. Open-boundary treatment is confirmed NOT to be a clean
reference either (its own, different edge distortion). The wrap-bias
question stays genuinely open; the real fix (a pre-cut, whole-box
global-NN ground truth) is named, not run. Full account: `experiments/
20260909-tng-mass-assortativity/FINDING_flamingo_subvolume_periodic_
wrap_bias.md`.

**Eighth update, same day (2026-09-12) — user-requested true global-NN
ground truth, run: the attempt itself is INVALIDATED by a real, self-
caught scale mismatch.** The "true" partner pool (top-5000-by-global-
mass) is `~4x` denser than each sub-cube's own local selection, pulling
"true" NN separations to `~22` Mpc median (only `5%` land in the
original `40-45` Mpc window) — `rho_true` answers a different question
than the one this branch cares about. Caught before any conclusion was
written, independently confirmed by Step 8a skeptic, which also found
a separate labeling bug (`frac_outside=75.7%` is dominated by a near-
trivial counting identity, not a clean measure of periodic-boundary
failure). A concrete, implementable fix (density-matched partner pool)
is named, not run. The periodic-vs-open question from the prior two
updates remains exactly where it was left — genuinely open. Full
account: `experiments/20260909-tng-mass-assortativity/FINDING_
flamingo_subvolume_true_global_nn.md`.

**Ninth update, same day (2026-09-12) — user-designed diagnostic
(same-mass-cut, full-box periodic NN) run: gate PASSES, but the
correctly-specified test finds no significant boundary-treatment
effect.** Held each sub-cube's own implicit mass cutoff fixed while
searching FLAMINGO's real, full 1000 Mpc periodic box instead of the
artificial sub-cube wrap. Geometric gate (decided BEFORE any rho was
computed, per the user's own explicit instruction): aggregate median
NN separation = 41.16 Mpc, well inside the pre-registered [35,55] Mpc
pass band — confirms the earlier top-5000 scale-mismatch was a
population-density artifact, not a fundamental flaw in scale-matching
FLAMINGO sub-volumes at all. Resulting rho_NN (mean=-0.082, 1/10
anomalous) is statistically indistinguishable (amplitude paired test,
p>0.5 both ways, independently re-verified) from the earlier periodic
and open treatments. A new, real, disclosed confound: matching mass
threshold does not match candidate-population density per cube (real
cosmic variance). Four tests on this same 10-cube sample now converge:
n=10 is the binding constraint, not boundary treatment. Full account:
`experiments/20260909-tng-mass-assortativity/FINDING_flamingo_
subvolume_same_mcut_global_nn.md`.

**Tenth update, same day (2026-09-12) — user requested the "definitive
global FLAMINGO estimand" (no sub-cubes, one geometrically pre-
registered global threshold, spatial-jackknife uncertainty); found it
already exists.** Consolidated rather than re-run (user's own choice,
since the numbers are deterministic): `rho_NN=-0.0231, jackknife
SE=0.0476` (real 125-block spatial jackknife on the full 1000 Mpc box)
+ `rho_band=+0.0271, jackknife SE=0.1231` (N_pairs=127) — both already
established in the FLAMINGO addendum, both already twice-skeptic-
reviewed, predating the 27-subcube detour entirely. This is a
DIFFERENT, complementary question from the subcube thread (FLAMINGO's
own best global estimate at N=1200, vs. TNG300-sized-volume
replication at n=10) — neither supersedes the other. Full account:
`experiments/20260909-tng-mass-assortativity/FINDING_flamingo_
definitive_global_estimand_synthesis.md`.

**Eleventh update, same day (2026-09-12) — CLOSING SYNTHESIS, user-
proposed, independently spot-checked, no discrepancy found.** The
`P158` magnitude/mechanism computational sub-branch is now CLOSED,
absent a new external argument specifically requiring `rho_band` or a
different population semantics. Corrected directional-risk statement:
"on the best available global, scale-matched FLAMINGO estimand
(`rho_NN=-0.0231+/-0.0476`, no sub-cubes, real spatial jackknife),
there is no evidence of the strong negative NN mass-correlation needed
to reverse `P158`'s own directional prediction — mechanism and exact
node-correspondence remain open." The `27`-subcube replication chain
(four real tests) and the withdrawn `"13 sigma"`/`"0/10"`/signed-vs-
amplitude corrections along the way are recorded as having functioned
as a genuine adversarial audit of the estimand itself — the pre-
existing global FLAMINGO result survived that audit better than any
newly-constructed alternative. **Next bottleneck is ontological, not
statistical: which real halo population corresponds to v82's own
"node."** Full account: `experiments/20260803-bridge/FINDING_P158_
jensen_mass_averaging_v82_force_terms.md` (Tenth entry), `docs/151`
(Third worked example), `experiments/20260909-tng-mass-assortativity/
FINDING_flamingo_definitive_global_estimand_synthesis.md`.

**Twelfth update, same day (2026-09-12) — the ontological question named
in the Eleventh update was started (user-requested): what physically is
a v82 "node"? Real answer found; `P158` REOPENED as an estimand-
specification question, not merely closed.** Direct primary-source read
of v82's own text (`P230`), Step 8a skeptic pass, plus a real, external
cross-check of the cited two-point-correlation-function paper's own
abstract: (1) a node's measurable properties are cluster ICM physics
(real citations, all verified); (2) v82's own mass/radius convention is
`R500`, stated twice, NOT `R200`/`M200c` — a genuine, previously-
unnoticed mismatch with this branch's entire prior simulation work; (3)
v82's own cited empirical route for node separation (`s0~30 Mpc`,
Basilakos & Plionis 2004) is a population-level, RICHNESS-DEPENDENT
two-point-correlation-function amplitude, NOT a nearest-neighbor-
distance rule — confirmed directly from the cited paper's own real
results (`r0=20.7 h^-1 Mpc` richer subsample `~=` v82's own `"~30 Mpc"`
after `h`-conversion). Skeptic caught real overclaims in three
downstream conclusions (each inherited a stronger textual commitment
than the source supports) — corrected framings recorded. Frozen
specification: `docs/162_ontology_spec_v82.md`. **Net effect: prior
`rho_NN`/`rho_band` numbers remain numerically valid but are
reclassified from "the intended v82 test" to "a related, not source-
faithful proxy" — pending a genuinely source-faithful estimand (2PCF-
style, `M500c`-based, population-clustering-amplitude, not nearest-
neighbor-on-a-ranked-subsample).** Full account: `experiments/
20260803-bridge/CLAIM_P230_what_physically_is_a_node.md` +
`FINDING_P230_what_physically_is_a_node.md`.

**Thirteenth update, same day (2026-09-12) — FINAL CLOSURE of `P158`'s
computational/statistical sub-branch.** Following the Twelfth update's
`R500`/`M500c` ontology discovery, three further real tests resolved
whether the mass-convention mismatch threatens the branch's strongest
result: `M500c`/`M200c` overlap (`~74-92%` across tested `N`), a direct
`rho_NN` recompute under both conventions, and a `2x2` factorial
separating selection-criterion from value-convention effects. **Result:
the branch's "definitive global estimand" (`N=1200`) is ROBUST to the
mass-convention choice** — `M200c`- vs. `M500c`-selection `rho_NN`
differ by `-0.0032`, `~15x` smaller than the real jackknife
`SE=0.0476`. `P158`'s own directional-safety claim (`rho > -0.5`) is
now DOUBLY confirmed, not merely unaffected by the ontology finding.
The smaller-`N` scale (matching TNG300's own anomaly) shows a real but
entangled shift (2x2 factorial: interaction term dominates, no single
driver) — this adds ambiguity to a scale ALREADY known to be
underpowered, it does not open a new concern. **The computational/
statistical sub-branch is CLOSED — no further statistical iteration on
the nearest-neighbor design is warranted.** The remaining open item
(`docs/162` item 9: a real, `M500c`-based, 2PCF-style population-
clustering-amplitude estimand, replacing nearest-neighbor entirely) is
an ESTIMAND-CONSTRUCTION question, not a statistics question — out of
scope for `P158`'s own thread, in scope for `docs/162` item 9's own
next step. Full account: `experiments/20260909-tng-mass-assortativity/
FINDING_flamingo_m500c_m200c_overlap.md`, `FINDING_flamingo_rho_nn_
m200c_vs_m500c_selection.md`, `FINDING_flamingo_rho_nn_2x2_factorial.
md`, `experiments/20260803-bridge/FINDING_P158_jensen_mass_averaging_
v82_force_terms.md` (Twelfth entry).

**Fourteenth update, same day (2026-09-13) — docs/162 item 9 (the
estimand-construction follow-on named by the Thirteenth update) is now
CLOSED as an active investigation thread, user-requested definitive
closure.** Two further tests beyond the first 2PCF pass: a mass-marked
`rho(r)` generalization (mark-shuffle permutation null, cell-block
positive control) found NO mass-assortativity signal anywhere in
`5-150` Mpc at the best-powered scale (`N=5000`) — an independent-
methodology confirmation of this branch's already-established null,
closing the direct `P158`-motivating question. A gamma-range diagnostic
(re-fitting already-recorded `xi(r)` over alternative ranges, no new
download) found the previously-flagged clustering-SHAPE mismatch is
REAL but only PARTIALLY a fit-range artifact — Step 8a skeptic caught
that the best-powered corrected fit still leaves a `~0.5`-unit residual
against the physically-correct literature comparator (FLAMINGO's mass-
selected sample matches Basilakos & Plionis's RICHER subsample,
`gamma=1.6`, not the numerically-closer "poorer" value this branch
first compared against). This residual is explicitly left OPEN —
closing it would require real observational data, outside this
branch's simulation-only toolkit; this is the honest stopping point,
not an oversight. Full account (3 linked FINDINGs) and the docs/151
three-field status separation: `docs/162_ontology_spec_v82.md`'s own
"[FINAL CLOSURE, 2026-09-13]" section.

**[Correction, 2026-09-13, user-caught precision issue, not a
rewrite]**: this "closed" framing means the computational branch is
closed for the CURRENT source-faithful FLAMINGO operationalization of
P158's question, not that v82's broader ontological/mechanistic
interpretation is settled (still OPEN) or that MULTING's causal
correctness has been assessed (`NON-IDENTIFIED`, unchanged). Full
correction text: `docs/162_ontology_spec_v82.md`'s own same-dated
correction note.

**[2026-09-05 annotation, not a rewrite — see `docs/156`]** This
document's §3a explicitly required that "a future 'go' ... should
answer these [pre-conditions] first, not treat this document's own
framing as sufficient preparation." `docs/156` is that check, run after
an explicit user go-ahead on 2026-09-05. Its finding: **this
document's own §3 "finite-r/single-pair calculation," as literally
worded, is not buildable** — this project's own S-S closure route has
no finite-r closed form independent of v82 (a proven non-uniqueness
lemma, `docs/126`, plus two independent prior BLOCKED/FALSIFIED
attempts, `docs/124`/`docs/125`, all predating this document and not
cited here). `docs/156` also found this document cited only
`FINDING_P156` for its precondition-1 evidence, missing `FINDING_P157`/
`P158` — written the same day as `P156`, already in the repository
when this document was written the next day, and directly relevant.
The mechanically-correct alternative those two files identify and
build (Jensen's inequality on v82's own mass-derived scalar chain) is
what this section's §3a actually licensed pursuing, and what
`docs/156`→`FINDING_P195` continued. Read `docs/156` alongside this
document, not as a replacement for it — this document's own reasoning
(§0-§2, the restated bottleneck itself) stands unaffected; only §3's
specific proposed next calculation and §3a's own citation completeness
are corrected.

**Date:** 2026-09-01
**Origin:** explicit user request ("go" on the recommendation from
`boyko-project-radar`'s atomize scan) to close the outstanding gate
decision `docs/147`/`docs/149` both flagged as pending since
2026-08-30 — a formal decision was never made, only deferred, and
`docs/149`'s own §3 states plainly: *"This document does not itself
reopen bottleneck 1 — that is a decision for the project's own gate
process... a decision about what to do with that is still open."*
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (a process/gate decision, not a new
physics claim — no new computation is performed by this document)
**Method:** applies `docs/151`'s three-field status-separation rule to
the specific reopen question, using only evidence already established
in `docs/149`, `docs/150`, and `FINDING_P156` — no new claim is made
about v82's own theory or about this project's own reconstruction
beyond what those three documents already record.

---

## Correction (2026-09-01, context-asymmetric skeptic-caught, applied
before finalizing — code/citations verified present in the dispatch)

A skeptic review of the first draft raised 4 concerns. Each independently
re-verified before accepting or rejecting, per this project's own hard-won
constraint ("a skeptic's own critique needs independent re-verification
too — cuts both ways").

**CONFIRMED, no change needed** — the "REJECTED-AS-SAME" framing in §2's
ontological-status field is faithful to `docs/149`'s own explicit
language ("a *different mechanism*... not a confirmation or
contradiction... a *structurally different question*"), not an
overclaim.

**REFUTED BY DIRECT CHECK** — the skeptic argued §3's GO-criterion-2
application stretches "competing models" to cover a single yes/no
question with two answers. Checked directly against `docs/147`'s own
exact wording (`grep`-confirmed): the criterion reads *"конкурирующие
модели/**чтения**"* — competing models **or readings** — and this
document's own §3 citation already includes "models/readings," not
"models" alone. The skeptic's critique evaluated an English paraphrase
that dropped the "/readings" half, not this document's actual text.
Separately: two mutually-exclusive live possibilities, only one of which
is true, is the normal and expected shape of any Cheapest Differentiating
Test setup (`falsification-ladder.md`'s own CDT Protocol, which `docs/
147`'s own criterion 2 cites as its analog) — not a defect specific to
this case.

**ACCEPTED, FIXED** — the skeptic's strongest point: this document does
90% of the pre-motivation work for the finite-r calculation (names it,
cites its exact `FINDING_P156` tag, argues it's GO-eligible), leaving the
"separate, explicit go-ahead" disclaimer with little structural work left
to do — a real soft-GO / stop-rule-erosion risk, not a technicality.
Fixed: added §3a, explicit pre-conditions that must be checked (not just
a calculation to run) before any future GO, giving the required "separate
explicit go-ahead" genuine gating content instead of a rubber stamp.

**ACCEPTED, VERIFIED** — the skeptic correctly noted the "nothing changed
since 2026-08-30" claim (Section 1's last row) was asserted from
`activeContext.md`'s own summary, at the same confidence weighting as the
PDF-verified v82 claims, without independent verification — an asymmetry
`docs/151`'s own status-separation rule exists to catch. Fixed by direct
check: `grep -l -i "bottleneck 1\|F→H_MULT\|F->H_MULT\|accretion-
kinematic\|F→H(z) bridge"` across all of `FINDING_P175`-`P187` returns
**zero matches** — none of those 13 findings mentions bottleneck 1, the
F→H(z) bridge, or accretion-kinematics language at all. The row's evidence
marker is upgraded from activeContext-summary to `[VERIFIED-BASH]`.

## Addendum (2026-09-01, user review, applied after the skeptic pass above)

The user's own review (independent of the skeptic dispatch) confirmed
this document's central move — restating rather than solving the
bottleneck — and flagged two real wording risks, both fixed:

1. **§2's "Empirical/Model status: VERIFIED"** could be misread as
   "confirmed by data," when what is actually established is narrower
   — that a published mechanism exists, not that it is empirically
   adequate. Fixed: the field's canonical name (`docs/151`'s fixed,
   greppable schema) is unchanged, but its content now says explicitly
   what "VERIFIED" does and does not cover.
2. **§3's bare "CLOSED, superseded by fact"** on the old bottleneck
   risked being read, in isolation, as "F→H(z) is solved." Fixed:
   replaced with an explicit `OLD-FORMULATION-SUPERSEDED` tag (kills
   only the "bridge absent" claim) paired with an explicit instruction
   that it must always be read alongside the new, OPEN causal-
   compatibility tag — never alone.

Also incorporated: the user's own refinement of what the eventual
decisive test should compare (matched intermediate physical
quantities from both routes, not final fitted `H(z)` curves) — added
to §3a as a forward-looking methodological note, not acted on now.

---

## 0. The question being decided

`docs/147`'s own text for bottleneck 1 states it is **BLOCKED, not
derived**, with an explicit reopen condition: *"не появилось новой
информации, разрешающей direct derivation reopening (`k_A(z)/r_A(z)/
D_cAB(z)` от TJB, или новая публикация)"* — no new information enabling
direct-derivation reopening (`k_A(z)/r_A(z)/D_cAB(z)` from TJB, **or**
a new publication).

`docs/149` already established, as a plain factual matter, that this
condition is met — v82 is simultaneously a new publication and a
source of explicit `k_A(z)/r_A(z)/m_A(z)` evolution laws — but
explicitly declined to make the reopen decision itself, deferring it
to "the project's own gate process." This document **is** that gate
process, run to completion.

## 1. Evidence assembled (no new computation — citing `docs/149`/`150`/`FINDING_P156` only)

| Question | Answer | Source |
|---|---|---|
| Does a real, published F→H(z) bridge from TJB now exist? | YES — Sec. II.B-C of v82, an explicit accretion-corrected two-body kinematic derivation, `ä/a=s̈(z)/s(z)` integrated to `H(z)²−H₀²` | `docs/149` §2 (II.C row), read from PDF page images |
| Are the explicit `m_A(z)/r_A(z)/k_A(z)` evolution laws `docs/147`'s condition asked for actually present? | YES — Eqs. (10)-(14), each classified by TJB's own Class I/II/III provenance system | `docs/149` §2 (II.D row), §3 |
| Is TJB's bridge mechanism the SAME as this project's own reconstruction route? | NO — TJB's route is accretion-corrected two-body kinematics (Sec. II.B-C); this project's own route (`docs/124`-`127`) is the Shtanov-Sahni generalized cosmic-energy equation, a structurally different framework | `docs/149` §2 (II.B row: "a *different* framework from TJB's own accretion-kinematics one"), `docs/150` §1 (F→H(z) bridge row) |
| Has this project already attempted to compare the two bridges directly? | YES, once — `FINDING_P156` (2026-08-30) | `docs/150` §6 item 2, `FINDING_P156` |
| What did that comparison find? | **Tier structure matches** (v82's own force-law tiers, Eqs. 1-4, are structurally identical to this project's own kernel assignment — `[VERIFIED-PDF]`+`[VERIFIED-sympy]`). **One agent-proposed claim was checked and found FALSE**: v82 does NOT assert `s(z)=d₀/(1+z)` exactly — v82's own text (pp. 5-6) explicitly disclaims this, using `a(z)` only as a redshift-mapping device. **The actual comparison remains unresolved**: whether this project's own S-S closure criterion (built for an isotropically-averaged, `r→∞` population) says anything about v82's own construction (finite separation, ~40-45 Mpc, single oriented pair, no averaging) is not established — this is exactly `docs/127`'s own scope caveat, named as untested. | `FINDING_P156` §4 verdict tags: `TIER-STRUCTURE-MATCHES`, `SS-CLOSURE-APPLICABILITY-TO-V82S-CONSTRUCTION-UNRESOLVED`, `ONE-LOAD-BEARING-AGENT-CLAIM-WAS-FALSE`, `FINITE-R-ANISOTROPIC-REGIME-REMAINS-OPEN` |
| Has anything changed since 2026-08-30 that bears on this specific bottleneck? | NO — the `P175`-`P187` v82-degeneracy thread (this session, closed 2026-09-01) attacked a *different* bottleneck (bottleneck 3, the `(β1,β2)` identifiability degeneracy in this project's own reconstruction). Directly checked, not merely summarized from `activeContext.md`: `grep -l -i "bottleneck 1\|F→H_MULT\|F->H_MULT\|accretion-kinematic\|F→H(z) bridge"` across all 13 files `FINDING_P175`-`P187` returns **zero matches**. `docs/149`/`150`/`FINDING_P156`'s 2026-08-30 state is still the most current evidence on this specific question. | `[VERIFIED-BASH]` grep across `experiments/20260803-bridge/FINDING_P17[5-9]*.md` + `FINDING_P18[0-7]*.md`, 2026-09-01 |

## 2. Applying `docs/151`'s status separation to the reopen decision itself

The reopen decision is not one claim but three separable ones, exactly
the pattern `docs/151` was written to keep from being silently
collapsed. Answered here as three explicit fields, per the rule:

> **Empirical/Model status:** VERIFIED, narrowly — what is verified is
> **published-mechanism existence**, not empirical adequacy: TJB has
> published a real, explicit F→H(z) derivation (v82, Sec. II.B-C),
> read directly from the PDF, not from a markdown conversion or a
> summary. `docs/147`'s own named reopen condition (a new publication
> supplying the bridge + evolution laws) is satisfied as a plain
> factual matter. **This field does NOT say the bridge is empirically
> adequate** — whether v82's own fit actually explains the observed
> `H(z)` data to any standard is a separate, unexamined question; "a
> published mechanism exists" and "that mechanism is confirmed by
> data" are different claims, and only the first is what this field
> asserts.
>
> **Ontological/mechanistic interpretation status:** REJECTED-AS-SAME,
> OPEN-AS-COMPATIBLE — v82's bridge is **not** the same mechanism as
> this project's own S-S route (established, not merely undetermined —
> `docs/149`/`150` both state this directly). Whether the two
> mechanisms are *compatible* in the region where they physically
> overlap (finite separation, single pair) is a **separate, still-open
> question** — `FINDING_P156` attempted exactly this comparison once
> and could not resolve it, because this project's own closure
> criterion was built for a different regime (isotropic average,
> `r→∞`) than v82's construction occupies.
>
> **Causal/cosmological claim status:** NON-IDENTIFIED — whether v82's
> own bridge, worked through in the finite-r single-pair regime,
> reintroduces `k_A(z)`-dependence into the background in a way that
> would conflict with this project's own `G_eff=0` result is not
> established either way. This is `FINDING_P156`'s own named "concrete
> next calculation" (its `FINITE-R-ANISOTROPIC-REGIME-REMAINS-OPEN`
> tag) — not attempted by that file, and not attempted here either.

## 3. Verdict

**The original bottleneck-1 wording is factually superseded and must
be restated, not merely marked "reopened."** The 2026-08-23 framing
("central bridge not established in published form") is no longer
true — TJB has published one. Marking the OLD bottleneck simply
"reopened" without restating it would misrepresent what is actually
still blocked, repeating exactly the kind of silent-collapse `docs/151`
exists to prevent.

**Applying `docs/147`'s own GO-criterion 2** ("differentiates at least
two competing models/readings currently both compatible with
established constraints") **to the candidate next step**: the old
bottleneck ("does a bridge exist at all?") no longer differentiates
anything — the answer is settled YES. The **new**, precisely-scoped
question DOES differentiate two live readings: (a) this project's own
S-S closure result and v82's bridge are compatible in their overlap
regime — v82's finite-r construction does not reintroduce
`k_A(z)`-dependence the S-S closure would consider a violation; or
(b) they are incompatible — the two mechanisms give genuinely
different predictions in that regime, which would mean this project's
own `docs/127` closure result does not generalize as far as it was
implicitly assumed to.

**GO — bottleneck 1 is formally RESTATED, not simply reopened:**

```
OLD-FORMULATION-SUPERSEDED (docs/147, 2026-08-23): "F→H_MULT(z) —
central bridge not established in published form." This specific
CLAIM ("bridge absent") is refuted by fact (docs/149) — the wording
itself is retired, retained in docs/147 as historical record, not
deleted. This tag is deliberately NOT "bottleneck 1 solved" or
"F→H(z) established" — read literally, it says only that "no bridge
exists" is false, not that any bridge is physically correct.

NEW, CAUSAL-COMPATIBILITY BOTTLENECK, OPEN (this document, 2026-09-01):
"F→H_MULT(z), finite-r/single-pair compatibility — does this project's
own S-S closure criterion (isotropic-average, r→∞) say anything about
v82's own bridge construction (finite separation ~40-45 Mpc, single
oriented pair, no population averaging)? Does v82's bridge, worked
through on its own terms in that regime, reintroduce k_A(z)-dependence
in a way `docs/127`'s own G_eff=0 result would consider a violation?"
— OPEN, GO-eligible under docs/147's own criterion 2. Concrete next
calculation named by FINDING_P156's own FINITE-R-ANISOTROPIC-REGIME-
REMAINS-OPEN tag: a finite-r, non-averaged, single-pair version of
the closure calculation this project has not yet built.

**Correction 2026-09-09:** "~40-45 Mpc" above is not sourced from v82's
own text (checked by direct grep this session — zero matches anywhere
in the document; full account in `FINDING_P156`'s own same-day
correction and `experiments/20260909-tng-mass-assortativity/
FINDING_mass_assortativity_and_scatter.md`). v82's own text names, then
explicitly rejects, `s₀~30 Mpc` (cluster-cluster correlation length) as
an observational anchor; its actually-fitted quantity, `H₀,anchor≡
ṡ₀/s₀` (Eq. 22), is a ratio that never separately pins down a
separation value. The qualitative bottleneck framing (finite-separation
single-pair vs. isotropic-population-average) is unaffected; the
specific Mpc figure is not load-bearing anywhere in this document and is
flagged here so it is not carried forward uncritically.
```

**The two tags above must always be read together, never the first
alone.** `OLD-FORMULATION-SUPERSEDED` kills exactly one claim
("bridge absent") — it is not a verdict on `F→H(z)` itself, which
remains a live, open causal-compatibility question under the second
tag. A future reader grepping only "bottleneck 1... superseded" and
concluding the physics is settled would be repeating precisely the
silent-collapse `docs/151` exists to prevent.

This is **not** an instruction to run that calculation now — per
`docs/147`'s own stop-rule, naming a GO-eligible next step is not the
same as authorizing it; per this session's own `activeContext.md`
("Nothing pre-authorized right now... a fresh direction awaits
explicit instruction"), running it requires a separate, explicit
go-ahead.

## 3a. Pre-conditions for an actual GO (not satisfied by this document)

Added per the skeptic's own soft-GO concern above: naming a calculation
precisely enough to be gate-able is not the same as having done the
gating work. Before any future "go" on the finite-r/single-pair
calculation, the following must be checked and answered — none of them
are answered here:

1. **Does a finite-r analog of the S-S closure calculation even exist
   in closed form**, or would it require a genuinely new derivation
   (not just re-evaluating `docs/127`'s existing result at finite `r`)?
   `FINDING_P156` did not check this.
2. **Is the single-pair, externally-oriented regime tractable** with
   this project's existing machinery (`two_charge_completion.py`,
   `two_field_action_closure.py`), or does it require a construction
   this project has not built at all?
3. **What would each of the two possible outcomes (compatible /
   incompatible) actually change** about this project's own standing
   results (`docs/127`'s `G_eff=0` claim, `P152`-`P155`'s S1/S2
   closure work) — is the calculation's cost proportionate to its
   consequence, per `falsification-ladder.md`'s own Cheapest
   Differentiating Test Protocol?

A future "go" on this specific calculation should answer these three
first, not treat this document's own framing as sufficient preparation.

**Methodological note for the eventual decisive test, once §3a's three
pre-conditions are answered** (user's own refinement, 2026-09-01, not
yet acted on — pre-conditions above still gate this): the sharpest
version of this test would NOT compare the two routes' final, fitted
`H(z)` curves — a match or mismatch there is downstream of enough free
parameters and fitting choices on both sides to be ambiguous either
way. Instead, take one shared physical ensemble/population model and
compute the **same intermediate physical quantity** by both routes:
(1) via v82's finite-pair/accretion-kinematics bridge, (2) via this
project's own population-averaged S-S closure. If the two routes
already disagree at that intermediate level, the question about final
`H(z)` becomes secondary — a much sharper test than comparing two
output curves. Naming the correct intermediate quantity is itself
part of pre-condition 1 above (whether a finite-r analog exists in
closed form), not solved by this note.

## 4. What changes in `docs/147`'s own bottleneck tracking

`docs/147`'s bottleneck-1 entry should be annotated (not rewritten) to
point here: the original entry stays as historical record (per this
project's own no-silent-correction convention — see every `FINDING_*`
file's own dated Correction sections), with a pointer to this
document's restated version as the current status.

## What this document does NOT establish

1. **Not a claim about v82's own theory being right or wrong**
   (`NO_AUTHOR_ERROR`) — entirely a process decision about this
   project's own bottleneck tracking.
2. **Does not run the finite-r/single-pair calculation** — names it as
   the concrete next GO-eligible step, per §3, does not attempt it.
3. **Does not reconcile `β1/β2` with this project's own `β_d/β_q`** —
   `docs/150` §6 item 1 remains a separate, still-open question, not
   addressed by this gate decision.
4. **Does not authorize any specific next computation** — per `docs/
   147`'s own stop-rule, GO-eligibility is necessary, not sufficient;
   an explicit user go-ahead is still required before building the
   finite-r closure calculation.
5. **Does not affect bottleneck 3** (Absolute scale) or **bottleneck 4**
   (IC-sensitivity) — both remain in their own, separately-decided
   states (`docs/147` points 3 and 4; bottleneck 3's own confound-
   breaking sub-thread, `P175`-`P187`, closed this session on entirely
   separate grounds).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
