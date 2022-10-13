import cv2
import numpy as np

gamma = 1.5

img = cv2.imread("hiro.jpg")

gamma_cvt = np.zeros((256,1),dtype = 'uint8')
for i in range(256):
    gamma_cvt[i][0] = 255*(float(i)/255)**(1.0/gamma)
img_gamma = cv2.LUT(img,gamma_cvt)

#cv2.imwrite("aaa.jpg",img)
cv2.imwrite("hirohiro.jpg",img_gamma)


