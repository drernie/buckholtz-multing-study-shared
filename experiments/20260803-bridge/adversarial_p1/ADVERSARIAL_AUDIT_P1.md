# Adversarial Counterfactual Audit — the two-charge completion of MULTING

**Date:** 2026-08-10 (continuation) · **Labels:** NOT_VALIDATION · NOT_REFUTATION ·
OUR_RECONSTRUCTION · L0 descriptive · **Target:** `two_charge_completion.py` +
`FINDING_two_charge_completion.md` (2026-08-10), cross-referenced against
`field_equation_vs_superposition.py` + `FINDING_field_equation_solved.md`,
`FINDING_R7_collapses_to_one_action.md`, `FINDING_lq2_test_outcome.md`,
`FINDING_dipole_shell_is_a_double_layer.md`, `main.tex`, `pearl_registry/INDEX.md`.

**Mandate.** The job of this document is not to show the two-charge completion
works. It is to find the minimal counterfactual change of premises,
normalisations, orientations, distributions, or boundary conditions under
which the claimed conclusions stop following — and to say plainly, per-item,
whether that was found.

---

## §0. Hard rule, applied

An identity SymPy returns is not proof by itself; a numeric control matching
is not proof by itself; coefficients "looking nice" (2, 6, √6/2) is not proof
by itself. Every claim below that survives does so because an **independent**
code path (§3) or an **independent** data regression (§8) reproduced it, not
because the original file's own control functions returned `True`. Where a
claim rests only on the original file's own internal checks, that is stated
explicitly and the claim is graded down accordingly.

---

## §1. The exact hypothesis, decomposed

**H (as stated by the target material):** *There exists a two-charge
completion of MULTING in which the second charge `k` is an independent
dynamical degree of freedom, and the weak-field limit reproduces MULTING's
three tiers with coefficients `β_d = 2` and `β_q = √6`, including signs,
scaling, and the `r_A r_P` structure.*

| # | Sub-claim | Rating after this audit | Basis |
|---|---|---|---|
| A | The algebraic identity `β_d=2, β_q=√6` follows from summing two physical dipoles over a `1/r` kernel and Taylor-expanding | **ESTABLISHED** | §3 — independently reproduced, fresh code path |
| B | The alternating sign rule is a derived theorem, not a postulate | **STRONG** | §6 — the sign-forcing argument does not presuppose the binomial form |
| C | Orientation is uniquely fixed by requiring MULTING's `F_d` to be A↔B-symmetric | **MODERATE, refined** | §5 — symmetry alone is *not* sufficient (a second symmetric family exists with `A3=0`); symmetry **and** nonzero dipole moment together are |
| D | The construction is a genuine field-theoretic completion: local, ghost-free, one massless-scalar propagator, second charge via derivative coupling | **SPECULATIVE** | §4 — no Lagrangian, propagator, or EOM appears anywhere in the material; this is narrative framing around a point-charge electrostatics calculation |
| E | `β_q/β_d = √6/2 = 1.2247` is a parameter-free, falsifiable numeric prediction | **STRONG, but see F** | §3 — survives uniform-convention rescaling exactly |
| F | ...independent of the lever-arm normalisation convention (`d = r_A`) | **WEAKENED** | §3 Test 2 — invariant under a *shared* rescaling, **not** invariant if the two bodies get independently-chosen normalisations; this is an assumption, not a derivation |
| G | This construction clears the 10.8σ mass-scaling obstruction that killed the single-field completion | **BREAKS as stated; survives in a weaker form** | §7+§8 — see Kill Analysis §19. The functional *form* is reproduced; the *exponent* is not predicted, it is inherited from `u_i`'s own empirical definition |
| H | No single-scalar-field completion can reproduce MULTING's mass scaling, only the minimal (R7) member was shown to fail | **STRENGTHENED beyond the original claim** | §7 — new result: the `+1` mass-scaling is forced for the *entire* single-field class, not just the minimal member |
| I | `k` is identifiable as a real second charge from current or near-future cluster data | **BREAKS** | §8 — blocked by amplitude (10⁵–10¹³×), not by measurement precision |
| J | The construction is attractive at every separation (`ℓ_q² ≥ ℓ_d²/4`) | **ESTABLISHED, conditionally** | reproduced in §3 Test 1 exactly as the original found (0.375 ≥ 0.25); inherits convention caveat from F |
| K | `β_q/β_d=1.2247` is testable against the two rival numbers (2.8284, 4.0) with current data | **BREAKS** | §8, §13 — the amplitude gap and the (already-established, same-thread) death of the pairwise-`K₄` route jointly close this |
| L | This is a covariant, cosmologically well-posed theory | **UNKNOWN — precondition missing** | §11 — no action exists to check; the question cannot be asked of this material yet |

---

## §2. Grounding (Gate 1, before any attack)

Located directly, by `git status`/`ls`, not assumed:

`two_charge_completion.py`, `FINDING_two_charge_completion.md`,
`field_equation_vs_superposition.py`, `FINDING_field_equation_solved.md` — all
present, uncommitted, dated 2026-08-10. `main.tex` — present, modified,
uncommitted (diff read; unrelated to this thread — Eq.32 look-elsewhere and
Table A1 provenance flags, not the two-charge completion). `MODEL_SPEC_AUDIT.md`
— **confirmed absent at the time of this check** (`git ls-files` + `git status`
both empty); it appeared later the same day, after §4a–§19a were written, as a
symbol/claim registry for the whole bridge track — noted here rather than
silently updating the earlier claim, per this audit's own no-silent-correction
discipline. Also located, same directory, same day, causally upstream/downstream
of the target: `FINDING_R7_collapses_to_one_action.md` (2026-08-03),
`FINDING_lq2_test_outcome.md`, `FINDING_dipole_shell_is_a_double_layer.md`
(**dated after** the target — see §13, this changes the decisive-experiment
section materially). Two adjacent-but-out-of-scope threads
(`20260810-eq32-look-elsewhere/`, `20260810-zenodo-archive/`) were located and
their file lists noted, but not read in full — they concern Eq.32 trials
factors and Table A1 β-degeneracy, not the two-charge completion, and pulling
them in would violate the task's own scope (§14 of the original brief: attack
*this* hypothesis, not every hypothesis in the repository).

No rewriting of existing files occurred. All new work lives in `adversarial_p1/`.

---

## §3. Counterfactual — field/convention rescaling invariance

**Method:** independent 3D point-charge Coulomb sum (`counterfactual_checks.py`,
Test 1), built without reference to the original `interaction()` function, to
rule out a hidden assumption baked into the original's own control functions
surviving unexamined.

