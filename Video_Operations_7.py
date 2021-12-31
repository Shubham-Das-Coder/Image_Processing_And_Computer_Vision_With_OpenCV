import cv2

cap = cv2.VideoCapture("E:\College Memories\VID20211228084153.mp4")
print("cap",cap)

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(800,450))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray",gray)
    k=cv2.waitKey(500) # On increasing the value of waitkey, the playback speed of the video decreases
    if(k==ord("q") & 0xFF):
        break

cap.release()
cv2.destroyAllWindows()