# P23 — MULTING's own model spec confirms `g` couples to total cluster mass, not a dark-matter-only population

**Date:** 2026-08-13
**Origin:** P22 flagged, as an *unverified assumption*, that using
Archidiacono et al.'s dark-matter-only `β` bound as a numeric proxy for
MULTING's monopole coupling `g` requires `g`'s target population to be at
least comparable to a DM-only coupling — and noted only that MULTING's
`g·mᵢ·φ` term "appears to couple to mass generically," without checking
further. This finding checks that directly against the project's own
authoritative model-spec registry, rather than leaving it as a hedge.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Method:** internal citation check only — no external fetch, no new
computation (same precedent as P13a).

**[CORRECTED after skeptic review, same day — §2's central claim was
backwards, a real physics error, not a framing nitpick.]** The original §2
argued a universal coupling faces "strictly more" experimental constraints
than a dark-matter-only one (CMB/BAO *plus* equivalence-principle tests),
concluding P22's ceiling is "loose" and the true bound "very plausibly
tighter." This is **wrong**: equivalence-principle tests specifically probe
*composition-dependence* (does material A fall differently than material
B?). A coupling exactly proportional to inertial mass for every material —
i.e. a truly *universal* coupling, indistinguishable in form from gravity
itself — has **zero** composition dependence and is therefore **not
constrained by EP tests at all**; it is degenerate with a small shift in
`G`, exactly what `two_field_action_closure.py`'s own text already says
("Its m-m exchange renormalises `G`... absorbed"). EP tests add a
constraint only if the coupling varies by *composition* — the opposite of
what §1 argues MULTING's `g` does. §2 is corrected below (not deleted — the
underlying observation that DM-only and universal couplings are *different
quantities* survives; the direction-of-tightening claim does not). §1's
framing is also softened: `MODEL_SPEC_AUDIT.md`'s own §7 explicitly limits
`HOLDS` to an internal-consistency verdict about substituting `M500` as
the *observational plug-in*, not a physics-validation of what the
*microscopic* Lagrangian coupling targets — that gap was not flagged in
the original version. See the Skeptic Verdict section for the full
breakdown.

## 1. The check

`MODEL_SPEC_AUDIT.md` (this project's own adversarially-reviewed symbol
registry, §1, "Force-law primitives — given by MULTING, not touched by this
track") states, verbatim:

```
| Symbol      | Meaning                | Given as | Independent input          | Status |
| m_A, m_P    | monopole (mass) charge | postulate | cluster M500 (MCXC-I/PSZ2) | HOLDS  |
```

`mᵢ` — the coefficient P1's own action couples `g` to (`g·mᵢ·φ`, per
`two_field_action_closure.py`) — is identified with **cluster `M500`**,
sourced from real observational catalogs (MCXC-I X-ray, PSZ2
Sunyaev-Zel'dovich). `M500` is a standard cluster-cosmology mass estimate:
the total mass enclosed within the radius where mean density is 500× the
critical density — **dark matter (the dominant fraction) plus baryonic gas
and galaxies combined**, not a dark-matter-only quantity. `[MEMORY]`,
domain-standard usage of `M500`/MCXC/PSZ2 in cluster cosmology, not
independently re-verified against the catalog papers this session — this is
well-established terminology, not a specific claim requiring external
fetch verification the way Archidiacono's own equations did.

**[Added after skeptic review]** `MODEL_SPEC_AUDIT.md`'s own §7 (point 3)
states, verbatim: *"Rows marked HOLDS are internal-consistency and
derivation-correctness verdicts, not claims that the two-charge completion
IS MULTING's actual physics — that remains untested."* The `m_A, m_P` row's
`HOLDS` therefore licenses only *"substituting `M500` as this project's
observational plug-in for `m` is internally consistent"* — a narrower claim
than *"MULTING's microscopic Lagrangian couples `g` identically to every
baryon and dark-matter particle."* The gap between "macroscopic cluster
mass used as input data" and "microscopic per-particle coupling structure"
is a real, additional inferential step this finding does not independently
close via the table alone — it is closed instead by the direct textual
evidence below (§1b), which the skeptic identified as strictly more direct.

**[Added after skeptic review] §1b — the more direct evidence, from the
action itself.** `two_field_action_closure.py`'s own printed action (line
113) is `S = ∫d⁴x(1/2)(∂φ)² + Σᵢ∫dτ[g·mᵢ+pᵢ·∇]φ(xᵢ)` — `mᵢ` enters as a
single, undifferentiated mass with **no baryon/dark-matter sector
distinction written anywhere** in this project's own reconstruction of the
action. This is the same observation P22 §3 already made ("MULTING's
`g·mᵢ·φ` term couples to a body's mass `mᵢ` generically") — this finding's
actual contribution is confirming there is no *countervailing* evidence
anywhere in the cited files that would restrict `g`'s target population,
not introducing new evidence beyond what P22 already had. The `M500` row
(§1 above) is corroborating, not load-bearing on its own.

## 2. Consequence

This **confirms**, using the project's own authoritative source (status
`HOLDS`, not `OPEN` or `postulate, not sharply defined` — contrast with the
`k_A, k_P` row on the same table, flagged `OPEN`), that MULTING's `g`
couples to the *same* total mass that dominates real cluster observables —
**not** restricted to a dark-matter-only component. P22's target-population
caveat is upgraded from *"unverified either way"* to *"confirmed real"*:
Archidiacono's `β<~0.01` genuinely bounds a different physical coupling
(dark matter only, zero baryon term) than the one MULTING's `g` needs to be
evaluated against (universal, coupling to `M500` as a whole).

