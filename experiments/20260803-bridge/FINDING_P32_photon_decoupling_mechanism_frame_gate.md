# P32 — two independent, cheap arguments against directly identifying Bean & Tangmatitham's Q with MULTING's own worldline coupling

**Date:** 2026-08-13 (corrected 2026-08-14)
**Origin:** direct continuation of `FINDING_P31`'s user-flagged correction,
which identified a deeper caveat than the earlier skeptic review found:
Bean & Tangmatitham's `(Q,R)` framework assumes matter stays minimally
coupled (new physics lives *only* in a modified metric Poisson equation),
while MULTING's own reconstructed action has a *worldline* coupling
(`g·mᵢ·φ`) acting directly on matter's equation of motion — a structurally
different mechanism. This finding checks two cheap, complementary
consequences of that difference.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P32_photon_decoupling_mechanism_frame_gate.py`

**[CORRECTED after skeptic review, same day.]** Four issues fixed, not just
framing. **(1)** §1's original claim — "no other direct matter-`φ` term
exists in the quoted action" — is false: the action's own text also
contains a separate dipole/`k`-charge term (`pᵢ·∇φ`, `pᵢ=κ·kᵢ·rᵢ/c²`), not
proportional to mass. Corrected below: explicitly acknowledged and scoped
— this finding is about the *monopole* sector specifically, the only one
implicated in the `ΔG`/growth-equation story; whether photons carry zero
`k`-charge too is now flagged as an open, unverified assumption, not
silently dropped. **(2)** The massless limit was taken by naively
substituting `m=0` into a term written as an integral over *proper time* —
ill-defined for a photon, since proper time is degenerate along a null
worldline. Corrected below via the rigorous affine-parameter (einbein)
argument, which gives the same conclusion without relying on an
ill-defined limit. **(3)** A cheaper, independent, more decisive argument
was missed entirely: Bean & Tangmatitham's own `φ` is a *metric* potential
with no independent kinetic term; MULTING's own `φ` is a canonical scalar
field with its own kinetic term, an additional matter-sector degree of
freedom. This definitional mismatch requires no assumption about
photon/`k`-charge coupling at all — added below as "Part B." **(4)** §3's
"supports" language overclaimed: with the backreaction channel (§4)
completely unbounded, a zero direct-channel result does not shift the
probability of the lensing question either way. Corrected to "is
consistent with, and a necessary but not sufficient condition for." See
the Skeptic Verdict section for the full 5-sub-verdict breakdown.

## 0. Honest scope, stated before anything else

This is deliberately a **narrower** question than the collaborator's full
proposed gate (deriving `μ(a,k)`, `γ(a,k)=Φ/Ψ`, `Σ(a,k)`, `G_matter(a,k)`
from a full covariant action with an Einstein-Hilbert term added). That
full derivation is real, substantial general-relativistic work this
project has never attempted — no metric perturbation, no Einstein
equations, and no stress-energy tensor for `φ` have been written down
anywhere in this project before now. Rushing that full derivation risks
introducing new errors under the same time pressure that has already
produced several corrected mistakes this session. **[Corrected after
skeptic review]** ~~This finding answers the single most decisive,
narrowly-scoped sub-question first~~ — this finding answers two cheap,
narrowly-scoped sub-questions (Parts A and B below); calling either "the
single most decisive" step overstated what a narrow check can establish,
and Part B turned out to be the cheaper of the two. Explicitly does
**not** claim to close the full mechanism-frame gate — see §4.

## 1. Method — Part A: monopole coupling, rigorous massless limit

`two_field_action_closure.py`'s own action (re-verified this session):

```
S = ∫d⁴x (1/2)(∂φ)² + Σᵢ∫dτ [g·mᵢ + pᵢ·∇]φ(xᵢ),   pᵢ = κ·kᵢ·rᵢ/c²
```

**[Corrected after skeptic review]** ~~the entire direct matter-`φ`
coupling for the monopole sector~~ — the action's own text contains **two**
direct matter-`φ` worldline terms: the monopole `g·mᵢ·φ(xᵢ)` (linear in
rest mass) and the dipole/`k`-charge `pᵢ·∇φ(xᵢ)` (not proportional to
mass at all). This finding is scoped to the **monopole** term only, since
that is the *only* sector implicated in the `ΔG`/growth-equation story
(P21's `A·g²=4π·ΔG`; P30's growth equation) that Bean & Tangmatitham's `Q`
addresses — the dipole/`κ` sector is a genuinely separate mechanism
(P18–P20's own analysis), not at stake in the Bean-`Q`-mapping question.
**Whether photons carry zero `k`-charge too is an open, unverified
assumption — flagged explicitly here, not silently dropped.**

**[Corrected after skeptic review]** ~~Evaluated the massless-particle
limit (mᵢ→0) symbolically~~ — naively substituting `m=0` into a term
written as `∫dτ[...]` is not rigorous: proper time `τ` is degenerate
(`dτ=0` identically) along a null (photon) worldline, so the substitution
is a limit on an object that is not well-defined in that parametrization
in the first place. Corrected: the rigorous route uses an affine parameter
`λ` instead (standard for massless-particle actions, e.g. via an einbein
formulation). For a coupling linear in `m` at fixed particle energy `E`,
`m·dτ → (m²c²/E)·dλ` — this scaling, not the bare coupling, is what must
vanish as `m→0`.

## 2. Result (Part A)

```
scaling term = m²c²/E
lim_{m→0} (m²c²/E) = 0   (at fixed E — sympy-verified, not asserted)
```

**Confirmed via the rigorous route.** Same conclusion as the original naive
substitution, reached without relying on an ill-defined limit. **The
monopole mechanism that produces the growth-equation modification (`ΔG`,
per P30) gives photons zero direct force — conditional on photons carrying
zero `k`-charge (§1's flagged, unverified assumption).**

## 2b. Part B — a cheaper, independent, definitional-mismatch check

**[Added after skeptic review — a genuinely stronger, cheaper argument the
original version missed entirely.]** Bean & Tangmatitham's own `φ` (their
eq. 6, per `FINDING_P31`) is a **metric potential** — part of the perturbed
spacetime geometry itself, paired with a second potential via their own
eq. 7 slip relation `R`, carrying **no independent kinetic term of its
own**. MULTING's own `φ` (`two_field_action_closure.py`) is a **canonical
scalar field** with its own kinetic term `(1/2)(∂φ)²` — an *additional*
matter-sector degree of freedom, not part of the metric. **These are
different kinds of object under the same symbol name.** This mismatch
requires no assumption about photon/`k`-charge coupling at all, and is a
cheaper, independent reason the direct `Q≡A·g²`-type identification (P22,
P31) needs the mechanism-frame caveat already recorded there.

## 3. What this is consistent with (and does not prove)

**[Corrected after skeptic review]** ~~This supports the collaborator's
flagged concern~~ — with §4's backreaction channel completely unbounded,
`0` (direct channel, Part A) `+ unknown` (backreaction) `= unknown`
(total). A zero direct-channel result does not, by itself, shift the
probability of the ultimate lensing question in either direction — calling
it "supporting" evidence overclaimed what a partial derivation licenses.
Corrected statement: Parts A and B are each **consistent with**, and a
**necessary but not sufficient condition for**, MULTING's mechanism
leaving lensing/ISW unaffected while modifying growth — not evidence that
shifts the probability either way. `FINDING_P31`'s status
(phenomenological soft ceiling) is unchanged by this finding.

## 4. What this does NOT establish — the open, larger question

**A genuinely separate, indirect channel is not addressed here.** `φ`
itself carries stress-energy (from its own kinetic term, `(1/2)(∂φ)²`, in
the action). In *any* standard-GR completion of this action — implicit
throughout this project, since no modified Einstein-Hilbert term has ever
been written down here — `φ`'s own stress-energy tensor `T_μν^(φ)` sources
Einstein's equations, exactly like any other field's energy density. This
is a genuinely separate mechanism through which `φ` **could** still perturb
the metric (and hence photons, via standard lensing), regardless of the
direct-coupling result in §2. Whether this backreaction channel produces a
lensing signal **comparable in size** to the direct growth-equation `ΔG`
is not addressed here — resolving it requires deriving Einstein's
equations, the scalar field equation, and the matter equation
*simultaneously* from a full covariant action (the collaborator's original
full P32 spec), not attempted in this narrower first step.

**Other things not established:**
1. **`γ(a,k)=Φ/Ψ`, the gravitational-slip parameter.** Whether the two
   metric potentials remain equal (`γ=1`, standard GR) or diverge under
   `φ`'s backreaction is not derived here.
2. **`Σ(a,k)`, the lensing-relevant combined potential.** Standard
   literature (per `FINDING_P31`'s own corrected §4) combines `Q` and `R`
   (or equivalently `γ`) into `Σ`, the quantity lensing actually measures —
   not derived here.
3. **A quantitative estimate of the backreaction channel's size relative to
   the direct channel.** Only that it exists in principle, as a standard
   consequence of any field's stress-energy sourcing gravity in GR.
4. **A resolution of `FINDING_P31`'s own status.** `FINDING_P31` remains a
   *phenomenological soft ceiling*, not upgraded to a direct bound by this
   finding — Parts A and B are each necessary-but-not-sufficient
   considerations, not evidence that moves the probability toward
   resolving that question in either direction (§3, corrected).
5. **[Added after skeptic review] That photons carry zero `k`-charge.**
   Part A's conclusion is explicitly conditional on this — plausible (the
   `k`-charge appears tied to bound, massive systems in this project's own
   materials) but not verified anywhere in this project.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction of
   P1's action — not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P32_photon_decoupling_mechanism_frame_gate.py
```

