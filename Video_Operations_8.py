# Now capture video from webcam and save into the memory

import cv2

cap = cv2.VideoCapture(0) # 0 means webcam of the system, but if we want to access from external camera then 1 must be passed
print("cap",cap)

while cap.isOpened(): # This function checks whether the webcam is opened or not
    ret,frame=cap.read()
    if(ret==True):
        frame=cv2.resize(frame,(800,450))
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray",gray)
        if(cv2.waitKey(1) & 0xFF==ord('q')): # Press 'q' to exit
            break

cap.release()
cv2.destroyAllWindows()