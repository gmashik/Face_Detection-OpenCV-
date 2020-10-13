import cv2
import numpy as np
img=np.zeros((515,515,3),np.uint8)
#img[:]=255,0,0
cv2.line(img,(0,0),(515,515),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),3)#cv2.FILLED)
cv2.circle(img,(300,300),30,(255,255,45),4)
cv2.putText(img,"Hello OpenCV",(300,100),cv2.FONT_HERSHEY_PLAIN,1,(150,0,0),3)
cv2.imshow("Image",img)
cv2.waitKey(0)