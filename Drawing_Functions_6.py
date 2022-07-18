import numpy as np
import cv2
img=cv2.imread("MSD_WC_Six.jpg")
#Circle accepts 5 parameters (img,center,radius,color,thickness)
img=cv2.circle(img,(447,125),63,(214,225,0),5) #Color format is in BGR
cv2.imshow("Res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()