## Skeptic verdict (context-blind, Step 8a, 2026-08-13)

Given only this file, the script, `FINDING_P31_growth_rate_bound_on_universal_g.md`
(the finding this directly continues, itself corrected twice), and
`two_field_action_closure.py` (the primary action this finding's central
claim rests on) — no session history. 5 sub-verdicts, per Step 8a (not merged):

- **A** ("no other direct matter-`φ` term exists in the quoted action"):
  **WEAKENED (framing) / one sentence FALSIFIED as literally written.** The
  action's own text does contain a second, dipole/`k`-charge term
  (`pᵢ·∇φ`), independently confirmed by direct re-read of the source file.
  The finding's own §1 prose was correctly scoped ("for the monopole
  sector"), but the script's print statement dropped that qualifier and
  stated the false stronger claim. *Applied: FIXED — §1 rewritten to
  acknowledge the dipole term explicitly and flag photon `k`-charge as an
  open, unverified assumption; script corrected to match.*
- **B** (naive `m→0` substitution into a proper-time integral):
  **WEAKENED.** Proper time is degenerate along a null worldline
  (`dτ=0`), so `.subs(m,0)` on a `∫dτ[...]` term is a limit on an
  ill-defined object, not a rigorous massless-particle limit — the
  physically correct route uses an affine parameter. The *conclusion*
  survives (confirmed independently via the affine-parameter scaling
  argument, `m²c²/E→0`), but the original derivation method was not
  rigorous as presented. *Applied: FIXED — script and finding rewritten
  with the einbein/affine-parameter argument.*