**[CORRECTED after skeptic review — the original version of this paragraph
had the physics backwards; struck through below, corrected version
follows.]**

~~This does not make P22's numeric ceiling wrong or unusable — it sharpens
what kind of number it is. Since a genuinely universal coupling is probed by
strictly more experimental channels than a dark-matter-only one (galaxy
cluster CMB/BAO physics plus equivalence-principle/laboratory tests, which a
DM-only coupling entirely evades), the true constraint on MULTING's g is
very plausibly tighter than P22's A·g²≲1.05×10⁻¹⁰ — meaning that number is
best read as a loose, permissive ceiling, not a state-of-the-art
constraint.~~

Equivalence-principle tests specifically probe *composition-dependence* —
do different materials free-fall differently? A coupling `g·mᵢ·φ` that is
exactly proportional to inertial mass, for *every* material equally (a
genuinely universal coupling, which §1/§1b argue is what MULTING's action
has), has **zero** composition-dependence by construction. It is therefore
**not constrained by EP tests at all** — it is observationally degenerate
with a small shift in `G` itself, exactly matching `two_field_action_closure.py`'s
own text: *"Its m-m exchange renormalises `G`... absorbed."* EP tests add a
constraint only for couplings that vary *by composition* (e.g. coupling to
baryon number, not to mass) — the opposite of the "universal, no sector
distinction" reading §1b establishes. Archidiacono's DM-only `β` bound works
specifically *because* their coupling is DM-only, creating a real,
detectable differential between dark matter and baryon evolution — a
channel a genuinely universal coupling does **not** have.

**Consequence, corrected:** the direction of P22's ceiling relative to the
"true" bound is **not established either way** by this finding. It is
plausible that a universal `g`-coupling is essentially *unconstrained* by
fifth-force-type searches (since it hides inside the measured value of
`G`), in which case Archidiacono's number is not a substitute bound at all
— tighter, looser, or simply the wrong kind of quantity to compare. This
finding's real, surviving contribution is narrower than originally
claimed: **Archidiacono's `β` measures a different physical situation than
what MULTING's `g` (per the action's own construction) requires** — not a
claim about which one is numerically tighter.

## 3. What this does NOT establish

1. **A tighter, quantified bound** — nor a looser one. §2's original claim
   that the true bound is "very plausibly tighter" is withdrawn (see
   correction banner and Skeptic Verdict). Whether Archidiacono's `β`,
   properly converted, over- or under-states the real constraint on a
   universal `g` is genuinely unresolved here.
2. **[Added after skeptic review] That EP/laboratory fifth-force tests
   constrain MULTING's `g` at all.** A composition-independent coupling
   exactly proportional to mass is degenerate with `G` and evades EP tests
   by construction — this finding does not identify *any* external bound
   that unambiguously applies to a universal `g` in the way Archidiacono's
   applies to a DM-only one.
3. **Anything about `κ` or `Ω_φ`.** `κ` (the dipole coupling) is coupled to
   `kᵢ`, a *separate* row in `MODEL_SPEC_AUDIT.md` explicitly flagged
   `OPEN` — "postulate, not sharply defined" — a different, already-known
   open problem, untouched by this finding.
