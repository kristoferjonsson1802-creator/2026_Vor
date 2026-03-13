import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.title("Verkefni 16")
root.geometry("800x400")

uppl = tk.LabelFrame(root, text="Upplýsingar", padx=10, pady=10)
uppl.place(x=20, y=20, width=200, height=200)

Label(uppl, text="Fornafn:").grid(row=0, column=0, sticky='e')
Entry(uppl).grid(row=0, column=1, padx=100, pady=2, sticky='we', columnspan=9)

Checkbutton(uppl, text='strákur').grid(row=1, column=1, columnspan=4, sticky='w')
Checkbutton(uppl, text='stelpa').grid(row=1, column=10, columnspan=4, sticky='w')
Checkbutton(uppl, text='hán').grid(row=1, column=20, columnspan=4, sticky='w')