# FINDING P165 — an idealized local calculation says `H0,anchor` cannot
# absorb an unmodeled monopole effect; v82's own actual fitting procedure
# and its own Table II data say the opposite is empirically plausible

**Date:** 2026-08-30
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 math (symbolic identifiability audit, same method
as `FINDING_P133`/`FINDING_P161`) + direct primary-source cross-check
**Script:** `P165_monopole_degeneracy_check.py` — extends `FINDING_P161`'s
own identifiability machinery with one new parameter, `ε` (a fractional
monopole-tier perturbation, `F^(0)→(1+ε)·F^(0)`, this project's own
`A·g²≡ΔG` construction injected into v82's own written force law).
`ε=0` recovers `P161`'s own construction exactly (verified as a positive
control).
**Verdict (final, post-skeptic — see "Correction" below, this is a
substantive reversal of the original draft's Part A, not a wording
tweak):** `PART A (LOCAL MATH, CORRECTED SCOPE): under an idealized
construction that declares `H0,anchor` a literal, exogenous initial
condition decoupled from the force law at exactly z=0 (the same
construction `FINDING_P161` already used), `H(0)` is tautologically
identical to `H0,anchor` — its Jacobian row w.r.t. `(H0,anchor,β1,β2,ε)`
is `[1,0,0,0]`, PROVEN symbolically within that idealization. THIS DOES
NOT REPRESENT HOW v82's OWN REAL FITTING PROCEDURE TREATS H0,ANCHOR.
v82's own text states directly: the SH0ES anchor is "treated as a data
point at z=0.0233, not z=0" (Sec. IV.L); all three parameters
`(H0,anchor,β1,β2)` are "jointly optimize[d]... against all 33 data
points simultaneously" (Sec. II.G) — not read off a single point;
`H0,anchor` is explicitly retained as "a free-floating third fit
parameter" (Sec. IV.M) specifically because TJB could not pin it
independently. v82's own Table II reports `H0,anchor` ranging over a real
~8.6% span (67.40→73.22) with `(β1,β2)` co-optimized at each value to
comparable fit quality — direct EMPIRICAL evidence FOR the kind of
`H0,anchor`↔coupling trade-off this file's own local math claimed was
impossible, not evidence against it. The idealized local result is not
wrong as math, but it answers a narrower, more artificial question than
"could v82's real fit hide a monopole effect" — and the primary source,
read directly, points toward plausible degeneracy, not away from it.
PART B (independent of Part A, unaffected by this correction): at fixed
`H0,anchor`, the reduced 2×3 Jacobian of the two remaining leading `H(z)`
observables w.r.t. `(β1,β2,ε)` has rank 2 with a nonzero-`ε` null
direction `(δβ1,δβ2,δε)∝(C,C²,1)`, `C≡d0·m0/(k0·r0)` — β1 and β2 CAN
jointly compensate a monopole `ε` at leading order, independent of where
`(β1,β2)` currently sit. This local result survives independently of
Part A's correction. NET: `FINDING_P163`'s own residual gap is NOT
closed by this file — if anything, it is SHARPENED: both the idealized
local math (Part B) and v82's own real, reported fit behavior (Table II)
point toward the same conclusion, that a monopole-tier effect could
plausibly be absorbed into `(β1,β2,H0,anchor)` without being visible in
fit quality alone. Magnitude (negligible vs. dangerous) remains
undetermined either way.`
**Correction (2026-08-30, context-asymmetric skeptic-caught — this
review could not execute the script directly, no Bash tool available to
it, and said so explicitly; its primary-source claims were independently
re-verified against the actual v82 text before applying, not accepted on
the skeptic's word alone):** the first draft made two errors, one small
and one substantive. (a) **Citation error**: "v82's own Eq. 6" was cited
as the source of the `H0,anchor` initial condition. `[VERIFIED-PDF]`:
Eq. (6) is v82's own *general momentum-conserving accretion equation*
("Eq. (6) is the general, momentum-conserving form," p.5) — unrelated to
`H0,anchor`. The actual initial condition (`ṡ(0)=H0,anchor·d0`) appears
as unlabeled prose on p.6 and is named directly in Sec. IV.M (p.22).
Fixed throughout. (b) **Substantive overclaim**: the original Part A
verdict stated `H0,anchor` "is pinned by the real `H(z≈0)` anchor data
point... cannot be shifted to compensate ε regardless of ε's size" —
framed as a fact about v82's actual fitting behavior. Direct re-reading
of v82's own Sec. II.G, Sec. IV.L, Sec. IV.M, and Table II (all quoted
in full below, §2) shows this does not hold: v82's real fit does not
anchor at z=0, jointly optimizes all three parameters against the full
33-point dataset, explicitly could not pin `H0,anchor` independently
(kept it free specifically because of this), and its own reported
results show `H0,anchor` moving across a real range while `(β1,β2)`
co-vary to compensate. The corrected file below narrows Part A to what
the idealized local calculation actually shows (a fact about that
specific mathematical construction, not about v82's real fit) and adds
the counter-evidence from v82's own text as new §2b, changing the
overall verdict from "gap closed" to "gap sharpened, not closed."
**Continues/answers:** `FINDING_P163`'s own "What this file does NOT
establish," point 5 — "Does not address whether v82's own OVERALL
STATISTICAL FIT could be practically degenerate with an unmodeled
monopole-tier effect... whether `H0,anchor`... could partially absorb
some of what a real, unmodeled `ΔG`-like monopole effect would produce."

## 0. Premise — `NO_AUTHOR_ERROR`

`ε` is not a quantity in v82's own theory — v82's own `F^(0)` is written
with no coefficient at all (`FINDING_P159`/`FINDING_P163`). `ε` here is a
purely hypothetical device, injected by this project, to ask a
well-posed mathematical question about v82's own fit's structural
sensitivity: IF the real universe had a small, unmodeled monopole-tier
deviation from plain Newtonian gravity that v82's own force law (as
written) does not include, would v82's own `(β1,β2,H0,anchor)` fitting
procedure be structurally capable of absorbing it invisibly, or would it
show up? This bounds only what this project's own reconstruction of
v82's fitting procedure implies — not a claim that such a deviation
exists, or that v82's own theory is deficient for not including it.

