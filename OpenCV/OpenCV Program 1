import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    ret,th = cv2.threshold(blur,100,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('threshold',th)
    contours, hierarchy = cv2.findContours(th,1,cv2.CHAIN_APPROX_NONE)
    if len(contours) > 0:
        for cnt in contours:
            rect=cv2.minAreaRect(cnt)
            box=cv2.boxPoints(rect)
            box=np.int0(box)
            cv2.drawContours(frame,[box],0,(0,0,255),2)
    cv2.imshow('final',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    
