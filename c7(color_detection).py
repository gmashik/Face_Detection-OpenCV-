import cv2
import numpy as np
cv2.namedWindow("TrackBars")
cv2.resize("TrackBars",640,240)
cv2.createTrackbar("Hue min","TrackBar",0,179)
img=cv2.imread("F:\\OPenCV\\project1\\venv\\Resources\\lambo.PNG")
imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("Original",img)
cv2.imshow("HSVIMG",imgHSV)
cv2.waitKey(0)