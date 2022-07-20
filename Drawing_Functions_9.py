import numpy as np
import cv2
img=cv2.imread("MSD_WC_Six.jpg")
#Ellipse  accepts (img,center,axes_length,rotation_angle,start_angle,end_angle,colour,thickness)
img=cv2.ellipse(img,(200,300),(100,50),0,0,180,(145,78,236),5) #Color format is in BGR
cv2.imshow("Res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()