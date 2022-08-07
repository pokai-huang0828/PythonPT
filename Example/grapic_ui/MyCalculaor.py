from tkinter import *

root = Tk()

root.title("PK's Calculator")
root.geometry("200x150")


def show(s):
    entry1.insert(END, s)


def cls():
    entry1.delete(0, END)


def calc():
    s = entry1.get()
    cls()
    entry1.insert(0, str(eval(s)))


entry1 = Entry(root, justify=RIGHT, width=20)
btn7 = Button(root, text='7', width=5, command=lambda: show('7'))
btn8 = Button(root, text='8', width=5, command=lambda: show('8'))
btn9 = Button(root, text='9', width=5, command=lambda: show('9'))
btnd = Button(root, text='/', width=5, command=lambda: show('/'))
btn4 = Button(root, text='4', width=5, command=lambda: show('4'))
btn5 = Button(root, text='5', width=5, command=lambda: show('5'))
btn6 = Button(root, text='6', width=5, command=lambda: show('6'))
btnm = Button(root, text='*', width=5, command=lambda: show('*'))
btn1 = Button(root, text='1', width=5, command=lambda: show('1'))
btn2 = Button(root, text='2', width=5, command=lambda: show('2'))
btn3 = Button(root, text='3', width=5, command=lambda: show('3'))
btns = Button(root, text='-', width=5, command=lambda: show('-'))
btn0 = Button(root, text='0', width=5, command=lambda: show('0'))
btnc = Button(root, text='C', width=5, command=cls)
btne = Button(root, text='=', width=5, command=calc)
btna = Button(root, text='+', width=5, command=lambda: show('+'))

entry1.grid(row=0, column=0, columnspan=4)
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btnd.grid(row=1, column=3)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btnm.grid(row=2, column=3)
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btns.grid(row=3, column=3)
btn0.grid(row=4, column=0)
btnc.grid(row=4, column=1)
btne.grid(row=4, column=2)
btna.grid(row=4, column=3)

root.mainloop()
