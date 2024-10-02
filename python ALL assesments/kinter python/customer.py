import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class CustomerWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Management System")
        self.root.geometry("1295x550+230+220")

        # Connect to the database and create the table if not exists
        self.connect_db()

        # Variables
        self.var_customer_id = StringVar()
        self.var_name = StringVar()
        self.var_company = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()

        # ----------------title-----------------------
        lbl_title = Label(self.root, text="CUSTOMER MANAGEMENT", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # -------------------LABEL FRAME-----------------
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # --------------labels and entries---------------
        # Customer ID
        lbl_cust_id = Label(labelframeleft, text="Customer ID", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_id.grid(row=0, column=0, sticky=W)
        entry_cust_id = ttk.Entry(labelframeleft, textvariable=self.var_customer_id, width=29, font=("arial", 13, "bold"))
        entry_cust_id.grid(row=0, column=1)

        # Customer Name
        lbl_name = Label(labelframeleft, text="Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_name.grid(row=1, column=0, sticky=W)
        txt_name = ttk.Entry(labelframeleft, textvariable=self.var_name, width=29, font=("arial", 13, "bold"))
        txt_name.grid(row=1, column=1)

        # Company Name
        lbl_company = Label(labelframeleft, text="Company", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_company.grid(row=2, column=0, sticky=W)
        txt_company = ttk.Entry(labelframeleft, textvariable=self.var_company, width=29, font=("arial", 13, "bold"))
        txt_company.grid(row=2, column=1)

        # Contact Number
        lbl_contact = Label(labelframeleft, text="Contact", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_contact.grid(row=3, column=0, sticky=W)
        txt_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, width=29, font=("arial", 13, "bold"))
        txt_contact.grid(row=3, column=1)

        # Email
        lbl_email = Label(labelframeleft, text="Email", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_email.grid(row=4, column=0, sticky=W)
        txt_email = ttk.Entry(labelframeleft, textvariable=self.var_email, width=29, font=("arial", 13, "bold"))
        txt_email.grid(row=4, column=1)

        # Address
        lbl_address = Label(labelframeleft, text="Address", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_address.grid(row=5, column=0, sticky=W)
        txt_address = ttk.Entry(labelframeleft, textvariable=self.var_address, width=29, font=("arial", 13, "bold"))
        txt_address.grid(row=5, column=1)

        # -------Buttons-------------------
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=350, width=412, height=40)

        btn_add = Button(btn_frame, text="Add", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, command=self.add_data)
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, text="Update", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, command=self.update_data)
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Delete", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, command=self.delete_data)
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, command=self.reset_data)
        btn_reset.grid(row=0, column=3, padx=1)

        # Database table and search area
        self.setup_table()

    def connect_db(self):
        """Connect to SQLite3 database and create table if not exists"""
        self.conn = sqlite3.connect("product_management.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY,
                name TEXT,
                company TEXT,
                contact TEXT,
                email TEXT,
                address TEXT
            )
        """)
        self.conn.commit()

    def add_data(self):
        """Add customer data to the database"""
        if self.var_customer_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            self.cursor.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?)", (
                self.var_customer_id.get(),
                self.var_name.get(),
                self.var_company.get(),
                self.var_contact.get(),
                self.var_email.get(),
                self.var_address.get()
            ))
            self.conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Customer details added successfully")

    def fetch_data(self):
        """Fetch all data from the database to the Treeview table"""
        self.cursor.execute("SELECT * FROM customers")
        rows = self.cursor.fetchall()
        if len(rows) != 0:
            self.customer_table.delete(*self.customer_table.get_children())
            for row in rows:
                self.customer_table.insert('', END, values=row)
            self.conn.commit()

    def update_data(self):
        """Update customer data"""
        if self.var_customer_id.get() == "":
            messagebox.showerror("Error", "Customer ID is required")
            return

        self.cursor.execute("""
            UPDATE customers SET
                name = ?,
                company = ?,
                contact = ?,
                email = ?,
                address = ?
            WHERE customer_id = ?
        """, (
            self.var_name.get(),
            self.var_company.get(),
            self.var_contact.get(),
            self.var_email.get(),
            self.var_address.get(),
            self.var_customer_id.get()
        ))
        self.conn.commit()
        self.fetch_data()
        messagebox.showinfo("Success", "Customer details updated successfully")

    def delete_data(self):
        """Delete customer data"""
        if self.var_customer_id.get() == "":
            messagebox.showerror("Error", "Customer ID is required")
            return

        self.cursor.execute("DELETE FROM customers WHERE customer_id = ?", (self.var_customer_id.get(),))
        self.conn.commit()
        self.fetch_data()
        messagebox.showinfo("Success", "Customer details deleted successfully")

    def reset_data(self):
        """Reset all fields"""
        self.var_customer_id.set("")
        self.var_name.set("")
        self.var_company.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_address.set("")

    def search_data(self):
        """Search data based on user input"""
        search_by = self.combo_search.get()
        search_term = self.search_txt.get()
        if search_term == "":
            messagebox.showerror("Error", "Please enter a search term")
            return
        column = "contact" if search_by == "Contact" else "customer_id"
        query = f"SELECT * FROM customers WHERE {column} LIKE ?"
        self.cursor.execute(query, ('%' + search_term + '%',))
        rows = self.cursor.fetchall()
        if len(rows) != 0:
            self.customer_table.delete(*self.customer_table.get_children())
            for row in rows:
                self.customer_table.insert('', END, values=row)
        else:
            self.customer_table.delete(*self.customer_table.get_children())
            messagebox.showinfo("Info", "No records found")

    def setup_table(self):
        """Set up Treeview table for displaying customer data"""
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details & Search System", font=("times new roman", 12, "bold"), padx=2)
        table_frame.place(x=435, y=50, width=860, height=490)

        lbl_search = Label(table_frame, text="Search by:", font=("arial", 12, "bold"), bg="red", fg="white")
        lbl_search.grid(row=0, column=0, sticky=W, padx=2)

        self.combo_search = ttk.Combobox(table_frame, font=("arial", 12, "bold"), width=24, state="readonly")
        self.combo_search["value"] = ("Contact", "Customer ID")
        self.combo_search.current(0)
        self.combo_search.grid(row=0, column=1, padx=2)

        self.search_txt = ttk.Entry(table_frame, width=24, font=("arial", 13, "bold"))
        self.search_txt.grid(row=0, column=2, padx=2)

        btn_search = Button(table_frame, text="Search", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, command=self.search_data)
        btn_search.grid(row=0, column=3, padx=1)

        btn_show_all = Button(table_frame, text="Show All", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, command=self.fetch_data)
        btn_show_all.grid(row=0, column=4, padx=1)

        table_details = Frame(table_frame, bd=2, relief=RIDGE)
        table_details.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(table_details, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_details, orient=VERTICAL)

        self.customer_table = ttk.Treeview(table_details, columns=("customer_id", "name", "company", "contact", "email", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.customer_table.xview)
        scroll_y.config(command=self.customer_table.yview)

        self.customer_table.heading("customer_id", text="Customer ID")
        self.customer_table.heading("name", text="Name")
        self.customer_table.heading("company", text="Company")
        self.customer_table.heading("contact", text="Contact")
        self.customer_table.heading("email", text="Email")
        self.customer_table.heading("address", text="Address")

        self.customer_table["show"] = "headings"
        self.customer_table.column("customer_id", width=100)
        self.customer_table.column("name", width=150)
        self.customer_table.column("company", width=150)
        self.customer_table.column("contact", width=100)
        self.customer_table.column("email", width=150)
        self.customer_table.column("address", width=200)

        self.customer_table.pack(fill=BOTH, expand=1)
        self.customer_table.bind("<ButtonRelease-1>", self.on_select)
        self.fetch_data()

    def on_select(self, event):
        """Populate the fields with the selected row data"""
        selected_row = self.customer_table.selection()
        if selected_row:
            row = self.customer_table.item(selected_row)['values']
            self.var_customer_id.set(row[0])
            self.var_name.set(row[1])
            self.var_company.set(row[2])
            self.var_contact.set(row[3])
            self.var_email.set(row[4])
            self.var_address.set(row[5])

if __name__ == "__main__":
    root = Tk()
    app = CustomerWindow(root)
    root.mainloop()


















