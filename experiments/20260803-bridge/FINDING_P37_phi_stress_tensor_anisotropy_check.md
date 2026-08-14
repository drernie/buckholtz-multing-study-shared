# P37 — φ's own static stress tensor has genuine, independently-confirmed anisotropic stress at the same O(ĝ²) order as ΔG: a real slip *source* exists, its magnitude on Φ,Ψ not yet solved for

**Date:** 2026-08-14
**Status:** **CORRECTED after context-blind skeptic review, same day —
the most favorable outcome of any review this campaign.** The core
physical claim (nonzero anisotropic stress) *survived* an independent
by-hand re-derivation by the reviewer. Issues found were about
completeness and framing, not a wrong core result: the assumed action
was never stated explicitly; the original "trace cross-check" was weaker
than it looked (tests internal algebraic consistency of one summed
formula, not independent information about the individual components);
and the "necessary but not sufficient" hedge on `Φ≠Ψ` *undersold* the
result. A genuine, independent conservation check (`∂ᵢT_ij=0`, using the
actual equation of motion) and a positive-energy-density check (`T₀₀`)
were added. Full verdict in the new §6 below.
**Origin:** fourth step of the covariant-completion campaign
(`PLAN_final_goal_20260814.md`), resumed at a deliberately slower pace
per explicit user instruction — one step at a time, full processing
before the next. Directly targets the narrowest, safest piece of P35's
own flagged open question (its withdrawn §5, its §6 point 8): does `φ`'s
own stress-energy, for the static solution `φ(r)=ĝM/(4πr)` P35 already
derived, actually have a nonzero anisotropic (traceless spatial) part?
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P37_phi_stress_tensor_anisotropy_check.py`, ruff clean, all
assertions pass.

## 0. Honest scope — deliberately narrow

This does **not** solve the full linearized Einstein `ij`-equation for
the resulting metric slip — that is a larger, separate step, appropriately
deferred, not attempted here. This finding only computes `φ`'s own
stress tensor `T_μν^φ` explicitly and checks whether its spatial part is
proportional to the identity (isotropic, no slip *source*) or has a
genuine traceless remainder (anisotropic — a real slip *source*, though
not yet its magnitude on the actual metric potentials `Φ,Ψ`).

**[CORRECTED — this framing undersold the result.]** ~~A nonzero
anisotropic source is necessary but not sufficient for `Φ≠Ψ`... requires
an implausible, fine-tuned cancellation in solving that equation.~~ For
a well-behaved, localized, static source that falls off at infinity (as
this one does), the standard `ij`-trace-free elliptic equation has a
**unique** solution under standard boundary conditions (ordinary
Green's-function/elliptic-PDE uniqueness) — `Φ=Ψ` despite this nonzero
source would require a *non-standard* boundary condition, not an ad hoc
"fine-tuned cancellation" with free parameters to tune (there are none
here). **This project does not, however, adopt any specific closed-form
value for `Φ−Ψ`** — the skeptic reviewer independently computed one
candidate closed form during review, but per this project's own Audit
Verification Gate (`audit-verification-gate.md`: "Agent's `[VERIFIED]`
is your `[INFERRED]`"), that specific result is **not** independently
re-checked here and is **not** cited as established. The equation itself
remains unsolved in this finding; only the qualitative uniqueness
principle is stated.

Uses the flat-background `φ(r)` from P35 (re-used, not re-derived) as the
leading-order field — standard, legitimate perturbative bookkeeping:
`φ`'s own equation only needs the flat metric to be solved correctly at
this order; its back-reaction on the metric is precisely the *next*-order
question this finding is investigating the source for, not something it
needs to have already solved to ask the question.

## 1. Method — the standard canonical scalar stress tensor, computed directly

**[CORRECTED — the assumed action was never stated explicitly before;
per skeptic review, added here.]** Canonical, minimally-coupled scalar,
`S_φ=∫d⁴x√-g·(1/2)(∂φ)²`, linear matter coupling, no potential, no
non-minimal `R`-coupling — P33/P34/P35's own already-flagged convention,
re-used here unchanged, not a new assumption.

`T_μν=∂_μφ∂_νφ−(1/2)g_μν(∂φ)²` — the same formula implicit in P34's own
`ρ_φ=φ̇²/2` (there, the homogeneous, time-only case; here, the static,
spatial-gradient-only case). Evaluated in Cartesian coordinates on
`φ(r)=ĝM/(4πr)` to avoid any risk of a spherical-coordinate conversion
error:

```
T_xx = ĝ²M²(x²−y²−z²)/(32π²r⁶)
T_yy = ĝ²M²(−x²+y²−z²)/(32π²r⁶)
T_zz = ĝ²M²(−x²−y²+z²)/(32π²r⁶)
T_xy = ĝ²M²xy/(16π²r⁶)
```

## 2. The load-bearing check — radial vs. tangential stress on the z-axis

On the `z`-axis (`x=y=0,z=r`), the radial direction is manifestly
`ẑ`, so `T_zz` is the radial stress and `T_xx=T_yy` (verified equal by
the script's own assertion) is the tangential stress by symmetry:

```
T_radial     =  +ĝ²M²/(32π²r⁴)
T_tangential =  −ĝ²M²/(32π²r⁴)
T_radial − T_tangential = ĝ²M²/(16π²r⁴)    (nonzero for all r>0)
```

**Isotropic (no anisotropic stress)?** `False` — confirmed by direct
calculation, not assumed.

## 3. Trace check — relabeled honestly (not independent verification)

`trace(T_ij) = Σᵢ(∂ᵢφ)² − (3/2)(∂φ)² = −(1/2)(∂φ)²` in 3 spatial
dimensions, confirmed exactly (script assertion, zero difference)
against the direct computation from §1. **[CORRECTED]** ~~a genuine
algebraic cross-check, not a repeat of the same computation~~ — per
skeptic review, this is weaker than that framing implied: each `T_ii` is
built from the *same formula* being summed, so this verifies internal
consistency of sympy's simplification, not independent information about
the individual components — a correlated sign error across all three
diagonal entries would still pass this specific check. Kept for context;
§4 below supplies the genuinely independent check.

## 4. Genuinely independent check — spatial divergence (added after skeptic review)

`∂ᵢT_ij` must vanish for `r>0` (the source-free region), by conservation
— equivalent to `φ`'s own equation of motion `∇²φ=0` there (already
established in P35). Unlike §3, this uses the *individual* components'
actual functional form, not just their sum — a correlated sign error
would generically **not** pass this check:

```
∂ᵢT_ix = 0
∂ᵢT_iy = 0
∂ᵢT_iz = 0
```

Confirmed exactly (script assertions, all three zero). A second free
check: `T₀₀=(1/2)(∂φ)²`, manifestly non-negative (a sum of squares) —
confirms the canonical, not ghost/wrong-sign, kinetic term for this
configuration.

## 5. What this establishes, precisely

`φ`'s own static stress-energy has genuine, nonzero, now
independently-confirmed anisotropic stress at `O(ĝ²)` — the **same**
parametric order as P35's own `ΔG` (the additive scalar-induced
correction to Newton's constant, **not** the full Newtonian potential
`G_N M/r`, which is `O(ĝ⁰)` — a clarification the original text left
ambiguous). This means P35's original, withdrawn claim
("second-order-small, no slip") could not have been correct even at the
level of checking whether a source exists — the source is present at
exactly the order that claim dismissed. This *sharpens* P35's own honest
"genuinely open" status, moving it from "unknown whether a source
exists" to "a source demonstrably exists, now with an independent
conservation check confirming the computation; its magnitude on `Φ,Ψ`
is the remaining open question."

## 6. Skeptic verdict (context-blind, Step 8a, 2026-08-14)

Reviewed with `claim.md`-equivalent content (this finding, pre-correction)
+ the script, **no session history**, per Falsification Ladder Context
Asymmetry Rule. The reviewer independently re-derived all stress-tensor
components by hand and constructed the standard sourced-potential
formalism to check the core claim. **The most favorable outcome of any
review this campaign:**

| # | Issue | Verdict | Disposition |
|---|---|---|---|
| 1 | Signature-convention risk in `T_μν` | CONFIRMED-REAL (no bug) | No fix needed |
| 2 | Does `T_radial≠T_tangential` actually license "a slip source exists"? | CONFIRMED-REAL | Reviewer independently confirmed the logic and constructed the sourced-potential formalism |
| 3 | Trace check is a trivial identity (correlated errors would pass) | WEAKENED | Relabeled honestly (§3); genuine `∂ᵢT_ij=0` check added (§4) |
| 4 | "Necessary but not sufficient" framing understates uniqueness | WEAKENED (finding undersold its own result) | Corrected to state standard elliptic-PDE uniqueness, without adopting the reviewer's own unverified closed-form claim (§0) |
| 5 | "Same parametric order as `ΔG`" ambiguous vs. full Newtonian potential | WEAKENED | Clarified explicitly (§5) |
| 6a | `T_ij~1/r⁴` diverges as `r→0` | Flag only | Noted — standard point-source self-energy divergence, doesn't affect the local `r>0` claim |
| 6b | Missing `T₀₀` check (free positive-energy confirmation) | Suggestion | Added (§4) |
| 6c | Missing `∂ᵢT_ij=0` check (genuine independent verification) | **Most valuable suggestion** | Added (§4) |
| 6d | Assumed action never stated explicitly | WEAKENED, flagged high-severity if action were non-canonical | Stated explicitly (§1) — confirmed canonical per P33/P34/P35's own convention |

**What survives:** the core claim (genuine, nonzero anisotropic stress at
`O(ĝ²)`) — independently re-derived by the reviewer and now additionally
confirmed by a genuine conservation check this finding did not originally
have. **What was corrected:** completeness (explicit action statement),
honest labeling of which checks are independent vs. which merely test
algebraic self-consistency, and a framing correction that *strengthens*
rather than weakens the practical conclusion. Kill classification:
framing/completeness only — the closest thing to a clean pass this
campaign has produced.

## Reproduction

```bash
python experiments/20260803-bridge/P37_phi_stress_tensor_anisotropy_check.py
```
