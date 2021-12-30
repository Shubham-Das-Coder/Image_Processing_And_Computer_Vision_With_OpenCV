import cv2

img1=cv2.imread("E:\College Memories\WhatsApp Image 2021-12-28 at 4.55.56 PM.jpeg",-1) # -1 means the image will remain the same but the saturation value of the colour will be more which means that the alpha channels will be more 
img1=cv2.resize(img1,(900,600))
print(img1)
cv2.imshow("Unchanged Image",img1)
cv2.waitKey(3000)
cv2.destroyAllWindows()