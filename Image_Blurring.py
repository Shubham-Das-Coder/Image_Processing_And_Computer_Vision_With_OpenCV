#Importing the modules
import cv2
import numpy as np

#Importing the image
img=cv2.imread("Nature.jpeg")

#Resizing the image
img=cv2.resize(img,(500,300))

#Creating the filters
kernel_1=np.array([[0,0,0],[0,1,0],[0,0,0]])/1.0
kernel_3=np.ones((3,3),dtype=np.float32)/9.0
kernel_5=np.ones((5,5),dtype=np.float32)/25.0
kernel_7=np.ones((7,7),dtype=np.float32)/49.0

#Applying the filters
output_1=cv2.filter2D(img,-1,kernel_1)
output_2=cv2.filter2D(img,-1,kernel_3)
output_3=cv2.filter2D(img,-1,kernel_5)
output_4=cv2.filter2D(img,-1,kernel_7)

while(True):
    #Displaying the image
    cv2.imshow('Original',output_1)
    cv2.imshow('3 Blur',output_2)
    cv2.imshow('5 Blur',output_3)
    cv2.imshow('7 Blur',output_4)
    if cv2.waitKey(1) & 0xff == 27:
        break
cv2.destroyAllWindows()