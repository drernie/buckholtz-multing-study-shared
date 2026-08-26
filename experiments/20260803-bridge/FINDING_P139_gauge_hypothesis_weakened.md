# FINDING P139 — the gauge-artifact hypothesis (M3) is WEAKENED by tracing,
# not refuted by a completed symbolic proof; 4th mechanism candidate exhausted

**Date:** 2026-08-24
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Verdict:** `M3-WEAKENED-BY-REASONING` (no `.py` script — this is a code-
tracing and derivation exercise, not a numerical experiment; matches
`FINDING_P138`'s own precedent that not every P-step produces a script)
**Origin:** direct follow-up to macro-locality's own `PART-OF-MACROSYSTEM`
verdict (this session), testing its `SURVIVING_HYPOTHESIS` (M3: gauge
artifact in the implicitly-chosen conformal-Newtonian/longitudinal gauge)

---

## 1. Why this file, and what changed the plan mid-stream

Macro-locality (this session) found `FINDING_P49`'s own caveat — "`Φ, Ψ`
are gauge-dependent quantities... implicitly used throughout" — as an
unexamined premise across `P38`-`P79`, and proposed a differentiating
prediction: a gauge-invariant reformulation of the completion-
discrimination test should show reduced/different IC-sensitivity at low
`k` if M3 is correct. The plan was to build a symbolic gauge-
transformation check (`claim-decomposer`'s own output flagged this as
`C3`: gauge artifacts near horizon crossing are real, general physics —
confirmed via `WebSearch`, textbook material — but `C4`/`C5`, whether
*this specific system* is affected, were named `[SPECULATIVE]`, untested).

**What actually happened when the derivation was attempted, traced
carefully rather than assumed:**

## 2. Three independent lines of evidence, each weakening M3

**Line 1 — `qm`'s exact definition, traced to `P73`'s own code, not
guessed.** An initial attempt to write the standard `δq_matter =
δq_tot − δq_phi` decomposition from memory got a sign wrong (predicted
`qm0 = -(Ψ̇+HΨ)/(4πG) − φ̄̇·δφ`; the actual code has `+`). Traced to
`P73_solve_Psi_k.py` directly: `dq_tot = -φ̄̇·δφ + Q_m` (line 111),
`C0i: Ψ̇+HΨ+4πG·δq_tot=0` (line 135) — confirming `qm` (code) `≡ Q_m`,
the matter sector's own momentum perturbation, with `δφ`'s own
contribution carrying a `−φ̄̇·δφ` sign in the total. Once traced
correctly, `contrast()`'s own `delta = δρ_m − 3H·Q_m` is structurally
the standard **comoving-gauge matter density contrast** `Δ_m = δρ_m −
3H·δq_m` — a combination well-known (and, per `FINDING_P49`, already
citing the *same* Amendola/Ma&Bertschinger coupled-quintessence
literature this project's own conventions match) to be invariant under
time-slicing gauge transformations, as a purely kinematic fact about how
any `(0,0)`/`(0,i)` stress-energy components transform under a
coordinate shift — independent of whether that component is separately
conserved (it is not, here — `FINDING_P55` established real energy/
momentum exchange with `φ`).

**Line 2 — Newtonian/longitudinal gauge is a *complete* gauge fixing.**
Unlike synchronous gauge (which famously retains a residual freedom —
historically the source of the "synchronous gauge mode" problem), the
Newtonian gauge condition (`B=E=0` in the metric) uses up *both* scalar
gauge degrees of freedom. There is, generically, no residual `ξ⁰(t)`
time-shift that preserves this gauge's own form — meaning the entire
premise of "a hidden residual gauge freedom in Newtonian gauge is
leaking into the observable" does not straightforwardly apply the way it
would for synchronous gauge (where such freedom genuinely exists and is
well documented as a source of spurious modes).

**Line 3 — `Φ=Ψ` is this project's own established *physical* result,
not a free gauge choice.** Checked directly in the code: the ODE state
vector carries a *single* variable `psi` for both `Φ` and `Ψ` — because
`FINDING_P49` independently proved `Φ_k=Ψ_k` (zero anisotropic stress)
as a genuine physical consequence of this system's own matter content,
not a gauge convention. Under a generic time-shift `ξ⁰`, `Ψ→Ψ+H·ξ⁰` and
`Φ→Φ−ξ̇⁰` transform *differently* — so requiring `Φ=Ψ` to be preserved
under a would-be residual gauge transformation forces `ξ⁰` into a very
narrow, specific family (`H·ξ⁰=−ξ̇⁰`), not a generic freedom. This
independently confirms Line 2's conclusion from a different angle: most
of the gauge freedom this hypothesis needed is already physically
spoken-for by an established result, not sitting unexamined.

## 3. Verdict

**`M3-WEAKENED-BY-REASONING`.** Not a completed symbolic kill-test (a
full from-scratch derivation of this specific `M(φ)`-coupled system's
own gauge-transformation formulas, independent of any external citation,
was judged too high-risk to complete safely within this session — real
risk of a sign/convention error of exactly the kind Line 1 already
caught once, compounding into a false verdict either direction). But
three *independently* derived lines of evidence — each grounded in this
project's own code/prior findings, not assumption — converge on the same
conclusion: this system's residual gauge freedom is much more
constrained than the informal M3 hypothesis assumed, and the observable
already structurally resembles a standard gauge-invariant-type
combination.

**Combined with the session's prior three attempts** (`FINDING_P135`
pole-at-anchor, REFUTED; `FINDING_P136` early-transient amplitude,
REFUTED; `FINDING_P138` horizon-crossing anchoring, DESIGN-LIMITED — not
testable for `k≥2` within the numerical domain) — **the natural space of
ad-hoc single-mechanism candidates for bottleneck 2's own IC-sensitivity
is now exhausted for this session.** A 5th candidate exists
(`Track B`'s harvest-agent flagged `P82`'s "common envelope `A(η)`"
route, explicitly hedged there as speculative and not independently
verified even by the agent that surfaced it) but was not pursued here,
per the user's own explicit decision to close this round honestly rather
than chase a fifth candidate the very report naming it called
speculative.

## 4. What this does NOT establish

1. **That M3 is formally refuted.** No completed symbolic proof exists —
   only convergent reasoning from three independent, code-traced angles.
   A careful, properly-sourced derivation (ideally cross-checked against
   an actual GR-perturbation-theory reference text, not memory) remains
   a legitimate future step if this bottleneck is ever reopened.
2. **That no gauge-related effect exists anywhere in this system.** Only
   that the *specific* mechanism macro-locality proposed (a residual
   time-slicing freedom leaking into `contrast()`) looks structurally
   unlikely given how tightly this gauge is already fixed.
3. **The P82-envelope candidate's own viability** — flagged by `Track B`,
   not evaluated here.
4. **A replacement observable, or the true mechanism.** Bottleneck 2
   remains `GENUINELY OPEN` — this file narrows the *excluded* space
   further, it does not close the bottleneck.
5. **Anything observational.** Internal units; `NO_BRIDGE_FITTING` in
   force.
6. **Anything about MULTING itself** (Gate 1). Both completions are
   ours.
