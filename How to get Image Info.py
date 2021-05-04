import cv2

img = cv2.imread('god.jpeg')
cv2.imshow('Output', img)

print(img.shape)
print("Height Pixel Value : ", img.shape[0])
print("Width Pixel Value : ", img.shape[1])


cv2.waitKey(0)
cv2.destroyAllWindows()