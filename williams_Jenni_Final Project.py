#import tkinter module
import tkinter as tk

#create window
window = tk.Tk()

#provide size to window
window.geometry("300x300")

#add text label
tk.Label(text="Hello from Sports and more!").pack()

window.mainloop()