import cv2

cap = cv2.VideoCapture(1)

face_cascade = cv2.CascadeClassifier("detect/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("detect/haarcascade_eye_tree_eyeglasses.xml")

while True:
    check , frame = cap.read()
    if check == True:
        gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        face_scaleFacter = 1.1
        face_minNeighbor = 4
        eye_scaleFacter = 1.1
        eye_minNeighbor = 1


        face_detect = face_cascade.detectMultiScale(gray_img,face_scaleFacter,face_minNeighbor)
        eye_detect = eye_cascade.detectMultiScale(gray_img,eye_scaleFacter,eye_minNeighbor)

        for (x,y,w,h) in face_detect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=5)
            #for (ex,ey,ew,eh) in eye_detect:
                #cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(255,0,0),thickness=5)
        
        cv2.imshow("Output",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
