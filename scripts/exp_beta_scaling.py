"""
EXP-BETA: Is β_l ∝ l²? — Testing the multipole scaling hypothesis.

Observation: Claude/NotebookLM extraction gives β_d=4.5, β_q=18.0 → ratio=4=2².
Hypothesis: β_l = C × l^n where C=9/2, n=2 (classical rotational energy scaling).

Zero-Signal Gate:
  Entity: β_d, β_q from three AI services
  Predicate: β_l = (9/2) × l² (power law with exponent 2)
  Measurable outcome: exponent n from log-ratio; octupole prediction β_3=40.5

CRITICAL BLOCKER: Ratio βq/βd is NOT consistent across AI services.
This script quantifies the inconsistency before any theory is proposed.
"""

import math

# ── Three AI service extractions ──────────────────────────────────────────
EXTRACTIONS = {
    "Claude/NotebookLM": {"beta_d": 4.50, "beta_q": 18.0},
    "Gemini": {"beta_d": 4.25, "beta_q": 8.10},
    "ChatGPT": {"beta_d": 0.78, "beta_q": 0.19},
}

# ── Physical scaling candidates ───────────────────────────────────────────
# β_l = C × f(l), where f(l) is the scaling function
SCALING_MODELS = {
    "l^2 (classical rotational KE)": lambda lv: lv**2,
    "l(l+1) (quantum Casimir C_2)": lambda lv: lv * (lv + 1),
    "2l+1 (degeneracy)": lambda lv: 2 * lv + 1,
    "l (linear)": lambda lv: lv,
    "const (no l-dep)": lambda lv: 1.0,
}

L_D = 1  # dipole
L_Q = 2  # quadrupole
L_OCT = 3  # octupole (prediction)

print("=" * 70)
print("EXP-BETA: β Scaling Hypothesis — β_l ∝ l^n?")
print("=" * 70)

# ── Step 0: ratio inconsistency check ────────────────────────────────────
print()
print("─" * 70)
print("STEP 0 — BLOCKER CHECK: β_q/β_d ratio across services")
print("─" * 70)
print(f"  {'Service':<22}  {'β_d':>6}  {'β_q':>6}  {'ratio':>7}  {'n=log(r)/log(2)':>17}")
print(f"  {'─' * 65}")

ratios = []
for svc, vals in EXTRACTIONS.items():
    bd = vals["beta_d"]
    bq = vals["beta_q"]
    ratio = bq / bd
    n_fit = math.log(ratio) / math.log(L_Q / L_D)  # log(ratio)/log(2)
    ratios.append(ratio)
    print(f"  {svc:<22}  {bd:6.2f}  {bq:6.2f}  {ratio:7.3f}  {n_fit:17.3f}")

ratio_spread = max(ratios) / min(ratios)
print(
    f"\n  Spread in ratio: {ratio_spread:.1f}×  "
    f"({'INCONSISTENT — stop here' if ratio_spread > 3 else 'consistent'})"
)

print()
if ratio_spread > 3:
    print("  [BLOCKER] β_q/β_d ranges from 0.24 to 4.00 (16× spread).")
    print("  The scaling law is extraction-dependent.")
    print("  Proceed with HYPOTHESIS status only, not [VERIFIED].")
    print()
    print("  Root cause candidates:")
    print("  A) Gemini/ChatGPT under-extracted β_q from the paper")
    print("  B) Claude over-extracted β_q (confirmation of l² pattern)")
    print("  C) Paper does not uniquely determine β_q (underdetermined)")
    print()
    print("  Required to resolve: read original paper Table A1 footnote")
    print("  or Appendix A.1 verbatim for β_d, β_q values.")

# ── Step 1: test scaling models ───────────────────────────────────────────
print()
print("─" * 70)
print("STEP 1 — SCALING MODEL COMPARISON (Claude extraction as reference)")
print("─" * 70)
bd_ref = EXTRACTIONS["Claude/NotebookLM"]["beta_d"]
bq_ref = EXTRACTIONS["Claude/NotebookLM"]["beta_q"]

print(f"\n  Reference: β_d={bd_ref}, β_q={bq_ref}")
print()
print(
    f"  {'Model':<30}  {'C from β_d':>12}  {'predicted β_q':>14}  {'actual β_q':>10}  {'error%':>8}"
)
print(f"  {'─' * 78}")

best_model = None
best_err = float("inf")
for name, f in SCALING_MODELS.items():
    c = bd_ref / f(L_D)  # calibrate from β_d
    pred_bq = c * f(L_Q)
    err_pct = abs(pred_bq - bq_ref) / bq_ref * 100
    marker = "  ← EXACT" if err_pct < 0.1 else ""
    print(f"  {name:<30}  {c:12.4f}  {pred_bq:14.4f}  {bq_ref:10.4f}  {err_pct:8.2f}%{marker}")
    if err_pct < best_err:
        best_err = err_pct
        best_model = name

print(f"\n  Best fit: '{best_model}' (error {best_err:.2f}%)")

