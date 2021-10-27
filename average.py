import cv2
img = cv2.imread('picture.jpg')

#Average picture with blur()
def average(img):
    img_blur = cv2.blur(img, (17, 17))
    return img_blur

cv2.imshow("picture_averaged.jpg", average(img))
cv2.waitKey()
cv2.destroyAllWindows()