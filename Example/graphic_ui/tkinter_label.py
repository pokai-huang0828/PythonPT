# 匯入 tkinter 模組
import tkinter

# Label 標籤元件：顯示文字或圖片內容

#  tkinter.Label(master=None, **kw)
#    master：父容器，所在的視窗物件
#    text：標籤中的文字，可以使用「\n」換行
#    image：指定標籤中的圖片，指向PhotoImage物件
#    width：指定標籤的寬度
#    height：指定標籤的高度
#    background（bg）：指定標籤的背景顏色
#    foreground（fg）：指定標籤的前景顏色

#  tkinter.Label(master=None, **kw)
#    font：指定標籤中文字的字型 (typeface, fontsize, style)
#    anchor：指定標籤中文字位置，tkinter.N/S/E/W/LEFT/RIGHT/CENTER
#    justify：指定標籤中多行文字對齊方式，tkinter.N/S/E/W/LEFT/RIGHT/CENTER

#  pack()：元件配置，預設於父容器中由上而下排列

#  destroy()：元件移除


root = tkinter.Tk()  # 建立主視窗物件 Tk
root.title("Hello Tkinter")  # 設定視窗標題

# geometry('width x height + x + y')
# width:視窗寬度, height:視窗高度
# 顯示視窗的位置 x:對應左上角x軸位置, y:對應左上角y軸位置
root.geometry('600x500+650+200')

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


img1 = tkinter.PhotoImage(file='img/Python.png')
label3 = tkinter.Label(root, image=img1)
label3.pack()

img2 = tkinter.PhotoImage(file='img/Tkinter.gif')
label4 = tkinter.Label(root, image=img2)
label4.pack()
label2.pack()

# 呼叫 mainloop() 進行訊息循環
# 等待處理視窗及其內部元件的事件
root.mainloop()
