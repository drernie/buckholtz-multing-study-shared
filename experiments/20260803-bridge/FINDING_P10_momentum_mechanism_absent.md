# P10 — does the theory's own action have a velocity/momentum-coupled source term? No.

**Date:** 2026-08-12 · checks the third candidate mechanism for P9's flagged gap
(§4(a)/(c) of `FINDING_P9_linear_order_is_nonzero.md`: some mechanism must
correlate the induced/effective dipole strength with a global direction for a
real cosmological `δ` to produce a nonzero `ε`, and none has been shown to
exist in this project). P4 already checked and ruled out one candidate
(gradient-of-Φ sourcing, in the *current* construction). This checks a
different, previously unexamined candidate: does the actual field action
contain any term coupling the dipole moment to a body's own **velocity or
momentum**, which — via the standard linear-theory relation between peculiar
velocity and `∇δ` — could provide exactly the missing correlation without
requiring a new, ad hoc assumption.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Method:** direct inspection + tool-verified grep of the two source files
that define this project's own field-theoretic construction — no new
computation needed, this is a structural/provenance check (Gate 1/2 in
spirit: what does the artifact actually contain, not what it is assumed to
contain).

**[CORRECTED after skeptic review, same day.] Verdict 1 (the raw grep
result and the static/internal characterization of `r_i`) is CONFIRMED-REAL
— independently re-verified symbol-by-symbol, including aliases the grep
pattern would have missed (`u`-ratios, `beta`, `gamma`, `boost`, `Lorentz`).
Verdict 2 (framing this as a "third checked-and-absent channel," parallel
in kind to P4 and P9) is WEAKENED — the skeptic found `two_charge_completion.py`
contains no time coordinate at all (a pure static Coulomb sum over fixed
positions), so the negative result is close to a predictable consequence
of the code's own structure, not a substantive mechanism check on the level
of P4 (which identified what mechanism the code DOES use) or P9 (which ran
an actual calculation). See "Skeptic verdict" section below; §3's framing
is corrected accordingly.**

---

## 1. The question, precisely

Peculiar velocity is not an ad hoc quantity — in linear cosmological
perturbation theory it is directly sourced by the density perturbation via
the continuity equation, `∂δ/∂t + ∇·v⃗ = 0`, giving the standard growing-mode
relation (curl-free, parallel to `∇Φ_v` with `∇²Φ_v = -δ`):

```
v⃗(k) = i (f a H) (k̂/k) δ(k)          [linear theory, e.g. Dodelson "Modern
                                        Cosmology" ch.5, or Peebles 1980]
```

A cluster's own peculiar velocity is therefore, on average, **coherently
correlated with the local `∇δ` direction** — unlike a pair's separation
vector (which P9's skeptic review found is not obviously correlated with any
global axis under isotropic pairing) or a static intrinsic moment (which P4
found is not gradient-responsive). If the theory's dipole source term `p_i`
depended on a body's own velocity/momentum, this would supply, for free, the
"additional alignment-correlation mechanism" P9's skeptic said was missing —
no new physical assumption needed beyond linear perturbation theory itself.

**So: does it?**

## 2. The check

The full stated action, from `two_field_action_closure.py` (P1, quoted
verbatim, its own inline print output):

```
S = int d^4x [ (1/2)(d phi)^2 ]
    + sum_i int dtau [ g m_i + p_i . grad ] phi(x_i),   p_i = kappa k_i r_i/c^2
```

