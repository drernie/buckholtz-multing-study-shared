# FINDING P223 — v82's single-pair bridge and docs/127's population
# closure answer different questions about the same power-law shape;
# H1/H2 CONFIRMED, H3 NARROWED after skeptic review

**Continues:** `CLAIM_P223_finite_r_single_pair_closure.md` (committed
`064d0fd`, BEFORE `P223_finite_r_single_pair_closure.py` was run) →
`docs/153` §0/§3a, `FINDING_P156`, `FINDING_P157`, `FINDING_P189_finite_
r_preconditions.md` (a shortcut attempt this file's own approach was
designed to avoid repeating).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive/mathematical

---

## Result

**H1 CONFIRMED (strengthened after skeptic review — see below).**
Substituting v82's own `F_P = F^(0) - F^(1) + F^(2)` (Eqs. 1-4, read
directly from the primary source) into v82's own `mu_reduced*s_ddot =
F_P` (Eq. 7, accretion-correction bracket set to 0, the Eq. 5 special
case) and `a_ddot/a = s_ddot(z)/s(z)` (Eq. 8) gives:

```
a_ddot/a = G*[beta_1*c^2*s*(k_A*m_P*r_A + k_P*m_A*r_P)
              - beta_2*k_A*k_P*r_A*r_P - c^4*m_A*m_P*s^2]
           / (c^4 * mu_reduced * s^5)
```

Four additive terms of distinct `s`-powers: `s^-3` (monopole-only,
`k`-independent), two `s^-4` terms (dipole cross-terms, one `~k_A`, one
`~k_P`), one `s^-5` term (quadrupole, `~k_A*k_P`). The `k`-dependent
piece does not vanish for generic parameters.

**H2 CONFIRMED, exact match.** Re-deriving `docs/127`'s own `G_alpha_
beta = G*lim_{r->inf}[f(r) - r*f'(r)]` for `f(r)=1, 1/r, 1/r^2` (the
monopole/dipole/quadrupole mapping of v82's own `1/s^2, 1/s^3, 1/s^4`
power laws) gives `G, 0, 0` — bit-for-bit the same table `docs/127`
already published.

**H3 (synthesis, NARROWED after skeptic review):** conditional on v82's
own Eq. 8 being taken literally as written — confirmed by direct reading
that no averaging, integration, or population sum appears anywhere in
Eqs. 5-9's primary text; `s(z)` is stated plainly as "the characteristic
distance between adjacent cosmic-web nodes," a single scalar trajectory
— `docs/127`'s `r->infinity` population-closure result and v82's own
single-pair bridge are computing two structurally different quantities
that happen to share the same `1/s^2, 1/s^3, 1/s^4` shape: (a) one
specific pair's own finite, never-taken-to-infinity separation `s(z)`
(H1), vs. (b) the tail contribution, as a DIFFERENT variable (a
background-source-to-test-point distance internal to the Shtanov-Sahni
convolution) grows without bound, to the MEAN field felt from an
isotropic population (H2). Under this literal reading,
`docs/127`'s result does not bear on v82's bridge one way or the other.

## Independent skeptic review (Step 8a, context-blind)

Given only the claim's own H1/H2/H3 statements and the actual script
output — no session reasoning chain. **Verdict: WEAKENED**, two
objections, both independently re-checked before accepting or
correcting (`audit-verification-gate.md`).

**Objection 1 — H1's non-cancellation test is "near-trivial by
construction"; specifically, does not rule out the two `s^-4` dipole
cross-terms canceling AGAINST EACH OTHER.** Checked directly, not taken
on the skeptic's word: the two `s^-4` terms combine into one additive
group, `k_A*m_P*r_A + k_P*m_A*r_P` — a SUM, not a difference. Every
factor (`k_A, m_P, r_A, k_P, m_A, r_P`) is declared `positive=True` in
the symbolic derivation, matching v82's own text verbatim ("Masses are
nonnegative... k_A is nonnegative..."). Independently re-verified with
sympy's own logic engine (`sp.ask(Q.positive(...))`, run separately from
the main script): **provably positive, hence provably nonzero** — not
merely "not shown to cancel." Separately, the `s^-5` quadrupole term
cannot cancel identically-in-`s` against the `s^-4` group regardless of
sign, since they are different powers of a free variable (a Laurent-
polynomial identity, not a coincidence at one value of `s`). **Response:
Accepted, with correction** — the original test (subtract `k_A=k_P=0`
case, observe nonzero remainder) was real but weaker than the write-up
implied; the stronger, now independently-verified claim (positivity
rules out ANY internal cancellation, at any `s`, for any physically
admissible parameter values) is substituted above and is a strictly
stronger, fully rigorous result.

