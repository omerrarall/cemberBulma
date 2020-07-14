import cv2
import numpy as np
cap = cv2.VideoCapture(0)

cap1 = cv2.VideoCapture(1)


while(True):

   ret, frame = cap.read()
   ret1, frame1 = cap1.read()

     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    blur=cv2.medianBlur(gray,5)
    
    gray1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

    blur1=cv2.medianBlur(gray1,5)

    cember=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,frame.shape[0]/2.8,param1=200,param2=10,minRadius=15,maxRadius=110)

    cember1=cv2.HoughCircles(blur1,cv2.HOUGH_GRADIENT,1,frame1.shape[0]/2.8,param1=200,param2=10,minRadius=15,maxRadius=110)

    if cember is not None:
        cember = np.uint16(np.around(cember))
        for i in cember[0,:]:
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
    
    if cember1 is not None:
    cember1 = np.uint16(np.around(cember))
    for j in cember[0,:]:
        cv2.circle(frame1,(j[0],j[1]),j[2],(0,255,0),2)

    cv2.imshow('frame',frame)
    cv2.imshow('frame1',frame1)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#cv2.imshow("Resim",img)
#cv2.waitKey(0)
cap.release()

cap1.release()

cv2.destroyAllWindows()
