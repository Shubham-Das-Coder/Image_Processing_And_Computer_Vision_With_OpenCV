import cv2 #openCV use as cv2 in python

img1=cv2.imread("E:\College Memories\WhatsApp Image 2021-12-28 at 4.55.56 PM.jpeg",0) #1 indicates that the image is greyscale mode
img1=cv2.resize(img1,(900,600)) #Resizing the image
print(img1)
cv2.imshow("original",img1)
cv2.waitKey(0) #Even if we dont pass any number in it, it takes 0 by default
cv2.destroyAllWindows()