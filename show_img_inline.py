import matplotlib.pyplot as plt
import numpy as np
import cv2
%matplotlib inline

cascade_file= cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
clas = cv2.CascadeClassifier(cascade_file)
img = cv2.imread("people.jpg")
face_list = clas.detectMultiScale(img, scaleFactor = 1.1, minSize=(30,30))
num = 1

for x, y, w, h in face_list:
    red=(0,0,255)
    cv2.rectangle(img, pt1=(x,y), pt2=(x+w, y+h), color=red, thickness=5)
    
    cv2.putText(img,
                text = str(num),
                org = (x, y),
                fontFace = cv2.FONT_HERSHEY_SIMPLEX,
                fontScale = 3.0,
                color = (0, 0, 255),
                thickness = 7,
                lineType = cv2.LINE_4)
    num += 1

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
