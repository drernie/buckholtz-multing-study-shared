# docs/150 — v82 vs. this project's own reconstruction: systematic
# comparison, and why the bridge wasn't found by us

**Date:** 2026-08-30
**Origin:** direct user request, following `docs/149`'s first-pass study
of TJB's v82 preprint — "почему мы сами не смогли дойти до таких
результатов... сравним наши результаты с его результатами... сделать
сравнительную таблицу... что нового? что мы знали? что мы не знали?"
**Method:** cross-referenced `docs/149`'s own v82 read against `docs/145`
(the project's comprehensive research-audit through Part 8, 2026-08-26)
and this session's own P148-P155 work, plus a direct grep of v6's own
markdown (`data/source_material/buckholtz_preprints202511.0598.v6.md`)
for whether the material now in v82 existed there in any form.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive — a provenance/comparison study, not a
falsification-ladder experiment.

---

## 0. The central question, answered first: why didn't we get there?

**Because in v6 (the version we had), there was nothing to get to.** This
project already established, independently, on 2026-08-03, that v6's own
`H(z)` values (Table A1, the object our earlier work spent months trying
to reverse-engineer a bridge from) are **the output of an AI service
answering a prompt** — TJB's own caption says so verbatim: *"Table A1.
Responses, to our prompt, by one online service that has bases in
artificial intelligence."* This project's own memory record on that
finding ends with exactly the right question, asked three and a half
weeks before v82 existed: *"is there a MULTING calculation of `H(z)` that
does not pass through an AI service? If yes, that is the object to
reconstruct. If no, the bridge does not exist in any form and building
one is new work, not reconstruction."*

A direct grep of v6's own text confirms this structurally, not just by
citing the earlier finding: v6 contains **zero** occurrences of "node,"
"accretion," "kinematic translation," "reduced mass," or any `m_X(z)` /
`r_X(z)` / `k_X(z)`-style scaling law. Its own `H(z)` machinery is
entirely contained in **Appendix A**, titled *"Using MULTING to calculate
the Hubble parameter `H(z)`"* — and that appendix's own first sentence
says the values come from *"a process for calculating `H(z)` by using
MULTING"* carried out **by an AI service**, not a closed-form derivation
TJB performed and published himself.

**v82 is not us having missed something in v6.** It is TJB having done,
between May and August 2026, the actual physics work that v6's own
Appendix A had outsourced to a prompt: an explicit two-body kinematic
derivation (Sec. II.B–C) replacing the AI-service call, and explicit
`m_X(z)`/`r_X(z)`/`k_X(z)` evolution laws (Sec. II.D) replacing the
unspecified cluster-property inputs that would have been needed to even
attempt one. This project's own bottleneck-1 verdict — *"BLOCKED, not
derived... remains so not because a test refuted it, but because no new
information has appeared enabling direct-derivation reopening"* — was
the epistemically correct call for the object we actually had. The
"new information" `docs/147` itself named as the only valid reopen
condition has now, genuinely, appeared.

## 1. Topic-by-topic comparison

| Topic | This project (v6-based) | v82 (TJB's current work) | Verdict |
|---|---|---|---|
| **Two-body force law** | `F_oP = Q_i^T K(r) Q_j`, exact bilinear factorization (`docs/125`, `P1`), `β_d=2, β_q=√6` dimensionless, derived from a symmetric point-charge construction (`two_charge_completion.py`) | `F_P=F⁽⁰⁾−F⁽¹⁾+F⁽²⁾` (Eqs. 1-4), same tier structure, `β₁≈1.4×10¹⁰, β₂≈7.7×10¹⁷` dimensional, fitted (not derived) via χ² | **Same physics, different status.** We *derived* the sign/tier structure from a covariant construction; v82 *fits* two free coefficients directly to data. Units/scale not yet reconciled — open item. |
| **Alternating sign rule** | Proven as a theorem: binomial expansion of `(m−κk)(m'−κk')` (`two_charge_completion.py`) | Stated as the paper's own multipole convention (`n_F=2,3,4` associate with `s⁻²,s⁻³,s⁻⁴`), not independently re-derived from a deeper structure in the text read | **We have something v82 doesn't show**: an actual derivation of why the signs alternate, not just a labelling convention. |
| **F→H(z) bridge** | Did not exist to find (§0). Our own route: Shtanov–Sahni generalized cosmic-energy equation, `G_eff=0` for the dipole/quadrupole terms under isotropic averaging (`docs/124`-`127`) | Explicit: accretion-corrected two-body kinematics → `ä/a=s̈(z)/s(z)` → integrate → `H(z)` (Sec. II.B-C, Eqs. 5-9) | **Genuinely new to us, and a *different mechanism* than ours.** Not yet compared for consistency — see §6. |
| **Cluster-property evolution** `m_A(z)`,`r_A(z)`,`k_A(z)` | Unspecified in v6; `docs/54`'s own Blocker 2 flagged this as missing; five independent P-steps (P14§6/P17/P21/P22/P26) kept rediscovering the same gap before P27 unified them | Explicit power-law/scaling-law derivations (Eqs. 10-14), each honestly classified as data-proximate / retained-theoretical / circular | **Directly closes a named, long-standing gap in our own project.** |
| **Provenance discipline** | This project's own `artifact-provenance-gates.md` (4 gates: identity, target provenance, positive-control digitization, conserved-budget) | TJB's own independent 3-class system (Sec. II.F: data-proximate / retained-theoretical / circular), applied to his own inputs, plus an explicit "path forward" methodology discussion (Sec. IV.O) | **Independently convergent methodology**, not derived from one another — worth noting as a real point of intellectual contact, not a coincidence to overstate. |
| **Dark energy / background** | `FINDING_P85`: direct numerical integration of the covariant two-field action → matter-dominated Einstein-de Sitter, `Ω_φ~10⁻⁶`, **no dark-energy term in the action at all** | Table IV: "dark-energy-free" is v82's own stated empirical scope | **Independent convergence, different methods, same qualitative conclusion** — real, worth being genuinely pleased about, and worth citing accurately (not overclaiming it as a joint result — two separate reconstructions from two separate source documents happened to agree). |
| **Dipole physical justification** | Mirror-symmetric/externally-supplied-axis convention (`two_charge_completion.py`, `P1`); `docs/123`'s own magnetic-moment-analogy citation from v6 | Sec. IV.F: same EM/magnetic-moment analogy, explicit "axis comes from outside the thermal energy itself" resolution | **Same physical picture in both versions** — this piece did *not* change between v6 and v82. |
| **Force-term near-cancellation** | `docs/144` (partial read, SH0ES-focused) already found `F⁽¹⁾`/`F⁽²⁾` ≈50%/50% opposite sign | Table III / Sec. IV.K: `F⁽¹⁾≈+53%`, `F⁽²⁾≈-46.5%`, net `4-6%`, explicitly identified by TJB as the paper's own central fragility | **Confirms and completes** what `docs/144` had already partially found from the same document. |
| **Identifiability / degeneracy of coupling constants** | `FINDING_P133`: `(A,g,κ)` are NOT jointly identifiable from current observational handles — `rank(Jacobian)=2<3`, proven two independent ways | Not addressed in the read portion (pp. 1-33) — `β₁,β₂,H₀,anchor` are fit as 3 free parameters with no stated identifiability check | **This project has something v82 does not show.** Whether v82's own 3 parameters have the same degeneracy is an open, checkable question (see §6), not yet asked. |
| **Covariant dipole-completion sign tension** | `FINDING_P148`/`docs/131`: the most natural covariant completion of the repulsive dipole settles into an *attractive* stable configuration — getting the repulsive sign requires relaxing EP, ghost-freeness, or staticity for one specific construction | Not addressed — v82 works entirely at the level of the phenomenological force law and its fit, not a covariant field-theoretic completion | **This project has something v82 does not attempt at all.** v82 does not build (or need, for its own purposes) a covariant Lagrangian completion. |
| **S1/S2 escape-route closure (this session)** | `P152`-`P155`: for the *specific* covariant scalar completion this project built, both named ways to simultaneously match the near-field ladder and source a nonzero cosmological background are closed | Not applicable / not addressed — v82 does not build the kind of covariant completion these findings are about | **Not comparable** — different objects. Our own S1/S2 work is about a covariant field-theory completion of the force law; v82 stays at the phenomenological force-law-plus-kinematics level throughout. |
| **Fifth-force / solar-system constraint mapping** | `P150`/`P151`: attempted to map `k_A` onto ordinary-matter test masses (MICROSCOPE, Cassini) — found the mapping itself construct-invalid/disputed for ordinary matter, and the Cassini check ultimately `UNRESOLVED` | Not addressed in the read portion — v82's own observational tests are Cosmic Chronometer/SH0ES/DESI (background `H(z)`), not laboratory/solar-system fifth-force bounds | **This project attempted something v82 doesn't cover at all** — whether/how `k_A` extends to non-cluster objects. |
| **Growth-rate / `fσ8` external ceiling** | `docs/147` bottleneck 3: `A·g²≲8.39×10⁻¹²`, a *soft* phenomenological ceiling borrowed from Bean & Tangmatitham's own parametrization, not derived from MULTING's own construction | Not addressed in the read portion | Different observable channel entirely — not directly comparable without checking whether v82's own `β₁,β₂` numbers, converted, would even approach this ceiling (not attempted here). |
| **S8 tension** | Never examined anywhere in this project's own work (checked: no `P`-step or `docs/` file addresses it) | Sec. IV.P: qualitative argument that `ΛCDM` techniques "estimate only half the relevant gravitational repulsion" and thereby overestimate lumpiness — not a quantitative derivation in the pages read | **Genuinely new territory for us, and admittedly under-developed in v82 itself** (qualitative, not computed). |
| **Phantom-`w`/"third era" behavior, `H(t)` turnover** | Never examined — this project's own work stayed within the Einstein-de-Sitter/matter-dominated regime `FINDING_P85` established | Sec. IV.Q-R: a genuinely new, self-reported feature — the spotlighted fit's `H(t)` stops falling and starts rising again around 1.1 Gyr ago (`q<-1` "phantom" regime), flagged by TJB himself as fit-configuration-dependent, not a confident prediction | **Entirely new to us.** Worth noting TJB's own candor: he explicitly separates this from the well-established era-one-to-era-two transition and states plainly it could be an artifact of this particular fit. |
| **Multi-body / population-averaging validity** | `P154`/`P155` (this session): does the isotropic *population* average of the dipole/quadrupole force vanish — yes, at the force level, for both tiers, via two convergent mechanisms | Sec. IV.H, "typical objects, not distributions": every quantity in Sec. II.D is a *single representative value* per redshift, explicitly *not* a population average — TJB flags this as an open, unquantified simplification | **Adjacent but different questions.** Ours: does the *background contribution* of a population of randomly-oriented sources vanish? His: does using one representative node (rather than a distribution) at each redshift introduce error? Neither answers the other. |
| **AI-assisted development methodology** | This entire project's own FL/EstimandOps stack, context-asymmetric skeptic dispatches, no-silent-correction convention | Sec. IV.U: TJB states plainly the paper was produced through "sustained, iterative collaboration" with AI systems, discloses a units error, a sign error, and a circular parameter search caught during development, and describes an independent AI-regeneration verification pass on the archived results | **Independently convergent process discipline** — arrived at separately, not through contact between the two efforts before this correspondence. |

## 2. What v82 tells us that we genuinely did not know

1. **A real F→H(z) bridge exists now**, closing `docs/147`'s named
   bottleneck-1 reopen condition (§0 above).
2. **Explicit `m_A(z)`/`r_A(z)`/`k_A(z)` evolution laws**, closing
   `docs/54`'s Blocker 2 (independently rediscovered five times in our
   own work before `P27` unified the finding).
3. **`H(t)` can turn over a second time** (the "third era," Sec. IV.Q) —
   a feature this project never had reason to look for, since our own
   background result (Einstein–de Sitter, matter-dominated) doesn't
   produce one.
4. **TJB's own submission history** — MDPI *Universe* rejected an
   earlier version; Springer's *Foundations of Physics* is a candidate
   next venue (from his 2026-08-29 email, not the preprint itself).

## 3. What we already had, that v82 independently confirms

1. **"Matter-dominated, no dark energy"** — `FINDING_P85` (v6-based,
   direct numerical integration) and v82's own Table IV (fit-based,
   different method, different source document) agree.
