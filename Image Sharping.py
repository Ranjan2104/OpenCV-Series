import cv2
import numpy as np

img = cv2.imread('men.jpg')
cv2.imshow('Original Image', img)
cv2.waitKey(0)

kernel_sharpening = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
sharpened = cv2.filter2D(img, -1, kernel_sharpening)
cv2.imshow('Image Sharpening', sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()