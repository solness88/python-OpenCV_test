import cv2
img = cv2.imread('bridge.jpg')
res = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
cv2.imwrite('bridge.jpg', res)
