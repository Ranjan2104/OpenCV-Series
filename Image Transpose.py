import cv2

img = cv2.imread('men.jpg')

rotated_img = cv2.transpose(img)

cv2.imshow("Rotated Image", rotated_img)
cv2.imshow("Original Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()