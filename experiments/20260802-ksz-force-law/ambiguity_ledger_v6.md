# Ambiguity ledger — v5 → v6

Control document for the v6 patch. Every entry is a registered ambiguity from
the round-4 static review, the choice made, the exact edit, and a regression
check that fails if the ambiguity returns.

**v6 is a patch release.** It removes registered ambiguities and adds nothing
else: no new derivation, no new explanation, no method improvement. An entry
whose fix would change what is computed is marked `DEFERRED` and left for a
later version.

Sources: two isolated readers on `DRAFT_SPEC_v5.md`, round 4. Reader A returned
19 blocking findings, reader B returned 15; the union after de-duplication is
28 entries, of which 20 were found by both.

Legend: **B** = both readers · **A** / **B'** = one reader only.

---

## RNG — stream contract

| ID | Two readings | Chosen | Edit | Regression check |
|---|---|---|---|---|
| RNG-01 **A** | `rootCal` is declared and never assigned; the primary scan uses `rootCal` by elimination / uses any root, since the text is silent | `rootCal` for §9–§11, `rootVal` for §13, `rootDual` for §14 | §8: replace the `<root>` placeholder with an explicit table root → consumer | linter: every declared root used ≥ 1 time outside its declaration |
| RNG-02 **B** | `stage` for the coverage study is 0 (coarse-anchored) / 1 (refined sample size) | new value `stage = 2`, reserved for the coverage ensemble | §8 stage enumeration; §13 states `stage = 2` | linter: every value a key field may take is enumerated |
| RNG-03 **B** | branch 2 draws its row via `integers` / `choice` / `floor(random()·1000)`; and §8's "same standard normals" is false for a branch that draws none | `rng.integers(0, 1000)` **after** drawing and discarding the 15 normals, so the normal stream stays aligned with the primary | §8 consumption order; §11 branch 2 | test vector: first 10 row indices at a fixed key |
| RNG-04 **A** | `z` drawn as `(nsim, 15)` / `(15, nsim)` transposed / via `normal(0,1,…)` | `rng.standard_normal(size=(nsim, 15), dtype=np.float64)`, C order, dataset `b` is row `b` | §8 draw contract | test vector: SHA-256 of the first 1000 float64 draws |
| RNG-05 **B** | at a bisection midpoint `μ = 0.025`, `j20 = round(0.5)` is 0 (half-to-even) / 1 (half-away) | bisection does not use `j20`; case-B midpoints get their own key field | §8 key gains `bisect_step`; §10 case B | test vector: two consecutive midpoints have different keys |
| RNG-06 **B** | in the dual-unit run the key's `0.05` is converted / kept literal, the latter making `j20` non-injective | the key is index arithmetic, not a length; it is **never** converted, and the dual-unit run indexes by the same integers | §8 states the key is unit-free; §14 excludes it from the conversion list | linter: key fields carry no units |

## TOL — tolerances

| ID | Two readings | Chosen | Edit | Regression check |
|---|---|---|---|---|
| TOL-01 **B** | "max relative deviation" is element-wise over the target / normalised by the target's max / normalised by `sqrt(V_ii V_jj)` | explicit formula with an absolute floor, applied identically in every control | new §12.0 defines `Drel(x,y)` and `Dabs(x,y)`; every control row names which it uses | synthetic case: target containing an exact zero must not divide by it |
| TOL-02 **A** | guard G3's condition number is `cond₂` / `cond_∞`; "symmetric to 1e-12 relative" is referenced to `\|V_ij\|` / `max\|V\|` | `cond₂` via SVD; symmetry referenced to `max\|V\|` | §7 guard G3 | unit test on a matrix at the threshold |
| TOL-03 **A** | "Silverman bandwidth" is `0.9·min(s, IQR/1.34)·n^(−1/5)` / scipy's `s·(3n/4)^(−1/5)` | the first, written out, with `ddof = 1`, IQR by `numpy.quantile(method='linear')`, a floor, and a zero-IQR fallback | §10 `dens` definition | unit test: bandwidth on a fixed 1000-sample vector |
| TOL-04 **A** | §14 says quadrature tolerances "are relative and are not converted" then converts the absolute one; and "scaled by `hdata`" admits × or ÷ | relative tolerance unchanged; absolute tolerance **multiplied** by `hdata` | §14 | linter: no sentence both asserts and contradicts a conversion |

