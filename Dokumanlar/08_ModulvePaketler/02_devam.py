import cv2 
import numpy as np
face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
while True:
    _,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    yuzler = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in yuzler:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("YuzTespit",img)
    if cv2.waitKey(30) & 0xFF == ord("e"):
        break

cv2.destroyAllWindows()
cap.release()