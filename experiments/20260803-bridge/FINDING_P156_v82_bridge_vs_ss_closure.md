# FINDING P156 — v82's kinematic F->H(z) bridge and this project's own
# Shtanov-Sahni background closure: tier structure matches, closure's own
# applicability to v82's construction does not, one agent-drafted claim was
# wrong

**Date:** 2026-08-30
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 math + primary-source reading
**Verdict:** `TIER-STRUCTURE-MATCHES; SS-CLOSURE-APPLICABILITY-TO-V82S-
SINGLE-PAIR-CONSTRUCTION-UNRESOLVED; ONE-LOAD-BEARING-AGENT-CLAIM-WAS-FALSE-
AND-IS-CORRECTED-HERE; FINITE-R-ANISOTROPIC-REGIME-REMAINS-OPEN`
**Origin:** Dr. Buckholtz gave access to his current preprint, v82
(Preprints.org 202608.0943v1, "Multi-Tier Newtonian Gravity..."), and the
user asked for a full decompose -> study -> verify -> recompose pass. This
pearl_registry's own 2026-08-30 entry (retroactive `docs/127` Caveat Gate
backfill) named the exact question: does v82's own bridge reintroduce
q(a)-like dependence the way `docs/127`'s own scope caveat flagged as
possible but untested?

## 0. Provenance of this finding — two independent corrections, both applied

1. `Agent(boyko-agent)` produced a first synthesis, verdict
   `BRIDGES-FORMALLY-DISTINCT-NOT-CONTRADICTORY`, across 4 supporting
   claims. It could not write files (blocked by
   `agent-tool-scope-guard`); its recommendations were handed to this
   session's orchestrator.
2. A context-asymmetric skeptic review (auto-triggered same session, no
   prior context) found 3 of the 4 claims **OVERSTATED**, most seriously
   Claim 2 (`s(z)=d0/(1+z)` "exactly, by linear-ODE uniqueness") — rated
   `GAP`, flagging the premise (that `a(t)` is fixed independently of
   `s(t)`'s own force-sourced dynamics) as unjustified from Eqs (8)-(9)
   alone.
3. This session's orchestrator then read v82 pp.5-6 directly (not the
   markdown conversion, which garbles equations) to resolve the ambiguity
   the skeptic could not close from the equations alone. **Claim 2 is not
   a gap — it is false**, and v82's own text says so explicitly (see §2).

Per `falsification-ladder.md`'s Recomposition Gate: the skeptic already
caught that the *combination* of the 4 claims silently selected the
favorable branch of an explicitly-flagged open question (`docs/127`'s own
"non-uniqueness... NOT settled" caveat). That correction stands and is
carried forward here unchanged. This file adds a second, independent
correction the skeptic itself could not make without the primary source.

## 1. What is directly, tool-verified true

**Tier structure matches** `[VERIFIED-PDF pp.4-5]`. v82's own force law
(Eqs 2-4):

```
F^(0) = -G m_A m_P / s^2                                  (monopole,  n=0)
F^(1) = +G beta1 (k_A m_P r_A + k_P m_A r_P) / (2 c^2 s^3)  (dipole,    n=1)
F^(2) = -G beta2 k_A k_P r_A r_P / (c^4 s^4)                (quadrupole, n=2)
```

is the same tier/radial-exponent assignment `docs/127` uses for MULTING's
own monopole/dipole/quadrupole pair kernel, independently corroborated by
`NR-018`'s Ground-1 indexing (potentials `U ~ s^-1, s^-2, s^-3`).

