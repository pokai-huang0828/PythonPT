import tkinter


def greet():  # 宣告greet函式
    name = entry.get()  # 取得entry輸入姓名 name
    label['text'] = "Hello, " + name + "!"  # label文字顯示 Hello, <name>!


def clear():  # 宣告greet函式
    entry.delete(0, tkinter.END)  # 刪除label文字


root = tkinter.Tk()
label = tkinter.Label(root, text="Hello, Tkinter!")
label.pack()
entry = tkinter.Entry(root, width=12)
entry.pack()
button1 = tkinter.Button(root, text="Submit",
                         command=greet)  # 按鍵按下時呼叫greet函式
button1.pack(side=tkinter.LEFT)
button2 = tkinter.Button(root, text="Cancel",
                         command=clear)  # 按鍵按下時呼叫clear函式
button2.pack(side=tkinter.RIGHT)
root.mainloop()