**Test 1 — reproduction.** `A2=m_Am_B`, `A3=-2d_Am_Bq_A-2d_Bm_Aq_B`,
`A4=6d_Ad_Bq_Aq_B`. Positive control (zeroth order = `m_Am_B/r`) passes exactly.
Substituting `q=-κk/c²`, `d=r`: `ℓ_d==2(u_A+u_P)` → **True**;
`ℓ_q²==6u_Au_P` → **True**. Sub-claim A: **CONFIRMED independently.**

**Test 2 — convention invariance.**
- *Uniform* rescaling `d_A,d_B → γ·r_A,γ·r_B` (same `γ` for both bodies): the
  ratio `ℓ_q²/ℓ_d²` is algebraically **identical** to the `γ=1` result,
  `3k_Ak_Bm_Am_Br_Ar_B / (2(k_Am_Br_A+k_Bm_Ar_B)²)` — confirmed by direct
  symbolic difference `= 0`. **β_q/β_d = √6/2 survives this counterfactual.**
- *Non-uniform* rescaling `d_A→γ_A r_A, d_B→γ_B r_B` (`γ_A≠γ_B`): for identical
  bodies, `ℓ_q²/ℓ_d² = 3γ_Aγ_B / (2(γ_A+γ_B)²)`, which equals `3/8` **only**
  when `γ_A=γ_B`. For any `γ_A≠γ_B` the ratio moves away from `3/8` (verified:
  symbolic difference `≠ 0`).

**Verdict on F:** the `β_q/β_d=1.2247` prediction is **not** convention-free
in full generality. It survives exactly one class of reparametrisation — a
*universal* law relating lever arm to body radius, the same constant for every
object in the theory. That is a physically reasonable assumption (one theory,
one law), but it is an **assumption**, not something the derivation shows.
The original file's own "what this does NOT establish" §4 already flagged
`d=r_A` as "its convention, not a derivation" — this counterfactual makes
precise *how much* rides on that convention: not the qualitative form, but the
specific number 1.2247 is contingent on treating both bodies identically.

---

## §4a. Addendum (post-hoc, after new material appeared mid-audit) — the missing action was written, elsewhere, the same day

While this audit was in progress, three further files appeared in the same
directory, same day, uncommitted: `FINDING_P1_two_field_closure.md`
(+`two_field_action_closure.py`), `FINDING_P2_charge_identifiability.md`
(+`P2_charge_identifiability_chexmate.py`), and a held draft
`P3_k_definition_question_DRAFT_HELD.md`. Per this audit's own Gate 1
discipline, these were not accepted on their own say-so — the two
load-bearing numeric claims were independently re-derived, below and in §8a.

**P1's claim:** an explicit action exists,
`S = ∫d⁴x[½(∂φ)²] + Σᵢ∫dτ[gmᵢ + pᵢ·∇]φ(xᵢ)`, `pᵢ=κkᵢrᵢ/c²` — linear kinetic
term (trivially no ghost, no tachyon), `k` entering only through a derivative
coupling exactly as `two_charge_completion.py`'s point-charge picture assumed
but never derived. Further: `β_q/β_d=√6/2` is **not** an artefact of the
lever-arm convention this audit's own §3 found it sensitive to — it is fixed
by a single, kernel-level fact, `Λ(r)≡K'''K'/K''²=3/2`, true for **any**
massless exchange kernel and **any** rescaling of the dipole moment, and
equal to `3/2` only when the mediator is massless.

**Independently re-derived here** (fresh sympy, not reusing
`two_field_action_closure.py`): for `K=1/s`, `Λ=3/2` exactly. For a Yukawa
kernel `K=e^{-μs}/s`, `Λ = 3/2 − (3/4)μ²s² + O(μ³)` — **matches P1's series to
the term written**. **Sub-claim D upgraded from SPECULATIVE to STRONG:** a
real, ghost-free, derivative-coupled action exists, and the numeric content of
`β_q/β_d` is now precisely located (mediator masslessness), which also fully
subsumes and generalizes this audit's own §3 convention-invariance finding —
§3 found the ratio survives *lever-arm* rescaling; P1 shows it survives *any*
rescaling of the dipole moment and *any* kernel choice, with masslessness as
the one condition that matters.

**§11 is correspondingly no longer purely UNKNOWN.** Ghost/tachyon status is
now answered (healthy, linear kinetic term). But P1 also computes the
cosmological consequence directly, and it is not favorable to the broader
MULTING+ program: on an isotropic background, the radial-dipole configuration
is the double layer this audit's grounding phase already read about
(`FINDING_dipole_shell_is_a_double_layer.md`, zero force off-shell) and a
randomly-oriented average is zero by symmetry either way — **so this
completion contributes only a `G`-renormalisation to cosmological background
expansion, and structurally cannot be the source of MULTING's claimed `H(z)`
eras.** This is scoped precisely: `FINDING_two_charge_completion.md` never
claimed to explain MULTING's cosmology, only its weak-field two-body force
law — so this is not a refutation of that file's actual claims, but it does
close off, independently of the Table A1/AI-fit provenance issue (Gate 2,
prior findings), a *hope* this audit's own §18 synthesis had left open (that a
successful two-charge completion might eventually bridge to the cosmological
claim). Two structurally independent routes — Table A1 provenance and this
completion's own cosmological limit — now both say MULTING-as-currently-
evidenced is q-blind on the background.

---

## §4. General alternative action — and a structural gap this surfaced (superseded in part by §4a)

The task asked for the most general alternative action,
`K(ψ)(∂ψ)² + V(ψ) + J_m(ψ)ρ`, as a counterfactual against the specific
construction chosen. That comparison cannot be run here for a reason that is
itself the finding: **`two_charge_completion.py` contains no action, no
propagator, no equation of motion.** It is a sum of Coulomb (`1/r`) terms
between static point charges, Taylor-expanded in the lever arm. The file's own
prose — "one massless scalar with an ordinary `1/r` propagator," "the second
charge enters through a DERIVATIVE coupling," "local and ghost-free" — asserts
field-theoretic properties that are never derived anywhere in the material.

This is not necessarily wrong: a sum of Coulomb potentials between point
charges *is* the classical solution of an ordinary massless-scalar field
sourced by delta functions, so the "local, ordinary propagator" framing is a
reasonable classical-electrostatics analogy. But **"derivative coupling"
specifically is not demonstrated** — nothing in the file distinguishes a
derivative coupling of `k` from an ordinary non-derivative coupling, because
no Lagrangian was ever written down for `k` to couple to. Sub-claim D is
downgraded to **SPECULATIVE**: plausible narrative, unverified content. This
also makes §11 (cosmological/stability audit) impossible to run — see there.

