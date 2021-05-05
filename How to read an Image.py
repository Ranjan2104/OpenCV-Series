import cv2

img = cv2.imread('god.jpeg')

cv2.imshow('Output Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()