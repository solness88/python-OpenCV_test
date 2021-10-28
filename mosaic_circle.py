
import cv2
import numpy as np

cascade_file= "cascade_classification.xml"
clas = cv2.CascadeClassifier(cascade_file)
img = cv2.imread("hiromaki.jpg")
face_list = clas.detectMultiScale(img, scaleFactor = 1.1, minSize=(30,30))
mask = np.zeros(img.shape, dtype=np.uint8)
white = (255,255,255)

for x, y, w, h in face_list:
    circle_center = (int(x+w/2), int(y+h/2))
    circle_radius = int(w/2)
    cv2.circle(mask, circle_center, circle_radius, white, -1)
    ROI = cv2.bitwise_and(img, mask)

    #face= img[y:y+h, x:x+w]
    #img_blur= cv2.blur(face,(55,55))
    #img[y:y+h, x:x+w]=img_blur

cv2.imshow("aaa.jpg", ROI)
cv2.waitKey()