# P34 — an explicit gravitational sector (flagged, standard GR) reduces MULTING's own matter+scalar action to a self-consistent FRW background; whether ΔG (P21–22) is a background or perturbative effect is NOT established by this finding alone (see P35)

**Date:** 2026-08-14
**Status:** **CORRECTED after context-blind skeptic review, same day.**
Three real issues, none core-predicate-false (the derived equation,
`φ̈+3Hφ̇=ĝρ₀`, is correct and unchanged). Most consequential: the
original title and §3 claimed `ΔG` "turns out to be a linear-perturbation
effect, not a background G_N modification" — this finding's own §4 (What
this does NOT establish) explicitly excludes any linear-perturbation
analysis, so that claim could not be concluded from this finding's own
background-only calculation. This is the same "conclusion arrives before
the analysis that would justify it" pattern already caught in P29/P30/P31
this session. Also corrected: "two independent derivation routes" was
overclaimed — the two routes share the same underlying action (Noether's
theorem *requires* their agreement, it doesn't confirm anything
independently). Full verdict in the new §5 below.
**Origin:** first step of the covariant-completion campaign
(`PLAN_final_goal_20260814.md`), authorized this session to pursue the
`S→field equations→forces→T_μν→H(z)→μ,γ,Σ` chain autonomously toward
either a working minimal completion or a proof of underdetermination.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P34_frw_background_two_routes.py`, ruff clean, all assertions pass.

## 0. Honest scope, and a units gap found before starting

Before writing any new physics, `two_field_action_closure.py` (the sole
authoritative source for MULTING's own reconstructed action, per Gate 1
Artifact Identity discipline) was re-read directly, not recalled from
memory. Finding: the action as literally stated there (`S = ∫d⁴x(1/2)(∂φ)²
+ Σᵢ∫dτᵢ[g·mᵢ+...]φ(xᵢ)`) appears **only as a print statement** (lines
111–116 of that file) — it has never been symbolically encoded or
dimensionally checked end-to-end anywhere in this project. This finding
does **not** inherit a units convention from the source (none was ever
fixed); it fixes one explicitly (`c=1`-relative units for the derivation,
standard practice in this literature) and defines `ĝ:=g/c` as a single
symbol throughout, sidestepping the source's own unfixed `c`-bookkeeping
rather than silently resolving it. Restoring explicit SI-like `c`-factors
to match P21–P33's own convention is deferred, flagged as future work —
not attempted here.

This finding does **not** derive the full Einstein field equations
(tensorial variation w.r.t. `g_μν`) — only the FRW-reduced (homogeneous)
background equations, via the standard, valid "minisuperspace" shortcut
of substituting the FRW ansatz into the action before varying (specific
to homogeneous/isotropic backgrounds, not the general case). Linear
perturbations (`μ,γ,Σ`) are P35+, not attempted here.

## 1. Method — single-metric action, gravitational sector explicitly added

Per P33's own corrected lesson (never silently assume a gravitational
sector), one is added here **explicitly, flagged as a choice**: the
simplest possible closure, standard unmodified Einstein-Hilbert gravity,
minimally coupled to a single physical metric `g_μν` (no second,
"Einstein-frame" metric invoked anywhere — MULTING's own action never
specified one, and P33's correction showed inventing one without
justification is exactly the overreach to avoid):

```
S = S_EH[g] + S_φ[φ,g] + S_matter[worldlines,φ;g]
S_EH   = standard, unmodified — the Friedmann equation this produces is
         the ordinary textbook one, H²=(8πG_N/3)ρ_total; NOT independently
         re-derived here (well-established GR result, unaffected by
         matter's φ-dependence, which enters only through ρ_total below)
S_φ    = ∫d⁴x√-g · φ̇²/2   (canonical, c=1 units, flagged)
S_matter = −Σᵢ∫dτᵢ · mᵢ(1−ĝ·φ(xᵢ)),  ĝ:=g/c
         (P33's own m_eff(φ)/m=1−(g/c)φ, re-used unchanged — that
         algebraic identification was NOT weakened by P33's correction,
         only its imported gravitational-sector consequences were)
```

Matter is treated as pressureless dust (standard for this class of
problem): bare rest mass is separately conserved (particle number
conservation, unaffected by `φ`), so the bare comoving mass
`M=ρ₀a³=const`; the *effective* (gravitating) density is
`ρ_m,eff=ρ₀(1−ĝφ)`.

## 2. Two independent derivation routes for the scalar's background equation

**Route A — Bianchi identity / total energy conservation.** Uses *only*
bare-mass conservation (`ρ̇₀=−3Hρ₀`) and the standard definitions
`ρ_m,eff=ρ₀(1−ĝφ)`, `ρ_φ=φ̇²/2`, `p_φ=φ̇²/2` (canonical scalar, no
potential), `p_m=0` (dust) — plugged into the standard total-conservation
law `ρ̇_total=−3H(ρ_total+p_total)`, which is *forced* by the Bianchi
identity for any matter content once gravity itself is standard,
unmodified GR. Solving for `φ̈` gives:

```
φ̈ + 3H·φ̇ = ĝ·ρ₀
```

**Route B — direct Euler-Lagrange variation.** Reduces the matter+scalar
action to a 1D (minisuperspace) Lagrangian for `φ(t)` alone, treating
`a(t)` and the comoving bare mass `M=ρ₀a³` as external background
functions (standard, valid for a homogeneous test-scalar sourced by
homogeneous dust), and derives `φ`'s own equation of motion via the
actual Euler-Lagrange equation — a *structurally different* starting
point (direct field variation, not energy bookkeeping). Result:

```
φ̈ + 3H·φ̇ = ĝ·ρ₀    (identical to Route A, ρ₀=M/a³)
```

**Both residuals vanish identically** (script assertion, `sp.simplify`
confirms exact algebraic zero). **[CORRECTED]** ~~This is a genuine,
non-tautological positive control — the two routes share no common
derivation step (Route A never touches the action; Route B never touches
energy conservation)~~ — this framing overclaimed. Route A's own
`ρ_φ=φ̇²/2`, `p_φ=φ̇²/2`, `ρ_m,eff=ρ₀(1−ĝφ)` are definitions read
*directly off* `S_φ`/`S_matter`, the very same action Route B varies. By
Noether's theorem, the Euler-Lagrange equations and the stress-energy
conservation law of a consistently-varied action are not independent
facts — their agreement is *required* by the theorem, not evidence *for*
it. This is a genuine **algebraic consistency check** (it does catch
typos, sign errors, and arithmetic slips — real value, since the two
routes independently hand-transcribed the same physics into different
formalisms) — not a Perelman-audit-style positive control, which needs an
*independent* oracle for the correct answer. Additionally, Route A's own
`ρ̇_total=−3H(ρ_total+p_total)` presupposes Einstein's equations hold for
this matter+scalar content with the standard, minimally-coupled `T_μν` —
a standard, textbook-plausible premise, but not independently re-derived
or verified anywhere in this script.

## 2b. External literature cross-check attempted — honest evidence-tier note

A background verification agent was asked to independently check this
structure against published mass-varying-particle / conformally-coupled
scalar-tensor cosmology literature (context-blind to my derivation, given
only the claimed equations). It reported the *structure* of Route A/B's
result as consistent with Brax, Davis, Li, Winther & Zhao, arXiv:1206.3568
(a chameleon/symmetron N-body paper), specifically citing their Eq. 9
(`ρ̇_m+3Hρ_m=0` for the bare matter density) and Eqs. 3–4 (`□φ=−βT+dV/dφ`,
`β=M_Pl·dlnA/dφ`, matching this finding's `ĝ` up to a `−M_Pl` normalization
convention) — and separately flagged that a wrongly-recalled "Bekenstein
1977" candidate citation is actually 1982 and mechanistically different
(couples to the EM field strength, not particle mass) — that miscitation
was never used in this finding, only floated in the verification prompt,
so nothing here needed correcting for it.

**Per this project's own Audit Verification Gate (`audit-verification-
gate.md`): a sub-agent's `[VERIFIED]` is my `[INFERRED]`, not my
`[VERIFIED]`.** I attempted to independently re-confirm by fetching
arXiv:1206.3568 myself (WebFetch on both the abstract page and the PDF) —
the abstract page carries no equations, and the PDF's text extraction
failed (compressed/binary stream, no readable equations recovered). **I
could not independently verify the specific equation numbers claimed.**
Marking this cross-check `[WEAK — sub-agent-sourced, structure plausible
and directionally consistent, NOT independently re-verified against the
primary text]`, not `[VERIFIED-WEBFETCH]`. This does **not** weaken
§2's central result, which rests on the internal Route A/Route B
cross-check (two structurally independent derivations agreeing exactly)
— that check needs no external citation to be valid, and remains the
load-bearing verification for this finding.

## 3. Structural observation — what THIS reduction shows about `ΔG` (P21–22) — corrected

~~The background Friedmann equation above uses the **unmodified** `G_N` —
`S_EH` was never touched by matter's `φ`-dependence.~~ **[CORRECTED]**
*By the choice made in §1* (standard, minimally-coupled `S_EH`, explicitly
flagged there as a choice, not derived — any `f(φ)R` non-minimal coupling
would give a *different*, modified background), the background Friedmann
equation uses the unmodified `G_N`. The *only* background-level deviation
from `ΛCDM` in *this reduction* is through `ρ_total`'s own content
(`ρ_φ`, and `ρ_m,eff`'s `ĝφ` correction), both second-order-small
whenever `ĝφ≪1` — consistent with `two_field_action_closure.py`'s own
line-128 claim ("MULTING q-blind on background, = `ΛCDM@73`"), which had
been *asserted* there since P1.

**[CORRECTED — the consequential fix.]** ~~New, previously-unstated
distinction: `ΔG`... is structurally a **linear-perturbation / two-body
potential effect**... not a background-level `G_N→G_N+ΔG` replacement.~~
This was an **unsupported leap**, caught by skeptic review: §4 of this
very finding explicitly excludes any linear-perturbation analysis, so a
claim about *where* `ΔG` lives cannot be concluded from this finding's
own background-only calculation. What is actually established: `ΔG` is
**not present in this background reduction**, under minimal coupling.
*Where* it lives is a question this finding does not answer on its own —
concluding "it lives in perturbations" requires an actual perturbative
calculation, not performed here.

**Addendum, added after the correction above was applied:** `FINDING_P35`
(built the same day, after this correction) independently performs
exactly that missing calculation — a static, weak-field, point-source
derivation from the same action — and *does* show `ΔG=ĝ²/(4π)` emerges
from the two-body potential, matching P21's own founding relation exactly.
That is `P35`'s result, established by `P35`'s own work, not something
this finding is entitled to claim as its own.

## 4. What this does NOT establish

1. The full (non-homogeneous) Einstein field equations — only the FRW
   minisuperspace reduction. Tensorial variation w.r.t. `g_μν` in general
   is not performed here.
2. Any statement about linear perturbations, `μ(a,k)`, `γ(a,k)`, or
   `Σ(a,k)` — that is P35, not yet attempted.
3. A restored, explicit-`c` version matching P21–P33's own SI-like
   convention — deferred, flagged.
4. Anything about the `κ` (dipole) sector — entirely about the monopole
   (`g`) sector, matching every prior finding in this sub-arc.
5. That this specific gravitational-sector choice (standard, unmodified
   EH) is the *only* one consistent with MULTING's matter action — it is
   the *simplest* choice, explicitly flagged as such (§1); other choices
   (e.g. a direct non-minimal `φ²R` coupling) are not excluded, only not
   pursued here per the plan's cheapest-differentiating-test ordering.
6. Any comparison against Table A1 — closed gate, not touched.
7. Per NO_AUTHOR_ERROR: entirely this project's own reconstruction
   (OUR_RECONSTRUCTION), not a claim about TJB's own unpublished theory.
8. **[ADDED after correction] That this scalar could plausibly drive
   late-time acceleration on its own.** With no potential `V(φ)`, `φ`'s
   equation of state is `w_φ=p_φ/ρ_φ=1` (canonical kinetic-energy-only
   scalar) — a **stiff fluid**, diluting as `ρ_φ∝a⁻⁶`, faster than matter
   (`a⁻³`) or radiation (`a⁻⁴`). This construction, as it stands, has
   nothing that can act like dark energy at late times — either a
   cosmological constant sits inside `S_EH` (never mentioned anywhere in
   this reconstruction) or a potential `V(φ)` needs to be added later,
   which would change `p_φ≠ρ_φ` and invalidate Route A's specific
   `p_total=ρ_φ` substitution as written (Route B's Euler-Lagrange
   variation would need `V(φ)` added to `L_φ` directly). Flagged as a
   real, currently-unaddressed scope limit, not previously noted.

## 5. Skeptic verdict (context-blind, Step 8a, 2026-08-14)

Reviewed with `claim.md`-equivalent content (this finding, pre-correction)
+ the script, **no session history**, per Falsification Ladder Context
Asymmetry Rule, explicitly asked to check for the "two routes agree but
share a hidden common input" pattern already caught 4 times this session.
Seven issues found, summarized:

| # | Issue | Verdict | Disposition |
|---|---|---|---|
| 1 | "Two independent routes, non-tautological positive control" | **WEAKENED** | Both routes read inputs off the same action; Noether's theorem *requires* agreement. Relabeled "algebraic consistency check" (§2) |
| 2 | §3 "unmodified G_N" reads as a discovered fact, not a stated §1 choice | **WEAKENED** | Explicit "by the choice made in §1" qualifier added throughout (§3) |
| 3 | §3 "`ΔG` is a linear-perturbation effect" is an unsupported leap given this finding's own §4 exclusions | **WEAKENED (most consequential)** | Withdrawn to "`ΔG` not present in this background reduction; where it lives is not established here" — see §3's addendum noting `FINDING_P35` (built same day) independently supplies the missing calculation |
| 4 | `sp.simplify==0` labeled a "positive control" overstates a symbolic equality check | **WEAKENED** | Folded into issue 1's fix |
| 5 | Route A's Bianchi argument presupposes Einstein's equations hold for this matter content, unverified here | **NEEDS-EXPLICIT-FLAG** | Flagged explicitly in §2 and in the script's Route A docstring |
| 6 | Dead code (`solved_a`, `eom_a` computed but unused) | INFO | Fixed — both now feed real assertions in the script |
| 7 | Canonical no-potential scalar is a stiff fluid (`w=1`), cannot drive late-time acceleration | HYPOTHESIS/scope-limit | Added as §4 point 8 |

**What survives:** the derived equation `φ̈+3Hφ̇=ĝρ₀` is correct (both
derivation paths, algebra checks out) and the observation "no background
`G_N` modification appears in this reduction, under the minimal-coupling
choice" is valid. **What does not survive:** the claim that `ΔG` has been
shown to live in linear perturbations specifically, and the "independent
positive control" framing of the two-route check. Kill classification:
framing/scope, not core-predicate-false.

## Reproduction

```bash
python experiments/20260803-bridge/P34_frw_background_two_routes.py
```
