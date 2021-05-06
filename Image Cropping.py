import cv2

img = cv2.imread('men.jpg')
height, width = img.shape[:2]

# let get the starting pixel coordinates(top left of cropping rect.)
start_row,start_col = int(height * .25), int(height * .25)

# let get the ending pixel coordinates(bottom right)
end_row,end_col = int(height * .75), int(height * .75)

# simply use the indexing to crop the image
cropped = img[start_row:end_row, start_col:end_col]

cv2.imshow('Original', img)
cv2.waitKey(0)

cv2.imshow('Cropped', cropped)
cv2.waitKey(0)

cv2.destroyAllWindows()