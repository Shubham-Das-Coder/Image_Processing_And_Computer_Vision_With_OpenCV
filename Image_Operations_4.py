import cv2 #openCV use as cv2 in python

img1=cv2.imread("E:\College Memories\WhatsApp Image 2021-12-28 at 4.55.56 PM.jpeg",0) # 0 indicates that the image is in greyscale mode
img1=cv2.resize(img1,(900,600)) 
print(img1)
cv2.imshow("original",img1)
cv2.waitKey()
cv2.destroyAllWindows()