# import tkinter as tk

# def main():
#     # Create the main window
#     root = tk.Tk()
#     root.title("Product Management Application")

#     # Create a label on top that says "Choose your ROLE"
#     role_label = tk.Label(root, text="Choose your ROLE", font=("Arial", 20))
#     role_label.pack(pady=20)

#     # Create frames for product manager and customer
#     product_manager_frame = tk.Frame(root, padx=10, pady=10)
#     customer_frame = tk.Frame(root, padx=10, pady=10)

#     # Create buttons for product manager
#     product_manager_button = tk.Button(product_manager_frame, text="Product Manager", command=lambda: print("Product Manager button clicked"))
#     product_manager_button.pack(side=tk.LEFT, padx=10)

#     # Create buttons for customer
#     customer_button = tk.Button(customer_frame, text="Customer", command=lambda: print("Customer button clicked"))
#     customer_button.pack(side=tk.RIGHT, padx=10)

#     # Pack frames
#     product_manager_frame.pack(pady=10)
#     customer_frame.pack(pady=10)

#     # Make window larger
#     root.geometry("600x400")

#     # Start the main loop
#     root.mainloop()

# if __name__ == "__main__":
#     main()