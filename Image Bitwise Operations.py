import cv2
import numpy as np

square = np.zeros((300,300),np.uint8)

cv2.rectangle(square,(50,50),(250,250),255,-1)
cv2.imshow("Square", square)
cv2.waitKey(0)

# making an eclipse
eclipse = np.zeros((300,300), np.uint8)
cv2.ellipse(eclipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow("Ellipse",eclipse)
cv2.waitKey(0)

And = cv2.bitwise_and(square,eclipse)
cv2.imshow("AND", And)
cv2.waitKey(0)

Or = cv2.bitwise_or(square,eclipse)
cv2.imshow("OR",Or)
cv2.waitKey(0)

Xor = cv2.bitwise_xor(square,eclipse)
cv2.imshow('XOR',Xor)
cv2.waitKey(0)

Not = cv2.bitwise_not(eclipse)
cv2.imshow("Not", Not)
cv2.waitKey(0)

Not = cv2.bitwise_not(square)
cv2.imshow("Not", Not)
cv2.waitKey(0)

cv2.destroyAllWindows()