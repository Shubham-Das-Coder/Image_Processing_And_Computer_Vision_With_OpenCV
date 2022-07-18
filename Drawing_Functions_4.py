import numpy as np
import cv2
img=cv2.imread("MSD_WC_Six.jpg")
#Rectangle accepts 5 parameters (img,starting,ending,color,thickness)
img=cv2.rectangle(img,(384,10),(510,128),(128,0,225),8) #Color format is in BGR
cv2.imshow("Res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()