# Resize picture and show them

import cv2

image = cv2.imread('Hiro.jpg')
print(image)
down_width = 300
down_height = 200
down_points = (down_width, down_height)
print(down_points)
resized_down = cv2.resize(image, down_points, interpolation = cv2.INTER_LINEAR)

up_width = 600
up_height = 400
up_points = (up_width, up_height)
resized_up = cv2.resize(image, up_points, interpolation= cv2.INTER_LINEAR)

cv2.imshow('Resized down by defining height and width', resized_down)
cv2.waitKey()
cv2.imshow('Resized up by defining height and width', resized_up)
cv2.waitKey()

cv2.destroyAllWindows()