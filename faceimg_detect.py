import cv2
import numpy
img = cv2.imread("img/vanderB.jpg")
img = cv2.resize(img,(600,600))

#อ่านไฟล์ classifier
face_cascade = cv2.CascadeClassifier("detect/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("detect/haarcascade_eye_tree_eyeglasses.xml")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#จำแนกใบหน้า
face_scaleFacter = 1.1
face_minNeighbor = 4
eye_scaleFacter = 1.1
eye_minNeighbor = 1


face_detect = face_cascade.detectMultiScale(gray_img,face_scaleFacter,face_minNeighbor)
eye_detect = eye_cascade.detectMultiScale(gray_img,eye_scaleFacter,eye_minNeighbor)

#แสดงตำแน่งใบหน้า
for (x,y,w,h) in face_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=5)
    for (ex,ey,ew,eh) in eye_detect:
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,0,0),thickness=5)


cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()