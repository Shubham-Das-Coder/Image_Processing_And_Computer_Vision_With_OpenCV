import cv2

img1=cv2.imread("E:\College Memories\WhatsApp Image 2021-12-28 at 4.55.56 PM.jpeg")
img1=cv2.resize(img1,(900,600)) # Resizing the image
print(img1)
cv2.imshow("Original Image",img1)
cv2.waitKey()
cv2.destroyAllWindows()