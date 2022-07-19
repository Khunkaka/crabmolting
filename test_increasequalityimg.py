import cv2
import matplotlib.pyplot as plt
'''
def display(value):
    pass

cv2.namedWindow("Output")
cv2.createTrackbar("value","Output",0,255,display)

while True:
    img = cv2.imread("night_vision.jpg",0)
    gray = cv2.resize(img, (1000,600))
    thres_value = cv2.getTrackbarPos("value","Output")
    thresh,result = cv2.threshold(gray,thres_value,255,cv2.THRESH_BINARY)
    

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    cv2.imshow("output",result)



#cv2.imshow("output",result)
#images = [img,gray,result]
#title = ["original","gray","thresh"]


for i in range(len(images)):
    plt.imshow(images[i])
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()


#cv2.waitKey(0)
cv2.destroyAllWindows()
'''
img = cv2.imread("resize/blue-crab-500x500.jpg",0)
gray = cv2.resize(img, (1000,600))
thresh,th1 = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,17,1)
th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,1)
cv2.imshow("thresh",th1)
cv2.imshow("mean",th2)
cv2.imshow("gaussian",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
