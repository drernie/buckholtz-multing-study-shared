# P26 — the "Level 3" covariant-action route: T_μν gives a real ρ_φ, but its equation of state is curvature-like (w=-1/3), not dark-energy-like

**Date:** 2026-08-13
**Origin:** user-directed roadmap (P24→P27), third item — "Level B": derive
cosmology from the action itself (`S → T_μν → ρ_φ,p_φ → H(z)`), not the
old manual force-to-`H(z)` bridge. Before building this blind, checked the
project's own prior context — found this is the long-deferred endpoint of
the *entire* bridge programme, not a fresh question.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P26_stress_tensor_equation_of_state.py`

**[CORRECTED after skeptic review, same day.]** The core math (the general
trace identity, `w=−1/3` for the dipole, the positive control matching
P14's formula) all survive as `CONFIRMED-REAL`. **One real overclaim, not
just framing**, in the original §2/§4: calling the corrected `E_self`
"**fully-corrected**." It is not. `FINDING_P14`'s own §6 (added the day
*before* this finding, and already read and quoted during this finding's
own research phase) documents that `E_self` — as computed by *any* version
of this formula, corrected or not — carries units `kg²/m`, not an energy
(`p` has units `kg·m`, so `p²/r_min³` is `kg²/m` regardless of the
numeric prefactor). The `1/(32π²)` factor found here is a real, additional
correction, but it does **not** touch that deeper dimensional gap — it
divides a wrong-units quantity by a pure number, which is still a
wrong-units quantity. §2 and §4 are corrected below. Also softened: §1's
framing of the trace identity as a discovery (it is standard, textbook
scalar-field cosmology — the novel part is applying it *here*, not the
identity itself), §3's "`ρ_φ` redshifts as `a⁻²`" (a fluid-limit
extrapolation, not derived on an actual FLRW background), and the implicit
`ρ_φ=n·E_self` population formula (silently drops cross-terms between
different sources — licensed as an *approximation* by P15/P16's own
already-established self-dominates-cross result, not an exact statement,
and not something the `w=−1/3` robustness argument by itself licenses).
See the Skeptic Verdict section for the full seven-claim breakdown.

## 0. Context chain — this question has a real history in this project

1. **`FINDING_effective_fluid_energy_scale.md` (2026-08-03)** — the naive
   statistical-mechanics "pair-fluid" bridge (MULTING potential →
   Layzer–Irvine energy → `ρ_pair` → `H(z)`) fails by **4–5 orders of
   magnitude**. Its own closing table says explicitly: *"the covariant-
   action route of level 3 [is] the only surviving route."* P26 is that
   route, six weeks and 25 findings later.
2. **P1 §4.3 (2026-08-10)** — the *force* on a test particle from an
   isotropic, randomly-oriented shell of dipoles averages to **exactly
   zero** (the "double layer," `FINDING_dipole_shell_is_a_double_layer.md`)
   — a narrower, **first-moment** result about forces, not energy density.
3. **P13a (2026-08-12, corrected)** — explicitly flags that a zero mean
   *force* (`⟨δ⟩=0`) does **not** imply zero *energy density* or power
   spectrum (`P(k)=0`) — names this the genuinely open next calculation.
4. **P14 (2026-08-12)** — computes the self-energy channel, but its own
   corrected §1 flags a real, unresolved tension: does self-energy survive
   ensemble averaging, or does it cancel against cross-terms the way P9's
   idealized *continuous* shell does?
5. **P15/P16 (2026-08-12)** — **resolve** that tension for realistic,
   *discrete* populations: self-energy is real and **dominant** over
   cross-terms (~4×10⁻⁵ to 1.4×10⁻⁴) at realistic cluster separations. The
   continuum cancellation P9 found does not extend to the physically
   realistic discrete case. Note: "dominant" means cross-terms are *small
   relative to* self-terms, not exactly zero — the `ρ_φ=n·E_self`
   formula below (§2) is therefore an approximation at that level of
   precision, not an exact statement.
6. **[Added after skeptic review] P14 §6 (2026-08-12, added one day before
   this finding)** — independently found that `E_self` as computed by
   *any* version of the self-energy formula carries units `kg²/m`, not an
   energy — a missing normalization constant, separate from `κ` and
   separate from P19's geometric `1/(4π)` factor, whose value is not
   fixed anywhere in this project. This finding was read in full during
   this finding's own research phase (quoted directly, see §2's positive
   control below) — its implication for §2's own "corrected" formula was
   missed in the original version and is fixed here.

Given (5) already resolves (4)'s tension in favor of "self-energy
survives," this finding does what (3) named as open: compute `T_μν`
directly and extract the equation of state.

## 1. Method

Canonical stress tensor `T_μν = ∂_μφ∂_νφ − η_μν(1/2)(∂φ)²`, matching the
action's own `(1/2)(∂φ)²` kinetic term (`two_field_action_closure.py` line
111) — static limit, consistent with every finding P9–P25. First proved a
**general** identity (sympy, arbitrary profile `f(r,θ)`, not special to the
dipole), then applied it to P19's normalized dipole field, then
cross-checked the volume integral of `T_00` against P14's own already-
verified `E_self` formula as a positive control.

## 2. Result

**General identity** (structural, any static scalar profile in 3D):

```
Trace(T_ij) = −T_00
```

verified symbolically for a generic `f(r,θ)`, not assumed. This makes what
follows a *robust* fact, not a fragile feature of the dipole's specific
angular shape.

**Applied to the P19-normalized dipole**, `φ=p·cosθ/(4πr²)`:

```
w = P/ρ = (1/3)·Trace(T_ij)/T_00 = −1/3   (POINTWISE, angle-independent)
```

Since `P(x)=−(1/3)ρ(x)` holds **pointwise**, this survives *any* linear
averaging or integration exactly — angle-averaging, volume-integrating
from `r_min` to `∞` (the same domain `E_self`'s own integral uses), or
ensemble-averaging over many randomly-oriented sources all give the same
`w=−1/3`, with no averaging-order-of-operations subtlety to worry about.

**Positive control**: volume-integrating `T_00` in P14's *own* (pre-P19,
un-normalized, no canonical `1/2` factor) convention reproduces P14's
already-skeptic-verified `E_self=(8π/3)p²/r_min³` **exactly** — confirming
the stress-tensor machinery here is consistent with this project's prior
work before trusting the new result built on top of it.

**A previously-unflagged factor-of-2, found via that same cross-check**:
P14's own `E_self` was computed as `∫(∇φ)²dV` — the *bare* gradient-squared
integral, **without** the canonical `(1/2)` factor from the action's own
kinetic term. Combined with P19's already-known `1/(4π)` geometric
normalization, the fully-corrected self-energy is:

```
E_self,correct = p²/(12πr_min³) = E_self,P14 / (32π²)
```

**[Corrected after skeptic review — "fully-corrected" was a real overclaim,
not just a framing issue, struck through below.]**

~~This does not change any qualitative conclusion — Ω_φ's absolute scale
was already blocked by A, κ being individually unknown (P17, P21, P22) —
it's one more, now-identified, order-unity factor to fold in whenever
that gap is eventually resolved.~~

`E_self,correct = p²/(12πr_min³)` is **not** dimensionally an energy —
`p` has units `kg·m` (established), so this quantity carries units
`kg²/m`, exactly the same wrong-units problem `FINDING_P14`'s own §6
already identified for the *uncorrected* formula. The `1/(32π²)` factor
found here is a valid, additional numeric correction on top of P19's
already-known geometric normalization — but dividing a wrong-units
quantity by a pure number does not fix its units. **A separate,
still-undetermined normalization constant** (the same one P14 §6, P17,
P21, and P22 already flagged as blocking any numeric `Ω_φ` value) is
still required before `E_self` — corrected or not — is a genuine energy.
This finding's real, surviving contribution is narrower: the `1/(32π²)`
*numeric prefactor* correction is real and additional to P19's own
`1/(4π)²`, to be applied *whenever* that separate normalization gap is
eventually closed — not a claim that it is closed here.

## 3. What this means, stated carefully

`w=−1/3` is the **curvature** equation of state: `ρ+3p=0` identically,
contributing **zero** to the Friedmann acceleration equation (`ä/a ∝
−(ρ+3p)`) — verified directly from the standard Friedmann acceleration
equation, not just asserted. This is **not** dark-energy-like — dark
energy needs `w<−1/3` (strict inequality) to source accelerated expansion.
**[Corrected after skeptic review]** In the *static-fluid approximation*
(the same approximation this project's own force/energy calculations have
used throughout), a component with constant `w=−1/3` would redshift as
`a⁻²`, exactly like spatial curvature `Ω_k`. This is a **fluid-limit
extrapolation, not something derived here on an actual FLRW background** —
this finding computes the static, flat-space `T_μν` and its equation of
state; it does not solve the field equations for `φ` evolving on an
expanding background, where Hubble friction and other effects could in
principle shift the effective `w` away from the static value. Still, the
static-limit result is a real, distinct redshift dependence from `Λ` or
matter — a **qualitatively different** kind of modification than "new
dark energy," not a quantitatively-smaller version of one.

**This does not contradict P1's own force-based null result, but the
consistency is not automatic — it depends on a specific, named prior
resolution, not just an analogy.** **[Corrected after skeptic review]**
The abstract point — a zero *mean* field (`⟨∇φ⟩=0`, P1's result) does not
imply zero *variance* (`⟨(∇φ)²⟩`, this finding's `T_00`) — is correct and
standard (the photon-gas comparison illustrates this general principle: an
isotropic radiation bath exerts zero net force at a center of symmetry
while its energy density and pressure fully source expansion). But P1's
own result is stronger than "the mean force is zero" — it establishes the
potential is *constant* (hence zero-gradient) essentially everywhere for
the idealized continuous shell, which is precisely the configuration P14
§1 shows would force cross-terms to exactly cancel self-terms if it
applied to the physically realistic case too. **The consistency between
P1 and this finding therefore rests specifically on P15/P16's resolution
that self-energy survives for discrete, realistic populations** (§0 item
5) — not on the mean-vs-variance analogy alone, which by itself would be
compatible with either outcome (self-energy surviving or self-energy
being exactly canceled, as P9's continuum limit shows it can be).

## 4. What this does NOT establish

1. **A numeric value for `ρ_φ` or `p_φ` — and not merely because `A`,`κ`
   are unknown.** **[Corrected after skeptic review]** `E_self,correct`
   (§2) does not even have the right *units* to be an energy — the same
   deeper dimensional gap `FINDING_P14` §6 already identified survives
   this finding's own correction unchanged. This finding's contribution is
   the *functional form* (`ρ_φ=n·E_self`, `p_φ=−ρ_φ/3`) and one additional
   numeric prefactor (`1/(32π²)`), not a step closer to a trustworthy
   number.
2. **A solved `H(z)`.** Only `ρ_φ`, `p_φ`'s *functional relationship* is
   derived here — actually solving the Friedmann equations with this
   `T_μν` as a source on an FLRW background (the final step of
   "`S→T_μν→ρ_φ,p_φ→H(z)`") is a further step, not attempted.
3. **Whether this component is large enough to matter at all.** `w=−1/3`
   only says *what kind* of term this is (curvature-like); whether `Ω_φ`'s
   magnitude is cosmologically significant remains exactly as unknown as
   before this finding.
4. **That `w=−1/3` is a novel discovery.** **[Added after skeptic review]**
   `Trace(T_ij)=−T_00` for a static massless scalar is standard, textbook
   scalar-field cosmology — the contribution here is applying it to this
   project's own reconstructed field, not the identity itself.
5. **That `ρ_φ=n·E_self` (dropping cross-terms) is exact.** **[Added after
   skeptic review]** P15/P16 established self-energy *dominates*
   cross-terms at realistic separations — a leading-order approximation,
   not an exact cancellation-free statement. The `w=−1/3` robustness
   argument (§2) licenses averaging the *ratio* this way; it does not by
   itself license dropping cross-terms from the *amplitude*.
6. **That `w` stays `−1/3` once `φ` actually evolves on an expanding
   background.** **[Added after skeptic review]** Only the static,
   flat-space equation of state is derived — see §3's correction.
7. **The monopole (`g`) sector's own equation of state.** The general
   trace identity applies structurally to *any* static profile, including
   the monopole's own gradient energy — not quantified here; this finding
   focuses on the `κ`/dipole sector, consistent with P14–P25's own scope.
8. **Whether the near-source region (`r<r_min`, where P20 found the
   point-dipole idealization breaks down) needs separate treatment.** The
   integral defining `E_self` already excludes this region (same `r_min`
   cutoff as P14–P20); this finding does not re-examine that boundary.
9. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P26_stress_tensor_equation_of_state.py
```

