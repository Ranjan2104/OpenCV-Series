import cv2

cap = cv2.VideoCapture(0)

while True:
    rel, frame = cap.read()
    cv2.imshow('Our Live sketch', frame)
    if cv2.waitKey(1) == 13:
       break

cap.release()
cv2.destroyAllWindows()