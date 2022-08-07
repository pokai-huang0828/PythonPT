import tkinter

root = tkinter.Tk()
root.title("Hello Tkinter")  # 設定視窗標題
root.geometry('280x150+650+100')
m = tkinter.StringVar()  # 使用StringVar產生字串變數用於單選元件
m.set('N/A')  # 初始化變數值
radio1 = tkinter.Radiobutton(root,  # 產生單選元件
                             variable=m,  # 關聯的變數
                             value='Steak',  # 被選擇時關聯變數的值(m = 'Steak')
                             text='牛排')  # 顯示的文字
radio1.pack()
radio2 = tkinter.Radiobutton(root,
                             variable=m,
                             value='Pasta',  # 被選擇時關聯變數的值(m = 'Pasta')
                             text='義大利麵')
radio2.pack()
radio3 = tkinter.Radiobutton(root,
                             variable=m,
                             value='Curry Rice',  # 被選擇時關聯變數的值(m = 'Curry Rice')
                             text='咖哩飯')
radio3.pack()
radio4 = tkinter.Radiobutton(root,
                             variable=m,
                             value='Hamburger',  # 被選擇時關聯變數的值(m = 'Hamburger')
                             text='漢堡')
radio4.pack()
root.mainloop()
print("主菜:", m.get())  # 取出m的值
