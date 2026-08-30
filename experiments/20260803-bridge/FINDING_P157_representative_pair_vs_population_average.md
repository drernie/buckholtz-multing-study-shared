# FINDING P157 — working out, in detail, a reframing `docs/149` already
# stated in one line: why a single-pair kinematic bridge and a population-
# density-sourced Friedmann closure are different mathematical objects
# — and why this project's own `C1` result, despite being the nearest
# available prior work, does NOT mechanistically transfer to v82's own
# scalar force-term structure

**Date:** 2026-08-30
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive/structural
**Verdict (final, post-skeptic):** `QUESTION-DEEPENED-NOT-RESOLVED;
CORE-REFRAME-ALREADY-IN-DOCS149-NOT-A-NEW-FINDING; C1-IS-SAME-GENERAL-
CLASS-BUT-MECHANISTICALLY-DISTINCT-FROM-V82S-OWN-SCALAR-F1-FORM
(ANGULAR-CANCELLATION-VS-SCALAR-NONLINEAR-AVERAGING, NO-TRANSFER-
LICENSED); NO-MECHANISM-APPROPRIATE-ESTIMATE-ATTEMPTED; NO-NEW-
COMPUTATION-ON-V82S-OWN-CONSTRUCTION-PERFORMED`
**Process note:** this file went through three distinct, sequential
corrections in one session — two provenance failures (§1, §2: presenting
already-existing `docs/149` content as new) and one mechanism-transfer
failure (§3: a context-asymmetric skeptic, dispatched deliberately for
this file, found `C1`'s angular-cancellation mechanism does not apply to
`F^(1)`'s scalar-product form). All three are corrected in place below,
not silently. See `lessons_learned.md` for the durable process lesson
this pattern produced.
**Continues:** `FINDING_P156` §3 ("finite-r/anisotropic regime remains
open"). **Provenance correction (2026-08-30, user-caught, twice in this
same file — see also §2's correction below):** this file's original draft
presented §1's core observation as a new reframing. It is not. `docs/149`
§3 (written in the prior session, reading v82 for the first time) already
states, verbatim: "`docs/127`'s own `G_eff=0` result... addresses a
structurally different question (does the pair-kernel correction survive
an `r→∞`/isotropic-population background limit) than TJB's own bridge
(does a *specific pair's* kinematics, integrated, reproduce the observed
`H(z)` curve)." That is the same core claim as this file's §1, stated
first, in the prior session, before `P156` was even written — `P156`
itself failed to build on `docs/149`'s own observation when it wrote its
looser "three axes" framing (limit / ensemble / coupling mechanism)
instead. **This file's actual, narrower contribution**: working out *why*
that structural mismatch holds (the `docs/124`/`docs/125` population-
density-convolution requirement, traced to Shtanov-Sahni's own Eqs.
15-18, and this project's own two independent, already-blocked attempts
to bridge single-pair quantities to that requirement), and quantifying
the stakes via `docs/127`'s `C1` result against v82's own Table III force
shares (§3). Neither of those two additions was in `docs/149` or `P156`.

## 1. Why "finite-r vs. r→∞" undersold the gap `docs/149` had already named

`P156` described the open regime as "finite, anisotropic, single-pair
separations" vs. our closure's `r→∞` isotropic-average limit — true as far
as it goes, but looser than what `docs/149` §3 had already stated (see the
correction above). `docs/124` (the original, `FALSIFIED` attempt to apply
Shtanov-Sahni to `F_oP` directly) supplies the derivation for *why* the
mismatch `docs/149` named is structural, not just semantic: S-S's entire
machinery is a **population-density convolution**,
`∫[ρ(r')-ϱ]φ(a,|r-r'|)d³r'` (their Eqs. 15-18) — it computes an effective
source term for the **second Friedmann equation**,
`ä/a = -(4πG_eff/3)(ρ+3P/c²)`, from a **field of matter/charge density**.
`docs/125` tried to promote this to a matrix-kernel population integral
and got `BLOCKED` — not for a finite-r/anisotropy reason, but because the
second "charge" (`q_i=k_i r_i`) has **no known evolution law / conserved
background** to subtract, per their own Eq. 15-18 requirement.

v82's bridge (Eqs. 5-9, `docs/149`) is not this kind of object at all. It
never builds a density field, never subtracts a background density, never
integrates over a population. It takes **one representative pair's own**
force-sourced acceleration `s̈(z)` and identifies `s̈/s = ä/a` directly
(Eq. 8) — v82's own words: "treating the background expansion as an
**integrated average of discrete node dynamics**" (p.6), but the actual
computation performed is a single deterministic evaluation, not a sum or
integral over discrete nodes.

**So the real open question, as `docs/149` already put it, is not "does
our r→∞ limit generalize to finite r" — it is whether a single
representative pair's own force-law evaluation is a valid proxy for
whatever a genuine population average would give.** This project has
twice tried to build the population-density side of that bridge
(`docs/124`, `docs/125`) and been blocked both times, for reasons
unrelated to v82's own construction — new content this file adds to
`docs/149`'s own already-correct framing.

## 2. v82 already names this gap, unprompted, as unaddressed — `[VERIFIED-PDF p.18]`

**Correction (2026-08-30, user-caught):** this section originally implied
the passage below was newly found, "past where `docs/149` had previously
stopped." That is false — `docs/149` §4 item 4 (written in the prior
session) already quotes this exact passage verbatim and already notes,
in one line, that it is "a genuinely different question from, but
**adjacent to**, this project's own isotropic-*orientation*-population
averaging work in `P154`/`P155`." This file re-read the primary source
directly (PDF p.18) before checking `docs/149` first, duplicating work
that had already been done and mischaracterizing it as new. This file's
own actual contribution is narrower than first stated: not *finding* the
caveat or *first noticing* its relevance to isotropic-averaging work
(both already in `docs/149`), but *working out* the connection in detail
— tracing why `docs/127`'s `C1` (not `P154`/`P155`, a related but
distinct screened-kernel analog) is the closer analogy, quantifying the
stakes via Table III's own force-share numbers (§3 below), and tracing
through `docs/124`/`docs/125`'s two prior, independently-motivated
attempts to bridge single-pair quantities to a population-sourced
background (§1). Below is the passage, quoted again here for this file's
own self-containedness, not as a new find:

