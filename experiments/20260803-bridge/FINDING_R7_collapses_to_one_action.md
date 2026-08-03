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