## GRID — grids and indices

| ID | Two readings | Chosen | Edit | Regression check |
|---|---|---|---|---|
| GRID-01 | grids stated by enumeration, step and endpoints simultaneously | every grid given by **one** integer formula and nothing else | §8, §9, §10 | linter: no grid statement carries two descriptions |
| SYM-01 **A** | `jlast` is "the last accepted index" (§1) / "the largest `j` with `acc(j)` true and `acc(j+1)` false" (§10) — these differ on any non-monotone `acc` | the §10 meaning; the registry entry is corrected to match | §1 registry; §10 | linter: symbol defined once |
| SYM-02 **B** | `k` is the `r_lo` node index (§1) / a kernel order (§5 "no kernel with `k = 4`") | kernel orders are written as literals; `k` stays the node index | §5 rewritten to name `Kraw4`/`Kw4` directly | linter: symbol defined once |
| SYM-03 **A** | §1 claims completeness while `i`, `a`, `p`, `row`, `mean` appear in equations | registry extended; the completeness claim is kept only because the linter now enforces it | §1 | linter: every code-block identifier is registered |
| SYM-04 **A** | §1 says §15.11 is "the complete list" of labels, but header labels are absent from it | §15.11 lists **outcome** labels; document-status labels are named separately | §1, §15.11 | linter: every `UPPER_SNAKE` token is in one of the two lists |

## COUNT — reporting granularity

| ID | Two readings | Chosen | Edit | Regression check |
|---|---|---|---|---|
| COUNT-01 **B** | boundary counts "per `(r_lo, μ)` aggregated over μ" — per node / summed over nodes | an array with a declared shape, `edge_count[model, r_lo_id, j, which]`, plus a stated aggregation for the report | §7 defines the counter, §15.9 declares the shape | linter: every counter has a declared shape |
| COUNT-02 **A** | the observed boundary count has no μ index yet is asked for per `(r_lo, μ)` | reported once per `(model, r_lo)` as two 0/1 integers | §15.9 | shape check |
| RANGE-01 **B** | §9 excludes "nodes returning a non-numeric outcome label"; a case-B node returns a **number** and a label | exclusion keyed on whether `L95` itself is numeric, not on whether a label was raised | §9 | test: a synthetic node set with one case-B node |
| RANGE-02 **A** | "largest violation" is the worst shortfall against the tolerance / the largest raw decrease; and after exclusions, adjacency closes the gap / drops both comparisons | shortfall against the tolerance; exclusions drop both comparisons and do not close the gap; "none" is reported when the sequence passes | §9 | test on a synthetic 10-node sequence |

## TERM — terminal states

| ID | Two readings | Chosen | Edit | Regression check |
|---|---|---|---|---|
| TERM-01 **B** | case C's `jlast` is undefined when no `acc(j)` true → `acc(j+1)` false pair exists (e.g. `acc(1)` false, rest true) | the case table is rewritten over the `acc` vector so that every pattern has an action; the pattern above gets its own label | §10 | test: enumerate the four qualitative `acc` shapes |
| TERM-02 **B** | case B's bisection has no `nsim`, no `stage`, no root | coarse count, `stage = 3`, `rootCal`, with the bisection index in the key | §10 case B | test: bisection is reproducible across two runs |
| TERM-03 **A** | `SdMC` is required as an output in cases A and B where its inputs do not exist | `NOT_DEFINED` in case A; in case B computed from the final bracket, which exists by construction | §10, §15 | shape check on all three cases |
| TERM-04 **B** | STOP aborts everything / only the affected item; and controls run before / after the pipeline | five distinct terminal verbs with stated scope, and a fixed execution order | new §12.0 and §15.0 | linter: every terminal token is one of the five |
| TERM-05 **A** | guard G4 applies to the observed fit only / to every simulated dataset | to every fit; a simulated dataset that trips it is counted and excluded from that node's sample, and the count is reported | §7 guard G4, §15 | counter shape check |

