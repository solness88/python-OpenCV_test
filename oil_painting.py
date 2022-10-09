import cv2

img = cv2.imread('hiro.jpg')
oil_painting = cv2.xphoto.oilPainting(img, 3, 1)

cv2.imwrite('oil_painting.jpg', oil_painting)
