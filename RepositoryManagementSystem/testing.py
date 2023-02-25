import datetime
import sqlite3
import tkinter as tk

# 建立數據庫連接
conn = sqlite3.connect('inventory.db')

# 建立商品資料表
conn.execute('''CREATE TABLE IF NOT EXISTS products
             (id TEXT PRIMARY KEY NOT NULL,
             name TEXT NOT NULL,
             quantity INT NOT NULL,
             location TEXT,
             update_time DATE);''')

# 建立新增商品函數
def add_product():
    # 獲取使用者輸入的商品編號、商品名稱、數量和存放位置
    id = product_id_entry.get()
    name = name_entry.get()
    quantity = int(quantity_entry.get())
    location = product_location_entry.get()

    # 獲取最後更新時間
    update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 插入新商品到數據庫
    conn.execute('INSERT INTO products (id, name, quantity, location, update_time) VALUES (?, ?, ?, ?, ?)',
                 (id, name, quantity, location, update_time))

    # 提交數據庫更新並顯示成功訊息
    conn.commit()
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, 'Product added to inventory.\n')

    # 更新商品列表
    show_all_products()

# 建立查詢函數
def search_products():
    # 獲取使用者輸入的查詢條件
    product_id = product_id_entry.get()
    product_name = name_entry.get()
    product_location = product_location_entry.get()

    # 構建查詢語句
    sql = 'SELECT * FROM products WHERE 1=1 '
    if product_id:
        sql += 'AND id = "{}" '.format(product_id)
    if product_name:
        sql += 'AND name = "{}" '.format(product_name)
    if product_location:
        sql += 'AND location = "{}" '.format(product_location)

    # 執行查詢並顯示結果
    cursor = conn.execute(sql)
    result_text.delete('1.0', tk.END)  # 清空原本的查詢結果
    for row in cursor:
        result_text.insert(tk.END, str(row) + '\n')

# 建立進出函數
def update_products():
    # 獲取使用者輸入的進出資訊
    product_id = product_id_entry.get()
    quantity = quantity_entry.get()
    direction = direction_var.get()

    # 根據進出方向更新商品數量
    if direction == 'in':
        conn.execute(
            'UPDATE products SET quantity = quantity + ? WHERE id = ?', (quantity, product_id))
        result_text.insert(tk.END, 'Product added to inventory.\n')
    elif direction == 'out':
        conn.execute(
            'UPDATE products SET quantity = quantity - ? WHERE id = ?', (quantity, product_id))
        result_text.insert(tk.END, 'Product removed from inventory.\n')
    else:
        result_text.insert(tk.END, 'Invalid direction.\n')

    # 更新最後更新時間
    update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn.execute('UPDATE products SET update_time = ? WHERE id = ?', (update_time, product_id))
    conn.commit()
    # 更新商品列表
    show_all_products()

# 建立顯示全部商品函數
def show_all_products():
    cursor = conn.execute('SELECT * FROM products')
    products_list.delete(0, tk.END)  # 清空原本的商品列表
    for row in cursor:
        products_list.insert(tk.END, str(row))

# 建立GUI界面
root = tk.Tk()
root.title('Inventory Management System')

# 建立商品編號輸入框
product_id_label = tk.Label(root, text='Product ID')
product_id_entry = tk.Entry(root)

# 建立商品名稱輸入框
name_label = tk.Label(root, text='Product Name')
name_entry = tk.Entry(root)

# 建立商品存放位置輸入框
product_location_label = tk.Label(root, text='Product Location')
product_location_entry = tk.Entry(root)

# 建立進出方向選擇框
direction_label = tk.Label(root, text='Direction')
direction_var = tk.StringVar()
in_radio = tk.Radiobutton(root, text='In', variable=direction_var, value='in')
out_radio = tk.Radiobutton(root, text='Out', variable=direction_var, value='out')

# 建立商品數量輸入框
quantity_label = tk.Label(root, text='Quantity')
quantity_entry = tk.Entry(root)

# 建立進出按鈕
update_button = tk.Button(root, text='Update', command=update_products)
add_button = tk.Button(root, text='Add', command=add_product)
search_button = tk.Button(root, text='Search', command=search_products)

# 建立查詢結果顯示框
result_text = tk.Text(root)

# 建立商品瀏覽列表
products_label = tk.Label(root, text='All Products')
products_list = tk.Listbox(root)

# 排版元件
product_id_label.grid(row=0, column=0, padx=10, pady=10)
product_id_entry.grid(row=0, column=1, padx=10, pady=10)
name_label.grid(row=1, column=0, padx=10, pady=10)
name_entry.grid(row=1, column=1, padx=10, pady=10)
product_location_label.grid(row=2, column=0, padx=10, pady=10)
product_location_entry.grid(row=2, column=1, padx=10, pady=10)
direction_label.grid(row=3, column=0, padx=10, pady=10)
in_radio.grid(row=3, column=1, padx=10, pady=10)
out_radio.grid(row=3, column=2, padx=10, pady=10)
quantity_label.grid(row=4, column=0, padx=10, pady=10)
quantity_entry.grid(row=4, column=1, padx=10, pady=10)
update_button.grid(row=5, column=0, padx=10, pady=10)
add_button.grid(row=5, column=1, padx=10, pady=10)
search_button.grid(row=5, column=2, padx=10, pady=10)
result_text.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
products_label.grid(row=0, column=3, padx=10, pady=10)
products_list.grid(row=1, column=3, rowspan=7, padx=10, pady=10)

# 啟動GUI界面
root.mainloop()

# 關閉數據庫連接
conn.close()
