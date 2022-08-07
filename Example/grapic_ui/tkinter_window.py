# 匯入 tkinter 模組
import tkinter

tk = tkinter.Tk()  # 建立主視窗物件 Tk
tk.title("Hello Tkinter")  # 設定視窗標題

# geometry('width x height + x + y')
# width:視窗寬度, height:視窗高度
# 顯示視窗的位置 x:對應左上角x軸位置, y:對應左上角y軸位置
tk.geometry('600x500+650+200')

label = tkinter.Label(tk, text="This is a test text.")
label.pack()

# 呼叫 mainloop() 進行訊息循環
# 等待處理視窗及其內部元件的事件
tk.mainloop()