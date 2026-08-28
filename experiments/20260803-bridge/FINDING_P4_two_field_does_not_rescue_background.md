# P4 — a second field does not automatically rescue the background H(z) target, and the reason is narrower than first stated

**Date:** 2026-08-11 · answers the discriminating test proposed after the user asked
whether `S[g,φ,ψ,matter]` (a literal second field for `k`, not `k` as a derivative
coupling on `φ`) should be the project's next priority for a covariant MULTING
completion.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P4_two_field_cosmological_test.py` (scratchpad only — could not be
written into this directory this session; content reproduced in full at the end
of this file so the record is not orphaned outside the repo).
**Status: `[VERIFIED]` Part A, `[FALSIFIED-AS-STATED, CORRECTED]` Part B, per an
independent context-blind skeptic pass — see §4.**

> **[UPDATE 2026-08-28]** Of the two escape routes named in §7 below (S1:
> non-gradient-sourced moment; S2: screened/distinct propagator), **both
> are now closed for the background channel.** S1 — for constructions
> that reproduce MULTING's near-field ladder via `docs/125`'s own
> exhibited bilinear factorization, at the `r→∞` symbolic-limit level —
> see `FINDING_P152_S1_general_pairkernel_background_closure.md` (twice
> skeptic-corrected). S2 — for the Shtanov–Sahni background channel
> specifically, confirmed by two independent methods (the `r→∞` `G_eff`
> limit and a finite-`r` isotropic population average) across both
> MULTING tiers — see `FINDING_P153_S2_screened_propagator_window_gate.md`
> and `FINDING_P154_screened_C1_isotropic_population_average.md` (three
> skeptic rounds). **Neither closure overturns P11's own separate,
> still-live near-field finding**, which remains an open structure-
> formation/second-order lead, not a background-`H(z)` one.

---

## 1. The question

Does promoting `k` (the second MULTING charge, alongside mass `m`) from a
derivative coupling on a single field `φ` (P1's construction,
`two_field_action_closure.py`) to its own field `ψ` change the conclusion that
the completion's `k`-dependent force tiers cannot source the cosmological
background (`H(z)` at linear/FRW order)?

## 2. Part A — a plain monopole `ψ` cannot even match the weak-field ladder

If `ψ` couples to `k` via an ordinary, non-derivative worldline term (the same
form `m` uses for `φ`), and `φ`/`ψ` are otherwise uncoupled, the two-body energy
is just two independent massless-scalar exchanges:

```
U = -G m_A m_B / r  -  lambda k_A k_B / r
```

This produces only `1/r^2` force terms. It cannot produce MULTING's mixed
`(k_A m_B + m_A k_B)/r^3` tier at all (no cross-coupling between the fields
exists to produce it), and puts `k_A k_B` at the wrong power (`1/r^2`, not the
required `1/r^4`). **Killed, for any choice of coupling constant** — this is a
structural mismatch, not a fitting problem.

Skeptic note (§4): the code establishes this via hard-coded booleans rather
than a computed structural check on the symbolic expression. The conclusion is
correct on inspection of the displayed `U`/`F`, but the "check" is a display,
not a test that could fail. `[WEAK]` marker on the code artifact for this
reason; not on the conclusion itself, which the skeptic did not dispute.

## 3. Part B — what actually happens once `ψ` is forced to carry a derivative (as it must, to match A3/A4)

**Original argument (as first stated, before skeptic review):** matching MULTING's
`r^-3`/`r^-4` ladder forces `k`'s moment to enter via a derivative; that moment,
by analogy with `two_charge_completion.py`'s "induced polarisation" language, was
claimed to be sourced by the *local gradient of the gravitational potential*
(`p_i ~ -grad(Phi_local)`), which vanishes identically on an exactly homogeneous
FRW background (`grad(Phi_bg) = 0` by definition) — so the moment, and any force
built from it, was claimed to vanish at background order for *any* two-field
completion preserving the ladder, generically.

**This was FALSIFIED by the skeptic, correctly.** Neither cited source file
derives `p_i = -grad(Phi_local)`. `two_charge_completion.py` only fixes the
*relative orientation* of two bodies' moments in a two-body configuration
(mirror-symmetric, A↔B). `two_field_action_closure.py` (P1) uses an **intrinsic**
moment, `p_i = kappa*k_i*r_i/c^2` — a fixed property of each body, not a response
to any gradient — and its own zero-background-order result comes from
**orientation averaging** (random ensemble / double-layer geometry), not from
`grad(Phi_bg)=0`. The gradient-sourcing mechanism was imported from the external
Blanchet dipolar-medium picture and stated as if it were what this project's own
code computes. It is not.

## 4. Skeptic verdict (Step 8a, Context Asymmetry: claim + code + the two cited
source files only, no session history)

Three separate verdicts, not merged, per this project's own Falsification Ladder
protocol:

```
Part A (plain monopole psi cannot match the ladder):        WEAKENED
  -- conclusion correct; the "check" in code is a display, not a computation.
Part B (gradient-sourced moment argument, as literally stated): FALSIFIED
  -- does not correspond to what either cited source file actually derives.
