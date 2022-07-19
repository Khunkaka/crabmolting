import cv2
import time

def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)

def notifySticker(stickerID,stickerPackageID):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return _lineNotify(payload)

def notifyPicture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload)

def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'x8TJhJRg4Tl1zUSqkwOD0W1aVLZcShkyHzIyd1Ls2KJ'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)
start_time = time.time()
end_time = start_time
cap = cv2.VideoCapture("0")
check , frame1 = cap.read()
check , frame2 = cap.read()
while True:
    
    if check == True:
        motiondiff = cv2.absdiff(frame1,frame2)
        gray = cv2.cvtColor(motiondiff,cv2.COLOR_BGR2GRAY)
        #blur = cv2.GaussianBlur(gray,(5,5),0)
        thresh,result = cv2.threshold(gray,10,255,cv2.THRESH_BINARY)
        dilation = cv2.dilate(result,None,iterations=5)
        open = cv2.morphologyEx(dilation,cv2.MORPH_OPEN,None,iterations=3)
        contours,hierarchy = cv2.findContours(open,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

        counter = 0
        for contour in contours:
            (x,y,w,h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour)<5000:
                continue
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
            counter+=1
            
            if counter == 2:
                print("{} {} {} {}".format(start_time,end_time,counter,time.time()-end_time))
                while (time.time()-end_time) >= 10:
                    print("ok")
                    lineNotify("ลอกคราบ")
                    end_time = time.time()
                    break
                break

                
        cv2.imshow("Output",frame1)
        frame1 = frame2
        check , frame2 = cap.read()
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()