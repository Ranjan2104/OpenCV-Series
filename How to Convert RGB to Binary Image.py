import cv2

img = cv2.imread('men.jpg',0)
cv2.imshow('Grey Image',img)
cv2.waitKey(0)

rel, bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary", bw)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 0 = black pixel
# 1 = White pixel