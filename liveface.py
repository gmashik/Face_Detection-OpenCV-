import cv2
faseCascade=cv2.CascadeClassifier("F:\\OPenCV\\project1\\venv\\Resources\\haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
cap.set(3,680)
cap.set(4,480)
cap.set(10,150)

while True:
  success, image = cap.read()
  imgGray=cv2.cvtColor(image,cv2.COLOR_RGBA2GRAY)
  faces = faseCascade.detectMultiScale(imgGray, 1.1, 4)
  for (x, y, w, h) in faces:
      if w*h>40000:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(image,"Face detected",(x+w,y+h),
                    cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),2)

  cv2.imshow("My Face Detector",image)
  if cv2.waitKey(1) & 0xff==ord("q"):
    break