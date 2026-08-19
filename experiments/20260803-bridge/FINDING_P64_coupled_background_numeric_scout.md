# FINDING P64 — g_hat≠0 coupled background is regime-dependent: regular for small |ĝ|/moderate φ̄₀, exits the physical (ρ_phys≥0) regime in finite time for large ĝ or φ̄₀ near 1/ĝ

**Status:** Skeptic-reviewed (Step 8a) and corrected. Genuinely
strengthened by three added checks (negative `ĝ`, φ̄-displacement
magnitude, integrator-sensitivity cross-check), not just re-worded.
**Script:** `P64_coupled_background_numeric_scout.py` (`experiments/20260803-bridge/`)
**Scope:** `V=0`, background order, `ĝ≠0`. **All claims [VERIFIED-NUMERIC]**,
not `[VERIFIED-SYMPY]` — illustrative/regime-dependent at specific
`(ĝ, φ̄₀)` choices, not a general proof for all parameter/IC space.

NOT_VALIDATION — NOT_REFUTATION — OUR_RECONSTRUCTION — L0: descriptive.

---

## Direct continuation of FINDING_P63

`FINDING_P63` proved the four typed background equations (`E_00, E_ii,
E_φ, E_ρ`) are mutually consistent under general covariance (an off-shell
Bianchi identity), ruling out C4 (internal inconsistency) — but explicitly
left C1-vs-C2-vs-C3 open, naming "attempt an actual solution" as the
natural next step.

## Method choice

A closed-form solution, as `FINDING_P62` found for `ĝ=0` (the exactly
solvable dust+stiff-fluid FRW system), is not expected to exist once `ĝ≠0`
couples `φ̄` into the Friedmann equation nonlinearly via `(1-ĝφ̄)`. Rather
than commit to a symbolic perturbative construction (order-by-order in
`ĝ`) without first knowing whether the system even behaves regularly,
this finding scouts **numerically** first. `scipy` is an existing
declared project dependency (`pyproject.toml`/`requirements.txt`), not a
new one.

## What was built

The three already-solved background equations from `FINDING_P63` were
integrated as an explicit ODE system (`ρ̄_A=C/a³` algebraically from `E_ρ`,
`φ̄̈` from `E_φ`, `H` from `E_00`, `ȧ=Ha`) — **`E_ii` was never imposed
directly**, reserved as a code-fidelity self-check (see corrected framing
below).

Initial conditions were matched to `FINDING_P62`'s own exact `ĝ=0`
solution at `t₀=1`, integrated forward with `scipy.integrate.solve_ivp`,
with a terminating event at `ρ_phys/ρ̄_A=1-ĝφ̄=0`.

## Skeptic review (Step 8a) — two framings corrected, real checks added

Context-blind review (finding.md + code only) confirmed the ODE
implementation itself is correct (independently re-derived the event
logic and the RHS), but found the write-up overclaimed in two specific,
verifiable ways, plus flagged three genuine coverage gaps. **All five
were independently verified before acceptance and fixed with real
computation, not just softened wording:**

