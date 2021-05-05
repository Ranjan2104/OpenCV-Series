import cv2

img = cv2.imread('god.jpeg')
cv2.imshow('Original Image', img)

cv2.imwrite('output1.jpeg',img)
cv2.imwrite('output2.png',img)

cv2.waitKey(0)
cv2.destroyAllWindows()