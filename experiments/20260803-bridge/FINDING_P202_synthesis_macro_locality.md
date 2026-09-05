# FINDING P202 — Synthesis: is the `P196`-`P201` residual a local
# artifact of this one comparison, or a manifestation of a known,
# field-wide macro pattern? (claim-decomposer + macro-locality, applied
# to the accumulated evidence rather than run as separate fresh passes)

**Date:** 2026-09-06
**Continues:** `FINDING_P199`, `FINDING_P200`, `FINDING_P201`. Closes
the 5-step autonomous follow-up the user authorized after reviewing
`P198`'s close-out ("возможно доктор ошибается и есть другой
механизм"). Steps 4 (claim-decomposer) and 5 (macro-locality) are run
here together, against the accumulated evidence from steps 1-3, rather
than as fresh, from-scratch passes — the concrete results already in
hand directly answer both questions.

## Step 4 — Claim decomposition: is `ratio_2b` even testing what it
## appears to test?

The `P196`-`P201` line implicitly rests on one load-bearing assumption
never previously stated explicitly:

> **A5 (implicit):** Girardi's `σ`-based virial-radius estimator and a
> caustic/SZ-mass-plus-NFW-based radius estimator, applied to the same
> real cluster, should agree closely — disagreement signals something
> wrong (in this project's reconstruction, in Girardi's formula, in the
> mass measurement, or, the user's own question, possibly in TJB's own
> construction).

**This assumption is contradicted by every real-data result this
project has produced in this exact investigation:**