> "**Typical objects, not distributions.** Every quantity in Sec. II D is
> a single, representative value at each redshift, not a scattered
> population of node properties. Because the force law is markedly
> nonlinear in these quantities, evaluating it at a representative value
> is not generally the same as averaging it over the distribution; we
> have not attempted to quantify this difference."

This is not this project's inference about v82 — it is v82's own,
explicit, unprompted statement of the exact structural gap identified in
§1, stated as **open and unquantified** by its own author.

## 3. `C1` is thematically related but mechanistically mismatched — corrected after a dispatched skeptic review

**Correction (2026-08-30):** this section originally claimed `docs/127`'s
`C1` result was "the closest existing analogy" and used its collapse-to-
zero shape to argue v82's `F^(1)` term faced comparable "stakes" (up to
"removing one side of the near-cancellation" in Table III). A context-
asymmetric skeptic review (dispatched deliberately for this file, given
its interpretive nature — not the automatic same-session trigger used
earlier for `FINDING_P156`) found this **overstated at the mechanism
level**, not merely in confidence. The finding survives independent
re-examination and is recorded here, not silently fixed:

`C1`'s null result (`+0.085±0.58`, `z=0.15σ`, vs. a coherent `+9.9`)
comes from **angular/orientation cancellation** — an isotropic population
of **vector** dipole moments, `[p−3(p·n̂)n̂]/r³`, integrated over a sphere
of directions `n̂`. v82's own `F^(1)` — quoted in this file's own §1,
`F^(1) = Gβ₁(k_A m_P r_A + k_P m_A r_P)/(2c²s³)` — is a **pure product of
scalar magnitudes with no angular variable anywhere in it**. `C1`'s
cancellation mechanism has nothing to act on here: there is no direction
to isotropically average over in this formula. v82's own Sec. IV.H
caveat, re-read carefully, is not about orientation at all — it is about
**nonlinearity in scalar quantities** ("the force law is markedly
nonlinear in these quantities... not a scattered population of node
properties," no angle mentioned). `C1` and Sec. IV.H's caveat share only
the broad, largely uninformative umbrella "a representative value is not
generally the same as a population average" (true of nearly any nonlinear
statistic) — not a shared mechanism.

**What the mechanically-correct question actually is, left unattempted
here:** for scalars, the relevant tool is Jensen's inequality /
covariance, not angular cancellation, and its sign and magnitude are
*not* generically "collapse toward zero" — for independent scalars,
`E[k·m·r] = E[k]·E[m]·E[r]` **exactly** (zero bias); for correlated
scalars, a shift set by covariance terms whose sign is undetermined
without data. v82's own Eqs. (10)-(14) (§1's table, also `docs/149` §2)
make `r_X(z)` and `k_X(z)` **derived, deterministic functions of `m_X(z)`
alone** (via `R_500`/`ρ_crit` and a mass→temperature→gas-mass→thermal-
energy chain respectively) — not independent scalars at all. This means
the real question is a **single-variable nonlinear-averaging** one
(`⟨f(m)⟩` vs. `f(⟨m⟩)` for the composite power-law `f` these equations
define), not a multi-variable independence/covariance one either. This
file does not attempt that calculation — it requires an actual node-mass
distribution at fixed `z`, which neither this project nor (per Sec.
IV.H's own admission) v82 currently has.

**Corrected statement:** v82's own Sec. IV.H caveat and this project's
`C1` result both instantiate the general pattern "representative value ≠
population average," at a level of generality too broad to transfer any
quantitative or qualitative expectation from one to the other. `C1` is
evidence about a mechanism (angular/vector cancellation) that does not
apply to `F^(1)`'s own scalar-product form. No claim about the sign,
magnitude, or even existence of a population-averaging correction to
`F^(1)` is licensed by anything in this file.

## 4. What this file does NOT establish

1. **Does not claim v82's `H(z)` values would change under a proper
   population treatment.** `C1`'s mechanism was derived for a genuinely
   different force law (a massless test-particle tidal sum over a filled
   ball of point dipoles) than v82's own two-body `F^(1)` (Eq. 3, already
   a scalar, self-projected onto the pair's own separation axis). No
   computation applying `C1`'s method to v82's own force law has been
   performed.
2. **Does not say v82's "representative value" choice is invalid** — that
   is v82's own explicitly-named open question (§2), not a verdict this
   project reaches. `NO_AUTHOR_ERROR`: this project has no standing to
   resolve it, only to note the analogy and its own prior, independently-
   obtained data point.
3. **Does not establish that TJB's calculation literally performs a
   population sum in disguise.** Read literally, Eq. 8 is a single
   deterministic kinematic identification for one pair; whether "the"
   representative pair is *intended* to already encode an ensemble
   average (in which case the C1-style question is about how that
   encoding was done, not whether averaging happened at all) is not
   addressed by v82's own text as read here.
4. **Does not close `docs/150` §6 item 2 or the 2026-08-30 pearl_registry
   row.** Both remain open; this file sharpens what "open" means and
   supplies the closest existing prior-work analogy, not a resolution.
5. **No new sympy/numeric computation in this file.** Every quantitative
   fact cited is either read directly from the v82 PDF or reused,
   unmodified, from `docs/127`'s already-established `C1` result.
