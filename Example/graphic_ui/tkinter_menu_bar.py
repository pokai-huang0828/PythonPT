import tkinter  # 匯入Tkinter模組

root = tkinter.Tk()

menu = tkinter.Menu(root)  # 產生選單

submenu = tkinter.Menu(menu, tearoff=0)  # 產生下拉選單
submenu.add_command(label="Open")  # 下拉選單中加入Open指令
submenu.add_command(label="Save")
submenu.add_command(label="Close")
menu.add_cascade(label="File", menu=submenu)  # 將下拉選單新增到選單中

submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label="Copy")
submenu.add_command(label="Paste")
submenu.add_separator()  # 向下拉選單中加入分隔符
submenu.add_command(label="Cut")
menu.add_cascade(label="Edit", menu=submenu)

submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label="About")
menu.add_cascade(label="Help", menu=submenu)

root.config(menu=menu)  # 設定視窗選單物件
root.mainloop()