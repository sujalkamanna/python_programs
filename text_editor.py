#text editor in python

from tkinter import tk
from tkinter import filedialog,messagebox

def new_file():
    text.delete(1.0,tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension= = ".txt" , filetypes= [("text Files ,*.txt")]) 
    if file_path:
        with open(file_path , "r") as file:
            text.delete(1.0,tk.END)
            text.insert(1.0,file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension= = ".txt" , filetypes= [("text Files ,*.txt")])