# P36 — κ's visibility to P34's background and P35's static ΔG is genuinely OPEN, not resolved; the original claim silently extended a shell-geometry result to two configurations it does not obviously cover

**Date:** 2026-08-14
**Status:** **CORRECTED after context-blind skeptic review, same day —
the most severe correction of this campaign so far.** Six issues found,
nearly all load-bearing, not merely framing. Most consequential: the
2026-08-10 double-layer result is proven for **one specific
configuration** — dipoles radially aligned from a single common center,
arranged on a shell around that center — and the original version of
this finding silently extended it to (a) P34's **homogeneous** FRW
background, which has **no privileged center** at all, and (b) a point
source's own internal `κ`-content, which requires **assuming** that
content is coherently radially aligned — an unmotivated, physically
implausible assumption for ordinary matter. A second, related error:
this finding conflated the double-layer argument with a genuinely
*different* theorem — `two_field_action_closure.py`'s own docstring
separately states "the random average is zero," an isotropic-orientation
argument that requires no alignment at all and was never examined here.
Full verdict in the new §5 below. **The original headline claim (`κ` is
structurally invisible to P34's/P35's channels) is withdrawn as
unestablished — not confirmed false, but not shown true either.**
**Origin:** third step of the covariant-completion campaign
(`PLAN_final_goal_20260814.md`), the first to address `κ` directly.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P36_kappa_invisible_to_g_sector_channels.py`, ruff clean, all
assertions pass.

## 0. Honest scope

This does **not** establish, in either direction, whether `κ` enters
P34's background or P35's static two-body `ΔG`. It does **not** newly
fix `κ`'s absolute value — P14–P17's one-sided bounds remain the best
available constraint. What survives, unaffected by this correction: the
2026-08-10 double-layer result for its **own** specific configuration
(unaffected — that finding was independently numerically verified with
its own positive control, not touched here), and P25's WEP
composition-dependence result.

## 1. What is genuinely cited (not re-derived, and not "independently cross-checked")

`FINDING_dipole_shell_is_a_double_layer.md` (2026-08-10, numerically
verified, positive control passed — the monopole-shell integral exactly
recovers Newton's shell theorem, `C₂=1`) established: for dipoles
**radially aligned from a single common center**, arranged on a shell
around that center, the sourced field is **exactly zero** — all
potential derivatives vanish — everywhere off the shell. This matches
the standard textbook "double layer" / dipole-sheet identity in
electrostatics.

~~Independently cross-checked here via a different argument (not a
re-run of the original numerical quadrature)...~~ **[CORRECTED — a real
issue, not just wording.]** The function claimed to perform this
cross-check, `dipole_layer_potential_jump_standard_result()`, contained
**zero computation** — it returned a hardcoded `True`, and its result was
assigned to a variable literally named `fact_confirmed_independently`.
Calling this an "independent cross-check" was false: it is a citation of
a textbook *name* for the same result, not a verification performed by
this script. Removed entirely; §1 above is now stated as a plain
citation, with no claim of independent confirmation.

## 2. Multipole exterior-solution check — a kinematic fact, not physical evidence

For each multipole order `ℓ`, `r^{-(ℓ+1)}` is verified (sympy) to solve
the source-free radial Laplace equation — `ℓ=0`: `1/r`; `ℓ=1`: `1/r²`;
`ℓ=2`: `1/r³`. **[CORRECTED]** ~~the standard reason a smooth, extended
source's higher multipoles are always subdominant to its monopole...~~
This is a **kinematic** fact about which falloffs are mathematically
admissible for a field of a given multipole order — it says **nothing**
about which multipoles a given physical source actually *excites*. `κ`
is intrinsically a dipole-type source with no natural monopole moment to
begin with, so "smooth sources are monopole-dominated" was the wrong
framing for this sector from the start. The sympy computation itself is
correct; its connection to the physical claim was decorative.

## 3. The generalization gap — withdrawn, the consequential fix

~~P34's homogeneous FRW background treats matter as a smooth, isotropic
density — exactly the continuum limit of many radially-aligned dipole
sources distributed isotropically. By the double-layer result, such a
distribution contributes exactly zero net κ-sourced force to the
background...~~ **[WITHDRAWN.]** A homogeneous distribution has **no
privileged center** — "radially aligned from a common center, distributed
isotropically" does not describe a coherent configuration; there is no
single well-defined "radial direction" for a homogeneous background. The
2026-08-10 shell result requires exactly that center to exist. This
extension was never justified.

Separately, `two_field_action_closure.py`'s own docstring states **two
different** things for the cosmological case: "the radial-dipole average
is a double layer" (§1's mechanism — Green's-identity-based, requires
coherent radial alignment) **and**, distinctly, "the random average is
zero" (isotropic-orientation averaging — a completely different
mechanism, requiring no alignment at all, only randomness). This finding
only ever examined the double-layer mechanism; citing it as confirmation
of the *random-average* sentence was a category error, conflating two
genuinely different theorems the source material itself keeps separate.

~~P35's static two-body ΔG used a spherically symmetric point source M
— for a spherically symmetric or smoothly-extended physical source, the
same double-layer cancellation applies to its own internal κ-content:
zero net contribution...~~ **[WITHDRAWN.]** This requires **assuming**
the source's own internal `κ`-content is organized as coherent,
radially-aligned nested shells — an additional, unmotivated assumption.
Real matter's dipole content, if anything, would be thermally
randomized (the *random-average* case, not examined here), not
coherently radially aligned. Not established.

**Corrected conclusion:** whether `κ` is invisible to P34's background or
P35's static `ΔG` is a genuinely **open question** — this finding does
not establish it in either direction for those two specific channels.

## 4. P25's WEP result — cited, unaffected, but the "duality" it fed does not survive

`FINDING_P25_wep_eotvos_kill_gate.md` (2026-08-13, sympy-verified,
skeptic-corrected) is **unaffected** by this correction: the `k`-sector
produces a genuine, composition-dependent term in a laboratory
Eötvös-type test; P23 already showed the `g`-sector is WEP-blind
(universal coupling). **[CORRECTED]** ~~The two sectors are each visible
to exactly the channel the other is blind to.~~ This establishes only
**one** one-way statement (`κ` *is* visible via WEP; `g` is *not*) — not
the general duality originally claimed, which needed §3's now-withdrawn
claims to supply the other half (that `g` *is* visible via smooth-source
channels with no cancellation of its own — asserted, not re-examined
here).

## 5. Skeptic verdict (context-blind, Step 8a, 2026-08-14)

Reviewed with `claim.md`-equivalent content (this finding, pre-correction)
+ the script, **no session history**, per Falsification Ladder Context
Asymmetry Rule. Six issues found, five FALSIFIED (not merely weakened) —
the most severe outcome of any review this session:

| # | Issue | Verdict | Disposition |
|---|---|---|---|
| 1 | `dipole_layer_potential_jump_standard_result()` was `return True` dressed as an "independent cross-check" | **FALSIFIED** | Function removed; §1 now a plain citation, no independent-verification claim |
| 2 | Shell result (proven for radially-aligned dipoles around one center) silently extended to P34's homogeneous background (no center) | **FALSIFIED** | Withdrawn; generalization gap stated explicitly (§3) |
| 3 | "Random average" (isotropic orientation) and "double layer" (coherent radial alignment) conflated as one fact, though the source's own docstring keeps them separate | **FALSIFIED** | Kept explicitly separate; only the examined mechanism (double layer) is cited (§3) |
| 4 | "Each visible to exactly the channel the other is blind to" overreached — only one channel pair examined | **WEAKENED** | Downgraded to the one supported one-way statement (§4) |
| 5 | Double-layer theorem applied to a point/extended source's own internal `κ`-content without justifying that content is radially-aligned shells | **FALSIFIED** | Withdrawn (§3) |
| 6 | Multipole falloff check (§2) treated as physical evidence for "monopole dominance," when it only shows kinematically-admissible falloffs, and `κ` has no natural monopole anyway | **FALSIFIED (as physical support)** | Reframed as a kinematic fact only (§2) |

**What survives:** the 2026-08-10 double-layer result and P25's WEP
result, both for their own already-established scope, untouched. The
sympy multipole computation itself is correct. **What does not survive:**
the entire connective argument (§3, the finding's actual point) and the
duality claim (§4) — both withdrawn as unestablished. Kill
classification: **the closest this session has come to core-predicate-
false** — the finding's headline claim was not merely overclaimed in
framing but was not actually shown by anything in the original script or
text. What remains is a genuinely open question, correctly stated as such
only after this correction.

## Reproduction

```bash
python experiments/20260803-bridge/P36_kappa_invisible_to_g_sector_channels.py
```