2. **Magnetic-moment/EM analogy for the dipole's physical origin** —
   present in both v6 (`docs/123`) and v82 (Sec. IV.F), essentially
   unchanged.
3. **Near-total dipole/quadrupole cancellation** — `docs/144` (partial
   v82 read) already found this; the full read confirms and quantifies
   it (Table III).

## 4. What this project has that v82 does not

1. **A derivation of the alternating-sign rule** from a covariant
   point-charge construction (v82 states it as a labelling convention).
2. **A formal, twice-proven identifiability degeneracy** for its own 3
   coupling constants (`FINDING_P133`) — v82 fits 3 free parameters
   without a stated identifiability check.
3. **An attempted covariant field-theoretic completion** of the force
   law, with its own internal tensions honestly catalogued (`FINDING_
   P148`, `P152`-`P155`) — v82 does not attempt this; it stays at the
   phenomenological-force-plus-kinematics level throughout the pages
   read.
4. **Explicit attempts to map `k_A` onto laboratory/solar-system test
   objects** (`P150`/`P151`) — v82 does not address whether/how its own
   node-based thermal-energy charge could apply outside cluster-scale
   nodes.

## 5. Where v82 goes further than anything we attempted

The F→H(z) bridge and the cluster-schedule (§2, items 1-2) are the clear
cases — this project never built or attempted either, correctly
recognizing (§0) that no real target existed in v6 to reconstruct. Beyond
that, v82's Sec. IV (A-U) is a substantially more thorough *observational
and methodological self-audit* than anything this project produced from
v6 alone — the SH0ES/DESI/Cosmic-Chronometer joint fit, the seven-way
robustness table (Table V, `z_{SH0ES}` choice), the explicit AIC/BIC
non-reporting justification, and the "circumstances where this framework
should not be expected to be accurate" catalogue (Sec. IV.H) go well
beyond what this project's own v6-based work had a target to test against
at all, since v6 never published a comparably worked-out fit.

