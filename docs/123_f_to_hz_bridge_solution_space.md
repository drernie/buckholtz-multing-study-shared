# docs/123 — F→H(z) Bridge: Solution Space (boyko-goal-expansion-100, deep mode)

**Date:** 2026-07-17
**Skill:** `/boyko-goal-expansion-100 deep`
**Status:** EXPLORATORY — this document is idea-generation, not a registered FL
experiment. No item here has been tested; each idea card lists a cheap test that
WOULD need to be run before any item could be promoted to `experiments/`.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NOT_AUTHOR_ERROR
**Validation:** `scripts/validate_output.py` run against this file — 0 CRITICAL
findings, 53/53 cards parsed and structurally complete (item 53 added 2026-07-17
after external review; re-validated). Category-distribution
WARNINGS remain by design (see "Honest scope note" below; not defects).
`scripts/detect_duplicates.py` flagged one pair above its 0.5 threshold: #36/#37
(similarity 0.58) — reviewed manually, not merged: they test different upstream
mechanisms (item 4's TeVeS route vs item 7's kinetic-theory route) through the same
downstream pipeline (item 35), so the high token overlap is from shared
test-procedure wording, not a shared physical mechanism. Kept as two cards,
documented here rather than silently dismissed.

---

## Honest scope note (per skill's own Step 7 discipline)

This report contains **53 content-distinct ideas** (52 original + item 53 added
2026-07-17 after external review), not 100. After generating a wider
internal pool and deduplicating by mechanism (not wording), padding to 100 would have
meant listing "apply method X" and "apply improved method X" as separate items, or
restating the same action-principle idea with different symbol names. The skill's own
instructions are explicit that this is the wrong trade — count is not the point,
survived content is.

A direct consequence: the automated validator's category-distribution targets
(`cross_domain_transfer >=25`, `no_go >=10`, `computational_experiment >=10`) are
calibrated for a full 100-idea run and are **not met** here (cross_domain_transfer=13,
no_go=5, computational_experiment=6). This is reported as WARNING, not CRITICAL, by
the validator itself, and is the expected, disclosed result of an honest 52-idea
pool rather than a padded 100-idea one.

---

## Stage A — Formalization

**Success criterion (observable):** A candidate bridge counts as a genuine answer
only if it (a) starts from a mathematically well-posed object — an action, field
equations, or an explicit statistical-mechanics coarse-graining procedure, not a
postulated mapping; (b) reduces to `F_oP = F_m - F_d + F_q` (or a stated
generalization of it) in an identified limit; (c) yields an explicit `H(z)` or
modified-Friedmann-equation prediction, numerically evaluable against real data with
this project's existing tooling (`src/pearson_fit.py`-style pipeline); (d) is
falsifiable — produces a curve shape genuinely different from the plain-monopole
baseline that `NR-013` already shows wins under simple coefficient-fitting, not a
relabeling of the same phenomenological placeholder.

**What falsifies the whole direction (not just one candidate):** if every
structurally distinct route surveyed here either (i) collapses back to the existing
`D=D0/(1+z)` placeholder once written out explicitly, or (ii) produces a bridge that,
when tested, also fails to beat the monopole baseline — that would extend `NR-013`'s
finding from "coefficient-fitting doesn't help" to "the mapping problem itself doesn't
help, regardless of construction route." That is itself a publishable negative result
for bottleneck #1, not a failure of this exercise.

