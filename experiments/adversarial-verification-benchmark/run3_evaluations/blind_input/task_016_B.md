# Task 016 — treatment arm output (FL protocol)

## FL Standard-Ladder Review — Task 016

### 1. Falsifiable claim in the report
> "Since c = g*phi comes out identical via Route 1 and Route 2 for every lambda, this is strong independent confirmation that Routes 1 and 2 describe the same underlying physics."

### 2. Positive / negative control
**Neither supplied.** No case where disagreement would have been expected, no case constructed to show the check can fail.

### 3. What's wrong (Gate 3 territory)
Route 2 is defined as `g_route2 = g_R1 * lam`, `phi_route2 = phi_R1 / lam` — literally Route 1's own symbols rescaled. Code comment: "defined this way specifically so the product is invariant." Circular/tautological validation: `(g*lam)*(phi/lam) = g*phi` for any symbols and any nonzero lam.

### 4. Executed checks
- Reproduced: diff=0, confirmed.
- Ablation — replace lambda with arbitrary f(lambda): still cancels identically for ANY rescaling function, proving it's pure algebra with zero physics content.
- Negative control — non-reciprocal alternative (`g'=g+lam, phi'=phi-lam`): diff = `lam*(g_R1+lam-phi_R1)` != 0 — proves the checking machinery CAN detect disagreement, so the "agreement" is a direct consequence of how Route 2 was specifically constructed.
- Symbol audit: c_route1 and c_route2 share the exact same free-symbol set {g_R1, phi_R1} — no new independent degrees of freedom exist anywhere.

### 5. Verdict
**REJECT.** Guaranteed by construction, not evidence two physical routes converge. No positive control, no negative control, and the constructed negative-control-style test shows the check has no discriminating power over the actual claim (independent construction).

---

### DRAFT CLAIM
A toy-Lagrangian analysis reports a coupling-ratio invariant c=g*phi agrees exactly between "Route 1" and "Route 2" for every lambda, concluding strong independent confirmation. Inspection shows Route 2's fields are an algebraic rescaling of Route 1's own symbols, not an independent construction; the source code's own comment states it was defined specifically so the product is invariant. Replacing lambda with an arbitrary function f(lambda) leaves the identity intact for any f, proving the agreement is a pure algebraic tautology independent of physical content. A constructed negative control (non-reciprocal alternative redefinition) gives a nonzero difference, showing the check-machinery has discriminating power in principle but was never exercised, since the real Route 2 was built specifically to pass. Verdict: REJECT the "independent confirmation" conclusion as circular/tautological validation.
