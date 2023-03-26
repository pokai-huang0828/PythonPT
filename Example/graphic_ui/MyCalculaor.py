from tkinter import *

root = Tk()

root.title("PK's Calculator")
root.geometry("350x350")



# 輸入框
entry1 = Entry(root, justify=RIGHT, font=('Arial', 16))
entry1.grid(row=0, column=0, columnspan=4, pady=10)

# 運算功能
def show(s):
    entry1.insert(END, s)

def cls():
    entry1.delete(0, END)

def delete():
    entry1.delete(len(entry1.get())-1, END)

def pm():
    s = entry1.get()
    if len(s) > 0 and s[0] == '-':
        entry1.delete(0)
    else:
        entry1.insert(0, '-')


def calc(): 
    s = entry1.get()
    cls()
    try:
        entry1.insert(0, str(eval(s)))
    except ZeroDivisionError:
        entry1.insert(0, "Can't divide by 0")
    except:
        entry1.insert(0, "Error")

# 加入按鈕
button_style = {'font': ('Arial', 16), 'width': 5,
                'height': 2, 'bd': 3, 'bg': 'lightgray', 'fg': 'black'}

btn7 = Button(root, text='7', **button_style, command=lambda: show('7'))
btn8 = Button(root, text='8', **button_style, command=lambda: show('8'))
btn9 = Button(root, text='9', **button_style, command=lambda: show('9'))
btnd = Button(root, text='/', **button_style, command=lambda: show('/'))

btn4 = Button(root, text='4', **button_style, command=lambda: show('4'))
btn5 = Button(root, text='5', **button_style, command=lambda: show('5'))
btn6 = Button(root, text='6', **button_style, command=lambda: show('6'))
btnm = Button(root, text='*', **button_style, command=lambda: show('*'))

btn1 = Button(root, text='1', **button_style, command=lambda: show('1'))
btn2 = Button(root, text='2', **button_style, command=lambda: show('2'))
btn3 = Button(root, text='3', **button_style, command=lambda: show('3'))
btns = Button(root, text='-', **button_style, command=lambda: show('-'))

btn0 = Button(root, text='0', **button_style, command=lambda: show('0'))
btnp = Button(root, text='.', **button_style, command=lambda: show('.'))
btnpm = Button(root, text='+/-', **button_style, command=pm)
btna = Button(root, text='+', **button_style, command=lambda: show('+'))

btnc = Button(root, text='C', **button_style, command=cls)
btndel = Button(root, text='Del', **button_style, command=delete)
btne = Button(root, text='=', **button_style, command=calc)

# 按鈕排列
btn7.grid(row=1, column=0, padx=2, pady=2)
btn8.grid(row=1, column=1, padx=2, pady=2)
btn9.grid(row=1, column=2, padx=2, pady=2)
btnd.grid(row=1, column=3, padx=2, pady=2)

btn4.grid(row=2, column=0, padx=2, pady=2)
btn5.grid(row=2, column=1, padx=2, pady=2)
btn6.grid(row=2, column=2, padx=2, pady=2)
btnm.grid(row=2, column=3, padx=2, pady=2)

btn1.grid(row=3, column=0, padx=2, pady=2)
btn2.grid(row=3, column=1, padx=2, pady=2)
btn3.grid(row=3, column=2, padx=2, pady=2)
btns.grid(row=3, column=3, padx=2, pady=2)

btn0.grid(row=4, column=0, padx=2, pady=2)
btnp.grid(row=4, column=1, padx=2, pady=2)
btnpm.grid(row=4, column=2, padx=2, pady=2)
btna.grid(row=4, column=3, padx=2, pady=2)

btnc.grid(row=5, column=0, padx=2, pady=2)
btndel.grid(row=5, column=1, padx=2, pady=2)
btne.grid(row=5, column=2, padx=2, pady=2, columnspan=2)

root.mainloop()
