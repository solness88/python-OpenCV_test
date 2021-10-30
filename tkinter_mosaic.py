import matplotlib.pyplot as plt
import cv2
import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.geometry("450x150")
window.title("AIモザイク")


#写真の中の顔を検出して自動でモザイクをかける処理
cascade_file= "cascade_classification.xml"
clas = cv2.CascadeClassifier(cascade_file)

def set_func(): 
    # ファイルダイアログメニューの設定
    typ = [("Image file","*.jpg")]
    file_path = filedialog.askopenfilename(filetypes = typ)
    input_box.delete(0, tk.END)
    input_box.insert(tk.END, file_path)

def run_func():
    img = cv2.imread(input_box.get())
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_list = clas.detectMultiScale(img_gray, minSize=(150,150))
    for x, y, w, h in face_list:
        #顔に四角の縁取りをする処理
        #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        #print("顔の座標(x,y,w,h):", x, y, w, h)
        #red=(0,0,255)
        #cv2.rectangle(img, (x,y), (x+w, y+h), red)

        #モザイク処理
        face= img[y:y+h, x:x+w]
        reduc = cv2.resize(face, (8,8))
        mosaic = cv2.resize(reduc,(w,h))
        img[y:y+h, x:x+w]=mosaic
        cv2.imwrite("Hiro_mosaic.jpg",img)

        #ステータスバーに完了メッセージ
        statusbar["text"] = "完了しました！"


run_button = tk.Button(window, text = "モザイク処理", command = run_func)
run_button.place(x = 160, y = 40)

set_button = tk.Button(window, text = "画像を選択", command = set_func)
set_button.place(x = 300, y = 7)

input_box = tk.Entry(width = 40)
input_box.place(x = 10, y = 10)

statusbar = tk.Label(window, text = "モザイクをかける画像を選択して下さい", bd = 1, relief = tk.SUNKEN, anchor = tk.W)
statusbar.pack(side = tk.BOTTOM, fill = tk.X)

window.mainloop()