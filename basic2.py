import cv2
import datetime
cap = cv2.VideoCapture("video/crabfromfarm3.mp4")

while (cap.isOpened()):
    check , frame = cap.read()[1]
    frame = cv2.flip(frame,1)
    cropu1 = frame[0:200,0:200]
   
    if check == True:
        currentDate = str(datetime.datetime.now())
        cv2.putText(frame,currentDate,(90,20),1,1,(265,265,265),1)
        cv2.imshow("Output",cropu1)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()  