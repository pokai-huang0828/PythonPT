import tkinter  # 匯入Tkinter模組
import tkinter.simpledialog  # 匯入tkSimpleDialog模組


def InStr():  # 按鈕事件處理函數
    r = tkinter.simpledialog.askstring('SimpleDialog', '輸入字串',  # 建立字串輸入交談視窗並指定提示字元
                                       initialvalue='Tkinter')  # 指定起始化文字
    print(r)  # 輸出傳回值


def InInt():  # 按鈕事件處理函數
    r = tkinter.simpledialog.askinteger('SimpleDialog', '輸入整數')  # 建立整數輸入交談視窗
    print(r)


def InFlo():  # 按鈕事件處理函數
    r = tkinter.simpledialog.askfloat('SimpleDialog', '輸入浮點數')  # 建立浮點數輸入交談視窗
    print(r)


root = tkinter.Tk()
button1 = tkinter.Button(root, text='輸入字串對話框',  # 建立按鈕
                         command=InStr)  # 指定按鈕事件處理函數
button1.pack(side='left')
button2 = tkinter.Button(root, text='輸入整數對話框',
                         command=InInt)  # 指定按鈕事件處理函數
button2.pack(side='left')
button2 = tkinter.Button(root, text='輸入浮點數對話框',
                         command=InFlo)  # 指定按鈕事件處理函數
button2.pack(side='left')
root.mainloop()  # 進入訊息循環
