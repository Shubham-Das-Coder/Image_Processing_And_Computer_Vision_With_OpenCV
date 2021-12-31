import cv2

cap = cv2.VideoCapture("E:\College Memories\VID20211228084153.mp4")
print("cap",cap)

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(800,450))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # Converting the video into grayscale
    cv2.imshow("Gray",gray)
    k=cv2.waitKey(25)
    if(k==ord("q") & 0xFF):
        break

cap.release()
cv2.destroyAllWindows()