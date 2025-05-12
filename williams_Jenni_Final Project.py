"""
Author: Jenni Williams
Date: May 5th, 2025
Assignment: Final Project
Description: This program allows users to select clothing items (shirts, pants, socks) with various options and submit their order.
 It includes a GUI with images and handles user input.
"""
# Import necessary libraries
import os
import tkinter as tk
from tkinter import messagebox

# Clothing options, including types, colors, and sizes
# These lists can be expanded or modified as needed
clothing_types = ["Shirt", "Pants", "Socks"]
colors = ["Red", "Blue", "Green", "Black", "White", "Yellow"]
sizes = ["XS", "S", "M", "L", "XL", "XXL"]

def open_details_window():
    name = name_entry.get().strip()
    if not name:
        messagebox.showerror("Input Error", "Please enter your name.")
        return

    details_window = tk.Toplevel()
    details_window.title("Your Clothing Selection")
    details_window.geometry("500x700")
    details_window.configure(bg="grey")

    # Image 1 (sports.png)
    try:
        img1 = tk.PhotoImage(file="sports.png")  # MUST be PNG or GIF
        img_label1 = tk.Label(details_window, image=img1, bg="grey")
        img_label1.image = img1  # Required to keep image
        img_label1.pack()
        tk.Label(details_window, text="Image: Sports Icon", bg="black", fg="red").pack()
    except:
        tk.Label(details_window, text="[Image: Sports Icon - Not Found]", bg="black", fg="red").pack()

    # Image 2 (gear.png)
    try:
        img2 = tk.PhotoImage(file="gear.png")
        img_label2 = tk.Label(details_window, image=img2, bg="black")
        img_label2.image = img2
        img_label2.pack()
        tk.Label(details_window, text="Image: Gear Icon", bg="black", fg="red").pack()
    except:
        tk.Label(details_window, text="[Image: Gear Icon - Not Found]", bg="black", fg="red").pack()

    tk.Label(details_window, text=f"Hello, {name}!", font=("Arial", 14), bg="black", fg="red").pack(pady=10)

    order_summary = [
    f"{shirt_quantity.get()} {shirt_color.get()} Shirt(s), Size {shirt_size.get()}",
    f"{pants_quantity.get()} {pants_color.get()} Pants(s), Size {pants_size.get()}",
    f"{socks_quantity.get()} {socks_color.get()} Socks(s)"
]

    for item in order_summary:
        tk.Label(details_window, text=item, bg="black", fg="red").pack()

    def submit_order():
        full_summary = f"Order for {name}:\n\n" + "\n".join(order_summary)
        messagebox.showinfo("Order Submitted", f"Thank you! Your order has been submitted:\n\n{full_summary}")
        details_window.destroy()

    tk.Button(details_window, text="Submit Order", command=submit_order, bg="green", fg="white", font=("Arial", 12)).pack(pady=20)

def clear_input():
    name_entry.delete(0, tk.END)
    result_label.config(text="")
    shirt_color.set(colors[0])
    shirt_size.set(sizes[0])
    shirt_quantity.set(1)

    pants_type.set(clothing_types[1])
    pants_color.set(colors[0])
    pants_size.set(sizes[0])
    pants_quantity.set(1)

    socks_type.set(clothing_types[2])
    socks_color.set(colors[0])
    socks_quantity.set(1)

def exit_app():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

# Main window setup
window = tk.Tk()
window.title("Sports and More!")
window.geometry("450x700")
window.configure(bg="grey")

tk.Label(window, text="Welcome to Sports and More!", font=("Arial", 14), bg="black", fg="red").pack(pady=10)
tk.Label(window, text="Enter your name:", bg="black", fg="red").pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Shirt options, including size color and quantity
tk.Label(window, text="Choose your shirt:", bg="black", fg="red").pack()
shirt_color = tk.StringVar(value=colors[0])
shirt_size = tk.StringVar(value=sizes[0])
shirt_quantity = tk.IntVar(value=1)

tk.Label(window, text="Item: Shirt", bg="grey", fg="black").pack()
tk.OptionMenu(window, shirt_color, *colors).pack()
tk.Label(window, text="Shirt Size:", bg="black", fg="red").pack()
tk.OptionMenu(window, shirt_size, *sizes).pack()
tk.Label(window, text="Quantity:", bg="black", fg="red").pack()
tk.Spinbox(window, from_=1, to=10, textvariable=shirt_quantity).pack()

# Pants options, including size color and quantity
tk.Label(window, text="Choose your pants:", bg="black", fg="red").pack()
pants_type = tk.StringVar(value="Pants")
pants_color = tk.StringVar(value=colors[0])
pants_size = tk.StringVar(value=sizes[0])
pants_quantity = tk.IntVar(value=1)

tk.Label(window, text="Item: Pants", bg="grey", fg="black").pack()
tk.OptionMenu(window, pants_color, *colors).pack()
tk.Label(window, text="Pants Size:", bg="black", fg="red").pack()
tk.OptionMenu(window, pants_size, *sizes).pack()
tk.Label(window, text="Quantity:", bg="black", fg="red").pack()
tk.Spinbox(window, from_=1, to=10, textvariable=pants_quantity).pack()

# Socks options, including color and quantity
tk.Label(window, text="Choose your socks:", bg="black", fg="red").pack()
socks_type = tk.StringVar(value="Socks")
socks_color = tk.StringVar(value=colors[0])
socks_quantity = tk.IntVar(value=1)

tk.Label(window, text="Item: Socks", bg="grey", fg="black").pack()
tk.OptionMenu(window, socks_color, *colors).pack()
tk.Label(window, text="Quantity:", bg="black", fg="red").pack()
tk.Spinbox(window, from_=1, to=10, textvariable=socks_quantity).pack()

# Buttons, including submit, clear, and exit
tk.Button(window, text="Submit", command=open_details_window, bg="black", fg="red").pack(pady=10)
tk.Button(window, text="Clear", command=clear_input, bg="black", fg="red").pack()
tk.Button(window, text="Exit", command=exit_app, bg="black", fg="red").pack(pady=5)

result_label = tk.Label(window, text="", fg="green", bg="black")
result_label.pack()

window.mainloop()
