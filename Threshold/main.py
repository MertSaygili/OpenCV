# importing libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Reading image
default_img = cv2.imread("img1.jpg", 0)
default_img = cv2.resize(default_img, (400, 400))

cv2.imshow("img", default_img)

# Simple Thresholding
_, img_Binary = cv2.threshold(default_img, 127, 255, cv2.THRESH_BINARY)
_, img_InverseBinary = cv2.threshold(default_img, 127, 255, cv2.THRESH_BINARY_INV)
_, img_Trunc = cv2.threshold(default_img, 127, 255, cv2.THRESH_TRUNC)
_, img_Tozero = cv2.threshold(default_img, 127, 255, cv2.THRESH_TOZERO)
_, img_InverseTozero = cv2.threshold(default_img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ["Default Image", "Binary", "Inverse Binary", "Trunc", "Tozero", "Inverse Tozero"]
images = [default_img, img_Binary, img_InverseBinary, img_Trunc, img_Tozero, img_InverseTozero]

for i in range(0, 6, 1):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], cmap="gray"), plt.title(titles[i]), plt.axis("off")

plt.show()

# Adaptive Thresholding
img_AdaptiveMean = cv2.adaptiveThreshold(default_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
img_AdaptiveGaussian = cv2.adaptiveThreshold(default_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

titles2 = ["Default Image", "Adaptive Mean", "Adaptive Gaussian"]
images2 = [default_img, img_AdaptiveMean, img_AdaptiveGaussian]

for i in range(0, 3, 1):
    plt.subplot(1, 3, i+1), plt.imshow(images2[i], cmap="gray"), plt.title(titles2[i]), plt.axis("off")
plt.show()

cv2.waitKey(0) # makes windows open unless you close it
