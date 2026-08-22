# FINDING P103 — **STEP2-UNAVAILABLE-PROVEN.** The first Step-2 attempt in the whole arc, and it's a proof, not a search

**Status:** built, run (design corrected mid-build before trusting a
result), verdict against pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P103_step2_absolute_scale_derivability.py`

> Nine straight attempts (`P93`–`P102`) all did the same kind of thing:
> pick an external anchor, search `Λ_internal` against it, ask whether a
> match exists. The **Gamow Bridge Test** (named `2026-08-22`) named this
> failure mode explicitly — that's Step 2 answered as "which `Λ` matches
> externally", never "what *is* `Λ`, derived from the model's own
> physics." This file is the first attempt at the second question, on
> user direction: **"attack Step 2 directly next."**

---

## The argument, and two corrections made before trusting it

**The claim:** `Λ_internal` (`lam_cc` in code) enters the completion's
equations of motion in exactly one place — additively, inside the total
energy density that sources `H` — and nowhere else. No equation of
motion, stability condition, or boundary condition anywhere in the
completion (`P58`–`P92`, extended by `P86`) depends on it in any other
way. This is the same structural freedom behind the real cosmological
constant problem: an additive vacuum-energy term coupled to gravity isn't
fixed by any consistency condition unless something *outside* minimal
coupling removes the freedom.

**Correction 1 — the code-level check itself was wrong at first.** A
naive grep for `lam_cc` in `P81.background_rhs`/`viability` found 5
occurrences and a crude "is it near a `V`?" string check said `False` —
because it counted the two `def` signature lines and one pass-through
call (`background_rhs(g_hat, lam, lam_cc)`) as if they were separate
equations. They aren't — a parameter declaration and a forwarding call
don't add a new place `Λ` is *used*, they just carry it to the one place
that does. Fixed by classifying each occurrence (signature / forwarding /
formula) before judging: **2 signature, 1 forwarding, 2 formula — and
both formula occurrences write the identical `V = lam*phibar^4/4 +
lam_cc` expression.** Caught and fixed before the verdict was written,
not after.

**Correction 2 — the planned numerical range was never actually
reachable.** The first design assumed `P81.viability()` could resolve
`Λ` across ~33 decades on the positive side and a comparable range on
the negative side. Individually probing values before trusting a full
scan found: positive-side `Λ` is only actually **measurable** up to
`~1e-13` (an arithmetic `rho_phys<=0` rejection at `1e-12`, then
`unresolved: integrator gave up` for essentially everything from `~1e-11`
up through `1e8` — fast to determine, ~1–3s per point, just not
measurable); and on the negative side, **every** value tried (`-1e-6`
through `-5.0`) made the integrator take **over 150 seconds with no sign
of finishing**, for reasons diagnosed as infrastructure (removing rather
than adding Hubble friction likely forces the default explicit RK45
method to grind toward `T_END=1e8`), not physics. Both corrections are
documented in the file's own docstring rather than silently fixed and
re-run as if the plan had been right all along.

## Results

**Step 1 — code-level, corrected classification:**

| kind | count |
|---|---|
| signature | 2 |
| forwarding | 1 |
| formula | 2 |

Both formula occurrences: `V = lam * pb**4 / 4.0 + lam_cc`, identical.

**Control** — `lam_cc=0.0` reproduces `P81`/`P86`'s own published
`min_M = 0.871740335` exactly. Passed before trusting anything wider.

**Step 2 — positive-side scan, 35 points, `1e-25` to `1e8`:**

| | count |
|---|---|
| measured | 15/35 |
| unresolved (BLOCKED-INFRASTRUCTURE) | 20/35 |

Measurable range: `[0, 1e-12]` — almost exactly `FINDING_P86`'s own
`~13`-decade window, not the `~33`-decade one first assumed. Within it,
`min_M` is flat to `1.28×10⁻¹¹` absolute spread (`0.871740335` throughout).

**Step 3 — negative side:** not run in the scan at all. Attempted
separately during the build; abandoned as BLOCKED-INFRASTRUCTURE after
every probed value exceeded 150s with no sign of finishing.

---

## Verdict — **STEP2-UNAVAILABLE-PROVEN**

On the strength of the **structural argument**, not the numerical scan:
`Λ_internal` enters this completion's equations in exactly one place,
additively, inside the one combined expression that sources `H`. That
fact is true regardless of what any solver can numerically reach — read
directly off the equations, the same register as `FINDING_P95`'s
`Ω_φ≥0` algebraic proof, not a claim that depends on scan coverage. The
numerical scan is bounded supporting evidence only, and it is exactly
consistent with — no stronger than — what `P86` already found.

**Step 2 of the Gamow Bridge Test is analytically unanswerable from this
completion's current construction.** A genuine answer requires
*extending* the completion (`Λ(φ)` instead of a bare constant, a
symmetry, a UV-completion argument) — not further analysis of what
`P58`–`P92` already contain. The nine anchor/search attempts (`P93`–
`P102`) were never going to succeed at *deriving* this number; at best
they could *measure* it against external data — a different, still-open
question this file does not resolve either.

### Not established

- That **no** extension of the completion could supply Step 2 — only
  that the current one (`P58`–`P92` + `P86`) cannot, proven not searched.
- What the correct extension would be, or whether MULTING itself already
  has one (Gate 1 — this file says nothing about the source theory).
- Any numeric value of `ε(k)` or `f(k)` in physical units.
- Anything about the negative-side boundary — BLOCKED-INFRASTRUCTURE, not
  run.
- That a different solver/method/tolerance couldn't measure further in
  either direction — only that `P81`'s current one, unchanged, cannot.
  Not fixed here.
