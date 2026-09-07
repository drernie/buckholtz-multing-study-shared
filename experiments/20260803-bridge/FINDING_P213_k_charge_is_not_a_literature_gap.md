# FINDING P213 — the `Δψ` gap is not a literature gap; it is `MODEL_SPEC_AUDIT` §5's
# own single open question, and the two readings differ by a factor 7×10⁸

**Date:** 2026-09-07
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive
**Artifact:** `scripts/p213_k_charge_fork.py`
**Origin:** `/hypothesis-revival` run on the live KG2 gap — *what fixes
`(K/c²)/M` for ordinary laboratory matter?*
**Verdict:** the revival lead is **real but forks**, and it works only
under the reading the project's own audit already disfavours.

---

## 1. What the search actually found

The revival engine looks for *abandoned* hypotheses. It found something
else, and the honest report is that difference: **the quantity MULTING
needs is a special case of a framework the equivalence-principle community
has used and constrained for decades.** The project is not missing a
forgotten idea — it is disconnected from a live one.

**[VERIFIED-REAL]** Bergé, Brax, Métris, Pernot-Borràs, Touboul & Uzan,
*"MICROSCOPE mission: first constraints on the violation of the weak
equivalence principle by a light scalar dilaton"*, PRL **120**, 141101
(2018), arXiv:1712.00483, read in full via arXiv. Their Eqs. (5)–(6):

```
α_ij = α · (q/μ)_i · (q/μ)_j
η    = α · [ (q/μ)_Pt − (q/μ)_Ti ] · (q/μ)_E · (1 + r/λ) e^(−r/λ)
```

with `μ` the atomic mass in atomic units (their own example: *"μ = 47.948
for titanium"*) and `q` a dimensionless "Yukawa charge" of each material.

**This is structurally the same equation `P208` derived for MULTING:**

```
η_E = 2 · η_MULT · |Δψ| / r ,      ψ_i = K_i r_i / (M_i c²)
```

| theirs | ours |
|---|---|
| `α`, coupling strength relative to gravity | `η = κ/g` |
| `Δ(q/μ)`, composition contrast of the test bodies | `Δψ` |
| `(q/μ)_E`, the source body's charge | the source factor |
| `(1+r/λ)e^(−r/λ)`, Yukawa range | our massless limit, `λ→∞` ⇒ 1 |

**One real structural difference, stated rather than smoothed over:**
their `q/μ` is **dimensionless**; our `ψ` is a **length**, because
MULTING's dipole carries a lever arm `r_i` their monopole-coupled scalar
does not have. The mapping is a correspondence, not an identity.

## 2. Why it forks — `MODEL_SPEC_AUDIT` §5

Bergé et al. state that *"taking into account the electromagnetic and
nuclear binding energies, the charge are usually reduced to the material's
baryon and/or lepton numbers (B and L)."*

That is the **broad** reading of `k`. And `MODEL_SPEC_AUDIT.md` §5 — *"Every
unresolved row above terminates at the same place: what is `k`?"* — already
records both readings and their consequences:

| reading of `k` | audit's own consequence | audit's own verdict |
|---|---|---|
| **broad** — kinetic energy of sub-objects generally (binding, rotational, degeneracy) | periastron bound `β_d < 1.2×10⁻⁵`, **five orders below Table A1** | disfavoured |
| **narrow** — thermal kinetic energy specifically | cold neutron stars give `u_NS ≈ 0`, the periastron bound evaporates | *"consistent with the cluster analysis"* |

## 3. The fork, quantified `[VERIFIED-run]`

`scripts/p213_k_charge_fork.py`:

| branch | `\|Δψ\|` | implied bound on `η = κ/g` | does MICROSCOPE bite? |
|---|---|---|---|
| **broad**, `k → B` (`\|Δ(B/μ)\| = 8.94×10⁻⁴`, natural Ti vs Pt) | `~2.7×10⁻⁵ m` | **`η ≲ 9×10⁻⁴`** | **hard** |
| **narrow**, thermal at 300 K (`Δ(E_th/Mc²) ~ 1.3×10⁻¹²`) | `~3.9×10⁻¹⁴ m` | `η ≲ 6×10⁵` | **not at all** |

**The two readings differ in `|Δψ|` by a factor ~6.8×10⁸.**

So the revival lead **works only on the branch the audit already
disfavours**, and on the branch the audit calls consistent it fails
completely — the k-sector escapes MICROSCOPE through exactly the
"`K/M` universality" route `FINDING_P25` named as its own escape, now
quantified rather than merely named.

## 4. The actual conclusion

**`Δψ` was never a literature gap.** `P208`/`P209` framed the remaining
obstacle as "the model does not fix the composition contrast." That is
true but understated: the contrast is not a separate unknown at all — it
is a **direct consequence of `k`'s definition**, and `MODEL_SPEC_AUDIT` §5
had already identified that definition as *the* single load-bearing open
question the entire audit terminates at.

Resolving `k`'s reading does two things at once, which is why it is worth
more than it looked: it fixes `Δψ` **and** it decides whether MICROSCOPE is
a live test or no test at all.

## 5. What this does NOT establish

1. **Not that either reading is correct.** The audit's own periastron
   bound disfavours the broad one; this file adds no new evidence on that.
2. **Not a bound on `η`.** Both rows in §3 are *conditional* on a reading
   that is not settled. Quoting either as "the bound on `η`" would be the
   fit-presented-as-measurement failure Gate 2 exists to catch.
3. **The numbers are order-of-magnitude.** Isotopic masses are entered from
   memory and marked `[MEMORY]` in the script; verify against AME2020
   before quoting a precise figure. The **factor 10⁸ between branches** is
   the robust output, not the last digit of either.
4. **The `r_i` lever arm is unresolved** in the correspondence of §1 —
   their charge is dimensionless, ours is a length.
5. **Nothing about MULTING** (`NO_AUTHOR_ERROR`). `k`'s two readings are
   the project's own audit of the corpus, not a claim about the author.

## 6. Consequence for the open-questions list

`P208`/`P209`'s "blocked model-side, not data-side" verdict **stands and
sharpens**: the model-side blocker is not a vague under-specification but
one named question with two enumerated answers and a factor-10⁸ gap
between them. `MODEL_SPEC_AUDIT` §5 also records that this question was
drafted for the author and **held**:
`P3_k_definition_question_DRAFT_HELD.md`, *"not sent, per the standing
pause."*
