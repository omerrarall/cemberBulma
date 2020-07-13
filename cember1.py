import cv2
import numpy as np
cap = cv2.VideoCapture(0)

cap = cv2.VideoCapture(0)

if not (cap.isOpened()):
    print(“Kamera bulunamadı”)

while(True):
    ret, frame = cap.read()
   # img=cv2.imread("cember.png")
   # img1=np.copy(img)
    print("-------------")
    print(frame.shape)
    print("-------------")

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    blur=cv2.medianBlur(gray,5)

    cember=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,img.shape[0]/2.8,param1=200,param2=10,minRadius=15,maxRadius=110)
    cv2.imshow('frame',gray)

    if cember is not None:
        cember = np.uint16(np.around(cember))
        for i in cember[0,:]:
            cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#cv2.imshow("Resim",img)
#cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
