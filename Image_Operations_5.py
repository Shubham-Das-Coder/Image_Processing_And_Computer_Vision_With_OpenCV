import cv2

img1=cv2.imread("E:\College Memories\WhatsApp Image 2021-12-28 at 4.55.56 PM.jpeg",0)
img1=cv2.resize(img1,(900,600))
print(img1)
cv2.imshow("original",img1)
# cv2.waitKey() controls the visulization which means it cannot hold the screen
cv2.destroyAllWindows()