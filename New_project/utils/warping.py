import cv2
import numpy as np

def simple_warp(cloth_img, target_shape):
    cloth = cv2.imread(cloth_img)
    cloth = cv2.resize(cloth, (target_shape[1], target_shape[0]))
    return cloth