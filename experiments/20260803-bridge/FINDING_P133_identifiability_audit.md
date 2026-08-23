# FINDING P133 — Formal Identifiability Audit: theta=(A,g,kappa)

**Date:** 2026-08-24
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Verdict:** `H3-NOT-IDENTIFIABLE-AS-CURRENTLY-POSED` (BLOCKED BY STRUCTURAL
UNDERDETERMINATION, not REFUTED)
**Script:** `P133_identifiability_audit.py` (sympy, exact symbolic algebra,
positive-control-tested, cross-checked by two independent methods)

---

## 1. Why this file

After `/hypothesis-arbiter`'s own H4 (P132) closed cleanly, informal review of
H3 (absolute-scale/observable mapping) found the candidate normalization
(`FINDING_P42`'s shared `A/c²`) sits on two unresolved prior questions
(`FINDING_P39`'s Reading 1/2 ambiguity; `FINDING_P14` §1's channel-existence
tension) and, even setting both aside, combining the one existing observable
(`O1=A·g²`, growth-rate data) with a hypothetical second (`O2=A·f(κ)`, an
external `Ω_φ` bound) gives 2 equations for 3 unknowns — underdetermined by
simple counting. The user asked for something stronger than that prose: a
**formal audit** that (1) explicitly searches the project's own registered
findings for a hidden third relation before concluding degeneracy, and (2)
computes the actual Jacobian rank.

## 2. The hidden-relation search

Grepped every `FINDING_P*.md` for a κ↔g relation. Found one:
`FINDING_P24_gk_matching_eta_invariant.md` already establishes `η:=κ/g` as
the sole parameter controlling every cross-sector force ratio (`χ_d`, `χ_q`),
with `A` cancelling identically — confirmed symbolically there, skeptic-
reviewed (Step 8a, 2026-08-13), no sub-verdict falsified. This is a genuine
candidate third observable, `O3=κ/g`, independent of `A` by construction —
exactly the user's own named "Вариант 1" (κ=F(g)) / "Вариант 2" (an
A-independent observable) territory. **P24 itself does not give η a numeric
value** — only the functional form (its own §4, "What this does NOT
establish," point 1).

## 3. The audit

θ=(A,g,κ). Observable map:
- `O1 = A·g²` (existing external channel: growth-rate/modified-gravity data,
  `FINDING_P22`/`FINDING_P31`/`FINDING_P132`)
- `O2 = A·κ²` (hypothetical: `FINDING_P14`'s own κ² scaling for `Ω_φ`, IF that
  channel exists and IF Reading 1 of `FINDING_P39` holds)
- `O3 = κ/g` (`FINDING_P24`'s η, real, A-independent, numerically unmeasured)

Jacobian `J = ∂(O1,O2,O3)/∂(A,g,κ)`, computed symbolically (sympy, exact):

```
J = [ g²    2Ag    0   ]
    [ κ²    0      2Aκ ]
    [ 0    -κ/g²   1/g ]

det(J) = 0        rank(J) = 2
```

**Positive control** (run first, before trusting the method on the real
case): a synthetic observable set `(A, g, κ)` itself — trivially
identifiable — gives `det=1≠0`, correctly classified as rank 3. The
rank-check machinery is not broken.

**Cross-check 1 — exact identity.** `O2 − O1·O3² = 0` for ALL `(A,g,κ)`,
verified symbolically (not at a point). I.e. `O2 ≡ O1·O3²` — `O2` carries
**zero information** beyond `O1` and `O3` combined.

**Cross-check 2 — exponent-matrix method.** `O1,O2,O3` are monomials in
`(A,g,κ)`; for power-law observables, log-linearization means the Jacobian's
rank equals the rank of the matrix of exponent vectors:

```
        A   g   κ
O1  [   1   2   0  ]
O2  [   1   0   2  ]
O3  [   0  -1   1  ]

det = 0, rank = 2.   Explicit dependency: row(O1) − row(O2) + 2·row(O3) = 0
```

i.e. `log(O1) − log(O2) + 2·log(O3) = const` — algebraically the same
statement as the exact identity above, reached by an independent route. Both
methods agree.

## 4. Verdict

`H3-NOT-IDENTIFIABLE-AS-CURRENTLY-POSED` — **not** REFUTED, **BLOCKED BY
STRUCTURAL UNDERDETERMINATION**. `rank(J)=2<3`, proven symbolically (exact,
not floating-point), by two independent methods that agree. The third
candidate relation this file went looking for (`FINDING_P24`'s η) is real
but does **not** rescue identifiability — it is degenerate with `O1` and the
hypothetical `O2` by an exact algebraic identity, not by coincidence at some
parameter point. Even `O1+O3` alone (no `O2` at all) leave a 1-parameter
family of `(A,g,κ)` solutions: a genuine, provable, 1-dimensional continuous
degeneracy that no amount of precision on *these three specific observable
types* can close.

**Reusable criterion, going forward:** any future candidate observable `O4`
that is a monomial `A^a·g^b·κ^c` breaks the degeneracy **only if** its
exponent vector `(a,b,c)` is linearly independent of the current
two-dimensional row space (spanned by, e.g., `O1`'s and `O3`'s own exponent
vectors — concretely, `(1,2,0)` and `(0,-1,1)`) — checkable by one 3×3
determinant BEFORE spending any effort chasing external data for it. This
converts the user's own three reopen-classes into a sharper filter for class
2 specifically: a "genuinely new observable" only helps if it is either
non-monomial in `(A,g,κ)`, or a monomial whose exponent vector clears this
determinant test.

## 5. What this does NOT establish

1. Whether `FINDING_P14`'s own `Ω_φ` self-energy channel physically exists
   at all (§1's cancellation tension, unresolved) — per the user's own
   prioritization, this is logically **prior** to this file's own question:
   if the channel doesn't exist, `O2` is moot regardless of this file's
   algebra.
2. `FINDING_P39`'s own Reading 1 vs Reading 2 ambiguity for `[g]` — this
   file's `O2` (and `FINDING_P42`'s `A/c²` normalization behind it) is
   Reading-1-specific.
3. A resolution via any of the user's own three reopen-classes: a
   theoretical `κ=F(g)` relation (P24 gives the *form*, not a value — this
   would need an independent derivation of η's numeric value, or a genuinely
   different relation entirely); a new non-monomial observable; or a
   theory-fixed value of `A`. None searched for here.
4. Anything about MULTING itself (Gate 1, artifact-provenance-gates.md). No
   `k[h/Mpc]` quoted.

## 6. Controls

- **Positive control**: synthetic `(A,g,κ)` observable set, known rank 3,
  correctly classified — PASSES (§3 above).
- **Cross-check**: direct Jacobian determinant vs. exponent-matrix
  determinant — two independent derivations of the same rank, AGREE.
- **Regression**: `ruff check` clean; script is read-only (no state
  mutation, no dependence on prior scripts' output files).

## 7. Next allowed action (per `docs/147`)

Per the user's own proposed sequence: **STOP H3** (this audit closes it,
not with a numeric answer but with a proven structural verdict — a
legitimate, informative closure per `falsification-ladder.md`'s own
Kill Analysis discipline: what was killed — identifiability via *these
three* specific observables; what was NOT killed — the possibility of
identifiability via a future non-monomial or exponent-independent
observable, or a theory-fixed `A`). Then re-run a short strategic arbiter
with updated statuses (H1 blocked, H2 blocked, H3 structurally
underidentified — now with a precise, reusable test for what would change
that) and ask directly whether any internal GO remains, per the user's own
final framing.
