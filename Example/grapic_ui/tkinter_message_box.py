import tkinter
import tkinter.messagebox  # 匯入tkMessageBox模組


def cmd1():
    tkinter.messagebox.askokcancel('Ttile', 'Message')


def cmd2():
    tkinter.messagebox.askquestion('Ttile', 'Message')


def cmd3():
    tkinter.messagebox.askyesno('Ttile', 'Message')


def cmd4():
    tkinter.messagebox.showerror('Ttile', 'Message')


def cmd5():
    tkinter.messagebox.showinfo('Ttile', 'Message')


def cmd6():
    tkinter.messagebox.showwarning('Ttile', 'Message')


root = tkinter.Tk()
btn1 = tkinter.Button(root, text='askokcancel', width=12, command=cmd1)
btn1.grid(row=0, column=0)
btn2 = tkinter.Button(root, text='askquestion', width=12, command=cmd2)
btn2.grid(row=0, column=1)
btn3 = tkinter.Button(root, text='askyesno', width=12, command=cmd3)
btn3.grid(row=0, column=2)
btn4 = tkinter.Button(root, text='showerror', width=12, command=cmd4)
btn4.grid(row=1, column=0)
btn5 = tkinter.Button(root, text='showinfo', width=12, command=cmd5)
btn5.grid(row=1, column=1)
btn6 = tkinter.Button(root, text='showwarning', width=12, command=cmd6)
btn6.grid(row=1, column=2)
root.mainloop()
