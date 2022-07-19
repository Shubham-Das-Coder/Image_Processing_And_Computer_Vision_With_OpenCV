import numpy as np
import cv2
img=cv2.imread("MSD_WC_Six.jpg")
#Puttext accepts (img,text,starting,font,fontsize,colour,thickness,linetype)
img=cv2.putText(img,'MSD',(20,200),cv2.FONT_HERSHEY_COMPLEX,4,(0,125,255),10,cv2.LINE_AA) #Color format is in BGR
cv2.imshow("Res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()