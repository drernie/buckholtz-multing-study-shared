# Skeptic review — P129's amplitude-prediction claim

**Context Asymmetry Rule applied:** the skeptic agent was given only the
claim (as printed by P129's own VERDICT section) and the full script code
— no reasoning chain, no session history, no framing of *why* the claim
might be wrong.

**Verdict: OVERCLAIM, HIGH confidence.**

---

## The mathematical core

Given the two pointwise equivalences the script itself relies on (k=0.3
established in `FINDING_P128`; k=0.5 measured in-flight by `P129` to
0.0000% up to N=3e5):

```
c_reduced_k03(N)  ≡  c_full_k03(N)     for all tested N
c_reduced_k05(N)  ≡  c_full_k05(N)     for all tested N
```

then for any pointwise functional `F` (including deviation ratios and
their means):

```
F[c_red_k03, c_red_k05]  ≡  F[c_full_k03, c_full_k05]     to the same precision
```

**A_pred ≡ A_hat is a corollary of the pre-established pointwise
equivalence, not an independent measurement.**

## What is and isn't new information

**Genuinely new in this script:** pointwise equivalence between
reduced-forward-from-hand-off and full-actual, extended to k=0.5 (the
prior file established it only for k=0.3). This is a real, non-trivial
result — the reduced system's applicability to a second k value was not
guaranteed a priori.

**Corollary — NOT new evidence:** A_pred matching A_hat to 0.01%. Once
the pointwise equivalence holds at both k values, any downstream
statistic (ratios, means over N_ANCHORS) on the reduced trajectory
equals the same statistic on the full trajectory by arithmetic. The
"entirely different method" framing conflates "different code path" with
"different information content."

## Where the original verdict text overreached

| Verdict phrase | Problem |
|---|---|
| "entirely different method" | Not different once k=0.5 pointwise equivalence is granted — it is the same trajectory reached by a different route |
| "non-tautological cross-check" | One step milder than tautology (ratio of two pointwise-equal functions equals ratio of those functions) — arithmetic, not physics |
| "closes the low-k mechanism line" | Overreach on the strength of the ratio-match; closure would need to rest on the pointwise-equivalence extension, not its arithmetic corollary |
| "SAME k-independent reduced system with zero fitting to 6679" | True but misleading — the hand-off states ic03/ic05 were extracted FROM the full system, so the "prediction" inherits the full system's information content |

## Two subordinate caveats

1. Pointwise equivalence at k=0.5 was measured up to N≈3e5. `N_ANCHORS`
   includes 541049 and 920067. Equivalence at those larger N is
   extrapolated, not measured. Unlikely to move 6679 by more than the
   observed 0.01%, but worth stating.
2. `c_inf03` is hard-set from `FINDING_P128`'s own constant; `c_inf05` is
   re-derived by `self_consistent_plateau` on this script's own
   trajectory. The METHOD matches `FINDING_P126`'s own construction
   (same bounds, same optimizer), which reduces but does not eliminate
   this as a residual concern.

## What WOULD be a genuinely independent cross-check

Use an input to the reduced system that does NOT come from the full
system's own trajectory — e.g. an analytic low-k asymptotic hand-off
state, a perturbative expansion, or a held-out k value where the full
system's trajectory was never used to seed anything. If THAT reproduces
6679, the reduced system's low-k asymptotics would carry independent
predictive content. Not attempted in `P129`.

## Resolution

`P129`'s own VERDICT section and docstring were corrected to report two
separate claims — `[NEW]` (pointwise fidelity extends to k=0.5) and
`[COROLLARY]` (amplitude match follows arithmetically, not independent
evidence) — instead of the original single, overclaimed statement.
