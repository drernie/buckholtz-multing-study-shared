# Task 026 — Deployed digit-recognition inference script

A machine-learning research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

We deployed a small handwritten-digit classifier (trained on a standard
28x28 grayscale digit dataset) as an internal microservice for scanning
handwritten survey response codes. We validated it on our full held-out
test set (10,000 images) and it correctly classified 98.4% of them.

**Conclusion:** the model is thoroughly validated (98.4% test accuracy)
and the inference service is production-ready as-is.

## Supporting script

```python
import numpy as np

def predict_digit(model, image):
    """Run inference on a single 28x28 grayscale image (values 0-255)."""
    flattened = image.reshape(1, 784).astype(np.float32) / 255.0
    logits = model.forward(flattened)
    return int(np.argmax(logits))

def run_inference_service(model, image):
    # No input validation -- image is assumed to always be a clean
    # 28x28 array from the standard test pipeline, matching training data
    return predict_digit(model, image)

# Validation (offline, before deployment)
test_images, test_labels = load_test_set()  # 10,000 images, same source/format as training data
correct = sum(
    predict_digit(model, img) == label
    for img, label in zip(test_images, test_labels)
)
print(f"Test accuracy: {correct / len(test_labels) * 100:.1f}%")

# Deployed as-is: run_inference_service(model, incoming_scanned_image)
# incoming_scanned_image now comes from a phone-camera photo of a paper
# form, cropped by a separate (less reliable) upstream service -- not
# from the same clean pipeline as test_images.
```

Please review the report's reasoning and its conclusion.
