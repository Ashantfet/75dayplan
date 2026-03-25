import cv2
import numpy as np
from models.segmentation import get_mask
from utils.warping import simple_warp

person_path = "data/person.jpg"
cloth_path = "data/image.png"
import mediapipe as mp
import cv2

mp_pose = mp.solutions.pose

def get_shoulders(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with mp_pose.Pose(static_image_mode=True) as pose:
        results = pose.process(image_rgb)

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark

        left_shoulder = landmarks[11]
        right_shoulder = landmarks[12]

        h, w, _ = image.shape

        left = (int(left_shoulder.x * w), int(left_shoulder.y * h))
        right = (int(right_shoulder.x * w), int(right_shoulder.y * h))

        return left, right

    return None, None
left, right = get_shoulders(person_path)

shoulder_width = abs(right[0] - left[0])
# Step 1: Get segmentation mask
image, mask = get_mask(person_path)
image = np.array(image)

# Step 2: Warp cloth
cloth = simple_warp(cloth_path, image.shape[:2])

# Step 3: Create binary mask (simplified)
# Resize mask to original image size
mask_resized = cv2.resize(mask, (image.shape[1], image.shape[0]))

binary_mask = (mask_resized > 0).astype(np.uint8)
# Step 4: Overlay
output = image.copy()
output[binary_mask == 1] = cloth[binary_mask == 1]

# Save result
cv2.imwrite("output.jpg", output)