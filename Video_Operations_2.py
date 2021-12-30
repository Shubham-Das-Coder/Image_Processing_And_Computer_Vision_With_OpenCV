import cv2

cap = cv2.VideoCapture("E:\College Memories\WhatsApp_Video_2021-12-28_at_4.05.46_PM.mp4") # Accessing the video
print("cap",cap)

while True:
    ret,frame=cap.read() # read() function returns two values, one boolean value and the other an image
    cv2.imshow("Frame",frame)
    cv2.waitKey(25)

cap.release()
cv2.destroyAllWindows()