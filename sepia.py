import cv2
 
img = cv2.imread('profile-image.jpg')
 
img[:,:,(0)] = img[:,:,(0)] * 0.1
img[:,:,(1)] = img[:,:,(1)] * 0.7
img[:,:,(2)] = img[:,:,(2)]
 
cv2.imwrite("sepia.jpg",img) #別ウィンドウ"sepia"を開きimgを表示
#cv2.waitKey(0) #キー入力待ち
#cv2.destroyAllWindows() #ウインドウを閉じる
