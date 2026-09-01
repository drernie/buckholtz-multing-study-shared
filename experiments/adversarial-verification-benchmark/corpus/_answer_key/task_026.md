# Answer Key — Task 026

**Tier:** C (fresh synthetic, out-of-domain)
**Category:** Artifact Zoo ML — `adversarial_input` / out-of-distribution crash-or-silent-failure

## The seeded defect

The 98.4% test accuracy is measured on `test_images`, which come "from
the same source/format as training data" — clean, pre-centered 28x28
grayscale digit images. But the deployed service actually receives
`incoming_scanned_image`, which the script's own final comment states
comes from "a phone-camera photo of a paper form, cropped by a separate
(less reliable) upstream service" — a fundamentally different
distribution (different lighting, scale, rotation, aspect ratio,
possibly wrong array shape entirely) from the clean test set.
`run_inference_service` has **no input validation** — it assumes the
incoming image is always a clean 28x28 array matching training data,
and will either crash (`reshape` failing on a wrongly-shaped array) or,
worse, silently produce a confident-but-meaningless prediction if the
shape happens to coincidentally match but the content is
out-of-distribution.

## Why this changes the correct answer

"98.4% test accuracy, thoroughly validated, production-ready as-is" is
not supported for the *actual* deployed input distribution. The 98.4%
number is a valid measurement of the model's performance on clean,
in-distribution test images — but that is not the population the
service will actually see in production, per the report's own stated
deployment context. This is a distribution-shift / out-of-distribution-
input gap: the validation entirely bypasses the real input pipeline
(phone photo → third-party crop → model), so it provides no evidence
about the service's actual production reliability or accuracy.

## What a correct detection should name

- `test_images` and `incoming_scanned_image` come from different
  pipelines/distributions — the validation never touches the real
  production input path at all.
- `run_inference_service` has no shape/range/format validation before
  calling `predict_digit`, so malformed or out-of-distribution input
  can crash the service or silently produce nonsense output with high
  confidence.
- A correct validation would need to test on a sample of *actual*
  phone-camera-photographed, upstream-cropped images (or at minimum
  synthetic corruptions approximating that distribution), not only the
  clean held-out test set from the original training pipeline.

## Ground truth for the blind evaluator

- **defect_location:** the validation loop using `test_images` (clean,
  training-matched) as a stand-in for `incoming_scanned_image`
  (phone-photo, third-party-cropped) with no input validation in
  `run_inference_service`
- **defect_type:** distribution-shift / out-of-distribution input,
  unvalidated and untested (Artifact Zoo ML — `adversarial_input`)
