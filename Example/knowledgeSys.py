from tkinter import Tk, Label, Button, simpledialog, messagebox, LEFT, RIGHT


def inputCountry():
    query_country = simpledialog.askstring('Country', '輸入查詢國家')
    if query_country in capitals:
        city = capitals[query_country]
        messagebox.showinfo('Answer', '%s的首都是%s' % (query_country, city))
    else:
        new_city = simpledialog.askstring('No Data', '請輸入%s的首都' % query_country)
        capitals[query_country] = new_city


root = Tk()
label = Label(root, text="世界各國首都專家系統")
label.pack()

capitals = {}

button1 = Button(root, text="查詢", command=inputCountry, width=10)
button1.pack(side=LEFT)
button2 = Button(root, text="離開", command=root.destroy, width=10)
button2.pack(side=RIGHT)

root.mainloop()