| Comparison | Real, independent, published proxies compared | Disagreement found |
|---|---|---|
| `P197` | Caustic mass vs Planck SZ mass, same 123 clusters | `2.5×` (mean), `74.5%` scatter |
| `P200` (literature) | Caustic vs X-ray hydrostatic mass, same survey family, 44 clusters (Logan et al. 2022) | `1.12×` best case, worse when undersampled |
| `P201` | Simulated (Duffy+08) vs real X-ray (Buote+07/Schmidt&Allen+07) concentration, feeding the same mass conversion | `15-32%` shift in the derived mass, by concentration-source choice alone |
| `P196`-`P198` (this project's own headline) | Girardi's `σ`-virial radius vs NFW `R500`/`R_vir` from caustic mass | `1.47×`, robust to 4 tested candidates |

**None of these four comparisons involve MULTING, v82, or any TJB
construction at all** — they are pairwise comparisons between
*standard, independent, real, published, non-MULTING* cluster mass or
concentration estimators, and every single one disagrees by a real,
substantial, non-trivial amount. `A5` is false as a general premise in
cluster astrophysics: independent mass/radius proxies for real clusters
routinely disagree at the `10-150%+` level, for well-understood
astrophysical reasons (non-equilibrium dynamics, projection effects,
hydrostatic bias, sparse sampling, concentration-relation choice) that
have nothing to do with any specific theory being tested against them.

**Recomposition Gate verdict:** the individually-real, individually-
verified sub-findings (`P196`-`P201`, each independently correct) do
**not** license the stronger, unstated claim the investigation was
implicitly organized around — that a `~1.47×` disagreement between
Girardi's estimator and an NFW/catalog-mass-based one is a special,
in-need-of-explanation anomaly. Stating the full chain honestly: these
sub-claims combine to show the *opposite* — that a disagreement of this
size is unsurprising given how much independent, non-MULTING proxies
already disagree with each other in this exact literature.

## Step 5 — Macro-locality verdict

**OBJECT:** the `~1.47×`-`2.5×` residual between Girardi's virial-radius
estimator and NFW/catalog-mass-based radius estimators for the same
real HeCS-SZ clusters.
**LOCAL_EXPLANATION tried first (per this protocol's own falsification-
first discipline):** something specific to *this* comparison — a bug,
a wrong formula, a misapplied definition — is responsible. `P196`-`P201`
tested exactly this, exhaustively, across 4 named candidates plus 2
newly-discovered ones (6 total): concentration scatter, concentration
source (twice, in two different roles), mass-measurement method,
Girardi's own internal inconsistency, and caustic sparse-sampling bias.
**None closes the gap alone**, and no code bug was found in any of
them (`P196`'s and `P197`'s own corrections were real, but each made
the reconstruction *more* correct, not the residual smaller).

**Boundary audit:** the investigation's original framing implicitly
drew its boundary around "this one Girardi-vs-NFW comparison, for these
123 clusters, in this project's reconstruction." Sliding that boundary
outward — to "how do independent cluster mass/radius proxies compare to
each other, in general, in the published literature" — the same-sized
anomaly (large, real, well-documented disagreement) turns out to be the
*normal* state of that broader system, not a local exception.

**Competing hypotheses (M0-M3):**
- `M0` (noise): rejected — the disagreements are large, consistent in
  direction across multiple independent tests, and match published
  literature values.
- `M1` (local error, in this project's reconstruction): tested directly
  and exhaustively across 6 candidates; each is real where checked, but
  none is a *bug* — `P196`/`P197` found and fixed real bugs early on,
  and the residual persisted after those fixes, at a stable, real
  magnitude.
- `M2` (artifact of measurement method): partially true and already
  captured inside `M1`'s candidate list (mass-measurement method,
  concentration source) — these ARE real contributors, just each
  individually insufficient.
- `M3` (macro structure — this disagreement is a manifestation of a
  field-wide pattern, not specific to this comparison): **directly
  supported** by `P200` and `P201`'s literature grounding — the same
  order-of-magnitude disagreement recurs across multiple, mutually
  independent pairs of standard (non-MULTING) cluster proxies.

**Differentiating prediction, stated before concluding:** if `M3` is
correct, a *different* pair of independent, real, standard cluster mass
proxies — unrelated to Girardi or NFW specifically — applied to *any*
real cluster sample should show comparable-order disagreement. This
project already has that test, run incidentally rather than for this
purpose: `P197`'s caustic-vs-SZ comparison (`2.5×`) and the literature's
own hydrostatic-vs-caustic comparison (`1.12×`, worse when undersampled)
are exactly such independent pairs, and both show real, substantial
disagreement, in the same qualitative range as the Girardi-vs-NFW
result this project set out to explain.

**Stop condition check:** does treating this as `M3` (macro) yield a
new prediction `M1` alone would not? Yes — it predicts that *no* single
additional mechanism-hunt inside this specific comparison will ever
fully close the residual, because the residual's true scale reflects
the field's *general* proxy-disagreement floor, not a fixable local
error. This is a falsifiable, differentiating claim, not an
unfalsifiable retreat.

**VERDICT: `PART-OF-MACROSYSTEM`.**
```
BOUNDARY: this-one-comparison -> field-wide cluster mass/radius proxy agreement
SURVIVING_HYPOTHESIS: M3 (macro structure), moderate-high confidence
DIFFERENTIATING_PREDICTION: independent, non-MULTING proxy pairs (already
  observed: caustic-vs-SZ 2.5x, hydrostatic-vs-caustic 1.12x) show
  comparable-order disagreement, confirming this is not special to Girardi/NFW
NEXT: stop mechanism-hunting inside this one comparison; if this line is
  revisited, the informative next step is characterizing the FULL
  distribution of proxy disagreement across many published pairs (a
  meta-analysis), not another single-mechanism test
```

## Answer to the user's original question — "может доктор ошибается и
## есть другой механизм?"

**No evidence Dr. Buckholtz's own construction is wrong.** `FINDING_P199`
independently re-verified, against v82's own text (not a paraphrase),
that this project's `Δ=500` target selection is exactly what v82 itself
specifies — and found, as a bonus, that TJB's own paper *already*
explicitly flags this exact radius construction as "Class III, circular
... the most serious residual dependence in the present computations"
(his own words, `NO_AUTHOR_ERROR` — a quote, not this project's
assessment).

**"Is there a different mechanism?" — yes, but not a single exotic one.**
The mechanism is: comparing any two independent, real cluster mass or
radius proxies routinely produces disagreements of this general size,
for reasons well documented in the cluster-astrophysics literature and
unrelated to MULTING specifically. Six candidates were tested this
session and last (`P196`-`P201`); several are real, partial
contributors (mass-measurement choice, concentration-source choice,
Girardi's own internal `R_c` inconsistency); none closes the gap alone,
and — a new, general finding from `P201` — none of the concentration-
based corrections *could ever* close the residual's dominant scatter
component even in principle, since they only ever shift a population
mean. Taken together, this session's own evidence points toward
`PART-OF-MACROSYSTEM`: the residual is largely an instance of a known,
field-wide phenomenon, not a local bug or a special anomaly requiring
one more targeted fix.

## What this does NOT establish

1. Does not prove `M3` with certainty — a genuinely new, MULTING-
   specific mechanism cannot be ruled out by this synthesis alone;
   `PART-OF-MACROSYSTEM` is the best-supported reading of the evidence
   gathered, not a closed question.
2. Does not draft or send anything to TJB.
3. `NO_AUTHOR_ERROR` — entirely about this project's own reconstruction
   and its comparison to standard, published, non-MULTING cluster
   astrophysics literature.
