import tkinter
#  Entry 輸入元件：單行文字輸入
#    tkinter.Entry(master=None, **kw)
#        master：父容器，所在的視窗物件
#        show：輸入後顯示的字元，一般使用「*」表示密碼輸入
#        font：指定標籤中文字的字型 (typeface, fontsize, style)
#        width：輸入元件的寬度
#        background（bg）：輸入元件的背景顏色
#        foreground（fg）：輸入元件的前景顏色
#    tkinter.Entry(master=None, **kw)
#        selectbackground：文字選取後的背景顏色
#        selectforeground：文字選取後的前景顏色
#  Text 輸入元件：多行文字輸入
#    tkinter.Text(master=None, **kw)
#        屬性與 Entry 相同  height：輸入元件的高度
#  get()：取得輸入文字

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


img1 = tkinter.PhotoImage(file='img/Python.png')
label3 = tkinter.Label(root, image=img1)
label3.pack()

img2 = tkinter.PhotoImage(file='img/Tkinter.gif')
label4 = tkinter.Label(root, image=img2)
label4.pack()

entry1 = tkinter.Entry(root,  # 產生單行文字框元件
                       width=30)  # 文字框寬度設為30
entry1.pack()  # 將文字框新增到視窗中
entry2 = tkinter.Entry(root,
                       show='*')  # 文字框輸入的字元顯示為“*”
entry2.pack()
entry3 = tkinter.Entry(root,
                       bg='red',  # 文字框的背景色設為紅色
                       fg='blue')  # 文字框的前景色設為藍色
entry3.pack()
entry4 = tkinter.Entry(root,
                       selectbackground='red',  # 選取文字的背景色設為紅色
                       selectforeground='gray')  # 選取文字的前景色設為灰色
entry4.pack()
entry5 = tkinter.Entry(root,
                       state=tkinter.DISABLED)  # 將文字框設定為禁用
entry5.pack()
edit1 = tkinter.Text(root,  # 產生多行文字框元件
                     width=30,  # 多行文字框寬度
                     height=10)  # 多行文字框高度
edit1.pack()

label2.pack()

root.mainloop()
