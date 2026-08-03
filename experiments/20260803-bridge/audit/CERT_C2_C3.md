# Certificates C2 and C3

**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
Criteria frozen 2026-08-03 before either run.

---

# C2 — transcription fidelity · **PASS**

## Result

```
Path B transcription vs our source-verified file : 0 mismatches of 132 fields
Path B vs the ORIGINAL working file              : exactly 4, all in row 1

   z=0.0  sigma_H      pathB=1.0    original=1.1
   z=0.0  H_MULT       pathB=73.0   original=71.1
   z=0.0  sigma_MULT   pathB=0.0    original=1.3
   z=0.0  w_eff        pathB=-1.3   original=NaN
```

The independent transcription reproduces our corrected file exactly and finds
precisely the four discrepancies we found, at the same fields. **PASS on the
criterion as frozen.**

## Why the independent transcription is trustworthy

Path B had no access to our CSV or our diff. It recovered the row structure from
a flat token stream and validated it three ways, two of which we had not used:

1. **The `±` anchor.** Under a 10-line stride the `±` lands in slot 3 in all
   twelve rows and nowhere else. Any off-by-one anywhere breaks the pattern.
2. **Internal arithmetic, 36 of 36 instances.** The three sigma columns are
   standardised residuals, and all three reproduce to the table's own rounding:
   `sigma_FLRW = (H_FLRW − H_obs)/sigma_H`, and likewise for MULT and w_eff.
   A single misplaced boundary destroys this everywhere downstream.
3. **A prose cross-check using text not used to build the rows.** Page 38 states
   that for nine of twelve times `|σ_MULT|/|σ_FLRW|` lies in 0–0.2, and that
   "for the other three times (13, 5, and 4) the ratios are about 1.3, 0.5, and
   0.3". The reconstruction gives exactly nine rows ≤ 0.2 and those three
   exceptions with ratios 1.33, 0.50, 0.30. **This validates the time column
   independently of the numbers used to build the rows.**

Path B also stated what its checks do *not* cover: the identities constrain the
relative alignment of columns 3–10 within a row but pin `z` only by position and
monotonicity. It flagged `z = 1` and `z = 5` as the most fragile fields, being
bare integers that would also be plausible time values.

## Independent confirmations of earlier findings

Path B reached two of our findings without being told them:

- **The caption's σ_MULT definition is self-referential** — "the number of
  observational standard deviations that associates with σ_MULT minus the
  nominal value of H-data". The C1 reader found the same defect independently.
  Both confirmed arithmetically that the intended reading is *H-MULT* minus
  H-data.
- **The `(z, t)` pairs are inconsistent with standard cosmology** — z = 8.5 at
  3 Gyr against roughly 0.6 in ΛCDM, the discrepancy growing systematically.
  Path B reached this from the transcription alone and correctly noted that the
  source itself does not vouch for these values.

## Items Path B raised that we had not

- **Row 1's bare integers** (`H_MULT = 73`, `sigma_MULT = 0`, `H_w_eff = 73`,
  `sigma_w_eff = 0`) and `H_FLRW = 75, 83` in rows 5–6. Transcribed as written;
  whether the source meant `73.0` or an integer is not determinable from the
  text layer.
- **`sigma_w_eff` rounding is inconsistent between rows.** Rows 5 and 6 compute
  to 0.060 and 0.057 and are both written `0.1`, while row 3 keeps `0.03` for a
  computed 0.025.
- **`w_eff` crosses −1 and is non-monotone** (rows 8–11 sit above −1). Path B
  correctly connected this to the page-38 text anticipating exactly that
  objection, so it is intended behaviour of the source construction rather than
  a suspected transcription error.

---

# C3 — the virial identity `w = n/3` · **PASS**

## Independence conditions met

| condition | met |
|---|---|
| given only the two definitions and the potential form | yes |
| **not told** the expected answer | yes |
| **not told** the expected sign | yes |
| no file access, no web, no literature | yes |
| told there is no expected value, and to derive rather than recall | yes |

## Result returned