## CTRL — controls

| ID | Two readings | Chosen | Edit | Regression check |
|---|---|---|---|---|
| CTRL-01 **B** | control 2's comparison target omits the `1/R²` prefactor that §5 puts on `Kraw2` | the target carries the prefactor; the two routes differ only in whether `G₂` is applied explicitly | §12 row 2 | unit test: the two routes agree on a synthetic ξ |
| CTRL-02 **B** | control 3 evaluates `gcurve` by nearest row / interpolation; "their ratio" is `Kw2/gcurve` / the inverse | linear interpolation onto the fitted `r_mp`; ratio is `Kw2_norm / gcurve_norm`; rms with `ddof = 1` | §12 row 3 | value is invariant to input row order |
| CTRL-03 **B'** | control 7 gates at 1e-9 against a minimiser whose tolerance is unstated | the minimiser's tolerance is pinned tighter than the gate | §12 row 7 | unit test against the closed form |
| CTRL-04 **B** | control 8 pairs `r_hi`/`rXiMin` with "first and last", which is order-dependent while §4 is order-free | the ξ table is sorted ascending at load; the control then compares min↔first, max↔last | §4 adds the sort; §12 row 8 | test: an unsorted input file yields the same result |
| CTRL-05 **A** | control 6 varies ε to 0.10 without saying whether guard G2 is re-applied | G2 is re-applied at each ε; a violation there is a control failure, not a run guard | §12 row 6 | test at an ε that violates G2 |

## UNIT — units

| ID | Two readings | Chosen | Edit | Regression check |
|---|---|---|---|---|
| UNIT-01 **A** | `r_mp_over_h` holds `r_mp/h` (ratio `1/hdata`) / `r_mp·h` (ratio `hdata`); the document never says | the control is made direction-agnostic: it checks the ratio against **both** `hdata` and `1/hdata` and reports which matched, failing only if neither does | §12 row 1 | test on both orientations of a synthetic pair |
| UNIT-02 **B** | §14 orders `r_mp` converted; §3 says `r_mp` is never converted | §14 lists the quantities re-expressed, and states that re-expression means the same physical length in the other unit — so the bin window converts with `r_mp` and the same 15 bins are selected | §3 cross-reference; §14 | test: the dual run selects the same 15 bins |

## SIM — simulation counts

| ID | Two readings | Chosen | Edit | Regression check |
|---|---|---|---|---|
| SIM-01 **B** | §11's "100 000 sims per node" for branches versus §10's mandatory 200 000 on the refined grid | §11 states the coarse count only; refinement keeps 200 000, as in the primary | §11 | linter: no count stated in two places with different values |

---

## Deferred — not fixed in v6

| ID | Item | Why deferred |
|---|---|---|
| DEF-01 | Whether the KDE belongs in the frozen core at all, given that it affects only `SdMC` and through it the monotonicity verdict | Removing it changes what is computed. v6 pins its formula instead; the question is a method change and belongs to a later version. |
| DEF-02 | Whether the `L95(r_lo)` curve should remain the primary deliverable | Changes the estimand, not an ambiguity. Open for the supervisor. |
| DEF-03 | Control 4 has no threshold, so the Hartlap premise can never fail | Adding a threshold changes behaviour. Recorded, not changed. |

---

## Verification that this ledger is complete

Every blocking finding from both round-4 readers maps to exactly one ID above.
Reader A's B1–B19 and reader B's B1–B15, after removing the 20 duplicates, are
covered by the 28 entries; the non-blocking findings that had a mechanical fix
(SYM-02, SYM-03, SYM-04, TOL-02, TOL-04, CTRL-05) are included, and those whose
fix would change behaviour are in the deferred table.
