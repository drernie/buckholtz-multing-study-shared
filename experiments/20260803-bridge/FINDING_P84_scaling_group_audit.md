# FINDING P84 — **B-INVARIANT.** The bridge for `ε(k)` costs **one** external number, not three

**Status:** built, run, verdict against pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P84_scaling_group_audit.py`

> The symbolic gate fired **before a single integration** and caught a real hole
> in my derivation. Had the numerical check run first, it would have returned
> "the symmetry is broken" — the right verdict for the wrong reason.

---

## Why this before any mapping

`FINDING_P82` produced `f(a,k)` in **internal** units. But `P76` sets `G_N = 1`,
`C_MATTER = 1`, `a(1)³ = 6π−1`, `φ̄̇(1) = √2/A3_INIT` — every one a **choice**.
Until we know which numbers survive changing that choice, a mapping to `h/Mpc` is
fitting dressed as derivation.

So the first bridge step is not a mapping but an audit: **which combinations are
invariant under the scaling freedom the equations possess, and does `ε` depend
only on those?** The count of invariants *is* the answer to "how many external
numbers does the bridge need" — a falsifiable internal question that touches no
data, so `NO_BRIDGE_FITTING` is not at risk.

---

## The group, and the hole the symbolic gate found

```
S1  COMOVING      a → b·a ,  C → b³·C ,  k → b·k
S2  TIME/DENSITY  t → α·t ,  C → C/α² , λ → λ/α² , k → k/α
S3  FIELD         φ̄ → γ·φ̄ , ĝ → ĝ/γ , C → γ²·C , λ → λ/γ² , G → G/γ²
```

**`G → G/γ²` in S3 was missing from my first draft.** Under the field rescaling
the Friedmann *right* side picks up `γ²` (`ρ_A`, the kinetic term and `V` all
scale that way) while the *left* side `(ȧ/a)²` does not move at all. With
`G → G/γ²` the two sides match and Klein–Gordon then scales uniformly as `γ¹` —
which is exactly the weight sympy had already reported as "invariant" for KG, so
the tool was pointing at the gap.

**The same run produced a second residual that was NOT a physics error.** S2's
first test wrote `a.subs(t, t/α)` and compared an expression built on `a(t/α)`
against one built on `a(t)`. Those are different symbolic functions; their
difference cannot simplify to zero however correct the physics. Fixed by giving
every equation the same argument `u` and putting the time rescaling into the
derivative operator by hand.

**Two residuals that looked identical, with completely different causes — one a
hole in the derivation, one a defect in the test. A numerical run would not have
separated them.**

---

## Results

### Part A — symbolic, all three exact

| transformation | Friedmann | Klein–Gordon |
|---|---|---|
| S1 | invariant | invariant |
| S2 | invariant | invariant |
| S3 (with `G`) | invariant | invariant |

### Part B — numerical: does `ε` actually survive?

Reference `ε` at `k=10, ĝ=1, λ=1, C=1, G=1`: **`0.045627233456`**

| transformation | `ε` | rel change |
|---|---|---|
| S1, `b=2` | `0.045627233456` | `1.168e-13` |
| S1, `b=0.5` | `0.045627233456` | `2.240e-13` |
| S2, `α=3` | `0.045627234648` | `2.611e-08` |
| S2, `α=0.25` | `0.045627232147` | `2.869e-08` |
| S3, `γ=2` | `0.045627233456` | `1.349e-12` |
| S3, `γ=0.5` | `0.045627233456` | `2.304e-12` |

S2's residual is five orders larger than S1's and S3's, and that is expected
rather than worrying: S2 rescales the **integration span**, so the solver takes a
genuinely different path and the agreement is solver-level, not exact.

### Part C — negative control: the test must be able to fail

| transformation | `ε` | rel change | |
|---|---|---|---|
| `λ → 2λ` | `0.045428038850` | `4.366e-03` | changed ✓ |
| `λ → 10λ` | `0.044697223905` | `2.038e-02` | changed ✓ |
| `λ → 0.1λ` | `0.045811485652` | `4.038e-03` | changed ✓ |

Without this, Part B would prove nothing — the trap `FINDING_P77`'s
non-discriminating pole test fell into.

### Part D — **which invariant does `k` enter through?**

`k/(a·H)` at `t₀`, across every transformation: **`5.43511093944054`**, rel
change `0.000e+00` in all six. Bare `k` moves by `1.000e+00` (S1) and
`6.667e-01` (S2).

**Scope of that `0.000e+00`, stated because it looks stronger than it is.**
`k/(aH)` here is computed **algebraically from the parameters**, not from an
integration — so Part D verifies that my transformation functions are consistent
with the invariant's formula. That is *exact arithmetic*, weaker than Part B's
*dynamical* statement. The two together are what establish the claim; Part D
alone would not.

**And Part D does not show `k/(aH)` is the ONLY invariant `k` enters through.**
Others exist — `k²/(a²V'')` with `V'' = 3λφ̄²` is dimensionless and invariant
too. What is established is that `k/(aH)` *is* invariant and bare `k` is not.

---

## Verdict — **B-INVARIANT**

Of the eight internal quantities `(a, C, G, ĝ, λ, φ̄, k, t)`, **three are pure
convention**, and `P76` spent exactly three: `G_N=1`, `C_MATTER=1`, and the
choice of `a(1)`. The group's dimension and the conventions spent match.

### What this means for the bridge — and it corrects my own first answer

I was about to record that the bridge needs **three** external numbers. That is
true of mapping *every* internal quantity, and it is **not** the question we have.

`ε` and `f` are invariant under the **whole** group. They carry **no unit
convention at all** — they are already physical numbers and need nothing
external. Only `k` does.

> **The bridge for `ε(k)` needs exactly ONE external number: the physical value
> of `a·H` at one reference epoch.**

Quoting three would have **overstated the cost of the bridge by a factor of
three**, by conflating "map everything" with "map the observable we actually
have".

### This also narrows the `NO_BRIDGE_FITTING` concern I raised earlier

`a·H` at a reference epoch is a **standard cosmological quantity**, not something
extracted from Table A1 or from correspondence. Using it is a **unit conversion**,
not a fit. So the constraint does not block this step.

**What it does not settle**, and this is now the sharp version of the worry:
*which epoch of our internal history corresponds to an observed `z`.* That is not
fixed by an external `H₀`; it needs a mapping of internal time to cosmological
time, and **that** is where `Q005` can genuinely bite. The bridge splits into two
questions of very different difficulty:

| | cost |
|---|---|
| `ε(k)` → observed `k` | **one** external number |
| `ε(k, z)` → observed `k` and `z` | open; needs the time mapping |

---

## What is NOT established

- **`k` in `h/Mpc`.** This step cannot produce it — only the *count* of external
  numbers and what each one fixes.
- **That the symmetry holds away from the points tested.** Evidence at those
  points; the negative control is what stops it being vacuous, not a proof.
- **That `k/(aH)` is the unique `k`-invariant.** See above.
- **Anything about whether the completion is right.**
- **Anything observational.** No dataset and no Table A1 quantity enters this
  file.
- **Perelman condition 5** — still not met.
