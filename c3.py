import cv2
import numpy as np
img=cv2.imread("F:\\OPenCV\\project1\\venv\\Resources\\lambo.png")
print(img.shape)
imgresize=cv2.resize(img,(300,200))
cropped=img[0:200,200:500]
cv2.imshow("Image",img)
cv2.imshow("reImage",imgresize)
cv2.imshow("cropImage",cropped)
cv2.waitKey(0)