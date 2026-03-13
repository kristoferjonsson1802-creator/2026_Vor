import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.title("Spurning")
root.geometry("1000x600")

val = tk.StringVar()

tk.Label(root, text="Nafn:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
tk.Entry(root).grid(row=0, column=1, columnspan=3, sticky="w", padx=5, pady=5)

moguleikar = tk.LabelFrame(root, text="Möguleikar", padx=10, pady=10)
moguleikar.grid(row=1, column=1, padx=20, pady=20, sticky="n")

tk.Radiobutton(moguleikar, text="Ameríka", variable=val, value="Amerika").grid(row=0, column=0, sticky="w")
tk.Radiobutton(moguleikar, text="Bandaríkin", variable=val, value="Bandarikin").grid(row=0, column=1, sticky="w")
tk.Radiobutton(moguleikar, text="Kanada", variable=val, value="Kanada").grid(row=1, column=0, sticky="w")
tk.Radiobutton(moguleikar, text="Mexíkó", variable=val, value="Mexico").grid(row=1, column=1, sticky="w")

mynd = tk.PhotoImage(file="usa.gif")
label_mynd = tk.Label(root, image=mynd, text="Fáni", compound="top")
label_mynd.grid(row=1, column=0, padx=20, pady=20)

root.mainloop()
