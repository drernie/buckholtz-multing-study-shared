# FINDING P152 — S1 (non-gradient-sourced moment) is closed for any
# construction that inherits F_oP's own established universal-kernel
# factorization — narrower than "closed in general," per skeptic review

**Date:** 2026-08-28 (corrected same day, context-asymmetric skeptic review)
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 math
(internal consistency / structural closure of an escape route named in
`FINDING_P4`)
**Verdict:** `S1-CLOSED-FOR-DOCS125-FACTORIZATION-AT-SYMBOLIC-LIMIT-LEVEL`
(twice-renamed: `S1-CLOSED-FOR-PAIRKERNEL-CHANNEL` → overclaimed
"regardless of mechanism," see §0 → `S1-CLOSED-FOR-UNIVERSAL-KERNEL-
CHANNEL` → overclaimed uniqueness (W1) and applicability generality (W2),
see §0b — this final name says exactly and only what §3/§4 establish:
closed for the specific factorization `docs/125` exhibited, at the level
of the `r→∞` symbolic limit, not a re-verified physical-applicability
claim beyond what `docs/127` itself already checked)
**Origin:** `FINDING_P4` (2026-08-10/11) named two live, uncomputed escape
routes for a genuine two-field completion (Branch B) to simultaneously
match MULTING's near-field ladder and source a nonzero background `H(z)`:
**S1** (a moment sourced by something other than a potential gradient —
intrinsic spin, a non-gradient background VEV, an equation-of-state
parameter) and **S2** (a `ψ` with its own distinct/screened propagator).
Neither had been computed; the user directed continuing S1 first, before
S2, explicitly not jumping to TeVeS/Horndeski.
**Script:** `P152_S1_general_pairkernel_background_closure.py` (symbolic
sympy, positive control against `docs/127`'s own two established cases,
plus an explicit — not merely asserted — n=0 screened-case check added
after skeptic review, ruff clean, does not touch the 881-test suite)

## 0. Correction (context-asymmetric skeptic review, same day)

The first version of this file claimed the closure holds "regardless of
the mechanism that produced" the pair-kernel correction — "the S–S formula
only sees the radial falloff... not the mechanism that produced it." A
context-asymmetric skeptic review (claim + code + explicitly cited source
docs only, no session history) found this claim **overreaches**, and
found the overreach traces to a real prior failure mode already on
record in this project:

**`docs/124` (2026-07-19) was itself FALSIFIED** for exactly this framing.
Its "naive form" tried to map `F_oP` into a single `φ(r)` shared by every
pair; the skeptic that killed it showed Shtanov–Sahni's own convolution
machinery (`∫[ρ(r')−ϱ]φ(|r−r'|)d³r'`) requires the kernel to be
**universal across pairs** — the same function of `r` for every pair —
and `F_oP`'s naive mapping `φ(r)=V(r)/(m_Am_P)` is **not** universal,
because it depends on `k_A/m_A`, `k_P/m_P` individually, not on `r` alone.
"The S–S formula only sees the radial falloff, not the mechanism" is
*exactly* the framing that failed once already in this project's own
history — restating it unqualified in P152 silently reintroduced the same
risk.

