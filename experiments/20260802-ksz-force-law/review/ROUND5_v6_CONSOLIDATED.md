# Round 5 — consolidated static review of DRAFT_SPEC_v6

**Verdict: FAIL.** Not frozen. Blind C not launched. The stop rule is **not**
met: number-changing ambiguities remain.

Two isolated readers, specification only. Each returned exactly 13 blocking
findings under the operational gate (`Reading A` / `Reading B` /
`Affected output`). Union after de-duplication: **18**, of which **8 were found
by both** and **10 by one reader only**.

---

## 1. What the round confirmed

Both readers independently checked and confirmed the arithmetic and structural
work of the v6 patch:

- `r_lo(kk) = 3.8 + 0.8·kk` reproduces 3.8 … 11.0 in ten nodes and correctly
  excludes 6.0.
- The coarse grid `mu = 0.1·jj`, `jj = 1…600` reaches `mumax = 60` exactly;
  `keyMu = round(mu/0.05)` is integral on both grids.
- Guard G1's grid rule reproduces both endpoints exactly over `m = 0…9999`.
- The refinement window is 81 integral `ii` values symmetric about `2·jlast`;
  both clip bounds lie on the 0.05 lattice.
- `alpha = 983/999`.
- **Cases A–D are provably mutually exclusive and total over every possible
  `acc` vector**, and case D's "smallest `jj` with `acc` true" is unique.
- Case B terminates in seven bisections, well inside its 20-iteration cap.
- Control 9's key resolves to a real node; the digest is `nsim`-invariant.

The case-totality repair — the v6 change that added case D — is therefore
confirmed correct. It is the one structural fix from the previous round that
landed cleanly.

## 2. Found by both readers — the core of v7

| # | Finding | R9 | R10 |
|---|---|---|---|
| 1 | **Case B returns a value the same section forbids.** The bracket `[0, 0.1]` has its left end "accepted by construction"; if every midpoint is rejected the accepted end is `mu = 0`, which §10 declares "is not evaluated and is never an endpoint". `SdMC` then needs `Qobs(0)` at a node that is never evaluated. | F1 | B6 |
| 2 | **Case A reports "the `mu` attaining max `Qobs`" with no tie rule, and a 600-fold tie is reachable.** If `muhat = mumax`, `Qstat ≡ 0` on the whole grid: below `muhat` by the first branch, at `muhat` by cancellation. §7 and §15.1 both give tie rules; §10 does not. | F2 | B2 |
| 3 | **Counters are indexed by `jj` but fire where no `jj` exists.** `edgeCount[·,·,jj,·]` and `degenCount[·,·,jj]` use the acceptance-vector index, while G4 is "applied to every fit" — including refined nodes (`ii`), bisection nodes (`keyStep`), coverage nodes and all four branches. | F3 | B3 |
| 4 | **`range` and `maxViolation` are maxima over an empty set** when every grid node lands in case A — the very situation case A exists to describe. | F4 | B7 |
| 5 | **`gcurve` is underdetermined in column, units and extrapolation.** §3 fixes the units and column roles of `xi_zbin2.dat` and §2 fixes every `dr6.hdf` shape; `sdss_g_sqrtg.csv` gets neither, and its filename names two candidate curves. | F5 | B4 |
| 6 | **§15 item 9 declares a `(2,11,2)` observed-boundary array** while §6 keeps MODEL-R off the `r_lo` grid, leaving twenty slots with no defined content. | F6 | B12 |
| 7 | **`INVALID_INPUT` and `NUMERICAL_FAILURE` never say which §15 items are absent.** Only `STOP_RUN` has that list, and both are reachable after item 1 is computable. | F9 | B9 |
| 8 | **Controls 5 and 6 do not say how many `Drel` values they emit** (two and four comparisons respectively, one "measured value" required). | F12 | B11* |

\* The two readers arrive at the same section from opposite directions — see §4.

## 3. Found by one reader only

**R10 only, number-changing:**

- **B1** — §13 takes its threshold from "the coarse-grid value at that mu", which
  reads either as reusing §10's `rootCal` value or as recomputing it under the
  study's own assigned `rootVal`. Neither reading is contradicted.
- **B5** — `IntGK` is the only numerical operator with no named routine, rule
  order or subdivision limit, while `CubicSpline`, `numpy.quantile`,
  `minimize_scalar` and `default_rng` are all pinned with options. The
  subdivision cap decides whether `QUADRATURE_NOT_CONVERGED` fires. *R9 rated
  this NON-BLOCKING on the ground that both implementations are bound to 1e-10
  and every downstream threshold is 1e-6 or looser — see §4.*
