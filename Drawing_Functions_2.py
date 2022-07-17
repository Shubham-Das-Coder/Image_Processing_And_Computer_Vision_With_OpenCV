import numpy as np
import cv2
img=cv2.imread("MSD_WC_Six.jpg")
img=cv2.line(img,(0,0),(200,200),(154,92,424),5) #On increasing the thickness, the thickness of the line increases
cv2.imshow("Res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()