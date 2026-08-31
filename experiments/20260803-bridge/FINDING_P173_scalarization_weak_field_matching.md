# FINDING P173 — weak-field matching: does a scalarization-type `k_A`
# completion reproduce MULTING's own `F^(1)` radial form and sign?

**Date:** 2026-08-31
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (does a specific candidate completion
reproduce a target mathematical structure — not a causal claim, not a
claim about v82's own construction)
**Continues/answers:** `FINDING_P172`'s own explicitly-named next step
("no calculation was attempted matching MULTING's own `1/s³` form to
scalarization's asymptotic falloff") — done here.
**Script:** `P173_scalarization_weak_field_matching.py` (sympy, 4 tests
incl. 1 positive control, ruff clean, does not touch the 881-test suite)
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** N/A — symbolic derivation, no fit.
> **Ontological/mechanistic interpretation status:** `FINDING_P172`'s
> scalarization candidate is now CLOSED (not open) as a route to
> reproducing MULTING's own `F^(1)` — it fails on radial power in its
> simplest form, and the one variant that fixes the power reduces to a
> construction `docs/131` already tested and already found blocked on
> the same positive-energy sign obstruction. `docs/131`'s own residual
> branch #1 (`k_A` redefinition in general) is not fully closed by this
> — only the specific scalarization-inspired realization is.
> **Causal/cosmological claim status:** N/A.

**Adjudication note (2026-08-31, methodologically notable — a skeptic's
OWN critique was itself independently falsified, not just the file it
reviewed):** a context-blind skeptic review of this file's first draft
returned a detailed, confident **FALSIFIED** verdict, arguing Case 2's
own sign was computed backward — that the code's `u = -p_A * dphi_ds`
contained an unjustified extra minus sign, and that correcting it would
flip Case 2 to REPULSIVE, matching MULTING's own needed sign (i.e.,
reversing this file's entire conclusion). Given the magnitude of that
claim — it would have overturned `docs/130`/`docs/131`'s own multi-week
no-go findings — this was treated as an extraordinary claim requiring
extraordinary verification (per this project's own Sagan-standard
discipline), not accepted or rejected on the skeptic's word alone.
**Independently re-derived the sign four separate ways**, each starting
from nothing but the already-validated two-point-charge formula (no
shared abstraction with the disputed derivation): (1) direct symbolic
limit of two point charges (`+q` at `s-ε/2`, `-q` at `s+ε/2`) as `ε→0`
with `p_A=qε` fixed, both by hand and independently via a fresh sympy
script; (2) the charge-density/Green's-function convolution
`U=∫ρ_A·Φ_P d³x`, worked through explicitly rather than via the
shortcut the skeptic's own derivation used; (3) the standard textbook
point-dipole-in-external-field formula (`U=-p·E`), correctly re-
calibrated for THIS project's own like-charges-attract convention
(textbook electrostatics uses like-repel — a naive copy-paste would
itself be an error). **All four independently agree: `U_dipole(s) =
-p_A·q_P/(4πs²)`, ATTRACTIVE — the code's ORIGINAL sign was correct.**
Given the stakes, a SECOND, freshly-briefed skeptic agent (no shared
context with the first, working from its own coordinate setup) was
separately dispatched to adjudicate the same question from scratch,
per this project's own Paraphrase-Sensitivity Probe protocol for high-
stakes disagreements — it independently reproduced the identical
result and independently located the first skeptic's own error at the
same specific step this project's own re-derivation had already
identified: conflating `dφ/ds` (with `s` defined as distance FROM the
source `q_P`, i.e., a derivative taken in the outward-from-source
direction) with the properly-oriented spatial gradient `∇φ` dotted
into `p_A`'s own direction (which points TOWARD the source) — these
differ by exactly one sign, and the first skeptic's derivation used
the wrong one. **This file's original conclusion is CONFIRMED
unchanged.** Documented here not to relitigate the finding but because
it is a genuine, rare, instructive data point for this session's own
governing discipline ("never accept a skeptic's claim at face value,
independently re-verify") — that discipline caught a real error IN a
skeptic review, not only in this project's own drafts, which is
exactly what it is for. Two smaller, valid points from that same first
review (Case 1's `1/s²` result is a standard field-theory fact, not a
novel discovery; the "two independent derivations converge" language
in §3 slightly overstated how independent a simple toy model really is
from a full covariant action) ARE incorporated below.

## 0. Premise — `NO_AUTHOR_ERROR`

This file tests whether a specific candidate construction (from this
project's own `FINDING_P172`) reproduces a specific mathematical target
(MULTING's own published `F^(1)`, `[VERIFIED-PDF]`). It is not a claim
about v82's own theory — only about whether this project's own attempted
completion works.

## 1. Setup

Two constructions, both built on the SAME calibrated linear scalar
coupling already verified in `P172_scalar_exchange_sign_rule.py`
(same-sign charges attract, matching `FINDING_P162`/`docs/130`'s own
established fact):

**Case 1 — simple isotropic scalarization charge** (`FINDING_P172`'s own
literal proposal): both nodes couple to a scalar field via an ordinary
monopole coupling `L_int = q·φ`, with `q = q(k)` a function of thermal
energy — standard monopole-monopole scalar exchange.

**Case 2 — monopole-dipole**: node `P` sources an ordinary monopole
field via its mass (`q_P ~ m_P`, matching v82's own Newtonian `F^(0)`);
node `A` couples via the field's GRADIENT rather than its value
(`L_int = p_A·∇φ`), with `p_A = f(k_A)·n̂` — magnitude from `A`'s own
thermal energy, direction supplied EXTERNALLY by the separation vector.
This external-axis structure is not invented here — it is v82's own
explicit claim, quoted in `FINDING_P162` §3: "a node's own thermal
energy has no intrinsic axis... the line connecting the two nodes...
supplies the direction, with a node's thermal energy setting only the
magnitude."

**Target:** MULTING's own `F^(1)`, `[VERIFIED-PDF, P161_v82_beta_
identifiability.py's own code]`: `f1 = -G·β1·2·k_x·m_x·r_x/s³` — an
explicit `1/s³` radial dependence, with a THREE-quantity product
(`k`, `m`, `r`, not merely two "charges").

## 2. Results

**Positive control** (`test_case1_matches_docs130_calibration`): Case
1's own same-sign-attractive behavior matches `docs/130`'s already-
established fact — confirms the calibration is consistent before
trusting anything derived from it.

**Case 1 — radial power mismatch, independent of sign:**
```
U(s) = -q_A·q_P/(4πs)
F(s) = -q_A·q_P/(4πs²)
```
`F ~ 1/s²` — the ordinary monopole-monopole (Coulomb/Yukawa-type)
falloff. **This does NOT match MULTING's own `1/s³`.** This is a
standard field-theory fact (any linear monopole-monopole scalar
coupling in 3D flat space gives `1/s²`, essentially by the same Green's-
function structure as Newtonian gravity itself) — not a novel discovery
about scalarization specifically, and it holds for whatever function of
`k_A` the charge is, which is precisely why it is useful here as an
explicit, checked baseline: `FINDING_P172` checked the SIGN mechanism
in detail but never checked the radial power, so stating this plainly,
even though unsurprising, closes a real gap that file left open.

**Case 2 — radial power matches, sign does not:**
```
U(s) = -p_A·q_P/(4πs²)
F(s) = -p_A·q_P/(2πs³)
```
`F ~ 1/s³` — **matches MULTING's own `F^(1)` radial form exactly.**
But for ordinary positive quantities (`p_A=f(k_A)>0` for positive
thermal energy, `q_P>0` matching ordinary attractive monopole gravity),
`F<0` — **ATTRACTIVE, not the repulsion MULTING's dipole needs.**

## 3. The decisive structural observation

Case 2's own construction — "an effective dipole moment, magnitude set
by a node's own internal energy, direction supplied externally by the
separation vector, coupled via the field gradient" — **is not a new
idea.** It is, structurally, exactly what `docs/131`'s own `CANDIDATE-
L1` (a covariant vector-type internal-dipole medium, Blanchet–Le Tiec
action) already built and weak-field-matched, arriving independently at
this file at the same construction from a scalarization starting point.
`docs/131` already found: this construction reproduces MULTING's own
`1/s³` structure (its own "sombrero branch" result, per `FINDING_P162`
§1's own quote), but the repulsive sign requires abandoning positive-
energy/ghost-freedom/staticity — **exactly reproduced here**,
independently, via a completely different derivation route (gradient-
coupled scalar dipole vs. covariant vector-field action).

**Two derivations agree on the same conclusion — a real but modest
corroboration, not independent proof (softened, skeptic-caught
overstatement).** This file's toy gradient-coupling model is much
simpler than `docs/131`'s own full covariant vector-field action, and
both ultimately rest on the same root field-theory fact (linear
coupling + ordinary positive sources → attraction) — so this is not
strong, independent evidence in the sense of two unrelated physical
mechanisms converging. What it DOES show, honestly: the obstruction is
not an artifact specific to `docs/131`'s own particular covariant
construction (Blanchet–Le Tiec action) — the simplest possible toy
model that reproduces the right radial power hits the identical wall,
which is worth stating plainly, without inflating it into "independent
proof."

## 4. Verdict

**`FINDING_P172`'s own scalarization candidate is now CLOSED as a route
to `docs/131`'s residual branch #1**, on two independent grounds:

1. The literal proposal (isotropic scalarization charge, Case 1) fails
   on radial power alone — `1/s²` not `1/s³` — a mismatch `FINDING_P172`
   itself did not check.
2. The one modification that fixes the radial power (Case 2, an
   effective external-axis dipole) is not actually a new construction —
   it reduces to `docs/131`'s own already-tested `CANDIDATE-L1`, and
   independently reproduces its already-known sign obstruction.

**This does NOT close `docs/131`'s residual branch #1 in general** — it
closes the SPECIFIC scalarization-inspired realization `FINDING_P172`
proposed. The general question ("is there ANY positive-energy, ghost-
free construction where `k_A` sources gravity as something other than
its own ordinary mass-energy") remains open in the sense that this
project has now tried three independent starting points (bare scalar
mediator `docs/130`, covariant vector-dipole medium `docs/131`, and
scalarization-inspired gradient coupling here) and all three converge
on the SAME obstruction — a convergence worth naming explicitly as a
strengthening of the original no-go's own robustness, even though no
single one of the three constitutes a general proof.

## What this file does NOT establish

1. **Not a claim that no construction could ever work** (`NO_AUTHOR_
   ERROR`, §0) — only that these two specific, natural constructions,
   both weak-field-matched explicitly, fail — one on power, one on sign.
2. **Does not prove Case 2 is the UNIQUE way to fix Case 1's radial-
   power mismatch** — a genuinely different mechanism (not a gradient/
   dipole-type coupling) might reproduce `1/s³` without inheriting the
   same sign obstruction; not searched for here.
3. **Does not address the `r_P` factor in MULTING's own `F^(1)`**
   explicitly (`k_x·m_x·r_x/s³`, a three-quantity product) — this file's
   `q_P` stands in for `m_P·r_P`-type combinations without separately
   modeling the `r_P` dependence; does not change the `s`-power
   conclusion, which is what this file tests.
4. **The "two independent derivations converge" claim (§3) is offered
   as a real, checkable observation** (different starting theory,
   different derivation route, same conclusion) **but is not a formal
   proof of generality** — three convergent attempts is suggestive
   corroboration of `docs/131`'s own robustness, not an exhaustive
   theorem covering all possible constructions.
5. **Does not revisit `docs/131`'s residual branches #1 (in full
   generality) or #3 (driven non-equilibrium)** — only closes the
   specific scalarization-inspired sub-branch of #1 this session opened
   in `FINDING_P172`.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
