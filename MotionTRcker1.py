import cv2

cap = cv2.VideoCapture("video/crabfromfarm3.mp4")
check , frame1 = cap.read()
check , frame2 = cap.read()
while True:
    
    if check == True:
        motiondiff = cv2.absdiff(frame1,frame2)
        gray = cv2.cvtColor(motiondiff,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        thresh,result = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
        dilation = cv2.dilate(result,None,iterations=3)
        contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

        for contour in contours:
            (x,y,w,h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour)<5000:
                continue
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.imshow("Output",frame1)
        frame1 = frame2
        check , frame2 = cap.read()
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()