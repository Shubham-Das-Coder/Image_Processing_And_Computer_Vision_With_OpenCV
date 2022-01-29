# Now capture video from webcam and save into the memory

import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#DIVX, XVID, MJGP, X264, WMV1, WMV2
fourcc=cv2.VideoWriter_fourcc(*"XVID") #*"XVID"
#It contains 4 parameter , name, codec, fps, resolution
output=cv2.VideoWriter("output_gray.avi",fourcc,20.0,(640,480),0)

print("cap",cap)

while cap.isOpened():
    ret,frame=cap.read()
    if(ret==True):
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray=cv2.flip(gray,0)
        cv2.imshow("Gray",gray)
        output.write(gray)
        if(cv2.waitKey(1) & 0xFF==ord('q')):
            break

cap.release()
output.release()
cv2.destroyAllWindows()