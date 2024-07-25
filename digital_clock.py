import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")


def time():
    string = strftime('Current time is : %I:%M:%S %p')
    string += "\n" + strftime("Today's Date :%d/%m/%Y")
    label.config(text=string)
    label.after(1000, time)


label = tk.Label(root, font=("calibri", 60, "bold"),
                 background="white", foreground="black")

label.pack(anchor="center")

time()

root.mainloop()
