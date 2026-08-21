# FINDING P80 — on-shell attribution: what the split can and cannot say

**Status:** built, run, verdict **A-OK** against pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P80_onshell_attribution.py`

> Three things in this file are corrections to my own reasoning, not to the code.
> All three were within one edit of being written into the repository as findings.

---

## Why this step exists

`FINDING_P77` split `ε` into a background-mediated part and a "direct force"
part by **deleting** the `+ĝρ_Aδφ` term from the matter Euler equation. That
takes the system off-shell: `FINDING_P73`'s first-class algebra breaks, the `0i`
constraint residual reaches `6.8e-2`, and the answer moves from **6.61%** to
**16.39%** depending only on when the probe starts. A factor 2.5 from an
arbitrary protocol choice is not a measurement.

P80 replaces the deletion with a **derivative at the physical point**. Promote
the coupling to two parameters — `ĝ_bg` in the background equations, `ĝ_pert` in
the perturbation sector — and evaluate

```
pert_sector := ĝ · ∂ε/∂ĝ_pert  |_(ĝ_pert = ĝ_bg = ĝ)
background  := ĝ · ∂ε/∂ĝ_bg    |_(ĝ_pert = ĝ_bg = ĝ)
```

A derivative at the on-shell point never leaves the constraint surface; a finite
deletion does. This is thermodynamic integration's trick — integrate `dH/dλ`
along the coupling rather than subtracting two states.

---

## Correction 1 — the name. It is **not** "the direct fifth force"

`∂ε/∂ĝ_pert` was going to be called the direct fifth-force contribution. That is
wrong, and not by a little. `ĝ_pert` moves **four** things simultaneously:

1. the source of `δφ`,
2. the scalar's stress perturbation,
3. the metric response through `δρ_φ`,
4. the Euler force on matter.

The derivative sees their sum. Calling it "the fifth force" assigns the whole
number to item 4. The honest name is **perturbation-sector sensitivity**, and
the columns in the code now say that.

## Correction 2 — Part C's closure is the chain rule, so this is a sensitivity decomposition and never a causal one

The closure test is

```
∂ε(ĝ,ĝ)/∂ĝ  =  ∂ε/∂ĝ_bg  +  ∂ε/∂ĝ_pert
```

which **every** smooth function of two variables satisfies. It therefore tests
the implementation and can never be evidence that the two coordinates name two
physical mechanisms. Off-diagonal points `ĝ_bg ≠ ĝ_pert` need not correspond to
any action at all.

There is a stronger version worth stating, because it may be the actual answer
rather than a caveat: in the action **one** function `M′(φ)` governs both the
sourcing of the scalar and the force back on matter. They are two faces of a
single interaction term. If they cannot be varied independently without changing
the theory, then *X% background versus Y% force* has **no unique physical
answer**, and only the total along the diagonal `ĝ_bg = ĝ_pert` is defined.

---

## Control A2 — retracted as **invalid**, not merely failed

A2 originally read: *at `ĝ_bg = 0` the derivative must vanish, because `ε`
responds to `ĝ_pert` only as `source(h) × force(h) = O(h²)`.*

It returned `1.921e-04`, then `1.924e-04`. I called it a bug twice.

**My first diagnosis was wrong.** I blamed `ĝ_pert` leaking into the observable's
definition — `Δ_m = δρ_A·M + ρ_A·M′·δφ` uses the *physical* coupling, so `ĝ_pert`
has no business there. That fix is correct on its own merits and stays in, but it
moved A2 by `3e-07`, not by `1.9e-04`.

**The control itself asserted false physics.** At `ĝ_bg = 0` the background
scalar is still running (`φ̄̇ ≠ 0`), so

```
δρ_A --h--> δφ --> δρ_φ = φ̄̇·δφ̇ + V′·δφ --> Ψ --> δ_m
```

is **linear** in `h`. A nonzero derivative there is correct.

### Correction 3 — and the reason A2 was wrong is also not what I first wrote

I was about to record *"the pure Euler term is `O(ĝ_pert²)`, so a first
derivative is blind to it."* That holds only if `δφ` is entirely proportional to
`ĝ_pert`. `initial_data` seeds `dph0 = 1e-6`, so `δφ` carries a
`ĝ_pert`-**independent** piece and `ĝ_pert·ρ_A·δφ_HOM` is linear. Measured, not
argued (constraint rebuilt at the actual `φ̄̇`, `k=10`, `h=1e-3`):

| `dph0` | `∂ε/∂ĝ_pert` at `φ̄̇(1)=0` | ratio to `dph0` |
|---|---|---|
| `0` | **`0.000000e+00`** | — |
| `2.5e-07` | `-1.724228e-07` | `-6.896912e-01` |
| `5.0e-07` | `-3.448501e-07` | `-6.897002e-01` |
| `1.0e-06` | `-6.896965e-07` | `-6.896965e-01` |
| `2.0e-06` | `-1.379394e-06` | `-6.896970e-01` |

Exactly proportional to `dph0` (ratio constant to `1.3e-05` across 8× in `dph0`)
and exactly zero at `dph0 = 0`. The residual is the pure Euler force acting on
the initial-condition seed — real physics, not a leak. The same sweep under the
other IC convention (state overridden without rebuilding the constraint) gives
ratio `-7.1148e-01`, constant to `1.6e-04`: same conclusion, different constant.

### The valid control, which passes exactly

Close **both** linear channels at once — background scalar off (`φ̄̇(1)=0`, hence
`φ̄ ≡ 0`, hence `δρ_φ ≡ 0`) **and** no `δφ` seed (`dph0 = 0`, leaving the Euler
term purely `O(ĝ_pert²)`, which a central difference cancels identically):

| configuration | `∂ε/∂ĝ_pert` at `ĝ_bg=0`, `k=10` |
|---|---|
| both channels closed | **`0.000000e+00`** — exact |
| `+ δφ` seed only | `-6.897e-07` |
| `+` background scalar too | `1.9235e-04` (**≈279×**) |

The scalar's own gravity dominates the `ĝ_pert` response by more than two orders
of magnitude.

### What that zero does **not** prove — narrowed after review

A context-blind reviewer pointed out that A2's zero is a **parity identity**, not
a general no-leak certificate: with `φ̄ ≡ 0` and `dph0 = 0` the system is
invariant under `(ĝ_pert, δφ, δφ̇) → (−ĝ_pert, −δφ, −δφ̇)`, so a central
difference vanishes for anything **even** in `ĝ_pert`. Verified — `ε(+h)` and
`ε(−h)` agree **bitwise** at `h = 1e-2, 5e-3, 2.5e-3`. The reviewer is right, and
the earlier wording *"the split has no implementation leak"* was stronger than
this control licenses.

My counter-prediction — that the `O(ĝ_pert²)` response underneath would show up
as a clean `h²` in `ε(h) − ε(0)` — **also failed**: the differences read
`1.04e-08`, `2.76e-11`, `−2.58e-09`, flipping sign, with ratios `378` and
`−0.011` against the predicted `4`. They sit below the solver's floor for a
quantity of size `0.046`. So the quadratic response is not characterised either;
that estimator does not resolve it.

The no-leak claim therefore rests on a **parity-blind** test instead (new control
**A2c**): the observable's *definition* must not depend on `ĝ_pert` at any
parity. Measured — `initial_data` and `contrast` are **bitwise identical** for
`ĝ_pert = 0.0` versus `ĝ_pert = 999.0`. Stated honestly: this is trivially true
of the source as written, since neither function reads `ĝ_pert`; its value is as
a **regression guard** that fires if anyone puts it back.

### The derivative is a property of the model, not of the solver

Central difference, `D(h) = D₀ + Ch² + O(h⁴)`:

| `h` | `∂ε/∂ĝ_pert` |
|---|---|
| `1.0e-02` | `1.923629e-04` |
| `3.0e-03` | `1.923532e-04` |
| `1.0e-03` | `1.923523e-04` |
| `3.0e-04` | `1.923522e-04` |

Successive differences fall `9.7e-09 → 9.0e-10 → 1.0e-10`, i.e. as `h²`
(predicted ratio `11.1` for `h: 1e-2 → 3e-3`, observed `10.8`). Seven significant
figures.

Note that the textbook `h ~ ε_mach^{1/3}` does **not** apply here — that balances
function-evaluation roundoff against truncation, whereas the dominant error is
the ODE solver's own tolerance, many orders above machine epsilon. The optimal
`h` had to be found empirically, which is what the sweep does.

---

## The gap this step does **not** close

`∂ε/∂ĝ_pert` at `ĝ_bg = 0`, `k=10`, against `η = φ̄̇(1)/φ̄̇_ref`, with the
constraint rebuilt at each `φ̄̇` (P80's own numbers, not the scratchpad's —
the override convention gives the same conclusions with slightly different
constants, e.g. `η=−2` reads `-2.511583e-04` there against `-2.470709e-04`
here):

| `η` | `D` | `D/η` | `D(+η)+D(−η)` |
|---|---|---|---|
| `-2.00` | `-2.470709e-04` | `1.235355e-04` | |
| `-1.00` | `-1.938703e-04` | `1.938703e-04` | |
| `-0.50` | `-1.601963e-04` | `3.203927e-04` | |
| `-0.25` | `-1.324305e-04` | `5.297221e-04` | |
| `0.25` | `1.310431e-04` | `5.241724e-04` | `-1.387e-06` |
| `0.50` | `1.587834e-04` | `3.175667e-04` | `-1.413e-06` |
| `1.00` | `1.923523e-04` | `1.923523e-04` | `-1.518e-06` |
| `2.00` | `2.450934e-04` | `1.225467e-04` | `-1.978e-06` |

Three signatures were pre-registered. **Zero** holds — exactly, see A2 above.
**Odd** holds — worst violation `|D(+)+D(−)|/|D(+)| = 1.1%`. **Linear fails**:
`D/η` spreads `4.32×` across the sweep and the power law is `D ~ η^0.299`.

Two explanations were built for the sublinearity and **both failed**:

1. *"the channel is linear in `φ̄̇` at the measurement epoch; the nonlinearity
   lives in the seven-decade map from the initial condition"* — this was an
   **invalid test**, not a negative result. It sampled `φ̄̇` at one instant, and
   by that epoch the field oscillates in `V = λφ⁴/4`: the four samples came back
   `-4.638535e-10`, `+8.062532e-10`, `-8.626693e-10`, `+9.209078e-10`,
   alternating in sign, with 81–179 zero crossings inside the window. A point
   sample measures **phase**; the claim was about **amplitude**.
2. the same claim with a matched estimator — RMS envelope over the growth window
   in `ln a`, including the `V′δφ` half of `δρ_φ` that (1) ignored entirely:

   | `η` | `D` | rms `φ̄̇` | rms drive | sign flips |
   |---|---|---|---|---|
   | `0.25` | `1.311730e-04` | `3.547660e-08` | `2.443870e-07` | 81 |
   | `0.50` | `1.589589e-04` | `5.384786e-08` | `5.800534e-07` | 104 |
   | `1.00` | `1.923523e-04` | `9.681852e-08` | `1.166509e-06` | 135 |
   | `2.00` | `2.437542e-04` | `1.675690e-07` | `2.748855e-06` | 179 |

   Exponents `D ~ (rms φ̄̇)^0.390` and `D ~ (rms drive)^0.257`. Nowhere near 1.

Recorded as an open gap. The oddness says the channel runs through `φ̄̇`, which
A2b already established by a cleaner route; the **amplitude scaling is not
explained by anything tested here**, and it is not being fitted until something
matches.

### The pre-gate that caught (1), stated so it can be reused

Before running any diagnostic, write three lines and check they share a subject:

| | |
|---|---|
| **Claim** | what property of the *model* is asserted? |
| **Estimator** | what formula measures it? |
| **Intervention** | what changes between the compared runs? |

For (1): Claim named the *amplitude over the window*; Estimator returned a
*single-instant value of an oscillating field*; they did not share a subject, so
the test should never have been run.

This is the **seventh** instance in the campaign of one failure mode — *the gate
measures something other than what the claim asserts* — after accumulated ratio
vs rate (P76), reference run vs numerator (P77), precision vs existence (P79),
rounded literal vs value (P78), and the definitional leak plus A2's wrong
physical expectation (P80). It is the first instance inside a diagnostic rather
than a build step.

---

---

## Result — **A-OK**, as a sensitivity decomposition

**A1** — at `ĝ_bg = ĝ_pert` the split system reproduces `FINDING_P76`'s system
**bit-for-bit**: `rel diff = 0.00e+00` at `k = 3, 10, 30`. Compared against P76's
own code, not against numbers copied from a finding — the error P78 made.

**B — the derivative converges.** Central differences at `k=10`:

| `h` | `∂ε/∂ĝ_pert` | change vs previous |
|---|---|---|
| `1e-02` | `0.048595740` | |
| `5e-03` | `0.048595487` | `5.19e-06` |
| `2e-03` | `0.048595417` | `1.45e-06` |
| `1e-03` | `0.048595407` | `2.08e-07` |

**C — the two channels sum to the total**, which is the chain-rule check:

| `k` | pert-sector | background | sum | total | closure |
|---|---|---|---|---|---|
| 3 | `0.042303` | `0.036206` | `0.078508` | `0.078508` | `2.44e-08` |
| 10 | `0.048595` | `0.040843` | `0.089439` | `0.089439` | `8.02e-08` |
| 30 | `0.049647` | `0.042017` | `0.091664` | `0.091664` | `7.74e-08` |

Closure holds eight orders below the 1% threshold. Perturbation-sector share:
**53.88% / 54.33% / 54.16%** at `k = 3 / 10 / 30` — flat across `3…30`, which is
**all** that is measured. `k=1` (where `FINDING_P77` found the coupled contrast
crosses zero ~160 times) and `k ≥ 100` are not in this table.

> ### ~~A consistency check that was not designed in~~ — **STRUCK, it was wrong**
>
> This slot held: *"the total `ĝ·∂ε/∂ĝ = 0.089439` against `ε = 0.045688` gives a
> ratio `1.958`, close to the `2` demanded by `ε ∝ ĝ²`, the shortfall being the
> cubic term P77 measured at 14.8%."*
>
> A context-blind reviewer flagged that this does not reconcile. Re-measured, it
> is **wrong in sign, not merely in size**. Refitting `G−1 = Cĝ²(1+Dĝ)` on P80's
> own runs gives `C = 0.268649`, `D = +0.163252` (16.3%), and if `ε ∝ (G−1)` then
> the ratio would be `(2+3D)/(1+D) = 2.140` — **above** 2, where the measurement
> is `1.958`, **below** it. The cubic pushes the opposite way.
>
> The comparison was ill-founded from the start: `ε = ln(G)/ln(a₂/a₁)` is a
> **logarithm**, and `G−1 = 0.3149` at `ĝ=1` is not small, so `ε ∝ ĝ²` is not
> expected at all and `1.958 ≈ 2` is evidence of nothing. Struck rather than
> rescued.

## D — this does **not** contradict `FINDING_P77`'s 6.61%…16.39%

The temptation is to read `54%` against `7%` as a contradiction. It is not, and
saying so would repeat the campaign's dominant error in a new place. **The two
cut the coupling in different places**, verified by reading the code:

- `FINDING_P77` deleted the Euler exchange term **only**.
- `ĝ_pert` here appears in the perturbed KG **source** (lines 136–137) *and* in
  the Euler term (line 143).

So this coordinate strictly **contains** P77's channel, plus the `δφ` source and
everything downstream of it. The move from `~7%` to `~54%` measures **what P77's
"background" label was carrying that is not background history at all** —
perturbation-sector physics its probe could not separate.

What that does kill: `FINDING_P77`'s conclusion *"this is a modified expansion
history, not a fifth force"* holds only under P77's own cut. Under the
constraint-preserving cut, more than half the sensitivity lives in the
perturbation sector. Neither number is wrong; the **label** on P77's 93% was.

---

## Skeptic verdict (FL Step 8a — context-blind, `claim.md` + code only)

The reviewer **disclosed at the top that it had no Bash**, so every one of its
claims is read-only inference. Per `audit-verification-gate.md`, its `[VERIFIED]`
is my `[INFERRED]`: all three load-bearing points were re-run here before any was
accepted. Verdict returned: **CONFIRMED-REAL**.

| # | Reviewer's point | My independent check | Outcome |
|---|---|---|---|
| A | split assignments complete; only judgement call is `1/(1−ĝφ̄)` inside `drAd` assigned to `ĝ_bg` | read the code; it is a background function used in a perturbation equation, and the docstring already flags split non-uniqueness | **accepted, no change** |
| B | A2's zero is a **parity identity**, catches only odd-in-`ĝ_pert` leaks; "no implementation leak" overclaims | **ran it**: `ε(+h)==ε(−h)` bitwise at 3 step sizes → reviewer correct. My counter-prediction of a clean `h²` underneath **also failed** (below noise floor) | **ACCEPTED — wording narrowed, new control A2c added** |
| C | A1 compares against P76's real code, not a re-implementation | confirmed by reading the `importlib` path | **accepted, no change** |
| D | closure is not trivial — `dp`, `db`, `tot` are three independent `eps_of` calls | confirmed by reading; cache keys distinct | **accepted, no change** |
| E | `ĝ_pert` strictly contains P77's ablated channel | confirmed by reading both files: P77 deletes 1 term, `ĝ_pert=0` removes 3 | **accepted, no change** |
| F | `η^0.30` is measured *off* the on-shell point, so it does not invalidate the derivative *at* `η=1` | agreed; the finding already scopes it as an open gap | **accepted, no change** |
| G | the `1.958`-vs-`14.8%` consistency claim does not reconcile | **ran it**: `D = +0.163` gives a predicted ratio `2.140`, **above** 2, against a measured `1.958` **below** 2 — wrong in **sign** | **ACCEPTED — claim STRUCK** |
| — | "flat in k" rests on 3 points; `k=1` and `k≥100` not reported | agreed | **ACCEPTED — scope note added to code and finding** |

Two of the reviewer's points changed the file's claims (B and G), and one of my
own counter-tests failed in the process. Nothing it raised falsified the core
result.

---

## What is NOT established

- **That the split is unique.** `ĝ_bg / ĝ_pert` is *one* way to cut the coupling.
  A different cut attributes differently, and nothing here privileges this one
  beyond its being on-shell. See Correction 2: a single `M′(φ)` drives both
  sides, so a unique physical split may not exist at all.
- **Which channel carries `FINDING_P79`'s initial-condition dependence.** That
  needs the derivative measured *under the lever*, which is not done here.
- **The `η^0.30` scaling.** Open gap, above.
- **Anything observational.** Internal units; `NO_BRIDGE_FITTING` in force.
- **Anything about MULTING itself** (Gate 1). The completion is ours; a verdict
  on our reconstruction does not transfer to Dr. Buckholtz's model.
- **Perelman condition 5** (external reconstruction) — still not met, as
  throughout this campaign.
