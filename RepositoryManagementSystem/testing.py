import tkinter as tk

class ItemList:
    def __init__(self, parent):
        self.parent = parent
        self.items = ["Item 1", "Item 2", "Item 3"]
        self.selected_index = None
        self.setup_ui()

    def setup_ui(self):
        self.listbox = tk.Listbox(self.parent)
        self.listbox.pack()
        for item in self.items:
            self.listbox.insert(tk.END, item)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

    def on_select(self, event):
        # Get the index of the selected item and store it in self.selected_index
        if self.listbox.curselection():
            self.selected_index = int(self.listbox.curselection()[0])

    def update_selected_item(self, new_value):
        # Update the selected item with the new value and update the listbox
        if self.selected_index is not None:
            self.items[self.selected_index] = new_value
            self.listbox.delete(0, tk.END)
            for item in self.items:
                self.listbox.insert(tk.END, item)

if __name__ == "__main__":
    root = tk.Tk()
    app = ItemList(root)

    # Add a button to update the selected item
    update_button = tk.Button(root, text="Update Selected Item", command=lambda: app.update_selected_item("New Value"))
    update_button.pack()

    root.mainloop()