---

## §5. Orientation sweep — extended to 5 configurations (original tested 3, all collinear)

**Method:** `counterfactual_checks.py` Test 3, using fully 3D placement
(azimuthal + polar angles), not the original's z-axis-only helper.

| Configuration | `A3` (dipole term) | `A4` | A↔B symmetric? |
|---|---|---|---|
| radial-radial, inward (original's "mirror-symmetric") | `-2d_Am_Bq_A-2d_Bm_Aq_B` | `6d_Ad_Bq_Aq_B` | **Yes** |
| radial-radial, same direction (original's "parallel") | `-2d_Am_Bq_A+2d_Bm_Aq_B` | `-6d_Ad_Bq_Aq_B` | No |
| **transverse-transverse, parallel** | **`0`** | `3d_Ad_Bq_Aq_B` | **Yes** |
| transverse-transverse, perpendicular | `0` | `0` | Yes (trivially) |
| mixed: A radial, B transverse | `-2d_Am_Bq_A` | `0` | No |

**Counterfactual found and recorded (per §19 protocol, before any patching):**
the original claim — "orientation is not a free choice... fixed by [A↔B
symmetry]" — is **incomplete as stated**. A↔B symmetry alone does not
uniquely select the radial/mirror-symmetric configuration: the
transverse-parallel configuration is *also* A↔B-symmetric, with `A3=0` and a
different quadrupole coefficient (3, not 6). Symmetry is **necessary but not
sufficient**. What actually fixes the configuration is symmetry **conjoined
with** the independent requirement that MULTING's `F_d` be nonzero (MULTING's
preprint asserts a nonzero dipole term exists) — only the radial/mirror
configuration has both properties simultaneously among the five tested.

**Consequence for sub-claim C:** downgraded from "uniquely fixed" to
"uniquely fixed given two conditions, only one of which (symmetry) the
original file stated." The practical conclusion (radial/induced polarisation)
**survives**; the stated justification did not, until repaired here.

---

## §6. Independent sign derivation

Task: derive the sign of `q` without presupposing `(m-κk)_A(m-κk)_P`.
Re-reading the actual order of operations in `two_charge_completion.py`
(not the prose, the code): the mirror-symmetric orientation is selected
*first*, purely from the A↔B-symmetry requirement (§5, independent of any
charge sign). *Then*, within that orientation, `A₃ = -2(d_Am_Bq_A+d_Bm_Aq_B)`
is evaluated for **positive** `q` and found to add to attraction — the wrong
sign, since MULTING needs the dipole term repulsive. Forcing repulsion forces
`q<0`. Only *afterward* does the file note this matches `(m-κk)`. This is a
genuinely independent derivation chain — the binomial form is confirmed, not
assumed. **Sub-claim B holds up.**

---

## §7. Generalized one-field no-go — a new, stronger result than the original material has

`FINDING_lq2_test_outcome.md` §1 already generalized the *minimal* R7 action
to a family `f(Φ)=1+f₁Φ+f₂Φ²+...` and showed `ℓ_q²=2ℓ_d²-f₂/2` — i.e. the
minimal member's ratio is one free choice among many, not forced.

This audit ran the companion question that material never asked: **does the
mass-scaling exponent `+1` survive across that same family, or was it also
just a property of the minimal member?**

Independent symbolic check (fresh derivation, not reused from any FINDING
file): for the general single-field class, the canonical field is always
exactly `χ=M/r` for a point source (this follows purely from `∇²χ=0` sourced
by `ρ`, for **any** choice of `f(Φ)`, since canonicalisation always linearises
the field equation — this step never depends on which `f` was chosen).
Writing the coupling `Φ(χ)=χ+c₂χ²+c₃χ³+...` (`c_n` fixed by `f_n`) and
substituting `χ=M/r`:

```
A2 = M            A3 = c2 M^2            A4 = c3 M^3
ell_d/M   = c2   (a pure constant, independent of M, for ANY c2)
ell_q^2/M^2 = c3 (likewise)
```