## Skeptic verdict (context-blind, Step 8a, 2026-08-13)

Given only this file, the script, `two_field_action_closure.py`,
`FINDING_P14_kappa_normalization_unfixed.md`, and
`FINDING_effective_fluid_energy_scale.md` — no session history. The
skeptic's own tool access could run the script and independently
hand-re-derived every symbolic result before accepting it, including a
from-scratch re-derivation of the stress tensor using an independent
signature convention (mostly-plus vs. mostly-minus) as a cross-check on
sign errors. **Explicit scope disclosure by the skeptic itself**: P15/P16
were not among the files provided, so any claim resting on their
resolution of P14's tension is marked `[NOT-VERIFIABLE-IN-SCOPE]` rather
than confirmed or denied. Seven sub-verdicts, per Step 8a (not merged):

- **(a)** General trace identity: **CONFIRMED-REAL**, independently
  re-derived from the standard scalar stress tensor and cross-checked via
  the 4-trace `T^μ_μ`; framing **WEAKENED** — this is standard, textbook
  scalar-field cosmology (Peebles & Ratra), not a novel identity. *Applied:
  §1's framing softened; the true contribution named as applying it here.*
- **(b)** Specific dipole `w=−1/3`: **CONFIRMED-REAL**, independently
  re-derived by hand from `φ=p·cosθ/(4πr²)`.
