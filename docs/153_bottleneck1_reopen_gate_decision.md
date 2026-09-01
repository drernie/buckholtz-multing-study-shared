# docs/153 — Bottleneck 1 (F→H_MULT(z)) reopen gate decision

**Date:** 2026-09-01
**Origin:** explicit user request ("go" on the recommendation from
`boyko-project-radar`'s atomize scan) to close the outstanding gate
decision `docs/147`/`docs/149` both flagged as pending since
2026-08-30 — a formal decision was never made, only deferred, and
`docs/149`'s own §3 states plainly: *"This document does not itself
reopen bottleneck 1 — that is a decision for the project's own gate
process... a decision about what to do with that is still open."*
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (a process/gate decision, not a new
physics claim — no new computation is performed by this document)
**Method:** applies `docs/151`'s three-field status-separation rule to
the specific reopen question, using only evidence already established
in `docs/149`, `docs/150`, and `FINDING_P156` — no new claim is made
about v82's own theory or about this project's own reconstruction
beyond what those three documents already record.

---

## Correction (2026-09-01, context-asymmetric skeptic-caught, applied
before finalizing — code/citations verified present in the dispatch)

A skeptic review of the first draft raised 4 concerns. Each independently
re-verified before accepting or rejecting, per this project's own hard-won
constraint ("a skeptic's own critique needs independent re-verification
too — cuts both ways").

**CONFIRMED, no change needed** — the "REJECTED-AS-SAME" framing in §2's
ontological-status field is faithful to `docs/149`'s own explicit
language ("a *different mechanism*... not a confirmation or
contradiction... a *structurally different question*"), not an
overclaim.

**REFUTED BY DIRECT CHECK** — the skeptic argued §3's GO-criterion-2
application stretches "competing models" to cover a single yes/no
question with two answers. Checked directly against `docs/147`'s own
exact wording (`grep`-confirmed): the criterion reads *"конкурирующие
модели/**чтения**"* — competing models **or readings** — and this
document's own §3 citation already includes "models/readings," not
"models" alone. The skeptic's critique evaluated an English paraphrase
that dropped the "/readings" half, not this document's actual text.
Separately: two mutually-exclusive live possibilities, only one of which
is true, is the normal and expected shape of any Cheapest Differentiating
Test setup (`falsification-ladder.md`'s own CDT Protocol, which `docs/
147`'s own criterion 2 cites as its analog) — not a defect specific to
this case.

**ACCEPTED, FIXED** — the skeptic's strongest point: this document does
90% of the pre-motivation work for the finite-r calculation (names it,
cites its exact `FINDING_P156` tag, argues it's GO-eligible), leaving the
"separate, explicit go-ahead" disclaimer with little structural work left
to do — a real soft-GO / stop-rule-erosion risk, not a technicality.
Fixed: added §3a, explicit pre-conditions that must be checked (not just
a calculation to run) before any future GO, giving the required "separate
explicit go-ahead" genuine gating content instead of a rubber stamp.

**ACCEPTED, VERIFIED** — the skeptic correctly noted the "nothing changed
since 2026-08-30" claim (Section 1's last row) was asserted from
`activeContext.md`'s own summary, at the same confidence weighting as the
PDF-verified v82 claims, without independent verification — an asymmetry
`docs/151`'s own status-separation rule exists to catch. Fixed by direct
check: `grep -l -i "bottleneck 1\|F→H_MULT\|F->H_MULT\|accretion-
kinematic\|F→H(z) bridge"` across all of `FINDING_P175`-`P187` returns
**zero matches** — none of those 13 findings mentions bottleneck 1, the
F→H(z) bridge, or accretion-kinematics language at all. The row's evidence
marker is upgraded from activeContext-summary to `[VERIFIED-BASH]`.

---

## 0. The question being decided

`docs/147`'s own text for bottleneck 1 states it is **BLOCKED, not
derived**, with an explicit reopen condition: *"не появилось новой
информации, разрешающей direct derivation reopening (`k_A(z)/r_A(z)/
D_cAB(z)` от TJB, или новая публикация)"* — no new information enabling
direct-derivation reopening (`k_A(z)/r_A(z)/D_cAB(z)` from TJB, **or**
a new publication).

`docs/149` already established, as a plain factual matter, that this
condition is met — v82 is simultaneously a new publication and a
source of explicit `k_A(z)/r_A(z)/m_A(z)` evolution laws — but
explicitly declined to make the reopen decision itself, deferring it
to "the project's own gate process." This document **is** that gate
process, run to completion.

## 1. Evidence assembled (no new computation — citing `docs/149`/`150`/`FINDING_P156` only)

| Question | Answer | Source |
|---|---|---|
| Does a real, published F→H(z) bridge from TJB now exist? | YES — Sec. II.B-C of v82, an explicit accretion-corrected two-body kinematic derivation, `ä/a=s̈(z)/s(z)` integrated to `H(z)²−H₀²` | `docs/149` §2 (II.C row), read from PDF page images |
| Are the explicit `m_A(z)/r_A(z)/k_A(z)` evolution laws `docs/147`'s condition asked for actually present? | YES — Eqs. (10)-(14), each classified by TJB's own Class I/II/III provenance system | `docs/149` §2 (II.D row), §3 |
| Is TJB's bridge mechanism the SAME as this project's own reconstruction route? | NO — TJB's route is accretion-corrected two-body kinematics (Sec. II.B-C); this project's own route (`docs/124`-`127`) is the Shtanov-Sahni generalized cosmic-energy equation, a structurally different framework | `docs/149` §2 (II.B row: "a *different* framework from TJB's own accretion-kinematics one"), `docs/150` §1 (F→H(z) bridge row) |
| Has this project already attempted to compare the two bridges directly? | YES, once — `FINDING_P156` (2026-08-30) | `docs/150` §6 item 2, `FINDING_P156` |
| What did that comparison find? | **Tier structure matches** (v82's own force-law tiers, Eqs. 1-4, are structurally identical to this project's own kernel assignment — `[VERIFIED-PDF]`+`[VERIFIED-sympy]`). **One agent-proposed claim was checked and found FALSE**: v82 does NOT assert `s(z)=d₀/(1+z)` exactly — v82's own text (pp. 5-6) explicitly disclaims this, using `a(z)` only as a redshift-mapping device. **The actual comparison remains unresolved**: whether this project's own S-S closure criterion (built for an isotropically-averaged, `r→∞` population) says anything about v82's own construction (finite separation, ~40-45 Mpc, single oriented pair, no averaging) is not established — this is exactly `docs/127`'s own scope caveat, named as untested. | `FINDING_P156` §4 verdict tags: `TIER-STRUCTURE-MATCHES`, `SS-CLOSURE-APPLICABILITY-TO-V82S-CONSTRUCTION-UNRESOLVED`, `ONE-LOAD-BEARING-AGENT-CLAIM-WAS-FALSE`, `FINITE-R-ANISOTROPIC-REGIME-REMAINS-OPEN` |
| Has anything changed since 2026-08-30 that bears on this specific bottleneck? | NO — the `P175`-`P187` v82-degeneracy thread (this session, closed 2026-09-01) attacked a *different* bottleneck (bottleneck 3, the `(β1,β2)` identifiability degeneracy in this project's own reconstruction). Directly checked, not merely summarized from `activeContext.md`: `grep -l -i "bottleneck 1\|F→H_MULT\|F->H_MULT\|accretion-kinematic\|F→H(z) bridge"` across all 13 files `FINDING_P175`-`P187` returns **zero matches**. `docs/149`/`150`/`FINDING_P156`'s 2026-08-30 state is still the most current evidence on this specific question. | `[VERIFIED-BASH]` grep across `experiments/20260803-bridge/FINDING_P17[5-9]*.md` + `FINDING_P18[0-7]*.md`, 2026-09-01 |

## 2. Applying `docs/151`'s status separation to the reopen decision itself

The reopen decision is not one claim but three separable ones, exactly
the pattern `docs/151` was written to keep from being silently
collapsed. Answered here as three explicit fields, per the rule:

> **Empirical/Model status:** VERIFIED — TJB has published a real,
> explicit F→H(z) derivation (v82, Sec. II.B-C), read directly from
> the PDF, not from a markdown conversion or a summary. `docs/147`'s
> own named reopen condition is satisfied as a plain factual matter.
> This is not in dispute and requires no further checking to accept.
>
> **Ontological/mechanistic interpretation status:** REJECTED-AS-SAME,
> OPEN-AS-COMPATIBLE — v82's bridge is **not** the same mechanism as
> this project's own S-S route (established, not merely undetermined —
> `docs/149`/`150` both state this directly). Whether the two
> mechanisms are *compatible* in the region where they physically
> overlap (finite separation, single pair) is a **separate, still-open
> question** — `FINDING_P156` attempted exactly this comparison once
> and could not resolve it, because this project's own closure
> criterion was built for a different regime (isotropic average,
> `r→∞`) than v82's construction occupies.
>
> **Causal/cosmological claim status:** NON-IDENTIFIED — whether v82's
> own bridge, worked through in the finite-r single-pair regime,
> reintroduces `k_A(z)`-dependence into the background in a way that
> would conflict with this project's own `G_eff=0` result is not
> established either way. This is `FINDING_P156`'s own named "concrete
> next calculation" (its `FINITE-R-ANISOTROPIC-REGIME-REMAINS-OPEN`
> tag) — not attempted by that file, and not attempted here either.

## 3. Verdict

**The original bottleneck-1 wording is factually superseded and must
be restated, not merely marked "reopened."** The 2026-08-23 framing
("central bridge not established in published form") is no longer
true — TJB has published one. Marking the OLD bottleneck simply
"reopened" without restating it would misrepresent what is actually
still blocked, repeating exactly the kind of silent-collapse `docs/151`
exists to prevent.

**Applying `docs/147`'s own GO-criterion 2** ("differentiates at least
two competing models/readings currently both compatible with
established constraints") **to the candidate next step**: the old
bottleneck ("does a bridge exist at all?") no longer differentiates
anything — the answer is settled YES. The **new**, precisely-scoped
question DOES differentiate two live readings: (a) this project's own
S-S closure result and v82's bridge are compatible in their overlap
regime — v82's finite-r construction does not reintroduce
`k_A(z)`-dependence the S-S closure would consider a violation; or
(b) they are incompatible — the two mechanisms give genuinely
different predictions in that regime, which would mean this project's
own `docs/127` closure result does not generalize as far as it was
implicitly assumed to.

**GO — bottleneck 1 is formally RESTATED, not simply reopened:**

```
OLD (docs/147, 2026-08-23): "F→H_MULT(z) — central bridge not
established in published form." — CLOSED, superseded by fact
(docs/149). Retained in docs/147 as historical record, not deleted.

NEW (this document, 2026-09-01): "F→H_MULT(z), finite-r/single-pair
compatibility — does this project's own S-S closure criterion
(isotropic-average, r→∞) say anything about v82's own bridge
construction (finite separation ~40-45 Mpc, single oriented pair, no
population averaging)? Does v82's bridge, worked through on its own
terms in that regime, reintroduce k_A(z)-dependence in a way `docs/
127`'s own G_eff=0 result would consider a violation?" — OPEN,
GO-eligible under docs/147's own criterion 2. Concrete next
calculation named by FINDING_P156's own FINITE-R-ANISOTROPIC-REGIME-
REMAINS-OPEN tag: a finite-r, non-averaged, single-pair version of
the closure calculation this project has not yet built.
```

This is **not** an instruction to run that calculation now — per
`docs/147`'s own stop-rule, naming a GO-eligible next step is not the
same as authorizing it; per this session's own `activeContext.md`
("Nothing pre-authorized right now... a fresh direction awaits
explicit instruction"), running it requires a separate, explicit
go-ahead.

## 3a. Pre-conditions for an actual GO (not satisfied by this document)

Added per the skeptic's own soft-GO concern above: naming a calculation
precisely enough to be gate-able is not the same as having done the
gating work. Before any future "go" on the finite-r/single-pair
calculation, the following must be checked and answered — none of them
are answered here:

1. **Does a finite-r analog of the S-S closure calculation even exist
   in closed form**, or would it require a genuinely new derivation
   (not just re-evaluating `docs/127`'s existing result at finite `r`)?
   `FINDING_P156` did not check this.
2. **Is the single-pair, externally-oriented regime tractable** with
   this project's existing machinery (`two_charge_completion.py`,
   `two_field_action_closure.py`), or does it require a construction
   this project has not built at all?
3. **What would each of the two possible outcomes (compatible /
   incompatible) actually change** about this project's own standing
   results (`docs/127`'s `G_eff=0` claim, `P152`-`P155`'s S1/S2
   closure work) — is the calculation's cost proportionate to its
   consequence, per `falsification-ladder.md`'s own Cheapest
   Differentiating Test Protocol?

A future "go" on this specific calculation should answer these three
first, not treat this document's own framing as sufficient preparation.

## 4. What changes in `docs/147`'s own bottleneck tracking

`docs/147`'s bottleneck-1 entry should be annotated (not rewritten) to
point here: the original entry stays as historical record (per this
project's own no-silent-correction convention — see every `FINDING_*`
file's own dated Correction sections), with a pointer to this
document's restated version as the current status.

## What this document does NOT establish

1. **Not a claim about v82's own theory being right or wrong**
   (`NO_AUTHOR_ERROR`) — entirely a process decision about this
   project's own bottleneck tracking.
2. **Does not run the finite-r/single-pair calculation** — names it as
   the concrete next GO-eligible step, per §3, does not attempt it.
3. **Does not reconcile `β1/β2` with this project's own `β_d/β_q`** —
   `docs/150` §6 item 1 remains a separate, still-open question, not
   addressed by this gate decision.
4. **Does not authorize any specific next computation** — per `docs/
   147`'s own stop-rule, GO-eligibility is necessary, not sufficient;
   an explicit user go-ahead is still required before building the
   finite-r closure calculation.
5. **Does not affect bottleneck 3** (Absolute scale) or **bottleneck 4**
   (IC-sensitivity) — both remain in their own, separately-decided
   states (`docs/147` points 3 and 4; bottleneck 3's own confound-
   breaking sub-thread, `P175`-`P187`, closed this session on entirely
   separate grounds).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
