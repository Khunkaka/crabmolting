import cv2
from cv2 import LINE_4
img = cv2.imread("img/test2.jpg")
img = cv2.resize(img,[500,500])

def clickposition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = str(x)+","+str(y)
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
        cv2.imshow("Output",img)

cv2.imshow("Output",img)
cv2.setMouseCallback("Output",clickposition)
cv2.waitKey(0)
cv2.destroyAllWindows()