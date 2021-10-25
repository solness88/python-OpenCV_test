#detect faces in the picture, then put frames aroud faces

import cv2
 
cascade_file= "cascade_classification.xml"
clas = cv2.CascadeClassifier(cascade_file)
img = cv2.imread("photo.jpg")
face_list = clas.detectMultiScale(img, scaleFactor = 1.1, minSize=(30,30))

for x, y, w, h in face_list:
    red=(0,0,255)
    cv2.rectangle(img, pt1=(x,y), pt2=(x+w, y+h), color=red, thickness=5)

cv2.imshow("Hiro_mosaic.jpg",img)
cv2.waitKey()

cv2.destroyAllWindows()