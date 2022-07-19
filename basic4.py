import cv2

img = cv2.imread("img/ปูดำ.png")
#img = cv2.resize(img,(600,600))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#thresh,result = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)

#contours,hierarchy = cv2.findContours(result,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(img,contours,-1,(0,255,0),2)
#for contour in contours:
#    (x,y,w,h) = cv2.boundingRect(contour)
#    if cv2.contourArea(contour)<5000:
#        continue
#    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


#print(len(contours))

cv2.imshow("output",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
