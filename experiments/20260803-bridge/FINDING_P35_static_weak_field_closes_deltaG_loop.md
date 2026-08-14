# P35 — a flat-background Yukawa-exchange calculation reproduces the functional form of P21's ΔG formula under a specific, already-flagged-as-conventional normalization choice; the full self-consistent O(ĝ²) treatment (and the slip question) remain genuinely open

**Date:** 2026-08-14
**Status:** **CORRECTED after context-blind skeptic review, same day.**
Four real issues, the most consequential of which is a genuine physics
gap, not just framing. Most consequential: independently re-reading
`FINDING_P21_shared_phi_normalization_constraint.md` directly (not from
memory, per the skeptic's flagged open question) confirmed P21's own
already-corrected text states the normalization constant `A`'s
*placement* is "a convention, not a forced discovery" — P21 never claimed
a specific numeric value for `A`. This script's canonical-kinetic-term
choice makes `A=1` true *by construction*, not by independent physical
content, so the original "P21's relation is derived, not merely
restated" claim was substantially circular. Second, genuinely-a-physics-
gap issue: §5's "qualitative slip, second-order-small" claim conflated
two different perturbation expansions and was simply wrong (not just
unproven) — withdrawn to an open question. Full verdict in the new §7
below.
**Origin:** second step of the covariant-completion campaign
(`PLAN_final_goal_20260814.md`), continuing directly from P34's explicit
gravitational-sector choice (standard, unmodified Einstein-Hilbert
gravity).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P35_static_weak_field_closes_deltaG_loop.py`, ruff clean, all
assertions pass.

## 0. Honest scope

This is the static, weak-field, point-source (two-body Newtonian) limit
— not the cosmological perturbation theory of P34's own FRW background.
It reuses two already-established, already-verified building blocks
rather than re-deriving them (Using Wheels First):

1. **P34's own matter+scalar Lagrangian**, here kept fully
   space-*and*-time dependent (P34 only ever derived the spatially
   *homogeneous* FRW-restricted case — the general, non-homogeneous
   field equation is the genuinely new derivation step in this finding).
2. **P19's own already-skeptic-confirmed 3D Green's function**
   (`∇²[1/(4πr)]=−δ³(x)`, `CONFIRMED-REAL`,
   `FINDING_P19_greens_function_normalization_derived.md`) — cited
   directly, not re-derived from scratch.

**What this does NOT establish, stated up front (expanded in §4):** the
static two-body `G_eff` extracted here is **not automatically** the same
object as P30's *cosmological* growth-equation `G_eff` — connecting a
static, `k→∞`-subhorizon potential to the full perturbed cosmological
Poisson equation is a standard, well-established step in scalar-tensor
cosmology (the quasi-static, sub-horizon approximation), but that step
is **not performed here**, only asserted as plausible. This finding
closes the loop on P21's own *definition*, not on P30's cosmological
usage of `G_eff` — those remain linked only by name until a genuine
quasi-static reduction is done (deferred, flagged as the actual content
of the plan's still-open "P36" item).

**Relationship to `FINDING_P34`'s own correction (added after P34's
skeptic review landed, same day):** `FINDING_P34`'s original text claimed
`ΔG` "is structurally a linear-perturbation / two-body potential effect,"
a claim its own skeptic review withdrew as an unsupported leap — P34
*alone* only showed `ΔG` is absent from the *background*, not where it
actually lives. **This finding is the calculation that closes that gap**
— built independently, the same day, before the P34 skeptic verdict was
read — and its own result (§3–§4 below) is exactly what P34's corrected
text now points to. The two findings are complementary and mutually
consistent: P34 (corrected) says "not in the background, location not
shown by that finding alone"; this finding shows the location (the
static two-body potential) directly, from the same action.

## 1. Method — the general (non-homogeneous) scalar field equation

Same Lagrangian density P34 used, restored to full space+time dependence:

```
L = (1/2)φ̇² − (1/2)(∇φ)² − ρ(x)·(1−ĝφ)
```

Direct Euler-Lagrange variation (sympy, `general_scalar_field_equation`)
gives:

```
φ̈ − ∇²φ = ĝ·ρ(x)
```

**Static limit** (`φ̈=0`), point source `ρ(x)=M·δ³(x)`:

```
∇²φ = −ĝM·δ³(x)
```

## 2. Solving via P19's own already-confirmed Green's function

Using `∇²[1/(4πr)]=−δ³(x)` (P19, `CONFIRMED-REAL`):

```
φ(r) = ĝM/(4πr)
```

Verified (script, `sp.simplify` on the spherical Laplacian away from the
origin) to solve the source-free Laplace equation for `r>0` exactly.

## 3. Fifth-force potential energy, combined with the standard Newtonian term

From the *same* matter-action interaction term used throughout P33–P35
(`S_matter=−∫dτ·m(1−ĝφ)` ⟹ `U_5th=−m·ĝ·φ(r)`):

```
U_5th(r) = −ĝ²mM/(4πr)
```

~~Attractive for like-sign `ĝ`, matching `two_field_action_closure.py`'s
own docstring point 2...~~ **[CORRECTED]** "Like-sign" is meaningless
here — `U_5th` is attractive for *any real* `ĝ`, since `ĝ` enters
**squared** (`m_eff` applies to both the source and the test particle).
The original wording uncritically echoed the source docstring's phrasing
without checking whether it actually applied to this specific
calculation — flagged by the skeptic as a "pattern-matching tell."

**[CORRECTED]** ~~Combined with the standard (P34: `S_EH` unmodified)
Newtonian potential energy `U_N(r)=−G_N·mM/r` — linear superposition of
two independently-sourced, leading-order-weak fields...~~ `U_N` is
**imported**, not derived from `S_EH` anywhere in this finding (`S_EH`
itself was never varied to linear order in a metric perturbation here —
that full calculation is not attempted). Only `U_5th` is genuinely
derived from the action. Combining a derived quantity with an imported
one and calling their sum "`G_eff`, derived" would overclaim:

```
U_total(r) = −mM/r·[G_N + ĝ²/(4π)]     [G_N imported, ĝ²/(4π) derived]
⟹ ΔG = ĝ²/(4π)     [only this additive piece is genuinely derived here]
```

## 4. The check against P21's own formula — corrected, largely circular as originally framed

~~P21 (start of the whole `ΔG`-normalization arc) **defined** the relation
`A·g²=4π·ΔG` by dimensional matching... P21's founding relation is
derived here, not merely restated.~~ **[CORRECTED — the consequential
fix.]** Independently re-read `FINDING_P21_shared_phi_normalization_
constraint.md` directly before accepting this correction (not from
memory): P21's own text — already corrected once by its own skeptic
review — explicitly states the normalization constant `A`'s *placement*
is **"a convention, not a forced discovery: the identical physics
results from placing an equivalent factor in the kinetic term instead."**
P21 never claimed a specific numeric value for `A` — only that *some*
factor carrying `G`'s units must exist.

This script **chose** the canonical-kinetic-term convention (`S_φ` with
coefficient exactly `1/2`, no separate `A`) — the *same* convention P21
already flagged as one equally-valid option among several. That choice
makes `A=1` **true by construction**, not by independent physical
content:

```
P21's ΔG (A left general):  A·ĝ²/(4π)
This derivation's ΔG:            ĝ²/(4π)
Difference at A=1:                    0    (script assertion, exact)
```

**What this comparison actually shows:** the **functional form**
`ΔG∝ĝ²/(4π)` — the generic shape of any canonically-normalized
massless-scalar Yukawa exchange — is reproduced by an actual calculation
from the action. **What it does NOT show:** independent numeric
confirmation of P21's specific coefficient, since P21's own text already
states that coefficient is convention-dependent, not a physical
prediction. The original "derived, not merely restated" framing
overclaimed in essentially the same way the P34 skeptic review flagged
the same day (a check whose "independence" partly dissolves once its
shared premises are examined) — caught here on a genuinely different
mechanism (convention-freedom, not shared-action tautology), by
independently reading the comparison target's own text rather than
trusting a summary of it.

## 5. The slip claim — withdrawn, a real physics gap not just framing

~~Dust has zero anisotropic stress; `φ` is a canonical, minimally-coupled
scalar... its own anisotropic-stress contribution at linear order is
second-order-small (`∇φ·∇φ`, with `φ` itself already first-order)...
NO slip (`γ:=Φ/Ψ=1`) at this order.~~ **[WITHDRAWN — the consequential
physics gap, not a framing issue.]** This reasoning conflated two
*different* perturbation expansions. In cosmological perturbation theory,
a genuinely small perturbation `δφ` makes `(∇δφ)²` second-order-small —
correctly. But `φ(r)=ĝM/(4πr)` in *this* static, two-body picture is not
a small cosmological perturbation — it is the **full** field sourced by
`M`, and its own `|∇φ|²` is `O(ĝ²)`, the **exact same parametric order**
as `ΔG` itself. `φ`'s own stress-energy — and hence any contribution it
makes to a metric slip `Φ≠Ψ` — is **uncomputed at the order that would
actually matter**, not "second-order-small." Status: genuinely **open**,
not asserted at any confidence level. A real, correctly-scoped treatment
would require the full self-consistent `O(ĝ²)` calculation (§6 point 8).

## 6. What this does NOT establish

1. The connection between this **static, two-body** `ΔG` and P30's
   **cosmological, perturbation-growth** `G_eff` — related by the
   standard quasi-static/sub-horizon approximation, but that reduction
   is **not performed here**. Until it is, treat the two as linked by
   strong physical plausibility, not by an explicit derivation chain.
2. `γ(a,k)=Φ/Ψ` at any confidence level — §5's original qualitative claim
   was withdrawn as wrong, not merely unproven; the question is open.
3. `μ(a,k)`'s scale (`k`) dependence — the static result here is
   `k`-independent by construction (massless mediator, point-source
   limit), consistent with expectation, but the full `k`-dependent
   quasi-static Poisson equation is not derived.
4. A restored, explicit-`c`, SI-like version matching P21's own original
   unit convention — still deferred (same caveat as P34).
5. Anything about the `κ` (dipole) sector.
6. Any comparison against Table A1 — closed gate, not touched.
7. Per NO_AUTHOR_ERROR: entirely this project's own reconstruction
   (OUR_RECONSTRUCTION), not a claim about TJB's own unpublished theory.
8. **[ADDED after correction] A fully self-consistent `O(ĝ²)` solution.**
   `φ`'s own stress-energy sources gravity (via Einstein's equations) at
   the *same* `O(ĝ²)` order as the claimed `ΔG`. This finding computed
   `U_5th` on a flat background (no metric response to `φ`) and combined
   it with an *unperturbed* `U_N` (also no metric response to `φ`) — a
   linear superposition of two decoupled leading-order pieces, not the
   fully coupled Einstein+scalar+matter solution a genuine `G_eff`
   derivation needs. This gap is neither computed nor bounded here, and
   is the same underlying issue as §5's withdrawn slip claim.

## 7. Skeptic verdict (context-blind, Step 8a, 2026-08-14)

Reviewed with `claim.md`-equivalent content (this finding, pre-correction)
+ the script, **no session history**, per Falsification Ladder Context
Asymmetry Rule, explicitly asked to check the slip-order reasoning and
whether `U_N` is derived or asserted. Six issues found:

| # | Issue | Verdict | Disposition |
|---|---|---|---|
| 1 | "Derives (not merely restates)" oversells the actual algebraic work done | WEAKENED | Retitled, softened throughout |
| 2 | `U_N` asserted not derived; summing derived+asserted and calling it "derived" | **FALSIFIED (strict claim)** | Narrowed to: only the additive `ΔG` is derived; `U_N`/`G_N` explicitly flagged as imported (§3) |
| 3 | Circularity risk vs. P21 — skeptic could not resolve without P21's content | **NEEDS-REAL-DATA → resolved** | Independently re-read `FINDING_P21` directly: confirmed `A`'s value is explicitly convention-dependent per P21's own text — the "A=1 match" is largely circular, not independent confirmation (§4, most consequential fix) |
| 4 | "Second-order-small" slip claim conflates cosmological-perturbation and static-field expansions | **FALSIFIED** | Withdrawn to a genuinely open question (§5) |
| 5 | Signs/dimensions in the field-equation and Green's-function steps | CONFIRMED-REAL | No fix needed |
| 6 | "Attractive for like-sign `ĝ`" is meaningless (`ĝ` enters squared) | **FALSIFIED** | Wording removed (§3) |
| + | Scalar's own metric backreaction at the same `O(ĝ²)` order, uncomputed | WEAKENED | Added as §6 point 8 |

**What survives:** the general (non-homogeneous) field-equation derivation
and the Green's-function point-source solution (§1–§2) are correct,
sympy-verified. `U_5th=−ĝ²mM/(4πr)` is genuinely derived from the action.
**What does not survive:** "`G_eff` is derived," "P21's relation is
derived, not merely restated," and the qualitative slip claim — all three
withdrawn or substantially narrowed. Kill classification: mixed — issues
2/3/6 are framing/scope; issue 4 (and its companion, §6 point 8) is a
real, unresolved physics gap, the most serious correction of the P34–P35
pair.

## Reproduction

```bash
python experiments/20260803-bridge/P35_static_weak_field_closes_deltaG_loop.py
```