4. **That `M500` itself is free of any modeling assumptions.** `M500`
   estimates (X-ray hydrostatic mass, SZ mass-observable scaling relations)
   carry their own systematic uncertainties in the cluster-cosmology
   literature; this finding only established *what* MULTING's `mᵢ` is
   identified with, not the precision of that identification.
5. **[Added after skeptic review] That `MODEL_SPEC_AUDIT.md`'s `HOLDS`
   status validates MULTING's actual microscopic physics.** Per the file's
   own §7, `HOLDS` is an internal-consistency verdict about this project's
   reconstruction, not a physics-validation claim about TJB's theory.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction
   and its own prior model-spec registry, not a claim about any error in
   TJB's own theory.

## Reproduction

No new computation — a citation check against
`experiments/20260803-bridge/MODEL_SPEC_AUDIT.md` §1 (row `m_A, m_P`) and
`two_field_action_closure.py` line 113 (the `g·m_i·φ` coupling term), both
already in the repository.

## Skeptic verdict (context-blind, Step 8a, 2026-08-13)

Given only this file, `MODEL_SPEC_AUDIT.md`, `two_field_action_closure.py`,
and `FINDING_P22_archidiacono_beta_mapping.md` (corrected version) — no
session history. Four sub-verdicts, per Step 8a (not merged):

- **(A)** Citation accuracy + row trustworthiness: **WEAKENED** — the row
  is quoted verbatim correctly, but `MODEL_SPEC_AUDIT.md`'s own §7 limits
  `HOLDS` to an internal-consistency verdict, not physics-validation of
  MULTING's actual theory; the original framing overread it. *Applied:
  §1 corrected with the exact §7 quote; §1b added pointing to the more
  direct evidence (the action's own lack of sector distinction).*
- **(B)** M500 = total mass: **CONFIRMED-REAL at the surface / WEAKENED as
  chained** — the `[MEMORY]`-labeled semantic claim is honestly flagged and
  likely correct, but the further step from "macroscopic cluster mass" to
  "microscopic per-particle coupling structure" was smuggled in unlabeled.
  *Applied: the gap is now stated explicitly in §1; §1b supplies the
  actually load-bearing evidence instead.*
- **(C)** §2's "universal coupling → strictly more constraint channels →
  P22's ceiling is loose" inference: **FALSIFIED** — a genuine physics
  error, not a framing issue. Equivalence-principle tests probe
  *composition-dependence*; a coupling exactly proportional to mass for
  every material (universal, no sector distinction) has zero
  composition-dependence and is **not** constrained by EP tests — it is
  degenerate with `G` itself, exactly per `two_field_action_closure.py`'s
  own "renormalises `G`... absorbed" text, which this finding cited but
  did not apply consistently. Ran a soundness check before accepting (is
  the counter-argument actually correct, not just plausible-sounding?) —
  confirmed: EP tests are specifically designed to catch composition-
  *dependent* violations, so a composition-*independent* coupling evades
  them by construction. *Applied: FIXED, §2 rewritten — direction of the
  bound left genuinely open rather than asserted either way.*
- **(D)** Overall value/necessity: **WEAKENED, approaching FALSIFIED on
  necessity** — the core observation (DM-only vs. universal mismatch) was
  already present in P22 §3 directly from the action; the `M500` detour
  added an unnecessary inferential step and enabled the §2 error. *Applied:
  §1b reframes the action itself as the primary evidence, `M500` as
  corroborating only.*

**Recomposition Gate note (per Step 8a):** the original finding chained
four sub-claims (table row → M500 semantics → universal coupling → tighter
bound) into a stronger combined claim than any individual piece, or their
conjunction, actually licensed — flagged explicitly by the skeptic and
corrected by narrowing the recomposed claim to what survives: MULTING's
`g`, per the action's own construction, plausibly has no target-population
restriction, and Archidiacono's DM-only `β` measures a genuinely different
physical situation — **not** a claim about which bound is numerically
tighter.

**Not a core-predicate-false kill.** The narrow, action-grounded core
observation survives fully; what was withdrawn is the M500-based
"confirmation" framing (softened to corroborating) and the §2 directional
claim (withdrawn entirely, left as an open question).
