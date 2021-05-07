import cv2
import numpy as np

img = cv2.imread('men.jpg')

height, width = img.shape[:2]
print("Height is : ",height)
print("Width is : ", width)

quater_height, quater_width = height/4, width/4
print('quater_height is : ', quater_height)
print('quater_width is : ', quater_width)

T = np.float32([[1,0,quater_width],[0,1,quater_height]])
print(T)
# T is translation matrix
# we use WarpAffine Transformation to shift the image.
img_tans = cv2.warpAffine(img, T, (width, height))

cv2.imshow('Original Image', img)
cv2.imshow("Translation Image", img_tans)
cv2.waitKey(0)
cv2.destroyAllWindows()
