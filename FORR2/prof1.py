import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.title("prof")
root.geometry("1700x550")

team = tk.StringVar(value="HK")
mode = tk.StringVar(value="kyn")

def update_team(*args):
    filename = f"{team.get()}.gif"
    img = tk.PhotoImage(file=filename)
    team_label.config(image=img)
    team_label.image = img

left = tk.LabelFrame(root, text="Rammi1", padx=10, pady=10)
left.place(x=20, y=20, width=500, height=500)

right = tk.LabelFrame(root, text="Rammi2", padx=10, pady=10)
right.place(x=550, y=150, width=500, height=300)

entry = tk.LabelFrame(left, text="Upplýsingar", padx=10, pady=10)
entry.place(x=20, y=20, width=350, height=100)

Label(entry, text="Fornafn:").grid(row=0, column=0, sticky='e')
Entry(entry).grid(row=0, column=1, padx=100, pady=2, sticky='we', columnspan=9)

Label(entry, text="Eftirnafn:").grid(row=1, column=0, sticky='e')
Entry(entry).grid(row=1, column=1, padx=100, pady=2, sticky='we', columnspan=9)

kyn = tk.LabelFrame(left, text="Kyn", padx=10, pady=10)
kyn.place(x=20, y=150, width=200, height=100)

combo = ttk.Combobox(kyn, state="readonly", width=20)
combo["values"] = ("karl", "kona")
combo.current(0)
combo.pack(anchor="w")

skoli = tk.LabelFrame(left, text="Menntun", padx=10, pady=10)
skoli.place(x=20, y=300, width=350, height=125)

Checkbutton(skoli, text='Grunnskoli').grid(row=1, column=1, columnspan=4, sticky='w')
Checkbutton(skoli, text='Menntaskoli').grid(row=1, column=10, columnspan=4, sticky='w')
Checkbutton(skoli, text='Haskoli').grid(row=1, column=20, columnspan=4, sticky='w')

button1 = Button(right, text='upp', width=20)
button1.pack(side='top', padx = 15, pady = 15)
button2 = Button(right, text='vinstri', width=20)
button2.pack(side='left', padx = 15, pady = 15)
button3 = Button(right, text='hægri', width=20)
button3.pack(side='right', padx = 15, pady = 15)
button4 = Button(right, text='niður', width=20)
button4.pack(side='bottom', padx = 15, pady = 15)

pic = tk.LabelFrame(root, text="Rammi3", padx=10, pady=10)
pic.place(x=1100, y=20, width=550, height=500)

pic2 = tk.LabelFrame(root, text="íþróttafélög", padx=10, pady=10)
pic2.place(x=1125, y=50, width=500, height=450)

Radiobutton(pic2, text='HK', variable=team, value='HK', command=update_team).grid(row=1, column=1, columnspan=4, sticky='w')
Radiobutton(pic2, text='Breiðablik', variable=team, value='breidablik', command=update_team).grid(row=1, column=10, columnspan=4, sticky='w')
Radiobutton(pic2, text='ÍR', variable=team, value='IR', command=update_team).grid(row=1, column=20, columnspan=4, sticky='w')

pic3 = tk.LabelFrame(root, text='', padx=10, pady=10)
pic3.place(x=1125, y=100, width=500, height=400)

team_label = tk.Label(pic3)
team_label.pack(expand=True)

update_team()
root.mainloop()