**Objection 2 — H3's "docs/127 places no constraint on v82" overreaches;
it silently assumes v82's own `s_ddot/s -> a_ddot/a` identification
(Eq. 8) carries no hidden population content, which this project's own
scope does not audit.** **Response: Accepted, with correction.** The
skeptic is right that an unconditional "no constraint at all" claim
smuggles in an assumption about how v82's own equation should be read.
Fixed above: H3 is now stated explicitly conditional on the literal
reading of Eq. 8 (verified by direct primary-source check, not assumed)
— whether v82's own physical INTENT for `s(z)` secretly encodes some
population-level meaning beyond what Eqs. 5-9 literally say is outside
what this project's reconstruction can establish from the text alone,
and the conclusion is narrowed accordingly: "these two specific
calculations, as literally written, answer structurally different
questions" rather than a categorical claim about all possible readings
of v82's construction.

## What this DOES support

- v82's own published bridge (Eqs. 1-9), read and computed directly
  from the primary source, manifestly and provably keeps
  `k_A(z)`-dependent (dipole/quadrupole) contributions in `H(z)`, with
  no internal algebraic cancellation mechanism — consistent with, and
  now symbolically grounding, `FINDING_P156`'s empirical reading of
  v82's own Table IIIa (`k`-tiers dominate 96-99.65% of the force
  budget).
- `docs/127`'s own `G_alpha_beta=0` result is independently reproduced
  exactly by a separate re-implementation, for the same `1/s^2, 1/s^3,
  1/s^4` power-law shapes v82 uses.
- Taken together, and reading v82's Eq. 8 literally, `docs/153` §0's
  causal-compatibility question resolves to: `docs/127`'s S-S closure
  and v82's single-pair bridge are **structurally answering different
  questions** about the shared force-law shape — not compatible, not
  incompatible in the contradicting sense. This directly answers `docs/
  153` §3a precondition 1 (does a finite-r closed form exist, or is new
  derivation needed?): **the comparison IS tractable and IS now done**,
  using v82's own equations directly, without needing a new derivation
  of a "finite-r analog" of `docs/127`'s own formula (the route
  `FINDING_P189` correctly killed as a category error).

## What this does NOT establish

1. Not a claim about whether v82's own physical theory is correct
   (`NO_AUTHOR_ERROR`) — entirely about whether two of THIS project's
   own reconstruction routes contradict each other (they do not, under
   the literal reading established here).
2. **Not an unconditional claim that no reading of v82's bridge could
   ever be constrained by a population-averaging argument** — narrowed
   per skeptic Objection 2; this file establishes the literal-text
   reading only.
3. Not a resolution of `docs/153` §3a preconditions 2-3 beyond what this
   specific calculation itself demonstrates: precondition 2 (tractable
   with existing machinery) — YES, using v82's own equations directly,
   no new machinery needed; precondition 3 (cost vs. consequence) — this
   calculation's own cost was low (a single sympy script, no new
   physics framework), and its consequence is the resolution above, so
   the proportionality question for THIS specific route is favorable.
4. Not a claim that `two_charge_completion.py`/`two_field_action_
   closure.py`'s own single-pair force-law machinery was needed here —
   it was not; v82's own Eqs. 1-4 already supply everything required,
   and using them directly (rather than this project's own re-derived
   analog) is the more faithful comparison to "v82's own bridge."

## Status

**P223 complete: H1/H2 CONFIRMED (H1 strengthened via an independently
sympy-verified positivity argument), H3 NARROWED to the literal-text
reading of v82's Eq. 8, per Skeptic Response Matrix.** `docs/153`
should be annotated (not rewritten) to record this as the answer to the
restated bottleneck-1 causal-compatibility question and to §3a
precondition 1. A portable methodological lesson (two calculations
sharing a power-law SHAPE need not be comparable at all if the variable
in that shape means something structurally different in each — a
population/environment coordinate vs. a specific instance's own state
variable) is recorded as a pearl_registry entry.