`r_i` here is not the body's position in space or its trajectory — it is the
same internal structural displacement used throughout
`two_charge_completion.py`'s point-charge construction (`tiers_from_kernel`,
this same directory): body A is built as `{m_A at 0, +q_A at d_A/2, -q_A at
-d_A/2}`, i.e. `d_A` (identified with `r_A`, per P1's own docstring: "lever
arm identified with r_A") is the **internal charge-separation length scale**
of body A's own dipole structure — a fixed, static property of the body, the
same quantity `β_d = 2, β_q = √6` were derived from with "zero free
parameters after `κ`" in `FINDING_two_charge_completion.md`.

Tool-verified check — grep both files that define this construction for any
velocity- or momentum-related symbol:

```bash
grep -inE "veloc|momentum|\bv_[a-z]|xdot|\\\\dot|u\^mu|four-velocity|peculiar" \
    experiments/20260803-bridge/two_field_action_closure.py
# exit code 1 (no match)
grep -inE "veloc|momentum|\bv_[a-z]|xdot|\\\\dot|u\^mu|four-velocity|peculiar" \
    experiments/20260803-bridge/two_charge_completion.py
# exit code 1 (no match)
```

Zero matches in either file. The worldline integral `∫dτ` is the standard
parametrization for *any* point-particle source term in a scalar-field
action (the monopole term `g·m_i` uses the identical `∫dτ` — this alone does
not introduce velocity-dependence into a term's magnitude or direction; it
only reflects that the source is evaluated along the body's trajectory). The
coupling `p_i · ∇φ(x_i)` evaluates a **fixed** vector `p_i` at the body's
instantaneous position — `p_i` itself, per its own defining formula
`κ·k_i·r_i/c²`, carries no velocity or momentum dependence whatsoever.

## 3. The result

**No velocity/momentum-coupled source term exists in this project's own
field-theoretic construction, as actually written.** The dipole moment
`p_i` is built entirely from static, internal, body-frame quantities
(`k_i`, `r_i`) — confirmed by direct grep, not just by reading.

**[SUPERSEDED framing — see the corrected paragraph after this one.]**
~~This closes a **third** candidate channel for the mechanism P9's skeptic
review said was missing, joining:~~

- P4: gradient-of-Φ sourcing — checked, **absent** from the current
  construction (two live, *unbuilt* escape routes named: non-gradient
  intrinsic moment, screened/massive propagator).
- P9 (via its own skeptic review): isotropic orientation-averaging of
  pairwise-radial alignment — **gives zero**, no additional correlation
  shown to arise from density modulation alone.
- ~~P10 (this finding): velocity/momentum coupling — **absent** from the
  current construction, grep-verified.~~

**Corrected framing (post-skeptic):** P10 is not parallel in kind to P4 or
P9. P4 identified what mechanism the code *does* use in place of the ruled-
out one, and named specific live alternatives. P9 ran an actual numerical
calculation, independently re-derived to 6 significant figures. P10 checked
whether one specific, lexically-searchable candidate (velocity/momentum
coupling) is present in a code base that was never built with such a term
in mind — `two_charge_completion.py` computes a purely **static** Coulomb
pair-energy sum over fixed positions, with no time coordinate anywhere in
the code. A grep-confirmed absence of velocity terms in code that contains
no dynamics at all is close to a predictable consequence of the code's own
structure, not a substantive test on the same footing as P4's mechanism
identification or P9's real computation. What P10 actually establishes is
narrower: **one specific candidate mechanism (velocity/momentum coupling)
has not been deliberately built into this project's construction, and it
remains genuinely unknown whether such a construction is even possible
while respecting the `A↔B` mirror-symmetry constraint that fixed the
existing radial dipole orientation** — a scope statement about what exists,
not a mechanism ruled out by testing it.

**Important scope limit, exactly parallel to P4's own escape-route framing:**
this shows the mechanism is **not present in the construction as built**, not
that it is **impossible in principle**. Nothing here rules out extending the
action with an explicit velocity-coupled term (e.g. `p_i = κ·k_i·v̂_i/c` or a
current-current coupling analogous to gravitomagnetism) — that would be a
genuinely different, unbuilt construction, and building it was not attempted
here (per the "cheapest differentiating test" discipline: check what exists
before proposing what to build). Whether such an extension would still
respect the `A↔B` mirror-symmetry constraint that fixed the *radial* dipole
orientation in `two_charge_completion.py` is itself an open question this
finding does not address.

## What this does NOT establish

1. **That a velocity-coupled completion is impossible.** Only that the
   construction actually built and used for `β_d=2, β_q=√6` (P1) does not
   have one. An unbuilt alternative remains open, per §3.
2. **A resolution of P9's "still UNDETERMINED" status.** If anything, this
   narrows the space of live mechanisms further — three checked, three
   absent, two still-open-but-unbuilt escape routes remain (P4's own list,
   neither velocity-related).
3. **That linear-theory peculiar-velocity correlation with `∇δ` (§1) is
   itself in question** — that relation is standard, independently
   established cosmology, cited `[DOCS]`, not something this project derived
   or is testing; only its *relevance* (whether this theory's dipole moment
   actually couples to it) is what was checked, and the answer is no.
4. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction (the
   two-field/two-charge completion built in P1), not a claim about TJB's own
   unpublished theory.

## Skeptic verdict (context-blind, 2026-08-12)

Two separate verdicts, per Step 8a / Context Asymmetry (skeptic given only
this file, the two source files, and the two cited prior findings — no
session history):

- **Empirical content** (grep result; `r_i` characterized as static/
  internal, not kinematic): **CONFIRMED-REAL.** Independently re-verified
  symbol-by-symbol, checking aliases the grep pattern could have missed
  (`u`-ratios, `beta`, `gamma`, `boost`, `Lorentz`, dot-notation). Every
  symbol in both files is a static geometric quantity, a mass, a charge, a
  static structural coupling, or series-expansion bookkeeping. One
  subtlety raised and then dismissed by the skeptic itself: a genuinely
  *covariant* reading of `p^μ` (4-vector, not 3-vector) would carry
  implicit boost-dependence in a lab frame via `dτ=dt·√(1−v²/c²)` — but the
  code never implements the covariant action, only static pair energies at
  fixed positions, so this does not affect the verdict on the code as
  actually written.
- **Framing** ("closes a third checked-and-absent channel," parallel to P4
  and P9): **WEAKENED.** `two_charge_completion.py` contains no time
  coordinate at all — a pure static Coulomb sum over fixed positions — so
  the negative grep result is close to what any competent reader would
  predict from the code's visible structure without running it. P4 and P9
  both did substantive work (mechanism identification; an actual
  computation) that P10 does not match. The finding's own §"What this does
  NOT establish" already partially conceded this, but the top-line "third
  channel" summary did not carry that caveat with it — corrected in §3
  above.

## Reproduction

```bash
grep -inE "veloc|momentum|\bv_[a-z]|xdot|\\\\dot|u\^mu|four-velocity|peculiar" \
    experiments/20260803-bridge/two_field_action_closure.py \
    experiments/20260803-bridge/two_charge_completion.py
```

Exit code 1 (no output) on both files is the entire empirical content of
this finding — a negative grep result, tool-verified, not a claim from
memory. **What that empirical fact is worth is narrower than first framed
— see "Skeptic verdict" above and the corrected §3.**
