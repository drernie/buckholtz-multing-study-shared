# FINDING — Stage 1+2: the thermal-energy response is **fitted, not
# structural** — and at TJB's own fit its sign is **negative**

> **[AMENDED 2026-09-07 — Step 8a skeptic]** Nine corrections were applied
> to this branch after a context-blind skeptic pass, all independently
> re-verified by tool before acceptance. **Read
> `AMENDMENTS_after_step8a_skeptic.md` before quoting anything below.**
> Load-bearing among them: any sentence of the form *"more thermal energy
> means less local EXPANSION"* is **WITHDRAWN** — the computed quantity is
> the response of ACCELERATION (s^-2), and no statement about `H` (s^-1)
> follows without integrating over history. No claim was killed.

**Date:** 2026-09-07
**Artifact:** `stage1_dHdk_derivability.py`
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR` · L0 `descriptive` (what does the written force law
imply, not whether it is true)
**Status:** Stage-1 result. **Not promoted** — a context-blind Step 8a
skeptic pass has NOT been run on this text and is required before any of
it is quoted outside this folder.

---

## 0. My own Stage-1 hypothesis was FALSIFIED

Before running, I predicted `[INFERRED]`:

> "sign and radial law survive the bottleneck-1 block; only the absolute
> magnitude needs `β_d`."

**Wrong.** All three components inherit the `β` calibration. Recorded
here rather than quietly dropped.

## 1. The derivative

From TJB's own force law as implemented in
`experiments/20260803-bridge/_v82_shared_physics.py`:

```
addot/a = [F0 - F1 + F2 - F_acc] * 2 / (M d)
F0 = -G M²/d²                          (no k)
F1 = -G b1 · 2 M (k/c²)(R/d)/d²        (enters as -F1 ⇒ REPULSIVE)
F2 = -G b2 · (k/c²)²(R²/d²)/d²         (enters as +F2 ⇒ ATTRACTIVE)
```

```
∂(addot/a)/∂k = 4G [ b1·R/(c²d⁴)  −  b2·k R²/(M c⁴ d⁵) ]
                     └─ dipole, + ─┘   └─ quadrupole, − ─┘
```

**Sign is positive iff `Q < 1`, where `Q := (b2/b1)·kR/(M c² d)`.**

## 2. Controls

| control | result |
|---|---|
| **PC1** analytic vs finite difference on the real kernel, 8 redshifts | worst relative error **2.9×10⁻¹⁰** — PASS |
| **NC1** mechanism removed (`b1=b2=0`) | **exactly** `0.0`, analytically and numerically — PASS |
| **SC1** dipole alone (`b2=0`) | `∂/∂k` **positive** — repulsive, as the term is meant to be |
| **SC2** quadrupole alone (`b1=0`) | `∂/∂k` **negative** — attractive, as intended |
| **SC3** is `k` thermal? | `k_of(z) = 1.5·(M_gas/μm_p)·k_BT` — literally `3/2 N k_B T`. **The narrow (thermal) reading is already baked into the kernel.** Stage 2's "assume `k=thermal`" is therefore not an added assumption; it is the code's existing one. |
| **SC4** flip scale | `d_flip = (b2/b1)kR/(Mc²) = 92.67 Mpc` |

## 3. The result at TJB's own published fit

`b1 = 1.4335×10¹⁰`, `b2 = 7.8067×10¹⁷` (Table II spotlighted row, taken
verbatim from `P176` via `P190`), `d₀ = 45 Mpc`:

| z | dipole (+) | quadrupole (−) | total | Q | sign |
|---|---|---|---|---|---|
| 0.000 | +4.646e-91 | −9.569e-91 | **−4.922e-91** | 2.059 | − |
| 0.500 | +1.683e-90 | −3.065e-90 | **−1.382e-90** | 1.821 | − |
| 1.000 | +3.911e-90 | −6.875e-90 | **−2.965e-90** | 1.758 | − |
| 2.330 | +1.592e-89 | −2.811e-89 | **−1.219e-89** | 1.766 | − |

**Negative at every redshift tested** (`Q ∈ [1.75, 2.06]`, all `> 1`).

> **At TJB's own fitted parameters and his own node separation, more
> intracluster thermal energy means LESS local expansion, not more.**
> The attractive quadrupole (`∝ k²`) outruns the repulsive dipole
> (`∝ k`) by roughly a factor two.

This is the opposite of the intuitive reading of the mechanism — the one
Ernest's own phrasing assumes ("thermal energy pushing nodes apart").

## 4. The sign reverses with separation — a distinctive signature

Treating `d` as a free variable, at `z=0`:

| d [Mpc] | Q | sign |
|---|---|---|
| 5 | 18.53 | − |
| 22.5 | 4.12 | − |
| **45 (TJB's d₀)** | **2.06** | **−** |
| 90 | 1.03 | − |
| 180 | 0.51 | **+** |

Crossing at **`d_flip = 92.67 Mpc`**.

`[INFERRED, not tested]` A sign **reversal at a specific separation** is
much harder for an astrophysical confounder to mimic than a monotone
correlation: infall, mass-scaling and merger-state effects all decay
monotonically. **The discriminant may be the SHAPE, not the sign** — this
re-frames Stage 3 and is the most useful thing this stage produced.

## 5. Magnitude — large, and that is a warning

`d ln(addot/a) / d ln k = +28.7` at `z=0`. A 1% change in thermal energy
moves `addot/a` by ~29%. That is the near-cancellation fragility the
project has flagged repeatedly, seen from a new angle: `addot/a` is a
small residue of large opposing terms, so its logarithmic sensitivity to
`k` is enormous. **A prediction resting on this is fragile by
construction.**

## 6. What this does NOT establish

1. **Not that MULTING predicts a negative correlation.** It says the
   force law *as written, at one published parameter row, at one
   separation* does. `β_d`/`β_q` are `Q004`/`BETA-1`-blocked and not
   first-principles values.
2. **Treating `d` as free goes beyond the kernel's own construction.**
   `FINDING_P157` established that v82 evaluates **one representative
   pair**, not a population; §4 extrapolates the formula outside the
   construction it came from. Flagged, not hidden.
3. **Not a claim about Dr. Buckholtz's theory** (`NO_AUTHOR_ERROR`) —
   this is arithmetic on this project's own reconstruction of the
   published force law.
4. **The `REFUSE` of `claim.md` §3 is only PARTLY lifted.** A predicate
   now exists **conditional on a published fit**, not structurally. That
   is weaker than "MULTING predicts X" and must never be quoted as it.
5. **No skeptic pass yet.** Step 8a required before promotion.

## 7. Consequence for the plan

- **Stage 1: answered.** The response is a *fitted* quantity. Route 2 does
  not die — it changes shape: the predicate is conditional on TJB's fit.
- **Stage 2: folded in.** `k=thermal` was already the kernel's own
  assumption (SC3), so there was no separate assumption to add.
- **Stage 3: re-framed.** Do not chase the floor's *sign* first. Ask
  instead whether **any** standard-astrophysics path produces a **sign
  reversal near ~90 Mpc**. If none does, the shape is the discriminant
  and the floor's sign matters much less.
- **Stage 4 unchanged**, and still needs a local-expansion dataset the
  repo does not have.
