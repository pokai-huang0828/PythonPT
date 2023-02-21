from logging import root
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import sqlite3

conn = sqlite3.connect('warehouse.db')
conn.execute("CREATE TABLE IF NOT EXISTS items (name TEXT, quantity INTEGER, price REAL)")
conn.close()

class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def insert(self):
        conn = sqlite3.connect('warehouse.db')
        c = conn.cursor()
        c.execute("INSERT INTO items (name, quantity, price) VALUES (?, ?, ?)",
                  (self.name, self.quantity, self.price))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect('warehouse.db')
        c = conn.cursor()
        c.execute("UPDATE items SET quantity=?, price=? WHERE name=?", (self.quantity, self.price, self.name))
        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.connect('warehouse.db')
        c = conn.cursor()
        c.execute("DELETE FROM items WHERE name=?", (self.name,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_items():
        conn = sqlite3.connect('warehouse.db')
        c = conn.cursor()
        c.execute("SELECT * FROM items")
        items = c.fetchall()
        conn.close()
        return items
        
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.configure(bg = "white")
        self.master.title("倉儲管理系統")
        self.master.geometry("600x400+250+250")
        self.create_widgets()

    def create_widgets(self):
        self.label_name = tk.Label(self.master, text="商品名稱", bg = "white", fg = "black")
        self.label_name.grid(row=0, column=0)

        self.entry_name = tk.Entry(self.master, bg = "white", fg = "black")
        self.entry_name.grid(row=0, column=1)

        self.label_quantity = tk.Label(self.master, text="商品數量", bg = "white", fg = "black")
        self.label_quantity.grid(row=1, column=0)

        self.entry_quantity = tk.Entry(self.master, bg = "white", fg = "black")
        self.entry_quantity.grid(row=1, column=1)

        self.label_price = tk.Label(self.master, text="商品價格", bg = "white", fg = "black")
        self.label_price.grid(row=2, column=0)

        self.entry_price = tk.Entry(self.master, bg = "white", fg = "black")
        self.entry_price.grid(row=2, column=1)

        self.button_add = tk.Button(self.master, text="新增", command=self.add_item, bg = "white", fg = "black")
        self.button_add.grid(row=3, column=0)

        self.button_remove = tk.Button(self.master, text="刪除", command=self.remove_item, bg = "white", fg = "black")
        self.button_remove.grid(row=3, column=1)

        self.button_update = tk.Button(self.master, text="修改", command=self.update_item, bg = "white", fg = "black")
        self.button_update.grid(row=3, column=2)

        self.listbox_items = tk.Listbox(self.master, bg = "white", fg = "black", width=50, height=15, selectmode=tk.SINGLE)
        self.listbox_items.grid(row=4, column=0, columnspan=5, rowspan=5, padx=10, pady=10)

        self.load_items()

    def load_items(self):
        self.listbox_items.delete(0, tk.END)
        Items = Item.get_all_items()

        for item in self.Items:
            self.listbox.insert(tk.END, item)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

    def add_item(self):
        name = self.entry_name.get()
        quantity = int(self.entry_quantity.get())
        price = float(self.entry_price.get())

        item = Item(name, quantity, price)
        item.insert()

        self.load_items()

    def remove_item(self):
        index = self.listbox_items.curselection()
        if index:
            name = self.listbox_items.get(index).split()[0]
            
            item = Item(name, 0, 0)
            item.delete()
            
            self.load_items()
            
    def update_item(self):
        index = self.listbox_items.curselection()
        if index:
            name = self.listbox_items.get(index).split()[0]
            quantity = int(self.entry_quantity.get())
            price = float(self.entry_price.get())
            
            item = Item(name, quantity, price)
            item.update()
            
            self.load_items()
            
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

