from tkinter import *
from tkinter.messagebox import *

accounts = {"pokai": "kenny0828", "popo": "popo0828"}


def login():
    acct = entryID.get()
    if acct not in accounts:
        showwarning('Warning', "Your account is not exist")
    else:
        passwd = entryPW.get()
        if passwd == accounts[acct]:
            showinfo("Successfully login", "Welcome to PoPo system!!")
            clear()
            showImg(acct)
        else:
            showerror("Login fail", "Your password is not correct.\n"
                                    "Please check again!")


def clear():
    widgets = win.grid_slaves()
    for w in widgets:
        w.destroy()


def showImg(acct):
    img1 = PhotoImage(file="img/Python.png")
    label1 = Label(win, image=img1)
    label1.pack()
    win.mainloop()


win = Tk()
win.title("Login")
win.geometry("370x250")

img1 = PhotoImage(file="img/Python.png")

Label(win, image=img1).grid(row=0, column=0, columnspan=3)

Label(win, text=" User Name: ").grid(row=1)
Label(win, text=" Password : ").grid(row=2)

entryID = Entry(win, width=20)
entryPW = Entry(win, width=20, show="*")
entryID.grid(row=1, column=1)
entryPW.grid(row=2, column=1)

btnLogin = Button(win, text="Login", width=10, command=login)
btnLogin.grid(row=3, column=0, pady=10, padx=5)

btnExit = Button(win, text="Exit", width=10, command=win.destroy)
btnExit.grid(row=3, column=1, pady=10, padx=5)

win.mainloop()
