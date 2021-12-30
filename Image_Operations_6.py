import cv2

img1=cv2.imread("E:\College Memories\WhatsApp Image 2021-12-28 at 4.55.56 PM.jpeg",0)
img1=cv2.resize(img1,(900,600))
print(img1)
cv2.imshow("Greyscale Image",img1)
cv2.waitKey(0) # Even if we dont pass any number in it, it takes 0 by default
cv2.destroyAllWindows()