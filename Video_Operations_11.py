# Now capture video from webcam and save into the memory

import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#DIVX, XVID, MJGP, X264, WMV1, WMV2
fourcc=cv2.VideoWriter_fourcc(*"XVID") #*"XVID"
#It contains 4 parameter , name, codec, fps, resolution
output=cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))

print("cap",cap)

while cap.isOpened():
    ret,frame=cap.read()
    if(ret==True):
        cv2.imshow("Frame",frame)
        output.write(frame)
        if(cv2.waitKey(1) & 0xFF==ord('q')):
            break

cap.release()
output.release()
cv2.destroyAllWindows()