#detect faces in the picture, then put circles aroud faces

import cv2

cascade_file= "cascade_classification.xml"
clas = cv2.CascadeClassifier(cascade_file)
img = cv2.imread("people.jpg")
face_list = clas.detectMultiScale(img, scaleFactor = 1.1, minSize=(30,30))
red = (0,0,255)
for x, y, w, h in face_list:
    circle_center = (int(x+w/2), int(y+h/2))
    circle_radius = int(w/2)
    cv2.circle(img, circle_center, circle_radius, red, 3)

cv2.imshow("photo_processed.jpg",img)
cv2.waitKey()

cv2.destroyAllWindows()