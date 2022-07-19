import cv2
import numpy as np

#ข้อความ
def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)

#สติกเกอร์
def notifySticker(stickerID,stickerPackageID):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return _lineNotify(payload)

#รูปภาพ
def notifyPicture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload)

#ส่งแจ้งเตือน
def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'x8TJhJRg4Tl1zUSqkwOD0W1aVLZcShkyHzIyd1Ls2KJ'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)


img = cv2.imread("img/test2.jpg")
img = cv2.resize(img,[500,500])

up = [img[32:215,37:216],img[55:215,295:451],img[279:455,37:217],img[292:455,293:449]]
# up[0] = img[15:244,8:234]
# up[1] = img[15:244,274:474]
#A3 = img[55:160,421:567]

B1 = img[279:460,10:236]
B2 = img[278:460,274:468]
#B3 = img[268:390,414:559]
#C1 = img[447:546,52:160]
#C2 = img[442:544,229:354]
#C3 = img[446:544,412:525]
def processing(channel,fullimg):
    cv2.imshow("output",fullimg)
    for i in channel:
        #tag = str(channel)
        gray = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(3,3),0)
        thresh,result = cv2.threshold(blur,120,255,cv2.THRESH_BINARY_INV)
        dilation = cv2.dilate(result,None,iterations=3)

        contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        counter = 0
        for contour in contours:
            (x,y,w,h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour)<1500:
                continue
            cv2.rectangle(i,(x,y),(x+w,y+h),(0,255,0),2)
            counter+=1
            if counter == 2:
                #lineNotify('ปูลอกคราบกล่องที่ ' + str(channel.index(i) + 1))
                lineNotify("ปูลอกคราบกล่องที่ {box}".format(box=channel.index(i) + 1))
                #print('ปูลอกคราบกล่องที่ ' + str(channel.index(i) + 1))
                print("ปูลอกคราบกล่องที่ {box}".format(box=channel.index(i) + 1))
                #print('กล่องที่ ' + str(i))
                pass

        print(len(contours))
        print(counter)
        cv2.imshow("output",fullimg)
        cv2.waitKey(5000)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

processing(up,img)