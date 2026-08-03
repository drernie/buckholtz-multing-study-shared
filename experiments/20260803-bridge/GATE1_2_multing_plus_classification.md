# Gate 1/2 classification — MULTING+ handoff content

**Date:** 2026-08-03 · Applies `artifact-provenance-gates.md` Gates 1 (Identity)
and 2 (Target Provenance) to `HANDOFF_multing_plus_next_session.md`, per the
standing instruction not to build on that content until it passes the same
scrutiny as everything else in this project.

**What this pass is, and is not.** This is a classification and one bounded
independent check — **not** a from-scratch rederivation of the covariant
P(X)/multipole theory. Redoing that properly (an actual action, a
consistent propagator, the two-body coefficient dependence) is a
multi-session research task in its own right, not something to attempt
inside a "go through the list" pass. Per the handoff's own instruction:
pick at most one candidate, run the cheapest differentiating test, don't
start a new ten-theory tournament.

---

## The one thing independently checked: R7, the radial-power ladder

**Claim (handoff §4.1, labelled the most credible positive result):**
nested source equations `∇²φ ~ ρ`, `∇²σ ~ -(∇φ)²`, `∇²ξ ~ -φ(∇φ)²`
naturally generate `φ~1/r, σ~1/r², ξ~1/r³` — i.e. one propagator's
derivatives can produce MULTING's whole radial power sequence.

**Independently re-derived here**, symbolically (`sympy.dsolve`, not hand
algebra alone):

```
phi = 1/r                                          (given: point-source Poisson)
nabla^2 sigma = -(d phi/dr)^2 = -1/r^4
    => sigma(r) = C1 + C2/r - 1/(2 r^2)             particular term ~ 1/r^2  ✓
nabla^2 xi = -phi*(d phi/dr)^2 = -1/r^5
    => xi(r)    = C1 + C2/r - 1/(6 r^3)             particular term ~ 1/r^3  ✓
```

**Verdict: `CONFIRMED` as a scaling argument.** This is now `[VERIFIED]` by
this session, not merely relayed from an unverified source — upgraded from
the handoff's own "useful hypothesis, not certified."

**What this does and does not establish.** It confirms that a specific,
simple class of nested-source field equations reproduces the right *powers*
of `r`. It says nothing about:
- whether any covariant, ghost-free action actually generates exactly these
  three coupled equations (this is precisely what NR-019, below, flags as
  the open problem — ties directly to the ghost-condensate/static-propagator
  tension)
- whether the *coefficients* — not just the powers — reproduce MULTING's
  real `A2, A3, A4` for two composite (non-point) objects
- anything about the cosmological magnitude question (§6 of the technical
  memorandum; a separate, much harder issue)

So: the radial-ladder mechanism is real as arithmetic, and remains exactly
as far from "the bridge" as the handoff itself said — a necessary ingredient
confirmed, not a sufficient one.

## NR-019 — plausible, not independently re-derived here

**Claim:** an exact ghost-condensate configuration (`P_X=0`, giving `w=-1`)
is in tension with an ordinary static `1/r` propagator, which needs `P_X>0`.

This is consistent with the general phenomenology of ghost-condensate
theories in the literature (Arkani-Hamed, Cheng, Luty, Mukohyama 2004 and
follow-ups establish that the standard kinetic term vanishes at the
condensate point, forcing modified, higher-derivative-dominated dispersion
in the IR rather than an ordinary Coulomb-like propagator). This project has
not re-derived the specific dispersion relation here — the claim is graded
`[WEAK-CONSISTENT]`: plausible given known results in the class of theory
invoked, not verified from first principles in this session.

## NR-020 — genuinely unverifiable from the material available

**Claim:** bare multipole exchange in "the dipole-polarization thawing
model" gives `ell_q²/ell_d² = 3/2 + 3/(4 g_m²) >= 3/2`, failing an
"F7 repulsive-window condition" that needs `< 1/4`.

**Blocker, stated plainly: `F7` is never defined in the saved handoff.**
This project's own repulsive-window derivation (technical memorandum §5)
gives the *same* threshold value, `ell_q²/ell_d² < 1/4`, for a repulsive
interval to exist at all — so "F7" plausibly refers to that same relation,
carried over from whatever prior session produced the handoff. But that is
an inference, not a confirmed identification, and the formula
`3/2 + 3/(4g_m²)` cannot be checked without the underlying field content
(what `g_m` is, what the actual action/coupling structure is) — none of
which survived into the saved handoff text, only the result.

**Verdict: `UNVERIFIED`, and not verifiable without either (a) the original
derivation this session doesn't have, or (b) reconstructing the model from
scratch — which is exactly the "new research task" this pass is scoped not
to attempt.**

## Everything else in the handoff (cascade EFT as a full action, P(X)
worldline multipoles as a covariant construction, the decorrelation rescue
`C(r/xi)`, the fσ8 growth claim)

Unchanged from the handoff's own self-assessment: `PROMISING FORMAL
CONSTRUCTION`, `PHYSICAL LINK NOT ESTABLISHED`, `NECESSARY RESCUE
HYPOTHESIS / MICROPHYSICAL DERIVATION ABSENT`, `UNVERIFIED` respectively.
Nothing in this pass changes those statuses — no attempt was made to verify
them, by design.

---

## What this changes about "what's next" for this thread

If this thread is picked up again, it should NOT restart as a broad
multi-candidate tournament. Per the handoff's own T1–T4 priority (technical
memorandum-equivalent for MULTING+, not written here) and this pass's
finding, the cheapest next differentiating step is:

**Either** (a) obtain the actual derivation behind NR-020 — the formula, not
just its result — so it can be checked the way R7 just was, **or** (b) treat
R7 as the one surviving thread and ask what covariant action would need to
produce exactly `∇²φ~ρ, ∇²σ~-(∇φ)², ∇²ξ~-φ(∇φ)²` — which is a real,
well-posed field-theory construction problem, not a literature-tournament
problem.

Both are substantial, dedicated pieces of work — multi-session, not a
subsection of a status pass. Recorded here so the next session doesn't have
to re-discover this scoping.
