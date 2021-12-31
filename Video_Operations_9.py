# Now capture video from webcam and save into the memory

import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) # This time no error will be shown
print("cap",cap)

while cap.isOpened():
    ret,frame=cap.read()
    if(ret==True):
        frame=cv2.resize(frame,(800,450))
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray",gray)
        if(cv2.waitKey(1) & 0xFF==ord('q')):
            break

cap.release()
cv2.destroyAllWindows()