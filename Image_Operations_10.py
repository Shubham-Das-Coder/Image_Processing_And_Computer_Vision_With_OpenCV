import cv2

img1=cv2.imread("E:\College Memories\WhatsApp Image 2021-12-28 at 4.55.56 PM.jpeg",-1) 
img1=cv2.resize(img1,(900,600))
img1=cv2.flip(img1,0) # It flips the image upside-down
print(img1)
cv2.imshow("Unchanged Image",img1)
cv2.waitKey(3000)
cv2.destroyAllWindows()