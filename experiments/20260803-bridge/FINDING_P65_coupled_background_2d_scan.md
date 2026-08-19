# FINDING P65 — a test-field analytic solution plus a systematic 2D scan: the "regular" region found by FINDING_P64 is not eternal

**Status:** Skeptic-reviewed (Step 8a) — **CONFIRMED-REAL**, no falsifying
issue found; six clarifications/caveats applied below in direct response.
**Script:** `P65_coupled_background_2d_scan.py` (`experiments/20260803-bridge/`)
**Scope:** `V=0`, background order, `ĝ≠0`. Symbolic derivation is
`[VERIFIED-SYMPY]`; the 2D scan and cross-validation numbers are
`[VERIFIED-NUMERIC]` — illustrative at tested grid/parameter choices.

NOT_VALIDATION — NOT_REFUTATION — OUR_RECONSTRUCTION — L0: descriptive.

---

## Direct response to the user's request

The user asked to "run the systematic 2D scan for the C1/C2/C3 boundary" —
`FINDING_P64`'s own explicitly-flagged next step. Before building the
literal grid, an analytic shortcut was checked by hand and confirmed
tractable (see below), and it turned out to reveal something important
enough to change how the 2D map itself should be read — so this finding
presents both, in the order they were actually discovered.

## Part A — a test-field analytic solution

Ignoring the `(1-ĝφ̄)` backreaction of `φ̄` on the Friedmann equation
(valid while `ĝφ̄` stays small), `E_φ` on the *fixed* `FINDING_P62`
background reduces to a linear ODE. Since `ρ̄_A·a³=C` exactly:

```
d/dt(a³φ̄̇) = ĝ·ρ̄_A·a³ = ĝC   (a CONSTANT right-hand side)
```

This integrates immediately: `a³φ̄̇(t) = a₀³φ̄̇₀ + ĝC(t-t₀)`. Verified
symbolically (`a₀³φ̄̇₀=√2` exactly, confirmed to `10⁻¹⁰`) and confirmed the
resulting closed form satisfies the test-field ODE identically
(`sp.simplify(...)==0`). A further closed form for `φ̄(T)-φ̄₀` (a
combination of logarithms) was derived by symbolic integration and
independently cross-checked against a separately-coded numeric evaluator
(two spot-checks, residuals `<10⁻¹⁷`).

**The structural fact this reveals:** the `T`-dependent term in the
closed form is `∝ĝ·log(T²b-1)`, and this coefficient **never cancels**
for `ĝ≠0`. As `T→∞`, `φ̄(T)` grows **without bound** — very slowly
(logarithmically), but unboundedly, for *any* nonzero `ĝ`. No test-field
trajectory is eternally regular; every finite boundary `1/ĝ` is
eventually reached, given enough time.

## Part B — cross-validation against the full nonlinear system

Before trusting either the analytic result or the numeric scan's
interpretation, the test-field prediction was checked against the full
(backreacting) numeric integration:

| `ĝ` | `φ̄(51)` full | `φ̄(51)` test-field | relative diff |
|---|---|---|---|
| 0.01 | 0.076506 | 0.076496 | `1.2×10⁻⁴` |
| 0.1 | 0.090789 | 0.090631 | `1.7×10⁻³` |
| 1.0 | 0.246100 | 0.231981 | `6.1×10⁻²` |

Small `ĝ`: excellent agreement — backreaction genuinely negligible over
this timescale. At `ĝ=1.0` the two already differ by 6%.

**Boundary-crossing time**, test-field root-find vs. `FINDING_P64`'s own
full-nonlinear event times:

| `ĝ` | test-field predicted `T` | actual (full) `T` |
|---|---|---|
| 3.0 | 12.999 | 9.672 |
| 10.0 | 1.720 | 1.710 |

At `ĝ=3`, the full system reaches the boundary **faster** than the
test-field prediction. **[Skeptic-completed]** Two co-directional
mechanisms, both independently confirmed numerically (not just asserted)
by comparing `H` and `ρ̄_A` between the full and test-field trajectories
at matched `t`: (1) as `φ̄` grows, `(1-ĝφ̄)` shrinks, lowering the
effective matter density sourcing `H` relative to the test-field
background — lower `H` means less Hubble friction on `φ̄̇`; **and** (2)
because `ȧ=Ha`, a lower `H` also means `a` grows *more slowly* than in
the test-field case, so `ρ̄_A=C/a³` — unaffected by the coupling directly,
but sensitive to `a`'s own trajectory — stays *larger* than the
test-field comparison at the same `t`, directly strengthening the source
term `ĝρ̄_A` in `E_φ`. Verified: at `ĝ=3`, `H_full<H_testfield` and
`ρ̄_{A,full}>ρ̄_{A,testfield}` simultaneously at every sampled `t∈[2,9]`.
Both effects push the same direction; the original version of this
finding named only the first.

## Part C — the systematic 2D scan (the literal request)