# ── Step 2: physical interpretation of l² ────────────────────────────────
print()
print("─" * 70)
print("STEP 2 — PHYSICAL MOTIVATION FOR β_l ∝ l²")
print("─" * 70)
print()
print("  Classical orbital mechanics:")
print("  Angular momentum magnitude: L = l × ħ  (classical approximation)")
print("  Rotational kinetic energy:  E_rot = L²/(2I) = l² × ħ²/(2I)")
print("  → β_l ∝ E_rot/E_unit ∝ l²")
print()
print("  Quantum mechanics (comparison):")
print("  ⟨L²⟩ = l(l+1)ħ²")
print(
    f"  l=1: ⟨L²⟩ = {1 * (1 + 1)} · l=2: ⟨L²⟩ = {2 * (2 + 1)} · ratio = {2 * (2 + 1) / (1 * (1 + 1)):.1f}"
)
print("  → quantum Casimir gives ratio 3, not 4")
print()
print("  MULTING uses classical l² (ratio=4) vs quantum l(l+1) (ratio=3).")
print("  This is a distinguishing prediction: if β_l ∝ l² is verified,")
print("  it implies MULTING's gravitational multipole expansion is CLASSICAL.")

# ── Step 3: falsifiable prediction ───────────────────────────────────────
print()
print("─" * 70)
print("STEP 3 — FALSIFIABLE PREDICTION")
print("─" * 70)
c_classical = bd_ref / L_D**2  # C = β_d / l_d² = 4.5 / 1 = 4.5

print(f"\n  If β_l = C × l² with C = {c_classical} (= β_d):")
print()
print(f"  {'l':<4}  {'Name':>12}  {'β_l (predicted)':>17}  {'Ratio to β_d':>14}")
print(f"  {'─' * 55}")
for l_val in [1, 2, 3, 4, 5]:
    beta_pred = c_classical * l_val**2
    ratio_to_d = beta_pred / bd_ref
    names = {1: "dipole", 2: "quadrupole", 3: "octupole", 4: "hexadecapole", 5: "triakontadipole"}
    marker = (
        "  ← calibrated"
        if l_val == 1
        else ("  ← matches Claude" if l_val == 2 else "  ← PREDICTION")
    )
    print(f"  {l_val:<4}  {names[l_val]:>12}  {beta_pred:17.2f}  {ratio_to_d:14.1f}{marker}")

print()
print(f"  KEY PREDICTION: β_octupole = {c_classical * L_OCT**2:.1f}")
print(f"  If paper mentions β for l=3 multipole → compare to {c_classical * L_OCT**2:.1f}.")

# ── Step 4: natural constant C = 9/2 ─────────────────────────────────────
print()
print("─" * 70)
print("STEP 4 — IS C = 9/2 NATURAL?")
print("─" * 70)
print()
print(f"  C = β_d / 1² = {bd_ref} = 9/2")
print()
print("  Candidate origins of 9/2:")
print("  (a) 9 = 3² (spatial dimensions D=3): C = D²/2 = 9/2  ✓")
print("  (b) 9 = N_isomers + 4:  5+4 = 9  →  weak")
print("  (c) 9 = 3 × N_isomers - 6: 15-6  →  weak")
print("  (d) 9/2 = 4.5 ≈ cluster virial ratio (kinetic/potential): depends on profile")
print()
print("  Candidate (a) is most natural: C = D²/2 where D=3 is spatial dimension.")
print("  Then: β_l = (D²/2) × l² = (9/2) × l²")
print("  This would link MULTING's coupling to 3D spatial geometry.")
print("  Testable: in D=4 cosmology (KK reduction), C' = D'²/2 = 8 → β_d'=8.")

# ── Summary ───────────────────────────────────────────────────────────────
print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()
print("  Hypothesis: β_l = (9/2) × l²  →  CLOSED")
print()
print("  [VERIFIED from paper, 2026-06-25]")
print("  Table A1 caption (p.38): 'the online service reported choosing β_d=4.5 and β_q=18.0'")
print("  Step 5 (p.34): 'Try to choose positive values for β_d and β_q that MINIMIZE")
print("  standard-deviations away from nominal observed H(z).'")
print()
print("  CONCLUSION: β_d and β_q are FREE FITTING PARAMETERS, not derived quantities.")
print("  Buckholtz does not prescribe their values — each AI service chooses them")
print("  independently to minimize σ_MULT. The ratio βq/βd = 4 is a coincidence")
print("  of one optimization run (Claude/NotebookLM), NOT a physical law.")
print()
print("  Evidence FOR l² law:")
print("  ✓ Claude/NotebookLM fit: β_d=4.5, β_q=18 → ratio=4=2² (exact, [VERIFIED])")
print("  ✓ Mathematical fit is perfect within this one run")
print()
print("  Evidence AGAINST l² as physical law:")
print("  ✗ β_d, β_q are free parameters — any ratio is equally valid a priori")
print("  ✗ Gemini's fit: ratio=1.9 (different optimization settled elsewhere)")
print("  ✗ ChatGPT's fit: ratio=0.24 (optimization gives inverse scaling)")
print("  ✗ No octupole β_3 term exists in paper to test against 40.5")
print("  ✗ Buckholtz explicitly says values come from fitting, not derivation")
print()
print("  VERDICT: CLOSED — not a physical law, fitting artifact.")
print("  The l² coincidence is mathematically exact for ONE service's run.")
print("  It could constrain a future Lagrangian (if MULTING ever gets one),")
print("  but cannot be claimed as a finding from the current paper.")
print()
print("  Value: 3/10 as physical insight, 8/10 as diagnostic of parameter freedom.")
