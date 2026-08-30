# FINDING P160 — narrowing (not fully closing) P159's last two named
# gaps: asymmetric coupling is inconsistent with MULTING's current
# written equation; angular averaging is not needed to match MULTING's
# own stated idealization — neither claim is a physical exclusion

**Date:** 2026-08-30
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 math (symbolic derivation) + direct primary-source
reading
**Verdict (final, post-skeptic — language downgraded from the original
draft's absolutist framing, substance unchanged):** `κ_A≠κ_P CANNOT
REPRODUCE MULTING'S CURRENT PUBLISHED DIPOLE EQUATION'S FUNCTIONAL FORM
(shown, not assumed) — this makes it not viable AS AN EXPLANATION FOR
MATCHING THAT EQUATION specifically, but does NOT independently show
asymmetric coupling is physically impossible, since the single-
coefficient form is the preprint author's own modeling choice (repeated
across two drafts, not shown first-principles-derived). QUADRUPOLE TIER
ROBUST (depends only on κ_A·κ_P). ANGULAR AVERAGING NOT NEEDED TO MATCH
MULTING'S OWN STATED IDEALIZATION (dipole axis = separation direction,
by the preprint's own text) — this settles internal consistency with
that idealization, not whether the idealization itself is physically
complete. THREE ITEMS REMAIN FORMALLY OPEN (not closed by this file):
(i) node-property-dependent κ(x) (weakly motivated, untested); (ii)
whether the preprint's own zero-orientation-variance idealization holds
for a real, non-ideal node; (iii) temporal/dynamical lag in a single
pair's own induced-dipole alignment under relative motion — a third
case, distinct from both "static single pair" and "population of
pairs," untested by this file or by `FINDING_P157`/`P158`.`
**Correction (2026-08-30, context-asymmetric skeptic-caught):** the
original verdict used "NOT-A-VIABLE-ALTERNATIVE," "EXCLUDED," "REQUIRED,"
and "NOT-APPLICABLE" — language a dispatched skeptic found overstated:
the actual results are conditional on (a) taking MULTING's *currently
published* equation as the fixed comparison target (not an independent
physical exclusion of asymmetric coupling as such), and (b) matching
MULTING's own *stated idealization* for the dipole axis (not an
independent verification that the idealization has zero real-world
variance). Both are corrected in place below, not silently, along with a
newly-identified third open item (temporal lag) the skeptic surfaced.
**Continues:** `FINDING_P159` §5 item 3 ("does not check angular/
orientation-averaging factors or `κ_A≠κ_P` asymmetry... a genuinely
different, currently-unknown-magnitude source of the `19.5×` gap").
**Script:** `P160_asymmetric_kappa_and_angular_averaging.py` —
symbolic re-derivation (sympy), positive control (symmetric case
recovers the original exactly), does not touch the 881-test suite.

## 1. Asymmetric coupling (`κ_A≠κ_P`) — checked by direct computation

Re-ran `two_charge_completion.py`'s own mirror-symmetric two-point-charge
derivation with the charge substitution generalized from a single shared
`κ` to two independent `κ_A`, `κ_P` (`q_A=-κ_A k_A/c²`, `q_P=-κ_P k_P/c²`).
`[VERIFIED-sympy]`:

```
dipole tier   C3 = 2·(κ_A·k_A·m_P·r_A + κ_P·k_P·m_A·r_P)/c²
quadrupole    C4 = 6·κ_A·κ_P·k_A·k_P·r_A·r_P/c⁴
```

**Quadrupole is robust**: `C4` depends only on the *product* `κ_A·κ_P`,
which is a single well-defined number regardless of whether `κ_A=κ_P`
individually — matches MULTING's own single-`β₂`/`β_q²` functional form
(v6 Eq. 16/20, v82 Eq. 4) with no constraint needed.

**Dipole is not.** `C3`'s two terms carry *different* coefficients,
`2κ_A/c²` and `2κ_P/c²` — `[VERIFIED-sympy]`, extracted via `.coeff()`
after expansion. v6's own Eq. 15/18 and v82's own Eq. 3 write **one**
`β_d`/`β₁` multiplying the *entire* symmetric sum
`(k_A m_P r_A + k_P m_A r_P)` — not two independently-normalized
per-node coefficients. Algebraically, `2κ_A/c² = 2κ_P/c²` **iff**
`κ_A=κ_P`; asymmetric coupling produces a force that is **not
expressible in MULTING's own written dipole equation at all**, not
merely a differently-valued one.

**Consequence (corrected scope):** symmetric coupling (`κ_A=κ_P`), used
throughout `FINDING_P159`, is not an arbitrary simplifying assumption —
it is the **only** choice, among the specific per-node-constant
parametrization tested, under which the two-point-charge construction
reproduces MULTING's *currently published* dipole equation's functional
form. **This shows asymmetric κ is inconsistent with matching v6/v82's
own written equation as it stands — it does not independently show
asymmetric coupling is physically excluded**, since that single-
coefficient form is the preprint author's own modeling choice (repeated
across both v6 and v82, which is evidence of a deliberate, consistent
convention — but consistency across one author's own drafts is not
independent confirmation the convention is first-principles-required).

**Not tested, genuinely open**: a node-property-*dependent* `κ(k,m,r,...)`
(not a global constant) that happens to produce equal effective
coefficients for a specific pair without `κ_A` literally equaling `κ_P`
as a universal constant. This is weakly motivated — `κ` was structurally
introduced as a factor separate from the node-dependence already carried
by `k_A`, `m_A`, `r_A` themselves, and any such `κ(x)` would need to
reduce to an effectively-constant value across whatever node population
underlies v82's own single fitted `β1` — but it was not tested here, and
is named rather than dismissed.

