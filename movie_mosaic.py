import cv2

#モザイクかけて保存
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

#動画を保存
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
fps = 20.0
size = (640, 360)
writer = cv2.VideoWriter('./test2.mp4', fmt, fps, size)

#１フレームずつモザイクをかける
while (cap.isOpened()):
    ret, frame = cap.read()
    
    #retがFalseの場合は終了
    if not ret:
        break

    frame=cv2.resize(frame, size)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #１フレーム（＝静止画）の顔をすべて検出して周囲の四角形の座標を取得
    face_list = clas.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3, minSize=(30,30))

    #モザイク処理
    #[四角の左上のx座標、四角の左上のy座標、幅、高さ]をそれぞれ変数x, y, w, hに代入
    for x, y, w, h in face_list:
       frame[y : y+h, x : x+w] = mosaic(frame[y : y + h, x : x + w], 0.05)

    writer.write(frame)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

writer.release()
cap.release()
cv2.destroyAllWindows()