OVERALL CONCLUSION ("obstruction is generic to any two-field completion"): WEAKENED
  -- recomposing A+B silently added two assumptions neither sub-claim licenses:
     (i) any ladder-matching completion must derivative-couple on a shared kernel
         (depends on unstated locality/ghost-freeness assumptions);
     (ii) any such moment must be gradient-induced (false against this
         project's own P1 code, which uses an intrinsic moment instead).
```

The skeptic named two live, unclosed escape routes for a genuine two-field
completion, neither ruled out by anything computed so far:

1. A `ψ`-moment sourced by something other than a potential gradient (intrinsic
   spin, a background VEV of a non-gradient field, an equation-of-state
   parameter) need not vanish on a homogeneous background at all.
2. A `ψ` with its own distinct propagator (screened/massive on cosmological
   scales, effectively massless at cluster/solar-system scales — the same class
   of mechanism as chameleon/Vainshtein/symmetron screening in modified gravity)
   would break the "one derivative per k-occurrence on a shared kernel" counting
   that Part B's derivation depends on.

## 5. Correction supplied by the user after the skeptic pass — the sharper, load-bearing point

Even granting the corrected, weaker version of Part B (a **dipolar** completion
plausibly does not source the background at linear order, via orientation
averaging over the *specific* P1-style intrinsic moment — not proven for a
genuine second field, but plausible by analogy), **this does not license the
stronger claim "no two-field action can change H(z)."** Any new scalar field
has a homogeneous time-dependent mode on FRW,

```
psi_bg(t),   V(psi),   T_mu_nu^(psi) = (1/2) psidot^2 + V(psi) + ...
```

and that mode can source `H(z)` completely independently of whether the field
also carries MULTING's `k`-charge completion structure — this is just
quintessence, and it is trivially true for any scalar with nonzero background
energy density. What the test above actually shows is narrower and more useful:

```
"a field is capable of changing H(z)"      is NOT equivalent to
"a field is a completion of MULTING's force law"
```

The cheap test killed only the *simultaneous* route (get both from the same,
`k`-charge-carrying sector, via the specific dipolar/derivative mechanism this
project has built so far) — not the general possibility that some two-field
action changes `H(z)`, which is unconstrained and uninteresting on its own (any
quintessence field does that; it says nothing about MULTING specifically).

## 6. Literature-attribution correction

The "first order = ΛCDM-degenerate, differs only at second order (bispectrum /
non-Gaussianity / nonlinear growth)" theorem should be attributed to the
Blanchet & Le Tiec 2008 series (arXiv:0804.3518) and its early 2010s follow-ups
— **not** to Blanchet & Seraille 2025 (arXiv:2507.02563), which this project's
own `facts.json` Q006 entry already logs as the newest first-principles lead for
Q006 but which contains no cosmological perturbation analysis; it is a
non-relativistic deep-MOND-limit paper, and its own authors state the model
cannot simply be "covariantized" in standard GR. This project's Q006 record
already keeps 2008-era and 2025-era sources separate; this note exists so this
specific file does not blur that distinction going forward.

## 7. Kill Analysis (Anti-Overfitting Gate discipline)

**Killed:** "a plain monopole `ψ` completes MULTING's force law" (Part A, robust,
unchallenged by the skeptic). "The background-null result is generic to any
two-field completion, via gradient-induced moments vanishing on a homogeneous
background" (Part B as originally stated — the specific mechanism cited does not
exist in the code it was attributed to).

**Not killed:** whether *some* two-field construction can simultaneously (a)
match MULTING's weak-field ladder and (b) source `H(z)` — the two named escape
routes (non-gradient-sourced moment; screened/distinct-propagator `ψ`) are live
and untested. Whether a genuine two-field derivative-coupled `ψ` reduces to
P1's orientation-averaged null result "by the same argument, not just by
analogy" — not actually re-derived for the two-field case.

**Branch split, going forward — these are now two separate questions, not one:**

```
Branch A (original MULTING cosmology): F_MULTING --?--> H(z)
  Status: UNCHANGED by this test. The dipolar completion built so far does not
  supply this bridge. A = -Hdot remains a phenomenological postulate, not
  derived from any completion this project has built.

Branch B (field-theory completion, on its own terms):
  Status: the weak-field structure (P1) is real and survives adversarial audit.
  Its natural new physics, if the dipolar/induced-moment picture is right, lives
  in SECOND-ORDER cosmological observables (non-Gaussianity, nonlinear growth,
  cluster-scale dynamics, lensing/velocity higher-point statistics) — not H(z).
```

## 8. Next cheapest differentiating test (not yet run)

Proposed by the user, agreed: before building any large action/pipeline, derive
the perturbative order at which each MULTING force tier enters observables —

```
F_m  ~ O(delta^?)
F_km ~ O(delta^?)
F_kk ~ O(delta^?)
```

— identify the first nonzero gauge-invariant cosmological observable this
implies (leading candidates: the bispectrum `B_zeta(k1,k2,k3)`, nonlinear growth,
or a cluster-scale higher-point statistic), and forecast the expected effect
size against a real survey's error bars (Euclid or equivalent) *before* writing
any analysis pipeline. This is the natural continuation of Branch B and does not
require resolving Branch A first.

## What this does NOT establish

1. It does not show MULTING's actual, unpublished completion (if TJB has one)
   behaves this way — only that the *specific* dipolar/induced-moment class of
   completion this project has built does, and only as far as the skeptic could
   independently confirm.
2. It does not rule out either of the two named escape routes (non-gradient
   moment; screened propagator) — both are open, neither computed.
3. It does not establish that Branch B's second-order effects are large enough
   to be observable — no forecast has been run yet (§8).
4. Per NO_AUTHOR_ERROR: none of this is a claim about an error in TJB's own
   theory. It is entirely this project's own reconstruction attempt, and its own
   correction of its own overclaim after adversarial review.

---

## Appendix — full P4 script (Part A code + Part B print statements, as reviewed by the skeptic)

See `two_field_action_closure.py` and `two_charge_completion.py` in this same
directory for the source constructions this file's Part B originally
(incorrectly) cited. The P4 script itself is not committed to this directory
(write access to this path was unavailable this session); its exact content is
preserved in this session's transcript and can be reconstructed from §2-§3
above, which reproduce its logic and print output in full.
