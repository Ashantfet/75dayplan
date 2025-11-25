import cv2
import albumentations as A
from albumentations.pytorch import ToTensorV2
import numpy as np
from utils import plot_examples
from PIL import Image
import os

image = Image.open("../base.png").convert("RGB")

transform = A.Compose([
    A.Resize(width=256, height=256),
    A.Rotate(limit=35, p=1.0),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Convert PIL → numpy
original_np = np.array(image)

# List to store original + augmented images for plotting
image_list = [original_np]

# Create 5 augmented versions
for i in range(10):
    augmented = transform(image=original_np)["image"]
    # Albumentations returns normalized float32 — convert back to [0,255] uint8 for plotting
    aug_show = np.clip((augmented * 255), 0, 255).astype(np.uint8)
    image_list.append(aug_show)

# Plot all 6 images (original + 5 augmentations)
plot_examples(image_list, figsize=(15, 6))
