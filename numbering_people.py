import cv2

#モザイクかけて保存する関数
def mosaic(img, mosaic_rate):
    w = img.shape[1]
    h = img.shape[0]

    #モザイク加工
    img = cv2.resize(img, (int(w * mosaic_rate), int(h * mosaic_rate)))
    img = cv2.resize(img, (w, h), interpolation = cv2.INTER_NEAREST)

    return img

#識別器を読み込む
cascade_file= cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
clas = cv2.CascadeClassifier(cascade_file)
cap = cv2.VideoCapture("movie.mp4")

num = 0
red = (0,0,255)
white = (255,255,255)

#１フレームずつモザイクをかける
while (cap.isOpened()):
    ret, frame = cap.read()
    
    #retがFalseの場合は終了
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #１フレーム（＝静止画）の顔をすべて検出して周囲の四角形の座標を取得
    face_list = clas.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3, minSize=(30,30))

    num = 0
    #モザイク処理
    #[四角の左上のx座標、四角の左上のy座標、幅、高さ]をそれぞれ変数x, y, w, hに代入
    for x, y, w, h in face_list:
       frame[y : y+h, x : x+w] = mosaic(frame[y : y + h, x : x + w], 0.05)
        
       num += 1
       cv2.rectangle(frame, pt1=(x,y), pt2=(x + w, y + h), color=red, thickness=5)

       cv2.rectangle(frame,
                      (x, y),
                      (x + 60, y - 60),
                      color = red,
                      thickness = -1
                     )    

       cv2.putText(frame,
                    text = str(num),
                    org = (x, y),
                    fontFace = cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale = 2.5,
                    color = white,
                    thickness = 10,
                    lineType = cv2.LINE_4)
        
       cv2.imshow("frame", frame)
       if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
