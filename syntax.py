import cv2
import numpy
back =  numpy.zeros([400,400,3])
img = cv2.imread("elephant.jpg")
imgresize = cv2.resize(img,(1000,700))

point = []

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(back,(x,y),10,(0,0,255),4)
        point.append((x,y))
        if len(point)>=2:
            cv2.line(back,point[-2],point[-1],(0,255,0),5)
            print(point)
        cv2.imshow("Output",back)
   

cv2.imshow("Output",back)
cv2.setMouseCallback("Output",clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()
