# Round 3 — consolidated static review of DRAFT_SPEC_v4

**Verdict: FAIL.** Not frozen. Blind C not launched.

Two isolated readers, specification only — no code, no data, no earlier
versions, no prior review reports. Pseudocode and prose only; arithmetic
permitted solely to check the document's internal consistency.

---

## 1. Acceptance stage — PASS

All twelve questions answered identically in content by both readers: kernels
and their model assignment, placement and epistemic status of `1/(1+ξ)`, which
`h` and what is never converted, pole-vs-logarithm treatment, pseudo-data
generation, weight matrix and what `α` affects, `μ̂` and its algorithm, `q̃_μ`
and edge datasets, limit selection and the non-standard outcomes, `r_lo` and
why the scan is not data-supported, unused files and the eight controls, the
exact claim and its exclusions.

Both readers volunteered the same caveats *inside* their answers — that the
α-accounting is incomplete (Q6), that "edge dataset" is never defined (Q8), and
that the outcome triggers overlap (Q9). Agreement extends to the objections.

## 2. Defect stage — FAIL

### Both readers' top three findings are the same three, in the same order

| Rank | Finding | Reader 5 | Reader 6 |
|---|---|---|---|
| 1 | The saturation argument is mathematically wrong where it gates a terminal verdict | C-2 · SEVERE | M1 · MAJOR |
| 2 | `σ_MC` propagation uses unit weights instead of the crossing fraction | C-12 · MODERATE | M2 · MAJOR |
| 3 | Coverage pass criterion treats `q₉₅` as exact → ≈50% spurious FAIL across eight nodes | C-6 · SEVERE | M3 · MAJOR |

**Severity calibration diverged even where content did not.** Reader 5 issued
three SEVERE; reader 6 issued none, topping out at MAJOR. Since the freeze gate
reads "zero SEVERE **and** zero MAJOR", the verdict is unaffected — but a gate
phrased in labels that two honest readers assign differently is a weakness of
the gate, not of the readers. Noted for the v5 gate wording.

### Convergent findings — both readers, independently

| Finding | R5 | R6 |
|---|---|---|
| α-accounting incomplete: `σ_A ∝ α^(−1/2)`, so α enters branches 3/4 and the zero-amplitude flag | C-10 | D1 |
| Control 2 is tautological — compares a quantity with the expression §2 mandates for it | C-13 | D3 |
| §0's justification for the coverage study is a non-sequitur | C-18 | D2 |
| Symbol registry declares itself complete and is not; `a`, `f`, `p` each carry two meanings | C-15 | D4 |
| RNG: §10 requires shared streams, §11's key includes `branch_id`, which guarantees different ones | C-4, C-5 | M4, D6 |
| Refinement pass undefined when there are several crossings, or none, or the window clips | C-9 | M5, M6 |
| Control 8 demands 9-significant-figure agreement on a 5-figure constant → near-certain STOP | C-8 | D8 |
| "Edge dataset" is a required output and is never defined | C-16 | D10 |

### Unique to reader 5