Grid: `ĝ` — 24 points, `±geomspace(0.01,10,12)` (both signs, log-spaced
magnitude, **`ĝ=0` itself not a grid point** — see below) — ×
`x0:=ĝφ̄₀` — 20 points, linear in `[-3.0, 0.95]` (`x0=1` is exactly the
boundary at `t₀`; `x0<1` required for a physical starting point). Fixed
reference horizon `t≤100`. `480` total points: **382 regular, 98 exit**
the physical regime within that window.

**[Skeptic-added]** `t≤100` is a **compute-budget choice, not a
physically motivated one** — with `FINDING_P39`'s `G_N`-vs-`ĝ`
normalization still open, this model has no established correspondence
to a real cosmic-time unit, so "100" carries no physical weight by
itself; it fixes *which* short/medium-term boundary is being mapped, no
more.

**[Skeptic-added]** The `(ĝ,x0)` parametrization is a **choice**, not the
only reasonable one — `x0` mixes `ĝ` and `φ̄₀` together (e.g. `ĝ=0.01,
x0=0.9` means `φ̄₀=90`, a large bare field value). The map's *shape*
would look different plotted directly in `(ĝ,φ̄₀)` — the "clean funnel"
described below is a real feature of the `(ĝ,x0)` view specifically, not
claimed to be parametrization-independent.

The resulting ASCII map (full detail in the script's own output) shows a
clean, physically sensible funnel in this `(ĝ,x0)` view: the regular
region is widest near `ĝ=0` and narrows as `|ĝ|` grows (the boundary
`1/ĝ` moves closer to `φ̄=0` and the driving source term strengthens
simultaneously), with a real asymmetry between positive and negative `ĝ`
reflecting the source term's sign. **`ĝ=0` itself is not a sampled grid
point** (log-spacing excludes it) — "regular at `ĝ=0`" is an inference
from `FINDING_P62`'s own already-rigorously-proven exact solution (no
coupling, no boundary to reach at all), not a measurement made by this
scan.

One representative `E_ii` code-fidelity check (per `FINDING_P64`'s own
corrected framing — an algebraic consequence of the coded RHS, not
independent physics) was run on the grid: `max|E_ii|=4.4×10⁻¹³`,
consistent with the finite-difference roundoff floor. **[Skeptic-noted]**
Sufficient to catch a *systematic* miscoding of the RHS (present at every
grid point if present at all), not a bug conditional on a specific
integration path — though such a path-dependent issue would likely
surface as a failed/NaN solve regardless, which the grid loop does not
silently suppress.

## Verdict

**The 2D scan maps a genuine, structured short/medium-term boundary** —
not an artifact of `FINDING_P64`'s sparse 1D sampling.

**Critical reframing, from Parts A/B:** this map should be read as a
`t≤100` boundary, not an eternal one. The test-field structural fact
(verified accurate to `<10⁻³` relative for small `ĝ`) says every `ĝ≠0`
trajectory from this reference IC eventually reaches *some* boundary,
given enough time — the 2D map's "regular" region is regular *up to the
scanned horizon*, which was not visible from `FINDING_P64`'s finite-time
results alone.

**Reading for C1/C2/C3, updated — [Skeptic-tightened]:** the case against
a clean C1 ("bounded but permanently regular domain") reading rests on
extrapolating the test-field's asymptotic divergence into a regime the
cross-validation in Part B never actually reaches. The test-field
approximation is verified accurate *while `ĝφ̄` stays small*; the
crossing itself happens exactly where `ĝφ̄→1` — precisely where that
approximation is weakest, and precisely the part of the trajectory this
finding did not numerically confirm for small `ĝ` (Part B only ran to
`t=51`/`t=10⁷` in earlier scouting, not to the — potentially
astronomically distant — `t` where crossing would occur for very small
`ĝ`). Backreaction is shown (Part B) to *accelerate* the approach to the
boundary wherever it has been checked, which argues against a
backreaction-induced stabilization *appearing from nowhere* at small
`ĝ` — but this is suggestive, not a proof that covers the untested
regime. **The honest statement:** if the true asymptotic behavior tracks
the test-field prediction, no `ĝ≠0` trajectory from this reference IC is
eternally regular, and the relevant question shifts to *timescale* — C2
(tied to `FINDING_P39`'s still-open `G_N`-vs-`ĝ` gap, fixing what a
realistic `ĝ` and cosmic-time unit are) vs. C3 (reaching the boundary at
all, however long it takes, signaling a genuine structural gap). This is
a **plausible reading given the evidence, not a demonstrated one** — a
reader should not treat "less supported" as "C1 is refuted." **Not
adjudicated here.**

## What this does NOT establish

- **That the full (backreacting) system genuinely diverges at long `ĝ`-
  dependent times for small `ĝ`.** Only verified up to `t=10⁷` for
  `ĝ=0.01,0.001` (outside the formally-scoped 2D scan itself, done as a
  scouting check before committing to this finding's design) — the full
  system tracked the test-field prediction closely there too, but this
  is not a proof it continues to do so at the (potentially
  astronomically larger) `t` where crossing would actually occur for
  very small `ĝ`.
- **The full causal decomposition of "backreaction accelerates" as
  independently proven** — two co-directional mechanisms (friction
  reduction, source-term enhancement) were confirmed numerically to both
  push the same direction, but no claim is made that these are the
  *only* two mechanisms or that their relative weights are known.
- **A precise analytic threshold condition** for the 2D boundary itself
  — the test-field solution gives the *asymptotic* structural fact
  (eventual, unbounded growth), not a closed-form prediction of the
  `t≤100` boundary's exact shape (which the cross-validation in Part B
  shows the test-field approximation does NOT reproduce quantitatively
  once `ĝφ̄` grows past ~0.1).