**What rescues P152's actual result, checked against the primary
sources, not asserted:** `docs/125` (same day as `docs/126`/`docs/127`,
2026-07-21) proved — algebraically, sympy-CONFIRMED, independent of P152
— that `F_oP` admits an **exact 2×2 bilinear factorization**
`F_oP = Q_iᵀ K(r) Q_j` with charge vectors `Q_i=(m_i, k_ir_i)` and a
**global, pair-independent** kernel matrix `K(r)` (`κ_mm=G`,
`κ_mq=Gβ_d/c²`, `κ_qq=Gβ_q²/c⁴` — constants, not functions of any
particular pair's own `k`, `m`, `r`). This is precisely the "universal
kernel, non-universal amplitude" structure the S–S formula needs: `K(r)`'s
own radial shape is genuinely shared across every pair, while all
per-object variation (however large) lives in the charge vectors, which
multiply the kernel but do not change its `r`-dependence — and the S–S
`G_eff` limit is insensitive to any such overall multiplicative factor
(§2's own general-`C` computation already shows this: the limit is zero
for *any* value of `C`, precisely because `C` never re-enters the
`r→∞` asymptotics).

**docs/125 also recorded an important limit on itself**, which this
correction inherits rather than overrides: the *algebraic* factorization
was `CONFIRMED`, but the *interpretation* "this revives Shtanov–Sahni" was
separately `FALSIFIED` in that same document, because the second charge
`q_i=k_ir_i` has **no known conserved cosmological background** `ϱ_q(t)`
for the convolution's subtraction step. `docs/126`→`docs/127` (P2)
resolved this specific concern **constructively, not by assuming it
away**: rather than needing to derive `ϱ_q(t)`, P2 showed the
`G_eff`-contribution of the `q`-charge terms is exactly zero for *any*
admissible evolution law `q(a)` (frozen or virial-scaling, `ΔH=0` either
way) — making the "what is `ϱ_q(t)`" question moot for the background,
not answered.

**Corrected scope, replacing the first version's unqualified claim:** the
"mechanism-independence" the S–S limit exhibits is legitimate **for any
construction that inherits `F_oP`'s own established universal-kernel
factorization** (`docs/125`) — i.e., any S1 candidate that reproduces
MULTING's near-field ladder via the *same* bilinear `K(r)⊗Q_i` structure
`docs/125` **exhibited** for `F_oP` itself. It is **not** a blanket claim
that *any* non-gradient sourcing mechanism whatsoever automatically
produces a universal kernel — `docs/124`'s own history is the standing
counterexample to that stronger claim. §3/§4 below are rewritten to state
the narrower, correctly-scoped result. The skeptic separately found the
symbolic derivation itself correct (independently re-derived by hand) and
one minor gap — the screened-case `n=0` limit was asserted, not
sympy-evaluated — now fixed in the script (§2).

## 0b. Second correction (second, independent context-asymmetric skeptic
review, same day) — two residual overreaches in the §0 rescue itself

A second skeptic pass, dispatched specifically to attack the §0 rescue
argument (not just accept it because it responds to the first review),
found the mathematical core sound but flagged two further overreaches,
both now fixed:

**W1 — no uniqueness claim in `docs/125`.** The previous version of §0
said `docs/125` "proved is the (unique, sympy-confirmed) way `F_oP`
factors this way." `docs/125`'s own text says `F_oP` **admits** an exact
2×2 bilinear factorization — it demonstrates one factorization exists (and
that a *single-scalar* kernel fails), not that no other bilinear or
higher-order factorization of the same `F_ij` values is possible (e.g. an
invertible linear change of the charge basis, a `3×3` structure separating
`k_i` and `r_i`, or a non-linear charge combination — none tested or
excluded by `docs/125`). "Unique" is struck throughout this file (§0
above, and §3/§4 below); the closure is scoped to *the specific
factorization `docs/125` exhibited*, not *the only possible one*.

