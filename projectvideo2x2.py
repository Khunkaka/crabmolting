from operator import index
import cv2
import numpy as np
import datetime
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

cap=cv2.VideoCapture(0)

def processing(cap):
    start_time = time.time()
    end_time = start_time

    while(cap.isOpened()) :
        ref,fullframe = cap.read()
        height, widght, color = fullframe.shape
        splitframe = [
        fullframe[:int(height/2), 0:int(widght/2)], 
        fullframe[:int(height/2), int(widght/2):], 
        fullframe[int(height/2):, 0:int(widght/2)], 
        fullframe[int(height/2):, int(widght/2):]
        ]
        for index, frame in enumerate(splitframe):
            print(index)
            roi=frame

            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            gray_blur=cv2.GaussianBlur(gray,(15,15),0)
            thresh=cv2.adaptiveThreshold(gray_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,1)
            kernel=np.ones((2,2),np.uint8)
            closing=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations=2)
            result_img=closing.copy()
            contours,hierachy=cv2.findContours(result_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            counter=0
            for contour in contours:
                (x,y,w,h) = cv2.boundingRect(contour)
                if cv2.contourArea(contour)<7000:
                    continue
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                '''area = cv2.contourArea(contour)
                if area < 500 :
                    continue
                ellipse = cv2.fitEllipse(cnt)
                cv2.ellipse(roi,ellipse,(0,255,0),2)'''
                counter+=1

                if counter == 2:
                    #print("{} {} {} {}".format(start_time,end_time,counter,time.time()-end_time))
                    while (time.time()-end_time) >= 10:
                        print("ok")
                        lineNotify("ลอกคราบ")
                        end_time = time.time()
                        break
                    break
            currentDate = str(datetime.datetime.now())
            cv2.putText(roi,"amount : " + str(counter),(10,60),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(roi,currentDate,(10,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.imshow("Show",fullframe)
            
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

    #cap.release()
    cv2.destroyAllWindows()

processing(cap)
#def processingvideo(video):
