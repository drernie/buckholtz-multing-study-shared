# Task 026 — baseline arm output

## Findings

**Verdict: not well-supported.** Target-provenance error: validates one artifact (accuracy on held-out test split of training distribution) then asserts readiness for a different artifact (phone-camera photos cropped by an unreliable upstream service). The script's own comments contradict each other: "no input validation" block assumes clean 28x28 matching training data, while the deployment note says the real input "is not from the same clean pipeline as test_images."

1. **Distribution mismatch is the load-bearing flaw.** 98.4% characterizes performance on curated, canonical images — says nothing about off-center, rotated, unevenly-lit, arbitrarily-cropped photographs.
2. **Executed the reshape operation against plausible cropper outputs:**
```
clean 28x28 grayscale: OK, shape (1, 784)
32x30 crop:            CRASH -> ValueError: cannot reshape array of size 960 into shape (1,784)
28x28x3 RGB:            CRASH -> ValueError: cannot reshape array of size 2352 into shape (1,784)
```
Not hypothetical — this is the documented deployment scenario doing exactly what such services do. Zero input validation, zero exception handling: crashes outright.
3. No control/calibration on data resembling actual deployment distribution.
4. Secondary: no confidence thresholding/fallback, no guarantee response codes are single digits, no monitoring plan.

---

**DRAFT CLAIM:** A reported 98.4% accuracy on a held-out test set from the same clean distribution as training was used to conclude a deployed inference microservice is "production-ready as-is." This doesn't follow: production input is phone-camera photos cropped by an explicitly "less reliable" upstream service, a materially different distribution never validated against. The code hard-codes the false assumption that images always arrive as clean 28x28 arrays; direct execution confirms non-canonical shapes (32x30 crop, 28x28 RGB) cause unhandled ValueError in reshape — the service crashes on realistic deployment inputs. The 98.4% figure is not fabricated, but it's evidence for a claim it cannot support. Verdict: unsupported, downgrade to "validated on original clean-dataset distribution only" pending real-sample validation and input handling.
