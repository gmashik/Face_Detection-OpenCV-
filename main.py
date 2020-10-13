import cv2
print(cv2.__version__)
import numpy as np
kernel=np.ones((5,5),np.uint8)
img=cv2.imread("F:\\OPenCV\\project1\\venv\\Resources\\lena.png")
img2gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blrimg=cv2.GaussianBlur(img,(7,7),0)
imgcanny=cv2.Canny(img,100,100)
dialimg=cv2.dilate(imgcanny,kernel,iterations=1)
erodedimg=cv2.erode(dialimg,kernel,iterations=1)
#cv2.imshow("My_output",img2gray)
cv2.imshow("My_output",blrimg)
cv2.imshow("My_output2",imgcanny)
cv2.imshow("My_output3",dialimg)
cv2.imshow("My_output4",erodedimg)
cv2.waitKey(0)

"""
img=cv2.imread("F:\\OPenCV\\project1\\venv\\Resources\\lena.png")
cv2.imshow("My_output",img)
cv2.waitKey(0)
#cv2.imshow("mat",img)
#cap=cv2.VideoCapture(0)
#cap.set(3,680)
#cap.set(4,480)
#cap.set(10,50)
"""
"""
while True:
  success, image = cap.read()
  cv2.imshow("mat",image)
  if cv2.waitKey(1) & 0xff==ord("q"):
    break
"""