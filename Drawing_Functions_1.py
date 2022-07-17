import numpy as np
import cv2
img=cv2.imread("MSD_WC_Six.jpg")
#Here line accept 5 parameter (img,starting,ending,color,thickness)
img=cv2.line(img,(0,0),(200,200),(154,92,424),8) #Color format is in BGR
cv2.imshow("Res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()