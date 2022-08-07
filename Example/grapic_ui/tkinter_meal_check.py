import tkinter

root = tkinter.Tk()
root.title("Meal Check")  # 設定視窗標題
root.geometry('350x280+650+100')
m = tkinter.StringVar()
m.set('N/A')

label = tkinter.Label(root,
                      text="主餐",
                      anchor=tkinter.CENTER,
                      width=50,
                      bg='black',
                      fg='white',
                      font=("Mono", 18)
                      )
label.pack()

radio1 = tkinter.Radiobutton(root,
                             variable=m,
                             value='Steak',
                             indicatoron=0,  # 將單選框繪製成按鈕型態
                             text='牛排')
radio1.pack()
radio2 = tkinter.Radiobutton(root,
                             variable=m,
                             value='Pasta',
                             indicatoron=0,
                             text='義大利麵')
radio2.pack()
radio3 = tkinter.Radiobutton(root,
                             variable=m,
                             value='Curry Rice',
                             indicatoron=0,
                             text='咖哩飯')
radio3.pack()
radio4 = tkinter.Radiobutton(root,
                             variable=m,
                             value='Hamburger',
                             indicatoron=0,
                             text='漢堡')
radio4.pack()


label2 = tkinter.Label(root,
                      text="附餐",
                      anchor=tkinter.CENTER,
                      width=50,
                      bg='black',
                      fg='white',
                      font=("Mono", 18)
                      )
label2.pack()

s1 = tkinter.StringVar()
s1.set('')
check1 = tkinter.Checkbutton(root,
                             text='薯條',
                             variable=s1,
                             indicatoron=0,
                             onvalue='Fries',
                             offvalue='')
check1.pack()
s2 = tkinter.StringVar()
s2.set('')
check2 = tkinter.Checkbutton(root,
                             text='可樂',
                             variable=s2,
                             indicatoron=0,
                             onvalue='Coke',
                             offvalue='')
check2.pack()
root.mainloop()
print("主餐:", m.get())
print("附餐:", s1.get(), s2.get())
