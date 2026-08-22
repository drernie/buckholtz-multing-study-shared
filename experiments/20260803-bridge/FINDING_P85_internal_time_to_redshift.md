# FINDING P85 — **Z-CONDITIONAL.** The `t → z` mapping is free; what is missing is dark energy

**Status:** built, run, verdict against pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P85_internal_time_to_redshift.py`

> **This corrects a claim I made twice in this campaign.** I named `Q005` — the
> missing bridge information from the author — as the likely blocker for the
> time mapping. It is not the blocker, and no answer from anyone would change
> what is.

---

## The question `FINDING_P84` left sharp

P84 showed `ε` and `f` carry no unit convention and the bridge for `ε(k)` costs
**one** external number. It named what that did not settle: which epoch of our
internal history corresponds to an observed `z`.

**The first thing to see is that this is not a units problem.** Redshift is a
*ratio* of scale factors, `1 + z = a_ref/a`, so it is automatically invariant
under P84's `S1` (`a → b·a`). No scaling freedom stands in the way.

---

## The control that failed first — and it was the control's fault

**C3** asked whether `1+z` is `S1`-invariant. The first version scaled `a₀` by 7
and **left `C` alone** — but `S1` is `a → b·a` **together with** `C → b³·C`.
With `C` fixed, `ρ_A = C/a³` drops 343× at the start: a *different universe*, not
a relabelled one. It reported `5.279e-03` and that number was honest about what
it actually measured.

Applying the whole of `S1`:

| | `1+z` between mid-span and end |
|---|---|
| `a₀` as usual | `463.446741921283` |
| **full `S1`**, `b = 7` | `463.446741921283` |
| relative difference | **`4.441e-16`** |

Machine precision. **C3 passes.**

This is the same class of error as `P84`'s S2 symbolic test and `P83`'s bracket
endpoint: *a transformation called a symmetry while not being one.*

## The other two controls

**C1 — the uncoupled background must be EdS**, an analytic target external to the
project. `H/H_EdS` runs `1.000000027937 → 1.000000000087 → 1.000000000000` while
`Ω_φ` falls `5.6e-08 → 5.3e-18`. **Exact.**

**C2 — the `w_eff` detector must be able to say *not* matter.** Handed a
background with a cosmological constant it reports `−3e-07 → −0.0617 → −0.99993`.
Without this, "our background is EdS" would carry no information — a detector
that answers "matter" for everything is not a detector.

---

## Result

### The mapping costs **nothing extra**

`1 + z = a_ref/a`. Choosing which epoch is `a_ref` is one number — and P84's
"physical `a·H` at a reference epoch" is the **same** choice, not a second one.
**The `z`-mapping adds no external input beyond what P84 already counted.**

### What the background actually is

| `a` | `w_eff` (`ĝ=1, λ=1`) | `Ω_φ` | `H/H_EdS` |
|---|---|---|---|
| 12.18 | `−0.123109524` | `1.231e-01` | `0.997060885` |
| 74.64 | `+0.005312425` | `5.474e-03` | `1.005399351` |
| 444.3 | `+0.000132282` | `2.495e-04` | `1.000764546` |
| 2658 | `+0.000444861` | `4.661e-04` | `1.000125249` |
| 15924 | `+0.000002056` | `6.412e-06` | `1.000022670` |
| 571611 | **`+0.000001124`** | `1.045e-06` | `1.000000627` |

`w_eff → +1.1e-06`: **matter**, to a part in a million — far tighter than the 2 %
threshold pre-registered. `Ω_φ` at `1e-06`. And **no dark-energy term exists
anywhere in the action this campaign built.**

### Verdict — **Z-CONDITIONAL**

The mapping is free and well-defined. What is not free is the **meaning** of the
epoch chosen: an Einstein-de Sitter universe has no accelerating phase, so **no
epoch in our trajectory is "today"** in the sense an observation means. `z` may
be quoted **only** with the scope attached — *matter-dominated, no dark energy* —
which limits any comparison to redshifts where EdS is itself acceptable.

### The correction: `Q005` is **not** the blocker

I flagged `Q005` twice as the likely obstacle. The obstacle is that **the
completion as built contains no dark energy.** That is a statement about the
**model**, not about missing information from the author. No answer from anyone
would change it — which makes it a cheaper problem to state and a harder one to
solve than I had it.

---

## The coupling's imprint on `H`, and an unplanned cross-check

`H/H_EdS` with the coupling on is the closest **internal** analogue of the
`H_MULT/H_FLRW` ratio this campaign has circled since the start — computed
against an *analytic* EdS reference, nothing fitted:

| `a` | `ĝ=0, λ=1` | `ĝ=1, λ=1` | difference |
|---|---|---|---|
| **12.18** | `1.004374157` | `0.997060885` | **`−7.313e-03`** |
| 74.64 | `1.001313642` | `1.005399351` | `+4.086e-03` |
| 444.3 | `1.000481233` | `1.000764546` | `+2.833e-04` |
| 2658 | `1.000067671` | `1.000125249` | `+5.758e-05` |
| 15924 | `1.000010904` | `1.000022670` | `+1.177e-05` |
| 571611 | `1.000000308` | `1.000000627` | `+3.184e-07` |

The difference is **largest, and negative, at `a = 12.18`**, then flips sign and
decays by four orders.

**The cross-check nobody designed:** the diamond scan located
`min(1−ĝφ̄)` for `(ĝ,λ)=(1,1)` at `t = 1.00e+01`, **`a = 12.18`** — the *same*
epoch. Both are the **first oscillation peak of `φ̄`**, and one mechanism
produces both: `ρ_phys = ρ_A(1−ĝφ̄)`, so maximal `φ̄` simultaneously minimises `M`
and maximally suppresses `H`.

**So the epoch that sets the viability boundary is the same epoch that carries
the coupling's largest imprint on the expansion.** Diamond D2 said the constraint
lives in an epoch the observable has forgotten; P85 adds that the *signal* lives
there too.

---

## What is NOT established

- **Whether EdS is adequate at any particular redshift.** That is a judgement
  about observational tolerance and is not measured here.
- **Anything about MULTING itself** (Gate 1). Our completion lacking dark energy
  says nothing about the source model.
- **Any comparison to data.** `NO_BRIDGE_FITTING` untouched — the EdS reference
  is analytic.
- **That adding a dark-energy term would be legitimate.** It would be a *new
  completion*, and would have to re-enter at P81's viability gate.
- **Perelman condition 5** — still not met.
