import tkinter as tk
from tkinter import ttk

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

accounts = []

def create_account():
    name = name_entry.get()
    balance = float(balance_entry.get())
    acc = BankAccount(name, balance)
    accounts.append(acc)
    update_dropdowns()

def deposit():
    name = combo.get()
    amount = float(amount_entry.get())
    for acc in accounts:
        if acc.name == name:
            acc.deposit(amount)

def withdraw():
    name = combo.get()
    amount = float(amount_entry.get())
    for acc in accounts:
        if acc.name == name:
            acc.withdraw(amount)

def show_balance():
    name = combo2.get()
    for acc in accounts:
        if acc.name == name:
            result_label.config(text=f"Staða: {acc.balance}")

def update_dropdowns():
    names = [acc.name for acc in accounts]
    combo['values'] = names
    combo2['values'] = names

root = tk.Tk()
root.title("Banki")
root.geometry('400x300')

notebook = ttk.Notebook(root)
notebook.pack()

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Stofna")

tk.Label(tab1, text="Nafn").pack()
name_entry = tk.Entry(tab1)
name_entry.pack()

tk.Label(tab1, text="Innistæða").pack()
balance_entry = tk.Entry(tab1)
balance_entry.pack()

tk.Button(tab1, text="Stofna", command=create_account).pack()

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Færa")

combo = ttk.Combobox(tab2)
combo.pack()

tk.Label(tab2, text="taka út/leggja inn").pack()
amount_entry = tk.Entry(tab2)
amount_entry.pack()

tk.Button(tab2, text="Leggja inn", command=deposit).pack()
tk.Button(tab2, text="Taka út", command=withdraw).pack()

tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Staða")

combo2 = ttk.Combobox(tab3)
combo2.pack()

tk.Button(tab3, text="Skoða", command=show_balance).pack()

result_label = tk.Label(tab3, text="")
result_label.pack()

root.mainloop()