- **(c)** Physical characterization: **CONFIRMED-REAL** for the static-
  fluid statement (`ρ+3p=0` verified against the actual Friedmann
  acceleration equation); **WEAKENED** on "`ρ_φ` redshifts as `a⁻²`" — a
  fluid-limit extrapolation, not derived on an actual FLRW background.
  *Applied: §3 corrected.*
- **(d)** Positive control: **CONFIRMED-REAL** — independently re-derived,
  the bare-integral algebra reproduces P14's `(8π/3)p²/r_min³` exactly.
- **(e)** "Factor of 2... fully-corrected": **WEAKENED, close to
  FALSIFIED on the "fully-corrected" wording specifically** — the
  arithmetic (`1/(32π²)`) is correct, but `FINDING_P14`'s own §6 (read
  during this finding's own research phase, then not carried through to
  its own conclusion) already documents that `E_self` — any version of it
  — has units `kg²/m`, not an energy. *Applied: FIXED — §2 corrected,
  "fully-corrected" removed, the deeper dimensional gap stated explicitly.*
  This was the single most consequential specific overreach the skeptic
  found.
- **(f)** Citation chain: **WEAKENED** — the 2026-08-03 quote and P14 §1
  tension are cited accurately, but the original version selectively
  omitted P14 §6 (which undermines the "fully-corrected" claim) while
  citing P15/P16 (which support the finding) — an asymmetry not
  necessarily intentional but real. *Applied: §0 item 6 added, citing
  P14 §6 explicitly.*
- **(g)** "Does not contradict P1" / photon-gas analogy: **WEAKENED** —
  the abstract mean-vs-variance logic is correct, but P1's own result is
  stronger than "mean force is zero" (it shows the potential is *constant*
  for the idealized continuous case, which P14 §1 shows would force exact
  cancellation if it extended to the discrete case) — consistency between
  P1 and this finding rests specifically on P15/P16's resolution, not on
  the analogy alone. *Applied: §3's closing paragraph corrected to name
  this dependency explicitly.*

**Additional finding, not in the seven claims**: the implicit
`ρ_φ=n·E_self` population formula silently drops cross-terms between
different sources; the `w=−1/3` robustness-under-averaging argument
licenses this for the *ratio*, not for treating the *amplitude* as exact.
*Applied: added to §4 item 5.*

**Not a core-predicate-false kill.** The core mathematical results — the
general trace identity, `w=−1/3` for the dipole, and the positive control
— all survive independent re-derivation fully intact. What was withdrawn
is the "fully-corrected" overclaim (a real, specific factual error, not
just framing) and several places where the finding's own scope was stated
more strongly than what was actually shown.
