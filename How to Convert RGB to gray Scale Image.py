import  cv2

img = cv2.imread('men.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)

grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey img', grey_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

# OR Another way is
# img = cv2.imread('men.jpg',0)
# cv2.imshow("grey img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()