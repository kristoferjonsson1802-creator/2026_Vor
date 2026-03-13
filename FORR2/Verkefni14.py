import tkinter as tk
from tkinter import ttk
from tkinter import *

gluggi = tk.Tk()
gluggi.title("Myndir")
gluggi.geometry("800x600")

val = tk.StringVar()

Myndir = tk.LabelFrame(gluggi, text="Möguleikar", padx=10, pady=10)
Myndir.grid(row=1, column=1, padx=20, pady=20, sticky="n")

tk.Radiobutton(Myndir, text="Mynd 1", variable=val, value="Mynd1").grid(row=0, column=0, sticky="w")
tk.Radiobutton(Myndir, text="Mynd 2", variable=val, value="Mynd2").grid(row=0, column=1, sticky="w")
tk.Radiobutton(Myndir, text="Mynd 3", variable=val, value="Mynd3").grid(row=1, column=0, sticky="w")
tk.Radiobutton(Myndir, text="Mynd 4", variable=val, value="Mynd4").grid(row=1, column=1, sticky="w") 