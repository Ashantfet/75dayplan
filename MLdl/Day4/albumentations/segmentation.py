import cv2
import albumentations as A
import numpy as np
from utils import plot_examples
from PIL import Image

image = Image.open("../base.png").convert("RGB")
mask = Image.open("../binary.png")

transform = A.Compose([
    A.Resize(width=256, height=256),
    A.Rotate(limit=35, p=1.0),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.ShiftScaleRotate(shift_limit=0.1, scale_limit=0.1, rotate_limit=15, p=1.0),
    A.GridDistortion(num_steps=5, distort_limit=0.3, p=0.5),  # mask-friendly
])

image_np = np.array(image)
mask_np = np.array(mask)

pairs = []  # (image, mask) pairs for plotting

# Create 10 augmented versions
for i in range(10):
    augmented = transform(image=image_np, mask=mask_np)

    aug_img = augmented["image"]
    aug_mask = augmented["mask"]

    pairs.append((aug_img, aug_mask))

# ---- Plot side by side ----
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 20))

for idx, (img, msk) in enumerate(pairs):
    plt.subplot(10, 2, idx*2 + 1)
    plt.imshow(img)
    plt.axis("off")
    plt.title(f"Augmented Image {idx}")

    plt.subplot(10, 2, idx*2 + 2)
    plt.imshow(msk, cmap="gray")
    plt.axis("off")
    plt.title(f"Mask {idx}")

plt.tight_layout()
plt.show()
