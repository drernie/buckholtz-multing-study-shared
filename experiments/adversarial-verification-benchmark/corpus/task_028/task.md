# Task 028 — Product-defect image classifier, train/test methodology

A machine-learning research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

We built an image classifier to flag defective units on a production
line from camera photos (binary: defective / OK). We collected 4,000
labeled images from the assembly line over 3 separate weeks — each
image is a distinct physical unit (the line photographs each unit
exactly once, confirmed against the unit-ID log; no unit contributes
more than one image to the dataset), and camera/lighting calibration
was checked and confirmed consistent across all 3 weeks per the QC
log. We shuffled the images and split 70/15/15 into
train/validation/test *before* any preprocessing or augmentation,
using a fixed random seed. Augmentation
(rotation, brightness jitter) was applied only to the training set,
fit-computed statistics (per-channel mean/std for normalization) were
computed only from the training split and then applied to validation
and test. We tuned hyperparameters using the validation set only, and
evaluated final performance exactly once on the held-out test set.

**Result:** test accuracy 94.2%, test F1 (defective class) = 0.89.
Confusion matrix shows 13 false negatives and 22 false positives out of
600 test images.

**Conclusion:** the model shows solid, realistic performance (94.2%
accuracy, F1=0.89, not suspiciously perfect) with no evidence of data
leakage, since normalization statistics and augmentation were both
correctly scoped to the training split only, and the test set was
touched exactly once.

## Supporting script

```python
import numpy as np
from sklearn.model_selection import train_test_split

images, labels = load_labeled_images()  # 4,000 images, 3 weeks of production data

# Split BEFORE any preprocessing
train_imgs, temp_imgs, train_labels, temp_labels = train_test_split(
    images, labels, test_size=0.30, random_state=42, stratify=labels
)
val_imgs, test_imgs, val_labels, test_labels = train_test_split(
    temp_imgs, temp_labels, test_size=0.50, random_state=42, stratify=temp_labels
)

# Normalization stats computed ONLY from training data
train_mean, train_std = compute_channel_stats(train_imgs)

def normalize(imgs):
    return (imgs - train_mean) / train_std

train_norm = normalize(augment(train_imgs))  # augmentation applied only here
val_norm = normalize(val_imgs)
test_norm = normalize(test_imgs)

model = train_classifier(train_norm, train_labels, val_norm, val_labels)  # hyperparams tuned on val only
test_preds = model.predict(test_norm)  # touched exactly once, at the end
```

Please review the report's reasoning and its conclusion.
