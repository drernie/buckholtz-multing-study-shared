# P32 — MULTING's own worldline coupling gives photons zero direct force, supporting (not proving) the mechanism-frame divergence from Bean & Tangmatitham

**Date:** 2026-08-13
**Origin:** direct continuation of `FINDING_P31`'s user-flagged correction,
which identified a deeper caveat than the earlier skeptic review found:
Bean & Tangmatitham's `(Q,R)` framework assumes matter stays minimally
coupled (new physics lives *only* in a modified metric Poisson equation),
while MULTING's own reconstructed action has a *worldline* coupling
(`g·mᵢ·φ`) acting directly on matter's equation of motion — a structurally
different mechanism. This finding checks the single most decisive,
cheaply-derivable consequence of that difference: does the worldline
coupling give photons a direct force, the way Bean's metric modification
would?
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P32_photon_decoupling_mechanism_frame_gate.py`

## 0. Honest scope, stated before anything else

This is deliberately a **narrower** question than the collaborator's full
proposed gate (deriving `μ(a,k)`, `γ(a,k)=Φ/Ψ`, `Σ(a,k)`, `G_matter(a,k)`
from a full covariant action with an Einstein-Hilbert term added). That
full derivation is real, substantial general-relativistic work this
project has never attempted — no metric perturbation, no Einstein
equations, and no stress-energy tensor for `φ` have been written down
anywhere in this project before now. Rushing that full derivation risks
introducing new errors under the same time pressure that has already
produced several corrected mistakes this session. This finding answers the
single most decisive, narrowly-scoped sub-question first, and explicitly
does **not** claim to close the full mechanism-frame gate — see §4.

## 1. Method

`two_field_action_closure.py`'s own action (re-verified this session, no
Einstein-Hilbert term present anywhere): the monopole worldline coupling is

```
L_coupling = g·mᵢ·φ(xᵢ)
```

— the entire direct matter-`φ` coupling for the monopole sector, linear in
the particle's rest mass `mᵢ`. Evaluated the massless-particle limit
(`mᵢ→0`, the photon case) symbolically.

## 2. Result (sympy-verified)

```
L_coupling(m=0) = g·0·φ = 0
```

**Identically zero, for any `g` or `φ`.** A massless particle has exactly
zero direct coupling to `φ` via this term — forced by the coupling's own
linear-in-mass structure, not assumed or approximated.

**Consequence for the direct-coupling channel:** the same mechanism that
produces the growth-equation modification (`ΔG`, per P30) — a direct
worldline force proportional to mass — produces **exactly zero** direct
force on photons. This is a genuine structural contrast with Bean &
Tangmatitham's own `(Q,R)` framework, where `Q` modifies the *metric*
Poisson equation itself — a quantity both matter and light are sourced
by/move through equally, per standard GR geodesics, with no mass-dependence
built in.

## 3. What this supports (and does not prove)

This **supports** the collaborator's flagged concern (`FINDING_P31`): if
the direct-coupling channel were the whole story, MULTING's own mechanism
would leave lensing/ISW unaffected while modifying growth — a genuine
divergence from Bean & Tangmatitham's phenomenology, whose own likelihood
is calibrated to growth and lensing moving *together*. **It does not fully
prove this**, because of the indirect channel in §4.

## 4. What this does NOT establish — the open, larger question

**A genuinely separate, indirect channel is not addressed here.** `φ`
itself carries stress-energy (from its own kinetic term, `(1/2)(∂φ)²`, in
the action). In *any* standard-GR completion of this action — implicit
throughout this project, since no modified Einstein-Hilbert term has ever
been written down here — `φ`'s own stress-energy tensor `T_μν^(φ)` sources
Einstein's equations, exactly like any other field's energy density. This
is a genuinely separate mechanism through which `φ` **could** still perturb
the metric (and hence photons, via standard lensing), regardless of the
direct-coupling result in §2. Whether this backreaction channel produces a
lensing signal **comparable in size** to the direct growth-equation `ΔG`
is not addressed here — resolving it requires deriving Einstein's
equations, the scalar field equation, and the matter equation
*simultaneously* from a full covariant action (the collaborator's original
full P32 spec), not attempted in this narrower first step.

**Other things not established:**
1. **`γ(a,k)=Φ/Ψ`, the gravitational-slip parameter.** Whether the two
   metric potentials remain equal (`γ=1`, standard GR) or diverge under
   `φ`'s backreaction is not derived here.
2. **`Σ(a,k)`, the lensing-relevant combined potential.** Standard
   literature (per `FINDING_P31`'s own corrected §4) combines `Q` and `R`
   (or equivalently `γ`) into `Σ`, the quantity lensing actually measures —
   not derived here.
3. **A quantitative estimate of the backreaction channel's size relative to
   the direct channel.** Only that it exists in principle, as a standard
   consequence of any field's stress-energy sourcing gravity in GR.
4. **A resolution of `FINDING_P31`'s own status.** `FINDING_P31` remains a
   *phenomenological soft ceiling*, not upgraded to a direct bound by this
   finding — this is one supporting data point toward resolving that
   question, not the resolution itself.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction of
   P1's action — not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P32_photon_decoupling_mechanism_frame_gate.py
```
