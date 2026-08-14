# P39 — the "restore explicit c-factors" task P34 and P35 both deferred is not simple bookkeeping: P21's own `g` and P33's own `ĝ:=g/c` formula are mutually inconsistent, and the resulting gap is not a missing power of `c`

**Date:** 2026-08-14
**Status:** Built, run, ruff clean, all assertions pass.
**Pending context-blind skeptic review (Step 8a) — not yet run.**
**Origin:** sixth step of the covariant-completion campaign
(`PLAN_final_goal_20260814.md`), continuing at the deliberately slower,
one-step-at-a-time pace per explicit user instruction ("продолжай P39,
медленно"). **This finding changed scope mid-investigation, honestly
reported:** the originally-planned step was a direct numeric comparison of
P38's `Φ−Ψ` against `FINDING_P22`/`FINDING_P31`'s phenomenological ceiling
on `ΔG`. Before attempting that, this step checked whether the comparison
is even well-posed — both `FINDING_P34` (§0, §4 point 3) and `FINDING_P35`
(§6 point 4) explicitly flag "a restored, explicit-`c`, SI-like version
matching P21's own convention" as deferred, not-yet-done work. Checking
that first, mechanically, found a real problem — the planned comparison is
currently blocked, and *why* it's blocked is itself the result reported
here.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P39_g_ghat_dimensional_consistency_audit.py`, ruff clean, all
assertions pass.

## 0. Honest scope — what kind of finding this is

This is a **symbol/units provenance audit**, not new physics. It traces
one specific coupling symbol (`g`) through four already-committed
findings' own stated formulas, quoted directly from each source file (not
paraphrased, not from memory), and checks dimensional consistency
mechanically (exponent bookkeeping on `kg, m, s`, via a small script — not
hand algebra, which is exactly the kind of thing this project's own
history shows is error-prone for exactly this class of check). This
directly instantiates `research-methodology.md`'s own still-open "gap #2 —
symbol/parameter registry" (Тип 1 error class: one symbol, two objects in
different parts of the project) — this finding is a concrete case of
running that check, not an abstract proposal to build a checker someday.

**What this does NOT do:** it does not fix the gap it finds, does not
pick which candidate reading of `g`'s units is "correct," and does not
complete the originally-planned P22/P31 numeric comparison — that remains
open, explicitly blocked by what's found here.

## 1. The chain, quoted exactly

- **`FINDING_P21_shared_phi_normalization_constraint.md` §1–2:**
  `S = ∫d⁴x (1/2)(∂φ)² + Σᵢ∫dτ[g·mᵢ+pᵢ·∇]φ(xᵢ)`. *"Taking `g` dimensionless
  (matching `κ`'s convention) as a working assumption... `[φ]_monopole =
  kg⁰ m² s⁻²` (from `g·m·φ = energy`)."*
- **`FINDING_P33_covariantize_mass_varying_classification.md` line 69:**
  `m_eff(φ)/m = (c−g·φ)/c = 1−(g/c)·φ`.
- **`FINDING_P34_frw_background_two_routes.md` §1:** re-uses P33's formula
  *"unchanged"*, defining `ĝ:=g/c` as a single symbol for the rest of the
  campaign (P34 through P38).
- **`FINDING_P35_static_weak_field_closes_deltaG_loop.md` §3:**
  `U_total(r)=−mM/r·[G_N+ĝ²/(4π)]` ⟹ `ΔG=ĝ²/(4π)` — an *additive*
  correction to `G_N`, which requires `[ĝ²]=[G_N]` exactly, not merely
  proportionality.
- **`FINDING_P38...py` Step 7:** `Φ−Ψ=G_N·ĝ²·M²/(16π·r²)`.

## 2. What the mechanical check found

Deriving `[φ]` from P21's own `g·m·φ=energy` requirement, taking `g`
dimensionless as P21 itself states, gives `[φ]=kg⁰m²s⁻²` — exactly
matching P21's own printed result (script assertion, confirms the
re-derivation is faithful before using it further).

Applying **the same `φ`** to P33's own `m_eff/m=1−(g/c)φ` — which P34
explicitly says it reuses *unchanged* — that ratio of two masses must be
dimensionless, so `(g/c)·φ` must be dimensionless. Solving for what `[g]`
this specific requirement demands: `[g]=kg⁰m⁻¹s¹` — **not** dimensionless.
This directly contradicts P21's own stated assumption, using P21's own
formula and P33's own formula together, neither reinterpreted nor
extended beyond what each already states.

**This tension was never checked when P33/P34 (both dated 2026-08-14)
adopted `ĝ:=g/c` — P21 (2026-08-13) is a full day earlier, and neither
P33 nor P34 re-verified `g`'s own assumed units against P21's stated
assumption before building on it.**

Checking `[ĝ²]` against `[G_N]` under **both** candidate readings of `[g]`
(P21's stated dimensionless assumption, and P33's own internally-required
units) — **neither matches**. `FINDING_P35`'s own `ΔG=ĝ²/(4π)`, presented
as literally additive to `G_N`, does not carry `G_N`'s SI units under
either reading.

**The more precise result:** checking whether the residual gap between
`[ĝ²]` and `[G_N]` is itself a pure power of `c` (dimension `(0,1,-1)`,
mass-exponent always zero) — under both readings, the residual carries a
**nonzero mass exponent** (`-1` in both cases). No power of `c`, however
large or fractional, can supply a nonzero mass exponent. **"Restore
explicit `c`-factors"** — P34's and P35's own characterization of the
deferred task — **understates what is actually missing: a genuinely new,
mass-dependent constant, not a pure `c`-power.**

Tracing this into P38's own `Φ−Ψ=G_N·ĝ²·M²/(16π·r²)` (using reading 1,
`g` dimensionless, the more standard of the two): the result carries
dimension `kg¹m⁻¹s⁰` — not dimensionless, as a metric perturbation
combination must be. **Worth flagging, not established:** this residual's
exponents (`kg¹m⁻¹s⁰`, i.e. "kg/m") are the *same* exponents
`FINDING_P17` already flagged for `Ω_φ` ("has units `kg/m`, not
dimensionless... a missing normalization/coupling constant (units `m/kg`)
is silently assumed to be 1"). This is a striking structural echo between
the `κ`-sector's already-known gap and this newly-found `g`-sector gap —
but this finding does **not** claim they are the *same* missing constant;
that would require independently checking `Ω_φ`'s own derivation chain
against this one, not attempted here.

## 3. What this establishes, precisely

The originally-planned next step of this campaign — comparing P38's
`Φ−Ψ` numerically against `FINDING_P22`/`FINDING_P31`'s SI-valued `ΔG`
ceiling — **is currently blocked**, and specifically *why*: not by a
missing power of `c` (as P34's and P35's own "deferred" framing implied),
but by a genuine, previously-unchecked inconsistency between P21's own
stated assumption (`g` dimensionless) and P33's own formula (reused by
P34 onward), which together do not supply `ĝ` with units that make
`ΔG=ĝ²/(4π)` or `Φ−Ψ=G_N·ĝ²M²/(16πr²)` actually dimensionless/`G_N`-valued
under any straightforward reading.

## 4. What this does NOT establish

1. **Which reading of `[g]` is correct**, or whether either is — this
   audit only shows the two already-committed formulas (P21's assumption,
   P33's requirement) don't agree; resolving that requires either
   reopening P21's own working assumption or reopening P33's own
   `m_eff(φ)` construction, neither attempted here.
2. **A numeric value for the missing mass-dependent constant** — only
   that one is required, and that it cannot be absorbed into powers of
   `c` alone.
3. **That this is the same missing constant `FINDING_P17` already flagged
   for `Ω_φ`** — only that the residual units happen to match; not
   independently checked.
4. **That P34–P38's own internal self-consistency (each finding's own
   sympy assertions) is wrong** — those scripts never actually plug in
   P21's real, SI-valued `g`/`β` bound; they use `ĝ` purely as an internal
   symbol, and their own internal algebra (e.g. P38's Step 9 trace-equation
   cross-check) remains valid as *internal* consistency checks. This
   finding only blocks *connecting* that internal chain back to any
   external, SI-valued number (like P22/P31's ceiling) — exactly the
   connection P34/P35 both flagged as deferred and not yet attempted.
5. **Anything about the `κ` (dipole) sector directly** — entirely about
   the monopole (`g`) sector's own chain, though §2's noted structural
   echo with `FINDING_P17` may be worth a future, separate check.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction's
   internal bookkeeping, not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P39_g_ghat_dimensional_consistency_audit.py
```
