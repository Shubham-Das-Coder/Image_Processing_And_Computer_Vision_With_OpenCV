import cv2

img1=cv2.imread("E:\College Memories\WhatsApp Image 2021-12-28 at 4.55.56 PM.jpeg",-1) 
img1=cv2.resize(img1,(900,600))
print(img1)
cv2.imshow("Unchanged Image",img1)
cv2.waitKey(3000)
cv2.destroyAllWindows() # It releases all the memory which are used, so when the code terminates all the windows will be destroyed