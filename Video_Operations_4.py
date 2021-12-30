import cv2

cap = cv2.VideoCapture("E:\College Memories\VID20211228084153.mp4")
print("cap",cap)

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(800,450))
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(25)
    if(k==ord("q") & 0xFF): # Sometimes error can be seen in some systems, so the second part is shown
        break

cap.release()
cv2.destroyAllWindows()