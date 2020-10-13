import cv2
faseCascade=cv2.CascadeClassifier("F:\\OPenCV\\project1\\venv\\Resources\\haarcascade_frontalface_default.xml")
img=cv2.imread("F:\\OPenCV\\project1\\venv\\Resources\\lena.png")
imgGray=cv2.cvtColor(img,cv2.COLOR_RGBA2GRAY)
faces=faseCascade.detectMultiScale(imgGray,1.1,4)
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow("Results",img)
cv2.waitKey(0)