**S-S closure criterion, applied to v82's own kernels** `[VERIFIED-sympy,
re-run independently by this file's author, not merely trusted from the
agent]`:

```
n=0 (monopole):    lim[f - r f'] = C      (nonzero -- positive control)
n=1 (dipole):       lim[f - r f'] = 0
n=2 (quadrupole):   lim[f - r f'] = 0
negative control (f = C r^2, not in the docs/125 kernel family): diverges
```

`P156_v82_bridge_vs_ss_closure.py` reproduces this and both controls,
runtime <1s.

**Table IIIa, read directly, no extrapolation** `[VERIFIED-PDF p.14]`: at
all four z v82 tabulates (0.070, 0.5, 1.07, 1.965), the monopole share of
the gross force budget is `-0.05%` to `-0.06%` — negligible — while the
k-dependent (dipole+quadrupole) tiers together account for `~96%-99.65%`.
This is the tier our S-S criterion zeroes, at every epoch v82 actually
reports, with no need to convert between separation and redshift via any
disputed relation.

**No asymptotic/large-separation limit anywhere in v82, no citation of
Shtanov-Sahni** `[VERIFIED-GREP, re-run independently: zero hits for
"asymptot|large separation|infinite separation" and for "shtanov|sahni"
in the v82 markdown conversion]`. The two constructions were built
independently — v82 does not build on or cite this project's own S-S
result, and vice versa.

**`docs/127`'s own prior work needs no correction** `[VERIFIED, docs/127
lines 45-65]`. `NR-018`'s note that "Shtanov-Sahni was misapplied, not
refuted" and its citation of `NR-016` are both already reconciled in
`docs/127` itself: `NR-016`'s naive single-kernel mapping was invalid, but
its conclusion was independently re-derived correctly via the proper
matrix-kernel `G_ab` computation. `P152`'s own verdict was already
narrowed to `...-AT-SYMBOLIC-LIMIT-LEVEL` by two skeptic rounds on
2026-08-28 — pre-empting exactly the qualifier this file would otherwise
have needed to add.

## 2. What was claimed and is now corrected: v82 does NOT assert `s(z)=d0/(1+z)`

`Agent(boyko-agent)`'s Claim 2 read v82's Eq. (8)
(`s-double-dot/s = a-double-dot/a`) plus ODE-uniqueness as implying
`s(t) = d0 * a(t)` exactly, and derived a "crossover separation"
(`s* ~ 3-11x c/H0`) from it. **This is not what v82 does**, and v82 says
so explicitly, in its own words `[VERIFIED-PDF p.5]`:

> "We define the scale factor a(z) = (1+z)^-1, the same scale factor
> introduced in standard FLRW cosmology (Sec. IV B); we use a(z) as a
> bridging device to connect this framework's local dynamics to the
> observational, redshift-based quantities discussed there, **not as an
> assumption this framework otherwise relies on**."

And, more decisively, on p.6, in the paragraph immediately following the
integration that produces `H(z)^2 - H0^2` `[VERIFIED-PDF p.6]`:

> "`H_0,anchor` is not an incomplete initial condition for the
> second-order equation governing s(t); it is the single combination,
> `s-dot(0)/s(0)`, that the H(z) trajectory alone depends on. Recovering
> `s(t)` itself requires both `s(0)` and `s-dot(0)` separately."

`s(t)` is governed by its own second-order, force-sourced ODE (Eq. 7: the
two-node reduced-mass equation, sourced by `F_P` and the accretion
correction of Sec. II E) — **not** by `s(t)=d0*a(t)`. `a(z)` is used only
as the standard kinematic mapping between cosmic time `t` and observed
redshift `z` (via Eq. 9, `dz/dt=-(1+z)H(z)`), exactly as v82's own text
says. If `s(t)=d0*a(t)` held exactly, `H(z)` would be trivially the FLRW
kinematic `H(z)` for all `t` — which directly contradicts the paper's own
stated purpose (a force-law-sourced *departure* from FLRW `H(z)`) and its
own stated derivation route (integrate the force-sourced acceleration
equation to get `H(z)^2-H0^2`, not assume the trajectory shape first).

**Consequence:** the specific number `boyko-agent` reported
(`s* ~ 3-11x c/H0`) rests on a false premise and is **dropped, not
carried forward**. The qualitative point it was reaching for — that
realistically-scaled pairs sit far from wherever the monopole would
dominate — survives on its own, more direct footing via §1's Table IIIa
reading (no extrapolation, no disputed relation needed): at every z v82
actually tabulates, the monopole is negligible and the k-dependent tiers
dominate. That is a fact about v82's own reported force budget, not a
derived crossover distance.

## 3. What remains genuinely open (skeptic's correction, not resolved by this file either)

The skeptic's strongest, and still-standing, point: the S-S closure
criterion this project built (`docs/127`, `P152`) is for the **isotropic
population average** of a scalar-radial pair kernel. v82's own dipole
term is **not** that — per v82 Sec. IV.F/IV.H (read in a prior session,
not re-verified again here), the dipole's direction is supplied
externally, "by the line connecting the two nodes," for a **single,
representative pair** — a fixed-orientation, two-body construction, not
an isotropically-averaged population.

Whether the tier-level `G_eff=0` result (which required averaging away
orientation, or taking a radial `r->oo` limit that v82 never takes) says
anything about v82's own finite-separation (`~40-45` Mpc), single-pair,
externally-oriented construction is **not established by this file**.
This is exactly the case `docs/127`'s own scope caveat named as untested
("a genuinely different closure... could reintroduce q-dependence;
non-uniqueness for arbitrary closures is NOT settled") — the caveat this
finding's own trigger (the 2026-08-30 pearl_registry row) was written to
eventually check. It is not checked here; checking it would require a
finite-r, non-averaged, single-pair calculation this project has not
built.

## 4. Verdict and disposition

`TIER-STRUCTURE-MATCHES` — real, `[VERIFIED-PDF]` + `[VERIFIED-sympy]`.

`SS-CLOSURE-APPLICABILITY-TO-V82S-CONSTRUCTION-UNRESOLVED` — the
isotropic-average / finite-r mismatch the skeptic identified is real and
unresolved by this file.

`ONE-LOAD-BEARING-AGENT-CLAIM-WAS-FALSE` — `s(z)=d0/(1+z)` is not v82's
claim; v82's own text explicitly disclaims it. The numeric consequence
(`s*~3-11x c/H0`) is retracted, not merely caveated.

`FINITE-R-ANISOTROPIC-REGIME-REMAINS-OPEN` — the physically relevant
comparison (finite separation, single oriented pair) has not been
attempted by this project. `docs/150` §6 item 2 is **not** closed by this
file; it is sharpened (we now know precisely which calculation would
close it, and that our own closure result does not reach it).

## What this file does NOT establish

1. **Not a claim about Dr. Buckholtz's own theory being right or wrong**
   (`NO_AUTHOR_ERROR`) — entirely about whether this project's own S-S
   closure result says anything about v82's construction. It mostly does
   not, at the level this file checked.
2. **Does not re-derive or validate v82's own fit** — Table IIIa numbers
   are read directly from the printed table, not recomputed; `beta1`,
   `beta2`, `H_0,anchor` are taken as given, not re-fit.
3. **Does not reconcile the two H(z) values** (our own reconstruction's
   `H_MULT` vs. v82's) — out of scope for this file.
4. **Does not settle whether the S-S criterion validly generalizes to a
   single, externally-oriented pair** — named as the concrete next step,
   not attempted here.
5. **The `beta1/beta2` <-> `beta_d/beta_q` unit reconciliation is
   untouched** — separate, still-open item per `docs/150` §6.
