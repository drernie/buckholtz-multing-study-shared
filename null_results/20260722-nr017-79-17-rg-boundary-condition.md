# NR-017 — 7:9:17 as an RG coupling boundary condition: REJECTED (non-post-hoc, 1-loop decisive)

**Date:** 2026-07-22 (T3.1, docs/132 P1 backlog item; follow-up to T3/T3b same day)
**Verdict:** REJECT. The last untested "physics reading" of the empirical `m_W^2:m_Z^2:m_H^2
= 7:9:17` pattern (R002) — a boundary condition on the *running gauge couplings*, not on the
pole masses — fails, decisively, at 1-loop, with no post-hoc scale-picking available.
**Branch:** T3 (docs/132) — third and final sub-test after T3 (look-elsewhere, rank #1) and
T3b (SM one-loop mass-ratio correction, NULL/loop-invariant). Together T3b + T3.1 (this entry)
exhaust every tested mechanism route for 7:9:17.

---

## Claim (falsified)

`tan^2(theta_W)(mu*) = 2/7` (equivalently `sin^2(theta_W)(mu*) = 2/9`, the tree-level value
implied by `m_W^2:m_Z^2 = 7:9`) holds at some physically-motivated high scale `mu*` (e.g.
GUT-adjacent or another independently-motivated scale), found by solving the 1-loop SM gauge
RGE from `m_Z` upward — **not** chosen to fit the answer.

## Why falsified (what is solid)

`tan^2(theta_W)(m_Z) = 0.30088` [VERIFIED-BASH, from PDG 2024 `sin^2(theta_W)_eff = 0.23129`
MS-bar] is **already above** the target `2/7 = 0.28571` — a gap of `+0.0152` — before any
running is applied. The 1-loop beta-function coefficients (`b1=+41/10`, `b2=-19/6` in GUT
normalization) [VERIFIED-WEBSEARCH, consistent with Buttazzo et al. arXiv:1307.3536] give `g'`
rising and `g2` falling with scale — the standard qualitative SM picture (approximate
unification near ~10^16 GeV). Consequence: `tan^2(theta_W)` **increases monotonically** with
scale, moving *away* from `2/7`, not toward it.

| Test | Value | Evidence |
|------|---|---|
| `tan^2(theta_W)(m_Z)`, MS-bar | 0.30088 | `[VERIFIED-BASH]`, coordinator-reproduced, matches `scripts/t3c_rg_boundary_check.py` output exactly |
| Target | 2/7 = 0.28571 | tree-level identification from 7:9 |
| Gap at m_Z | +0.0152 (already wrong side) | `[VERIFIED-BASH]` |
| `tan^2(theta_W)` at 10^16 GeV | ~0.4-0.6 | `[VERIFIED-BASH]`, moves further away, not closer |
| Only crossing found | mu* = 14.61 GeV | below m_Z; unmotivated; opposite direction from unification; inside the threshold-matching region |
| lambda(mu*) Higgs-mass cross-check | m_H predicted = 96.64 GeV vs measured 125.20 GeV | `[VERIFIED-BASH]` — cross-check fails, and is not independently informative anyway (mu* too low for a genuine high-scale test; near m_Z the relation is close to algebraically circular) |
| On-shell alternative starting point (sanity check) | tan^2 = 0.2874, still >= 2/7 | `[VERIFIED-INLINE]` (skeptic review) — does not flip the verdict, just narrows the margin |

**Anti-post-hoc discipline:** `mu*` was obtained by *solving* the running equation, not chosen.
The decisive finding is structural, not numerical: the trajectory starts on the wrong side of
the target and the beta-function signs guarantee it moves further away with increasing scale.
No scale choice, and no scheme choice (checked: MS-bar and on-shell both start above 2/7),
rescues the pattern. 1-loop is dispositive — 2-loop gauge corrections are O(few %) and cannot
reverse a monotonic trend that starts on the wrong side.

## Skeptic Response Matrix (context-asymmetric review, 2026-07-22, code-only)

| Concern | Response | Status |
|---|---|---|
| Sign/direction error in the beta functions (could the code have inverted which coupling rises vs falls)? | Checked against the standard SM 1-loop qualitative picture (g' non-asymptotically-free, rises; g2 asymptotically free, falls; approximate unification ~10^16 GeV) — code matches, not inverted | **CONFIRMED** — FAIL verdict holds |
| Scheme mismatch (MS-bar boundary vs on-shell running) could shift which side of 2/7 the trajectory starts on | Real effect exists (on-shell tan^2(m_Z)=0.2874 vs MS-bar 0.30088), but on-shell is the reading T3b already tested and killed (pole-mass reading); MS-bar is the correct scheme for *this* (high-scale coupling) reading. Switching schemes collapses T3.1 into T3b, doesn't rescue it | **NEEDS-CHECK on wording, does not reopen the pattern** — verdict scope narrowed: T3.1 kills the MS-bar high-scale reading specifically; T3b independently killed the on-shell pole-mass reading; the two together exhaust the RG-adjacent readings |
| Could a different target than 2/7 (an alternative 7:9:17-derived combination) have a real high-scale crossing? | Checked sin^2=2/9 (same statement, same result), g'^2/g^2=9/17 and 7/17 (arbitrary rechoices with no independent motivation from the tree relation) — no natural rechoice rescues the pattern | **CONFIRMED** — FAIL verdict holds |

**True kill condition met:** the core predicate — "a non-post-hoc high scale exists where the
gauge-coupling boundary condition holds" — is directly contradicted by the RGE's own sign
structure, confirmed by adversarial review. This is a clean REJECT, not a narrowed survival.

## Kill Analysis

**What this KILLED:** the hypothesis that 7:9:17 encodes a physically-motivated *gauge-coupling
boundary condition* at any sensible high scale. Combined with T3b (same-day, pole-mass /
on-shell reading killed via loop-invariance), **every tested mechanism-level reading of 7:9:17
is now exhausted** — the pattern has no surviving derivation attempt.

**What this does NOT kill:**
- The **statistical standout** status of 7:9:17 itself (R002/T3: rank #1 in the look-elsewhere
  scan, next-best triple ~8x worse chi^2) — that is a separate, still-standing empirical fact.
- The **Higgs-sector fit** (0.4sigma) — unaffected, it was never part of either RG or mass-ratio
  mechanism claims.
- Any **non-RG, non-mass-ratio** mechanism nobody has proposed yet — this entry only closes the
  two mechanism classes actually tested (T3b: pole masses; T3.1: gauge running).

**Relaxation Map:** revival requires a genuinely new mechanism class not yet conceived (neither
mass-ratio nor RG-running) — no such candidate is currently on the table. Do not re-run the
mass-ratio or gauge-boundary readings without a fundamentally different physical motivation for
the scale/scheme choice.

## Forbidden use

Do NOT cite 7:9:17 as "physically explained" or "derivation-adjacent" — both attempted
derivations (T3b mass-ratio, T3.1 gauge-boundary) failed. Do NOT drop the on-shell/MS-bar
distinction when citing the residual (T3b's +3.7-3.8sigma is scheme-independent in direction,
per T3.1's cross-check, but the *magnitude* is not m_W-choice-invariant — see T3b/docs/132).
Correct citable status: **statistically real (rank #1 look-elsewhere), Higgs-sector-confirmed
(0.4sigma), but mechanism-less** — an integer coincidence, same epistemic class as Eq.32 post-T1.

## Correct next direction

None identified as cheap. The two natural mechanism classes (pole-mass, RG-boundary) are both
closed. Any further work on 7:9:17 would require either (a) a new theoretical mechanism nobody
has proposed, or (b) treating it purely as a statistical curiosity alongside Eq.32 in any
external write-up, honestly labeled as such.

---

*REJECT of the RG-boundary-condition reading, 1-loop decisive, skeptic-confirmed
(context-asymmetric, code-only review). Companion to T3b's same-day REJECT of the pole-mass
reading — together they close the mechanism-search for 7:9:17.*
*Script: `scripts/t3c_rg_boundary_check.py` (ruff-clean, self-reproducing, coordinator-verified).*
*NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION*