## 6. Open questions this comparison surfaces (not answered here)

1. **Does v82's own `β₁,β₂,H₀,anchor` triple suffer the same
   identifiability degeneracy** `FINDING_P133` proved for our own
   `(A,g,κ)`? Not checked — would require reading v82's own units
   convention carefully enough to set up the same Jacobian-rank test.
2. **[WORKED, 2026-08-30, `experiments/20260803-bridge/FINDING_P156`]**
   Does TJB's own accretion-kinematics F→H(z) bridge agree or disagree
   with this project's own Shtanov–Sahni `G_eff=0` result? **Partially
   sharpened, not closed.** `P156` found: (a) v82's own force-law tiers
   match our own kernel structure exactly ([VERIFIED-PDF]+[VERIFIED-sympy]
   re-derivation), and our closure criterion zeroes the same
   dipole/quadrupole tiers when applied to v82's own printed kernels; (b)
   an initial claim that v82 asserts `s(z)=d₀/(1+z)` exactly is **false**
   — v82's own text (p.5–6) explicitly disclaims this reading, using
   `a(z)` only as a redshift-mapping device, not as a statement about
   `s(t)`'s own force-sourced trajectory; (c) the genuinely open question
   — whether our isotropic-average/`r→∞` closure criterion says anything
   about v82's finite-separation, single-pair, externally-oriented
   dipole construction — is **not** answered by `P156` either, and is
   named there as the concrete next calculation. This is exactly the
   case `docs/127`'s own scope caveat (pearled 2026-08-30) flagged as
   untested. **Addendum, `FINDING_P164` (2026-08-30):** of `P160`'s own
   3 leftover open items, 2 are directly addressed by v82's own Sec. IV.H
   limitations catalogue (temporal lag: closed, via TJB's own "retarded
   times... formal limit" statement; real-node anisotropy: elevated to a
   TJB-acknowledged, still-unquantified limitation, not resolved) and 1
   (node-dependent `κ(x)`) is closed within the "typical node" scope this
   project's own work and v82's own fit itself both operate in (v82's
   own Eq. 10, a single baseline `m_0` for both nodes), though it remains
   open for a hypothetical real, diverse-cluster application.
