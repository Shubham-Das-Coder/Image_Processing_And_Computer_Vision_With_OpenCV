# Now capture video from webcam and save into the memory

import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
print("cap",cap)

while cap.isOpened():
    ret,frame=cap.read()
    if(ret==True):
        frame=cv2.resize(frame,(800,450)) # Coloured video will be displayed
        cv2.imshow("Frame",frame)
        if(cv2.waitKey(1) & 0xFF==ord('q')):
            break

cap.release()
cv2.destroyAllWindows()