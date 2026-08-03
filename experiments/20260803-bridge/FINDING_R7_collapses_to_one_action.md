# R7's cascade has an exact, closed-form covariant completion

**Date:** 2026-08-03 · Answers the second of two next-steps named in
`GATE1_2_multing_plus_classification.md`: *"ask what covariant action would
need to produce exactly ∇²φ~ρ, ∇²σ~-(∇φ)², ∇²ξ~-φ(∇φ)²."*
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Status: `[VERIFIED]`, exact closed form, cross-checked two independent ways.**

This supersedes the same-day earlier version of this file, which only
checked a perturbative truncation to two orders and left a numerical factor
unexplained. That factor is now explained — see §3.

---

## 1. The exact field redefinition

Start from the field-dependent-kinetic action (found earlier the same day,
matching R7's first-order term exactly):

```
L = 1/2 * f(Phi) * (d Phi/dr)^2 ,     f(Phi) = 1 + 2*eps*Phi
```

Define `chi` by `dchi/dPhi = sqrt(f(Phi))`. This is the standard trick for
removing a *purely kinetic-normalisation* nonlinearity: it makes `chi` exactly
canonical, and its equation of motion in the source-free region becomes
exactly `∇²chi = 0` — not just to leading order in `eps`, **to all orders**.

Solving explicitly (`sympy`, verified by round-trip substitution):

```
chi(Phi) = [(1 + 2*eps*Phi)^(3/2) - 1] / (3*eps)      chi(0) = 0 for all eps

Phi(chi) = [(1 + 3*eps*chi)^(2/3) - 1] / (2*eps)       exact inverse, checked
```

## 2. The covariant action

Because the field redefinition is purely a relabelling of the scalar — it
does not reference the metric — it holds in any spacetime, not just the flat
static case it was derived in. The genuinely covariant, exact action is
therefore simply that of a **canonical free scalar with a nonlinear coupling
to the source**:

```
S = INTEGRAL d^4x sqrt(-g) [ (1/2) g^{mu nu} d_mu(chi) d_nu(chi)  -  rho(x) * Phi(chi) ]

Phi(chi) = [(1 + 3*eps*chi)^(2/3) - 1] / (2*eps)
```

`chi` has an ordinary kinetic term — no ghost, no strong-coupling issue in
the kinetic sector at all. All of the original nonlinearity has been moved
into the **coupling to matter**, `Phi(chi)`. This is structurally the same
kind of object as a chameleon-type scalar-matter coupling (Khoury–Weltman
2004 use `A(chi) = e^{beta*chi/M_Pl}`; here the coupling function is the
different, specific form `Phi(chi) ~ chi^(2/3)` at large `chi`) — a named,
well-studied *class* of theory, with a specific, new coupling function.

**Scope of "covariant" claimed here, stated precisely:** minimally coupled
to a *fixed* background metric `g^{mu nu}` (matter and `chi` do not yet source
gravity in this calculation); Lorentz-covariant in flat spacetime by
construction, since the field redefinition step used no metric structure.
Full gravitational back-reaction (varying `g^{mu nu}` too) was not computed.

## 3. Exact solution, and what it resolves

For a static point source, `chi` is exactly harmonic: `chi(r) = 1/r` (the
same boundary condition that fixed the earlier perturbative `phi`). Feed this
into `Phi(chi)` and Taylor-expand — no further perturbation theory needed,
the exact answer is one substitution away:

```
Phi_exact(r) = [ (1 + 3*eps/r)^(2/3) - 1 ] / (2*eps)

Taylor series in eps:
  O(eps^0):   1/r                    matches R7's phi exactly
  O(eps^1):  -1/(2 r^2)              matches R7's sigma exactly (coefficient 1, not just power)
  O(eps^2):   2/(3 r^3)              SAME power as R7's xi (~1/r^3), coefficient differs
  O(eps^3):  -7/(6 r^4)              a genuinely NEW term, not in R7's original claim at all
```

**Cross-checked two fully independent ways** — solving the O(eps^2)
Euler–Lagrange equation directly with `sympy.dsolve`, and Taylor-expanding
the exact closed form — and they agree exactly (`2/(3 r^3)` both ways). The
earlier same-day version of this file called the `-4` factor between this
result and R7's own `xi` "unexplained." It is not an error or an artefact:
**it is the theory's genuine, unique prediction.** Once the action is fixed
to reproduce R7's `sigma` term exactly, its `xi` term is no longer free — it
is determined, and what it determines is `2/(3 r^3)`, not R7's own
`-1/(6 r^3)`. Same functional form (both `~1/r^3`), different coefficient,
and there is no remaining freedom in this action to fix that: matching order
1 exhausts the one available coupling constant.

**Honest reading:** this is evidence *for* the general mechanism (radial
powers from a single field via a nonlinear coupling) and evidence *against*
this particular coupling function being the exact, complete answer — a
correct covariant completion of MULTING's actual `A3, A4` structure would
need either a different `Phi(chi)`, or additional terms/fields beyond this
minimal one-parameter family.

## 4. A free, falsifiable extra prediction

The `O(eps^3)` term, `-7/(6r^4)`, is not something R7 asked for — it falls
out for free because the solution is exact rather than truncated. It
predicts a further potential term `~1/r^4`, corresponding to a force term
`~1/r^5`. **MULTING's own published force law,
`F = -A2/r^2 + A3/r^3 - A4/r^4`, has no such term** — it terminates at
`1/r^4`. So either this specific action needs to be truncated by hand (an
ad hoc extra assumption), or it is not the right completion, or MULTING's
own published law is itself understood as a truncation of something with
further terms nobody has written down. This is flagged as an open
discriminating question, not resolved here.

## 5. The ghost-condensate boundary, now exact and checked against the physical branch

`f(Phi) = 0` (NR-019's ghost-condensate point) sits at `Phi_ghost = -1/(2*eps)`,
equivalently `chi_ghost = -1/(3*eps)`.

For the physical static point-source solution, `chi(r) = 1/r` ranges over
`(0, +infinity)` as `r` ranges over `(0, +infinity)`. Since `chi_ghost` is
**negative** (for `eps > 0`), **this branch never reaches it** — the kinetic
term stays healthy (`f(Phi) > 0`) at every radius from the source outward.
This is a clean, positive, checked statement: NR-019's worry is real *as a
class of theory*, but for this specific solution and this specific sign of
`eps`, the pathology sits on a branch (negative `chi`, i.e. a different
source configuration) that the ordinary attractive point-source solution
does not visit.

## 6. Matched to MULTING's actual `ℓ_d`, `ℓ_q` — a sharp, falsifiable structural prediction

Section 4 flagged that this action's series has no natural place to stop.
Matching it to MULTING's *own* potential pins that down properly. From the
technical memorandum, `U(r,z) = -A2/r + A3/(2r²) - A4/(3r³) + C(z)`, and
Section 5's own definitions `ℓ_d = A3/A2`, `ℓ_q² = A4/A2`, so:

```
-U/A2  =  1/r  -  ell_d/(2 r^2)  +  ell_q^2/(3 r^3)
```

matched term by term against `Φ_exact`'s own series (§3):

```
O(eps^0):  1/r                                       <-> 1/r                    (identity, fixes normalisation)
O(eps^1): -eps/(2 r^2)                                <-> -ell_d/(2 r^2)         =>  eps = ell_d  (exact match)
O(eps^2):  2*eps^2/(3 r^3), eps=ell_d -> 2 ell_d^2/(3 r^3)  <-> ell_q^2/(3 r^3)  =>  ell_q^2 = 2 ell_d^2
```

**`ε = ℓ_d` is dimensionally sound** — `Φ ≡ -U/A2` carries dimensions of
inverse length (since `U/A2` has dimensions of `1/r`), so `ε ~ 1/Φ` has
dimensions of length, matching `ℓ_d` exactly. Not a coincidence of numbers;
the identification is unit-consistent.

**An error caught mid-derivation, left in the record on purpose.** A first
hand-tracked version of this match produced `ℓ_q² = -2ℓ_d²` — the wrong sign,
from a bookkeeping slip (dividing a series *coefficient* by `eps` when the
coefficient no longer contained one). Redone cleanly in `sympy`, working with
the literal `eps^1`/`eps^2` *terms* rather than manually-extracted
coefficients, the correct result is:

```
ell_q^2 = 2 * ell_d^2        (positive)
```

**Self-consistency check against this project's own earlier result.** Branch
C (`FINDING_cluster_pair_sign_constraint.md`, same day) established
`ℓ_q ≥ ℓ_d/2` as the exact condition for the force to stay attractive at
every separation. The predicted value, `ℓ_q = √2·ℓ_d ≈ 1.414·ℓ_d`,
comfortably satisfies it — this specific action, if correct, would put
MULTING's local force **safely inside the always-attractive regime**, with
real headroom (1.414 vs. the 0.5 threshold), not marginally.

**The `O(ε³)` term is now a concrete number, with nothing to compare it to.**
At `ε=ℓ_d`, it evaluates to `-7ℓ_d³/(6r⁴)` — a specific, falsifiable
prediction for a fifth force term MULTING's own published law does not
carry. Section 4's flag now has a number attached, still unresolved.

**What this does NOT do — stated to prevent a specific, tempting error.**
Table A1's fitted `β_d, β_q` enter a *different* force formula (per TJB's own
prompt to the AI services: `F_3_1 = β_d·G·mass_1·(ICM thermal energy)_1/c²·.../r³`
etc., built from cluster-specific mass/energy/radius variables) — not simply
`ℓ_d = A3/A2`, `ℓ_q² = A4/A2` from the letter's own `F(r)` parametrisation.
Converting between the two requires a derivation not attempted here.
Plugging `β_d=4.5, β_q=18.0` into `ℓ_q²=2ℓ_d²` without that derivation would
silently conflate two different parametrisations of the theory — exactly the
class of error this project's own Gate 1 exists to catch. Not done.

## Verdict against the frozen classification

```
MULTIPOLE RADIAL LADDER (R7):   [VERIFIED], STRENGTHENED to an exact, not
                                 perturbative, closed-form covariant action.
                                 First two orders checked two independent
                                 ways; matches R7 in FORM at every order
                                 checked, matches R7's own COEFFICIENT only
                                 at first order (exactly).
NR-019 (ghost tension):         sharpened to an exact boundary,
                                 chi_ghost = -1/(3 eps), and shown NOT to be
                                 reached by the physical static solution
                                 branch used here.
Covariant MULTING+ completion:  STILL OPEN. This is one witness action that
                                 reproduces the radial powers and locates
                                 its own ghost boundary cleanly -- it is not
                                 shown to be MULTING's actual completion,
                                 and section 4's extra term is a concrete,
                                 named reason to doubt it is the final one.
Matched to real ell_d, ell_q:   ell_q^2 = 2*ell_d^2 predicted -- self-
                                 consistent with the attractive-everywhere
                                 bound (comfortably, 1.414 vs required 0.5)
                                 -- but NOT checked against real fitted
                                 numbers (Table A1's beta_d/beta_q use a
                                 different parametrisation; converting was
                                 not attempted, deliberately).
```

## What remains exactly as open as before

- Full gravitational back-reaction (`g^{mu nu}` dynamical) — not computed.
- Two-body `A3, A4` coefficient dependence on both objects' `m, k, r` — not
  touched.
- Cosmological magnitude — separate question, addressed elsewhere (§6 of
  the technical memorandum for the pair-fluid route; untouched here).
- Uniqueness — only this one coupling family was tried.

## Reproduction

```python
import sympy as sp
r, eps, chi = sp.symbols('r epsilon chi', positive=True)
Phi_of_chi = ((1+3*eps*chi)**sp.Rational(2,3) - 1) / (2*eps)
Phi_exact  = Phi_of_chi.subs(chi, 1/r)
series     = sp.series(Phi_exact, eps, 0, 4).removeO()
# -> 1/r - eps/(2 r^2) + 2 eps^2/(3 r^3) - 7 eps^3/(6 r^4)
```