3. **[WORKED, 2026-08-30, `experiments/20260803-bridge/FINDING_P162`]**
   Would this project's own covariant-completion tensions (`P148`,
   `docs/131`) survive being re-expressed in v82's own node/kinematic
   language, or are they specific to the particular construction
   `two_field_action_closure.py` chose? **Not specific to our
   construction — the tension survives, and no working mechanism (standard
   or exotic) was identified.** `P162` found: the force law both
   `docs/130`/`docs/131` tested is unchanged in v82 (`P159`); v82's own
   Sec. IV.F "pressure sources gravity" passage, read as its single most
   literal candidate mechanism (Tolman/Komar active mass, `ρ+3P/c²`),
   fails for ordinary positive thermal pressure — but that mechanism is
   monopole-level while the passage motivates a dipole effect, and v82's
   own explicit denial of internal anisotropy ("no intrinsic axis")
   forecloses the standard bridge between the two, so the failure is
   illustrative rather than a direct refutation. v82's own many-body node
   ontology does **not** supply a new escape route via simple statistical/
   mean-field averaging (that reduces to the same tested mechanism, a
   point the first draft got wrong and a dispatched skeptic caught); the
   one genuinely distinct remaining channel — correlation/fluctuation-
   induced (gravitational-Casimir-type) forces — is **not unspecified**,
   per a literature-check correction (2026-08-30): a real, peer-reviewed
   "gravitational Casimir-Polder" effect exists (Ford-Hertzberg-Karouby,
   PRL 116, 151301, 2016, `arXiv:1512.07632`) and is attractive for
   similar-composition bodies (matching the EM precedent's own sign); the
   one known repulsive term (`arXiv:2501.02470`, Hao-Hu-Yu 2025) is
   explicitly subdominant for identical polarizabilities; and the entire
   effect is a one-loop quantum-gravity correction, negligible at
   galaxy-cluster scales regardless of sign — checked, not merely
   unbuilt, and confirmed wrong-signed and too small.
4. **[WORKED, 2026-08-30, `experiments/20260803-bridge/FINDING_P163`]**
   Do the `A·g²` growth-rate ceiling (bottleneck 3) and v82's own fit
   parameters connect at all, once unit conventions are reconciled?
   **No — not merely a units gap, a tier mismatch.** `A·g²` is a
   monopole-tier quantity in this project's own construction
   (`F_MULT(r)=A·c_G·g²·m₁m₂/r²`), but v82's own monopole term carries
   zero free coefficient (`F⁽⁰⁾=−Gm_Am_P/s²`, Eq. 2) — only `β1, β2,
   H0,anchor` are fitted, and all three live at the dipole/quadrupole
   tiers. There is no v82-native number occupying the tier `A·g²`
   constrains. Reinforced by `β1, β2` being a structurally different kind
   of object (dimensionless directly-fitted coefficients, no field
   theory behind them) than `A, g, κ` (couplings in a never-completed
   covariant Lagrangian). A skeptic-caught correction narrowed the
   verdict to v82's *written model structure* specifically — whether
   v82's overall statistical fit could practically be degenerate with an
   unmodeled monopole effect via `H0,anchor` is a distinct, unexamined
   question.

None of these is answered in this document — per the project's own
standing methodology, each would need its own claim/estimand and
positive-controlled test before being trusted, not a side effect of a
comparison read.

## What this document does NOT establish

1. **Not a claim about which version (v6 or v82) is "more correct"** —
   both are TJB's own work, at different stages of development; this
   project's role is reconstruction and honest reporting, never
   authority over that judgment (`NO_AUTHOR_ERROR`).
2. **Does not reconcile the two F→H(z) mechanisms** (§6, item 2) — flagged
   as open, not resolved.
3. **Does not check whether v82's own fitted parameters are
   identifiable** (§6, item 1) — flagged as open, not resolved.
4. **Does not itself decide whether to reopen bottleneck 1** — that
   remains a separate gate decision, per `docs/149`'s own scope note.
