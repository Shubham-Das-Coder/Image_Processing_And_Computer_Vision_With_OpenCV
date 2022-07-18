import numpy as np
import cv2
img=cv2.imread("MSD_WC_Six.jpg")
img=cv2.rectangle(img,(384,10),(510,128),(128,0,225),-1) #If we make thickness -1, then the rectangle gets filled with the colour
cv2.imshow("Res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()