- **B13** — §9 specifies the monotonicity pairing twice, incompatibly:
  "consecutive retained nodes `p` and `q_`" (skip the excluded, compare the
  survivors) versus "Excluded nodes remove both comparisons that involve them;
  the gap is not closed."

**R10 only, format:** B8 (a branch with no numeric `L95` has no disposition;
`STOP_BRANCH` is defined and listed but assigned to no condition), B10 (control
6 versus guard G2 — *excluded by R9, see §4*).

**R9 only, all format:** F7 (the excluded-node list has two populations — range
exclusions and monotonicity-only exclusions), F8 (`STOP_RUN` lists item 8 as
surviving, yet item 8 requires all nine controls and up to six never ran), F10
(§0 attaches `stat-only, fixed-template` and `MODEL-SUPPORT CONDITIONAL` to
reported items while §1 and §15.11 forbid a run to emit anything outside the
outcome set), F11 (items 3 and 4 declare float shapes for arrays that must hold
outcome labels), F13 (row order and row count unspecified for items 3, 10, 12).

## 4. Where the readers disagreed, and who is right

The gate's escape clause — *a reading that contradicts another explicit line is
not blocking* — resolved two of the three disagreements without appeal.

**Control 6 versus guard G2 (R10 blocking, R9 not).** R9 is right. R10 argues
a G2 failure at `eps = 0.10` could raise either `EXCISION_WINDOW_OUT_OF_RANGE`
(§5's verb) or `PV_EPSILON_SENSITIVE` (control 6's). But the control table has
an explicit **Verb on failure** column reading `STOP_RUN PV_EPSILON_SENSITIVE`,
which contradicts the first reading. Not blocking.

**Control 5's operands (R10 blocking, R9 format-only).** R10 is right, and R9's
own analysis shows why. §12.0 states "`y` is the second-named quantity in each
control row". Control 5 is the only gated row that does not contain the word
"against", so its second-named quantity is `Kw3`, not a recomputation — making
the comparison `Kraw3` versus `Kw3`, which differ by exactly `1 + xi(R)`.
R9 computed the deviation under the *intended* reading (each kernel against its
own recomputation), where the factor cancels and the two numbers are equal.
Both computations are correct; they answer different readings, which is the
finding. Under R10's reading `Drel = max|xi(R)|` over the fitted bins — orders
of magnitude above the 1e-6 gate — and the run dies.

**`IntGK` (R10 blocking, R9 not).** Unresolved, and it should be fixed
regardless. R9's argument bounds the *kernel values* but not the *terminal
state*: the subdivision limit is what decides whether the integrator reports
non-convergence, and no threshold argument constrains it. Fixing it costs one
line and removes the dispute.

## 5. The PART D split, and a category it misses

Each reader was asked how many of its blocking findings change a **number** and
how many change only **format**. They disagreed:

```
R9 : 6 number  /  7 format
R10: 10 number /  3 format
```

The disagreement is not noise — it traces to which findings each reader raised,
not to different judgements about shared ones. On the eight shared findings they
agree. Taking the union and applying each reader's own classification, with the
§4 resolutions:

```
UNION: 18 blocking  →  10 change a number  ·  8 change only the report
```

**A category the binary split does not capture**, named by R9 and worth carrying
into the stop rule: findings F8 and F9 alter no *value*, but under one reading up
to six controls' measured values and up to ten whole report items are **absent
entirely**. Same numbers where both readings report them — fewer numbers
reported. "Format-only" understates that.

## 6. Consequence

The stop rule was: if only format micro-details remain, stop refining the text,
freeze a reference implementation and proceed to Blind C.

**Ten number-changing ambiguities remain, six of them found independently by
both readers.** The condition is not met. v7 is required, as a mechanical patch
on the same terms as v6: ledger first, no new derivation, no method change.

Two of the six shared findings are v6's own doing — case B (finding 1) and the
`jj`-indexed counters (finding 3) were both introduced by the v6 patch while
repairing v5. The pattern is now established across three consecutive versions
and should be treated as a standing risk of the patch process, not as an
accident: **every repair to a terminal-state rule has so far created a new state
the repaired rule does not cover.** v7's ledger must therefore carry, for each
terminal-state edit, an explicit enumeration of the states the edited rule can
now reach.
