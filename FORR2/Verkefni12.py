import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Fánar")
root.geometry("800x400")

country = tk.StringVar(value="usa")
mode = tk.StringVar(value="Lit")

def update_flag(*args):
    suffix = "_sh" if mode.get() == "Svart/Hvítt" else ""
    filename = f"{country.get()}{suffix}.gif"
    img = tk.PhotoImage(file=filename)
    flag_label.config(image=img)
    flag_label.image = img

left = tk.LabelFrame(root, text="Veldu land", padx=10, pady=10)
left.place(x=20, y=20, width=200, height=200)

right = tk.LabelFrame(root, text="Fáni", padx=10, pady=10)
right.place(x=250, y=20, width=500, height=280)

tk.Radiobutton(left, text="USA", variable=country, value="usa", command=update_flag).grid(row=0, column=0, sticky="w")
tk.Radiobutton(left, text="Þýskaland", variable=country, value="germ", command=update_flag).grid(row=0, column=1, sticky="w")

tk.Radiobutton(left, text="Danmörk", variable=country, value="danm", command=update_flag).grid(row=1, column=0, sticky="w")
tk.Radiobutton(left, text="England", variable=country, value="england", command=update_flag).grid(row=1, column=1, sticky="w")

mode_frame = tk.LabelFrame(root, text="Litur eða svart/hvítt", padx=10, pady=10)
mode_frame.place(x=20, y=230, width=150, height=90)

combo = ttk.Combobox(mode_frame, textvariable=mode, state="readonly", width=15)
combo["values"] = ("Lit", "Svart/Hvítt")
combo.current(0)
combo.pack(anchor="w")
combo.bind("<<ComboboxSelected>>", update_flag)

flag_label = tk.Label(right)
flag_label.pack(expand=True)

update_flag()
root.mainloop()