## 2. Angular averaging — not applicable, per v82's own text `[VERIFIED-PDF p.17]`

`two_charge_completion.py`'s own construction places both point-charges
of each node **collinear with the separation vector** — no free
orientation angle exists in the code (`interaction()`'s own docstring:
"every separation is `z_b − z_a`," a 1-D construction). This looked, on
its face, like a simplifying assumption that might need checking against
a more general 3-D, angle-dependent (and possibly averaged) geometry.

v82's own Sec. IV.F (p.17, "Bases for gravitationally dipole effects"),
read directly, settles it — this is not a simplification this project
introduced; it is v82's own stated physical picture:

> "Thermal motion is, physically, a pressure term, and... does not favor
> any one direction: a node's own thermal energy has no intrinsic axis.
> (To the extent that one has concerns about a possible tension -- an
> isotropic quantity contributing to a dipole-like force -- one might
> consider that the tension might resolve once an axis is recognized as
> coming from **outside** the thermal energy itself. One might consider
> that **the line connecting the two nodes**, not any internal property
> of either node, **supplies the direction**, with a node's thermal
> energy setting only the magnitude of a force acting along that
> externally-supplied axis.)"

MULTING's own dipole term, by this account, has no independent
orientation degree of freedom **in its own idealized picture** — the
axis *is defined to be* the separation direction, for every pair. v82's
own force equations (Eqs. 2-4) correspondingly contain no angular
variable, consistent with this reading. `two_charge_completion.py`'s
collinear (radially-aligned) construction matches this idealization
exactly — it is not an unexamined simplification of some more general
angular scenario v82 also entertains.

**Corrected scope — two things this settles, and one it does not:**
1. It settles the *mean/nominal* direction question: there is no free
   angle to choose or average over when comparing the project's
   construction against v82's own equations, because both sides agree
   the axis is deterministically the separation direction.
2. It does **not** independently verify that a real, physical node (finite
   thermal motion, not a literal ideal point-dipole) has *zero variance*
   around that nominal axis — v82's own text asserts this ("thermal
   energy sets only the magnitude"), but this file takes that assertion
   at face value rather than independently testing it. If real nodes have
   any variance around the nominal axis, that is a property of v82's own
   idealization's completeness, not of whether this project's
   construction faithfully matches what v82 itself claims.
3. **A third, genuinely distinct and untested case, not covered by
   either this section or by `FINDING_P157`/`P158`'s population-level
   work**: whether a *single, fixed* pair's own induced-dipole axis
   tracks the separation direction *without lag* as the pair's relative
   configuration evolves over time (orbital motion, relative drift
   between the two nodes). "One static pair" (this section) and "a
   population of many differently-oriented pairs" (`P157`/`P158`) are
   not exhaustive — a temporal/dynamical misalignment for one evolving
   pair is a third bucket, unaddressed anywhere in this project's work.

## 3. Consequence for `FINDING_P159`'s ratio finding (narrowed, not fully closed)

Both items `FINDING_P159` named as open are **narrowed, not fully
closed**: `κ_A≠κ_P` (as a per-node constant) cannot reproduce MULTING's
*currently written* dipole equation, and angular averaging is not needed
to match MULTING's *own stated idealization* for the dipole axis. Neither
of these is an independent, physics-level exclusion — both are
statements about consistency with v6/v82's own equations and text as
currently published, which is the correct scope for a `NOT_AUTHOR_ERROR`
comparison of this project's own reconstruction against those documents,
but should not be read as ruling out every conceivable physical
alternative. Three items remain explicitly open (§1, §2): node-dependent
`κ(x)`, whether v82's own zero-variance idealization holds for a real
node, and temporal/dynamical lag for a single evolving pair. Combined
with `FINDING_P159`'s own resolved gaps (independent primary-source
confirmation; `κ` proven to cancel in the ratio), the `19.5×` ratio
discrepancy between this project's own two-point-charge prediction
(`β_q/β_d=√6/2`) and v82's fitted analog (`√β₂/β₁≈0.063`) stands on
firmer ground than before this file, but not as a fully closed case.

## What this file does NOT establish

1. Not a claim about v82's own theory being wrong (`NO_AUTHOR_ERROR`).
2. **Does not rule out other, un-named degrees of freedom** — e.g.
   whether the two-point-charge model's own choice of exactly *two*
   point charges per node (vs. some other multi-charge distribution),
   or the specific lever-arm identification `d_A=r_A` (checked
   separately, `FINDING_P159` §2.1, for uniform rescaling only), might
   still account for the gap. Not exhaustive.
3. **Does not check `FINDING_P133`-type identifiability** for v82's own
   `(β1,β2,H0,anchor)` fit (`docs/150` §6 item 1, still open) — if these
   are not jointly identifiable, the specific fitted point compared
   against here may not be uniquely meaningful regardless of this file's
   own findings.
4. Does not attempt to quantify how large a departure from perfect
   radial dipole alignment (if any exists in reality, contrary to v82's
   own idealized picture) could shift the ratio — v82's own text treats
   perfect radial alignment as the model's own assumption, not
   something this file independently verified against real cluster-pair
   geometry.
5. **Three items named in §1/§2 remain genuinely open, not merely
   theoretical**: (a) a node-property-dependent `κ(x)` (untested,
   weakly motivated); (b) whether v82's own asserted zero-variance
   dipole-axis idealization holds for a real, non-ideal node (this file
   takes v82's own claim at face value); (c) temporal/dynamical lag in a
   single pair's induced-dipole alignment under relative motion — a
   third case distinct from both "one static pair" and "population of
   pairs," addressed nowhere in this project's work to date.
