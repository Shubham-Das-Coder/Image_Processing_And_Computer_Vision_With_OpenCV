import cv2

img1=cv2.imread("E:\College Memories\WhatsApp Image 2021-12-28 at 4.55.56 PM.jpeg",0)
img1=cv2.resize(img1,(900,600))
print(img1)
cv2.imshow("Greyscale Image",img1)
cv2.waitKey(3000) # The screen holds the image for 3 seconds or 3000 milliseconds
cv2.destroyAllWindows()