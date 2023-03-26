from tkinter import *

root = Tk()
root.title("PK's Calculator")
root.geometry("400x400")

result = ""
input_text = StringVar()

entry1 = Entry(root, justify=RIGHT).grid(row=0, column=0, columnspan=5)
btn1 = Button(root, text="1", width=5).grid(row=4, column=0)
btn2 = Button(root, text="2", width=5).grid(row=4, column=1)
btn3 = Button(root, text="3", width=5).grid(row=4, column=2)
btn4 = Button(root, text="4", width=5).grid(row=3, column=0)
btn5 = Button(root, text="5", width=5).grid(row=3, column=1)
btn6 = Button(root, text="6", width=5).grid(row=3, column=2)
btn7 = Button(root, text="7", width=5).grid(row=2, column=0)
btn8 = Button(root, text="8", width=5).grid(row=2, column=1)
btn9 = Button(root, text="9", width=5).grid(row=2, column=2)
btn0 = Button(root, text="0", width=12).grid(row=5, column=0, columnspan=2)
btnplus = Button(root, text="+", width=5).grid(row=4, column=3)
btnmi = Button(root, text="-", width=5).grid(row=3, column=3)
btndivi = Button(root, text="/", width=5).grid(row=1, column=3)
btntime = Button(root, text="x", width=5).grid(row=2, column=3)
btndeci = Button(root, text=".", width=5).grid(row=5, column=2)
btnenter = Button(root, text="=", width=5).grid(row=5, column=3)
btnc = Button(root, text="C", width=18).grid(row=1, column=0, columnspan=3)

root.mainloop()