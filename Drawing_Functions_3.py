import numpy as np
import cv2
img=cv2.imread("MSD_WC_Six.jpg")
#Arrowed line accepts 5 parameters (img,starting,ending,color,thickness)
img=cv2.arrowedLine(img,(0,125),(255,255),(255,0,125),10) #Color format is in BGR
cv2.imshow("Res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()