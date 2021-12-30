import cv2

cap = cv2.VideoCapture("E:\College Memories\VID20211228084153.mp4")
print("cap",cap)

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(800,450)) # Resizing the frame, here, 800 is the width and 450 is the height
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(25)
    if(k==ord("q")): # If q is pressed, then the video stops
        break

cap.release()
cv2.destroyAllWindows()