- **C-1 · SEVERE** — the "exact constrained minimiser" recipe is not one. §8
  says to evaluate `χ²` at both roots and both endpoints and take the smallest;
  when the minimising root lies outside `[0, μ_max]` the recipe returns it as
  `μ̂`. No clip was written. The following sentence ("without the endpoint
  clamp") implies a clamp exists in the constrained case, so a careful reader
  clips and a literal reader does not.
- **C-3 · SEVERE** — the three-outcome table is not a partition, and the v4 fix
  of v3's μ=0 degeneracy created an inversion. If every node above 0 is
  accepted, both `NO_UPPER_ENDPOINT` and `NO_CROSSING` apply with no precedence.
  Worse: if the *first* node above 0 is already rejected, no accepted→rejected
  pair exists inside the search, so the run reports "statistic saturates *below*
  threshold" when it is *above* threshold everywhere above zero — the genuine
  result `L₉₅ ∈ (0, first node]` is discarded and has no label.
- **C-11** — `σ_A = (tᵀWt)^(−1/2)` is a Δχ²=1 width; the sampling sd of `Â` is
  `√α·(tᵀWt)^(−1/2)`. The registry calls it "its error".
- **C-19** — the identifiability flag is evaluated at `μ̂`, the point where it is
  least informative; `Â` vanishes at `μ₀ = (K₂ᵀWd)/(K₃ᵀWd)`, which is where the
  acceptance boundary is most likely to fall.
- **C-21** — the overshoot guard covers `1+ξ(R)` at 15 fitted `R` but leaves the
  spline unguarded across `[r_lo, r_hi]`, including the very gap §6 identifies
  as the object under test, where a not-a-knot cubic can overshoot negative.
- **C-17** — control 1 verifies two shipped arrays differ by a factor `h`;
  nothing anchors the *absolute* unit of `r_mp`. A global 1.486× error passes
  all eight controls.
- **C-24** — §5's template-uncertainty numbers come from a file declared unused
  and cannot be reproduced by the specified pipeline.

### Unique to reader 6

- **D5** — the identifiability paragraph mis-describes the document's own
  parameterisation. `A₂ ≡ A` and `A₃ ≡ A·μ` are *definitions* over one amplitude
  and one shape parameter, so `A₃/A₂ ≡ μ` identically and is never estimated as
  a ratio of two independently fitted quantities. The real failure is that the
  profile *flattens* in μ as `A → 0`.
- **D16** — the freeze criterion is satisfied by relabelling rather than
  resolution. The header sets "zero SEVERE", then declares one of the two prior
  SEVERE findings "not a defect of the specification at all". A reader who
  honestly rates it SEVERE can never let the document freeze, and the document
  forecloses that by reclassification rather than by arguing the impact is
  bounded.
- **D11** — §5's "the 1/r³ constraint is driven by the large-R bins" is asserted
  without derivation and sits in tension with the kernels' own scaling
  (`μK₃/K₂ ∝ 1/R`, so the μ-sensitivity weakens with separation).
- **C-20 (R5's numbering)** — the header claims two prior SEVERE, names one, and
  never states the second, so a reader cannot check whether that fix landed.

---

## 3. Six errors in the author's own derivations — all verified

Every one of these is a claim v4 *added* in order to be more rigorous.

| # | v4 asserted | Check | Result |
|---|---|---|---|
| 1 | "α survives only in the p-value and branch 1" | `σ_A(α)/σ_A(1) = 1.008106`, exactly `α^(−1/2)`; branches 3/4 generate at `Â ± σ_A` | **wrong** |
| 2 | `σ_A = (tᵀWt)^(−1/2)` is "its error" | empirical sd of `Â` over 4×10⁵ draws = 1.1363; `√α·(tᵀWt)^(−1/2)` = 1.1378; v4's value = 1.1470 | **wrong — Δχ²=1 width, not sampling sd** |
| 3 | `σ_MC = √(σ_a²+σ_b²)/\|slope\|` | direct MC sd of the crossing = 0.002338; weighted `√((1−w)²σ_a²+w²σ_b²)/\|slope\|` = 0.002306; v4's = 0.004125 | **overstates ×1.76** |
| 4 | "plateau below `q₉₅` ⇒ no crossing at any μ" | see numerical demonstration below | **wrong** |
| 5 | "take the smallest of both roots and both endpoints = the exact constrained minimiser" | no clip to `[0, μ_max]` written; an out-of-interval root is returned | **wrong** |
| 6 | three-outcome table | not a partition; the tight-limit case routes to `NO_CROSSING` | **wrong, and inverted** |

### Demonstration for #4

```
μ̂                          = 0.063
μ* = −a/b   (Â = 0 here)    = 1.379
χ²(μ*)  vs  dᵀWd            = 1.040037 vs 1.040037   ← global MAXIMUM
q̃ peak                      = 1.0386 at μ = 1.38
q̃ plateau (μ → ∞)           = 0.0944
threshold 0.5665, strictly above the plateau:
   v4 claim : no crossing at any μ
   reality  : q̃ exceeds it on μ ∈ [1.08, 1.91] — ACC is disconnected
```

`q̃` does not approach the plateau monotonically. It rises to a peak at `μ*`,
where `Â = 0` and `χ²` attains its global maximum `dᵀWd`, and only then falls to
`dᵀWd − b²/f`. The plateau is not the supremum. Both readers located `μ*`
independently — one via the saturation argument, one via identifiability.

---

## 4. What both readers checked and confirmed CORRECT

Recorded so it is not re-litigated, and because it is the load-bearing half of
the result.

- Splitting `G₃` into pole and logarithm; the pole needs a Cauchy PV, the
  logarithm is integrable and must not be excised; symmetric excision belongs in
  the physical variable `r′`; the §4 correction of v3's stated reason is right.
- One-sided truncation at `r′ = R` is log-divergent for k=3; a double pole is
  not defined by an ordinary principal value.
- The α-cancellation through `Â → χ² → q̃ → q₉₅ →` acceptance set, hence exact
  α-invariance of `L₉₅` itself. (Only the "survives only in…" enumeration is
  wrong.)
- The profiled objective and its expansion into `(a+μb)²/(c+2μe+μ²f)`;
  `c, e, f` are μ-independent, so the closed form genuinely replaces the
  withdrawn scan.
- `χ²(∞) = dᵀWd − (K₃ᵀWd)²/(K₃ᵀWK₃)` — the limit itself, as distinct from the
  inference drawn from it.
- Hartlap with `p = 15` after slice-then-invert is the right dimension (a
  sub-block of a Wishart is Wishart at the same `N`).
- Units self-consistent; cubic splines are equivariant under affine abscissa
  rescaling, so the dual-unit run really is a no-op except for hard-coded
  lengths.
- Grid arithmetic: `3.8 + 0.8·9 = 11.0`, ten nodes, all strictly inside
  `(3.69, 11.08)`; `(6.0−3.8)/0.8 = 2.75`, so 6.0 is genuinely off-grid;
  `[0,60]` step 0.1 is 601 nodes.
- Retention of edge datasets, and its justification.
- Branch 2's `[WEAK]` caveat: ≤1000 distinct support points, the 0.95 quantile
  set by a few dozen rows.
- The distinction between the acceptance rate at `μ_true` and
  `P(L₉₅ ≥ μ_true)` under a possibly disconnected `ACC`, and the admission that
  plug-in validation cannot detect plug-in bias.
- `Δχ² ≥ 0` and the `p = 0.5` convention at `Δχ² = 0`.

---

## 5. The result of three rounds

Everything v4 **prescribes** — kernels, units, grid, quadrature, the PV split,
the closed form, Hartlap — both readers checked and confirmed. Zero errors.

Everything v4 **derives and asserts about itself** — six claims checked, six
wrong.

A specification that argues for its own correctness creates a new error surface
per argument, and each one is something a reader must verify before the document
can freeze. v4 is more precise than v3 *and* contains more false statements,
because the added precision was largely added reasoning.

**Consequence for v5:** the specification states what to compute, in what order,
with what tolerances, and what to do on failure — nothing else. Every derivation,
justification and "v_n got this wrong" migrates to a companion `derivations.md`
that is not gated. This also dissolves D16: the freeze gate then stands over
determinacy of the procedure, which is what a specification can actually
guarantee, rather than over the correctness of the author's algebra, which it
cannot.

**Gate wording must also change.** Round 3 showed two honest readers assigning
different severity labels to identical findings. The v5 gate should be stated in
operational terms — "no finding for which two readers would compute different
numbers" — rather than in a severity vocabulary that is not calibrated between
readers.
