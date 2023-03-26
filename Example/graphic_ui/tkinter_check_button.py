import tkinter  # 匯入Tkinter模組

root = tkinter.Tk()
root.title("Hello Tkinter")  # 設定視窗標題
root.geometry('280x150+650+100')
s1 = tkinter.IntVar()  # 使用IntVar產生整數變數用於複選元件
s1.set(0)  # 初始化變數值
check1 = tkinter.Checkbutton(root,  # 產生複選元件
                             variable=s1,  # 關聯的變數
                             text='薯條',  # 顯示的文字
                             onvalue=1,  # 被選擇時關聯變數的值(s1 = 1)
                             offvalue=0)  # 未選擇時關聯變數的值(s1 = 0)
check1.pack()
s2 = tkinter.IntVar()
s2.set(0)
check2 = tkinter.Checkbutton(root,
                             variable=s2,
                             text='咖啡',
                             onvalue=1,  # 被選擇時關聯變數的值(s2 = 1)
                             offvalue=0)  # 未選擇時關聯變數的值(s2 = 0)
check2.pack()
s3 = tkinter.IntVar()
s3.set(0)
check3 = tkinter.Checkbutton(root,
                             variable=s3,
                             text='蛋糕',
                             onvalue=1,  # 被選擇時關聯變數的值(s3 = 1)
                             offvalue=0)  # 未選擇時關聯變數的值(s3 = 0)
check3.pack()
root.mainloop()
print('附餐:', end=' ')
if s1.get() == 1:  # s1被選擇(s1 = 1)
    print("Fries", end=', ')
if s2.get() == 1:  # s2被選擇(s2 = 1)
    print("Coffee", end=', ')
if s3.get() == 1:  # s3被選擇(s3 = 1)
    print("Cake", end=', ')