- **Adjudication of C1 vs. C2 vs. C3** — deliberately not resolved.
- **Sensitivity to a different reference background.** `φ̄₀` itself IS
  varied across the scan (via `x0`) — what's actually held fixed
  throughout is the background solution `FINDING_P62`'s own specific
  `(B,D)=(1,1)` provides (`a₀`, `φ̇₀`, and the functional forms `a(t)`,
  `ρ̄_A(t)` built from it). A different `(B,D)` choice, or a genuinely
  different reference cosmology, was not tested and could shift the map.
- **A `(ĝ,φ̄₀)`-parametrization-independent boundary shape** — the
  reported "funnel" is a feature of the `(ĝ,x0)` view specifically (see
  Part C); the same underlying data plotted directly in `(ĝ,φ̄₀)` would
  look different, though it would encode the same physical information.
- **That the single `E_ii` code-fidelity check rules out every possible
  RHS coding error** — it catches a systematic miscoding (present at
  every grid point), not necessarily a path-dependent one, though such
  an issue would likely surface as a failed/NaN solve regardless.
- **Resolution of `FINDING_P39`'s SI-normalization gap** — still open,
  and directly relevant to which `(ĝ,t)` regime is physically realistic;
  `t≤100` here is a compute-budget choice with no established physical
  correspondence.

## Not yet done

- A rigorous (not just scouting) very-long-time numeric confirmation that
  small-`ĝ` "regular" trajectories genuinely do eventually cross, at the
  timescale the test-field solution predicts.
- Independent verification of the "backreaction accelerates" mechanism —
  e.g., an analytic next-order (in `ĝφ̄`) correction to the test-field
  solution.
- A precise analytic fit or derivation for the `t≤100` boundary shape
  itself (only mapped numerically here).
- Sensitivity of the whole picture to the reference IC choice.
- Returning to the perturbation sector (`Ψ_k(t)`, D2/D3/D4) — still
  blocked on C1/C2/C3, now with a more nuanced but still unresolved
  picture.

## Skeptic Verdict table

| # | Claim reviewed | Skeptic verdict | Response |
|---|---|---|---|
| 1 | Symbolic test-field derivation (`d/dt(a³φ̄̇)=ĝC`, closed-form `δφ`) | Independently re-derived by hand, confirmed correct; log-domain checked, no sign/negative-argument issue | No change needed |
| 2 | Asymptotic unbounded-growth claim as `T→∞` | Mathematically genuine — the `ĝ`-coefficient on `log(T)` never cancels | No change needed |
| 3 | "Leans against C1" argument | **Real gap** — extrapolates the test-field asymptotic into the near-boundary regime (`ĝφ̄→1`) where the approximation is weakest and was never numerically confirmed for small `ĝ` | **Fixed**: Verdict section rewritten to state this explicitly, downgraded from "leans against" to "a plausible reading, not a demonstrated one" |
| 4 | "Backreaction accelerates" mechanism | Directionally right but incomplete — only named friction reduction, missed the co-directional source-term enhancement (slower `a`-growth → larger `ρ̄_A`) | **Fixed**: both mechanisms named, both independently confirmed numerically (`H_full<H_testfield` and `ρ̄_{A,full}>ρ̄_{A,testfield}` simultaneously) |
| 5 | 2D scan code correctness | No bugs found | No change needed |
| 6 | `(ĝ,x0)` parametrization and single-point `E_ii` check adequacy | Defensible for the stated purpose, but map shape is parametrization-dependent and the check catches systematic not path-dependent bugs | **Fixed**: both caveats added explicitly |
| 7 | `t≤100` horizon physical motivation | Real gap — compute-budget choice, not physically motivated given `FINDING_P39`'s open gap | **Fixed**: stated explicitly in Part C and "does NOT establish" |
| 8 | `ĝ=0` implicitly treated as sampled | Real gap — log-spacing excludes it; "regular at `ĝ=0`" is inferred from `FINDING_P62`, not measured here | **Fixed**: stated explicitly |
| 9 | "Different reference IC" caveat wording | Ambiguous — `φ̄₀` IS varied via `x0`; what's actually fixed is the background solution | **Fixed**: reworded to clarify |

**Overall verdict: CONFIRMED-REAL.** No falsifying issue found. All nine
points were clarifications and honest-scoping fixes to an already-correct
symbolic derivation and a bug-free numeric scan — the core results
(closed-form test-field solution, the 480-point 2D map, the
cross-validation numbers) are unchanged; what changed is how confidently
the C1/C2/C3 implications are stated.
