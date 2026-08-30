# FINDING P163 — docs/150 §6 item 4: does the growth-rate ceiling
# `A·g²≲8.39×10⁻¹²` connect to v82's own fit parameters `(β1,β2,H0,anchor)`?

**Date:** 2026-08-30
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (structural comparison, not a
falsification-ladder experiment — no new claim is tested, this is a
provenance/tier check on two already-established quantities)
**Verdict (final, post-skeptic — see "Correction" below for what
changed and why):** `NOT-CONNECTED AT THE LEVEL OF v82's WRITTEN MODEL,
AND NOT MERELY A UNITS-CONVERSION GAP. The growth-rate ceiling A·g² is
specifically a MONOPOLE-TIER quantity in this project's own hypothetical
covariant-completion construction (F_MULT(r)=A·c_G·g²·m₁m₂/r², P21/P22)
— but v82's own monopole term, read directly from its own equations,
carries ZERO free coefficient at that tier (F⁽⁰⁾=−Gm_Am_P/s², Eq. 2 —
plain, unmodified Newtonian gravity; only β1, β2, H0,anchor are fitted,
per FINDING_P161's own title, and those three live entirely at the
DIPOLE and QUADRUPOLE tiers). This is the DECISIVE reason: there is no
v82-native quantity occupying the tier A·g² constrains — not because the
numbers haven't been converted yet, but because v82's own force law does
not populate that channel at all. v82's own β1, β2 REINFORCE this: they
are, structurally, dimensionless coefficients of a directly-fitted
algebraic force law (`[VERIFIED-sympy, FINDING_P159]`), with no field-
theoretic Lagrangian, no A-like normalization constant, and no g-like
monopole coupling anywhere in their own construction — a different KIND
of object from A, g, κ, not a differently-scaled version of the same
one. A THIRD, already-established fact — A and g are not independently
well-defined within this project's own reconstruction either (only the
product A·g² has external meaning, per P21/P22; g's own units are
unresolved, FINDING_P39; and FINDING_P133 already proved (A,g,κ) are not
jointly identifiable, rank=2<3) — is real but, on correction, does NOT
function as an independent third blocker: the comparison item 4 asks for
only ever needs the already-well-defined product A·g², so this fact adds
compounding weakness on this project's own side rather than a separate
way the comparison fails. NOT ADDRESSED: whether v82's overall
STATISTICAL fit of (β1,β2,H0,anchor) against real data could practically
be degenerate with an unmodeled monopole effect via H0,anchor (an
initial condition, not a coupling) — a distinct question from the
model-structure claim above. The honest answer to item 4
is not "open, needs unit reconciliation" but "closed: no bridge exists,
for a specific, checkable structural reason — the two quantities occupy
different, non-overlapping tiers of the force law, and one side of the
would-be comparison isn't even well-defined on its own terms."`
**Correction (2026-08-30, context-asymmetric skeptic-caught, two points,
both independently re-derived before applying — not accepted on the
skeptic's word alone):** the first draft (a) presented §1-2 (tier
mismatch), §3 (A,g individually ill-defined), and §4 (β1,β2 a different
kind of object) as "three independent facts, each individually
sufficient" to block the comparison. On independent re-check this
overstates §3's role: the comparison at hand is `A·g²` (already a
well-defined *product*, per §3's own point 1) against a hypothetical
v82-native monopole coefficient — if v82 *did* have one, comparing the
product directly would need neither `A` nor `g` separately, so §3's
non-identifiability finding does not actually block *this specific*
comparison; it is real, already-established context about this
project's own construction, not a third freestanding blocker. Reframed
below: §1-2 (tier mismatch) is the decisive reason, §4 reinforces it, §3
is included as compounding context, not as an independent condition. (b)
The verdict's strong language ("no bridge exists") was a claim about
v82's *written model structure* (Eq. 2 has no coefficient) but did not
explicitly disclaim a distinct, unexamined question: whether v82's
*overall statistical fit* (using `β1,β2,H0,anchor` together against real
`H(z)` data) could be practically degenerate with — i.e. partially
absorb — an unmodeled monopole-tier effect through `H0,anchor` (an
*initial condition*, not a coupling, and therefore a different kind of
free parameter than a force-law coefficient). This is a real gap, now
named explicitly in "What this file does NOT establish," not resolved
here.
**Continues/answers:** `docs/150` §6 item 4 ("Do the `A·g²` growth-rate
ceiling (bottleneck 3) and v82's own fit parameters connect at all, once
unit conventions are reconciled?").

## 0. Premise — `NO_AUTHOR_ERROR`

This file bounds only whether *this project's own* hypothetical
covariant-completion parametrization `(A,g,κ)` can be meaningfully
compared, numerically, against v82's own fitted `(β1,β2,H0,anchor)`. It
says nothing about whether TJB's own theory, if and when fully
covariantly completed by TJB himself, would or would not populate a
monopole-tier channel — only that v82 **as currently written** (Eqs.
1-4) does not. `A·g²` itself is not part of MULTING as TJB has published
it; it is a quantity from *this project's own* attempted covariant
completion (`FINDING_P21`/`P22`), external to anything TJB has written.

## 1. What `A·g²` is, and which tier it occupies — `[VERIFIED-file]`

`FINDING_P22_archidiacono_beta_mapping.md:96-97` (quoting `FINDING_P21`'s
own corrected force law):

> "F_MULT(r) = A·c_G·g²·m₁m₂/r² = (A·g²/4π)·m₁m₂/r², defining ΔG via
> F_MULT(r) ≡ ΔG·m₁m₂/r²: ΔG = A·g²/4π"

This is a **monopole-tier** quantity by construction: it scales as
`m₁m₂/r²`, the same functional form as ordinary Newtonian gravity, with
no dependence on any internal node property (`k_A`, `r_A`, etc.) — it is
literally *defined* as a fractional addition to Newton's own constant,
`ΔG`. The external bound this project derived, `A·g²≲8.39×10⁻¹²` (SI,
m³kg⁻¹s⁻²), comes from mapping this monopole-tier `ΔG` against an
assumed-analogous dark-matter fifth-force channel (Archidiacono et al.,
`FINDING_P22`) — itself already flagged there as a **soft ceiling**, not
a precision result (`FINDING_P22`'s own "User-Flagged Correction"
section, lines 219-230).

## 2. v82's own monopole tier carries zero free coefficient — `[VERIFIED-PDF/FINDING_P159]`

v82's own Eq. 2, quoted directly in `FINDING_P159_beta_ratio_v82_vs_two_
charge_prediction.md:55`:

```
F^(0) = -G m_A m_P / s^2                                          (2)
```

No coefficient, no `A`, no `g`, no fitted parameter of any kind — `G` is
the ordinary Newton's constant, unmodified. The **only** three quantities
v82 fits to data are `(β1, β2, H0,anchor)` (`FINDING_P161`'s own title
and construction throughout), and both `β1` (Eq. 3) and `β2` (Eq. 4)
multiply exclusively the **dipole** and **quadrupole** force terms
respectively — `F^(1)` and `F^(2)`, both of which depend on the internal
node quantities `k_A/c², r_A` (dipole) and `k_A k_P r_A r_P/c⁴`
(quadrupole), unlike the monopole term. v82's own force law, as written,
simply does not have a monopole-tier free coefficient to compare `A·g²`
against — this is a structural fact about which channel v82's own fit
touches, not an unconverted-units problem.

## 3. This project's own `A`, `g` are not independently well-defined either — compounding context, not an independent blocker (corrected scope)

**Corrected role (skeptic-caught, point (a) above):** the comparison
`docs/150` §6 item 4 asks for is `A·g²` (already a well-defined product,
per point 1 below) against whatever v82's own fit offers at that tier.
§2 already shows there is nothing there to compare against — so this
section's own finding, that `A` and `g` individually are ill-defined
within this project's construction, does **not** add a second,
independent way the comparison fails; it would only matter if the
comparison needed `A` or `g` *separately* (e.g. against two distinct
v82-native numbers), which it does not. It is included here as
already-established, relevant context — this project's own side of a
hypothetical future comparison is doubly troubled, not just blocked once
— not as a third necessary condition for §5's verdict.

Three already-established facts (none newly derived here) illustrate this:

1. **Only the product `A·g²` is externally meaningful.** `FINDING_P22`
   works entirely with `A·g²≡ΔG` — no external channel this project has
   found constrains `A` or `g` separately.
2. **`g`'s own units are internally unresolved.** `FINDING_P39_g_ghat_
   dimensional_consistency_audit.md` finds two incompatible readings
   still open within this project's own construction: `g` dimensionless
   (P21's stated assumption, line 60) vs. `[g]=kg⁰m⁻¹s¹` (forced by
   `FINDING_P33`'s own reused `m_eff` formula, line 84) — this file does
   not resolve that ambiguity, only notes it is still live.
3. **`(A,g,κ)` are not jointly identifiable from this project's own
   observables at all**, independent of v82. `FINDING_P133` proved
   `rank(Jacobian)=2<3` for the observable set `(O1=A·g², O2=A·κ²,
   O3=κ/g)` this project actually has access to — an exact algebraic
   degeneracy (`O2≡O1·O3²`), not a numerical coincidence. There is no
   principled single value of `A` or `g` alone to extract from this
   project's own construction, even before asking whether it would
   compare to anything in v82.

## 4. v82's `β1, β2` are a structurally different kind of object

`FINDING_P159` §1 (independently sympy-verified there, not re-derived
here): v82's `β1`, `β2` are **dimensionless**, direct algebraic
coefficients of a two-body force law fitted to `H(z)` data — with **no**
underlying field-theoretic Lagrangian, no `A`-like overall field-
normalization constant, and no `g`-like monopole coupling anywhere in
their own construction. `A`, `g`, `κ` are, by contrast, couplings in a
**hypothetical, never-completed** covariant scalar-field action
(`S=∫d⁴x(1/2)(∂φ)²+Σᵢ∫dτ[g·mᵢ+pᵢ·∇]φ(xᵢ)`, `FINDING_P39:60`) that this
project attempted to construct as a completion of MULTING's own force
law — a project-internal theoretical scaffold, not anything TJB has
published. Comparing a dimensionless, directly-fitted force-law
coefficient (`β1`) against a dimensional coupling in an unfinished field
theory (`A·g²`, units m³kg⁻¹s⁻²) is not a matter of applying a conversion
factor between two unit systems (like Mpc → m) — it requires *inventing*
a physical relationship between two constructions that were never
designed to correspond, which is a new theoretical claim this file does
not make.

## 5. Answer to item 4 (corrected structure, skeptic-caught point (a))

**No, they do not connect at the level of v82's written model — and the
reason is structural, not merely that "unit conventions" have not yet
been "reconciled."** One decisive reason, reinforced by a second;
a third, already-established fact adds compounding context without
being an independent condition of its own:

1. **Decisive.** `A·g²` occupies the monopole tier; v82's own monopole
   tier has zero free coefficient in its written equations. There is no
   v82-native number to compare `A·g²` against (§1-2).
2. **Reinforcing.** v82's `β1, β2` are dimensionless coefficients of a
   directly-fitted algebraic force law with no field-theoretic
   normalization behind them — a different *kind* of object from `A, g,
   κ`, not merely a differently-scaled version of the same one (§4).
3. **Compounding context, not a third independent blocker (corrected).**
   Even setting reason 1 aside, `A` and `g` are not independently
   well-defined within this project's own construction (§3) — but since
   the comparison item 4 asks for only ever needs the already-well-
   defined *product* `A·g²`, this fact does not by itself block anything
   beyond what reason 1 already blocks; it only shows this project's own
   side of a hypothetical future comparison carries a second, separate
   weakness.

`docs/150` §6 item 4's own phrasing ("once unit conventions are
reconciled") presupposes the comparison becomes meaningful after a units
conversion. This file finds that presupposition does not hold for v82's
*written model*: there is no arithmetic step that would make the
comparison meaningful, because the two quantities are not measuring the
same physical channel. See "What this file does NOT establish," point 5,
for the distinct, unexamined question of whether v82's *overall
statistical fit* could nonetheless be practically degenerate with an
unmodeled monopole effect.

## What this file does NOT establish

1. **Not a claim about v82's own theory being wrong or incomplete**
   (`NO_AUTHOR_ERROR`, §0) — v82's own choice to leave the monopole tier
   unmodified is a modeling choice TJB is free to make; this file only
   confirms it is a choice v82's own Eq. 2, as written, actually makes.
2. **Does not resolve `FINDING_P39`'s own `[g]` ambiguity** — noted as
   still-open context for point 2 of §3, not addressed here.
3. **Does not resolve `FINDING_P133`'s own identifiability blocker** —
   cited as independently-standing prior evidence, not re-derived.
4. **Does not rule out that some future, genuinely different quantity**
   (not `A·g²` as currently constructed) could someday connect this
   project's own reconstruction to v82's fitted numbers — only that the
   specific comparison `docs/150` §6 item 4 named does not work, for the
   reasons given.
5. **Does not address whether v82's own OVERALL STATISTICAL FIT could be
   practically degenerate with an unmodeled monopole-tier effect**
   (skeptic-caught, correction (b) above) — this file's claim is about
   the *written model's structure* (Eq. 2 literally has no coefficient),
   not about whether fitting `(β1,β2,H0,anchor)` together against real
   `H(z)` data could, in practice, let `H0,anchor` (an *initial
   condition*, not a force-law coupling) partially absorb some of what a
   real, unmodeled `ΔG`-like monopole effect would produce. That is a
   distinct, numerical/statistical identifiability question this file
   does not raise or examine.
5. **Does not address bottleneck 3's own status** beyond this specific
   cross-reference question — `docs/147`'s own "STRUCTURALLY BLOCKED"
   verdict for bottleneck 3 (via `FINDING_P133`) is unchanged by this
   file, which only closes the separate question of whether v82 offers
   an alternative route around that block. It does not.
