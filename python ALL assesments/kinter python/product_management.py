from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image, ImageTk
from customer import CustomerWindow  
from stock_details import Stock_Window 

class ProductManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Management System")
        self.root.geometry("1550x800+0+0")

        #==================1st Image (Banner)====================
        img1 = Image.open(r"C:/Users/sanke/OneDrive/Desktop/Tkinter2 ME Assesment -python youtube/images/logoo2.png")
        img1 = img1.resize((1550, 140), Image.LANCZOS)  # Resize first image
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image=self.photoimg1)
        lblimg1.place(x=0, y=0, width=1550, height=140)

        #--------------------Title----------------------------------
        lbl_title = Label(self.root, text="PRODUCT MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        #---------------------Menu--------------------------------
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        #------------------------Button Frame---------------------
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=130)  # Adjusted height

        # Button managing stocks (linked to CustomerWindow)
        manage_stock_btn = Button(btn_frame, text="MANAGE STOCK", command=self.open_customer_window, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        manage_stock_btn.grid(row=0, column=0, pady=1)

        # Button viewing all stocks
        view_stock_btn = Button(btn_frame, text="VIEW ALL STOCK", command=self.open_stock_window, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        view_stock_btn.grid(row=1, column=0, pady=1)

        # Button  logging out
        logout_btn = Button(btn_frame, text="LOGOUT", command=self.logout, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=2, column=0, pady=1)

        #-------Right Side Image -----------------------------------
        try:
            img3 = Image.open(r"C:/Users/sanke/OneDrive/Desktop/Tkinter2 ME Assesment -python youtube/images/product4.png")
            img3 = img3.resize((1310, 590), Image.LANCZOS)  
            self.photoimg3 = ImageTk.PhotoImage(img3)

            lblimg3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
            lblimg3.place(x=225, y=0, width=1310, height=590)
        except Exception as e:
            print(f"Error loading image: {e}")

    # Function to open the Customer Management window (CustomerWindow)
    def open_customer_window(self):
        """Open the Customer Management System."""
        self.new_window = Toplevel(self.root)
        self.app = CustomerWindow(self.new_window)

    # Function to open the Stock Management window
    def open_stock_window(self):
        """Open the Stock Management System."""
        self.new_window = Toplevel(self.root)
        self.app = Stock_Window(self.new_window)  

    def logout(self):
        """Function to handle logout action."""
        response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if response:
            self.root.destroy()  


if __name__ == "__main__":
    root = Tk()
    app = ProductManagementSystem(root)
    root.mainloop()
