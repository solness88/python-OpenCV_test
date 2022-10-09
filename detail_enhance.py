import cv2

img = cv2.imread('people.jpg')

detail_enhance = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)

cv2.imwrite('detail_enhance.jpg', detail_enhance)
