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

lineNotify('ทดสอบการแจ้งเตือน')