**Known logical gaps (from `src/pearson_fit.py`'s own "G1 BLOCKER" docstring and this
session's `docs/122`/`NR-013` chain):**
- **Gap 1 — no Lagrangian/action.** `F_oP` is motivated by an EM analogy and
  Lorentz-invariance-of-internal-kinetic-energy, not derived from a stated action.
- **Gap 2 — no aggregation prescription.** No stated rule for going from a pairwise
  two-body force to a continuum source term usable in a Friedmann equation.
- **Gap 3 — no relativistic completion checked.** Even a valid weak-field bridge
  needs PPN/gravitational-wave/causality checks before it is a real theory, not just
  a fitting function with a new name.
- **Gap 4 — parameter re-identifiability.** Any new bridge introduces its own free
  constants; unless they are fixed independently of the `H(z)` fit itself, it
  reopens exactly the identifiability problem `R011`/`NR-013` already closed for
  `(beta_d, beta_q)` in the current placeholder.

**Unknowns:** whether TJB has an unpublished action/field formulation in mind (not in
the public preprint); whether the EM analogy is meant literally (a real vector/tensor
field sourced by "isomer charge") or only heuristically; whether the six IDM isomers
are meant to source six independent multipole channels or one shared one.

---

## Stage C — Domain lens map (19 lenses selected, ≥12 required)

| # | Lens | Why it applies here |
|---|---|---|
| 1 | Modified-gravity phenomenology (MOND/TeVeS/AQUAL) | Closest existing precedent for "non-Newtonian per-particle force law → cosmology" |
| 2 | Effective Field Theory of Dark Energy/Inflation | Standard modern shortcut: parametrize cosmological behavior without a full covariant Lagrangian first |
| 3 | Dipolar/polarizable-medium electrodynamics | `F_oP`'s own stated EM analogy — literalize it via an existing covariant dipolar-fluid action (Blanchet-Le Tiec) |
| 4 | Statistical mechanics / kinetic theory (Boltzmann, Vlasov-Poisson) | The right tool for turning a microscopic pair-force into a macroscopic pressure/energy-density term |
| 5 | GR cosmological perturbation theory | Needed regardless of which action is chosen, to get from field equations to `H(z)` |
| 6 | Entropic/thermodynamic gravity (Verlinde, Jacobson) | An alternative route to an effective force law that bypasses writing a Lagrangian at all |
| 7 | Post-Newtonian formalism (PPN) | Standard weak-field consistency check any candidate bridge must eventually pass |
| 8 | N-body / cosmological simulation methods | Lets the bridge be tested numerically before it is solved analytically |
| 9 | Higher-dimensional / Kaluza-Klein reduction | Six isomers is suggestive of a compact internal space; dimensional reduction is the standard tool for turning internal-space structure into 4D effective forces |
| 10 | Scalar-tensor gravity (Horndeski, Brans-Dicke) | The most general known family of single-extra-field gravity theories — natural target to check for structural match |
| 11 | Continuum mechanics / stress-energy construction | Standard bridge from "force between particles" to "T_munu of a fluid" |
| 12 | Renormalization-group coarse-graining | Formalizes "which microscopic details survive at cosmological scale" — directly relevant to Gap 2 |
| 13 | Symmetry / group theory (FRW as a constraint) | Homogeneity+isotropy is a strong constraint that can partially FIX the aggregation rule, not just describe it |
| 14 | Holographic / AdS-CFT dark-fluid models | Alternative non-Lagrangian route to an effective dark-sector equation of state |
| 15 | Bayesian model comparison / information theory | Needed once >1 candidate bridge exists, to decide between them without re-opening a fitting contest |
| 16 | Control theory / system identification | Reframes "find the bridge" as transfer-function identification from (force-law, observed H(z)) data, structurally different from curve-fitting |
| 17 | Condensed-matter analogy (dipolar order parameters) | Ferroelectric/paraelectric phase-transition machinery as a structural analogy for a "polarizable dark sector" |
| 18 | Symbolic regression / ML-assisted functional discovery | A tool for SUGGESTING candidate closed forms from simulation output, not for fitting the final answer |
| 19 | History/philosophy of science (precedent study) | How Newton's `F=Gm1m2/r^2` became Friedmann's equations via GR is the literal template for what bottleneck #1 needs to redo |

---

## Stage D/E/F — Idea pool (53 cards, full template)

Scores use exactly the validator's five 0-10 axes plus confidence (0-1):
`relevance, feasibility, novelty, expected_impact, evidence_strength, confidence`.
`adjusted = priority_score - speculation_penalty` (formula in Stage: Scoring below).

### Block 1 — Direct / adjacent established methods (14)

## 1. Literalize the EM analogy via Blanchet-Le Tiec's dipolar-fluid action
Type: cross_domain_transfer
Evidence: hypothesis
Core mechanism: Blanchet & Le Tiec (arXiv:0804.3518, 0901.3114) already built a
covariant GR action for a polarizable dipolar dark-matter fluid, sourced by ordinary
matter, that reduces to MOND-like phenomenology at galactic scale and LambdaCDM-like
behavior cosmologically. `F_oP`'s dipole term is structurally the same object (a
gravitationally-induced dipole moment) under a different name. Adapt their action by
swapping their polarization mechanism for MULTING's isomer-pair mechanism.
Why it may work: an already-relativistic, already-cosmologically-tested action exists
for exactly this class of object, so the hard relativistic-completion work (Gap 3) is
already done for the dipole piece — only the sourcing mechanism needs adaptation.
Required assumptions: `F_oP`'s dipole term can be written as a gradient of a
dipole-moment potential in Blanchet's sense; isomer-pair interaction can be recast as
a polarization response to a gravitational field.
Main obstacle: their dipole is sourced by ordinary-matter gravitational polarization
of a dark fluid; MULTING's dipole is sourced by pairwise isomer-isomer interaction —
the sourcing mechanisms differ and the adaptation is not line-by-line.
Cheapest test: rewrite `F_oP`'s dipole term in Blanchet's notation and check whether
the resulting Poisson-like equation has the same order and symmetry structure as
theirs (a day of algebra, no new data needed).
Falsifier: if `F_oP`'s dipole term cannot be written as `-nabla(Pi . nabla Phi)` for
any dipole-moment field `Pi` (Blanchet's form), the analogy is only cosmetic.
Expected output: a short note stating whether the rewrite succeeds, and if so, the
explicit dictionary mapping MULTING symbols to Blanchet-Le Tiec symbols.
Scores:
  relevance: 9
  feasibility: 7
  novelty: 4
  expected_impact: 8
  evidence_strength: 7
  confidence: 0.65
Sources: [Blanchet & Le Tiec 2008, arXiv:0804.3518](https://arxiv.org/abs/0804.3518);
[Blanchet & Le Tiec 2009, arXiv:0901.3114](https://arxiv.org/abs/0901.3114)

## 2. Check F_oP against Blanchet's existing Planck bispectrum constraint on primordial dipole
Type: established_method
Evidence: fact
Core mechanism: **corrected 2026-07-17 after external review** — arXiv:1312.6991
("Dipolar Dark Matter and Cosmology," Blanchet) is NOT a general PPN bound as this
card originally claimed. Verified via direct source check: it is a second-order
cosmological-perturbation-theory result specific to Blanchet's own dipolar-dark-matter
(DDM) model, constraining that model's *primordial dipole amplitude* via the
Planck-measured bispectrum non-Gaussianity the DDM internal energy induces at second
order (first order is LambdaCDM-degenerate — this is the same degeneracy item 13
already investigates). It is model-specific, not a universal PPN-class bound.
Why it may work: still cheaper than inventing a new bridge, but the transfer to
`F_oP` requires the full model dictionary from item 1, not a direct number lookup —
weaker claim than originally stated.
Required assumptions: item 1's DDM-to-MULTING mapping exists and is close enough
that Blanchet's second-order non-Gaussianity calculation transfers; without item 1,
this source constrains Blanchet's model, not `F_oP`, at all.
Main obstacle: this is a second-order-perturbation, model-specific result, not a
weak-field two-body (PPN) constraint — the original card conflated the two; using it
without item 1's mapping first would misapply the bound to an unrelated model.
Cheapest test: re-read arXiv:1312.6991's actual bispectrum constraint and item 1's
DDM-to-MULTING dictionary together; only then check whether the resulting
constraint bears on the `(beta_d, D0)` regime `docs/122`/`NR-013` found problematic.
Falsifier: if item 1's mapping fails (its own falsifier), this source gives no
transferable constraint on `F_oP` at all — this item is now gated on item 1, not
independent of it as originally claimed.
Expected output: either a transferred numeric constraint (contingent on item 1
succeeding) or an explicit statement that this source does not apply to `F_oP`
without a DDM mapping.
Scores:
  relevance: 6
  feasibility: 5
  novelty: 2
  expected_impact: 5
  evidence_strength: 6
  confidence: 0.55
Sources: [Blanchet 2013, "Dipolar Dark Matter and Cosmology," arXiv:1312.6991](https://arxiv.org/abs/1312.6991) — re-verified 2026-07-17, second-order bispectrum/non-Gaussianity constraint on Blanchet's own DDM model, not a general PPN bound

## 3. Effective Field Theory of Dark Energy (EFT-DE) parametrization
Type: established_method
Evidence: hypothesis
Core mechanism: instead of guessing a full covariant action, use the unitary-gauge
EFT-DE formalism (Gubitosi, Piazza, Vernizzi, arXiv:1210.0201) to parametrize any
single-extra-degree-of-freedom modified-gravity background evolution by 3 time
functions. Fit those 3 functions to reproduce `F_oP`'s weak-field limit, then read
off the corresponding `H(z)` directly from the EFT background equations.
Why it may work: EFT-DE is explicitly designed to bypass writing a full Lagrangian
before getting a testable background evolution — the standard modern shortcut used
across the modified-gravity field for exactly this kind of problem.
Required assumptions: `F_oP`'s combined dipole+quadrupole structure reduces to at
most one extra scalar degree of freedom in the relevant limit.
Main obstacle: EFT-DE assumes ONE extra scalar degree of freedom; if MULTING's dipole
and quadrupole terms need two independent d.o.f., the formalism needs the (less
standard) multi-field extension.
Cheapest test: check whether `F_oP`'s dipole and quadrupole terms can both be written
as functions of a single scalar field's derivatives, or whether they are independent.
Falsifier: if two independent extra fields are structurally required, standard
single-field EFT-DE does not apply without extension.
Expected output: the 3 EFT-DE background functions (or a documented failure of the
single-field reduction) usable directly in item 35's test pipeline.
Scores:
  relevance: 8
  feasibility: 6
  novelty: 5
  expected_impact: 7
  evidence_strength: 8
  confidence: 0.6
Source: [Gubitosi, Piazza, Vernizzi 2013, arXiv:1210.0201](https://arxiv.org/abs/1210.0201)

## 4. TeVeS-style relativistic completion of a MOND-like per-particle law
Type: established_method
Evidence: fact
Core mechanism: Bekenstein's TeVeS (tensor-vector-scalar gravity) is the standard
existing template for covariantly completing a non-Newtonian per-particle force law
so it has a cosmology at all; its cosmological perturbation equations are already
published (astro-ph/0511591). Map `F_oP`'s monopole/dipole/quadrupole structure onto
TeVeS's tensor+vector+scalar fields as a structural template.
Why it may work: TeVeS already solved the exact class of problem (per-particle force
modification → covariant cosmology) once; reusing its field content saves rederiving
the relativistic completion from scratch.
Required assumptions: `F_oP`'s radial falloff structure has a term-by-term
correspondence to TeVeS's weak-field expansion.
Main obstacle: TeVeS's vector field enforces MOND's specific acceleration-scale
nonlinearity; `F_oP`'s dipole/quadrupole terms have a different radial dependence, so
the vector-field potential would need to be re-derived, not reused.
Cheapest test: compare `F_oP`'s asymptotic radial falloff (1/r^2, 1/r^3, 1/r^4 terms)
to TeVeS's known weak-field expansion; check for a matching term-by-term structure.
Falsifier: no matching order-by-order correspondence found.
Expected output: a term-by-term comparison table, TeVeS order vs `F_oP` order, with a
pass/fail verdict per term.
Scores:
  relevance: 7
  feasibility: 5
  novelty: 4
  expected_impact: 6
  evidence_strength: 7
  confidence: 0.5
Source: [Bekenstein 2004; TeVeS cosmology, arXiv:astro-ph/0511591](https://arxiv.org/abs/astro-ph/0511591)

## 5. Verlinde emergent-gravity route (bypass the Lagrangian entirely)
Type: cross_domain_transfer
Evidence: hypothesis
Core mechanism: instead of writing an action, derive an effective force law from an
entropy/thermodynamic argument (Verlinde, arXiv:1611.02269) the way Verlinde derived
"apparent dark matter" from entropy displacement. Check whether a similarly-motivated
thermodynamic argument, applied to isomer-pair interactions, produces something with
`F_oP`'s dipole/quadrupole structure.
Why it may work: it is an independent, non-Lagrangian derivation route that would
sidestep Gap 1 entirely if the analogy holds.
Required assumptions: isomer-pair interactions admit a horizon-entropy-displacement
interpretation analogous to Verlinde's baryonic-matter case.
Main obstacle: Verlinde's argument is specific to de Sitter horizon entropy and
baryonic matter displacing dark energy; the analogy to isomer-pair dipole/quadrupole
terms is not close on inspection — flagged as the weakest of the "big name" analogies
surveyed here.
Cheapest test: check whether Verlinde's derived force law has any term structurally
matching `F_oP`'s quadrupole 1/r^4 falloff.
Falsifier: no such match — Verlinde's force law is a single term, not a
monopole/dipole/quadrupole expansion, so a term-by-term match is unlikely by
construction.
Expected output: explicit statement of match or no-match, terminating this route
quickly either way.
Scores:
  relevance: 5
  feasibility: 5
  novelty: 6
  expected_impact: 4
  evidence_strength: 4
  confidence: 0.3
Source: [Verlinde 2016, arXiv:1611.02269](https://arxiv.org/abs/1611.02269)

## 6. Effective stress-energy tensor from the two-body force (continuum mechanics route)
Type: established_method
Evidence: inference
Core mechanism: standard continuum-mechanics procedure — given a pairwise force law
between point particles, the coarse-grained stress-energy tensor of the resulting
continuum is built from a sum over pairs, averaged over a fluid element. Apply this
directly to `F_oP` to get a `T^munu` usable in the standard Friedmann equations.
Why it may work: this is the most direct, lowest-machinery route from a pairwise
force to a usable cosmological source term, requiring no new formalism.
Required assumptions: the isomer-pair medium is dilute/weakly-correlated enough for
the coarse-graining to be valid.
Main obstacle: this coarse-graining is only valid in the dilute/weakly-correlated
limit; cluster-scale strong correlations (exactly where R011/NR-013 tested it) may
violate the assumption.
Cheapest test: check the coarse-graining's own validity condition (mean free path
much greater than inter-particle spacing) against the actual cluster densities
already in this repo's CCCP catalog.
Falsifier: if the validity condition fails badly at cluster densities, this route is
inapplicable exactly where the project's data lives.
Expected output: a pass/fail verdict on the validity condition at real cluster
densities, and if it passes, the explicit `T^munu` expression.
Scores:
  relevance: 8
  feasibility: 7
  novelty: 3
  expected_impact: 6
  evidence_strength: 5
  confidence: 0.5
Source: standard continuum mechanics (Landau & Lifshitz, Statistical Physics Part 1,
ch. XII)

## 7. Kinetic-theory/Boltzmann-equation route treating multipole force as interaction term
Type: established_method
Evidence: inference
Core mechanism: write the Boltzmann equation for the isomer phase-space distribution
with `F_oP` as the interaction/collision term, then take moments to get continuity +
Euler equations, then close with an equation of state — the standard route from
microphysics to cosmological fluid equations, keeping velocity-space information
item 6 drops.
Why it may work: this is the technically correct version of item 6, and it may share
required machinery with the project's other open bottleneck (#8/9, relic-abundance
Boltzmann calculation), so solving part of one helps the other.
Required assumptions: an initial/thermal isomer distribution function can be
specified or reasonably approximated.
Main obstacle: needs to specify the isomer distribution function's initial/thermal
state — re-opens the exact "need Boltzmann mechanics for relic-abundance" gap already
flagged for bottleneck #8/9 (`pearl_registry` Gorbunov entry).
Cheapest test: check whether the same thermal-history assumptions needed for #8/9's
relic-abundance calc also suffice to close this route for #1.
Falsifier: if the required closure assumptions for #1 and #8/9 turn out to be
mutually incompatible, they cannot share a derivation.
Expected output: a shared-assumptions note determining whether bottlenecks #1 and
#8/9 can be worked on jointly or must stay separate.
Scores:
  relevance: 9
  feasibility: 4
  novelty: 5
  expected_impact: 8
  evidence_strength: 5
  confidence: 0.4
Source: standard kinetic theory (Boltzmann equation for self-gravitating systems,
Binney & Tremaine, Galactic Dynamics)

## 8. Horndeski/generalized scalar-tensor family — reverse search for a match
Type: established_method
Evidence: fact
Core mechanism: Horndeski's theory is the most general known 4D scalar-tensor theory
with second-order field equations. Systematically expand its weak-field two-body
force to the same order as `F_oP` and check for a parameter choice reproducing the
monopole-dipole-quadrupole structure.
Why it may work: if a match exists, it comes with an already-proven-consistent,
already-well-studied covariant theory attached, skipping Gaps 1 and 3 simultaneously.
Required assumptions: `F_oP` is representable within a single-scalar-tensor
framework at all.
Main obstacle: Horndeski's published weak-field expansions are usually given to
monopole (PPN gamma, beta) order; dipole/quadrupole terms are non-standard and may
require deriving the expansion further than published results go.
Cheapest test: literature search specifically for "Horndeski dipole term" or
"odd-parity modified gravity two-body force" before assuming new derivation is needed.
Falsifier: if no Horndeski subclass produces an odd-parity (dipole) term at all
(plausible — Horndeski is typically parity-even), this route is closed cleanly.
Expected output: either a matching Horndeski subclass with explicit parameters, or a
documented, cited closure of the route.
Scores:
  relevance: 7
  feasibility: 6
  novelty: 3
  expected_impact: 6
  evidence_strength: 6
  confidence: 0.5
Source: Horndeski 1974 (foundational, pre-arXiv); modern review Kobayashi,
Yamaguchi, Yokoyama 2011, arXiv:1105.5723

## 9. Post-Newtonian order-counting to find the correct H(z) route by elimination
Type: no_go
Evidence: hypothesis
Core mechanism: **corrected 2026-07-17 after external review** — the original card
stated "monopole 0PN, dipole 0.5PN, quadrupole 1PN" as if it followed from the
radial powers alone. This does not hold: PN order is fixed by powers of `v/c` under
a stated metric/action, not by a term's `1/r^n` falloff by itself — a term can have
any radial power at a given PN order depending on the underlying theory. The
classification is at best a starting guess to check, not a derived result.
Why it may work: PN order-counting, done correctly (from an actual metric ansatz,
not guessed from radial power), is still a cheap, purely-analytic filter — the
mechanism's VALUE survives the correction, only the specific numbers in the original
card do not.
Required assumptions: a metric ansatz (simplest choice: isotropic PPN gauge) must be
fixed FIRST and the PN order derived from it — not assumed from radial dependence.
Main obstacle: without Gap 1 (an action) solved, any metric ansatz is itself a
guess, so the "PN order" this item produces is conditional on that guess, not a
theory-independent fact — weaker than the original card implied.
Cheapest test: assume the simplest metric ansatz and derive (not guess) each term's
PN order from it; report the result explicitly as ansatz-conditional.
Falsifier: not directly falsifiable — this is a filtering tool feeding other items'
falsifiers, not a standalone physical claim.
Expected output: an ansatz-conditional PN-order table for `F_oP`'s three terms,
explicitly labeled as dependent on the chosen metric ansatz, not a theory-independent
classification.
Scores:
  relevance: 6
  feasibility: 6
  novelty: 4
  expected_impact: 4
  evidence_strength: 2
  confidence: 0.3
Source: standard PPN formalism (Will, "Theory and Experiment in Gravitational
Physics", Cambridge, 2018 ed.) — the formalism is real and correctly cited; the
original card's specific PN-order assignment was an unjustified extrapolation from
it, now corrected

## 10. Symmetry-first route — derive the aggregation rule from FRW homogeneity/isotropy
Type: established_method
Evidence: inference
Core mechanism: instead of guessing how to aggregate the pairwise force into a
continuum source (Gap 2), impose the requirement that the aggregate result be
compatible with FRW symmetry at large scale as a constraint — only isotropic
aggregates of an odd-parity (dipole) term survive averaging over random orientations
in the first place.
Why it may work: symmetry constraints can partially fix the allowed functional forms
of the aggregation rule without needing the full microphysics first.
Required assumptions: the isomer-pair orientation distribution is close to random at
cosmological scale (no large-scale preferred direction).
Main obstacle: this only constrains the form of the aggregate, not its
normalization — still needs items 6/7 (or similar) to fix the coefficient.
Cheapest test: check whether a naive orientation-averaged dipole term vanishes
identically at leading order (a well-known result for randomly-oriented dipoles).
Falsifier: if the leading-order average genuinely vanishes and no subleading term is
identified, the dipole's claimed low-z cosmological role (item #9 of the 36-point
preprint) has no leading-order mechanism at all.
Expected output: an explicit statement of whether the leading-order dipole average
vanishes, and if so, the identified subleading term (if any) that would need to carry
the effect instead.
Scores:
  relevance: 9
  feasibility: 7
  novelty: 6
  expected_impact: 8
  evidence_strength: 5
  confidence: 0.55
Source: standard cosmological-perturbation-theory symmetry arguments (Weinberg,
Cosmology, 2008, ch. 5)

## 11. N-body simulation with the exact pair-force (skip analytic derivation)
Type: computational_experiment
Evidence: hypothesis
Core mechanism: implement `F_oP` directly as the pair-interaction kernel in a
modified N-body/RAMSES-style code (precedent: dipolar-DM RAMSES simulations already
exist, arXiv:2209.07831) and measure the emergent large-scale expansion numerically,
instead of deriving it analytically.
Why it may work: sidesteps Gaps 1-3 entirely by measuring the emergent behavior
directly, at the cost of not producing a closed-form theory.
Required assumptions: the existing dipolar-DM RAMSES code's kernel can be swapped for
`F_oP` without a full rewrite.
Main obstacle: substantial compute/engineering cost; existing project resources
(this session's Python/numpy pipeline) are not an N-body code. **Caveat added
2026-07-17:** standard cosmological N-body codes take a background `H(a)` as INPUT
(to set the expanding comoving grid) and simulate structure formation ON TOP of it —
they do not, by themselves, output an independent background expansion history. This
item tests whether `F_oP` reproduces realistic STRUCTURE given a fixed background,
not whether it PRODUCES a background `H(z)`; for the latter, item 53's approach
(deriving the background equation directly) is the more direct route, and this item
should be understood as complementary to it, not a substitute.
Cheapest test: check whether the existing dipolar-DM RAMSES code is public and could
be re-purposed with `F_oP`'s exact kernel swapped in, rather than writing a new
N-body code from scratch.
Falsifier: if reproducing even the toy (non-cosmological) N-body result takes more
compute than reasonably available, deprioritize.
Expected output: a feasibility note on reusing the existing RAMSES code, and if
feasible, an emergent `H(z)`-like curve from a toy run.
Scores:
  relevance: 8
  feasibility: 3
  novelty: 5
  expected_impact: 7
  evidence_strength: 6
  confidence: 0.4
Source: [Dipolar DM RAMSES simulations, arXiv:2209.07831](https://arxiv.org/pdf/2209.07831)

## 12. Kaluza-Klein reduction from a 6-isomer internal space
Type: new_hypothesis
Evidence: hypothesis
Core mechanism: the postulate of exactly 6 IDM isomers is suggestive of a compact
internal space; standard Kaluza-Klein-type dimensional reduction of a
higher-dimensional gravity theory over such a space can generate an effective 4D
multipole force structure purely from geometry, with the reduced Friedmann equations
giving `H(z)` directly.
Why it may work: if the isomer structure IS geometric, this would make the
dipole/quadrupole terms derived rather than postulated, closing Gap 1 and Gap 2
simultaneously.
Required assumptions: the preprint's isomer count has a real geometric/group-theoretic
basis, not just a particle-physics multiplicity.
Main obstacle: highly speculative without any stated internal-space metric in the
preprint; risks inventing structure not actually implied by "6 isomers."
Cheapest test: check whether the preprint's isomer structure has any stated
group-theoretic or geometric relationship before assuming a KK interpretation is
intended at all (this is item 44, run first).
Falsifier: no such structure stated or implied anywhere in the source material —
this becomes purely OUR speculation, not a reading of TJB's framework.
Expected output: either a candidate internal-space metric (if item 44 finds
supporting structure) or a documented closure of this route.
Scores:
  relevance: 5
  feasibility: 2
  novelty: 8
  expected_impact: 6
  evidence_strength: 2
  confidence: 0.15
Source: standard Kaluza-Klein reduction (foundational technique, no specific paper)

## 13. Effective equation-of-state fitting via first-order perturbation matching, generalized
Type: extension
Evidence: hypothesis
Core mechanism: Blanchet & Le Tiec's own key technical result (item 1's source) is
that their dipolar fluid's first-order cosmological perturbations are
indistinguishable from standard LambdaCDM. Generalize their exact calculation to
MULTING's dipole+quadrupole (they only have a dipole) and check whether the same
indistinguishability holds.
Why it may work: if the same degeneracy holds with a quadrupole added, it would
explain WHY the current implementation can't beat monopole+LambdaCDM as a structural
degeneracy rather than an implementation artifact — extending `NR-013`'s finding to a
possible root cause, the highest-impact single result in this document if it succeeds.
Required assumptions: Blanchet & Le Tiec's perturbation-matching argument's
assumptions (weak clusterization, first-order only) are applicable to MULTING's case.
Main obstacle: requires redoing their perturbation calculation with an added
quadrupole term — real, nontrivial GR perturbation theory work, not a quick check.
Cheapest test: read their published first-order matching argument closely enough to
state precisely which assumption (dipole-only vs dipole+quadrupole) it depends on,
before committing to redoing the full calculation.
Falsifier: if their degeneracy argument depends on dipole-only structure and breaks
once a quadrupole is added, this predicts MULTING's quadrupole term SHOULD be
cosmologically distinguishable from LambdaCDM — testable against `NR-013`'s own data.
Expected output: a scoped statement of whether the quadrupole breaks the
dipole-only degeneracy, and if so, a testable prediction to check against NR-013's
existing dataset.
Scores:
  relevance: 9
  feasibility: 5
  novelty: 7
  expected_impact: 9
  evidence_strength: 7
  confidence: 0.5
Sources: same as item 1

## 14. Check whether the bridge problem is already closed by the field's own no-go literature
Type: no_go
Evidence: unknown
Core mechanism: before building anything, search specifically for published no-go
theorems on "odd-parity (dipole) modifications to gravity at cosmological scale" —
if a general theorem already forbids a cosmologically-relevant dipole term under
reasonable assumptions, that would explain NR-013's empirical finding from first
principles rather than needing a new bridge at all.
Why it may work: if such a theorem exists, it turns an empirical dead end (NR-013)
into a principled, general, citable result.
Required assumptions: none beyond the literature actually existing and being
findable — this is a search task, not a derivation.
Main obstacle: no specific such theorem is known to us yet — this is a
literature-search task, not yet a result.
Cheapest test: search specifically for "dipole gravity no-go theorem cosmological
scale" and "odd parity gravitational force theorem" before assuming one exists or
doesn't.
Falsifier: search returns nothing relevant — then this item converts from "check a
known result" to "an open question," not resolved either way.
Expected output: either a citation to an existing no-go theorem, or an honest
`<unknown>` verdict recorded so this search is not repeated blindly later.
Scores:
  relevance: 8
  feasibility: 8
  novelty: 5
  expected_impact: 8
  evidence_strength: 3
  confidence: 0.35
Source: `<unknown>` — literature search not yet performed, flagged honestly per the
skill's anti-hallucination rule (do not cite a theorem we have not found)

### Block 2 — Cross-domain transfers (13)

## 15. Condensed-matter ferroelectric/paraelectric phase-transition analogy
Type: cross_domain_transfer
Evidence: hypothesis
Core mechanism: in ferroelectrics, a collection of microscopic dipoles transitions
from disordered (paraelectric, net moment zero) to ordered (ferroelectric, net moment
nonzero) as a control parameter crosses a critical value, governed by a Landau
free-energy expansion. Apply this to ask whether the cosmic-scale net dipole effect
turns on/off with a cosmological control parameter (density, z) rather than being
uniform.
Why it may work: directly explains item 10's finding (naive orientation averaging
kills the leading-order effect) by giving a mechanism for when ordering DOES occur.
Required assumptions: isomer-pair dipole alignment behaves approximately like a
thermodynamic order parameter as a function of local density.
Main obstacle: cosmological structure formation is not obviously analogous to a
thermodynamic phase transition in the required (near-equilibrium) sense.
Cheapest test: check whether a Landau-type order-parameter expansion, applied to
isomer-pair dipole alignment vs local density (using existing CCCP cluster density
data), predicts a density threshold above which the dipole should switch on.
Falsifier: no threshold-like behavior found in the resulting expansion; a smooth,
monotonic dependence instead would not support the phase-transition framing.
Expected output: a predicted density threshold (or its absence), testable against
R011's own cluster mass range.
Scores:
  relevance: 6
  feasibility: 5
  novelty: 7
  expected_impact: 5
  evidence_strength: 3
  confidence: 0.35
Source: standard Landau theory (textbook)

## 16. Control-theory system identification (treat the bridge as a transfer function)
Type: cross_domain_transfer
Evidence: hypothesis
Core mechanism: system identification techniques recover an unknown transfer
function from input-output data pairs without assuming a parametric form in advance —
structurally different from curve-fitting because it doesn't presuppose
`D=D0/(1+z)`.
Why it may work: it is a genuinely different mathematical operation (system recovery)
than the coefficient-fitting `NR-013` already closed, so it explores a different part
of the space in principle.
Required assumptions: the true bridge is approximately linear/time-invariant enough
for standard system-ID methods to apply.
Main obstacle: system identification assumes linearity/time-invariance a genuinely
nonlinear gravity bridge likely violates; risks recovering an overfit, physically
meaningless function — the same failure mode `NO_BRIDGE_FITTING` already flags as
dangerous for this project.
Cheapest test: check the recovered transfer function's degrees of freedom against
the `NO_BRIDGE_FITTING` rule's own DOF argument before trusting any result.
Falsifier: if the recovered function's DOF count matches or exceeds what
`NO_BRIDGE_FITTING` already flags as overfitting-prone, the result must be discarded
regardless of apparent fit quality.
Expected output: a DOF-audited transfer function, or documentation that the DOF
check failed and the route was abandoned per project rule.
Scores:
  relevance: 4
  feasibility: 6
  novelty: 6
  expected_impact: 3
  evidence_strength: 2
  confidence: 0.2
Source: standard system identification theory (Ljung, "System Identification:
Theory for the User")

## 17. Renormalization-group flow between cluster-scale and cosmological-scale physics
Type: cross_domain_transfer
Evidence: inference
Core mechanism: RG flow formalizes which microscopic couplings survive
coarse-graining to a larger scale and which are "irrelevant." Apply this to ask
whether the dipole/quadrupole coupling strength found at cluster scale (where
R011/NR-013's data lives) RG-flows to a different effective strength at cosmological
scale.
Why it may work: directly addresses Gap 2 by giving a principled answer for how
coupling strength changes with scale, rather than assuming scale-invariance (which
the current placeholder implicitly does).
Required assumptions: a well-defined field theory exists to compute beta functions
from — only fully computable once Gap 1 is solved, so this is qualitative-only at
present.
Main obstacle: RG flow requires a well-defined field theory to compute beta functions
from; without Gap 1 solved first, this is not directly computable, only qualitatively
suggestive.
Cheapest test: check whether the dipole term's mass dimension (from dimensional
analysis of `F_oP`'s stated formula) suggests relevant/irrelevant/marginal scaling in
the RG sense, without needing the full theory.
Falsifier: if the dipole term is RG-irrelevant by simple dimensional analysis, that
would explain (not just describe) why it's undetectable at cosmological scale,
strengthening NR-013's finding rather than opening a new route.
Expected output: a dimensional-analysis-based relevant/irrelevant/marginal
classification of the dipole and quadrupole terms.
Scores:
  relevance: 8
  feasibility: 5
  novelty: 7
  expected_impact: 7
  evidence_strength: 4
  confidence: 0.4
Source: standard RG / effective field theory reasoning (Georgi 1993, Ann. Rev.
Nucl. Part. Sci.)

## 18. Bayesian model comparison across candidate bridges (information theory lens)
Type: cross_domain_transfer
Evidence: fact
Core mechanism: once more than one candidate bridge from this document is actually
worked out to the point of producing a testable `H(z)`, use Bayesian evidence
(marginal likelihood) rather than raw chi-squared/Pearson-r comparison to rank them —
automatically penalizes extra free parameters.
Why it may work: it is the standard, correct tool for exactly the "which of several
candidate models" situation this document will eventually produce, and it avoids the
`NO_BRIDGE_FITTING` overfitting trap by construction.
Required assumptions: at least two candidate bridges have been developed to testable
form (not yet true at time of writing).
Main obstacle: nothing structural — the risk is applying it too early, before any
candidate bridge is developed enough to have a real likelihood to compute.
Cheapest test: not runnable yet; the cheap first step is simply noting this
requirement in the prototyping plan so it isn't forgotten once candidates exist.
Falsifier: not applicable — this is a meta-tool for comparing physical claims, not a
physical claim itself.
Expected output: a documented decision procedure ready to apply once >=2 candidates
exist, avoiding an ad hoc comparison later.
Scores:
  relevance: 6
  feasibility: 8
  novelty: 3
  expected_impact: 6
  evidence_strength: 8
  confidence: 0.7
Source: Trotta 2008, "Bayes in the sky," arXiv:0803.4089

## 19. AdS/CFT-inspired holographic dark-fluid equation of state
Type: cross_domain_transfer
Evidence: hypothesis
Core mechanism: holographic dark energy models derive an effective equation of state
from a horizon-entropy bound (similar spirit to Verlinde's item 5, but a distinct,
more mathematically developed formalism with existing cosmological-perturbation
results ready to reuse).
Why it may work: offers a second, independent non-Lagrangian route to `w(z)` with
more developed perturbation-theory machinery than Verlinde's original argument.
Required assumptions: the dipole and quadrupole terms can be mapped onto a single
effective `w(z)` without losing information that matters for the test.
Main obstacle: holographic dark energy models are built for a single effective
fluid, not explicitly for a multipole-structured force; adapting may lose real
information if two independent degrees of freedom are genuinely needed.
Cheapest test: check whether holographic dark energy's standard `w(z)` functional
form already resembles the phenomenological `eps(z)` two-hump shape this project
already found and characterized (`pearl_registry`, fsig8_robustness.py results).
Falsifier: no resemblance in functional form — holographic DE models are typically
smooth single-peaked or monotonic, not the two-component shape already found in this
project's own eps(z) analysis.
Expected output: a direct shape comparison (already-computed eps(z) vs standard
holographic w(z)), reusing existing project output at zero new-data cost.
Scores:
  relevance: 6
  feasibility: 6
  novelty: 4
  expected_impact: 5
  evidence_strength: 5
  confidence: 0.3
Source: Cohen, Kaplan, Nelson 1999, hep-th/9803132 (holographic dark energy,
foundational)

## 20. Historical precedent study: how Newton's force law became Friedmann's equations
Type: cross_domain_transfer
Evidence: fact
Core mechanism: the literal historical template for "turn a two-body force law into
a cosmology" — Newton's law leads to the Poisson equation (aggregation), then to
Einstein's field equations (relativistic completion), then to Friedmann's equations
(symmetry reduction). Walking through it explicitly as a checklist clarifies exactly
which of Gaps 1-3 is the actual current blocker for `F_oP`.
Why it may work: this is not a new derivation but a proven historical process,
usable immediately as a sequencing tool for every other item in this document.
Required assumptions: none — this is a documented historical fact, used here as a
methodology, not a physical claim about `F_oP` itself.
Main obstacle: nothing structural; the only risk is spending time on pedagogy
instead of new physics — this item's value is entirely in using it to sequence the
other 51 items.
Cheapest test: not applicable as a physical test; immediately "testable" by using it
to reorder this document's own Prototyping Plan section.
Falsifier: not applicable — a methodology tool, not a falsifiable physical claim.
Expected output: the Gap-1/2/3 sequencing table already used to build this
document's Prototyping Plan (see below) — this item's output already exists in this
document.
Scores:
  relevance: 9
  feasibility: 9
  novelty: 2
  expected_impact: 6
  evidence_strength: 9
  confidence: 0.85
Source: standard cosmology textbook derivation chain (Weinberg, Cosmology, ch. 1)

## 21. Machine-learning symbolic regression on N-body output (discovery tool, not fit)
Type: cross_domain_transfer
Evidence: hypothesis
Core mechanism: if item 11's N-body simulation is run, symbolic regression can
suggest candidate closed-form functions relating simulation inputs to emergent
`H(z)`-like output, narrowing the search space of analytic bridges to try deriving
properly.
Why it may work: modern symbolic-regression tools (e.g. AI Feynman-style) are
already established for exactly this "suggest a closed form from data" role in
physics discovery pipelines.
Required assumptions: item 11 has been run and produced usable simulation output;
this item does nothing standalone.
Main obstacle: entirely dependent on item 11 being run first; there is no
independent path to this item's output.
Cheapest test: not runnable until item 11 produces output — recorded here as a
planned downstream step, not an independent action.
Falsifier: not applicable while dependent on item 11; once run, falsifiable by
whether any suggested closed form survives independent re-derivation.
Expected output: a shortlist of candidate closed-form functions, each requiring
independent derivation before being trusted (respects `NO_BRIDGE_FITTING`'s spirit —
ML output is a hypothesis generator, never the final answer).
Scores:
  relevance: 5
  feasibility: 3
  novelty: 6
  expected_impact: 5
  evidence_strength: 3
  confidence: 0.3
Source: Udrescu & Tegmark 2020, "AI Feynman," arXiv:1905.11481

## 22. Fluid-dynamics vorticity analogy for the dipole term
Type: cross_domain_transfer
Evidence: hypothesis
Core mechanism: treat the dipole term as a vorticity-like (odd-parity,
momentum-density) source in a cosmological fluid, borrowing the standard
scalar/vector/tensor (SVT) perturbation classification (Kodama & Sasaki 1984) — a
dipole force is naturally vector-type, not scalar-type, perturbation.
Why it may work: SVT decomposition is the standard, already-correct framework for
classifying exactly this kind of odd-parity source in cosmological perturbation
theory, and using it may explain why a scalar-type treatment (implicit in the current
`H(z)`-only bridge) misses the dipole's real effect.
Required assumptions: the dipole term is genuinely vector-type under SVT
classification, not accidentally scalar.
Main obstacle: vector perturbations decay in an expanding universe absent a
sustained source, so this route needs the dipole to be continuously sourced, not just
present initially.
Cheapest test: classify `F_oP`'s dipole term under SVT decomposition and check its
predicted decay rate against whether the claimed low-z effect (preprint item #9)
could survive to the present epoch.
Falsifier: predicted decay rate is too fast for the effect to survive to low z at any
reasonable initial amplitude.
Expected output: the SVT classification and decay-rate estimate for the dipole term.
Scores:
  relevance: 7
  feasibility: 6
  novelty: 5
  expected_impact: 6
  evidence_strength: 5
  confidence: 0.4
Source: standard SVT decomposition (Kodama & Sasaki 1984, textbook-standard)

## 23. Acoustic/plasma-physics two-fluid instability analogy
Type: cross_domain_transfer
Evidence: hypothesis
Core mechanism: treat ordinary matter plus the isomer dark sector as a two-fluid
plasma-like system; check whether known two-fluid instability criteria (Jeans-type)
predict a scale-dependent dipole/quadrupole visibility threshold.
Why it may work: could explain why cluster-scale tests (R011) see no effect while a
different (e.g. galactic) scale might, via a genuine physical scale-selection
mechanism rather than an ad hoc coefficient choice.
Required assumptions: the isomer sector behaves enough like a distinct fluid
component for two-fluid instability analysis to apply.
Main obstacle: two-fluid instability criteria are usually derived for
electromagnetically-coupled plasmas; the gravitational-only coupling case is less
standard and may not transfer cleanly.
Cheapest test: apply the standard two-fluid Jeans criterion with `F_oP`'s dipole
term as the inter-fluid coupling and check for a predicted critical scale.
Falsifier: no critical scale emerges, or the predicted scale is far from both cluster
and galactic scales, making the mechanism cosmologically irrelevant either way.
Expected output: a predicted critical scale (or its absence) for dipole visibility.
Scores:
  relevance: 6
  feasibility: 5
  novelty: 6
  expected_impact: 5
  evidence_strength: 3
  confidence: 0.3
Source: standard two-fluid plasma cosmology (textbook technique)

## 24. Optics/wave-scattering multipole-expansion formalism reused directly
Type: extension
Evidence: fact
Core mechanism: `F_oP` is already explicitly a multipole expansion
(monopole/dipole/quadrupole) — reuse the full formal machinery of
electromagnetic/acoustic multipole radiation theory, including known
cross-term/interference results between multipole orders, which the current
implementation (independent `beta_d`, `beta_q` with no cross term) may be missing.
Why it may work: this is not a loose analogy but a literal reuse of the same
mathematical object (multipole expansion) with a mature, well-developed formalism
already available.
Required assumptions: cross-terms between the dipole and quadrupole orders, absent
from the current implementation, are not negligible.
Main obstacle: EM multipole radiation theory is derived for wave propagation, not a
static/quasi-static gravitational potential — the analogy needs a static-limit
adaptation, not a direct import.
Cheapest test: derive the static-limit cross-term between `F_oP`'s dipole and
quadrupole pieces using standard multipole formalism and check its magnitude against
the individually-fitted terms already in `R011`'s data.
Falsifier: the cross-term is negligible compared to the individual terms already
tested, meaning the current implementation's omission doesn't matter.
Expected output: the magnitude of the dipole-quadrupole cross-term relative to the
individual terms already fit in this project.
Scores:
  relevance: 7
  feasibility: 6
  novelty: 5
  expected_impact: 6
  evidence_strength: 6
  confidence: 0.45
Source: standard multipole radiation theory (Jackson, Classical Electrodynamics,
ch. 9)

## 25. Network/graph-theory coarse-graining of the pairwise force
Type: cross_domain_transfer
Evidence: unknown
Core mechanism: treat the cluster galaxy distribution as a graph with
`F_oP`-weighted edges; use graph-Laplacian coarse-graining (spectral graph theory) as
an alternative aggregation rule to the naive continuum limit (item 6), potentially
capturing discreteness effects the continuum approximation misses at cluster scale.
Why it may work: spectral graph methods are specifically designed to capture
discrete-structure effects that continuum approximations smooth over, which is
exactly the concern flagged in item 6's own obstacle.
Required assumptions: the cluster distribution's discreteness is a significant
enough effect at the scales tested to matter for the aggregation rule.
Main obstacle: no prior application of this specific technique to cosmological
force aggregation is known to us — genuinely exploratory, not an established
transfer.
Cheapest test: build the graph-Laplacian aggregation on the already-available CCCP
cluster catalog and compare its predicted aggregate to the naive continuum limit's
prediction on the same data.
Falsifier: the graph-based and continuum aggregates agree closely, meaning
discreteness effects are negligible and this route adds nothing beyond item 6.
Expected output: a numeric comparison of graph-based vs continuum-limit aggregation
on the same real cluster data.
Scores:
  relevance: 5
  feasibility: 5
  novelty: 7
  expected_impact: 4
  evidence_strength: 2
  confidence: 0.25
Source: `<unknown>` — spectral graph theory is standard, but its cosmological
application here is not sourced to a specific prior paper; flagged honestly.

## 26. Epidemiology-style pairwise-interaction-to-population-rate transfer
Type: cross_domain_transfer
Evidence: hypothesis
Core mechanism: the general mathematical problem "aggregate a pairwise interaction
kernel into a population-level rate equation" is solved routinely in epidemiological
compartment modeling (SIR-type models derived from pairwise contact kernels) — a
mature, well-tested aggregation technique from a genuinely different field.
Why it may work: epidemiology has decades of practical experience turning pairwise
kernels into population equations under weaker assumptions than physics typically
requires, which may offer a more robust aggregation route for Gap 2.
Required assumptions: the isomer-pair interaction kernel can be cast in a form
structurally similar to a contact-rate kernel.
Main obstacle: epidemiological aggregation techniques assume discrete
individuals transitioning between states, not a continuous force field — the mapping
to a force law is not immediate.
Cheapest test: attempt to recast `F_oP`'s pairwise structure in Kermack-McKendrick
form and check whether the resulting rate equation resembles a Friedmann-like
equation at all.
Falsifier: the recast form bears no resemblance to any cosmologically meaningful
equation, closing this route quickly.
Expected output: a documented attempt at the recast, with a pass/fail verdict.
Scores:
  relevance: 6
  feasibility: 6
  novelty: 8
  expected_impact: 5
  evidence_strength: 3
  confidence: 0.3
Source: standard mathematical epidemiology (Kermack-McKendrick aggregation
technique, textbook)

## 27. Financial-mathematics mean-field game formalism for the isomer sector
Type: cross_domain_transfer
Evidence: unknown
Core mechanism: mean-field game theory, developed for large populations of
interacting agents in economics/finance, provides a formal N-to-infinity limit
procedure structurally similar to what is needed for Gap 2's aggregation problem.
Why it may work: if a physics adaptation of mean-field games already exists
elsewhere, it could be imported; the underlying N-to-infinity limit mathematics is
genuinely relevant to the aggregation problem in the abstract.
Required assumptions: an existing physics adaptation of mean-field game theory can
be found and is applicable to a gravitational (not economic) interaction kernel.
Main obstacle: no direct cosmology or gravity application of mean-field games is
known to us; unlikely to be directly applicable without substantial adaptation work.
Cheapest test: a literature search for "mean-field games gravity" or "mean-field
games cosmology" before investing further.
Falsifier: no relevant literature found and no direct adaptation path identified.
Expected output: a documented literature-search result, closing or opening this
route based on what is actually found.
Scores:
  relevance: 4
  feasibility: 3
  novelty: 7
  expected_impact: 3
  evidence_strength: 1
  confidence: 0.15
Source: `<unknown>` — no direct cosmology application found; flagged honestly rather
than invented, weakest cross-domain item in this document, kept for completeness per
the skill's own "no_go documentation is valuable too" principle.

### Block 3 — Hybrid combinations (7)

## 28. Blanchet-Le Tiec action plus Kaluza-Klein quadrupole extension
Type: hybrid
Evidence: hypothesis
Core mechanism: use the proven dipolar-fluid action (item 1) as the base, solving
the dipole term properly, and add a KK-derived quadrupole (item 12) sourced by a
second internal-space mode, instead of inventing the quadrupole term from scratch.
Why it may work: combines a well-supported dipole route with the only candidate
mechanism surveyed here that could make the quadrupole term geometric rather than
postulated.
Required assumptions: both item 1's adaptation and item 12's geometric-isomer
premise hold simultaneously.
Main obstacle: inherits item 12's speculative internal-space assumption on top of
item 1's adaptation difficulty — compounds two open questions rather than resolving
one.
Cheapest test: run item 1's test first; only proceed to the KK extension if item 1
succeeds and item 44 (checking whether "6 isomers is geometric" is even a reasonable
reading) also passes.
Falsifier: item 1's falsifier, inherited; additionally falsified if item 44 fails.
Expected output: a combined dipole+quadrupole action, contingent on both
prerequisite items succeeding.
Scores:
  relevance: 7
  feasibility: 3
  novelty: 6
  expected_impact: 7
  evidence_strength: 3
  confidence: 0.25
Sources: same as items 1 and 12

## 29. EFT-DE parametrization plus Bayesian model comparison pipeline
Type: hybrid
Evidence: hypothesis
Core mechanism: use EFT-DE (item 3) to generate several candidate background
evolutions, varying which of the 3 EFT functions absorb the dipole/quadrupole
structure, then use Bayesian evidence (item 18) rather than chi-squared to rank them
against real `H(z)` data.
Why it may work: directly reuses this project's existing verification pipeline with
a principled comparison metric instead of raw Pearson r, avoiding the
overfitting-prone comparison method `NO_BRIDGE_FITTING` warns against.
Required assumptions: item 3 produces at least two genuinely distinct candidate
parametrizations to compare.
Main obstacle: needs item 3 to actually produce two or more distinct candidates
first; not runnable standalone.
Cheapest test: implementable now with the existing `src/pearson_fit.py`-style
tooling once item 3's EFT functions are specified — the most shovel-ready hybrid in
this document.
Falsifier: if EFT-DE genuinely cannot represent the dipole/quadrupole structure at
all (item 3's own falsifier), this hybrid is moot.
Expected output: a Bayesian-evidence ranking of EFT-DE candidate parametrizations
against real H(z) data.
Scores:
  relevance: 8
  feasibility: 6
  novelty: 5
  expected_impact: 7
  evidence_strength: 6
  confidence: 0.5
Sources: same as items 3 and 18

## 30. PN order-counting plus symmetry-first aggregation (elimination pipeline)
Type: hybrid
Evidence: inference
Core mechanism: run the PN-order classification (item 9) first, then apply the FRW
symmetry constraint (item 10) only to the PN-consistent candidates — a cheap,
purely-analytic filtering pipeline that could rule out most of Blocks 1-2 before any
of them needs real computation.
Why it may work: both components are individually cheap and non-computational, so
the combination inherits no new obstacles while compounding their filtering power.
Required assumptions: none beyond items 9 and 10's individual assumptions.
Main obstacle: none new — genuinely low-risk as a combination.
Cheapest test: this pipeline IS the cheap test; a day or two of careful algebra, no
data needed.
Falsifier: not applicable — a filtering tool, not a physical claim to falsify.
Expected output: a filtered shortlist of Blocks 1-2 candidates that survive both the
PN-order and symmetry constraints, ready for the Month-1 prototyping stage.
Scores:
  relevance: 9
  feasibility: 8
  novelty: 5
  expected_impact: 7
  evidence_strength: 5
  confidence: 0.55
Sources: same as items 9 and 10

## 31. N-body plus symbolic regression as a single discovery pipeline
Type: hybrid
Evidence: hypothesis
Core mechanism: explicitly sequence item 11 (N-body simulation) and item 21
(symbolic regression on its output) as one combined workstream with a shared cost
estimate, rather than two separately-scoped items.
Why it may work: formalizing the sequence avoids double-counting cost/risk and makes
the combined workstream's go/no-go decision explicit at a single point (after item
11's feasibility check).
Required assumptions: same as items 11 and 21 combined.
Main obstacle: inherits item 11's compute/engineering cost as the binding
constraint for the whole pipeline.
Cheapest test: same as item 11's cheapest test — check RAMSES code reuse feasibility
first, since that gates the entire combined pipeline.
Falsifier: item 11's falsifier, inherited.
Expected output: a single combined go/no-go decision and cost estimate for the
N-body-to-symbolic-regression pipeline.
Scores:
  relevance: 6
  feasibility: 3
  novelty: 5
  expected_impact: 6
  evidence_strength: 4
  confidence: 0.3
Sources: same as items 11 and 21

## 32. Condensed-matter phase-transition analogy plus RG flow
Type: hybrid
Evidence: hypothesis
Core mechanism: combine item 15 (phase-transition analogy) and item 17 (RG flow)
into one "scale-dependent dipole visibility" investigation, since both concern how a
microscopic dipole property changes with an external scale/control parameter.
Why it may work: the two lenses are asking closely related questions (when does the
dipole effect turn on/off) from complementary formal directions (thermodynamic vs
field-theoretic), and combining them may triangulate a more robust answer than
either alone.
Required assumptions: same as items 15 and 17 combined.
Main obstacle: item 17's dependence on Gap 1 being solved first limits how far the
combination can go before other items are resolved.
Cheapest test: run item 15's density-threshold check and item 17's dimensional
RG-scaling check independently, then compare whether they predict compatible or
contradictory scale-dependence.
Falsifier: the two lenses predict qualitatively incompatible scale-dependence (e.g.
one predicts a sharp threshold, the other predicts smooth irrelevance), indicating
at least one framing is wrong.
Expected output: a compatibility check between the two lenses' independent
predictions.
Scores:
  relevance: 7
  feasibility: 5
  novelty: 6
  expected_impact: 6
  evidence_strength: 4
  confidence: 0.35
Sources: same as items 15 and 17

## 33. Historical precedent scaffold applied to sequence items 1-14
Type: hybrid
Evidence: fact
Core mechanism: a meta-application of item 20 (the Newton-to-Friedmann template),
formally producing the "which Gap does each item close" table used directly in this
document's own Prototyping Plan.
Why it may work: it is not a new idea but an explicit, disciplined use of an
already-validated methodology (item 20) to organize the rest of the document, which
is exactly what prevents "derive the bridge" from being treated as one undifferentiated
hard problem.
Required assumptions: none — this is an organizational application, not a physical
claim.
Main obstacle: none — the only risk is skipping this step and proceeding
unsequenced, which item 20 already warns against.
Cheapest test: not applicable as a physical test; its output is directly the
Prototyping Plan section of this document, already produced.
Falsifier: not applicable — a methodology application, not a falsifiable claim.
Expected output: the Gap-sequencing table (already delivered in this document's
Prototyping Plan section below).
Scores:
  relevance: 8
  feasibility: 9
  novelty: 2
  expected_impact: 7
  evidence_strength: 8
  confidence: 0.75
Sources: same as item 20

## 34. Blanchet bispectrum-constraint check plus TeVeS structural comparison
Type: hybrid
Evidence: hypothesis
Core mechanism: **corrected 2026-07-17** — item 2 is no longer a standalone "PPN
bound," it is now gated on item 1's DDM mapping (see item 2's own correction). This
hybrid combines item 2 (in its corrected, item-1-dependent form) and item 4 (TeVeS
structural comparison) into one literature-consistency pass, since both check
against an existing constraint/theory before building something new.
Why it may work: running both checks together is still more efficient than
sequentially, once item 2's real prerequisite (item 1) is acknowledged.
Required assumptions: same as items 2 and 4 combined, INCLUDING item 2's now-explicit
dependency on item 1 succeeding first.
Main obstacle: item 2's corrected scope means this hybrid is no longer two
independent low-risk checks — it inherits item 1's adaptation risk through item 2.
Cheapest test: perform item 4's TeVeS term-matching first (independent of item 1);
only attempt item 2's bispectrum-constraint transfer if item 1 succeeds.
Falsifier: combination of items 2 (as corrected) and 4's individual falsifiers.
Expected output: item 4's result standalone, plus item 2's result only if item 1's
prerequisite is met.
Scores:
  relevance: 8
  feasibility: 7
  novelty: 3
  expected_impact: 6
  evidence_strength: 6
  confidence: 0.55
Sources: same as items 2 and 4

### Block 4 — Computational/experimental tests (6)

## 35. Reuse NR-013's own pipeline to test EFT-DE-derived H(z) shapes
Type: computational_experiment
Evidence: fact
Core mechanism: directly reuse
`experiments/20260713-r011-beta-profile-nesting/artifacts/verify_r011_beta_profile.py`'s
structure — swap the phenomenological `D=D0/(1+z)` for an EFT-DE-derived `H(z;
theta)` and rerun the same nesting-inequality/profile-vs-monopole test that closed
NR-013, now against a genuinely different bridge instead of a different coefficient
choice.
Why it may work: the test infrastructure, data, and validity checks already exist
and are proven in this repo — this is the single most "shovel-ready" item in the
entire document.
Required assumptions: item 3 (EFT-DE) has produced an explicit, evaluable `H(z;
theta)` to plug in.
Main obstacle: entirely gated on item 3's output existing first.
Cheapest test: this literally is the cheap test — the infrastructure already exists
in this repo, only the input function needs to change.
Falsifier: same criterion as NR-013 — does any configuration beat `Q(0,0)=0.7334`?
Expected output: a REJECTED/PROMOTE verdict for the EFT-DE bridge, in the exact same
format as NR-013, directly comparable to it.
Scores:
  relevance: 9
  feasibility: 8
  novelty: 4
  expected_impact: 8
  evidence_strength: 7
  confidence: 0.6
Sources: this project's own `experiments/20260713-r011-beta-profile-nesting/`

## 36. Same pipeline, TeVeS-derived H(z)
Type: computational_experiment
Evidence: hypothesis
Core mechanism: same test infrastructure as item 35, applied to whatever `H(z; theta)`
item 4's TeVeS-structure comparison eventually produces.
Why it may work: same infrastructure-reuse advantage as item 35.
Required assumptions: item 4 has produced an explicit, evaluable `H(z; theta)`.
Main obstacle: entirely gated on item 4's output existing first, and item 4 is
lower-confidence than item 3.
Cheapest test: identical mechanics to item 35, once item 4's output exists.
Falsifier: same criterion as NR-013.
Expected output: a REJECTED/PROMOTE verdict for the TeVeS-structured bridge.
Scores:
  relevance: 8
  feasibility: 5
  novelty: 4
  expected_impact: 7
  evidence_strength: 5
  confidence: 0.4
Sources: same as item 4, applied via item 35's pipeline

## 37. Same pipeline, kinetic-theory-derived H(z)
Type: computational_experiment
Evidence: hypothesis
Core mechanism: same test infrastructure as item 35, applied to whatever `H(z;
theta)` item 7's Boltzmann-equation route eventually produces.
Why it may work: same infrastructure-reuse advantage as item 35, and item 7 has the
highest expected_impact among Block 1's non-established-fact items due to the
shared-machinery link to bottleneck #8/9.
Required assumptions: item 7 has produced an explicit, evaluable `H(z; theta)`.
Main obstacle: entirely gated on item 7's output, which itself requires the
thermal-history closure item 7 flags as its own main obstacle.
Cheapest test: identical mechanics to item 35, once item 7's output exists.
Falsifier: same criterion as NR-013.
Expected output: a REJECTED/PROMOTE verdict for the kinetic-theory bridge.
Scores:
  relevance: 9
  feasibility: 4
  novelty: 5
  expected_impact: 8
  evidence_strength: 5
  confidence: 0.4
Sources: same as item 7, applied via item 35's pipeline

## 38. Enforce held-out validation discipline on any future bridge test
Type: computational_experiment
Evidence: fact
Core mechanism: whatever bridge is eventually tested, apply this project's own
train/holdout discipline (already used in `NR-013`, grouped by unique `cluster_id`)
rather than a single in-sample fit.
Why it may work: it is a process requirement, not a new physical idea, but one this
project has already demonstrated matters — cheap to enforce and prevents a known
failure mode.
Required assumptions: none — directly reuses an already-validated protocol from
`NR-013`.
Main obstacle: easy to forget under the excitement of a new bridge candidate; the
main risk is procedural, not technical.
Cheapest test: not a test itself — a checklist item enforced whenever any of items
35-37 (or any future bridge test) is run.
Falsifier: not applicable — a process requirement, not a falsifiable physical claim.
Expected output: a standing checklist entry referenced by every future bridge test
in this project.
Scores:
  relevance: 8
  feasibility: 9
  novelty: 1
  expected_impact: 6
  evidence_strength: 8
  confidence: 0.8
Sources: this project's own `NR-013` methodology

## 39. Independent dataset cross-check against the DESI DR1 pipeline
Type: computational_experiment
Evidence: fact
Core mechanism: whatever bridge passes CCCP-cluster testing, additionally check it
against the DESI DR1 f-sigma8 pipeline already built this session
(`pearl_registry`, fsig8_robustness.py) — a second, independent real dataset already
wired into this project.
Why it may work: independent-dataset confirmation is a stronger evidence standard
than single-dataset testing, and the second pipeline already exists at zero
additional engineering cost.
Required assumptions: the candidate bridge's `H(z; theta)` can be evaluated against
f-sigma8 observables, not just `H(z)` directly — may need an additional derivation
step (growth-rate prediction) not automatically implied by an `H(z)` bridge alone.
Main obstacle: growth-rate (f-sigma8) predictions require more than just `H(z)` —
the bridge needs to also specify how structure growth is affected, an additional
piece beyond what items 1-14 directly provide.
Cheapest test: check whether any surviving candidate bridge (post items 35-37)
already implies a growth-rate prediction, or would need a separate derivation step
first.
Falsifier: no surviving candidate produces any growth-rate prediction at all,
meaning this cross-check cannot be run without additional theoretical work first.
Expected output: a documented growth-rate prediction (or its absence) for each
surviving candidate, and if present, its DESI DR1 f-sigma8 test result.
Scores:
  relevance: 8
  feasibility: 7
  novelty: 2
  expected_impact: 7
  evidence_strength: 7
  confidence: 0.55
Sources: this project's own `pearl_registry`, fsig8_robustness.py

## 40. Toy 2-body simulation before full N-body
Type: computational_experiment
Evidence: hypothesis
Core mechanism: before item 11's full N-body run, simulate just two interacting
bodies under `F_oP` and verify energy/momentum conservation numerically — a
near-zero-cost sanity check.
Why it may work: catches basic implementation or formula-consistency errors before
any larger compute investment, at negligible cost.
Required assumptions: `F_oP`'s formula is precise enough (all terms, signs, and
units specified) to implement directly in a toy simulation.
Main obstacle: none significant — this is deliberately the cheapest possible
computational step in the whole document.
Cheapest test: this item IS the cheap test; implement a 2-body simulation with
`F_oP` and check energy/momentum conservation to machine precision.
Falsifier: energy/momentum are not conserved to numerical precision, indicating an
error in the force law's implementation (not necessarily in `F_oP` itself) that must
be fixed before any larger simulation is trusted.
Expected output: a pass/fail conservation check, a prerequisite gate for item 11.
Scores:
  relevance: 6
  feasibility: 9
  novelty: 2
  expected_impact: 4
  evidence_strength: 6
  confidence: 0.7
Sources: standard numerical-integration sanity check (no specific paper needed)

### Block 5 — No-go / falsification-first approaches (5)

## 41. Explicitly attempt to prove a no-go theorem for cosmologically-relevant dipole terms
Type: no_go
Evidence: hypothesis
Core mechanism: rather than only searching for existing literature (item 14),
attempt to derive from scratch whether any odd-parity two-body force, under
reasonable assumptions (locality, Lorentz invariance of the underlying mechanism as
the preprint itself claims), can survive orientation-averaging at cosmological
scale — turning item 10's empirical observation into a proven, general statement.
Why it may work: a self-derived proof, even a narrow one, would be a genuinely new
and citable result regardless of what the literature search (item 14) finds.
Required assumptions: locality and Lorentz invariance of the underlying mechanism,
as already claimed by the preprint itself.
Main obstacle: proving a general no-go theorem is genuinely hard research
mathematics, not a quick check — real risk of spending significant effort without a
clean result.
Cheapest test: attempt the proof for the simplest possible case (pure dipole, no
quadrupole) first; if it succeeds trivially, extend; if it fails, that itself is
informative.
Falsifier: finding even one physically reasonable counter-example construction.
Expected output: either a proof sketch for the simplest case, or a documented
counter-example that blocks the general theorem.
Scores:
  relevance: 8
  feasibility: 4
  novelty: 7
  expected_impact: 8
  evidence_strength: 3
  confidence: 0.35
Sources: builds on item 10's finding, no additional external source

## 42. Adversarial minimal counter-model (existence-proof check)
Type: no_go
Evidence: hypothesis
Core mechanism: construct the simplest possible toy universe (2-3 clusters,
analytic not numerical) where `F_oP`'s dipole term demonstrably does produce a
detectable cosmological signature, to establish an existence proof that the
mechanism isn't impossible in principle.
Why it may work: it is the inverse of item 41, useful for bracketing the true
difficulty — if even a maximally favorable toy case fails to show a detectable
signature, that is itself informative independent of item 41's general proof
attempt.
Required assumptions: a toy universe can be constructed simply enough to solve
analytically while still containing the essential dipole physics.
Main obstacle: a toy model favorable enough to show a signature may be
unrepresentative of the real cosmological setting, limiting how much the result
generalizes.
Cheapest test: construct the 2-3 cluster toy case and solve for the dipole's
cosmological signature analytically.
Falsifier: even the most favorable toy construction shows no detectable signature,
which would be strong (though not conclusive) evidence against the whole mechanism.
Expected output: an existence-proof toy calculation, bracketing the difficulty
range together with item 41.
Scores:
  relevance: 7
  feasibility: 6
  novelty: 5
  expected_impact: 6
  evidence_strength: 4
  confidence: 0.4
Sources: builds on item 10's finding, no additional external source

## 43. Scope-check: is NR-013 already partial evidence for bottleneck #1 generally?
Type: no_go
Evidence: fact
Core mechanism: NR-013 shows no coefficient choice within the CURRENT bridge works;
explicitly write up whether this constitutes partial evidence against ANY bridge
(a strong claim, likely too strong) versus only against coefficient-tuning within one
specific placeholder (the actual, narrower, already-registered scope).
Why it may work: this is a documentation/scoping task, not new physics — cheap,
fast, and directly prevents this document's own findings from later being
misrepresented as stronger than they are.
Required assumptions: none — a scoping exercise on an already-completed result.
Main obstacle: none significant — the only risk is getting the scope statement
itself wrong, which is why it is written up explicitly rather than left implicit.
Cheapest test: not applicable as an external test; the output IS the test — a
written scope statement checked against NR-013's actual claim.
Falsifier: not applicable — a documentation task, not a falsifiable physical claim.
Expected output: an explicit scope statement (already partially present in this
document's Negative Results section) distinguishing "no coefficient works in this
placeholder" from "no bridge could ever work."
Scores:
  relevance: 8
  feasibility: 9
  novelty: 1
  expected_impact: 6
  evidence_strength: 8
  confidence: 0.8
Sources: this project's own `NR-013`

## 44. Falsify the "6 isomers is geometric" reading directly
Type: no_go
Evidence: unknown
Core mechanism: search the actual preprint text for any stated symmetry group or
geometric motivation for the isomer count, rather than assuming one — kills item 12
quickly if it fails.
Why it may work: this is the cheapest possible check that gates an entire
speculative branch (items 12 and 28) before any further investment in them.
Required assumptions: none — a direct text-search task against the source material
already available to this project.
Main obstacle: none significant — a fast, low-risk check.
Cheapest test: this item IS the cheap test — grep/read the preprint text for any
stated symmetry-group or geometric justification of the 6-isomer count.
Falsifier: finding an explicit statement in the preprint would falsify the "purely
our speculation" framing and instead confirm a real basis worth pursuing.
Expected output: a documented yes/no verdict on whether the preprint itself
motivates a geometric reading of the isomer count, gating items 12 and 28.
Scores:
  relevance: 6
  feasibility: 9
  novelty: 2
  expected_impact: 4
  evidence_strength: 6
  confidence: 0.65
Sources: the project's own source material (preprint text)

## 45. Sign-convention consistency check across surviving candidates
Type: no_go
Evidence: hypothesis
Core mechanism: check for an internal inconsistency between the dipole's claimed
sign convention (item #2 of the 36-point preprint, "even tiers attract, odd tiers
repel") and any candidate action's natural sign — several of Blocks 1-3's
action-based routes (items 1, 3, 4, 8) could each independently produce the wrong
sign.
Why it may work: a fast, cheap way to eliminate candidates before doing full
cosmological perturbation theory on any of them, catching a class of error early.
Required assumptions: each candidate action produces a well-defined sign for the
dipole term that can be directly compared to the preprint's stated convention.
Main obstacle: none significant — a bookkeeping check, not a derivation.
Cheapest test: for each surviving candidate from Blocks 1-3, check its natural
dipole sign against the preprint's stated "even attract, odd repel" convention.
Falsifier: not applicable in the usual sense — this item itself IS a falsifier
applied to other items; any candidate failing the sign check is eliminated by it.
Expected output: a sign-consistency table across all surviving Block 1-3 candidates.
Scores:
  relevance: 8
  feasibility: 8
  novelty: 3
  expected_impact: 7
  evidence_strength: 5
  confidence: 0.5
Sources: the project's own source material (preprint's stated sign convention)

### Block 6 — Formal verification approaches (3)

## 46. Computer-algebra-verified derivation (sympy/Mathematica)
Type: computational_experiment
Evidence: inference
Core mechanism: whichever candidate bridge is eventually selected for real
development, require the full derivation chain (action leads to field equations
leads to weak-field limit leads to matching `F_oP`) to be checked symbolically, not
by hand.
Why it may work: directly matches this project's own established discipline of
tool-verifying claims rather than trusting hand-derivation, already the gold
standard used elsewhere in this project's work.
Required assumptions: the derivation is concrete enough (a specific action, not just
a qualitative sketch) to encode symbolically.
Main obstacle: only applicable once a candidate derivation exists in explicit
symbolic form — not runnable on qualitative/exploratory items.
Cheapest test: not runnable yet; the cheap first step is stating this as a hard
requirement in the Prototyping Plan for any Month-1 derivation attempt.
Falsifier: not applicable — a verification requirement, not a physical claim.
Expected output: a symbolic-verification requirement attached to any future
candidate-derivation deliverable.
Scores:
  relevance: 7
  feasibility: 7
  novelty: 2
  expected_impact: 6
  evidence_strength: 7
  confidence: 0.6
Sources: this project's own verification discipline (established this session)

## 47. Dimensional-analysis audit of every candidate before further work
Type: computational_experiment
Evidence: fact
Core mechanism: a cheap, formal pass checking that every item in Blocks 1-5 is
dimensionally consistent as stated — catches errors before they propagate into
expensive derivations.
Why it may work: dimensional analysis is the cheapest possible formal check
available and catches a real, common class of error before any expensive work is
invested downstream.
Required assumptions: none — a mechanical check applicable to any item with a
stated formula.
Main obstacle: none significant — genuinely low-cost.
Cheapest test: this item IS the cheap test — walk through Blocks 1-5 and verify
dimensional consistency of every stated mechanism.
Falsifier: not applicable in the usual sense — any item found dimensionally
inconsistent is itself falsified by this check.
Expected output: a dimensional-consistency audit table across all 52 items.
Scores:
  relevance: 8
  feasibility: 9
  novelty: 1
  expected_impact: 5
  evidence_strength: 8
  confidence: 0.75
Sources: standard dimensional analysis (no specific paper needed)

## 48. Independent-model cross-check requirement
Type: computational_experiment
Evidence: fact
Core mechanism: per this project's own Independent Verification Strength Ladder
(`falsification-ladder.md`), once any candidate derivation is complete, have it
checked by a second, independently-written implementation, not just re-reading the
same derivation, before promoting to a real experiment.
Why it may work: directly reuses an already-established, already-validated project
protocol rather than inventing a new verification standard.
Required assumptions: none — a process requirement inherited directly from this
project's own methodology stack.
Main obstacle: none significant beyond the extra time cost of a genuinely
independent re-implementation, which the project's own ladder already treats as
worthwhile.
Cheapest test: not applicable as an external test; the requirement itself is the
deliverable, to be applied whenever a candidate reaches promotion-readiness.
Falsifier: not applicable — a process requirement, not a falsifiable physical claim.
Expected output: a standing promotion-gate requirement referenced before any item
in this document is registered as a formal FL experiment.
Scores:
  relevance: 7
  feasibility: 8
  novelty: 1
  expected_impact: 6
  evidence_strength: 7
  confidence: 0.7
Sources: this project's own `falsification-ladder.md`

### Block 7 — New mathematical constructions (2)

## 49. Define a multipole visibility function V(r, z)
Type: new_hypothesis
Evidence: hypothesis
Core mechanism: a new formal object tracking, as a function of both separation and
redshift, what fraction of a given multipole order's force survives coarse-graining —
generalizes item 10's binary "does it survive averaging" into a continuous
diagnostic usable across all of Blocks 1-6's candidate bridges uniformly.
Why it may work: a single, reusable diagnostic applicable across every candidate
bridge would let this document's items be compared on a common footing rather than
each needing its own bespoke survival check.
Required assumptions: a coarse-graining procedure (from any of items 1-14) exists
to define the function against.
Main obstacle: purely definitional at this stage — has no content until at least
one coarse-graining procedure (from Blocks 1-3) is worked out concretely enough to
instantiate it.
Cheapest test: instantiate `V(r, z)` for the simplest available candidate (item 10's
orientation-averaging result) as a proof of concept.
Falsifier: not applicable at the definitional stage; falsifiable once instantiated,
by comparing its predictions to any candidate's own direct calculation.
Expected output: a formal definition plus one worked instantiation.
Scores:
  relevance: 6
  feasibility: 5
  novelty: 7
  expected_impact: 6
  evidence_strength: 2
  confidence: 0.3
Sources: builds on item 10, no additional external source

## 50. Formalize a bridge equivalence class
Type: new_hypothesis
Evidence: hypothesis
Core mechanism: define two candidate bridges as equivalent if they produce the same
`H(z)` to within observational precision at current data quality, regardless of
differing internal structure — useful because several items above (1, 3, 4, 6, 7)
may turn out to be equivalence-class-identical even though they look structurally
different.
Why it may work: would prevent wasted effort developing multiple candidates that,
once tested, turn out to be numerically indistinguishable given current data
precision.
Required assumptions: at least two candidates reach testable form to compare (not
yet true at time of writing).
Main obstacle: purely definitional until at least two testable candidates exist to
actually compare.
Cheapest test: not runnable yet; recorded as a check to apply once items 35-37 (or
similar) produce multiple testable `H(z; theta)` outputs.
Falsifier: not applicable at the definitional stage.
Expected output: a formal equivalence-class definition, ready to apply once
multiple testable candidates exist.
Scores:
  relevance: 6
  feasibility: 6
  novelty: 5
  expected_impact: 5
  evidence_strength: 3
  confidence: 0.35
Sources: builds on items 1, 3, 4, 6, 7, no additional external source

### Block 8 — Minimal cheap prototypes (3)

## 51. One-week prototype: the PN-order plus symmetry filtering pipeline
Type: computational_experiment
Evidence: inference
Core mechanism: run item 30 (the PN-order-counting plus symmetry-first filtering
pipeline) as a scoped, one-week deliverable — the cheapest substantial prototype in
the entire document, pure analytic work, no new data, no new code.
Why it may work: directly actionable this week with existing knowledge and no
external dependencies, making it the natural first real prototyping step.
Required assumptions: same as item 30.
Main obstacle: same as item 30 — none new introduced by scoping it as a one-week
deliverable.
Cheapest test: this item IS the scoped cheap test, timeboxed to one week.
Falsifier: same as item 30's (not directly falsifiable — a filtering tool).
Expected output: the filtered shortlist described in item 30, delivered within one
week.
Scores:
  relevance: 9
  feasibility: 9
  novelty: 4
  expected_impact: 6
  evidence_strength: 5
  confidence: 0.6
Sources: same as item 30

## 52. One-day prototype: dimensional-analysis audit applied to this document itself
Type: computational_experiment
Evidence: fact
Core mechanism: recursively apply item 47's dimensional-analysis discipline to this
document's own Blocks 1-7 before any further investment is made in any of them — the
cheapest possible next action of all 52 items.
Why it may work: applying the skill's own quality-gate discipline to its own output
is the single cheapest, lowest-risk, most certain next step available, and it
directly protects every other item from carrying forward an undetected dimensional
error.
Required assumptions: none — a mechanical self-check.
Main obstacle: none significant.
Cheapest test: this item IS the cheap test, timeboxed to one day.
Falsifier: not applicable — a self-audit, not a falsifiable physical claim.
Expected output: a completed dimensional-consistency pass over this entire
document, one day after the document itself is produced.
Scores:
  relevance: 9
  feasibility: 10
  novelty: 2
  expected_impact: 5
  evidence_strength: 9
  confidence: 0.85
Sources: same as item 47

### Block 9 — Added 2026-07-17 after external adversarial review (1 item)

## 53. Shtanov et al. generalized cosmic energy equation (missing item, added post-review)
Type: established_method
Evidence: fact
Core mechanism: **added 2026-07-17 — a genuine gap in the original 52, confirmed via
WebSearch, arXiv:1010.6205 ("Generalizing the Cosmic Energy Equation," Shtanov et
al.) is real and directly on-point: it derives a Friedmann-equation-like expansion
law directly from a MODIFIED two-body gravitational interaction between dark-matter
particles, using the generalized Layzer-Irvine cosmic energy equation and cosmic
virial theorem — nonrelativistic, but a genuine existing precedent for exactly Gap 2
(pairwise force to Friedmann-like equation), missed in the original search.
Why it may work: unlike items 6/7 (this document's own from-scratch attempts at the
same aggregation step), this is an ALREADY-PUBLISHED, ALREADY-WORKED-OUT derivation
for a structurally similar problem (modified two-body DM interaction to modified
Friedmann equation) — directly reusable rather than reinvented.
Required assumptions: `F_oP` can be treated nonrelativistically for this route (the
same approximation Shtanov et al. use); a relativistic completion (Gap 3) is still
needed afterward, this item only addresses Gap 2.
Main obstacle: nonrelativistic — does not by itself resolve Gap 3 (relativistic
completion) or Gap 1 (action); it is the cheapest, most direct route to a
FIRST-PASS answer for Gap 2 specifically, not a full theory.
Cheapest test: apply Shtanov et al.'s generalized cosmic energy equation formalism
directly to `F_oP` (their method is designed for exactly this: a modified two-body
DM potential) and read off the resulting renormalized-G Friedmann-like equation.
Falsifier: if `F_oP`'s dipole/quadrupole terms cannot be cast in the modified-
potential form their method requires, this route does not apply without adaptation.
Expected output: a first-pass, nonrelativistic modified Friedmann equation directly
derived from `F_oP`, usable as an initial candidate for item 35's test pipeline
pending a relativistic completion.
Scores:
  relevance: 9
  feasibility: 8
  novelty: 6
  expected_impact: 9
  evidence_strength: 8
  confidence: 0.65
Source: [Shtanov et al., "Generalizing the Cosmic Energy Equation," arXiv:1010.6205](https://arxiv.org/abs/1010.6205) — verified real via WebSearch 2026-07-17

---

## Stage: Scoring formula (per skill's `references/scoring-model.md`)

```
priority_score = 0.25*relevance + 0.20*feasibility + 0.20*expected_impact
               + 0.15*evidence_strength + 0.10*novelty + 0.10*falsifiability
speculation_penalty: 0 (established technique) .. 4 (only verbal/visual similarity)
adjusted_score = priority_score - speculation_penalty
```
`falsifiability` (used in the formula but not a separately-tracked 0-10 field above)
is read qualitatively from whether each card's Falsifier is concrete and specific
(high) vs. "not applicable / meta-tool" (scored as moderate, since a process item's
lack of a physical falsifier is not a defect for that item's own type). Items 16
(control theory, overlaps `NO_BRIDGE_FITTING`), 12 (Kaluza-Klein, no stated textual
basis), and 27 (mean-field games, no cosmology precedent found) carry the heaviest
speculation penalties for exactly the reasons stated in each card, not as a blanket
discount.

---

## Top-12 (by adjusted priority)

**Revised 2026-07-17 after external review** — item 53 (real, on-point,
previously-missed source) enters at rank 2; the "check the dipole's tensor
character first" unknown (see Unknowns section) is now flagged as a P0 prerequisite
above even rank-1, since items 10/22/41's no-go arguments are conditional on it.

| Rank | # | Idea | Type | Why it ranks here |
|---|---|---|---|---|
| P0 | — | Resolve whether `F_oP`'s dipole is a true vector or a scalar tier label | (prerequisite, not a card) | gates items 10, 22, 41's entire no-go argument — see Unknowns |
| 1 | 52 | Dimensional-analysis audit of this document itself | computational_experiment | feasibility=10, evidence_strength=9, zero risk |
| 2 | 53 | Shtanov et al. generalized cosmic energy equation | established_method | expected_impact=9, real published precedent for Gap 2, added post-review |
| 3 | 20 | Historical precedent study (Newton→Friedmann template) | cross_domain_transfer | relevance=9, evidence_strength=9, already delivered its own output |
| 4 | 43 | Scope-check: is NR-013 partial evidence for #1 generally? | no_go | feasibility=9, evidence_strength=8, prevents overclaiming this document's own results |
| 5 | 38 | Enforce held-out validation on any future bridge test | computational_experiment | feasibility=9, evidence_strength=8, already-proven protocol |
| 6 | 33 | Historical scaffold applied to sequence items 1-14 | hybrid | feasibility=9, evidence_strength=8, output already delivered |
| 7 | 47 | Dimensional-analysis audit, general | computational_experiment | feasibility=9, evidence_strength=8 |
| 8 | 13 | Blanchet-Le Tiec perturbation-matching, generalized to quadrupole | extension | expected_impact=9, highest-impact genuine new-physics item |
| 9 | 35 | Reuse NR-013's pipeline for EFT-DE-derived H(z) | computational_experiment | feasibility=8, relevance=9, shovel-ready |
| 10 | 1 | Literalize EM analogy via Blanchet-Le Tiec action | cross_domain_transfer | relevance=9, feasibility=7 |
| 11 | 48 | Independent-model cross-check requirement | computational_experiment | feasibility=8, evidence_strength=7, already-proven protocol |
| 12 | 30 | PN-order + symmetry-first filtering pipeline (now ansatz-conditional, demoted) | hybrid | feasibility=6, relevance=6 after item 9's correction |

**Dropped from Top-12 after correction:** item 2 (Blanchet bispectrum constraint) —
was rank 11, now gated on item 1 succeeding first, no longer an independent
low-risk check; item 9 (PN order-counting) — was rank 8 as item 30's input, its
evidence_strength dropped 4→2 after the ansatz-conditional correction.

**Pattern worth naming explicitly:** the top of this ranking is dominated by cheap,
low-risk PROCESS/filtering items (dimensional analysis, held-out validation,
historical scaffolding, reusing existing infrastructure), not by ambitious new
physics content. That is not an artifact of the scoring formula being broken — it
correctly reflects that `feasibility` and `evidence_strength` are weighted highly
(0.20 and 0.15) relative to `novelty` (0.10), and that this project's own history
(the `eta_q=0` bug in `docs/122` v3, the `NO_BRIDGE_FITTING` rule) shows cheap
process discipline catching real errors before expensive physics work does.

---

## Three portfolios

**Conservative** (lowest risk, reuses existing tooling): 52, 47, 20, 33, 43, 38, 2,
35. Total new derivation required: near zero — mostly organizing and filtering
existing project material plus one PPN literature check.

**Balanced** (real new physics, bounded scope): add 1, 13, 30, 9, 10, 6 to the
Conservative set — commits to actually working out the Blanchet-Le Tiec adaptation
(items 1, 13) and the PN/symmetry filtering (items 9, 10, 30) as the first genuine
new-derivation attempts, gated by the Conservative portfolio's cheap checks first.

**Moonshot** (highest novelty, highest risk): add 12 (Kaluza-Klein), 11+21 (N-body +
symbolic regression discovery pipeline), 5 (Verlinde route) — explicitly flagged as
the least-supported items in the document (lowest evidence_strength scores),
included because the skill's own distribution requirements call for a moonshot tier,
not because they are currently recommended.

---

## Dependency matrix (abbreviated — key chains only)

```
44 (falsify "6 isomers is geometric") --blocks--> 12 (Kaluza-Klein) --enables--> 28
9 (PN order-counting) --feeds--> 30 (PN+symmetry pipeline) --feeds--> most of Block 1
1 (Blanchet-Le Tiec literalize) --feeds--> 13 (perturbation matching) --feeds--> 35
11 (N-body) --feeds--> 21 (symbolic regression) --feeds--> 31
3 (EFT-DE) --feeds--> 29 (EFT-DE + Bayesian) --feeds--> 35, 36, 37
14 (no-go literature search) --informs--> 41 (attempt own no-go proof)
40 (toy 2-body sanity check) --gates--> 11 (full N-body)
39 (DESI cross-check) --requires--> any surviving candidate from 35/36/37
```

---

## Prototyping plan

**Day 1:** item 52 (audit this document), item 44 (falsify/confirm the "6 isomers is
geometric" reading against actual preprint text), item 9 (PN order-counting, first
pass), item 40 (toy 2-body conservation sanity check).

**Week 1:** item 51/30 (PN+symmetry filtering pipeline, full run against all of
Blocks 1-3), item 2 (re-read the existing PPN dipole bound already used in this
project), item 14 (literature search for existing no-go theorems).

**Month 1:** item 1 + 13 (Blanchet-Le Tiec adaptation, the highest-scoring genuine
new-physics item), item 3 (EFT-DE parametrization attempt), item 45 (sign-convention
consistency check across surviving candidates).

**Year 1 (contingent on Month 1 producing at least one candidate that survives its
own falsifier):** item 35/36/37 (test the surviving candidate(s) against real data
via the existing NR-013-style pipeline), item 38/39 (held-out + independent-dataset
validation), item 48 (independent cross-check before any promotion to a registered
FL experiment).

---

## Negative results already known (do not re-derive)

- `NR-013`: no `(beta_d, beta_q)` coefficient choice in the CURRENT placeholder
  bridge beats the monopole baseline — this document's entire premise is built on
  NOT repeating that specific dead end.
- `NO_BRIDGE_FITTING` (facts.json, added 2026-07-08): forbids reconstructing the
  bridge by ANY error-minimizing optimization against Table A1 — items 16 and 21 in
  this document are flagged as at-risk of violating this rule if not implemented
  carefully (used only as discovery/suggestion tools, never as the final answer).
- Item 5 (Verlinde route) and item 19 (holographic route) are graded low specifically
  because, on inspection, their known functional forms do not obviously match
  `F_oP`'s multipole structure — recorded here so this is not re-attempted from
  scratch without new information.

## Unknowns (explicitly not resolved by this exercise)

- Whether TJB has an unpublished action-level formulation of `F_oP` (would make most
  of Blocks 1-2 unnecessary if it exists and is shared).
- Whether the isomer count (6) has any geometric/group-theoretic motivation at all
  (item 44 is the cheap first check).
- Whether Gaps 1-3 are independently solvable or genuinely coupled (item 33's
  historical-scaffold sequencing is a first attempt to find out, not a resolution).
- **Added 2026-07-17 after external review, highest-priority open unknown:**
  whether the preprint's "dipole" is a genuine oriented (odd-parity, vector-moment)
  object at all, or a scalar radial-power-law "tier" label (a `1/r^3` amplitude with
  no directional character). This is NOT resolved anywhere in this document. Items
  10, 22, and 41 all assume a true vector dipole subject to orientation-averaging
  cancellation — if the preprint's "dipole" is actually a scalar tier amplitude,
  their entire no-go/averaging argument does not apply, and the leading-order
  cancellation they rely on may not occur at all. This should be checked directly
  against the preprint's own definition BEFORE trusting items 10/22/41's
  conclusions, and is now the single most consequential unresolved ambiguity in this
  document — more consequential than any individual idea card's own score.

## Sources (all real, checked this session)

- [Blanchet & Le Tiec 2008, arXiv:0804.3518](https://arxiv.org/abs/0804.3518)
- [Blanchet & Le Tiec 2009, arXiv:0901.3114](https://arxiv.org/abs/0901.3114)
- [Dipolar DM RAMSES simulations, arXiv:2209.07831](https://arxiv.org/pdf/2209.07831)
- [Gubitosi, Piazza, Vernizzi 2013, arXiv:1210.0201](https://arxiv.org/abs/1210.0201)
- [Bekenstein TeVeS cosmology, arXiv:astro-ph/0511591](https://arxiv.org/abs/astro-ph/0511591)
- [Verlinde 2016, arXiv:1611.02269](https://arxiv.org/abs/1611.02269)
- Blanchet arXiv:1312.6991 (already used in this project, task #8)
- Kobayashi, Yamaguchi, Yokoyama 2011 (Horndeski review), arXiv:1105.5723
- Udrescu & Tegmark 2020 (AI Feynman), arXiv:1905.11481
- Trotta 2008 (Bayesian model comparison in cosmology), arXiv:0803.4089
- Cohen, Kaplan, Nelson 1999 (holographic dark energy), hep-th/9803132
- Textbook/foundational (no single arXiv ID): Weinberg *Cosmology* (2008); Will,
  *Theory and Experiment in Gravitational Physics* (2018 ed.); Jackson, *Classical
  Electrodynamics* ch. 9; Binney & Tremaine, *Galactic Dynamics*; Landau & Lifshitz,
  *Statistical Physics* Part 1 ch. XII; Georgi 1993 Ann. Rev. Nucl. Part. Sci.
  (effective field theory); Kermack-McKendrick (1927, epidemiology aggregation,
  pre-arXiv); Horndeski 1974 (pre-arXiv); Kodama & Sasaki 1984 (SVT decomposition)
- Item 14 explicitly marked `<unknown>` — no specific no-go theorem source found or
  cited; flagged per the skill's own anti-hallucination rule rather than invented.
- Item 25 (graph-theory route) and item 27 (mean-field games) explicitly marked
  `<unknown>` for "has this been tried in cosmology" — no source found either way.

---

*NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NOT_AUTHOR_ERROR*
*This document is idea-generation output from `/boyko-goal-expansion-100`, not a
registered FL experiment. Promotion of any item to `experiments/` requires its own
claim.md pre-registration per this project's standard protocol.*

---

## Update, 2026-08-26 — re-score against the P58-P141 campaign (`boyko-goal-expansion-100` re-invoked)

**Why this update exists.** The user re-invoked `/boyko-goal-expansion-100` on this
exact goal ("F→H_MULT(z) мост") today. Before generating anything new, the campaign
history since this document's 2026-07-17 write date was checked — 40 days, 130+
P-scripts (`experiments/20260803-bridge/`), 14 new structural facts established.
Blindly regenerating 100 fresh cards would have violated this project's own Novelty
Check discipline (grep null_results/parked/prior-runs before re-attempting). Instead:
every one of the 53 existing cards was re-scored against what actually happened
since, per the user's own explicit choice ("Re-score docs/123 + точечный добор").

**P0 unknown resolved.** The single most consequential open question flagged in this
document (line ~1858 above — is the dipole a true oriented vector or a scalar radial
"tier" label; "more consequential than any individual idea card's own score") was
never directly checked against source text by the P58-P141 campaign — every
downstream result (two-charge completion, double-layer theorem, EP-tension) was
built on a *constructed* dipole model ("induced, radially-aligned polarisation",
`FINDING_two_charge_completion.md:63`), not a source-verified one. Checked now,
directly: `data/source_material/buckholtz_preprints202511.0598.v6.md` lines 467-470 —
TJB's own text: *"thinking of the notion of a magnetic moment that has bases in
currents of charges, the motion of charges of the sub-objects can associate with
dipole... effects regarding forces."* A magnetic-moment analogy is unambiguously a
genuine oriented-vector object, not a scalar tier label — **P0 resolved: true vector
dipole, confirmed from source, 40 days after being flagged as the top-priority
prerequisite.** Note the analogy suggests orientation tied to internal
rotational/orbital sub-object motion (like a magnetic moment from circulating
charge), not necessarily "radially aligned toward the other object" as Family F's
specific construction assumed — but `FINDING_dipole_shell_is_a_double_layer.md`
already checked BOTH the radially-aligned and the randomly-oriented branches and
found exact zero either way, so this resolution is confirmatory of the campaign's
downstream validity, not overturning.

**Full re-score (all 53 cards).** Status counts: **EXECUTED 12** (1, 6, 10, 13, 38,
39, 41, 42, 45, 46, 48, 53) · **KILLED-BY-NEW-EVIDENCE 5** (2, 22, 24, 25, 28) ·
**SUPERSEDED-BY-BETTER-VERSION 8** (3, 14, 15, 17, 29, 32, 35, 49) · **STRENGTHENED
4** (30, 33, 43, 51) · **STILL-OPEN 24** (4, 5, 7, 8, 9, 11, 12, 16, 18, 19, 20, 21,
23, 26, 27, 31, 34, 36, 37, 40, 44, 47, 50, 52).

| # | Title (short) | New status | Justification (fact # or file) |
|---|---|---|---|
| 1 | Blanchet-Le Tiec dipolar-fluid action | EXECUTED | `docs/131` builds exactly this as CANDIDATE-L1 — FAILS weak-field matching on the repulsive-dipole sign, requires abandoning EP/ghost-freeness/staticity |
| 2 | Blanchet bispectrum constraint | KILLED-BY-NEW-EVIDENCE | Gated on item 1 succeeding cleanly; item 1 built but the resulting theory violates EP |
| 3 | EFT-DE parametrization | SUPERSEDED | Family-F/M wrote the actual Lagrangian and got the answer directly: EdS, Ω_φ~1e-6, w=-1/3 exactly |
| 4 | TeVeS structural completion | STILL-OPEN | Untried; distinct from CANDIDATE-L1's Blanchet route |
| 5 | Verlinde emergent-gravity route | STILL-OPEN | Untried; already weakest of the "big-name" analogies |
| 6 | Continuum-mechanics T^μν from pair force | EXECUTED | `NR-018` Ground 1: w=n/3>0 for every multipole order, independent of ξ/amplitude/cutoff |
| 7 | Kinetic-theory/Boltzmann route | STILL-OPEN | Untried; confirmed absent from campaign file list |
| 8 | Horndeski reverse search | STILL-OPEN | Untried |
| 9 | PN order-counting | STILL-OPEN | Term appears only inside docs/123 itself, never run |
| 10 | FRW-symmetry orientation-averaging of dipole | EXECUTED | `FINDING_dipole_shell_is_a_double_layer.md`: exact zero at ~1e-16, both branches |
| 11 | N-body simulation | STILL-OPEN | Untried |
| 12 | Kaluza-Klein reduction | STILL-OPEN | Untried, gating item 44 also never run |
| 13 | Blanchet perturbation-matching + quadrupole | EXECUTED | `FINDING_P6`: quadrupole stays 2nd-order (falsifier didn't trigger), dipole gives real local prediction dG_eff/G~7e-8-7e-6 |
| 14 | No-go literature search | SUPERSEDED | Item 41 executed from scratch, stronger in-house result (exact zero) than any literature search would find |
| 15 | Ferroelectric/paraelectric analogy | SUPERSEDED | Two-charge completion already fixes the orientation mechanism by A↔B symmetry, not a speculative order parameter |
| 16 | Control-theory system ID | STILL-OPEN | Untried; fact 11 (Table A1=AI-output) reinforces NO_BRIDGE_FITTING obstacle but doesn't newly kill it |
| 17 | RG flow, cluster→cosmological | SUPERSEDED | `docs/127` gives exact-zero, strictly stronger than any RG estimate |
| 18 | Bayesian model comparison | STILL-OPEN | Still gated on ≥2 simultaneously-surviving candidates — precondition never met |
| 19 | Holographic dark-fluid EoS | STILL-OPEN | Untried; weakened by facts 6/9 but not directly killed |
| 20 | Historical Newton→Friedmann precedent | STILL-OPEN | Self-referential tool, output already delivered |
| 21 | Symbolic regression on N-body output | STILL-OPEN | Gated on item 11, untried |
| 22 | SVT vorticity/decay-rate classification | KILLED-BY-NEW-EVIDENCE | Fact 3 is a stronger non-perturbative closure than mere decay |
| 23 | Two-fluid Jeans-instability analogy | STILL-OPEN | Untried, different scale question than fact 3 |
| 24 | Dipole-quadrupole cross-term | KILLED-BY-NEW-EVIDENCE | Strong inference from fact 3's general closure (not literally computed) |
| 25 | Graph-Laplacian discreteness-aware aggregation | KILLED-BY-NEW-EVIDENCE | NR-018 Ground 1 explicitly independent of ξ/cutoff — closes the discreteness-rescue this item hoped for |
| 26 | Epidemiology aggregation transfer | STILL-OPEN | Untried; different mathematical object than fact 6 covers |
| 27 | Mean-field-game aggregation | STILL-OPEN | Untried, already weakest card |
| 28 | Blanchet-Le Tiec + KK hybrid | KILLED-BY-NEW-EVIDENCE | Inherits item 1's falsifier; item 1 executed and failed |
| 29 | EFT-DE + Bayesian hybrid | SUPERSEDED | Inherits item 3's status |
| 30 | PN + symmetry filtering pipeline | STRENGTHENED | Half the pipeline (averaging) now exact proof, not hypothesis |
| 31 | N-body + symbolic-regression pipeline | STILL-OPEN | Gated on item 11, untried |
| 32 | Phase-transition + RG-flow hybrid | SUPERSEDED | Both halves superseded by exact results |
| 33 | Historical scaffold → Gap-sequencing table | STRENGTHENED | Gap 1 (no action) and Gap 2 (no aggregation rule) both substantially closed since write-time — table is now stale, worth re-issuing |
| 34 | Blanchet-bispectrum + TeVeS hybrid | STILL-OPEN | Item-2 half low-value now; item-4 half (TeVeS) still fully untried |
| 35 | NR-013 pipeline on EFT-DE H(z) | SUPERSEDED | The generic purpose was carried out on the actual completion instead — `FINDING_P99`: NO JOINT FIT |
| 36 | Same pipeline, TeVeS-derived H(z) | STILL-OPEN | Gated on item 4 |
| 37 | Same pipeline, kinetic-theory H(z) | STILL-OPEN | Gated on item 7 |
| 38 | Enforce held-out validation discipline | EXECUTED | `FINDING_P99` reserves z=1.0/3.0 as genuine out-of-sample check |
| 39 | Independent DESI DR1 f-σ8 cross-check | EXECUTED | `FINDING_P132` + P22-P32 chain: A·g²≲8.39e-12, but only constrains the product (inherits fact 8's degeneracy) |
| 40 | Toy 2-body conservation sanity check | STILL-OPEN | No direct evidence this standalone gate was run |
| 41 | Attempt own no-go proof (dipole averaging) | EXECUTED | Exact zero for dipole AND quadrupole, both branches — beyond what the card modestly asked for |
| 42 | Adversarial minimal counter-model | EXECUTED | `FINDING_P6`: local (non-averaged) regime dipole IS detectable, dG_eff/G~7e-8-7e-6 — brackets item 41 |
| 43 | Scope-check: does NR-013 generalize? | STRENGTHENED | 3 more independent construction routes have now all failed for non-overlapping reasons |
| 44 | Falsify "6 isomers is geometric" | STILL-OPEN | Never run |
| 45 | Sign-convention consistency check | EXECUTED | Two-charge completion enforces it as a theorem; CANDIDATE-L1 checked and failed exactly on this |
| 46 | Sympy-verified derivation chain | EXECUTED | `docs/125` and `FINDING_P133` are direct instances |
| 47 | Dimensional-analysis audit, all 52 items | STILL-OPEN | No standalone audit artifact found despite 130+ P-scripts since |
| 48 | Independent-model cross-check requirement | EXECUTED | Context-blind skeptic review is now the project's default discipline |
| 49 | Multipole visibility function V(r,z) | SUPERSEDED | Sharper closed-form answer already obtained for the channel that mattered: exact zero |
| 50 | Bridge equivalence-class formalism | STILL-OPEN | Never became necessary — attempts rejected sequentially, not simultaneously |
| 51 | 1-week PN+symmetry prototype | STRENGTHENED | Same as item 30, timeboxed |
| 52 | 1-day dimensional-audit of docs/123 itself | STILL-OPEN | Ranked #1 in original Top-12 as cheapest item — still not done, 40 days later |
| 53 | Shtanov-Sahni generalized cosmic energy equation | EXECUTED | `docs/127`/P2/C1: background coupling vanishes exactly for any q(a) and any coefficient — stronger than hoped |

**New forward-looking Top-12** (STILL-OPEN + STRENGTHENED only; EXECUTED / KILLED /
SUPERSEDED items are retired, not deleted — see table above): 33, 43, 52, 20, 47,
30, 18, 51, 4, 8, 7, 37. Honest caveat: #33/#43 rank highest mostly as cheap
consolidation of what's already known, not new physics. #18 has been stuck on the
same unmet precondition (≥2 simultaneously-surviving candidates) since write-time —
not newly urgent, just never got easier. The two genuinely live new-physics
frontiers remaining untried are **#4 (TeVeS)** and **#7/#8 (kinetic theory,
Horndeski)**.

**Three genuinely new cards — visible only because of facts established since
2026-07-17, not present among the original 53:**

## 54. k-sector cosmological-perturbation exact-cancellation extension test
Type: computational_experiment
Evidence: hypothesis
Core mechanism: Facts 3 (force-level isotropic average of the k-sector is exactly
zero, ~1e-16, both branches) + 5 (Shtanov-Sahni background coupling vanishes exactly
for any q(a)) + 6 (no positive-density virial fluid from any pure inverse-power pair
potential is ever dark-energy-like) are all **background-level** or
isotropically-averaged-force-level results. `FINDING_P47_linearized_phi_stress_tensor_no_anisotropic_stress.md`
explicitly scopes ITS OWN perturbation-level (structure-formation) work to "monopole
(g) sector only" — the k-sector was never checked at the perturbation level at all.
Why it may work: if the same exact-cancellation mechanism (double-layer symmetry, or
an analogous argument) extends to every order of linear cosmological perturbation
theory (δG_μν, growth rate, weak lensing, anisotropic stress), that closes "does
MULTING's k-sector affect cosmology at all" — not just background expansion — a
strictly stronger, cleaner, more general result than any of the original 53 cards.
Required assumptions: the perturbed-universe loss of perfect isotropy doesn't
restore the local visibility `FINDING_P6` already found in the non-averaged
two-body regime (dG_eff/G~7e-8-7e-6).
Main obstacle: this is a genuinely new derivation, not a re-run of existing code —
requires extending the P34-P57 monopole-sector perturbation machinery to the k-sector
specifically, which nobody has attempted.
Cheapest test: check whether the exact double-layer cancellation argument
(shell-theorem, angular-momentum/multipole selection rule) survives a perturbed
(non-exactly-isotropic) background at leading order, before attempting the full
δG_μν calculation.
Falsifier: if the k-sector produces a nonzero contribution at ANY perturbative order
even under the same symmetry argument that zeroes the background, that IS the
strongest, most directly-derived discriminating observable this campaign has found —
either outcome is a genuine result, not a null exercise.
Expected output: either a general no-go closing bottleneck 1's k-sector question
entirely, or a concrete new falsifiable prediction stronger than the external DESI/fσ8
ceiling (fact 14), because it would be MULTING-specific rather than an imported bound.
Scores: relevance=9, feasibility=6, novelty=9, expected_impact=9, evidence_strength=4,
confidence=0.55

## 55. WEP/Eötvös MICROSCOPE numeric cross-check (kill-gate completion)
Type: computational_experiment
Evidence: hypothesis
Core mechanism: Fact 13 — the k-sector produces a genuine, falsifiable,
composition-dependent Eötvös-experiment acceleration difference (unlike the g-sector,
which is EP-test-invisible), per `FINDING_P25_wep_eotvos_kill_gate.md`'s full closed
form (corrected for a completeness gap: originally omitted F_mm and F_kk terms).
This kill-gate exists ONLY because of post-docs/123 work (two-charge completion, fact
2) — none of the original 53 cards proposed an equivalence-principle test.
Why it may work: MICROSCOPE (Touboul et al. 2022, published) is the tightest existing
Eötvös bound (η~1e-15); if the k-sector's predicted composition-dependent signature
at the derived β_d, β_q values exceeds this bound, the k-sector as currently
constructed is directly excluded by existing data — no new observation needed.
Required assumptions: the composition ratio K/M is not universal across the
MICROSCOPE test masses (platinum/titanium) — `FINDING_P25` itself flags a
codimension-1 cancellation surface in κ where this escape route exists.
Main obstacle: the full closed form (F_mm + F_km + F_kk) has never been numerically
evaluated against actual MICROSCOPE composition/sensitivity parameters — only
derived symbolically.
Cheapest test: plug MICROSCOPE's published test-mass compositions and η-sensitivity
directly into `FINDING_P25`'s corrected closed form; check whether the codimension-1
escape surface is fine-tuned or generic.
Falsifier: if the predicted η exceeds MICROSCOPE's bound for generic (non-fine-tuned)
K/M, the k-sector's current normalization is directly excluded by existing published
data.
Expected output: either a clean exclusion (strong negative result, closes a whole
completion class) or a bound on κ tighter than the DESI/fσ8 ceiling.
Scores: relevance=8, feasibility=8, novelty=7, expected_impact=8, evidence_strength=6,
confidence=0.65

## 56. Explicit scale-dependent screening construction (resolve the Yukawa/masslessness tension)
Type: extension
Evidence: hypothesis
Core mechanism: Fact 12 — a Yukawa (massive) mediator breaks the double-layer
cancellation for any finite mass (fact 3's cancellation is specific to
masslessness), but the two-charge completion's own derivation of `β_q/β_d=√6/2`
requires an exactly massless mediator (fact 2) — these two established results
directly conflict unless the mediator mass is genuinely scale-dependent
(negligible at cluster scale, O(1) cosmologically), which `FINDING_P11`/`P12` note
but never construct.
Why it may work: chameleon/Vainshtein/symmetron-class screening mechanisms are
standard, published tools for exactly this kind of scale-dependent mass; none has
been checked for compatibility with the two-charge completion's own derived
coupling structure.
Required assumptions: a screening mechanism exists that (a) reduces to
near-exact masslessness at cluster scale (preserving `β_q/β_d=√6/2` to the
precision item 45's checks require) and (b) becomes O(1) massive at cosmological
scale (potentially restoring cosmological visibility that fact 3's exact-zero result
currently forecloses).
Main obstacle: constructing (a)+(b) simultaneously in a single consistent field
theory is itself a nontrivial model-building exercise, not guaranteed to exist.
Cheapest test: check whether any of the three standard screening classes
(chameleon, Vainshtein, symmetron) has a published parametrization compatible with
BOTH cluster-scale near-masslessness AND the coupling structure `docs/125`/P1
already derived, before attempting to build a new one from scratch.
Falsifier: if no standard screening class is structurally compatible with the
already-derived coupling, that itself narrows the viable-completion space further
(a negative result, not a dead end for the exercise).
Expected output: either a concrete, checkable screened-completion candidate, or a
documented incompatibility that further narrows bottleneck 1's viable-mechanism
space.
Scores: relevance=7, feasibility=5, novelty=7, expected_impact=7, evidence_strength=3,
confidence=0.4

**Recommendation, not a decision made here:** the highest-leverage single next step,
if the user wants to continue this bottleneck, is item 54 — it is the only one of
the three new cards capable of closing bottleneck 1's k-sector question outright
(either direction) rather than adding one more external-literature ceiling. Per
`docs/147`'s own stop-rule discipline: this update does NOT launch a new P-script.
It records the re-score and the 3 new candidates for the user's own next decision.

*NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NOT_AUTHOR_ERROR — this
update, like the rest of this document, is idea-generation output, not a claim
about TJB's own theory or a registered FL result.*
