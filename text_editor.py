import tkinter as tk
from tkinter import filedialog, messagebox


def new_file():
    text.delete(1.0, tk.END)


def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(1.0, file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo("Info", "File Saved Successfully!")


root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("500x500")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

text = tk.Text(root, wrap=tk.WORD, font=("Times New Roman", 12), fg="blue")
text.pack(expand=True, fill=tk.BOTH)

root.mainloop()
