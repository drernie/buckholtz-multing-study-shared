# docs/137 — TJB Immediate Help Brief (GREEN tier)

**Date:** 2026-07-24
**Origin:** boyko-agent full-project harvest (`scratchpad/boyko_MAXHELP_dossier_for_TJB.md`,
"internal provisional harvest v1"), triaged after user-directed epistemic review found several
items overclaimed their evidence tier. Companion docs: docs/138 (optional technical modules,
AMBER tier), docs/139 (internal null/hypothesis registry, RED tier — never author-facing).
**Purpose:** the only tier of the harvest that is candidate content for outward correspondence
with Dr. Buckholtz — still requires Sergey's own final read plus a cooling-off pass before
anything is actually sent; nothing here is pre-approved for send.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · NO_AUTHOR_ERROR · OUR_RECONSTRUCTION

---

**Evidence scale used below** (replaces the coarser VERIFIED/INFERRED/MEMORY/UNKNOWN used in v1):
`SOURCE-LOCATED` (claim found in a document) → `RECOMPUTED-SAME-PIPELINE` (our own script/formula
re-run with our own assumed inputs — confirms arithmetic, NOT the input choice) →
`INDEPENDENTLY-REDERIVED` (worked from equations only, no shared code) →
`INDEPENDENTLY-REIMPLEMENTED` (separate code, same equations) → `EMPIRICALLY-CROSS-CHECKED`
(tested against a dataset neither side chose to fit) → `AUTHOR-CONFIRMED` (TJB has verified it).
Every item below is `RECOMPUTED-SAME-PIPELINE` or weaker unless stated otherwise — **none of this
is `AUTHOR-CONFIRMED`, `EMPIRICALLY-CROSS-CHECKED`, or a global statistical proof.**

---

## 1. Caption fix for the adopted control figure

**Finding:** the caption drafted for our control figure states the crossing "reflects genuine
dynamical differences between MULTING and ΛCDM." The figure only establishes that a pure H0-anchor
change cannot produce the crossing; with 3 fitted parameters (β1, β2, H0_anchor) the crossing
could also reflect fitting flexibility rather than dynamics — and this is what your own Table IV
already reports plainly ("this parameter's freedom is doing much of the work").
**Suggested wording:** end the caption at "...must instead reflect a difference in the
dimensionless expansion history E(z)," without asserting which cause (dynamics vs. fit freedom)
produced that difference.
**Evidence tier:** `SOURCE-LOCATED` (your Table IV, your own caption draft) + direct logical
reading, not a new computation.

## 2. Ωm consistency for the Table VI ΛCDM row

**Finding:** the "ΛCDM, fixed Planck" row in Table VI uses (H0=67.4, Ωm=0.30) → H(2.33)=231.3 →
−1.64σ vs. the cited DESI value. The Planck-2018 published pair is (67.36, **0.315**); using it
gives H(2.33)=236.4 → **−0.58σ**.
**What this does and does not mean:** the arithmetic shift is confirmed
(`RECOMPUTED-SAME-PIPELINE`). What it means for the MULTING-vs-ΛCDM comparison is genuinely
open — a more accurate ΛCDM row could equally be read as making ΛCDM's own agreement with DESI
better, which is not automatically favorable or unfavorable to MULTING's relative case without a
shared likelihood framework. State the correction as a fact, not as an argument for either side.
**Suggested wording:** "The Planck row in Table VI uses Ωm=0.30; the published Planck-2018 value
is 0.315, which moves that row from −1.6σ to −0.6σ against the cited DESI point. Flagging this in
case it matters for how a referee reads the ΛCDM comparison — the direction of any resulting
effect on the MULTING-vs-ΛCDM comparison itself would need a shared likelihood to assess, which
we have not attempted."

## 3. r_d-dependence of the DESI z=2.33 point

**Finding:** DESI DR2 reports the invariant D_H(z)/r_d = 8.632±0.098. Converting to H(z) in
km/s/Mpc requires choosing r_d. At the standard r_d=147.09 Mpc: H(2.33)=236.1±2.8. At a lower,
early-dark-energy-style r_d (e.g. 139.5 Mpc): H(2.33)=249.0. The paper's cited 239.2±4.8 implies
a still-different r_d/release convention.
**Why this is useful regardless of outcome:** the DESI comparison in Table VI is r_d-convention-
dependent, not a single model-independent number. Stating the invariant (D_H/r_d) alongside the
converted H(z) removes that ambiguity for a reader.
**Suggested wording:** "The DESI point's value in km/s/Mpc depends on the assumed sound horizon
r_d; the invariant D_H(z)/r_d=8.632±0.098 is convention-independent. Noting the specific r_d and
release used for the cited 239.2±4.8 would let a reader reproduce the conversion exactly."
**Evidence tier:** `RECOMPUTED-SAME-PIPELINE` (`scripts/hz_desi_and_redcurve_space.py`, re-run
2026-07-24).

## 4. Offer: independent clean-room reimplementation

**Offer, with explicit conditions attached** (per this project's own Independent Verification
Strength Ladder, falsification-ladder.md — a "clean-room" claim is only as strong as its stated
conditions):
- no import of your code or internal tables;
- built only from the equations printed in the paper (Eqs. 5–9 kinematic route, Eqs. 12–14
  thermal k_X);
- an explicit discrepancy log against your reported numbers, not a silent match/no-match;
- scope: reproduce χ²_MULT=13.565, χ²_ΛCDM=14.500, the Case1/Case2 degeneracy structure, and the
  DESI extrapolation — nothing beyond what the paper specifies.
**What this would and would not establish:** a match would be `INDEPENDENTLY-REIMPLEMENTED`
evidence that the paper's stated procedure is well-specified and reproducible from the text alone
— a genuinely strong but narrow claim. It would say nothing about whether the procedure itself is
the right physical model.
**Suggested wording:** "If useful, we would be glad to build an independent, code-separate
reimplementation from the paper's equations alone (with a documented discrepancy log) and confirm
the three headline χ² numbers and the degeneracy — offered at your discretion, findings reported
only to you."

## 5. Cosmic-chronometer covariance (open question, not a predetermined outcome)

**Finding:** both models sit at χ²/dof≈0.5 on the 31-point CC compilation, consistent with
conservative or correlated point-to-point errors. Moresco et al. (2020) publish a covariance
recipe for this exact dataset. Whether folding it in would strengthen, weaken, or leave unchanged
the Δχ²=0.94 gap between MULTING and ΛCDM is an **empirical question we have not answered** — do
not present a predicted direction.
**Suggested wording:** "The CC compilation has documented covariance (Moresco et al. 2020);
whether including it changes how significant the 0.94 χ² gap is, in either direction, is an open
question — we could help implement it if useful, with no assumption about which way it would
move the comparison."
**Evidence tier:** `SOURCE-LOCATED` (Moresco 2020 exists; we have not run the covariance-aware fit).

---

## What was deliberately left out of this brief

Several dossier items are genuinely interesting but require either (a) a separate technical
memo with its own caveats stated in full — see docs/138 (AMBER tier: β-degeneracy analogy,
real-cluster k_X cross-check, background-invisibility scoping, growth-branch map, Blanchet
literature note, Eq.32/7:9:17 look-elsewhere framing, N_opt reinterpretation) — or (b) should not
leave the project at all in their current form — see docs/139 (RED tier: Birge-ratio-as-proof,
global p-values from a grid whose definition needs its own audit trail, S3→6-isomer "prediction",
"exhausted" literature-search claims, a global EP no-go).
