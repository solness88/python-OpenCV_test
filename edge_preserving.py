import cv2

img = cv2.imread('hiro.jpg')
edge_preserving = cv2.edgePreservingFilter(img, flags=1, sigma_s=70, sigma_r=0.6)

cv2.imwrite('edge_preserving.jpg', edge_preserving)
