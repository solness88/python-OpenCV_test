#mosaic and defocus picture, then show them on the screen

import cv2

img = cv2.imread('photo.jpg')

def mosaic(img, ratio):
    small = cv2.resize(img, None, fx=ratio, fy=ratio)
    return cv2.resize(small, img.shape[:2][::-1])

def average(src, ratio = 0.5):
    dst = cv2.GaussianBlur(src, (55, 55),0)
    return dst

cv2.imshow('photo_mosaic.jpg', mosaic(img,ratio=0.1))
cv2.waitKey()

cv2.imshow('opencv_mosaic_005.jpg', average(img))
cv2.waitKey()

cv2.destroyAllWindows()