import cv2

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

def insertimg(device):
    img = cv2.imread(device)
    img = cv2.resize(img,(600,600))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #ปรับคุณภาพภาพ
    blur = cv2.GaussianBlur(gray,(3,3),0)
    thresh,result = cv2.threshold(blur,180,255,cv2.THRESH_BINARY)
    dilation = cv2.dilate(result,None,iterations=3)

    contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    counter = 0
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour)<1800:
            continue
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        counter+=1
    lineNotify("{}".format(counter))

    print(len(contours))
    print(counter)
    
    cv2.imshow("output",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

insertimg("img/coin.jpg")

