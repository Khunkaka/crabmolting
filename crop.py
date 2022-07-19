import cv2
img = cv2.imread("img/re3x3.jpg")
cropped = img[66:166,26:157]

cv2.imshow("Output",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()