import cv2

img = cv2.imread('men.jpg')
cv2.imshow("original", img)
cv2.waitKey()

# let make the size of image 3/4 of its original size
img_scaled = cv2.resize(img,None,fx=0.75,fy=0.75)
cv2.imshow('Scale linear Interpolatation', img_scaled)
cv2.waitKey()

# let double the size of Image
img_scaled1 = cv2.resize(img,None,fx=2, fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow('Scaling cubic Interpolatation', img_scaled1)
cv2.waitKey()

# let skew the resizing by setting exact dimensions
img_scaled2 = cv2.resize(img,(900,400),interpolation=cv2.INTER_AREA)
cv2.imshow('Scaling Skewed size', img_scaled2)
cv2.waitKey()

cv2.destroyAllWindows()
