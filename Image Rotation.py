import cv2

img = cv2.imread('men.jpg')

height, width = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 70, 0.7)
rotated_image = cv2.warpAffine(img, rotation_matrix, (width,height))

cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Original Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()