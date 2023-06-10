import cv2
import numpy as np 
cap = cv2.VideoCapture(0)
kernel = np.ones((15,15),np.float32)/225
while True:
    _,frame = cap.read()
    sb = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.rectangle(frame,(15,25),(200,150),(0,0,255),15)
    # blur =  cv2.filter2D(frame,-1,kernel)
    cv2.imshow("Kamera",frame)
    if cv2.waitKey(5) & 0xFF == ord("e"):
        break

cap.release()
cv2.destroyAllWindows()