**W2 — the general-`n` math fact was quietly promoted to an
applicability claim it does not license.** The previous version said
P152's proof "does not need `ϱ_q(t)` to be known because the S–S limit
kills any `n≥1` term for any amplitude, regardless of the amplitude's own
cosmological evolution or conservation properties" and called this "the
same mechanism restated more generally" as `docs/127`'s resolution. This
conflates two different statements: (a) the narrow, `[FACT]`-level math
result that `lim_{r→∞}[C·r⁻ⁿ − r·d/dr(C·r⁻ⁿ)]=0` for any `n>0`,
independent of `C`'s *value* — true, and all §2 actually establishes; vs.
(b) the stronger claim that the S–S formalism's *applicability* to a
charge sector without a conserved cosmological background is itself
`n`-independent — not established. `docs/127`'s own `ΔH=0` result rests
on a **three-rung convergence**: the same sympy limit P152 generalizes
(rung 1, the weakest — `docs/127`'s own words, "Weak-Medium
independence"), an independent brute-force Monte-Carlo re-derivation with
its own shell-theorem positive control (rung 2, "Strong" independence —
no S–S formula used at all), and the `C1` isotropic-orientation-averaging
N-body test with its own aligned-control (rung 3, a *different*
mechanism). P152 generalizes only rung 1 (the sympy limit) to arbitrary
`n>0`; it does not extend rungs 2 or 3 beyond the specific integer powers
(`n=1,2,3,4`) `docs/127` actually tested. The applicability warrant for
`ϱ_q(t)`-free charges therefore still rests, for `n>0` values beyond what
`docs/127` explicitly checked, on accepting that rungs 2/3 generalize the
same way rung 1 provably does — an assumption, not a re-derivation, and
now stated as such rather than folded silently into "the same mechanism
restated more generally."

## 1. Why S1 was still open

`docs/127` (P2) already found `G_eff=0` in the Shtanov–Sahni background
closure for MULTING's own dipole (`f(r)~1/r`) and quadrupole
(`f(r)~1/r²`) terms, and its own follow-up "C1" test confirmed this holds
even keeping the dipole's full vector/anisotropic character — but via a
**different mechanism** (isotropic-orientation washout, `⟨n̂⟩=0`) than the
plain radial-asymptotic limit. Separately, `FINDING_P4`'s skeptic review
found that P1's own construction (`p_i=κk_ir_i/c²`) is **already**
intrinsic/non-gradient, not gradient-induced — so the specific argument
that killed "Part B" (a moment must be gradient-induced, hence vanish on
a homogeneous background) never actually applied to this project's own
code, and the pearl-registry entry recording this explicitly flagged
S1/non-gradient sourcing as **live and untested**, not closed.

Two different zero-mechanisms (radial-asymptotic for the scalar
quadrupole; orientation-averaging for the vector dipole) had each been
checked for one specific case. It was not established whether the zero
is a structural fact about the S–S formula covering *both* mechanisms at
once — which would close S1 for the whole class of pair-kernel-type
completions — or a coincidence of the two powers already tested.

## 2. Method — general symbolic proof, not case-by-case

For `φ(r) = -(G/r)f(r)`, `G_eff = G·lim_{r→∞}[f(r) − r f'(r)]`
(`docs/124`'s own citation of Shtanov & Sahni's Eq. 22). `P152` computes
this symbolically for `f(r) = C·r⁻ⁿ` with `n` left as a **free symbolic
parameter**, not substituted case-by-case:

```
f - r·f' = C·(1+n)·r⁻ⁿ
lim_{r→∞} = 0   for any n > 0
          = C   for n = 0
```

**Positive control:** substituting `n=0` reproduces `docs/127`'s own
`G_eff=G` monopole result exactly; substituting `n=1,2` reproduces its
own `G_eff=0` dipole/quadrupole results exactly — confirming the general
symbolic form is not a different (possibly wrong) derivation before
trusting it for untested `n` values.

A second case, `f(r) = C·r⁻ⁿ·e^{-μr}` (screened/Yukawa-type, `μ>0`), is
also computed symbolically: the limit is zero for **any** `n≥0`,
including `n=0` — an exponentially-screened correction kills even a
monopole-shaped term at `r→∞`, consistent with (not contradicted by)
`P149`'s separate finding that a massive mediator suppresses the same
project's kernel invariant at large `r`.

## 3. Result

The zero is **not** a coincidence of the two specific powers `docs/127`
tested. It is a structural property of the `r→∞` limit itself: **any**
pair-kernel correction whose radial profile falls off strictly faster
than `1/r` (any power `n>0`, or any exponentially-screened form)
contributes exactly zero to the Shtanov–Sahni background `G_eff`,
**independent of**:

- which multipole tier it represents (dipole, quadrupole, or higher),
- whether the sourcing moment is a **vector** (which would separately
  need the `C1` orientation-averaging argument to vanish under isotropic
  population-averaging) or a **scalar** (spin-squared, an
  equation-of-state parameter, `k_i·k_j`) that has no orientation to
  average away in the first place,
- whether the moment is **gradient-induced or intrinsic** (non-gradient),
- **and — per §0's correction, narrowed further by §0b's W2 fix — how
  large or non-universal the moment's own *amplitude* `C` is, as far as
  the `r→∞` limit itself is concerned**, provided that amplitude
  multiplies a kernel whose *radial shape* is itself universal across
  pairs, which is what `docs/125`'s factorization theorem exhibits for
  the specific 2×2 structure it built for `F_oP` (not proved unique,
  §0b W1). The *applicability* of the S–S formalism to a charge sector
  with no known conserved background, beyond the specific integer powers
  `docs/127` verified via its independent MC and `C1` rungs, is inherited
  as an assumption, not re-derived at general `n` here (§0b W2) — this is
  a narrower, better-grounded statement than "the mechanism never
  matters," and a narrower one still than the first correction (§0)
  itself stated.

## 4. Consequence for S1

**S1 (non-gradient-sourced moment) is closed for constructions that
reproduce MULTING's near-field ladder via the specific bilinear
`K(r)⊗Q_i` factorization `docs/125` exhibited for `F_oP`** (any tier
`n≥1` in that universal kernel, at the `r→∞`-limit level the S–S formula
itself computes) — not merely for the two specific cases (vector dipole
via orientation-averaging; scalar quadrupole via the radial limit)
already computed separately, and not merely by assuming universality as
P152's first version implicitly did. Within that structure, no choice of
non-gradient sourcing mechanism — intrinsic spin, an equation-of-state
parameter, a non-gradient background VEV — can rescue a nonzero
contribution to the `r→∞` limit itself, because the amplitude never
re-enters that limit regardless of its own physical origin (§0, §2); the
*applicability* of the limit's zero value as the actual background
coupling, for `q(a)`-type charges beyond the specific powers `docs/127`
independently verified, is an inherited assumption (§0b W2), not a new
independent re-derivation.

**This closes S1 for the specific case `docs/125` exhibited** — a real,
non-trivial narrowing of the open question, not the unqualified "S1 as
originally posed, however sourced, however structured" claim the first
version of this file overstated, and not the "the unique way `F_oP`
factors" framing the first correction itself briefly overstated (§0b W1).
Whether some *other* completion could reproduce the same near-field
forces through a structurally different factorization, or through a
structurally different route entirely (anisotropic/non-central,
velocity-dependent, or genuinely three-body-irreducible — none of which
reduce to a single `f(r)` at all), is a separate, **unresolved** question,
now stated as an explicit open item below rather than silently assumed
away.

## What this file does NOT establish

0. **Does not establish that reproducing MULTING's near-field ladder
   *requires* a construction expressible as a central, static, scalar
   pair potential `φ(r)=-(G/r)f(r)` at all** — the skeptic named three
   structurally different routes not addressed here: (a) an anisotropic
   / non-central force (MULTING's own dipole is already a vector,
   `docs/127`'s own `C1` test uses the full `[p−3(p·r̂)r̂]/r³` form, not a
   scalar reduction — its zero comes from isotropic orientation-averaging,
   a *different* mechanism than this file's radial-asymptotic argument,
   and nothing here proves a completion whose anisotropy does *not*
   average away under isotropy is impossible); (b) a velocity-dependent
   or retarded force; (c) a genuinely three-body-irreducible interaction.
   None of these have a well-defined `f(r)` for the S–S formula to act
   on in the first place, so this file's closure does not cover them.
   `docs/125`'s factorization theorem establishes that `F_oP` *itself*
   has the bilinear `K(r)⊗Q_i` form — it does not prove that form is the
   *only* way to reproduce `F_oP`'s force values.
1. **Does not close the channel `FINDING_P4` §5 already separately
   flagged**: a second scalar `ψ`'s own homogeneous background mode
   (`ψ_bg(t)`, `V(ψ)`) can source `H(z)` via ordinary quintessence-type
   physics, entirely independent of the S–S pair-kernel channel tested
   here, and independent of whether `ψ` carries any MULTING `k`-charge
   structure at all. This was already correctly identified as generic to
   *any* scalar field and *not specific to MULTING* — this file does not
   reopen or resolve that question, only confirms the *other* route (S1
   via the pair-kernel channel) does not provide a MULTING-specific
   escape either.
2. **Does not touch S2** (screened/distinct propagator) — a separate,
   still-open question, per the user's own stated priority (S1 before
   S2, explicitly not TeVeS/Horndeski).
3. **Not a claim about MULTING's own theory** (`NO_AUTHOR_ERROR`) —
   entirely this project's own reconstruction of the S–S background
   closure applied to its own candidate completion.
4. **Assumes the S–S closure formula itself is the correct background
   test** — the same closure `docs/127`/`P2` already used and validated
   (independent MC re-derivation, `C1` vector test); this file does not
   re-litigate whether that closure is the right physics, only whether
   its own zero result generalizes.
5. **`C=const` is assumed** in the power-law family — a coefficient that
   is itself time-dependent (`C=C(a)`) was already shown irrelevant to
   this specific limit in `docs/127`/`P2` (the `q(a)` evolution-law test,
   `ΔH=0` for both frozen and virial `q(a)`) and is not re-derived here;
   this file's own contribution is the **power/mechanism** generality
   (any `n`, any vector-or-scalar sourcing), not the **time-dependence**
   generality (already covered by P2).