`p / rho = n / 3`, derived from Euler's identity for a homogeneous function:
`s·dU/ds = −n·U`, an identity in `s` holding **pair by pair**, before any
averaging. Checked with SymPy, then over 360 synthetic configurations spanning
four correlation shapes, five values of `n` including non-integer, both signs of
`C`, three separation windows and two volumes. Worst deviation from `n/3`:
**6.7 × 10⁻¹⁶**.

Evaluations: `n = 1 → 1/3`, `n = 2 → 2/3`, `n = 3 → 1`. Matches Path A exactly.

## Three refinements Path B supplied that Path A had not

**1. The invariance caveat, stated precisely.** The ratio is invariant under any
regularisation acting on the **pair set** — inner cutoff, outer cutoff, any
weight `w(s)` — because those multiply both sums identically. It is **not**
invariant under a regularisation acting on the **functional form of `U`**:

| modification | effect |
|---|---|
| Yukawa screening `U = C s^(−n) e^(−s/λ)` | breaks it: `s dU/ds = −(n + s/λ)U`, so the ratio becomes a ξ-weighted average and now depends on ξ, density and cutoffs |
| softened core `U = C(s²+a²)^(−n/2)` | breaks it, same reason |
| additive constant `U = C s^(−n) + U₀` | breaks it: `U₀` enters `rho` but not `p` |
| sum of two powers `n₁, n₂` | gives a ξ-weighted average of `n₁/3`, `n₂/3` |

This sharpens NR-018's relaxation map from "possibly survives" to a determinate
rule: **only pair-set regularisations preserve the identity.**

**2. The sign analysis, confirming our correction.** `rho + 3p = (1+n)·rho`, and
since `n > 0` the factor is always positive, so `sign(rho + 3p) = sign(rho)`
unconditionally. For a single-signed potential `sign(rho) = sign(C)`, so `rho`
cannot vanish for `C ≠ 0` whatever `ξ` is.

Path B noted that `n = 1, C < 0` gives `rho < 0` and `rho + 3p < 0`, and then
**declined to draw any cosmological conclusion from it**, on the ground that
doing so would first require establishing that these configurational averages
are the quantities appearing in the equation one has in mind. That is the exact
discipline our first draft failed.

**3. A caution that bears directly on C4.** Path B flagged, unprompted, that the
sums as defined are generally **not finite**:

- Long distance: the uncorrelated part grows as `L^(3−n)` for `n < 3`, so `rho`
  is **not intensive** without a neutralising background, screening or an
  imposed outer cutoff. All three cases of interest are in this regime, and
  `n = 3` is logarithmically divergent.
- Short distance: clustering with `ξ ~ s^(−γ)` pushes the UV divergence down to
  `n + γ ≥ 3`, so even `n = 1` or `n = 2` can diverge for strongly clustered
  configurations. With no form assumed for `ξ`, UV convergence cannot be
  asserted at all.
- `n = 3` is **doubly marginal** — log-divergent at both ends.

> "Each of `rho` and `p` is separately cutoff-dependent and may be arbitrarily
> large; only their ratio is clean. So `p/rho = n/3` should not be read as
> evidence that `rho` and `p` are individually well-defined here."

**This is a direct constraint on C4**, which computes `rho` individually. It
means C4's admissible verdict ceiling is `CONDITIONAL`, not `VERIFIED`, unless
the background subtraction and cutoffs are themselves justified rather than
chosen — and it was raised by an analyst who did not know C4 existed.

**4. A convention point.** The prefactor ratio `(1/2):(1/6) = 3:1` is the
standard virial normalisation **if** the sums run over ordered pairs. Under that
reading these are the conventional quantities. The ratio `n/3` is unchanged
either way; only absolute magnitudes shift by a factor of two — which again
touches C4, not C3.

---

## Combined scope statement

C2 establishes that our copy of the table is faithful. It says nothing about
whether the source numbers are correct.

C3 establishes an identity of one mapping applied to pure inverse powers. It
says nothing about cosmology, nothing about whether `rho` and `p` so defined are
the quantities entering any field equation, and — per Path B's own caution —
nothing about whether either is individually well-defined.