**1. The "E_ii self-check" does not test independent physics.** The
skeptic derived, and this file independently re-verified via `sympy`
(before accepting), that given how `H` (from `E_00`), `φ̄̈` (from `E_φ`),
and `ρ̄̇_A` (from `E_ρ`) are *coded*, `E_ii=0` is an **algebraic identity**
of the RHS as written — it holds on any trajectory this code produces,
regardless of whether the physics is right, as long as the formulas were
transcribed correctly. The original framing ("independent test of P63's
closure identity," "confirms... to near machine precision") overclaimed
on both counts: it is a **code-fidelity check** (would catch a
sign/factor typo relative to `FINDING_P63`'s own formulas — a real,
useful thing to check), not independent evidence the physics holds; and
the measured residual (`~10⁻¹¹`–`10⁻¹²`) sits almost exactly at the
finite-difference method's own expected roundoff floor
(`ε_machine/dt≈10⁻¹¹` at `dt=10⁻⁵`) — consistent with exact zero, not
confirmation of something smaller than that floor. **Fixed:** renamed
`check_Eii_selfconsistency`→`check_Eii_code_fidelity`, reworded every
print statement to state precisely what is and isn't being tested.

**2. "Singular" was the wrong word.** The skeptic pointed out (and this
file independently re-verified symbolically) that at `1-ĝφ̄=0`, `H²`
reduces to `K·φ̄̇²/2≥0` — generically *positive*, not zero or negative.
The ODE itself stays perfectly finite there; `φ̄̈` is finite too.
Terminating the integration at that surface is a **modeling decision**
(the `ρ_phys<0` regime is deemed unphysical for ordinary dust), not a
mathematical blow-up. **Fixed:** every occurrence of "singular"/"hits a
singularity" replaced with "exits the physical regime," with the
finite-`H` fact stated explicitly in the script's own printed output.

**3. "Not a numerical artifact" was asserted, not demonstrated.** Only
one solver (`RK45`), one tolerance, one `max_step` had been tried.
**Fixed:** added Sweep 3 — re-ran the `ĝ=3.0` boundary-exit case with
three genuinely different methods (`RK45`, `DOP853`, `LSODA`) and
different tolerances. Exit times agree to **3.7×10⁻⁷ relative
precision** — now a *demonstrated*, not merely asserted, robust feature
of the dynamics.

**4. Small-`ĝ` "regular" could have been "coupling hasn't kicked in
yet."** A fair concern: over a fixed integration window, weak coupling
might look "regular" simply because it hadn't had time to do anything.
**Fixed:** now reports `Δφ̄` (net displacement from `φ̄₀`) for every
regular trajectory. Even at `ĝ=0.01`, `Δφ̄≈+0.077` over `t≤51` —
non-trivial, not vacuous.

**5. Negative `ĝ` was untested — a qualitatively different regime (source
term sign flips).** **Fixed:** Sweep 1 now includes `ĝ=-1.0,-0.1` —
both regular, with `Δφ̄` of the same order of magnitude as the positive
cases (no sign-driven pathology observed at these values).

**6. C3 attribution was over-committed relative to the evidence.** The
skeptic pointed out that reaching the `ρ_phys=0` boundary in finite time
is equally compatible with C1 (bounded-but-real regularity domain — very
common for nonlinear systems, doesn't by itself require new machinery),
C2 (which side of the boundary is "physically relevant" depends on the
still-open `FINDING_P39` `G_N`-vs-`ĝ` normalization — could simply place
the realistic `ĝ` safely inside the regular region), or C3. **Fixed:**
the Verdict section (both in-script and below) now presents all three as
live possibilities with explicit reasoning for each, adjudicating none.

## Results (post-correction)

**Sweep 1** — `φ̄₀=0`, `ĝ ∈ {-1.0, -0.1, 0.01, 0.1, 0.3, 1.0, 3.0, 10.0}`,
integrated to `t=51`:

| `ĝ` | Outcome | `Δφ̄` |
|---|---|---|
| -1.0 | Regular | -0.0816 |
| -0.1 | Regular | +0.0592 |
| 0.01, 0.1, 0.3, 1.0 | Regular | +0.077 to +0.246 |
| 3.0 | Exits physical regime at `t≈9.67` | — |
| 10.0 | Exits physical regime at `t≈1.71` | — |

**Sweep 2** — `ĝ=0.3` fixed, `φ̄₀ ∈ {-0.5, 0.0, 0.5, 0.9/ĝ}`: first three
regular (`Δφ̄` all `≈0.1`), last (`φ̄₀≈3.0`, boundary at `1/ĝ≈3.33`) exits
at `t≈14.04`.

**Sweep 3** — integrator cross-check on the `ĝ=3.0` exit: `RK45`,
`DOP853`, `LSODA` agree to `3.7×10⁻⁷` relative precision.

**Sanity assertions (all passed):** at least one regular trajectory; at
least one regime-exit trajectory (confirms the split was actually
*observed*); max `E_ii` code-fidelity residual `<10⁻⁶` on regular
trajectories; integrator spread `<10⁻³` relative.

## Verdict

**Regime-dependent, not a uniform answer.** For small `|ĝ|` (`≤1.0`
tested, both signs) with `φ̄₀` not close to `1/ĝ`, the coupled system
evolves regularly over long timescales, with genuinely non-trivial `φ̄`
displacement. For large `ĝ` (`≥3.0` tested) or `φ̄₀` close to `1/ĝ`, `φ̄`
is driven monotonically toward the `ρ_phys=0` surface by the `ĝρ̄_A`
source term, and reaches it in finite time — a robust, method-independent
feature of the dynamics, not a solver artifact, but **not a mathematical
singularity either**: the ODE stays finite there, and stopping is a
modeling choice about where `ρ_phys<0` becomes unphysical.

**On C1 vs. C2 vs. C3: three live readings, not one.** This finding does
not adjudicate between them:

- **C1-compatible:** the system admits regular solutions within a
  bounded region of `(ĝ, IC)` space — common for nonlinear systems, no
  new machinery required by this observation alone.
- **C2-compatible:** which side of the boundary is "physically relevant"
  depends on `FINDING_P39`'s own still-open `G_N`-vs-`ĝ` SI relation —
  resolving it could simply place a realistic `ĝ` inside the regular
  region.
- **C3-compatible:** if a realistic `ĝ` and IC genuinely fall in the
  exit region, `ρ_phys<0` may signal the point-particle-dust
  construction needs a new prescription there — one live possibility,
  not established here.

## What this does NOT establish

- **A general proof for all `(ĝ, IC)` space** — two 1-D sweeps around one
  reference trajectory, not a systematic 2-D scan.
- **A clean analytic threshold condition** predicting when the boundary
  is hit — observed numerically, not derived.
- **Which regime is physically relevant** — depends on `FINDING_P39`'s
  still-open gap.
- **Late-time (`t→∞`) asymptotic behavior** of the regular trajectories —
  only finite-`t` regularity was checked.
- **A single C1/C2/C3 verdict** — deliberately not adjudicated; see above.
- **That the `E_ii` code-fidelity check is independent physical
  confirmation** — it is a code-correctness check only, per the
  skeptic-corrected framing above.
- **A wider parameter sweep for `|ĝ|` between 1.0 and 3.0** — the exact
  location of the regular/exit boundary (as a function of `ĝ` at
  `φ̄₀=0`) was not mapped, only bracketed.

## Not yet done

- A systematic 2-D `(ĝ, φ̄₀)` scan to map the regular/exit boundary
  precisely.
- An analytic (even perturbative) understanding of *why* and *when* the
  boundary is reached.
- Late-time asymptotic analysis of the regular trajectories.
- Whether `FINDING_P39`'s SI-normalization gap, once resolved, would fix
  `ĝ` to a value inside or outside the regular regime found here.
- Returning to the perturbation sector (`Ψ_k(t)`, D2/D3/D4) — still
  blocked on resolving C1/C2/C3 more definitively than this finding does.

## Skeptic Verdict table

| # | Claim reviewed | Skeptic verdict | Response |
|---|---|---|---|
| 1 | ODE implementation (H, φ̄̈, event logic) correctness | Independently re-derived, confirmed correct | No change needed |
| 2 | "E_ii self-check confirms P63's closure identity to near machine precision" | **Overstated** — `E_ii=0` is an algebraic identity of the coded RHS, not independent physics; residual sits at the finite-difference roundoff floor | **Fixed**: reframed as a code-fidelity check throughout, precision language corrected |
| 3 | "Singular trajectory" terminology | **Misleading** — the ODE stays finite at `ρ_phys=0`; termination is a modeling choice | **Fixed**: relabeled "exits the physical regime" throughout, finite-`H` fact stated explicitly |
| 4 | "Not a numerical artifact" claim | Asserted, not demonstrated — only one solver/tolerance tested | **Fixed**: Sweep 3 added, three methods agree to `3.7e-7` relative |
| 5 | Small-`ĝ` "regular" could be coupling-too-weak-to-matter | Real concern, not previously quantified | **Fixed**: `Δφ̄` now reported for every regular trajectory, confirmed non-trivial |
| 6 | Negative `ĝ` untested | Real coverage gap | **Fixed**: added to Sweep 1, both regular |
| 7 | "C3-flavored structural boundary" as the physical reading | **Over-committed** — equally compatible with C1 (bounded domain) or C2 (normalization) | **Fixed**: Verdict presents all three as live possibilities, adjudicates none |

**Overall: WEAKENED → substantially strengthened.** No claim was
falsified outright, but several were meaningfully overstated in the
original version. All six corrections involved real new computation
(sympy re-derivation, three new solver runs, a wider parameter sweep),
not just softened language — the finding is more defensible now than
before review, not merely more hedged.
