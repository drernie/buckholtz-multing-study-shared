# Task 026 — treatment arm output (FL protocol)

## FL Standard-Ladder Review — Task 026

### 1. Falsifiable claim
"98.4% test accuracy" therefore "production-ready as-is." Unpacked: (a) 98.4% is representative of deployed-input accuracy; (b) no-input-validation is safe because images will always be clean 28x28; (c) no further work needed.

### 2. Controls
Positive control present (held-out test set) but answers a narrower question than the conclusion asserts. **Negative control absent** — no test against actual deployment distribution, no OOD test, no malformed-input test.

### 3. What's wrong
Target-provenance mismatch: validation set is "same source/format as training," while the code's own trailing comment says the deployed image "now comes from a phone-camera photo... cropped by a separate (less reliable) upstream service — not from the same clean pipeline." The report's own artifact contradicts its own conclusion. Silently-fixed parameter: predict_digit hard-codes "28x28 uint8, single channel," zero validation.

### 4. Executed checks
- Distribution-shift mechanism (stand-in dataset, illustrative): clean held-out 95.7% -> same items with phone-photo-like corruption 46.7% -- a ~49-point drop from distribution shift alone, no retraining, demonstrating the mechanism the report's own comment already flags.
- Report's own reshape/normalize logic against plausible cropper outputs: 30x26 crop -> `ValueError` (784-mismatch); 28x28x3 RGB -> `ValueError`; already-[0,1]-range image divided by 255 again -> silently corrupted, no error. Both crashes and silent corruption are direct, checkable contradictions of "production-ready as-is."

### 5. Verdict
**REJECT.** 98.4% is a real but narrow positive-control result — evidence the model fits its own training-format distribution, nothing more. Directly contradicted by the deployment note in the SAME file.

---

### DRAFT CLAIM
A digit-classifier microservice reports 98.4% accuracy on a held-out test set from the same source/format as training, claimed "production-ready as-is." The deployed input stream is explicitly different (phone-camera photos cropped by a less-reliable upstream service), and the inference code performs no input validation, hard-coding clean 28x28 uint8 grayscale assumptions. A stand-in distribution-shift experiment showed a ~49-point accuracy drop under camera-capture-style corruption with no retraining. Executing the report's own reshape/normalize logic against differently-shaped/scaled inputs either crashed with unhandled ValueError or silently corrupted the input with no error signal. Verdict: 98.4% is a valid positive-control measurement but does not support production-readiness, since no negative control or deployment-distribution test was performed and the code has no defined behavior for the shape/format/range deviations that distribution is known to produce.