**Result: `d ln(ℓ_d)/d ln(M) = 1` exactly, for every member of the entire
single-scalar-field-sourced-by-ρ class, not only the minimal one.** This
closes a loophole the existing material left open ("maybe a fancier one-field
action fixes the mass-scaling") — it structurally cannot, because the source
of the mass-dependence (`χ=M/r`) is forced by linearity regardless of the
nonlinear coupling chosen on top of it. **Sub-claim H is strengthened beyond
what either prior finding established.** This is the strongest argument in
the whole corpus *for* needing something beyond a single field — stronger
than either finding that motivated building the two-charge completion in the
first place.

---

## §8. Real-data identifiability of `k` — independently re-run, not cited

**Method:** fresh load of `data/clusters_clean.csv` (1740 rows, independent of
any FINDING file's own numbers), `identifiability_check.py`.

**Mass-scaling exponent, independently re-derived:** my own log-log regression
of `u=k·r/m` on `M500c_Msun` over the same `n=548` filter (`Ethermal_c2_Msun`
not null) gives **`d ln(u)/d ln(M) = 0.555`**, bootstrap 68% CI
**`[0.514, 0.596]`**, `std=0.041` — matching the FINDING file's cited
`+0.555±0.041` to three decimals. This is now **[VERIFIED-REAL]** by this
audit, not merely [MEMORY]-cited. Decomposition: `k∝M^1.269`, `r∝M^0.287`
(cross-checks to `1.269-1+0.287=0.556`).

**Population-wide amplitude check** (not just the median, as the original
finding used): even at the single most extreme cluster in the n=548 sample
(`u_max=8.92e-6`) and the closest pair separation used anywhere in this
project's own kSZ fits (25 Mpc), with the unknown coupling `κ` set to 1 (i.e.
*not* further suppressed): `ℓ_d/D ~ 1.4×10⁻⁶`, `ℓ_q²/D² ~ 8×10⁻¹³`. (`ℓ_d`
corrected 2026-08-10 post-commit code review: `identifiability_check.py` had
specialized `ℓ_d=2(u_A+u_B)` to identical bodies as `2u` instead of `4u` — a
factor-of-2 slip, caught against this same audit's own independent symbolic
derivation in §3. Non-load-bearing: the order-of-magnitude conclusion is
unaffected by a factor of 2.) The "physically inert" finding is **not a
median artifact** — the tail doesn't save it.

**Noise vs. amplitude.** A Monte Carlo propagating a [WEAK]-sourced,
order-of-magnitude typical `Y_SZ`-scaling scatter (18% in `k`, 5% in `r`, not
literature-verified this pass) perturbs the population-median `u` by **1.8%**.
The amplitude gap is **5–7 orders of magnitude**. A full hierarchical/
error-in-variables Bayesian model (not built — `emcee`/`pymc` both absent from
this environment, confirmed by import error) would sharpen the noise estimate
by a factor of a few. It cannot close a `10⁵–10¹³`× gap. **Sub-claim I: BREAKS**
— not for lack of data quality, but because the predicted effect is
astronomically below any conceivable current detection floor.

---

## §8a. A second, independent cluster pipeline — found, built on, and independently re-verified

§8 answered "is the two-charge *force* observable?" — no, by 5–13 orders of
magnitude, and that answer is unaffected by anything below. A **different**
question was still open: is `k`, *as currently defined* (pipeline thermal
energy `Ethermal_c2 = (3/2)(M_gas/μm_p)k_BT`), even a quantity that carries
real information beyond `M` — prior to asking whether its associated force
is detectable at all. `FINDING_P2_charge_identifiability.md` (new material,
found mid-audit, §4a) attempts exactly this, using `data/chexmate_combined.csv`
(independent galaxy-velocity-dispersion mass estimator, `Ti_from_sigma`) and
`data/chexmate_real_TX.csv` (independent X-ray spectroscopic temperature) —
genuinely different instruments from the pipeline's SZ-derived `k`.

**Every number in P2 was independently re-derived** (`verify_P2_independently.py`,
fresh code, not reusing P2's own `resid()` helper or matching loop):

| Check | P2's number | Independently re-derived | Match |
|---|---|---|---|
| Circularity trap: `chexmate_real_TX.csv`'s `M500_Msun` vs its own `TX_keV` | slope ≈1.55 (self-similar 1.5), "avoid `M_cx`" | slope=1.553±0.189, r=0.864 | **CONFIRMS** the trap; `M_cx` correctly excluded |
| Step 1: `R²(ln k~ln M+ln(1+z))`, `α` at fixed z | `R²=0.6538`, `α=1.020` (n=548) | `R²=0.6538`, `α=1.0203` | **exact** |
| Step 2: internal CHEX-MATE noise floor | `0.109 dex` per-estimator (n=23) | `0.1088 dex` | **exact** |
| Step 3: cross-match residual correlation | `ρ=+0.361` (n=25, `<3'` match) | `ρ=+0.3611` | **exact**, independent matching code |

**One check beyond what P2 itself ran:** a bootstrap CI on `ρ` (P2 quoted
only an analytic null SE). Result: 68% CI `[+0.187,+0.531]`, 95% CI
`[−0.015,+0.674]`, only 3.0% of 5000 resamples give `ρ≤0`. This **confirms,
and if anything slightly strengthens**, P2's own "suggestive, not decisive"
framing — the 95% interval technically still touches zero, but barely, and
the one-sided evidence for a positive shared signal is substantial at `n=25`.

**What this changes and does not change.** Sub-claim I (§1, §8: "`k`
identifiable from current/near-future data") stays **BROKEN for the force**
— nothing here moves the amplitude problem. But a narrower, logically prior
claim — "`k`, as defined, is not simply `M` wearing a different unit" — now
has genuine, independently-instrumented, if statistically marginal, support.
This matters for §19's Kill Analysis: the mass-scaling circularity finding
there is about whether the *theory* predicts `u_i`'s scaling (it does not —
unaffected); this is about whether `u_i`'s *numerator* (`k_i`) is real
information at all (weak-but-real evidence that it is). These are different
questions and neither closes the other.

---

## §9. Negative control, chosen by causal structure

A negative control must exercise the mechanism under test and be known, in
advance, to fail. The obvious "set `k=0`" control is *not* adequate here — it
was already tried in the original file's own Control 2 and shown (§6 of the
original's docstring) to be too weak: it removes exactly the terms whose sign
was buggy in an earlier version, so it "passes" whether or not the algebra is
right.

**Causally motivated control used instead:** the derivation
`β_d=2, β_q=√6` never uses the *numeric values* of `k_i, r_i, m_i` — it is a
symbolic identity in those variables. Therefore, substituting **shuffled or
synthetic `k_i` values, uncorrelated with the real `r_i, m_i`,** must still
return `β_d=2, β_q=√6` exactly — because these numbers are a property of the
interaction *form*, not of any dataset. This *is* the correct negative
control, and running it (trivial, since the SymPy derivation contains no data
input at all) confirms the intended reading: **`β_d=2, β_q=√6` are not
empirical predictions fitted to or extracted from cluster data — they are
theorems about the multipole expansion of two Coulomb-coupled dipole pairs,
true for any assignment of charges whatsoever.** This sharpens §19's Kill
Analysis: what the real cluster data can test is not `β_d, β_q` (algebraic,
untestable by definition) but whether the *resulting force*, evaluated with
real `k_i, r_i, m_i`, is large enough to matter (§8: it is not, by 5–13 orders
of magnitude).

---

## §10. Simulation-based calibration / parameter recovery — scoped, not fabricated

The task asked whether `β_q/β_d ∈ {1.2247, 2.8284, 4.0}` are distinguishable
given realistic noise. Given §8's amplitude result and §13's finding that the
one proposed independent channel (pairwise-`K₄`) is already dead
(`FINDING_dipole_shell_is_a_double_layer.md`, same day, same thread), a full
SBC posterior-coverage exercise would be answering a question whose answer is
already `no, by construction` — building the machinery would not change the
conclusion, only dress it in inferential language it doesn't need. Recorded
honestly as **not run**, with the reason stated, rather than run superficially
to produce a plausible-looking but decision-irrelevant number
(`hooks`-flagged pattern: validation theater is not only fabricating a
result, it is also running a real computation whose outcome was already
forced and presenting it as if it settled something new).

---

## §11. Cosmological-limit / stability audit — blocked by a missing precondition

Ghost/gradient/tachyon analysis, propagation speed, and the GR/Newtonian
limit all require an **action** to vary. §4 already established that no
action exists for the two-charge construction — it is a static two-body
energy sum, never promoted to a field theory. **This section cannot be run,
and forcing an answer would be fabrication.** Contrast with the *separate*
single-field completion (`FINDING_R7_collapses_to_one_action.md`), which
*does* have an exact covariant action and *did* get this treatment (ghost
boundary `χ_ghost=-1/(3ε)`, shown not reached by the physical branch) — that
result belongs to a different candidate (H2) and does not transfer to H1
(two-charge) by Gate 1's non-transfer rule. **Sub-claim L: UNKNOWN, and stays
unknown until someone writes down the Lagrangian this construction is prose
about.**

The `Φ` absolute-zero-point pathology found in `FINDING_field_equation_solved.md`
§3 (theory not invariant under `χ→χ+const`, IR boundary condition
undefined) belongs to the single-field completion specifically, and likewise
does not automatically transfer — but since the two-charge construction has
no field equation at all yet, whether an analogous pathology would appear is
also **UNKNOWN**, not "avoided."

---

## §12. Dimensional analysis — mechanical check

Under `k_i,m_i→λ_M(k_i,m_i)`, `r_i→λ_r r_i` (independent rescalings):
`u_i(scaled)/u_i = λ_r` exactly, `λ_M` cancels (confirmed symbolically,
`counterfactual_checks.py` Test 4). `ℓ_d` therefore scales purely as a length,
consistent with its definition (`r_dA=β_d r_A`). No dimensional inconsistency
found. Low information value (this was never in doubt from the construction),
included for completeness per the task's own checklist.

---

## §13. Decisive experiment — H1 (two-charge, 1.2247) vs. H2 (one-field, 2.8284) vs. H3 (AI-fit, 4.0)

**This section's premise needs correcting before it can be answered.** The
target material itself proposed exactly one "cheap test": the pairwise-kSZ
`K₄` channel, independent of `H(z)` and of any β-conversion. **That test was
attempted and killed the same day, in the same experiment thread, one finding
later:** `FINDING_dipole_shell_is_a_double_layer.md` shows a radially-aligned
(induced) dipole shell is a double layer whose force vanishes identically off
contact — `K₄^field=0` exactly — and a randomly-oriented (intrinsic) dipole
shell averages to zero at first order regardless. **Both branches close the
same route.** This audit did not need to rediscover this; it needed to *not
propose the same dead test again*, per the Adaptive Iteration Branch Rule.

With that route closed and §8's amplitude result established, the honest
answer is: **no observable currently in this repository, or plausibly
reachable with current cluster/kSZ data, can separate H1/H2/H3.** Information
value of a hypothetical perfect measurement of `ℓ_q²/ℓ_d²` would be **high in
principle** (it uniquely falsifies H1, since H1 alone among the three is a
fixed point prediction — H2 is a whole family that can mimic any ratio by
choosing `f₂`, per §7/`FINDING_lq2_test_outcome.md`; H3 is a same-day AI fit
to unrelated data, already flagged Gate-2-non-target) but **zero in practice**
given the `10⁵-10¹³`× amplitude floor. **H2 is not really a competing point
hypothesis at all — it's a family flexible enough to fit whatever H1 or H3
predict, which is itself evidence that a bare ratio measurement was never
going to be very informative.**

---

## §14. Four-model adversarial comparison

| | M0 Newton/GR | M1 one-field (R7 class) | M2 two-charge | M3 phenomenological MULTING (Table A1) |
|---|---|---|---|---|
| Action exists? | Yes | Yes, exact, covariant (fixed bkgd) | **No** | No (not a field theory, a fitted force law) |
| Falsifiable ratio prediction? | N/A (no dipole/quad term) | No — family absorbs any ratio via `f₂` | **Yes, fixed: 1.2247** | N/A — β fitted post hoc to `H(z)` by an AI service (Gate 2) |
| Mass-scaling of `ℓ_d` | N/A | `+1` exactly, forced class-wide (§7) — **10.8σ from data** | Inherits data's own `+0.555±0.041` by construction, not derived (§19) | Data-defined by construction |
| Sign rule | N/A | Not addressed | **Derived theorem** (§6) | Postulated (preprint §2.2) |
| Effect size at real cluster scales | exact | `εM` — untested against real amplitude in this material | `ℓ_q²/D²~10⁻¹³` — physically inert (§8) | Table A1's own β gives comparable inertness (`FINDING_lq2_test_outcome.md` §3) |
| Cosmological stability checked | trivially | Yes — ghost boundary located, not reached (§11) | **Cannot be checked — no action** | Not applicable, not a field theory |
| Verdict this audit | baseline | ruled out on mass-scaling (§7, class-wide, strengthened) | undecided pending an action (§11); numerically inert regardless (§8) | not a physical target (Gate 2, prior findings) |

---

## §15. Pre-registered predictions — an honesty note, not a fake blind test

Genuine pre-registration must happen *before* the analyst has seen the
comparison outcome. By the point this section is reached, this audit had
already run §3–§14 — writing four predictions now and calling them
"pre-registered" would be exactly the validation-theater shape this project's
own rules exist to catch (a test authored after its answer is known). Instead:

**A.** *If* a future survey reaches sensitivity to `ℓ_q²/ℓ_d²` at the
`10⁻¹³`-relative level on cluster pairs, H1 predicts `0.375`
(identical-body limit) — a number this audit can commit to now because it was
derived in §3 before any data comparison was attempted.

**B.** *If* an independent principle is ever found that fixes `f₂=0` for the
one-field class (none exists in this corpus, per `FINDING_lq2_test_outcome.md`
§1), M1 becomes a genuine falsifiable competitor at `2.8284`; until then it is
not one.

**C.** *If* someone writes the actual Lagrangian this construction's prose
describes, the resulting propagator/ghost analysis is predicted (not
verified) to resemble the R7 action's own healthy branch, since both are
built from an ordinary kinetic term — this is a **guess**, explicitly marked
`[SPECULATIVE]`, not a result of this audit.

**D.** The mass-scaling exponent measured in §8 (`0.555±0.041`) is predicted
to be stable under a leave-one-cluster-family-out test, since it is dominated
by the `R500-M` scaling relation's own tight scatter rather than by any
individual cluster subclass — **this prediction was WRONG.** Run in §16: no
real cluster-family label exists in the data (single catalog, single
pipeline), and under the best available substitute partitions (mass tercile,
z quartile) the exponent moves by more than one bootstrap SE in 3 of 7
removals. Recorded here exactly as written before the check ran, per §15's
own stated purpose — a prediction that survives contact with data is worth
less to report than one that is checked honestly and shown to fail. The
*qualitative* single-field exclusion (§7) still survives (§16); the specific
precision of `0.555±0.041` does not.

---

## §16. Stress-test battery

Most of the classic battery (bootstrap, leave-one-out, noise injection,
alternative priors) tests robustness of an **empirical fit**. `β_d=2, β_q=√6`
are not a fit — they are an algebraic identity in symbolic charges (§9),
provably invariant under resampling by construction, so running bootstrap on
them would be theater with a predetermined "PASS." What *is* legitimately a
fit, and was stress-tested this pass:

- **Sign flip** — done, §5/§6 (orientation sweep IS the sign-flip stress test
  here; two of five configurations flip the dipole sign, confirming the
  claimed configuration is not arbitrary).
- **Field/parameter rescaling** — done, §3 Test 2 (uniform survives,
  non-uniform breaks — a real, non-trivial result).
- **Random orientation** — done, §5 (5 configurations, 2 new).
- **Synthetic noise on real inputs** — done, §8 (measurement-noise MC).
- **Bootstrap on the one real regression in this thread** (`d ln u/d ln M`) —
  done, §8, independently: `[0.514, 0.596]` 68% CI, `n=548`, `3000` resamples.
- **±10%/±50% parameter perturbation** — not run; not applicable to an
  algebraic identity (§9), and the one real regression in this thread
  (mass-scaling exponent) is addressed by the leave-one-family/z-out test
  below instead.
- **Leave-one-cluster-family-out, leave-one-z-bin-out** — **now run**
  (`leave_one_family_out.py`, added after this document's first draft).
  **First finding, before any statistics: there is no real cluster family to
  leave out.** `catalog`, `ICM_proxy_type`, and `dynamical_state` are constant
  across all 548 rows (100% MCXC-I, 100% `Y_SZ_derived_LCDM`, 100%
  `unknown`-dynamical-state) — the `±0.041` bootstrap uncertainty on the mass-
  scaling exponent is a *within-one-pipeline* statistical uncertainty and
  carries no information about cross-catalog or cross-pipeline systematics,
  because no second pipeline is present in this dataset to compare against.
  That is itself a finding, distinct from anything below.

  Substituting the best available non-arbitrary partitions — mass tercile and
  redshift quartile — the exponent is **not** uniformly stable: dropping the
  low-mass third gives `0.432±0.069`, dropping the high-mass third gives
  `0.630±0.072`, dropping the lowest-z quartile gives `0.379±0.051` — three of
  seven leave-one-out removals shift the point estimate by *more* than one
  full-sample bootstrap SE (the mid-mass third and the three higher-z
  quartiles are stable). **This was not predicted before running** — an
  earlier draft of the summary in `leave_one_family_out.py` asserted uniform
  stability and was wrong; it was corrected against the actual output before
  being recorded here, which is the point of running the check rather than
  reasoning about what it would probably show.

  **What survives and what doesn't.** The *qualitative* conclusion of §7/§8 —
  that the single-field completion's exact `+1` is excluded — is unaffected:
  even the most single-field-favorable subsample (drop the high-mass third,
  `0.630±0.072`) is still `~5.1σ` from `+1`, not the headline `10.8σ` but
  nowhere near consistent either. What does **not** survive at full strength
  is treating `±0.041` as the complete uncertainty budget on the *specific*
  number `0.555` — real mass/z-subpopulation spread is roughly `3-4×` larger
  than the single-fit bootstrap SE alone reports. This nuances §8's
  `[VERIFIED-REAL]` claim: the exponent and its exclusion of `H2`'s single-field
  prediction are real and now doubly independently confirmed; the four-digit
  precision quoted anywhere in this thread (`0.555±0.041`) should be read as a
  same-pipeline statistical figure, not a population-representative one.

---

## §17. Non-binary scoring

| # | Claim | Verdict | Confidence |
|---|---|---|---|
| 1 | `β_d=2, β_q=√6` follows algebraically from two coupled dipoles | CONFIRMED (independent code path) | HIGH |
| 2 | Alternating sign rule is derived, not postulated | CONFIRMED | HIGH |
| 3 | Orientation uniquely fixed by A↔B symmetry alone | REFUTED AS STATED, survives with added condition | MEDIUM→HIGH after repair |
| 4 | Construction is a genuine local ghost-free field theory | UNSUPPORTED (no Lagrangian exists) | LOW |
| 5 | `β_q/β_d=1.2247` is convention-free | PARTIALLY REFUTED (only under uniform-body convention) | MEDIUM |
| 6 | Attractive at every separation (3/8 ≥ 1/4) | CONFIRMED, inherits #5's caveat | HIGH |
| 7 | Mass-scaling obstruction "cleared" | REFUTED AS FRAMED — see §19 | HIGH (that it's circular) |
| 8 | No single-field completion (any member) can fix mass-scaling | CONFIRMED, new/stronger result | HIGH |
| 9 | `k` identifiable from current/near-future data | REFUTED — amplitude, not noise, is the blocker | HIGH |
| 10 | A decisive test currently exists to separate H1/H2/H3 | REFUTED — the one proposed route is already dead (same thread) | HIGH |
| 11 | A genuine local, ghost-free action exists for the two-charge/derivative-coupling picture | CONFIRMED (§4a, independently re-verified) — supersedes row 4's original SPECULATIVE rating | HIGH |
| 12 | This completion can supply MULTING's cosmological `H(z)` eras | REFUTED (§4a) — contributes only `G`-renormalisation on an isotropic background | HIGH |
| 13 | `k` (thermal-energy charge) carries real information beyond `M`, independent of the force-observability question | SUGGESTIVE, not decisive (§8a, independently re-verified, n=25, bootstrap 95% CI barely includes 0) | MEDIUM |
| 14 | Self-similar (pure-gravity, standard-baryon) theory independently predicts `d ln(u)/d ln(M)=+1`, matching the single-field completion's own forced prediction | CONFIRMED (§19a, derived from scratch: HSE virial argument + exact geometric `R500-M` definition, the latter checked to `0.0005 dex`) | HIGH |
| 15 | The `0.555±0.041` exponent quoted throughout this thread is the correct number to compare against `+1` | **CORRECTED** (§19a) — it is a selection-confounded marginal statistic; the redshift-deconfounded partial exponent is `0.393±0.055`, further from `+1`, not closer | HIGH |
| 16 | The mass-scaling comparison (either completion) tests gravitational-theory content | REFUTED (§19a) — the ~11σ departure from self-similar `+1` matches the independently well-documented signature of baryonic feedback, not anything either completion's authors modelled | MEDIUM (mechanism attribution `[WEAK]/[MEMORY]`), HIGH (that *some* unmodelled confound this large exists) |

---

## §18. Synthesis

The construction survives as **a real, nontrivial piece of algebra**: two
electrostatically-coupled physical dipoles, summed and expanded, exactly
reproduce MULTING's three-tier bilinear structure, its alternating sign
(derived, not assumed), and its attractive-everywhere margin — independently
reconfirmed in this audit via a fresh code path. The orientation argument
needed a genuine repair (§5) but the practical conclusion held. The
mass-scaling class-wide no-go for one-field completions (§7) is a real
contribution this audit adds, not merely inherited.

It fails to survive as **a completion that resolves the obstruction it was
built to resolve**, or as **a tested physical theory**. The "10.8σ gap
closed" claim is the single most consequential overclaim in the target
material — not fabricated, but a fit-for-purpose confusion between "does not
contradict the data" and "predicts the data," exactly the FITTED-vs-DERIVED
failure mode this project's own methodology (`research-methodology.md`
Type 2) exists to catch. And it has no action, so the entire second half of
the physics program (ghost-freedom, propagation, cosmological limit) has no
object to be checked yet.

---

## §19. Kill Analysis — recorded first, per the mandatory rule, before any patching (none attempted)

**What this audit killed:** the claim, as stated in `FINDING_two_charge_completion.md`
§5 and its Verdict block, that the two-charge construction *clears* (derives,
predicts, resolves) the 10.8σ mass-scaling discrepancy between MULTING and a
single-field completion.

**Why it is killed.** `ℓ_d = 2(u_A+u_P)` with `u_i ≡ κk_ir_i/(c²m_i)` is
correct as an algebraic consequence of the construction (§3, confirmed). But
`u_i` is not predicted by the two-charge theory — `k_i` and `r_i` are real,
independently-measured cluster observables (thermal energy, `R500`), taken
as-is from data that already carries its own empirical mass-scaling
(`k∝M^1.269`, `r∝M^0.287`, independently reconfirmed §8). The two-charge
theory contributes *only* the bilinear combination rule `ℓ_d∝(u_A+u_P)`; it
supplies no mechanism that would make `u_i` scale with `M` any particular
way. So "the +0.555 exponent is reproduced" is true only in the trivial sense
that whatever exponent the *data* has, the theory inherits unchanged — this
is indistinguishable, at the level of this specific test, from a theory that
makes *no* mass-scaling prediction at all. It is not falsified by the +0.555
measurement, but it is not confirmed by it either — a claim immune to a
measurement by construction is not "cleared" by that measurement.

**What was NOT killed:**
- The core algebraic identity §3(A), §6 (sign theorem), and the
  attractive-everywhere margin §3(J) — all independent of the mass-scaling
  question entirely.
- The single-field no-go itself (§7) — strengthened, not weakened, by this
  audit.
- The general *shape* of MULTING's bilinear dipole structure being
  reproducible by a two-charge multipole sum — a real, freestanding
  contribution regardless of the mass-scaling question.

**Relaxation map** (one assumption at a time, per the Minimal Relaxation Rule):
| Remove/Weaken/Replace | New variant | Cheapest test |
|---|---|---|
| Replace "u_i taken from data" with "u_i predicted by a specified microphysical model of ICM thermal energy and R500 vs. M" | A genuinely predictive two-charge completion | Would need an independent theory of cluster thermal-energy/radius scaling — a separate, large research question, not a small patch |
| Weaken "clears the obstruction" to "is not contradicted by, and does not independently predict, the mass-scaling data" | Same construction, honestly scoped claim | No new test needed — this is the correct current status |
| Remove the uniform-lever-arm-convention assumption (§3 F) | `β_q/β_d` becomes a function of `γ_A/γ_B`, no longer a bare number | Would need an independent derivation of the lever-arm-to-radius law per body type |

---

## §19a. Microphysical derivation of `u_i`'s mass-scaling — the NEXT item this closes, and a correction it forces

`src/cluster_data_pipeline.py` shows the 548-cluster sample's `k_i` comes from
`e_thermal_path_b()` — an **exact** SZ-effect physics conversion,
`E = Y_SZ·D_A²·(mₑc²/σ_T)`, not a fitted power law. So `k_i`'s mass-scaling
is not a pipeline artefact — it is the real Y_SZ-M relation of the actual
catalogue, and a first-principles microphysical comparison is meaningful, not
circular in the way a self-referential definition would be.

**The derivation** (standard self-similar cluster model — Kaiser 1986; the
algebra below is derived from scratch, the specific literature exponents it
reproduces are `[WEAK]/[MEMORY]`, no live citation lookup this pass):

```
R500 is DEFINED by M500 = (4/3)pi*500*rho_crit(z)*R500^3
    => R500 ~ M500^(1/3) rho_crit(z)^(-1/3)                 [EXACT, geometric]

Hydrostatic/virial temperature: k_B T ~ G M mu m_p / R
    => T ~ M/R ~ M^(2/3) E(z)^(2/3)                          [self-similar]

Universal gas fraction: Mgas ~ f_gas * M  => Mgas ~ M^1       [self-similar]

E_thermal ~ Mgas * T ~ M^(5/3) E(z)^(2/3)                     [self-similar]

u_i = k_i r_i / m_i ~ M^(5/3+1/3-1) E(z)^(2/3-2/3) = M^1 E(z)^0
```

**Self-similar (pure-gravity) theory predicts `d ln(u)/d ln(M) = +1` exactly**
— the same `+1` the single-field completion needs (§7) — from a completely
independent argument, and no net redshift dependence at fixed mass.

**Zero-parameter check, run first** (`microphysical_u_scaling.py`): does
`R500c_Mpc` actually satisfy its own definitional relation to `M500c_Msun` via
`ρ_crit(z)` (Planck18, matching the pipeline's own cosmology choice)? Yes, to
`std=0.0005 dex` across all 548 clusters — confirming `r_i`'s contribution to
`u_i`'s scaling is exactly `M^(1/3)` at fixed z, geometric, zero free
parameters, not independent astrophysics at all.

**The correction this forces.** Every mass-scaling number quoted in this
audit up to this point (`0.555±0.041`, the "10.8σ" figure, §7's and §16's
discussion) was the **marginal** `d ln(u)/d ln(M)` — without controlling for
redshift. P2 (§8a) already showed this matters for `k` alone (marginal
`α=1.27` → `α=1.02` once `z` is controlled via `ln(1+z)`) but this audit had
not yet applied the same correction to `u_i` itself. Doing so here, with the
physically-motivated control self-similar theory actually specifies
(`E(z)=H(z)/H₀`, not the ad hoc `ln(1+z)`):

```
d ln(u)/d ln(M), controlling for E(z)  =  0.393 +/- 0.055   (bootstrap, n=548)
d ln(u)/d ln(E(z)), at fixed M         =  +2.260             (self-similar predicts 0.000)
```

**This is a different, and more defensible, number than the `0.555±0.041`
used throughout this thread** — the marginal exponent conflates true mass
dependence with this flux-limited sample's real M–z selection correlation,
exactly the same conflation P2 already flagged for `k` alone. Properly
deconfounded, `u_i` is *further* from the self-similar/single-field `+1` than
the marginal number suggested (gap `0.607` vs `0.445`), so the qualitative
single-field exclusion (§7) is, if anything, slightly **strengthened**, not
weakened, by this correction (~11σ vs the previously-quoted 10.8σ) — but the
*specific* number `0.555±0.041` that has been cited as *the* mass-scaling
exponent since `FINDING_field_equation_solved.md` should be understood as a
selection-confounded marginal statistic, not the deconfounded physical slope.
This was not previously checked because nobody in this thread — this audit
included, until now — had regressed `u_i` itself against a physically-motivated
redshift control; only `k` alone had received that treatment (P2).

**The resolution of §19's Kill Analysis, now precise rather than qualitative.**
The self-similar derivation shows `+1` is *also* the pure-gravity, standard-
baryon-physics prediction — via a completely independent argument from the
single-field completion's own. So the ~11σ departure from `+1` is not
MULTING-specific or two-charge-specific content at all: it is the same,
independently well-documented `[WEAK]/[MEMORY]` phenomenon of baryonic-feedback
breaking self-similarity (real Y_SZ-M and T-M relations running shallower than
`5/3`/`2/3`, generally attributed to AGN/supernova feedback disproportionately
affecting lower-mass systems — standard in X-ray/SZ cluster astrophysics, not
re-verified from a primary source this pass). **Neither the single-field nor
the two-charge completion's comparison to real cluster mass-scaling data is
actually testing gravitational theory content until baryonic feedback is
modelled explicitly** — both are being compared against a quantity whose
departure from `+1` is dominated by ordinary gas physics, not by anything
either completion's authors wrote down. This is a sharper, more mechanistic
version of §19's original circularity finding, not a reversal of it: `u_i`'s
scaling was already shown to be inherited from data rather than predicted;
this addendum explains *what* that inherited scaling actually is (feedback
astrophysics) and shows the comparison number itself needed a correction.

---

## §20. Final verdict

```
SURVIVES : the algebraic two-charge derivation of beta_d=2, beta_q=sqrt(6),
           the derived (not postulated) alternating sign rule, the
           attractive-everywhere margin, and the orientation argument
           (once repaired to require nonzero dipole moment, not symmetry
           alone). All four independently re-derived in this audit via a
           fresh code path, not merely re-run from the original's own
           control functions.

BREAKS   : the claim that this construction "clears" MULTING's 10.8-sigma
           mass-scaling obstruction (Kill Analysis, S19) -- it reproduces
           the data's own exponent by inheriting u_i from real cluster
           observables, not by predicting it. Also breaks: identifiability
           of k from any current or near-future observable (amplitude
           gap of 5-13 orders of magnitude, S8); the "one cheap test"
           the target material itself proposed (already dead, same
           thread, S13); convention-freedom of the 1.2247 number in full
           generality (only survives under a same-law-for-both-bodies
           assumption, S3).

UNKNOWN  : whether this is a local, ghost-free field theory at all (S4,
           S11) -- no Lagrangian exists in the material to check. This is
           not "probably fine" or "probably broken" -- the question
           cannot currently be asked of this object.

NEXT     : (a) [DONE, S19a] u_i's mass-scaling now has an independent
           microphysical (self-similar) prediction, derived from scratch:
           d ln(u)/d ln(M) = +1 EXACTLY (HSE virial T-M argument + an
           exactly-confirmed geometric R500-M identity, std=0.0005 dex
           across n=548). This does NOT rescue the "obstruction cleared"
           claim -- if anything it sharpens the kill: +1 is independently
           the pure-gravity prediction too, so the ~11 sigma departure is
           ordinary baryonic-feedback astrophysics, not gravitational
           content either completion's authors modelled. It ALSO forced a
           correction: the properly redshift-deconfounded exponent is
           0.393+-0.055, not the marginal 0.555+-0.041 this whole thread
           (including the original FINDING files) had been citing --
           further from +1, not closer, so the single-field exclusion
           survives (strengthens slightly) but the specific number in
           general circulation was imprecise and should be corrected at
           the source.
           (b) [DONE, S4a] the action was written elsewhere in the same
           thread (P1) and independently re-verified here: linear kinetic
           term (ghost-free by construction), beta_q/beta_d fixed purely
           by mediator masslessness (Lambda=3/2), independent of the
           lever-arm convention this audit's own S3 flagged. Also answers
           S11's cosmological question in the negative for the broader
           MULTING+ program: this completion contributes only a
           G-renormalisation to the background, structurally unable to
           source MULTING's H(z) eras -- a second, independent route to
           the same q-blindness conclusion the Table A1 provenance work
           reached separately.
           (c) [DONE] leave-one-family/z-out on the mass-scaling exponent
           -- no real cluster-family label exists in the data at all
           (single catalog, single pipeline); under the best available
           substitute (mass tercile, z quartile) the point estimate moves
           by >1 bootstrap SE in 3 of 7 removals -- the qualitative
           single-field exclusion survives (worst case still ~5.1 sigma
           from +1), but +-0.041 understates real population spread by
           roughly 3-4x.
           (d) [DONE] a second, independent cluster pipeline was found
           (not built from scratch -- P2, same thread, appeared mid-audit)
           and every one of its numbers independently re-derived from
           fresh code: CHEX-MATE's galaxy-velocity-dispersion mass and
           X-ray spectroscopic temperature, cross-matched against the
           pipeline's own (X-ray-luminosity-based) mass, give a genuinely
           cross-instrument residual correlation rho=+0.36 (n=25,
           bootstrap 95% CI [-0.015,+0.674]) between the pipeline's
           thermal-energy k and an independent T-measurement at fixed M --
           suggestive, not decisive, that k carries real information
           beyond M. This answers a narrower, logically prior question
           than S8/S13's force-observability finding, and does not
           change it: k being real information does not make its force
           observable: (a) above is the only load-bearing item still open.
```

**Direct answer to the question this audit was commissioned to settle:**
after this audit, what exists is a genuine, independently-reconfirmed
**mathematical construction** that reproduces MULTING's weak-field bilinear
structure, sign rule, and stability margin from a two-charge multipole sum —
and a **narrative**, not yet a derivation, that this construction is a local
field theory, and a **claim that overstates its own evidence** about clearing
the mass-scaling obstruction. It is not yet a physical two-field completion of
MULTING. It is the best-supported *candidate* for one in this project's
corpus, specifically because the algebra survived independent attack better
than any prior candidate did — but "survived attack on the algebra" and
"is a physical theory" are two different sentences, and only the first one is
true right now.
