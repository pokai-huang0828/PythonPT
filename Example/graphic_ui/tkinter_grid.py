import tkinter
root = tkinter.Tk()
root.title("Grid UI")  # 設定視窗標題
root.geometry('100x100+650+100')
btnN = tkinter.Button(root, text='北', width=5)
btnW = tkinter.Button(root, text='西', height=3)
btnS = tkinter.Button(root, text='南', width=5)
btnE = tkinter.Button(root, text='東', height=3)
btnC = tkinter.Button(root, text='中')

btnN.grid(row=0, column=0, columnspan=2)
btnW.grid(row=1, column=0, rowspan=2)
btnS.grid(row=2, column=1, columnspan=2)
btnE.grid(row=0, column=2, rowspan=2)
btnC.grid(row=1, column=1)
root.mainloop()
