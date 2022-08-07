import tkinter

root = tkinter.Tk()
root.title("Tkinter UI")  # 設定視窗標題
root.geometry('250x80+650+100')


def greet():  # 宣告greet函式
    name = entry.get()  # 取得entry輸入姓名 name
    label['text'] = "Hello, " + name + "!"  # label文字顯示 Hello, <name>!


def clear():  # 宣告greet函式
    entry.delete(0, tkinter.END)  # 刪除label文字


label = tkinter.Label(root, text="Hello, Tkinter!")
label.pack()
entry = tkinter.Entry(root, width=12)
entry.pack()

button1 = tkinter.Button(root, text="Submit", command=greet)
# 按鍵按下時呼叫greet函式
button1.pack(side=tkinter.LEFT)  # 將button1靠左新增到root主視窗
button2 = tkinter.Button(root, text="Cancel", command=clear)
# 按鍵按下時呼叫clear函式
button2.pack(side=tkinter.RIGHT)  # 將button2靠右新增到root主視窗
root.mainloop()
