import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("倉儲管理系統")
        self.master.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.label_name = tk.Label(self.master, text="商品名稱")
        self.label_name.grid(row=0, column=0)

        self.entry_name = tk.Entry(self.master)
        self.entry_name.grid(row=0, column=1)

        self.label_quantity = tk.Label(self.master, text="商品數量")
        self.label_quantity.grid(row=1, column=0)

        self.entry_quantity = tk.Entry(self.master)
        self.entry_quantity.grid(row=1, column=1)

        self.label_price = tk.Label(self.master, text="商品價格")
        self.label_price.grid(row=2, column=0)

        self.entry_price = tk.Entry(self.master)
        self.entry_price.grid(row=2, column=1)

        self.button_add = tk.Button(self.master, text="新增", command=self.add_item)
        self.button_add.grid(row=3, column=0)

        self.button_remove = tk.Button(self.master, text="刪除", command=self.remove_item)
        self.button_remove.grid(row=3, column=1)

        self.button_update = tk.Button(self.master, text="修改", command=self.update_item)
        self.button_update.grid(row=3, column=2)

        self.listbox_items = tk.Listbox(self.master)
        self.listbox_items.grid(row=4, column=0, columnspan=3)

        self.load_items()

    def load_items(self):
        self.listbox_items.delete(0, tk.END)
        items = Item.get_all_items()

        for item in items:
            self.listbox_items.insert(tk.END, str(Item(*item)))

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

if __name__ == "__
