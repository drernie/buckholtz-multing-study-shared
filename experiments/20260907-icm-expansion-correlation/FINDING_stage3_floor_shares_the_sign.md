# FINDING — Stage 3: the astrophysical floor has the **same sign** as
# MULTING-at-TJB's-fit, so the monotone test is `CRITERION_INVALID`

> **[AMENDED 2026-09-07 — Step 8a skeptic]** Nine corrections were applied
> to this branch after a context-blind skeptic pass, all independently
> re-verified by tool before acceptance. **Read
> `AMENDMENTS_after_step8a_skeptic.md` before quoting anything below.**
> Load-bearing among them: any sentence of the form *"more thermal energy
> means less local EXPANSION"* is **WITHDRAWN** — the computed quantity is
> the response of ACCELERATION (s^-2), and no statement about `H` (s^-1)
> follows without integrating over history. No claim was killed.

**Date:** 2026-09-07
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR` · L0 `descriptive`
**Evidence level:** `[VERIFIED-arXiv-abstract]` — abstracts and titles read
via the arXiv API. **No full text read.** Do not quote any number below as
`[VERIFIED-REAL]` without opening the papers.

---

## 1. Correction to `claim.md` §5

`claim.md` §5 said the dependent variable is *"neither in hand nor a
catalog column."* **Half of that is now wrong and is corrected here.**

- **In the repo:** still absent. Unchanged.
- **In the literature:** *not* absent. There is an active, decade-long
  line measuring exactly this.

| paper | what it measures |
|---|---|
| Migkas, Pacaud, Schellenberger, Erler, Nguyen-Dang, Reiprich, Ramos-Ceja, Lovisari, arXiv:**2103.13904** | *"Cosmological implications of the anisotropy of ten galaxy cluster scaling relations"* — an apparent **spatial variation of `H₀`** derived from cluster scaling relations |
| Pandya, Migkas, Reiprich et al., arXiv:**2408.00726** | follow-up using **velocity-dispersion** scaling relations; its own abstract quotes the earlier result as *"approximately 9% in the Hubble constant"* |
| He, Migkas, Schaye, Braspenning, Schaller, arXiv:**2504.01745** | FLAMINGO simulations as a null/systematics check; abstract quotes *"an apparent `H₀` anisotropy at 5.4σ that could be attributed to large bulk flows extending beyond 500 Mpc"* |

So Ernest's *"testable against existing X-ray cluster catalogs"* is
**more right than my Stage-0 assessment allowed**. I was measuring the
repo, and reported that as if it were the world. Recorded, not deleted.

## 2. The floor's sign — and it is bad news

The Stage-1 result put MULTING-at-TJB's-fit at **negative**
`∂H_local/∂E_th` for all `d < 92.67 Mpc`. The floor question is whether a
construction with **no MULTING in it** already gives the same.

**It appears to.** Bolejko, Nazer & Wiltshire, arXiv:**1512.07364**,
*"Differential cosmic expansion and the Hubble flow anisotropy"*, abstract
verbatim:

> *"The Universe on scales `10-100 h⁻¹` Mpc is dominated by a cosmic web
> of voids, filaments, sheets and knots of galaxy clusters. These
> structures participate differently in the global expansion of the
> Universe: **from non-expanding clusters to the above average expansion
> rate of voids**."*

Read against our variables: high `E_th` ⇒ cluster/knot ⇒ **not expanding**;
low `E_th` ⇒ void ⇒ **expanding above average**. That is a **negative**
`E_th`–`H_local` correlation produced by ordinary structure formation,
on **exactly the `10–100` Mpc scale** where `d_flip = 92.67 Mpc` sits.

## 3. Verdict on the monotone test

| | sign of `∂H_local/∂E_th` at `d ≲ 90` Mpc |
|---|---|
| MULTING at TJB's own fit (`Stage 1`, `[VERIFIED-run]`) | **negative** |
| Standard structure formation (`[VERIFIED-arXiv-abstract]`) | **negative** |

**Same sign ⇒ `CRITERION_INVALID`** by the Step-4a rule in `claim.md` §4:
a criterion that a mechanism-free construction already passes cannot be
failed by the mechanism.

**The monotone version of Ernest's test is dead.** Measuring a negative
`E_th`–`H_local` correlation would confirm nothing — ΛCDM plus a cosmic
web predicts it already.

## 4. What survives — and what it now needs

Only the **shape** argument from Stage 1 §4: a **sign reversal at a
specific separation** (`d_flip = 92.67 Mpc` at TJB's fit).

But this is **not** established as discriminating, and Bolejko et al. is
precisely why: their void-vs-cluster contrast spans the same `10–100` Mpc
band and could plausibly produce a reversal of its own as the sampled
environment shifts from knots to voids. **`[UNKNOWN]` whether the two
reversals are distinguishable.**

Deciding it needs something this stage did not do: the **predicted
`d_flip` of the standard picture**, computed or measured, against
MULTING's `92.67 Mpc`. If they differ enough to separate — the test lives,
in a much sharper form (*a scale, not a sign*). If they coincide — the
whole direction closes.

## 5. What this does NOT establish

1. **Not that the floor's sign is settled.** One paper's abstract is one
   source. §2 is `[WEAK]` by this project's own confidence rules: <2
   independent sources caps confidence at MEDIUM, and no full text was read.
2. **Not that Migkas et al.'s `H₀` anisotropy is the right outcome
   variable.** It is *directional* (across the sky), not *per-separation*.
   Whether it can be re-cut into `∂H_local/∂E_th(d)` is untested here, and
   its own systematics are actively debated in the papers listed.
3. **Not a refutation of the mechanism.** `CRITERION_INVALID` is a verdict
   on the *criterion*, never on the claim — the same third-outcome rule
   that governs `BLOCKED-INFRASTRUCTURE` and `ORACLE_INADEQUATE`.
4. **Nothing about Dr. Buckholtz's theory** (`NO_AUTHOR_ERROR`).

## 6. Consequence

Stage 4 (dataset hunt) is **not** the next step and would have been wasted
effort — which is what Step 4a exists to prevent. The next question is
narrow and answerable without new data:

> **What separation scale does the standard cosmic-web picture put its own
> cluster-to-void expansion reversal at, and is it distinguishable from
> `92.67 Mpc`?**