- **C** ("supports... does not fully prove"): **WEAKENED.** With the
  backreaction channel (§4) completely unbounded, `0 (direct) + unknown
  (backreaction) = unknown (total)` — a zero direct-channel result does
  not shift the probability of the lensing question in either direction.
  "Supports" oversold a structural non-answer as partial evidence.
  *Applied: FIXED — corrected to "is consistent with, and a necessary but
  not sufficient condition for."*
- **D** ("the single most decisive, cheaply-derivable first step"):
  **WEAKENED — and a genuinely cheaper, more decisive argument was
  missed.** Bean & Tangmatitham's own `φ` is a metric potential with no
  independent kinetic term (confirmed via `FINDING_P31`'s own eq. 6/eq. 7
  quotes); MULTING's own `φ` is a canonical matter-sector scalar field with
  its own kinetic term — a definitional mismatch checkable by inspection,
  requiring no assumption about photon/`k`-charge coupling at all, cheaper
  than the massless-limit argument. *Applied: FIXED — added as Part B,
  §2b, an independent, complementary result.*
- **E** (sympy "verification" as tautology, same pattern as P29/P30):
  **WEAKENED, but different in kind.** Unlike P29/P30 (where the tautology
  *was* the entire finding), here the trivial substitution packages a real,
  substantive claim about the action's own structure (linearity in `m`) —
  but per sub-verdict A, that reading of the action was itself incomplete.
  The sympy step adds no independent verification value; the real work is
  in correctly reading the source file. *Applied: script's docstring now
  states this plainly — the substantive claim is established by reading
  `two_field_action_closure.py`, not by sympy arithmetic.*

**Not a core-predicate-false kill.** The narrow claim that survives —
photons feel zero *direct* force from MULTING's monopole coupling,
conditional on carrying zero `k`-charge — is correct, now reached via a
rigorous route. What was withdrawn is the overclaimed completeness of the
action-reading (sub-verdict A), the rigor of the original derivation
(sub-verdict B), the logical force of "supports" (sub-verdict C), and the
claim that this was the cheapest available argument (sub-verdict D, which
produced a genuine improvement — Part B). The skeptic's own summary: *"What
survives is exactly this: in MULTING's own reconstructed action, the
monopole worldline term is linear in rest mass, and therefore, IF photons
carry no k-charge and IF the null-worldline limit is taken via the
standard einbein procedure, they feel zero force from that specific term —
the two IFs and the untreated φ-backreaction leave the actual observational
lensing question open, and the direct-channel result should be read as
'consistent with' rather than 'evidence for' MULTING leaving lensing
unmodified."*
