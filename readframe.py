import cv2
import time


cap=cv2.VideoCapture("video/crab.mp4")

while(cap.isOpened()) :
    ref,frame = cap.read()
    # for y in range(0,600,200):
    #     for x in range(0,600,200): 
    #         roi=frame[x:x+200,y:y+200]
    #         cv2.imshow("Show",roi)
    #         time.sleep(1)
    
    if cv2.waitKey(30) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()