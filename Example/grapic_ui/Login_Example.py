from tkinter import *
from tkinter.messagebox import *

accounts = {"pokai": "kenny0828", "popo": "popo0828"}

def login():
    acct = entryID.get()
    if acct not in accounts:
        showwarning('Warning', "Your account is not exsit")

win = Tk()
win.title("Login")

Label(win, text=" User Name: ").grid(row=0)
Label(win, text=" Password : ").grid(row=1)

entryID = Entry(win, width=20)
entryPW = Entry(win, width=20, show="*")
entryID.grid(row=0, column=1)
entryPW.grid(row=1, column=1)

btnLogin = Button(win, text="Login", width=10)
btnLogin.grid(row=2, column=0, pady=10, padx=5)

btnExit = Button(win, text="Exit", width=10)
btnExit.grid(row=2, column=1, pady=10, padx=5)

win.mainloop()