import tkinter

#  Button按鈕元件：
#    tkinter.Button(master=None, **kw)
#        text / image ：按鈕上顯示的文字 /圖片
#        width / height ：按鈕的寬度/高度
#        anchor：按鈕上文字的位置
#        background（bg）/ foreground（fg）：按鈕的背景/前景顏色
#        borderwidth（bd）按鈕邊框的寬度
#        font：按鈕上文字的字型
#        cursor：滑鼠移動到按鈕上的指標樣式
#        state：按鈕的狀態tkinter.DISABLED
#        command：指定按鈕訊息的回呼函數

root = tkinter.Tk()  # 建立主視窗物件 Tk
root.title("Hello Tkinter")  # 設定視窗標題
root.geometry('600x800+650+100')

label = tkinter.Label(root,
                      text="Hello Visitor :)",
                      anchor=tkinter.CENTER,
                      width=50,
                      height=5,
                      bg='black',
                      fg='white',
                      font=("Mono", 28)
                      )
label.pack()

label2 = tkinter.Label(root,
                       text="Python GUI\nPoKai Huang",
                       anchor=tkinter.S,
                       width=30,
                       )


button1 = tkinter.Button(root,
                         anchor=tkinter.W,  # 指定文字對齊模式
                         text='Submit',  # 按鈕上的文字
                         width=10,  # 按鈕的寬度設為10個字元
                         height=2)  # 按鈕的高度設為2行字元
button1.pack()  # 將按鈕新增到視窗
button2 = tkinter.Button(root,
                         text='Delete',
                         bg='Green',  # 按鈕的背景為綠色
                         fg='Red')  # 按鈕的前景文字為紅色
button2.pack()
button3 = tkinter.Button(root,
                         text='Cancel',
                         bd=3,  # 按鈕邊框寬度
                         font=("Arial", 18))  # 文字字型
button3.pack()

#img4 = tkinter.PhotoImage(file='Images/Python.png')
#button4 = tkinter.Button(root, image=img4)
#button4.pack()

label2.pack()

root.mainloop()