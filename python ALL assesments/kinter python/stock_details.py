from tkinter import *
from tkinter import messagebox, ttk
import sqlite3

# Initialize database connection
conn = sqlite3.connect('hotel_management.db')
cur = conn.cursor()

class Stock_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Details")
        self.root.geometry("1295x550+230+220")

        # Variables
        self.product_id_var = StringVar()
        self.product_name_var = StringVar()
        self.price_var = StringVar()
        self.stock_quantity_var = StringVar()

        # Title Label
        lbl_title = Label(self.root, text="STOCK DETAILS", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1000, height=50)

        # Frame to hold stock information
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=50, width=1000, height=300)

        # Labels and Entry fields for stock details
        lbl_product_id = Label(main_frame, text="Product ID", font=("times new roman", 12, "bold"))
        lbl_product_id.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        txt_product_id = Entry(main_frame, textvariable=self.product_id_var, font=("times new roman", 12, "bold"))
        txt_product_id.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        lbl_product_name = Label(main_frame, text="Product Name", font=("times new roman", 12, "bold"))
        lbl_product_name.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        txt_product_name = Entry(main_frame, textvariable=self.product_name_var, font=("times new roman", 12, "bold"))
        txt_product_name.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        lbl_price = Label(main_frame, text="Price", font=("times new roman", 12, "bold"))
        lbl_price.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        txt_price = Entry(main_frame, textvariable=self.price_var, font=("times new roman", 12, "bold"))
        txt_price.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        lbl_stock_quantity = Label(main_frame, text="Stock Quantity", font=("times new roman", 12, "bold"))
        lbl_stock_quantity.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        txt_stock_quantity = Entry(main_frame, textvariable=self.stock_quantity_var, font=("times new roman", 12, "bold"))
        txt_stock_quantity.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Buttons
        btn_add = Button(main_frame, text="Add Stock", command=self.add_stock, font=("times new roman", 12, "bold"), bg="green", fg="white")
        btn_add.grid(row=4, column=0, padx=10, pady=5)

        btn_update = Button(main_frame, text="Update Stock", command=self.update_stock, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        btn_update.grid(row=4, column=1, padx=10, pady=5)

        btn_delete = Button(main_frame, text="Delete Stock", command=self.delete_stock, font=("times new roman", 12, "bold"), bg="red", fg="white")
        btn_delete.grid(row=4, column=2, padx=10, pady=5)

        # Frame for Treeview
        stock_display_frame = Frame(self.root, bd=4, relief=RIDGE)
        stock_display_frame.place(x=0, y=350, width=1000, height=250)

        # Treeview for stock details
        self.stock_table = ttk.Treeview(stock_display_frame, columns=("product_id", "product_name", "price", "stock_quantity"))
        self.stock_table.heading("product_id", text="Product ID")
        self.stock_table.heading("product_name", text="Product Name")
        self.stock_table.heading("price", text="Price")
        self.stock_table.heading("stock_quantity", text="Stock Quantity")
        self.stock_table["show"] = "headings"

        self.stock_table.column("product_id", width=100)
        self.stock_table.column("product_name", width=150)
        self.stock_table.column("price", width=100)
        self.stock_table.column("stock_quantity", width=100)
        
        self.stock_table.pack(fill=BOTH, expand=1)
        self.stock_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_stock_details()

    def fetch_stock_details(self):
        conn = sqlite3.connect('hotel_management.db')  
        cur = conn.cursor()
        cur.execute("SELECT product_id, product_name, price, stock_quantity FROM stock")  
        rows = cur.fetchall()

        if len(rows) != 0:
            self.stock_table.delete(*self.stock_table.get_children())
            for row in rows:
                self.stock_table.insert("", END, values=row)
        conn.commit()
        conn.close()

    def add_stock(self):
        if self.product_id_var.get() == "" or self.product_name_var.get() == "" or self.price_var.get() == "" or self.stock_quantity_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = sqlite3.connect('hotel_management.db')
                cur = conn.cursor()
                cur.execute("INSERT INTO stock (product_id, product_name, price, stock_quantity) VALUES (?, ?, ?, ?)", (
                    self.product_id_var.get(),
                    self.product_name_var.get(),
                    self.price_var.get(),
                    self.stock_quantity_var.get()
                ))
                conn.commit()
                conn.close()
                self.fetch_stock_details()
                self.clear()
                messagebox.showinfo("Success", "Stock Added Successfully")
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Failed to add stock: {e}")

    def update_stock(self):
        if self.product_id_var.get() == "":
            messagebox.showerror("Error", "Please select a stock item to update")
        else:
            try:
                conn = sqlite3.connect('hotel_management.db')
                cur = conn.cursor()
                cur.execute("UPDATE stock SET product_name=?, price=?, stock_quantity=? WHERE product_id=?", (
                    self.product_name_var.get(),
                    self.price_var.get(),
                    self.stock_quantity_var.get(),
                    self.product_id_var.get()
                ))
                conn.commit()
                conn.close()
                self.fetch_stock_details()
                self.clear()
                messagebox.showinfo("Success", "Stock Updated Successfully")
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Failed to update stock: {e}")

    def delete_stock(self):
        if self.product_id_var.get() == "":
            messagebox.showerror("Error", "Please select a stock item to delete")
        else:
            try:
                conn = sqlite3.connect('hotel_management.db')
                cur = conn.cursor()
                cur.execute("DELETE FROM stock WHERE product_id=?", (self.product_id_var.get(),))
                conn.commit()
                conn.close()
                self.fetch_stock_details()
                self.clear()
                messagebox.showinfo("Success", "Stock Deleted Successfully")
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Failed to delete stock: {e}")

    def clear(self):
        self.product_id_var.set("")
        self.product_name_var.set("")
        self.price_var.set("")
        self.stock_quantity_var.set("")

    def get_cursor(self, event):
        cursor_row = self.stock_table.focus()
        content = self.stock_table.item(cursor_row)
        row = content['values']
        self.product_id_var.set(row[0])
        self.product_name_var.set(row[1])
        self.price_var.set(row[2])
        self.stock_quantity_var.set(row[3])


cur.execute('''
CREATE TABLE IF NOT EXISTS stock (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price REAL NOT NULL,
    stock_quantity INTEGER NOT NULL
)
''')

conn.commit()
conn.close()

print("Table created successfully!")

if __name__ == "__main__":
    root = Tk()
    obj = Stock_Window(root)
    root.mainloop()