## 1. Method — same machinery as `FINDING_P161`, one parameter added

`FINDING_P161` already built the full perturbative solution of v82's own
coupled `(s,z,H)` system (Eqs. 1-14) to 2nd order in cosmic time `t`
around `t=0`, extracting three leading observables — `H(0)`, `dY/dz|₀`,
`d²Y/dz²|₀` (`Y≡H²`) — as functions of `(H0,anchor, β1, β2)`, and proved
these three are jointly, locally identifiable (`rank(J)=3`).

This file adds exactly one new parameter, `ε`, multiplying `F^(0)` as
`(1+ε)` — the same `A·g²≡ΔG` construction this project's own `FINDING_
P21`/`P22`/`P163` already use for a monopole-tier deviation from Newton's
constant — and re-derives the same three observables as functions of
`(H0,anchor, β1, β2, ε)`. `[VERIFIED-sympy]` (`test_epsilon_zero_
recovers_p161_exactly`): setting `ε=0` recovers `P161`'s own `dY/dz|₀`
and `d²Y/dz²|₀` term-for-term, confirming this is a genuine superset
construction, not a divergent reconstruction.

## 2a. Part A — the idealized local math (corrected scope)

`[VERIFIED-sympy]` (`test_h0_anchor_is_pinned_independent_of_
everything`): the Jacobian row of the FIRST observable, `H(0)`, w.r.t.
`(H0,anchor, β1, β2, ε)` is exactly `[1, 0, 0, 0]` — proven by direct
symbolic differentiation, not inferred from a clean final formula. This
holds *within the specific idealized construction* used here and in
`FINDING_P161`: cosmic time `t` is expanded perturbatively around `t=0`,
with `s(0)=d0` and `ṡ(0)=H0,anchor·d0` declared as literal, exogenous
initial conditions (unlabeled prose, v82 p.6, formalized in Sec. IV.M
p.22 — **not** Eq. 6, a citation error in the first draft, corrected
here), decoupled from the force law at that instant by construction.
Under that construction, `H(0)` is tautologically identical to
`H0,anchor` — not merely correlated, definitionally equal — and this
holds for *any* force law whatsoever, since it follows purely from how
the initial-value problem is set up, before any force-law-specific term
enters.

**This is a real, correctly-proven fact about that idealized
construction. It is not, on its own, a fact about how v82's actual
fitting procedure behaves — see §2b.**

## 2b. Part A corrected — v82's own real fitting procedure contradicts the naive reading, empirically

`[VERIFIED-PDF]`, all four points read directly from v82's own text, not
inferred:

1. **The anchor is not at z=0.** Sec. IV.L (p.21), verbatim: *"Throughout
   this paper, SH0ES is treated as a data point at z=0.0233, not z=0."*
   `H0,anchor` in v82's own fit is not literally `H(0)` from a single
   `z≈0` measurement — it is a fitted parameter constrained by a data
   point at `z=0.0233`, among 33 total points.
2. **All three parameters are fit jointly, not sequentially.** Sec. II.G
   (p.11), verbatim: *"we... jointly optimize all three free parameters
   (H0,anchor, β1, and β2) against all 33 data points simultaneously."*
   This is a single, coupled chi-squared minimization — not a procedure
   where `H0,anchor` is fixed first from one point and `β1,β2` fit
   afterward (which is closer to what the idealized §2a construction
   implicitly models).
3. **TJB himself could not pin `H0,anchor` independently and says so.**
   Sec. IV.M (p.22), verbatim: *"We therefore retain H0,anchor as a
   free-floating third fit parameter,"* after describing an explicit,
   failed attempt to ground `s0, ṡ0` in independent real data (circular
   reasoning; no well-defined "typical peculiar velocity" at the
   relevant scale). This is the *opposite* of `H0,anchor` being cleanly,
   independently pinned.
4. **v82's own Table II is direct empirical evidence of exactly the
   trade-off Part A's original claim said was impossible.** Table II
   (p.12) reports `H0,anchor` fixed at several representative values
   spanning `67.40→73.22` km/s/Mpc (an 8.6% range, between the Planck and
   SH0ES anchors) with `β1, β2` **re-optimized at each value** to
   comparable fit quality (`χ²₃₃` mostly `15.75–34.14` across the range,
   per the table's own reported column). This is a real, reported
   demonstration that `H0,anchor` can move substantially while `(β1,β2)`
   absorb the difference without a correspondingly catastrophic fit-
   quality collapse — the empirical shape of a genuine degeneracy, not
   proof against one.

**Consequence:** the first draft's claim that `H0,anchor` "is pinned...
cannot be shifted to compensate ε regardless of ε's size" does not
survive contact with v82's own text. The idealized local construction
(§2a) proves a fact about *that specific construction* — declaring
`H0,anchor` an exogenous initial condition makes it trivially independent
of everything else *within that declaration* — but v82's own real fit
does not treat `H0,anchor` this way at all: it is one of three jointly-
optimized parameters, not independently pinned, and the paper's own
reported results show it trading against `(β1,β2)` over a real range.
The naive mechanism `FINDING_P163`'s own residual gap named is not shown
false by this file — the opposite: v82's own data gives it a foothold.

## 3. Part B — a separate, local degeneracy via β1 and β2 jointly (independent of Part A, unaffected by its correction)

`[VERIFIED-sympy]` (`test_epsilon_and_beta_degeneracy_at_fixed_h0_
anchor`): as a *conditional* result — IF `H0,anchor` is held fixed
(matching v82's own "fix `H0,anchor` at several representative values,
re-optimizing only `β1,β2`" procedure, Sec. II.G p.11, the same procedure
Table II itself reports) — the reduced `2×3` Jacobian of the two remaining
observables (`dY/dz|₀`, `d²Y/dz²|₀`) w.r.t. `(β1, β2, ε)` has **rank 2**
— the maximum possible for a `2×3` matrix, and by rank-nullity this
guarantees (not merely permits) a 1-dimensional null space. The
informative question is not *whether* a null direction exists (it must,
by counting alone, whenever rank=2 with 3 unknowns and 2 equations) but
*whether its `ε`-component is zero* (no real degeneracy — `ε` would be
independently pinned by these two observables alone) *or nonzero*
(`ε` genuinely absorbable). Computed directly: the null vector is

```
(δβ1, δβ2, δε) = (d0·m0/(k0·r0), (d0·m0/(k0·r0))², 1) · t,   for any t
```

**The `ε`-component is nonzero** — confirmed by direct inspection, not
approximation. This means: a small monopole perturbation `ε` *can* be
exactly compensated, at leading order, by simultaneously shifting
`β1 → β1+δβ1` and `β2 → β2+δβ2` along this specific direction, leaving
both `dY/dz|₀` and `d²Y/dz²|₀` — the leading-order *shape* of `H(z)` near
`z=0` — completely unchanged. This is a second, independent line of
evidence for a real degeneracy, on top of — not instead of — the direct
empirical evidence already found in v82's own Table II (§2b): both a
local mathematical construction (this section, `H0,anchor` fixed) and
v82's own actually-reported joint fit behavior (§2b, `H0,anchor` free)
point toward the same qualitative conclusion, that a monopole-tier
effect is plausibly absorbable into this framework's own fitted
parameters without a clean, isolated signature.

## 4. The degeneracy direction is set by physical scale, not by where `(β1,β2)` currently sit

`[VERIFIED-sympy]` (`test_degeneracy_direction_is_independent_of_beta_
operating_point`): the null vector `(δβ1, δβ2, δε)` contains **no**
`β1` or `β2` symbols at all — checked directly via `.free_symbols`, not
assumed from the clean closed form. It depends only on `C≡d0·m0/(k0·r0)`,
the ratio of v82's own physical baseline pair-separation and node-mass
scale to its baseline node-radius/thermal-energy scale (`d0`, `m0`,
`k0`, `r0` — the same symbols `FINDING_P161`'s own script leaves as free,
unassigned-value parameters). Two consequences: (a) this is not a
special feature of v82's own particular fitted `β1≈1.4×10¹⁰, β2≈7.7×10¹⁷`
values — the same degeneracy direction would exist at any `(β1,β2)`
operating point, since it is a leading-order (linearized) fact about the
*force law's own structure*, not about the current fit; (b) `δβ2 = C·δβ1`
along this direction — a clean, checkable relation between how much `β2`
must shift per unit shift in `β1` to keep compensating the same `ε`.

## 5. What this file does NOT establish

1. **Not a claim about v82's own theory being wrong or incomplete**
   (`NO_AUTHOR_ERROR`, §0) — `ε` is this project's own hypothetical
   device, not a claim about what the real universe or v82's own theory
   actually contains.
2. **Does not determine whether the degeneracy (Part A/§2b's empirical
   version, or Part B/§3's local-math version) is practically dangerous
   or practically negligible in magnitude.** v82's own Table II shows
   `H0,anchor` moving over a real range with comparable fit quality, but
   this file does not re-derive or re-fit Table II's own numbers, does
   not quantify how much of that range-tolerance would remain if a
   specific-sized `ε` were injected, and does not compute the numeric
   value of `C=d0·m0/(k0·r0)` (Part B) in v82's own actual units. Both
   remain natural next steps, not attempted here.
3. **§2a/§3's results are LOCAL/leading-order** — a 2nd-order Taylor
   expansion near `z=0`, not a re-derivation of v82's own full 33-point
   fit. §2b's evidence, by contrast, IS v82's own full-range, real result
   (Table II) — read directly, not derived by this file's own math.
4. **Does not test whether the accretion correction term** (`F_acc`,
   dropped in Part B as `FINDING_P161` proved it never touches `β1`/`β2`'s
   own Jacobian columns) **could interact with `ε` differently** —
   `F_acc`'s self-referential `H(z)`-dependence was checked against
   `β1`/`β2` in `P161`, not against a hypothetical monopole `ε` here.
5. **Does not re-open or contradict `FINDING_P163`'s own main verdict**
   (item 4's tier-mismatch answer) — that verdict was about v82's
   *written* model structure (`F^(0)` has no coefficient, full stop),
   which this file's own `ε=0` positive control confirms is exactly
   right as written. This file addresses the *separate*, explicitly
   flagged residual question about the fitting *procedure's* structural
   sensitivity — and, after correction, finds that question sharpened
   toward "plausible degeneracy," not resolved toward "no degeneracy."
6. **Does not establish that a real monopole effect exists**, or that
   v82's own reported `Table II` range-tolerance is CAUSED by an
   unmodeled monopole effect specifically, as opposed to ordinary
   parameter-fitting flexibility unrelated to any monopole channel —
   only that the data pattern is *consistent with* the kind of
   degeneracy this file was checking for, not a demonstration that this
   specific mechanism is what produces it.
