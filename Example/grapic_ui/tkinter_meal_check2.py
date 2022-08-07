import tkinter
import tkinter.messagebox


def getOrder():
    mainDish = m.get()
    sideDish = s1.get() + s2.get()
    if mainDish == 'N/A' or sideDish == '':
        tkinter.messagebox.showwarning('警告訊息', '請點一個主餐及至少一個附餐')
    else:
        order = f"主餐: {mainDish}\n附餐: {sideDish}"
        tkinter.messagebox.showinfo("餐點資訊", order)


root = tkinter.Tk()
m = tkinter.StringVar()
m.set('N/A')
radio1 = tkinter.Radiobutton(root, variable=m, value='Steak', text='牛排')
radio1.grid(row=0, column=0, columnspan=2)
radio2 = tkinter.Radiobutton(root, variable=m, value='Pasta', text='義大利麵')
radio2.grid(row=1, column=0, columnspan=2)
radio3 = tkinter.Radiobutton(root, variable=m, value='Curry Rice', text='咖哩飯')
radio3.grid(row=2, column=0, columnspan=2)
radio4 = tkinter.Radiobutton(root, variable=m, value='Hamburger', text='漢堡')
radio4.grid(row=3, column=0, columnspan=2)

s1 = tkinter.StringVar()
s1.set('')
check1 = tkinter.Checkbutton(root, text='薯條', variable=s1,
                             onvalue='Fries ', offvalue='')
check1.grid(row=4, column=0)

s2 = tkinter.StringVar()
s2.set('')
check2 = tkinter.Checkbutton(root, text='可樂', variable=s2,
                             onvalue='Coke ', offvalue='')
check2.grid(row=4, column=1)

btn = tkinter.Button(root, text='送出', command=getOrder)
btn.grid(row=5, column=0, columnspan=2)
root.mainloop()
